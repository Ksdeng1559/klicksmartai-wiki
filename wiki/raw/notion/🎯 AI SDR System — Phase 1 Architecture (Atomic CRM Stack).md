---
title: "🎯 AI SDR System — Phase 1 Architecture (Atomic CRM Stack)"
created: 2026-09-07
updated: 2026-09-07
type: process
status: active
source: notion
notion_id: 3a19e94cf0a481488e61e42c6b2c88b3
notion_url: https://app.notion.com/p/3a19e94cf0a481488e61e42c6b2c88b3?pvs=204
tags: [sop, notion-mirror]
sources: [notion: 🎯 AI SDR System — Phase 1 Architecture (Atomic CRM Stack)]
---

# 🎯 AI SDR System — Phase 1 Architecture (Atomic CRM Stack)

> Mirrored from Notion page `3a19e94cf0a481488e61e42c6b2c88b3` on 2026-09-07. Source: https://app.notion.com/p/3a19e94cf0a481488e61e42c6b2c88b3?pvs=204

{"type":"emoji","emoji":"🎯"}

# Business Objective
Sales motion continues without Dennis watching it. The system researches, qualifies, drafts, waits for approval, sends, and follows up — logging every step in Atomic CRM as the single source of truth.
**Success criterion for Phase 1:** One lead travels the full loop — intake → research → qualify → draft → approval → send → logged — end to end, manually triggered.
# Stack Decision (2026-07-19)
- **CRM / System of record:** `marmelab/atomic-crm` (MIT, React + shadcn/ui + Supabase) — self-hosted, matches existing stack
- **Agent access layer:** `marmelab/atomic-crm-mcp` (official, OAuth 2.1, SQL with RLS enforcement)
- **Orchestration pattern:** Plan–Apply–Unify loop (`ChristopherKahler/paul`)
- **Quality gates / approval rules:** patterns from `affaan-m/ECC`
- **Agent role prompts:** researcher / qualifier / outreach-writer from `msitarzewski/agency-agents`
- **Sending:** Resend (email) + Twilio (SMS) — Atomic CRM has no native outbound
- **Scheduling (Phase 2):** pg_cron on the same Supabase Postgres — replaces external scheduler for v1
- **Superseded:** GoHighLevel-MCP → Reference Only
# Component Breakdown (each \

#
Module
Responsibility (SOLID: one job each)
Est. lines

1
`config.ts`
Env vars, thresholds (approval \$ limit, follow-up days), ICP definition
\~80

2
`crm-client.ts`
All reads/writes to Atomic CRM via MCP SQL. No business logic.
\~200

3
`researcher.ts`
Builds prospect dossier (web research + SGI patterns). Input: contact. Output: dossier JSON.
\~250

4
`qualifier.ts`
Scores dossier vs ICP → route: outreach / nurture / reject + reason logged
\~150

5
`writer.ts`
Drafts outreach in Dennis's voice from dossier + template library
\~200

6
`quality-gate.ts`
ECC-style checks: tone, claims, compliance (BCFSA-sensitive language), length
\~150

7
`approval.ts`
Queues drafts for Dennis; auto-approve below threshold, hold above
\~120

8
`sender.ts`
Resend/Twilio dispatch. Retries, delivery logging. Nothing else.
\~150

9
`sdr-loop.ts`
PAUL orchestrator: Plan → Apply (call modules 3–8) → Unify (write back via 2)
\~300

**DRY note:** crm-client.ts is the ONLY module that touches the database. Every other module receives data as parameters and returns results — testable in isolation with mock inputs.
# Data Flow
```javascript
Lead source (form / import / Marketplace)
  → Atomic CRM contact created (Supabase Postgres = truth)
  → sdr-loop PLAN: crm-client queries "contacts needing action"
  → APPLY: researcher → qualifier → writer → quality-gate
  → approval queue (auto if