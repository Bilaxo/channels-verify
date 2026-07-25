# Stream health

_Last checked 2026-07-25 06:31 UTC_

- Channels in playlist: **1346**
- Failed this run: **26**
- Healed this run: **0**
- Removed this run: **6**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 23 |
| connect timeout | 1 |
| read timeout | 1 |
| http 502 | 1 |

## Removed this run

| Channel | Last error |
| --- | --- |
| ARB | http 404 |
| ARB 24 | http 404 |
| ARB Gunes | http 404 |
| Baku TV (720p) | http 404 |
| Space TV | http 404 |
| TMB TV | http 404 |
