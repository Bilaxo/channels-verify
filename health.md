# Stream health

_Last checked 2026-09-25 09:38 UTC_

- Channels in playlist: **1255**
- Failed this run: **16**
- Healed this run: **2**
- Removed this run: **4**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 10 |
| connect timeout | 2 |
| http 503 | 1 |
| connectionerror | 1 |
| read timeout | 1 |
| http 403 (blocked) | 1 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| Viasat Explore | iptv-org | https://shift03.isp.bg/ViasatExplorer_HD/index.m3u8 |
| YourTime TV | iptv-org | https://live.yourtime.tv/hls/stream.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| Astha TV (1080p) [Not 24/7] | http 404 |
| NCM Educational & Kids Channel | http 403 (blocked) |
| TVKU (720p) | http 404 |
| Tunes 6 (720p) | http 404 |
