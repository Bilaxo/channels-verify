# Stream health

_Last checked 2026-08-19 04:54 UTC_

- Channels in playlist: **1300**
- Failed this run: **38**
- Healed this run: **0**
- Removed this run: **16**

When a channel fails twice in a row we first try to heal it with a fresh URL from upstream sources (iptv-org, Free-TV). Only channels with no working replacement are moved to `removed.m3u`.

## Why streams failed

| Reason | Channels |
| --- | ---: |
| http 404 | 18 |
| connect timeout | 14 |
| http 502 | 3 |
| read timeout | 2 |
| http 403 (blocked) | 1 |

## Removed this run

| Channel | Last error |
| --- | --- |
| &flix (1080p) | http 404 |
| Badakhshon (576p) | connect timeout |
| Dushanbe HD (1080p) | connect timeout |
| Futbol (1080p) | connect timeout |
| Ilm va Tabiat (1080p) | connect timeout |
| Jahonnamo (1080p) | connect timeout |
| Khatlon (576p) | connect timeout |
| TMT (1080p) | connect timeout |
| TV Bahoriston (1080p) | connect timeout |
| TV Kulob (576p) | connect timeout |
| TV Safina (1080p) | connect timeout |
| TV Sayohi (1080p) | connect timeout |
| TV Sinamo (1080p) | connect timeout |
| TV Sugd (1080p) | connect timeout |
| Tajikistan (1080p) | connect timeout |
| ZB Music (720p) | http 404 |
