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
