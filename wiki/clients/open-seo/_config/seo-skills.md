# OpenSEO — SEO Skill Bindings

This client has **all 14 SEO skills** bound by default. Per-client overrides documented below.

## Bound skills (full catalog)

| Layer | Skill | Status |
|---|---|---|
| 1. Plan | `seo-enrichment-planner` | ✅ bound |
| 2. Discover | `keyword-research` | ✅ bound |
| 2. Discover | `paa-demand-mining` | ✅ bound (flagship use-case) |
| 2. Discover | `serp-intelligence` | ✅ bound |
| 2. Discover | `domain-research` | ✅ bound |
| 3. Enrich | `content-optimization` | ⏸️ dormant (On-Page.ai key empty — skill reports "module dormant") |
| 3. Enrich | `openseo-keyword-library` | ✅ bound |
| 4. Score | `site-audit` | ✅ bound |
| 4. Score | `rank-tracking` | ✅ bound |
| 5. Outreach | `analytics-reporting` | ⏸️ partial (GSC + GA4 require OAuth setup per project) |
| 5. Outreach | `local-seo` | ✅ bound |
| Cross | `openseo-project-intake` | ✅ bound |
| Cross | `openseo-data-export` | ✅ bound |

## Universal HITL gate

Per the catalog, every skill below Layer 1 must present:

```
## Assumptions
- <3-5 bullets>
## Cost Estimate
<markdown table>
## Spend Cap
- max spend: <cap>
## Approval Question
Approve full run? (yes / no / adjust)
```

…and wait for explicit "yes" before spending any credit.

## Module dormancy rules

- `content-optimization` — when `ONPAGE_API_KEY` is empty, the skill reports "On-Page.ai module dormant — content scan disabled" rather than silently failing. The UI sidebar item stays hidden; MCP tool returns `{error: "module disabled"}`.
- `analytics-reporting` — Google Search Console + GA4 require OAuth per project. Without connection, the skill reports "GSC not connected for this project — analytics features disabled".
- `local-seo` — always available, no setup.
- `rank-tracking` — always available, charged per-keyword monthly.

## Per-client overrides

This client is **technical/infra** (the engagement is *building* OpenSEO itself). For real client engagements, the binding changes:

| Client type | Bind | Skip |
|---|---|---|
| **Local business (Veritas, etc.)** | `local-seo`, `rank-tracking`, `site-audit`, `analytics-reporting`, `domain-research` | `paa-demand-mining` (low-intent for LBs) |
| **National SaaS (TBD)** | `keyword-research`, `paa-demand-mining`, `content-optimization`, `rank-tracking`, `analytics-reporting` | `local-seo` |
| **E-commerce** | `keyword-research`, `serp-intelligence`, `content-optimization`, `site-audit`, `analytics-reporting`, `rank-tracking` | `local-seo` |
| **Investor-facing site (Spectra, Veritas)** | `paa-demand-mining`, `content-optimization`, `rank-tracking`, `analytics-reporting` | `local-seo`, `serp-intelligence` |

## Files

- Skill catalog: `_config/seo-skill-catalog.md`
- Live data source: `http://127.0.0.1:3005/mcp` (50 tools)
- DuckDB mirror: `.local_tier/clients/open-seo.duckdb` (8.5MB, refreshed every 30 min)
- Workflow pattern: `seo-enrichment-planner` (the gate skill)