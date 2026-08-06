---
title: LeadSniperAI Project Docs
created: 2026-08-05
updated: 2026-08-05
type: summary
tags: [technology, research]
sources: [notion]
---

# LeadSniperAI Project Docs

Complete LeadSniperAI product documentation ingested from Notion (2026-08-05). The six documents form the full product stack:

| Doc | Role | Size |
|-----|------|------|
| [Marketplace PRD](./marketplace-prd.md) | What to build — Convex multi-tenant lead marketplace + rank-and-rent assets | 37K |
| [CLI PRD](./cli-prd.md) | How to build — `leadsniper` CLI for LeadSniperAI 3.0 (FastAPI wrapper) | 101K |
| [Workflow Improvement](./workflow-improvement.md) | How to make it accurate — adversarial refutation, deterministic scoring | 13K |
| [Marketplace OS](./marketplace-os.md) | Canadian funding front door — /funding-assessment funnel | 36K |
| [Venture OS](./venture-os.md) | How to sell — Free Audit offer ladder, Klick2Client brand | 33K |
| [Integration API Catalog](./integration-api-catalog.md) | What APIs — research, enrichment, social, CRM, outreach | 54K |

**Related docs:** [[lead-sniperai-cli-os]] (master OS spec, `processes/`), [[lead-sniperai-signal-cold-email-sop]] (operational SOP, `processes/`)

**Through-line:** Marketplace PRD (what) → CLI PRD (build) → Workflow Improvement (accuracy) → Marketplace OS (funding front door) → Venture OS (GTM/sell) → Integration Catalog (APIs).

**Key entities:** Convex (backend), Clerk (identity), Stripe (billing), Deepline (contacts), Atomic CRM (system of record), Notion (control plane), Klick2Client.com (brand), DataForSEO/Tavily/Apify/Gemini (research).
