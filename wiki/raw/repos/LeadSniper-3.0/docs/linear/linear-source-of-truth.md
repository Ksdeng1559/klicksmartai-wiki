# LeadSniperAI 3.0 — Linear Source of Truth

## Purpose

This document is the operating source of truth for managing LeadSniperAI 3.0 in Linear.

LeadSniperAI 3.0 is a Website Revenue Infrastructure Intelligence system. It evaluates local service businesses using observable public signals and determines whether a business website functions as a revenue-supporting system or a conversion liability.

The system is designed for pre-sales intelligence, not sales execution.

---

## Product Definition

**Product Name:** LeadSniperAI 3.0  
**Repository:** `Ksdeng1559/LeadSniper-3.0`  
**Execution Layer:** Linear  
**Code + Docs Layer:** GitHub  
**Future Data Layer:** Supabase  
**Future Orchestration Layer:** RIOS / Hermes  

---

## Strategic Positioning

LeadSniperAI 3.0 is not a generic scraper or outreach tool.

It converts:

```text
Google Maps / website data → qualification → website revenue leak diagnosis → AI Employee fit score → CRM-ready intelligence
```

Core thesis:

```text
Raw leads are not the constraint. Qualified, governed, execution-ready intelligence is the constraint.
```

---

## Linear Teams

### PRODUCT
Strategy, roadmap, PRDs, feature definitions, prioritization.

### ENGINEERING
Repo implementation, application logic, APIs, database, frontend, backend, integrations.

### INTELLIGENCE
Scoring logic, prompts, website diagnostics, AI Employee fit rules, quality control.

### GTM
Positioning, pricing, vertical battle cards, partner workflows, sales-safe language.

### OPS
QA, documentation, sprint hygiene, backlog grooming, deployment readiness.

---

## Linear Initiatives

### Initiative 1 — Core Lead Intelligence Engine
Purpose: Build the qualification and scoring layer that determines whether a business should proceed to diagnostic review.

Projects:
- Business Eligibility Engine
- Demand Signal Detection
- Website Failure Detection
- Final Qualification Override
- AI Employee Fit Scoring

### Initiative 2 — Website Revenue Leak System
Purpose: Diagnose whether a website supports conversion or creates friction.

Projects:
- Website Readiness Classifier
- Revenue Leak Detection
- Intake Method Detection
- Trust Signal Detection
- Mobile / UX Friction Review

### Initiative 3 — Linear Operating System
Purpose: Make Linear the execution layer for LeadSniperAI.

Projects:
- Workspace Setup
- Issue Template Library
- Label / Priority Taxonomy
- Sprint Workflow
- Product Roadmap

### Initiative 4 — Vertical Battle Cards
Purpose: Build reusable diagnostic logic for priority verticals.

Launch verticals:
- HVAC
- Plumbing
- Roofing
- Painting

Expansion verticals:
- Solar / Energy
- MedSpa / Dental
- B2B Professional Services

### Initiative 5 — CRM / Export Readiness
Purpose: Prepare diagnostic outputs for CRM, CSV, Loom walkthroughs, and future RIOS/Hermes activation.

Projects:
- CRM-ready Output Schema
- CSV Export Format
- Lead Intelligence JSON
- Audit Trail Logging
- Human Review Queue

---

## Linear Workflow

Recommended statuses:

1. Backlog
2. Ready
3. In Progress
4. In Review
5. QA / Validation
6. Done
7. Blocked
8. Icebox

---

## Label Taxonomy

### Type Labels
- `type: feature`
- `type: bug`
- `type: chore`
- `type: research`
- `type: documentation`
- `type: prompt`
- `type: schema`
- `type: integration`
- `type: qa`

### System Labels
- `system: maps`
- `system: website-analysis`
- `system: scoring`
- `system: ai-employee-fit`
- `system: crm-export`
- `system: linear`
- `system: database`
- `system: frontend`
- `system: backend`

### Vertical Labels
- `vertical: hvac`
- `vertical: plumbing`
- `vertical: roofing`
- `vertical: painting`
- `vertical: solar`
- `vertical: medspa-dental`
- `vertical: professional-services`

### Priority Labels
- `priority: p0-critical`
- `priority: p1-core`
- `priority: p2-important`
- `priority: p3-later`

### Stage Labels
- `stage: discovery`
- `stage: spec`
- `stage: build`
- `stage: review`
- `stage: blocked`
- `stage: ready-to-ship`

---

## MVP Definition

The MVP must analyze one local service business and produce a CRM-ready intelligence record.

MVP requirements:

1. Google Maps business eligibility checklist
2. Website URL validation
3. Local/offline service classification
4. Demand signal capture
5. Website revenue leak detection
6. Website type classification
7. AI Employee fit score
8. Qualified / Watchlist / Disqualified status
9. CRM-ready output format
10. Linear issue templates and operating structure

---

## Qualification Statuses

### Qualified
The business meets absolute eligibility, has at least one observable demand signal, has at least one observable website conversion failure, and passes the final override test.

### Watchlist
The business has some relevant signals but insufficient observable evidence to qualify.

### Low Priority
The business passes eligibility but has no clear demand signal.

### Disqualified
The business fails absolute eligibility or does not present a reasonable observable conversion failure.

---

## Final Override Test

Every business must answer this question:

```text
Could a real customer land on this website and reasonably fail to convert?
```

If yes: Qualified.  
If no: Disqualified.

This test overrides all other logic.

---

## Recommended System Architecture

```text
GitHub = Code + Docs
Linear = Product Execution
Supabase = Structured Intelligence Database
LeadSniperAI = Diagnostic Engine
RIOS / Hermes = Future Agentic Workforce Layer
```

---

## First Execution Milestones

### Milestone 1 — Source of Truth Setup
- Create Linear workspace structure
- Add teams
- Add labels
- Add workflow statuses
- Add initial backlog

### Milestone 2 — MVP Intelligence Engine
- Eligibility logic
- Demand signal logic
- Website failure detection
- Qualification status
- Output schema

### Milestone 3 — AI Employee Fit Layer
- Fit score model
- Fit tiers
- AI Employee opportunity mapping

### Milestone 4 — CRM Export Layer
- JSON output
- CSV output
- Human review queue
- CRM-ready fields
