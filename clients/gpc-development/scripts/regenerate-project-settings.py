#!/usr/bin/env python3
"""
GPC Development — Project Settings Brief Regenerator

Pulls all project context, competitors, key pages, keyword library, SERP,
PAA, and research log from OpenSEO D1 (via DuckDB mirror) and regenerates
the project-settings-YYYY-MM-DD-gpc-development.md content brief.

Usage:
    python3 scripts/regenerate-project-settings.py [output-path]

If no path is given, writes to:
    drafts/seo/project-settings-YYYY-MM-DD-gpc-development.md
"""

import sys
import duckdb
from pathlib import Path
from datetime import datetime


PROJECT_ID = "34afee19-d725-4073-b43f-1b76c6275c11"
DUCKDB_PATH = "/home/denni/wiki/clients/gpc-development/.local_tier/clients/gpc-development.duckdb"


def fetch_context(con):
    """Pull all project context from DuckDB mirror."""
    sections = {}
    for r in con.execute("""
        SELECT key, title, content
        FROM gpc.project_context_sections
        WHERE project_id = ?
        ORDER BY key
    """, [PROJECT_ID]).fetchall():
        key, title, content = r
        sections[key] = {"title": title, "content": content}

    competitors = []
    for r in con.execute("""
        SELECT domain, name, notes
        FROM gpc.project_competitors
        WHERE project_id = ?
        ORDER BY domain
    """, [PROJECT_ID]).fetchall():
        competitors.append({"domain": r[0], "name": r[1], "notes": r[2]})

    key_pages = []
    for r in con.execute("""
        SELECT role, url, topic, notes
        FROM gpc.project_key_pages
        WHERE project_id = ?
        ORDER BY role, url
    """, [PROJECT_ID]).fetchall():
        key_pages.append({"role": r[0], "url": r[1], "topic": r[2], "notes": r[3]})

    research_log = []
    for r in con.execute("""
        SELECT entry_date, created_by, summary
        FROM gpc.project_research_log
        WHERE project_id = ?
        ORDER BY created_at DESC
    """, [PROJECT_ID]).fetchall():
        research_log.append({"date": r[0], "by": r[1], "summary": r[2]})

    return sections, competitors, key_pages, research_log


def fetch_keyword_library(con):
    """Pull keyword library snapshot."""
    total_saved = con.execute("""
        SELECT COUNT(*) FROM gpc.saved_keywords
    """).fetchone()[0]

    total_metrics = con.execute("""
        SELECT COUNT(*) FROM gpc.keyword_metrics
    """).fetchone()[0]

    rank_tracker = con.execute("""
        SELECT COUNT(*) FROM gpc.rank_tracking_keywords
    """).fetchone()[0]

    paa_count = con.execute("""
        SELECT COUNT(*) FROM gpc.paa_scans
    """).fetchone()[0]

    # Top 10 keywords by volume (joined view)
    try:
        top_kw = con.execute("""
            SELECT keyword, search_volume, keyword_difficulty, cpc, intent
            FROM gpc.v_keyword_metrics_by_project
            WHERE search_volume IS NOT NULL
            ORDER BY search_volume DESC
            LIMIT 15
        """).fetchall()
    except Exception:
        top_kw = []

    return {
        "total_saved": total_saved,
        "total_metrics": total_metrics,
        "rank_tracker": rank_tracker,
        "paa_count": paa_count,
        "top_keywords": [
            {"keyword": r[0], "volume": r[1], "kd": r[2], "cpc": r[3], "intent": r[4]}
            for r in top_kw
        ],
    }


def fetch_rank_tracker(con):
    """Pull rank tracker keywords."""
    try:
        kw = con.execute("""
            SELECT keyword FROM gpc.rank_tracking_keywords ORDER BY keyword
        """).fetchall()
        return [r[0] for r in kw]
    except Exception:
        return []


def render_brief(sections, competitors, key_pages, research_log, kw_lib, rank_tracker):
    """Render the content brief as Markdown."""
    date = datetime.now().strftime("%Y-%m-%d")
    md = f"""# GPC Development — Project Settings & Content Brief

**Source:** OpenSEO D1 → DuckDB mirror (synced via `openseo-duckdb-sync` cron, every 30 min)
**Project ID:** `{PROJECT_ID}`
**Last refreshed:** {date}
**Audience for this brief:** Internal (Dennis / KlickSmartAI content team)
**Purpose:** Single source of truth for content + SEO work.

---

## Part 1 — Business context

"""
    # Add each section
    section_labels = {
        "business_overview": "### Business overview",
        "current_goal": "### Current goal (organic)",
        "positioning": "### Positioning",
        "custom:brand-voice": "### Brand voice & audience",
        "custom:market": "### Market & competition",
        "custom:technical-seo": "### Technical SEO baseline (CRITICAL)",
    }

    for key in ["business_overview", "current_goal", "positioning", "custom:brand-voice", "custom:market", "custom:technical-seo"]:
        if key in sections:
            label = section_labels.get(key, f"### {key}")
            md += f"{label}\n\n> {sections[key]['content'].strip()}\n\n"

    md += """---

## Part 2 — Writing preferences & keyword strategy

"""
    if "writing_preferences" in sections:
        md += f"> {sections['writing_preferences']['content'].strip()}\n\n"

    # Keyword library snapshot
    md += f"""---

## Part 3 — Keyword library snapshot

| Dimension | Live count |
|---|---|
| Saved keywords (library) | {kw_lib['total_saved']} |
| With hydrated metrics | {kw_lib['total_metrics']} |
| Rank tracker keywords | {kw_lib['rank_tracker']} |
| PAA scans | {kw_lib['paa_count']} |

### Top performing keywords (by volume)

| Keyword | Vol/mo | KD | CPC | Intent |
|---|---|---|---|---|
"""
    for k in kw_lib["top_keywords"]:
        vol = k["volume"] if k["volume"] is not None else "—"
        kd = k["kd"] if k["kd"] is not None else "—"
        cpc = k["cpc"] if k["cpc"] is not None else "—"
        intent = k["intent"] or "—"
        md += f"| {k['keyword']} | {vol} | {kd} | {cpc} | {intent} |\n"

    if rank_tracker:
        md += f"\n### Rank tracker ({len(rank_tracker)} keywords, weekly schedule)\n\n"
        for k in rank_tracker:
            md += f"- {k}\n"

    # Key pages
    md += "\n---\n\n## Part 4 — Key pages (site architecture)\n\n"
    by_role = {}
    for p in key_pages:
        by_role.setdefault(p["role"], []).append(p)
    for role in ["hub", "money", "spoke"]:
        if role in by_role:
            md += f"### {role.capitalize()} pages ({len(by_role[role])})\n\n"
            md += "| URL | Topic | Notes |\n|---|---|---|\n"
            for p in by_role[role]:
                topic = p["topic"] or "—"
                notes = (p["notes"] or "")[:200].replace("|", "\\|")
                md += f"| {p['url']} | {topic} | {notes} |\n"
            md += "\n"

    # Competitors
    md += "\n---\n\n## Part 5 — Competitors\n\n"
    for c in competitors:
        md += f"### {c['domain']}\n\n"
        if c["name"]:
            md += f"**Name:** {c['name']}\n\n"
        if c["notes"]:
            md += f"> {c['notes']}\n\n"

    # Research log
    md += "\n---\n\n## Part 6 — Research log (chronological)\n\n"
    md += "| Date | Author | Summary |\n|---|---|---|\n"
    for entry in research_log:
        summary = (entry["summary"] or "")[:200].replace("|", "\\|").replace("\n", " ")
        md += f"| {entry['date']} | {entry['by']} | {summary} |\n"

    md += """

---

## Part 7.5 — Live snapshot in OpenSEO (D1)

A compact version of this brief is also stored as a **custom section** in OpenSEO D1 (`custom:content-brief`, ~3 KB).

Query it via MCP:
```python
mcp.call("get_project_context", {"projectId": "34afee19-d725-4073-b43f-1b76c6275c11"})
# → .customSections → slug: "content-brief" → title: "Content brief (live snapshot)"
```

Or via DuckDB mirror:
```sql
SELECT content FROM gpc.project_context_sections WHERE key = 'custom:content-brief';
```

The full brief (this file, ~12 KB) lives in the client workspace. The compact version (in OpenSEO D1) is what SAM, the app, and other agents read.

---

## When to regenerate this brief

- After any new project onboarding (project_context_sections, project_key_pages)
- After competitor discovery (project_competitors)
- After positioning shifts (project_context_sections.positioning)
- After keyword library changes (saved_keywords, keyword_metrics)
- After SERP analysis (get_serp_results data)
- After PAA scans (paa_scans)

## How to regenerate

```bash
python3 scripts/regenerate-project-settings.py
# Or with custom output path:
python3 scripts/regenerate-project-settings.py drafts/seo/project-settings-2026-08-30-gpc-development.md
```

*Auto-generated from OpenSEO D1 → DuckDB mirror.*
"""

    return md


def main():
    output_path = None
    if len(sys.argv) > 1:
        output_path = Path(sys.argv[1])
    else:
        today = datetime.now().strftime("%Y-%m-%d")
        output_path = Path(f"/home/denni/wiki/clients/gpc-development/drafts/seo/project-settings-{today}-gpc-development.md")

    print(f"Opening DuckDB: {DUCKDB_PATH}")
    con = duckdb.connect(DUCKDB_PATH, read_only=True)

    print("Pulling project context...")
    sections, competitors, key_pages, research_log = fetch_context(con)

    print("Pulling keyword library...")
    kw_lib = fetch_keyword_library(con)

    print("Pulling rank tracker keywords...")
    rank_tracker = fetch_rank_tracker(con)

    con.close()

    print(f"Rendering brief...")
    md = render_brief(sections, competitors, key_pages, research_log, kw_lib, rank_tracker)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(md)

    print(f"\n✓ Written: {output_path}")
    print(f"  size: {output_path.stat().st_size:,} bytes")
    print(f"  sections: {len(sections)}")
    print(f"  competitors: {len(competitors)}")
    print(f"  key pages: {len(key_pages)}")
    print(f"  research log entries: {len(research_log)}")
    print(f"  saved keywords: {kw_lib['total_saved']}")
    print(f"  rank tracker keywords: {kw_lib['rank_tracker']}")


if __name__ == "__main__":
    main()
