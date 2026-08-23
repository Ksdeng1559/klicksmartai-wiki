# GTM Skills Registry — <client_name>

This file is the **canonical GTM skills binding** for <client_name>. It lists every GTM (go-to-market) Hermes / Claude Code skill the agent is allowed to invoke on this client, organized by **use-case** and **role**.

**Default binding mode:** skills referenced in this file are **available** to the agent — but **never invoked autonomously**. Every GTM action that costs credits, sends outreach, or commits to a workflow requires HITL approval via Dennis + the relevant client reviewer.

---

## Use-case bindings

### Signal-Based Outbound
- **Primary:** `buying-signals-6`, `signal-interpreter`, `niche-signal-discovery`
- **Supporting:** `account-intelligence-analyst`, `intent-research`, `strategic-intelligence-briefing`
- **Use when:** identifying prospects showing intent / buying signals; sequencing outreach based on signal strength.

### Automated Lead Qualification
- **Primary:** `score`, `account-tier-scoring`, `abm-engagement-scoring`
- **Supporting:** `account-intelligence-analyst`, `icp`, `icp-builder`, `list-architect`
- **Use when:** tiering and scoring inbound / scraped leads against ICP + buying signals; routing to SDR / AE queues.

### Contact Data Enrichment
- **Primary:** `gtm-enrichment-planner` + `deepline` (Deepline CLI: `plays` only — NOT `tools execute`; `Limadata`=Canada, `Enformion`/`OpenSOSData`=US-only)
- **Supporting:** `find-qualified-titles`, `linkedin-url-lookup`, `never-guess-an-email`, `leadsniper-cli`
- **Use when:** resolving names → emails, filling missing fields, validating contact data. **Always** via the `gtm-enrichment-planner` HITL approval gate before any paid run. Hermes + Claude BOTH route through Deepline CLI.

### AI Sales Workflow Automation
- **Primary:** `sdr-outbound-rules`, `revops`, `deal-desk-operations`, `cs-operations`
- **Supporting:** `pipeline-review`, `call-scorecards`, `lead-routing`
- **Use when:** codifying repeatable sales motions — SDR rules, routing, deal desk, CS ops — into agent-executable workflows.

### AI ABM Targeting
- **Primary:** `linkedin-abm-1to1-few-many`, `abm-engagement-scoring`, `account-intelligence-analyst`
- **Supporting:** `account-tier-scoring`, `citation-gap-outreach`, `category-of-one-positioning`
- **Use when:** 1:1, 1:few, 1:many ABM programs with named-account lists, engagement scoring, and personalized playbooks.

### AI-Powered Cold Outreach
- **Primary:** `cold-email-strategist`, `cold-email-4-sequence`, `cold-email-first-touch`, `reach-out`
- **Supporting:** `cold-email-preflight`, `cold-email-templates-34`, `cold-call-scripts`, `pain-is-the-pitch`, `bridge-before-cold`, `sdr-outbound-rules`
- **Use when:** end-to-end cold outreach — copy, sequence, preflight checks, follow-ups — across email, LinkedIn, and phone.

### Intent-Based Prospecting
- **Primary:** `buying-signals-6`, `signal-interpreter`, `pre-ma-offmarket-discovery`
- **Supporting:** `account-intelligence-analyst`, `niche-signal-discovery`, `strategic-intelligence-briefing`
- **Use when:** finding prospects in active buy-mode — funding events, hiring signals, leadership changes, content engagement.

---

## Role-based bindings

### RevOps
- **Primary:** `revops`, `revops-hubspot`, `deal-desk-operations`, `pipeline-review`
- **Supporting:** `lead-routing`, `cs-operations`, `call-scorecards`
- **Use when:** RevOps workflows — pipeline review, lead routing, deal desk, CS ops.

### Demand Gen
- **Primary:** `lead-magnets`, `lead-sources-guide`, `list-architect`
- **Supporting:** `programmatic-seo`, `ai-seo`, `ads`, `ad-creative`, `seo-topic-prioritization`
- **Use when:** top-of-funnel demand — content offers, paid ads, SEO, list-building.

### Sales
- **Primary:** `pain-is-the-pitch`, `positioning-and-story`, `positioning-messaging-designer`, `category-of-one-positioning`
- **Supporting:** `roi-proof-generator`, `call-scorecards`, `founder-led-sales`, `sales-enablement`
- **Use when:** mid-funnel — pitch craft, messaging, ROI proof, sales enablement.

### CRO
- **Primary:** `cro`, `paywall-upgrade-cro`, `pipeline-review`, `cs-operations`
- **Supporting:** `revops`, `roi-proof-generator`, `churn-prevention`
- **Use when:** C-suite revenue ownership — pipeline health, conversion, churn.

### AI SDR
- **Primary:** `sdr-outbound-rules`, `reach-out`, `cold-email-4-sequence`, `linkedin-abm-1to1-few-many`
- **Supporting:** `bridge-before-cold`, `never-guess-an-email`, `gtm-enrichment-planner`, `leadsniper-cli`
- **Use when:** AI SDR workflows — list building, enrichment, sequencing, follow-up.

---

## Client-specific overrides

<Add the client's GTM profile here. Example for a real-estate developer raising capital:>

| Use case | Bound for <client_slug>? | Notes |
|----------|--------------------------|-------|
| Signal-based outbound | ✅ yes | |
| Automated lead qualification | ✅ yes | |
| Contact data enrichment | ✅ yes | **Routes through Deepline CLI** (`deepline plays` only, not `tools execute`). Always via `gtm-enrichment-planner` HITL gate before any paid run. Provider: `Limadata` for CA, `Enformion`/`OpenSOSData` for US. |
| AI sales workflow automation | ✅ yes | |
| AI ABM targeting | ✅ yes | |
| AI-powered cold outreach | ✅ yes | |
| Intent-based prospecting | ✅ yes | |

---

## HITL gate (binding)

Every GTM action follows this 4-step gate, regardless of use case:

1. **Plan first.** Run `gtm-enrichment-planner` (or the relevant planning skill) and present a credit-cost + workflow-cost estimate to Dennis. Wait for "yes" / "proceed."
2. **Route enrichment through Deepline CLI.** Both Hermes and Claude call `deepline plays` (prebuilt workflows) only — never `deepline tools execute` directly. Provider selection is automatic: `Limadata` for Canada, `Enformion` / `OpenSOSData` for US, waterfall per play.
3. **Draft outputs to `drafts/<vertical>/`.** Never auto-send outreach or commit to a workflow.
4. **Promote via `VALIDATION_QUEUE.md`.** After Dennis + relevant client reviewer approval, move `.md` to `projects/` / `deliverables/` and execute.

**No exceptions for paid runs.** Deepline, LeadSniper, Clay, and any other credit-consuming provider requires the HITL gate.