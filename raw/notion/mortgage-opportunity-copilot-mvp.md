# Source: Notion (page 3ab9e94c-f0a4-810c-9f6c-f1f49892f3bb)

<callout icon="🎯" color="blue_bg">
	**Current controlling objective:** Mortgage CoPilot exists to generate more qualified mortgage opportunities by combining existing relationship data, borrower stories, LeadSniperAI signals, construction intelligence, and disciplined follow-up. Every MVP feature must help detect, create, prioritize, or convert an opportunity.
</callout>
# Executive Refactor — Mortgage Opportunity CoPilot
## North-Star Outcome
Build an opportunity-generation operating system that answers:
> **Who should Dennis help today, why now, and what is the highest-value action most likely to create a qualified mortgage opportunity?**
The product is not primarily a generic CRM, website, content platform, or GoHighLevel clone. Those are supporting capabilities.
The commercial outcomes are:
1. More qualified mortgage conversations
2. More applications started
3. More renewal, refinance, equity, construction, and alternative-lending opportunities
4. More self-employed and Story Before Score borrowers identified
5. More professional referrals
6. Higher funded volume and gross commission revenue
## Product Constraint
Before accepting a feature into the MVP, apply this test:
> **Will this feature help detect, create, prioritize, or convert a mortgage opportunity within the next 180 days?**
If not, defer it.
---
# 1. Opportunity Engine Model
Mortgage CoPilot will operate five connected opportunity engines.
## Engine A — Existing Relationship and Database Reactivation
Detect opportunities among:
- Past clients
- Old leads
- Uncompleted applications
- Previously declined borrowers
- Alternative borrowers who may now qualify for prime lending
- Clients without a recent annual mortgage review
- Clients with increased equity
- Clients with additional property or family financing needs
Primary offers:
- Annual mortgage review
- Renewal strategy review
- Equity and debt restructuring review
- Alt-to-prime transition review
- Property portfolio review
## Engine B — Renewal Intelligence
Every funded mortgage becomes a future opportunity.
```plain text
Mortgage recorded
→ maturity date captured
→ annual review scheduled
→ 180/120/90/60/30-day renewal triggers
→ updated borrower story collected
→ renewal, refinance, consolidation, or equity opportunity created
```
## Engine C — Self-Employed Borrower Discovery through LeadSniperAI
LeadSniperAI discovers external signals and Mortgage CoPilot converts them into evidence-backed opportunities.
Target segments:
- Incorporated business owners
- Sole proprietors
- Trades and contractors
- Commission earners
- Professionals operating through corporations
- Restaurant, retail, e-commerce, and service businesses
- Real estate investors
- Owners with tax-minimized income
- Owners using retained earnings
- Businesses showing expansion, hiring, new-location, equipment, or property signals
Value-first offer:
> **Business-owner mortgage and financing review covering cash flow, add-backs, retained earnings, property equity, debt structure, and alternative income documentation.**
## Engine D — Construction Opportunity Intelligence
Detect projects and parties associated with:
- Land acquisition
- Major renovations
- Custom homes
- Infill and multiplex development
- Laneway homes
- Small multifamily development
- Bridge and takeout financing
- Private construction loans
- Commercial renovation
- Builder and developer financing
Signal sources may include permits, development applications, rezoning, demolition, property transactions, builder activity, project announcements, and professional referrals.
Each project should connect:
```plain text
Property
├── Owner
├── Developer
├── Builder
├── Architect
├── Realtor
├── Lawyer
├── Accountant
├── Permit or planning signal
└── Financing opportunities
```
## Engine E — Professional Alliance Network
Create opportunities through accountants, lawyers, realtors, financial planners, insolvency professionals, immigration consultants, developers, and builders.
Mortgage CoPilot should identify:
- Which partner should be contacted
- Why the timing is relevant
- What value Dennis can provide first
- Which client or project may justify an introduction
- Which referral relationships are becoming inactive
---
# 2. Story Before Score Segmentation
## Core Principle
A credit score, T4, or debt-service ratio is one data point. The complete story explains:
```plain text
What happened?
Why did it happen?
What has changed?
What strengths and resources exist?
What is the financing objective?
What is the credible path forward?
```
## Four Opportunity Families
### Income-Story Borrowers
- Self-employed and business-for-self
- Commission and bonus income
- Seasonal and contract workers
- Transitional or recently increased income
- Retained earnings and shareholder income
- Foreign income
- Returning-to-work borrowers
### Credit-Story Borrowers
- Credit recovery
- Consumer proposal or bankruptcy history
- Divorce-related credit damage
- Temporary arrears caused by a resolved life event
- High utilization with improving behaviour
- Private-mortgage exit borrowers
- Previously declined borrowers with a defined recovery plan
### Asset-Story Borrowers
- High-net-worth, low-verifiable-income borrowers
- Equity-rich homeowners
- Retirees and aging homeowners
- Real estate investors
- Estate and intergenerational borrowers
- Overseas or non-traditional assets
### Event-Story Borrowers
- Divorce and separation
- Construction and renovation
- Business expansion
- New-to-Canada transition
- Retirement
- Special assessments
- Debt consolidation
- Legal, tax, estate, or mortgage-maturity deadlines
## Additional High-Value Segments
- New-to-Canada borrowers
- Real estate investors and portfolio owners
- Debt consolidation and cash-flow restructuring
- Divorce and spousal buyout
- Estate and family-property transfer
- Reverse mortgage and retirement planning
- Construction and renovation
- Transitional income
- Commission and variable income
- Private-mortgage exit
- Previously declined borrowers
- Non-traditional properties
- Urgent-event borrowers
## Multi-Dimensional Borrower Profile
Do not assign only one borrower label.
```plain text
Primary segment
Secondary segments
Life event
Property context
Opportunity type
Urgency
Current constraint
Positive factors
Evidence confidence
Recommended financing path
Next best action
```
---
# 3. MVP Definition
## MVP Commercial Promise
The first product must allow Dennis to:
1. Import and organize existing contacts and mortgage records
2. Capture new website, partner, LeadSniperAI, and construction leads
3. Understand each borrower’s Story Before Score profile
4. Create and score mortgage opportunities
5. See a daily ranked action queue
6. Record notes, tasks, appointments, and communication history
7. Track opportunities through a practical mortgage pipeline
8. Trigger renewal and reactivation workflows
9. Generate AI-assisted summaries and next-best actions
10. Measure qualified conversations, applications, funded volume, and revenue
## MVP Features — Required
### Relationship Foundation
- Contacts
- Households
- Companies
- Professional partners
- Properties
- Mortgages
- Notes
- Tasks
- Appointments
- Activity timeline
- Consent and communication preferences
### Opportunity Foundation
- Leads and opportunities
- Opportunity type and segment
- Trigger signal
- Evidence
- Estimated mortgage or financing amount
- Estimated revenue
- Probability
- Urgency
- Relationship strength
- Recommended action
- Assigned advisor
- Pipeline stage
- Next-action date
### Command Centre
The home screen must emphasize action, not passive reporting.
Example:
```plain text
Today's highest-value opportunities

1. Renewal opportunity — maturity in 142 days
2. Self-employed owner — expansion signal detected
3. Past alternative borrower — potential prime transition
4. Construction project — permit-backed financing signal
5. Accountant partner — no contact in 90 days
```
### Initial Pipelines
**Consumer Mortgage**
```plain text
New Inquiry
→ Contact Attempted
→ Connected
→ Discovery Scheduled
→ Discovery Complete
→ Documents Requested
→ Application Prepared
→ Submitted
→ Approved
→ Funded
→ Nurture / Not Proceeding
```
**Self-Employed Opportunity**
```plain text
Signal Detected
→ Owner Identified
→ Financing Hypothesis
→ Value-First Outreach
→ Discovery Review
→ Qualified Opportunity
→ Application
→ Funding
```
**Construction Opportunity**
```plain text
Project Signal
→ Parties Identified
→ Financing Need Estimated
→ Project Qualified
→ Capital Strategy
→ Documents and Feasibility
→ Lender / Capital Matching
→ Commitment
→ Funding
```
## Deferred Until After MVP
- Generic visual funnel builder
- Full GoHighLevel feature parity
- Broad social-media publishing
- White-label SaaS administration
- Complex commission accounting
- Fully autonomous outbound agents
- Full CMS replacing Git-based content
- Advanced warehouse and BI platform
- Uncontrolled AI submissions or recommendations
---
# 4. Technical Architecture
## Target Stack
```plain text
Astro application
├── Public SEO and AIO website
├── Landing pages and assessments
├── React islands for calculators and forms
└── React CRM workspace

Convex backend
├── CRM system of record
├── Real-time queries and mutations
├── Opportunity and scoring engine
├── Scheduled renewal and nurture workflows
├── Agent state and recommendations
├── Audit, consent, and integration events
└── HTTP endpoints and external API actions

External services
├── Telnyx — preferred telecom platform under evaluation for SMS, MMS, calls, voice AI, and telecom events
├── Twilio — fallback or transitional telecom provider until Telnyx validation is complete
├── Unipile — connected email, calendar, LinkedIn, and messaging
├── Resend — transactional and lifecycle email where appropriate
├── Clerk — operator and partner authentication
├── LeadSniperAI — external signal and prospect discovery
└── Future Velocity API or structured imports
```
## Frontend Rule
Astro owns public pages, SEO content, layouts, and routing. React remains the runtime for the interactive CRM workspace. Existing React components should be reused rather than rewritten without business justification.
## Backend Rule
Convex becomes the operational system of record. Existing Supabase functionality should be replaced in vertical slices, with a working and testable product after every migration phase.
## Tenancy and Workflow Portability Rule
The first 180-day MVP will operate as a **single-tenant system for **[**MortgagesByDennisEng.ca**](http://MortgagesByDennisEng.ca). Full multi-tenant administration, tenant switching, white-label controls, tenant billing, tenant provisioning, and per-tenant infrastructure are explicitly deferred until commercial demand justifies them.
The MVP should still preserve a low-cost future migration path by:
- Using a simple internal `workspaceId` or equivalent boundary on major business records
- Centralizing authentication and role checks
- Keeping provider credentials and operating settings outside feature logic
- Avoiding Dennis-specific values inside reusable workflow definitions
- Separating workflow definitions from workflow assignments and workflow executions
The initial workspace may use a single identifier such as `mortgages-by-dennis`, without exposing tenant-management features in the user interface.
### Reusable Workflow Architecture
Workflows created during the MVP must be designed as reusable, versioned templates that can later be assigned to additional tenants or workspaces.
```plain text
Workflow template
→ versioned trigger, steps, timing, approvals, and outcomes

Workflow assignment
→ workspace, branding, advisor, channel, timing, and enabled status

Workflow run
→ contact, mortgage, opportunity, project, or partner instance
```
Recommended workflow entities:
- `workflowTemplates`
- `workflowVersions`
- `workflowAssignments`
- `workflowRuns`
- `workflowSteps`
- `workflowEvents`
- `workflowApprovals`
- `integrationConfigs`
Initial reusable templates should include:
- 180/120/90/60/30-day renewal sequence
- Dormant-client reactivation
- New-lead speed-to-contact
- Document collection reminders
- Private-to-prime transition review
- Annual mortgage review
- Self-employed borrower follow-up
- Construction-project qualification
- Google review request
- Professional referral follow-up
Future workspace-level configuration may control:
- Branding and message wording
- Assigned advisor
- Business hours and timing
- Telnyx or Twilio numbers
- Email and calendar accounts
- Consent and approval requirements
- Enabled workflow stages
- Escalation contacts
The MVP does not require a visual workflow builder. Templates may be defined in code or structured configuration, provided they are testable, versioned, auditable, and assignable to the initial workspace.
## Execution Platform Rule — Use ChatGPT Work, Not a Separate Orchestration Application
The 180-day implementation program should use the existing **ChatGPT Convex Backend Project** as the delivery command centre rather than building a separate internal project-management or agent-orchestration application.
The product being built remains Mortgage CoPilot. ChatGPT Work coordinates delivery and monitors progress; Claude Code serves as the primary implementation engine; Codex provides independent review, parallel bounded implementation, CI repair, and verification; GitHub holds the technical source of truth; Notion holds the approved plan, decisions, acceptance evidence, SOPs, and progress record.
```plain text
Dennis — product priorities, mortgage-domain judgment, and final business acceptance
        |
        v
ChatGPT Project: Convex Backend
├── ChatGPT Work — program control, research, specifications, work packages, progress monitoring, reviews, and reporting
├── Claude Code — primary repository implementation, refactors, local testing, debugging, and Convex MCP execution
├── Codex — independent code review, parallel bounded tasks, CI repair, regression testing, and alternative implementations
├── GitHub — branches, pull requests, issues, code review, and technical evidence
├── Notion — roadmap, decisions, status, SOPs, acceptance records, and handoffs
├── Convex MCP — schema, functions, logs, environments, test data, and deployment inspection
└── Scheduled Tasks — recurring status reviews, blocker checks, release reviews, and KPI reporting
```
### Standard Execution Loop
```plain text
Notion phase and commercial priority reviewed
→ ChatGPT Work selects or defines the next bounded work package
→ specification, exclusions, dependencies, and acceptance criteria approved
→ one implementation owner is assigned: Claude Code, Codex, or a human engineer
→ implementation occurs in an isolated branch or worktree
→ automated tests, build checks, and Convex MCP verification completed
→ the non-authoring agent performs independent review where practical
→ ChatGPT Work reconciles Slack activity, GitHub evidence, and Notion acceptance criteria
→ technical reviewer approves the change
→ Dennis performs business acceptance on a real operating scenario
→ GitHub merge and staged deployment
→ Notion status, decision record, SOPs, and known limitations updated
```
### Persistent Work Threads
Maintain focused execution threads inside the Convex Backend Project:
- **Program Control:** roadmap, phase gates, risks, blockers, status, and next work package
- **Product and Mortgage Workflows:** opportunity engines, Story Before Score, pipelines, and business acceptance
- **Architecture and Data:** Astro, React, Convex, authentication, migration, schemas, privacy, and audit
- **Growth Engines:** LeadSniperAI, self-employed signals, construction opportunities, SEO, and AIO assets
- **Integration Review:** Telnyx versus Twilio, Unipile, Resend, Velocity imports, webhooks, and retries
### Platform Boundary
Do not build a separate orchestration product during the MVP merely to manage implementation. Build delivery-management features inside Mortgage CoPilot only when they create direct user or commercial value. ChatGPT Work must not replace Git controls, automated testing, staging, human compliance review, production permissions, or final mortgage-business judgment.
---
# 5. Delegated Delivery Operating Model
## Delivery Goal
The 180-day program must produce both a working product and a repeatable delivery system in which defined work can be delegated to AI agents or an implementation team without losing architectural control, security, compliance, or acceptance quality.
Dennis remains the product owner and mortgage-domain authority. He should approve priorities, borrower-facing positioning, compliance-sensitive workflows, and commercial acceptance. He should not become the daily bottleneck for coding, testing, documentation, data preparation, or routine implementation decisions.
## Delegation Structure
```plain text
Dennis — Product Owner and Final Business Acceptance
        |
        v
AI / Human Delivery Lead — backlog, sequencing, dependencies, reviews
        |
        +-- Architecture Agent / Technical Lead
        +-- Convex Backend Agent / Engineer
        +-- Astro + React Frontend Agent / Engineer
        +-- Data Migration and QA Agent / Analyst
        +-- Integration Agent / Engineer
        +-- SEO and Content Agent / Specialist
        +-- Compliance Review Agent + Human Reviewer
        +-- Test and Release Agent / QA Engineer
```
## Required Work-Package Standard
No delegated task should begin without:
- Business objective
- User story or operating scenario
- Scope and explicit exclusions
- Dependencies
- Files or modules affected
- Data and security requirements
- Acceptance criteria
- Required tests
- Evidence to attach when complete
- Reviewer and approval owner
- Rollback or recovery notes where applicable
Tasks should normally be sized to one or two working days. Larger features must be decomposed into independently testable vertical slices.
## AI Agent Responsibilities
AI agents may:
- Inspect repositories and document architecture
- Draft specifications and implementation plans
- Create isolated feature branches or worktrees
- Implement bounded code changes
- Write and run tests
- Produce migration scripts and seed data
- Draft technical documentation and SOPs
- Review diffs against acceptance criteria
- Investigate defects using logs and Convex MCP
- Prepare release notes and handoff packages
AI agents may not independently:
- Approve mortgage advice or lender recommendations
- Initiate uncontrolled prospect outreach
- Change consent, retention, or compliance policy
- Deploy high-risk changes without review
- Access production secrets beyond least privilege
- Delete production data without an approved recovery plan
- Mark a business feature accepted on Dennis’s behalf
## Implementation Team Responsibilities
Human implementers should own work requiring:
- Production infrastructure judgment
- Security and privacy review
- Complex third-party integration troubleshooting
- Data reconciliation and migration sign-off
- Accessibility and usability judgment
- Regulatory interpretation
- Final release approval
## ChatGPT Work, Claude Code, Codex, Superpowers, and Convex MCP Workflow
ChatGPT Work, Claude Code, and Codex should coexist through explicit role separation.
### Primary Responsibilities
- **ChatGPT Work:** program control, monitoring, specifications, work-package creation, evidence reconciliation, status reporting, and phase-gate review
- **Claude Code:** primary builder for substantial repository changes, Astro/React/Convex implementation, local debugging, testing, and direct Convex MCP use
- **Codex:** independent code review, parallel non-overlapping work packages, CI and test repair, security and regression checks, and alternative implementation where useful
- **Human implementation team:** production judgment, complex integration troubleshooting, security review, data reconciliation, accessibility, and release approval
```plain text
Brief approved
→ Superpowers discovery and specification
→ ChatGPT Work decomposes the plan into bounded work packages
→ one owner is assigned to each package
→ isolated branch or worktree created
→ tests written or acceptance harness defined
→ Claude Code, Codex, or human engineer implements
→ Convex MCP used for schema, logs, functions, environments, test data, and debugging
→ non-authoring agent or human reviewer performs independent review
→ automated verification and CI pass
→ ChatGPT Work checks evidence against the approved work package
→ Dennis performs business acceptance
→ merge and staged deployment
→ operational documentation updated
```
### Agent-Collision Rules
- One GitHub issue and one implementation owner per work package
- Separate branch or worktree for every active package
- Claude Code and Codex must not edit the same files concurrently without an explicit coordination note
- The latest main branch must be pulled before a package begins
- Shared architecture, schema, naming, security, and testing standards are authoritative
- Pull requests must identify the authoring agent and reviewing agent
- No agent may approve its own high-risk change as the sole reviewer
- Notion records accepted architecture and product decisions; GitHub records actual implementation evidence
### Default Maker–Reviewer Assignment
<table fit-page-width="true" header-row="true">
<tr>
<td>Work type</td>
<td>Primary maker</td>
<td>Reviewer</td>
</tr>
<tr>
<td>Convex schema and backend vertical slices</td>
<td>Claude Code</td>
<td>Codex or technical lead</td>
</tr>
<tr>
<td>Astro and React migration</td>
<td>Claude Code or assigned engineer</td>
<td>Codex</td>
</tr>
<tr>
<td>Small isolated bug or CI failure</td>
<td>Codex</td>
<td>Claude Code or technical lead</td>
</tr>
<tr>
<td>Large repository refactor</td>
<td>Claude Code</td>
<td>Codex plus human review</td>
</tr>
<tr>
<td>Security, tenant isolation, and regression audit</td>
<td>Codex or technical lead</td>
<td>Human reviewer</td>
</tr>
<tr>
<td>Business and mortgage workflow acceptance</td>
<td>Dennis</td>
<td>ChatGPT Work records evidence</td>
</tr>
</table>
Convex MCP should be used for deployment inspection, schema awareness, function execution, logs, environment validation, test data, and debugging. MCP access is an implementation accelerator, not a substitute for application authorization, tenant isolation, code review, staging, or audit controls.
## Definition of Done
A delegated feature is complete only when:
1. Acceptance criteria pass
2. Automated tests pass
3. Security, authenticated-role boundaries, and the future workspace boundary are verified
4. Failure and retry behaviour is documented
5. User-facing behaviour is demonstrated
6. Documentation is updated
7. A reviewer approves the change
8. Dennis or the delegated business owner accepts the operating outcome
## Management Cadence
- **Daily:** agents and implementers update task status, evidence, blockers, and next action
- **Twice weekly:** technical review of merged work, defects, architecture drift, and dependencies
- **Weekly:** Dennis performs business acceptance on real mortgage scenarios
- **Every 30 days:** release gate, KPI review, scope reset, and delegation-effectiveness review
## Delegation Success Metrics
- Percentage of tasks completed without Dennis performing implementation work
- Acceptance-pass rate on first review
- Defect and regression rate
- Cycle time from approved brief to deployed feature
- Percentage of tasks with tests and evidence attached
- Number of unresolved blockers older than five working days
- Opportunity outcomes produced by released features
Target by Day 180:
- At least 70% of routine implementation work delegated
- At least 80% first-pass acceptance on well-defined work packages
- No critical production change without human review
- Complete SOPs for development, release, incident response, data imports, and integration failures
- A prioritized post-180-day backlog that the team or agent system can continue executing
---
# 6. Phased 180-Day Delegated Implementation and Execution
## Phase 0 — Discovery, Scope Lock, Delegation Design, and Migration Map
**Timing:** Days 1–10
**Objective:** Prevent uncontrolled rebuilding and define the smallest revenue-producing product.
### Deliverables
- Complete repository architecture inventory
- Route and React component inventory
- Supabase dependency map
- Existing table and data-flow inventory
- Authentication and authorization map
- External integration inventory
- Astro route and island boundary map
- Convex schema proposal
- Feature reuse, refactor, and replacement map
- Security and compliance risk register
- Final MVP acceptance criteria
- Delegation responsibility matrix
- Standard work-package template
- AI-agent permissions and prohibited actions
- Implementation-team role assignments
- Review, release, and escalation workflow
### Exit Gate
Proceed only when every MVP feature has a clear commercial outcome, owner, dependency, and acceptance test.
## Phase 1 — Astro Shell and Convex Relationship Foundation
**Timing:** Days 11–35
**Objective:** Produce a working application foundation using existing UI assets.
### Build
- Astro shell and public layouts
- React CRM island
- Convex project and environments
- Authentication and organization boundaries
- Contacts, households, companies, partners
- Properties and mortgages
- Notes, tasks, appointments, and activities
- Basic CSV import centre
- Audit and consent event foundation
### Acceptance Criteria
- Existing contacts can be imported safely
- A contact journey can be viewed and edited
- Notes, tasks, and appointments update in real time
- Mortgage and property records can be attached to a household
- Authenticated user and role access is enforced by Convex functions; full multi-tenant isolation is deferred
## Phase 2 — Opportunity Pipeline and Command Centre MVP
**Timing:** Days 36–60
**Objective:** Turn the CRM foundation into an opportunity-generation product.
### Build
- Opportunity schema and pipeline stages
- Story Before Score classification
- Opportunity scoring
- Evidence and trigger records
- Daily priority queue
- Renewal-date tracking
- Database reactivation lists
- Lead intake and attribution
- AI-generated contact and opportunity summaries
- Next-best-action recommendations with human approval
### Acceptance Criteria
- Dennis can open the system and immediately see the highest-priority actions
- Each opportunity explains why it exists
- Each score is traceable to evidence and assumptions
- Leads can move from capture to funded or nurture status
- Renewal and dormant-client opportunities are generated automatically
## Phase 3 — Communication and Workflow Automation
**Timing:** Days 61–90
**Objective:** Increase speed-to-lead and prevent opportunities from being lost.
### Build
- Complete a Telnyx-versus-Twilio technical validation covering SMS, MMS, calling, voice AI, number provisioning, webhook reliability, deliverability, Canadian number support, compliance controls, operating cost, and migration risk
- Implement a provider-neutral telecom adapter so Telnyx can become the preferred provider without tightly coupling Mortgage CoPilot to one vendor
- Use Twilio only as the fallback or transitional provider where Telnyx does not yet meet an MVP requirement
- Email and calendar connection through Unipile or approved provider
- Unified activity timeline
- New-lead confirmation and advisor notification
- Appointment reminders
- Document reminders
- Renewal workflow
- Database reactivation sequence
- Google review and referral request workflow
- Failed-event queue and retry handling
### Acceptance Criteria
- Communication is logged against the correct contact and opportunity
- Consent and suppression rules are enforced
- Failed sends and webhook events are visible and recoverable
- Human operators can pause or override automation
## Phase 4 — LeadSniperAI Self-Employed Engine
**Timing:** Days 91–120
**Objective:** Create a repeatable external prospecting pipeline for business owners.
### Build
- LeadSniperAI ingestion endpoint or import process
- Business, owner, signal, and evidence normalization
- Deduplication against existing CRM records
- Self-employed opportunity scoring
- Financing-hypothesis templates
- Business-owner review offer
- Advisor approval queue
- Outreach and outcome tracking
### Acceptance Criteria
- Every candidate includes source evidence, timing rationale, and likely financing need
- No prospect enters outreach without review and appropriate compliance controls
- Outcomes feed back into signal and segment scoring
## Phase 5 — Construction Opportunity Engine
**Timing:** Days 121–145
**Objective:** Detect and qualify project-based financing opportunities.
### Build
- Projects and project-parties data model
- Property and permit signal ingestion
- Construction pipeline
- Project-stage qualification
- Budget, land, equity, permit, experience, and exit-strategy fields
- Builder, developer, and professional relationship mapping
- Construction opportunity dashboard
### Acceptance Criteria
- A detected project connects to the relevant property and decision-makers
- Dennis can assess project readiness and financing hypothesis
- Construction opportunities can progress independently from consumer mortgages
## Phase 6 — SEO, AIO, Content Assets, and Conversion Optimization
**Timing:** Days 146–165
**Objective:** Scale inbound opportunities using the working product and observed borrower questions.
### Priority Content Clusters
- Self-employed mortgages
- Story Before Score
- B-lender and alternative financing
- Private-mortgage exit
- Construction and renovation financing
- Debt consolidation and equity restructuring
- Divorce and spousal buyout
- New-to-Canada mortgages
- Rental and investor qualification
- Renewal strategy
### Conversion Assets
- Business-owner mortgage review
- Story Before Score assessment
- Construction financing readiness assessment
- Private-to-prime exit planner
- Renewal review
- Debt consolidation and equity review
### Acceptance Criteria
- Every major page maps to a segment, problem, offer, and CRM workflow
- Attribution is retained through lead capture and conversion
- Content is reviewed for accuracy, disclosure, and human accountability
## Phase 7 — Production Hardening, Delegation Transfer, and Commercial Validation
**Timing:** Days 166–180
**Objective:** Validate business value and safely begin replacing GoHighLevel functions.
### Activities
- Data reconciliation
- Agent and implementation-team handoff validation
- SOP completion and ownership transfer
- Delegated release rehearsal
- Post-180-day operating backlog and capacity plan
- Permission and privacy testing
- Workflow failure testing
- Mobile usability review
- Performance and accessibility review
- Parallel-run comparison where necessary
- Operator SOPs
- Backup and incident procedures
- Commercial KPI baseline
- MVP retrospective and next-stage decision
### Final MVP Gate
The MVP is successful when it can demonstrate:
- Consistent opportunity creation from at least three engines
- A working daily priority queue
- Reliable lead capture and follow-up
- Renewal and database-reactivation workflows
- Self-employed opportunity ingestion
- Construction opportunity tracking
- Clear attribution from signal or page to opportunity and outcome
- Evidence of qualified conversations, applications, or funded-volume growth
---
# 7. Opportunity Scoring Framework
Use a shared explainable framework.
<table fit-page-width="true" header-row="true">
<tr>
<td>Dimension</td>
<td>Question</td>
</tr>
<tr>
<td>Fit</td>
<td>Does the person or project match a segment Dennis can serve?</td>
</tr>
<tr>
<td>Timing</td>
<td>Is there a current trigger or deadline?</td>
</tr>
<tr>
<td>Value</td>
<td>What is the estimated mortgage, financing amount, or revenue?</td>
</tr>
<tr>
<td>Evidence</td>
<td>How reliable and current is the supporting information?</td>
</tr>
<tr>
<td>Access</td>
<td>Can the decision-maker be reached directly or through a partner?</td>
</tr>
<tr>
<td>Relationship</td>
<td>Is there an existing relationship, referral, or trust advantage?</td>
</tr>
<tr>
<td>Readiness</td>
<td>Can the borrower or project reasonably proceed?</td>
</tr>
<tr>
<td>Strategic value</td>
<td>Could this create repeat business, referrals, or a valuable relationship?</td>
</tr>
</table>
Every recommendation must display the evidence, confidence, assumptions, and next action. AI never submits a mortgage or initiates sensitive activity without human review.
---
# 7. KPIs and Commercial Scorecard
## North-Star Metric
**Monthly expected mortgage revenue represented by active qualified opportunities.**
## Primary KPIs
- New qualified opportunities created
- Qualified conversations
- Discovery appointments booked
- Applications started
- Applications submitted
- Funded volume
- Gross commission revenue
- Renewal capture rate
- Database reactivation rate
- Self-employed opportunities created
- Construction opportunities created
- Referral opportunities created
- Lead response time
- Opportunity-to-application conversion
- Application-to-funded conversion
- Revenue by segment, signal, partner, and content asset
## Guardrail Metrics
- Consent and suppression violations
- Failed workflow rate
- Duplicate-contact rate
- Unreviewed AI recommendation rate
- Stale opportunity rate
- Average time without next action
- Data completeness
---
# 8. Claude Code and Superpowers Execution Method
Use Claude Code as the implementation team and Superpowers as the engineering control system.
## Required Workflow
```plain text
Discovery
→ written specification
→ architecture and data-model review
→ phased implementation plan
→ small vertical slice
→ automated tests
→ code review
→ business acceptance
→ merge
```
## First Vertical Slice
```plain text
Contact
→ contact detail
→ property and mortgage
→ notes and tasks
→ opportunity
→ daily action queue
```
Do not start with a full-system rewrite.
## Engineering Rules
- Preserve functioning React components
- Use Astro for public pages and shell
- Use React for the interactive CRM
- Replace Supabase one bounded module at a time
- Keep the application runnable after every phase
- Test authorization in every Convex query and mutation
- Design all external event handlers to be idempotent
- Record audit, consent, and integration events
- Keep AI recommendations explainable and human-approved
---
# 9. Immediate Execution Backlog
## Sprint 0
- [ ] Run complete repository discovery
- [ ] Lock MVP scope and exclusions
- [ ] Approve Astro, React, Convex, Telnyx, Unipile, and LeadSniperAI boundaries
- [ ] Define production, staging, and local environments
- [ ] Map existing Supabase tables and functions
- [ ] Approve Convex schema v1
## Sprint 1
- [ ] Create Astro application shell
- [ ] Mount the existing React CRM workspace
- [ ] Configure Convex and authentication
- [ ] Migrate contacts, companies, notes, tasks, and activities
- [ ] Build import preview, validation, and deduplication
## Sprint 2
- [ ] Add households, properties, mortgages, and renewals
- [ ] Build opportunity pipeline
- [ ] Add Story Before Score segmentation
- [ ] Build Command Centre priority queue
- [ ] Add AI summary and next-action draft
## Sprint 3
- [ ] Connect communications
- [ ] Add workflow scheduling and retries
- [ ] Build database reactivation
- [ ] Build renewal sequence
- [ ] Add referral and review workflow
## Sprint 4
- [ ] Ingest LeadSniperAI signals
- [ ] Build self-employed opportunity queue
- [ ] Create construction project and party model
- [ ] Add construction qualification pipeline
## Sprint 5
- [ ] Publish priority SEO and AIO clusters
- [ ] Launch conversion assessments
- [ ] Measure opportunity quality by source
- [ ] Complete production hardening and commercial validation
---
<callout icon="📌" color="yellow_bg">
	The original SEO, AIO, CRM, data-model, workflow, and content plan remains below as supporting detail. Where it conflicts with this executive refactor, the opportunity-generation objective and phased MVP gates above control implementation priority.
</callout>
---
# Executive Summary
This implementation plan defines how to build [**mortgagesbydenniseng.ca**](http://mortgagesbydenniseng.ca) as a compliance-controlled, organic lead-generation digital asset using **Astro** for the public web experience and **Convex** as the real-time CRM, workflow, lead-intelligence, and follow-up backend.
The system will combine:
- Strong technical and topical SEO
- AI-search and answer-engine optimization
- Story Over Score messaging
- Conversion-focused mortgage calculators and assessments
- Subdomain-based lead-generation assets under `*.mortgagesbydenniseng.ca`
- A custom Convex CRM capable of the core marketing and follow-up functions commonly associated with GoHighLevel
- Twilio for SMS and phone workflows
- Resend for transactional and nurture email
- Unipile for WhatsApp, LinkedIn, and unified messaging connections
- Real-time lead scoring, routing, pipeline management, attribution, tasking, and reporting
The initial 120-day objective is to establish the technical foundation, publish a focused content cluster around **B lending, alternative mortgages, self-employed financing, construction financing, rental income qualification, and mortgage problem-solving**, and build a repeatable lead-capture and follow-up system.
The strategic principle is:
> **Do not build a generic mortgage website. Build a portfolio of useful decision assets that answer difficult borrower questions, tell credible borrower stories, and convert search intent into structured mortgage opportunities.**
---
# 1. Product Vision
## Vision Statement
Build [mortgagesbydenniseng.ca](http://mortgagesbydenniseng.ca) into a trusted mortgage problem-solving platform for borrowers who do not fit conventional lender boxes, while operating every public lead-generation asset, calculator, assessment, and follow-up workflow through one compliant backend.
## Primary Business Outcome
Turn organic search and AI-answer visibility into:
1. Qualified mortgage conversations
2. Completed assessments
3. Document-ready mortgage opportunities
4. Referral opportunities
5. Repeatable rank-and-rent or sponsored subdomain assets
6. A growing proprietary database of borrower intent, questions, conversion patterns, and lender-fit insights
## 120-Day Outcome
By day 120, the platform should have:
- A production Astro website
- A Convex-powered lead CRM
- Compliance-controlled subdomain architecture
- Analytics and attribution
- At least three working lead magnets or calculators
- Automated SMS, email, and unified-message follow-up
- A functioning mortgage opportunity pipeline
- A published topical authority cluster
- Structured data and answer-engine-ready content
- A documented editorial and review process
- Initial performance baselines for rankings, impressions, conversion rate, lead quality, and booked calls
---
# 2. Strategic Positioning
## Core Position
Mortgages by Dennis Eng should be positioned as a **mortgage problem-solving and strategy platform**, not merely a rate-comparison site.
The strongest initial market position is:
- Borrowers declined by banks
- Self-employed borrowers
- Borrowers with complex income
- B-lender and alternative mortgage scenarios
- Construction and renovation financing
- Rental-property qualification
- Debt consolidation and credit-recovery scenarios
- Commercial and business-owner mortgage needs
## Differentiation
The site should compete through:
- Clear explanations of lender decision logic
- Practical calculators and assessments
- Scenario-based examples
- Transparent trade-offs
- Strong local and Canadian context
- Fast response and structured follow-up
- Human review supported by AI
- Story Over Score messaging
## Story Over Score Framework
The Story Over Score framework means the site should not reduce a borrower to a credit score, debt-service ratio, or lender category.
Every high-value page should explain:
1. **The borrower’s situation** — what changed or created the financing need
2. **The obstacle** — why the conventional approach may not work
3. **The evidence** — income, property, equity, cash flow, experience, exit plan, or documentation
4. **The strategy** — how the mortgage request can be structured
5. **The trade-off** — rate, fees, term, lender type, documentation, or timeline
6. **The path forward** — what the borrower should prepare or do next
Suggested editorial pattern:
```plain text
Situation → Constraint → Strengths → Strategy → Trade-offs → Next Step
```
This framework should be applied to service pages, calculators, case studies, FAQs, email sequences, and AI-generated summaries.
---
# 3. Domain and Subdomain Architecture
## Primary Domain
`mortgagesbydenniseng.ca` is the controlled public brand and should contain the principal authority-building content.
Recommended primary-domain structure:
```plain text
mortgagesbydenniseng.ca/
mortgagesbydenniseng.ca/b-lender-mortgages/
mortgagesbydenniseng.ca/self-employed-mortgages/
mortgagesbydenniseng.ca/construction-financing/
mortgagesbydenniseng.ca/rental-income-mortgages/
mortgagesbydenniseng.ca/debt-consolidation/
mortgagesbydenniseng.ca/calculators/
mortgagesbydenniseng.ca/guides/
mortgagesbydenniseng.ca/case-studies/
mortgagesbydenniseng.ca/about/
mortgagesbydenniseng.ca/contact/
mortgagesbydenniseng.ca/privacy/
mortgagesbydenniseng.ca/disclosures/
```
## Compliance-Controlled Subdomains
All specialized lead-generation assets should remain under the primary domain:
```plain text
apply.mortgagesbydenniseng.ca
assessment.mortgagesbydenniseng.ca
calculator.mortgagesbydenniseng.ca
construction.mortgagesbydenniseng.ca
selfemployed.mortgagesbydenniseng.ca
blending.mortgagesbydenniseng.ca
partners.mortgagesbydenniseng.ca
```
Each subdomain must:
- Identify Mortgages by Dennis Eng
- Display brokerage and licensing disclosures as required
- Link to the canonical privacy policy and terms
- Record the consent language version
- Submit to the same Convex backend
- Use the approved brand and disclosure components
- Preserve source subdomain and page attribution
## Recommended SEO Use
Use the primary domain for topical authority and long-form search content. Use subdomains primarily for:
- Application flows
- Assessments
- Calculators
- Campaign-specific experiences
- Partner or referral portals
- Distinct conversion funnels
Where a subdomain page targets an important organic keyword, publish a corresponding authority page on the main domain and link it to the subdomain conversion experience.
---
# 4. Technical Architecture
## High-Level Stack
```plain text
Astro public site and landing pages
        |
        |-- Static and hybrid SEO pages
        |-- React islands for calculators and forms
        |-- Structured data
        |-- Hostname-aware subdomain rendering
        v
Convex operational backend
        |
        |-- CRM and contacts
        |-- Lead capture and consent
        |-- Pipelines and opportunities
        |-- Tasks and appointments
        |-- Messaging and campaigns
        |-- Workflow orchestration
        |-- Lead scoring and routing
        |-- Page and offer configuration
        |-- Real-time dashboards
        v
Communications and services
        |-- Twilio: SMS, phone verification, voice workflows
        |-- Resend: transactional and nurture email
        |-- Unipile: WhatsApp, LinkedIn, unified messaging
        |-- Clerk: operator and partner authentication
        |-- Stripe: future payments, subscriptions, lead products
        |-- DataForSEO: SEO and SERP intelligence
        |-- Analytics warehouse: optional historical reporting
```
## Why Astro
Astro is selected for:
- Fast static output
- Excellent Core Web Vitals potential
- Strong control over metadata and structured data
- Flexible content collections
- React islands for interactive calculators
- Multi-page and multi-domain deployment
- Low JavaScript overhead
- Strong suitability for SEO-first content sites
## Why Convex
Convex is selected because the application requires:
- Real-time CRM updates
- Type-safe TypeScript server functions
- Durable follow-up workflows
- Scheduled messages and tasks
- Transactional pipeline changes
- Multi-tenant and role-based access
- External API actions
- Agent and AI state persistence
- Auditable consent and communication records
- Live dashboards without manual polling
---
# 5. Astro Implementation Plan
## Application Structure
```plain text
src/
  components/
    seo/
    compliance/
    forms/
    calculators/
    story-over-score/
    calls-to-action/
    navigation/
  content/
    services/
    guides/
    case-studies/
    locations/
    faqs/
  layouts/
    BaseLayout.astro
    ServiceLayout.astro
    GuideLayout.astro
    CaseStudyLayout.astro
    LandingPageLayout.astro
  pages/
    index.astro
    b-lender-mortgages/
    self-employed-mortgages/
    construction-financing/
    rental-income-mortgages/
    calculators/
    api/
  lib/
    convex.ts
    seo.ts
    schema.ts
    attribution.ts
    consent.ts
```
## Reusable Page Blocks
Create configurable components for:
- Hero and primary promise
- Borrower situation selector
- Story Over Score narrative
- Eligibility summary
- Scenario cards
- Lender option comparisons
- Process timeline
- Calculator
- FAQ
- Case study
- Proof and credentials
- Disclosure footer
- Progressive lead form
- Call-booking CTA
## Hostname-Aware Rendering
The same frontend may support multiple subdomains. The request hostname should resolve a Convex `webAsset` configuration containing:
- Brand and headline
- Vertical
- Geography
- Offer
- Form configuration
- Calculator configuration
- Disclosure version
- Consent version
- Routing policy
- Tracking configuration
## Content Source
Start with Astro content collections or MDX stored in Git for speed, quality control, and version history.
Convex should initially store:
- Page metadata
- Offer associations
- publication status
- review status
- conversion configuration
- content performance references
A full CMS can be added later, but it should not delay launch.
---
# 6. Convex CRM Scope
The custom CRM should reproduce the most important GoHighLevel-style functions needed for this business without attempting to copy every feature.
## Core CRM Modules
### Contacts
- Name
- Email
- Phone
- Preferred channel
- Address and geography
- Borrower type
- Consent status
- Source and attribution
- Duplicate detection
### Leads and Opportunities
- Mortgage purpose
- Requested amount
- Property details
- Income type
- Credit range
- Timing
- Documentation readiness
- Lead quality
- Assigned advisor
- Pipeline stage
- Estimated revenue
### Pipeline
Recommended stages:
```plain text
New Inquiry
Attempting Contact
Connected
Discovery Scheduled
Discovery Completed
Documents Requested
Documents Received
Strategy Review
Application Prepared
Submitted to Lender
Conditional Approval
Approved
Funded
Nurture
Not Proceeding
```
### Conversations
Unified activity timeline containing:
- Email
- SMS
- WhatsApp
- LinkedIn messages where appropriate
- Call records
- Notes
- Tasks
- Form submissions
- Calculator results
- Consent events
- Appointment events
### Tasks
- Call lead
- Send document checklist
- Review assessment
- Follow up after lender response
- Confirm appointment
- Request missing information
- Review renewal opportunity
### Appointments
- Discovery calls
- Document reviews
- Strategy reviews
- Partner meetings
- Renewal reviews
### Campaigns and Sequences
- New inquiry follow-up
- Missed-call text back
- Application abandonment
- Document reminder
- Self-employed education sequence
- B-lender education sequence
- Construction financing sequence
- Renewal sequence
- Referral partner sequence
### Templates
- SMS templates
- Email templates
- WhatsApp templates
- Call scripts
- Document checklists
- Story Over Score summaries
### Reporting
- Traffic by source
- Conversion by page
- Lead-to-contact rate
- Contact-to-appointment rate
- Appointment-to-application rate
- Application-to-funded rate
- Response time
- Revenue by asset
- Lead quality by keyword cluster
- Message performance
---
# 7. Recommended Convex Data Model
## `webAssets`
- hostname
- primaryDomain
- assetName
- vertical
- geography
- offerId
- formConfigId
- calculatorConfigId
- disclosureVersion
- consentVersion
- routingPolicyId
- status
## `pages`
- webAssetId
- path
- pageType
- primaryKeyword
- searchIntent
- topicCluster
- canonicalUrl
- title
- description
- schemaTypes
- publicationStatus
- lastReviewedAt
## `contacts`
- name
- email
- phone
- preferredChannel
- location
- consentStatus
- firstTouch
- lastTouch
- createdAt
## `leads`
- contactId
- webAssetId
- sourcePageId
- mortgagePurpose
- requestedAmount
- propertyType
- location
- incomeType
- creditRange
- timeline
- score
- storySummary
- assignedUserId
- pipelineStage
- status
## `consents`
- contactId
- leadId
- consentVersion
- channelsAllowed
- sharingScope
- sourceUrl
- hostname
- timestamp
- evidenceReference
- withdrawalStatus
## `pipelineEvents`
- leadId
- fromStage
- toStage
- actorId
- reason
- timestamp
## `conversations`
- contactId
- leadId
- channel
- provider
- externalThreadId
- status
## `messages`
- conversationId
- direction
- provider
- templateId
- contentReference
- deliveryStatus
- sentAt
- deliveredAt
- repliedAt
## `tasks`
- leadId
- assignedUserId
- taskType
- title
- dueAt
- status
- completedAt
## `appointments`
- leadId
- contactId
- appointmentType
- startAt
- endAt
- status
- reminderState
## `workflows`
- workflowType
- entityId
- currentStep
- status
- nextRunAt
- retryCount
- errorSummary
## `attributionEvents`
- anonymousVisitorId
- contactId
- webAssetId
- pageId
- eventType
- source
- medium
- campaign
- keyword
- referrer
- timestamp
## `contentPerformance`
- pageId
- date
- impressions
- clicks
- averagePosition
- conversions
- assistedConversions
- AIReferralVisits
## `auditEvents`
- actorId
- resourceType
- resourceId
- action
- metadata
- timestamp
---
# 8. Lead Capture and Follow-Up Workflows
## Workflow 1 — New Organic Lead
```plain text
Visitor submits assessment
Validate fields
Create or merge contact
Create consent record
Create lead
Record attribution
Send confirmation email through Resend
Send SMS confirmation through Twilio where permitted
Create advisor task
Start response-time timer
Notify operator
Wait for reply or advisor action
Escalate if no contact attempt
```
## Workflow 2 — Progressive Assessment Abandonment
```plain text
Visitor starts assessment
Stores anonymous progress
Visitor provides contact information
Assessment remains incomplete
Wait 30 minutes
Send helpful reminder
Wait 24 hours
Send value-based education message
Wait 72 hours
Create nurture task or stop based on engagement
```
## Workflow 3 — Missed Call Text Back
```plain text
Inbound call not answered
Receive Twilio event
Match or create contact
Send approved text-back message
Create lead or task
Notify advisor
Log consent and channel status
```
## Workflow 4 — Document Readiness
```plain text
Discovery completed
Determine document checklist
Send personalized checklist
Track uploads or confirmations
Send reminders at approved intervals
Notify advisor when complete
Advance pipeline stage
```
## Workflow 5 — B-Lender Education Sequence
Message themes:
1. Why a bank decline is not necessarily the end
2. How equity, income story, and exit plan affect lender fit
3. Rate versus overall financing outcome
4. Documents that make the application stronger
5. When a short-term alternative mortgage can be strategic
6. Invitation to review the borrower’s complete story
## Workflow 6 — Construction Financing Follow-Up
- Confirm project stage
- Confirm land ownership and value
- Request budget and plans
- Confirm permits and experience
- Clarify exit strategy
- Schedule strategy review
- Route to construction-financing pipeline
## Workflow 7 — Renewal and Long-Term Nurture
- Record maturity date
- Trigger review 180, 120, 90, 60, and 30 days before maturity
- Update borrower situation
- Reassess lender fit
- Present renewal, refinance, or consolidation options
---
# 9. Communication Layer
## Twilio
Use Twilio for:
- SMS confirmations
- Two-way SMS
- Missed-call text back
- Phone verification
- Appointment reminders
- Time-sensitive document reminders
- Optional voice workflows
Controls:
- Store channel consent
- Honour stop requests
- Use approved templates
- Apply quiet-hour rules
- Record provider message IDs
- Track delivery and failure events
## Resend
Use Resend for:
- Form confirmations
- Assessment summaries
- Document checklists
- Educational nurture
- Appointment confirmations
- Advisor notifications
- Lead and workflow alerts
Controls:
- Domain authentication
- Transactional versus marketing classification
- Bounce and complaint handling
- Idempotency
- Template versioning
- Unsubscribe management where required
## Unipile
Use Unipile for:
- WhatsApp conversations where consent and channel rules permit
- LinkedIn relationship workflows for referral partners
- Unified inbox connections
- Cross-channel thread references
Avoid automating aggressive or non-compliant cold outreach. Unipile should support relationship management and approved outreach rather than uncontrolled bulk messaging.
---
# 10. SEO Strategy
## Primary SEO Goal
Build topical authority around complex and alternative mortgage situations in British Columbia and Canada, beginning with commercially valuable, high-intent clusters.
## Initial Topic Clusters
### Cluster A — B Lender and Alternative Mortgages
- What is a B lender?
- B lender mortgage requirements
- B lender rates and fees
- Bank decline alternatives
- Alternative mortgages in BC
- B lender versus private lender
- Exit strategies from a B mortgage
### Cluster B — Self-Employed Mortgages
- Self-employed mortgage qualification
- Stated-income alternatives
- Add-backs and gross-ups
- Low taxable income mortgage strategies
- Corporation income and dividends
- Business-for-self documentation
- Rental income combined with self-employed income
### Cluster C — Construction and Renovation Financing
- Construction mortgage process
- Progress draws
- Land equity
- Builder experience
- Permit and appraisal requirements
- Major renovation financing
- Construction budget and contingency
### Cluster D — Rental Income Qualification
- Rental offset
- Rental add-back
- Rental surplus and deficit
- Subject property versus rental property treatment
- TDS and GDS with rental income
- Multiple-property qualification
### Cluster E — Credit, Debt, and Mortgage Recovery
- Debt consolidation mortgage
- Credit rebuilding with mortgage strategy
- Consumer proposal mortgage timing
- Mortgage arrears options
- Property tax or strata arrears
- Short-term bridge strategy
## Technical SEO Requirements
- Fast static HTML
- Clean semantic markup
- Canonical tags
- XML sitemap
- Robots rules
- Breadcrumbs
- Structured data
- Image optimization
- Internal-link graph
- Pagination controls
- Redirect management
- Broken-link monitoring
- Core Web Vitals monitoring
- Indexation monitoring
- Unique titles and descriptions
- Clear author and reviewer information
## Structured Data
Use appropriate schema types such as:
- Organization
- Person
- FinancialService
- LocalBusiness where appropriate
- Service
- Article
- FAQPage when the content qualifies
- BreadcrumbList
- WebSite
- WebPage
- HowTo only where the page genuinely meets the standard
---
# 11. AIO and Answer-Engine Optimization
AIO should make the content easy for AI systems to retrieve, understand, quote, and connect to the correct entity.
## AIO Content Rules
Every major page should include:
- A clear one-paragraph direct answer near the beginning
- Concise definitions
- Explicit Canadian and provincial context
- Tables for comparisons
- Numbered processes
- Decision criteria
- Common exceptions
- Examples and scenarios
- FAQ sections
- Updated and reviewed dates
- Author identity and qualifications
- Source references for factual claims
- Clear distinction between general information and individual advice
## Entity Signals
Consistently connect:
- Dennis Eng
- Mortgages by Dennis Eng
- Brokerage affiliation
- Service areas
- Mortgage specialties
- Contact points
- Relevant professional profiles
## AI-Readable Page Pattern
```plain text
Question or decision
Direct answer
Who this applies to
Key qualification factors
Options and trade-offs
Example scenario
Required documents
Common mistakes
Next step
FAQ
Author and review details
```
## Original Information Assets
Create proprietary assets that AI systems may cite or summarize:
- Rental offset and add-back calculator
- B-lender readiness assessment
- Self-employed income documentation checklist
- Construction financing readiness score
- Mortgage scenario comparison tables
- Story Over Score case studies
- Quarterly alternative mortgage market observations
---
# 12. Conversion Strategy
## Lead Magnets
Initial lead magnets should include:
1. **B-Lender Readiness Assessment**
2. **Self-Employed Mortgage Documentation Checklist**
3. **Rental Offset, Add-Back, Deficit and Surplus Calculator**
4. **Construction Financing Readiness Assessment**
5. **Bank Decline Next-Step Guide**
## Progressive Form Design
Step 1: Financing goal
Step 2: Property and location
Step 3: Income type and basic qualification
Step 4: Timing and urgency
Step 5: Contact details
Step 6: Consent and preferred channel
Step 7: Optional document or call booking
## Call-to-Action Types
- Check my options
- Review my mortgage story
- Estimate my rental-income treatment
- Prepare for a B-lender application
- Assess my construction financing readiness
- Book a mortgage strategy review
Avoid generic calls to action such as “Submit” when a more outcome-focused phrase is available.
---
# 13. 120-Day Content Plan
## Publishing Cadence
Target:
- Two substantial authority pages or articles per week
- One supporting FAQ, comparison, case study, or glossary asset per week
- One original calculator, checklist, assessment, or data asset per month
- Weekly content refresh and internal-link review
- Monthly performance review
This yields approximately 36 to 44 meaningful assets during the first 120 days without sacrificing quality.
## Phase 1 — Days 1–30: Foundation and Core Intent
### Week 1
**Authority page:** B-Lender Mortgages in British Columbia: Requirements, Costs, and When They Make Sense
**Supporting page:** What Is a B Lender in Canada?
**FAQ asset:** B Lender versus Bank versus Private Lender
**Conversion asset:** B-Lender Readiness Assessment specification
**Implementation focus:** Analytics, Search Console, sitemap, schema foundation, author page, disclosures, Convex intake endpoint
### Week 2
**Authority page:** Self-Employed Mortgages in BC: How Lenders Review Income
**Supporting page:** Mortgage Add-Backs and Gross-Ups for Business Owners
**Story asset:** A borrower with strong cash flow but low taxable income
**Conversion asset:** Self-employed document checklist
**Implementation focus:** Progressive forms, consent logging, Resend confirmation workflow
### Week 3
**Authority page:** Rental Income Mortgage Qualification: Offset, Add-Back, Surplus, and Deficit
**Supporting page:** How Rental Income Changes GDS and TDS
**FAQ asset:** Can projected rent be used to qualify?
**Conversion asset:** Rental-income calculator version 1
**Implementation focus:** Calculator event tracking, lead attribution, CRM contact creation
### Week 4
**Authority page:** What to Do After a Bank Declines Your Mortgage
**Supporting page:** B Lender versus Private Mortgage: Key Differences
**Story asset:** Bank decline caused by income documentation rather than affordability
**Conversion asset:** Bank-decline next-step guide
**Implementation focus:** Twilio SMS confirmation and operator task workflow
## Phase 2 — Days 31–60: Construction, Credit, and Decision Content
### Week 5
**Authority page:** Construction Financing in British Columbia: A Step-by-Step Guide
**Supporting page:** How Construction Mortgage Progress Draws Work
**FAQ asset:** Do you need permits before arranging construction financing?
**Conversion asset:** Construction readiness assessment
**Implementation focus:** Construction lead pipeline and conditional fields
### Week 6
**Authority page:** Major Renovation Financing Options in BC
**Supporting page:** Construction Budget, Contingency, and Cost Overrun Planning
**Story asset:** Using land equity to support a construction project
**Comparison asset:** Purchase-plus-improvements versus construction financing
**Implementation focus:** Document checklist automation and workflow reminders
### Week 7
**Authority page:** Debt Consolidation Through a Mortgage Refinance
**Supporting page:** When Mortgage Refinancing May Lower Monthly Obligations
**FAQ asset:** Can unsecured debt be consolidated into a mortgage?
**Story asset:** Strong home equity but short-term credit pressure
**Implementation focus:** Pipeline value, estimated savings fields, advisor review task
### Week 8
**Authority page:** Mortgage Options After a Consumer Proposal
**Supporting page:** How Credit Recovery Affects Mortgage Timing
**FAQ asset:** How long after a consumer proposal can someone qualify?
**Conversion asset:** Mortgage recovery planning checklist
**Implementation focus:** Nurture sequences and future eligibility dates
## Phase 3 — Days 61–90: Deep Topical Authority and Local Relevance
### Week 9
**Authority page:** Mortgage Qualification for Incorporated Business Owners
**Supporting page:** Salary versus Dividends in a Mortgage Application
**Story asset:** Business retained earnings and personal borrowing capacity
**FAQ asset:** Can corporate financial statements support mortgage qualification?
**Implementation focus:** Business-owner lead scoring and story-summary generation
### Week 10
**Authority page:** Alternative Mortgage Options for Commission and Variable Income
**Supporting page:** How Two-Year Income Averaging Works
**FAQ asset:** What happens when the most recent year is lower?
**Story asset:** Recovering income after a temporary business interruption
**Implementation focus:** Income-type branching logic and document requests
### Week 11
**Authority page:** Multiple Rental Properties and Mortgage Qualification
**Supporting page:** Rental Portfolio Cash Flow versus Personal Debt-Service Ratios
**Comparison asset:** Lender rental-calculation methods
**Conversion asset:** Rental portfolio assessment
**Implementation focus:** Multi-property data model and calculator expansion
### Week 12
**Authority page:** Alternative and B-Lender Mortgage Options in Vancouver and the Lower Mainland
**Supporting local page:** Burnaby alternative mortgage scenarios
**Supporting local page:** Surrey and Fraser Valley self-employed mortgage scenarios
**Story asset:** Local property equity supporting a short-term financing strategy
**Implementation focus:** Location schema, local internal links, geography reporting
## Phase 4 — Days 91–120: Commercial Intent, Proof, and Optimization
### Week 13
**Authority page:** How to Exit a B-Lender Mortgage and Return to an A Lender
**Supporting page:** One-Year versus Two-Year Alternative Mortgage Terms
**FAQ asset:** What makes an exit strategy credible?
**Story asset:** Using a short-term mortgage to bridge an income-documentation issue
**Implementation focus:** Maturity tracking and renewal workflows
### Week 14
**Authority page:** Mortgage Fees, Lender Fees, and Broker Fees Explained
**Supporting page:** How to Compare Total Mortgage Cost Instead of Rate Alone
**Comparison asset:** Rate, fee, term, penalty, and exit-plan comparison table
**Conversion asset:** Mortgage option comparison worksheet
**Implementation focus:** Transparent calculation components and disclosure review
### Week 15
**Authority page:** Private Mortgage Financing in BC: Uses, Risks, and Exit Planning
**Supporting page:** First, Second, and Third Mortgages Explained
**FAQ asset:** When is a private mortgage appropriate?
**Story asset:** Time-sensitive financing supported by property equity
**Implementation focus:** High-risk lead review, manual QA, escalation rules
### Week 16
**Authority page:** The Story Over Score Mortgage Framework
**Supporting page:** How to Prepare a Strong Mortgage Explanation Letter
**Case-study hub:** Publish three anonymized scenario summaries
**Performance asset:** First 120-day mortgage search and borrower-question report
**Implementation focus:** Content pruning, internal-link optimization, conversion review, workflow tuning, and next-quarter roadmap
## Weekly Supporting Distribution
For every authority page:
- Publish one concise LinkedIn post for referral partners
- Create one Google Business Profile update where appropriate
- Produce three to five short FAQ answers
- Add internal links from at least three existing pages
- Add one email or nurture lesson
- Create one reusable answer for the advisor knowledge base
---
# 14. Content Quality and Review Workflow
## Content Statuses
```plain text
Idea
SERP Evidence Required
Brief Approved
Drafting
Technical Review
Mortgage/Compliance Review
SEO/AIO Review
Ready to Publish
Published
Refresh Due
Archived
```
## Required Content Brief Fields
- Primary query
- Search intent
- Audience
- Borrower situation
- Unique angle
- Story Over Score narrative
- Required facts and sources
- Page structure
- Conversion offer
- Internal links
- Schema types
- Compliance notes
- Review date
## Quality Gate
A page should not publish unless it has:
- A clear search intent
- Original value
- Accurate mortgage context
- A direct answer
- A useful example or framework
- Appropriate disclosures
- Internal links
- Metadata
- Structured data where applicable
- A conversion action
- An assigned review date
---
# 15. 120-Day Technical Delivery Plan
## Sprint 1 — Days 1–15
- Initialize Astro project
- Configure domain and deployment
- Establish design tokens and reusable layouts
- Create compliance components
- Connect Convex
- Define core schema
- Implement lead intake mutation
- Implement consent records
- Install analytics and attribution
- Publish home, about, contact, privacy, and disclosure pages
## Sprint 2 — Days 16–30
- Build service-page templates
- Build guide and case-study collections
- Create progressive lead form
- Implement contact merge and duplicate logic
- Configure Resend transactional email
- Create operator lead queue
- Publish first topic cluster
- Launch B-Lender Readiness Assessment MVP
## Sprint 3 — Days 31–45
- Add Twilio SMS integration
- Create new-lead workflow
- Create missed-call text-back workflow
- Add pipeline stages and tasks
- Build calculator framework
- Publish construction content cluster
- Launch construction assessment MVP
## Sprint 4 — Days 46–60
- Build rental offset/add-back calculator
- Add appointment and reminder model
- Add unified conversation timeline
- Implement message templates
- Build nurturing and abandonment workflows
- Publish debt and mortgage-recovery cluster
## Sprint 5 — Days 61–75
- Integrate Unipile for approved channels
- Add partner and referral contact workflows
- Add Story Over Score AI summary
- Build content-performance records
- Add location-aware pages and schema
- Publish self-employed deep-dive cluster
## Sprint 6 — Days 76–90
- Add multi-property assessment
- Build KPI dashboard
- Add response SLA alerts
- Add renewal and maturity tracking
- Improve internal-link automation
- Publish rental portfolio and local content
## Sprint 7 — Days 91–105
- Add workflow failure and retry dashboard
- Add communication preference centre
- Add audit-event viewer
- Improve lead scoring
- Implement content refresh queue
- Publish exit-strategy and fee-comparison cluster
## Sprint 8 — Days 106–120
- Complete security and compliance review
- Review Core Web Vitals
- Review indexing and structured data
- Tune messaging sequences
- Evaluate conversion paths
- Publish Story Over Score hub and case studies
- Produce 120-day performance report
- Create next 180-day roadmap
---
# 16. KPIs and Success Criteria
## Organic Visibility
- Indexed pages
- Search impressions
- Non-branded clicks
- Top-20 keyword count
- Top-10 keyword count
- Featured snippet or answer visibility
- AI referral sessions
- Branded search growth
## Engagement
- Engaged sessions
- Scroll depth
- Calculator starts
- Calculator completions
- Assessment starts
- Assessment completions
- Return visits
## Lead Generation
- Visitor-to-lead conversion rate
- Lead-to-contact rate
- Lead-to-appointment rate
- Appointment-to-application rate
- Application-to-funded rate
- Cost per lead, including content production and tools
- Revenue per page
- Revenue per topic cluster
## Operational
- Median first-response time
- Percentage contacted within five minutes
- Workflow completion rate
- Message delivery rate
- SMS reply rate
- Email reply rate
- Appointment show rate
- Document completion time
## Content Quality
- Pages reviewed on schedule
- Pages with original examples
- Pages with structured data
- Internal-link coverage
- Content decay alerts resolved
- Conversion actions per page
## Initial 120-Day Targets
Use the first 30 days to establish baselines. Directional targets for days 31–120:
- All priority pages indexed
- At least 36 high-quality published assets
- Three working lead magnets or calculators
- More than 98% transactional email delivery where provider data permits
- Median first-response time below five minutes during operating windows
- At least 70% completion rate for short assessments
- Every lead linked to source page, consent version, and campaign attribution
- Every communication represented in the CRM timeline
---
# 17. Security, Privacy, and Compliance Requirements
- Do not expose contact details in public client queries
- Separate sensitive lead contact data from public summaries
- Enforce server-side authorization
- Version all consent language
- Record channel permissions
- Store audit events for access and status changes
- Implement data-retention policies
- Support correction and deletion workflows
- Encrypt sensitive data through supported platform controls
- Use minimal necessary data collection
- Include appropriate brokerage, licensing, privacy, and information-only disclosures
- Route higher-risk or unusual scenarios to human review
- Avoid automated promises of approval, rate, or funding
- Distinguish educational calculations from lender commitments
Legal and regulatory wording should be reviewed by the applicable brokerage or qualified compliance professional before launch.
---
# 18. Dependencies and Risks
## Dependencies
- Domain and DNS access
- Astro hosting decision
- Convex project
- Clerk organization setup for operator access
- Twilio account and approved numbers
- Resend domain authentication
- Unipile account connections
- Analytics and Search Console access
- Approved brokerage and licensing disclosures
- Brand assets
## Key Risks
### Thin or repetitive SEO pages
Mitigation: require original examples, unique intent, useful tools, and editorial review.
### Overbuilding the CRM before validating traffic
Mitigation: implement only the workflows required by the first three offers.
### Messaging compliance failures
Mitigation: channel-specific consent, template controls, stop handling, quiet hours, and audit records.
### Poor lead response time
Mitigation: real-time alerts, Twilio confirmation, operator tasks, SLA escalation.
### AI-generated inaccuracies
Mitigation: human review, source references, versioned prompts, and clear information-only framing.
### Fragmented authority across subdomains
Mitigation: keep core authority content on the primary domain and use subdomains chiefly for conversion experiences.
---
# 19. Working Assumptions and Open Decisions
## Working Assumptions
- The initial geography is British Columbia, with emphasis on Vancouver, Burnaby, Surrey, Fraser Valley, and nearby markets.
- The initial commercial focus is alternative/B lending, self-employed borrowers, rental income, and construction financing.
- Astro content begins Git-managed rather than requiring a full CMS.
- Convex becomes the operational CRM and workflow backend.
- Clerk is used for authenticated operator and partner access.
- Twilio, Resend, and Unipile are the selected communication providers.
- Subdomain assets must remain within `*.mortgagesbydenniseng.ca` for brand and compliance control.
## Decisions to Finalize During Sprint 1
- Exact brokerage and licence disclosure language
- Hosting provider
- Calendar/appointment provider or custom implementation
- Document-storage provider
- Initial three offers to launch
- Contact hours and escalation rules
- Data-retention schedule
- Which Unipile channels are approved for the first release
---
# 20. Definition of Done for Day 120
The first implementation phase is complete when:
- The Astro site is live on [mortgagesbydenniseng.ca](http://mortgagesbydenniseng.ca)
- Priority subdomain conversion flows resolve correctly
- Convex stores contacts, leads, consent, attribution, pipeline stages, tasks, appointments, messages, and workflow state
- Resend confirmations and nurture emails are functioning
- Twilio SMS confirmations and reminders are functioning
- Approved Unipile channels appear in the conversation timeline
- At least three lead magnets or calculators are live
- The 120-day content plan has been substantially published
- SEO metadata, schema, sitemap, canonical rules, and internal links are implemented
- Every lead has traceable source and consent evidence
- Operators can manage leads in a real-time pipeline
- Automated follow-up stops or adapts when a human reply is received
- Performance can be reviewed by page, topic, asset, channel, pipeline stage, and outcome
---
# Recommended Immediate Build Order
1. Astro foundation and compliance components
2. Convex contact, consent, lead, attribution, and pipeline schema
3. Progressive assessment form
4. Resend confirmation
5. Operator lead queue
6. Twilio SMS confirmation and missed-call workflow
7. B-lender authority cluster
8. Rental-income calculator
9. Construction readiness assessment
10. Unified conversation timeline
11. Nurture and document workflows
12. AIO refinements and Story Over Score case-study system
