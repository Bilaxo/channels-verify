# Stream health

_Last checked 2026-09-07 09:24 UTC_

- Channels in playlist: **1276**
- Failed this run: **47**
- Healed this run: **0**
- Removed this run: **1**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 37 |
| connect timeout | 5 |
| http 403 (blocked) | 2 |
| http 502 | 2 |
| read timeout | 1 |

## Removed this run

| Channel | Last error |
| --- | --- |
| Al Iraqia Sport (720p) | http 404 |
