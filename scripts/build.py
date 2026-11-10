"""Generate the static, multilingual (EN, DE, ES) Bej Off The Record website.

Usage: python3 scripts/build.py

Inputs:
  data/series-videos.json   series and their TikTok video URLs
  data/video-meta.json      publish date and caption text per video ID
  data/episodes/*.json      full episode pages (translated)
  scripts/content.py        translated page copy

Every page is written as plain HTML so search engines and AI crawlers can
read all text without running JavaScript.
"""
import html
import json
import re
from datetime import date
from pathlib import Path

from content import (ABOUT, COLLABS, HOME, LANGUAGES, LANGS, LOCALES, MONTHS,
                     PLACES, SERIES, SERIES_PAGE, UI)

ROOT = Path(__file__).resolve().parent.parent
SITE = {
    "name": "Bej Off The Record",
    "url": "https://bejofftherecord.com",
    "tiktok": "https://www.tiktok.com/@bejofftherecord",
    "instagram": "https://www.instagram.com/bejofftherecord/",
    "youtube": "https://www.youtube.com/@bejofftherecord",
}
SOCIAL = [("TikTok", SITE["tiktok"]), ("Instagram", SITE["instagram"]), ("YouTube", SITE["youtube"])]

SERIES_DATA = json.loads((ROOT / "data" / "series-videos.json").read_text())
META = json.loads((ROOT / "data" / "video-meta.json").read_text())
EPISODES = []
for f in sorted((ROOT / "data" / "episodes").glob("*.json")):
    EPISODES.extend(json.loads(f.read_text()))
EPISODE_BY_VIDEO = {e["video"]: e for e in EPISODES}
WRITTEN = []


# ---------- helpers ----------

def esc(text):
    return html.escape(str(text), quote=True)


def clean(text):
    """Remove em and en dashes from captions (house style)."""
    text = re.sub(r"\s*[—–]\s*", ", ", text)
    return re.sub(r",\s*,", ",", text).strip(" ,")


def t(entry, lang):
    return entry.get(lang) or entry["en"]


def url(lang, path=""):
    prefix = "" if lang == "en" else f"/{lang}"
    return f"{prefix}/{path}"


def fmt_date(iso, lang):
    d = date.fromisoformat(iso)
    month = MONTHS[lang][d.month - 1]
    if lang == "en":
        return f"{d.day} {month} {d.year}"
    if lang == "de":
        return f"{d.day}. {month} {d.year}"
    return f"{d.day} de {month} de {d.year}"


def video_id(u):
    return u.rstrip("/").rsplit("/", 1)[1]


def series_videos(slug):
    """Video IDs of a series, oldest first."""
    s = next(x for x in SERIES_DATA["series"] if x["slug"] == slug)
    vids = [video_id(u) for u in s["videos"]]
    vids.sort(key=lambda v: META.get(v, {}).get("date", "9999"))
    return vids


def place(name, lang):
    return name if lang == "en" else PLACES.get(name, {}).get(lang, name)


def language(name, lang):
    return name if lang == "en" else LANGUAGES.get(name, {}).get(lang, name)


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>"


def plural(n, lang):
    return f"{n} {t(UI['episodes'] if n != 1 else UI['episode'], lang)}"


# ---------- layout ----------

def page(lang, path, title, description, body, active="", body_class="", schema=None):
    """Wrap content in the shared layout and write it for one language."""
    canonical = SITE["url"] + url(lang, path)
    alternates = "".join(
        f'<link rel="alternate" hreflang="{l}" href="{SITE["url"]}{url(l, path)}">' for l in LANGS
    ) + f'<link rel="alternate" hreflang="x-default" href="{SITE["url"]}{url("en", path)}">'
    nav_items = [("nav_home", ""), ("nav_about", "about/"), ("nav_series", "series/")]
    nav = "".join(
        f'<a href="{url(lang, p)}"{" class=active" if k == active else ""}>{t(UI[k], lang)}</a>' for k, p in nav_items
    )
    nav += f'<a class="cta" href="{url(lang, "collabs/")}">{t(UI["nav_collabs"], lang)}</a>'
    switch = "".join(
        f'<a href="{url(l, path)}" hreflang="{l}" lang="{l}"{" class=on" if l == lang else ""}>{l.upper()}</a>'
        for l in LANGS
    )
    footer_links = "".join(f'<a href="{u}" target="_blank" rel="noopener">{n}</a>' for n, u in SOCIAL)
    schema_html = "".join(jsonld(s) for s in (schema or []))
    doc = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
{alternates}
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:locale" content="{LOCALES[lang]}">
<meta property="og:image" content="{SITE["url"]}/assets/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/avatar.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@400;500;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
{schema_html}
</head>
<body class="{body_class}">
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{url(lang)}"><img class="avatar" src="/assets/avatar.png" alt="" width="56" height="56"><span>BEJ OFF THE RECORD</span></a>
    <button class="menu-toggle" aria-label="{t(UI['menu'], lang)}">{t(UI['menu'], lang).upper()}</button>
    <nav class="nav">{nav}<span class="langs">{switch}</span></nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="links">{footer_links}</div>
    <div class="langs">{switch}</div>
    <small>&copy; 2026 Bej Off The Record</small>
  </div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""
    out = ROOT / url(lang, path).lstrip("/") / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc)
    WRITTEN.append(url(lang, path))


def lite_video(vid, label, lang):
    """Click-to-load TikTok player. Nothing loads from TikTok until clicked."""
    return (
        f'<div class="lite" data-id="{vid}"><button type="button" aria-label="{esc(label)}">'
        f'<span class="play" aria-hidden="true"></span><span class="lite-label">{t(UI["play"], lang)}</span></button></div>'
    )


def ep_url(lang, ep):
    return url(lang, f"series/{ep['series']}/{ep['slug']}/")


def breadcrumb(lang, items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": name, "item": SITE["url"] + url(lang, p)}
        for i, (name, p) in enumerate(items)
    ]}


# ---------- pages ----------

def build_home(lang):
    social_btns = "".join(
        f'<a class="btn{" pink" if i == 1 else ""}" href="{u}" target="_blank" rel="noopener">{n.upper()}</a>'
        for i, (n, u) in enumerate(SOCIAL)
    )
    cards = "".join(f'<div class="card"><h3>{t(h, lang)}</h3><p>{t(p, lang)}</p></div>' for h, p in HOME["cards"])
    platforms = "".join(
        f'<div class="card light"><h3>{n}</h3><p>{t(HOME["platforms"][n], lang)}</p>'
        f'<a class="btn" href="{u}" target="_blank" rel="noopener">{t(UI["follow_on"], lang)} {n}</a></div>'
        for n, u in SOCIAL
    )
    latest = sorted([e for e in EPISODES if e["series"] == "cover-atlas"], key=lambda e: META[e["video"]]["date"], reverse=True)[:3]
    latest_html = "".join(
        f'<a class="series-card" href="{ep_url(lang, e)}"><h3>{esc(t(e["title"], lang))}</h3>'
        f'<p>{esc(t(e["lead"], lang).split(". ")[0])}.</p><span class="count">{t(UI["read_episode"], lang)}</span></a>'
        for e in latest
    )
    body = f"""
<section class="hero grid-bg">
  <div class="wrap">
    <div>
      <span class="badge">{t(HOME['badge'], lang)}</span>
      <h1>BEJ OFF THE RECORD</h1>
      <p class="subtitle">{t(HOME['subtitle'], lang)}</p>
      <p class="tagline">{t(HOME['tagline'], lang)}</p>
      <div class="btn-row">{social_btns}</div>
    </div>
    <div class="hero-art"><img src="/assets/avatar.png" alt="Bej" width="420" height="420"></div>
  </div>
</section>
<section class="sec-navy">
  <div class="wrap">
    <span class="badge">{t(HOME['badge'], lang)}</span>
    <h2 style="margin-top:18px">{t(HOME['what_title'], lang)}</h2>
    <p class="lead">{t(HOME['what_text'], lang)}</p>
  </div>
</section>
<section class="grid-bg">
  <div class="wrap">
    <h2>{t(HOME['content_title'], lang)}</h2>
    <p class="lead">{t(HOME['content_text'], lang)}</p>
    <div class="cards">{cards}</div>
    <div class="btn-row"><a class="btn pink" href="{url(lang, 'series/')}">{t(UI['see_all_series'], lang)}</a></div>
  </div>
</section>
<section class="sec-navy">
  <div class="wrap">
    <h2>{t(HOME['latest_title'], lang)}</h2>
    <div class="series-list">{latest_html}</div>
  </div>
</section>
<section class="sec-pink">
  <div class="wrap">
    <h2>{t(HOME['find_title'], lang)}</h2>
    <div class="cards">{platforms}</div>
  </div>
</section>
<section class="grid-bg">
  <div class="wrap" style="text-align:center">
    <h2>{t(HOME['collab_title'], lang)}</h2>
    <p class="lead" style="margin:0 auto">{t(HOME['collab_text'], lang)}</p>
    <div class="btn-row" style="justify-content:center"><a class="btn" href="{url(lang, 'collabs/')}">{t(UI['nav_collabs'], lang)}</a></div>
  </div>
</section>
"""
    schema = [{
        "@context": "https://schema.org", "@type": "Organization", "name": SITE["name"], "url": SITE["url"],
        "logo": SITE["url"] + "/assets/avatar.png", "description": t(HOME["description"], "en"),
        "sameAs": [u for _, u in SOCIAL], "founder": {"@type": "Person", "name": "Bej"},
    }, {"@context": "https://schema.org", "@type": "WebSite", "name": SITE["name"], "url": SITE["url"], "inLanguage": LANGS}]
    page(lang, "", t(HOME["title"], lang), t(HOME["description"], lang), body, active="nav_home", schema=schema)


def build_about(lang):
    names = ", ".join(t(SERIES[s["slug"]]["name"], lang) for s in SERIES_DATA["series"])
    body = f"""
<section class="grid-bg">
  <div class="wrap about-grid">
    <div>
      <span class="badge">{t(UI['nav_about'], lang).upper()}</span>
      <h1 style="margin:18px 0 24px">{t(ABOUT['h1'], lang)}</h1>
      <p class="lead">{t(ABOUT['p1'], lang)}</p>
      <p class="lead">{esc(t(ABOUT['p2'], lang))}</p>
    </div>
    <div class="hero-art"><img src="/assets/avatar.png" alt="Bej" width="420" height="420"></div>
  </div>
</section>
<section class="sec-navy">
  <div class="wrap">
    <h2>{t(ABOUT['make_title'], lang)}</h2>
    <p class="lead">{t(ABOUT['make_text'], lang)}</p>
    <p style="margin-top:14px;opacity:.8">{esc(names)}.</p>
    <div class="btn-row"><a class="btn lime" href="{url(lang, 'series/')}">{t(UI['see_all_series'], lang)}</a></div>
  </div>
</section>
<section class="grid-bg">
  <div class="wrap" style="text-align:center">
    <h2>{t(ABOUT['cta'], lang)}</h2>
    <div class="btn-row" style="justify-content:center"><a class="btn pink" href="{url(lang, 'collabs/')}">{t(ABOUT['cta_btn'], lang)}</a></div>
  </div>
</section>
"""
    schema = [{"@context": "https://schema.org", "@type": "AboutPage", "name": t(ABOUT["title"], lang),
               "url": SITE["url"] + url(lang, "about/"), "inLanguage": lang,
               "mainEntity": {"@type": "Person", "name": "Bej", "sameAs": [u for _, u in SOCIAL]}}]
    page(lang, "about/", t(ABOUT["title"], lang), t(ABOUT["description"], lang), body, active="nav_about", schema=schema)


def build_series_overview(lang):
    cards = "".join(
        f'<a class="series-card" href="{url(lang, "series/" + s["slug"] + "/")}"><h3>{esc(t(SERIES[s["slug"]]["name"], lang))}</h3>'
        f'<p>{esc(t(SERIES[s["slug"]]["short"], lang))}</p><span class="count">{plural(len(s["videos"]), lang)}</span></a>'
        for s in SERIES_DATA["series"]
    )
    body = f"""
<section class="grid-bg">
  <div class="wrap">
    <span class="badge">{t(UI['nav_series'], lang).upper()}</span>
    <h1 style="margin:18px 0 16px">{t(SERIES_PAGE['h1'], lang)}</h1>
    <p class="lead">{t(SERIES_PAGE['lead'], lang)}</p>
    <div class="series-list">{cards}</div>
  </div>
</section>
"""
    names = ", ".join(t(SERIES[s["slug"]]["name"], lang) for s in SERIES_DATA["series"])
    page(lang, "series/", t(SERIES_PAGE["title"], lang), names + ".", body, active="nav_series")


def build_series_page(lang, slug):
    info = SERIES[slug]
    name = t(info["name"], lang)
    vids = series_videos(slug)
    items = ""
    for i, vid in enumerate(vids, start=1):
        m = META.get(vid, {"date": "", "text": ""})
        ep = EPISODE_BY_VIDEO.get(vid)
        if ep:
            text, text_lang = t(ep["lead"], lang), lang
            heading = f'<h2 class="ep-title"><a href="{ep_url(lang, ep)}">{esc(t(ep["title"], lang))}</a></h2>'
            read = f'<a class="read" href="{ep_url(lang, ep)}">{t(UI["read_episode"], lang)}</a>'
        else:
            text, text_lang, heading, read = clean(m["text"]), "en", "", ""
        when = f'<time datetime="{m["date"]}">{fmt_date(m["date"], lang)}</time>' if m["date"] else ""
        items += f"""
      <li class="ep-item">
        {lite_video(vid, f"{name} {t(UI['ep'], lang)} {i}", lang)}
        <div class="ep-text">
          <p class="ep-meta"><span class="num">{t(UI['ep'], lang)} {i}</span> {when}</p>
          {heading}
          <p lang="{text_lang}">{esc(text)}</p>
          <p class="ep-links">{read}<a href="https://www.tiktok.com/@bejofftherecord/video/{vid}" target="_blank" rel="noopener">{t(UI['open_tiktok'], lang)}</a></p>
        </div>
      </li>"""
    all_translated = all(v in EPISODE_BY_VIDEO for v in vids)
    note = "" if all_translated else t(UI["captions_note"], lang)
    n = len(vids)
    toggle = (f'<button class="on" data-order="oldest">{t(UI["oldest"], lang)}</button>'
              f'<button data-order="newest">{t(UI["newest"], lang)}</button>') if n > 1 else ""
    body = f"""
<article class="reading">
  <div class="wrap">
    <nav class="crumbs"><a href="{url(lang, 'series/')}">{t(UI['nav_series'], lang)}</a> / {esc(name)}</nav>
    <span class="series-tag">{esc(name.upper())}</span>
    <h1>{esc(name)}</h1>
    <p class="lead">{esc(t(info['intro'], lang))}</p>
    <div class="toolbar"><span class="badge">{plural(n, lang)}</span>{toggle}</div>
    {f'<p class="note">{note}</p>' if note else ''}
    <ol class="ep-list" id="ep-list">{items}
    </ol>
    <div class="btn-row"><a class="btn pink" href="{SITE['tiktok']}" target="_blank" rel="noopener">{t(UI['follow_tiktok'], lang)}</a></div>
  </div>
</article>
"""
    schema = [breadcrumb(lang, [(t(UI["nav_series"], lang), "series/"), (name, f"series/{slug}/")]), {
        "@context": "https://schema.org", "@type": "ItemList", "name": name, "numberOfItems": n,
        "itemListElement": [{"@type": "ListItem", "position": i, "url": f"https://www.tiktok.com/@bejofftherecord/video/{v}"}
                            for i, v in enumerate(vids, 1)],
    }]
    suffix = {"en": "All Episodes", "de": "Alle Folgen", "es": "Todos los episodios"}[lang]
    page(lang, f"series/{slug}/", f"{name}: {suffix}, Bej Off The Record", t(info["short"], lang), body,
         active="nav_series", body_class="read", schema=schema)


def build_episode(lang, ep):
    slug = ep["series"]
    sname = t(SERIES[slug]["name"], lang)
    num = series_videos(slug).index(ep["video"]) + 1
    m = META[ep["video"]]
    path = f"series/{slug}/{ep['slug']}/"
    facts = "".join(f'<div><dt>{esc(t(f["label"], lang))}</dt><dd>{esc(t(f["value"], lang))}</dd></div>' for f in ep["facts"])
    paras = "".join(f"<p>{esc(p)}</p>" for p in ep["body"][lang])
    rows = ""
    for v in ep["versions"]:
        bits = [esc(v["song"])]
        if v.get("place"):
            bits.append(esc(place(v["place"], lang)))
        if v.get("language"):
            bits.append(esc(language(v["language"], lang)))
        if v.get("original"):
            cls, tag = ' class="orig"', f'<span class="tag">{t(UI["original"], lang).upper()}</span>'
        elif v.get("bonus"):
            cls, tag = ' class="bonus"', '<span class="tag">BONUS</span>'
        else:
            cls, tag = "", ""
        rows += (f'<li{cls}><div><strong>{esc(v["artist"])}</strong>{tag}<em>{" · ".join(bits)}</em></div>'
                 f'<span class="y">{v.get("year", "")}</span></li>')
    others = [e for e in EPISODES if e["series"] == slug and e is not ep]
    more = "".join(f'<li><a href="{ep_url(lang, o)}">{esc(t(o["title"], lang))}</a></li>' for o in others)
    title = t(ep["title"], lang)
    tiktok = f"https://www.tiktok.com/@bejofftherecord/video/{ep['video']}"
    body = f"""
<article class="reading">
  <div class="wrap">
    <nav class="crumbs"><a href="{url(lang, 'series/')}">{t(UI['nav_series'], lang)}</a> / <a href="{url(lang, 'series/' + slug + '/')}">{esc(sname)}</a> / {t(UI['ep'], lang)} {num}</nav>
    <span class="series-tag">{esc(sname.upper())}</span>
    <h1>{esc(title)}</h1>
    <p class="lead">{esc(t(ep['lead'], lang))}</p>
    <p class="meta">{t(UI['by_bej'], lang)} · {t(UI['published'], lang)} <time datetime="{m['date']}">{fmt_date(m['date'], lang)}</time></p>
    <div class="ep-grid">
      <aside class="ep-video">{lite_video(ep['video'], t(UI['watch_episode'], lang), lang)}
        <a class="small" href="{tiktok}" target="_blank" rel="noopener">{t(UI['open_tiktok'], lang)}</a></aside>
      <div class="ep-body">
        <dl class="facts">{facts}</dl>
        <h2>{t(UI['the_story'], lang)}</h2>
        {paras}
        <h2>{t(UI['every_version'], lang)}</h2>
        <ol class="versions">{rows}</ol>
        <p class="note">{t(UI['year_note'], lang)}</p>
        <h2>{t(UI['more_in_series'], lang)} {esc(sname)}</h2>
        <ul class="more-list">{more}</ul>
      </div>
    </div>
  </div>
</article>
"""
    schema = [breadcrumb(lang, [(t(UI["nav_series"], lang), "series/"), (sname, f"series/{slug}/"), (title, path)]), {
        "@context": "https://schema.org", "@type": "VideoObject", "name": title, "description": t(ep["lead"], lang),
        "uploadDate": m["date"], "thumbnailUrl": SITE["url"] + "/assets/og.jpg",
        "embedUrl": f"https://www.tiktok.com/player/v1/{ep['video']}", "url": tiktok, "inLanguage": "en",
        "isPartOf": {"@type": "CreativeWorkSeries", "name": sname, "url": SITE["url"] + url(lang, f"series/{slug}/")},
        "creator": {"@type": "Organization", "name": SITE["name"], "url": SITE["url"]},
    }, {
        "@context": "https://schema.org", "@type": "Article", "headline": title, "description": t(ep["lead"], lang),
        "datePublished": m["date"], "inLanguage": lang,
        "author": {"@type": "Person", "name": "Bej", "url": SITE["url"] + url(lang, "about/")},
        "publisher": {"@type": "Organization", "name": SITE["name"], "logo": {"@type": "ImageObject", "url": SITE["url"] + "/assets/avatar.png"}},
        "mainEntityOfPage": SITE["url"] + url(lang, path),
    }]
    desc = t(ep["lead"], lang)
    if len(desc) > 158:
        desc = desc[:155].rsplit(" ", 1)[0] + "..."
    page(lang, path, f"{title}, {sname}", desc, body, active="nav_series", body_class="read", schema=schema)


def build_collabs(lang):
    cards = "".join(f'<div class="card"><h3>{t(h, lang)}</h3><p>{t(p, lang)}</p></div>' for h, p in COLLABS["cards"])
    body = f"""
<section class="grid-bg">
  <div class="wrap">
    <span class="badge">{t(UI['nav_collabs'], lang).upper()}</span>
    <h1 style="margin:18px 0 16px">{t(COLLABS['h1'], lang)}</h1>
    <p class="lead">{t(COLLABS['lead'], lang)}</p>
    <div class="cards">{cards}</div>
  </div>
</section>
<section class="sec-navy">
  <div class="wrap">
    <h2>{t(COLLABS['contact_title'], lang)}</h2>
    <p class="lead">{t(COLLABS['contact_text'], lang)}</p>
    <div class="btn-row"><a class="btn pink" href="{SITE['instagram']}" target="_blank" rel="noopener">{t(COLLABS['dm_ig'], lang)}</a><a class="btn lime" href="{SITE['tiktok']}" target="_blank" rel="noopener">{t(COLLABS['dm_tt'], lang)}</a></div>
  </div>
</section>
"""
    page(lang, "collabs/", t(COLLABS["title"], lang), t(COLLABS["description"], lang), body, active="nav_collabs")


def build_extras():
    """Sitemap with hreflang, robots.txt, llms.txt and CNAME."""
    bases = sorted({re.sub(r"^/(de|es)/", "/", p) for p in WRITTEN})
    today = date.today().isoformat()
    urls = ""
    for base in bases:
        path = base.lstrip("/")
        alts = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{SITE["url"]}{url(l, path)}"/>' for l in LANGS)
        for l in LANGS:
            urls += f'<url><loc>{SITE["url"]}{url(l, path)}</loc><lastmod>{today}</lastmod>{alts}</url>'
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
        f'xmlns:xhtml="http://www.w3.org/1999/xhtml">{urls}</urlset>'
    )
    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "PerplexityBot",
            "Google-Extended", "Applebot-Extended"]
    robots = "User-agent: *\nAllow: /\nDisallow: /preview/\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots)
    (ROOT / "robots.txt").write_text(robots + f"Sitemap: {SITE['url']}/sitemap.xml\n")
    lines = [
        "# Bej Off The Record", "",
        "> Music history channel by Bej on TikTok, Instagram and YouTube. Short episodes with names, dates and an opinion: "
        "Mexican music history decade by decade, biographies of rock frontwomen, music video directors, and Cover Atlas, "
        "which follows one song through its versions in other countries and languages. Site in English, German and Spanish.",
        "", "## Series",
    ]
    for s in SERIES_DATA["series"]:
        lines.append(f"- [{t(SERIES[s['slug']]['name'], 'en')}]({SITE['url']}/series/{s['slug']}/): {t(SERIES[s['slug']]['short'], 'en')}")
    lines += ["", "## Cover Atlas episodes"]
    for e in EPISODES:
        lines.append(f"- [{t(e['title'], 'en')}]({SITE['url']}{ep_url('en', e)}): {t(e['lead'], 'en')}")
    lines += ["", "## Profiles"] + [f"- [{n}]({u})" for n, u in SOCIAL]
    (ROOT / "llms.txt").write_text("\n".join(lines) + "\n")
    (ROOT / "CNAME").write_text("bejofftherecord.com\n")
    print(f"Wrote {len(WRITTEN)} pages, sitemap.xml, robots.txt, llms.txt")


if __name__ == "__main__":
    for lang in LANGS:
        build_home(lang)
        build_about(lang)
        build_series_overview(lang)
        for s in SERIES_DATA["series"]:
            build_series_page(lang, s["slug"])
        for ep in EPISODES:
            build_episode(lang, ep)
        build_collabs(lang)
    build_extras()
