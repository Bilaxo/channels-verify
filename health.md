# Stream health

_Last checked 2026-08-25 04:56 UTC_

- Channels in playlist: **1294**
- Failed this run: **37**
- Healed this run: **4**
- Removed this run: **6**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 13 |
| connectionerror | 11 |
| connect timeout | 8 |
| http 403 (blocked) | 1 |
| http 401 (blocked) | 1 |
| read timeout | 1 |
| http 502 | 1 |
| http 500 | 1 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| CGTN Arabic (1080p) [Not 24/7] | iptv-org | https://news.cgtn.com/resource/live/arabic/cgtn-a.m3u8 |
| CGTN Français (1080p) [Not 24/7] | iptv-org | https://amg01314-cgtn-amg01314c2-rakuten-us-1319.playouts.now.amagi.tv/cgtn-fr-rakuten/playlist.m3u8 |
| SYFY (1080p) | iptv-org | http://23.237.104.106:8080/USA_SYFY/index.m3u8 |
| Salam TV (1080p) | iptv-org | https://live.salamtelevisi.com/hls/0/stream.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| All Time Movies (576p) | connect timeout |
| Big Magic (576p) | connect timeout |
| Colors Infinity (1080p) | connect timeout |
| On4 TV (1080p) | http 404 |
| RFD-TV | http 404 |
| Star Gold Romance (576p) | http 403 (blocked) |
