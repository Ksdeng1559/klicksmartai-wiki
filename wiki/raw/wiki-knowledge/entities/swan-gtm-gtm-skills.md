---
title: Swan GTM Skills Library
created: 2026-08-06
updated: 2026-08-06
type: entity
category: gtm
url: https://github.com/swan-gtm/gtm-skills
pricing: open-source (MIT)
status: ingested
source: raw/swan-gtm/
tags: [entity, gtm, skills, sales, revops, outreach, prospecting, signals, leadgen]
related: [leadsniper-sgi-prd, research-intelligence-workflow, b2b-outreach-intelligence-pipeline, hnw-lead-sniper]
---

# Swan GTM Skills Library

Open, production-grade go-to-market skills for AI agents — prospecting, research, outreach, signals, pipeline, RevOps. Curated by Swan (getswan.com), authored by the GTM community. Every skill is a plain `SKILL.md` readable by any agent (Claude Code, Cursor, Codex, Hermes).

**Ingested 2026-08-06** from https://github.com/swan-gtm/gtm-skills (commit d31ef43). Full mirror: `raw/swan-gtm/` — **267 SKILL.md files, 45 authors**, 7MB.

## Strategic role (from Notion summary)

Use as the **GTM playbook and decision layer**. Does NOT replace CRM, operational database, workflow engine, enrichment services, or communication infrastructure.

**Recommended architecture:**
1. **Data/signals:** DataForSEO, Exa, Serper, Deepline, Happenstance, Enrich.so, government APIs, job boards, CRM activity
2. **Signal normalization:** Convex ingestion, dedup, entity resolution, timestamps, provenance
3. **LeadSniperAI signal engine:** ICP matching, intent classification, urgency, confidence, funding-need probability, lead tier
4. **GTM skills layer:** account research, signal validation, outreach strategy, qualification, objection handling, pipeline, RevOps
5. **Execution:** Resend, Twilio, Unipile, voice agents, CRM tasks, approved automations
6. **Learning loop:** replies → meetings → qualifications → funded deals → skill-level performance measurement

## Skill inventory (by category)

| Category | Count | Category | Count |
|----------|-------|----------|-------|
| RevOps | 41 | Reddit | 9 |
| Outreach | 39 | Deals | 8 |
| Ads | 39 | Sales | 6 |
| Signals | 29 | Research | 6 |
| ABM | 18 | AEO (Answer Engine Opt.) | 6 |
| Newsletters | 17 | Pricing | 5 |
| Influencers | 15 | Positioning | 3 |
| Prospecting | 14 | Events | 1 |
| SEO | 9 | Affiliates | 1 |

## Notable authors

lucas-godtfredsen (inbox warm-up, never-guess-an-email), shane-oconnor (positioning-and-story, founder-led-sales, dev-tool-pricing), amos-bar-joseph (account-tier-scoring), kevin-kd-dorsey (call-scorecards, sales-playbook-foundations), thomas-marcelle (creator campaigns/ROI/pricing), luke-shalom (category-of-one-positioning), nadav-david (bridge-before-cold, reply-pull-gate), sangram-vajre (move-gtm-diagnostic), plus 36 more.

## Curated structure for KlickSmartAI verticals (from Notion)

- **Shared:** account research, signal validation, contact research, outreach quality control, pipeline review
- **Mortgage:** alternative-lending triggers, self-employed borrower ID, construction-financing opportunity, mortgage-renewal triggers, accountant-referral outreach
- **Business funding:** funding-readiness assessment, business-growth signals, lender-fit analysis, advisor-ready opportunity, application readiness
- **Spectra:** affordable-housing opportunity research, municipality research, capital-source matching, family-office research, investor outreach

## Pilot skills (Notion recommendation)

1. **Signal qualification** — genuine financing/commercial trigger vs general news
2. **Account research** — evidence-backed brief: signal, date, need, timing, decision-makers, confidence, next action
3. **Opportunity scoring** — ICP fit, signal strength, funding-need probability, timing, contactability, data completeness
4. **Outreach strategy selection** — reason, evidence, channel, offer, CTA before generating copy
5. **Governance** — automated research/classification/drafting/compliance; HITL for campaign launches, sensitive financial cases, bulk actions

## Convex implementation (Notion)

Store each skill invocation: tenant ID, skill ID+version, account ID, signal IDs, input snapshot, output, confidence, approval status, execution status, outcome, timestamps — for revenue/pipeline attribution to individual skills.

## Adoption recommendation (Notion)

1. Curate ~10–15 skills → 2. Adapt to LeadSniperAI + Canadian financing workflows → 3. Instrument in Convex → 4. Pilot one signal-to-outreach workflow first.

## Install methods

```bash
# one skill
npx skills add swan-gtm/gtm-skills --skill <name>
# everything from one creator
npx skills add swan-gtm/gtm-skills/skills/<creator-slug>
# whole library (interactive)
npx skills add swan-gtm/gtm-skills
```

## Related

- [[leadsniper-sgi-prd]] — LeadSniper SGI domain audit + GTM recommendation app (built on OpenSEO + DataForSEO)
- [[research-intelligence-workflow]] · [[b2b-outreach-intelligence-pipeline]] · [[hnw-lead-sniper]]
