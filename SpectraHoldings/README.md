# SpectraHoldings

A governed, agent-ready financial intelligence wiki for Spectra Holdings Group.

This folder is the canonical Spectra knowledge and agent layer inside the KlickSmartAI wiki.

## Primary Goal

Build a reusable Financial Intelligence System that helps Spectra Holdings evaluate, fund, validate, and execute housing and community redevelopment opportunities using consistent, defensible, and investor-ready logic.

This wiki exists to convert raw information into decision-ready outputs.

```text
Raw Inputs -> Structured Knowledge -> Agent Workflows -> Validation -> Stored Intelligence -> Decision-Ready Reports
```

## Mission

Turn Spectra's raw documents, meeting transcripts, county research, capital assumptions, operating models, project reports, leadership explanations, and investor narratives into reusable institutional intelligence.

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
| Gemini | multimodal analysis, map/image/deck interpretation, Google ecosystem support |

Recommended handoff:

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

## Goal 9: Build Investor-Ready Governance

Every material claim must be classified and validated before investor use.

The system must protect against:

- unsupported return claims
- unclear assumptions
- stale market data
- unverified public finance claims
- overstated incentive availability
- unvalidated build-cycle assumptions
- legal or tax-sensitive claims used without review

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

## Near-Term Build Priorities

1. `DUCKDB-SCHEMA.md` — define storage tables for reports, assumptions, MCF draws, incentives, capital stack items, and leadership clarifications.
2. `CLAUDE.md` — define long-context ingestion and synthesis workflow.
3. `CODEX.md` — define coding, SQL, and financial model implementation standards.
4. `HERMES.md` — define recurring research and county monitoring workflows.
5. `agents/validation-agent.md` — define investor-readiness and assumption validation rules.
6. `workflows/capital-stack-workflow.md` — define the complete funding stack process.
7. `workflows/mcf-deployment-workflow.md` — define facility draw, deployment, recycle, and reporting logic.

## Success Condition

The SpectraHoldings wiki succeeds when every project, county, capital source, leadership clarification, and investor output can be:

- sourced
- structured
- validated
- stored
- queried
- reused
- converted into a decision-ready report

## Governance Rule

Every agent must connect source inputs to a decision-ready output.

Every report must be both:

1. readable by humans, and
2. queryable by agents.

Leadership explanations must be stored as structured institutional memory, not informal notes.

## Canonical Path

This folder supersedes `Spectraholdings/` as the canonical Spectra wiki path.
