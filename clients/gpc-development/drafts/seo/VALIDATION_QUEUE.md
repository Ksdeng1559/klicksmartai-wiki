# VALIDATION_QUEUE.md — pending reviews

This is the source-of-truth gate ledger. Every artifact in `drafts/seo/` gets a row here. Dennis's "approve" / "revise" / "kill" response updates the row.

## Format

| File | Type | Cost | Status | Notes |
|---|---|---|---|---|

## Current queue

| File | Type | Cost | Status | Notes |
|---|---|---|---|---|
| `audit-quote-2026-08-26-gpc-development.md` | audit-quote | $0 (used existing audit data) | pending Dennis review | First-pass quote sheet for GPC. URL: `gpcdevelopment.ca`. 21 pages, 110 issues. Total quoted: $8,000 + $1,500/mo optional. |
| `audit-2026-08-26-gpc-development.md` | audit-page | $0 (used existing audit data) | pending Dennis review | Client-facing audit page (gatekept via `audit-page-gate` skill). 21 pages, 135 opportunities across 7 categories. Long-form (8.7 KB). No internal costs, no tool names, no Phase sequencing. |
| `audit-1page-2026-08-26-gpc-development.md` | audit-page-1p | $0 (used existing audit data) | pending Dennis review | **1-page visual** with score card (18/100), issue fingerprint radar, priority ladder, before/after impact bars, 4-step engagement timeline. **Supersedes** the long-form for first-touch. Companion stub to `drafts-preview/seo/audit-1page-2026-08-26-gpc-development.html`. 0 gate violations. |
| `CLIENT-SCORE-gpc-development-2026-08-28.md` | client-score | $0 (derived from existing audit + DuckDB keyword data) | promoted 2026-08-28 via openseo-data-export (HTML + 6 analyst views CSV exported) | **New deliverable type** (registered in `_config/deliverables.md`). 23/100 CONDITIONAL tier, 4-dim weighted scoring (tech 30 / content 18 / local 12 / SERP 28). ROI: $148K Yr-1 / $284K Yr-2 run-rate on $8K spend (18.5× / 35.5×). Companion to existing audit + quote. Requires new `deliverables/seo/` subfolder + render via `seo-audit-report` skill once approved. |
| `project-settings-2026-08-26-gpc-development.md` | project-settings | $0 (auto-generated from DuckDB mirror) | **ready to use** | Content brief: business context, writing preferences, keyword library, key pages, 29 competitors, rank tracker, SERP landscape, PAA findings, research log, recommended work order. Auto-regeneratable via `scripts/regenerate-project-settings.py` — cron `gpc-project-settings-refresh` (job_id `6e682fc4f022`) re-runs every 30 min. **Source of truth for content + SEO work.** |

## Regenerated 2026-08-26 14:35

All 3 drafts regenerated with **current live OpenSEO data** (audit `94478bde-5e6b-4376-8288-61c157eb830a`):

- 21 pages, 131 issues (was 110/135/134 from earlier audits — site unchanged)
- Issue categories: 7 (duplicate-meta-description 21, duplicate-title 21, missing-h1 21, no-outgoing-links 21, thin-content 21, orphan-page 20, slow-response 6)
- 0 critical issues
- GPC added 25 Vancouver buyer-intent keywords to rank tracker (weekly schedule, ~$0.50/mo)
- Saved keyword library grew from 83 → 120 (added 55 buyer-intent seeds)

Gate checks on regeneration: **0 violations** on all 3 drafts.

| File | Size | Word count | Format |
|---|---|---|---|
| `audit-1page-2026-08-26-gpc-development.md` (stub) | 2.0 KB | — | stub for HTML preview |
| `drafts-preview/seo/audit-1page-2026-08-26-gpc-development.html` | 23.2 KB | — | visual HTML |
| `audit-2026-08-26-gpc-development.md` | 8.6 KB | 1,395 | long-form Markdown |
| `drafts-preview/seo/audit-2026-08-26-gpc-development.html` | 10.9 KB | — | long-form HTML |
| `audit-quote-2026-08-26-gpc-development.md` | 5.9 KB | 936 | quote sheet |
| `drafts-preview/seo/audit-quote-2026-08-26-gpc-development.html` | 8.9 KB | — | quote HTML |

Ready for promotion to `projects/seo/` and `deliverables/seo/` once Dennis signs off.

## Status legend

| Status | Meaning |
|---|---|
| pending | Drafted, awaiting Dennis's first review |
| approved | Dennis signed off — promote via openseo-data-export |
| revised | Dennis asked for changes — agent updated the draft, awaiting re-review |
| killed | Dennis rejected — archived or deleted |
| promoted | Moved to `projects/seo/` + `deliverables/seo/` |

## Workflow

```
agent writes draft + adds row (status: pending)
  │
  ▼
Dennis reviews
  │
  ▼
approve → openseo-data-export → status: promoted
revise → agent updates → status: revised → back to Dennis
kill → agent archives → status: killed
```

## Per-row required fields

- **File** — relative to `drafts/seo/`
- **Type** — audit, audit-quote, paa, keywords, serp, domain, content, rank-tracking-setup, analytics, local, monthly-report, etc.
- **Cost** — total spend in credits / cash for this artifact
- **Status** — one of the values above
- **Notes** — what Dennis should focus on, what's actionable, any open questions
