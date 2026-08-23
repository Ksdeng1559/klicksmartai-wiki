#!/usr/bin/env python3
"""
Build the Veritas drafts preview site.

Reads markdown drafts from ~/wiki/clients/veritas-developments/drafts/,
renders them as standalone HTML pages with shared CSS, generates an
index page, and copies the TAM CSV.

Output: ~/wiki/clients/veritas-developments/drafts-preview/
"""

import os
import shutil
import csv
import html
from pathlib import Path
import markdown_it

WIKI = Path.home() / "wiki" / "clients" / "veritas-developments"
DRAFTS_DIR = WIKI / "drafts"
OUT_DIR = WIKI / "drafts-preview"

DRAFTS = [
    ("VALIDATION_QUEUE.md", "Validation Queue", "5 HITL questions per draft + cleanup options"),
    ("tam-co-sponsor-capital-2026-08-22.md", "TAM — Co-Sponsor Capital", "54 orgs, $0 cost, 3 tiers"),
    ("kc-family-office-law-firm-channel-2026-08-22.md", "KC Family Office Law Firm Channel", "5 KC firms + outreach playbook"),
    ("team-profile-daniel-bailey-2026-08-22.md", "Team Profile — Daniel Bailey", "FO outreach lead + Veritas team"),
    ("7-touch-outreach-playbook-2026-08-22.md", "7-Touch Outreach Playbook", "T1-T7 templates + Reg D 506(b) compliance"),
]

CSS = """
:root {
    --paper: #fafaf7;
    --ink: #1a1a1a;
    --ink-soft: #4a4a4a;
    --rule: #d8d4c8;
    --accent: #8b3a2a;
    --accent-soft: #c4665a;
    --draft-bg: #fdf6e3;
    --draft-border: #d4a418;
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
    margin: 0; font-size: 22px; letter-spacing: 0.02em;
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
.draft-banner {
    background: var(--draft-bg);
    border: 1px solid var(--draft-border);
    border-left: 4px solid var(--draft-border);
    padding: 16px 20px;
    margin-bottom: 32px;
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 14px;
    color: #5c4a0a;
}
.draft-banner strong { color: #3d2f00; }
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
.toc {
    background: #fdfaf0;
    border: 1px solid var(--rule);
    padding: 16px 24px;
    margin: 24px 0;
    font-size: 14px;
}
.toc h4 { margin: 0 0 8px; font-family: 'Helvetica Neue', sans-serif; }
.toc ul { margin: 0; padding-left: 20px; }
.toc a { color: var(--ink-soft); }
.csv-link {
    background: #fff;
    border: 1px solid var(--rule);
    padding: 8px 14px;
    margin: 8px 0;
    font-family: 'SF Mono', monospace;
    font-size: 13px;
    display: inline-block;
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
  <h1>Veritas Lee's Summit — Drafts Preview</h1>
  <p class="meta">Local preview · built 2026-08-22 · David + Daniel review · awaiting HITL validation</p>
</header>
<nav class="site-nav">{nav}</nav>
<main>
  <div class="draft-banner">
    <strong>⚠ DRAFTS — NOT SOURCE-OF-TRUTH</strong><br>
    These documents are working hypotheses built by AI from public web research + inference about Veritas team relationships.
    All 5 files have been moved from <code>projects/</code> to <code>drafts/</code> per the
    <code>wiki-source-of-truth-governance</code> skill. Promotion to <code>projects/</code> requires
    David Poole + Daniel Bailey HITL approval of the 5 questions in the Validation Queue.
  </div>
"""

INDEX_TAIL = """</main>
<footer class="site-footer">
  Built by KlickSmartAI · 2026-08-22 · preview-only · no commits to source-of-truth
</footer>
</body>
</html>
"""

DOC_HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<header class="site-header">
  <h1>Veritas Lee's Summit — Drafts Preview</h1>
  <p class="meta">Local preview · built 2026-08-22 · David + Daniel review · awaiting HITL validation</p>
</header>
<nav class="site-nav">{nav}</nav>
<main>
  <div class="draft-banner">
    <strong>⚠ DRAFT — NOT SOURCE-OF-TRUTH</strong> ·
    <a href="index.html">Back to drafts list</a>
  </div>
  <article>
"""

DOC_TAIL = """  </article>
</main>
<footer class="site-footer">
  Built by KlickSmartAI · 2026-08-22 · preview-only · no commits to source-of-truth
</footer>
</body>
</html>
"""

def build_nav(current_slug=None):
    parts = ['<a href="index.html"' + (' class="current"' if current_slug is None else "") + '>Index</a>']
    for fn, title, _ in DRAFTS:
        slug = fn.replace(".md", ".html")
        cls = ' class="current"' if current_slug == slug else ''
        parts.append(f'<a href="{slug}"{cls}>{title}</a>')
    return "\n    ".join(parts)

def extract_frontmatter(md_text):
    """Returns (title, body) — title from frontmatter, body without frontmatter."""
    title = None
    if md_text.startswith("---"):
        end = md_text.find("\n---", 3)
        if end != -1:
            fm = md_text[3:end]
            body = md_text[end + 4:].lstrip("\n")
            for line in fm.splitlines():
                if line.startswith("title:"):
                    title = line.split(":", 1)[1].strip().strip('"').strip("'")
                    break
            return title, body
    return title, md_text

def render_md(md_text):
    title, body = extract_frontmatter(md_text)
    md = markdown_it.MarkdownIt("commonmark", {"html": True, "typographer": True})
    md.enable("table")
    md.enable("strikethrough")
    return md.render(body), title

def render_tam_csv_to_table():
    csv_path = DRAFTS_DIR / "tam-co-sponsor-capital-2026-08-22.csv"
    with open(csv_path, newline='') as f:
        rdr = csv.reader(f)
        rows = list(rdr)
    if not rows:
        return "<p><em>CSV empty</em></p>"
    head = rows[0]
    body = rows[1:]
    out = ['<table>', '<thead><tr>']
    for h in head:
        out.append(f"<th>{html.escape(h)}</th>")
    out.append('</tr></thead><tbody>')
    for row in body:
        out.append('<tr>')
        for cell in row:
            out.append(f"<td>{html.escape(cell)}</td>")
        out.append('</tr>')
    out.append('</tbody></table>')
    return "\n".join(out)

def render_index():
    nav = build_nav()
    parts = [INDEX_HEAD.format(title="Veritas Drafts — Index", nav=nav)]
    parts.append('<article>')
    parts.append('<h1>Drafts awaiting HITL validation</h1>')
    parts.append('<p>Built 2026-08-22 from public web research + AI inference. Promote to source-of-truth only after David Poole + Daniel Bailey answer the 5 questions in the Validation Queue.</p>')
    parts.append('<h2>5 Drafts in <code>drafts/</code></h2>')
    parts.append('<table>')
    parts.append('<thead><tr><th>#</th><th>Document</th><th>What it is</th><th>Validation owner</th><th>Status</th></tr></thead><tbody>')
    for i, (fn, title, desc) in enumerate(DRAFTS, 1):
        slug = fn.replace(".md", ".html")
        if "VALIDATION" in fn:
            owner = "Dennis + David + Daniel"
            status = "ACTIVE gate"
        elif "tam" in fn:
            owner = "Dennis + David"
            status = "awaiting review"
        elif "law-firm" in fn:
            owner = "Dennis + David"
            status = "awaiting review"
        elif "daniel-bailey" in fn:
            owner = "Daniel"
            status = "awaiting review"
        elif "playbook" in fn:
            owner = "David + Daniel"
            status = "awaiting review"
        else:
            owner, status = "—", "—"
        parts.append(f'<tr><td>{i}</td><td><a href="{slug}">{title}</a></td><td>{desc}</td><td>{owner}</td><td>{status}</td></tr>')
    parts.append('</tbody></table>')
    parts.append('<h2>TAM CSV (downloadable)</h2>')
    parts.append('<a class="csv-link" href="tam-co-sponsor-capital-2026-08-22.csv">⬇ tam-co-sponsor-capital-2026-08-22.csv</a>')
    parts.append('<p>Or view rendered:</p>')
    parts.append(render_tam_csv_to_table())
    parts.append('<h2>How to give feedback</h2>')
    parts.append('<p>Reply to any of these to David / Daniel:</p>')
    parts.append('<ul>')
    parts.append('<li>"Confirmed, promote to projects/" → moves file to <code>projects/</code> + commits + pushes to both wikis</li>')
    parts.append('<li>"Confirmed with changes: ..." → modifies + promotes + commits</li>')
    parts.append('<li>"Not ready yet, leave in drafts/" → stays uncommitted</li>')
    parts.append('<li>"Delete entirely" → removes from <code>drafts/</code></li>')
    parts.append('</ul>')
    parts.append('<h2>Cleanup options for <code>veritasdevelopment-wiki</code> client-visible repo</h2>')
    parts.append('<p>The 5 files were pushed to the client-visible repo before the validation gate existed. Awaiting David decision:</p>')
    parts.append('<ul>')
    parts.append('<li><strong>Option A (recommended):</strong> remove the 5 files from veritasdevelopment-wiki</li>')
    parts.append('<li><strong>Option B:</strong> rename folder to <code>drafts-pending-validation/</code></li>')
    parts.append('<li><strong>Option C:</strong> leave as-is (risky)</li>')
    parts.append('</ul>')
    parts.append('</article>')
    parts.append(INDEX_TAIL)
    return "\n".join(parts)

def render_doc(filename, title):
    src = DRAFTS_DIR / filename
    with open(src) as f:
        md = f.read()
    body_md, fm_title = render_md(md)
    display_title = fm_title or title
    slug = filename.replace(".md", ".html")
    nav = build_nav(slug)
    head = DOC_HEAD.format(title=f"Veritas Draft — {display_title}", nav=nav)
    return head + body_md + DOC_TAIL

def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "styles.css").write_text(CSS)
    (OUT_DIR / "index.html").write_text(render_index())
    for fn, title, _ in DRAFTS:
        out_name = fn.replace(".md", ".html")
        (OUT_DIR / out_name).write_text(render_doc(fn, title))
        print(f"  ✓ {out_name}")
    src_csv = DRAFTS_DIR / "tam-co-sponsor-capital-2026-08-22.csv"
    dst_csv = OUT_DIR / "tam-co-sponsor-capital-2026-08-22.csv"
    shutil.copy(src_csv, dst_csv)
    print(f"  ✓ {dst_csv.name}")
    print(f"\nBuilt → {OUT_DIR}")
    files_in = sorted(OUT_DIR.iterdir())
    print(f"Files: {len(files_in)}")
    for f in files_in:
        size_kb = f.stat().st_size / 1024
        print(f"  {f.name:50s}  {size_kb:7.1f} KB")

if __name__ == "__main__":
    main()