# SpectraHoldings

A governed, agent-ready financial intelligence wiki for Spectra Holdings Group.

This folder is the canonical Spectra knowledge and agent layer inside the KlickSmartAI wiki.

## Mission

Turn Spectra's raw documents, meeting transcripts, county research, capital assumptions, operating models, project reports, leadership explanations, and investor narratives into reusable, decision-ready intelligence.

The wiki supports AI agents that help Spectra:

- evaluate development opportunities
- assess counties and municipalities
- structure capital stacks
- model Master Credit Facility deployment
- evaluate CDFI and municipal bond capital
- optimize incentives including NMTC, LIHTC, and OBBBA-related opportunities
- prepare investor-ready decision briefs
- preserve report outputs for future reuse
- validate assumptions, citations, leadership explanations, and financial claims

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

## Strategic Purpose

The purpose of this wiki is to help Spectra move from one-off reports and presentations into a repeatable institutional intelligence system.

The system must allow users of reports to:

- read executive-ready outputs
- query the underlying facts and assumptions
- compare reports across counties and projects
- audit citations and validation status
- reuse prior outputs in future capital formation work
- track project, investor, and MCF funding progress over time
- preserve leadership clarification as structured institutional memory

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

## Leadership Clarification Layer

Leadership explanations are primary internal source material but must be classified before being used in investor-ready outputs.

The leadership clarification workflow captures explanations from:

| Leader | Primary Validation Role |
|---|---|
| Willis Andrews | CEO / originator / strategic thesis / MCF vision / public-private narrative |
| Eric Katz | finance / legal / capital structure / investor-risk logic / counsel review requirements |
| Emmanuel Okoye | operations / execution / construction timeline / delivery capacity validation |

The goal is to convert leadership discussions into:

- source notes
- assumptions
- model implications
- capital stack implications
- operational constraints
- legal / tax review items
- contradiction logs
- validation requirements
- wiki updates
- DuckDB / MotherDuck records

Leadership statements must be classified as:

- confirmed operating fact
- strategic intent
- projected assumption
- hypothesis
- requires third-party validation
- investor-sensitive claim
- legal / tax sensitive claim
- operations-sensitive claim

## LLM Usage and Workflow Layer

Different LLMs and coding agents should be used for different layers of the Spectra intelligence system.

No single model is the system of record. The wiki and DuckDB / MotherDuck storage layer are the system of record.

### ChatGPT

Primary role:

- executive reasoning
- financial intelligence design
- workflow architecture
- agent specification
- investor-ready narrative development
- decision brief drafting
- cross-functional synthesis

Best used for:

- turning messy inputs into structured plans
- designing agent workflows
- creating problem definition documents
- drafting investor, county, and landowner narratives
- converting strategy into wiki pages

Outputs should be stored in:

- `summaries/`
- `decisions/`
- `workflows/`
- `agents/`
- `prompts/`

### Claude AI

Primary role:

- long-context synthesis
- document analysis
- transcript digestion
- contradiction detection
- narrative refinement
- assumptions memo drafting

Best used for:

- reading long Spectra documents
- comparing multiple transcripts or briefs
- finding inconsistencies across materials
- producing polished memos
- preparing executive summaries

Outputs should be stored in:

- `summaries/`
- `validations/`
- `queries/`
- `comparisons/`

### Claude Code

Primary role:

- repository operations
- code implementation
- data pipeline creation
- agent workflow implementation
- schema and application development

Best used for:

- creating DuckDB / MotherDuck schemas
- building ingestion scripts
- creating report-generation pipelines
- implementing validation checks
- building dashboard or API layers
- maintaining repository structure

Outputs should be stored in:

- `CODEX.md` or `CLAUDE.md` guidance files as applicable
- `workflows/`
- `_meta/`
- implementation repositories outside the wiki when production code is required

### Codex

Primary role:

- financial model coding
- SQL generation
- Python analysis scripts
- testing and validation logic
- model automation

Best used for:

- creating capital stack calculators
- building IRR / DSCR / ROI models
- writing DuckDB SQL
- generating database migration scripts
- building data validation tests
- reviewing model code for correctness

Outputs should be stored in:

- `CODEX.md`
- `workflows/`
- `validations/`
- DuckDB / MotherDuck schema files
- production code repositories when applicable

### Hermes

Primary role:

- autonomous research
- scheduled monitoring
- county intelligence gathering
- signal detection
- recurring data refresh
- multi-source research orchestration

Best used for:

- monitoring target counties
- collecting housing, migration, wage, and market signals
- tracking municipal meetings, grants, incentives, and public finance opportunities
- running recurring research jobs
- feeding structured findings into the wiki and database

Outputs should be stored in:

- `HERMES.md`
- `raw/`
- `queries/`
- `summaries/`
- DuckDB / MotherDuck tables

### Gemini

Primary role:

- multimodal analysis
- document and image interpretation
- Google ecosystem integration
- map, location, and large context support
- visual asset analysis

Best used for:

- reading maps, site images, aerials, and diagrams
- analyzing presentation decks
- extracting structured data from visual materials
- supporting Google Drive / Workspace based workflows
- assisting with county and site-level research where visuals matter

Outputs should be stored in:

- `raw/assets/`
- `summaries/`
- `queries/`
- `validations/`

## LLM Handoff Rules

All LLM workflows must follow this sequence:

```text
Research / Source Collection
    -> Synthesis
    -> Structured Output
    -> Validation
    -> Storage
    -> Decision Brief
```

Recommended handoff pattern:

```text
Hermes / Gemini
    -> source collection and raw extraction

Claude AI / ChatGPT
    -> synthesis, reasoning, narrative, decision framing

Codex / Claude Code
    -> schemas, automation, models, tests, pipelines

Validation Agent
    -> assumptions, citations, risk, contradiction checks

DuckDB / MotherDuck
    -> structured storage

SpectraHoldings Wiki
    -> semantic memory and reusable knowledge
```

## LLM Governance Rules

- Do not treat any LLM output as final without validation.
- Every important claim must be tied to a source, assumption, or confidence score.
- Every generated report must be stored as both a wiki artifact and a structured database record.
- Contradictions must be logged rather than overwritten.
- Financial models must be reviewed before investor use.
- Investor return language must be reviewed for compliance sensitivity.
- Public finance claims must distinguish confirmed, likely, possible, speculative, and rejected sources.

## Capital Formation System

The capital formation layer determines how Spectra projects should be funded.

It supports three primary funding modes:

1. Whole Project Investor Funding
2. MCF Segment Funding
3. Blended Funding Structure

The system must determine whether a project can be funded by:

- one investor or investor group
- a defined draw or segment of the Master Credit Facility
- a blended stack of investor capital, MCF capital, CDFI debt, municipal bonds, grants, incentives, tax credits, and landowner contributions

## CDFI and Municipal Bond Layer

CDFI and municipal bond capital are first-class funding sources in this wiki.

They are not treated as generic debt.

The Capital Formation Agent must evaluate:

- CDFI eligibility
- municipal bond applicability
- issuer or conduit availability
- public purpose alignment
- repayment source
- approval requirements
- execution timeline
- compliance burden
- impact on funding gaps
- impact on MCF deployment

## Incentive Optimization Layer

The incentive optimization layer evaluates how NMTC, LIHTC, OBBBA-related opportunities, grants, tax credits, and public-purpose benefits should be placed inside the capital stack.

The agent must determine:

- whether the project is eligible
- which project component qualifies
- where the incentive belongs in the stack
- whether it supports predevelopment, infrastructure, construction, permanent financing, tax credit equity, or MCF liquidity
- what timing and compliance requirements apply
- whether legal, tax, bond counsel, CDE, or agency confirmation is required
- whether the incentive belongs in the base case, upside case, or not at all

## Work in Progress Funding Model

The Work in Progress Funding Model evaluates funding needs by project stage.

Stages may include:

- predevelopment
- land / site control
- entitlements and approvals
- infrastructure
- vertical construction
- stabilization, sale, or refinance

Each stage may use a different capital source.

The model must track:

- immediate capital required
- full project capital requirement
- committed capital
- soft committed capital
- possible capital
- speculative capital
- remaining funding gap
- repayment source
- expected recycle date
- MCF capacity impact
- investor return exposure

## Data Architecture

The wiki is the semantic and governance layer.

DuckDB or MotherDuck is the structured storage and analytics layer.

```text
Raw Sources
    -> SpectraHoldings Wiki
    -> DuckDB / MotherDuck
    -> Agent Workflows
    -> Report Outputs
    -> User-Facing Reports / Dashboards
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
- validation results
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

## Governance Rule

Every agent must connect source inputs to a decision-ready output.

Every report must be both:

1. readable by humans, and
2. queryable by agents.

Leadership explanations must be stored as structured institutional memory, not informal notes.

## Canonical Path

This folder supersedes `Spectraholdings/` as the canonical Spectra wiki path.
