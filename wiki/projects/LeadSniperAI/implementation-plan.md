---
title: LeadSniperAI Implementation Plan
type: project-plan
status: architecture-spec
prd: projects/LeadSniperAI/PRD.md
owner: Dennis
agent: Hermes Agent (orchestrator) + Claude Code (analysis & generation)
target-kpi: 1000+ businesses/day, <3min audit, >25% qualified
---

# LeadSniperAI — Implementation Plan

> **One-liner.** Autonomous Business Opportunity Discovery Engine that finds businesses with strong reputations but weak websites, audits them with AI, scores the opportunity, and generates AI Search–ready rebuilds — every artifact lands in RIOS.

This plan implements the [LeadSniperAI PRD](projects/LeadSniperAI/PRD.md) as a **RIOS Workforce pillar** (see `drafts/rios-north-star-architecture.md` §3) — specifically the **LeadSniper Worker** + **Website Rescue Worker** + **SEO Worker** + **Proposal Worker** working in concert, with Hermes as the long-running orchestrator.

---

## 1. Strategic Fit with RIOS

| RIOS layer | LeadSniperAI mapping |
|---|---|
| **Signal** | Discovery sources (Google Maps / Google Business Profile / Exa / Tavily) surface weak-website signals |
| **Context** | Scrapling crawl + ScrapeGraphAI extraction builds business context |
| **Relationship Intelligence** | Business → Website → Audit → Proposal as linked RIOS entities |
| **Opportunity** | Opportunity score + revenue estimate = RIOS Opportunity record |
| **Action** | Outreach workers (Resend / Unipile / SmartLead / GoHighLevel) execute against RIOS Opportunity |
| **Learning Loop** | Proposal acceptance/feedback adjusts scoring weights over time |

**Outputs feed**: `entities/`, `opportunities/`, `audit/`, `proposals/`, `communications/` in the wiki. Workspace pattern follows `reference/hermes-dev-to-prod-implementation-plan.md` §Projects/LeadSniperAI.

---

## 2. Guiding Principles

1. **Orchestrator + workers.** Hermes schedules, queues, monitors, and dispatches. Claude Code does the *reasoning* per business. Scrapling does the *crawling*. ScrapeGraphAI does the *extraction*. Never mix concerns.
2. **State is durable.** Every crawl emits a JSON artifact committed to disk. Hermes can resume from any artifact. No in-memory pipelines that vanish on crash.
3. **Quotas first.** Discovery APIs (Google, Exa, Tavily) cost money. Hermes enforces per-source rate limits, retries with exponential backoff, and never burns through a quota on a single bad seed.
4. **HITL on outbound.** Per RIOS north-star §3, all external communication (email, LinkedIn, proposal send) requires human approval. Auto-generation is fine; auto-send is not.
5. **Schema before scoring.** Every artifact has a versioned JSON schema. The Opportunity Score is a pure function of inputs — so we can A/B test score versions against historical win/loss.
6. **Idempotency by URL.** The same `business_id` always produces the same `audit_id`. Re-runs update, never duplicate.
7. **Earn the rebuild.** The system generates a website *only after* the audit + proposal are accepted. Never auto-deploy to a prospect without explicit go.

---

## 3. Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    Hermes Agent (Orchestrator)                  │
│  Schedule │ Queue │ Rate-limit │ Monitor │ Dispatch │ Resume    │
└──────┬──────────────────────────────────────────────┬───────────┘
       │                                              │
       ▼                                              ▼
┌──────────────┐    ┌──────────────┐    ┌───────────────────────┐
│  Discovery   │    │  Inspection  │    │  Generation & Outreach│
│              │    │              │    │                       │
│ • Google Maps│    │ • Scrapling  │    │ • Claude Code:        │
│ • Google BP  │───▶│ • ScrapeGraph│───▶│   - Audit             │
│ • Exa        │    │   AI (opt)   │    │   - Proposal          │
│ • Tavily     │    │ • Lighthouse │    │   - Next.js rebuild   │
└──────────────┘    │   (Phase 2)  │    │ • Resend/Unipile      │
                    └──────────────┘    │ • SmartLead           │
                           │             │ • GoHighLevel         │
                           ▼             └───────────────────────┘
                    ┌──────────────┐
                    │     RIOS     │  ◀── every artifact lands here
                    │  (this wiki) │
                    └──────────────┘
```

### 3.1 Worker Responsibilities

| Worker | Runtime | Job |
|---|---|---|
| **Discovery Worker** | Hermes cron | Pull businesses from Google Maps / GBP / Exa / Tavily matching filters (high reviews, weak site, outdated, missing). Dedup, geocode, stage to `inbox/`. |
| **Crawl Worker** | Scrapling (subprocess via Hermes) | Full-site crawl. Emits `site.json`, `pages.json`, `images.json`, `links.json`, `schema.json`, `performance.json`. |
| **Extract Worker** (optional) | ScrapeGraphAI | When layouts vary, extract services, staff, pricing, FAQs, contact info. |
| **Analyzer Worker** | Claude Code | Score the website on 10 axes, write human-readable findings. |
| **Proposal Worker** | Claude Code | Generate executive summary, audit, pricing, roadmap → Markdown + PDF. |
| **Rebuild Worker** | Claude Code | Generate Next.js + Tailwind site, schema, location pages, blog. |
| **CMS Worker** | Claude Code | Scaffold CMS structure (blog/pages/services/staff/FAQs). |
| **Outreach Worker** | Hermes → Resend/Unipile/SmartLead/GHL | Sequence cold email + LinkedIn, with HITL gate. |

### 3.2 Claude Code vs Hermes Agent Split (per PRD §13–14)

- **Claude Code** = per-business deep work: crawl coordination, analysis, JSON output, audit/proposal/website code, git commit.
- **Hermes Agent** = long-running operator: scheduling, queue management, API quota control, parallel dispatch, artifact persistence, failure notification, status tracking.

---

## 4. Data Contracts (JSON Schemas)

Every artifact has a versioned schema. Store under `projects/LeadSniperAI/schemas/v{N}/`.

```json
{
  "schema_version": "1.0",
  "business_id": "b_01HMXXXXXXXXXXXX",
  "source": "google_maps",
  "name": "Joe's Plumbing",
  "category": "Plumber",
  "address": {
    "line1": "123 Main St",
    "city": "Kelowna",
    "region": "BC",
    "postal_code": "V1Y 1A1",
    "country": "CA"
  },
  "geo": {"lat": 49.8880, "lng": -119.4960},
  "phone": "+1-250-555-0100",
  "website_url": "https://joesplumbing.example.com",
  "rating": 4.7,
  "review_count": 213,
  "hours": {"mon_fri": "08:00-17:00", "sat": "09:00-13:00", "sun": "closed"},
  "discovered_at": "2026-06-29T10:00:00Z",
  "discovery_signals": {
    "review_strength": "high",
    "website_signal": "weak",
    "outdated_detected": true
  }
}
```

```json
{
  "schema_version": "1.0",
  "audit_id": "a_01HMXXXXXXXXXXXX",
  "business_id": "b_01HMXXXXXXXXXXXX",
  "crawled_at": "2026-06-29T10:05:00Z",
  "scores": {
    "website_quality":  48,
    "seo":              32,
    "technical":        55,
    "performance":      61,
    "trust":            40,
    "conversion":       25,
    "ai_search":        12,
    "content":          38,
    "brand":            30,
    "accessibility":    50,
    "overall":          39
  },
  "findings": {
    "critical":   ["No HTTPS on contact form", "No LocalBusiness schema anywhere"],
    "high":       ["Missing FAQPage schema", "Title tag > 60 chars on 4 pages"],
    "medium":     ["Images missing alt text", "Mobile CLS > 0.25"],
    "low":        ["Twitter card meta missing on blog posts"]
  },
  "evidence": {
    "links":          ["https://joesplumbing.example.com/contact"],
    "screenshots":    ["runs/2026-06-29/b_01HM/screenshots/home.png"],
    "page_samples":   ["runs/2026-06-29/b_01HM/pages/home.html"]
  },
  "revenue_opportunity_usd": {
    "website_rebuild":     4500,
    "ai_search":            800,
    "monthly_cms":          300,
    "monthly_seo":          500,
    "ltv_estimate":       14000
  }
}
```

```json
// opportunity.json (v1) — RIOS Opportunity entity
{
  "schema_version": "1.0",
  "opportunity_id": "o_...",
  "business_id": "b_...",
  "audit_id": "a_...",
  "score": 39,
  "qualified": true,
  "estimated_ltv_usd": 14000,
  "stage": "audit_ready",
  "owner": null,
  "next_action": "generate_proposal"
}
```

Other schemas: `proposal.json`, `rebuild.json` (Next.js repo metadata), `crm.json`, `outreach.json`.

---

## 5. Implementation Phases

### Phase 0 — Skeleton & Schemas (Week 1)
- [ ] Create `projects/LeadSniperAI/{PRD.md, implementation-plan.md, schemas/v1/, scripts/, prompts/}` in this wiki.
- [ ] Write all v1 JSON schemas (business, audit, opportunity, proposal, rebuild).
- [ ] Define `RIOS LeadSniper` directory structure: `entities/{businesses,opportunities}/`, `audit/`, `proposals/`, `communications/`.
- [ ] Set up Scrapling in a venv; smoke-test crawl against 3 known sites.
- [ ] Pick one pilot business end-to-end manually.

**Exit criteria**: Manual flow works for 1 business — discovery → crawl → audit → proposal → Markdown deliverable.

### Phase 1 — Single-Business Pipeline (Weeks 2–3)
- [ ] Build `scripts/discover.py` — Google Maps Places API search by category + geography + min rating + min reviews.
- [ ] Build `scripts/crawl.py` — Scrapling orchestrator that emits the 6 JSON artifacts per business.
- [ ] Build `scripts/extract.py` — ScrapeGraphAI optional extractor for services/staff/pricing/FAQs.
- [ ] Build `scripts/analyze.py` — Claude Code reasoning step. Input: artifacts. Output: `audit.json`.
- [ ] Build `scripts/score.py` — Pure function mapping audit fields → 10-axis score + revenue estimate.
- [ ] Build `scripts/propose.py` — Claude Code generates executive summary, audit narrative, pricing, roadmap → Markdown + PDF (WeasyPrint).
- [ ] Wire all 6 scripts as a CLI: `python -m leadsniper run --business-id <id>`.
- [ ] Persist every artifact under `projects/LeadSniperAI/runs/<business_id>/`.

**Exit criteria**: 10 businesses processed end-to-end; all artifacts valid against v1 schema; manual review of audits shows >80% accuracy.

### Phase 2 — Hermes Orchestration (Weeks 4–5)
- [ ] Hermes `cronjob` for Discovery Worker (daily, region-rotated).
- [ ] Hermes Kanban-style queue: `inbox/ → crawling/ → analyzing/ → audited/ → proposed/ → outreach/`.
- [ ] Rate-limit guard: per-source tokens/sec, daily budget, exponential backoff.
- [ ] Parallel dispatch: 5–20 concurrent crawl workers (configurable).
- [ ] Resume logic: if Hermes crashes, picks up next pending business from queue.
- [ ] Failure alerts: Slack/Telegram on >5% error rate or quota exhaustion.
- [ ] Status dashboard note in wiki: `projects/LeadSniperAI/Dashboard.md` (auto-updated).

**Exit criteria**: 200 businesses/day sustained for 3 days; >95% crawl success; <3 min audit p50.

### Phase 3 — Opportunity Score & Qualification (Week 6)
- [ ] Implement qualification gates: minimum score threshold + minimum review count + active GBP + serviceable geography.
- [ ] Wire scoring function to be hot-swappable (v1, v1.1, v2, …) — store score version in audit.
- [ ] A/B test scaffold: run two score versions on same cohort; compare downstream proposal-acceptance.
- [ ] RIOS Opportunity entity auto-created in `entities/opportunities/` for every qualified audit.

**Exit criteria**: >25% of audited businesses classified as qualified opportunities (per PRD KPI).

### Phase 4 — Proposal Generator & HITL Gate (Week 7)
- [ ] Proposal templates: 3 pricing tiers (good/better/best).
- [ ] PDF rendering with WeasyPrint or Playwright.
- [ ] Proposal library under `proposals/<business_id>/<date>/`.
- [ ] Hermes approval workflow: generates draft → notifies human → human approves → marks `status=approved` → enables Outreach.
- [ ] Proposal delivery: PDF attached to Resend email OR hosted link.

**Exit criteria**: Proposal generation <60s; 100% of outbound requires explicit approval.

### Phase 5 — Website Rebuild (Weeks 8–10)
- [ ] Next.js 15 + Tailwind scaffold template under `rebuilds/_template/`.
- [ ] Claude Code-driven generation per business: pages from crawl artifacts + extracted content.
- [ ] SEO defaults: meta, OG, Twitter cards, canonical, sitemap.xml, robots.txt.
- [ ] Schema defaults: Organization, LocalBusiness, FAQ, Breadcrumb, Review.
- [ ] AI Search defaults: llms.txt, structured Q&A blocks, citation-friendly headings, FAQPage schema.
- [ ] Location pages auto-generated from service areas (if present).
- [ ] Blog starter with 3 posts based on extracted FAQs/topics.
- [ ] Git workflow: each rebuild in its own branch in `rebuilds/<business_id>/`; PR-ready for human review.

**Exit criteria**: Generated site passes Lighthouse 90+ on all 4 axes for a test business; HITL review of 3 generated sites shows production-ready quality.

### Phase 6 — CMS Generation (Week 11)
- [ ] CMS schema: blog, pages, services, staff, projects, testimonials, FAQs, images, downloads, news, resources.
- [ ] CLI: `python -m leadsniper cms --business-id <id>`.
- [ ] Optional: scaffold against Payload / Sanity / TinaCMS (decision deferred to Phase 6 start).
- [ ] Seed with content extracted in Phase 1.

**Exit criteria**: 1 generated site has working CMS with seed content; admin can add a blog post end-to-end.

### Phase 7 — Outreach Integration (Weeks 12–13)
- [ ] Resend integration: cold email with HTML + plain-text + PDF attachment + open/click tracking.
- [ ] Unipile integration: LinkedIn connection + message sequence.
- [ ] SmartLead integration: multi-step drip campaigns.
- [ ] GoHighLevel integration: pipeline + SMS + calendar booking.
- [ ] All sends gated by HITL approval.
- [ ] Reply capture → RIOS entity update → next-action recommendation.

**Exit criteria**: >10% website-to-meeting conversion (per PRD KPI) on first 50 outreach sequences.

### Phase 8 — Learning Loop (Weeks 14–15)
- [ ] Track every proposal outcome (accepted / declined / no-response) in `entities/opportunities/<id>/outcome.json`.
- [ ] Monthly report: conversion rates by score bucket, by category, by geography.
- [ ] Score calibration: regress accepted LTV against audit features; publish score v2 if it improves lift.
- [ ] RIOS knowledge graph update: each closed-loop deal becomes a training case.

**Exit criteria**: Score v2 published; backtest shows ≥10% lift on accepted-deal prediction vs v1.

### Phase 9 — Phase 2 PRD Features (Weeks 16+, ongoing)
From PRD §15, gated on Phase 8 completion:
- Vision-based UI screenshot analysis
- Lighthouse / PageSpeed Insights integration
- AI citation & answer-engine visibility scoring
- Competitor benchmarking
- Google Search Console + GA4 integrations
- Heatmap / session-replay
- Continuous monitoring + change detection
- Automated monthly client health reports
- RIOS learning engine for scoring

---

## 6. Pilot Run (Before Phase 2)

Pick **one business** (Dennis's pick) and run Phases 0–1 manually:

1. Discover via Google Maps (e.g., "plumbers in Kelowna with 50+ reviews and weak websites").
2. Crawl with Scrapling — confirm 6 artifacts emitted.
3. Optional ScrapeGraphAI extraction — confirm services/staff/FAQs captured.
4. Claude Code analysis — produce `audit.json` with 10-axis scores.
5. Claude Code proposal — Markdown + PDF.
6. Manual review by Dennis — sanity check narrative, pricing, recommendations.

**Why**: validates the pipeline shape before Hermes orchestration multiplies it 1000×.

---

## 7. Technical Risks & Mitigations

| Risk | Mitigation |
|---|---|
| **Scrapling breakage** (JS-heavy sites, anti-bot) | Headless fallback (Playwright); retry queue with backoff; respect robots.txt but allow override per business. |
| **Google API quota** | Daily budget caps in Hermes; multi-source fallback (Exa / Tavily / GBP); cache Places results 30 days. |
| **Claude hallucination on audit findings** | Ground every finding in a crawl artifact path (cite page + selector). Manual review on first 100 audits. |
| **Scoring drift** | Versioned score functions; A/B harness; backtest before promote. |
| **HITL bypass** | Outbound worker hard-coded to require `status=approved`; no admin override path. |
| **Rebuild quality** | Generated site stays in PR until human review; Lighthouse gate before merge. |
| **GDPR / ToS** | Respect robots.txt; only crawl public pages; do not store PII beyond public business contact info; log ToS acceptance per source. |
| **Cost blowout** | Per-day cost cap in Hermes; alert at 80%; auto-pause at 100%. |

---

## 8. Success Metrics (from PRD)

| KPI | Target | Measured by |
|---|---|---|
| Businesses analyzed/day | 1,000+ | `runs/<date>/count.json` |
| Audit generation time (p50) | < 3 min | `audit.json.crawled_at → analyzed_at` |
| Crawl success rate | > 95% | `crawl_status.json` |
| AI audit accuracy | > 90% | Manual review sample (n=50/quarter) |
| Proposal generation time | < 60 s | `propose.py` wall clock |
| Qualified opportunity rate | > 25% | `opportunity.json.qualified=true / total` |
| Website → meeting conversion | > 10% | Outreach → Calendly/GHL booking |
| Proposal acceptance rate | > 30% | `entities/opportunities/<id>/outcome.json` |

Live dashboard: `projects/LeadSniperAI/Dashboard.md` (Hermes-writes daily).

---

## 9. Directory Layout (Wiki)

```
projects/LeadSniperAI/
├── PRD.md                              # the PRD
├── implementation-plan.md              # this file
├── Dashboard.md                        # auto-updated KPIs
├── schemas/
│   └── v1/
│       ├── business.schema.json
│       ├── audit.schema.json
│       ├── opportunity.schema.json
│       ├── proposal.schema.json
│       └── rebuild.schema.json
├── prompts/
│   ├── analyze.txt                     # Claude Code audit prompt
│   ├── propose.txt                     # Claude Code proposal prompt
│   └── rebuild.txt                     # Claude Code Next.js generation prompt
├── scripts/
│   ├── discover.py
│   ├── crawl.py
│   ├── extract.py
│   ├── analyze.py
│   ├── score.py
│   ├── propose.py
│   ├── rebuild.py
│   └── cms.py
├── runs/
│   └── <YYYY-MM-DD>/
│       └── <business_id>/
│           ├── business.json
│           ├── site.json
│           ├── pages.json
│           ├── images.json
│           ├── links.json
│           ├── schema.json
│           ├── performance.json
│           ├── extracted.json
│           ├── audit.json
│           └── proposal.pdf
├── rebuilds/
│   ├── _template/                      # Next.js starter
│   └── <business_id>/
└── logs/
    └── <YYYY-MM-DD>.log
```

RIOS-side artifacts (auto-created by workers):
```
entities/
├── businesses/<business_id>.md
└── opportunities/<opportunity_id>.md
audit/<business_id>/<date>/audit.md
proposals/<business_id>/<date>/proposal.md
communications/<business_id>/<date>/sequence.md
```

---

## 10. Open Questions (resolve before Phase 2 start)

1. **Discovery geography**: national, regional, or city-by-city at launch?
2. **Vertical scope at launch**: all categories or pilot in 1–2 (e.g., plumbers, dentists, lawyers)?
3. **Hosting target for rebuilds**: Vercel default, or self-hosted?
4. **CMS choice**: Payload, Sanity, Tina, or bespoke MDX-only?
5. **Pricing tiers**: confirm good/better/best ranges ($4.5K / $8K / $15K?) before proposal template.
6. **Outbound brand**: LeadSniperAI branding on cold email, or white-label per agency partner?
7. **Cost ceiling per day**: what's the budget cap for API spend before auto-pause?

---

## 11. Next 5 Concrete Actions

1. **Dennis approves this plan** (or flags changes).
2. Move PRD into `projects/LeadSniperAI/PRD.md` (canonical location).
3. Resolve Open Questions §10 (at minimum: geography, verticals, pricing).
4. Phase 0 work begins: schemas + Scrapling smoke test + RIOS directory structure.
5. Pilot business picked + Phase 1 manual run scheduled.

---

*This plan treats the PRD as an autonomous-agent architecture spec. The order matters: schemas before crawlers, pilot before parallelization, HITL before any outbound send, scoring before proposal generation, learning loop before any claim of system-wide success.*