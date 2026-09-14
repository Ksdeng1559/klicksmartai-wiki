---
title: Klick2Client Agentic OS
tags: [products, architecture, agentic-os]
type: products / note
---

# Klick2Client Agentic OS

**Status:** Architecture decision (2026-09-13). Source: [[Executive Summary — KlickSmartAI.com + Klick2Client.com Agentic OS]] (Notion 3b59e94cf0a481099eebfd747a0ce2ad).

## Two layers of one Agentic OS
- **KlickSmartAI.com = agency/operator layer** — internal operating company: client GTM strategy, vertical playbooks, LeadSniperAI, Hermes research/enrichment, campaign ops, service delivery.
- **Klick2Client.com = client-facing service platform** — each client gets a secure workspace on Atomic CRM surfacing signals, research, GTM recs, outreach, conversations, opportunities, reporting, revenue attribution.

## Operating loop
`Signal → Diagnose → Strategic Intelligence Briefing → GTM Strategy → Execute → Attribute → Opportunity → Revenue → Learn`

**Strategic Intelligence Briefing (SIB)** = the canonical handoff artifact between KlickSmartAI intelligence and Klick2Client execution (confirmed signal, diagnosis, ranked recs, proof hooks, friction evidence, decision-maker intel, next-best action, confidence, attribution).

## Method
Brain → Build → Ship, extended for production with **Operate → Measure → Learn**. SEED (structured ideation = *what* to build) → PAUL (Plan→Apply→Test→UAT→Unify→Loop = *how*).

**Core principle:** the LLM must never be the sole holder of system state — business/engineering/code/agent state, evidence, decisions, outcomes persisted externally.

## Production stack (decision)
- **Default:** Atomic CRM (owns CRM functions + customer/revenue lifecycle) + **Supabase/PostgreSQL** (primary database) + **shadcn/ui** (modular layer for Signal Intelligence, GTM Playbooks, Outreach, AI Copilot, Reporting, Integrations).
- **Convex is NOT part of the default stack.** Dropped as native CRM backend; only introduced if a bounded capability can't be built in the stack with measurable advantage.
- Klick2Client adds proprietary revenue-intelligence modules on top (LeadSniperAI signals/evidence, ICP/signal/contactability scoring, GTM playbooks, research/enrichment, campaign orchestration, next-best-action, revenue attribution).

## Dev state standard
Each project keeps `SEED.md / PROJECT.md / ROADMAP.md / ARCHITECTURE.md / STATE.json / DECISIONS.md / SCHEMA.md` under `/apps/<project>/`.

See [[KlickSmartAI-commercial-scope]] and [[Atomic-CRM-stack]] (related). Notion source stays internal (not shared with client teams).
