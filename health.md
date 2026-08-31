# Stream health

_Last checked 2026-08-31 10:54 UTC_

- Channels in playlist: **1290**
- Failed this run: **37**
- Healed this run: **10**
- Removed this run: **4**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 14 |
| connectionerror | 13 |
| http 403 (blocked) | 7 |
| connect timeout | 3 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| B4U Movies (1080p) [Geo-blocked] | iptv-org | https://s3.itcnbd.live/channel/129d01070adb9ee3.m3u8 |
| Bilyonaryo News Channel (1080p) | iptv-org | https://amg19223-amg19223c11-amgplt0352.playout.now3.amagi.tv/playlist/amg19223-amg19223c11-amgplt0352/playlist.m3u8 |
| NEW K-POP (1080p) | iptv-org | https://ads.its-newid.net/api/manifest.m3u8?ads.service_id=USAJ3000013FJ&channel_id=newid_338&tp=samsung_tvplus |
| Vevo 2K (1080p) | iptv-org | https://d3150hggbcolbo.cloudfront.net/Vevo_2K.m3u8 |
| Vevo 70s (1080p) | iptv-org | https://d341pfs1smb2ef.cloudfront.net/Vevo_70s.m3u8 |
| Vevo 80s (1080p) | iptv-org | https://d3svsvgc81yfe1.cloudfront.net/Vevo_80s.m3u8 |
| Vevo 90s (1080p) | iptv-org | https://d29u7uq3k6xqk0.cloudfront.net/Vevo_90s.m3u8 |
| Vevo Country (1080p) | iptv-org | https://pb-xrdbj9zdgm6ez.akamaized.net/Vevo_Country.m3u8 |
| Vevo Pop (1080p) | iptv-org | https://amg00056-amg00056c9-rakuten-fr-3243.playouts.now.amagi.tv/playlist/amg00056-vevotvfast-vevopopfr-rakutenfr/playlist.m3u8 |
| Vevo Retro Rock (1080p) | iptv-org | https://d2hdqrshyzxswl.cloudfront.net/Vevo_Retro_Rock.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| ANC (480p) | connect timeout |
| Alwafa Tarim TV (Am Media) (720p) | http 404 |
| CHCO-TV (720p) [Geo-blocked] | connectionerror |
| Legislative Assembly of Ontario | connectionerror |
