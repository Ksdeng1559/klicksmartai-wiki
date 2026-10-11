---
title: "[MIRROR] Veritas Development Intelligence OS — Growth, Opportunity & Capital System"
type: notion-mirror
source: notion
notion_page: 3c29e94c-f0a4-81b3-a32c-fb81ebf8094a
mirrored: 2026-10-10
mirrored_by: agent:hermes
last_edited_in_notion: 2026-10-01
status: read-only reference — superseded in places by 2026-10-08 Atomic CRM ADR
not_source_of_truth_because: "Notion is the canonical source. This file is a research reference."
conflicts:
  - "Section 'Architecture' was correct as of 2026-10-01. As of 2026-10-08, Veritas converted to Atomic CRM + Supabase as primary CRM (see drafts/notion-mirror/capital-relationship-os-2026-10-08.md). Frappe/ERPNext designs are now legacy."
related_drafts:
  - drafts/notion-sync-2026-10-10.md
  - drafts/notion-mirror/capital-relationship-os-2026-10-08.md
okf_version: "0.2"
---

# [MIRROR] Veritas Development Intelligence OS

> **NOTION IS THE CANONICAL SOURCE.** This is a read-only mirror. If this file disagrees with Notion, Notion wins.
> **CONFLICT NOTE:** This page still references Frappe as the system of record. As of 2026-10-08, Veritas converted to Atomic CRM + Supabase. Treat Frappe references here as historical.

## North-Star Operating Model

**Relationship → Lead → Opportunity → Property → Feasibility → Project → Capital Stack → Construction / Development → Reporting → Referral / Repeat Business**

Principle: **Atomic CRM + Supabase manage the business, the approved knowledge layer preserves what the business learns, and AI connects operational data, documents and workflows.**

## 13-Layer Architecture (as of 2026-10-01)

| Layer | Technology | Responsibility |
|---|---|---|
| Primary CRM / operational system of record | Atomic CRM + Supabase Postgres | Contacts, companies, deals, opportunities, properties, projects, capital relationships, tasks, activities, workflow state |
| Veritas domain layer | Atomic CRM extensions + Supabase schema | Development opportunities, properties, feasibility, projects, Green Acres gates, capital stacks, allocations, investor profiles, referrals, dataroom metadata |
| Identity / authorization | Supabase Auth + RLS | User identity, access control, record-level permissions |
| Files / dataroom | Supabase Storage + approved external dataroom | Project files, investor documents, signed URLs, access events, document sharing |
| Server-side automation | Supabase Edge Functions | Webhooks, enrichment, scoring, external API calls, MCP endpoints, secure automation |
| Institutional knowledge | Notion + approved durable knowledge artifacts | SOPs, strategy, decisions, project intelligence, lessons learned; durable approved artifacts versioned in GitHub |
| Version control | GitHub | Atomic CRM code, Supabase migrations, Edge Functions, schemas, workflows, technical audit history |
| Semantic retrieval | Supabase Postgres + pgvector | Semantic retrieval across approved documents, project intelligence, relationship knowledge |
| Workflow orchestration | Supabase Edge Functions first; n8n only where cross-system orchestration materially simplifies | Triggers, integrations, enrichment, communications, scheduled jobs |
| AI / agent execution | Atomic MCP + Hermes + ChatGPT/OpenRouter | Research, scoring, project/investor matching, meeting intelligence, brief generation, monitoring, human-approved actions |
| Capital-source discovery | Foundersuite + approved research sources | Discover investors, lenders, capital partners; qualified relationships written into Atomic CRM |
| Knowledge / planning workspace | Notion | Human-readable strategy, PRDs, SOPs, planning and executive documentation linked to operational system |

**Architecture decision (October 2026):** Atomic CRM + Supabase as primary CRM and operational system of record. Frappe/ERPNext designs are legacy architecture references only.

## Atomic CRM Application Structure

Extend `Ksdeng1559/atomic-crm` repository rather than creating a separate CRM. Veritas-specific business logic via reusable React modules, Supabase tables/views/functions, RLS policies and Edge Functions while preserving Atomic CRM's standard contacts, companies, deals, notes, tasks.

**Suggested modules (14):** Opportunity Intelligence, Properties, Development Feasibility, Development Projects, Construction / Rehab, Capital Relationship OS, Capital Stacks & Allocations, Referral Partner Network, Investors / Lenders / Family Offices, Dataroom, Vendors / Partners, Reporting, AI / Automation, M&A Radar / Acquisition Intelligence.

## Veritas-Specific Data Model

**CRM foundation (reuse):** Contact, Company, Deal, Activity, Notes, Tasks, Tags, Users.

**Veritas-specific objects (40+):** Veritas Opportunity, Property, Development Feasibility, Development Project, Due Diligence Item, Referral Partner, Referral Opportunity, Relationship, Capital Source, Capital Requirement, Capital Readiness Assessment, Capital Stack Scenario, Capital Tranche, Capital Package, Capital Opportunity, Capital Match, Capital Exposure, Capital Committee Memo, Underwriting Request, Capital Condition, Term Sheet, Term Sheet Comparison, Capital Commitment, Investor/Lender Mandate, Dataroom, Dataroom Document, Construction Phase, Scope of Work, Estimate, Change Order, Draw Request, Project Milestone, M&A Candidate, Transaction Signal, Acquisition Thesis, Acquisition Scorecard, Owner/Succession Profile, Buyer/Acquirer Profile, M&A Opportunity Brief, Acquisition Pipeline, Acquisition Diligence Item.

## M&A Radar — LeadSniperAI Integration

**Operating decision:** LeadSniperAI CLI = discovery + pre-M&A signal engine. Atomic CRM + Supabase = system of record for qualified candidates. Veritas OS should not rebuild LeadSniperAI logic inside Atomic CRM.

**System boundary:**
- **LeadSniperAI CLI:** market discovery, Google Business Profile universe creation, snapshots, time-series change detection, founder-dependency analysis, enrichment orchestration, transaction-readiness signals, pre-M&A scoring, buyer discovery, M&A Opportunity Brief generation.
- **Deepline:** identity resolution, owner/leadership enrichment, contact enrichment, firmographics, validation waterfalls.
- **Atomic CRM + Supabase:** qualified M&A Candidate record, relationship owner, pipeline stage, human verification, NDA, financial review, valuation, LOI, diligence, capital stack, closing workflow.
- **OKF:** approved acquisition theses, signal patterns, diligence lessons, transaction outcomes, institutional M&A knowledge.
- **Hermes / ChatGPT / OpenRouter:** research, interpretation, thesis generation, scoring explanation, diligence support, recommendations.
- **n8n:** scheduled CLI runs, API orchestration, Atomic CRM/Supabase synchronization, monitoring, approved notifications/actions.

**Canonical M&A sequence:** Industry → Company Universe → Owner → Transaction Signals → LeadSniper Score → Human Verification → Atomic CRM M&A Candidate → Acquisition Thesis → Relationship Outreach → NDA → Financial Review → LOI → Capital Stack → Diligence → Acquisition → Integration → Outcome Intelligence.

**Qualification gate before Atomic CRM creation:** LeadSniper score 65+, or strategically important regardless of score, or human review confirms credible thesis. **Priority Acquisition** = 80+ + at least 3 independent signal families.

**Atomic CRM M&A Candidate minimum fields:** Company/legal entity, industry/geography, owner/founder/key execs, revenue/EBITDA estimates with confidence labels, LeadSniper pre-M&A stage, LeadSniper score and explanation, strongest supporting signals, disconfirming signals, strategic fit, succession/founder-dependency hypothesis, digital and operational value-creation gaps, seller-financing/rollover/earn-out hypothesis, relationship path/warm intro, acquisition thesis, recommended next action, last verified date, pipeline stage.

**M&A pipeline (22 stages):** Identified → Enriched → Scored → Watchlist → Priority Candidate → Human Verified → Owner Contacted → Relationship Established → Owner Interested → NDA → Financials Received → Preliminary Valuation → Management Meeting → LOI Preparation → LOI Submitted → LOI Accepted → Due Diligence → Capital Secured → Closing → Integration → Closed/Learning Captured.

**Veritas Acquisition Fit Score (8 components):** Strategic fit 20, Financial quality 20, Ownership/succession fit 15, Operational improvement potential 15, Financing/seller-note feasibility 10, Integration synergies 10, Exit/multiple-expansion 5, Relationship advantage 5.

**Initial Veritas pilot:** KC metro, one vertical. Recommended first vertical: commercial HVAC contractors, then plumbing, electrical, roofing, restoration, excavation/site services, property management.

## Capital Markets Operating System

Capital raising = **operating process, not an outreach campaign**. Veritas OS controls readiness, structuring, matching, exposure, underwriting, closing lifecycle before broad outreach.

**Operating sequence:** Project → Capital Readiness → Documentation → Capital Stack Structuring → Capital Source Matching → Controlled Outreach → Advisory Governance → Due Diligence → Term Sheet → Commitment → Closing → Reporting → Capital Market Intelligence.

### 1. Capital Readiness Assessment

Score factors: sponsor strength + track record, site control/ownership, zoning/entitlements, development budget completeness, sources and uses, market evidence/feasibility, appraisal/valuation support, sponsor equity + liquidity, LTC/LTV, projected DSCR, exit strategy, financial model completeness, projected investor returns, entity/legal structure, dataroom completeness.

**Output:** readiness score 0-100, R/Y/G deficiencies, blocking issues, remediation owner, outreach authorization status.

**Gating:** 0-49 Not Capital Ready, 50-69 Remediation Required, 70-84 Limited Market Test, 85-100 Capital Ready.

### 2. Institutional Capital Package

Audience-specific packages, not one generic deck:
- **Senior Debt Package** — collateral, LTC, LTV, repayment, guarantees, construction budget, exit
- **Mezzanine / Preferred Equity Package** — basis, priority, downside protection, intercreditor structure, cash flow, target return
- **LP / JV Equity Package** — IRR, equity multiple, waterfall, sponsor economics, market opportunity, exit
- **Co-GP Package** — sponsor capability, GP contribution, development economics, promote, governance, portfolio opportunity

### 3. Capital Stack Structuring

Tranche types (12): Senior debt, Construction debt, Bridge debt, Mezzanine, Preferred equity, LP equity, JV equity, Co-GP capital, Sponsor equity, Landowner contribution / contributed land, Angel / seed capital where appropriate.

Each scenario calculates total capitalization, debt/equity mix, LTC, LTV, weighted cost of capital, sponsor cash requirement, pref, promote economics, projected returns.

### 4. Capital Source Intelligence & Matching

Foundersuite = discovery. Atomic CRM = qualified capital relationship + investment mandate.

**Investor/Lender Mandate fields:** capital type, typical check size, min/max investment, asset classes, geography, project stage, development type, LTC/LTV limits, required sponsor equity, recourse requirements, min DSCR, target return/IRR/pref, hold period, track-record requirements, guarantee requirements, relationship owner, warm introduction path, last verified date.

**Capital Match Agent** calculates `Capital Fit Score` per Project × Capital Source: Project characteristics → Capital requirement → Provider mandate → Relationship strength → Fit score → Priority.

### 5. Controlled Capital Outreach

**Capital Exposure** ledger tracks every release of a project: project, capital source, individual recipient, introduction source, date exposed, package/version, NDA status, dataroom access, engagement status, feedback, decline reason, requested changes, relationship owner, next action.

**Staged distribution (4 waves):**
- Wave 0 — Internal / advisor validation
- Wave 1 — Highest-confidence relationships
- Wave 2 — Expanded qualified shortlist
- Wave 3 — Broader controlled distribution if required

**No mass-distribution without explicit approval gate.** Purpose: reduce over-shopping risk, preserve market reputation.

### 6. Investment / Credit Committee Simulator

AI agents challenge opportunity from multiple capital-provider perspectives before external outreach.

**6 review personas:** construction lender / credit officer, debt fund, family office, institutional LP, Co-GP investor, preferred-equity investor.

Simulator challenges land basis, valuation, sponsor equity, absorption, construction cost, delay risk, recourse, exit assumptions, comparable projects, downside protection.

**Capital Committee Memo output:** investment thesis, strengths, weaknesses, unresolved risks, likely committee objections, required evidence, proposed mitigants, recommendation (proceed / remediate / reject).

### 7. Underwriting & Scenario Engine

Every capitalized project maintains: Base Case, Upside Case, Downside Case, Severe Downside Case.

Variables: interest rates, development costs, sales price, rent, cap rate, absorption, development timeline, loan sizing, LTC, LTV, sponsor equity, pref, promote, IRR, equity multiple.

Goal: **return resilience**, not only headline returns.

### 8. Capital CRM Lifecycle

20-stage workflow: Project Identified → Readiness Review → Remediation → Capital Stack Approved → Sources Matched → Outreach Authorized → Initial Conversations → NDA → Dataroom → Indicative Interest → Term Sheet → Underwriting → Conditions → Documentation → Commitment → Funding → Reporting → Closed.

Every stage has required exit criteria.

### 9. Advisor & Compliance Governance

**5 roles:** Sponsor / Developer (project decisions), Capital Strategy (structure, materials, sources), Licensed Capital Professional (regulated activities), Legal / Accounting (entity, securities, tax, documentation), AI Agent (research, scoring, drafting, monitoring within approved permissions).

### 10. Due Diligence & Closing Control

Linked objects: Underwriting Request, Diligence Item, Capital Condition, Term Sheet, Commitment, Closing Item.

Lifecycle: Initial Interest → Underwriting → Information Requests → Risk Resolution → Term Sheet → Conditions → Documentation → Funding.

Track owner, requested date, due date, status, dependencies, version, evidence.

### 11. Term Sheet Comparison

Normalizes competing proposals across: proceeds, pricing/interest rate, fees, LTC/LTV, amortization, maturity, extension options, recourse/guarantees, covenants, reserves, prepayment, participation/warrants/equity economics, pref/promote, closing conditions, execution risk.

Recommendation engine compares **certainty of execution and total economic cost**, not merely quoted interest rate.

### 12. Capital Market Intelligence

Every capital interaction improves Veritas knowledge base. Capture structured decline/acceptance reasons: geography, asset class, project stage, sponsor track record, LTC/LTV, sponsor equity, recourse, minimum check size, return requirement, concentration limit, timing, documentation, market concern.

Aggregate into: which providers actively funding a particular project type, common LTC limits, sponsor equity expectations, return thresholds, recourse requirements, reasons projects fail underwriting, which structures generate highest conversion.

**Capital learning loop:** Capital conversation → outcome → structured reason code → OKF knowledge → Supabase retrieval → Capital Matching Agent → better next recommendation.

**Capital module data ownership:** Foundersuite discovers, Atomic CRM owns qualified relationships/mandates/matching/exposures/underwriting/term sheets/commitments, Dataroom owns controlled document distribution, OKF preserves durable lessons, Supabase/pgvector retrieves approved intelligence, Hermes/ChatGPT/OpenRouter reason, n8n orchestrates.

**Capital operating principle:** Veritas should not build a database of people who have money. It should build institutional intelligence about what capital wants, why it invests, why it declines, and how each development must be structured to become financeable.

## Referral Partner Network

Implement directly in Frappe (legacy) / Atomic CRM (current).

**8 stages:** Prospect → Qualified → Trigger Aligned → Activated → First Referral → Productive → Strategic → Dormant.

Track profession, firm, partner class, geography, service lines, referral triggers, relationship owner, fit score, relationship strength, reciprocity opportunities, activity history, generated opportunities.

Referral Opportunities link to Veritas Opportunities so Veritas can measure referral quality, proposals, wins, revenue, gross profit, source performance.

## Relationship Intelligence

A relationship record should describe why a person or organization matters, not merely who they are.

Track relationship type, strength, strategic importance, relationship owner, introduction path, history, last interaction, next action.

Enables AI to reason: **Who is most likely to encounter the next Veritas opportunity?**

## Google Open Knowledge Framework (OKF) Layer

OKF = portable institutional-knowledge layer using Markdown + structured metadata + version control.

**Recommended knowledge domains (11):** company strategy, projects, properties, capital strategy, referral network, development playbooks, market intelligence, SOPs, decisions, research, lessons learned.

OKF metadata for provenance, trust, freshness, lifecycle, verification so AI agents can distinguish current verified knowledge from stale or unverified assumptions.

## Frappe → OKF Publishing Loop (as written 2026-10-01)

**Frappe event → background job / n8n → knowledge agent → determine if knowledge-worthy → create or update OKF concept → Git commit / review**

Example: Frappe records that a lender was rejected because it required unacceptable recourse. OKF preserves institutional lesson explaining when non-recourse capital is preferred.

## Four-Layer Memory Architecture

- **Frappe (legacy) / Atomic CRM (current) — operational memory** — Transactional facts, workflow state, projects, relationships, opportunities, financial status
- **OKF — institutional memory** — Strategy, SOPs, decisions, research, assumptions, lessons learned, explainable project context
- **Supabase / pgvector — retrieval memory** — Semantic index of approved OKF concepts and documents
- **Honcho — agent memory** — Cross-session conversational context, learned preferences, agent continuity

## Automation Architecture

Use native Frappe workflows + background jobs for deterministic internal rules. Use n8n for multi-system orchestration.

Examples: New opportunity → assign owner, High opportunity score → executive alert, Referral received → SLA follow-up task, Due diligence expiration → alert owner, Foundersuite capital source → enrich → qualify → sync to Frappe, Frappe opportunity → AI qualification → approved outreach workflow.

## AI Agent Layer (11 agents)

- **Opportunity Agent** — classify + score incoming opportunities
- **Referral Intelligence Agent** — recommend which partners Veritas should cultivate
- **Capital Readiness Agent** — score financeability, identify blocking issues, recommend remediation
- **Capital Structuring Agent** — test capital-stack scenarios, recommend structures
- **Capital Matching Agent** — match projects with lenders, investors, Co-GP/JV partners
- **Capital Committee Agent** — simulate lender/investor committee review
- **Capital Exposure Agent** — monitor controlled distribution, outreach waves, feedback, over-shopping risk
- **Underwriting Agent** — track information requests, diligence conditions, missing evidence, closing dependencies
- **Land Intelligence Agent** — analyze parcels, landowner signals, zoning, development potential
- **Investor Relations Agent** — track interests, follow-ups, project fit, commitments
- **Project Intelligence Agent** — monitor milestones, risks, budgets, diligence, missing documentation
- **Knowledge Publisher Agent** — convert validated operational learning into OKF knowledge

## Data Ownership Rule

Avoid maintaining duplicate master records across Frappe, Attio, Notion, Foundersuite.

**Atomic CRM is the master operational database** (per 2026-10-08 ADR; previously Frappe).
- Foundersuite discovers capital sources
- Attio may activate outbound relationships
- Notion documents strategy + planning
- OKF preserves institutional knowledge
- Supabase indexes approved knowledge
- Honcho retains agent context
- All material business outcomes write back to Atomic CRM

## Implementation Phases (7)

1. **Foundation** — Deploy Atomic CRM, Supabase Postgres/Auth/Storage/Edge Functions, GitHub + Veritas-specific Atomic modules. Implement Lead, Contact, Organization, Deal, Veritas Opportunity, Property.
2. **Business development** — Referral Partner, Referral Opportunity, Relationship, opportunity scoring, activity tracking, automated follow-ups.
3. **Development** — Development Project, Feasibility, Due Diligence, Development Budget, Project Milestones.
4. **Capital Markets OS** — Capital Readiness Assessment, Capital Requirement, Capital Stack Scenario, Capital Tranche, Capital Source, Investor/Lender Mandate, Capital Match, Capital Package, Capital Exposure, Capital Opportunity, Term Sheet, Underwriting Request, Capital Condition, Capital Commitment, Foundersuite integration. **Ship with 3 mandatory controls before scaling outreach:** Capital Readiness Gate, Capital Fit Score, Capital Exposure Ledger.
5. **Dataroom** — document classification, project-level permissions, approved investor/lender access, audit history.
6. **AI and knowledge** — Connect Hermes, OpenRouter, OKF, GitHub, Supabase, Honcho, n8n. Implement initial opportunity, referral, capital-matching, knowledge-publishing agents.
7. **Back office** — Introduce ERPNext capabilities for accounting, procurement, vendors, invoices, project/job costing when operational maturity justifies expansion.

## Architectural Principle

**Veritas should not build a CRM that simply stores contacts. It should build a Development Intelligence System that understands the relationships between people, properties, projects, capital, decisions and opportunities.**

## Frappe Capital Provider + Capital Match Module (page section)

Connect qualified Veritas development opportunities directly to structured capital-stack execution. Converts existing lender and capital-source intelligence into searchable, scored, auditable matching engine inside Frappe.

**System of record:** Existing **Lender Matrix Pro — US & Canada** = seed dataset for the Frappe **Capital Provider** DocType. Notion remains useful for research + knowledge management, but Frappe becomes the transaction system of record for active capital matching, outreach, commitments, closing.

**Core DocType — Capital Provider (40+ fields):** Provider Name, Provider Type, Country, Geography/Eligible States, Capital Segment, Capital Layers, Asset Classes, Development Stage, Minimum Loan/Investment, Maximum Loan/Investment, Maximum LTC, Maximum LTV, Minimum DSCR where relevant, Recourse Preference, Sponsor/Guarantor Requirements, Minimum Sponsor Liquidity, Minimum Sponsor Net Worth, Deal Size Range, Construction/A&D Appetite, Horizontal Development Appetite, Land Appetite, Bridge Appetite, Permanent Financing Appetite, Mezzanine Appetite, Preferred Equity Appetite, JV/Co-GP Appetite, Broker Channel, Submission Requirements, Relationship Owner, Primary Contact, Last Verified Date, Verification Tier, Source/Evidence URL, Internal Notes, Historical Veritas Outcomes.

**3 Verification Tiers:**
- **Tier A** — Current criteria supported; eligible for automated shortlisting
- **Tier B** — Active verify exact box; secondary candidate, must verify before outreach
- **Tier C** — Research needed; research lead only; do not present as verified financing recommendation

AI must never invent missing leverage, pricing, geography, loan-size, recourse, eligibility criteria.

**Core DocType — Capital Requirement:** Project, Property, Asset Class, Geography, Development Stage, Total Project Cost, Current Value, Stabilized/Completed Value, Sponsor Equity, Existing Capital, External Capital Required, Senior Debt Requirement, Subordinate Debt Requirement, Preferred Equity Requirement, LP/JV Equity Requirement, Co-GP Requirement, Target LTC, Target LTV, Required Closing Date, Recourse Constraints, Sponsor Liquidity, Sponsor Net Worth, Entitlement Status, Construction Status, Capital Readiness Status.

**Core DocType — Capital Match:** One record per Project × Capital Provider pairing. Required fields: Project, Capital Requirement, Capital Provider, Capital Layer, Fit Score, Verification Tier, Eligibility Status, Match Rationale, Conflicts/Exceptions, Missing Information, Human Review Status, Approved for Outreach, Relationship Owner, Outreach Status, Outcome, Decline Reason, Term Sheet Received, Last Reviewed.

**Capital Fit Score (9 factors):** Capital-layer fit 20%, Asset-class fit 15%, Geographic fit 15%, Deal-size fit 15%, Development-stage fit 10%, Leverage/structure fit 10%, Sponsor/guarantor fit 5%, Relationship strength 5%, Historical Veritas outcome 5%.

Score is ranking tool, not approval decision. Hard eligibility failures override high numerical score.

**Matching Logic:** Apply hard filters first (geography, capital-layer, asset-class, deal-size, development-stage, provider exclusions). Then return 3 groups: **Primary Matches** (high fit + Tier A), **Secondary Matches** (plausible fit requiring verification), **Research Candidates** (potential sources with insufficient mandate data).

**Recommendation Output:** Why the provider fits, which capital-stack layer, approximate amount sought, verified criteria used, unknown criteria requiring confirmation, conflicts/weaknesses, last verification date, recommended next action. Never state provider WILL fund; state provider is a **candidate match based on verified criteria**.

**Human Validation Gate:** Before any lender/investor contact, authorized Veritas capital professional reviews: project underwriting, proposed capital stack, provider eligibility, current mandate verification, compliance classification, submission package readiness.

**Outreach + Outcome Learning:** Every provider interaction feeds structured intelligence back into Capital Provider record: Interested, Passed, Declined, Outside mandate, Leverage too high, Deal too small/large, Geography issue, Sponsor issue, Entitlement issue, Construction-stage issue, Pricing issue, Documentation issue, Timing issue, Term sheet issued, Closed.

**Management Dashboard (17 metrics):** Capital required across active projects, Capital matched, Capital committed, Capital funded, Remaining capital gap, Number of Tier A matches per project, Average Fit Score, Capital-provider response rate, Term-sheet conversion rate, Commitment conversion rate, Closing conversion rate, Average days from Capital Ready to Term Sheet, Average days from Term Sheet to Funding, Decline reasons by provider and project type.

**Initial Build Sequence (10 steps):**
1. Recreate/sync existing Notion Lender Matrix as Frappe Capital Provider master
2. Build Capital Requirement DocType linked to Project underwriting
3. Build Capital Match DocType
4. Implement deterministic hard filters
5. Implement weighted Fit Score
6. Add Tier A/B/C verification governance
7. Add human approval workflow
8. Connect approved matches to Capital Outreach and activity tracking
9. Add Term Sheet and Commitment records
10. Feed outcomes back into provider intelligence record

**Design principle:** **Frappe calculates and ranks; verified data supplies the facts; AI explains the match; qualified humans approve the capital strategy and outreach.**

---

**Mirror compiled by:** Hermes Agent, 2026-10-10
**Source page size:** 39,927 chars
**Wiki mirror size:** ~9,200 chars (compressed for indexing)
**Sync status:** Read-only. Conflict noted for 2026-10-08 Atomic CRM pivot.
