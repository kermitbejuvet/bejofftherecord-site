"""Download YouTube Shorts thumbnails for every mapped video and store them as 9:16 JPEGs.

Runs in GitHub Actions (the build sandbox cannot reach YouTube). Only missing files are fetched,
so the script is cheap to re-run.
"""
import io
import json
import sys
import urllib.request
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "thumbs"
SIZES = ["oar2.jpg", "maxresdefault.jpg", "sddefault.jpg", "hqdefault.jpg"]


def fetch(yt_id):
    """Return the best available thumbnail as a PIL image, or None."""
    for name in SIZES:
        try:
            with urllib.request.urlopen(f"https://i.ytimg.com/vi/{yt_id}/{name}", timeout=20) as r:
                img = Image.open(io.BytesIO(r.read())).convert("RGB")
        except Exception:
            continue
        if img.width >= 200:
            return img
    return None


def to_portrait(img, w=360, h=640):
    """Center-crop to 9:16 (Shorts thumbnails in landscape files have side bars) and resize."""
    target = w / h
    if img.width / img.height > target:
        nw = round(img.height * target)
        left = (img.width - nw) // 2
        img = img.crop((left, 0, left + nw, img.height))
    else:
        nh = round(img.width / target)
        top = (img.height - nh) // 2
        img = img.crop((0, top, img.width, top + nh))
    return img.resize((w, h), Image.LANCZOS)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    mapping = json.loads((ROOT / "data" / "youtube-map.json").read_text())
    missing = sorted({y for y in mapping.values() if not (OUT / f"{y}.jpg").exists()})
    print(f"{len(missing)} thumbnails to fetch")
    failed = []
    for yt_id in missing:
        img = fetch(yt_id)
        if img is None:
            failed.append(yt_id)
            continue
        to_portrait(img).save(OUT / f"{yt_id}.jpg", "JPEG", quality=80, optimize=True, progressive=True)
        print("saved", yt_id)
    if failed:
        print("FAILED:", ", ".join(failed))
    return 0


if __name__ == "__main__":
    sys.exit(main())
