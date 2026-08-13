# Stream health

_Last checked 2026-08-13 05:50 UTC_

- Channels in playlist: **1316**
- Failed this run: **56**
- Healed this run: **3**
- Removed this run: **17**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 25 |
| connect timeout | 17 |
| http 403 (blocked) | 9 |
| connectionerror | 2 |
| http 502 | 2 |
| read timeout | 1 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| ArabTV (720p) | iptv-org | https://streamtv2.elitecomunicacion.cloud:3628/live/arabitv2025live.m3u8 |
| Bharat Express (1080p) | iptv-org | https://stream1.livebox.co.in/VCAREhls/live.m3u8 |
| Panorama TV (720p) | iptv-org | https://159.69.221.56/panorama/livestream/playlist.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| ATN News (1080p) | http 404 |
| Andijon MTRK (576i) | read timeout |
| Buxoro MTRK (720p) | http 404 |
| DM TV Malang | http 404 |
| Desh TV (1080p) | http 404 |
| Dijlah TV (1080p) | http 404 |
| Farg'ona MTRK | http 404 |
| Independent TV (1080p) | http 404 |
| Jamuna TV (1080p) | http 404 |
| Ketchup TV (720p) | http 502 |
| MoviePlex (576p) | http 404 |
| Munsif Tv (720p) | connectionerror |
| Navoiy MTRK (576i) | http 404 |
| Qaraqalpaqstan (720p) | http 404 |
| Sakti TV (720p) | http 404 |
| YAAAS! (720p) [Geo-blocked] | http 502 |
| Yemen TV (480p) | connect timeout |
