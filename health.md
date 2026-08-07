# Stream health

_Last checked 2026-08-07 05:52 UTC_

- Channels in playlist: **1333**
- Failed this run: **27**
- Healed this run: **1**
- Removed this run: **0**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 19 |
| connectionerror | 3 |
| read timeout | 3 |
| http 502 | 2 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| All Time Movies (576p) | iptv-org | http://103.175.73.12:8080/live/54/54_0.m3u8 |
