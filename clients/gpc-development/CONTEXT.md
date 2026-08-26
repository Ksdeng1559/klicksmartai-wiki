# CONTEXT.md — GPC Development Workspace

This is **ICM Layer 1**. It defines the task routing table and the 5-stage
pipeline that turns a Dennis request into a validated deliverable.

## Task routing

When Dennis (or a subagent) asks for something, route by **verb**:

| If the request is... | Route to | First skill to invoke |
|---|---|---|
| "audit gpc" / "run a site audit" | `drafts/seo/audit-*.md` | `site-audit` |
| "find keywords for X" / "research X" | `drafts/seo/keywords-*.md` | `keyword-research` |
| "what does Google show for X" / "SERP X" | `drafts/seo/serp-*.md` | `serp-intelligence` |
| "what are people asking about X" | `drafts/seo/paa-*.md` | `paa-demand-mining` |
| "check gpc's backlinks" / "compare to X.com" | `drafts/seo/domain-*.md` | `domain-research` |
| "optimize the services page" / "score a page" | `drafts/seo/content-*.md` | `content-optimization` |
| "track gpc's positions" / "rank tracker" | `drafts/seo/rank-tracking-setup-*.md` | `rank-tracking` |
| "monthly report" / "ga4 numbers" | `drafts/seo/analytics-*.md` | `analytics-reporting` |
| "GBP health" / "local pack rank" | `drafts/seo/local-*.md` | `local-seo` |
| "export this" / "render HTML" / "promote to client" | `deliverables/seo/` | `openseo-data-export` |
| "new project" / "set up another client" | (off-workspace) | `icm-client-workspace-setup` |

## The 5-stage pipeline (Quick-mode)

Quick-mode means **virtual stages**, not physical folders. The pipeline is:

```
01_intake → 02_research → 03_draft → 04_review → 05_publish
   │            │             │          │           │
   │            │             │          │           └─► deliverables/seo/<artifact>.html
   │            │             │          └─► (Dennis reviews the draft)
   │            │             └─► drafts/seo/<artifact>.md  ← FIRST PASS
   │            └─► skill runs (paid credits)
   └─► skill runs (free, $0)
```

Each stage:

| # | Stage | Who runs it | Cost | Output |
|---|---|---|---|---|
| 01 | Intake | Agent | $0 | Confirm scope + project + market |
| 02 | Research | Skill (e.g. `keyword-research`) | varies | Data gathered |
| 03 | Draft | Skill (e.g. `site-audit`) | varies | `drafts/seo/<phase>-<date>-<topic>.md` |
| 04 | Review | Dennis | $0 | "approve" / "revise" / "kill" |
| 05 | Publish | `openseo-data-export` | $0 | `projects/seo/<artifact>.md` + `deliverables/seo/<artifact>.html` |

**Promotion happens at stage 5 only.** Stage 3 always lands in `drafts/seo/`.

## Quick-reference: skills available for GPC

All 12 SEO skills are bound (per `_config/deliverables.md`):

| Layer | Skill | State |
|---|---|---|
| Plan | `seo-enrichment-planner` | active (gate every spend) |
| Discover | `keyword-research` | active |
| Discover | `paa-demand-mining` | active |
| Discover | `serp-intelligence` | active |
| Discover | `domain-research` | active |
| Enrich | `content-optimization` | dormant (On-Page.ai key not configured) |
| Score | `site-audit` | active |
| Score | `rank-tracking` | active |
| Outreach | `analytics-reporting` | dormant (GA4 not connected for GPC) |
| Outreach | `local-seo` | active |
| Outreach | `openseo-data-export` | active |
| Cross | `openseo-project-intake` | already done — GPC is set up |

## Common workflows (worked examples)

### Example A: Dennis asks "audit gpc"

```
1. Read this CONTEXT.md → route to site-audit
2. Invoke seo-enrichment-planner → produce cost plan
3. Present cost plan to Dennis → wait for "yes"
4. On approval → invoke site-audit
5. Skill writes draft to drafts/seo/audit-<date>-gpc.md
6. Skill renders HTML preview to drafts-preview/seo/
7. Skill adds row to drafts/seo/VALIDATION_QUEUE.md
8. Skill reports back: "Audit complete. Draft at <path>. HTML preview at <path>. Awaiting your review."
```

### Example B: Dennis asks "promote the audit to a quote sheet"

```
1. Read this CONTEXT.md → already done; quote sheet exists at drafts/seo/audit-quote-2026-08-26-gpc-development.md
2. Verify with Dennis that the quote sheet is approved
3. On approval → invoke openseo-data-export → move to projects/seo/ + deliverables/seo/
4. Update VALIDATION_QUEUE.md status to "promoted"
```

### Example C: Dennis asks "track gpc's positions for our top 25 keywords"

```
1. Read this CONTEXT.md → route to rank-tracking
2. Invoke seo-enrichment-planner → produce cost plan (per-keyword monthly)
3. Present cost plan to Dennis → wait for "yes"
4. On approval → invoke rank-tracking
5. Skill creates tracker + adds 25 keywords
6. Skill writes draft setup report to drafts/seo/rank-tracking-setup-<date>.md
7. Skill reports back: "Tracker created. 25 keywords added. Awaiting your review."
```

## DuckDB queries (read-only path)

For analytical queries that don't need MCP round-trips, query the DuckDB mirror at `.local_tier/clients/gpc-development.duckdb`:

```sql
-- Top keywords by search volume
SELECT * FROM v_keyword_metrics_by_project WHERE project_id = '34afee19-d725-4073-b43f-1b76c6275c11' ORDER BY search_volume DESC LIMIT 25;

-- Recent audit issues
SELECT issue_type, severity, COUNT(*) AS cnt
FROM d1_raw.audit_issues
WHERE audit_id IN (SELECT id FROM d1_raw.audits WHERE project_id = '34afee19-d725-4073-b43f-1b76c6275c11')
GROUP BY issue_type, severity
ORDER BY cnt DESC;

-- PAA intent distribution
SELECT intent, COUNT(*) AS cnt FROM v_paa_demand_signals WHERE project_id = '34afee19-d725-4073-b43f-1b76c6275c11' GROUP BY intent ORDER BY cnt DESC;

-- Rank tracker status
SELECT * FROM v_rank_tracking_summary WHERE project_id = '34afee19-d725-4073-b43f-1b76c6275c11';
```

## See also

- `IDENTITY.md` — workspace map + rules
- `drafts/seo/VALIDATION_QUEUE.md` — what's currently pending review
- `~/.hermes/skills/seo-enrichment-planner/SKILL.md` — universal SEO orchestration
- `~/.hermes/skills/openseo-project-intake/SKILL.md` — already-completed onboarding
