# Stream health

_Last checked 2026-07-31 07:16 UTC_

- Channels in playlist: **1342**
- Failed this run: **25**
- Healed this run: **1**
- Removed this run: **4**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 15 |
| connectionerror | 5 |
| connect timeout | 4 |
| http 401 (blocked) | 1 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| Big Magic (576p) | iptv-org | http://103.175.73.12:8080/live/13/13_0.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| Guneydogu TV (720p) | http 404 |
| Islam Channel Urdu (576p) | http 404 |
| Planeta Channel | http 404 |
| TVSN Beauty (1080p) | http 404 |
