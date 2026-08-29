# Deliverables — GPC Development

Vertical artifact map: what each deliverable type is, where it lives, and which
Hermes skill produces it.

## Active verticals

| Vertical | Status | Default skill |
|---|---|---|
| `seo` | active | varies by sub-phase (see table below) |

## SEO vertical — sub-phase binding

| Phase | Skill | Output format | Cost |
|---|---|---|---|
| Plan | `seo-enrichment-planner` | Markdown cost plan | $0 |
| Discover (PAA) | `paa-demand-mining` | Markdown + Markdown brief | ~$0.018/scan |
| Discover (keywords) | `keyword-research` | Markdown + CSV | ~96 cr/seed |
| Discover (SERP) | `serp-intelligence` | Markdown | ~30 cr/run |
| Discover (domain) | `domain-research` | Markdown | ~50 cr/domain |
| Enrich (content) | `content-optimization` | Markdown | dormant (no On-Page.ai key) |
| Score (audit) | `site-audit` | Markdown + HTML | ~$0.03/page |
| Score (client) | `seo-audit-report` | Markdown + HTML | $0 (derived from audit data) |
| Score (rank) | `rank-tracking` | Markdown + setup | per-kw/mo when activated |
| Outreach (analytics) | `analytics-reporting` | Markdown | dormant (no GA4) |
| Outreach (local) | `local-seo` | Markdown | mostly free + ~10-50 cr for paid lookups |
| Outreach (export) | `openseo-data-export` | HTML + CSV | $0 |

## Folder binding per phase

| Phase → Skill | First-pass output |
|---|---|
| Plan → `seo-enrichment-planner` | inline (no draft) — present cost plan in chat, await "yes" |
| Discover (PAA) → `paa-demand-mining` | `drafts/seo/paa-<date>-<topic>.md` |
| Discover (keywords) → `keyword-research` | `drafts/seo/keywords-<date>-<topic>.md` |
| Discover (SERP) → `serp-intelligence` | `drafts/seo/serp-<date>-<topic>.md` |
| Discover (domain) → `domain-research` | `drafts/seo/domain-<date>-<topic>.md` |
| Enrich → `content-optimization` | `drafts/seo/content-<date>-<url-slug>.md` |
| Score → `site-audit` | `drafts/seo/audit-<date>-<topic>.md` |
| Score → `seo-audit-report` (client score) | `drafts/seo/CLIENT-SCORE-<client-slug>-<date>.md` |
| Score → `rank-tracking` | `drafts/seo/rank-tracking-setup-<date>.md` |
| Outreach → `analytics-reporting` | `drafts/seo/analytics-<date>-<month>.md` |
| Outreach → `local-seo` | `drafts/seo/local-<date>-<business>.md` |
| Outreach → `openseo-data-export` | (runs on existing drafts — promotes to projects/ + deliverables/) |

## File format conventions

| Format | Used for | Tool |
|---|---|---|
| Markdown (.md) | Source-of-truth for every artifact (always) | skills write directly |
| HTML (.html) | Client-facing preview + final export | `scripts/render-report.py` (python-markdown) |
| CSV (.csv) | Bulk data exports (keywords, audits, ranks) | DuckDB `COPY TO` |
| PDF (.pdf) | Future — quote sheets, monthly reports | TBD (not in current stack) |

## Promotion workflow

```
drafts/seo/<artifact>.md     ← first pass (AI)
        │
        ▼ Dennis reviews
        │
drafts/seo/VALIDATION_QUEUE.md  ← "approved" row
        │
        ▼ invoke openseo-data-export
        │
projects/seo/<artifact>.md       ← source of truth (promoted)
deliverables/seo/<artifact>.html ← client-facing (rendered)
deliverables/seo/csv/<table>.csv ← optional data export
```

## No vertical subfolders needed

This client only has `seo` vertical. Subfolders (`drafts/seo/`, `projects/seo/`, etc.) are the only artifact folders. If a new vertical is added (e.g. `email` for outreach later), regenerate this file and add the subfolders.
