"""Generate the static HTML pages of the Bej Off The Record website.

Usage: python3 scripts/build.py

Page copy and links live in this file. Video lists live in
data/series-videos.json and are loaded in the browser, so adding a video
only needs a JSON change (no rebuild). Rebuild after adding a new series
or changing copy.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Site settings. Empty links are hidden.
SITE = {
    "name": "Bej Off The Record",
    "url": "https://bejofftherecord.com",
    "tiktok": "https://www.tiktok.com/@bejofftherecord",
    "instagram": "https://www.instagram.com/bejofftherecord/",
    "youtube": "https://www.youtube.com/@bejofftherecord",
    # Web3Forms access key: messages go to the owner's inbox, the address stays hidden.
    "web3forms_key": "",
}

DATA = json.loads((ROOT / "data" / "series-videos.json").read_text())

NAV = [("Home", ""), ("About", "about/"), ("Series", "series/")]


def esc(text):
    return html.escape(text, quote=True)


def social_links():
    out = []
    for label, key in (("TikTok", "tiktok"), ("Instagram", "instagram"), ("YouTube", "youtube")):
        if SITE[key]:
            out.append((label, SITE[key]))
    return out


def page(path, title, description, body, active="", body_attrs=""):
    """Wrap page content in the shared layout and write it to disk."""
    depth = path.count("/")
    root = "../" * depth
    canonical = f'<link rel="canonical" href="{SITE["url"]}/{path.replace("index.html", "")}">' if SITE["url"] else ""
    nav = "".join(
        f'<a href="{root}{href}"{" class=active" if label == active else ""}>{label}</a>' for label, href in NAV
    )
    nav += f'<a class="cta" href="{root}collabs/">Collabs</a>'
    footer_links = "".join(f'<a href="{u}" target="_blank" rel="noopener">{l}</a>' for l, u in social_links())
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
{canonical}
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE["url"]}/assets/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{root}assets/avatar.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/style.css">
</head>
<body data-root="{root}" {body_attrs}>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{root}"><img class="avatar" data-avatar onerror="this.removeAttribute('src');this.alt=''" src="{root}assets/avatar.png" alt="Bej avatar"><span>BEJ OFF THE RECORD</span></a>
    <button class="menu-toggle" aria-label="Menu">MENU</button>
    <nav class="nav">{nav}</nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="links">{footer_links}</div>
    <small>&copy; 2026 Bej Off The Record</small>
  </div>
</footer>
<script src="{root}assets/site.js"></script>
</body>
</html>
"""
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc)
    print(f"Wrote {path}")


def social_buttons(cls="btn"):
    styles = ["", " pink", ""]
    return "".join(
        f'<a class="{cls}{styles[i % 3]}" href="{u}" target="_blank" rel="noopener">{l.upper()}</a>'
        for i, (l, u) in enumerate(social_links())
    )


def build_home():
    platform_copy = {
        "TikTok": "Full episodes. History, deep dives and ongoing series.",
        "Instagram": "Carousels, reels and concert diaries.",
        "YouTube": "Shorts and Cover Atlas.",
    }
    platforms = "".join(
        f'<div class="card light"><h3>{l}</h3><p>{platform_copy[l]}</p>'
        f'<a class="btn" href="{u}" target="_blank" rel="noopener">Follow on {l}</a></div>'
        for l, u in social_links()
    )
    body = f"""
<section class="hero grid-bg">
  <div class="wrap">
    <div>
      <span class="badge">OFF THE RECORD</span>
      <h1>BEJ OFF THE RECORD</h1>
      <p class="subtitle">Music deep dives for people who read the liner notes.</p>
      <p class="tagline">The B-side of music history.</p>
      <div class="btn-row">{social_buttons()}</div>
    </div>
    <div class="hero-art"><img data-avatar onerror="this.removeAttribute('src');this.alt=''" src="assets/avatar.png" alt="Bej"></div>
  </div>
</section>

<section class="sec-navy">
  <div class="wrap">
    <span class="badge">OFF THE RECORD</span>
    <h2 style="margin-top:18px">What is Bej Off The Record?</h2>
    <p class="lead">Music history with names, dates and an opinion. The stories behind songs, the artists the algorithm forgot, and the covers you didn't know existed.</p>
  </div>
</section>

<section class="grid-bg">
  <div class="wrap">
    <h2>The Content</h2>
    <p class="lead">Every episode starts with one question: what's the real story behind this song? Short, specific, no fan worship.</p>
    <div class="cards">
      <div class="card"><h3>Music History</h3><p>Eras, scenes and countries, told in order.</p></div>
      <div class="card"><h3>Deep Dives</h3><p>One artist, taken apart properly.</p></div>
      <div class="card"><h3>Cover Stories</h3><p>One song, every language it travelled into.</p></div>
      <div class="card"><h3>Live</h3><p>Concert diaries from the crowd.</p></div>
    </div>
    <div class="btn-row"><a class="btn pink" href="series/">See all series</a></div>
  </div>
</section>

<section class="sec-pink">
  <div class="wrap">
    <h2>Where to find me</h2>
    <div class="cards">{platforms}</div>
  </div>
</section>

<section class="grid-bg">
  <div class="wrap" style="text-align:center">
    <h2>Want to work together?</h2>
    <p class="lead" style="margin:0 auto">Labels, venues, festivals and brands with a story worth telling. Let's talk.</p>
    <div class="btn-row" style="justify-content:center"><a class="btn" href="collabs/">Collabs</a></div>
  </div>
</section>
"""
    page(
        "index.html",
        "Bej Off The Record: Music History, Deep Dives and Cover Stories",
        "Short music history episodes with names, dates and an opinion. Deep dives, cover stories from around the world, and concert diaries.",
        body,
        active="Home",
    )


def build_about():
    series_names = ", ".join(s["name"] for s in DATA["series"])
    body = f"""
<section class="grid-bg">
  <div class="wrap about-grid">
    <div>
      <span class="badge">ABOUT</span>
      <h1 style="margin:18px 0 24px">Critic, not fangirl.</h1>
      <p class="lead">I'm Bej. I talk about music with names, dates and an opinion.</p>
      <p class="lead">No "this song is so powerful." I'll tell you what the song actually does, who made it that way, and why nobody talks about it anymore.</p>
    </div>
    <div class="hero-art"><img data-avatar onerror="this.removeAttribute('src');this.alt=''" src="../assets/avatar.png" alt="Bej"></div>
  </div>
</section>

<section class="sec-navy">
  <div class="wrap">
    <h2>What I make</h2>
    <p class="lead">Short episodes. One artist, one era or one song at a time. History, deep dives, cover stories and concert diaries.</p>
    <p style="margin-top:14px;opacity:.8">{esc(series_names)}.</p>
    <div class="btn-row"><a class="btn lime" href="../series/">See all series</a></div>
  </div>
</section>

<section class="grid-bg">
  <div class="wrap" style="text-align:center">
    <h2>Know a song with a better backstory than its chorus?</h2>
    <div class="btn-row" style="justify-content:center"><a class="btn pink" href="../collabs/">Tell me</a></div>
  </div>
</section>
"""
    page("about/index.html", "About Bej, Bej Off The Record",
         "Critic, not fangirl. Who is behind Bej Off The Record and what the channel is about.", body, active="About")


def build_series_overview():
    cards = "".join(
        f'<a class="series-card" href="{s["slug"]}/"><h3>{esc(s["name"])}</h3><p>{esc(s["description"])}</p>'
        f'<span class="count" data-count="{s["slug"]}">{len(s["videos"])} episodes</span></a>'
        for s in DATA["series"]
    )
    body = f"""
<section class="grid-bg">
  <div class="wrap">
    <span class="badge">SERIES</span>
    <h1 style="margin:18px 0 16px">The Series</h1>
    <p class="lead">Every series has one rule. Here they are.</p>
    <div class="series-list">{cards}</div>
  </div>
</section>
"""
    names = ", ".join(s["name"] for s in DATA["series"])
    page("series/index.html", "All Series, Bej Off The Record", f"{names}.", body, active="Series")


def build_series_pages():
    for s in DATA["series"]:
        body = f"""
<section class="grid-bg">
  <div class="wrap">
    <a href="../" style="font-family:var(--display);font-size:20px;letter-spacing:1px;text-decoration:none">&larr; ALL SERIES</a>
    <h1 style="margin:14px 0 14px">{esc(s["name"])}</h1>
    <p class="lead">{esc(s["description"])}</p>
    <div class="toolbar">
      <span class="badge" id="count">{len(s["videos"])} episodes</span>
      <button class="on" data-order="oldest">Oldest first</button>
      <button data-order="newest">Newest first</button>
    </div>
    <div class="videos" id="videos" data-slug="{s["slug"]}"></div>
    <div class="more">
      <button class="btn" id="more">Load more</button>
      <div class="btn-row" style="justify-content:center"><a class="btn pink" href="{SITE["tiktok"]}" target="_blank" rel="noopener">Follow on TikTok</a></div>
    </div>
  </div>
</section>
"""
        page(f"series/{s['slug']}/index.html", f"{s['name']}: All Episodes, Bej Off The Record",
             s["description"], body, active="Series")


def build_collabs():
    if SITE["web3forms_key"]:
        contact = f"""<form class="contact-form" action="https://api.web3forms.com/submit" method="POST" id="contact">
      <input type="hidden" name="access_key" value="{SITE["web3forms_key"]}">
      <input type="hidden" name="subject" value="New collab message from bejofftherecord.com">
      <input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off">
      <input type="text" name="name" placeholder="Name" required>
      <input type="email" name="email" placeholder="Email" required>
      <input type="text" name="company" placeholder="Company or project">
      <textarea name="message" placeholder="What do you have in mind?" required></textarea>
      <div><button class="btn pink" type="submit">Send</button></div>
      <p class="form-status" id="form-status"></p>
    </form>"""
    else:
        contact = (
            f'<div class="btn-row"><a class="btn pink" href="{SITE["instagram"]}" target="_blank" rel="noopener">DM me on Instagram</a>'
            f'<a class="btn lime" href="{SITE["tiktok"]}" target="_blank" rel="noopener">Message me on TikTok</a></div>'
        )
    body = f"""
<section class="grid-bg">
  <div class="wrap">
    <span class="badge">COLLABS</span>
    <h1 style="margin:18px 0 16px">Want to work together?</h1>
    <p class="lead">I work with labels, venues, festivals and brands that have a story worth telling. If it's about music, I'm listening.</p>
    <div class="cards">
      <div class="card"><h3>Artist and album features</h3><p>A deep dive episode on an artist, release or catalogue.</p></div>
      <div class="card"><h3>Live coverage</h3><p>Concert and festival diaries in Berlin and beyond.</p></div>
      <div class="card"><h3>Series sponsorship</h3><p>Support a running series like Cover Atlas or World Music History.</p></div>
      <div class="card"><h3>Research and storytelling</h3><p>The backstory behind a song, scene or archive.</p></div>
    </div>
  </div>
</section>
<section class="sec-navy">
  <div class="wrap">
    <h2>Get in touch</h2>
    <p class="lead">Send me a short note on what you have in mind. Content in English, with descriptions in English and Spanish.</p>
    {contact}
  </div>
</section>
"""
    page("collabs/index.html", "Work With Bej Off The Record",
         "Artist features, live coverage and series sponsorships for labels, venues, festivals and brands.", body)


def build_sitemap():
    if not SITE["url"]:
        return
    paths = ["", "about/", "series/", "collabs/"] + [f"series/{s['slug']}/" for s in DATA["series"]]
    urls = "".join(f"<url><loc>{SITE['url']}/{p}</loc></url>" for p in paths)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>'
    )
    (ROOT / "CNAME").write_text(SITE["url"].split("//")[1] + "\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /preview/\nSitemap: {SITE['url']}/sitemap.xml\n")
    print("Wrote sitemap.xml and robots.txt")


if __name__ == "__main__":
    build_home()
    build_about()
    build_series_overview()
    build_series_pages()
    build_collabs()
    build_sitemap()
