# Stream health

_Last checked 2026-10-01 10:59 UTC_

- Channels in playlist: **1254**
- Failed this run: **17**
- Healed this run: **3**
- Removed this run: **1**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 10 |
| connectionerror | 2 |
| http 503 | 2 |
| connect timeout | 1 |
| http 502 | 1 |
| http 403 (blocked) | 1 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| Balapan (1080p) | iptv-org | https://balapantv-stream.qazcdn.com/balapantv/balapantv/playlist.m3u8 |
| News 24 (720p) | iptv-org | https://skynewsau-live-premium.akamaized.net/hls/live/2105299/skynews/live.m3u8 |
| Tarab (1080p) | iptv-org | https://shd-amg-fast.edgenextcdn.net/tx002/playlist.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| Win TV (720p) | http 404 |
