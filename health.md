# Stream health

_Last checked 2026-10-31 10:25 UTC_

- Channels in playlist: **1228**
- Failed this run: **24**
- Healed this run: **1**
- Removed this run: **9**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 10 |
| http 403 (blocked) | 6 |
| read timeout | 3 |
| connect timeout | 2 |
| connectionerror | 2 |
| http 410 | 1 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| Az TV (1080p) | iptv-org | http://109.205.166.68/server124/aztv/index3.m3u8?e=1676581573&st=AzGSZjk1DpXY1SLc1m4OvA |

## Removed this run

| Channel | Last error |
| --- | --- |
| DHA (720p) [Not 24/7] | read timeout |
| Eagle One News (576p) | http 404 |
| Kanal 35 (720p) | http 403 (blocked) |
| Kanal Hayat (1080p) | connectionerror |
| Medeniyyet TV (1080p) | http 403 (blocked) |
| Naxcivan TV (720p) | http 403 (blocked) |
| TVNET (1080p) | http 403 (blocked) |
| Terra Mater WILD English (1080p) | connectionerror |
| Xezer TV (720p) | http 410 |
