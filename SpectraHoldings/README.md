# SpectraHoldings

A governed, agent-ready financial intelligence wiki for Spectra Holdings Group.

This folder is the canonical Spectra knowledge and agent layer inside the KlickSmartAI wiki.

## Mission

Turn Spectra's raw documents, meeting transcripts, county research, capital assumptions, operating models, project reports, and investor narratives into reusable, decision-ready intelligence.

The wiki supports AI agents that help Spectra:

- evaluate development opportunities
- assess counties and municipalities
- structure capital stacks
- model Master Credit Facility deployment
- evaluate CDFI and municipal bond capital
- prepare investor-ready decision briefs
- preserve report outputs for future reuse
- validate assumptions, citations, and financial claims

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
│   └── cdfi-and-municipal-bond-capital.md
├── agents/
│   └── capital-formation-agent.md
├── workflows/
│   └── work-in-progress-funding-model.md
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
- `workflows/work-in-progress-funding-model.md` — project-stage funding and MCF segment workflow

## Governance Rule

Every agent must connect source inputs to a decision-ready output.

Every report must be both:

1. readable by humans, and
2. queryable by agents.

## Canonical Path

This folder supersedes `Spectraholdings/` as the canonical Spectra wiki path.
