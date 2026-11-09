# Bej Off The Record website

Static site, hosted on GitHub Pages.

- `data/series-videos.json`: every series and its TikTok videos, oldest first. To add a video, append its URL to the end of the right series. No rebuild needed.
- `scripts/build.py`: generates all HTML pages (copy, links, SEO). Run `python3 scripts/build.py` after changing copy or adding a new series.
- `assets/`: styles, script and `avatar.png`.
