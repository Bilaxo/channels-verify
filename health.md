# Stream health

_Last checked 2026-07-22 00:26 UTC_

- Channels in playlist: **1351**
- Failed this run: **55**
- Healed this run: **28**
- Removed this run: **14**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 40 |
| http 403 (blocked) | 4 |
| connect timeout | 3 |
| http 503 | 2 |
| http 500 | 2 |
| http 523 | 2 |
| http 400 | 1 |
| connectionerror | 1 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| &flix (1080p) | iptv-org | https://gpuserver3.tier1streams.com/FLIX/index.m3u8 |
| Abadan | iptv-org | https://ncdn.telewebion.ir/abadan/live/playlist.m3u8 |
| Aflak | iptv-org | https://ncdn.telewebion.ir/aflak/live/playlist.m3u8 |
| Africanews English | iptv-org | https://c3c275b999764df8a2dd55ffe2996818.mediatailor.eu-west-1.amazonaws.com/v1/master/0547f18649bd788bec7b67b746e47670f558b6b2/production-LiveChannel-6576/bitok/eyJzdGlkIjoiOTU0NDAyODQtOTU0My00Yzc2LThmZjQtNDRhY2YwYmQxYTYwIiwibWt0IjoicGwiLCJjaCI6NjYwNiwicHRmIjo1fQ==/26036/africanews-en.m3u8 |
| Aftab | iptv-org | https://ncdn.telewebion.ir/aftab/live/playlist.m3u8 |
| Al Araby TV (1080p) | iptv-org | https://live.kwikmotion.com/alaraby1live/alaraby_abr/playlist.m3u8 |
| Al Araby TV 2 (1080p) | iptv-org | https://live.kwikmotion.com/alaraby2live/alaraby2.smil/playlist.m3u8 |
| Azerbaijan Gharbi | iptv-org | https://ncdn.telewebion.ir/azarbayjangharbi/live/playlist.m3u8 |
| Baran | iptv-org | https://ncdn.telewebion.ir/baran/live/playlist.m3u8 |
| Colors Infinity (1080p) | iptv-org | http://103.175.73.12:8080/live/29/29_0.m3u8 |
| Fars | iptv-org | https://ncdn.telewebion.ir/fars/live/playlist.m3u8 |
| IRINN2 | iptv-org | https://ncdn.telewebion.ir/irinn2/live/playlist.m3u8 |
| Isfahan | iptv-org | https://ncdn.telewebion.ir/esfahan/live/playlist.m3u8 |
| Kerman | iptv-org | https://ncdn.telewebion.ir/kerman/live/playlist.m3u8 |
| KhozestanTV | iptv-org | https://ncdn.telewebion.ir/khoozestan/live/playlist.m3u8 |
| Kordestan | iptv-org | https://ncdn.telewebion.ir/kordestan/live/playlist.m3u8 |
| Namayesh | iptv-org | https://ncdn.telewebion.ir/namayesh/live/playlist.m3u8 |
| Ofogh | iptv-org | https://ncdn.telewebion.ir/ofogh/live/playlist.m3u8 |
| Omid | iptv-org | https://ncdn.telewebion.ir/omid/live/playlist.m3u8 |
| Qazvin | iptv-org | https://ncdn.telewebion.ir/qazvin/live/playlist.m3u8 |
| Quran | iptv-org | https://ncdn.telewebion.ir/quran/live/playlist.m3u8 |
| RFD-TV | iptv-org | http://40.160.24.55/RFD-TV/index.m3u8 |
| Sahand | iptv-org | https://ncdn.telewebion.ir/sahand/live/playlist.m3u8 |
| Sepehr | iptv-org | https://ncdn.telewebion.ir/sepehr/live/playlist.m3u8 |
| Star Gold Romance (576p) | iptv-org | http://103.253.18.58:8000/play/a017 |
| Tamasha | iptv-org | https://ncdn.telewebion.ir/hdtest/live/playlist.m3u8 |
| Yazd | iptv-org | https://ncdn.telewebion.ir/taban/live/playlist.m3u8 |
| Zee TV (1080p) | iptv-org | http://38.96.178.205/ZEE_TV/index.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| &xplor HD (1080p) | http 404 |
| Al Jazeera Documentary (1080p) [Geo-blocked] | http 403 (blocked) |
| AlKawthar | http 404 |
| Anjan (1080p) [Not 24/7] | http 403 (blocked) |
| Ayeneh TV | http 403 (blocked) |
| CPAC (720p) | http 503 |
| Colors (1080p) | http 404 |
| Colors Rishtey Asia (576p) | http 404 |
| Colors Super (720p) | http 404 |
| Dhamaal (576p) [Not 24/7] | http 404 |
| Izzah TV (480p) | http 404 |
| Mastiii (1080p) | http 400 |
| Mazandaran TV | http 404 |
| Star Utsav (576p) | http 523 |
