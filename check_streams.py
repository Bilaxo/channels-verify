#!/usr/bin/env python3
"""
check_streams.py - test every stream in list.m3u, heal or remove the dead ones.

A channel is not removed the first time it fails. Each failure adds a strike,
any success clears it, and a channel is only removed after 2 consecutive
failing runs. This matters because GitHub's runners have US datacenter IPs:
some streams are geo-blocked or reject datacenter ranges and will fail there
while working perfectly from home.

Before a channel is removed we try to HEAL it: sources.py looks the channel up
by name in the upstream sources (the iptv-org API and the Free-TV playlist) and
returns a fresh URL. The candidate is liveness-checked like everything else,
and if it responds we swap it into list.m3u in place and clear the strike, so
the channel stays. Only channels with no working replacement are moved to
removed.m3u (rather than deleted outright). Pass --no-replace to skip healing.

    python3 check_streams.py list.m3u
"""

import argparse
import json
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests
import urllib3

import sources

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/125.0 Safari/537.36"),
    "Accept": "*/*",
}


def check(url, timeout, referrer=None, user_agent=None):
    """Fetch enough of the stream to tell whether it is alive.

    referrer/user_agent override the defaults for candidate streams that
    only respond when the right headers are sent (iptv-org records these).
    """
    headers = dict(HEADERS)
    if user_agent:
        headers["User-Agent"] = user_agent
    if referrer:
        headers["Referer"] = referrer
    try:
        with requests.get(url, headers=headers, timeout=timeout, stream=True,
                          allow_redirects=True, verify=False) as r:
            if r.status_code in (401, 403):
                return False, f"http {r.status_code} (blocked)"
            if r.status_code >= 400:
                return False, f"http {r.status_code}"
            chunk = next(r.iter_content(4096), b"") or b""
            ctype = r.headers.get("Content-Type", "").lower()
            if b"#EXTM3U" in chunk[:512]:
                return True, "hls"
            if b"<MPD" in chunk[:512]:
                return True, "dash"
            if chunk[:1] == b"\x47":                       # MPEG-TS sync byte
                return True, "mpeg-ts"
            if any(t in ctype for t in ("video", "audio", "mpegurl",
                                        "octet-stream", "dash+xml")):
                return True, "media"
            if chunk:
                return True, "data"
            return False, "empty response"
    except requests.exceptions.ConnectTimeout:
        return False, "connect timeout"
    except requests.exceptions.ReadTimeout:
        return False, "read timeout"
    except requests.exceptions.SSLError:
        return False, "ssl error"
    except requests.exceptions.RequestException as e:
        return False, type(e).__name__.lower()
    except Exception as e:                       # never let one stream abort
        return False, f"error: {type(e).__name__}"


def parse(path):
    """Yield (lines_of_entry, url, channel_name)."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        if not lines[i].startswith("#EXTINF"):
            i += 1
            continue
        entry = [lines[i]]
        j = i + 1
        while j < len(lines) and lines[j].startswith("#"):
            entry.append(lines[j])
            j += 1
        if j >= len(lines):
            break
        url = lines[j].strip()
        i = j + 1
        name = entry[0].split(",", 1)[-1]
        yield entry, url, name


def find_replacement(name, dead_url, index, timeout, max_tries=6):
    """Look up a working replacement URL for a dead channel.

    Tries the channel's candidates (best-first: original source, then higher
    quality) and returns the first one that passes the liveness check. The
    dead URL itself is skipped. Returns a candidate dict on success, else None.
    """
    tried = 0
    for cand in sources.candidates_for(index, name):
        if cand["url"] == dead_url:
            continue
        if tried >= max_tries:
            break
        tried += 1
        alive, _ = check(cand["url"], timeout,
                         referrer=cand.get("referrer"),
                         user_agent=cand.get("user_agent"))
        if alive:
            return cand
    return None


def rebuild_entry(entry, candidate):
    """Return entry lines with the URL swapped and the right VLC opts set.

    Keeps the #EXTINF line (and any non-EXTVLCOPT metadata), drops stale
    header options that belonged to the old URL, and appends the ones the
    replacement stream needs.
    """
    kept = [ln for ln in entry if not ln.startswith("#EXTVLCOPT")]
    return kept + sources.opt_lines(candidate) + [candidate["url"]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("playlist", nargs="?", default="list.m3u")
    ap.add_argument("--removed", default="removed.m3u")
    ap.add_argument("--strikes", default="strikes.json")
    ap.add_argument("--report", default="health.md")
    ap.add_argument("--max-strikes", type=int, default=2)
    ap.add_argument("--timeout", type=float, default=12.0)
    ap.add_argument("--workers", type=int, default=40)
    ap.add_argument("--max-loss", type=float, default=40.0,
                    help="abort if more than this %% would be removed at once")
    ap.add_argument("--no-replace", action="store_true",
                    help="do not try to heal dead channels from upstream sources")
    ap.add_argument("--sources-cache", default=".sources_cache",
                    help="scratch dir for downloaded source playlists")
    args = ap.parse_args()

    entries = list(parse(args.playlist))
    if not entries:
        sys.exit("no channels found in the playlist - stopping")
    print(f"checking {len(entries)} streams "
          f"({args.workers} at a time, {args.timeout}s timeout)")

    strikes = {}
    sp = Path(args.strikes)
    if sp.exists():
        try:
            strikes = json.loads(sp.read_text())
        except json.JSONDecodeError:
            print("strike file unreadable, starting fresh", file=sys.stderr)

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(lambda e: check(e[1], args.timeout), entries))

    # first pass: tally strikes and note which channels would be removed
    records, reasons, failing = [], Counter(), 0
    for (entry, url, name), (alive, why) in zip(entries, results):
        n = 0 if alive else strikes.get(url, 0) + 1
        if not alive:
            failing += 1
            reasons[why] += 1
        records.append({"entry": entry, "url": url, "name": name,
                        "why": why, "n": n, "cand": None})

    would_drop = [r for r in records if r["n"] >= args.max_strikes]

    # heal, don't just remove: before dropping a channel, try to find a live
    # replacement URL for it in the upstream sources
    if would_drop and not args.no_replace:
        print(f"looking for replacements for {len(would_drop)} dead "
              f"channel(s) in upstream sources...")
        index = sources.build_index(cache_dir=args.sources_cache,
                                    timeout=max(args.timeout, 30.0))
        if index:
            def heal(r):
                r["cand"] = find_replacement(r["name"], r["url"], index,
                                             args.timeout)
                return r
            with ThreadPoolExecutor(max_workers=args.workers) as pool:
                list(pool.map(heal, would_drop))
        healed = sum(1 for r in would_drop if r["cand"])
        print(f"  healed {healed} of {len(would_drop)} channel(s)")

    # second pass: assemble the outputs
    keep, drop = ["#EXTM3U"], ["#EXTM3U"]
    new_strikes, dropped, replaced = {}, [], []
    for r in records:
        entry, url, name, n, cand = (r["entry"], r["url"], r["name"],
                                     r["n"], r["cand"])
        if cand:                                   # healed: keep, clear strike
            keep.extend(rebuild_entry(entry, cand))
            replaced.append((name, url, cand["url"], cand["source"]))
            continue
        if n:
            new_strikes[url] = n
        if n >= args.max_strikes:
            drop.extend(entry + [url])
            dropped.append((name, r["why"]))
        else:
            keep.extend(entry + [url])

    kept = len(entries) - len(dropped)
    loss = 100 * len(dropped) / len(entries)
    print(f"done in {time.time() - t0:.0f}s: {kept} kept, "
          f"{failing} failed this run, {len(replaced)} healed, "
          f"{len(dropped)} removed")

    if loss > args.max_loss:
        sys.exit(f"\nERROR: this run would remove {loss:.0f}% of the playlist "
                 f"({len(dropped)} channels).\nThat points to a network problem, "
                 f"not a mass outage. Nothing was written.")

    Path(args.playlist).write_text("\n".join(keep) + "\n", encoding="utf-8")
    Path(args.removed).write_text("\n".join(drop) + "\n", encoding="utf-8")
    sp.write_text(json.dumps(new_strikes, indent=0, sort_keys=True),
                  encoding="utf-8")

    out = [
        "# Stream health", "",
        f"_Last checked {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}_", "",
        f"- Channels in playlist: **{kept}**",
        f"- Failed this run: **{failing}**",
        f"- Healed this run: **{len(replaced)}**",
        f"- Removed this run: **{len(dropped)}**", "",
        "When a channel fails twice in a row we first try to heal it with a "
        "fresh URL from upstream sources (iptv-org, Free-TV). Only channels "
        "with no working replacement are moved to `removed.m3u`.", "",
        "## Why streams failed", "", "| Reason | Channels |", "| --- | ---: |",
    ]
    out += [f"| {r} | {n} |" for r, n in reasons.most_common()]
    if replaced:
        out += ["", "## Healed this run", "",
                "| Channel | New source | New URL |", "| --- | --- | --- |"]
        out += [f"| {n} | {src} | {u} |"
                for n, _old, u, src in sorted(replaced)]
    if dropped:
        out += ["", "## Removed this run", "", "| Channel | Last error |",
                "| --- | --- |"]
        out += [f"| {n} | {w} |" for n, w in sorted(dropped)]
    Path(args.report).write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
