---
title: LeadSniperAI CLI — Signal-Based Cold Email Operating System
created: 2026-08-05
updated: 2026-08-05
type: summary
tags: [how-to, guide, technology, research]
sources: [notion: LeadSniperAI CLI — Signal-Based Cold Email Operating System]
related: [lead-sniperai-signal-cold-email-sop, deepline]
---

# Executive Summary
This document defines the operating system for building and running a signal-based cold email program using the LeadSniperAI CLI.
The system is designed around one principle:
> Cold email is not the product. It is a controlled actuator inside a larger opportunity-intelligence, buyer-matching, compliance, and feedback system.
LeadSniperAI must determine what outcome is being pursued, identify the correct decision-maker, detect observable evidence of pain or intent, qualify the opportunity, record evidence and compliance data, generate a reviewable value-first message, and route the response into the correct next step.
The system supports two connected commercial rails:
```plain text
Rail A — Buyer Acquisition
Discover lead buyers
→ detect demand and capacity signals
→ qualify buyer requirements
→ secure trial or conditional purchase commitments

Rail B — Opportunity Generation
Discover businesses or prospects with observable needs
→ qualify and verify the opportunity
→ match it to eligible buyers or services
→ route, sell, or distribute the opportunity
```
The initial rule is:
> Buyer demand, buyer criteria, geography, lead economics, and compliance rules should be validated before expensive opportunity generation begins.
# 1. System Outcome
## Primary Outcome
Build a repeatable cold email operating system that uses LeadSniperAI CLI to convert observable business signals into qualified conversations, buyer commitments, appointments, and revenue.
## Economic Drivers
The system can generate revenue through:
- Lead sales
- Shared or exclusive opportunity distribution
- Qualified appointment delivery
- AI employee implementation
- Local growth and intake optimization services
- Buyer subscriptions or marketplace access
- Referral fees where legally and contractually permitted
- Financing and advisory mandates
## Trust-Meter Doctrine
Prospect trust starts at zero.
- Reply requires approximately 7/10 trust.
- Sale or commercial commitment requires approximately 8/10 trust.
- Every system interaction must increase trust through relevance, evidence, clarity, restraint, and permission.
Trust is reduced by:
- Generic targeting
- Unsupported claims
- Incorrect personalization
- Premature meeting requests
- Links and tracking in the first touch
- Unverified contact details
- Lack of lawful-use evidence
- Repeated or irrelevant follow-ups
# 2. Product Positioning
LeadSniperAI should be positioned as:
> An AI-operated business opportunity intelligence, qualification, and routing engine.
It should not be positioned as:
- A bulk Google Maps scraper
- A mass email blaster
- A system that fabricates buying intent
- A tool that treats guessed contacts as verified
- A campaign generator without evidence, compliance, or feedback controls
# 3. Architectural Model
```plain text
Human Operator or AI Agent
        ↓
LeadSniperAI Skill or Approved MCP Client
        ↓
Canonical LeadSniper CLI Command Contract
        ↓
LeadSniper Domain Services and Policy Engine
        ↓
Discovery, Signal, Audit, Scoring, Matching, Compliance
        ↓
Deepline Contact and Delivery Layer
        ↓
Provider Waterfalls, Email Verification, Delivery Adapters
        ↓
CRM, Marketplace, Buyer Network, Outreach Platform
        ↓
Replies, Acceptance, Conversion, Revenue, Feedback
```
## Architectural Boundaries
LeadSniperAI owns:
- Vertical strategy
- Market selection
- Outcome definition
- Signal classification
- Evidence requirements
- Opportunity scoring
- Buyer scoring
- Matching logic
- Compliance state
- Economics
- Campaign orchestration
- Feedback and optimization
Deepline owns:
- Contact sourcing
- Provider waterfalls
- Work-email lookup
- Email verification
- External research adapters
- Outbound-provider adapters
Deepline does not determine:
- Which vertical should be targeted
- What a signal means
- Whether a company is qualified
- Whether an opportunity should be sold
- Whether a message is strategically appropriate
# 4. Canonical CLI Command Taxonomy
All previous command structures should be reconciled into one stable LeadSniper-owned command contract.
```plain text
leadsniper
├── config
├── vertical
├── market
├── discover
├── entity
├── contact
├── signal
├── evidence
├── audit
├── qualify
├── score
├── match
├── economics
├── campaign
├── asset
├── outreach
├── workflow
├── job
├── export
├── compliance
└── system
```
## 4.1 Vertical Commands
```bash
leadsniper vertical list
leadsniper vertical show mortgage-brokerage
leadsniper vertical validate mortgage-brokerage
leadsniper vertical activate mortgage-brokerage
```
Each vertical package must define:
- Entity types
- Decision-maker personas
- Observable signals
- Eligibility rules
- Exclusions
- Opportunity classifications
- Buyer requirements
- Compliance rules
- Scoring weights
- Recommended value assets
- Approved outreach angles
## 4.2 Discovery Commands
```bash
leadsniper discover businesses
leadsniper discover buyers
leadsniper discover people
leadsniper discover opportunities
```
Discovery finds candidates. It does not automatically qualify them.
## 4.3 Entity Commands
```bash
leadsniper entity enrich
leadsniper entity inspect
leadsniper entity merge
leadsniper entity refresh
```
Provider enrichment belongs under entity management.
## 4.4 Contact Commands
```bash
leadsniper contact find
leadsniper contact waterfall
leadsniper contact verify
leadsniper contact refresh
```
Every contact result must include:
- Value
- Source
- Discovery timestamp
- Verification timestamp
- Verification status
- Confidence
- Evidence type
- Compliance state
## 4.5 Signal Commands
```bash
leadsniper signal scan
leadsniper signal classify
leadsniper signal refresh
leadsniper signal explain
```

### Signal Family Build Status
The six diagram families map to implemented generators as follows. MVP output is the current acceptable surface; any family marked **FUTURE** is NOT built yet and must not be assumed available.

| Signal family | Status | Generator / evidence source |
|---|---|---|
| Website signals | ✅ IMPLEMENTED (MVP) | `analyze-reviews` website axis + SiteDoctor PageSpeed (score, LCP/CLS/FCP/TTFB, top bottlenecks w/ savings ms) |
| Growth signals | ✅ IMPLEMENTED (MVP) | `enrich-tavily-full` → `growth_signals[]`, funding_status, hiring_roles, is_hiring |
| Competitive signals | ✅ IMPLEMENTED (MVP) | `seo-audit` competitors/advantages + Tavily `competitive_advantages[]`, market_position |
| Conversion issues | ✅ IMPLEMENTED (MVP) | Website intake audit: booking, click-to-call, contact form, after-hours intake |
| Reputation / review-intelligence | ✅ IMPLEMENTED (MVP) | `analyze-reviews` → health score, phase, rescue number, 30d velocity, theme share %, `place_topics` bridge |
| Risk signals | ✅ IMPLEMENTED (MVP) | `risk_signals[]` (layoffs, negative press, legal), news sentiment trend |
| Firmographic / tech stack | ✅ IMPLEMENTED (MVP) | `tech_stack[]` (software-change → SaaS buying), presence/enrichment scores, establishment date |
| Decision-maker & contact | ✅ IMPLEMENTED (MVP) | `search-decision-makers`, verified emails/phones, LinkedIn |
| Offer gaps | 🔜 **FUTURE — post-MVP** | Proposal: `~/wiki/drafts/leadsniperai-offer-gap-signal-proposal.md`. Inferred today only (review themes + `generate-recommendations`). Requires validation pilot (20 businesses / 2 verticals, precision ≥70% per rule) before build. No dedicated CLI command yet. |
| SEO/AEO opportunities | 🔜 **FUTURE — post-MVP** | Planned: `seo-audit` keywords (volume/CPC) + DataForSEO AI-Opt LLM-mention data. Explicitly deferred — add later. |
| GMB-grounding signals | 🔜 **FUTURE — post-MVP** | Proposal: `~/wiki/drafts/leadsniperai-gmb-signal-engine-proposal.md`. Unanswered Q&A, owner response rate, photos→AI-vision, category changes, post history. |

"⛔ NO signal means no outreach" still governs: FUTURE families must not be used as outreach hooks until implemented and validated.

## 4.6 Score Commands
```bash
leadsniper score fit
leadsniper score urgency
leadsniper score opportunity
leadsniper score buyer
leadsniper score evidence
leadsniper score composite
```
## 4.7 Matching Commands
```bash
leadsniper match opportunity-to-buyers
leadsniper match buyer-to-opportunities
leadsniper match explain
leadsniper match reserve
```
## 4.8 Asset Commands
```bash
leadsniper asset diagnostic
leadsniper asset audit
leadsniper asset brief
leadsniper asset loom-outline
leadsniper asset case-breakdown
```
## 4.9 Outreach Commands
```bash
leadsniper outreach generate
leadsniper outreach approve
leadsniper outreach queue
leadsniper outreach send
leadsniper outreach stop
```
Generation, approval, and sending remain separate. Sending is disabled by default until compliance, infrastructure, and human-review gates pass.
# 5. Deprecation Map
<table header-row="true">
<tr>
<td>Existing Command</td>
<td>Canonical Replacement</td>
</tr>
<tr>
<td>`search local`</td>
<td>`discover businesses`</td>
</tr>
<tr>
<td>`lead enrich`</td>
<td>`entity enrich`</td>
</tr>
<tr>
<td>Deepline `enrich`</td>
<td>`contact waterfall`</td>
</tr>
<tr>
<td>Vertical-specific `enrich`</td>
<td>`entity enrich --vertical`</td>
</tr>
<tr>
<td>`intelligence signals`</td>
<td>`signal scan`</td>
</tr>
<tr>
<td>`qualify eligibility`</td>
<td>`qualify entity`</td>
</tr>
<tr>
<td>`score ai-employee`</td>
<td>`score fit --model ai-employee`</td>
</tr>
<tr>
<td>GTM `score market`</td>
<td>`score fit --type market`</td>
</tr>
<tr>
<td>`recommend`</td>
<td>`asset diagnostic` or `market recommend`</td>
</tr>
<tr>
<td>`campaign run`</td>
<td>`workflow run`</td>
</tr>
<tr>
<td>`batch` and `queue`</td>
<td>`job`</td>
</tr>
<tr>
<td>`outreach email generate`</td>
<td>`outreach generate --channel email`</td>
</tr>
<tr>
<td>`export CRM`</td>
<td>`export --format crm`</td>
</tr>
</table>
Existing commands may remain as aliases during a documented deprecation period.
# 6. Canonical Data Model
LeadSniperAI should distinguish the following record types:
- Market
- Vertical
- Entity
- Person
- Contact
- Signal
- Evidence
- Opportunity
- Buyer
- Match
- Campaign
- Asset
- Outreach Event
- Compliance Record
- Economic Event
An organization may hold more than one role. For example, a mortgage brokerage may be both a buyer of mortgage applicants and a source of commercial-finance referrals.
## 6.1 Evidence Object
```json
{
  "claim": "No visible online booking option",
  "source_url": "https://example.ca/contact",
  "observed_at": "2026-07-27T10:30:00-07:00",
  "evidence_type": "website_observation",
  "confidence": 0.98,
  "expires_at": "2026-08-27T10:30:00-07:00"
}
```
## 6.2 Compliance Object
```json
{
  "jurisdiction": "CA",
  "communication_type": "commercial_electronic_message",
  "lawful_basis": "conspicuously_published_business_address",
  "basis_source_url": "https://example.ca/contact",
  "basis_observed_at": "2026-07-27T10:00:00-07:00",
  "basis_expires_at": null,
  "role_relevance": "Owner responsible for commercial partnerships",
  "identity_disclosed": true,
  "postal_address_available": true,
  "unsubscribe_supported": true,
  "do_not_contact": false,
  "opt_out_at": null,
  "legal_review_status": "pending"
}
```
The exact CASL basis, validity period, and expiry logic must be confirmed by qualified Canadian legal counsel before automated production sending.
# 7. Vertical Package Architecture
```plain text
verticals/
├── local-services/
├── mortgage-brokerages/
├── commercial-finance/
├── private-lending/
├── equipment-finance/
├── alternative-funding/
├── accounting/
├── legal-services/
├── wealth-management/
├── real-estate/
├── healthcare/
├── construction/
├── transportation/
└── marketing-agencies/
```
## Vertical Package Structure
```plain text
mortgage-brokerages/
├── vertical.yaml
├── personas.yaml
├── signals.yaml
├── qualification.yaml
├── opportunity-model.yaml
├── buyer-model.yaml
├── scoring.yaml
├── compliance.yaml
├── assets.yaml
└── outreach-policy.yaml
```
Each vertical must answer:
1. What outcome does the market purchase?
2. Who owns the outcome?
3. Which observable signals indicate pain, stress, or growth?
4. What makes an entity eligible?
5. What makes an opportunity valuable?
6. Which buyer types purchase that opportunity?
7. What evidence is required?
8. What communication is permitted?
9. Which value asset should be used?
10. Which events invalidate or refresh the record?
# 8. Priority Vertical Portfolio
## 8.1 Lead Buyer Verticals
<table header-row="true">
<tr>
<td>Vertical</td>
<td>Buyer Outcome</td>
<td>Decision-Maker</td>
<td>Lead Type</td>
</tr>
<tr>
<td>Independent mortgage brokerages</td>
<td>More fundable mortgage files</td>
<td>Owner, principal broker, team lead</td>
<td>Mortgage applicants</td>
</tr>
<tr>
<td>Commercial finance brokers</td>
<td>More qualified financing mandates</td>
<td>Founder, managing partner</td>
<td>Business financing opportunities</td>
</tr>
<tr>
<td>Equipment finance brokers</td>
<td>More equipment purchase and refinance files</td>
<td>President, sales director</td>
<td>Equipment finance opportunities</td>
</tr>
<tr>
<td>Private lenders</td>
<td>Deploy capital into qualified secured files</td>
<td>Principal, underwriting head</td>
<td>Mortgage and real-estate opportunities</td>
</tr>
<tr>
<td>Alternative funders</td>
<td>Increase funded business volume</td>
<td>ISO manager, partnerships director</td>
<td>Revenue-based financing leads</td>
</tr>
<tr>
<td>Wealth-management firms</td>
<td>Reach incorporated professionals and liquidity events</td>
<td>Managing director, advisor</td>
<td>HNW and business-owner opportunities</td>
</tr>
<tr>
<td>AI and marketing agencies</td>
<td>Acquire audited local-business prospects</td>
<td>Founder, owner</td>
<td>Local-business growth opportunities</td>
</tr>
</table>
## 8.2 Opportunity-Source Verticals
<table header-row="true">
<tr>
<td>Vertical</td>
<td>Observable Need</td>
<td>Opportunity Created</td>
</tr>
<tr>
<td>Construction companies</td>
<td>Working capital, equipment, project financing</td>
<td>Commercial finance lead</td>
</tr>
<tr>
<td>Transportation firms</td>
<td>Fleet acquisition and refinancing</td>
<td>Equipment finance lead</td>
</tr>
<tr>
<td>Restaurants</td>
<td>Expansion, equipment, cash-flow stress</td>
<td>Business finance lead</td>
</tr>
<tr>
<td>Dental and medical clinics</td>
<td>Equipment, acquisition, expansion</td>
<td>Equipment or commercial finance lead</td>
</tr>
<tr>
<td>Real-estate investors</td>
<td>Purchase, refinance, construction capital</td>
<td>Mortgage or private-lending lead</td>
</tr>
<tr>
<td>Self-employed professionals</td>
<td>Income-documentation challenges</td>
<td>Alternative mortgage lead</td>
</tr>
<tr>
<td>Local home-service firms</td>
<td>Missed-call and booking leakage</td>
<td>AI automation or growth-services lead</td>
</tr>
<tr>
<td>Accounting firms</td>
<td>Client financing and advisory gaps</td>
<td>Referral-partner opportunity</td>
</tr>
<tr>
<td>Law firms</td>
<td>Client liquidity and transition needs</td>
<td>Referral-partner opportunity</td>
</tr>
<tr>
<td>Property managers</td>
<td>Vendor, financing, and operational needs</td>
<td>Multi-vertical opportunity source</td>
</tr>
</table>
# 9. Required Discovery Agents
## Agent 1 — Local Business Discovery
Finds eligible local businesses using Google Business Profiles, Maps, directories, websites, and local search.
## Agent 2 — Website and Intake Audit
Detects:
- Hero clarity
- CTA visibility
- Contact forms
- Online booking
- Mobile click-to-call
- After-hours intake
- Trust signals
- Reviews and testimonials
- Broken forms and links
- Page speed
- Phone-only intake risk
## Agent 3 — Operational Signal Discovery
Monitors:
- Reviews
- Hiring
- Expansion
- New locations
- Service-area growth
- Software changes
- Advertising activity
- Public complaints
- Seasonal demand
## Agent 4 — Decision-Maker Discovery
Finds owners, founders, principals, managing partners, operations leaders, and growth leaders.
## Agent 5 — Contact Waterfall and Verification
Uses Deepline to source, waterfall, and verify work-email contacts.
## Agent 6 — Opportunity Qualification
Applies vertical rules, evidence standards, exclusions, and economics.
## Agent 7 — Lead Buyer Discovery
This agent should be implemented before large-scale opportunity acquisition.
```bash
leadsniper discover buyers \
  --vertical equipment-finance \
  --geography Canada \
  --buyer-type broker,lender \
  --status active \
  --json
```
For each buyer, collect:
- Buyer type
- Products funded or purchased
- Geography
- Transaction-size range
- Accepted industries
- Credit profile
- Time-in-business requirements
- Security requirements
- Documentation requirements
- Excluded industries
- Capacity
- Shared or exclusive preference
- Price tolerance
- Acquisition activity
- Decision-maker
- Contact status
- Compliance status
- Evidence freshness
# 10. Signal Classification
Every signal must be classified into one primary category.
## Priority Order
1. Revenue Leakage
2. Capacity Overload
3. Event-Driven Stress
4. Growth Attempt
5. Operational Friction

**Proposed future family (NOT yet implemented — post-MVP, see 4.5 Build Status):** `Offer Gap` — demand exists, offer does NOT exist. Distinct from Revenue Leakage (demand + offer exist, capture fails). Would slot between Revenue Leakage and Capacity Overload once validated. Do not classify into it until the engine ships.
## Buyer-Specific Signals
- Explicitly recruiting brokers, ISOs, affiliates, or referral partners
- Hiring originators, underwriters, or business-development staff
- Launching a new lending product
- Expanding into new geography
- Announcing a new funding facility
- Opening a branch
- Increasing paid acquisition
- Publicly discussing low pipeline or poor lead quality
## Local-Service Signals
- Reviews stating calls were unanswered
- Delayed callbacks
- Customers calling another company
- Emergency-service positioning without visible after-hours intake
- Phone-only intake
- Broken or difficult forms
- Hiring dispatch or administrative staff
- Multiple technician openings
- New locations or service areas
No signal means no outreach.
# 11. Lead Prioritization
Only surface leads where:
- Pain or growth is observable
- Decision-maker is reachable
- Fix is simple relative to value
- ROI can be explained without hype
- Evidence is recent
- Contact is verified
- Compliance status permits review or outreach
Avoid:
- Pre-revenue companies
- Over-complex enterprises
- No-signal prospects
- Unsupported intent assumptions
- Personal emails without a valid basis
- Companies with unresolved suppression or opt-out status
## Example Composite Score
<table>
<tr>
<td>Component</td>
<td>Weight</td>
</tr>
<tr>
<td>---</td>
<td>---:</td>
</tr>
<tr>
<td>Signal strength</td>
<td>25</td>
</tr>
<tr>
<td>Evidence quality</td>
<td>20</td>
</tr>
<tr>
<td>Outcome fit</td>
<td>15</td>
</tr>
<tr>
<td>Decision-maker reachability</td>
<td>10</td>
</tr>
<tr>
<td>Economic value</td>
<td>10</td>
</tr>
<tr>
<td>Urgency</td>
<td>10</td>
</tr>
<tr>
<td>Data completeness</td>
<td>5</td>
</tr>
<tr>
<td>Compliance readiness</td>
<td>5</td>
</tr>
</table>
Paid contact enrichment should be gated by score.
Suggested defaults:
- Score below 40: no paid contact enrichment
- Score 40–74: work email and essential enrichment only
- Score 75 and above: phone and deeper buyer or opportunity enrichment permitted
# 12. Cold Email as System Actuator
Cold email has one job:
> Create a trust-based handoff into the next system layer.
Cold email should not attempt to close the sale.
## Required Format
- Plain text
- Mobile readable
- Under 150 words
- Preferably under 80–100 words for first touch
- One observation
- One consequence framed carefully
- One value offer
- One permission-based CTA
- No links in the first touch
- No tracking pixels
- No unsupported guarantee
- No immediate calendar request
## Approved CTA Types
- “Would it be useful if I sent the short breakdown?”
- “Open to seeing the buyer-fit matrix?”
- “Worth sending the one-page diagnostic?”
- “Would a short example help?”
# 13. Value Asset Logic
After permission is granted, recommend one primary asset:
- Loom walkthrough
- One-page mini audit
- Buyer-fit matrix
- Case-style breakdown
- Diagnostic assessment
- Opportunity specification
- Geographic opportunity snapshot
The asset must:
- Explain why the problem exists
- Show the observable evidence
- Explain the mechanism
- Demonstrate implementation knowledge
- Reduce downstream sales friction
- Avoid a hard close
# 14. Campaign Workflow
## 14.1 Campaign Creation
```bash
leadsniper campaign create \
  --name "Canadian Equipment Finance Buyer Acquisition" \
  --vertical equipment-finance \
  --motion buyer-acquisition \
  --minimum-score 70
```
## 14.2 Workflow Stages
```bash
leadsniper workflow run <campaign-id> \
  --stages discover,signal,enrich,qualify,score,verify,compliance \
  --stop-before outreach \
  --json
```
## 14.3 Human Review Gate
Before outreach:
- Evidence reviewed
- Contact verified
- Compliance reviewed
- Offer approved
- Value asset defined
- Message manually approved
- Suppression checked
## 14.4 Reply Handoff
```plain text
Positive reply
→ classify intent
→ confirm permission
→ generate value asset
→ human review
→ deliver asset
→ ask one operational question
→ qualify fit
→ schedule only after demonstrated interest
```
# 15. Sample Buyer-Acquisition Email
Subject: Your current deal criteria
Hi \{\{first_name\}\},
I noticed \{\{company_name\}\} is currently \{\{observable_signal\}\}, particularly around \{\{product_or_market\}\}.
We are mapping where qualified \{\{opportunity_type\}\} opportunities should be routed based on transaction size, geography, documentation, and credit profile.
Before adding another source to your pipeline, I wanted to confirm whether you are actively reviewing these files and what makes one worth your team’s time.
I prepared a short buyer-fit matrix for firms operating in \{\{market\}\}.
Would it be useful if I sent it over?
Dennis
The first sentence must use stored evidence. General website statements must not be treated as proof of active demand.
# 16. Sample Local-Service Email
Subject: Question about after-hours calls
Hi \{\{first_name\}\},
I noticed \{\{company_name\}\} promotes \{\{emergency_or_high_value_service\}\}, but the website appears to route new enquiries mainly through the phone.
When the line is busy or a call comes in after hours, some customers may have no immediate way to explain the job or request a booking.
I mapped a simple intake and missed-call recovery workflow for your current setup.
Would it be useful if I sent the short breakdown?
Dennis
This message may only be used when the opening observation is verified.
# 17. Deliverability Infrastructure
Deliverability is infrastructure, not copywriting.
## Required Controls
- Dedicated sending domains
- Main brand domain protected
- Reputable domain extensions
- SPF configured
- DKIM configured
- DMARC configured
- MX records active
- Gradual mailbox warm-up
- Conservative daily send limits
- Verified contacts
- Bounce suppression
- Opt-out suppression
- No first-touch links
- No open tracking
- No click tracking
- Plain-text messages
- Sender identity and business details available
## Initial Pilot Limits
- 20 manually reviewed contacts
- 10–20 messages per inbox per day during early validation
- Increase only after stable delivery and constructive replies
- Pause when bounce, complaint, or negative-reply patterns increase
# 18. Compliance and CASL Control Layer
Compliance must be modeled as state, not a note.
Before Canadian outreach, the system must record:
- Jurisdiction
- Communication type
- Lawful-use basis
- Source of the basis
- Observation date
- Expiry or review date where applicable
- Role relevance
- Sender identity
- Mailing address availability
- Unsubscribe capability
- Opt-out history
- Do-not-contact state
- Legal review status
The system must support:
```bash
leadsniper compliance inspect <contact-id>
leadsniper compliance validate <campaign-id>
leadsniper compliance suppress <contact-id>
leadsniper compliance export-audit <campaign-id>
```
Legal counsel must validate the final CASL policy before production automation.
# 19. Economics Model
LeadSniperAI must forecast two separate acquisition engines.
## Rail A — Buyer Acquisition
```plain text
Buyer prospects
→ verified contacts
→ delivered messages
→ replies
→ interested buyers
→ approved buyers
→ trial buyers
→ paying buyers
```
## Rail B — Opportunity Acquisition
```plain text
Traffic or discovery
→ assessments
→ qualified opportunities
→ verified opportunities
→ accepted opportunities
→ sold leads
→ invoices
→ cash collected
```
## Required Economics Fields
- Cost per buyer contact
- Buyer reply rate
- Buyer activation rate
- Cost per opportunity
- Qualification rate
- Verification cost
- Buyer acceptance rate
- Lead selling price
- Shared versus exclusive revenue
- Refund or rejection rate
- Payment terms
- Receivables lag
- Collection probability
- Gross margin
- Cash conversion cycle
- Working-capital requirement
- Break-even volume
```bash
leadsniper economics forecast \
  --buyer-acquisition outbound \
  --opportunity-acquisition paid-search \
  --vertical equipment-finance \
  --days 90
```
Revenue recognition and cash collection must be reported separately.
# 20. Feedback and Optimization Loop
Diagnose the system layer before changing copy.
## Diagnostic Rules
- Low delivery or high bounce → contact quality or infrastructure issue
- Low opens → infrastructure, sender reputation, timing, or targeting issue
- Opens without replies → outcome, signal, relevance, or trust issue
- Positive replies without progression → value asset or handoff issue
- Buyer interest without activation → onboarding, criteria capture, or economics issue
- High opportunity volume with low acceptance → qualification or matching issue
- High invoicing with weak cash → receivables and collection issue
Never “fix copy” before checking evidence, audience, compliance, deliverability, and handoff.
# 21. Pilot Program
## Recommended First Motion
Buyer acquisition for:
1. Independent mortgage brokerages
2. Commercial finance brokers
3. Equipment finance brokers
## Pilot Scope
- 50 buyer entities per vertical
- Top 10–15 deeply reviewed per vertical
- Minimum score: 70
- Verified work email required
- One observable demand or growth signal required
- Human approval required
- One buyer-fit value asset per vertical
## Pilot Success Criteria
<table>
<tr>
<td>Metric</td>
<td>Target</td>
</tr>
<tr>
<td>---</td>
<td>---:</td>
</tr>
<tr>
<td>Verified contacts</td>
<td>90%+ of selected records</td>
</tr>
<tr>
<td>Bounce rate</td>
<td>Below 2%</td>
</tr>
<tr>
<td>Total reply rate</td>
<td>5%+</td>
</tr>
<tr>
<td>Positive reply rate</td>
<td>2%+</td>
</tr>
<tr>
<td>Buyer-fit matrix permissions</td>
<td>Minimum 2 per vertical</td>
</tr>
<tr>
<td>Structured buyer criteria captured</td>
<td>Minimum 5 buyers</td>
</tr>
<tr>
<td>Trial or conditional commitments</td>
<td>Minimum 1 per vertical</td>
</tr>
</table>
Do not scale opportunity acquisition until at least one buyer segment produces repeatable engagement and clear purchasing criteria.
# 22. Implementation Roadmap
## Phase 0 — Contract Reconciliation
- Finalize canonical command tree
- Publish deprecation map
- Define record types
- Add compliance object
- Define Deepline boundaries
- Define error and output standards
## Phase 1 — Buyer Discovery
- Build `discover buyers`
- Build buyer signal detection
- Build buyer enrichment
- Build buyer qualification schema
- Build buyer-fit score
- Build buyer outreach workflow
## Phase 2 — Priority Buyer Verticals
Implement:
1. Independent mortgage brokerages
2. Commercial finance brokers
3. Equipment finance brokers
4. Private lenders
5. Alternative funders
## Phase 3 — Opportunity Verticals
Implement:
1. Construction
2. Transportation
3. Healthcare practices
4. Real-estate investors
5. Self-employed mortgage borrowers
6. Local home-service businesses
## Phase 4 — Matching and Marketplace
- Opportunity-to-buyer matching
- Buyer-to-opportunity matching
- Capacity rules
- Geographic rules
- Exclusivity
- Duplicate prevention
- Reservation logic
- Acceptance and rejection feedback
## Phase 5 — Economics and Cash
- Dual-rail forecasting
- Buyer billing
- Receivables
- Refunds and rejection logic
- Cash conversion
- Marketplace margin reporting
## Phase 6 — Controlled Outreach
- Human approval
- CASL checks
- Suppression
- Deliverability controls
- Deepline provider adapters
- Reply classification
- Buyer onboarding
## Phase 7 — Optimization
- Signal performance reports
- Vertical conversion comparisons
- Buyer acceptance models
- Asset performance
- Match-quality feedback
- Domain and inbox health
- Cash and margin dashboards
# 23. Required System Outputs
Each campaign should produce:
- Industry requirements summary
- Decision-maker persona
- Digital map
- Signals monitored
- Lead sourcing strategy
- Qualification rules
- Evidence record
- Compliance record
- Score explanation
- Cold email angle
- Sample Email 1
- Value asset specification
- Handoff plan
- Metrics and thresholds
- Economics forecast
- Confidence level
# 24. Source Basis
This operating system was synthesized from:
- LeadSniperAI CLI — Product Requirements & Implementation Plan
- The Bulletproof B2B Client Acquisition Protocol
- The 90-Day Cold Email Blueprint
- Cold Email Systems & Intent List Data Research Report
- Cold Email Standard Operating Procedure — 2026
- The Complete OpenClaw Cold Outreach Playbook
- The 15-Minute AI Lead Pipeline Builder
- High-Conversion VSL Playbook
- Cold Email Tactics for High-Net-Worth Client Acquisition
- Deal Generation and client-acquisition reference materials in the project folder
- The system-design decisions and vertical refactor developed in this chat thread
# 25. Confidence and Open Decisions
## Confidence Level
91%
## Open Decisions
- Final CASL legal interpretation and expiry rules
- Exclusive versus shared lead pricing
- Buyer reservation duration
- Refund and rejection policy
- Canonical CRM destination
- Initial outreach sending provider
- Which vertical receives the first production pilot
- Minimum acceptable buyer commitment before opportunity acquisition begins
# 22. Notion AI Operations Layer
This section applies the operating model from Notion's July 2026 AI operations playbook to the LeadSniperAI cold email system.
The implementation principle is:
> Consolidate the work, connect the tools, and place agents on the repetitive operating loops.
LeadSniperAI remains the opportunity-intelligence and orchestration engine. Notion becomes the human-readable operating workspace where strategy, evidence, relationships, work, decisions, and agent outputs are consolidated.
## 22.1 Three-Step Compounding Loop
```plain text
1. Build the core operating hubs
        ↓
2. Connect the systems where work and decisions occur
        ↓
3. Deploy agents that maintain the hubs and advance the workflow
        ↺
Every completed loop improves the quality of future discovery, qualification, outreach, and decision-making.
```
The system should eliminate the operator acting as a manual integration between LeadSniperAI, email, calendar, CRM, documents, GitHub, and outreach providers.
# 23. Four Core Notion Hubs
LeadSniperAI should have four primary hubs inside Notion.
## 23.1 Tasks and Projects Hub
Purpose: one database for all implementation, campaign, research, compliance, and follow-up work.
Minimum properties:
- Task name
- Status
- Owner
- Due date
- Priority
- Related vertical
- Related campaign
- Related buyer or opportunity
- Source event
- Agent-generated
- Human approval required
- Last updated
Agents use this hub to:
- Create tasks from replies, meetings, failed jobs, and campaign exceptions
- Assign owners
- Update task status
- Surface blocked work
- Compile the daily operating brief
## 23.2 CRM and Relationship Hub
Purpose: one system for buyers, prospects, partners, referral sources, opportunities, and active conversations.
Minimum properties:
- Organization or person
- Relationship type
- Vertical
- Stage
- Owner
- Next step
- Last touch
- Signal class
- Signal strength
- Opportunity score
- Buyer score
- Compliance state
- Contact verification status
- Related campaign
- Related evidence
- Do-not-contact status
Agents use this hub to:
- Log outreach and replies
- Advance relationship stages
- Flag stale conversations
- Draft follow-ups
- Route qualified responses
- Detect missing next steps
## 23.3 Notes and Research Hub
Purpose: one searchable location for discovery notes, meetings, audits, buyer interviews, market research, campaign retrospectives, and decisions.
Minimum properties:
- Note title
- Type
- Date
- Attendees
- Related entity
- Related vertical
- Related campaign
- Decision made
- Action items
- Source URLs
- Evidence confidence
- Verified status
Agents use this hub to:
- Summarize meetings and buyer interviews
- Extract qualification criteria
- Record decisions
- Convert action items into tasks
- Answer questions such as “What did this buyer say about minimum deal size?”
## 23.4 Company Knowledge Hub
Purpose: long-term operational memory for the LeadSniperAI system.
Store:
- Product positioning
- Canonical CLI command contract
- Vertical packages
- Signal definitions
- Qualification rules
- Scoring models
- Compliance policies
- Deliverability policies
- Outreach policies
- Value-asset standards
- Buyer acceptance criteria
- Data schemas
- Implementation SOPs
- Decision frameworks
Minimum properties:
- Knowledge item
- Owner
- Category
- Last reviewed
- Verified
- Effective date
- Review date
- Related vertical
- Supersedes
Agents should only use verified or explicitly draft-labelled knowledge for consequential actions.
# 24. Hub Relationship Model
The four hubs should be relational rather than isolated.
Example:
```plain text
Buyer record
→ linked to buyer interview note
→ linked to qualification specification
→ linked to campaign
→ linked to outreach events
→ linked to follow-up tasks
→ linked to accepted opportunities
→ linked to invoicing and cash events
```
Operating rule:
> If a decision, relationship, signal, compliance record, or piece of active work will matter in 30 days, it must live in one of the four hubs rather than only in chat, email, or an agent log.
# 25. Connector Strategy
Connect systems in the order of decision volume and operational value.
## 25.1 Priority 1 — Email
Connect Gmail or Outlook first.
What flows in:
- Outreach replies
- Buyer criteria
- Objections
- Introductions
- Opt-outs
- Attachments
- Commercial commitments
What it unlocks:
- Reply triage
- CRM stage updates
- Follow-up drafting
- Task creation
- Compliance suppression updates
- Buyer-intent extraction
## 25.2 Priority 2 — Calendar
What flows in:
- Buyer calls
- Sales conversations
- implementation meetings
- Follow-up dates
What it unlocks:
- Meeting preparation
- Attendee and CRM context
- Post-meeting action extraction
- Follow-up scheduling
- Time and conversion analysis
## 25.3 Priority 3 — GitHub
Connect the LeadSniperAI repository and implementation issues.
What flows in:
- Issues
- Pull requests
- Releases
- Test status
- CLI command implementation progress
What it unlocks:
- Engineering status in daily briefs
- Product requirement traceability
- Implementation task updates
- Release readiness reporting
## 25.4 Priority 4 — File Storage
Connect Google Drive or the selected document store.
What flows in:
- Audits
- Loom scripts
- Case studies
- Compliance opinions
- Buyer specifications
- CSV exports
- Sales and training assets
What it unlocks:
- Unified search
- Asset retrieval
- Evidence linking
- Agent-grounded content generation
## 25.5 Priority 5 — Outreach and CRM Adapters
Connect through approved adapters only after the data contract and compliance gates are stable.
Systems may include:
- Deepline
- Smartlead or Instantly
- Atomic CRM or Convex-backed CRM
- Resend for transactional messages
- Unipile for approved unified messaging
# 26. Agent Design Standard
Every agent must have the same three-part definition.
## 26.1 Instructions
The agent's job, allowed actions, prohibited actions, evidence standard, escalation rules, and expected outputs.
## 26.2 Connections
The databases, email, calendar, GitHub, files, LeadSniperAI CLI commands, and provider adapters it may read or update.
## 26.3 Triggers
The event or schedule that activates the agent.
Examples:
- Scheduled every weekday morning
- New verified reply received
- CRM stage changes
- Opportunity score exceeds threshold
- Compliance record expires
- Campaign bounce rate exceeds threshold
- GitHub issue changes status
No agent should receive unrestricted access to all systems by default.
# 27. LeadSniperAI Operations Agents
## 27.1 Outreach Reply Triage Agent
Trigger: new reply to an approved campaign.
Responsibilities:
- Classify reply as positive, question, objection, referral, not now, unsubscribe, automated response, or irrelevant
- Update the CRM record
- Apply suppression immediately for opt-outs
- Draft a response when human review is required
- Create a follow-up task
- Route qualified interest into the value-asset workflow
Prohibited:
- Sending unapproved commercial commitments
- Overriding compliance status
- Inventing facts about the buyer or prospect
## 27.2 Daily Cold Email Operating Brief Agent
Trigger: weekday morning.
Inputs:
- Campaign status
- Replies
- Tasks
- CRM movement
- Signal discoveries
- Failed jobs
- Infrastructure alerts
- GitHub implementation progress
Output:
- What changed yesterday
- What requires human judgment today
- Positive replies requiring response
- At-risk campaigns
- Stale buyer conversations
- Compliance or deliverability exceptions
- Top three recommended actions
## 27.3 Self-Updating CRM Agent
Trigger: new email, meeting note, approved outreach event, buyer response, or opportunity disposition.
Responsibilities:
- Log touchpoints
- Update stage and last-touch date
- Set next step
- Link evidence and notes
- Flag stale or incomplete records
- Never downgrade do-not-contact restrictions
## 27.4 Buyer Criteria Extraction Agent
Trigger: buyer interview note or substantive buyer email.
Responsibilities:
- Extract geography
- Transaction size
- Industry preferences
- Credit requirements
- Time-in-business requirements
- Documentation requirements
- Security requirements
- Exclusions
- Capacity
- Lead-sharing preference
- Pricing expectations
Output must be marked draft until reviewed by a human.
## 27.5 Signal-to-Task Agent
Trigger: new high-priority signal with sufficient evidence.
Responsibilities:
- Create or update the entity record
- Attach the evidence
- Run or request qualification
- Create a research or outreach-review task
- Prevent outreach when evidence or compliance is incomplete
## 27.6 Campaign Health Agent
Trigger: scheduled review or metric threshold breach.
Responsibilities:
- Diagnose by system layer
- Low delivery or high bounce → infrastructure and verification
- Low replies → signal, vertical, outcome, or targeting mismatch
- Positive replies without progression → value asset or handoff
- Buyer rejection → qualification or matching rules
- Slow cash collection → economics and receivables
It must not default to rewriting email copy before upstream layers are checked.
## 27.7 Meeting Follow-Up Agent
Trigger: completed buyer, prospect, implementation, or strategy meeting.
Responsibilities:
- Summarize decisions
- Extract action items
- Assign owners and deadlines
- Update CRM stage and next step
- Draft a reviewable recap
- Link the note, entity, campaign, and tasks
# 28. Agent-Readable Context Pages
Create one short context page for each major operating area.
Required context pages:
- LeadSniperAI company and product context
- Cold email operating principles
- Buyer acquisition rail
- Opportunity generation rail
- Vertical portfolio
- Signal classification
- Scoring and qualification
- Compliance and suppression
- Deliverability infrastructure
- Value-asset standards
- Campaign diagnosis
- Economics and cash conversion
- Human approval policy
Each page should explain:
- Purpose
- Inputs
- Rules
- Outputs
- Owner
- Review cycle
- Related databases
- Related CLI commands
# 29. Structured Data Over Freeform Rule
Use databases for recurring operational objects.
Use structured records for:
- Buyers
- Opportunities
- Signals
- Evidence
- Contacts
- Campaigns
- Outreach events
- Compliance records
- Tasks
- Economic events
Use pages and notes for:
- Research synthesis
- Meeting summaries
- Decisions
- Retrospectives
- SOPs
- Strategic reasoning
This reduces agent guessing and makes state changes auditable.
# 30. Notion as Control Plane, Not System of Record
Notion should provide the human operating surface and knowledge layer.
LeadSniperAI or its operational backend remains authoritative for:
- Job execution state
- Provider usage and billing
- Evidence timestamps
- Contact verification
- Campaign send state
- Compliance enforcement
- Matching decisions
- Idempotency
- Audit logs
- Marketplace transactions
Notion mirrors and organizes decision-relevant state. It must not silently overwrite authoritative backend data.
# 31. Suggested Database Build Order
## Day 1 — Core Hubs
Build:
1. Tasks and Projects
2. CRM and Relationships
3. Notes and Research
4. Company Knowledge
Move all active LeadSniperAI cold email work into these hubs.
## Day 2 — Connections and Context
Connect:
1. Email
2. Calendar
3. GitHub
4. File storage
Create the required context pages and relations.
## Day 3 — First Agents
Deploy:
1. Daily Cold Email Operating Brief Agent
2. Outreach Reply Triage Agent
3. Self-Updating CRM Agent
Start with read, classify, draft, and route permissions. Add write or send permissions only after validation.
# 32. First 30-Day Rollout
## Week 1 — Workspace Foundation
- Create four hubs
- Define schemas and relations
- Import current buyers, campaigns, verticals, tasks, and decisions
- Mark verified versus draft knowledge
## Week 2 — Connector Foundation
- Connect email and calendar
- Connect GitHub and file storage
- Map events to CRM and task updates
- Establish suppression synchronization
## Week 3 — Agent Pilot
- Launch daily brief
- Launch reply triage in draft-only mode
- Launch CRM update recommendations
- Review agent accuracy daily
## Week 4 — Controlled Automation
- Permit low-risk CRM updates
- Permit task creation
- Keep commercial sends human-approved
- Measure time saved, missed follow-ups, data freshness, and error rate
# 33. Notion Operations Success Metrics
Track:
- Hours of manual coordination removed
- Percentage of active relationships with a next step
- Percentage of replies classified within target time
- Percentage of meetings with completed follow-up
- CRM freshness
- Knowledge verification coverage
- Signal-to-review time
- Positive-reply response time
- Compliance exception count
- Agent correction rate
- Tasks created automatically versus completed
- Campaign decisions supported by complete evidence
The goal is not maximum automation.
The goal is:
> A workspace that is already current when the operator opens it, so human time is spent on judgment, relationships, and high-value decisions rather than copying information between systems.
<page url="https://app.notion.com/p/3aa9e94cf0a481cfa59ac2b6dec86f44">SOP — Signal-Based Cold Email System Using LeadSniperAI</page>