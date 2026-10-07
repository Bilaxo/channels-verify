# Stream health

_Last checked 2026-10-07 11:07 UTC_

- Channels in playlist: **1248**
- Failed this run: **18**
- Healed this run: **2**
- Removed this run: **6**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 11 |
| http 403 (blocked) | 4 |
| read timeout | 2 |
| connectionerror | 1 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| 9XM (1080p) | iptv-org | https://wiselp.wiseplayout.com/9XM/master.m3u8 |
| TVNET (1080p) | iptv-org | https://player.tvnet.lv/stream/amlst:61659/playlist.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| EET TV (1080p) [Not 24/7] | http 404 |
| EET TV (1080p) [Not 24/7] | http 404 |
| GZT (1080p) | http 404 |
| Spacetoon Arabic (576p) | http 403 (blocked) |
| Tele 1 (1080p) | http 404 |
| Zjarr TV (360p) | http 404 |
