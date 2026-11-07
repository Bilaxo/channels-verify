# Stream health

_Last checked 2026-11-07 11:06 UTC_

- Channels in playlist: **1221**
- Failed this run: **23**
- Healed this run: **1**
- Removed this run: **3**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 403 (blocked) | 8 |
| http 404 | 6 |
| connectionerror | 4 |
| read timeout | 4 |
| connect timeout | 1 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| ATV (1080p) | iptv-org | http://stream.mcquack.net/36/index.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| Aryan TV National (576p) | http 404 |
| EmanTv (1080p) | http 404 |
| Panorama TV (720p) | connect timeout |
