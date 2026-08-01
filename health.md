# Stream health

_Last checked 2026-08-01 06:42 UTC_

- Channels in playlist: **1333**
- Failed this run: **18**
- Healed this run: **3**
- Removed this run: **9**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 13 |
| connectionerror | 5 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| MTRSPT1 (1080p) | iptv-org | https://amg02873-kravemedia-mtrspt1-samsungau-2anp4.amagi.tv/playlist/amg02873-kravemedia-mtrspt1-samsungau/playlist.m3u8 |
| MY5 (1080p) | iptv-org | https://stream8.cinerama.uz/1217/tracks-v1a1/playlist.m3u8 |
| Vive Kanal D Drama (1080p) | iptv-org | https://jmp2.uk/plu-639751f81a36b400072b8f5a.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| Al-Sahat TV (720p) | http 404 |
| DiscoverFilm (720p) | connectionerror |
| DİM TV (720p) [Geo-blocked] | http 404 |
| Juice TV (1080p) [Not 24/7] | http 404 |
| Kilisuci TV | http 404 |
| Metaleitor TV | http 404 |
| NTV IC Kakanj (720p) | connectionerror |
| Nepal 1 (396p) | http 404 |
| Shamshad TV [Not 24/7] | http 404 |
