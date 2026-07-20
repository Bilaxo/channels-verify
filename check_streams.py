#!/usr/bin/env python3
"""
check_streams.py - test every stream in list.m3u and remove the dead ones.

A channel is not removed the first time it fails. Each failure adds a strike,
any success clears it, and a channel is only removed after 2 consecutive
failing runs. This matters because GitHub's runners have US datacenter IPs:
some streams are geo-blocked or reject datacenter ranges and will fail there
while working perfectly from home. Removed channels are written to
removed.m3u rather than deleted outright.

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

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/125.0 Safari/537.36"),
    "Accept": "*/*",
}


def check(url, timeout):
    """Fetch enough of the stream to tell whether it is alive."""
    try:
        with requests.get(url, headers=HEADERS, timeout=timeout, stream=True,
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

    keep, drop = ["#EXTM3U"], ["#EXTM3U"]
    new_strikes, reasons, dropped = {}, Counter(), []
    failing = 0

    for (entry, url, name), (alive, why) in zip(entries, results):
        n = 0 if alive else strikes.get(url, 0) + 1
        if not alive:
            failing += 1
            reasons[why] += 1
        if n:
            new_strikes[url] = n
        if n >= args.max_strikes:
            drop.extend(entry + [url])
            dropped.append((name, why))
        else:
            keep.extend(entry + [url])

    kept = len(entries) - len(dropped)
    loss = 100 * len(dropped) / len(entries)
    print(f"done in {time.time() - t0:.0f}s: {kept} kept, "
          f"{failing} failed this run, {len(dropped)} removed")

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
        f"- Removed this run: **{len(dropped)}**", "",
        "Channels are removed after failing 2 checks in a row, and are kept in "
        "`removed.m3u` rather than deleted.", "",
        "## Why streams failed", "", "| Reason | Channels |", "| --- | ---: |",
    ]
    out += [f"| {r} | {n} |" for r, n in reasons.most_common()]
    if dropped:
        out += ["", "## Removed this run", "", "| Channel | Last error |",
                "| --- | --- |"]
        out += [f"| {n} | {w} |" for n, w in sorted(dropped)]
    Path(args.report).write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
