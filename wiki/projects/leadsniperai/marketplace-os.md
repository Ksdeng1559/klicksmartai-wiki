---
title: LeadSniperAI Marketplace OS
created: 2026-08-05
updated: 2026-08-05
type: summary
tags: [technology, research, how-to]
sources: [notion: LeadSniperAI Marketplace OS]
related: [lead-sniperai-cli-os, lead-sniperai-signal-cold-email-sop, deepline]
---

# Mission
Build LeadSniperAI Marketplace into a Canadian business-funding lead generation, qualification, verification, scoring, distribution, and monetization operating system.
# Role in the Business OS
This is the **front door for all business funding requests**. Where [www.mortgagesbydenniseng.ca](http://www.mortgagesbydenniseng.ca) is the front door for mortgage clients into Mortgage CoPilot, the `/funding-assessment` funnel and compact-keyword pages documented here are the entry point for Canadian business-funding inquiries. Every funding request enters through this system before qualification, verification, and marketplace or internal routing.
# Operating Model
LeadSniperAI Marketplace OS is the Notion command center for strategy, content, operations, partner onboarding, task management, and weekly/monthly review. Atomic CRM remains the system of record for live CRM operations. Convex powers the external buyer marketplace. Notion manages the business OS, documentation, planning, workflows, SOPs, and executive visibility.
# Core Outcomes
- Generate qualified Canadian business-funding assessment submissions.
- Convert assessments into voice-verified funding opportunities.
- Route opportunities as exclusive, shared, or cross-professional marketplace leads.
- Build a compact-keyword content engine for Canadian business financing.
- Track marketplace revenue, buyer quality, lead quality, and funding outcomes.
- Create a repeatable /goal and /loop operating cadence.
# Dashboard Sections
## 1. Executive Command Center
Use this page as the weekly review hub for:
- Marketplace revenue
- Completed assessments
- Verified applicants
- Discovery interviews
- Tier A opportunities
- Active buyers
- Lead acceptance rate
- Funding outcomes
- Content production velocity
- Top risks and blockers
## 2. Operating Databases
The OS includes these databases:
- LeadSniperAI Lead Pipeline
- Funding Opportunities
- Marketplace Buyers & Partners
- Content Operating System
- Product & Engineering Tasks
- SOP & Knowledge Base
- KPI / Loop Scorecard
## 3. Priority Build Sequence
### Phase 1 — Intake and Qualification
Build the `/funding-assessment` funnel first. Capture consented applicant information, funding purpose, amount, business history, revenue range, credit band, debt profile, timeline, documents, and consent.
### Phase 2 — Opportunity Packaging
Create advisor-ready briefing cards that include company snapshot, funding need, growth intelligence, financial signals, AI opportunity summary, confidence score, completeness score, document-readiness checklist, and lender recommendations.
### Phase 3 — Marketplace Distribution
Support exclusive leads, shared leads, and cross-professional opportunities. Track buyer category, jurisdiction, specialties, deal size, credit balance, subscription status, and lead acceptance quality.
### Phase 4 — Compact Keyword Content Engine
Turn 1–3 word high-intent business-funding keywords into landing pages, comparison hubs, AI-retrievable knowledge assets, assessment entry points, and conversion assets.
### Phase 5 — Monthly /Loop Review
Every month, review what converted, what failed, what content ranked, what buyers purchased, which lead tiers monetized, and what to improve next.
# Lead Product Definition
A saleable Voice-Verified Business Funding Opportunity should include:
- Completed one-minute assessment
- Completed AI discovery interview
- Verified telephone connection
- Confirmed funding amount and purpose
- Business operating history
- Revenue range and financial indicators
- Existing debt profile
- Credit-score range
- Funding timeline
- Available security or owner contribution
- Document-readiness checklist
- Applicant’s stated business objective
- AI-generated opportunity summary
- Confidence and completeness scores
- Human quality-control status
- Timestamped consent to share with approved professionals
# Lead Tiers
<table header-row="true">
<tr>
<td>Tier</td>
<td>Description</td>
<td>Marketplace Use</td>
</tr>
<tr>
<td>Assessment Lead</td>
<td>Completed short intake only</td>
<td>Low-cost nurture or internal review</td>
</tr>
<tr>
<td>Voice-Verified Lead</td>
<td>Assessment + verified phone + discovery</td>
<td>Saleable marketplace opportunity</td>
</tr>
<tr>
<td>Advisor-Ready Opportunity</td>
<td>Complete briefing card + scoring</td>
<td>Premium lead for approved professionals</td>
</tr>
<tr>
<td>Application-Ready Opportunity</td>
<td>Documents and lender fit mostly complete</td>
<td>Highest-value opportunity</td>
</tr>
</table>
# Weekly Operating Cadence
## Monday — Pipeline Review
- Review new assessments
- Assign qualification status
- Identify urgent funding timelines
- Confirm next-step tasks
## Wednesday — Content & SEO Review
- Review keyword pipeline
- Check pages in production
- Assign article/page owners
- Review AI search visibility opportunities
## Friday — Marketplace Review
- Review buyers/partners
- Track sold leads
- Track buyer feedback
- Review accepted/rejected opportunities
- Update lead quality rules
## Monthly — /Loop Review
- What produced revenue?
- What generated qualified leads?
- What content ranked or indexed?
- Which buyer categories performed?
- Which lead tiers had best conversion?
- What should be stopped, improved, or doubled down on?
# Source Context
This OS is based on the LeadSniper Marketplace strategy, the voice-verified opportunity model, the compact-keyword content system, and the business-funding marketplace architecture.
<database url="https://app.notion.com/p/c55a6585b3384761b0b247eceb357a58" inline="false" data-source-url="collection://945ea605-a336-4318-9ece-b32db04b6828">LeadSniperAI Lead Pipeline</database>
<database url="https://app.notion.com/p/da39840685db4a139fb5c0063ccbf697" inline="false" data-source-url="collection://eec3adba-514a-4974-8db6-7fba2e31b4a7">Funding Opportunities</database>
<database url="https://app.notion.com/p/91298b3ce8774275beeeaa4f32ba6481" inline="false" data-source-url="collection://bcdd3a56-25ad-4d78-8c5a-d7d4b1fd6147">Marketplace Buyers & Partners</database>
<database url="https://app.notion.com/p/85fa678904264023bab8b2ea02bd917d" inline="false" data-source-url="collection://8ee6e1b6-469d-4177-acee-33bebbe278bc">Content Operating System</database>
<database url="https://app.notion.com/p/77e91818a5b148e89e0142d88317efcf" inline="false" data-source-url="collection://17e581a1-f7d5-4428-a820-1bfe670a6890">Product & Engineering Tasks</database>
<database url="https://app.notion.com/p/f791eabea03f42faae62cb4caa1ac604" inline="false" data-source-url="collection://41d73faa-a3f3-4c0a-9af4-46905a20e2c4">SOP & Knowledge Base</database>
<database url="https://app.notion.com/p/68ac672ea2d047399ec136d960a7a2a4" inline="false" data-source-url="collection://e31eba5c-abd9-46c4-9076-608927ba2905">KPI / Loop Scorecard</database>
# Enterprise Build-Out — Multi-Tenant Marketplace
## Architectural Decision
The private source inquiry is not the marketplace product. The operating model is:
```plain text
Private inquiry
→ separately consented vertical opportunities
→ immutable qualification snapshots
→ priced marketplace offers
→ reservations and purchases
→ tenant-scoped access grants
→ outcomes and learning
```
This separation allows one business inquiry to create legitimate opportunities across multiple verticals without mixing consent, qualification, pricing, buyers, or outcomes.
## Product Ladder
1. **Assessment Inquiry** — self-reported request with valid intake and purpose consent.
2. **Verified Lead** — contact and material business assertions have verification evidence.
3. **AI-Discovered Lead** — targeted public intelligence, evidence provenance, confidence scoring, and identified opportunity.
4. **Human-Requalified Opportunity** — verified need, timing, fit, consent, and human approval.
5. **Advisor-Ready Opportunity** — complete briefing card, document-readiness, qualification snapshot, and recommended next action.
6. **Lead Generation System** — recurring tenant subscription for acquisition, qualification, routing, and reporting; not unlimited access to personal information.
Each tier is an immutable version. Upgrading a lead creates a new qualification snapshot and commercial offer rather than silently changing what a previous buyer purchased.
## Multi-Tenant Enterprise Model
- **Platform operator:** governs verticals, qualification policies, pricing rules, consent policy, risk, and marketplace integrity.
- **Buyer organizations:** brokers, lenders, accountants, lawyers, insurers, benefits advisors, and other approved professionals.
- **Internal organizations:** Dennis and authorized internal teams receiving assigned opportunities.
- **Partner organizations:** lead suppliers, referral sources, verification providers, and service partners.
- **Users and memberships:** users act through one active organization context; roles and capabilities are checked server-side.
- **Capabilities:** buyer eligibility combines active status, accepted terms, vertical approval, credentials, geography, capacity, and offer rules.
- **Access grants:** cross-tenant protected information is available only after confirmed payment or authorized internal assignment.
## Vertical Expansion Framework
Every industry vertical requires a versioned package:
- Target customer and opportunity definition
- AI discovery interview module
- Consent purpose and distribution language
- Intelligence collection mission
- Qualification and verification policy
- Evidence and freshness requirements
- Buyer credential requirements
- Geography and serviceability rules
- Preview allowlist
- Pricing and distribution rules
- KPI definitions
- Playbooks and compliance review
- Buyer feedback and outcome taxonomy
Initial sequence:
1. Canadian business funding
2. Commercial mortgages
3. Residential mortgages
4. Equipment financing and leasing
5. Accounting and tax advisory referrals
6. Legal and transaction-support referrals
7. Insurance, benefits, and wealth opportunities
8. Repeatable templates for other industries
## AI Discovery and Intelligence Workflow
The AI Discovery Interview captures business objectives, financing needs, operating history, revenue range, timing, constraints, technology, and explicit consent. It also identifies unknowns and produces an Intelligence Mission Brief.
The Mission Planner then selects only relevant collection modules:
- Website intelligence
- Search intelligence
- Business and registry intelligence
- Technology intelligence
- Market and competitor intelligence
- Government and public-program intelligence
- Voice-of-customer intelligence
Every finding must retain source, retrieval date, evidence class, freshness, confidence, and applicable policy basis. AI recommendations remain untrusted until human approval during the MVP.
## System Ownership
- **Notion:** strategy, vertical packages, playbooks, scorecards, objectives, decisions, operating cadence, and executive reporting.
- **Astro/React:** public acquisition, discovery interview, buyer marketplace, and operator interfaces.
- **Convex:** tenants, memberships, inventory, reservations, purchases, access grants, and audit events.
- **Atomic CRM/Supabase:** internal contacts, engagement pipeline, tasks, activities, referrals, and funded outcomes.
- **Stripe:** authoritative payment events, refunds, and disputes.
- **Private data services:** encrypted subject and business identifiers and secure documents.
- **Claude/ChatGPT agents:** planning, intelligence, classification, implementation support, and recommendations within bounded authority.
Notion must not store raw applicant PII, authoritative consent evidence, payment state, or protected purchased-lead data.
## Enterprise Workstreams
### 1. Acquisition
SEO pages, calculators, partnerships, paid media, referral sources, and attribution.
### 2. Discovery and Consent
Progressive intake, AI interview, versioned consent, duplicate detection, withdrawal, and audit.
### 3. Intelligence and Qualification
Mission planning, collection, evidence validation, tier scoring, human review, and PII-free offer preparation.
### 4. Marketplace and Commerce
Buyer onboarding, capability matching, exclusive/shared inventory, reservations, Stripe payment, refunds, and access grants.
### 5. Buyer Success
Contact SLA, outcomes, quality feedback, credits, repeat purchases, subscriptions, and buyer performance.
### 6. Vertical Factory
Reusable interview, policy, scoring, buyer, pricing, content, workflow, and KPI templates for launching new industries.
### 7. Governance
Privacy, security, consent, legal review, agent boundaries, audit, retention, incident response, and change decisions.
## KPI Tree
### North-star measures
- Qualified opportunity revenue
- Funded or successfully completed opportunities
- Buyer repeat purchase rate
- Contribution margin by source, tier, and vertical
### Acquisition
- Assessment starts and completions
- Cost per consented inquiry
- Organic conversion rate
- Source-to-qualified-opportunity rate
### Qualification
- Verification completion rate
- Time to qualification
- Tier advancement rate
- Human rejection and correction rate
- Evidence freshness and completeness
### Marketplace
- Listing rate
- Time to first reservation
- Exclusive sell-through
- Shared-seat utilization
- Revenue per opportunity
- Refund, dispute, and quality-complaint rate
### Buyer success
- Time to first contact
- Lead acceptance
- Outcome reporting completeness
- Repeat purchase and churn
- Revenue and funded volume by buyer
## Implementation Roadmap
1. **Governance foundation:** accept inquiry/opportunity/offer separation, tenant model, consent policy, privacy boundaries, and architecture decisions.
2. **Tenant foundation:** organizations, memberships, roles, vertical capabilities, credentials, territories, and horizontal-access tests.
3. **Discovery intake:** build `/funding-assessment`, progressive save, attribution, consent ledger, private profiles, and deduplication.
4. **Qualification:** opportunity splitting, evidence records, tier snapshots, human review, and PII-free preview tests.
5. **Marketplace:** offer catalog, capability matching, exclusive/shared/internal inventory, and atomic reservations.
6. **Commerce:** Stripe checkout, signed idempotent webhooks, purchases, refunds, scoped access grants, and protected-view audits.
7. **Operations:** Atomic CRM outbox, buyer outcomes, SLAs, quality management, and dashboards.
8. **Vertical factory:** cross-professional consent, reusable vertical packages, subscriptions, and white-label tenant configuration.
9. **Continuous intelligence:** evidence refresh, requalification queues, scorecard updates, and Golden Market Strategy reviews.
## Immediate 30-Day Build Objective
Prove one complete Canadian business-funding path:
- One AI discovery intake
- One versioned consent record
- One private inquiry
- One business-funding opportunity
- One approved qualification snapshot
- One PII-free shared offer with two seats
- Two eligible buyer tenants
- Two reservations and confirmed test payments
- No third purchase
- Two scoped access grants
- Two Atomic CRM opportunity syncs
- Complete audit evidence
## Clarifying Questions and Working Assumptions
- **Lead resale policy:** Working assumption — exclusive sells once; shared has a small disclosed cap; each buyer organization purchases once.
- **Tier upgrades:** Working assumption — upgrades create a new offer version; prior-buyer access or credits require a written commercial policy.
- **Cross-vertical distribution:** Working assumption — every new vertical opportunity requires separate purpose and distribution consent.
- **Buyer licensing:** Working assumption — credentials and permitted geography are enforced per vertical before purchase.
- **AI publication:** Working assumption — AI recommends and drafts; a human approves marketplace publication during MVP.
- **Lead-system product:** Working assumption — this is a recurring service/subscription with quotas and routing rules, not bulk access to source records.
## Definition of Done
A marketplace capability is complete only when authorization, consent, validation, audit events, privacy controls, loading/error states, automated tests, documentation, handoff evidence, and independent review are included.
## Source and Implementation References
- [LeadSniper Marketplace repository](https://github.com/Ksdeng1559/LeadSniperMarketplace)
- Local architecture implementation pack: `implementation/`
- Repository sources: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `CLAUDE.md`, and `convex/schema.ts`
## Change Log
- **2026-07-17:** Added the multi-tenant enterprise build-out, opportunity-based product model, qualification tier ladder, vertical factory, KPI tree, and incremental implementation roadmap.
<page url="https://app.notion.com/p/3a09e94cf0a481fa98aff9a8e9ca384d">LeadSniper AI Marketplace — 60-Day Implementation Plan</page>
# End-to-End Business Funding Lead Workflow
## Workflow Goal
Convert a business owner’s initial interest into a consented, verified, advisor-ready funding opportunity, route it to an eligible buyer, track the application outcome, and feed the results back into the qualification and marketplace systems.
## Workflow Summary
```plain text
Interest captured
→ Funding assessment
→ Consent and contact verification
→ Initial qualification
→ AI discovery interview
→ Intelligence and opportunity analysis
→ Human quality review
→ Advisor-ready opportunity
→ Marketplace matching and offer creation
→ Reservation or internal assignment
→ Protected lead delivery
→ Advisor contact and document collection
→ Application submission
→ Approval, decline, or nurture
→ Outcome capture and scoring improvement
```
## Stage 1 — Interest Capture
### Entry Sources
- `/funding-assessment` landing page
- SEO and compact-keyword pages
- Calculators and comparison pages
- Referral partners
- Paid advertising
- AI chat or voice intake
- Internal advisor referral
- Imported campaign lead
### System Actions
1. Create an anonymous session and attribution record.
2. Capture source, campaign, keyword, landing page, referral partner, and device metadata.
3. Create a draft inquiry only after the lead begins the assessment.
4. Do not expose the lead to marketplace buyers at this stage.
### Exit Criteria
- Applicant has started or completed the assessment.
- Marketing source and campaign attribution are stored.
### Primary Owner
Astro/React acquisition interface with Convex session and intake services.
## Stage 2 — One-Minute Funding Assessment
### Required Fields
- Applicant name and business name
- Email and telephone number
- Province and operating location
- Industry
- Funding amount requested
- Primary use of funds
- Time in business
- Monthly or annual revenue range
- Existing debt profile
- Credit-score range
- Funding timeline
- Security or owner contribution
- Document availability
- Preferred contact method and time
### Consent Requirements
Capture versioned consent for:
- Contact by LeadSniperAI and authorized agents
- AI-assisted discovery and analysis
- Storage and processing of submitted information
- Sharing with approved financing professionals after qualification
- Call recording or transcription where applicable
### System Actions
1. Validate required fields.
2. Run duplicate detection using protected identifiers.
3. Record the exact consent version, timestamp, source, and evidence.
4. Create the private inquiry record.
5. Create an initial Assessment Lead snapshot.
6. Send confirmation by email or SMS.
### Exit Criteria
- Required fields are complete.
- Valid consent exists.
- Contact information passes basic format checks.
- Inquiry is not an unresolved duplicate.
### Failure Routes
- Incomplete assessment → reminder and progressive-save recovery.
- No consent → store only the minimum legally permitted operational record and do not distribute.
- Duplicate → merge or route to human review.
## Stage 3 — Initial Qualification and Triage
### Qualification Dimensions
- Funding need fit
- Revenue and operating-history strength
- Credit range
- Existing debt burden
- Security or owner contribution
- Funding urgency
- Document readiness
- Contactability
- Geography and lender serviceability
- Stated business objective
### Outputs
- Initial fit score
- Completeness score
- Urgency classification
- Recommended discovery path
- Missing-information list
- Risk flags
- Suggested product categories
### Routing Rules
- Strong fit and urgent → immediate discovery invitation.
- Strong fit and non-urgent → scheduled discovery.
- Incomplete but potentially viable → information-request workflow.
- Weak current fit → nurture, education, or alternate referral.
- Fraud, consent, or identity concern → manual hold.
### Exit Criteria
- Lead has a triage status and next action.
- Discovery path or nurture path is assigned.
## Stage 4 — Contact Verification and Discovery Scheduling
### Verification Actions
- Verify telephone connection.
- Validate email deliverability.
- Confirm applicant identity at a proportionate level.
- Confirm that the person has authority to discuss the business.
- Reconfirm contact and sharing consent.
- Schedule or immediately launch the AI discovery interview.
### Automation
- SMS confirmation link
- Calendar booking
- Reminder sequence
- Missed-call and rescheduling workflow
- Escalation to a human agent after repeated failed attempts
### Exit Criteria
- Verified phone connection or documented alternative verification.
- Discovery interview scheduled or completed.
## Stage 5 — AI Discovery Interview
### Discovery Objectives
Confirm the funding request, uncover the real business objective, identify constraints, collect material financial context, and determine the next-best funding route.
### Core Interview Modules
1. Business profile and ownership
2. Funding amount and exact use of proceeds
3. Expected business outcome from funding
4. Revenue, profitability, cash flow, and seasonality
5. Existing loans, leases, liens, CRA obligations, and monthly payments
6. Credit challenges and explanations
7. Assets, collateral, guarantees, and owner contribution
8. Customer concentration, contracts, and recurring revenue
9. Required timing and consequences of delay
10. Available financial and corporate documents
11. Prior applications and lender decisions
12. Applicant preferences regarding rate, payment, term, and security
### Dynamic Follow-Up Logic
The interview agent should ask follow-up questions whenever:
- Values conflict with the assessment.
- The use of funds is vague.
- Revenue does not support the requested amount.
- A material debt or tax issue is disclosed.
- The timeline is unusually urgent.
- Security, contracts, or purchase orders may improve eligibility.
### Agent Output
- Transcript and structured answers
- Confirmed facts versus self-reported estimates
- Contradictions and unresolved questions
- Missing-document checklist
- Applicant’s stated outcome
- Discovery confidence score
- Recommended next action
### Exit Criteria
- Material questions are answered or flagged.
- Verified phone connection is documented.
- Interview transcript and structured record are complete.
## Stage 6 — Intelligence Mission and Opportunity Analysis
### Eve Agent Responsibilities
The Eve funding agent receives the assessment, consent permissions, structured discovery output, and only the external-research permissions required for the case.
### Relevant Intelligence Modules
- Website and business-model analysis
- Search and local-market presence
- Corporate and registry information where legally accessible
- Industry and competitor context
- Government funding and public-program research
- Technology and operating signals
- Public customer, hiring, expansion, or contract signals
### Required Evidence Fields
Every external finding must include:
- Source
- Retrieval date
- Evidence class
- Freshness
- Confidence
- Relevance to the funding decision
- Policy basis for collection
### Opportunity Analysis Output
- Company snapshot
- Confirmed funding request and use of proceeds
- Business objective
- Financial and operating signals
- Strengths
- Risks and inconsistencies
- Suggested funding products
- Potential lender or advisor categories
- Missing documents
- Confidence score
- Completeness score
- Recommended next action
### Example Funding Routes
- Equipment financing
- Working-capital term loan
- Line of credit
- Commercial mortgage
- Invoice financing
- Purchase-order financing
- Revenue-based financing
- Government-backed financing
- Private lending
- Equity or strategic capital referral
### Exit Criteria
- PII-free opportunity summary is generated.
- Evidence and recommendations are traceable.
- Case is ready for human review.
## Stage 7 — Human Quality Assurance
### Reviewer Checklist
- Confirm consent and permitted distribution purpose.
- Confirm the lead is real and contactable.
- Review inconsistencies between intake and discovery.
- Confirm the funding request is plausible.
- Confirm suggested product and buyer categories.
- Review risk and compliance flags.
- Remove unsupported AI claims.
- Confirm preview contains no prohibited PII.
- Assign quality-control status.
### Reviewer Decisions
- Approve as Advisor-Ready Opportunity
- Request more information
- Return for discovery follow-up
- Reclassify funding route
- Route internally
- Place into nurture
- Reject or suppress
### Exit Criteria
- Human approval exists for MVP marketplace publication.
- Immutable qualification snapshot is created.
## Stage 8 — Opportunity Tier Assignment
### Tier Rules
- **Assessment Lead:** completed short assessment only.
- **Voice-Verified Lead:** completed assessment, valid consent, verified contact, and discovery interview.
- **Advisor-Ready Opportunity:** human-approved briefing card, qualification score, buyer fit, and next action.
- **Application-Ready Opportunity:** core documents are substantially complete and submission path is confirmed.
### Versioning Rule
Every material upgrade creates a new immutable qualification snapshot. Previously purchased versions are not silently changed.
## Stage 9 — Marketplace Matching and Offer Creation
### Matching Inputs
- Province and permitted jurisdiction
- Funding amount
- Industry
- Revenue range
- Time in business
- Credit band
- Security type
- Funding product
- Urgency
- Buyer licensing and credentials
- Buyer territory and capacity
- Buyer performance and contact SLA
- Exclusive, shared, internal, or referral distribution rule
### Offer Types
- Exclusive opportunity
- Shared opportunity with a disclosed seat cap
- Internal assignment
- Referral-fee opportunity
- Subscription or quota-based allocation
### Marketplace Preview
The buyer may see only approved PII-free fields before purchase or assignment:
- Industry and province
- Funding amount range
- Funding purpose
- Revenue and time-in-business ranges
- Credit band
- Security indicator
- Timeline
- Opportunity tier
- Completeness and confidence scores
- High-level strengths and concerns
### Exit Criteria
- Eligible buyer set is calculated.
- Price and distribution rules are applied.
- Marketplace offer is published or internally assigned.
## Stage 10 — Reservation, Purchase, and Access Grant
### Commerce Sequence
1. Buyer selects an opportunity.
2. Convex creates an atomic reservation.
3. Buyer completes Stripe checkout or consumes an authorized subscription credit.
4. Signed and idempotent payment event confirms purchase.
5. System enforces exclusive or shared-seat limits.
6. Scoped access grant is created.
7. Protected details become available only to the purchasing organization.
8. Audit event records reservation, purchase, access, and viewer identity.
### Controls
- No access before confirmed payment or authorized assignment.
- One organization cannot purchase the same offer twice unless policy explicitly permits it.
- A shared opportunity cannot exceed its disclosed seat cap.
- A refunded or revoked purchase updates the access grant according to policy.
### Exit Criteria
- Buyer has a valid scoped access grant.
- Lead receives a coordinated introduction notice.
## Stage 11 — Advisor Introduction and Contact SLA
### Buyer Package
- Contact information
- Consent record reference
- Assessment answers
- Discovery summary and transcript access policy
- Opportunity briefing card
- Qualification snapshot
- Risks and missing information
- Document checklist
- Recommended next action
### Service-Level Rules
- Buyer acknowledges receipt immediately.
- First contact target: within 15 minutes during service hours.
- Buyer records disposition within 24 hours.
- Missed SLA triggers reminder, escalation, or reassignment according to commercial policy.
### Lead Communication
Notify the applicant:
- The advisor or organization name
- Expected contact timeframe
- Purpose of the introduction
- How to withdraw or report a problem
## Stage 12 — Document Collection and Application Readiness
### Personalized Checklist Examples
#### General Business Financing
- Six to twelve months of bank statements
- Most recent financial statements
- Current interim statements
- Debt schedule
- Corporate registration documents
- Identification
- CRA statement where relevant
- Use-of-funds breakdown
- Projections or business plan where required
#### Equipment Financing
- Equipment quote
- Vendor information
- Specifications and serial information where applicable
- Down-payment evidence
- Existing equipment obligations
#### Secured Financing
- Property details
- Mortgage statement
- Property-tax statement
- Leases
- Appraisal or valuation
- Corporate ownership documents
### Application-Ready Criteria
- Identity and authority confirmed.
- Required credit authorization captured by the licensed party.
- Material documents received.
- Debt and cash-flow information reconciled.
- Funding product and target lender category selected.
## Stage 13 — Submission and Decision Tracking
### Required Statuses
- Advisor contacted
- Discovery confirmed
- Documents requested
- Documents received
- Application ready
- Submitted to lender
- Additional information required
- Conditional approval
- Approved
- Funded
- Declined
- Withdrawn
- Referred elsewhere
- Follow-up later
- Unable to contact
### Decision Data
- Lender or provider category
- Submission date
- Requested amount
- Approved amount
- Product type
- Rate and fees where permitted
- Conditions
- Decline reason
- Closing or funding date
- Funded amount
### Agent Assistance
Eve may draft:
- Lender submission summaries
- Credit narratives
- Use-of-funds explanations
- Missing-document reminders
- Approval-condition checklists
- Option comparisons
Final advice, suitability determination, credit decision, and regulated activity remain with authorized professionals and lenders.
## Stage 14 — Outcome Capture and Learning Loop
### Outcome Taxonomy
- No contact
- Not interested
- Not qualified
- Information incomplete
- Application submitted
- Conditional approval
- Approved
- Funded
- Declined
- Referred elsewhere
- Follow-up later
### Learning Actions
- Update lead-source quality.
- Update qualification rules.
- Update interview questions.
- Update buyer matching.
- Update offer pricing.
- Update buyer performance score.
- Update content targeting and keyword priorities.
- Identify missing lender or partner categories.
### Monthly Review Questions
- Which sources produced funded opportunities?
- Which assessment fields best predicted qualification?
- Which discovery questions exposed material risk?
- Which opportunity tiers sold and converted best?
- Which buyers met contact and outcome-reporting SLAs?
- Which decline reasons should change acquisition or qualification?
- Which funding products have unmet demand?
## System Responsibility Matrix
<table header-row="true">
<tr>
<td>System</td>
<td>Primary Responsibility</td>
</tr>
<tr>
<td>LeadSniper Marketplace</td>
<td>Acquisition, intake experience, buyer marketplace, previews, and buyer workflow</td>
</tr>
<tr>
<td>Eve</td>
<td>Durable case orchestration, AI discovery, analysis, delegation, approvals, and resumable workflows</td>
</tr>
<tr>
<td>ICM</td>
<td>Business intelligence, qualification logic, scoring models, funding strategies, and outcome frameworks</td>
</tr>
<tr>
<td>n8n</td>
<td>External triggers, messaging, scheduling, integrations, notifications, and legacy workflow connections</td>
</tr>
<tr>
<td>Convex</td>
<td>Tenants, inventory, reservations, purchases, access grants, and audit events</td>
</tr>
<tr>
<td>Atomic CRM / Supabase</td>
<td>Internal relationship record, activities, tasks, referrals, applications, and funded outcomes</td>
</tr>
<tr>
<td>Stripe</td>
<td>Authoritative payment, refund, and dispute events</td>
</tr>
<tr>
<td>Notion</td>
<td>Strategy, SOPs, policies, scorecards, task planning, decisions, and executive review</td>
</tr>
</table>
## Workflow Events
```plain text
assessment.started
assessment.completed
consent.recorded
inquiry.created
qualification.initialized
verification.completed
discovery.scheduled
discovery.completed
intelligence.mission.created
opportunity.analysis.completed
human_review.requested
qualification.approved
opportunity.snapshot.created
marketplace.offer.published
marketplace.offer.reserved
payment.confirmed
access_grant.created
advisor.introduced
advisor.contacted
documents.requested
application.ready
application.submitted
decision.received
opportunity.funded
opportunity.closed
outcome.recorded
scorecard.updated
```
## MVP Build Sequence
### Sprint 1 — Intake and Consent
- Build `/funding-assessment`.
- Implement progressive save and validation.
- Create versioned consent ledger.
- Create private inquiry and Assessment Lead snapshot.
- Implement duplicate detection.
### Sprint 2 — Verification and Discovery
- Implement SMS/email verification.
- Add calendar and reminder workflow.
- Build AI discovery interview schema.
- Store structured answers and transcript references.
- Generate missing-information list.
### Sprint 3 — Qualification and Human Review
- Implement initial scoring.
- Add Eve intelligence mission planner.
- Generate PII-free opportunity briefing card.
- Build human review queue.
- Create immutable qualification snapshots.
### Sprint 4 — Marketplace and Commerce
- Implement buyer capability matching.
- Create exclusive and two-seat shared offers.
- Add atomic reservations.
- Integrate Stripe test payments.
- Create scoped access grants and protected views.
### Sprint 5 — Advisor Operations and Outcomes
- Sync purchased opportunities to Atomic CRM.
- Implement contact SLA tracking.
- Build document-readiness workflow.
- Add application and decision statuses.
- Capture funded and declined outcomes.
### Sprint 6 — Learning Loop
- Build source, tier, buyer, and funding-outcome dashboards.
- Review scoring accuracy and human corrections.
- Update interview, matching, and pricing rules.
- Document the first Golden Market Strategy review.
## Workflow Success Criteria
- At least 80% of completed assessments receive a next-action status automatically.
- At least 70% of contactable qualified leads complete discovery.
- Every published opportunity has valid consent and human approval during MVP.
- No protected lead details are exposed before authorized access.
- Exclusive opportunities cannot sell more than once.
- Shared opportunities cannot exceed the disclosed seat cap.
- Buyers receive purchased opportunities with complete audit evidence.
- Buyer contact time and outcome reporting are measurable.
- Funded, declined, and nurture outcomes feed back into scoring and acquisition decisions.
## Working Assumptions
- Human approval is required before marketplace publication during MVP.
- Notion stores workflow definitions, policies, and scorecards but not raw applicant PII or authoritative consent evidence.
- The licensed advisor or lender owns regulated advice, credit authorization, product suitability, submission, and final funding decisions.
- Shared opportunities initially use a maximum of two buyer seats.
- Applicants can withdraw consent and request suppression through a documented workflow.
## Change Log
- **2026-07-18:** Added the complete business-funding lead workflow from initial interest through discovery, qualification, marketplace purchase, advisor handling, funding outcome, and continuous learning.