# Source: Notion (page 3a69e94c-f0a4-8167-b21c-d3330c67aa51)

## Executive recommendation
Adopt Resend MCP as the **email operations, conversion intelligence, and agent-administration layer** for Mortgages by Dennis Eng. It should support the Search Engine Intelligence (SEI) platform and rank-and-rent model after organic traffic has been acquired.
Resend MCP should not replace the Resend SDK/API for immediate transactional email. The recommended division is:
- **Resend SDK/API:** production-triggered transactional messages.
- **Resend webhooks:** delivery, bounce, complaint, click, open, and inbound-email events.
- **Resend MCP:** agent-assisted template management, segmentation, campaign operations, troubleshooting, inbound triage, reporting, and controlled administrative actions.
- **Atomic CRM or Convex:** system of record for leads, consent, ownership, qualification, broker assignment, and revenue attribution.
- **Twilio:** urgent SMS, verification, and fast-response notifications.
- **Unipile:** WhatsApp, LinkedIn, and unified conversation channels.
- **Stripe:** broker subscriptions, territory rental, and accepted-lead charges.
> **Strategic principle:** SEO and SEI create demand; Resend increases the percentage of that demand that becomes complete, qualified, routed, accepted, and monetized mortgage opportunities.
---
## 1. Business objective
Build a measurable acquisition and monetization system for B-lender, alternative mortgage, self-employed, credit-challenged, construction, and renewal-related searches in British Columbia.
The system should connect the complete customer journey:
1. Search demand is identified through SEI.
2. A targeted content page, service page, calculator, or assessment is published.
3. Organic and AI-search visitors enter the funnel.
4. The visitor completes an assessment and provides channel-specific consent.
5. Resend delivers the result, requests missing information, and supports nurturing.
6. The CRM qualifies and scores the opportunity.
7. The opportunity is routed to Dennis, an approved broker, or a rank-and-rent tenant.
8. Email and CRM events determine whether the lead was accepted, booked, submitted, and funded.
9. Revenue is attributed to the originating keyword cluster, page, location, and digital property.
### Target outcomes
- Increase assessment completion rate.
- Reduce time from lead capture to first meaningful response.
- Increase the proportion of leads that become advisor-ready.
- Improve broker acceptance and follow-up rates.
- Identify the keyword clusters and pages producing funded revenue.
- Establish recurring revenue through territory rental and accepted-lead fees.
- Create a repeatable operating system that can be deployed across additional mortgage niches and locations.
---
## 2. Role of Resend MCP within SEI
SEI should not end at keyword volume, rankings, or website traffic. It should measure the commercial value of each search opportunity.
### SEI data loop
`Keyword → SERP → Page → Visitor → Assessment → Lead → Advisor-ready → Broker accepted → Appointment → Application → Funded → Revenue`
Resend contributes evidence at the middle of this loop:
- Email delivered or bounced
- Assessment-result email opened
- Continuation link clicked
- Missing-information request completed
- Borrower reply received
- Broker notification delivered
- Broker acceptance link clicked
- Educational nurture engagement
- Unsubscribe or complaint event
These events should be written back to the CRM and SEI warehouse so SEO decisions are based on **revenue contribution**, not traffic alone.
### Recommended SEI metrics
<table header-row="true">
<tr>
<td>Metric</td>
<td>Purpose</td>
</tr>
<tr>
<td>Organic visitor-to-lead rate</td>
<td>Measures landing-page conversion</td>
</tr>
<tr>
<td>Lead-to-completed-assessment rate</td>
<td>Measures form and follow-up effectiveness</td>
</tr>
<tr>
<td>Completed-to-advisor-ready rate</td>
<td>Measures lead quality</td>
</tr>
<tr>
<td>Email delivery rate</td>
<td>Identifies sender, list, or domain problems</td>
</tr>
<tr>
<td>Continuation-link click rate</td>
<td>Measures recovery of incomplete applications</td>
</tr>
<tr>
<td>Borrower reply rate</td>
<td>Measures intent and trust</td>
</tr>
<tr>
<td>Broker acceptance rate</td>
<td>Measures commercial lead quality</td>
</tr>
<tr>
<td>First-response time</td>
<td>Measures operational speed</td>
</tr>
<tr>
<td>Appointment-booked rate</td>
<td>Measures sales progression</td>
</tr>
<tr>
<td>Application-submitted rate</td>
<td>Measures funnel quality</td>
</tr>
<tr>
<td>Funded rate</td>
<td>Measures final commercial outcome</td>
</tr>
<tr>
<td>Revenue per lead</td>
<td>Supports lead pricing</td>
</tr>
<tr>
<td>Revenue per organic visit</td>
<td>Supports SEO investment decisions</td>
</tr>
<tr>
<td>Revenue per keyword cluster</td>
<td>Determines content priorities</td>
</tr>
<tr>
<td>Revenue per territory</td>
<td>Supports rank-and-rent pricing</td>
</tr>
</table>
---
## 3. Rank-and-rent operating model
### Recommended digital-property structure
Build focused properties or tightly defined site sections based on:
`Mortgage product + borrower problem + geography`
Priority clusters may include:
- B-lender mortgages in Vancouver
- Alternative mortgage financing in Burnaby
- Self-employed mortgages in Surrey
- Credit-challenged mortgages in the Fraser Valley
- Mortgage renewal denied in British Columbia
- Mortgage and property-tax arrears solutions
- Construction and infill development financing
- Debt consolidation using home equity
- Rental-property financing using offsets, add-backs, surplus, and deficit calculations
### Monetization models
#### Model A — Territory rental
A broker pays a fixed monthly amount for exclusive or semi-exclusive access to a city and product cluster.
Example structure:
- Monthly territory fee
- Included number of qualified leads
- Additional accepted-lead fee
- Defined service-level agreement
- Minimum response standards
- Renewal based on lead quality and close reporting
#### Model B — Accepted-lead pricing
A broker receives a masked opportunity summary and pays when the lead is accepted and contact details are released.
#### Model C — Exclusive subscription
One approved broker receives all qualified opportunities from a defined property, location, or cluster.
#### Model D — Marketplace routing
Multiple approved brokers can review masked opportunities. The first eligible broker to accept and meet the required conditions receives the lead.
### Recommended starting model
Use a **hybrid territory-rental plus accepted-lead fee** model.
This provides:
- Predictable recurring revenue
- Additional upside from lead volume
- Incentives to maintain lead quality
- Better valuation of each SEO property
- Reduced dependence on a single close or commission
---
## 4. Lead magnets and conversion assets
Rank-and-rent pages should not rely only on contact forms. Each property should include tools that reveal borrower intent and produce structured underwriting information.
### Priority tools
#### B-Lender Mortgage Assessment
Collect:
- Property location and type
- Estimated property value
- Current mortgage balance
- Requested mortgage amount
- Purpose of funds
- Income type
- Credit range
- Mortgage or tax arrears
- Occupancy
- Financing timeline
#### Self-Employed Mortgage Assessment
Collect:
- Business type and tenure
- Gross revenue
- Declared income
- Business add-backs
- Down payment or available equity
- Rental income
- Credit range
- Purchase, refinance, or renewal purpose
#### Alternative Mortgage Cost Calculator
Estimate and disclose:
- Payment range
- Interest assumptions
- Lender fee
- Brokerage fee
- Legal and appraisal expenses
- Potential exit timeline
- Approximate borrowing cost
#### Renewal or Credit-Challenge Review
Collect:
- Renewal date
- Current lender
- Current balance
- Payment history
- Credit challenges
- Property equity
- Reasons for declined renewal
- Urgency
### Conversion rule
Display meaningful results on the website before requesting optional marketing consent. Email can provide a saved report, continuation link, document checklist, or next-step review.
---
## 5. Resend implementation pattern
### Production pathway
`Website event → authentication and consent checks → CRM record → workflow/queue → Resend SDK/API → webhook event → CRM and SEI update`
### MCP pathway
`Authorized operator or agent → policy gateway → approved Resend MCP tools → audit log → CRM/SEI update`
### Use Resend MCP for
- Creating and updating email templates
- Managing approved contact properties and segments
- Drafting educational sequences
- Preparing broadcasts for approval
- Inspecting delivery failures and API logs
- Creating or reviewing webhooks
- Managing inbound email operations
- Identifying bounced or unengaged contacts
- Producing operational reports
- Comparing performance between sites, territories, and keyword clusters
### Do not depend on Resend MCP for
- Password resets
- Authentication emails
- Payment receipts
- Lead-purchase confirmations
- Immediate borrower confirmations
- Time-sensitive broker notifications
- Any production event where deterministic execution is required
These messages should be sent directly through the Resend SDK/API.
---
## 6. Lead data model
The CRM should remain the source of truth. Resend contact properties should contain only the minimum data needed for segmentation and communication.
### Core lead fields
- `lead_id`
- `tenant_id`
- `site_id`
- `source_page`
- `keyword_cluster`
- `province`
- `city`
- `mortgage_type`
- `property_type`
- `property_value_band`
- `mortgage_balance_band`
- `requested_amount_band`
- `estimated_ltv_band`
- `income_type`
- `credit_band`
- `urgency`
- `lead_score`
- `lead_tier`
- `consent_email_service`
- `consent_email_marketing`
- `consent_sms`
- `assigned_broker_id`
- `broker_status`
- `resend_contact_id`
- `last_email_event`
- `last_email_event_at`
### Avoid storing in Resend contact properties
- Social insurance numbers
- Full bank statements
- Tax returns
- Complete credit reports
- Detailed account numbers
- Highly sensitive identity documents
- Unnecessary free-form underwriting notes
Store sensitive material in a secure document system and use controlled, expiring links.
---
## 7. Borrower communication sequences
### Sequence 1 — Completed assessment
**Trigger:** Visitor submits a complete assessment.
**Immediate email:**
- Confirm receipt
- Summarize the information submitted
- State that the result is not an approval
- Explain the next review step
- Include a secure continuation or booking link
**Follow-up:**
- Request missing documents or clarification
- Explain why the information affects lender selection
- Provide a direct booking or callback option
**Educational follow-up:**
Send content based on the lead cluster, such as:
- How B lenders evaluate equity and exit strategy
- Self-employed income documentation options
- How lender fees affect total borrowing cost
- What happens when a mortgage renewal is declined
- How rental offsets and add-backs affect qualification
### Sequence 2 — Incomplete assessment recovery
**Trigger:** Assessment started but not completed.
The message should explain that the assessment was saved and identify the minimum missing information required to continue.
Recommended fields to request first:
- Property value
- Mortgage balance
- Requested amount
- Financing purpose
- Timeline
### Sequence 3 — Urgent opportunity
**Trigger examples:**
- Financing required within 30 days
- Renewal declined
- Mortgage or property-tax arrears
- Firm purchase or completion deadline
- Construction draw or project deadline
**Actions:**
1. Resend confirmation and document checklist
2. Twilio alert to assigned advisor
3. High-priority CRM task
4. Broker acceptance request when applicable
5. Escalation if response SLA is missed
### Sequence 4 — Long-term nurture
Use only when optional marketing consent has been provided.
Segment by actual need rather than sending generic newsletters.
Examples:
- B-lender exit planning
- Credit-rebuilding milestones
- Self-employed documentation preparation
- Renewal preparation 90–180 days in advance
- Construction-financing readiness
---
## 8. Broker and tenant communication
### Masked lead notification
A notification should contain:
- Lead tier
- Location
- Mortgage purpose
- Property-value band
- Mortgage balance and requested-amount bands
- Estimated LTV band
- Income type
- Credit band
- Financing timeline
- Key risks or missing information
- Acceptance deadline
- Accept and decline actions
Do not send full documents or excessive personal information before the broker has been authorized and assigned.
### Acceptance workflow
`Broker accepts → Clerk verifies broker and tenant → system confirms availability → Stripe charges fee if required → CRM assigns lead → borrower introduction is sent → response SLA begins`
### Service-level requirements
Recommended initial standards:
- Urgent leads acknowledged within 5 minutes
- Standard advisor-ready leads acknowledged within 15 minutes during business hours
- First borrower contact within 30 minutes
- Broker status updated within 24 hours
- Lead outcome updated at application and funding stages
If the assigned broker misses the SLA, the system should notify an operator or reroute the opportunity according to the territory agreement.
---
## 9. Inbound email workflow
Resend inbound email can support case-specific borrower replies.
### Recommended process
`Borrower reply → Resend inbound event → case and tenant identified → full message retrieved → attachment metadata checked → AI classifies response → CRM updated → human reviews sensitive documents → response drafted or task created`
### Useful classifications
- Qualification answer
- Document received
- Callback request
- Information correction
- Not interested
- Consent withdrawal
- Complaint
- Urgent deadline
- Broker or lender response
### Safety requirement
AI may summarize, classify, and draft. A licensed mortgage professional must make lending recommendations and suitability decisions.
---
## 10. Domain and sender architecture
Separate website identity, transactional messages, replies, and educational communication.
### Example property architecture
- Website: `vancouveralternativemortgages.ca`
- Transactional email: `notify.vancouveralternativemortgages.ca`
- Inbound replies: `reply.vancouveralternativemortgages.ca`
- Optional educational nurture: `updates.vancouveralternativemortgages.ca`
### Portfolio recommendation
Start with centralized administration but maintain:
- Separate sending domains or subdomains by brand and purpose
- A `site_id` and `tenant_id` on every relevant event
- Tenant-specific templates and sender identities
- Central suppression and consent controls
- Volume and complaint monitoring by domain
High-volume or independently rented properties can later move to separate Resend accounts or isolated sending configurations.
---
## 11. Multi-tenant controls
A raw Resend MCP connection should not be shared across all rank-and-rent tenants.
### Required policy gateway
Before an MCP action is executed, confirm:
- Authenticated user
- Clerk organization or tenant
- Allowed sender domain
- Allowed recipient relationship
- Consent status
- Suppression status
- Message type
- Daily and campaign limits
- Required human approval
- Audit-log creation
### Agent roles
<table header-row="true">
<tr>
<td>Agent</td>
<td>Recommended access</td>
</tr>
<tr>
<td>Template Agent</td>
<td>Create and update approved templates</td>
</tr>
<tr>
<td>Email Operations Agent</td>
<td>Read delivery status, logs, and diagnostics</td>
</tr>
<tr>
<td>Campaign Agent</td>
<td>Prepare segments and broadcast drafts</td>
</tr>
<tr>
<td>Inbound Triage Agent</td>
<td>Classify replies and create CRM tasks</td>
</tr>
<tr>
<td>Domain Administrator</td>
<td>Domains, webhooks, and API keys with strict approval</td>
</tr>
<tr>
<td>Lead Workflow Agent</td>
<td>Use controlled application functions rather than broad MCP access</td>
</tr>
<tr>
<td>Public chatbot</td>
<td>No direct Resend MCP access</td>
</tr>
</table>
### Human approval required
- Sending broadcasts
- Uploading or importing large contact lists
- Deleting contacts, segments, templates, or domains
- Changing DNS or sending configuration
- Creating or deleting API keys
- Creating or changing webhooks
- Accessing sensitive inbound attachments
- Sending to recipients outside an existing lead or partner relationship
---
## 12. Compliance and consent design
The intake experience should clearly explain:
- The identity of the organization collecting the information
- The purpose of collection
- Whether information may be shared with a licensed broker, lender, or financing provider
- Which communication channels may be used
- How consent may be withdrawn
- That an assessment does not represent mortgage approval
### Recommended consent separation
- **Required:** Contact me regarding this mortgage request.
- **Required:** Share my information with an appropriate licensed mortgage professional or financing provider for this request.
- **Optional:** Send me educational mortgage information and future offers.
- **Optional:** Contact me by SMS.
Do not make future marketing consent a condition of receiving the requested assessment or response.
### Audit fields
Record:
- Consent language version
- Consent timestamp
- IP and source page where legally appropriate
- Channel selected
- Purpose of consent
- Withdrawal timestamp
- Suppression reason
- User or agent responsible for each communication
---
## 13. SEI reporting and decision framework
### Commercial formulas
**Lead value by page**
`Funded or lead-sale revenue attributed to page ÷ leads generated by page`
**Revenue per organic visit**
`Revenue attributed to organic page ÷ organic visits to page`
**Expected monthly lead value**
`Organic visits × visitor-to-lead rate × advisor-ready rate × accepted-lead value`
**Rank-and-rent property value**
`Monthly territory rent + accepted-lead revenue + funded referral/commission value − operating cost`
### Decision rules
Increase SEO investment when a cluster demonstrates:
- Meaningful advisor-ready lead volume
- Strong broker acceptance
- Acceptable acquisition and operating cost
- Low complaint and bounce rates
- Clear funded or lead-sale revenue
Improve or consolidate a page when it has:
- Traffic but weak lead conversion
- High incomplete-assessment rates
- Strong email engagement but low form completion
- Low broker acceptance due to missing qualification data
Pause or reposition a cluster when it has:
- Persistent low commercial intent
- High lead volume but negligible advisor-ready outcomes
- Poor consent quality
- High complaint or invalid-contact rates
- No credible path to territory rent or lead monetization
---
## 14. Resend MCP agent use cases
### Template operations
> Create a borrower confirmation template for the B-lender assessment. Include a summary of submitted information, a disclaimer that this is not an approval, a secure continuation link, and a next-step booking action. Save as a draft for review.
### Incomplete-lead recovery
> Identify leads generated by the self-employed mortgage cluster during the last 30 days that received the assessment email but did not complete the application. Create a follow-up segment and draft a compliant educational message. Do not send without approval.
### Territory comparison
> Compare delivery, click, completion, broker-acceptance, appointment, and funded performance for Vancouver, Burnaby, and Surrey alternative-lending properties. Flag material differences and recommend which territory should receive the next content investment.
### Deliverability monitoring
> Review bounce and complaint performance by sending domain for the last 30 days. Flag domains or templates outside approved thresholds and recommend corrective actions.
### Broker notification design
> Create a broker notification template for construction-financing opportunities over \$1 million. Include project type, location, land status, permit status, sponsor experience, requested amount, timeline, and missing information. Use masked borrower details until acceptance.
### Inbound triage
> Classify new inbound borrower replies as qualification answer, document received, callback request, correction, withdrawal, complaint, or urgent deadline. Update the CRM task and prepare a draft response for human review.
---
## 15. Phased implementation roadmap
### Phase 1 — Foundation
**Goal:** Establish secure, deterministic transactional email and attribution.
Deliverables:
- Verify sending and reply subdomains
- Implement Resend SDK/API
- Implement delivery and inbound webhooks
- Add consent and suppression fields to CRM
- Add `site_id`, `tenant_id`, `keyword_cluster`, and `lead_id` attribution
- Create borrower confirmation and broker notification templates
- Create delivery-event logging
### Phase 2 — Funnel recovery
**Goal:** Increase completed assessments and advisor-ready opportunities.
Deliverables:
- Incomplete-assessment recovery sequence
- Missing-information sequence
- Secure continuation links
- Urgent-lead workflow using Resend and Twilio
- Lead-tier definitions
- Broker acceptance workflow
- Response SLA tracking
### Phase 3 — MCP operations
**Goal:** Enable supervised agent management.
Deliverables:
- Connect Resend MCP for approved internal operators
- Implement role-based tool permissions or gateway controls
- Add approval requirements for bulk, destructive, and administrative actions
- Create template-management agent
- Create delivery-diagnostics agent
- Create inbound-triage agent
- Log MCP actions to the audit system
### Phase 4 — Rank-and-rent commercialization
**Goal:** Monetize territories and lead inventory.
Deliverables:
- Territory and product definitions
- Broker subscription agreements
- Stripe billing for territory rent and accepted leads
- Masked lead preview
- Lead acceptance and release workflow
- Rerouting rules
- Broker performance scorecard
### Phase 5 — SEI optimization
**Goal:** Allocate content and SEO investment based on commercial return.
Deliverables:
- Revenue attribution by keyword, page, site, and territory
- Funnel dashboards
- Content opportunity scoring
- Email and lead-quality diagnostic reporting
- Territory pricing model
- Automated monthly SEI performance review
---
## 16. Proposed technical architecture
`Astro/WordPress SEO pages and calculators`
`→ Lead intake API`
`→ Clerk identity and tenant resolution`
`→ Atomic CRM or Convex lead record`
`→ Workflow engine / queue`
`→ Resend SDK + Twilio + Unipile`
`→ Resend/Twilio/Unipile webhook events`
`→ CRM event timeline`
`→ SEI warehouse and attribution model`
`→ Rank-and-rent broker dashboard`
`→ Stripe billing and revenue tracking`
### Architectural principle
Communication providers should execute messages. The CRM and SEI layer should own identity, consent, qualification, routing, attribution, and commercial logic.
---
## 17. Initial KPI targets
These are starting operating targets and should be revised after sufficient traffic and lead volume are available.
<table>
<tr>
<td>KPI</td>
<td>Initial target</td>
</tr>
<tr>
<td>---</td>
<td>---:</td>
</tr>
<tr>
<td>Transactional email delivery</td>
<td>Greater than 98%</td>
</tr>
<tr>
<td>Invalid or hard-bounce rate</td>
<td>Less than 2%</td>
</tr>
<tr>
<td>Complaint rate</td>
<td>Less than 0.1%</td>
</tr>
<tr>
<td>Assessment completion after recovery</td>
<td>10–25% improvement</td>
</tr>
<tr>
<td>Urgent-lead acknowledgement</td>
<td>Under 5 minutes</td>
</tr>
<tr>
<td>Standard lead acknowledgement</td>
<td>Under 15 minutes</td>
</tr>
<tr>
<td>Advisor-ready lead rate</td>
<td>Establish baseline, then improve monthly</td>
</tr>
<tr>
<td>Broker acceptance rate</td>
<td>30–60%, depending on qualification standard</td>
</tr>
<tr>
<td>Appointment-booked rate</td>
<td>20–40% of accepted leads</td>
</tr>
<tr>
<td>Outcome reporting completeness</td>
<td>Greater than 90%</td>
</tr>
<tr>
<td>Revenue attribution coverage</td>
<td>Greater than 90% of monetized leads</td>
</tr>
</table>
---
## 18. Risks and mitigations
<table header-row="true">
<tr>
<td>Risk</td>
<td>Mitigation</td>
</tr>
<tr>
<td>MCP agent sends unauthorized email</td>
<td>Policy gateway, approval workflow, role restrictions</td>
</tr>
<tr>
<td>Cross-tenant data leakage</td>
<td>Tenant-scoped queries, sender restrictions, audit tests</td>
</tr>
<tr>
<td>Poor sender reputation</td>
<td>Separate subdomains, suppression controls, monitoring</td>
</tr>
<tr>
<td>Marketing without valid consent</td>
<td>Separate required and optional consent fields</td>
</tr>
<tr>
<td>Sensitive documents exposed in email</td>
<td>Secure document portal and expiring links</td>
</tr>
<tr>
<td>Broker delays reduce lead value</td>
<td>SLA alerts and rerouting rules</td>
</tr>
<tr>
<td>SEO traffic fails to monetize</td>
<td>Track advisor-ready, accepted, and funded outcomes</td>
</tr>
<tr>
<td>Too many low-quality microsites</td>
<td>Use live SERP and revenue evidence before expansion</td>
</tr>
<tr>
<td>AI treated as underwriting authority</td>
<td>Human licensed review and explicit system boundaries</td>
</tr>
<tr>
<td>Lead pricing lacks evidence</td>
<td>Start with pilot pricing and calculate revenue per accepted lead</td>
</tr>
</table>
---
## 19. Recommended pilot
Launch a 90-day pilot using three funnels on Mortgages by Dennis Eng:
1. B-Lender Mortgage Assessment
2. Self-Employed Mortgage Qualification
3. Renewal Denied or Credit-Challenge Review
### Pilot scope
- One primary domain
- Vancouver, Burnaby, Surrey, and Fraser Valley attribution
- Three borrower confirmation templates
- Three incomplete-assessment sequences
- One urgent-lead workflow
- One broker notification and acceptance workflow
- Resend webhooks connected to CRM
- MCP access limited to templates, diagnostics, and draft campaign preparation
- Monthly SEI review measuring traffic through revenue
### Pilot success criteria
- Reliable attribution from search page to lead outcome
- Improved assessment completion
- Faster borrower and broker response
- Measurable advisor-ready and accepted-lead rates
- Evidence to set territory rent and lead prices
- No material consent, deliverability, or cross-tenant incidents
---
## 20. Final recommendation
Proceed with Resend MCP as a **supervised operations capability** within the broader SEI and rank-and-rent platform.
The primary operating design should be:
`SEO demand intelligence + high-intent mortgage tools + consented lead capture + deterministic transactional email + MCP-assisted operations + human qualification + broker routing + revenue attribution`
The highest-value use of Resend MCP is not simply allowing an AI agent to send email. Its strategic value is enabling agents to create, inspect, troubleshoot, segment, and optimize the communication lifecycle while the application retains strict control over identity, consent, tenant boundaries, lead ownership, and monetization.
## Reference links
- Resend MCP repository: [https://github.com/resend/resend-mcp](https://github.com/resend/resend-mcp)
- Resend documentation: [https://resend.com/docs](https://resend.com/docs)
- Mortgages by Dennis Eng: [https://mortgagesbydenniseng.ca](https://mortgagesbydenniseng.ca)
---
## Paper + Resend MCP Email Design and Production Workflow
### Purpose
Use Paper as the visual email-design layer for Mortgages by Dennis Eng, then use Paper MCP and Resend MCP to convert approved designs into operational Resend templates and draft broadcasts.
The recommended division of responsibilities is:
`Paper → visual design`
`Paper MCP → reads the selected artboard, styles, copy, images, and variables`
`AI coding agent → converts the design into email-safe HTML`
`Resend MCP → creates templates, drafts broadcasts, manages segments, and supports review`
`Resend SDK/API → sends production transactional email`
`Resend webhooks → records delivery, click, bounce, complaint, and inbound events`
`CRM + SEI → attributes email outcomes to keyword, landing page, property, tenant, broker, and funded revenue`
> **Operating principle:** Paper determines how the communication looks; Resend MCP turns the design into an operational asset; the Resend API sends it; SEI determines whether it creates a valuable mortgage outcome.
### Recommended architecture
`Paper visual artboard → Paper MCP → Codex/Claude/Cursor → email-safe HTML → Resend MCP template or broadcast draft → Resend API → webhook events → CRM and SEI`
Paper Desktop exposes a local MCP endpoint while a Paper file is open. The agent can inspect the selected artboard and translate it into a table-based, inline-styled email compatible with major email clients.
### Mortgage email design system
Create one master Paper file named:
**Mortgages by Dennis Eng — Email Design System**
Use reusable artboards rather than creating each email from scratch.
#### Borrower-facing artboards
1. **MBDE-01 — Assessment Received**
	- Confirms receipt
	- Summarizes the request
	- Explains the next step
	- Includes a continuation or booking link
	- States that submission is not an approval
2. **MBDE-02 — Complete Your Assessment**
	- Recovers incomplete submissions
	- Identifies the minimum missing information
	- Links to the saved assessment
3. **MBDE-03 — B-Lender Education**
	- Explains why a B lender may be considered
	- Addresses equity, income, credit, fees, and exit strategy
	- Encourages a professional review
4. **MBDE-04 — Personalized Document Checklist**
	- Requests only relevant documents
	- Explains why each item is needed
	- Links to a secure upload portal
5. **MBDE-05 — Borrower and Advisor Introduction**
	- Introduces the assigned advisor or broker
	- Confirms expected response time
	- Summarizes the borrower request
	- Reinforces consent and privacy expectations
#### Broker- and tenant-facing artboards
- New masked lead preview
- Lead accepted
- Lead reassigned
- Response-SLA warning
- Appointment booked
- Application-ready opportunity
- Lead-outcome request
- Monthly territory performance report
### Email-safe Paper standards
Use these standards for every artboard:
- Single-column layout
- Approximately 600-pixel content width
- One primary call to action
- Real production copy rather than placeholder text
- Web-safe fonts
- PNG or JPG images where possible
- Minimal navigation
- Limited decorative effects
- Strong mobile readability
- Clear compliance and contact footer
- Triple-brace variables written directly into the design
Recommended layout:
`Brand header → headline → concise explanation → borrower-specific summary → primary CTA → secondary contact option → compliance statement → sender and unsubscribe information`
The implementation agent should convert the visual design into table-based HTML with inline styles because modern website CSS is not consistently supported across email clients.
### Recommended template variables
Use Resend template variables such as:
- `{{{FIRST_NAME|there}}}`
- `{{{ASSESSMENT_TYPE}}}`
- `{{{PROPERTY_CITY}}}`
- `{{{REQUESTED_AMOUNT}}}`
- `{{{MISSING_ITEMS}}}`
- `{{{CONTINUE_URL}}}`
- `{{{BOOKING_URL}}}`
- `{{{ADVISOR_NAME|Dennis Eng}}}`
- `{{{BROKER_NAME}}}`
- `{{{BROKER_PHONE}}}`
- `{{{SITE_NAME}}}`
- `{{{CITY}}}`
- `{{{PROVINCE}}}`
- `{{{PRIVACY_URL}}}`
- `{{{LEAD_ID}}}`
Do not place sensitive financial data in reusable email-template variables unless strictly necessary. Use secure links for documents and detailed underwriting information.
### Template creation workflow
For transactional emails, the agent should:
1. Read the selected Paper artboard.
2. Recreate it as email-safe HTML.
3. Preserve approved copy, hierarchy, variables, images, spacing, and brand treatment where email-client limitations allow.
4. Create the Resend template as a draft.
5. Produce a review summary listing any visual elements that could not be translated reliably.
6. Publish only after approval.
7. Return the template name, template identifier, subject, variables, triggering event, and version.
#### Suggested agent prompt
`Read the selected Paper artboard and recreate it as a reusable Resend email template. Convert it into email-safe HTML using a single-column, table-based layout and inline styles. Preserve the approved copy, spacing, brand colors, images, and triple-brace variables as closely as email clients allow. Create the template as a draft only. Do not publish or send it. Report any Paper elements that could not be translated reliably.`
### Transactional template use cases
Use published templates when an individual application event triggers an email.
- Assessment submitted → Assessment Received
- Assessment incomplete → Complete Your Assessment
- Lead reviewed → Personalized Document Checklist
- Broker assigned → Borrower and Advisor Introduction
- Broker accepts marketplace lead → Lead Accepted
- Territory SLA missed → Broker SLA Warning
The application should send these through the Resend SDK/API using deterministic workflow logic, tenant checks, consent validation, and secure variables.
### Broadcast use cases
Use Resend Broadcasts for approved educational or partner campaigns sent to a defined segment.
Examples:
- Vancouver self-employed mortgage leads
- Burnaby alternative-lending prospects
- B-lender guide subscribers
- Mortgage renewals expected within 90–180 days
- Construction-financing prospects
- Broker partners renting a territory
Broadcasts should be created as drafts and reviewed before scheduling or sending.
#### Suggested broadcast prompt
`Read the selected Paper artboard and create a Resend Broadcast. Convert it to email-safe HTML using inline styles and a table-based layout. Preserve the approved visual hierarchy and personalization variables. Create the Broadcast as a draft only. Do not schedule or send it. Return the proposed segment, sender, subject, preview text, and review summary.`
### Rank-and-rent property model
Use one parent email design system with controlled local variations.
`Master design system`
`├── Mortgages by Dennis Eng`
`├── Vancouver Alternative Mortgages`
`├── Burnaby B-Lender Solutions`
`├── Surrey Self-Employed Mortgages`
`└── Fraser Valley Mortgage Renewal Help`
Each property may vary by:
- Property or site name
- Local headline and examples
- Assigned broker
- Phone number
- Booking link
- Sender identity and domain
- Compliance disclosures
- Local offer or assessment type
The structural design, accessibility, consent language, and tracking model should remain standardized.
### SEI attribution model
Every Paper-created template and broadcast should be connected to the search and revenue funnel:
`Keyword → landing page → assessment → email template → engagement → completed assessment → advisor-ready → broker accepted → appointment → application → funded → revenue`
Recommended tracking fields:
- `tenant_id`
- `site_id`
- `page_id`
- `keyword_cluster`
- `lead_id`
- `assessment_type`
- `campaign_id`
- `template_id`
- `template_version`
- `assigned_broker_id`
- `territory_id`
- `message_type`
- `resend_email_id`
- `conversion_event`
This allows SEI to answer:
- Which landing pages generate leads who complete the email sequence?
- Which B-lender topics produce advisor-ready opportunities?
- Which email designs increase completed assessments?
- Which geographic properties produce the most accepted leads?
- Which rank-and-rent tenants meet response standards?
- Which keyword clusters generate funded mortgages rather than only form submissions?
### Experimentation framework
Create controlled Paper variants for important emails.
Example:
- MBDE-02A — Continue Your Assessment
- MBDE-02B — Review Your Potential Mortgage Options
- MBDE-02C — Three Details Needed to Complete Your Review
Test one material variable at a time:
- Subject line
- Headline
- CTA wording
- Summary-card treatment
- Educational versus urgency framing
- Advisor image versus no image
Evaluate downstream business outcomes rather than optimizing only for opens:
`Delivered → continuation click → assessment completed → advisor-ready → broker accepted → application submitted → funded`
### First implementation sequence
Prioritize these artboards:
1. B-Lender Assessment Received
2. Complete Your Assessment
3. Personalized Document Checklist
4. New Broker Lead Preview
5. Borrower and Broker Introduction
6. Self-Employed Mortgage Guide
7. Renewal Review Reminder
8. Territory Performance Report
### Recommended pilot
Begin with one complete funnel:
`B-lender landing page → assessment submission → Paper-designed confirmation → incomplete-assessment reminder → broker lead-preview email → broker acceptance → borrower introduction → SEI revenue attribution`
Success criteria for the pilot:
- Templates render correctly on desktop and mobile
- Transactional messages are sent through the API rather than free-form MCP execution
- Every message is attached to a lead, site, tenant, and keyword cluster
- Incomplete-assessment recovery can be measured
- Broker acceptance can be measured
- Borrower introductions are auditable
- Funded outcomes can be attributed back to the originating page and email sequence
### Governance controls
- Paper designs require marketing and compliance approval before publishing.
- Resend MCP should create drafts by default.
- Broadcast sending requires human approval.
- Tenant and sender-domain rules must be enforced by the application.
- Sensitive attachments must use secure storage and expiring links.
- Every template should have an owner, purpose, version, triggering event, and review date.
- Retired templates should not remain callable from production workflows.
### Source
- [Resend guide: Paper integration](https://resend.com/docs/guides/paper)
---
## Addendum — Professional Referral Outreach and Referral Lifecycle
### Purpose
Add a structured professional-referral channel to the Mortgages by Dennis Eng growth system. The objective is to build recurring referral relationships with professionals whose clients may require B-lender, alternative, self-employed, construction, debt-consolidation, renewal, or private-mortgage solutions.
Priority referral partners include:
- Accountants and bookkeepers
- Lawyers and notaries
- Realtors and commercial real-estate agents
- Financial planners and wealth advisors
- Insurance advisors and employee-benefits consultants
- Insolvency trustees and credit counsellors
- Bank representatives and credit-union lenders with declined or non-prime files
- Property managers and strata professionals
- Builders, developers, contractors, and construction consultants
- Business brokers, M&A advisors, and commercial-finance professionals
> **Operating principle:** professional outreach should create trust before asking for referrals. Referral communications should be educational, specific to the partner’s client situations, and supported by clear confirmation, status visibility, privacy controls, and reliable follow-through.
### 1. Referral partner segmentation
The CRM should classify partners by profession, geography, client profile, referral potential, and relationship stage.
Recommended fields:
- `partner_id`
- `partner_type`
- `firm_name`
- `contact_name`
- `city`
- `province`
- `specialty`
- `client_profile`
- `relationship_stage`
- `outreach_source`
- `consent_or_business_basis`
- `assigned_owner`
- `last_contact_at`
- `next_follow_up_at`
- `referrals_submitted`
- `advisor_ready_referrals`
- `funded_referrals`
- `funded_volume`
- `attributed_revenue`
- `partner_tier`
- `preferred_contact_channel`
- `resend_contact_id`
Recommended relationship stages:
1. Identified
2. Researched
3. Outreach approved
4. Contacted
5. Engaged
6. Introductory meeting booked
7. Referral partner activated
8. Active referrer
9. Strategic partner
10. Dormant or do-not-contact
### 2. Professional outreach campaign structure
Use separate campaigns for each partner category rather than one generic referral email.
#### Accountant and bookkeeper campaign
Primary value proposition:
- Alternative documentation for self-employed clients
- Income add-backs and business-for-use analysis
- Mortgage planning around tax filings
- Options when declared income does not reflect actual cash flow
- Early identification of financing barriers before a purchase or renewal
#### Lawyer and notary campaign
Primary value proposition:
- Urgent completions
- Estate, separation, buyout, and payout situations
- Mortgage arrears and property-tax issues
- Private and alternative financing
- Clear communication on conditions, funding, and closing timelines
#### Realtor campaign
Primary value proposition:
- Rescue options for declined approvals
- Self-employed and credit-challenged buyers
- Alternative financing for firm deals
- Prequalification escalation before subject removal
- Construction, renovation, and rental-property financing
#### Financial planner, wealth advisor, and insurance advisor campaign
Primary value proposition:
- Debt restructuring without liquidating long-term assets
- Equity-based financing
- Mortgage planning for incorporated professionals and business owners
- Referral coordination that protects the primary advisor relationship
#### Bank and credit-union referral campaign
Primary value proposition:
- A responsible destination for files outside institutional policy
- B-lender, private, commercial, and alternative options
- A referral process that protects the original lender relationship
- Status confirmation and professional feedback on outcomes
#### Builder and developer campaign
Primary value proposition:
- Land, construction, infill, bridge, and completion financing
- Project-readiness assessment
- Sponsor, equity, permit, budget, and exit-strategy review
- Access to alternative and private capital sources
### 3. Recommended outreach sequence
#### Stage 1 — Initial professional introduction
The first message should:
- Identify Dennis and the relevant specialty
- Demonstrate understanding of the partner’s client situations
- Explain the referral process
- Emphasize professional communication and relationship protection
- Offer a short call, resource, or referral guide
- Avoid asking for confidential client information by ordinary email
#### Stage 2 — Educational proof of value
Send a profession-specific resource such as:
- Self-employed mortgage documentation guide for accountants
- Declined-financing rescue checklist for Realtors
- Alternative mortgage closing checklist for lawyers
- Debt-restructuring referral guide for financial planners
- B-lender referral criteria for bank representatives
- Construction financing readiness checklist for builders
#### Stage 3 — Case-pattern examples
Use anonymized, non-promissory examples showing when a referral may be useful:
- Strong equity but limited provable income
- Business owner with low declared personal income
- Renewal declined because of credit or debt-service ratios
- Firm purchase requiring an alternative solution
- Mortgage or property-tax arrears
- Estate or relationship buyout
- Construction project requiring bridge or completion capital
#### Stage 4 — Meeting invitation
Offer a concise partner meeting focused on:
- The partner’s typical client problems
- Referral criteria
- Communication expectations
- Privacy and consent
- Status reporting
- Escalation procedures
#### Stage 5 — Referral activation
After a positive response:
- Create or confirm the partner profile
- Issue the secure referral link
- Send the referral criteria guide
- Explain confirmation and status milestones
- Record preferred communication method
- Assign an internal relationship owner
#### Stage 6 — Ongoing nurture
Send useful updates only at an appropriate cadence, such as:
- New lender appetite or program changes
- Common documentation issues
- Case-study summaries
- Market or policy implications
- Referral-partner webinars
- Quarterly outcome summaries
### 4. Referral intake methods
Provide three controlled referral paths:
#### Secure referral form
The preferred method. It should collect:
- Referring professional and firm
- Client name and contact information
- Confirmation that the client agreed to be contacted
- Referral category
- Brief financing objective
- Property location
- Approximate timeline
- Preferred introduction method
- Any immediate deadline
Do not request highly sensitive documents during the first referral submission.
#### Warm email introduction
The professional introduces the client and Dennis in one email. The system should identify the referral, create the CRM records, and reply with a confirmation while avoiding unnecessary disclosure in the email thread.
#### Partner portal or CRM submission
Strategic partners may receive a secure portal showing referral submission and permitted status information.
### 5. Referral received confirmation
Every referral should trigger two separate confirmations.
#### Confirmation to the referring professional
**Trigger:** `referral.received`
The message should:
- Thank the professional
- Confirm the referral reference number
- Identify the general referral category
- Confirm the date and time received
- State who will review it
- Explain the expected first-contact timeframe
- Provide a secure status link when available
- Avoid repeating unnecessary client-sensitive details
Recommended wording components:
- “We have received your referral.”
- “The referral has been assigned for initial review.”
- “We expect to contact the client within the stated service window.”
- “We will provide milestone updates where consent and privacy requirements allow.”
#### Confirmation to the referred client
**Trigger:** referral consent validated and contact authorized
The message should:
- Identify the referring professional
- Explain why Mortgages by Dennis Eng is contacting the client
- Confirm the type of assistance requested
- State that no approval or commitment has been made
- Provide a secure assessment or booking link
- Explain privacy and consent options
- Provide a direct contact method
### 6. Referral milestone communications
Use a controlled status vocabulary so the professional receives useful information without receiving confidential underwriting details.
Recommended milestones:
- Referral received
- Client contact attempted
- Client contacted
- Initial consultation booked
- Initial review completed
- Additional information requested
- Application preparation underway
- Submitted for financing review
- Financing option identified
- Transaction completed or funded
- Referral paused
- Client declined to proceed
- Unable to assist
The referring professional should not automatically receive:
- Credit scores
- Income documents
- lender conditions
- detailed decline reasons
- account balances
- private legal or personal information
Status updates should be based on client consent, legitimate operational need, and the professional’s role in the transaction.
### 7. Core referral email templates
Add the following templates to the Paper and Resend registry:
- `MBDE-REF-001 — Professional Outreach Introduction`
- `MBDE-REF-002 — Profession-Specific Resource Delivery`
- `MBDE-REF-003 — Referral Partnership Meeting Invitation`
- `MBDE-REF-004 — Referral Partner Activation`
- `MBDE-REF-005 — Referral Received — Partner Confirmation`
- `MBDE-REF-006 — Referral Introduction — Client Confirmation`
- `MBDE-REF-007 — Client Contacted — Partner Update`
- `MBDE-REF-008 — Consultation Booked — Partner Update`
- `MBDE-REF-009 — Referral Progress Update`
- `MBDE-REF-010 — Referral Completed or Funded`
- `MBDE-REF-011 — Referral Unable to Proceed`
- `MBDE-REF-012 — Partner Quarterly Outcome Report`
- `MBDE-REF-013 — Partner Re-engagement`
Each template should include:
- Audience
- Trigger
- sender identity
- permitted data fields
- consent basis
- human approval requirement
- primary CTA
- version number
- owner
- KPI
### 8. Event and trigger specification
Recommended event flow:
`partner.identified → outreach reviewed → professional outreach draft created`
`partner.outreach_approved → campaign email sent → delivery and reply events written to CRM`
`partner.responded_positive → relationship task created → meeting link sent`
`partner.activated → secure referral link issued → partner segment updated`
`referral.received → CRM lead and referral records created → partner confirmation sent`
`referral.consent_validated → client confirmation sent → advisor task created`
`referral.client_contacted → permitted partner status update sent`
`referral.consultation_booked → partner milestone updated`
`referral.application_started → internal pipeline updated; external update sent only when permitted`
`referral.funded → attribution recorded → thank-you and outcome message sent`
`referral.closed_unfunded → reason category recorded → appropriate partner update sent`
Every trigger should define:
- Required payload
- idempotency key
- eligibility and consent checks
- template version
- delivery channel
- retry rule
- failure escalation
- CRM state change
- SEI attribution event
### 9. Referral attribution model
Extend SEI beyond organic search to measure professional-referral value.
Recommended attribution chain:
`Professional category → partner → campaign → response → meeting → referral → advisor-ready → application → funded → revenue`
Track:
- Outreach delivery rate
- Positive reply rate
- Meeting-booked rate
- Partner activation rate
- Referrals per active partner
- Advisor-ready referral rate
- Application rate
- Funded rate
- Funded volume by partner
- Revenue by partner and profession
- Average time from referral to first contact
- Average time from referral to funding
- Partner retention and repeat-referral rate
Recommended partner value calculation:
`Partner value = attributed funded revenue + strategic opportunity value − outreach and servicing cost`
### 10. Referral partner scorecard
Create a quarterly scorecard containing only appropriate aggregate information:
- Referrals submitted
- Referrals contacted within SLA
- Consultations completed
- Applications initiated
- Transactions completed
- Aggregate funded volume where appropriate
- Common referral-fit observations
- Recommended future referral categories
- Relationship next steps
Do not include client-sensitive details in aggregate partner reporting.
### 11. Service-level standards
Recommended initial standards:
- Automated referral receipt confirmation: immediately
- Internal assignment: within 5 minutes
- Urgent referral acknowledgement by advisor: within 5 minutes during operating hours
- Standard first client contact: within 15–30 minutes during operating hours
- Partner confirmation of first-contact outcome: same business day when permitted
- Material milestone update: within one business day of the milestone
- Final outcome record: within two business days of closure or funding
Missed SLAs should create an escalation task and notify the relationship owner.
### 12. Resend MCP and Paper workflow
Use Paper to create profession-specific branded campaigns and referral confirmations. Use Resend MCP to:
- Create draft outreach templates
- Create profession-based partner segments
- Prepare approved broadcasts
- Create and version referral confirmations
- Inspect delivery and reply failures
- Monitor partner engagement
- Produce campaign performance summaries
- Update template copy after approved learnings
Use the Resend SDK/API for deterministic referral confirmations and milestone messages triggered by the CRM.
### 13. Compliance and relationship safeguards
Required controls:
- Do not imply guaranteed approvals, rates, or funding outcomes
- Do not purchase or exchange referrals where prohibited by licensing, brokerage, employer, or professional rules
- Confirm the client has agreed to be contacted
- Separate professional relationship communication from broad marketing consent
- Maintain suppression and do-not-contact controls
- Avoid sensitive client information in outreach and confirmation emails
- Record the referring source accurately
- Preserve the referring professional’s relationship with the client
- Require licensed review for mortgage recommendations
- Review referral-fee or co-marketing arrangements before implementation
### 14. Recommended pilot
Launch a 60–90 day professional referral pilot with three partner segments:
1. Accountants and bookkeepers serving self-employed clients
2. Realtors handling declined, non-prime, or firm-purchase situations
3. Lawyers and notaries involved in urgent closings, estates, buyouts, and arrears
Pilot assets:
- Three profession-specific landing pages
- Three outreach sequences
- Three downloadable referral guides
- One secure referral form with profession-specific routing
- Partner and client referral confirmations
- Referral status milestones
- Quarterly-style pilot scorecard
- CRM and SEI attribution dashboard
Initial pilot targets:
- Outreach delivery rate above 97%
- Positive reply rate of 5–10%
- Meeting-booked rate of 2–5%
- Activation of 5–10 referral partners
- First referral from at least 25% of activated partners
- First client contact within 30 minutes during operating hours
- Referral receipt confirmation delivered immediately
- 90% or greater completion of required referral-status records
### 15. Implementation priority
Add the professional referral channel in this order:
1. Partner data model and consent rules
2. Secure referral intake
3. Partner and client confirmation templates
4. CRM event and status model
5. Profession-specific Paper artboards
6. Resend template creation and approval
7. Outreach pilot campaigns
8. Referral SLA monitoring
9. Referral attribution dashboard
10. Quarterly partner scorecards and optimization
---
## Addendum — Twilio SMS Integration for SEI, Rank-and-Rent, and Professional Referrals
### Strategic role
Twilio should operate as the **real-time SMS, verification, and response-acceleration layer** for Mortgages by Dennis Eng. Resend remains the primary email platform, while Twilio handles urgent, concise, action-oriented communications where timing matters.
Twilio should not be treated as the system of record. Atomic CRM or Convex must retain consent, lead ownership, referral attribution, campaign state, tenant identity, message history, and funded outcomes.
### Recommended division of responsibility
- **Twilio MCP:** read-only API discovery and development assistance for Codex, Claude Code, Warp, or another coding agent.
- **Twilio CLI:** configuration, testing, diagnostics, deployment scripts, and controlled administrative tasks.
- **Twilio SDK or REST API:** deterministic production delivery of SMS messages.
- **Twilio webhooks:** inbound replies, delivery events, STOP requests, failures, and message-status updates.
- **Atomic CRM or Convex:** workflow orchestration, consent, segmentation, suppression, ownership, and attribution.
- **SEI:** measurement of how SMS contributes to assessment completion, appointments, accepted referrals, applications, and funded revenue.
### Target architecture
`SEO or referral source → landing page or referral form → CRM consent and eligibility checks → workflow queue → Twilio Messaging Service → delivery and inbound webhooks → CRM and SEI attribution`
The messaging layer should be event-driven rather than agent-dependent. AI agents may draft templates, inspect failures, classify replies, and recommend changes, but production sends should originate from approved workflows.
### Twilio Messaging Services
Create separate Messaging Services by communication purpose.
#### MBDE Transactional
Use for:
- Mortgage assessment confirmations
- Appointment confirmations and reminders
- Secure-link notifications
- Referral-received confirmations
- Document-readiness notifications
#### MBDE Lead Follow-up
Use for:
- Incomplete assessment recovery
- Callback requests
- Renewal reminders
- Alternative-lending follow-up
- Time-sensitive lead reactivation
#### MBDE Professional Partners
Use for:
- Referral acknowledgement
- Referral milestone updates
- Partner event invitations
- Educational campaign follow-up
- Partner re-engagement
#### Rank-and-Rent Tenant Messaging
Use for:
- Tenant-specific sender identity
- Territory-specific campaigns
- Broker alerts and lead acceptance
- Tenant-level reporting
- Separate consent, suppression, and audit controls
### Core borrower SMS workflows
#### Workflow 1 — New mortgage inquiry
**Trigger:** `assessment.completed`
**Actions:**
1. Confirm service-related SMS consent.
2. Create or update the lead in the CRM.
3. Send immediate confirmation.
4. Alert the assigned advisor when urgency or lead score meets the threshold.
5. Record delivery and reply events.
**Template:**
> Dennis here. We received your alternative mortgage assessment. I’ll review the property, equity, and financing goal and follow up shortly. Reply CALL for a callback or STOP to opt out.
#### Workflow 2 — Incomplete assessment recovery
**Trigger:** `assessment.started` followed by an incomplete status after the approved delay.
**Eligibility checks:**
- Valid SMS consent
- Assessment still incomplete
- No active suppression
- Frequency cap not exceeded
- Local quiet hours respected
**Template:**
> Your mortgage assessment has been saved. We still need the approximate property value, mortgage balance, and financing timeline. Continue securely: `{{continuation_url}}`
#### Workflow 3 — Urgent alternative mortgage lead
**Trigger examples:**
- Renewal declined
- Financing required within 30 days
- Mortgage or property-tax arrears
- Firm completion date
- Construction draw deadline
**Actions:**
1. Send borrower acknowledgement.
2. Send advisor or broker alert.
3. Create a priority task.
4. Start the first-response SLA.
5. Escalate or reroute when the SLA is missed.
#### Workflow 4 — Appointment lifecycle
Messages may include:
- Appointment confirmation
- 24-hour reminder
- Short same-day reminder
- Reschedule link
- Post-call document or assessment link
Do not include detailed financial information in appointment messages.
### Professional referral SMS lifecycle
#### Event: `referral.received`
Send two separate confirmations.
**Referral partner confirmation:**
> Thank you, `{{partner_first_name}}`. We received your referral for `{{client_first_name}}`. Reference: `{{referral_reference}}`. We will acknowledge the client and provide permitted milestone updates.
**Referred client introduction:**
> Hi `{{client_first_name}}`, `{{partner_name}}` introduced us regarding your mortgage financing needs. I’m Dennis Eng. Reply CALL for a confidential conversation or use this secure assessment: `{{assessment_url}}`.
#### Recommended referral milestone events
- `referral.received`
- `client.acknowledged`
- `client.contacted`
- `discovery.completed`
- `strategy.review_started`
- `application.submitted`
- `financing.arranged`
- `referral.closed`
The referral partner should receive only the minimum status permitted by the client’s consent and the referral agreement. Do not disclose credit details, balances, income, documents, lender terms, or underwriting issues without express authorization.
### Professional outreach campaigns
Twilio may support professional referral campaigns, but it should complement—not replace—trust-based email and personal outreach.
Priority partner audiences:
- Accountants and bookkeepers
- Realtors and real-estate teams
- Financial planners and insurance advisors
- Business lawyers and family lawyers
- Contractors, builders, and renovation firms
- Commercial bankers and business-loan officers
- Property managers and strata professionals
Recommended SMS use cases:
- Follow-up after an email introduction
- Event or webinar reminder
- Referral-link delivery after a partner conversation
- Confirmation that a co-branded assessment page is active
- Re-engagement of an existing partner relationship
Cold bulk SMS should not be used as the default professional-acquisition method. Every send must have an appropriate consent basis, clear sender identity, and opt-out handling.
### Campaign themes for alternative lending
Approved themes may include:
- **Tax Strategy:** tax-efficient business owners whose taxable income understates real cash flow
- **Bank-No Reset:** a traditional lender decline may require a different lending strategy
- **Debt Reset:** use of home equity to restructure expensive debt and improve cash flow
- **Life Event / Cause and Cure:** temporary credit issues caused by a specific event and supported by a documented resolution
- **Alt-to-Prime Review:** a 12–24 month transition strategy toward prime eligibility
- **Renewal Readiness:** preparation before maturity or lender renewal review
SMS copy must remain educational and action-oriented. It should not promise approval, rates, savings, or lender outcomes.
### Event and trigger specification
#### `assessment.completed`
- Audience: borrower
- Message: confirmation and next step
- Channel: transactional SMS
- Duplicate prevention: one confirmation per assessment version
- CRM update: `sms_confirmation_sent`
#### `assessment.incomplete`
- Audience: borrower
- Message: secure continuation link
- Delay: configurable
- Maximum attempts: defined by campaign policy
- Stop condition: assessment completed, replied, opted out, or assigned to active advisor
#### `referral.received`
- Audience: referral partner and referred client
- Message: acknowledgement and introduction
- CRM update: referral confirmation timestamps
#### `lead.advisor_ready`
- Audience: assigned broker or tenant
- Message: masked lead alert with secure acceptance link
- Sensitive data: prohibited in SMS
#### `appointment.scheduled`
- Audience: borrower
- Message: appointment confirmation and reminder sequence
#### `sms.inbound_received`
- Actions: classify intent, update consent, create task, or trigger response workflow
#### `sms.delivery_failed`
- Actions: record failure, apply retry policy, verify phone number, or switch to email when appropriate
### Inbound reply classification
AI may classify inbound SMS into approved categories:
- CALL request
- Booking request
- Assessment question
- Document question
- Information correction
- Not interested
- STOP or unsubscribe
- Wrong number
- Complaint
- Urgent deadline
- Referral partner update
STOP, UNSUBSCRIBE, CANCEL, END, or equivalent opt-out language must immediately update the suppression record. Automated classification must not override an explicit opt-out.
### Data model additions
Add the following fields to the CRM or event store:
- `twilio_message_sid`
- `twilio_messaging_service_sid`
- `sms_campaign_id`
- `sms_template_id`
- `sms_template_version`
- `phone_e164`
- `consent_sms_status`
- `consent_sms_source`
- `consent_sms_timestamp`
- `sms_suppression_status`
- `sms_sent_at`
- `sms_delivered_at`
- `sms_failed_at`
- `sms_error_code`
- `sms_reply_intent`
- `sms_reply_at`
- `referral_id`
- `partner_id`
- `tenant_id`
- `site_id`
- `keyword_cluster`
- `appointment_id`
- `application_id`
- `funded_file_id`
### SEI attribution model
Twilio events should be connected to the same commercial attribution chain used for email:
`Keyword or referral partner → landing page or referral form → lead → SMS confirmation → reply or continuation click → completed discovery → appointment → application → funded mortgage → revenue`
Recommended SMS-assisted metrics:
- SMS delivery rate
- Reply rate
- Callback-request rate
- Continuation-link click rate
- Incomplete-assessment recovery rate
- Time to first meaningful response
- Appointment-booked rate
- Referral acknowledgement time
- Referral-to-discovery rate
- Broker lead-acceptance rate
- Application rate after SMS engagement
- Funded revenue influenced by SMS
- Opt-out and complaint rate
### Multi-tenant controls
A rank-and-rent tenant must not receive unrestricted Twilio access.
Before every send, confirm:
- Authenticated user and tenant
- Approved Messaging Service
- Approved sender identity
- Lead or partner relationship
- SMS consent basis
- Suppression status
- Message category
- Quiet-hour rules
- Frequency cap
- Territory ownership
- Required approval status
- Audit-log creation
Tenant messages must use tenant-specific templates and tracking. A tenant may not export or reuse another tenant’s leads, phone numbers, templates, or campaign history.
### Compliance and privacy safeguards
- Identify the sender clearly.
- Maintain separate consent for service messages and optional promotional campaigns.
- Capture consent source, timestamp, language, and disclosure version.
- Process opt-outs immediately.
- Respect applicable quiet hours and frequency limits.
- Do not include sensitive borrower details in SMS.
- Use secure, expiring links for assessments, documents, and lead acceptance.
- Do not state or imply mortgage approval.
- Do not disclose referral details beyond the client’s authorization.
- Retain an auditable record of every send, reply, consent change, and suppression event.
### Failure and fallback handling
When SMS delivery fails:
1. Record the Twilio error code.
2. Do not repeatedly retry permanent failures.
3. Verify whether the number is valid and mobile-capable.
4. Use email fallback when consent and workflow permit.
5. Create a manual task for urgent leads.
6. Monitor failure patterns by tenant, campaign, carrier, and template.
### Development workflow using Twilio MCP and CLI
#### Twilio MCP
Use the official Twilio MCP server for:
- API discovery
- Endpoint and parameter lookup
- Webhook schema retrieval
- SDK integration planning
- Coding-agent assistance
The MCP layer should be treated as a development aid, not the production execution engine.
#### Twilio CLI
Use the CLI for:
- Sending controlled test messages
- Inspecting message records
- Verifying numbers and Messaging Services
- Configuring development and staging resources
- Testing webhook endpoints
- Supporting deployment and diagnostics
#### Production execution
Use the Twilio SDK or REST API from the application workflow layer. Production actions should be deterministic, tenant-aware, consent-aware, and fully audited.
### Initial implementation phases
#### Phase 1 — Foundation
- Create Twilio subaccount or approved account structure
- Configure Messaging Services
- Acquire or assign sender numbers
- Configure delivery-status and inbound webhooks
- Add SMS consent and suppression fields to the CRM
- Create development and production environments
#### Phase 2 — Transactional workflows
- Assessment confirmation
- Incomplete assessment recovery
- Appointment confirmation and reminders
- Referral received confirmations
- Broker or advisor priority alerts
#### Phase 3 — Professional referral operations
- Partner referral acknowledgement
- Referred-client introduction
- Milestone status updates
- Secure referral-link delivery
- Partner-level attribution dashboard
#### Phase 4 — Rank-and-rent tenant messaging
- Tenant-specific services and templates
- Territory and sender controls
- Broker lead-acceptance SMS
- SLA escalation
- Tenant-level performance reporting
#### Phase 5 — SEI optimization
- Attribute SMS engagement to keyword clusters and referral partners
- Compare SMS-assisted and email-only conversion
- Test timing and CTA variations
- Optimize based on applications and funded outcomes rather than clicks alone
### Pilot recommendation
Launch the first Twilio pilot around the **professional referral and B-lender assessment lifecycle**.
Pilot scope:
1. Professional submits a referral.
2. Referral partner receives immediate SMS and email confirmation.
3. Referred client receives an introduction and secure assessment link.
4. Dennis or the assigned advisor receives an urgent task.
5. Appointment reminders are sent.
6. Referral partner receives consented milestone updates.
7. SEI attributes the opportunity and funded outcome to the referring partner, campaign, landing page, and message sequence.
### Initial acceptance criteria
- Transactional SMS delivery rate at or above 95%
- Referral acknowledgement issued within one minute
- Opt-out events processed immediately
- No sensitive borrower data transmitted in SMS
- Duplicate-send rate below 0.5%
- All SMS events recorded against the correct lead, referral, tenant, and campaign
- Broker or advisor priority alerts delivered within the workflow SLA
- Referral partners receive only authorized milestone information
- SMS-assisted conversions are measurable through application and funding outcomes
> **Operating principle:** Resend builds trust through complete, informative email communication. Twilio protects momentum through timely, concise action. Atomic CRM or Convex governs consent and workflow, while SEI determines whether each message contributes to a qualified and funded mortgage opportunity.
---
## Addendum — Twilio enquiry confirmation, lead verification, and double opt-in automation
Twilio should be used as an **identity, consent, and application-activation layer** at the beginning of the mortgage lead journey—not only as a follow-up channel.
### Strategic objective
Use SMS to confirm that:
1. The enquiry was intentionally submitted.
2. The mobile number belongs to the person completing the form.
3. The lead agrees to continue the mortgage application process.
4. The borrower has an immediate path back into the application.
5. The CRM records a defensible verification and consent event before deeper automation begins.
### Recommended intake flow
`Website enquiry submitted → CRM creates unverified lead → Twilio sends confirmation or verification message → borrower verifies mobile number and intent → CRM marks lead verified → application workflow is activated → Resend sends full email confirmation and next steps → advisor is notified`
### Verification options
#### Option A — One-tap confirmation
The borrower receives a message such as:
> Hi \{\{\{FIRST_NAME\|there\}\}\}, this is Mortgages by Dennis Eng. We received your mortgage enquiry. Please confirm that you submitted it and want us to continue: \{\{\{CONFIRM_URL\}\}\}. Reply STOP to opt out.
The secure link should:
- expire after a defined period,
- be tied to the lead and mobile number,
- prevent reuse,
- write the verification timestamp to the CRM,
- preserve the source page, keyword cluster, and referral source.
#### Option B — Twilio Verify one-time code
Use Twilio Verify when stronger proof of mobile-number ownership is required.
`Lead enters mobile number → Twilio sends one-time code → borrower enters code → number marked verified → application continues`
Recommended use cases:
- High-value alternative or commercial leads
- Paid rank-and-rent leads
- Professional referrals
- Lead marketplace distribution
- Cases where duplicate or fraudulent submissions are a concern
#### Option C — SMS reply confirmation
The borrower receives:
> We received your mortgage enquiry. Reply YES to confirm that you want Mortgages by Dennis Eng to review it. Reply STOP to opt out.
The inbound webhook classifies:
- `YES` or `CONFIRM` → verified and active
- `CALL` → create urgent callback task
- `TEXT` → continue by SMS
- `STOP` → suppress SMS and record withdrawal
- Any other reply → route to inbound triage
### Double opt-in model
The recommended double opt-in sequence is:
1. The borrower submits the web form and checks the appropriate communication consent box.
2. The system stores the submission as `pending_verification`.
3. Twilio sends an SMS verification message.
4. The borrower confirms through a secure link, one-time code, or approved keyword.
5. The CRM stores:
	- original consent text,
	- form version,
	- page and site source,
	- submission timestamp,
	- IP and device metadata where appropriate,
	- mobile number,
	- verification method,
	- verification timestamp,
	- Twilio message or verification reference,
	- current communication status.
6. The lead becomes `verified_active`.
7. The automated application and nurturing workflows begin.
This verification should confirm the requested mortgage-service communication. Optional future marketing consent should remain separate.
### Lead state model
Use explicit lifecycle states:
- `enquiry_received`
- `pending_mobile_verification`
- `verified_active`
- `verification_failed`
- `verification_expired`
- `duplicate_review`
- `application_started`
- `application_incomplete`
- `application_completed`
- `advisor_ready`
- `withdrawn`
- `sms_suppressed`
Automation should only advance verified leads into sensitive or higher-cost workflows unless an authorized operator overrides the rule.
### Automated lead-application workflow
Once the enquiry is verified:
1. Send an SMS confirmation with the secure application link.
2. Send a detailed Resend email with the assessment summary and next steps.
3. Create or activate the CRM opportunity.
4. Pre-fill the application with verified form data.
5. Start the incomplete-application timer.
6. Notify Dennis or the assigned broker.
7. Trigger urgency routing when the borrower has a deadline, arrears, declined renewal, or purchase completion.
8. Write every interaction to SEI for source-to-funded attribution.
### Example verified-lead message
> Thank you, \{\{\{FIRST_NAME\|there\}\}\}. Your mortgage enquiry is confirmed. Continue your secure application here: \{\{\{APPLICATION_URL\}\}\}. Your reference is \{\{\{LEAD_REFERENCE\}\}\}. Reply CALL for a callback or STOP to opt out.
### Incomplete application recovery
After verification, use controlled reminders:
- 30–60 minutes: saved-application reminder
- Next business day: missing-information request
- 48–72 hours: educational follow-up based on mortgage scenario
- Final reminder: close or pause the application unless the borrower continues
Each reminder must check:
- consent status,
- suppression status,
- application status,
- duplicate-message protection,
- quiet hours,
- tenant and sender identity,
- recent advisor contact.
### Professional referral workflow
For referred leads:
`Partner submits referral → client receives verification SMS → client confirms intent → referral marked verified → partner receives referral-received confirmation → client application activates → milestone updates begin`
The professional should not receive a detailed status until the client has confirmed the referral and the permitted disclosure scope.
### Fraud, duplicate, and lead-quality controls
Twilio verification can reduce:
- fake enquiries,
- incorrect phone numbers,
- duplicate submissions,
- accidental referral entries,
- low-intent or automated form spam,
- charge disputes for paid leads.
Recommended controls:
- rate-limit verification attempts,
- limit code retries,
- expire links and codes,
- detect repeated numbers across multiple identities,
- flag multiple submissions from the same device or session,
- prevent lead sale or broker routing before verification,
- preserve an auditable verification trail.
### CRM and SEI fields
Add:
- `phone_verification_status`
- `phone_verified_at`
- `phone_verification_method`
- `twilio_verify_sid`
- `twilio_message_sid`
- `double_opt_in_status`
- `double_opt_in_at`
- `consent_form_version`
- `consent_source_url`
- `application_activation_at`
- `verification_attempt_count`
- `verification_expiry_at`
- `sms_suppressed_at`
### Success metrics
Track:
- Enquiry-to-verification rate
- Verification completion time
- Verified-to-application-start rate
- Verified-to-completed-application rate
- Invalid-number rate
- Duplicate-lead rate
- Referral verification rate
- Time from verified enquiry to first advisor contact
- Cost per verified lead
- Funded revenue per verified lead
### Recommended implementation priority
Build this before broad SMS nurturing.
The first production workflow should be:
`B-lender enquiry → Twilio verification → verified lead activation → secure application link → Resend confirmation → advisor alert → incomplete-application recovery → SEI attribution`
This positions Twilio as the **trust and activation gate** for the mortgage application process, while Resend handles richer email communication and Atomic CRM or Convex remains the system of record.
