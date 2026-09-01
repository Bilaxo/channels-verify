# Stream health

_Last checked 2026-09-01 09:26 UTC_

- Channels in playlist: **1277**
- Failed this run: **21**
- Healed this run: **4**
- Removed this run: **13**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 9 |
| http 403 (blocked) | 7 |
| connectionerror | 2 |
| connect timeout | 1 |
| http 503 | 1 |
| read timeout | 1 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| Al-Iman TV (720p) | iptv-org | https://svs.itworkscdn.net/alimanlive/imantv.smil/playlist.m3u8 |
| Korean Central Television (1080p) | iptv-org | https://stream.intchoson.com/kctv/index.m3u8 |
| Schwab Network (1080p) | iptv-org | https://content.uplynk.com/channel/f9aafa1f132e40af9b9e7238bc18d128.m3u8 |
| Taaza TV (720p) | iptv-org | https://tvsen3.aynaott.com/yRMLky2j/index.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| Alkass Four (1080p) | http 403 (blocked) |
| Alkass One (1080p) | http 403 (blocked) |
| Alkass SHOOF (1080p) | http 403 (blocked) |
| Alkass SHOOF 2 (1080p) | http 403 (blocked) |
| Alkass Six (1080p) | http 403 (blocked) |
| Alkass Three (1080p) | http 403 (blocked) |
| Alkass Two (1080p) | http 403 (blocked) |
| Aragon TV Internacional (720p) [Not 24/7] | http 404 |
| BPX TV Radio | http 404 |
| FX TV 2 | connect timeout |
| InfoWars Network (1080p) | connectionerror |
| NTD TV English UK (1080p) | read timeout |
| TATV (720p) [Not 24/7] | http 404 |
