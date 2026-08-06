---
title: Swan GTM Skills Library
created: 2026-08-04
updated: 2026-08-06
type: concept
tags: [how-to, guide, technology, research]
sources: [notion: swan-gtm/gtm-skills, https://github.com/swan-gtm/gtm-skills]
---

# Swan GTM Skills Library

**Source:** [GitHub — swan-gtm/gtm-skills](https://github.com/swan-gtm/gtm-skills) (ingested from Notion page `swan-gtm/gtm-skills`, 2026-08-04; full mirror at `raw/swan-gtm/` — 267 SKILL.md, 45 authors)

## Summary

Swan GTM Skills is an **open library of reusable, production-oriented GTM instructions for AI agents**. It packages operator methodology into portable `SKILL.md` files covering prospecting, account research, buying signals, outreach, pipeline management, RevOps, and sales strategy.

## Strategic role

Use this repository as the **GTM playbook and decision layer**. It should **not** replace the CRM, operational database, workflow engine, enrichment services, or communication infrastructure — it sits on top of them as the reasoning layer.

## Recommended architecture (6 layers)

1. **Data and signals** — DataForSEO, Exa, Serper, Deepline, Happenstance, Enrich.so, government APIs, websites, job boards, CRM activity
2. **Signal normalization** — Convex ingestion, deduplication, entity resolution, timestamps, provenance
3. **LeadSniperAI signal engine** — ICP matching, intent classification, urgency, confidence, funding-need probability, lead tier
4. **GTM skills layer** — account research, signal validation, outreach strategy, qualification, objection handling, pipeline management, RevOps playbooks
5. **Execution** — Resend, Twilio, Unipile, voice agents, CRM tasks, approved automations
6. **Learning loop** — replies, meetings, qualifications, applications, funded deals, skill-level performance measurement

## Recommended curated structure

- **Shared:** account research, signal validation, contact research, outreach quality control, pipeline review
- **Mortgage:** alternative-lending triggers, self-employed borrower identification, construction-financing opportunity, mortgage-renewal triggers, accountant-referral outreach
- **Business funding:** funding-readiness assessment, business-growth signals, lender-fit analysis, advisor-ready opportunity, application readiness
- **Spectra:** affordable-housing opportunity research, municipality research, capital-source matching, family-office research, investor outreach

## Initial pilot skills

| Skill | Purpose |
|-------|---------|
| **Signal qualification** | Determine whether an observed event is a genuine financing/commercial trigger vs. general company news |
| **Account research** | Evidence-backed account brief: signal, date, likely need, timing, decision-makers, evidence, confidence, recommended next action |
| **Opportunity scoring** | Qualitative skill judgment + deterministic scoring: ICP fit, signal strength, funding-need probability, timing, contactability, data completeness |
| **Outreach strategy selection** | Select reason, evidence, channel, offer, CTA *before* generating outreach copy |
| **Governance** | Automate research, signal classification, drafting, compliance checks. Human approval required for initial campaign launches, sensitive financial cases, material bulk actions |

## Installed locally (2026-08-06)

15 curated skills installed to `~/.hermes/skills/gtm/`: `signal-interpreter`, `score`, `icp`, `account-tier-scoring`, `research`, `reach-out`, `bridge-before-cold`, `never-guess-an-email`, `cold-email-4-sequence`, `cold-email-preflight`, `citation-gap-outreach`, `pipeline-review`, `call-scorecards`, `category-of-one-positioning`, `founder-led-sales`.

## Convex implementation

Store each skill invocation with: tenant ID, skill ID + version, account ID, signal IDs, input snapshot, output, confidence, approval status, execution status, outcome, timestamps. This enables **attribution of revenue and pipeline results to individual skills, signals, and messages**.

## Adoption recommendation

1. Curate ~10–15 skills
2. Adapt to LeadSniperAI and Canadian financing workflows
3. Instrument skill runs and revenue outcomes in Convex
4. Pilot one signal-to-outreach workflow before broader adoption

## KlickSmartAI relevance

- Direct fit with the [[gtm-engineer-resources]] stack (signal → enrich → outbound → convert)
- Complements [[explorium-ai]], [[enrichlayer]], [[dataforseo]] as the *decision layer* over data/enrichment layers
- Architecture mirrors KlickSmartAI's [[klick2client-os]] and [[signal-intelligence-agent]] signal engine design
- The Spectra section maps to [[spectra-holdings-group]] county-level research + investor outreach work
- The mortgage section maps to [[gtm-strategies-mortgage-clients-2026]] and alternative-lending triggers
