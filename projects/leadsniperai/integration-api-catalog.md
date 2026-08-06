---
title: Application Integration API Catalog — KlickSmartAI & LeadSniperAI
created: 2026-08-05
updated: 2026-08-05
type: summary
tags: [technology, research, how-to]
sources: [notion: Application Integration API Catalog — KlickSmartAI & LeadSniperAI]
related: [lead-sniperai-cli-os, lead-sniperai-signal-cold-email-sop, deepline]
---

# Purpose
This document is the working API integration catalog for KlickSmartAI, LeadSniperAI, the Growth Intelligence Platform, Mortgage CoPilot, and related business-funding workflows.
It organizes APIs by function, shows where each service fits in the application architecture, and identifies recommended implementation priorities.
# Core Architecture
**Data sources → Research and enrichment → AI reasoning → CRM and workflow automation → Outreach and transactions → Analytics and monitoring**
# 1. Web Search, Research and Market Intelligence
## Exa
**Primary role:** Open-web search, page retrieval, structured research, company discovery, and monitoring.
- Search API — semantic and neural web search
- Contents API — retrieve clean page content, highlights, summaries, and metadata
- Answer API — source-grounded answers
- Deep Search / Research — multi-step web research
- Exa Agent API — autonomous research, enrichment, and list-building
- Websets — continuously maintained sets of companies, people, or entities
- Monitors API — recurring monitoring for changes and new signals
- Exa MCP Server — agent access to Exa search and retrieval
**Application uses:**
- Company and competitor research
- Market mapping
- Funding and expansion signals
- Lead research
- Executive-change monitoring
- Content and source retrieval
## Parallel Search API
**Primary role:** AI-oriented web search that combines a natural-language objective with multiple concise search queries and returns ranked web results with excerpts.
**Endpoint:** `POST https://api.parallel.ai/v1/search`
**Authentication:** `x-api-key` request header.
**Core request fields:**
- `search_queries` — required list of concise 3–6 word searches; Parallel recommends 2–3 high-quality queries
- `objective` — self-contained description of the business question or research goal
- `mode` — `turbo`, `basic`, or `advanced`; advanced is the default
- `max_chars_total` — controls the total excerpt size returned
- `session_id` — maintains context across related Search and Extract requests
- `client_model` — identifies the model consuming the results
- `advanced_settings` — optional source, fetch, and excerpt controls
**Response fields:**
- `search_id`
- ranked `results` containing URL, title, publication date, and excerpts
- `session_id` for continued research
- optional warnings and usage metrics
**Application uses:**
- Company, competitor, and market research
- Current funding, hiring, expansion, product-launch, and executive-change signals
- Evidence retrieval for GTM and growth strategies
- Multi-query research for LeadSniperAI opportunity scoring
- Source discovery before website extraction and enrichment
- Agent research sessions that continue from Search into Parallel Extract
**Recommended integration pattern:**
`business objective → generate 2–3 focused search queries → Parallel Search → deduplicate and rank sources → Parallel Extract or Firecrawl → signal classification → strategy engine → Atomic CRM`
**Routing position:** Use Parallel when the application needs objective-aware, evidence-rich research. Use [Serper.dev](http://Serper.dev) for fast Google SERPs, Maps, Places, and local discovery; use Exa for semantic discovery and content retrieval; use DataForSEO for SEO metrics and scaled SERP intelligence.
## [Serper.dev](http://Serper.dev)
**Primary role:** Google Search API access.
**Application uses:**
- Search results
- Local business discovery
- News and review discovery
- Zero-volume keyword validation
- Google Maps and local-intent research
## DataForSEO
**Primary role:** SEO, keyword, SERP, backlink, business-data, and competitive-search intelligence.
**Useful APIs:**
- Keywords Data API
- SERP API
- Labs API
- Backlinks API
- On-Page API
- Business Data API
- Content Analysis API
- Domain Analytics API
- Merchant API
- App Data API
**Application uses:**
- SEO audits
- Competitor keyword analysis
- Search-demand discovery
- Local business intelligence
- Content-gap analysis
- Ranking and visibility monitoring
## Tavily
**Primary role:** AI-focused web search and research.
**Application uses:**
- Fast agent search
- Source retrieval
- Research augmentation
- Fallback search provider
## Firecrawl
**Primary role:** Website crawling and structured extraction.
**Application uses:**
- Crawl company websites
- Extract products, services, team, contact, and policy pages
- Convert sites into Markdown or structured JSON
- Build company knowledge profiles
## Apify
**Primary role:** Managed web scraping and automation actors.
**Application uses:**
- Public website extraction
- Directory and marketplace research
- Review gathering
- Scheduled data collection
## NotebookLM Python API (`teng-lin/notebooklm-py`)
**Primary role:** Programmable, source-grounded research synthesis and content-generation layer for Google NotebookLM.
**Repository:** [teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py)
**Capabilities:**
- Create and manage NotebookLM notebooks programmatically
- Import websites, PDFs, YouTube videos, and Google Drive sources
- Run structured questions against controlled source collections
- Generate research reports, summaries, tables, mind maps, quizzes, slide decks, audio overviews, videos, and downloadable artifacts
- Operate through Python, CLI, and agent skills for tools such as Codex, Claude Code, and OpenClaw
**Application uses:**
- Build a dedicated evidence notebook for each KlickSmartAI client, market, or competitor study
- Convert LeadSniperAI assessments, transcripts, financial documents, program guidelines, and lender criteria into advisor-ready funding intelligence
- Produce source-grounded growth briefs, competitor comparisons, funding-readiness assessments, executive reports, presentations, and audio briefings
- Support reusable research pipelines in which one validated source set produces multiple client deliverables
**Recommended integration pattern:**
`Parallel / Exa / Serper / DataForSEO / government sources → source validation and deduplication → notebooklm-py → structured research questions → citation and quality review → strategy engine → Notion / Drive / CRM / client deliverables`
**Implementation guidance:**
- Use it after the discovery and extraction layer rather than as the primary search engine
- Integrate through a Python service or CLI step within n8n
- Store original sources, generated outputs, citations, and final artifacts outside NotebookLM
- Require human review before external funding, legal, financial, or strategic recommendations
**Risk:** This is an unofficial integration that relies on undocumented NotebookLM endpoints. Authentication, RPC methods, quotas, and behavior may change without notice, so it should remain a replaceable synthesis service rather than the permanent system of record.
# 2. Company, Contact and Lead Enrichment
## [Snov.io](http://Snov.io)
**Primary role:** Prospecting, email discovery, verification, campaigns, and CRM enrichment.
**Application uses:**
- Domain search
- Email finder
- Email verifier
- Prospect list enrichment
- Outreach campaign handoff
- MCP-enabled prospecting workflows
## Apollo
**Primary role:** B2B company and contact data.
**Application uses:**
- Contact discovery
- Firmographic filtering
- Account enrichment
- Persona-based prospecting
## People Data Labs
**Primary role:** Person and company enrichment.
**Application uses:**
- Identity resolution
- Company matching
- Employment and firmographic enrichment
- Lead-profile completion
## Clearbit / HubSpot Breeze Intelligence
**Primary role:** Company and contact enrichment.
**Application uses:**
- Domain enrichment
- Firmographics
- Website visitor enrichment
- Lead routing
## Crunchbase
**Primary role:** Company, funding, acquisition, investor, and growth-event data.
**Application uses:**
- Funding signals
- Investor research
- Company growth indicators
- Acquisition monitoring
## BuiltWith
**Primary role:** Technology-stack intelligence.
**Application uses:**
- Detect website technologies
- Identify CRM, CMS, ecommerce, analytics, and marketing tools
- Find technology replacement opportunities
## Wappalyzer
**Primary role:** Website technology detection.
**Application uses:**
- Lightweight technographic enrichment
- Website modernization signals
- Sales segmentation
## Hunter
**Primary role:** Business-email discovery and verification.
**Application uses:**
- Domain search
- Email finding
- Email verification
## ZeroBounce / NeverBounce
**Primary role:** Email validation and deliverability protection.
**Application uses:**
- Pre-send verification
- Bounce reduction
- List hygiene
# 3. Social, Reviews and Public Signals
## Reddit API
**Primary role:** Community conversations, pain points, trends, and product sentiment.
**Application uses:**
- Voice-of-customer research
- Emerging topic discovery
- Competitor sentiment
- Content ideation
## LinkedIn integrations
**Primary role:** Professional identity, company, content, and outreach workflows where authorized.
**Application uses:**
- Company research
- Professional-network context
- Social-selling workflows
- Content-performance tracking
## Google Business Profile API
**Primary role:** Business listings, locations, and reviews for owned or authorized profiles.
**Application uses:**
- Local business profile management
- Review monitoring
- Location data
## Google Places API
**Primary role:** Place, business, address, category, and location data.
**Application uses:**
- Local lead discovery
- Address validation
- Territory mapping
- Business-category enrichment
## Yelp Fusion API
**Primary role:** Local business and review data.
**Application uses:**
- Local-market research
- Reputation signals
- Category and location discovery
## YouTube Data API
**Primary role:** Video, channel, search, and engagement data.
**Application uses:**
- Topic research
- Competitor content analysis
- Video-content intelligence
# 4. AI Models and Reasoning
## OpenAI API
**Primary role:** Reasoning, structured outputs, agents, embeddings, speech, and multimodal processing.
**Application uses:**
- Research synthesis
- Lead scoring
- Strategy generation
- Document analysis
- Voice workflows
- Structured extraction
- Agent orchestration
## Anthropic API
**Primary role:** Long-context analysis, reasoning, document work, and agent tasks.
**Application uses:**
- Research analysis
- Long-form strategy
- Document review
- Workflow agents
## Google Gemini API
**Primary role:** Multimodal reasoning, long-context processing, and Google ecosystem integration.
**Application uses:**
- Document and image analysis
- Research synthesis
- Multimodal workflows
## xAI API
**Primary role:** Model inference and research-oriented reasoning.
**Application uses:**
- Alternative-model analysis
- Model-consensus workflows
- Real-time research augmentation where available
## OpenRouter
**Primary role:** Unified access to multiple AI models.
**Application uses:**
- Model routing
- Cost optimization
- Provider fallback
- A/B model evaluation
## Ollama
**Primary role:** Local model serving.
**Application uses:**
- Private local inference
- Development and testing
- Lower-cost background classification
# 5. Embeddings, Vector Search and Knowledge Retrieval
## Qdrant
**Primary role:** Vector database and semantic search.
**Application uses:**
- Company knowledge retrieval
- Client-specific memory
- Document search
- RAG workflows
## Pinecone
**Primary role:** Managed vector search.
**Application uses:**
- Semantic retrieval
- Production RAG
- Knowledge-base search
## Weaviate
**Primary role:** Vector and hybrid search.
**Application uses:**
- Structured and semantic knowledge search
- Entity-based retrieval
## Neo4j
**Primary role:** Graph database and relationship intelligence.
**Application uses:**
- Company-person-investor relationships
- Referral networks
- Funding ecosystems
- Opportunity graphs
# 6. Databases, Storage and Data Infrastructure
## Supabase
**Primary role:** PostgreSQL database, authentication, storage, realtime, and edge functions.
**Application uses:**
- Multi-tenant application database
- User and organization records
- Lead and opportunity storage
- File storage
- Realtime workflows
## PostgreSQL
**Primary role:** Core relational database.
**Application uses:**
- Leads
- Companies
- Deals
- tasks
- workflow state
- audit logs
## MotherDuck / DuckDB
**Primary role:** Analytical data warehouse and embedded analytics.
**Application uses:**
- Research-result analysis
- Bulk lead analysis
- KPI reporting
- Data-model experimentation
## Google Drive API
**Primary role:** Connected file and document storage.
**Application uses:**
- Client document intake
- Proposal storage
- Research archive
- Workflow attachments
## Google Sheets API
**Primary role:** Spreadsheet data exchange and operational reporting.
**Application uses:**
- Imports and exports
- Lightweight operational databases
- Client reports
- Manual review queues
## Notion API
**Primary role:** Knowledge management, documentation, databases, and operating-system pages.
**Application uses:**
- API catalog
- SOPs
- client workspaces
- project documentation
- meeting notes
- strategy repositories
# 7. CRM, Sales and Customer Operations
## Atomic CRM
**Primary role:** Core CRM and lead-management layer.
**Application uses:**
- Leads and contacts
- Deal stages
- activity tracking
- opportunity management
- AI-enriched records
## HubSpot API
**Primary role:** CRM, marketing, sales, and service automation.
**Application uses:**
- Contact synchronization
- Deal management
- campaign automation
- reporting
## Salesforce API
**Primary role:** Enterprise CRM integration.
**Application uses:**
- Account and opportunity synchronization
- enterprise-client integrations
- workflow triggers
## Pipedrive API
**Primary role:** Sales-pipeline integration.
**Application uses:**
- Deal synchronization
- activity creation
- pipeline reporting
## Zoho CRM API
**Primary role:** CRM and business-suite integration.
**Application uses:**
- Lead and deal synchronization
- SMB client integrations
# 8. Email, Messaging and Communications
## Resend
**Primary role:** Transactional and application email.
**Application uses:**
- Notifications
- assessment results
- onboarding
- transactional outreach
## SendGrid
**Primary role:** Transactional and marketing email delivery.
**Application uses:**
- Email delivery
- templates
- event webhooks
## Postmark
**Primary role:** High-deliverability transactional email.
**Application uses:**
- Critical notifications
- application-generated mail
## Gmail API
**Primary role:** Mailbox search, reading, drafting, sending, and workflow automation.
**Application uses:**
- Lead-response monitoring
- email triage
- reply drafting
- thread-aware workflows
## Microsoft Graph
**Primary role:** Microsoft 365 email, calendar, files, contacts, and Teams integration.
**Application uses:**
- Outlook integration
- OneDrive and SharePoint
- calendar and Teams workflows
## Twilio
**Primary role:** SMS, phone, verification, and communications infrastructure.
**Application uses:**
- Lead verification
- SMS follow-up
- phone notifications
- OTP authentication
## Vapi
**Primary role:** AI voice-agent infrastructure.
**Application uses:**
- AI discovery interviews
- voice-qualified leads
- appointment setting
- follow-up calls
## Telnyx
**Primary role:** Voice, messaging, and telecom APIs.
**Application uses:**
- Alternative communications provider
- phone provisioning
- messaging workflows
## WhatsApp Business Platform
**Primary role:** Business messaging.
**Application uses:**
- Lead follow-up
- document reminders
- client updates
## Slack API
**Primary role:** Internal alerts, collaboration, and workflow actions.
**Application uses:**
- Sales alerts
- research-review queues
- operational notifications
## Chatwoot API
**Primary role:** Omnichannel customer-support inbox.
**Application uses:**
- Website chat
- email and messaging inbox
- human handoff from AI agents
# 9. Calendar, Scheduling and Meetings
## Google Calendar API
**Primary role:** Calendar availability and event management.
**Application uses:**
- Discovery-call booking
- advisor scheduling
- reminders
- meeting workflows
## Microsoft Graph Calendar
**Primary role:** Outlook calendar integration.
**Application uses:**
- Enterprise scheduling
- Microsoft 365 availability
## Calendly API
**Primary role:** Scheduling-event automation.
**Application uses:**
- Booking-event ingestion
- lead-stage updates
- reminder workflows
## [Cal.com](http://Cal.com) API
**Primary role:** Open scheduling infrastructure.
**Application uses:**
- Embedded scheduling
- white-label booking
- routing forms
## Zoom API
**Primary role:** Video-meeting management.
**Application uses:**
- Meeting creation
- recordings and transcripts
- client-call workflows
# 10. Authentication, Identity and Permissions
## Clerk
**Primary role:** Authentication, users, organizations, sessions, and permissions.
**Application uses:**
- Multi-tenant authentication
- organization membership
- role-based access
- user onboarding
## Auth0
**Primary role:** Enterprise identity and authentication.
**Application uses:**
- SSO
- enterprise connections
- identity federation
## Supabase Auth
**Primary role:** Authentication integrated with Supabase.
**Application uses:**
- Email and social login
- user sessions
- row-level security
## Google OAuth
**Primary role:** Google account authorization.
**Application uses:**
- Gmail
- Drive
- Calendar
- Sheets
## Microsoft Entra ID
**Primary role:** Microsoft identity and enterprise SSO.
**Application uses:**
- Microsoft Graph authorization
- enterprise-client access
# 11. Payments, Billing and Commerce
## Stripe
**Primary role:** Payments, subscriptions, invoices, payment links, and billing.
**Application uses:**
- Marketplace payments
- subscription billing
- one-time purchases
- invoices
- webhook-driven provisioning
## PayPal
**Primary role:** Alternative online payments.
**Application uses:**
- Customer payment option
- invoicing
## Square
**Primary role:** Payments and merchant services.
**Application uses:**
- SMB payment integrations
- in-person and online payment workflows
# 12. Workflow Automation and Agent Orchestration
## n8n
**Primary role:** Workflow automation and agent-loop orchestration.
**Application uses:**
- API integrations
- scheduled monitoring
- lead enrichment
- CRM synchronization
- outreach sequences
- human review steps
- retry and approval loops
## Composio
**Primary role:** Tool and application integrations for AI agents.
**Application uses:**
- Unified agent actions
- OAuth management
- third-party application access
## Pipedream
**Primary role:** Developer-first API workflow automation.
**Application uses:**
- Event-driven integrations
- webhook processing
- rapid API prototypes
## Zapier
**Primary role:** No-code application automation.
**Application uses:**
- Client-specific integrations
- simple workflow handoffs
## Make
**Primary role:** Visual workflow automation.
**Application uses:**
- SMB integration workflows
- data synchronization
## Vercel Workflow / Queues / Cron
**Primary role:** Durable application workflows, queues, and scheduled execution.
**Application uses:**
- Long-running application processes
- asynchronous jobs
- retries
- scheduled signal scans
# 13. Application Hosting, Deployment and Observability
## Vercel API
**Primary role:** Deployment, project, domain, environment, and observability management.
**Application uses:**
- Deploy applications
- manage domains
- environment configuration
- deployment monitoring
## Firebase
**Primary role:** Hosting, database, authentication, analytics, and messaging.
**Application uses:**
- Static hosting
- application services
- push notifications
## Cloudflare API
**Primary role:** DNS, security, edge networking, Workers, and storage.
**Application uses:**
- Domain management
- tenant routing
- edge functions
- rate limiting
- security
## Google Cloud APIs
**Primary role:** Cloud Run, storage, AI, logging, and managed infrastructure.
**Application uses:**
- Backend services
- document processing
- scalable workloads
## AWS APIs
**Primary role:** Cloud infrastructure and managed services.
**Application uses:**
- storage
- compute
- queues
- enterprise integrations
## Sentry
**Primary role:** Error tracking and application performance monitoring.
**Application uses:**
- Error alerts
- release monitoring
- debugging
## PostHog
**Primary role:** Product analytics, session replay, feature flags, and experiments.
**Application uses:**
- User behavior
- funnel analysis
- feature adoption
- experiments
## OpenTelemetry
**Primary role:** Standardized logs, traces, and metrics.
**Application uses:**
- Cross-service observability
- workflow tracing
- AI-agent monitoring
# 14. Documents, Forms and E-Signatures
## DocuSign API
**Primary role:** Electronic signatures and agreement workflows.
**Application uses:**
- Client agreements
- lending disclosures
- service contracts
## Dropbox Sign API
**Primary role:** Electronic signatures.
**Application uses:**
- Lightweight contract signing
- embedded signatures
## PandaDoc API
**Primary role:** Proposals, quotes, documents, and signatures.
**Application uses:**
- Funding proposals
- service agreements
- sales documents
## Typeform API
**Primary role:** Forms and assessment intake.
**Application uses:**
- Lead qualification
- funding assessments
- discovery questionnaires
## Tally API / Webhooks
**Primary role:** Lightweight form intake.
**Application uses:**
- Lead forms
- application intake
- workflow triggers
## [PDF.co](http://PDF.co) / Adobe PDF Services
**Primary role:** PDF generation, conversion, extraction, and document workflows.
**Application uses:**
- Application packages
- statement extraction
- report generation
# 15. Accounting and Financial Data
## QuickBooks Online API
**Primary role:** Accounting, invoices, customers, transactions, and reporting.
**Application uses:**
- Business financial verification
- bookkeeping integrations
- invoice synchronization
## Xero API
**Primary role:** Accounting and financial records.
**Application uses:**
- SMB financial-data integration
- cash-flow analysis
## Plaid
**Primary role:** Bank-account connectivity and transaction data.
**Application uses:**
- Account verification
- cash-flow analysis
- transaction categorization
## Flinks
**Primary role:** Canadian financial-data connectivity.
**Application uses:**
- Canadian bank-data access
- lending and affordability workflows
## Stripe Financial Connections
**Primary role:** Bank-account and financial-data connection.
**Application uses:**
- Account verification
- financial-data intake
# 16. Mortgage and Lending Integrations
## Newton Velocity
**Primary role:** Canadian mortgage origination and broker workflow platform.
**Potential uses:**
- Application data synchronization
- deal-status tracking
- broker dashboards
- document and milestone workflows
## Credit bureau integrations
**Examples:** Equifax, TransUnion, Experian where authorized and contractually available.
**Application uses:**
- Credit assessment
- identity verification
- lending qualification
## Lender and underwriting APIs
**Primary role:** Product eligibility, pricing, submissions, status, and document exchange where available.
**Application uses:**
- Product matching
- application submission
- status updates
- underwriting support
# 17. Analytics, Reporting and Marketing Data
## [Windsor.ai](http://Windsor.ai)
**Primary role:** Marketing-data connectors and unified reporting.
**Application uses:**
- Advertising data
- SEO and social data
- cross-channel reporting
- client dashboards
## Google Analytics Data API
**Primary role:** Website and application analytics.
**Application uses:**
- Traffic analysis
- conversion tracking
- campaign attribution
## Google Search Console API
**Primary role:** Organic-search performance data.
**Application uses:**
- query and page performance
- SEO monitoring
- indexing checks
## Meta Marketing API
**Primary role:** Facebook and Instagram advertising data and campaign management.
**Application uses:**
- campaign reporting
- lead-ad ingestion
- audience and creative analysis
## Google Ads API
**Primary role:** Google advertising campaign management and reporting.
**Application uses:**
- keyword data
- campaign performance
- conversion analysis
## LinkedIn Marketing API
**Primary role:** LinkedIn campaign and lead-generation integrations where approved.
**Application uses:**
- ad reporting
- lead-form synchronization
- campaign analytics
# Recommended Integration Tiers
## Tier 1 — Core Platform
- OpenAI
- Exa
- DataForSEO
- Supabase
- Clerk
- n8n
- Atomic CRM
- Resend
- Twilio
- Vapi
- Stripe
- Qdrant
- Google Drive, Gmail, Calendar, and Sheets
- Vercel
## Tier 2 — Growth Intelligence
- Parallel
- [Serper.dev](http://Serper.dev)
- Firecrawl
- [Snov.io](http://Snov.io)
- Crunchbase
- BuiltWith or Wappalyzer
- Reddit
- [Windsor.ai](http://Windsor.ai)
- Google Analytics
- Search Console
## Tier 3 — Enterprise and Expansion
- Microsoft Graph
- HubSpot
- Salesforce
- Plaid or Flinks
- DocuSign
- Neo4j
- OpenTelemetry
- Sentry
- PostHog
# Recommended Integration Pattern
1. **Collect** data through search, enrichment, forms, CRM, and connected applications.
2. **Normalize** all records into a common company, contact, signal, opportunity, and source schema.
3. **Enrich** records using company, contact, technology, funding, and public-signal providers.
4. **Reason** over the evidence using AI models and retrieval.
5. **Score** fit, intent, urgency, confidence, and opportunity value.
6. **Route** the opportunity into CRM, human review, or automated outreach.
7. **Execute** email, SMS, voice, scheduling, proposal, and payment workflows.
8. **Monitor** performance, source reliability, costs, conversion, and workflow failures.
# Governance Requirements
For every API integration, document:
- Business purpose
- Data owner
- Authentication method
- Required scopes
- Data collected
- Data retention period
- Consent requirements
- Privacy and compliance requirements
- Rate limits
- Cost model
- Retry policy
- Webhook behavior
- Failure fallback
- Monitoring owner
- Production status
# Suggested API Registry Fields
Create a future Notion database with these properties:
- API / Provider
- Category
- Business Purpose
- Product / Workflow
- Priority
- Integration Status
- Owner
- Authentication Type
- Documentation URL
- Base URL
- Environment Variables
- Webhooks
- Rate Limits
- Monthly Cost
- Data Sensitivity
- Compliance Notes
- Last Reviewed
- Next Action
# Immediate Next Build Sequence
1. Exa + DataForSEO research layer
2. Firecrawl website extraction
3. [Snov.io](http://Snov.io) contact discovery and verification
4. Supabase normalized intelligence store
5. OpenAI reasoning and structured scoring
6. Atomic CRM opportunity creation
7. n8n orchestration
8. Resend, Twilio, and Vapi outreach
9. Google Calendar booking
10. Stripe transaction and provisioning workflow
# Source Reference
- Exa Labs GitHub organization: [https://github.com/exa-labs](https://github.com/exa-labs)
# Status
**Document type:** Working integration architecture
**Recommended review cadence:** Monthly and whenever a provider, pricing model, authentication method, or API version changes.
# [Serper.dev](http://Serper.dev) Integration Detail
## [Serper.dev](http://Serper.dev)
**Primary role:** Fast, real-time Google SERP retrieval for search-driven application workflows.
**Supported result types:**
- Google Search
- Images
- News
- Maps
- Places
- Videos
- Shopping
- Scholar
- Patents
- Autocomplete
**Best application uses:**
- Local-business and prospect discovery
- Competitor and brand-result monitoring
- Current news and market-signal discovery
- Google Maps and location-based lead research
- Review-source discovery
- Keyword and search-intent validation
- Search-result enrichment before AI analysis
- Low-latency search for conversational agents
**Role in the architecture:**
[Serper.dev](http://Serper.dev) should act as the **fast Google retrieval layer**. It provides current search-result data quickly, while Exa and Parallel handle deeper semantic discovery, source retrieval, multi-step research, and synthesis.
**Recommended workflow:**
`User or scheduled query → Serper.dev search → normalize results → fetch selected pages → AI classification and synthesis → company/lead record → CRM or signal workflow`
**Recommended provider routing:**
- Use [**Serper.dev**](http://Serper.dev) when Google rankings, Maps, Places, News, Shopping, or immediate SERP visibility matter.
- Use **Exa** for semantic company discovery, relevant-page retrieval, Websets, and open-web research.
- Use **Parallel** for deeper multi-source research and structured intelligence reports.
- Use **DataForSEO** for scaled SEO metrics, keyword data, backlinks, rankings, and competitive search analytics.
**Implementation priority:** High
**Suggested integration fields:**
- Query
- Search type
- Country
- Language
- Location
- Number of results
- Organic position
- Result title
- Result URL
- Snippet
- Knowledge graph
- Places or Maps result
- Related searches
- People-also-ask questions
- Retrieved timestamp
- Source provider
- Workflow or client ID
**Operational notes:**
- Cache results where suitable to control credit usage.
- Store query, location, language, and retrieval time for auditability.
- Deduplicate URLs before sending pages to Firecrawl, Exa Contents, or another extraction service.
- Apply rate limiting, retries, and provider fallback through n8n or the application backend.
- Do not treat SERP snippets as final evidence; fetch and verify important source pages before generating strategic conclusions.
**Official site:** [Serper.dev](https://serper.dev)
# 18. GitHub Repository Integration Registry
The separate <mention-page url="https://app.notion.com/p/ac225ddcc33b4eb4a6ffe765ad25857f"/> is the implementation-source registry for open-source frameworks, SDKs, MCP servers, agent runtimes, workflow components, and reference architectures that may connect to the APIs in this catalog.
## API-ready repositories already identified
### n8n
**Integration role:** Workflow and API orchestration bus.
**Relevant interfaces:** Webhooks, REST APIs, scheduled triggers, Gmail/IMAP, Supabase, Twilio, CRM and custom HTTP nodes.
**Recommended use:** Intake, enrichment calls, signal routing, CRM synchronization, notifications and human-review workflows. Keep core LeadSniperAI decision logic in version-controlled application code.
### Resend
**Integration role:** Transactional and application email API.
**Relevant interfaces:** Node/TypeScript SDK, email-send API, React Email templates and delivery-event webhooks.
**Recommended use:** Assessment results, onboarding, notifications and controlled outbound messaging. Use a dedicated sending subdomain and feed delivery, bounce and complaint events back into the CRM.
### Atomic CRM
**Integration role:** CRM and operational system of record.
**Relevant interfaces:** Supabase/PostgreSQL data layer, REST access, custom fields and activity records.
**Recommended use:** Contacts, companies, opportunities, tasks, outreach state and AI-enriched records.
### Atomic CRM MCP
**Integration role:** Governed agent access to CRM data.
**Relevant interfaces:** MCP tools for schema discovery and SQL queries, Supabase OAuth 2.1, JWT validation and row-level security.
**Recommended use:** Allow approved agents to find neglected leads, update records and retrieve pipeline context without exposing unrestricted database access.
### LeadSniper Search Engine Growth Intelligence
**Integration role:** Internal intelligence and strategy application.
**Relevant interfaces:** DataForSEO, [Serper.dev](http://Serper.dev), Exa, Parallel, community-data sources, CRM outputs and workflow webhooks.
**Recommended use:** Convert search, market and community evidence into SEO, AEO, GTM, funding and growth recommendations.
## Reference repositories rather than external APIs
The following catalogue entries provide code, runtime patterns or reusable skills rather than standalone third-party APIs:
- PAUL — bounded Plan–Apply–Unify execution-loop pattern
- Anthropic Skills and Vercel Agent Skills — portable agent-skill conventions
- Hermes Agent — autonomous runtime, tools and memory
- AionUI — operator interface for supervising agents
- Claude SEO — reusable SEO analysis workflows
- Obsidian CLI Skill — operational knowledge access
- Harness-engineering references — evaluation, governance and reliability patterns
## Registry relationship
Use this API Catalog to decide **which external capability is required**. Use the GitHub Repository Catalogue to decide **which SDK, framework, MCP server, implementation pattern or open-source component will deliver it**.
Recommended linking model:
**Business capability → API provider → GitHub implementation source → application service → workflow → CRM record → measurable outcome**
# BuildData — Canadian Construction and Property Data API
**Primary role:** Specialized Canadian construction, property, permitting, contractor, zoning, and municipal business-data intelligence.
**Official site:** [BuildData](https://www.builddata.ca/)
**API access:** Available through RapidAPI, with an OpenAPI specification published by BuildData.
## Data products
- Building permits — new construction, renovations, additions, demolitions, status, construction value, and geocoded addresses
- Building inspections — inspection type, result, and date linked to permit activity
- Business licences — active and historical municipal business licences
- Contractor profiles — permit history, licence status, and trade type
- Development permits — land-use and development applications
- Planning applications — rezoning, variance, subdivision, and municipal-planning activity
- Property assessments — assessed value, land value, improvement value, lot size, year built, and property class
- Zoning — zoning codes, descriptions, land-use categories, and polygon-based location resolution
- Geocoding — Canadian address lookup and reverse geocoding
## Core API patterns
- Search endpoints for each dataset
- Statistics endpoints
- Municipality and coverage filters
- Record lookup by ID
- Full-text search
- Date, value, permit-type, and location filters
- Latitude, longitude, and radius-based proximity search
- Cursor or offset pagination
## Representative endpoints
- `/permit`
- `/permit/stats`
- `/permit/{record_id}`
- `/inspection`
- `/licence`
- `/contractor`
- `/development_permit`
- `/planning_application`
- `/assessment`
- `/zone`
- `/zoning`
- `/geocode`
- `/reverse-geocode`
## Application uses
- Detect businesses and property owners beginning construction or renovation projects
- Identify commercial-development and real-estate financing opportunities
- Find contractors and developers with active project pipelines
- Trigger mortgage, construction-finance, equipment-finance, insurance, website, marketing, and business-services outreach
- Monitor zoning changes, development applications, and planning approvals
- Enrich property and business records inside LeadSniperAI and Atomic CRM
- Build city-level construction-market dashboards and opportunity heat maps
- Validate property, address, zoning, and municipal-record information
## Recommended LeadSniperAI workflow
`BuildData permit or development signal → address and company resolution → contractor/property enrichment → funding and growth classification → opportunity score → Atomic CRM → advisor or outreach workflow`
## Suggested signal rules
- High-value new permit → construction or commercial financing opportunity
- Renovation or addition permit → refinance, equipment, contractor, and service opportunity
- New business licence → website, CRM, payments, marketing, or working-capital opportunity
- Development or planning application → early-stage developer and land-financing opportunity
- Repeated contractor permit activity → active contractor account with recurring financing potential
- Assessment plus zoning data → property-development feasibility and mortgage intelligence
## Architecture position
BuildData should sit in the **specialized Canadian business and property signal layer**, alongside government open data and commercial enrichment providers. [Serper.dev](http://Serper.dev) and Exa can enrich the entities discovered through BuildData; Parallel can research the project and organization; DataForSEO can evaluate digital demand and visibility; Atomic CRM stores the resulting opportunity.
# API Marketplaces and Discovery Layers
## RapidAPI Hub
**Primary role:** Marketplace, gateway, testing environment, subscription manager, and discovery layer for third-party APIs.
**What it provides:**
- Searchable catalogue of APIs across many categories
- Interactive endpoint testing from the browser
- Generated code examples in multiple programming languages
- Centralized API-key and subscription management
- Usage, latency, request-volume, and error-rate dashboards
- Free, freemium, paid, and usage-based plans determined by each provider
- Provider tools for publishing, documenting, securing, monitoring, and monetizing APIs
**Application uses:**
- Discovering niche data sources not covered by core strategic providers
- Quickly prototyping an integration before negotiating directly with a provider
- Testing endpoint inputs and responses
- Comparing alternative APIs for the same capability
- Temporary or secondary providers for enrichment, geocoding, company information, news, translation, and other supporting capabilities
**Recommended architectural position:** RapidAPI should be treated as an API marketplace and procurement channel, not as a single authoritative data provider. Each API listed on the marketplace must be assessed independently.
**Due-diligence checklist for every RapidAPI integration:**
- Identify the actual API provider and upstream data source
- Review terms of use, permitted storage, resale, and commercial-use rights
- Confirm geographic coverage, update frequency, and data provenance
- Test accuracy, completeness, latency, uptime, and pagination
- Review pricing, quotas, overage charges, and rate limits
- Confirm privacy, consent, and Canadian regulatory requirements where applicable
- Check whether a direct provider agreement or official API offers better reliability
- Build provider abstraction, caching, monitoring, and fallback routing
**Governance rule:** Do not place marketplace-specific request formats directly throughout application code. Route approved RapidAPI services through an internal provider adapter so they can be replaced without changing LeadSniperAI, KlickSmartAI, or Mortgage CoPilot business logic.
**Recommended status:** Approved for discovery and controlled pilots. Production adoption requires individual provider review.
**Reference:** [https://rapidapi.com/hub](https://rapidapi.com/hub)
# Unipile API
**Primary role:** Unified account connectivity and communication operations across supported professional-network, email, calendar, and messaging providers.
## List all accounts
**Endpoint:** `GET https://{subdomain}.unipile.com:{port}/api/v1/accounts`
**Purpose:** Returns the accounts currently linked to the Unipile workspace. This should be called before account-specific actions so the application can identify available connected accounts, provider type, account status, and the account identifier required by downstream operations.
**Query parameters:**
- `cursor` — pagination cursor returned by the previous response
- `limit` — number of records to return, from 1 to 250
**Application uses:**
- Build a connected-accounts dashboard
- Map each Unipile account to a KlickSmartAI or LeadSniperAI user or organization
- Select the correct LinkedIn, email, calendar, or messaging identity for a workflow
- Detect disconnected or expired accounts
- Prevent outreach from using the wrong account
- Route account-specific webhooks and activity into Atomic CRM
**Recommended workflow:**
`User connects provider → Unipile creates account → List Accounts → store account ID and provider metadata → health/status validation → enable permitted workflows`
**Implementation guidance:**
- Store the Unipile account ID as an external identifier, not as the CRM contact ID.
- Associate every account with a tenant, application user, provider, status, and consent record.
- Retrieve all pages until no next cursor remains.
- Cache the account list briefly, but refresh before sensitive send or synchronization operations.
- Treat disconnected, expired-credential, insufficient-privilege, and provider errors as recoverable account-health states.
- Require explicit authorization and comply with provider terms and outreach rules.
**Best fit:** Shared communication integration layer for LeadSniperAI, KlickSmartAI, Mortgage CoPilot, and Atomic CRM.
# Repliers Real Estate API
**Primary role:** Canadian and U.S. real-estate listing, MLS®, brokerage, office, agent, property-search, comparables, and market-data integration.
**Core API base:** `https://api.repliers.io`
**Important endpoints and capabilities:**
- `POST /listings` — search listings with filters, pagination, aggregates, map clusters, market statistics, and AI image search
- `GET /listings/{mlsNumber}` — retrieve a detailed listing, including MLS® history and comparable properties
- `GET /listings/{mlsNumber}/similar` — retrieve similar active listings
- `GET /offices` — retrieve brokerage offices
- Agent, location, building, saved-search, favorites, and market-statistics resources where enabled
- Standardized normalized fields across MLS® systems, with optional raw MLS® fields using `fields=raw`
- Listing images delivered through the Repliers CDN
**Authentication:** Send the API credential in the `REPLIERS-API-KEY` request header.
**Canadian data coverage:** Repliers supports most Canadian MLS® systems through regional MLS® access and [REALTOR.ca](http://REALTOR.ca) DDF® arrangements, subject to the appropriate board, brokerage, agent, or vendor approval.
**Application uses:**
- Mortgage CoPilot property search and property context
- Mortgage prequalification tied to active listings
- Affordability and payment scenarios built from listing prices
- Comparable-property and listing-history research
- Realtor referral and co-marketing workflows
- Property alerts and saved searches
- LeadSniperAI property-owner, brokerage, agent, and market-opportunity intelligence
- Market dashboards by city, neighbourhood, property type, price band, and listing status
- Automated CRM records when a buyer saves, views, or inquires about a property
**Recommended workflow:**
`Buyer profile → mortgage prequalification → Repliers listing search → payment and affordability calculation → saved property → realtor or mortgage-advisor assignment → Atomic CRM → follow-up automation`
**Architecture position:** Repliers is the normalized MLS® and real-estate application layer. BuildData supplies permits, zoning, licences, assessments, and construction signals; Repliers supplies listings, comparable properties, agents, offices, and market activity.
**Compliance warning:** Production MLS® access is not automatically available to a mortgage brokerage or general technology company. Canadian production access typically requires approval through a participating real-estate brokerage, agent, MLS® board, [REALTOR.ca](http://REALTOR.ca) DDF®, or an approved technology-vendor arrangement. A mortgage broker alone is not treated as an eligible real-estate professional for MLS® licensing purposes. Store the authorized brokerage, board, permitted domains, end-user scope, display rules, attribution requirements, and data-retention restrictions in the integration registry before production deployment.
**Implementation recommendation:** Begin with a sandbox proof of concept using simulated data. Move to production only after confirming the licensed real-estate entity, intended application, boards or DDF® feed, display requirements, and vendor approval.
# Repliers Brokerage Partnership Update
**Decision:** Proceed with Repliers through a licensed real-estate brokerage partnership.
## Operating model
- **Brokerage:** MLS® data sponsor, licensed real-estate service provider, and recipient/owner of real-estate leads under the partnership agreement.
- **KlickSmartAI / Mortgage CoPilot:** technology, affordability, mortgage-readiness, CRM, automation, and AI workflow layer.
- **Repliers:** normalized MLS® listing, comparable, agent, office, and market-data API.
## Production access path
1. Select a brokerage partner with the required board/MLS® authorization.
2. Confirm that the brokerage can sponsor or authorize Repliers production access in the intended markets.
3. Execute the brokerage partnership, MLS® data-use, privacy, branding, and technology agreements.
4. Configure the Repliers production account under the approved brokerage or vendor arrangement.
5. Map brokerage, agent, office, listing, inquiry, borrower, and mortgage-advisor identifiers in the shared data model.
6. Launch a limited-market pilot before expanding to additional boards or provinces.
## Co-branded product concept
**Home Search + Mortgage Readiness Platform**
`borrower intake → mortgage readiness or prequalification → affordability range → Repliers listing search → saved property or inquiry → brokerage agent assignment → mortgage advisor assignment → Atomic CRM → coordinated follow-up`
## Lead-routing rules
- Property inquiries and showing requests route to the partner brokerage or assigned licensed agent.
- Mortgage-readiness, prequalification, refinancing, and financing inquiries route to the mortgage-advisory workflow.
- Shared leads require explicit customer consent and a visible record of which parties may contact the customer.
- Atomic CRM should maintain separate ownership fields for the brokerage, agent, mortgage advisor, and platform source.
- Duplicate records should be resolved using normalized email, phone, Repliers identifiers, and CRM identifiers.
## Agreement requirements
- MLS® and listing-data access responsibilities
- Permitted data displays, retention, caching, and derivative calculations
- Brokerage and platform branding or co-branding
- Lead ownership, assignment, response-time standards, and reassignment rules
- Referral, marketing-service, or revenue-sharing terms subject to applicable regulation
- Customer consent, privacy notices, data-processing responsibilities, and breach response
- Advertising, listing attribution, trademark, and board-specific display requirements
- Service levels, API costs, termination, data deletion, and transition rights
## Recommended pilot
- One brokerage
- One MLS® market or board
- Buyer leads and purchase-mortgage scenarios first
- Core functions: listing search, listing detail, saved properties, inquiry capture, affordability calculation, agent routing, mortgage routing, and CRM activity logging
- Human review before any automated outreach
## Success measures
- Search-to-inquiry conversion
- Inquiry response time
- Percentage of inquiries matched to an agent
- Percentage completing mortgage-readiness assessment
- Prequalification conversion
- Appointments booked
- Applications submitted
- Funded mortgage volume
- Brokerage closed transactions influenced by the platform
- Customer consent and routing-error rate
## Integration status
**Priority:** High
**Status:** Partnership-dependent pilot candidate
**Next action:** Identify and approach a brokerage partner, validate its MLS® authorization and desired service area, and prepare a co-branded pilot proposal.
# 13. Canadian Government APIs and Public Data Sources
## Statistics Canada Developer Portal
**Primary role:** National demographic, census, labour, income, housing, business, and economic statistics.
**Direct links:**
- [Statistics Canada Developer Portal](https://www.statcan.gc.ca/en/developers)
- [Statistics Canada Web Data Service](https://www.statcan.gc.ca/en/developers/wds)
- [Web Data Service User Guide](https://www.statcan.gc.ca/en/developers/wds/user-guide)
**Application uses:**
- Market sizing and territory analysis
- Demographic and household-income profiling
- Labour-market and employment signals
- Business counts and industry analysis
- Housing and population-growth intelligence
- Geographic market scoring for LeadSniperAI and KlickSmartAI
## Government of Canada Open Government Portal
**Primary role:** Discovery and retrieval of federal government datasets and APIs across departments.
**Direct links:**
- [Open Government Portal](https://open.canada.ca/en/open-data)
- [Open Government API guidance](https://open.canada.ca/en/working-data-api/api)
- [Open Government API dataset page](https://open.canada.ca/data/en/dataset/2d90548d-50ef-4802-91f8-c59c5cf68251)
- [Search Canadian government datasets classified as APIs](https://search.open.canada.ca/opendata/?collection=api)
**Application uses:**
- Discovering government datasets by department, topic, geography, and format
- Building a government-data catalog for automated research workflows
- Finding economic, infrastructure, environmental, transportation, health, and regulatory data
- Feeding trusted public-sector evidence into the Growth Intelligence Platform
## ISED API Catalogue
**Primary role:** Federal business, innovation, corporate, intellectual-property, and economic-development APIs.
**Direct links:**
- [ISED API Catalogue](https://api.ised-isde.canada.ca/en/)
- [Corporations Canada Federal Corporation API](https://api.ised-isde.canada.ca/en/docs?api=corporations)
**Application uses:**
- Federal corporation verification
- Corporation status and registered-office lookup
- Director and company-record enrichment where available
- Business identity matching before EnrichLayer enrichment
- Company validation for LeadSniperAI opportunities
**Implementation note:** The Corporations Canada API may require account registration and plan access. Confirm current rate limits and terms before production use.
## Canada Mortgage and Housing Corporation
**Primary role:** Housing-market, rental, construction, affordability, mortgage, and regional housing intelligence.
**Direct links:**
- [CMHC Housing Data](https://www.cmhc-schl.gc.ca/professionals/housing-markets-data-and-research/housing-data)
- [CMHC Housing Market Information Portal](https://www.cmhc-schl.gc.ca/hmiportal)
- [CMHC Data Tables](https://www.cmhc-schl.gc.ca/professionals/housing-markets-data-and-research/housing-data/data-tables)
**Application uses:**
- Housing starts and completions
- Rental vacancy and rent analysis
- Regional housing-market trends
- Affordability and supply intelligence
- Mortgage CoPilot market context
- Real-estate and development opportunity scoring
**Implementation note:** CMHC often provides downloadable tables and portal-based data rather than a single general-purpose public REST API. Recommended pattern: scheduled CSV/XLSX ingestion → normalization → internal housing-data API.
## Canadian Importers Database
**Primary role:** Identification of Canadian companies importing specific products, grouped by product, city, and source country.
**Direct link:**
- [Canadian Importers Database](https://ised-isde.canada.ca/site/ised/en/research-and-business-intelligence/canadian-importers-database)
**Application uses:**
- B2B company discovery
- Trade and supply-chain signals
- Importer prospecting
- Market-entry research
- Company-list generation for enrichment and outreach
## Provincial and Municipal Open Data
**Primary role:** Local and regional datasets covering property, permits, zoning, licences, transportation, infrastructure, land, and demographics.
**Priority sources:**
- [British Columbia Data Catalogue](https://catalogue.data.gov.bc.ca/)
- [Ontario Data Catalogue](https://data.ontario.ca/)
- [Alberta Open Government](https://open.alberta.ca/opendata)
- [Données Québec](https://www.donneesquebec.ca/)
- [City of Vancouver Open Data](https://opendata.vancouver.ca/)
- [City of Toronto Open Data](https://open.toronto.ca/)
- [City of Calgary Open Data](https://data.calgary.ca/)
- [City of Edmonton Open Data](https://data.edmonton.ca/)
**Application uses:**
- Building permits and development activity
- Business licences and local-company discovery
- Property, zoning, and land-use intelligence
- Municipal expansion and infrastructure signals
- Local-market opportunity scoring
## Recommended Canadian Government Data Stack
**Priority 1 — Core foundation**
1. Statistics Canada
2. Government of Canada Open Government Portal
3. ISED API Catalogue
4. Corporations Canada
**Priority 2 — Industry intelligence**
1. CMHC housing datasets
2. Canadian Importers Database
3. Provincial open-data portals
4. Municipal open-data portals
**Recommended architecture:**
`Government APIs and public datasets → entity matching and normalization → EnrichLayer person/company/contact enrichment → AI signal classification → opportunity scoring → Atomic CRM → n8n execution`
**Strategic role:** Government sources should serve as the trusted signal and evidence layer. EnrichLayer should remain the foundation enrichment layer used to resolve company and people identities, complete profiles, and prepare records for AI scoring and outreach.