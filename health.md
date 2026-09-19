# Stream health

_Last checked 2026-09-19 08:50 UTC_

- Channels in playlist: **1259**
- Failed this run: **28**
- Healed this run: **0**
- Removed this run: **5**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 22 |
| http 403 (blocked) | 3 |
| connect timeout | 3 |

## Removed this run

| Channel | Last error |
| --- | --- |
| ARTN TV (1080p) [Not 24/7] | http 403 (blocked) |
| CBC (576p) | http 404 |
| CBC Drama (576p) | http 404 |
| CBC Sofra (576p) | http 404 |
| ZB Cinema (720p) | http 404 |
