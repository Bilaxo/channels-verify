# IPTV playlist

Auto-tested IPTV playlist. Every 3 days a GitHub Action tests every stream and
removes the dead ones from `list.m3u`.

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
| `list.m3u` | The playlist. This is the file that gets cleaned. |
| `check_streams.py` | Tests the streams |
| `requirements.txt` | Python dependency |
| `.github/workflows/check-playlist.yml` | Runs the check every 3 days |
| `removed.m3u` | Channels that were removed (created on first run) |
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

## How channels get removed

A channel is not removed the first time it fails — it gets a strike, and any
success clears it. Only after **failing twice in a row** is it removed, and it
is moved to `removed.m3u` rather than deleted.

The reason for that delay: GitHub's servers are in a US datacenter. Some
streams are geo-blocked or reject datacenter connections, so they fail there
while working fine on your home connection. Removing on the first failure
would strip out channels that work for you.

There is also a hard stop: if a single run would remove more than 40% of the
playlist, it aborts and saves nothing, since that means the network failed
rather than a thousand channels dying at once.

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
