#!/usr/bin/env python3
"""
Build the Veritas RELEASED deliverables preview site.

Reads markdown files from ~/wiki/clients/veritas-developments/projects/,
renders them as standalone HTML pages with shared CSS, generates an index page.

Output: ~/wiki/clients/veritas-developments/projects-preview/

Convention:
- draft-preview = working hypothesis, NOT source-of-truth (yellow banner)
- project-preview = HITL-validated, RELEASED (green banner)
"""

import os
from pathlib import Path
import markdown_it
import re

WIKI = Path.home() / "wiki" / "clients" / "veritas-developments"
PROJECTS_DIR = WIKI / "projects"
OUT_DIR = WIKI / "projects-preview"

# (path_relative_to_projects/, display_title, short_description, owner, status, validation_date)
RELEASED = [
    (
        "website/COVER-NOTE-seo-audit-v4-2026-08-28.md",
        "Cover Note — SEO Audit v4",
        "60s exec summary + 2 decisions for David + Daniel",
        "Dennis Eng",
        "RELEASED",
        "2026-08-28",
    ),
    (
        "website/seo-audit-veritasdevelopmentgroupllc-2026-08-28-client.md",
        "SEO Audit — veritasdevelopmentgroupllc.com (v4)",
        "8-keyword SERP intel, 90-day content plan, keyword reclassifications",
        "Dennis Eng (KlickSmartAI)",
        "RELEASED — presentable to David + Daniel",
        "2026-08-28",
    ),
    (
        "website/CLIENT-SCORE-veritas-developments-2026-08-28.md",
        "Client Score — Veritas (Composite 32/100, CONDITIONAL)",
        "Pre-quote ROI snapshot — $358K/yr at $75/click, Year-1 ROI 1,647%, break-even 0.7mo",
        "Dennis Eng (KlickSmartAI)",
        "RELEASED — presentable to David + Daniel",
        "2026-08-28",
    ),
]

CSS = """
:root {
    --paper: #fafaf7;
    --ink: #1a1a1a;
    --ink-soft: #4a4a4a;
    --rule: #d8d4c8;
    --accent: #2d5f3f;
    --accent-soft: #5b8a6b;
    --released-bg: #e9f3ec;
    --released-border: #2d5f3f;
    --shadow: 0 1px 2px rgba(0,0,0,.05);
}
* { box-sizing: border-box; }
html, body {
    margin: 0; padding: 0;
    background: var(--paper);
    color: var(--ink);
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 16px;
    line-height: 1.6;
}
header.site-header {
    border-bottom: 2px solid var(--rule);
    padding: 20px 32px 16px;
    background: #f5f3eb;
}
header.site-header h1 {
    margin: 0; font-size: 22px; letter-spacing: 0.02em; color: var(--accent);
}
header.site-header .meta {
    margin: 4px 0 0; font-size: 13px; color: var(--ink-soft);
    font-family: 'Helvetica Neue', sans-serif;
}
nav.site-nav {
    border-bottom: 1px solid var(--rule);
    padding: 12px 32px;
    background: #fffef9;
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 14px;
}
nav.site-nav a {
    color: var(--accent); text-decoration: none; margin-right: 24px;
    border-bottom: 1px dotted var(--accent-soft);
}
nav.site-nav a:hover { color: var(--ink); border-bottom: 1px solid var(--ink); }
nav.site-nav a.current { font-weight: bold; color: var(--ink); border-bottom: 1px solid var(--ink); }
main { max-width: 920px; margin: 32px auto 64px; padding: 0 32px; }
.released-banner {
    background: var(--released-bg);
    border: 1px solid var(--released-border);
    border-left: 4px solid var(--released-border);
    padding: 16px 20px;
    margin-bottom: 32px;
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 14px;
    color: #1d3d27;
}
.released-banner strong { color: #143320; }
.draft-banner {
    background: #fff8e6;
    border: 1px solid #b8821d;
    border-left: 4px solid #b8821d;
    padding: 16px 20px;
    margin-bottom: 32px;
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 14px;
    color: #5a3d0e;
}
.draft-banner strong { color: #3d2a08; }
article h1 {
    font-size: 36px; line-height: 1.2; margin: 0 0 8px;
    border-bottom: 1px solid var(--rule); padding-bottom: 16px;
}
article h2 {
    font-size: 24px; margin: 40px 0 12px;
    border-bottom: 1px dotted var(--rule); padding-bottom: 8px;
}
article h3 { font-size: 18px; margin: 28px 0 8px; color: var(--accent); }
article h4 { font-size: 15px; margin: 20px 0 6px; text-transform: uppercase; letter-spacing: 0.04em; }
article p { margin: 12px 0; }
article ul, article ol { padding-left: 28px; }
article li { margin: 4px 0; }
article code {
    background: #efece2; padding: 1px 5px; border-radius: 2px;
    font-family: 'SF Mono', 'Consolas', monospace; font-size: 14px;
}
article pre {
    background: #f5f3eb; border-left: 3px solid var(--accent-soft);
    padding: 12px 16px; overflow-x: auto; font-size: 13px;
    border-radius: 0 3px 3px 0;
}
article pre code { background: none; padding: 0; }
article blockquote {
    border-left: 3px solid var(--rule);
    margin: 16px 0; padding: 8px 16px;
    color: var(--ink-soft); font-style: italic;
}
article table {
    border-collapse: collapse; width: 100%; margin: 16px 0;
    font-family: 'Helvetica Neue', sans-serif; font-size: 14px;
    box-shadow: var(--shadow);
}
article table th {
    background: #eae6d6; text-align: left; padding: 8px 12px;
    border-bottom: 2px solid var(--rule); font-weight: 600;
}
article table td {
    padding: 8px 12px; border-bottom: 1px solid var(--rule);
    vertical-align: top;
}
article table tr:hover td { background: #fbfaf3; }
article hr { border: none; border-top: 1px solid var(--rule); margin: 32px 0; }
article a { color: var(--accent); }
footer.site-footer {
    border-top: 1px solid var(--rule);
    padding: 20px 32px;
    text-align: center;
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 12px;
    color: var(--ink-soft);
    background: #f5f3eb;
}
.kbd {
    background: #fff;
    border: 1px solid var(--rule);
    border-bottom-width: 2px;
    border-radius: 3px;
    padding: 1px 6px;
    font-family: 'SF Mono', monospace;
    font-size: 12px;
}
.summary-card {
    background: #fff;
    border: 1px solid var(--rule);
    border-top: 3px solid var(--accent);
    padding: 20px 24px;
    margin: 24px 0;
    box-shadow: var(--shadow);
    border-radius: 0 0 3px 3px;
}
.summary-card h3 {
    margin: 0 0 8px;
    color: var(--accent);
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 0.04em;
}
"""

INDEX_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="site-header">
  <h1>Veritas Lee's Summit — Released Deliverables</h1>
  <p class="meta">Source-of-truth · HITL-validated · {build_date} · Dennis Eng (KlickSmartAI) for David Poole + Daniel Bailey</p>
</header>
<nav class="site-nav">{nav}</nav>
<main>
  <div class="released-banner">
    <strong>✅ RELEASED — SOURCE-OF-TRUTH</strong><br>
    These documents have moved out of <code>drafts/</code> into <code>projects/</code> after HITL validation
    (Dennis sign-off 2026-08-28; pending David + Daniel review on the 2 documented decisions).
    Anything in this folder is presentable to the client.
  </div>
"""

INDEX_TAIL = """</main>
<footer class="site-footer">
  Built by KlickSmartAI · {build_date} · source-of-truth · promotion requires Dennis + client signoff
</footer>
</body>
</html>
"""

DOC_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="site-header">
  <h1>{header_title}</h1>
  <p class="meta">Veritas Development Group LLC · Released Deliverables · built {build_date}</p>
</header>
<nav class="site-nav">{nav}</nav>
<main>
  <div class="{banner_class}">
    <strong>{banner_emoji} {banner_status}</strong> · {validation_meta} ·
    <a href="index.html">Back to released list</a>
  </div>
  <article class="doc-body">
"""

DOC_TAIL = """  </article>
</main>
<footer class="site-footer">
  Built by KlickSmartAI · {build_date} · source-of-truth · promotion requires Dennis + client signoff
</footer>
</body>
</html>
"""

def build_slug(rel_path: str) -> str:
    return rel_path.replace("/", "__").replace(".md", ".html")

def build_nav(current_slug=None):
    parts = ['<a href="index.html"' + (' class="current"' if current_slug is None else "") + '>Index</a>']
    for rel_path, title, *_ in RELEASED:
        slug = build_slug(rel_path)
        cls = ' class="current"' if current_slug == slug else ''
        parts.append(f'<a href="{slug}"{cls}>{title}</a>')
    return "\n    ".join(parts)

def extract_frontmatter(md_text):
    """Returns (frontmatter_dict, body) — body without frontmatter."""
    fm = {}
    body = md_text
    if md_text.startswith("---"):
        end = md_text.find("\n---", 3)
        if end != -1:
            fm_text = md_text[3:end]
            body = md_text[end + 4:].lstrip("\n")
            for line in fm_text.splitlines():
                m = re.match(r"^(\w[\w_-]*)\s*:\s*(.*)$", line)
                if m:
                    key = m.group(1)
                    val = m.group(2).strip().strip('"').strip("'")
                    fm[key] = val
    return fm, body

def render_md(md_text):
    fm, body = extract_frontmatter(md_text)
    md = markdown_it.MarkdownIt("commonmark", {"html": True, "typographer": True})
    md.enable("table")
    md.enable("strikethrough")
    return md.render(body), fm

def render_index(build_date):
    nav = build_nav()
    parts = [INDEX_HEAD.format(title="Veritas Released Deliverables — Index", nav=nav, build_date=build_date)]
    parts.append('<article>')
    parts.append('<h1>Released deliverables awaiting David + Daniel review</h1>')
    parts.append('<p>Documents promoted from <code>drafts/</code> → <code>projects/</code> after HITL validation. Anything here can be presented to the client.</p>')
    parts.append('<h2>✅ Released files</h2>')
    parts.append('<table>')
    parts.append('<thead><tr><th>#</th><th>Document</th><th>What it is</th><th>Released by</th><th>Status</th><th>Date</th></tr></thead><tbody>')
    for i, (rel_path, title, desc, owner, status, vdate) in enumerate(RELEASED, 1):
        slug = build_slug(rel_path)
        parts.append(f'<tr><td>{i}</td><td><a href="{slug}">{title}</a><br><span style="font-family:SF Mono,monospace;font-size:11px;color:#888">{rel_path}</span></td><td>{desc}</td><td>{owner}</td><td>{status}</td><td>{vdate}</td></tr>')
    parts.append('</tbody></table>')
    parts.append('<h2>Linked companion assets</h2>')
    parts.append('<ul>')
    parts.append('<li><code>../drafts/website/serp-intelligence-2026-08-28.md</code> — raw SERP analysis that backs the audit (drafts/, not released)</li>')
    parts.append('<li><code>../drafts/outreach/2026-08-28-decision-matrix-for-david-daniel.md</code> — full decision matrix awaiting David + Daniel signoff (drafts/)</li>')
    parts.append('<li><code>../drafts/VALIDATION_QUEUE.md</code> — row 8a marked RELEASED 2026-08-28</li>')
    parts.append('</ul>')
    parts.append('<h2>How to give feedback</h2>')
    parts.append('<p>Reply to Dennis with one of these:</p>')
    parts.append('<ul>')
    parts.append('<li><span class="kbd">approved</span> — drop the gate, mark David + Daniel signoff complete</li>')
    parts.append('<li><span class="kbd">changes: ...</span> — specify edits, re-release</li>')
    parts.append('<li><span class="kbd">not ready</span> — promote back to <code>drafts/</code></li>')
    parts.append('</ul>')
    parts.append('</article>')
    parts.append(INDEX_TAIL.format(build_date=build_date))
    return "\n".join(parts)

def render_doc(rel_path, title, desc, owner, status, vdate, build_date):
    src = PROJECTS_DIR / rel_path
    with open(src) as f:
        md = f.read()
    body_md, fm = render_md(md)
    fm_title = fm.get("title", title)
    slug = build_slug(rel_path)
    nav = build_nav(slug)
    validation_meta = f'Released by <strong>{owner}</strong> on <strong>{vdate}</strong> — <span style="color:var(--accent-soft)">{status}</span>'
    # Pick banner style based on status
    is_draft = "DRAFT" in status.upper()
    banner_class = "draft-banner" if is_draft else "released-banner"
    banner_emoji = "📝" if is_draft else "✅"
    banner_status = "DRAFT" if is_draft else "RELEASED"
    head = DOC_HEAD.format(
        title=f"Veritas — {fm_title}",
        header_title=f"Veritas {fm_title}",
        nav=nav,
        build_date=build_date,
        validation_meta=validation_meta,
        banner_class=banner_class,
        banner_emoji=banner_emoji,
        banner_status=banner_status,
    )
    tail = DOC_TAIL.format(build_date=build_date)
    return head + body_md + tail

def main():
    import datetime
    build_date = datetime.date.today().isoformat()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "styles.css").write_text(CSS)
    (OUT_DIR / "index.html").write_text(render_index(build_date))
    print(f"  ✓ index.html")

    for rel_path, title, desc, owner, status, vdate in RELEASED:
        out_name = build_slug(rel_path)
        out_path = OUT_DIR / out_name
        out_path.write_text(render_doc(rel_path, title, desc, owner, status, vdate, build_date))
        size_kb = out_path.stat().st_size / 1024
        print(f"  ✓ {out_name:60s}  {size_kb:7.1f} KB")

    print(f"\nBuilt → {OUT_DIR}")

if __name__ == "__main__":
    main()