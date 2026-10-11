---
title: "Status — Veritas Development OS (Frappe plan) — SUPERSEDED"
type: archive-status
archived: 2026-10-10
archived_by: agent:hermes
reason: Architecture pivot to Atomic CRM + Supabase (Notion ADR, approver Dennis Eng, 2026-10-08)
superseded_by:
  - notion_page: 3ec9e94c-f0a4-81e6-bca7-c8e6aaa2c375 (Veritas Capital Relationship OS — canonical CRM implementation source)
  - notion_page: 3c29e94c-f0a4-81b3-a32c-fb81ebf8094a (Veritas Development Intelligence OS — full architecture)
supersession_decision:
  source: Notion change log, 2026-10-08 entry
  approver: Dennis Eng
  summary: "Veritas runs as a second organization inside the shared Atomic CRM Supabase project, using Clerk Organizations. Build and test first in a separate staging Supabase project."
  change_log_sections: "6 (Required New Supabase Tables) and 17 (Compliance and Governance Guardrails) updated to reflect multi-tenant + ledger-computed totals + per-raise investor eligibility + declarative schema files."
related_wiki_drafts:
  - drafts/notion-sync-2026-10-10.md (delta report, 17,972 chars)
  - drafts/notion-mirror/capital-relationship-os-2026-10-08.md
  - drafts/notion-mirror/dev-os-architecture-2026-10-01.md
  - drafts/notion-mirror/real-estate-capital-os-pilot-2026-09-20.md
  - drafts/notion-mirror/investor-white-paper-2026-09-08.md
okf_version: "0.2"
---

# Status — Veritas Development OS (Frappe plan)

> **SUPERSEDED 2026-10-10.** The 5-phase Frappe/ERPNext build plan in `JOB.md` (Lovable v1 → Astro v2 → Vercel → Frappe POST) is **legacy architecture**. The new build plan is in Notion under `Veritas Capital Relationship OS` and `Veritas Development Intelligence OS`. Do not execute any of the Phase 0–4 steps in `JOB.md` against Frappe without re-approval from Dennis.

## What changed

| Aspect | Old (this file) | New (Notion) |
|---|---|---|
| Primary CRM | Frappe + ERPNext (Frappe Framework v14, Railway-hosted) | Atomic CRM + Supabase |
| Code repo | Astro v2 standalone (Vercel) | `Ksdeng1559/atomic-crm` fork |
| Multi-tenant | Single-tenant | Clerk Organizations (Veritas = second org) |
| Schema | Numbered migrations in `supabase/migrations/` | Declarative files in `supabase/schemas/` |
| Capital data | Capital Provider DocType in Frappe | 14 new Supabase tables in Atomic |
| Build order | Phase 0 → 4 (sequential) | Sprint 1 → 5 (Data → UI → Workflow → AI → Governance) |

## Why we kept this file

Per Dennis's standing rule (2026-08-29): never auto-delete superseded work. The Frappe plan is reference material for understanding what was considered before the Atomic CRM pivot. The new work in Notion supersedes it but does not erase it.

## Re-approval conditions

This plan may be re-elevated only if:

1. The Atomic CRM pilot on `Ksdeng1559/atomic-crm` fails the staging-Supabase isolation test
2. Securities counsel requires a Frappe-ERPNext back office for accounting/audit reasons
3. Dennis + David + Daniel explicitly re-approve Frappe in writing

None of these conditions are currently met.

## Next build plan (canonical)

- Source: Notion → `Veritas Capital Relationship OS` (page `3ec9e94c-f0a4-81e6-bca7-c8e6aaa2c375`)
- 5-sprint plan: Data Model → UI → Workflow → AI → Governance
- Tenant: Veritas runs as second org via Clerk Organizations
- Staging: separate staging Supabase project in new account
- This wiki's `drafts/notion-mirror/capital-relationship-os-2026-10-08.md` is a read-only reference copy.

## File location

- `JOB.md` (167 lines, 8,286 chars) preserved at this archive path
- `drafts/veritas-development-os/` directory removed (only JOB.md was in it)
- This STATUS file at `_archive/veritas-development-os-frappe-2026-08-29/STATUS.md`

---

*Authored by Hermes Agent, 2026-10-10. Source: Notion change log entry 2026-10-08.*
