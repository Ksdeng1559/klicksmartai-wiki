#!/usr/bin/env python3
"""Render Markdown reports to styled HTML for client viewing.

Usage:
    python3 scripts/render-report.py drafts/seo/<artifact>.md
    # Output: drafts-preview/seo/<artifact>.html
"""
import markdown
from pathlib import Path
import sys


def render(md_path: Path, html_path: Path):
    md_text = md_path.read_text()
    html_body = markdown.markdown(md_text, extensions=["tables", "fenced_code"])

    styled = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>{md_path.stem} — GPC Development</title>
    <meta name="author" content="KlickSmartAI">
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
            max-width: 880px;
            margin: 40px auto;
            padding: 0 32px;
            line-height: 1.7;
            color: #1a1a1a;
            background: #fff;
        }}
        h1 {{
            border-bottom: 3px solid #0066cc;
            padding-bottom: 16px;
            color: #003d7a;
            font-size: 32px;
        }}
        h2 {{
            border-bottom: 1px solid #e5e5e5;
            padding-bottom: 10px;
            margin-top: 40px;
            color: #003d7a;
        }}
        h3 {{
            margin-top: 28px;
            color: #1a1a1a;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
            font-size: 14px;
        }}
        th, td {{
            padding: 10px 14px;
            border: 1px solid #d4d4d4;
            text-align: left;
        }}
        th {{ background: #f5f7fa; font-weight: 600; }}
        tr:nth-child(even) {{ background: #fafafa; }}
        code {{
            background: #f5f7fa;
            padding: 2px 6px;
            border-radius: 3px;
            font-size: 90%;
            font-family: 'SF Mono', Monaco, monospace;
        }}
        pre {{
            background: #f5f7fa;
            padding: 16px 20px;
            border-radius: 6px;
            overflow-x: auto;
            font-size: 13px;
            line-height: 1.5;
        }}
        blockquote {{
            border-left: 4px solid #0066cc;
            margin-left: 0;
            padding: 8px 16px;
            background: #f5f7fa;
            color: #003d7a;
        }}
        hr {{
            border: none;
            border-top: 1px solid #e5e5e5;
            margin: 32px 0;
        }}
        strong {{ color: #003d7a; }}
    </style>
</head>
<body>
{html_body}
</body>
</html>
"""
    html_path.write_text(styled)


if __name__ == "__main__":
    src = Path(sys.argv[1])
    # Convention: drafts/seo/*.md → drafts-preview/seo/*.html
    if "drafts/seo/" in str(src):
        dst = Path(str(src).replace("drafts/seo/", "drafts-preview/seo/")).with_suffix(".html")
    else:
        dst = src.with_suffix(".html")
    dst.parent.mkdir(parents=True, exist_ok=True)
    render(src, dst)
    print(f"✓ {src.name} → {dst}")
