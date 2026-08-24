# GTM Skills Registry — Veritas Development Group LLC

This file is the **canonical GTM skills binding** for Veritas Development Group LLC. It lists every GTM (go-to-market) Hermes / Claude Code skill the agent is allowed to invoke on this client, organized by **use-case** and **role**.

**Default binding mode:** skills referenced in this file are **available** to the agent — but **never invoked autonomously**. Every GTM action that costs credits, sends outreach, or commits to a workflow requires HITL approval via Dennis + the relevant client reviewer (David Poole for relationship facts, Daniel Bailey for RE advisory).

---

## Use-case bindings

### Signal-Based Outbound
- **Primary:** `buying-signals-6`, `signal-interpreter`, `niche-signal-discovery`
- **Supporting:** `account-intelligence-analyst`, `intent-research`, `strategic-intelligence-briefing`
- **Use when:** identifying CDFIs, family offices, and Christian foundations showing investor intent; sequencing outreach based on signal strength.

### Automated Lead Qualification
- **Primary:** `score`, `account-tier-scoring`, `abm-engagement-scoring`
- **Supporting:** `account-intelligence-analyst`, `icp`, `icp-builder`, `list-architect`
- **Use when:** tiering and scoring inbound investor leads / webinar attendees / co-sponsor inbound against the Veritas ICP (faith-aligned capital, Jackson County MO / KC MSA focus, $1M–$10M check size).

### Contact Data Enrichment
- **Primary:** `gtm-enrichment-planner` + `deepline` (Deepline CLI: `plays` only — NOT `tools execute`; `Limadata`=Canada, `Enformion`/`OpenSOSData`=US-only)
- **Use when:** resolving names → emails at CDFIs and family offices, filling missing fields, validating contact data. **Always** via the `gtm-enrichment-planner` HITL approval gate before any paid run.

### AI Sales Workflow Automation
- **Primary:** `sdr-outbound-rules`, `revops`, `deal-desk-operations`, `cs-operations`
- **Supporting:** `pipeline-review`, `call-scorecards`, `lead-routing`
- **Use when:** codifying repeatable investor-engagement motions — SDR rules, lead routing, deal-desk for capital calls — into agent-executable workflows.

### AI ABM Targeting
- **Primary:** `linkedin-abm-1to1-few-many`, `abm-engagement-scoring`, `account-intelligence-analyst`
- **Supporting:** `account-tier-scoring`, `citation-gap-outreach`, `category-of-one-positioning`
- **Use when:** 1:few ABM programs targeting named Christian foundations and CDFIs; engagement scoring on webinar funnels; personalized investor playbooks.

### AI-Powered Cold Outreach
- **Primary:** `cold-email-strategist`, `cold-email-4-sequence`, `cold-email-first-touch`, `reach-out`
- **Supporting:** `cold-email-preflight`, `cold-email-templates-34`, `cold-call-scripts`, `pain-is-the-pitch`, `bridge-before-cold`, `sdr-outbound-rules`
- **Use when:** end-to-end cold outreach — copy, sequence, preflight checks, follow-ups — across email and LinkedIn to CDFIs / family offices / Christian foundations.

### Intent-Based Prospecting
- **Primary:** `buying-signals-6`, `signal-interpreter`, `pre-ma-offmarket-discovery`
- **Supporting:** `account-intelligence-analyst`, `niche-signal-discovery`, `strategic-intelligence-briefing`
- **Use when:** finding prospects in active buy-mode — recent fund deployment, hiring signals at CDFIs, leadership changes, content engagement (regenerative capital, faith-aligned investing, KC MSA real-estate).

---

## Role-based bindings

### AI SDR
- **Primary:** `sdr-outbound-rules`, `reach-out`, `cold-email-4-sequence`, `linkedin-abm-1to1-few-many`
- **Supporting:** `bridge-before-cold`, `never-guess-an-email`, `gtm-enrichment-planner`, `leadsniper-cli`
- **Use when:** AI SDR workflows — list building, enrichment, sequencing, follow-up. The Veritas investor flywheel IS an AI-SDR motion.

### Sales
- **Primary:** `pain-is-the-pitch`, `positioning-and-story`, `positioning-messaging-designer`, `category-of-one-positioning`
- **Supporting:** `roi-proof-generator`, `call-scorecards`, `founder-led-sales`, `sales-enablement`
- **Use when:** mid-funnel — pitch craft for the 7-touch CDFI outreach, ROI proof for sponsors (deal-by-deal IRR, MOIC), positioning for faith-aligned investor segments.

### Demand Gen
- **Primary:** `lead-magnets`, `lead-sources-guide`, `list-architect`
- **Supporting:** `programmatic-seo`, `ai-seo`, `ads`, `ad-creative`, `seo-topic-prioritization`
- **Use when:** top-of-funnel demand — webinars, content offers (TAM lists, county intelligence, capital-stack explainers), SEO for faith-aligned capital topics.

### RevOps
- **Primary:** `revops`, `revops-hubspot`, `deal-desk-operations`, `pipeline-review`
- **Supporting:** `lead-routing`, `cs-operations`, `call-scorecards`
- **Use when:** Veritas CRM build, pipeline review for the deal pipeline (Prime Lee's Summit, Stonehaven Estates, future deals), lead routing between David (principal) and Daniel (RE advisor).

### CRO
- **Primary:** `cro`, `paywall-upgrade-cro`, `pipeline-review`, `cs-operations`
- **Supporting:** `revops`, `roi-proof-generator`, `churn-prevention`
- **Use when:** C-suite revenue ownership — pipeline health across deals, conversion through the 7-touch cadence, repeat-investor retention (LP base).

---

## How runtime agents consume this file

This file is the **per-client binding**. The runtime rule is:

1. **Read `gtm-enrichment-planner` SKILL.md** for the universal orchestration: which stack layer we're in (Plan → Discover → Enrich → Score → Outreach), the HITL gate format, the credit-cost estimation model, the Deepline CLI rule (`plays` only, NEVER `tools execute`), and the geographic provider rules (`Limadata`=CA, `Enformion`/`OpenSOSData`=US, waterfall otherwise).
2. **Read this file (`_config/gtm-skills.md`)** for the **client-specific bindings**: which skills are bound for each use-case, which are blocked (Demand Gen paid ads = ⛔), which compliance overlay applies (Reg D 506(b) for Veritas), which client reviewers must approve relationship-touching drafts (David for relationships, Daniel for RE advisory).
3. **Compose the runtime plan** by intersecting the two: the layer ordering comes from `gtm-enrichment-planner`'s Skill stack recommendations; the actual skill *names* come from this file's Use-case / Role bindings.

**In practice**, when an agent says "build me a TAM list of faith-aligned investors for Jackson County MO":

- `gtm-enrichment-planner` says: walk Plan → Discover → Enrich → Score → Outreach, with HITL gates between layers, $0 Phase 0 build before any spend.
- This file says: for Veritas, **Signal-Based Outbound** binds `buying-signals-6` + `signal-interpreter` + `niche-signal-discovery` (primary); **Automated Lead Qualification** binds `score` + `account-tier-scoring` + `abm-engagement-scoring` (primary); Demand Gen paid ads are **⛔ blocked**; Reg D 506(b) overlay required.
- The runtime resolves to: `buying-signals-6 → niche-signal-discovery → signal-interpreter → score → account-tier-scoring → cold-email-first-touch (post-preflight)`.

**Client-specific overrides** (above) ALWAYS win over the `gtm-enrichment-planner` defaults. If this file says Demand Gen paid ads are ⛔, the agent does not propose Meta or Google campaigns — even if `gtm-enrichment-planner`'s Demand Gen stack would normally include them.

## Routing — Deepline CLI

All enrichment actions in Veritas route through **Deepline CLI** (`deepline plays` against prebuilt workflows). Never invoke `deepline tools execute` directly. Provider selection is automatic per play's waterfall (Limadata for Canada, Enformion / OpenSOSData for US, others per play's recipe).

- **Binary:** `deepline` (PATH lookup — see `~/.hermes/.env` for `DEEPLINE_*` tokens)
- **Pattern:** `deepline plays run prebuilt/<play-name> --input '<json>' --watch`
- **HITL gate:** Phase 3 approval format from `gtm-enrichment-planner` (assumptions, CSV preview, credits + scope + cap, approval question)
- **Output location:** `~/wiki/clients/veritas-developments/intelligence/<task-slug>/` (canonical Veritas pattern)
- **Audit:** keep `_metadata` lineage columns — `email_source`, `validation_status`, `_metadata.provider` — the trail proves which provider won each lookup.

For non-Deepline enrichment (LeadSniper, Clay), the same HITL gate applies — different tool, same rule.

## Client-specific overrides

| Use case | Bound for Veritas? | Notes |
|----------|--------------------|-------|
| Signal-based outbound | ✅ yes | CDFI / family-office / Christian foundation channel |
| Automated lead qualification | ✅ yes | Investor + co-sponsor inbound scoring against Veritas ICP |
| Contact data enrichment | ✅ yes | **Requires `gtm-enrichment-planner` HITL gate before any paid run** |
| AI sales workflow automation | ✅ yes | Codifying the 7-touch cadence + capital-call workflows |
| AI ABM targeting | ✅ yes | Named-investor lists (CDFIs, foundations) |
| AI-powered cold outreach | ✅ yes | Primary revenue motion — 7-touch sequence |
| Intent-based prospecting | ✅ yes | Active scanning for faith-aligned capital signals |
| By-role RevOps | ✅ yes | CRM build + pipeline review per deal |
| By-role AI SDR | ✅ yes | The investor flywheel IS an AI-SDR motion |
| By-role Sales | ✅ yes | Pitch craft + positioning for faith-aligned capital |
| By-role Demand Gen (paid ads) | ⛔ no | We use content + webinar flywheel, not paid media |
| By-role CRO | ✅ yes | Pipeline + repeat-investor retention |

**Compliance overlay:** every GTM output to investors MUST pass Reg D 506(b) screening (`_config/compliance.md`). The `cold-email-preflight` skill is bound for every send.

---

## HITL gate (binding)

Every GTM action follows this 4-step gate, regardless of use case:

1. **Plan first.** Run `gtm-enrichment-planner` (or the relevant planning skill) and present a credit-cost + workflow-cost estimate to Dennis. Wait for "yes" / "proceed."
2. **Route through Deepline CLI.** Hermes and Claude BOTH route enrichment through Deepline CLI — call `deepline plays` (prebuilt workflows) only. Never invoke `deepline tools execute` directly. Provider selection is automatic: `Limadata` for Canada, `Enformion` / `OpenSOSData` for US, waterfall per play.
3. **Draft outputs to `drafts/<vertical>/`.** Never auto-send outreach or commit to a workflow.
4. **Promote via `VALIDATION_QUEUE.md`.** After Dennis + relevant client reviewer approval, move `.md` to `projects/` / `deliverables/` and execute.

**No exceptions for paid runs.** Deepline, LeadSniper, Clay, and any other credit-consuming provider requires the HITL gate.

**Reg D 506(b) reminder:** investor-touching communications must not be general solicitation. Use the `cold-email-preflight` skill for every send; verify the prospect was either a pre-existing substantive relationship or an accredited investor with a verifiable prior connection. Mark `[COMPLIANCE: securities]` at the top of every investor-facing draft.
