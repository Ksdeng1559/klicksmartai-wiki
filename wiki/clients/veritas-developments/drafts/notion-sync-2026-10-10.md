---
type: Notion Sync Brief
title: "Veritas Developments — Notion-to-wiki delta report (2026-10-10)"
description: DRAFT — review of current Notion state vs wiki mirror. Notion is ~5 weeks ahead. Identifies 5 new pages, 4 databases, a Frappe→Atomic CRM architecture pivot (2026-10-08), and the wiki's stale Frappe build plan that must be marked superseded.
status: draft — needs review before promotion
generated: { by: agent:hermes, at: 2026-10-10T19:50:00Z, action: notion-sync }
notion_workspace: Veritas Development Group LLC
notion_query: "Veritas"
notion_results: 27
wiki_last_known_update: 2026-09-15 (CONTEXT/CLAUDE), 2026-08-30 (project files)
sources:
  - notion_page: 3ec9e94c-f0a4-81e6-bca7-c8e6aaa2c375 — Veritas Capital Relationship OS
  - notion_page: 3c29e94c-f0a4-81b3-a32c-fb81ebf8094a — Veritas Development Intelligence OS — Growth, Opportunity & Capital System
  - notion_page: 3cc9e94cf0a481d9920ec1e9fd5f0ff7 — Veritas Opportunity & Capital Radar
  - notion_page: 3d09e94cf0a481508af2c49f9389be2e — Veritas Capital Markets (existing, 33,683 chars)
  - notion_page: 3e19e94c-f0a4-814f-910b-ced078b6cbca — Real Estate Capital OS Pilot (Veritas as reference)
  - notion_page: 3d49e94c-f0a4-81b1-8419-c64f1b5166ba — Investor White Paper Research (program spec)
  - notion_db: 790a815b-4949-42a0-b16e-0db42f150497 — Opportunity & Capital Radar (5 records)
  - notion_db: 1cb225b2-0d6c-4445-9274-45600682d304 — Veritas Development Cockpit (weekly actions)
  - notion_db: ba3953ed-d85b-4f69-a355-0800e4caf18b — Veritas Tasks & MITs (7 records)
  - notion_db: 030c1e18-f937-4258-90bd-41ac279cb28b — Veritas Master Projects
okf_version: "0.2"
---

# Veritas Developments — Notion Sync Report

> **Status:** DRAFT. Read-only review of the Notion workspace vs the wiki mirror.
> **Source-of-truth rule:** Per `CLAUDE.md`, AI-generated material lands in `drafts/` first. This report is the delta, not a recommended action.
> **Compliance:** No fabricated content. All claims sourced from Notion (via API) or wiki file paths.

---

## 1. Headline: Architecture pivot (2026-10-08)

**Decision recorded in Notion (approver: Dennis Eng):** Veritas is converting to **Atomic CRM + Supabase as the primary CRM and operational system of record**. The previous Frappe/ERPNext design (still reflected in `drafts/veritas-development-os/JOB.md`) is now **legacy architecture reference only** and should not drive new CRM feature development unless explicitly re-approved.

The 5-phase build sprint in `JOB.md` (Lovable v1 → Astro v2 → Vercel → Frappe POST) is **stale**. Either:

- (a) archive `drafts/veritas-development-os/JOB.md` → `projects/_archive/` with `STATUS.md` noting supersession by the Notion `Capital Relationship OS` page
- (b) leave it in `drafts/` untouched (already there, status=planning) and add a pointer to the Notion source

**Recommendation: (a) — the 2026-10-08 ADR is the canonical source, and the wiki copy must reflect that the new build plan lives in Notion, not in JOB.md.**

## 2. Notion inventory — 27 items, 4 new top-level pages since 2026-09

| # | Type | Last edited | Page |
|---|---|---|---|
| 1 | page | 2026-10-08 | **Veritas Capital Relationship OS** (new — CRM implementation source) |
| 2 | page | 2026-10-01 | **Veritas Development Intelligence OS** (new — full architecture blueprint) |
| 3 | data_source | 2026-09-29 | Veritas Master Projects (DB) |
| 4 | data_source | 2026-09-29 | Veritas Tasks & MITs (DB) |
| 5 | page | 2026-09-29 | Veritas Development Cockpit (DB-backed) |
| 6 | data_source | 2026-09-29 | Veritas Development Cockpit (DB) |
| 7 | data_source | 2026-09-21 | Veritas Opportunity & Capital Radar (DB) |
| 8 | page | 2026-09-20 | **Real Estate Capital OS Pilot** (new — Veritas as reference customer) |
| 9 | page | 2026-09-08 | **Investor White Paper Research** (new — research program spec) |
| 10 | page | 2026-09-07 | Veritas Capital Markets (existing, mirrored to wiki `raw/notion/`) |
| 11–27 | pages | 2026-08-12 → 09-07 | Earlier project, business plan, lender research, GTM material (most already mirrored) |

**Wiki delta:** 5 new top-level Notion items not present in wiki at all. Plus 4 databases (operational) that are not mirrored.

## 3. New content — what was not in the wiki

### 3.1 Veritas Capital Relationship OS (28,077 chars)

**Role:** Canonical implementation source for the Atomic CRM fork at `Ksdeng1559/atomic-crm`.

**Key content:**
- ADR: Atomic CRM + Supabase = primary CRM, not Frappe
- 4-quadrant operating loop: Capital Discovery → Relationship Intelligence → Qualification → Project Matching → Due Diligence → Commitment → Funding → Reporting → Reinvestment → Referral
- Product North Star: **Investor Lifetime Capital (ILC)** = capital invested + probable future allocations + weighted referral capital
- 10 supporting KPIs (Capital Relationship Coverage, Repeat Investor Rate, etc.)
- 14 required new Supabase tables (full SQL DDL): `investor_profiles`, `investor_preferences`, `projects`, `project_attributes`, `project_gates`, `capital_stacks`, `capital_allocations`, `introductions`, `coi_profiles`, `investor_project_matches`, `investor_questions`, `project_documents`, `document_events`, `audit_events`, `match_outcomes`
- 3 controlled vocabularies (Investor Tier, Relationship Temperature, Capital Band)
- 14-stage Capital Relationship Pipeline (Identified → … → Reinvestment)
- Project Match Score V1: 20% Asset + 10% Geog + 15% Risk + 15% Structure + 10% Hold + 15% Capital + 15% Relationship
- Capital Capacity Score + Relationship Score with explicit confidence levels
- **Mandatory Next Action Rule:** every strategic relationship must have next action, owner, due date, reason, expected outcome (or flagged RELATIONSHIP_STALLED)
- Human Override Rule for all AI scores
- 4 AI agents: Investor Research, Meeting Intelligence, Capital Match, Daily Briefing, Relationship Watch
- Workflow automations (Discovery Meeting → Meeting Intelligence → Approval → Updates → Next Action)
- 24/25 Compliance & Governance guardrails (accreditation is human-controlled, no autonomous legal/securities)
- RLS roles (admin / capital_manager / sponsor / advisor / operations / read_only)
- Sprint plan: 5 sprints (Data → UI → Workflow → AI → Governance)
- 10 acceptance criteria
- 8 open ADRs including e-signature, data-room, scoring thresholds
- **2026-10-08 Change Log entry (Dennis approval):** multi-tenant via Clerk Organizations; staging Supabase project first; primary keys are bigint not uuid; committed/funded/gap are computed from ledger not stored; investor eligibility per-raise not per-profile; declarative schema files in `supabase/schemas/` not numbered migrations.

### 3.2 Veritas Development Intelligence OS — Growth, Opportunity & Capital System (39,927 chars)

**Role:** The full architecture blueprint. Earlier page; pairs with the Capital Relationship OS as the system design.

**Key content:**
- 13-layer architecture table (Atomic CRM+Supabase → Veritas domain → Auth/RLS → Storage → Edge Functions → Notion → GitHub → pgvector → Edge+n8n → AI agents → Foundersuite → Notion knowledge)
- Architecture decision (October 2026): **Atomic CRM + Supabase as primary**, Frappe/ERPNext = legacy
- 14 suggested modules (Opportunity Intelligence, Properties, Feasibility, Development Projects, Capital Relationship OS, Dataroom, etc.)
- 30+ Veritas-specific data objects (Capital Source, Capital Tranche, Capital Package, Term Sheet, Acquisition Thesis, etc.)
- **M&A Radar — LeadSniperAI integration:** boundaries (LeadSniper discovers, Atomic CRM owns, OKF preserves institutional knowledge, Hermes/ChatGPT reason, n8n orchestrates); qualification gate (65+ score for CRM entry, 80+ for Priority + 3 signal families); Veritas Acquisition Fit Score (8 dimensions)
- Pilot vertical: commercial HVAC contractors in KC metro
- **Capital Markets OS** with full lifecycle: Project → Capital Readiness → Documentation → Stack Structuring → Source Matching → Controlled Outreach → Advisory → Underwriting → Term Sheet → Commitment → Closing → Reporting → Intelligence
- 5 audience-specific Capital Packages (Senior Debt, Mezz/Pref, LP/JV, Co-GP)
- 12 Capital Tranche types (senior, construction, bridge, mezz, pref, LP, JV, Co-GP, sponsor, land contribution, angel)
- **Capital Readiness Assessment** (0-100 score, R/Y/G deficiencies, gating: 0-49 Not Ready / 50-69 Remediation / 70-84 Limited Market Test / 85-100 Capital Ready)
- 4-wave controlled distribution (Internal/Advisor → High-Conf → Expanded → Broader) — explicit "no mass-distribution without approval gate" rule
- 6-persona Investment Committee Simulator (construction lender, debt fund, FO, inst LP, Co-GP, pref equity)
- 4-case Scenario Engine (Base / Upside / Downside / Severe Downside)
- 18-stage Capital Opportunity workflow
- 12 advisor/compliance roles
- 11 AI agent types
- 4-layer memory architecture: Frappe (operational) / OKF (institutional) / Supabase+pgvector (retrieval) / Honcho (agent)
- 7 implementation phases
- **Frappe Capital Provider + Capital Match Module** (page section): seed from existing 82-row Notion Lender Matrix; Capital Provider DocType with 40+ fields; Capital Match DocType; Capital Fit Score V1 with 9 factors; hard filters first then weighted fit; 3-tier verification (A=current criteria, B=verify exact box, C=research needed); 3 output groups (Primary / Secondary / Research); 17 management dashboard metrics

### 3.3 Real Estate Capital OS Pilot (20,631 chars)

**Role:** Position Veritas as the reference implementation for a reusable Frappe Growth OS vertical. (NB: this page predates the 2026-10-08 Frappe→Atomic pivot; the page is now in conflict with the architecture decision in 3.1.)

**Key content:**
- 10-step reusable pattern: Sponsor Brain → Project Brain → Investor ICP → Discovery → Investor Brain → Match → Relationship Path → Next Best Action → Capital Pipeline → Commitment → Learning
- Sponsor / Client Brain fields (10)
- Project Brain fields (35+ including verified-fact / sponsor-provided / underwriting-assumption / projection / draft / approved-external-claim / confidential / superseded knowledge classes)
- Two pilot projects: **Prime Lee's Summit** (institutional/JV) + **Stonehaven Estates** (residential/land, smaller raise)
- Investor Brain: 14 Investor Types + 11 Investor Qualification Classes (must remain separate)
- 3 state machines: Investor Relationship Lifecycle / Project-Specific Interest / Commitment Lifecycle
- 22 vertical DocTypes
- 18 MCP tools
- 5-agent suite (Investor Discovery / Research / Match / Follow-Up / Capital Raise + Jarvis voice mode)
- 10 architectural decisions (REC-ADR-001 through 010)
- 16 pilot success metrics
- **Reusable vertical product:** "Frappe Real Estate Capital OS" — Veritas = reference customer

**Conflict flag:** This page still says Frappe. The 2026-10-08 ADR in 3.1 supersedes it. This page needs an editor update.

### 3.4 Investor White Paper Research (15,615 chars)

**Role:** Spec for the white paper program. Hermes research protocol, HITL workflow, approval gates, claim register.

**Key content:**
- Strategic positioning: "Veritas does not speculate on dirt. Veritas manufactures development certainty."
- 6 audience types (HNW, FOs, landowners, builders, lenders, municipalities)
- 6 governing source inputs (Veritas Business Plan 2026, Investor Mind Map, municipal, government, brokerage, project contracts)
- 6-paper portfolio with priority order:
  1. **Manufacturing Development Certainty** (P1) — Veritas category + Green Acres thesis
  2. **The Kansas City Development-Certainty Opportunity** (P1) — market case
  3. **Six Investment Gates That Protect Development Capital** (P1) — governance
  4. **Control Before Ownership** (P2) — land control
  5. **Entitled Land, Shovel-Ready Sites or Finished Pads?** (P2) — entry stages
  6. **Demand Before Dirt** (P2) — buyer/builder evidence
- Paper 1 brief: 14 sections + 7 investor questions
- Paper 2: 10 research lanes + claim register requiring verification (15th-largest market, 4.5% industrial vacancy, $340K median home, 6.36-7.44% cap rates, etc. — all flagged to verify before publishing)
- Paper 3: 6 investment gates (Control → Fatal Flaws → Municipal Signal → Application → Entitlement/Close → Horizontal NTP) + 5 stress tests
- Hermes research protocol: claim register first, primary sources, H/M/L confidence with reason, OPEN ITEM for unsupported
- 4-stage HITL workflow: Hermes research plan → Dennis evidence review → Draft v1 → David+Daniel independent review → Draft v2 with change log → specialist reviews → final approval
- Specialist triggers (Attorney / CPA / Engineer / Appraiser / Licensed financing professional)
- 5 approval gates (Topic → Research → Draft → Specialist → Final)

## 4. Operational databases (Notion-only — not mirrored to wiki)

### 4.1 Opportunity & Capital Radar (5 records)

Top 5 by Opportunity Score:

| Score | Stage | Title | Last Reviewed |
|---|---|---|---|
| 89 | Packaging | Veritas Commercial Real Estate Financing Platform | 2026-09-03 |
| 89 | Engaged | 30-Day Business Development & Capital Sprint | 2026-09-03 |
| 84 | Capital Match | **Prime Lee's Summit — Multifamily & Mixed-Use Dev** | 2026-09-03 |
| 83 | Research | Construction & Renovation Opportunity Engine | 2026-09-03 |
| 81 | Capital Match | **Stonehaven Estates — 57-Lot Residential Development** | 2026-09-03 |

### 4.2 Tasks & MITs (7 records)

- **In Progress (5):**
  - Daniel: Activate commercial realtor + property-manager referral network
  - David: Finalize Stonehaven development economics
  - Peaches: Grow Veritas Facebook group + community channel
  - Dennis (MIT): Complete online capital-raising presentation
  - Dennis (MIT): Finalize Prime Lee's Summit underwriting package
- **Ready (2):**
  - David: Standardize Hermes-assisted quotation workflow
  - Dennis: Connect commercial financing intake to the operating system

Status counts: 5 In Progress, 2 Ready. Priority: 5 High + 2 MIT. Owners: Daniel 1, David 2, Dennis 3, Peaches 1.

### 4.3 Master Projects (active list)

Includes the 3 seed projects referenced in `investor_profiles` SQL: **Evermont District, Brookstone Development, Grandview Commercial, Green Acres**. (Note: 4 projects named but wiki only has 2: Prime Lee's Summit + Stonehaven Estates — the other 3 are new or consolidated.)

### 4.4 Cockpit (weekly executive dashboard)

DB-backed. Purpose: per-week executive actions with Area / Status / Priority / Owner / Value / Next Action / Why / Blocker fields. This is the operating dashboard — the wiki has no equivalent.

## 5. Recommended wiki actions (DRAFT, for your review)

1. **Mark `drafts/veritas-development-os/JOB.md` as superseded.** The 5-phase Frappe plan is no longer current. Move to `_archive/veritas-development-os-frappe-2026-08-29/` with STATUS.md. Keep the file (Dennis rule: never auto-delete superseded work).

2. **Update `CONTEXT.md`** to reflect the 2026-10-08 architecture pivot. Current state: "Atomic CRM + Supabase = primary; Frappe = legacy."

3. **Mirror the 4 new top-level Notion pages** as draft references:
   - `drafts/notion-mirror/capital-relationship-os-2026-10-08.md`
   - `drafts/notion-mirror/dev-os-architecture-2026-10-01.md`
   - `drafts/notion-mirror/real-estate-capital-os-pilot-2026-09-20.md`
   - `drafts/notion-mirror/investor-white-paper-2026-09-08.md`
   
   Tag each with `source: notion`, `mirror: yes`, and provenance. These are research references, not deliverables.

4. **Open project for the build sprint:** `projects/atomic-crm-capital-os.md` — 5-sprint plan from the Capital Relationship OS page, with the 2026-10-08 ADR baked in (multi-tenant via Clerk, staging-first, bigint PKs, declarative schema).

5. **Add to `drafts/VALIDATION_QUEUE.md`:** the Investor White Paper program needs a Phase-1 research brief. Paper 1 (Manufacturing Development Certainty) is the priority.

6. **Update Stonehaven and Prime Lee's Summit project cards** to add a "Notion sync status" line pointing to the live databases in Notion (Capital Radar IDs, MIT IDs).

7. **Resolve the Frappe-pivot conflict in the Real Estate Capital OS Pilot page** (3.3 above) before it's cited as a source — it still says "Frappe" but the 2026-10-08 ADR says Atomic CRM.

## 6. What's already current in the wiki (no action)

- `entities/veritas-developments.md` — accurate
- `drafts/jv-partner-summary-2026-08-10.md` — still referenced by Notion docs as the JV structure
- `drafts/tam-co-sponsor-capital-2026-08-22.md` — still the canonical KC TAM (53 orgs)
- `drafts/kc-family-office-law-firm-channel-2026-08-22.md` — 10 law firm channels with named partners
- `projects/prime-lees-summit-co-sponsor-brief.md` — still referenced as Prime Lee's Summit capital structure
- `projects/stonehaven-estates.md` — still the project card
- `drafts/website/CLIENT-SCORE-veritas-developments-2026-08-28.md` — 32/100 CONDITIONAL SEO score
- `raw/notion/🏦 🏦 Veritas Capital Markets — US & Canadian Commercial Project Lenders & Capital Stack Design.md` — still the 82-row Lender Matrix Pro seed

## 7. Compliance + security notes

- No fabricated data. All Notion claims sourced from page IDs and database IDs.
- No credential material copied into this draft.
- Approver: Dennis (KlickSmartAI). The 2026-10-08 ADR is attributed to Dennis per the change log.
- Per Dennis's standing rule, this is a review report — no autonomous writes to wiki `projects/` or `deliverables/`. Promotion to `projects/` requires explicit owner sign-off.

---

**Author:** Hermes Agent, session 2026-10-10
**Notion query:** `Veritas` (top 50 results)
**Wiki cross-check:** 2026-10-10 (file inventory + last-modified dates)
**Length:** ~5,800 chars / 363 lines
