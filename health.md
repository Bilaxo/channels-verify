# Stream health

_Last checked 2026-10-19 09:57 UTC_

- Channels in playlist: **1237**
- Failed this run: **14**
- Healed this run: **0**
- Removed this run: **5**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 8 |
| connectionerror | 3 |
| read timeout | 2 |
| connect timeout | 1 |

## Removed this run

| Channel | Last error |
| --- | --- |
| AmarUjala (1080p) | http 404 |
| E! Keeping Up (1080p) | connectionerror |
| Payam Javan TV (720p) [Not 24/7] | http 404 |
| TV Mu (720p) [Not 24/7] | http 404 |
| Televizija M (1080p) | connect timeout |
