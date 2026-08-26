# SEO Skill Catalog

Per-client skill catalog for any OpenSEO-backed engagement. Skills follow the same **5-layer Plan → Discover → Enrich → Score → Outreach** pattern as the GTM enrichment stack, with HITL gates between layers and credit-cost estimates before any spend.

## When to use

- A new client engagement is set up via `icm-client-workspace-setup` and needs SEO deliverable skills
- A user says "build the SEO skill catalog", "what can we do with OpenSEO", or "set up SEO skills for <client>"
- A client already has OpenSEO running but no SEO skill layer wired

## The principle (insight-first)

SEO tools are **spend-controlled**. Most of OpenSEO's 50 MCP tools cost real money:

| Provider | Cost | Where |
|---|---|---|
| DataForSEO | ~96 credits per keyword seed | keyword research, SERP, backlinks, search volume |
| Serper.dev | ~$0.018 per PAA scan | PAA + social mining |
| On-Page.ai | per-URL content optimization | content optimization |
| Rank Tracker | per-keyword/month | position tracking |
| Site Audit | ~$0.03/page | technical SEO audit |

A skill that doesn't surface cost BEFORE spending is a credit leak. **Every skill in this catalog must include a Phase 0 cost estimate + HITL approval gate.**

## Skill catalog (14 skills, 5 layers)

### Layer 1 — Plan (cost + scope confirmation)

| Skill | Purpose | Tools |
|---|---|---|
| `seo-enrichment-planner` | Plan cost + scope + ICP for any SEO task before spend | `whoami`, `list_projects`, `estimate_rank_tracker_cost` |

**Always start here.** No skill below runs without a cost estimate agreed.

### Layer 2 — Discover (keyword universe)

| Skill | Purpose | Tools |
|---|---|---|
| `keyword-research` | Build keyword universe from 1-5 seeds | `research_keywords`, `find_serp_competitors`, `get_domain_keyword_suggestions` |
| `paa-demand-mining` | Mine People Also Ask + social threads (the "demand discovery" mode) | `run_paa_mining`, `get_paa_scan` |
| `serp-intelligence` | Inspect live SERPs for 1-10 keywords, find intent gaps | `get_serp_results`, `get_local_serp_results`, `get_local_rank_grid` |
| `domain-research` | Competitor + own-domain organic footprint | `get_domain_overview`, `get_ranked_keywords`, `get_backlinks_overview`, `get_backlinks_profile` |

### Layer 3 — Enrich (deep data)

| Skill | Purpose | Tools |
|---|---|---|
| `content-optimization` | Score + improve a page for a target keyword (On-Page.ai) | `run_content_scan`, `get_content_scan`, `inspect_urls` |
| `keyword-library` | Save + hydrate keyword store | `save_keywords`, `list_saved_keywords`, `get_keyword_metrics` |

### Layer 4 — Score (technical + position)

| Skill | Purpose | Tools |
|---|---|---|
| `site-audit` | Crawl + prioritize technical SEO issues | `run_site_audit`, `get_audit_status`, `get_audit_issues`, `get_audit_pages` |
| `rank-tracking` | Track positions over time | `create_rank_tracker`, `add_rank_tracking_keywords`, `run_rank_tracker`, `get_rank_tracker`, `remove_rank_tracking_keywords` |

### Layer 5 — Outreach (report + distribute)

| Skill | Purpose | Tools |
|---|---|---|
| `analytics-reporting` | Pull GA4 + Search Console performance, find opportunities | `get_search_console_performance`, `get_google_analytics_*` (8 tools), `get_search_opportunities` |
| `local-seo` | Google Business Profile + Local SERP for SMB clients | `get_business_profile`, `get_business_reviews`, `get_business_questions`, `get_business_updates`, `search_local_businesses`, `list_business_categories` |

### Cross-cutting (work in any layer)

| Skill | Purpose | Tools |
|---|---|---|
| `openseo-project-intake` | Set up project + shared memory | `create_project`, `get_project_context`, `update_project_context` |
| `openseo-data-export` | Export OpenSEO data to DuckDB mirror for OLAP | (read-only operations on `d1_raw` schema) |

## Stack-walk rules (same as GTM)

1. **Always start at Layer 1 (Plan)**. No Discover/Enrich/Score/Outreach skill runs without the cost estimate + scope agreed.
2. **HITL gates between layers.** Phase 3 approval format applies at every boundary.
3. **Cost plan with a range, not a point.** e.g. "5-8 cr" not "6 cr". Include a **spend cap** explicitly.
4. **Phase the budget when scope exceeds balance.** Don't abort — phase.
5. **Discover before Enrich.** A keyword universe that starts with content-optimization scans wastes money on pages for keywords you haven't qualified yet.
6. **Module dormancy.** If a module's API key is missing, the corresponding skill reports "module dormant" — don't pretend to work.

## Worked example — Veritas (existing client, retrofit to SEO)

Veritas has GTM skills (signal-based outbound, cold outreach, etc.) — adding SEO is the second functional area.

| Layer | Veritas-relevant skill | Why |
|---|---|---|
| 1. Plan | `seo-enrichment-planner` | Cost per keyword research / rank tracker / audit |
| 2. Discover | `paa-demand-mining` | "What are developers asking about CDFIs, multifamily, KC development?" |
| 2. Discover | `keyword-research` | Build keyword universe for Jackson County + KC real-estate terms |
| 3. Enrich | `content-optimization` | Optimize each verified landing page for target keyword |
| 4. Score | `site-audit` | Crawl `veritasdevelopments.com` for technical issues |
| 4. Score | `rank-tracking` | Track 50-100 Jackson County / KC real-estate keywords monthly |
| 5. Outreach | `analytics-reporting` | GA4 + Search Console performance report for landing pages |
| Cross-cutting | `openseo-project-intake` | Create `veritas-developments` project, write context |
| Cross-cutting | `openseo-data-export` | Sync to `clients/veritas-developments/.local_tier/clients/veritas.duckdb` |

## How to add these to a client workspace

For each new client engagement:

1. **Scaffold the client workspace** with `icm-client-workspace-setup` (already creates `_config/` + `projects/`, `drafts/`, etc.).
2. **Create a `projects/seo/`** subdirectory (per the vertical map convention).
3. **Bind the relevant skills** to `clients/<slug>/_config/seo-skills.md` (mirroring `_config/gtm-skills.md`).
4. **Wire `openseo` MCP server** in the user's `~/.hermes/config.yaml`:
   ```yaml
   mcp_servers:
     openseo:
       command: /mnt/c/Windows/system32/cmd.exe
       args: [/c, npx.cmd -y mcp-remote http://127.0.0.1:3005/mcp]
   ```
5. **Set up the DuckDB mirror** by adapting `scripts/sync-openseo-duckdb.py` for the client slug.
6. **Run `openseo-project-intake`** to create the project in OpenSEO's D1 with the right context.

## Files

- This doc: `/home/denni/wiki/clients/open-seo/_config/seo-skill-catalog.md`
- Reference implementation: `/home/denni/wiki/hermes/skills/seo/` (each skill will be a subfolder here)

## What this is NOT

- Not a checklist of OpenSEO features — that's the docs.
- Not a copy of GTM skills — different tools, different costs, but same shape.
- Not a replacement for the existing `seo-audit` skill — this is a per-client binding layer; the seo-audit skill (in `~/.hermes/skills/`) is one of many skills the catalog references.