# Stream health

_Last checked 2026-11-01 11:18 UTC_

- Channels in playlist: **1224**
- Failed this run: **17**
- Healed this run: **2**
- Removed this run: **4**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 9 |
| connect timeout | 3 |
| ssl error | 3 |
| http 500 | 1 |
| read timeout | 1 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| Chardikla Time TV (1080p) | iptv-org | https://streams.tangotv.in/CHARDIKALATIMETV/ORIGIN/index.m3u8 |
| News 12 New York (1080p) | iptv-org | https://jmp2.uk/plu-5fff49cfb5cd4f0007c2b0dc.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| Alau TV (576p) | connect timeout |
| For You TV | http 404 |
| GBN Global Buddhist Network (1080p) | http 404 |
| Green TV (1080p) | http 500 |
