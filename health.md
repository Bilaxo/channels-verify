# Stream health

_Last checked 2026-10-13 11:51 UTC_

- Channels in playlist: **1242**
- Failed this run: **29**
- Healed this run: **2**
- Removed this run: **6**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 20 |
| read timeout | 5 |
| connectionerror | 2 |
| connect timeout | 1 |
| http 403 (blocked) | 1 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| News of the World (720p) | iptv-org | https://live.nowtelly.com/now_spanish/live/playlist.m3u8 |
| TVP World (1080p) | iptv-org | https://dash2.antik.sk/live/test_tvp_world/playlist.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| Azan TV | http 404 |
| Filmax (576p) | http 403 (blocked) |
| GEM Pixel | http 404 |
| ICC Plus (1080p) | http 404 |
| Palestine Edu (1080p) | http 404 |
| The Film Detective (720p) | connectionerror |
