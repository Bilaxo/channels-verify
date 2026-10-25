# Stream health

_Last checked 2026-10-25 09:11 UTC_

- Channels in playlist: **1237**
- Failed this run: **17**
- Healed this run: **0**
- Removed this run: **0**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 403 (blocked) | 5 |
| http 404 | 5 |
| read timeout | 3 |
| connectionerror | 2 |
| http 410 | 1 |
| connect timeout | 1 |
