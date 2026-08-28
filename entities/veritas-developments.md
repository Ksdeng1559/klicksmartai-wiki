---
title: Veritas Developments
type: entity
created: 2026-08-28
updated: 2026-08-28
tags: [company, real-estate, klicksmartai-client, missouri, jackson-county]
related:
  - clients/veritas-developments/IDENTITY.md
  - veritas-growth-program-pilot
status: active
client_slug: veritas-developments
---

# Veritas Developments

**Corporate:** Veritas Development Group LLC
**Web:** veritasdevelopmentgroupllc.com
**Location:** Jackson County, Missouri (Kansas City metro)
**Workspace:** `~/wiki/clients/veritas-developments/`
**DuckDB canonical store:** `~/wiki/clients/veritas-developments/.local_tier/clients/veritas-developments.duckdb` (v1.1.0)

## Contacts

- **David Poole** — Managing Partner (decision authority: final, status: awaiting-reply)
  - Owns web fix priority + client-engagement signoff. Primary decision authority.
- **Daniel Bailey** — CFO (decision authority: consult, status: awaiting-reply)
  - Co-approver on engagement quote. Compliance-side review.

## Active Engagement

Deal-loan structure, investor flywheel (webinars), and CRM build. See
[veritas-growth-program-pilot](veritas-growth-program-pilot.md) for the
5-pillar content program foundation.

## Released Deliverables (2026-08-28 SEO audit cycle)

- [audit-audit-v4-2026-08-28](audit-audit-v4-2026-08-28.md) — **SEO Audit — veritasdevelopmentgroupllc.com (v4)** · 3816 words · released 2026-08-28 · by hermes
- [audit-client-score-2026-08-28](audit-client-score-2026-08-28.md) — **Client Score — Veritas Development Group LLC** · 1490 words · released 2026-08-28 · by hermes
- [audit-cover-memo-v4-2026-08-28](audit-cover-memo-v4-2026-08-28.md) — **Cover Note — SEO Audit v4** · 1043 words · released 2026-08-28 · by hermes

## Workspace Architecture

The Veritas workspace is the **pilot implementation** of KlickSmartAI's
multi-agent client-workspace pattern:

- **Canonical source of truth:** the `.duckdb` file (not the markdown files)
- **Markdown deliverables:** derived output, regenerable from the DB
- **Multi-agent safe:** every row carries `created_by`; writes go through
  the protocol in `~/wiki/_internal/agent-duckdb-protocol.md`
- **Migration-ready:** schema is MotherDuck-compatible; specific tables can
  sync to Supabase Postgres later if needed

Phase A implementation complete (2026-08-28): schema v1.1.0 with 8 workspace
tables + 3 views + 11 audit events. Phase C is the publish pipeline — this
page is the first deliverable published through it.

## Related

- [veritas-growth-program-pilot](veritas-growth-program-pilot.md) — content program foundation
- [klicksmartai](klicksmartai.md) — system owner
- [dennis-eng](dennis-eng.md) — engagement lead
