# IPTV playlist

Auto-tested IPTV playlist. Every 6 days a GitHub Action tests every stream. A
channel that goes dead is first **healed** with a fresh URL pulled from upstream
sources; only channels with no working replacement are removed from `list.m3u`.

**Playlist URL for your player:**

```
https://raw.githubusercontent.com/USERNAME/REPO/main/list.m3u
```

Replace `USERNAME` and `REPO`. Use exactly this form — if you copy the link
GitHub gives you after clicking the **Raw** button, it may contain a long
commit hash, and that version stays frozen forever no matter how many times
the file is updated.

## Files

| File | Purpose |
| --- | --- |
| `list.m3u` | The playlist. This is the file that gets healed and cleaned. |
| `check_streams.py` | Tests the streams, then heals or removes the dead ones |
| `sources.py` | Finds replacement URLs for dead channels in the upstream sources |
| `requirements.txt` | Python dependency |
| `.github/workflows/check-playlist.yml` | Runs the check every 6 days |
| `removed.m3u` | Channels that had no replacement and were removed (created on first run) |
| `strikes.json` | Failure counts between runs (created on first run) |
| `health.md` | Report from the last run (created on first run) |

## Setup

1. Put the files in the repo, with the workflow at
   `.github/workflows/check-playlist.yml`.
2. Go to **Settings → Actions → General → Workflow permissions** and select
   **Read and write permissions**. Without this the Action cannot save the
   updated playlist.
3. Go to the **Actions** tab, pick **Check playlist**, and press **Run
   workflow** to test it now.

## How channels get healed, then removed

A channel is not removed the first time it fails — it gets a strike, and any
success clears it. Only after **failing twice in a row** does it become a
removal candidate.

The reason for that delay: GitHub's servers are in a US datacenter. Some
streams are geo-blocked or reject datacenter connections, so they fail there
while working fine on your home connection. Removing on the first failure
would strip out channels that work for you.

**Before removing, the channel is healed.** `sources.py` looks the channel up
by name in two upstream sources and tries their URLs. The first replacement
that actually responds is swapped into `list.m3u` in place (carrying any
`user-agent` / `referrer` the stream needs), and the strike is cleared, so the
channel stays. Only channels with **no working replacement anywhere** are moved
to `removed.m3u`.

The two sources give each channel a primary link and a fallback, so if one dies
we can pull the other:

1. **The original source** — the [iptv-org](https://github.com/iptv-org/iptv)
   database/API. This is the canonical, structured collection that most other
   playlists copy from. It often lists several stream URLs per channel
   (different feeds and qualities), which become fallback candidates.
2. **An aggregator repo** — the [Free-TV](https://github.com/free-tv/iptv)
   playlist, a hand-curated, quality-first list.

Candidates are tried best-first (original source before aggregator, higher
resolution before lower). To turn healing off, add `--no-replace` to the test
step in the workflow.

There is also a hard stop: if a single run would still remove more than 40% of
the playlist **after** healing, it aborts and saves nothing, since that means
the network failed rather than a thousand channels dying at once.

To change how strict it is, edit the workflow's test step:

```yaml
- name: Test every stream
  run: python3 check_streams.py list.m3u --max-strikes 3
```

## Running it yourself

Testing from your own connection is more accurate than GitHub's, because you
won't hit the datacenter blocks:

```bash
pip install -r requirements.txt
python3 check_streams.py list.m3u
```
