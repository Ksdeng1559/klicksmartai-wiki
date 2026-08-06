---
title: LeadSniperAI Marketplace PRD
created: 2026-08-05
updated: 2026-08-05
type: summary
tags: [technology, research, how-to]
sources: [notion: LeadSniperAI Marketplace PRD]
related: [lead-sniperai-cli-os, lead-sniperai-signal-cold-email-sop, deepline]
---

# Executive Summary
LeadSniperAI will use **Convex as the real-time operational backend** for a multi-tenant marketplace that generates, qualifies, packages, prices, distributes, and tracks leads produced by rank-and-rent web assets.
The platform combines two business models:
1. **Rank-and-rent lead generation assets** — SEO-focused websites, landing pages, calculators, assessments, and content hubs that attract high-intent organic traffic.
2. **Lead marketplace infrastructure** — a controlled marketplace where verified opportunities are sold, licensed, assigned, or distributed to qualified buyers by geography, vertical, exclusivity, tier, and subscription entitlement.
Convex becomes the central system for application data, real-time updates, workflow state, lead inventory, tenant access, agent activity, marketplace transactions, and operational dashboards. Clerk manages identity and organizations; Stripe manages billing; Resend, Twilio, and Unipile manage communications; DataForSEO and related intelligence services support SEO opportunity research and enrichment.
---
# 1. Product Vision
## Vision Statement
Build a repeatable platform that can launch and operate multiple rank-and-rent web assets across financing and professional-service verticals, convert visitor intent into structured and verified opportunities, and monetize those opportunities through a multi-tenant lead marketplace.
## Core Outcome
A visitor searching for a financing solution reaches a focused web asset, completes a useful assessment or calculator, consents to contact, is progressively qualified, and becomes a marketplace-ready opportunity that can be matched with one or more appropriate buyers.
## Initial Vertical Focus
- B-lender and alternative mortgages
- Self-employed mortgage financing
- Construction and development financing
- Commercial mortgages
- Business acquisition financing
- Working-capital and growth financing
- Equipment financing
- Professional referral opportunities for accountants, lawyers, brokers, consultants, and lenders
## Long-Term Platform Direction
The same backend should support separate brands, domains, locations, service verticals, content libraries, lead products, buyer groups, and revenue models without rebuilding the core application.
---
# 2. Business Model
## Revenue Streams
### Lead sales
- Non-exclusive assessment leads
- Voice-verified leads
- Advisor-ready opportunities
- Application-ready opportunities
- Exclusive leads
- Shared leads sold to compatible non-competing verticals
### Subscriptions
- Monthly lead-credit plans
- Geography-based access plans
- Vertical-specific buyer memberships
- First-look or priority access subscriptions
- Marketplace intelligence subscriptions
### Rank-and-rent agreements
- Fixed monthly rental of a web asset or territory
- Base rent plus performance fee
- Revenue share on funded transactions
- White-label microsite rental
- Exclusive sponsorship of a content or calculator cluster
### Software and services
- CRM and lead-management access
- AI qualification assistant
- Underwriting or funding-readiness reports
- SEO intelligence and content operations
- Managed outreach and follow-up
## Lead Monetization Rules
Every lead product must define:
- Vertical
- Geography
- Buyer type
- Qualification threshold
- Verification level
- Exclusivity model
- Maximum number of buyers
- Price or credit cost
- Delivery method
- Refund or replacement policy
- Consent scope
- Expiration window
- Required buyer credentials
---
# 3. Why Convex
Convex is selected as the operational backend because LeadSniperAI requires more than a traditional database.
## Required backend capabilities
- Real-time lead inventory and dashboard updates
- Type-safe TypeScript functions
- Transactional mutations
- Durable scheduled and background processes
- Workflow state that survives failures
- Controlled concurrency for external APIs
- Multi-tenant authorization
- Agent conversation and execution persistence
- File metadata and document access controls
- Search and optional RAG
- Live status for assessments, qualification, distribution, and purchases
## Convex responsibilities
- Operational data store
- Lead lifecycle state
- Marketplace inventory
- Tenant and entitlement enforcement
- Workflow orchestration
- Job and API execution state
- Notifications and event tracking
- Agent threads and generated analysis
- Real-time buyer and operator dashboards
## Systems Convex complements
- **Clerk:** authentication, organizations, invitations, identity
- **Stripe:** subscriptions, credits, payments, invoices, webhooks
- **Resend:** transactional email
- **Twilio:** SMS and phone verification
- **Unipile:** LinkedIn, WhatsApp, and unified messaging connections
- **DataForSEO:** keyword, SERP, competitor, backlink, and rank intelligence
- **Deepline / enrichment providers:** company and contact enrichment
- **Cloudflare R2:** large files, recordings, and generated reports
- **MotherDuck or warehouse:** historical analytics and BI
- **Qdrant, optional:** specialized large-scale semantic retrieval
- **Vercel:** frontend hosting and deployment
---
# 4. Target Users
## Lead visitor
A person or business seeking financing, advice, a lender, or a service provider.
### Needs
- Fast answers
- Useful calculators and assessments
- Clear next steps
- Privacy and consent clarity
- Confidence that the request reaches an appropriate advisor
## Lead buyer
A mortgage broker, commercial lender, alternative lender, business lender, accountant, lawyer, consultant, or other qualified professional.
### Needs
- Relevant opportunities
- Transparent lead quality
- Defined territory and exclusivity
- Fast notifications
- Simple purchase and acceptance
- Complete context and consent evidence
- Performance and ROI reporting
## Marketplace operator
LeadSniperAI administrators and quality-assurance staff.
### Needs
- Centralized lead operations
- Workflow visibility
- Buyer management
- Pricing and allocation controls
- Fraud and duplicate detection
- Compliance records
- Revenue and conversion reporting
## Rank-and-rent asset partner
A local operator, broker, agency, lender, or investor who rents or sponsors a digital asset.
### Needs
- Territory reporting
- Brand and content controls
- Lead delivery
- Attribution
- Performance transparency
- Renewal and expansion options
---
# 5. Product Architecture
## High-Level Architecture
```plain text
SEO / AEO Web Assets
Astro or Next.js websites
Landing pages, calculators, assessments, content hubs
                |
                v
Clerk identity and organizations
                |
                v
Convex operational backend
  - tenants and memberships
  - sites and domains
  - content-to-offer mapping
  - visitors and sessions
  - consent records
  - assessments and calculations
  - leads and qualification
  - verification and enrichment
  - marketplace listings
  - buyers, plans, credits, and entitlements
  - purchases and lead access grants
  - communication events
  - workflow and agent state
  - attribution and operational metrics
                |
       ---------------------
       |         |         |
       v         v         v
     Stripe    Resend    Twilio / Unipile
                |
                v
External intelligence and enrichment
DataForSEO, Deepline, registries, AI models
                |
                v
Analytics warehouse and reporting
```
## Frontend Surfaces
### Public rank-and-rent websites
- Astro or Next.js
- Static or hybrid rendering for SEO
- Server-rendered high-intent pages where useful
- React components for calculators and assessment flows
- Structured data and local schema
- Programmatic page generation with quality controls
### Buyer marketplace
- Search and filter lead inventory
- View masked opportunity summaries
- Purchase or claim leads
- Track credits and subscriptions
- Receive real-time lead alerts
- Review performance and ROI
### Operator console
- Lead queue
- QA and verification
- Workflow inspection
- Buyer and tenant management
- Site and content asset management
- Pricing and allocation rules
- Compliance and consent review
- Revenue, inventory, and conversion dashboards
### Partner portal
- Asset-specific reporting
- Territory and keyword performance
- Lead delivery status
- Conversion reporting
- Invoices and agreement status
- Content and offer requests
---
# 6. Multi-Tenant Model
## Tenant Types
- LeadSniperAI platform tenant
- Buyer organization
- Rank-and-rent partner
- White-label operator
- Internal operations organization
## Identity Model
Clerk is the identity provider.
Every authenticated request must resolve:
- `clerkUserId`
- `clerkOrganizationId`
- Convex `userId`
- Convex `tenantId`
- Membership role
- Subscription and entitlement state
## Roles
- Platform owner
- Platform administrator
- QA analyst
- Content and SEO operator
- Tenant owner
- Buyer manager
- Buyer user
- Partner user
- Read-only analyst
## Authorization Principle
Every public Convex query, mutation, and action must validate tenant membership and resource access. Client-provided tenant IDs must never be trusted without server-side verification.
## Recommended access pattern
```plain text
Authenticate user
Resolve Clerk organization
Find active Convex membership
Confirm role and entitlement
Confirm resource belongs to tenant or is marketplace-visible
Execute operation
Write audit event
```
---
# 7. Core Convex Data Model
## `users`
- Clerk user ID
- Name
- Email
- Phone
- Status
- Last active time
## `tenants`
- Name
- Slug
- Tenant type
- Clerk organization ID
- Billing customer ID
- Status
- Branding configuration
- Default geography
## `memberships`
- User ID
- Tenant ID
- Role
- Status
- Permissions
- Invited by
## `sites`
Represents each rank-and-rent web asset.
- Tenant owner
- Brand name
- Domain
- Site type
- Vertical
- Primary geography
- Status
- Deployment URL
- Analytics configuration
- Partner agreement ID
## `site_pages`
- Site ID
- URL path
- Page type
- Search intent
- Primary keyword
- Keyword cluster
- Location
- Offer ID
- Content status
- Published version
- Last reviewed date
## `offers`
- Name
- Vertical
- Offer type
- Qualification flow
- Calculator or assessment configuration
- Lead product mapping
- Active status
## `visitors`
Use privacy-conscious identifiers.
- Anonymous visitor ID
- First-touch site
- First-touch page
- First-touch channel
- Last-touch channel
- UTM values
- Initial timestamp
## `sessions`
- Visitor ID
- Site ID
- Entry page
- Referrer
- Campaign
- Device category
- Started and ended timestamps
## `consents`
- Lead or visitor ID
- Consent language version
- Contact channels permitted
- Marketplace-sharing scope
- Timestamp
- IP or evidence reference where lawful
- Source page
- Withdrawal status
## `assessments`
- Site ID
- Offer ID
- Visitor ID
- Answers
- Completion percentage
- Calculated results
- Started and completed timestamps
- Conversion status
## `leads`
- Lead ID
- Source site
- Source page
- Offer
- Vertical
- Geography
- Person and company references
- Funding amount
- Funding purpose
- Time horizon
- Lead status
- Quality score
- Completeness score
- Confidence score
- Duplicate risk
- Fraud risk
- Consent ID
- Created timestamp
## `lead_contacts`
Sensitive contact details should be separated from public marketplace summaries.
- Lead ID
- Name
- Email
- Phone
- Company
- Preferred contact channel
- Verification state
## `lead_enrichments`
- Lead ID
- Provider
- Request ID
- Status
- Normalized result
- Confidence
- Cost
- Started and completed timestamps
## `lead_verifications`
- Lead ID
- Verification type
- Provider
- Result
- Evidence reference
- Timestamp
## `lead_scores`
- Lead ID
- Score model version
- Dimension scores
- Overall score
- Explanation
- Generated timestamp
## `lead_products`
Defines what can be sold.
- Product name
- Lead tier
- Vertical
- Minimum score
- Required fields
- Verification requirements
- Exclusivity type
- Buyer limit
- Base price
- Credit cost
- Expiry period
- Refund policy
## `marketplace_listings`
- Lead ID
- Lead product ID
- Masked summary
- Listing status
- Price
- Credit cost
- Geography
- Eligible buyer segment
- Available quantity
- Reserved quantity
- Listed and expiry timestamps
## `buyers`
- Tenant ID
- Buyer type
- Licences and credentials
- Verticals
- Geographies
- Funding range
- Risk appetite
- Lead preferences
- Status
## `buyer_entitlements`
- Buyer tenant ID
- Plan ID
- Allowed verticals
- Allowed geographies
- Monthly credits
- Remaining credits
- Priority tier
- First-look rights
## `lead_matches`
- Lead ID
- Buyer ID
- Match score
- Match reasons
- Eligibility status
- Notification status
- Ranking
## `lead_orders`
- Buyer tenant ID
- Lead ID
- Listing ID
- Price
- Credits used
- Stripe reference
- Order status
- Purchase timestamp
## `lead_access_grants`
Controls access to contact details.
- Lead ID
- Buyer tenant ID
- Order ID
- Access scope
- Granted timestamp
- Expiry timestamp
- Revoked timestamp
## `lead_outcomes`
- Lead ID
- Buyer tenant ID
- Contacted status
- Appointment status
- Application status
- Funded status
- Revenue amount
- Outcome reason
- Updated timestamp
## `communications`
- Lead ID
- Tenant ID
- Channel
- Provider
- Direction
- Template
- Delivery status
- External message ID
- Timestamp
## `workflows`
- Workflow type
- Entity ID
- Current status
- Current step
- Retry count
- Started and completed timestamps
- Error summary
## `agent_threads`
- Tenant ID
- Agent type
- User ID
- Lead ID
- Thread status
- Model
- Token and cost tracking
## `audit_events`
- Actor
- Tenant
- Action
- Resource type
- Resource ID
- Previous state reference
- New state reference
- Timestamp
---
# 8. Lead Lifecycle
## Stage 1 — Traffic acquisition
Visitor arrives through:
- Organic search
- Local search
- AI answer engines
- Paid search
- Social or community content
- Referral partners
- Email or outbound campaigns
## Stage 2 — Engagement
Visitor uses one or more lead magnets:
- Mortgage or business-financing calculator
- Funding-readiness assessment
- Eligibility checker
- Rental offset or add-back calculator
- Construction financing assessment
- Self-employed income assessment
- Lender comparison
- Downloadable guide
## Stage 3 — Progressive capture
The platform should capture information in stages rather than requiring a long initial form.
Suggested sequence:
1. Goal and funding need
2. Geography
3. Timing
4. Basic qualification
5. Contact details
6. Consent
7. Optional document or voice-based completion
## Stage 4 — Verification and enrichment
- Validate email and phone
- Detect duplicates
- Normalize address and geography
- Enrich company information
- Confirm business identity where appropriate
- Run AI summary and completeness analysis
- Request voice interview for higher-value tiers
## Stage 5 — Qualification
Assign:
- Lead category
- Lead tier
- Quality score
- Completeness score
- Confidence score
- Readiness score
- Urgency
- Recommended buyer type
## Stage 6 — Marketplace packaging
Create a masked opportunity summary that reveals enough information for a buyer to assess relevance without exposing protected contact data before purchase.
## Stage 7 — Matching and distribution
Match according to:
- Vertical
- Geography
- Funding amount
- Purpose
- Buyer credentials
- Buyer preferences
- Capacity
- Subscription entitlement
- Historical response and conversion
- Exclusivity rules
## Stage 8 — Purchase and access
- Reserve listing transactionally
- Confirm credit or payment
- Create order
- Grant lead access
- Deliver details
- Log audit trail
- Trigger response-time tracking
## Stage 9 — Outcome and learning
Collect:
- Contact attempt
- Contact success
- Appointment
- Application
- Approval
- Funding
- Revenue
- Reason lost
Use outcomes to improve traffic targeting, content, scoring, pricing, matching, and buyer quality.
---
# 9. Durable Convex Workflows
## Lead intake workflow
```plain text
Submission received
Validate payload
Create consent and lead records
Check duplicate and abuse signals
Verify email and phone
Run enrichment in parallel
Generate AI summary
Calculate scores
Determine lead product tier
Route low-confidence cases to QA
Publish eligible marketplace listing
Match eligible buyers
Send notifications
Track completion
```
## Voice-verification workflow
```plain text
Invite lead to voice interview
Wait for acceptance or expiry
Receive provider webhook
Store transcript and recording reference
Extract structured answers
Calculate completeness and confidence
Escalate contradictions to QA
Upgrade or retain lead tier
```
## Lead purchase workflow
```plain text
Validate buyer identity and tenant
Check entitlement and credentials
Reserve listing atomically
Confirm Stripe payment or credit balance
Create order
Create lead access grant
Reveal contact information
Notify buyer and lead where required
Start response SLA timer
```
## Buyer follow-up workflow
```plain text
Lead delivered
Wait for contact confirmation
Send reminder before SLA breach
Request outcome update
Escalate repeated non-response
Adjust buyer quality score
Release or redistribute lead when policy permits
```
## Content opportunity workflow
```plain text
Import DataForSEO opportunity
Cluster keyword and search intent
Evaluate SERP overlap
Assign target site and page type
Generate content brief
Human review
Publish
Request indexing
Monitor ranking and conversion
Refresh when performance decays
```
---
# 10. Workpool and API Controls
Create isolated work pools for external systems.
<table>
<tr>
<td>Pool</td>
<td>Purpose</td>
<td>Initial concurrency</td>
</tr>
<tr>
<td>---</td>
<td>---</td>
<td>---:</td>
</tr>
<tr>
<td>`dataforseo`</td>
<td>Keyword, SERP, competitor, rank data</td>
<td>3–5</td>
</tr>
<tr>
<td>`enrichment`</td>
<td>Company and contact enrichment</td>
<td>5–10</td>
</tr>
<tr>
<td>`llm-analysis`</td>
<td>Summaries, scoring explanations, content briefs</td>
<td>10–20</td>
</tr>
<tr>
<td>`email`</td>
<td>Transactional email</td>
<td>20–30</td>
</tr>
<tr>
<td>`sms`</td>
<td>SMS verification and alerts</td>
<td>5–10</td>
</tr>
<tr>
<td>`unipile`</td>
<td>LinkedIn and WhatsApp operations</td>
<td>3–5</td>
</tr>
<tr>
<td>`document-processing`</td>
<td>Extraction and classification</td>
<td>3–5</td>
</tr>
</table>
Every external call should include:
- Idempotency key
- Provider request ID
- Attempt count
- Backoff policy
- Cost record
- Tenant attribution
- Error classification
- Completion callback
---
# 11. Rank-and-Rent Web Asset System
## Site Types
### Authority site
A broad domain that covers a vertical nationally or provincially.
### Local service site
A geographically focused asset targeting a city, region, or service area.
### Specialty microsite
A focused asset targeting one financing problem or audience.
### Calculator-led asset
A site or section where a specialized calculator is the main acquisition mechanism.
### Partner-branded asset
A white-label or co-branded site rented to a buyer or operator.
## Page Architecture
Each site may contain:
- Primary service pillar
- Location pages
- Problem and scenario pages
- Eligibility and qualification pages
- Comparison pages
- Calculator pages
- Case studies
- Lender or solution guides
- FAQ and glossary pages
- Assessment results pages
- Trust, disclosure, and privacy pages
## SEO Evidence Requirement
Page architecture must be based on live SERP evidence rather than keyword similarity alone.
For each proposed page:
- Pull the same-location and same-device SERP
- Measure shared ranking URLs across related keywords
- Identify dominant intent and content format
- Determine local versus national intent
- Evaluate authority and backlink requirements
- Estimate commercial value
- Map the page to a lead offer
## Asset-to-Marketplace Linkage
Every public page must map to:
```plain text
site -> page -> keyword cluster -> search intent -> offer -> assessment -> lead product -> buyer segment
```
This creates closed-loop measurement from rankings to revenue.
---
# 12. SEO, AEO, and Content Intelligence
## Data sources
- DataForSEO keyword data
- Google SERP results
- Local pack data
- Competitor pages and domains
- Backlink data
- Search Console
- Web analytics
- Reddit, Quora, forums, and social questions where permitted
- CRM and lead outcome data
## Content prioritization formula
Prioritize opportunities based on:
- Commercial intent
- Search demand
- Ranking difficulty
- SERP fit
- Local relevance
- Lead value
- Buyer demand
- Existing topical authority
- Content-production cost
- Expected time to revenue
## AEO requirements
- Direct answers near the top of pages
- Clear entity relationships
- Defined terminology
- First-party calculations and examples
- Structured FAQs
- Citations and review dates
- Expert review and author identity
- Consistent schema
- Unique local or vertical evidence
---
# 13. Lead Scoring Framework
## Core dimensions
<table>
<tr>
<td>Dimension</td>
<td>Example weight</td>
</tr>
<tr>
<td>---</td>
<td>---:</td>
</tr>
<tr>
<td>Contact verification</td>
<td>15%</td>
</tr>
<tr>
<td>Completeness</td>
<td>15%</td>
</tr>
<tr>
<td>Funding fit</td>
<td>20%</td>
</tr>
<tr>
<td>Timing and urgency</td>
<td>10%</td>
</tr>
<tr>
<td>Financial readiness</td>
<td>15%</td>
</tr>
<tr>
<td>Documentation readiness</td>
<td>10%</td>
</tr>
<tr>
<td>Intent strength</td>
<td>10%</td>
</tr>
<tr>
<td>Fraud and duplicate adjustment</td>
<td>5%</td>
</tr>
</table>
Weights should vary by lead product and vertical.
## Example lead tiers
### Assessment Lead
- Valid contact information
- Consent captured
- Core need identified
- Limited qualification
### Voice-Verified Lead
- Assessment requirements met
- Phone ownership or contact verified
- Voice interview completed
- Structured summary available
### Advisor-Ready Opportunity
- Strong product fit
- Meaningful funding need
- Clear timeline
- Sufficient context for an advisor conversation
- High completeness and confidence
### Application-Ready Opportunity
- Required documents identified or supplied
- Financial readiness confirmed
- Product and buyer fit established
- Human QA completed where required
---
# 14. Marketplace Rules
## Listing visibility
A buyer sees only listings that satisfy:
- Tenant status
- Active subscription or purchase eligibility
- Approved vertical
- Approved geography
- Buyer credentials
- Listing availability
- Compliance restrictions
## Reservation rules
Use a transactional Convex mutation to prevent overselling.
The mutation must:
1. Confirm listing is active
2. Confirm buyer eligibility
3. Confirm remaining quantity
4. Reserve one allocation
5. Create a pending order
6. Set reservation expiry
## Shared lead model
The same opportunity may be sold to multiple buyers only when:
- Consent allows the intended sharing
- The lead product defines the buyer limit
- Buyers are informed that the lead is shared
- Geographic and vertical conflicts are respected
- The maximum allocation is enforced transactionally
## Cross-vertical monetization
A single business event may create multiple related but distinct opportunities.
Example:
```plain text
Business owner seeks acquisition financing
  -> commercial financing opportunity
  -> accountant advisory opportunity
  -> legal transaction opportunity
  -> insurance or benefits review opportunity
```
Each derived opportunity requires appropriate consent, relevance, and non-deceptive disclosure.
---
# 15. Billing and Entitlements
## Stripe objects
- Customer per buyer tenant
- Subscription per plan
- Price per membership tier
- Optional credit packs
- One-time lead purchase payment
- Invoice and payment status
## Convex billing records
Store normalized references rather than relying on Stripe as the application database.
- Stripe customer ID
- Subscription ID
- Price ID
- Current plan
- Subscription status
- Period start and end
- Monthly credits
- Purchased credits
- Used credits
- Grace period
## Webhook handling
Stripe webhooks update Convex entitlements through idempotent HTTP actions.
Critical events:
- Checkout completed
- Subscription created or updated
- Payment succeeded
- Payment failed
- Subscription cancelled
- Refund created
- Dispute created
---
# 16. Communications
## Resend
Use for:
- Assessment confirmations
- Lead verification requests
- Buyer notifications
- Purchase receipts
- Lead delivery
- SLA reminders
- Partner reports
## Twilio
Use for:
- Phone verification
- SMS consented follow-up
- Buyer alerts
- Appointment reminders
## Unipile
Use for:
- Unified messaging records
- LinkedIn connection workflows
- WhatsApp conversations
- Channel-specific outreach where permitted
## Communication safeguards
- Channel-specific consent
- Quiet hours
- Frequency caps
- Opt-out enforcement
- Template versioning
- Provider delivery and complaint events
- Tenant and campaign attribution
---
# 17. Compliance, Privacy, and Trust
The platform must be designed for Canadian privacy, anti-spam, lending, advertising, and professional-service requirements, with jurisdiction-specific legal review before launch.
## Required controls
- Explicit consent records
- Consent text versioning
- Purpose limitation
- Data minimization
- Role-based access
- Contact detail masking
- Encryption in transit and at rest
- Audit logging
- Data retention policies
- Deletion and correction workflows
- Export capability
- Opt-out and consent withdrawal
- Vendor and subprocessor records
- Breach-response procedures
## Marketplace disclosure
The visitor should understand:
- Who operates the site
- Whether LeadSniperAI is a lender, broker, marketplace, or referral platform
- That information may be shared with matched service providers
- Whether multiple providers may receive the request
- How the user can withdraw consent
## Sensitive documents
Store large documents in controlled object storage. Keep access metadata in Convex and issue time-limited access only to authorized users.
---
# 18. Analytics and KPI Framework
## Acquisition metrics
- Organic impressions
- Organic clicks
- Ranking distribution
- Non-branded traffic
- Local pack visibility
- Landing-page conversion
- Calculator starts and completions
- Assessment starts and completions
## Lead metrics
- Leads by site, page, keyword cluster, and offer
- Cost per lead
- Verified lead rate
- Duplicate rate
- Qualification rate
- Lead-tier distribution
- Time to qualification
## Marketplace metrics
- Listing-to-purchase rate
- Average lead price
- Revenue per lead
- Lead inventory age
- Buyer response time
- Refund and replacement rate
- Buyer retention
- Credit utilization
## Outcome metrics
- Contact rate
- Appointment rate
- Application rate
- Approval rate
- Funded rate
- Revenue generated
- Buyer ROI
- Revenue per organic visitor
- Revenue per ranked page
## North-star metric
**Qualified marketplace revenue generated per active web asset.**
Supporting metric:
**Funded or accepted opportunity value per 1,000 high-intent organic sessions.**
---
# 19. MVP Scope
## MVP vertical
Start with one focused market, such as British Columbia alternative and self-employed mortgage leads, before expanding to multiple verticals.
## MVP public experience
- One authority or specialty site
- Five to ten high-intent landing pages
- One calculator
- One progressive assessment
- Consent capture
- Confirmation and booking flow
## MVP backend
- Clerk authentication
- Convex tenant and membership model
- Site, page, offer, assessment, consent, lead, and contact tables
- Basic lead scoring
- Lead operator queue
- Buyer records and preferences
- Marketplace listings
- Lead purchase or manual allocation
- Stripe subscription or credit purchase
- Resend lead delivery
- Audit events
## MVP workflows
- Lead intake
- Email and phone verification
- AI summary
- QA routing
- Marketplace publication
- Buyer notification
- Purchase and access grant
- Outcome reminder
## Explicit MVP exclusions
- Fully autonomous lead pricing
- Broad multi-vertical expansion
- Complex revenue sharing
- Advanced semantic RAG
- Large-scale programmatic SEO
- Automated cross-vertical resale
- Self-hosted Convex
---
# 20. Phased Implementation Plan
## Phase 0 — Architecture and controls
### Deliverables
- Confirm initial vertical and geography
- Finalize lead products
- Define consent language and sharing model
- Define buyer eligibility
- Establish repository structure
- Configure Convex, Clerk, Stripe, and environments
- Create security and tenant-access test plan
### Exit criteria
- Approved data model
- Approved user journeys
- Approved compliance assumptions
- Test and production environments created
## Phase 1 — Acquisition and intake
### Deliverables
- Launch initial SEO site
- Build calculator and assessment
- Create offers and page mappings
- Store sessions, consent, assessments, and leads
- Build operator lead queue
### Exit criteria
- A visitor can complete the full intake flow
- Every lead has attribution and consent evidence
- Operators can review incoming leads
## Phase 2 — Qualification and workflow automation
### Deliverables
- Add email and phone verification
- Add enrichment providers
- Add AI summary and scoring
- Add durable workflow orchestration
- Add QA escalation
### Exit criteria
- Qualified leads are produced consistently
- Failed external calls retry safely
- Operators can inspect workflow state
## Phase 3 — Buyer marketplace
### Deliverables
- Buyer onboarding
- Buyer preferences and credentials
- Masked listings
- Matching
- Subscription and credit billing
- Purchase reservations
- Lead access grants
- Delivery notifications
### Exit criteria
- Eligible buyers can discover and purchase leads
- Listings cannot be oversold
- Contact details remain protected before access is granted
## Phase 4 — Outcome intelligence
### Deliverables
- Buyer outcome tracking
- Response SLA monitoring
- Site-to-revenue attribution
- Buyer quality scoring
- Lead score calibration
- Operational dashboards
### Exit criteria
- Revenue can be traced to a site, page, offer, and buyer
- Scoring and content decisions use outcome evidence
## Phase 5 — Rank-and-rent replication
### Deliverables
- Site templates
- Tenant and brand configuration
- Vertical configuration
- Location expansion workflow
- Partner reporting
- Asset rental and revenue-share agreements
### Exit criteria
- A new compliant asset can be launched without changing core backend architecture
- New vertical configuration is primarily data-driven
---
# 21. Repository Structure
```plain text
/apps
  /marketplace
  /operator-console
  /partner-portal
  /public-sites
/packages
  /ui
  /domain
  /analytics
  /seo
  /lead-scoring
/convex
  /schema.ts
  /auth
  /tenants
  /sites
  /offers
  /assessments
  /consents
  /leads
  /marketplace
  /billing
  /communications
  /workflows
  /agents
  /analytics
  /audit
```
## Convex function conventions
- Queries read data and enforce access
- Mutations perform transactional state changes
- Actions call external services
- Internal functions handle privileged workflow steps
- HTTP actions receive signed webhooks
- Scheduled functions manage expiry and reminders
---
# 22. Engineering Standards
## Required practices
- Strict TypeScript
- Schema validation for all arguments
- Generated Convex API types
- No direct trust of client tenant identifiers
- Idempotency for webhooks and external calls
- Transactional inventory reservation
- PII separation and masking
- Audit logging for sensitive access
- Unit tests for scoring and allocation rules
- Integration tests for purchase and access workflows
- Seed data for development
- Migration procedures for schema changes
## Observability
Track:
- Workflow failure rate
- Provider latency and error rate
- Cost per enrichment
- Function execution volume
- Queue depth
- Lead processing time
- Purchase failures
- Notification failures
- Access-control denials
---
# 23. Key Risks and Mitigations
## Risk: SEO assets do not rank
**Mitigation:** Use live SERP evidence, start with narrow high-intent clusters, build differentiated tools, and validate buyer economics before scaling content.
## Risk: Lead quality is inconsistent
**Mitigation:** Progressive qualification, verification, voice interviews, clear tier definitions, human QA, and outcome-based score calibration.
## Risk: Marketplace lacks buyer liquidity
**Mitigation:** Recruit anchor buyers before traffic scale, use territory waitlists, support direct assignment, and launch with one vertical and geography.
## Risk: Leads are oversold or exposed incorrectly
**Mitigation:** Transactional reservations, access-grant records, explicit allocation limits, contact masking, and audit logs.
## Risk: Multi-tenant data leakage
**Mitigation:** Central authorization helpers, tenant-derived access, internal functions, automated tests, and least-privilege design.
## Risk: Workflow and provider costs grow too quickly
**Mitigation:** Workpool concurrency, cost attribution, enrichment thresholds, caching, provider fallbacks, and budget limits by tenant.
## Risk: Legal or consent model is inadequate
**Mitigation:** Versioned consent, jurisdiction review, clear disclosures, opt-out handling, data minimization, and documented buyer obligations.
---
# 24. Success Criteria
## Product success
- Visitors receive immediate value from calculators and assessments
- Operators can process leads without spreadsheets or disconnected tools
- Buyers can acquire relevant leads through transparent rules
- Rank-and-rent partners can see performance and attribution
## Technical success
- Real-time updates work across operator and buyer interfaces
- Workflows recover from external failures
- No lead is oversold beyond its allocation rule
- Tenant isolation tests pass
- Every sensitive data access is attributable
- A new site can be added through configuration rather than backend duplication
## Commercial success
Initial targets should be finalized after validating lead prices and buyer demand. Suggested pilot targets:
- 3%–8% visitor-to-lead conversion on high-intent pages
- 50%+ assessment completion after contact capture
- 60%+ verified-contact rate
- 25%+ qualified or advisor-ready rate
- Under 5 minutes median buyer notification time
- 70%+ buyer contact attempt within agreed SLA
- Positive contribution margin per paid or organic lead
- A repeatable path to launch the second asset at materially lower cost than the first
---
# 25. Working Assumptions and Decisions Required
## Working assumptions
- Convex Cloud will be used for the initial release
- Clerk remains the authentication and organization provider
- Stripe manages subscriptions and lead-credit purchases
- Resend, Twilio, and Unipile remain the communication stack
- The initial launch focuses on one financing vertical and one geography
- Contact details are masked until a valid access grant exists
- Human QA remains part of high-value lead tiers
## Decisions required before development
1. Select the first vertical and geography.
2. Define whether initial leads are exclusive, shared, or both.
3. Set the maximum number of buyers for shared leads.
4. Approve lead-tier definitions and pricing.
5. Confirm buyer credential requirements.
6. Approve consent and marketplace disclosure language.
7. Choose the first public domain and brand.
8. Choose Astro or Next.js for the first rank-and-rent asset.
9. Define the refund, replacement, and redistribution policy.
10. Define the minimum outcome data buyers must report.
---
# 26. Recommended Initial Decision
Proceed with a focused pilot:
- **Vertical:** Alternative and self-employed mortgage financing
- **Geography:** British Columbia, beginning with Vancouver, Burnaby, Surrey, and the Fraser Valley
- **Asset:** A focused authority site with local service pages, educational content, and a qualification calculator
- **Lead products:** Assessment Lead, Voice-Verified Lead, and Advisor-Ready Opportunity
- **Marketplace:** Invitation-only buyers during pilot
- **Backend:** Convex Cloud
- **Identity:** Clerk organizations
- **Billing:** Stripe subscriptions and lead credits
- **Communications:** Resend, Twilio, and Unipile
- **SEO intelligence:** DataForSEO
This approach validates ranking ability, conversion, qualification quality, buyer demand, lead economics, and operational workflows before expanding into a broad marketplace.
---
# 27. Immediate Next Actions
1. Finalize the initial lead-product matrix.
2. Confirm the first domain, vertical, and geographic cluster.
3. Convert the core data model into `convex/schema.ts`.
4. Define Clerk organization and role mappings.
5. Build the public assessment journey.
6. Build the operator lead queue.
7. Implement the lead-intake workflow.
8. Recruit three to five pilot buyers.
9. Create the initial keyword-to-offer map using DataForSEO.
10. Launch the first five high-intent pages and one calculator.
---
# References
- Convex GitHub organization: [https://github.com/get-convex](https://github.com/get-convex)
- Convex documentation: [https://docs.convex.dev](https://docs.convex.dev)
- Clerk: [https://clerk.com](https://clerk.com)
- Stripe: [https://stripe.com](https://stripe.com)
- DataForSEO: [https://dataforseo.com](https://dataforseo.com)
<page url="https://app.notion.com/p/3ab9e94cf0a4810c9f6cf1f49892f3bb">🚀 [MortgagesByDennisEng.ca](http://MortgagesByDennisEng.ca) — Mortgage Opportunity CoPilot MVP & 180-Day Delegated Execution Plan</page>