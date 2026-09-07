---
title: "🎯 LeadSniperAI CLI — Product Requirements & Implementation Plan"
created: 2026-09-07
updated: 2026-09-07
type: process
status: active
source: notion
notion_id: 3a89e94cf0a48100800ef4a2f57f842a
notion_url: https://app.notion.com/p/3a89e94cf0a48100800ef4a2f57f842a?pvs=204
tags: [sop, notion-mirror]
sources: [notion: 🎯 LeadSniperAI CLI — Product Requirements & Implementation Plan]
---

# 🎯 LeadSniperAI CLI — Product Requirements & Implementation Plan

> Mirrored from Notion page `3a89e94cf0a48100800ef4a2f57f842a` on 2026-09-07. Source: https://app.notion.com/p/3a89e94cf0a48100800ef4a2f57f842a?pvs=204

{"type":"emoji","emoji":"🎯"}

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
leadsniper --request-id 
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
leadsniper batch show 
leadsniper batch status 
leadsniper batch leads 
leadsniper batch errors 
```
```bash
leadsniper queue stats
leadsniper queue list --status failed
```
Future backend work:
```bash
leadsniper batch retry 
leadsniper batch cancel 
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
leadsniper audit hero --url 
leadsniper audit conversion --url 
leadsniper audit mobile --url 
leadsniper audit intake --url 
leadsniper audit trust --url 
leadsniper audit pagespeed --url 
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
leadsniper campaign discover 
leadsniper campaign enrich 
leadsniper campaign audit 
leadsniper campaign score 
leadsniper campaign verify 
leadsniper campaign generate-outreach 
leadsniper campaign export 
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
LeadSniperAI Workflow & Search Results Improvement Plan