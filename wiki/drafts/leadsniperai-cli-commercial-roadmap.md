---
title: LeadSniperAI CLI — Commercial Launch Roadmap (phased)
created: 2026-08-05
updated: 2026-08-05
type: roadmap
status: active
source: Notion "LeadSniperAI CLI Product Requirements & Implementation Plan" (3a89e94cf0a48100800ef4a2f57f842a) — full text at `drafts/leadsniperai-cli-commercial-plan.md`
tags: [leadsniperai, cli, commercialization, roadmap, phases]
---

# LeadSniperAI CLI — Commercial Launch Roadmap

Guiding principle: the Notion PRD is authoritative for what we build; this roadmap sequences it into launchable phases. **Current decision (Dennis, 2026-08-05): min MVP now — current CLI output is acceptable; offer-gap + SEO/AEO deferred post-MVP.**

## Commercial thesis (from PRD)

Three coordinated layers:
1. **LeadSniperAI CLI** — deterministic signal collection + structured analysis (execution engine)
2. **AI Agency Growth Analyst Skill** — agent operating instructions: when to invoke CLI, how to interpret evidence, how to convert signals into prioritized actions (portable judgment layer)
3. **LeadSniperAI managed platform** — monitoring, multi-tenant storage, campaigns, reporting via Convex (recurring-revenue layer)

First sellable vertical: **AI Agency Growth Intelligence**. Buyer JTBD: *"Help me identify why my AI agency is not generating enough qualified opportunities and show me which website, positioning, offer, and GTM changes to make first."*

## Signal-to-Action contract (all outputs must follow)

```
Observed signal → Evidence → Business implication → Growth opportunity → Recommended action → Expected outcome → Confidence
```

Shared `GrowthSignal` JSON object: category (positioning|offer|conversion|seo|aeo|content|trust|competitive|outreach), observation, evidence[], businessImpact, recommendedAction, priority, confidence, estimatedEffort, expectedOutcome.

## Phase map

### Phase 0 — Commercialize current MVP surface (NOW, in progress)
- ✅ CLI generates website + growth signals for AI agencies (working, verified)
- ⬜ Standardize `GrowthSignal` JSON contract
- ⬜ Capture 3 representative AI agency analyses as fixtures
- ⬜ Draft `ai-agency-growth-analyst` SKILL.md (structure defined in PRD: references/ templates/ examples/ scripts/)
- ⬜ Growth-audit report template + 30-day action plan template
- ⬜ Schema + report validators (validate-signal-schema.ts, validate-report-output.ts)
- ⬜ Licensing terms (Community vs Professional)
- ⬜ Stripe-compatible checkout + delivery
- ⬜ Public demo (consenting/public business website)

**Exit gate:** one AI agency scan → GrowthSignal JSON → report → sellable artifact.

### Phase 1 — CLI foundation + full MVP command set (PRD §14 P0–P2, §15 MVP)
- Repository hardening: rotate keys, remove secrets, resolve build errors, baseline tests, FastAPI health
- Click package skeleton, config profiles, HTTP client, JSON response envelope, exit codes 0–9
- `system doctor`, `config validate`
- MVP command set (14): `search local`, `import csv`, `lead enrich`, `lead contacts`, `intelligence company`, `audit seo`, `outreach email generate`, `outreach call-script`, `recommend`, `lookup reverse`, `batch status`, `export csv`
- SKILL.md drafted alongside, ≥60% test coverage, subprocess tests

**Exit gate:** full local-business workflow completes without React UI; JSON everywhere.

### Phase 2 — Evidence + qualification (PRD §14 P3, v1.1 addendum)
- Canonical lead record, identity resolution (CID → Place ID → phone → domain; never name alone)
- Evidence model + 9 evidence classes (grounded/source_reported/observed/derived/estimated/inferred/simulated/user_supplied/human_verified)
- Eligibility rules, verification commands, confidence scoring, source attribution
- Provider adapter interface (normalized schemas, fallback policy), idempotency keys, cost guardrails
- Multi-tenant + authorization model
- Release gates: alpha → beta → production

**Exit gate:** every score links to evidence + confidence; deep/contact enrichment only past configurable thresholds.

### Phase 3 — Proprietary intelligence (PRD §8, §14 P4)
- Website revenue-infrastructure audit (hero, CTA, forms, mobile, trust, booking, chat, PageSpeed, intake)
- AI Employee fit score (missed-call risk, booking friction, intake complexity, review opportunity, capacity, after-hours demand, lead-value, automation readiness)
- Opportunity classification (fixable-crisis, hidden-gem, sleeping-giant, reputation-rescue, intake-friction, missed-call-opportunity, seo-growth-opportunity, ai-employee-fit, not-qualified)
- 🔜 **Offer-gap signal engine** lands here — **deferred, needs validation pilot first** (20 biz / 2 verticals, ≥70% precision). Proposal: `drafts/leadsniperai-offer-gap-signal-proposal.md`
- 🔜 **SEO/AEO opportunities** land here — **deferred** (seo-audit keywords + DataForSEO AI-Opt LLM-mentions)

**Exit gate:** proprietary scoring outputs that generic audit tools cannot produce.

### Phase 4 — Campaign orchestration + GTM engine (PRD §9, §21)
- Campaign state machine: discover → enrich → audit → score → verify → generate-outreach → export; resumable, idempotent, cost-capped, approval-gated
- GTM command group: diagnose → segment → strategy → offer/positioning → channels → plan → campaign from playbooks
- Playbook registry (Printing Press sources, version-pinned), Dub attribution, experiment management, KPI tree, learning loop
- 8 initial GTM playbooks (PRD §21.20) — first: Free Audit → Strategy Call → Paid Implementation

**Exit gate:** a campaign runs end-to-end with approval gates and measured outcomes.

### Phase 5 — Vertical discovery agents + monitoring (PRD addendum)
- Vertical registry (schema: industries, personas, signals, scoring weights, exclusions, evidence freshness)
- Discovery-agent contract + resolver (`agent resolve` / `agent compose` from signal packs)
- Initial 6 agents: local marketing/reputation, accounting/bookkeeping, business financing, employee benefits, technology/automation, insurance/risk
- 17 signal packs (reputation_gap, review_velocity, intake_friction, missed_call_risk, capacity_growth, working_capital, technology_gap, …)
- DataForSEO Business Data integration: discovery, profile, reviews, place_topics, identity normalization
- Historical snapshots + monitoring: rating/review/profile/website/competitor/signal change detection, refresh cadences (active=weekly, high-potential=monthly, general=quarterly)
- Contact activation: Deepline + Happenstance at contact-ready threshold

**Exit gate:** one campaign auto-resolves agent from vertical+industry+location; multi-vertical scores per business.

### Phase 6 — Managed platform (recurring revenue)
- Convex persistence: scans, signal history, recommendations, outcomes, tenant records
- Packaging tiers live: Community (free–$49) → Professional ($149–499) → Expert Audit ($500–1,500) → Managed ($500–2,500+/mo) → White-label ($2.5k–10k+ setup)
- PLG funnel: free skill → automated snapshot → pro pack/expert audit → connected workspace → managed intelligence → white-label
- Success metrics instrumented: acquisition (installs, activations), value (evidence-cited %, acceptance, implementation rate), revenue (conversion, MRR, white-label), outcome (meetings, pipeline, revenue, retention)

**Exit gate:** recurring revenue measured against outcomes.

## Deferred items (tracked on task sheet, P3)
- Offer-gap signal engine → Phase 3, requires validation pilot
- SEO/AEO opportunities → Phase 3
- GMB-grounding signal engine → Phase 5 (proposal exists)

## Key principles to preserve (from PRD)
- Sending always disabled by default; generate ≠ approve ≠ send
- No fabrication: evidence-backed claims only; simulated content never used as evidence
- Stable LeadSniper-owned command contract even as providers change
- Cost-aware staged funnel: enrichment only for sufficiently scored records
- Deterministic, resumable, auditable, safe-by-default commands
