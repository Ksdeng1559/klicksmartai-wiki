---
title: "[MIRROR] Real Estate Capital OS Pilot — Veritas as Reference Implementation"
type: notion-mirror
source: notion
notion_page: 3e19e94c-f0a4-814f-910b-ced078b6cbca
mirrored: 2026-10-10
mirrored_by: agent:hermes
last_edited_in_notion: 2026-09-20
status: read-only reference — SUPERSEDED by 2026-10-08 Atomic CRM ADR
not_source_of_truth_because: "Notion is the canonical source. This file is a research reference."
conflicts:
  - "This page was written 2026-09-20 and still positions Veritas as Frappe-based. The 2026-10-08 ADR in 'Veritas Capital Relationship OS' converts Veritas to Atomic CRM + Supabase. Frappe references here are LEGACY."
  - "The 'reusable vertical product' (Frappe Real Estate Capital OS) was the pre-ADR plan. Post-ADR, the reusable vertical lives in Atomic CRM."
related_drafts:
  - drafts/notion-sync-2026-10-10.md
  - drafts/notion-mirror/capital-relationship-os-2026-10-08.md
  - drafts/notion-mirror/dev-os-architecture-2026-10-01.md
okf_version: "0.2"
---

# [MIRROR] Real Estate Capital OS Pilot

> **NOTION IS THE CANONICAL SOURCE.** This is a read-only mirror.
> **CONFLICT:** This page predates the 2026-10-08 Atomic CRM ADR. It still says "Frappe." Post-ADR, Veritas is on Atomic CRM. This page's reusable vertical concept survives, but the implementation platform changed. Treat all Frappe references as legacy.

## Vertical Decision (as written 2026-09-20)

Use Veritas Development as the reference implementation for a reusable **Real Estate Capital OS** vertical on top of the Frappe Agentic Business Operating System. Goal: discover, qualify, match, cultivate and advance investor and capital relationships for active real-estate projects while preserving project truth, investor mandates, relationship history, approvals, outcomes in Frappe.

## Why Veritas Is the Pilot

Veritas has the ingredients:
- Multiple real-estate development projects
- Project-specific capital requirements
- Investor, lender, co-GP and sponsor targeting
- Relationship-led capital development
- Existing Opportunity & Capital Radar logic
- Project underwriting and capital-stack work
- Active GTM and outreach planning

This makes Veritas a practical laboratory for turning the generic Frappe Growth OS into a specialized Real Estate Capital OS.

## Vertical Architecture

```
Veritas Client Brain → Project Brain → Investor ICPs
Project Brain → Capital Mandate / Raise
Investor ICPs → Investor Discovery Agent → Investor Brain / Profile
Investor Brain + Capital Mandate → Project × Investor Matching Engine
Match → Relationship Path / Connector Intelligence
→ Next Best Action → Frappe Investor CRM (legacy: Atomic CRM)
→ Outreach / Intro / Meeting / Diligence
→ Soft Circle / Commitment / Funding
→ Outcome + Learning → OKF Knowledge → back to Project Brain + Investor ICPs
```

**Reusable pattern (10 steps):** Sponsor Brain → Project Brain → Investor ICP → Investor Discovery → Investor Brain → Matching → Relationship Path → Next Best Action → Capital Pipeline → Commitment → Learning.

## Sponsor / Client Brain

Veritas remains the tenant-level Client Brain.

**Contains:** sponsor identity, development strategy, track record, target markets, asset classes, project portfolio, sponsor positioning, approved claims, relationship owners, capital-raising guardrails, communication approvals, legal/compliance review rules, current priorities.

Client Brain is shared across projects; each Project Brain is project-specific.

## Project Brain

Each capital-raising project requires its own governed Project Brain.

**Fields (35+):** Project Name, Sponsor, Property/Site, Location, Asset Class, Project Type, Development Stage, Entitlement Status, Project Summary, Business Plan, Total Project Cost, Capital Stack, Senior Debt, Preferred Equity, LP/JV Equity, Sponsor Equity, Capital Required, Current Raise/Tranche, Minimum Investment, Investor Type, Target Hold Period, Distribution Structure, Preferred Return where approved, Residual Split where approved, Exit Strategy, Timeline, Key Risks, Risk Mitigants, Sponsor Track Record, Approved Claims, Approved Materials, Data Room Status, Legal/Compliance Status, Last Reviewed Date.

**Knowledge discipline (8 classes):** Verified Fact, Sponsor-Provided Fact, Underwriting Assumption, Projection, Draft, Approved External Claim, Confidential, Superseded. **No agent should treat an underwriting assumption as a verified fact.**

## Initial Veritas Project Pilots

### Pilot A — Prime Lee's Summit

Use existing capital-raise planning as the first institutional/JV investor matching case.

**Primary test:** project-specific Project Brain, capital requirement, institutional investor ICP, family-office ICP, co-GP/co-sponsor ICP, investor matching, relationship-path discovery, controlled diligence pipeline.

### Pilot B — Stonehaven Estates

Use as a simpler residential/land-development capital case where appropriate.

**Primary test:** smaller raise profile, individual accredited investor / family office targeting, project fit scoring, relationship-led outreach, soft-circle and commitment tracking.

Two pilots should test whether the same vertical architecture can support different project sizes and capital structures.

## Investor Brain

Create an Investor Brain / Capital Source Profile for both qualified investors and earlier-stage potential investors. Must distinguish a researched prospect from a qualified investor — discovery does not imply eligibility, interest, mandate fit, or approval for solicitation.

**Investor / Capital Source Type (15):** Individual Investor, Accredited/Eligible Individual Investor where appropriately documented, High-Net-Worth Individual, Family Office, Multi-Family Office, RIA/Wealth Manager, Real Estate Fund, Private Equity/JV Capital, Institutional Investor, Co-GP/Co-Sponsor, Syndicator, Strategic Developer/Operator, Private Lender, Debt Fund, Bank/Credit Union, Other Capital Source, Connector/Introducer.

**Connector/Introducer** may facilitate access to capital without being the direct investor and should not be counted as committed capital.

**Investor Qualification Class (11):** Potential Investor, Researched Prospect, Potential Fit, Qualified Investor, Interested Investor, Active Diligence, Soft Circle, Committed Investor, Funded Investor, Nurture, Declined/Not a Fit.

Investor Type and Investor Qualification Class must remain separate. Example: a Family Office may be only a Potential Investor until mandate, check size, current appetite, decision makers, project fit are verified.

**Investor Brain fields (25+):** Investor/Organization Name, Investor Type, Geography, Decision Makers, Relationship Owner, Introduced By, Relationship Strength, Asset Classes, Preferred Markets, Development Stage Preference, Risk Profile, Typical Check Size, Minimum Check Size, Maximum Check Size, Debt/Equity Preference, Direct/Fund Preference, Hold Period Preference, Return/Structure Preference where evidenced, Prior Investments, Similar Projects, Current Mandate, Mandate Evidence, Mandate Freshness, Liquidity/Timing Signal where known, Accreditation/Eligibility Status where lawfully documented, Last Contact, Current Interest, Objections, Next Action, Confidentiality Level, Source/Provenance.

## Investor ICPs

Investor ICPs become structured Frappe (legacy: Atomic CRM) objects.

**Example ICP — Family Office:** real-estate allocation, development or value-add interest, relevant geography, typical check size aligned with project tranche, direct-investment capability, professional diligence capability, long-duration capital tolerance, relationship-driven process.

**Example ICP — Accredited Individual:** legally appropriate investor eligibility, passive real-estate interest, check size aligned with offering minimum, compatible hold horizon, compatible risk profile, appropriate jurisdiction and solicitation status.

**Example ICP — Institutional JV/PE Capital:** defined asset-class mandate, project-size fit, institutional diligence process, geography fit, investment-committee structure, relevant development-stage appetite, minimum transaction size aligned to project.

ICPs reusable across projects but versioned as mandate strategy changes.

## Investor Discovery Agent

```
Project Brain
→ Capital Requirement
→ Investor ICP
→ Existing CRM Search
→ Existing Connectors
→ Public / Licensed Research
→ Candidate Investor
→ Identity Resolution
→ Mandate Evidence
→ Duplicate Check
→ ICP Fit
→ Human Qualification Gate
→ Investor Brain
```

**Operating rule:** Search existing relationships and warm paths before paying for enrichment or initiating cold outreach. Do not create a qualified Investor record solely because a name appears in a directory.

## Project × Investor Matching Engine

**Suggested explainable score (8 dimensions, total 100):**

| Dimension | Weight |
|---|---|
| Investor mandate fit | 25 |
| Check-size fit | 20 |
| Asset-class fit | 15 |
| Geographic fit | 10 |
| Risk/structure fit | 10 |
| Relationship strength | 10 |
| Timing/current mandate | 5 |
| Prior similar investment evidence | 5 |

System must preserve each component score and evidence. Do not hide the rationale behind a single blended number.

## Relationship Intelligence

Fundraising should prioritize relationship paths.

**Create / reuse:** Relationship Path, Connector Profile, Introduction Status, Warm Path Score, Connector Economic Value, Introduction Outcome.

**Example:**
```
David Poole
→ Existing Connector
→ Family Office Principal
→ Prime Lee's Summit
```

Jarvis/agent should answer: "Who can introduce us to the top five investors for this project?" with evidence for each path.

## Capital-Raise Pipeline (3 separate state machines)

### A. Investor Relationship Lifecycle (6 stages)
Potential Investor → Researched Prospect → Potential Fit → Qualified Investor → Active Relationship → Nurture/Inactive. Describes the person or organization independent of any one project.

### B. Project-Specific Investment Interest (10 stages)
Identified for Project → Match Reviewed → Outreach/Introduction Approved → Contacted → Interested → Meeting → NDA → Data Room → Diligence → Soft Circle / Declined / Nurture. Belongs to the Investor × Project relationship.

### C. Commitment Lifecycle (6 stages)
No Commitment → Indication/Soft Circle → Documentation → Committed → Funded → Closed. Belongs to the capital commitment itself.

**Separation matters because:** a person can be a Potential Investor without being qualified; a qualified investor may fit one project but not another; an investor can be interested in several projects simultaneously; soft circles are not commitments; commitments are not funded capital until closing conditions are satisfied.

One investor can maintain a long-term relationship record while holding multiple project-specific Investor Interest and Capital Commitment records over time.

## Core Vertical DocTypes (22)

**Reuse from Growth OS:** Client Brain, ICP Profile, Knowledge Object, Knowledge Source, Agent Run, Agent Action, Next Best Action, Contact, Organization, Deal/Opportunity, Relationship Path.

**Add for Real Estate Capital OS:** Development Project, Project Brain, Capital Requirement, Capital Tranche, Investor Profile, Investor Organization, Investor Type, Investor Qualification Class, Investor Mandate, Investor Interest, Capital Match, Capital Exposure, Due Diligence Record, Data Room Access, Soft Circle, Capital Commitment, Capital Raise, Investment Package, Investor Meeting, Capital Outcome.

Extend the shared Growth OS rather than form a second CRM.

## MCP Tool Set (18 tools)

`get_project_brain(project_id)` / `get_capital_requirement(project_id)` / `get_active_raise(project_id)` / `search_investors(filters)` / `get_investor_profile(investor_id)` / `get_investor_mandate(investor_id)` / `match_investor_to_project(investor_id, project_id)` / `get_top_project_matches(project_id)` / `get_relationship_paths(investor_id)` / `create_investor_interest(...)` / `update_investor_stage(...)` / `create_investor_task(...)` / `record_investor_meeting(...)` / `record_soft_circle(...)` / `record_commitment(...)` / `get_raise_dashboard(project_id)` / `get_overdue_investor_followups(project_id)` / `get_capital_gap(project_id)`.

## Capital Raise Agent

Monitors active raise and recommends actions.

**Example briefing:**
```
Target Raise: $X
Committed: $X
Soft Circled: $X
Remaining: $X

High-Fit Uncontacted Investors: X
Interested but Stalled: X
Meetings This Week: X
Diligence Open: X
Overdue High-Value Follow-Ups: X
```

Answers: "What are the highest-value actions to advance this raise today?" and creates the Next Best Action queue.

## Jarvis — Real Estate Capital Mode (post-ADR: Atomic CRM voice mode)

Voice commands operate on the same vertical.

**Examples:**
- "Give me the Prime Lee's Summit capital briefing."
- "Who are our ten highest-fit investors?"
- "Which of them have warm introduction paths?"
- "Why did this family office score 86?"
- "Prepare a briefing for David before the call."
- "Show everyone in diligence who has not been contacted in seven days."
- "What is the remaining capital gap?"

Jarvis uses: **Project Brain + Investor Brain + OKF + current CRM state + active raise context.**

## Capital Exposure Ledger

For investor fundraising, track exactly what information was disclosed.

**Capital Exposure records:** Project, Investor, Contact, Material Sent, Version, Date, Approved By, Disclosure/NDA Status, Channel, Notes. Audit trail for decks, models, underwriting, data-room access, other project materials.

## OKF for Real Estate Capital

OKF layer governs reusable and project-specific knowledge.

**Knowledge types (15):** Sponsor Fact, Project Fact, Underwriting Assumption, Capital Structure, Approved Investor Claim, Risk Factor, Risk Mitigant, Market Research, Comparable Project, Capital Partner Insight, Investor Mandate Evidence, Objection Handling, Diligence FAQ, Legal/Compliance Rule, Capital Raise Learning.

Every item preserves provenance, approval state, freshness, sensitivity, allowed use.

## Compliance Boundary

Support relationship intelligence and capital operations without treating AI as legal or securities counsel.

**Require explicit human/qualified-review approval for:** offering terms, securities-law determinations, accreditation/eligibility representations, return representations, investor-facing financial projections, subscription documents, general solicitation decisions, cross-border investor outreach, legal disclosures, final investor materials, binding commitments.

Agent can organize, research, score, draft, summarize, recommend. Should not independently decide that a solicitation or offering structure is legally permissible.

## Veritas Migration / Reuse Strategy

Do not discard existing Veritas OS work. Map current concepts into the vertical:

| Existing Veritas Concept | Real Estate Capital OS Mapping |
|---|---|
| Veritas Client Profile | Sponsor / Client Brain |
| Development Project | Development Project + Project Brain |
| Capital Requirement | Capital Requirement + Capital Tranche |
| Investor / Lender Mandate | Investor Mandate |
| Capital Match | Project × Investor Match |
| Relationship Path | Relationship Intelligence |
| Opportunity & Capital Radar | Discovery + Monitoring Agents |
| Capital Exposure | Disclosure / Material Audit Ledger |
| Radar Outcome | Capital Outcome + OKF Learning Candidate |

Existing Veritas work becomes implementation evidence for the reusable vertical rather than a competing architecture.

## MVP for Veritas (6 phases)

**Phase 1 — Model the sponsor and projects:** Veritas Client Brain, Prime Lee's Summit Project Brain, Stonehaven Project Brain, capital requirements, approved project knowledge.

**Phase 2 — Investor CRM:** Investor Profile, Investor Organization, Investor Mandate, Relationship Path, Investor ICP.

**Phase 3 — Matching:** Capital Match, explainable score, match review queue, warm-path ranking.

**Phase 4 — Capital Pipeline:** Investor Interest, meetings, NDA/data room, diligence, soft circles, commitments, funded state.

**Phase 5 — Agents:** Investor Discovery Agent, Investor Research Agent, Matching Agent, Follow-Up Agent, Capital Raise Agent, Jarvis Capital Mode.

**Phase 6 — Learning:** funded/declined outcomes, investor objections, mandate accuracy, relationship path effectiveness, match-score calibration, OKF learning review.

## Pilot Success Metrics (16)

- Qualified investor candidates discovered
- Percent with verified mandate evidence
- Percent with warm paths
- Match-review acceptance rate
- Intro-to-meeting conversion
- Direct outreach-to-meeting conversion
- Meeting-to-diligence conversion
- Diligence-to-soft-circle conversion
- Soft-circle-to-commitment conversion
- Committed/funded capital
- Days from investor identification to meaningful engagement
- Stale-investor recovery
- False-positive match rate
- Relationship-path effectiveness
- Capital attributed to each source/connector

## Reusable Vertical Product (legacy framing)

> **Veritas Real Estate Capital OS — a reusable Growth OS vertical for sponsors, developers and capital-raising teams.**

Veritas = reference customer / pilot.

**Reusable vertical supports:** sponsor onboarding, project onboarding, investor ICP creation, investor discovery, investor research, project × investor matching, relationship intelligence, capital-raise workflow, diligence, commitment tracking, Jarvis voice operation, governance, institutional learning.

**POST-2026-10-08 NOTE:** The "Frappe" framing here is legacy. The reusable vertical concept survives but lives in Atomic CRM. The vertical name and DocType list remain valid; only the implementation platform changed.

## Architectural Decisions (10)

- REC-ADR-001 — Vertical: Real Estate Capital OS is a vertical module of the Growth OS
- REC-ADR-002 — Pilot: Veritas Development is the initial reference implementation
- REC-ADR-003 — Sponsor Brain: Veritas Client Brain owns sponsor-level context
- REC-ADR-004 — Project Brain: Each project has a separate governed Project Brain
- REC-ADR-005 — Investor Brain: Investor profiles store mandates, relationships, project-specific interest
- REC-ADR-006 — Matching: Project × Investor Match is explainable and evidence-backed
- REC-ADR-007 — Relationships: Warm-path and connector intelligence are first-class objects
- REC-ADR-008 — Pipeline: Investor relationship, project interest, capital commitment are separate states
- REC-ADR-009 — OKF: Project and investor knowledge use provenance, approval, freshness controls
- REC-ADR-010 — Compliance: Material investor-facing claims and regulated actions remain human-controlled

**POST-2026-10-08 NOTE:** REC-ADR-001 should be updated to "Atomic CRM Growth OS" instead of "Frappe Growth OS." Other ADRs unchanged in spirit.

## Core Product Statement

> **Frappe stores the investor relationship and capital workflow. The Project Brain defines the investment opportunity. The Investor Brain defines capital fit. The Matching Engine connects the two. Relationship Intelligence finds the warm path. Agents drive the next action. OKF governs what can be trusted and communicated.**

**POST-2026-10-08 NOTE:** "Frappe" → "Atomic CRM" in the first sentence.

---

**Mirror compiled by:** Hermes Agent, 2026-10-10
**Source page size:** 20,631 chars
**Wiki mirror size:** ~5,400 chars (compressed for indexing)
**Sync status:** Read-only. 2026-10-08 ADR supersedes the Frappe framing throughout.
