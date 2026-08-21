---
title: LeadSniperAI CLI PRD
created: 2026-08-05
updated: 2026-08-05
type: summary
tags: [technology, research, how-to]
sources: [notion: LeadSniperAI CLI PRD]
related: [lead-sniperai-cli-os, lead-sniperai-signal-cold-email-sop, deepline]
---

# Executive Summary
Build a production-ready `leadsniper` command-line interface that turns LeadSniperAI 3.0 into an agent-native local business opportunity intelligence system.
The CLI will expose LeadSniperAI's existing FastAPI capabilities through deterministic commands, structured JSON output, persistent job state, evidence tracking, testing, and an AI-readable `SKILL.md`. CLI Printing Press will be used as the preferred research and scaffolding accelerator to inspect API surfaces, generate an initial token-efficient Go CLI, produce the accompanying agent skill, and optionally expose approved commands through MCP. LeadSniperAI-owned domain rules, safety controls, tenancy, audit logging, and production verification remain authoritative.
The first release should wrap current repository functionality. Later releases should add proprietary website revenue-leak auditing, AI Employee fit scoring, campaign orchestration, compliance controls, and CRM routing.
## Source Repository
- GitHub: [https://github.com/Ksdeng1559/LeadSniper-3.0](https://github.com/Ksdeng1559/LeadSniper-3.0)
- Default branch: `main`
- Current application: React/Vite frontend with Python/FastAPI backend
- Current maturity: Beta; security, TypeScript, and test-coverage work remains before autonomous production use
# 1. Product Vision
## Vision Statement
LeadSniperAI CLI transforms the existing human-operated LeadSniper application into an agent-ready operating interface that AI agents can discover, invoke, verify, and chain into repeatable lead-intelligence workflows.
## Core Outcome
An authorized user or agent can run one command to:
1. Discover local service businesses.
2. Screen eligibility.
3. Enrich business and contact information.
4. Audit observable website and search weaknesses.
5. Score opportunity and AI Employee fit.
6. Record evidence and confidence.
7. Generate reviewable outreach assets.
8. Export qualified opportunities to downstream systems.
## Positioning
LeadSniperAI should be positioned as:
> An AI-operated local business opportunity intelligence and qualification engine.
It should not be positioned as a raw Google Maps scraper or as a system that fabricates buying intent, revenue loss, or contact information.
# 2. Objectives
## Primary Objectives
- Provide a stable `leadsniper` root command.
- Wrap existing FastAPI endpoints without duplicating business logic.
- Return machine-readable JSON for every operational command.
- Support human-readable terminal output for operators.
- Preserve evidence, source attribution, timestamps, and confidence.
- Keep outreach generation separate from outreach sending.
- Default to safe, read-oriented permissions.
- Support CLI-Anything conventions, including `SKILL.md`, `TEST.md`, structured commands, and production verification.
- Use CLI Printing Press to accelerate API research, command discovery, Go CLI scaffolding, agent-skill generation, and optional MCP exposure.
- Treat generated code as reviewed source material rather than automatically trusted production code.
- Preserve a stable LeadSniper-owned command contract even when underlying providers or generated adapters change.
## Non-Goals for Version 1
- Fully autonomous outbound sending.
- Unreviewed voice calling.
- Replacing the existing React application.
- Rebuilding every API integration inside the CLI.
- Treating guessed emails as verified contacts.
- Persisting an unauthorized replica of third-party business listings.
# 3. Target Users
- Lead-generation agencies
- Local SEO operators
- AI automation providers
- Business growth consultants
- Sales-development teams
- Lead marketplace operators
- AI agents working through Codex, Claude Code, or similar environments
# 4. Proposed Architecture
```plain text
Human or AI Agent
        ↓
Claude/Codex Skill or Approved MCP Client
        ↓
LeadSniper CLI Command Contract
        ↓
Printing Press Generated/Scaffolded Adapters
        ↓
FastAPI Client Layer
        ↓
LeadSniper Domain Services and Policy Engine
        ↓
Gemini / Tavily / Apify / DataForSEO / PageSpeed
        ↓
Convex or Supabase operational storage
        ↓
Qdrant semantic intelligence layer
        ↓
CRM / Marketplace / Outreach adapters
```
### Printing Press Architectural Role
CLI Printing Press is a build-time accelerator and interface generator, not the system of record. It may research documented APIs, identify useful command groupings, generate a token-efficient Go CLI, create an AI-readable skill, and optionally generate an MCP server. All generated artifacts must pass LeadSniperAI review, security, tenancy, compliance, idempotency, and testing gates before release.
The stable architectural boundary is the LeadSniper command contract. Provider-specific implementation details remain behind adapters so DataForSEO, Resend, Twilio, Unipile, Stripe, Clerk, Convex, or other integrations can change without breaking agent workflows.
## Architectural Principle
Version 1 should be a thin HTTP client over the existing FastAPI backend.
As stable logic emerges, move scoring, validation, evidence, and campaign orchestration into shared Python domain services consumed by both FastAPI and the CLI.
# 5. Proposed Repository Structure
```plain text
LeadSniper-3.0/
├── backend/
├── cli/
│   └── leadsniper_cli/
│       ├── main.py
│       ├── client.py
│       ├── config.py
│       ├── output.py
│       ├── state.py
│       ├── errors.py
│       └── commands/
│           ├── search.py
│           ├── import_data.py
│           ├── lookup.py
│           ├── lead.py
│           ├── intelligence.py
│           ├── audit.py
│           ├── qualify.py
│           ├── scoring.py
│           ├── evidence.py
│           ├── recommend.py
│           ├── campaign.py
│           ├── outreach.py
│           ├── batch.py
│           ├── queue.py
│           ├── export.py
│           └── system.py
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── subprocess/
│   └── true_backend/
├── SKILL.md
├── TEST.md
├── HARNESS.md
└── pyproject.toml
```
# 6. Top-Level Command Design
```plain text
leadsniper
├── config
├── search
├── import
├── lookup
├── lead
├── intelligence
├── audit
├── qualify
├── score
├── opportunity
├── evidence
├── recommend
├── campaign
├── outreach
├── batch
├── queue
├── export
└── system
```
## Global Options
```bash
leadsniper --help
leadsniper --version
leadsniper --json
leadsniper --quiet
leadsniper --verbose
leadsniper --api-url http://localhost:8000
leadsniper --profile production
leadsniper --request-id <id>
```
Every command must support structured output directly or through the global `--json` option.
# 7. Version 1 Command Catalogue
## 7.1 Configuration
```bash
leadsniper config init
leadsniper config show
leadsniper config validate
leadsniper config set api-url http://localhost:8000
leadsniper config profile use production
```
### Validation Requirements
Validate:
- Backend URL
- Gemini configuration
- Tavily configuration
- Apify configuration
- DataForSEO configuration when enabled
- Storage connection
- Required environment variables
- Outreach safety settings
## 7.2 Local Business Discovery
```bash
leadsniper search local \
  --niche "plumber" \
  --city "Vancouver, BC" \
  --focus growth \
  --limit 10 \
  --json
```
Supported initial focus values:
- `any`
- `crisis`
- `growth`
- `reactivation`
Suggested future filters:
- Minimum and maximum rating
- Minimum and maximum review count
- Website required
- Phone required
- Active-business requirement
- Geographic radius
- Exclusion list
- Result-source selection
## 7.3 Lead Enrichment
```bash
leadsniper lead enrich \
  --input lead.json \
  --provider gemini \
  --output enriched-lead.json
```
```bash
leadsniper lead enrich-batch \
  --input leads.json \
  --concurrency 5 \
  --output enriched.json
```
Providers:
- `gemini`
- `tavily`
- `apify`
- `all`
## 7.4 Contact and Social Discovery
```bash
leadsniper lead contacts \
  --input lead.json \
  --include email,phone,facebook,instagram,linkedin \
  --json
```
Every discovered contact must include:
- Value
- Source URL or source provider
- Discovery timestamp
- Confidence
- Verification status
- Evidence type
## 7.5 Company Intelligence
```bash
leadsniper intelligence company \
  --lead lead_123 \
  --include news,hiring,people,technology,competitors,growth,risk \
  --json
```
Additional commands:
```bash
leadsniper intelligence news lead_123
leadsniper intelligence hiring lead_123
leadsniper intelligence people lead_123
leadsniper intelligence competitors lead_123
leadsniper intelligence technology lead_123
leadsniper intelligence signals lead_123
```
## 7.6 SEO Audit
```bash
leadsniper audit seo \
  --lead lead_123 \
  --provider dataforseo \
  --location "Vancouver, British Columbia, Canada" \
  --language en \
  --include keywords,serp,competitors,local-pack
```
The current Gemini implementation must label its output as estimated and unverified.
```json
{
  "data_source": "gemini_estimate",
  "verified": false
}
```
## 7.7 Outreach Asset Generation
### Email Draft
```bash
leadsniper outreach email generate \
  --lead lead_123 \
  --offer "AI receptionist and missed-call recovery" \
  --problem "unanswered calls and weak online intake" \
  --case-study case-study.md \
  --output email.json
```
### Call Script
```bash
leadsniper outreach call-script \
  --lead lead_123 \
  --offer "AI receptionist" \
  --problem "missed inbound calls" \
  --json
```
### Safety Separation
```bash
leadsniper outreach email generate ...
leadsniper outreach email approve email_456
leadsniper outreach email send email_456
```
Sending must be disabled by default in Version 1.
## 7.8 Growth Recommendations
```bash
leadsniper recommend \
  --lead lead_123 \
  --categories reputation,reactivation,ads,automation \
  --json
```
## 7.9 Reverse Lookup
```bash
leadsniper lookup reverse \
  --input contacts.txt \
  --offer "AI receptionist and booking automation" \
  --output matched-leads.json
```
Single-contact aliases:
```bash
leadsniper lookup phone "+1-604-555-0123"
leadsniper lookup email "info@example.ca"
```
## 7.10 CSV Import
```bash
leadsniper import preview businesses.csv
```
```bash
leadsniper import csv businesses.csv \
  --name "Surrey Roofers July 2026" \
  --skip-duplicates \
  --validation standard \
  --enrich \
  --chunk-size 50
```
Version 1 should honour the current backend batch limit of 1,000 valid records and chunk sizes from 10 to 100.
## 7.11 Batch and Queue Management
```bash
leadsniper batch list
leadsniper batch show <batch-id>
leadsniper batch status <batch-id>
leadsniper batch leads <batch-id>
leadsniper batch errors <batch-id>
```
```bash
leadsniper queue stats
leadsniper queue list --status failed
```
Future backend work:
```bash
leadsniper batch retry <batch-id>
leadsniper batch cancel <batch-id>
leadsniper queue retry --status failed
```
## 7.12 Export
```bash
leadsniper export csv \
  --campaign campaign_123 \
  --minimum-score 70 \
  --output qualified-leads.csv
```
Formats:
- CSV
- JSON
- CRM payload
- Webhook payload
# 8. Proprietary Version 2 Commands
## 8.1 Eligibility Screening
```bash
leadsniper qualify eligibility \
  --lead lead_123 \
  --rules docs/scoring/eligibility-rules.md
```
Suggested output:
```json
{
  "eligible": true,
  "reasons": [
    "active local service business",
    "valid business website",
    "public telephone number"
  ],
  "disqualifiers": []
}
```
## 8.2 Website Revenue Infrastructure Audit
```bash
leadsniper audit website \
  --url "https://example.ca" \
  --include hero,cta,forms,mobile,trust,booking,chat
```
Subcommands:
```bash
leadsniper audit hero --url <url>
leadsniper audit conversion --url <url>
leadsniper audit mobile --url <url>
leadsniper audit intake --url <url>
leadsniper audit trust --url <url>
leadsniper audit pagespeed --url <url>
```
Observable audit dimensions:
- Hero message clarity
- Primary CTA visibility
- Mobile click-to-call
- Contact-form availability
- Online booking
- After-hours intake
- Trust signals
- Reviews and testimonials
- Page speed
- Accessibility
- Broken forms or links
- Phone-only intake risk
## 8.3 AI Employee Fit Score
```bash
leadsniper score ai-employee \
  --lead lead_123 \
  --use website-audit.json \
  --use enrichment.json
```
Initial score components:
- Missed-call risk
- Booking friction
- Intake complexity
- Review opportunity
- Business capacity
- After-hours demand
- Lead-value potential
- Automation readiness
## 8.4 Opportunity Classification
```bash
leadsniper score opportunity \
  --lead lead_123 \
  --model local-service-growth-v1
```
Initial categories:
- `fixable-crisis`
- `hidden-gem`
- `sleeping-giant`
- `reputation-rescue`
- `intake-friction`
- `missed-call-opportunity`
- `seo-growth-opportunity`
- `ai-employee-fit`
- `not-qualified`
## 8.5 Evidence Management
```bash
leadsniper verify lead_123
leadsniper evidence list lead_123
leadsniper evidence inspect evidence_456
leadsniper evidence refresh lead_123
```
Evidence object:
```json
{
  "claim": "No visible online booking option",
  "source_url": "https://example.ca/contact",
  "observed_at": "2026-07-25T10:30:00-07:00",
  "evidence_type": "website_observation",
  "confidence": 0.98
}
```
# 9. Campaign Orchestration
## Campaign Creation
```bash
leadsniper campaign create \
  --name "Vancouver Plumber AI Receptionist" \
  --niche plumber \
  --location "Vancouver, BC" \
  --offer ai-receptionist \
  --minimum-score 70
```
## Stage Commands
```bash
leadsniper campaign discover <campaign-id>
leadsniper campaign enrich <campaign-id>
leadsniper campaign audit <campaign-id>
leadsniper campaign score <campaign-id>
leadsniper campaign verify <campaign-id>
leadsniper campaign generate-outreach <campaign-id>
leadsniper campaign export <campaign-id>
```
## Orchestration Command
```bash
leadsniper campaign run campaign_123 \
  --stages discover,enrich,audit,score,verify \
  --stop-before outreach \
  --json
```
## State Requirements
Campaign runs must be:
- Resumable
- Idempotent where practical
- Auditable
- Timestamped
- Retryable by stage
- Protected from duplicate enrichment charges
# 10. Structured Output Standard
Every command should return a shared response envelope.
```json
{
  "success": true,
  "command": "search.local",
  "request_id": "req_123",
  "started_at": "2026-07-25T10:00:00-07:00",
  "completed_at": "2026-07-25T10:00:12-07:00",
  "data": {},
  "warnings": [],
  "errors": [],
  "provenance": [],
  "cost": {
    "currency": "CAD",
    "estimated": true,
    "amount": 0
  }
}
```
## Exit Codes
- `0`: Success
- `1`: General failure
- `2`: Invalid CLI arguments
- `3`: Configuration error
- `4`: Authentication or authorization error
- `5`: Upstream provider failure
- `6`: Validation failure
- `7`: Partial success
- `8`: Safety or compliance block
- `9`: Rate limit or quota reached
# 11. Security and Compliance Requirements
## Mandatory Before Production
- Rotate any previously exposed keys.
- Remove committed environment files and secrets from history where required.
- Fix unresolved TypeScript build errors.
- Add test coverage.
- Implement structured logging.
- Add CI/CD checks.
- Restrict provider keys to the backend.
- Redact credentials from logs and JSON output.
- Disable outbound sending by default.
- Require explicit approval for destructive or external actions.
## Outreach Controls
- `generate` creates drafts only.
- `approve` records human or authorized-system approval.
- `send` requires an explicit permission scope.
- Maintain suppression and do-not-contact lists.
- Record source and lawful-use basis where applicable.
- Implement per-channel rate limits.
- Preserve audit logs.
# 12. CLI-Anything Deliverables
## Agent Harness
A Click-based Python package exposing deterministic command groups.
## [SKILL.md](http://SKILL.md)
Must include:
- YAML frontmatter
- Tool purpose
- Installation
- Authentication and configuration
- Command groups
- JSON schema guidance
- Safe operating rules
- Common workflows
- Error recovery
- Token-efficient usage
- Examples for agents
## [TEST.md](http://TEST.md)
Must include:
- Test plan
- Unit cases
- API integration cases
- Native E2E cases
- True-backend validation
- CLI subprocess tests
- Live results
- Known limitations
## [HARNESS.md](http://HARNESS.md)
Must document:
- Domain model
- Endpoint-to-command mapping
- State model
- Undo or compensating-action strategy
- Output contract
- Provider abstraction
- Security boundaries
- Agent approval rules
# 13. Testing Strategy
## Layer 1 — Unit Tests
Test:
- Argument validation
- Configuration loading
- JSON serialization
- Scoring functions
- Evidence normalization
- Duplicate handling
- Exit-code mapping
- Redaction
## Layer 2 — Integration Tests
Test the CLI client against a mocked FastAPI backend.
Required endpoint coverage:
- Search
- Enrich
- Social enrich
- SEO audit
- Email generation
- Script generation
- Recommendations
- Reverse lookup
- Batch import
- Batch status
- Queue statistics
- Tavily enrichment
- Apify enrichment
## Layer 3 — CLI Subprocess Tests
Run the installed command as an actual subprocess and verify:
- Command is available on PATH.
- Help text renders.
- JSON output parses.
- Exit codes are correct.
- Errors do not leak secrets.
- Files are written to the requested path.
## Layer 4 — True Backend Tests
Verify real provider behavior in an isolated environment:
- Gemini returns parseable records.
- Tavily returns attributed intelligence.
- Apify returns expected fields.
- DataForSEO returns live keyword and SERP data.
- PageSpeed returns valid diagnostics.
- CRM export payload validates.
# 14. Implementation Phases
## Phase 0 — Repository Hardening
- Rotate and secure keys.
- Remove secrets from tracked files.
- Resolve build errors.
- Create baseline tests.
- Confirm FastAPI endpoint health.
- Document current API schemas.
## Phase 1 — CLI Foundation
- Create Python package.
- Add Click root command.
- Implement configuration profiles.
- Implement HTTP client.
- Add shared JSON response envelope.
- Add error and exit-code handling.
- Add `system doctor`.
## Phase 2 — Existing Endpoint Wrappers
Implement:
- `search local`
- `lead enrich`
- `lead contacts`
- `intelligence company`
- `audit seo`
- `outreach email generate`
- `outreach call-script`
- `recommend`
- `lookup reverse`
- `import csv`
- `batch status`
- `queue stats`
- `export csv`
## Phase 3 — Evidence and Qualification
- Eligibility rules
- Evidence model
- Verification commands
- Confidence scoring
- Source attribution
- Duplicate and identity resolution
## Phase 4 — Proprietary Auditing and Scoring
- Website revenue-infrastructure audit
- PageSpeed integration
- AI Employee fit score
- Opportunity classification
- Recommendation mapping
## Phase 5 — Campaign Orchestration
- Campaign state machine
- Resumable stages
- Cost controls
- Retry logic
- Approval gates
- Export routing
## Phase 6 — Agent Documentation and Publishing
- Complete `SKILL.md`.
- Complete `TEST.md` with live results.
- Complete `HARNESS.md`.
- Package with `pyproject.toml`.
- Install to PATH.
- Publish internally or to CLI-Hub when production-ready.
# 15. Minimum Viable Release
The MVP should contain these commands:
```bash
leadsniper config validate
leadsniper system doctor
leadsniper search local
leadsniper import csv
leadsniper lead enrich
leadsniper lead contacts
leadsniper intelligence company
leadsniper audit seo
leadsniper outreach email generate
leadsniper outreach call-script
leadsniper recommend
leadsniper lookup reverse
leadsniper batch status
leadsniper export csv
```
# 16. Acceptance Criteria
The MVP is accepted when:
- `leadsniper --help` works after package installation.
- All MVP commands support valid JSON output.
- The CLI can connect to a configured FastAPI instance.
- Provider failures return consistent error envelopes.
- Secrets are redacted from output and logs.
- Search results can be enriched and exported.
- Email and call-script commands create drafts without sending.
- Batch progress can be inspected.
- At least 60% automated test coverage is reached for the CLI package.
- Every public command has subprocess testing.
- `SKILL.md` includes at least three complete agent workflows.
- `TEST.md` records actual test results.
- A full local-business workflow can complete without using the React interface.
# 17. Suggested Agent Workflows
## Workflow A — Find and Qualify Local Businesses
```bash
leadsniper search local \
  --niche "roofing contractor" \
  --city "Surrey, BC" \
  --focus growth \
  --json > leads.json

leadsniper lead enrich-batch \
  --input leads.json \
  --provider all \
  --output enriched.json

leadsniper export csv \
  --input enriched.json \
  --output surrey-roofing-opportunities.csv
```
## Workflow B — Audit One Business
```bash
leadsniper audit website --url "https://example.ca" --json > website-audit.json
leadsniper audit seo --lead lead_123 --provider dataforseo --json > seo-audit.json
leadsniper score ai-employee --lead lead_123 --use website-audit.json --json
```
## Workflow C — Create Reviewable Outreach
```bash
leadsniper verify lead_123
leadsniper recommend --lead lead_123 --json
leadsniper outreach email generate --lead lead_123 --offer "AI receptionist" --output draft.json
```
# 18. Dependencies and Risks
## Dependencies
- Healthy FastAPI backend
- Provider credentials
- Stable request and response models
- Persistent storage for campaigns and evidence
- DataForSEO integration for verified keyword and SERP intelligence
- PageSpeed or browser auditing for observable website diagnostics
## Principal Risks
- Provider data inconsistency
- Hallucinated or weakly attributed enrichment
- Duplicate businesses
- Unauthorized data retention
- Accidental outreach sending
- API-cost escalation
- Long-running campaign failures
- Current in-memory batch storage
- Insufficient production tests
## Mitigations
- Provider adapters with normalized schemas
- Evidence and confidence requirements
- Identity-resolution layer
- Cost budgets and per-run caps
- Approval gates
- Resumable stages
- Persistent job storage
- Structured observability
# 19. Open Decisions
1. Use Convex or Supabase as the authoritative operational store?
2. Will the CLI call FastAPI only, or may it run domain services locally?
3. Should the first package be private, GitHub-distributed, or published to PyPI?
4. Which source becomes authoritative for local-business discovery?
5. Which CRM receives the first export adapter?
6. Should campaign orchestration use native workers, Celery, n8n, or Vercel Workflow?
7. Which actions require human approval versus policy-based automated approval?
## Working Assumptions
- FastAPI remains the initial execution layer.
- Supabase or Convex replaces current in-memory batch state before production.
- Qdrant is supplementary semantic storage, not the transactional source of truth.
- Outbound messages remain drafts in the MVP.
- DataForSEO becomes the preferred verified SEO-data provider.
# 20. Recommended Immediate Next Actions
1. Create the `cli/leadsniper_cli` package skeleton.
2. Add `config validate` and `system doctor` first.
3. Map every FastAPI endpoint to a typed CLI client method.
4. Implement `search local`, `lead enrich`, and `export csv` as the first end-to-end vertical slice.
5. Add the shared JSON envelope and exit-code rules.
6. Add unit and subprocess tests before adding more commands.
7. Draft `SKILL.md` alongside implementation rather than after development.
8. Replace in-memory batch state before enabling multi-step campaigns.
# Definition of Done
LeadSniperAI CLI is complete when an authorized agent can reliably discover, enrich, audit, qualify, verify, and export local business opportunities through deterministic commands, with machine-readable output, supporting evidence, controlled costs, test-backed reliability, and no dependency on fragile dashboard navigation.
<page url="https://app.notion.com/p/3a89e94cf0a4819ca43ad76e097f2473">LeadSniperAI Workflow & Search Results Improvement Plan</page>
# 18. Incremental Improvement Addendum — v1.1
*Last updated: July 25, 2026*
This addendum strengthens implementation precision without replacing the original PRD. It converts the command catalogue into enforceable contracts and clarifies sequencing, ownership boundaries, cost controls, and production gates.
## 18.1 Product Decisions
<table header-row="true">
<tr>
<td>Decision</td>
<td>Selected approach</td>
<td>Rationale</td>
<td>Consequence</td>
</tr>
<tr>
<td>CLI framework</td>
<td>Python Click</td>
<td>Aligns with CLI-Anything and the FastAPI backend</td>
<td>Shared Python models and services can be reused</td>
</tr>
<tr>
<td>Version 1 integration</td>
<td>Thin HTTP client over FastAPI</td>
<td>Fastest path with the least duplicated logic</td>
<td>Backend availability is required for most commands</td>
</tr>
<tr>
<td>Default output</td>
<td>Human-readable terminal output</td>
<td>Better operator experience</td>
<td>`--json` remains mandatory for agents</td>
</tr>
<tr>
<td>Agent output</td>
<td>Stable JSON response envelope</td>
<td>Deterministic parsing and orchestration</td>
<td>Breaking schema changes require versioning</td>
</tr>
<tr>
<td>Outreach</td>
<td>Generate and approve separately from send</td>
<td>Limits accidental or non-compliant outreach</td>
<td>Sending remains disabled by default</td>
</tr>
<tr>
<td>Primary operational store</td>
<td>Convex or Supabase selected during implementation spike</td>
<td>Existing architecture has not finalized one authority</td>
<td>CLI adapters must not couple domain models to either vendor</td>
</tr>
<tr>
<td>Semantic store</td>
<td>Qdrant as a complementary index</td>
<td>Suitable for similarity and retrieval, not transactions</td>
<td>Lead and campaign state remains in the operational database</td>
</tr>
<tr>
<td>Provider strategy</td>
<td>Adapter interface with configurable priority and fallback</td>
<td>Reduces vendor lock-in and upstream failures</td>
<td>Every result must retain source provenance</td>
</tr>
</table>
## 18.2 Endpoint-to-Command Contract
Version 1 should map the existing backend to CLI commands before adding new business logic.
<table>
<tr>
<td>CLI command</td>
<td>FastAPI capability</td>
<td>Method</td>
<td>Initial status</td>
<td>Notes</td>
</tr>
<tr>
<td>---</td>
<td>---</td>
<td>---:</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>`search local`</td>
<td>`/search`</td>
<td>POST</td>
<td>Existing</td>
<td>Accepts niche, city, focus</td>
</tr>
<tr>
<td>`lead enrich`</td>
<td>`/enrich`</td>
<td>POST</td>
<td>Existing</td>
<td>Gemini-based enrichment</td>
</tr>
<tr>
<td>`lead contacts`</td>
<td>`/social-enrich`</td>
<td>POST</td>
<td>Existing</td>
<td>Public social and contact discovery</td>
</tr>
<tr>
<td>`lead enrich --provider apify`</td>
<td>`/enrich-apify`</td>
<td>POST</td>
<td>Existing/partial</td>
<td>Normalize field names before release</td>
</tr>
<tr>
<td>`intelligence company`</td>
<td>`/enrich-tavily-full`</td>
<td>POST</td>
<td>Existing</td>
<td>Preferred Tavily intelligence endpoint</td>
</tr>
<tr>
<td>`audit seo`</td>
<td>`/seo-audit`</td>
<td>POST</td>
<td>Existing</td>
<td>Must label Gemini values as estimates</td>
</tr>
<tr>
<td>`outreach email generate`</td>
<td>`/generate-email`</td>
<td>POST</td>
<td>Existing</td>
<td>Draft only</td>
</tr>
<tr>
<td>`outreach call-script`</td>
<td>`/generate-script`</td>
<td>POST</td>
<td>Existing</td>
<td>Draft only</td>
</tr>
<tr>
<td>`recommend`</td>
<td>`/generate-recommendations`</td>
<td>POST</td>
<td>Existing</td>
<td>Returns structured recommendations</td>
</tr>
<tr>
<td>`lookup reverse`</td>
<td>`/reverse-lookup`</td>
<td>POST</td>
<td>Existing</td>
<td>Evidence and confidence must be added</td>
</tr>
<tr>
<td>`import csv`</td>
<td>`/import-batch`</td>
<td>POST</td>
<td>Existing/partial</td>
<td>Current persistence is in-memory</td>
</tr>
<tr>
<td>`import preview`</td>
<td>`/import-batch/preview`</td>
<td>POST</td>
<td>Existing</td>
<td>Validate before paid enrichment</td>
</tr>
<tr>
<td>`batch leads`</td>
<td>`/batch/{batch_id}/leads`</td>
<td>GET</td>
<td>Existing</td>
<td>Pagination supported</td>
</tr>
<tr>
<td>`batch errors`</td>
<td>Batch error endpoint</td>
<td>GET</td>
<td>Existing/mock</td>
<td>Requires persistent implementation</td>
</tr>
<tr>
<td>`queue stats`</td>
<td>`/enrichment-queue/stats`</td>
<td>GET</td>
<td>Existing/mock</td>
<td>Replace mock response before production</td>
</tr>
</table>
### Contract rule
Each wrapper must preserve the upstream HTTP status, map errors to the documented CLI exit code, attach a request ID, and emit a stable normalized response even when individual providers return different field names.
## 18.3 Canonical Lead Record
All providers and imports must normalize into one internal schema before scoring or export.
```json
{
  "schema_version": "1.0",
  "lead_id": "lead_01H...",
  "tenant_id": "tenant_123",
  "campaign_id": "campaign_123",
  "business": {
    "name": "Example Plumbing Ltd.",
    "legal_name": null,
    "niche": "plumber",
    "status": "active",
    "website": "https://example.ca",
    "phone": "+16045550123",
    "email": "info@example.ca"
  },
  "location": {
    "city": "Vancouver",
    "region": "BC",
    "country": "CA",
    "postal_code": null,
    "latitude": null,
    "longitude": null
  },
  "reputation": {
    "rating": 4.4,
    "review_count": 72,
    "source": "provider_name",
    "observed_at": "2026-07-25T10:30:00-07:00"
  },
  "contacts": [],
  "social_profiles": [],
  "audits": [],
  "scores": [],
  "evidence": [],
  "provenance": [],
  "created_at": "2026-07-25T10:30:00-07:00",
  "updated_at": "2026-07-25T10:30:00-07:00"
}
```
### Required normalization rules
- Phone numbers use E.164 when possible.
- URLs are canonicalized and stripped of tracking parameters.
- Missing values use `null`, not invented placeholders.
- Guessed email patterns are stored as `candidate`, never `verified`.
- Every externally sourced field retains provider, source URL where available, timestamp, and confidence.
- Raw provider payloads may be retained for audit purposes but must not become the canonical API contract.
## 18.4 Provider Adapter Interface
Every external service should implement a shared adapter contract:
```python
class ProviderAdapter(Protocol):
    name: str

    async def healthcheck(self) -> ProviderHealth: ...
    async def estimate_cost(self, request: ProviderRequest) -> CostEstimate: ...
    async def execute(self, request: ProviderRequest) -> ProviderResult: ...
    async def normalize(self, result: ProviderResult) -> NormalizedResult: ...
```
### Initial provider roles
<table header-row="true">
<tr>
<td>Provider</td>
<td>Primary role</td>
<td>Fallback or limitation</td>
</tr>
<tr>
<td>Gemini</td>
<td>Broad research, synthesis, copy generation</td>
<td>Do not treat model-generated metrics as verified facts</td>
</tr>
<tr>
<td>Tavily</td>
<td>Company intelligence and web research</td>
<td>Preserve source URLs and publication dates</td>
</tr>
<tr>
<td>Apify</td>
<td>Structured extraction where authorized</td>
<td>Actor dependency and usage cost require controls</td>
</tr>
<tr>
<td>DataForSEO</td>
<td>Verified SEO, SERP, keyword and local-search data</td>
<td>Preferred source for quantitative SEO metrics</td>
</tr>
<tr>
<td>PageSpeed Insights</td>
<td>Performance and Core Web Vitals</td>
<td>Audit only; not a complete conversion diagnosis</td>
</tr>
</table>
### Fallback policy
1. Use the campaign's configured primary provider.
2. Retry transient failures with bounded exponential backoff.
3. Switch providers only when the command explicitly permits fallback.
4. Mark fallback results in provenance.
5. Never silently replace verified quantitative data with an AI estimate.
6. Stop when the campaign cost ceiling would be exceeded.
## 18.5 Idempotency, Deduplication, and Cost Controls
### Idempotency keys
Paid and mutating commands must accept or generate an idempotency key:
```bash
leadsniper campaign run campaign_123 \
  --idempotency-key run_2026_07_25_vancouver_plumbers
```
The system must not repeat a paid enrichment when the same lead, provider, operation, and evidence freshness window have already completed successfully.
### Lead identity hierarchy
Deduplicate using the strongest available combination:
1. Provider place or business identifier.
2. Canonical domain plus normalized phone.
3. Canonical domain plus normalized business name and city.
4. Normalized phone plus business name and city.
5. Fuzzy name and address match, flagged for review.
### Cost guardrails
```bash
leadsniper campaign run campaign_123 \
  --max-cost-cad 50 \
  --max-cost-per-lead-cad 1.25 \
  --stop-on-budget
```
Required controls:
- Preflight estimated cost.
- Per-provider usage accounting.
- Campaign and tenant budgets.
- Warning threshold at 75% of budget.
- Hard stop at 100% unless an authorized override is supplied.
- Separate estimated and actual cost values.
## 18.6 Multi-Tenant and Authorization Model
Every persistent object must include `tenant_id`. Commands must resolve tenant context from the authenticated profile rather than accepting arbitrary tenant IDs by default.
Suggested roles:
<table header-row="true">
<tr>
<td>Role</td>
<td>Permissions</td>
</tr>
<tr>
<td>`viewer`</td>
<td>Read leads, campaigns, evidence, reports</td>
</tr>
<tr>
<td>`analyst`</td>
<td>Run discovery, audits, enrichment and scoring</td>
</tr>
<tr>
<td>`campaign_manager`</td>
<td>Create campaigns, approve exports and outreach drafts</td>
</tr>
<tr>
<td>`outreach_operator`</td>
<td>Send approved communications through enabled channels</td>
</tr>
<tr>
<td>`admin`</td>
<td>Configure providers, budgets, users and policy</td>
</tr>
</table>
High-risk operations require both role permission and explicit command confirmation or a non-interactive approval token.
## 18.7 Campaign State Machine
```plain text
DRAFT
  ↓
READY
  ↓
DISCOVERING
  ↓
ENRICHING
  ↓
AUDITING
  ↓
SCORING
  ↓
VERIFYING
  ↓
QUALIFIED
  ↓
OUTREACH_DRAFTED
  ↓
APPROVED
  ↓
EXPORTED or SENT
```
Terminal states:
- `COMPLETED`
- `CANCELLED`
- `FAILED`
- `BUDGET_BLOCKED`
- `COMPLIANCE_BLOCKED`
Every transition must record actor, timestamp, previous state, new state, reason, and request ID.
## 18.8 Freshness and Evidence Policy
Suggested default freshness windows:
<table>
<tr>
<td>Evidence type</td>
<td>Default freshness</td>
</tr>
<tr>
<td>---</td>
<td>---:</td>
</tr>
<tr>
<td>Website availability and CTA audit</td>
<td>14 days</td>
</tr>
<tr>
<td>PageSpeed audit</td>
<td>7 days</td>
</tr>
<tr>
<td>Contact information</td>
<td>30 days</td>
</tr>
<tr>
<td>Business operating status</td>
<td>30 days</td>
</tr>
<tr>
<td>Reviews and rating</td>
<td>14 days</td>
</tr>
<tr>
<td>SEO keyword and SERP data</td>
<td>30 days</td>
</tr>
<tr>
<td>Hiring and news signals</td>
<td>14 days</td>
</tr>
<tr>
<td>Decision-maker information</td>
<td>60 days</td>
</tr>
</table>
Commands should support:
```bash
leadsniper evidence refresh lead_123 --only stale
leadsniper audit website --lead lead_123 --max-age-days 14
```
## 18.9 Configuration Precedence
Configuration should resolve in this order, from highest to lowest precedence:
1. Explicit command flags.
2. Environment variables.
3. Named CLI profile.
4. Project-level configuration file.
5. User-level configuration file.
6. Built-in safe defaults.
Suggested files:
```plain text
./leadsniper.toml
~/.config/leadsniper/config.toml
```
Secrets must remain in environment variables or an approved secret manager and must never be written into normal profile files.
## 18.10 Versioning and Compatibility
- CLI version follows semantic versioning.
- JSON envelopes include `schema_version`.
- Breaking command or schema changes require a major version.
- Deprecated flags remain functional for at least one minor release where practical.
- `leadsniper system compatibility` reports CLI, backend API, schema, and provider-adapter compatibility.
```bash
leadsniper system compatibility --json
```
## 18.11 Delivery Plan as Independently Testable Work Packages
### Phase 0 — Production blockers
1. Rotate exposed credentials and remove committed secrets.
2. Resolve TypeScript build failures.
3. Replace mock batch and queue persistence or clearly disable those commands.
4. Add CI checks for backend tests, CLI tests, linting, type checking, and secret scanning.
### Phase 1 — CLI foundation
1. Create Click root command and global options.
2. Implement configuration profiles and `config validate`.
3. Implement HTTP client, request IDs, retries, timeouts, and error mapping.
4. Implement human and JSON output renderers.
5. Add subprocess tests for `--help`, `--version`, exit codes, and valid JSON.
### Phase 2 — Existing endpoint wrappers
1. `search local`.
2. `lead enrich` and `lead contacts`.
3. `intelligence company`.
4. `audit seo`.
5. Outreach draft and recommendation commands.
6. CSV import, preview, batch reads, and export.
### Phase 3 — Canonical data and evidence
1. Canonical lead schema and provider normalization.
2. Provenance and evidence models.
3. Deduplication and freshness policies.
4. Persistent campaign and job records.
5. Cost estimation and accounting.
### Phase 4 — Proprietary intelligence
1. Eligibility rules engine.
2. Website revenue-infrastructure audit.
3. AI Employee fit score.
4. Opportunity classification.
5. Verification and evidence refresh.
### Phase 5 — Orchestration and integrations
1. Resumable campaign state machine.
2. Convex or Supabase adapter selection and implementation.
3. Qdrant semantic indexing.
4. CRM and marketplace exports.
5. Approval-gated Resend, Twilio, and Unipile integrations.
## 18.12 Release Gates
### Alpha gate
- Six core commands execute against a development backend.
- Every command supports `--json`.
- Stable error envelope and exit-code tests pass.
- No outbound sending commands are active.
### Beta gate
- All Version 1 wrappers implemented.
- Canonical lead normalization operational.
- Persistent campaign and batch state available.
- Unit and integration coverage reaches at least 60% for new CLI code.
- Secret scan and dependency audit pass.
### Production gate
- No critical or high-severity unresolved security findings.
- True-backend tests cover all paid providers enabled in production.
- Cost limits, idempotency, audit logs, tenant isolation, and approval gates verified.
- Structured logs and monitoring deployed.
- Recovery procedure tested for interrupted campaign runs.
- `SKILL.md`, `TEST.md`, operator runbook, and release notes completed.
## 18.13 Additional Acceptance Tests
```gherkin
Scenario: Paid enrichment is not repeated
  Given a lead was enriched successfully with Tavily inside the freshness window
  When the same command is rerun with the same idempotency key
  Then the previous result is returned
  And no additional provider charge is incurred
```
```gherkin
Scenario: Estimated SEO data is not represented as verified
  Given DataForSEO is unavailable
  And Gemini fallback is permitted
  When an SEO audit completes
  Then the result is marked as estimated
  And verified is false
  And the fallback provider is recorded in provenance
```
```gherkin
Scenario: Campaign stops at its cost ceiling
  Given a campaign maximum cost of CAD 50
  When the next provider operation would exceed CAD 50
  Then the operation is not executed
  And the campaign enters BUDGET_BLOCKED
  And the CLI exits with a safety or quota code
```
```gherkin
Scenario: Sending requires explicit approval
  Given an outreach email draft exists
  And no approval record exists
  When an agent invokes the send command
  Then sending is blocked
  And the CLI returns exit code 8
```
## 18.14 Implementation Questions to Resolve During the First Architecture Spike
1. Will Convex or Supabase be the authoritative operational store for Version 1?
2. Should the CLI run only as an HTTP client, or also support an embedded local mode for tests and offline scoring?
3. Which local-business discovery source is approved as the production primary source?
4. What evidence may be persisted under each provider's terms?
5. Which outreach channels will be enabled in the first commercial release?
6. What constitutes a verified email, phone number, operating status, and decision maker?
7. What is the initial maximum provider cost per qualified opportunity?
8. Which scoring rules require human override, and which may be fully deterministic?
## 18.15 Changelog
### v1.1 — July 25, 2026
- Added endpoint-to-command implementation contract.
- Added canonical lead record and normalization rules.
- Added provider adapter and fallback policy.
- Added idempotency, deduplication, and cost controls.
- Added multi-tenant authorization model.
- Added campaign state machine and evidence freshness defaults.
- Added configuration precedence and compatibility rules.
- Converted implementation phases into independently testable delivery packages.
- Added alpha, beta, and production release gates.
- Added implementation-specific acceptance tests and architecture questions.
# Printing Press Integration Addendum
## Purpose
Integrate [CLI Printing Press](https://github.com/mvanhorn/cli-printing-press) into the LeadSniperAI CLI delivery process as an agent-native interface generator and research accelerator.
Printing Press should reduce the time required to understand external APIs, define command surfaces, scaffold adapters, produce agent instructions, and expose selected workflows through MCP. It must not bypass LeadSniperAI's domain services, approval gates, tenant isolation, consent rules, billing controls, or audit requirements.
## Operating Model
```plain text
API documentation / existing service / permitted website interface
        ↓
Printing Press research and command discovery
        ↓
Generated Go CLI scaffold + SKILL.md + optional MCP server
        ↓
LeadSniper engineering review and hardening
        ↓
LeadSniper command contract and policy controls
        ↓
Production release through CI/CD
```
## Recommended Use Cases
### Phase 1 — DataForSEO / SGI Pilot
Generate and harden a narrow `leadsniper-sgi` interface for:
- Keyword discovery
- SERP retrieval
- SERP-overlap clustering
- Competitor and content-gap analysis
- Opportunity scoring
- Research brief creation
Example compound command:
```bash
leadsniper-sgi market analyze \
  --vertical "alternative mortgage" \
  --location "British Columbia, Canada" \
  --domain mortgagesbydenniseng.ca \
  --json
```
### Phase 2 — Resend Draft and Delivery Adapter
Use Printing Press to scaffold low-risk email operations:
- Validate configuration
- Create email drafts
- Render templates
- Send approved transactional messages
- Retrieve delivery status
Sending remains disabled unless an explicit approval state and tenant-authorized credential are present.
### Phase 3 — Lead Lifecycle Commands
Extend the stable LeadSniper command vocabulary:
```bash
leadsniper lead create
leadsniper lead enrich
leadsniper lead verify
leadsniper lead score
leadsniper lead package
leadsniper lead distribute
```
### Phase 4 — Multi-Channel Messaging
Add controlled adapters for Twilio, Resend, and Unipile only after consent, channel availability, throttling, duplicate prevention, suppression lists, and human approval are enforced.
### Phase 5 — Marketplace and Billing
Generate Stripe and marketplace adapters only after idempotency keys, entitlement checks, purchase limits, refunds, dispute logging, and immutable transaction audit records are complete.
## Generated Artifact Policy
Printing Press outputs are drafts requiring review. Each generated integration must include:
- Source API and documentation references
- Generated command inventory
- Authentication model
- Required scopes and permissions
- Input and output schemas
- Error and exit-code mapping
- Rate-limit behaviour
- Retry and idempotency strategy
- Secrets-handling review
- Tenant-isolation review
- Compliance and consent review
- Unit, integration, subprocess, and true-backend tests
- Generated `SKILL.md`
- Generated or updated `TEST.md`
- Optional MCP exposure decision
- Named engineering owner and approval status
## Repository Refactor
Recommended target structure:
```plain text
LeadSniper-3.0/
├── backend/
├── cli/
│   ├── contracts/
│   │   ├── command-schema/
│   │   ├── response-envelope/
│   │   └── exit-codes/
│   ├── generated/
│   │   ├── dataforseo/
│   │   ├── resend/
│   │   ├── twilio/
│   │   ├── unipile/
│   │   └── stripe/
│   ├── internal/
│   │   ├── policy/
│   │   ├── tenancy/
│   │   ├── audit/
│   │   ├── approvals/
│   │   └── adapters/
│   └── cmd/leadsniper/
├── skills/
│   ├── leadsniper/SKILL.md
│   └── provider-skills/
├── mcp/
│   └── approved-tools/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── subprocess/
│   ├── contract/
│   └── true_backend/
├── printing-press/
│   ├── manifests/
│   ├── research/
│   ├── generation-config/
│   └── review-records/
├── TEST.md
└── HARNESS.md
```
Generated code must remain separated from LeadSniper-owned policy and domain code. This makes regeneration possible without overwriting safety controls or business rules.
## Command Design Rules for Printing Press
1. Prefer business-level compound commands over one command per API endpoint.
2. Keep command names stable and provider-neutral where practical.
3. Return the shared LeadSniper response envelope.
4. Preserve provenance, cost, timestamps, confidence, warnings, and partial-success state.
5. Require explicit approval for external side effects.
6. Default to read-only or draft-producing behaviour.
7. Never expose unrestricted provider administration through MCP.
8. Support `--dry-run`, `--json`, `--request-id`, and tenant context for side-effecting commands.
9. Avoid placing secrets in arguments, terminal history, logs, or output.
10. Ensure each compound command is resumable and idempotent where practical.
## MCP Exposure Policy
Printing Press may generate an MCP server, but only approved LeadSniper commands should be exposed.
### Safe Default MCP Tools
- Search and retrieve lead intelligence
- Run audits
- Read evidence
- Generate drafts
- Preview campaigns
- Validate configuration without revealing secrets
### Restricted MCP Tools
- Send email or SMS
- Initiate calls
- Publish marketplace listings
- Charge or refund payments
- Change Clerk organizations or roles
- Modify tenant configuration
- Export personal information
Restricted tools require explicit user intent, role-based authorization, tenant validation, approval records, and audit logging.
## Build and Review Workflow
```plain text
1. Select a narrow provider or workflow.
2. Record the official documentation and permitted access method.
3. Run Printing Press research and generation.
4. Review command names and consolidate endpoint-level commands.
5. Move policy and domain behaviour into LeadSniper-owned modules.
6. Add structured response envelopes and exit codes.
7. Add authentication, tenancy, consent, approval, and audit controls.
8. Add mocked and true-backend tests.
9. Generate and review SKILL.md and optional MCP definitions.
10. Release behind a feature flag.
11. Monitor errors, cost, latency, and agent success rate.
12. Promote only after acceptance criteria are met.
```
## Acceptance Criteria
A Printing Press-generated integration is production-ready only when:
- At least 95% of documented command contract tests pass consistently.
- No secrets appear in logs, subprocess output, fixtures, or generated documentation.
- Tenant context is required and validated for tenant-bound operations.
- Side effects support dry-run or preview where technically possible.
- Duplicate requests do not create duplicate sends, charges, listings, or enrichment costs.
- Every material claim includes provenance or an explicit estimated/unverified label.
- The generated skill accurately describes permissions, safe defaults, examples, and failure recovery.
- The optional MCP server exposes only approved commands.
- A human can reproduce the core workflow without relying on hidden agent context.
## Success Metrics
Track:
- Time from API selection to first working CLI command
- Engineering hours saved compared with manual scaffolding
- Agent tool-call success rate
- Average tokens required per completed workflow
- Percentage of commands returning valid response envelopes
- Contract-test pass rate
- Number of manual interventions per campaign
- Duplicate-action rate
- Provider-cost variance versus estimate
- Security or compliance exceptions
- Time required to regenerate an adapter after an upstream API change
## Key Decision
Adopt CLI Printing Press as the preferred generator for new external-service CLI adapters, beginning with a DataForSEO/SGI pilot. Maintain the LeadSniperAI command contract, domain services, safety controls, and production tests as the authoritative layer. Generated code is accelerative infrastructure, not trusted business logic.
## Changelog
- 2026-07-26: Refactored the CLI PRD to introduce Printing Press as the build-time research, Go CLI scaffolding, agent-skill generation, and optional MCP layer. Added phased adoption, generated-code separation, MCP restrictions, acceptance criteria, and success metrics.
# 21. Printing Press GTM Strategy Engine Addendum
## Purpose
Extend the LeadSniperAI CLI from lead discovery and qualification into an evidence-driven go-to-market operating system. The Printing Press library will provide reusable GTM strategy patterns, channel playbooks, campaign templates, measurement frameworks, and integration recipes that LeadSniperAI can adapt to each market, offer, account segment, and lead opportunity.
Printing Press strategies are treated as versioned reference playbooks. LeadSniperAI remains responsible for evidence collection, market fit, recommendation logic, compliance, approvals, execution state, and outcome measurement.
## Strategic Outcome
An authorized user or agent can move from a qualified lead or market opportunity to a reviewable GTM plan through a deterministic command sequence:
```plain text
Evidence → Segment → Problem → Offer → Positioning → Channel Mix → Campaign → Execution → Attribution → Learning
```
The CLI must not blindly apply a generic marketing template. It must select, adapt, and score strategies using current evidence about the business, buyer, market, competitive environment, channel readiness, economics, and available execution capacity.
## 21.1 Printing Press Library Role
The Printing Press library will act as the GTM playbook and integration registry for:
- Positioning and messaging frameworks
- Ideal customer profile and segment selection
- Offer design and lead-magnet patterns
- Product-led and service-led growth motions
- SEO, content, AEO, local search, and programmatic landing-page strategies
- Cold email, LinkedIn, SMS, direct-response, and multi-channel outreach
- Referral, partnership, affiliate, and channel-development strategies
- Launch, waitlist, nurture, reactivation, and lifecycle campaigns
- Conversion-rate optimization and funnel diagnostics
- Attribution, link tracking, campaign measurement, and experimentation
- Provider-specific implementation recipes such as Dub for links and attribution
Printing Press content must be imported as metadata and references rather than copied into hard-coded application logic.
## 21.2 Proposed GTM Command Group
```plain text
leadsniper gtm
├── library
├── diagnose
├── segment
├── strategy
├── offer
├── positioning
├── channels
├── plan
├── campaign
├── experiment
├── attribution
├── measure
└── learn
```
## 21.3 Library Discovery and Synchronization
```bash
leadsniper gtm library list
leadsniper gtm library search --query "local service outbound"
leadsniper gtm library inspect marketing/dub
leadsniper gtm library sync --source printing-press
leadsniper gtm library validate
```
Each registered playbook should include:
```json
{
  "playbook_id": "printing-press/marketing/dub",
  "name": "Dub Attribution and Link Management",
  "source": "printing-press-library",
  "source_url": "https://github.com/mvanhorn/printing-press-library/tree/main/library/marketing/dub",
  "version": "git-commit-or-release",
  "strategy_types": ["attribution", "campaign-links", "partner-tracking"],
  "supported_channels": ["email", "linkedin", "sms", "content", "partners"],
  "required_integrations": ["dub"],
  "approval_level": "review_required",
  "last_synced_at": "timestamp"
}
```
## 21.4 GTM Diagnosis
```bash
leadsniper gtm diagnose \
  --lead lead_123 \
  --include market,customer,offer,channels,funnel,competition,measurement \
  --json
```
Diagnosis dimensions:
- Buyer and decision-maker clarity
- Problem urgency and economic impact
- Existing offer strength
- Differentiation and proof
- Search demand and competitive intensity
- Outbound reachability
- Channel readiness
- Sales-cycle complexity
- Website and conversion readiness
- Retention, referral, and expansion potential
- Attribution maturity
- Compliance constraints
- Available budget, team, and execution capacity
The output must separate verified observations, reasonable inferences, missing information, and recommended next research actions.
## 21.5 Segment and ICP Selection
```bash
leadsniper gtm segment recommend \
  --campaign campaign_123 \
  --objective booked-meetings \
  --minimum-market-score 70
```
```bash
leadsniper gtm segment compare \
  --segments "mortgage-brokers,accountants,commercial-realtors" \
  --criteria urgency,reachability,deal-value,competition,proof
```
Recommended segment output:
```json
{
  "primary_segment": "independent mortgage brokerages",
  "secondary_segments": ["commercial finance brokers"],
  "excluded_segments": ["national banks"],
  "selection_reasons": [],
  "market_evidence": [],
  "assumptions": [],
  "confidence": 0.84
}
```
## 21.6 Strategy Selection
```bash
leadsniper gtm strategy recommend \
  --campaign campaign_123 \
  --objective qualified-opportunities \
  --horizon 90d \
  --budget-cad 5000 \
  --capacity "1 operator, 1 AI agent"
```
The strategy engine should rank a portfolio of motions rather than return one generic recommendation.
Initial GTM motion types:
- Founder-led outbound
- Account-based outbound
- Local market domination
- SEO and AEO authority building
- Programmatic SEO
- Lead-magnet acquisition
- Referral and professional-partner development
- Rank-and-rent lead generation
- Marketplace supply acquisition
- Marketplace buyer acquisition
- Database reactivation
- Event-triggered outreach
- Product-led assessment or calculator
- Free audit to paid implementation
- Content-led nurture
- Community-led growth
- Strategic partnerships
Strategy ranking factors:
- Evidence strength
- Time to first revenue
- Addressable market
- Expected customer value
- Cost to test
- Channel saturation
- Proof requirements
- Operational complexity
- Compliance risk
- Ability to measure
- Reusability across verticals
## 21.7 Offer and Positioning Generation
```bash
leadsniper gtm offer generate \
  --segment "mortgage brokers" \
  --problem "slow lead response and missed follow-up" \
  --outcome "more funded files" \
  --mechanism "AI intake and qualification"
```
```bash
leadsniper gtm positioning generate \
  --offer offer_123 \
  --competitors competitors.json \
  --proof evidence.json
```
Offer output should include:
- Target customer
- Expensive problem
- Desired outcome
- Unique mechanism
- Deliverables
- Time-to-value
- Proof requirements
- Pricing hypothesis
- Risk reversal
- Qualification rules
- Primary call to action
No performance guarantee may be generated without explicit, supportable evidence and required approval.
## 21.8 Channel Mix Recommendation
```bash
leadsniper gtm channels recommend \
  --strategy strategy_123 \
  --available email,linkedin,sms,seo,content,partners,voice \
  --json
```
The engine should recommend channel roles, not merely list channels.
Example:
```json
{
  "primary_acquisition": ["cold_email", "linkedin"],
  "trust_building": ["case_study", "seo_content"],
  "conversion": ["assessment", "calendar_booking"],
  "nurture": ["email_sequence", "retargeting"],
  "attribution": ["dub_links", "crm_campaign_ids"]
}
```
Channel-specific providers may include:
- Resend for transactional and approved email workflows
- Unipile for LinkedIn, WhatsApp, and unified messaging connections
- Twilio for approved SMS and voice-related workflows
- Dub for campaign links, attribution, partner links, and short domains
- DataForSEO for search demand, SERP, competitor, and keyword evidence
- Atomic CRM or a compatible CRM adapter for pipeline state
## 21.9 GTM Plan Generation
```bash
leadsniper gtm plan create \
  --strategy strategy_123 \
  --horizon 90d \
  --cadence weekly \
  --output gtm-plan.json
```
The generated plan should include:
- Strategic thesis
- Priority segment
- Offer and positioning
- Channel architecture
- Funnel stages
- Campaign calendar
- Weekly execution milestones
- Required assets
- Data and integration requirements
- Owners and approval gates
- Budget assumptions
- KPI tree
- Experiments
- Risks and mitigations
- Stop, continue, and scale rules
## 21.10 Campaign Generation from Playbooks
```bash
leadsniper gtm campaign generate \
  --plan gtm-plan.json \
  --playbooks printing-press/marketing/dub,printing-press/<selected-playbook> \
  --stop-before send
```
Generated campaign assets may include:
- Landing-page brief
- Assessment or calculator brief
- Lead-list specification
- Email sequence drafts
- LinkedIn sequence drafts
- SMS follow-up drafts
- Call script
- Content briefs
- Partner outreach kit
- Referral offer
- Retargeting audiences
- Tracking-link map
- CRM stages and automation rules
All outbound assets remain drafts until approved under the LeadSniperAI policy engine.
## 21.11 Dub Attribution Integration
Dub should be used as the standard attribution layer for trackable GTM links where appropriate.
```bash
leadsniper gtm attribution link create \
  --campaign campaign_123 \
  --destination "https://example.ca/assessment" \
  --channel email \
  --segment mortgage-brokers
```
```bash
leadsniper gtm attribution link bulk-create \
  --campaign campaign_123 \
  --input recipients.csv \
  --mode account-level
```
```bash
leadsniper gtm attribution report \
  --campaign campaign_123 \
  --group-by channel,segment,offer
```
Required attribution fields:
- Tenant ID
- Campaign ID
- Strategy ID
- Playbook ID
- Channel
- Segment
- Account or lead ID where permitted
- Offer
- Creative variant
- Destination
- Created timestamp
- Clicks
- Conversions
- Qualified opportunities
- Revenue attribution when available
Tracking must follow applicable privacy, consent, anti-spam, and platform requirements.
## 21.12 Experiment Management
```bash
leadsniper gtm experiment create \
  --campaign campaign_123 \
  --hypothesis "Outcome-led subject lines improve positive replies" \
  --primary-metric positive-reply-rate \
  --guardrail unsubscribe-rate
```
```bash
leadsniper gtm experiment evaluate experiment_123
leadsniper gtm experiment promote experiment_123
leadsniper gtm experiment stop experiment_123
```
Every experiment must define:
- Hypothesis
- Audience
- Control
- Variant
- Primary metric
- Guardrail metrics
- Sample threshold
- Evaluation period
- Decision rule
- Result confidence
- Learning record
## 21.13 Measurement and KPI Tree
```bash
leadsniper gtm measure scorecard --campaign campaign_123
leadsniper gtm measure funnel --campaign campaign_123
leadsniper gtm measure roi --campaign campaign_123
```
Core KPI hierarchy:
```plain text
Business Outcome
├── Revenue
├── Gross profit
├── Qualified pipeline
└── Customer acquisition cost

Conversion Outcomes
├── Opportunities created
├── Meetings booked
├── Positive replies
├── Assessments completed
└── Applications started

Channel Indicators
├── Delivery rate
├── Click-through rate
├── Reply rate
├── Search impressions
├── Organic conversions
├── Partner referrals
└── Cost per qualified opportunity

Guardrails
├── Unsubscribe rate
├── Complaint rate
├── Bounce rate
├── Opt-out compliance
├── Data-confidence score
└── Manual-review exceptions
```
## 21.14 Learning Loop
```bash
leadsniper gtm learn capture --campaign campaign_123
leadsniper gtm learn recommend-next --campaign campaign_123
leadsniper gtm learn update-playbook --experiment experiment_123 --review-required
```
Learning records should connect:
- Market and segment
- Strategy and playbook version
- Offer and message variant
- Channel and campaign
- Evidence used
- Result
- Confidence
- Recommendation
- Reusability across tenants or verticals
Tenant-specific confidential data must not be promoted into shared playbooks. Shared learning should contain generalized patterns, anonymized metrics, and approved reusable rules.
## 21.15 GTM Strategy Object
```json
{
  "strategy_id": "gtm_123",
  "tenant_id": "tenant_456",
  "objective": "qualified-opportunities",
  "segment": "independent mortgage brokerages",
  "problem": "slow lead response and inconsistent follow-up",
  "offer_id": "offer_789",
  "motions": ["founder-led-outbound", "assessment-led-inbound"],
  "channels": ["email", "linkedin", "seo"],
  "printing_press_playbooks": [
    {
      "id": "printing-press/marketing/dub",
      "version": "commit-sha"
    }
  ],
  "evidence_ids": [],
  "assumptions": [],
  "confidence": 0.82,
  "approval_status": "draft",
  "measurement_plan_id": "measurement_123"
}
```
## 21.16 Safety and Governance
- Strategies must be evidence-backed and show assumptions.
- Generated outreach must remain separate from sending.
- Sending must require tenant policy, channel authorization, consent logic, suppression checks, and approval.
- Canadian campaigns must support CASL-related controls and recordkeeping where applicable.
- SMS and voice workflows must support explicit opt-out handling.
- LinkedIn and other platforms must be used within applicable platform rules.
- Personally identifiable information must be minimized in logs and analytics.
- Playbook imports must be scanned, version-pinned, reviewed, and traceable to source.
- No imported strategy may override LeadSniperAI tenancy, security, evidence, or compliance controls.
## 21.17 Proposed Repository Additions
```plain text
cli/leadsniper_cli/commands/
├── gtm_library.py
├── gtm_diagnose.py
├── gtm_segment.py
├── gtm_strategy.py
├── gtm_offer.py
├── gtm_positioning.py
├── gtm_channels.py
├── gtm_plan.py
├── gtm_campaign.py
├── gtm_experiment.py
├── gtm_attribution.py
├── gtm_measure.py
└── gtm_learn.py

gtm/
├── playbooks/
├── registry/
├── schemas/
├── scoring/
├── templates/
├── experiments/
└── providers/
    ├── printing_press.py
    ├── dub.py
    ├── resend.py
    ├── unipile.py
    ├── twilio.py
    └── dataforseo.py
```
## 21.18 Implementation Phases
### Phase A — Playbook Registry
- Add Printing Press source registration and version pinning.
- Build list, search, inspect, sync, and validate commands.
- Define GTM playbook metadata schema.
- Store source attribution and licensing metadata.
### Phase B — Strategy Recommendation
- Add GTM diagnosis, segment scoring, strategy ranking, offer, positioning, and channel recommendation.
- Require evidence and assumption separation.
- Produce deterministic JSON schemas.
### Phase C — Plan and Asset Generation
- Generate 30-, 60-, and 90-day GTM plans.
- Generate reviewable campaign assets from approved playbooks.
- Add approval workflow and audit history.
### Phase D — Attribution and Measurement
- Add Dub link creation and campaign mapping.
- Add CRM campaign identifiers and conversion events.
- Build funnel, channel, experiment, and ROI scorecards.
### Phase E — Closed-Loop Learning
- Capture results and experiment findings.
- Recommend next-best actions.
- Promote approved generalized learnings into reusable internal playbooks.
## 21.19 Acceptance Criteria
The GTM extension is complete when:
1. The CLI can discover and inspect versioned Printing Press GTM playbooks.
2. A qualified lead, segment, or market can be converted into an evidence-backed GTM strategy object.
3. The strategy engine ranks multiple motions and explains its selection.
4. The CLI can generate a 90-day plan and reviewable campaign assets.
5. Dub attribution links can be mapped to tenant, campaign, channel, segment, offer, and variant.
6. All sending remains disabled until explicit authorization and policy checks succeed.
7. Campaign performance can be measured against business outcomes and guardrails.
8. Experiment results create traceable learning records.
9. Imported library updates do not break the stable LeadSniper command contract.
10. All recommendations preserve source attribution, evidence, confidence, assumptions, and approval status.
## 21.20 Recommended Initial LeadSniperAI GTM Playbooks
Prioritize these reusable playbooks for the first implementation:
1. **Free Audit → Strategy Call → Paid Implementation** for local businesses and professional services.
2. **Voice-Verified Opportunity Acquisition** for the LeadSniperAI marketplace.
3. **Founder-Led Account-Based Outbound** for high-value funding, AI automation, and growth advisory offers.
4. **SEO/AEO Authority + Assessment Funnel** for mortgage, alternative lending, and business-funding markets.
5. **Professional Referral Partner Development** targeting accountants, lawyers, commercial brokers, benefits advisers, and wealth professionals.
6. **Database Reactivation** using approved email, SMS, WhatsApp, and calling workflows.
7. **Rank-and-Rent Lead Supply Generation** with location, service, and financing-intent landing pages.
8. **Dub Attribution and Partner Link Management** across outbound, content, referral, and marketplace campaigns.
# Changelog
- 2026-07-26: Added Printing Press GTM Strategy Engine, command model, playbook registry, Dub attribution, experimentation, KPI measurement, governance, implementation phases, and initial LeadSniperAI GTM playbooks.
# GTM Strategy Extension — Deepline and Getaero Patterns
## Purpose
Extend the LeadSniperAI CLI from a lead-discovery interface into a signal-to-revenue GTM operating system. This section adapts reusable patterns from the getaero-io repositories, including GTM engineering skills, niche-signal discovery, account scoring, portfolio prospecting, inbound qualification, reply handling, cost-aware enrichment, and human-approved outbound.
## Strategic Outcome
LeadSniperAI should support the full GTM chain:
```plain text
Market discovery
    ↓
Company and financing signals
    ↓
Opportunity scoring
    ↓
Decision-maker enrichment
    ↓
AI qualification
    ↓
Human approval
    ↓
Multichannel outreach
    ↓
Voice verification
    ↓
Advisor-ready opportunity
    ↓
CRM / marketplace / lender routing
```
## 1. LeadSniper GTM Skill Library
Create a dedicated skill package modeled after the getaero GTM engineering approach.
```plain text
skills/
├── leadsniper-gtm/
├── build-financing-tam/
├── financing-signal-discovery/
├── business-owner-enrichment/
├── referral-partner-prospecting/
├── lender-fit-matching/
├── construction-financing-prospecting/
├── mortgage-renewal-signals/
├── advisor-ready-qualification/
├── lead-package-generation/
└── multichannel-outreach/
```
Each `SKILL.md` should define:
- Required input shape
- Provider sequence and waterfall logic
- Cost gates
- Validation rules
- Evidence requirements
- Output schema
- Deduplication rules
- Consent and compliance constraints
- Approved downstream actions
## 2. New CLI Command Groups
```plain text
leadsniper
├── tam
├── signals
├── icp
├── score
├── enrich
├── qualify
├── route
├── reply
├── portfolio
├── economics
└── workflow
```
### TAM Construction
```bash
leadsniper tam build \
  --vertical construction \
  --location "British Columbia, Canada" \
  --employee-range 10:250 \
  --titles owner,president,cfo,controller \
  --limit 500
```
### Financing Signal Discovery
```bash
leadsniper signals discover \
  --vertical construction \
  --location "British Columbia, Canada" \
  --include permits,hiring,expansion,contracts,property,grants \
  --lookback-days 90
```
### Closed-Won versus Closed-Lost Analysis
```bash
leadsniper icp analyze \
  --won funded-deals.csv \
  --lost declined-or-lost.csv \
  --vertical business-financing \
  --output financing-icp-report.json
```
The analysis should use only signals observable before advisor or salesperson intervention. CRM activity fields created after engagement must not be treated as causal scoring inputs.
## 3. Financing Signal Taxonomy
### Expansion Signals
- New location
- Warehouse or facility expansion
- New equipment
- Rapid hiring
- Geographic expansion
- New product line
- Franchise growth
- Increased production capacity
### Capital Event Signals
- Construction permit
- Development application
- Property acquisition
- Commercial lease
- Grant award
- Government contract
- Acquisition or succession event
- Ownership change
- Refinancing event
### Financial Pressure Signals
- Working-capital pressure
- Supplier constraints
- Large contract requiring upfront fulfillment
- Tax or creditor pressure where lawfully available
- Layoffs
- Declining service capacity
- Growth without corresponding financing
### Real Estate and Mortgage Signals
- Mortgage renewal window
- Construction completion
- Development approval
- Special assessment
- Commercial acquisition
- Rental portfolio growth
- Renovation permit
- Listing expiry
### Referral Partner Signals
- Accounting firms serving owner-managed companies
- Commercial real-estate brokers
- Business lawyers
- Insolvency professionals
- Equipment vendors
- Franchise consultants
- Wealth advisors
- Business bankers
## 4. Financing Opportunity Score
Use a transparent 100-point model.
```plain text
Opportunity Score = Need + Timing + Capacity + Access + Readiness + Fit + Engagement
```
<table>
<tr>
<td>Component</td>
<td>Maximum</td>
</tr>
<tr>
<td>---</td>
<td>---:</td>
</tr>
<tr>
<td>Financing need</td>
<td>25</td>
</tr>
<tr>
<td>Timing and urgency</td>
<td>20</td>
</tr>
<tr>
<td>Financial capacity</td>
<td>15</td>
</tr>
<tr>
<td>Decision-maker access</td>
<td>10</td>
</tr>
<tr>
<td>Document readiness</td>
<td>10</td>
</tr>
<tr>
<td>Product and lender fit</td>
<td>15</td>
</tr>
<tr>
<td>Consent and engagement</td>
<td>5</td>
</tr>
<tr>
<td>Total</td>
<td>100</td>
</tr>
</table>
### Score Bands
<table>
<tr>
<td>Score</td>
<td>Classification</td>
<td>Action</td>
</tr>
<tr>
<td>---:</td>
<td>---</td>
<td>---</td>
</tr>
<tr>
<td>85–100</td>
<td>Advisor-ready</td>
<td>Immediate advisor assignment</td>
</tr>
<tr>
<td>70–84</td>
<td>High-priority opportunity</td>
<td>Voice qualification</td>
</tr>
<tr>
<td>50–69</td>
<td>Signal-qualified</td>
<td>Enrich and nurture</td>
</tr>
<tr>
<td>30–49</td>
<td>Early-stage account</td>
<td>Monitor for additional signals</td>
</tr>
<tr>
<td>Below 30</td>
<td>Low confidence</td>
<td>Avoid paid enrichment</td>
</tr>
</table>
### CLI
```bash
leadsniper score financing-opportunity \
  --lead lead_123 \
  --model financing-v1 \
  --explain
```
Output must include the total score, component scores, evidence, confidence, missing data, and recommended next action.
## 5. Cost-Aware Enrichment Ladder
LeadSniperAI should not purchase the same level of data for every account.
```plain text
Stage 1 — Free or low-cost signal collection
Stage 2 — Company enrichment
Stage 3 — Decision-maker lookup
Stage 4 — Work-email waterfall
Stage 5 — Email verification
Stage 6 — Phone lookup
Stage 7 — Voice verification
Stage 8 — Human research
```
Recommended gates:
- Score below 40: no paid contact enrichment
- Score 40–59: decision-maker and LinkedIn lookup
- Score 60–74: work email plus verification
- Score 75–84: phone data and outreach eligibility
- Score 85+: human review, voice verification, and advisor routing
### CLI
```bash
leadsniper enrich plan --lead lead_123 --budget-cap 5.00
leadsniper enrich execute --lead lead_123 --respect-score-gates
leadsniper enrich waterfall metrics --campaign campaign_123
```
## 6. Deduplication and Lead State Model
Use apex-domain normalization and normalized company names. Do not silently delete matched records; classify them.
```plain text
NET_NEW
KNOWN_ACCOUNT_NO_CONTACT
PAST_PROSPECT
REENGAGE_ELIGIBLE
ACTIVE_OUTREACH
ASSESSMENT_STARTED
VOICE_VERIFIED
APPLICATION_STARTED
ADVISOR_ASSIGNED
FUNDED
DECLINED
DO_NOT_CONTACT
CURRENT_CLIENT
REFERRAL_PARTNER
```
### CLI
```bash
leadsniper lead dedupe \
  --candidates prospects.csv \
  --against crm-export.csv \
  --match apex-domain,company-name
```
## 7. Portfolio and Ecosystem Prospecting
Treat a portfolio as any structured relationship network, not only a venture-capital portfolio.
Supported portfolio sources:
- Grant recipients
- Trade associations
- Chambers of commerce
- Franchise networks
- Private-equity portfolios
- Accelerator cohorts
- Procurement award lists
- Accounting-firm niches
- Construction project owners
- Equipment-dealer segments
```bash
leadsniper portfolio prospect \
  --source bc-manufacturing-grant-recipients.csv \
  --find titles=owner,president,cfo \
  --score financing-opportunity \
  --draft-outreach
```
## 8. Inbound Qualification Workflow
```plain text
Assessment submitted
    ↓
Verify phone and email
    ↓
Enrich business and owner
    ↓
Classify financing category
    ↓
Calculate completeness
    ↓
Calculate opportunity score
    ↓
Match potential products and lenders
    ↓
Route to advisor-ready, voice verification, documents required, nurture, or not eligible
```
### CLI
```bash
leadsniper qualify inbound \
  --assessment assessment_123 \
  --voice-policy required-above-70 \
  --route
```
The output should generate an advisor brief with business summary, funding request, purpose, revenue range, years operating, trigger signals, decision-maker status, verification status, score, document readiness, and suggested financing products.
## 9. Human-Approved Outbound and Reply Engine
All initial outbound and material reply actions should pass through a review queue.
```plain text
Signal discovered
    ↓
AI researches account
    ↓
AI drafts outreach
    ↓
Claims and compliance check
    ↓
Human approval
    ↓
Undo-send delay
    ↓
Resend / Unipile / Twilio
    ↓
Reply classification
    ↓
Human-approved response
```
### Reply Classes
```plain text
POSITIVE_INTEREST
REQUEST_MORE_INFORMATION
NOT_NOW
REFERRAL
ALREADY_FINANCED
WRONG_CONTACT
UNSUBSCRIBE
APPLICATION_READY
CALL_REQUESTED
NEGATIVE
```
### CLI
```bash
leadsniper reply ingest --provider resend
leadsniper reply classify --message reply_123
leadsniper reply draft --message reply_123
leadsniper reply approve --draft draft_456
leadsniper reply send --draft draft_456 --delay 60
leadsniper reply cancel --draft draft_456
```
## 10. Campaign Economics Calculator
Measure economics at the advisor-ready and funded-deal level rather than only cost per contact.
```plain text
Accounts discovered
× signal qualification rate
× decision-maker match rate
× verified-contact rate
× delivery rate
× positive-response rate
× assessment completion rate
× voice-verification rate
× advisor acceptance rate
× funded-close rate
= funded transactions
```
### Required Metrics
- Cost per account researched
- Cost per qualified signal
- Cost per verified contact
- Cost per positive reply
- Cost per assessment
- Cost per voice-verified lead
- Cost per advisor-ready opportunity
- Cost per application
- Cost per funded deal
- Revenue per lead
- Gross margin by lead tier
- Lead-buyer return on spend
### CLI
```bash
leadsniper economics forecast \
  --accounts 1000 \
  --campaign construction-bc \
  --lead-price 250
```
## 11. Evidence-Backed Signal Objects
Every important signal must retain evidence.
```json
{
  "signal": "business_expansion",
  "strength": 0.92,
  "source": "company_careers_page",
  "observed_at": "2026-07-24T10:00:00-07:00",
  "evidence": "Hiring production operators for a new Surrey facility",
  "source_url": "https://example.ca/careers",
  "classification": "observed",
  "confidence": 0.92
}
```
Evidence classifications:
- `observed`
- `derived`
- `self_reported`
- `verified`
Top-scoring opportunities must expose the evidence that contributed to the score.
## 12. Closed-Loop Learning
```plain text
Funded and declined outcomes
    ↓
Signal-effectiveness analysis
    ↓
Updated scoring weights
    ↓
New prospect selection
    ↓
Enrichment and outreach
    ↓
Qualification
    ↓
New outcomes
```
### CLI
```bash
leadsniper model backtest \
  --outcomes funded-and-declined.csv \
  --model financing-v1

leadsniper model recommend-weights \
  --analysis backtest_123 \
  --require-human-approval
```
No scoring weights should update automatically in production without review, versioning, backtesting, and audit logging.
## 13. Recommended System Boundaries
### Deepline Owns
- Contact sourcing
- Provider waterfalls
- Work-email lookup
- Email verification
- External research adapters
- Outbound-provider adapters
### LeadSniperAI Owns
- Financing signal ontology
- Opportunity scoring
- Canadian consent and compliance logic
- Tenant isolation
- Lead ownership and resale rules
- Lender and advisor matching
- Lead tiers
- Marketplace transactions
- Outcome feedback
- Billing and audit trail
### Convex Owns
- Operational system of record
- Campaign state
- Tenant data
- Lead lifecycle
- Workflow state
- Marketplace inventory
- Real-time UI updates
## 14. Implementation Phases
### Phase 1 — Foundation
- Add `signals`, `tam`, `icp`, `score`, `portfolio`, and `economics` command groups
- Define financing signal schema
- Define evidence schema
- Implement lead states and deduplication
- Implement financing opportunity score v1
### Phase 2 — Deepline Integration
- Add Deepline adapter
- Implement decision-maker enrichment
- Implement email waterfall and verification
- Add score-based cost gates
- Add provider and cost metrics
### Phase 3 — Qualification and Routing
- Add inbound assessment qualification
- Add advisor brief generation
- Add product and lender matching hooks
- Add voice-verification routing
- Add CRM and marketplace export
### Phase 4 — Outbound and Replies
- Add draft, approval, reject, and undo-send flow
- Add Resend, Unipile, and Twilio adapters
- Add reply ingestion and classification
- Add compliance and claims checks
### Phase 5 — Learning Loop
- Import funded, declined, and lost outcomes
- Backtest signals and score weights
- Add model versions
- Add conversion dashboards
- Add lead-buyer performance feedback
## 15. Success Criteria
- Every lead score is explainable and evidence-backed
- No paid enrichment runs below configured score thresholds
- Duplicate enrichment and duplicate lead sales are blocked
- Advisor-ready leads contain verified contact, need, timing, fit, and readiness data
- All outbound sending is disabled by default until explicitly approved
- Reply actions are auditable and reversible during the configured delay window
- Campaign economics can be measured through funded outcome
- Scoring models are versioned and backtested
- LeadSniperAI retains ownership of the financing-specific proprietary layer
## Source References
- [https://github.com/getaero-io/gtm-eng-skills](https://github.com/getaero-io/gtm-eng-skills)
- [https://github.com/getaero-io/gtm-signal-scoring](https://github.com/getaero-io/gtm-signal-scoring)
- [https://github.com/getaero-io/deepline-gtm-agent](https://github.com/getaero-io/deepline-gtm-agent)
- [https://github.com/getaero-io/gtm-outbound-calculator](https://github.com/getaero-io/gtm-outbound-calculator)
- [https://deepline.com/docs/quickstart](https://deepline.com/docs/quickstart)
# Addendum — Vertical Discovery Agents and DataForSEO Enrichment
## Purpose
Extend the LeadSniperAI CLI enrichment workflow so discovery is no longer a generic business lookup followed by universal enrichment. The revised system must select or compose a specialized discovery agent according to the target vertical, industry, geography, service offer, and desired opportunity type.
The objective is to turn each local-business record into an evidence-backed professional-service opportunity hypothesis while preserving source attribution, confidence, freshness, and the distinction between observed facts and inferred needs.
## Updated Product Definition
LeadSniperAI is a local-business intelligence and opportunity-detection platform. It builds and maintains a grounded database of local companies and tracks local presence, reputation, reviews, visibility, competitive position, operational changes, and observable service gaps.
The system may identify potential needs relating to:
- Local marketing and reputation management
- Accounting, bookkeeping, payroll, tax planning, and fractional finance
- Business financing and working capital
- Employee benefits and insurance
- Technology, CRM, communication, booking, and automation
- Other professional services configured through vertical discovery packs
LeadSniperAI must describe these outputs as evidence-backed hypotheses requiring validation. It must not claim that a business definitely has a financial, accounting, operational, or compliance problem unless a verified source establishes that fact.
# 1. Revised Discovery and Enrichment Architecture
```plain text
Campaign or operator request
        ↓
Vertical and industry resolver
        ↓
Discovery-agent registry
        ↓
Selected vertical discovery agent
        ↓
Google Maps Grounding + DataForSEO Business Data
        ↓
Canonical local-business identity resolution
        ↓
Vertical-specific enrichment plan
        ↓
Presence, reputation, website, search and change analysis
        ↓
Professional-service signal extraction
        ↓
Opportunity scores with evidence and confidence
        ↓
Deepline / Happenstance contact and relationship enrichment
        ↓
Qualification, CRM routing, marketplace or reviewable outreach
```
## Architectural Roles
### Google Maps Grounding
Use for:
- Natural-language local-business exploration
- Grounded business discovery
- Small-batch verification
- Agent-assisted research questions
- Confirming business identity and local context
### DataForSEO Business Data API
Use for:
- Structured local-market acquisition at scale
- Business Listings Search
- Category and geographic filtering
- Google Business Profile data
- Review retrieval and review history
- Business updates and profile attributes
- Competitive reputation benchmarking
- Repeatable business snapshots and monitoring
### LeadSniperAI
Owns:
- Canonical business identity
- Historical business snapshots
- Local-presence and reputation scoring
- Vertical discovery-agent selection
- Evidence normalization
- Professional-service signal interpretation
- Opportunity scoring and routing
- Cost controls and refresh policy
### Deepline
Use only after the business has passed a configurable opportunity threshold for:
- Decision-maker discovery
- Work email and phone enrichment
- Provider waterfall execution
- Contact validation
- CRM-ready enrichment
### Happenstance
Use for:
- Relationship-aware people discovery
- Warm-path identification
- Network-based introductions
- Professional relationship context
# 2. New CLI Command Groups
Add the following top-level command group:
```plain text
leadsniper
├── agent
├── discover
├── enrich
├── monitor
└── vertical
```
## 2.1 Vertical Registry
```bash
leadsniper vertical list
leadsniper vertical show accounting
leadsniper vertical show financing
leadsniper vertical validate verticals/construction-financing.yaml
leadsniper vertical install verticals/dental-marketing.yaml
leadsniper vertical activate construction-financing
```
Each vertical definition must include:
- Vertical identifier
- Applicable industries and subindustries
- Geographic assumptions
- Target professional service
- Required and optional data sources
- Search and discovery filters
- Signal taxonomy
- Scoring weights
- Exclusions and disqualifiers
- Evidence freshness rules
- Required human validation steps
- Recommended enrichment depth
- Contact personas
- Outreach restrictions
## 2.2 Discovery-Agent Commands
```bash
leadsniper agent list
leadsniper agent show accounting-local-v1
leadsniper agent resolve \
  --industry construction \
  --vertical financing \
  --location "Vancouver, BC"
```
```bash
leadsniper agent run accounting-local-v1 \
  --industry restaurant \
  --location "Burnaby, BC" \
  --limit 250 \
  --json
```
```bash
leadsniper agent compose \
  --vertical accounting \
  --industry trades \
  --signals billing,payroll,growth \
  --output agent-plan.json
```
The resolver should prefer an exact vertical-and-industry agent. If none exists, it may compose an agent from approved signal packs and enrichment modules.
## 2.3 Structured Business Discovery
```bash
leadsniper discover businesses \
  --vertical accounting \
  --industry construction \
  --location "Surrey, British Columbia, Canada" \
  --provider dataforseo \
  --limit 500 \
  --json
```
Supported filters should include:
- Primary and secondary business categories
- Rating range
- Review-count range
- Website present or absent
- Phone present or absent
- Active-business requirement
- Geographic radius
- Postal area
- Business status
- Working hours
- Profile completeness
- Review velocity
- Last observed date
- Inclusion and exclusion lists
## 2.4 Vertical-Aware Enrichment
```bash
leadsniper enrich business lead_123 \
  --vertical accounting \
  --industry construction \
  --depth standard \
  --json
```
```bash
leadsniper enrich business lead_123 \
  --vertical financing \
  --industry restaurant \
  --depth deep \
  --include reviews,profile,website,serp,hiring,news \
  --json
```
Supported enrichment depths:
- `identity`: core business identity and deduplication fields
- `screening`: low-cost eligibility and opportunity screening
- `standard`: profile, reviews, website and competitor context
- `deep`: broader search, news, hiring, technology and contact preparation
- `contact-ready`: approved contact and relationship enrichment after opportunity qualification
# 3. Canonical Local-Business Record
The production system must replace browser-only persistence with a permanent operational database.
Recommended record structure:
```json
{
  "business_id": "biz_123",
  "identity": {
    "business_name": "ABC Roofing Ltd.",
    "google_cid": "...",
    "google_place_id": "...",
    "address": "...",
    "latitude": 49.0,
    "longitude": -123.0,
    "primary_category": "roofing contractor",
    "secondary_categories": [],
    "phone": "...",
    "domain": "..."
  },
  "source_provenance": [],
  "snapshots": [],
  "presence_scores": {},
  "reputation_scores": {},
  "vertical_opportunities": {},
  "contacts": [],
  "engagement_history": []
}
```
Identity resolution should prioritize:
1. Google CID
2. Google Place ID
3. Normalized phone
4. Normalized domain
5. Normalized business name plus address
6. Coordinates and category as supporting evidence
Do not deduplicate businesses using the business name alone.
# 4. Vertical Discovery-Agent Contract
Every discovery agent should implement the following contract:
```json
{
  "agent_id": "construction-financing-v1",
  "vertical": "financing",
  "industries": ["construction", "roofing", "electrical", "plumbing"],
  "target_personas": ["owner", "president", "controller", "cfo"],
  "discovery_sources": ["google_maps_grounding", "dataforseo_business_listings"],
  "enrichment_sources": ["dataforseo_reviews", "dataforseo_google_business", "website", "news", "hiring"],
  "signal_packs": ["capacity_growth", "equipment_need", "working_capital", "location_expansion"],
  "minimum_evidence_items": 2,
  "minimum_opportunity_score": 65,
  "contact_enrichment_threshold": 70,
  "refresh_policy": "monthly",
  "human_validation_required": true
}
```
Each agent must return:
- Business identity
- Eligibility decision
- Observed facts
- Derived metrics
- Inferred opportunity hypotheses
- Evidence items
- Confidence score
- Freshness status
- Missing information
- Recommended next research step
- Whether contact enrichment is authorized
# 5. Initial Vertical Discovery Agents
## 5.1 Local Marketing and Reputation Agent
Applicable industries:
- Home services
- Dental and medical clinics
- Legal services
- Restaurants
- Automotive services
- Beauty and wellness
- Local retail
Signals:
- Strong rating but low review volume
- Weak review velocity
- Negative-sentiment acceleration
- Low owner-response rate
- Missing website
- Incomplete Google Business Profile
- Stale business updates
- Competitor review-count gap
- Local-pack visibility weakness
- Inconsistent categories or business data
Opportunity outputs:
- Reputation management
- Review acquisition
- Google Business Profile optimization
- Local SEO
- Website improvement
- Paid local acquisition
- CRM reactivation
## 5.2 Accounting and Bookkeeping Agent
Applicable industries:
- Construction and trades
- Restaurants
- Multi-location local businesses
- Clinics
- Retail
- Professional services
Signals requiring further validation:
- Rapid location or workforce growth
- Multiple operating locations
- New administrative or finance hiring
- Billing, invoicing or refund complaints
- Quote-versus-invoice complaints
- Payroll complexity indicators
- Expanded service territory
- New incorporation, ownership or business-status changes
- Operational complexity beyond owner-managed administration
Opportunity outputs:
- Bookkeeping
- Payroll
- Tax planning
- Cash-flow advisory
- Controller services
- Fractional CFO services
- Business valuation or succession planning
The agent must not label a company as having poor accounting based solely on review complaints.
## 5.3 Business Financing Agent
Applicable industries:
- Construction and trades
- Restaurants
- Transportation
- Manufacturing
- Clinics
- Retail
- Multi-location service businesses
Signals requiring validation:
- Location expansion
- Equipment expansion
- High demand combined with capacity constraints
- Increased hiring
- Contract or project growth
- New commercial location
- Renovation or tenant-improvement activity
- New service-category expansion
- Seasonal demand and cash-flow timing
- Repeated stock or equipment limitations
Opportunity outputs:
- Working capital
- Equipment financing
- Commercial mortgage
- Construction financing
- Purchase-order or contract financing
- Business acquisition financing
- Refinancing or consolidation
The agent identifies a financing hypothesis, not borrower eligibility or lender approval.
## 5.4 Employee Benefits Agent
Applicable industries:
- Trades
- Clinics
- Professional firms
- Restaurants
- Multi-location service companies
- Growing employers
Signals:
- Sustained hiring
- Workforce growth
- New locations
- Competitive job market
- Job postings with weak or missing benefits
- Employee-retention complaints
- Transition from owner-operated to staffed business
Opportunity outputs:
- Group health and dental
- Disability coverage
- Employee assistance programs
- Retirement and savings programs
- Executive benefits
- Benefits benchmarking
## 5.5 Technology and Automation Agent
Signals:
- Missed-call complaints
- Slow response complaints
- No online booking
- No web chat
- Manual quotation process
- Weak intake forms
- No customer portal
- Poor review response management
- Fragmented communication channels
- Phone-only intake
Opportunity outputs:
- CRM implementation
- AI receptionist
- Booking automation
- Unified messaging
- Automated review management
- Quoting and intake systems
- Customer-service automation
## 5.6 Insurance and Risk Agent
Signals:
- Additional locations
- Equipment additions
- New vehicles
- Workforce expansion
- New services
- Construction contracts
- Property or occupancy changes
- Licensing or operating changes
Opportunity outputs:
- Commercial general liability review
- Property coverage review
- Fleet coverage
- Equipment coverage
- Cyber coverage
- Key-person coverage
- Benefits and disability coordination
# 6. Signal Packs
Discovery agents should be composed from reusable signal packs.
Initial signal packs:
```plain text
reputation_gap
review_velocity
profile_completeness
local_visibility
website_conversion
intake_friction
missed_call_risk
capacity_growth
location_expansion
workforce_growth
billing_friction
payroll_complexity
equipment_need
working_capital
benefits_need
insurance_change
technology_gap
```
Each signal pack must define:
- Required observations
- Optional supporting observations
- Exclusions
- Calculation method
- Confidence method
- Evidence requirements
- Vertical weighting
- Freshness requirements
- Recommended follow-up verification
# 7. Evidence and Claim Classification
Every field and conclusion must be assigned one of the following evidence classes:
- `grounded`
- `source_reported`
- `observed`
- `derived`
- `estimated`
- `inferred`
- `simulated`
- `user_supplied`
- `human_verified`
Production workflows must not use simulated reviews or simulated complaints as evidence.
Example opportunity response:
```json
{
  "vertical": "accounting",
  "opportunity_type": "billing_process_review",
  "score": 72,
  "confidence": 0.76,
  "hypothesis": "The business may benefit from reviewing billing and financial administration processes.",
  "evidence": [
    {
      "claim": "Seven recent reviews mention invoice or refund confusion",
      "evidence_class": "source_reported",
      "source": "dataforseo_google_reviews",
      "observed_at": "2026-07-26T10:00:00-07:00"
    }
  ],
  "validation_required": true
}
```
# 8. Vertical Opportunity Scoring
Do not use one universal lead score. Store a separate opportunity score for each professional-service vertical.
```json
{
  "business_id": "biz_123",
  "opportunity_scores": {
    "local_marketing": 86,
    "reputation_management": 91,
    "accounting": 54,
    "financing": 68,
    "employee_benefits": 33,
    "insurance": 47,
    "technology_automation": 79
  }
}
```
Recommended score dimensions:
- ICP fit
- Signal strength
- Evidence quality
- Evidence freshness
- Urgency
- Service-value potential
- Contactability
- Competitive gap
- Change velocity
- Validation risk
Every score must expose its component weights and evidence references.
# 9. Enrichment Workflow Changes
Replace the generic enrichment sequence with the following workflow:
```plain text
1. Resolve vertical and industry
2. Select or compose discovery agent
3. Run low-cost market discovery
4. Normalize and deduplicate business identities
5. Apply initial eligibility rules
6. Calculate preliminary vertical scores
7. Select enrichment depth by score and confidence
8. Retrieve profile, review and local-search evidence
9. Run vertical signal packs
10. Calculate final opportunity scores
11. Decide whether contact enrichment is authorized
12. Use Deepline or Happenstance where appropriate
13. Produce a reviewable opportunity brief
14. Route to CRM, marketplace or approved campaign workflow
```
## Enrichment Authorization Thresholds
Suggested defaults:
```plain text
Score below 40      → Store identity only
Score 40–59         → Screening enrichment
Score 60–69         → Standard enrichment
Score 70–79         → Deep enrichment
Score 80 or higher  → Contact-ready enrichment and human review
```
Thresholds must be configurable by vertical and campaign economics.
# 10. Monitoring and Refresh Commands
```bash
leadsniper monitor create \
  --vertical financing \
  --industry construction \
  --location "Greater Vancouver, BC" \
  --cadence monthly
```
```bash
leadsniper monitor business biz_123 \
  --include rating,reviews,profile,website,competitors,signals
```
```bash
leadsniper monitor changes biz_123 \
  --since 2026-04-01 \
  --json
```
Suggested refresh policies:
- Active opportunity: weekly
- High-potential monitored business: monthly
- General market record: quarterly
- Low-priority record: every 6–12 months
Monitoring must preserve prior snapshots rather than overwrite the latest state.
# 11. Campaign Workflow Changes
Campaign creation should resolve the vertical agent automatically:
```bash
leadsniper campaign create \
  --name "Surrey Construction Financing Opportunities" \
  --vertical financing \
  --industry construction \
  --location "Surrey, BC" \
  --minimum-score 70
```
```bash
leadsniper campaign run campaign_123 \
  --stages resolve-agent,discover,screen,enrich,score,verify \
  --stop-before contact-enrichment \
  --json
```
Add campaign stages:
- `resolve-agent`
- `discover`
- `identity-resolution`
- `screen`
- `enrich`
- `extract-signals`
- `score`
- `verify`
- `contact-enrichment`
- `relationship-discovery`
- `generate-opportunity-brief`
- `route`
# 12. Opportunity Brief Output
```bash
leadsniper opportunity brief biz_123 \
  --vertical financing \
  --json
```
The brief must contain:
- Business summary
- Vertical and industry
- Local-presence summary
- Reputation summary
- Observed changes
- Opportunity hypothesis
- Evidence table
- Confidence and freshness
- Missing information
- Validation questions
- Recommended contact personas
- Authorized next steps
- Disallowed claims
# 13. Cost-Control Requirements
Use a staged funnel so expensive enrichment is only applied to businesses with sufficient fit and evidence.
```plain text
Large local-market discovery set
        ↓
Eligibility and identity screening
        ↓
Preliminary vertical scoring
        ↓
Selective review, profile and website enrichment
        ↓
Deep research for high-scoring records
        ↓
Contact and relationship enrichment
        ↓
Human validation and activation
```
Requirements:
- Cache provider results according to permitted terms
- Prevent duplicate enrichment charges
- Record provider cost per task and business
- Set campaign enrichment budgets
- Support per-vertical maximum research cost
- Stop enrichment when confidence is already sufficient
- Require explicit authorization before contact-ready enrichment
# 14. Configuration Example
```yaml
vertical: financing
industry: construction
location: Greater Vancouver, BC
agent: construction-financing-v1
providers:
  discovery:
    - google_maps_grounding
    - dataforseo_business_listings
  enrichment:
    - dataforseo_google_business
    - dataforseo_google_reviews
    - website
    - news
    - hiring
  contacts:
    - deepline
  relationships:
    - happenstance
thresholds:
  identity_only: 40
  standard_enrichment: 60
  deep_enrichment: 70
  contact_ready: 80
monitoring:
  default_cadence: monthly
  active_opportunity_cadence: weekly
compliance:
  human_validation_required: true
  outreach_sending_enabled: false
```
# 15. Implementation Phases
## Phase A — Registry and Contracts
- Define vertical schema
- Define discovery-agent contract
- Define signal-pack contract
- Add CLI registry commands
- Add evidence classification
## Phase B — DataForSEO Business Data Integration
- Add Business Listings discovery adapter
- Add Google Business Profile adapter
- Add Google Reviews adapter
- Add identity normalization and deduplication
- Add provider cost and caching controls
## Phase C — Initial Discovery Agents
- Local marketing and reputation
- Accounting and bookkeeping
- Business financing
- Technology and automation
- Employee benefits
- Insurance and risk
## Phase D — Historical Monitoring
- Store business snapshots
- Detect changes
- Calculate review velocity and competitive gaps
- Add refresh scheduling
- Add change-triggered rescoring
## Phase E — Contact and Relationship Activation
- Add Deepline contact enrichment threshold
- Add Happenstance relationship discovery
- Add contact provenance and verification
- Add CRM and marketplace routing
# 16. Success Criteria
The change is successful when:
- A campaign can automatically resolve the correct discovery agent from vertical, industry and geography.
- DataForSEO can discover and enrich local businesses through structured commands.
- Google Grounding remains available for agent research and verification.
- Every opportunity score links to evidence and confidence.
- Each business can have multiple independent vertical opportunity scores.
- Deep and contact-ready enrichment only occur after configurable thresholds are met.
- Historical snapshots support change detection and rescoring.
- Simulated review content is excluded from production evidence.
- Agents produce reviewable hypotheses rather than unsupported declarations.
- The CLI remains deterministic, resumable, auditable and safe by default.
## Decision Record
Selected approach: use a registry of vertical discovery agents composed from reusable signal packs and provider adapters.
Rationale:
- Different industries expose different observable signals.
- Different professional-service verticals require different evidence and contact personas.
- A universal enrichment workflow wastes provider costs and produces weak conclusions.
- A registry allows new verticals to be added without breaking the stable CLI command contract.
- Reusable signal packs prevent duplicated scoring logic across agents.
Expected outcome: LeadSniperAI evolves from generic local-business enrichment into a configurable local commercial intelligence platform that discovers, monitors, scores and routes evidence-backed professional-service opportunities.
<page url="https://app.notion.com/p/3aa9e94cf0a481caa212c20a306e3703">LeadSniperAI CLI — Signal-Based Cold Email Operating System</page>