#!/usr/bin/env python3
"""
sources.py - find replacement stream URLs for dead channels.

When a channel in list.m3u dies, we try to heal it instead of deleting it by
looking the channel up, by name, in two upstream sources:

  Tier 2 - the ORIGINAL SOURCE. The iptv-org database/API
    (https://iptv-org.github.io/api/). This is the canonical, structured
    collection that the aggregator repos copy from. It often lists several
    stream URLs for one channel (different feeds/qualities), and carries the
    referrer / user-agent headers a stream needs, so it gives us the richest
    set of fallback candidates.

  Tier 1 - the AGGREGATOR REPOS. Free-TV/IPTV's single playlist
    (https://github.com/free-tv/iptv). A hand-curated, quality-first list.

Both tiers are merged into one name -> [candidate, ...] index. A candidate is
only used after it passes the same liveness check the rest of the pipeline
uses, so a swapped-in URL is always one that actually responded.

The two other repos that were considered are deliberately not used:
  - shovo127/IPTV-By-Shovo is itself a downstream aggregator of iptv-org, so
    its links duplicate tier 2 with far less coverage.
  - akiralereal/iptv is a self-hosted Docker app that generates China-only
    channels at runtime; it exposes no static playlist to pull from.
"""

import json
import re
import sys
from pathlib import Path

import requests

# --- source locations ------------------------------------------------------

IPTV_ORG_CHANNELS = "https://iptv-org.github.io/api/channels.json"
IPTV_ORG_STREAMS = "https://iptv-org.github.io/api/streams.json"
FREE_TV_PLAYLIST = "https://raw.githubusercontent.com/Free-TV/IPTV/master/playlist.m3u8"

# resolution ranking so we prefer the best feed when a channel has several
_QUALITY_RANK = {
    "2160p": 6, "1440p": 5, "1080p": 4, "1080i": 4, "720p": 3,
    "576p": 2, "576i": 2, "480p": 1, "480i": 1, "360p": 0,
}

# tokens that describe format/quality/status, not identity - dropped so that
# "Tolo TV (720p)" and "Tolo TV HD" collapse onto the same channel as "Tolo TV"
_NOISE = re.compile(
    r"\b("
    r"\d{3,4}[pi]|4k|uhd|fhd|hd|sd|hq|"
    r"h265|h264|hevc|"
    r"not\s*24\s*/?\s*7|geo[-\s]?blocked|backup|feed|stream"
    r")\b",
    re.IGNORECASE,
)


def normalize(name):
    """Reduce a channel name to a comparison key.

    Lowercases, strips anything in ()/[]/{}, drops quality/format noise words,
    and removes every non-alphanumeric character so punctuation and spacing
    stop mattering. Returns "" for names too short to match on safely.
    """
    if not name:
        return ""
    name = re.sub(r"[\(\[\{].*?[\)\]\}]", " ", name)   # (720p), [Not 24/7], ...
    name = _NOISE.sub(" ", name)
    name = re.sub(r"[^0-9a-zA-Z]+", "", name).lower()
    return name if len(name) >= 3 else ""


def _cached_get(url, cache_dir, timeout):
    """GET a URL, caching the body under cache_dir for the life of the run."""
    if cache_dir:
        cache_dir = Path(cache_dir)
        cache_dir.mkdir(parents=True, exist_ok=True)
        key = re.sub(r"[^0-9a-zA-Z]+", "_", url)[-120:]
        cached = cache_dir / key
        if cached.exists():
            return cached.read_text(encoding="utf-8")
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    body = r.text
    if cache_dir:
        cached.write_text(body, encoding="utf-8")
    return body


def _add(index, name, candidate):
    key = normalize(name)
    if not key:
        return
    index.setdefault(key, []).append(candidate)


def _load_iptv_org(index, cache_dir, timeout):
    """Tier 2: the iptv-org API - the original, structured source."""
    channels = json.loads(_cached_get(IPTV_ORG_CHANNELS, cache_dir, timeout))
    streams = json.loads(_cached_get(IPTV_ORG_STREAMS, cache_dir, timeout))
    id_to_name = {c["id"]: c.get("name", "") for c in channels}

    count = 0
    for s in streams:
        url = (s.get("url") or "").strip()
        if not url:
            continue
        candidate = {
            "url": url,
            "source": "iptv-org",
            "referrer": s.get("referrer") or None,
            "user_agent": s.get("user_agent") or None,
            "quality": s.get("quality") or None,
            "rank": _QUALITY_RANK.get((s.get("quality") or "").lower(), -1),
        }
        # index under both the channel's canonical name and the stream title,
        # so we still match when list.m3u uses a slightly different wording
        for name in {id_to_name.get(s.get("channel"), ""), s.get("title", "")}:
            _add(index, name, candidate)
        count += 1
    return count


def _iter_m3u(text):
    """Yield (name, url, opt_lines) for each entry in an m3u playlist."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if not lines[i].startswith("#EXTINF"):
            i += 1
            continue
        name = lines[i].split(",", 1)[-1].strip()
        opts, j = [], i + 1
        while j < len(lines) and lines[j].startswith("#"):
            if lines[j].startswith("#EXTVLCOPT"):
                opts.append(lines[j])
            j += 1
        if j >= len(lines):
            break
        yield name, lines[j].strip(), opts
        i = j + 1


def _load_free_tv(index, cache_dir, timeout):
    """Tier 1: the Free-TV aggregator playlist."""
    text = _cached_get(FREE_TV_PLAYLIST, cache_dir, timeout)
    count = 0
    for name, url, opts in _iter_m3u(text):
        if not url:
            continue
        referrer = user_agent = None
        for o in opts:
            low = o.lower()
            if "http-referrer" in low:
                referrer = o.split("=", 1)[-1].strip()
            elif "http-user-agent" in low:
                user_agent = o.split("=", 1)[-1].strip()
        _add(index, name, {
            "url": url, "source": "free-tv",
            "referrer": referrer, "user_agent": user_agent,
            "quality": None, "rank": -1,
        })
        count += 1
    return count


def build_index(cache_dir=None, timeout=30.0, log=print):
    """Build {normalized_name: [candidate, ...]} from both source tiers.

    Candidates within a name are ordered best-first: iptv-org (original
    source) before free-tv, and higher resolution before lower. Duplicate
    URLs are removed. Never raises - a source that fails to download is
    logged and skipped so a single outage can't break healing entirely.
    """
    index = {}
    for label, loader in (("iptv-org", _load_iptv_org),
                          ("free-tv", _load_free_tv)):
        try:
            n = loader(index, cache_dir, timeout)
            log(f"  source {label}: {n} streams indexed")
        except Exception as e:                       # noqa: BLE001
            log(f"  source {label}: unavailable ({type(e).__name__}) - skipped",
                file=sys.stderr)

    # source priority: iptv-org first, then higher quality first
    src_rank = {"iptv-org": 1, "free-tv": 0}
    for key, cands in index.items():
        seen, unique = set(), []
        for c in sorted(cands, key=lambda c: (src_rank.get(c["source"], 0),
                                              c["rank"]), reverse=True):
            if c["url"] in seen:
                continue
            seen.add(c["url"])
            unique.append(c)
        index[key] = unique
    return index


def candidates_for(index, name):
    """Return the ordered candidate list for a channel name (possibly [])."""
    return index.get(normalize(name), [])


def opt_lines(candidate):
    """VLC option lines a swapped-in URL needs, or [] if none."""
    out = []
    if candidate.get("user_agent"):
        out.append(f'#EXTVLCOPT:http-user-agent={candidate["user_agent"]}')
    if candidate.get("referrer"):
        out.append(f'#EXTVLCOPT:http-referrer={candidate["referrer"]}')
    return out
