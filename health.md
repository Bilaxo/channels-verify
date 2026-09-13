# Stream health

_Last checked 2026-09-13 09:35 UTC_

- Channels in playlist: **1264**
- Failed this run: **45**
- Healed this run: **19**
- Removed this run: **12**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 36 |
| connect timeout | 3 |
| connectionerror | 3 |
| http 403 (blocked) | 2 |
| http 503 | 1 |

## Healed this run

| Channel | New source | New URL |
| --- | --- | --- |
| B4U Movies (1080p) [Geo-blocked] | iptv-org | https://streams.tangotv.in/B4UMOVIES/ORIGIN/index.m3u8 |
| B4U Music (576p) | iptv-org | https://streams.tangotv.in/B4UMUSIC/ORIGIN/index.m3u8 |
| DD Urdu (720p) | iptv-org | https://d3qs3d2rkhfqrt.cloudfront.net/out/v1/9b91e9007e754db39a8b32c6bfc5b24a/index.m3u8 |
| Hi Dost! (720p) | iptv-org | https://mumt03.tangotv.in/Dsly5z3HHIDOST/index.m3u8 |
| INews (720p) | iptv-org | https://live.i-news.tv/hls/stream.m3u8 |
| MK Six (720p) [Not 24/7] | iptv-org | https://mumt06.tangotv.in/qYyB8fXVMKSIX/index.m3u8 |
| Manoranjan TV (720p) | iptv-org | https://streams.tangotv.in/MANORANJANTV/ORIGIN/index.m3u8 |
| Music India (720p) [Not 24/7] | iptv-org | https://streams.tangotv.in/MUSICINDIA/ORIGIN/index.m3u8 |
| News Daily 24 (576p) | iptv-org | https://mumt01.tangotv.in/O5aw8Zn3NEWSDAILY24/index.m3u8 |
| PTC Chakde (720p) | iptv-org | https://mumt06.tangotv.in/qYyB8fXVPTCCHAKDE/index.m3u8 |
| PTC News (576p) | iptv-org | https://streams.tangotv.in/PTCNEWS/ORIGIN/index.m3u8 |
| PTC Simran | iptv-org | https://streams.tangotv.in/PTCSIMRAN/ORIGIN/index.m3u8 |
| R Plus Gold (720p) | iptv-org | https://vglivessai.akamaized.net/sg/v1/master/611d79b11b77e2f571934fd80ca1413453772ac7/cf883da3-f9f5-4c70-b0ef-b3ac2e2ad1e3/index.m3u8 |
| Shemaroo TV (720p) | iptv-org | https://airtelapp.shemaroo.com/shemarootv/smil:shemarootvadp.smil/playlist.m3u8 |
| Studio One + (720p) | iptv-org | https://mumt04.tangotv.in/m18aqlK4STUDIOONEPLUS/index.m3u8 |
| Swadesh News (720p) | iptv-org | https://mumt03.tangotv.in/Dsly5z3HSWADESHNEWS/index.m3u8 |
| TV 7 Albania | free-tv | https://rpn3.bozztv.com/albaniatv/Med7-TV7Tirana/index.m3u8 |
| Tehzeeb TV (720p) | iptv-org | https://mumt05.tangotv.in/87NeALx2TEHZEEBTV/index.m3u8 |
| Win TV (720p) | iptv-org | https://mumt06.tangotv.in/qYyB8fXVWINTV/index.m3u8 |

## Removed this run

| Channel | Last error |
| --- | --- |
| 4TV News (576p) | http 404 |
| Afaq TV | connect timeout |
| BIG TV (720p) | http 404 |
| Gulistan News (720p) | connect timeout |
| Jinvani Channel (720p) | http 404 |
| Magna Vision (1080p) | http 404 |
| Maha Movie (576p) | http 404 |
| Maha Punjabi | http 404 |
| Manoranjan Grand (720p) | http 404 |
| News J (720p) [Not 24/7] | http 404 |
| Samachar Plus | http 404 |
| Tekyemadahi | http 404 |
