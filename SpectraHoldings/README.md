# SpectraHoldings

A governed, agent-ready financial intelligence wiki for Spectra Holdings Group.

This folder is the canonical Spectra knowledge, governance, and agent development layer inside the KlickSmartAI wiki.

## Primary Goal

Build a reusable Financial Intelligence System that helps Spectra Holdings evaluate, fund, validate, and execute housing and community redevelopment opportunities using consistent, defensible, and investor-ready logic.

This wiki exists to convert raw information into decision-ready outputs.

```text
Raw Inputs -> Structured Knowledge -> Agent Workflows -> Validation -> Stored Intelligence -> Decision-Ready Reports
```

## Mission

Turn Spectra's raw documents, meeting transcripts, county research, capital assumptions, operating models, project reports, leadership explanations, investor narratives, and visual design inputs into reusable institutional intelligence.

The wiki supports AI agents that help Spectra:

- evaluate development opportunities
- assess counties and municipalities
- structure capital stacks
- model Master Credit Facility deployment
- evaluate CDFI and municipal bond capital
- optimize incentives including NMTC, LIHTC, and OBBBA-related opportunities
- prepare investor-ready decision briefs
- create structured inputs for HyperFrames, OpenDesign, and `design.md` outputs
- preserve report outputs for future reuse
- validate assumptions, citations, leadership explanations, design claims, and financial claims

## Core Operating Principle

This is not a document archive.

It is a Financial Intelligence System.

Every workflow must follow:

```text
INPUT -> MODEL -> VALIDATION -> DECISION -> OUTPUT
```

No output is complete unless it supports one of these decisions:

- Proceed
- Pause
- Restructure
- Reject
- Request more data

## Agent Development Governing Principle

Spectra agents are not built by prompt experimentation alone.

Every agent must be developed using a test-driven output system.

```text
DEFINE INPUTS -> DEFINE OUTPUT CONTRACT -> RUN TEST CASES -> VALIDATE OUTPUT -> STORE LEARNING -> IMPROVE AGENT
```

This means every agent must have:

1. a clearly defined business objective
2. a defined input set
3. a required output contract
4. pass / fail tests
5. validation rules
6. a learning loop
7. a decision-ready final output

No agent is considered production-ready until it repeatedly produces outputs that pass its defined tests and support a real business decision.

## Test-Driven Agent Output System

The governing development method is:

```text
INPUT -> AGENT TASK -> TEST CASE -> VALIDATION -> DECISION OUTPUT -> LEARNING LOOP
```

This is similar to Test-Driven Development, but adapted for business intelligence agents.

The goal is not simply to make the agent respond.

The goal is to make the agent produce outputs that are:

- complete
- sourced
- structured
- repeatable
- auditable
- decision-ready
- improvable over time

## Required Agent Specification

Every Spectra agent must include the following specification before buildout.

### 1. Agent Objective

Define the business problem the agent solves.

Examples:

- evaluate a county for housing expansion
- produce an investor-ready capital stack
- explain MCF deployment
- identify incentive opportunities
- generate a municipal partnership brief
- validate financial assumptions
- convert research into a HyperFrames video plan

### 2. Input Contract

Define exactly what the agent is allowed or required to use.

Possible inputs include:

- user request
- meeting transcripts
- uploaded documents
- county reports
- Census data
- HUD data
- wage data
- migration data
- zoning documents
- municipal plans
- incentive programs
- CDFI data
- investor assumptions
- leadership explanations
- images, maps, slides, or diagrams
- prior wiki reports
- structured DuckDB / MotherDuck tables

Inputs must be classified as:

- required
- optional
- inferred
- missing
- stale
- needs validation

### 3. Output Contract

Define exactly what the agent must produce.

Each output contract must specify:

- required sections
- required metrics
- required citations
- required assumptions
- required decision language
- required formatting
- required risk flags
- required storage location

Example output contract for a County Intelligence Agent:

```text
Required Output:
- Executive Summary
- County Housing Need
- Population / Migration Summary
- Income and Affordability Profile
- Workforce and Employer Base
- Land / Zoning Signals
- Incentive and Public Finance Opportunities
- Manufacturing Hub Feasibility
- Stakeholder Map
- Investor Narrative
- Municipal Narrative
- Landowner Narrative
- Risks and Missing Data
- Go / No-Go / More Data Recommendation
```

### 4. Test Cases

Every agent must include test cases before production use.

Example tests:

| Test | Pass Condition | Fail Condition |
|---|---|---|
| Completeness Test | All required sections included | Missing required section |
| Citation Test | Material claims have sources | Unsupported claims included |
| Assumption Test | Assumptions are labeled | Assumptions presented as facts |
| Decision Test | Output supports a decision | Output is descriptive only |
| Risk Test | Risks and missing data are flagged | Risks omitted |
| Financial Logic Test | Calculations are internally consistent | Metrics conflict |
| Audience Test | Output is appropriate for intended stakeholder | Wrong tone or wrong emphasis |
| Reuse Test | Output can be stored and reused | Output is one-off or unstructured |

### 5. Validation Rules

Each agent must validate outputs against defined rules.

Validation may include:

- source verification
- citation review
- assumption classification
- contradiction detection
- stale data detection
- financial model checks
- capital stack logic checks
- incentive eligibility checks
- leadership clarification requirements
- legal / tax review flags
- investor-sensitivity flags
- design-claim validation

Validation status must be classified as:

- passed
- passed with caveats
- needs human review
- failed
- blocked by missing data

### 6. Learning Loop

Every agent must improve from use.

The learning loop must capture:

- human reviewer feedback
- investor objections
- county official objections
- landowner objections
- missing data discovered
- corrected assumptions
- better source types
- failed outputs
- successful outputs
- decision outcomes
- changes to templates
- changes to test cases

The learning loop follows:

```text
Output -> Human Review -> Score -> Correction -> Knowledge Update -> Test Update -> Agent Improvement
```

Learning records should be stored in the wiki or structured database so the system improves across counties, projects, investors, and capital sources.

## Agent Development Workflow

Every new agent must follow the standardized Spectra lifecycle.

```text
STEP 1 — DEFINE OBJECTIVE
- What business problem does the agent solve?
- What decision should the output support?

STEP 2 — DEFINE INPUTS
- APIs
- datasets
- files
- assumptions
- constraints
- required variables

STEP 3 — DEFINE OUTPUT CONTRACT
- required sections
- formatting
- scoring
- decision recommendation
- storage path

STEP 4 — DEFINE TEST CASES
- completeness tests
- citation tests
- calculation tests
- decision tests
- audience tests

STEP 5 — RUN SAMPLE OUTPUT
- use a real county, project, capital source, or transcript

STEP 6 — VALIDATE OUTPUT
- check sources
- classify assumptions
- identify contradictions
- flag missing data

STEP 7 — SCORE OUTPUT
- pass
- pass with caveats
- needs revision
- fail

STEP 8 — UPDATE AGENT
- revise prompt
- revise schema
- revise data sources
- revise test cases

STEP 9 — STORE LEARNING
- update wiki
- update DuckDB / MotherDuck
- update templates
- update validation rules

STEP 10 — DEPLOY OR REJECT
- production-ready
- limited use
- research only
- rejected
```

## Minimum Production Standard for Agents

An agent is production-ready only when it can:

- produce the required output format consistently
- separate facts from assumptions
- cite sources where available
- flag missing information
- support a clear decision
- pass defined tests
- improve from feedback
- store outputs in the correct location
- produce investor-safe language when required

## Strategic Goals

## Goal 1: Build Institutional Memory

Capture and preserve Spectra's evolving knowledge so it can be reused across counties, projects, investors, and capital structures.

This includes:

- leadership explanations
- project assumptions
- county research
- capital stack decisions
- MCF assumptions
- incentive eligibility logic
- public finance strategy
- investor narratives
- validation history
- visual and design intelligence
- agent test results
- learning loop improvements

## Goal 2: Standardize Project Evaluation

Every project should be evaluated using repeatable logic.

Required outputs include:

- base case model
- downside case
- upside case
- sensitivity analysis
- go / no-go recommendation
- assumptions memo
- executive decision brief

Required metrics include:

- IRR
- DSCR
- payback period
- cost to build
- absorption rate
- funding gap
- capital readiness score

## Goal 3: Build a Capital Formation System

The system must determine how each project should be funded.

Primary funding modes:

1. Whole Project Investor Funding
2. MCF Segment Funding
3. Blended Funding Structure

Capital sources may include:

- investor equity
- sponsor equity
- senior debt
- construction debt
- CDFI debt
- municipal bonds
- grants
- tax credits
- NMTC
- LIHTC
- OBBBA-related opportunities
- donor-advised / impact capital
- landowner contribution
- public infrastructure support

## Goal 4: Optimize Public Finance and Incentives

CDFI capital, municipal bonds, NMTC, LIHTC, OBBBA-related opportunities, grants, and public-purpose benefits must be evaluated as structured capital layers.

The system must determine:

- what the incentive can fund
- where it belongs in the stack
- what entity is eligible
- what approvals are required
- what timing risk exists
- what compliance burden exists
- whether it improves the base case or only the upside case

## Goal 5: Support Master Credit Facility Deployment

The wiki must support repeatable MCF analysis.

The system must track:

- facility size
- draw amount
- use of funds
- project stage
- cycle time
- expected recycle date
- repayment source
- return obligation
- facility utilization
- concentration risk
- available capacity

The MCF should be modeled as a deployable capital facility, not a generic pool of money.

## Goal 6: Store Report Outputs for Users

Reports must become reusable intelligence assets.

Every report should be:

1. readable by humans
2. queryable by agents
3. auditable against sources
4. comparable against prior reports
5. reusable in future investor, county, and landowner materials

The wiki stores meaning.

DuckDB / MotherDuck stores structured evidence.

## Goal 7: Capture Leadership Knowledge

Leadership explanations must be captured as structured institutional memory.

Primary leadership sources:

| Leader | Primary Validation Role |
|---|---|
| Willis Andrews | CEO / originator / strategic thesis / MCF vision / public-private narrative |
| Eric Katz | finance / legal / capital structure / investor-risk logic / counsel review requirements |
| Emmanuel Okoye | operations / execution / construction timeline / delivery capacity validation |

Leadership statements must be classified as:

- confirmed operating fact
- strategic intent
- projected assumption
- hypothesis
- requires third-party validation
- investor-sensitive claim
- legal / tax sensitive claim
- operations-sensitive claim

## Goal 8: Use the Right LLM for the Right Workflow

No single LLM is the system of record.

The wiki and DuckDB / MotherDuck storage layer are the system of record.

| Tool | Primary Role |
|---|---|
| ChatGPT | executive reasoning, system design, decision framing, narrative architecture |
| Claude AI | long-context synthesis, transcript analysis, contradiction detection, memo drafting |
| Claude Code | repo operations, pipeline implementation, schema development, automation |
| Codex | financial model coding, SQL generation, Python analysis, validation tests |
| Hermes | autonomous research, county monitoring, recurring signal collection |
| Gemini | multimodal ingestion, map/image/deck interpretation, Google ecosystem support, design data extraction |
| Multimodal LLMs such as MiniMax M2.7 | secondary multimodal extraction, visual comparison, document-to-design interpretation, redundancy check for Gemini outputs |

Recommended handoff:

```text
Hermes / Gemini / Multimodal LLMs
    -> source collection, raw extraction, visual interpretation, and design input extraction

Claude AI / ChatGPT
    -> synthesis, reasoning, narrative, decision framing, and design strategy

Codex / Claude Code
    -> schemas, automation, models, tests, pipelines, and design-output implementation support

Validation Agent
    -> assumptions, citations, risk, contradiction checks, and design-claim checks

DuckDB / MotherDuck
    -> structured storage

SpectraHoldings Wiki
    -> semantic memory and reusable knowledge
```

## Goal 9: Build Investor-Ready Governance

Every material claim must be classified and validated before investor use.

The system must protect against:

- unsupported return claims
- unclear assumptions
- stale market data
- unverified public finance claims
- overstated incentive availability
- unvalidated build-cycle assumptions
- unsupported design or visual claims
- legal or tax-sensitive claims used without review

## Goal 10: Create Design-Ready Intelligence for HyperFrames and OpenDesign

The wiki must support conversion of Spectra intelligence into visual communication systems.

This includes generating structured inputs for:

- HyperFrames video outputs
- OpenDesign outputs
- `design.md` files
- investor presentation design systems
- advertorial landing pages
- county pitch visuals
- landowner presentation assets
- capital stack explainer visuals
- MCF explainer videos

Gemini and other multimodal LLMs, such as MiniMax M2.7, should be used to ingest and interpret multimodal inputs such as:

- maps
- aerial images
- site photos
- diagrams
- mind maps
- slide decks
- architectural visuals
- county planning images
- screenshots
- visual brand references
- video frames
- PDF visuals
- scanned or photographed documents

Gemini should be treated as the primary Google ecosystem and multimodal ingestion tool.

MiniMax M2.7 or similar multimodal LLMs may be used as secondary multimodal interpreters for:

- cross-checking Gemini visual extraction
- extracting visual structure from decks and PDFs
- comparing multiple visual references
- generating design-ready descriptions
- producing scene-level observations for HyperFrames
- identifying visual inconsistencies or unsupported visual claims
- converting images into structured design intelligence

Multimodal outputs should be converted into structured design intelligence for LLMs to use.

Required design intelligence outputs:

- visual summary
- key visual elements
- stakeholder audience
- emotional tone
- visual hierarchy
- call-to-action objective
- proof points
- narrative sequence
- recommended scenes or sections
- data points to visualize
- claims requiring validation
- assets required
- multimodal model used
- extraction confidence
- cross-check status

The design workflow must follow:

```text
Visual / Source Input
    -> Gemini or Multimodal LLM Extraction
    -> Structured Design Intelligence
    -> Cross-Check if Needed
    -> ChatGPT / Claude Design Strategy
    -> design.md
    -> OpenDesign Output
    -> HyperFrames Output
    -> Validation
    -> Stored Artifact
```

## Design Governance Rule

Design outputs must not invent claims, numbers, maps, project status, or funding availability.

All visuals, captions, investor claims, county claims, and capital claims must trace back to:

- a source document
- a validated assumption
- a leadership clarification
- a report section
- a structured database record
- or a verified multimodal extraction record

## Core Intelligence Engines

1. Deal Intelligence Engine
2. Capital Stack Engine
3. Market Intelligence Engine
4. Enterprise Forecast System
5. Master Credit Facility Engine
6. County Intelligence Engine
7. Investor Narrative Engine
8. Landowner Partnership Engine
9. Validation and Compliance Engine
10. Agent Orchestration Layer
11. Public Finance Intelligence Engine
12. Work in Progress Funding Engine
13. Incentive Optimization Engine
14. Leadership Clarification Engine
15. Design Intelligence Engine
16. HyperFrames / OpenDesign Output Engine
17. Multimodal Extraction Engine
18. Agent Testing and Learning Loop Engine

## Data Architecture

The wiki is the semantic and governance layer.

DuckDB or MotherDuck is the structured storage and analytics layer.

```text
Raw Sources
    -> SpectraHoldings Wiki
    -> DuckDB / MotherDuck
    -> Agent Workflows
    -> Validation Tests
    -> Learning Loop
    -> Report Outputs
    -> Design Outputs
    -> User-Facing Reports / Dashboards / Presentations / Videos
```

## What Goes in the Wiki

The wiki stores human-readable and agent-readable intelligence:

- executive summaries
- county intelligence briefs
- investor narratives
- landowner briefs
- assumptions memos
- validation memos
- source notes
- contradiction logs
- decision briefs
- reusable prompt patterns
- agent instructions
- concept definitions
- relationship maps
- leadership clarification memos
- design briefs
- design.md files
- HyperFrames and OpenDesign instructions
- multimodal extraction summaries
- agent output contracts
- test cases
- validation rules
- learning loop notes

## What Goes in DuckDB / MotherDuck

DuckDB or MotherDuck stores structured evidence and report data:

- reports
- report sections
- citations
- assumptions
- metrics
- scores
- capital stack items
- funding modes
- funding stage schedules
- MCF draws
- investor commitments
- CDFI and municipal finance sources
- incentive programs
- project incentive analysis
- incentive stack placement
- leadership clarifications
- design assets
- design briefs
- visual source metadata
- multimodal extraction records
- validation results
- agent test runs
- output scores
- correction history
- learning loop records
- user access metadata

## Recommended Storage Path

```text
Phase 1: Local DuckDB
Phase 2: Shared MotherDuck
Phase 3: Dashboard layer
Phase 4: Snowflake or institutional warehouse integration, if required
```

## Core Agent Rules

Every agent must:

- cite sources where available
- identify assumptions
- separate fact from interpretation
- flag missing data
- classify capital as committed, soft committed, likely, possible, speculative, or rejected
- classify leadership statements by validation category
- store human-readable outputs in the wiki
- store structured outputs in DuckDB / MotherDuck
- preserve contradiction history
- produce a decision-ready output
- ensure design outputs use validated claims and traceable source material
- record which multimodal model produced visual or design extraction
- follow a test-driven output contract
- store test results and learning loop improvements

## Current Wiki Map

```text
SpectraHoldings/
├── README.md
├── SCHEMA.md
├── AGENTS.md
├── DATA-ARCHITECTURE.md
├── CLAUDE.md
├── CODEX.md
├── HERMES.md
├── index.md
├── log.md
├── raw/
├── entities/
├── concepts/
│   ├── cdfi-and-municipal-bond-capital.md
│   └── incentive-optimization-nmtc-lihtc-obbba.md
├── agents/
│   └── capital-formation-agent.md
├── workflows/
│   ├── work-in-progress-funding-model.md
│   └── leadership-clarification-workflow.md
├── prompts/
├── summaries/
├── decisions/
├── validations/
├── comparisons/
├── queries/
├── tests/
│   ├── agent-output-tests/
│   ├── validation-tests/
│   └── learning-loop-records/
├── design/
│   ├── design-briefs/
│   ├── design-md/
│   ├── hyperframes/
│   └── opendesign/
├── _meta/
└── _archive/
```

## Key Existing Files

- `SCHEMA.md` — wiki governance, metadata, tags, confidence scoring, and decision standards
- `AGENTS.md` — core Spectra agent system
- `DATA-ARCHITECTURE.md` — separation of wiki layer and DuckDB / MotherDuck storage layer
- `agents/capital-formation-agent.md` — capital formation and capital stack agent specification
- `concepts/cdfi-and-municipal-bond-capital.md` — public finance and CDFI capital concept
- `concepts/incentive-optimization-nmtc-lihtc-obbba.md` — incentive and tax credit optimization concept
- `workflows/work-in-progress-funding-model.md` — project-stage funding and MCF segment workflow
- `workflows/leadership-clarification-workflow.md` — structured interview and validation workflow for Willis, Eric Katz, and Emmanuel

## Near-Term Build Priorities

1. `DUCKDB-SCHEMA.md` — define storage tables for reports, assumptions, MCF draws, incentives, capital stack items, leadership clarifications, design assets, multimodal extraction records, agent tests, and learning loop records.
2. `CLAUDE.md` — define long-context ingestion and synthesis workflow.
3. `CODEX.md` — define coding, SQL, financial model, and design-output implementation standards.
4. `HERMES.md` — define recurring research and county monitoring workflows.
5. `agents/validation-agent.md` — define investor-readiness, assumption validation, and design-claim validation rules.
6. `agents/agent-testing-governance.md` — define test-driven output standards for every Spectra agent.
7. `workflows/capital-stack-workflow.md` — define the complete funding stack process.
8. `workflows/mcf-deployment-workflow.md` — define facility draw, deployment, recycle, and reporting logic.
9. `workflows/agent-learning-loop-workflow.md` — define how agent outputs are reviewed, scored, corrected, and improved.
10. `workflows/gemini-design-ingestion-workflow.md` — define Gemini visual extraction into design.md, OpenDesign, and HyperFrames inputs.
11. `workflows/multimodal-design-extraction-workflow.md` — define use of multimodal LLMs such as MiniMax M2.7 for visual extraction, cross-checking, and design-ready output creation.
12. `tests/agent-output-tests/` — store reusable pass / fail tests for each agent.
13. `tests/learning-loop-records/` — store feedback, corrections, and agent improvement history.
14. `design/design-md/` — store generated `design.md` files.
15. `design/hyperframes/` — store HyperFrames scene plans and output instructions.
16. `design/opendesign/` — store OpenDesign-ready design instructions.

## Success Condition

The SpectraHoldings wiki succeeds when every project, county, capital source, leadership clarification, investor output, agent output, and design output can be:

- sourced
- structured
- validated
- tested
- scored
- stored
- queried
- improved
- reused
- converted into a decision-ready report or presentation asset

## Governance Rule

Every agent must connect source inputs to a decision-ready output.

Every report must be both:

1. readable by humans, and
2. queryable by agents.

Every design output must be both:

1. visually usable by humans, and
2. traceable to validated source material.

Every agent output must be:

1. tested against its output contract, and
2. improved through a learning loop.

Leadership explanations must be stored as structured institutional memory, not informal notes.

## Final Principle

Spectra does not build isolated prompts.

Spectra builds governed agents that transform defined inputs into tested, validated, reusable, decision-ready intelligence.

## Canonical Path

This folder supersedes `Spectraholdings/` as the canonical Spectra wiki path.
