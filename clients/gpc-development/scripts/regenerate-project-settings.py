#!/usr/bin/env python3
"""
Generic project-settings regenerator — works for any client with an
OpenSEO project + DuckDB mirror.

Pulls project context (sections, custom sections, competitors, key pages,
research log), keyword library, rank tracker, and renders a structured
content brief as Markdown.

Usage:
    # Auto-discover from workspace path
    python3 scripts/regenerate-project-settings.py <workspace-dir>

    # Explicit project_id + workspace path
    python3 scripts/regenerate-project-settings.py <workspace-dir> <project-id>

    # With custom output
    python3 scripts/regenerate-project-settings.py <workspace-dir> <project-id> <output-path>

Examples:
    python3 scripts/regenerate-project-settings.py ~/wiki/clients/gpc-development/
    python3 scripts/regenerate-project-settings.py ~/wiki/clients/veritas-developments/ d506a90e-...
    python3 scripts/regenerate-project-settings.py ~/wiki/clients/gpc-development/ 34afee19... /tmp/brief.md

Auto-discovers:
- slug from workspace dir name (e.g. "gpc-development")
- project_id from CLAUDE.md or IDENTITY.md in workspace (looks for "project_id:" or "Project ID:")
- DuckDB mirror path from workspace's .local_tier/clients/<slug>.duckdb
"""

import sys
import re
import duckdb
from pathlib import Path
from datetime import datetime


def parse_args():
    """Parse CLI args: workspace_dir [project_id] [output_path]"""
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    workspace_dir = Path(sys.argv[1]).expanduser().resolve()
    if not workspace_dir.is_dir():
        print(f"ERROR: workspace dir not found: {workspace_dir}")
        sys.exit(1)

    project_id = sys.argv[2] if len(sys.argv) > 2 else None
    output_path = Path(sys.argv[3]).expanduser().resolve() if len(sys.argv) > 3 else None

    return workspace_dir, project_id, output_path


def slug_from_path(workspace_dir):
    """Extract slug from workspace dir name."""
    return workspace_dir.name


def duckdb_path_from_workspace(workspace_dir, slug):
    """Standard path: <workspace>/.local_tier/clients/<slug>.duckdb"""
    return workspace_dir / ".local_tier" / "clients" / f"{slug}.duckdb"


def discover_project_id(workspace_dir):
    """Try to find project_id in CLAUDE.md or IDENTITY.md."""
    for filename in ["CLAUDE.md", "IDENTITY.md"]:
        path = workspace_dir / filename
        if path.exists():
            content = path.read_text()
            # Look for "project_id:" or "Project ID:" followed by UUID
            match = re.search(
                r'(?:project_?id|project[_ ]ID)[:\s`]*([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})',
                content,
                re.IGNORECASE,
            )
            if match:
                return match.group(1)
            # Try a generic UUID match
            match = re.search(r'([a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})', content)
            if match:
                return match.group(1)
    return None


def fetch_context(con, project_id):
    """Pull all project context from DuckDB mirror."""
    sections = {}
    for r in con.execute("""
        SELECT key, title, content
        FROM gpc.project_context_sections
        WHERE project_id = ?
        ORDER BY key
    """, [project_id]).fetchall():
        key, title, content = r
        sections[key] = {"title": title, "content": content}

    competitors = []
    try:
        for r in con.execute("""
            SELECT domain, name, notes
            FROM gpc.project_competitors
            WHERE project_id = ?
            ORDER BY domain
        """, [project_id]).fetchall():
            competitors.append({"domain": r[0], "name": r[1], "notes": r[2]})
    except Exception:
        pass

    key_pages = []
    try:
        for r in con.execute("""
            SELECT role, url, topic, notes
            FROM gpc.project_key_pages
            WHERE project_id = ?
            ORDER BY role, url
        """, [project_id]).fetchall():
            key_pages.append({"role": r[0], "url": r[1], "topic": r[2], "notes": r[3]})
    except Exception:
        pass

    research_log = []
    try:
        for r in con.execute("""
            SELECT entry_date, created_by, summary
            FROM gpc.project_research_log
            WHERE project_id = ?
            ORDER BY created_at DESC
        """, [project_id]).fetchall():
            research_log.append({"date": r[0], "by": r[1], "summary": r[2]})
    except Exception:
        pass

    return sections, competitors, key_pages, research_log


def fetch_keyword_library(con):
    """Pull keyword library snapshot from DuckDB mirror."""
    counts = {}
    for table in ["saved_keywords", "keyword_metrics", "audits", "paa_scans",
                  "rank_tracking_configs", "rank_tracking_keywords"]:
        try:
            n = con.execute(f"SELECT COUNT(*) FROM gpc.{table}").fetchone()[0]
            counts[table] = n
        except Exception:
            counts[table] = 0

    # Top 15 keywords by volume
    top_kw = []
    try:
        for r in con.execute("""
            SELECT keyword, search_volume, keyword_difficulty, cpc, intent
            FROM gpc.v_keyword_metrics_by_project
            WHERE search_volume IS NOT NULL
            ORDER BY search_volume DESC
            LIMIT 15
        """).fetchall():
            top_kw.append({
                "keyword": r[0], "volume": r[1], "kd": r[2], "cpc": r[3], "intent": r[4]
            })
    except Exception:
        pass

    return counts, top_kw


def fetch_rank_tracker(con):
    """Pull rank tracker keywords."""
    try:
        kw = con.execute("""
            SELECT keyword FROM gpc.rank_tracking_keywords ORDER BY keyword
        """).fetchall()
        return [r[0] for r in kw]
    except Exception:
        return []


def render_brief(slug, project_id, sections, competitors, key_pages, research_log,
                 counts, top_kw, rank_tracker, duckdb_path):
    """Render the content brief as Markdown."""
    date = datetime.now().strftime("%Y-%m-%d")
    section_labels = {
        "business_overview": "### Business overview",
        "current_goal": "### Current goal (organic)",
        "positioning": "### Positioning",
        "custom:brand-voice": "### Brand voice & audience",
        "custom:market": "### Market & competition",
        "custom:technical-seo": "### Technical SEO baseline (CRITICAL)",
    }

    md = f"""# {slug} — Project Settings & Content Brief

**Source:** OpenSEO D1 → DuckDB mirror (synced via `openseo-duckdb-sync` cron, every 30 min)
**Project ID:** `{project_id}`
**DuckDB mirror:** `{duckdb_path}`
**Last refreshed:** {date}
**Audience for this brief:** Internal (Dennis / KlickSmartAI content team)
**Purpose:** Single source of truth for content + SEO work.

---

## Part 1 — Business context

"""
    for key in ["business_overview", "current_goal", "positioning", "custom:brand-voice", "custom:market", "custom:technical-seo"]:
        if key in sections:
            label = section_labels.get(key, f"### {key}")
            md += f"{label}\n\n> {sections[key]['content'].strip()}\n\n"

    md += """---

## Part 2 — Writing preferences & keyword strategy

"""
    if "writing_preferences" in sections:
        md += f"> {sections['writing_preferences']['content'].strip()}\n\n"

    md += f"""---

## Part 3 — Keyword library snapshot

| Dimension | Live count |
|---|---|
| Saved keywords (library) | {counts.get('saved_keywords', 0)} |
| With hydrated metrics | {counts.get('keyword_metrics', 0)} |
| Audits | {counts.get('audits', 0)} |
| PAA scans | {counts.get('paa_scans', 0)} |
| Rank tracker keywords | {counts.get('rank_tracking_keywords', 0)} |

### Top performing keywords (by volume)

| Keyword | Vol/mo | KD | CPC | Intent |
|---|---|---|---|---|
"""
    for k in top_kw:
        vol = k["volume"] if k["volume"] is not None else "—"
        kd = k["kd"] if k["kd"] is not None else "—"
        cpc = k["cpc"] if k["cpc"] is not None else "—"
        intent = k["intent"] or "—"
        md += f"| {k['keyword']} | {vol} | {kd} | {cpc} | {intent} |\n"

    if rank_tracker:
        md += f"\n### Rank tracker ({len(rank_tracker)} keywords, weekly schedule)\n\n"
        for k in rank_tracker:
            md += f"- {k}\n"

    md += "\n---\n\n## Part 4 — Key pages (site architecture)\n\n"
    by_role = {}
    for p in key_pages:
        by_role.setdefault(p["role"], []).append(p)
    for role in ["hub", "money", "spoke", "other"]:
        if role in by_role:
            md += f"### {role.capitalize()} pages ({len(by_role[role])})\n\n"
            md += "| URL | Topic | Notes |\n|---|---|---|\n"
            for p in by_role[role]:
                topic = p["topic"] or "—"
                notes = (p["notes"] or "")[:200].replace("|", "\\|")
                md += f"| {p['url']} | {topic} | {notes} |\n"
            md += "\n"

    md += "\n---\n\n## Part 5 — Competitors\n\n"
    for c in competitors:
        md += f"### {c['domain']}\n\n"
        if c["name"]:
            md += f"**Name:** {c['name']}\n\n"
        if c["notes"]:
            md += f"> {c['notes']}\n\n"

    md += "\n---\n\n## Part 6 — Research log (chronological)\n\n"
    md += "| Date | Author | Summary |\n|---|---|---|\n"
    for entry in research_log:
        summary = (entry["summary"] or "")[:200].replace("|", "\\|").replace("\n", " ")
        md += f"| {entry['date']} | {entry['by']} | {summary} |\n"

    md += """

---

## Part 7 — Live snapshot in OpenSEO (D1)

A compact version of this brief may also be stored as a **custom section** in OpenSEO D1 (`custom:content-brief`, ~3 KB).

Query it via MCP:
```python
mcp.call("get_project_context", {"projectId": "<project_id>"})
# → .customSections → slug: "content-brief"
```

Or via DuckDB mirror:
```sql
SELECT content FROM gpc.project_context_sections WHERE key = 'custom:content-brief';
```

---

## Part 8 — How to regenerate

```bash
# Generic — works for any client with workspace + DuckDB mirror
python3 scripts/regenerate-project-settings.py ~/wiki/clients/<slug>/

# Explicit project_id (skip auto-discovery)
python3 scripts/regenerate-project-settings.py ~/wiki/clients/<slug>/ <project-id>

# Custom output path
python3 scripts/regenerate-project-settings.py ~/wiki/clients/<slug>/ <project-id> /tmp/brief.md
```

---

*Auto-generated from OpenSEO D1 → DuckDB mirror.*
"""

    return md


def main():
    workspace_dir, project_id, output_path = parse_args()
    slug = slug_from_path(workspace_dir)
    duckdb_path = duckdb_path_from_workspace(workspace_dir, slug)

    print(f"Workspace: {workspace_dir}")
    print(f"Slug: {slug}")
    print(f"DuckDB mirror: {duckdb_path}")

    if not duckdb_path.exists():
        print(f"\nERROR: DuckDB mirror not found at {duckdb_path}")
        print(f"Run scripts/sync-{slug}-duckdb.py first to populate it.")
        sys.exit(1)

    if not project_id:
        project_id = discover_project_id(workspace_dir)
        if not project_id:
            print(f"\nERROR: could not auto-discover project_id.")
            print(f"  Pass it explicitly: python3 regenerate-project-settings.py <workspace> <project_id>")
            print(f"  Or add 'project_id: <uuid>' to CLAUDE.md or IDENTITY.md.")
            sys.exit(1)
        print(f"Project ID (auto-discovered): {project_id}")
    else:
        print(f"Project ID (passed): {project_id}")

    if not output_path:
        date = datetime.now().strftime("%Y-%m-%d")
        output_path = workspace_dir / "drafts" / "seo" / f"project-settings-{date}-{slug}.md"
        print(f"Output path (auto): {output_path}")
    else:
        print(f"Output path (passed): {output_path}")

    print(f"\nOpening DuckDB...")
    con = duckdb.connect(str(duckdb_path), read_only=True)

    print("Pulling project context...")
    sections, competitors, key_pages, research_log = fetch_context(con, project_id)

    print("Pulling keyword library...")
    counts, top_kw = fetch_keyword_library(con)

    print("Pulling rank tracker keywords...")
    rank_tracker = fetch_rank_tracker(con)

    con.close()

    print("Rendering brief...")
    md = render_brief(slug, project_id, sections, competitors, key_pages, research_log,
                     counts, top_kw, rank_tracker, duckdb_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(md)

    print(f"\n✓ Written: {output_path}")
    print(f"  size: {output_path.stat().st_size:,} bytes")
    print(f"  sections: {len(sections)}")
    print(f"  competitors: {len(competitors)}")
    print(f"  key pages: {len(key_pages)}")
    print(f"  research log entries: {len(research_log)}")
    print(f"  saved keywords: {counts.get('saved_keywords', 0)}")
    print(f"  rank tracker keywords: {counts.get('rank_tracking_keywords', 0)}")


if __name__ == "__main__":
    main()
