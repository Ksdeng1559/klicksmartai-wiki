# KlickSmartAI Knowledge Wiki

## Master Branch Governance Notice

The `master` branch is the production memory source for KlickSmartAI.

It is used or reserved for:

- Hermes memory
- wiki-llm memory
- Graphify production graph indexing
- Pinecone production vector database ingestion
- future agent retrieval systems

The `master` branch is production memory infrastructure, not a development workspace.

All new research, workflow design, project-specific intelligence, drafts, experiments, and system builds should begin on non-master branches.

Preferred branch families:

- `workflow/*` for active project and system development
- `research/*` for raw discovery and unverified research
- `archive/*` for inactive or historical material

Content should move toward `master` only after it has been reviewed, consolidated, and approved for production memory.

### wiki-llm Read-and-Merge Gate

Changes to `master` require wiki-llm review before promotion into production memory.

A proposed merge into `master` should confirm that the content is:

- stable
- reusable
- appropriate for Hermes default memory
- appropriate for wiki-llm default retrieval
- safe for Graphify production indexing
- safe for Pinecone production vector ingestion
- free of misleading semantic associations
- not raw research
- not workflow-specific material that should remain isolated

Approved merges into `master` should include this statement:

> wiki-llm has read and reviewed this change. This content is approved for production memory and may be merged into master.

### Graphify and Pinecone Scope

Graphify production indexing should use `master` as the clean production source.

Workflow branches may have separate Graphify indexes for project-specific reasoning.

Pinecone production ingestion should use a production namespace sourced from `master`.

Workflow branches should use separate Pinecone namespaces when vector retrieval is needed for project-specific work.

### Consolidation Path

Research and project knowledge should follow this lifecycle:

```text
research branch
→ workflow branch
→ review
→ approved production memory
→ master
→ Graphify update
→ Pinecone ingestion
Shared knowledge layer for all KlickSmartAI agents and LLMs.

## What This Is

This wiki is the **single source of truth** for all KlickSmartAI operations. Every LLM in the stack — Hermes, Claude, ChatGPT, Gemini — reads from and writes to this wiki. It is not a reference document. It is the actual knowledge layer.

This wiki now also supports three strategic operating layers:

1. **RIOS** — Relationship Intelligence Operating System
2. **GrantFunding Intelligence Layer** — federal, state, county, tribal, and private funding intelligence
3. **SBIR/STTR Intelligence Layer** — non-dilutive innovation funding and proposal intelligence

Together, these layers help KlickSmartAI convert research, relationships, funding signals, and institutional knowledge into executable opportunities.

---

## Stack

| Agent / System | Role |
|----------------|------|
| **Hermes** | Curator, executor, daily maintainer |
| **Claude** | Coding, deep research, architecture |
| **ChatGPT** | Drafting, brainstorming, prototyping |
| **Gemini** | Multi-modal, context window work |
| **Graphify** | Semantic graph indexing and entity mapping |
| **Pinecone** | Vector memory and semantic retrieval |
| **DuckDB** | Local analytics, scoring, and research staging |
| **MotherDuck** | Cloud persistence and shared intelligence storage |
| **SendGrid** | Email delivery and engagement tracking |
| **Vidyard** | Personalized video engagement and executive briefings |
| **Unipile** | LinkedIn/email synchronization and relationship activity capture |

---

## Sync Sequence

All changes follow this order:

```text
Wiki (~/wiki) → Graphify → GitHub
```

1. **Write** — edit files in `~/wiki`
2. **Index** — `cd ~/wiki && graphify update .`
3. **Sync** — push to GitHub two-way: fetch → merge → push

---

## Branching Rule

Non-Hermes LLMs write to **feature branches only**. Open a PR for Hermes to review and merge into `master`.

No direct force-push to `master`.

---

## Directory Structure

```text
~/wiki/
├── clients/          # Client contexts, projects, history
├── processes/        # Operating procedures, runbooks
├── agents/           # Agent configs, skill references
├── gtm/              # Go-to-market assets, pipelines
├── recruitment/      # Hiring workflows, candidate tracking
├── spectra/          # Spectra Holdings project context
├── sbir/             # SBIR/STTR research, agency maps, solicitation matching
├── grantfunding/     # Federal, state, county, tribal grant intelligence
├── rios/             # Relationship Intelligence Operating System
├── raw/              # Source data, transcripts, drafts
├── graphify-out/     # Knowledge graph output (do not edit)
└── hermes/           # Hermes operating directives
```

---

# RIOS — Relationship Intelligence Operating System

RIOS is the relationship and opportunity intelligence layer inside the KlickSmartAI wiki ecosystem.

Traditional CRM systems answer:

```text
What stage is this contact in?
```

RIOS answers:

```text
Why should we engage now?
What opportunity exists?
Who knows whom?
What funding aligns?
What problem matters most?
What action should occur next?
```

RIOS transforms fragmented information into actionable relationship, funding, and business development intelligence.

## RIOS Operating Loop

```text
Signal
→ Context
→ Relationship Intelligence
→ Opportunity
→ Action
→ Learning Loop
```

## Core RIOS Objects

- Organization
- Person
- Relationship
- Signal
- Opportunity
- Battlecard
- Meeting
- Policy
- Funding Source

## RIOS Execution Stack

| Layer | Tool / System | Function |
|-------|---------------|----------|
| Signal monitoring | Hermes | Scheduled research and change detection |
| Knowledge source | GitHub Wiki / Obsidian | Source of truth |
| Graph memory | Graphify | Entity and relationship mapping |
| Semantic memory | Pinecone | Vector search and retrieval |
| Local analytics | DuckDB | Fast local scoring and staging |
| Cloud storage | MotherDuck | Shared opportunity graph and historical records |
| Reasoning | Claude / GPT / Gemini | Battlecards, briefs, scoring, proposals |
| Outreach | SendGrid | Email delivery and tracking |
| Video | Vidyard | Personalized executive engagement |
| Relationship capture | Unipile | LinkedIn/email sync and conversation history |

---

# GrantFunding Intelligence Layer

The GrantFunding Intelligence Layer is the non-dilutive funding intelligence module inside the KlickSmartAI Knowledge Wiki and RIOS architecture.

Its purpose is to connect:

- county needs
- tribal priorities
- SBIR/STTR solicitations
- federal grants
- agency funding programs
- community development opportunities
- company technology capabilities
- relationship intelligence
- proposal workflows

into one repeatable opportunity detection and execution system.

## GrantFunding Operating Logic

```text
Community Need
→ Technology Fit
→ Agency Alignment
→ Funding Path
→ Relationship Map
→ Proposal Strategy
→ Execution
```

## Strategic Context

This layer supports current and future initiatives involving:

- Spectra Holdings
- Tiyo Energy
- MineTeck
- KlickSmartAI Venture Studio
- Whatcom County opportunity intelligence
- Oklahoma tribal opportunity intelligence
- SBIR/STTR matching
- federal/state/county grant discovery
- capital stack planning
- community development proposals

## GrantFunding Source Map

Primary sources:

- SBIR.gov
- Grants.gov
- SAM.gov
- FPDS
- USAspending.gov
- agency SBIR/STTR portals
- DOE funding opportunities
- EPA funding opportunities
- HUD programs
- USDA Rural Development
- EDA programs
- BIA / tribal funding sources
- APEX Accelerator resources
- state-level grant portals
- county economic development pages

## GrantFunding Scoring Framework

| Dimension | Weight |
|----------|--------|
| Community need alignment | 20 |
| Technology fit | 20 |
| Agency priority alignment | 15 |
| Eligibility confidence | 15 |
| Funding size | 10 |
| Relationship access | 10 |
| Proposal readiness | 10 |

Decision bands:

```text
85–100 = Priority pursuit
70–84  = Strong candidate
55–69  = Monitor / research further
Below 55 = Deprioritize
```

---

# SBIR/STTR Intelligence Layer

The SBIR/STTR Intelligence Layer supports non-dilutive innovation funding discovery, qualification, proposal development, and commercialization strategy.

The goal is not merely to find solicitations.

The goal is to match:

```text
Company Technology
→ Agency Need
→ Solicitation Topic
→ Prior Award Pattern
→ Proposal Strategy
→ Commercialization Path
```

## SBIR/STTR Use Cases

- Match Spectra, Tiyo, and MineTeck capabilities to active solicitations
- Track Phase I, Phase II, and Phase III award patterns
- Analyze prior awardees and agency funding preferences
- Identify agency technical priorities
- Generate proposal outlines and commercialization plans
- Connect SBIR/STTR opportunities to county, tribal, and infrastructure needs

## Reference GitHub Repositories

### trustdan/awesome-sbir-sttr

Curated SBIR/STTR resource list for small businesses interested in federal opportunities.

RIOS use:

```text
Resource Directory
→ Agency Source Map
→ Funding Navigation Layer
```

### USCTIE/SBIR-STTR-data

Data pipeline reference for retrieving and processing SBIR/STTR contract data from FPDS and SBIR.gov.

RIOS use:

```text
Historical Awards
→ Company Matching
→ Phase I/II/III Pattern Analysis
→ Funding Probability Signals
```

### cory-garms/proposal-pilot

RAG-based proposal automation engine for SBIR/STTR/BAA funding cycles. It scrapes SBIR.gov, Grants.gov, and SAM.gov, scores solicitations against technical capability profiles, and generates proposal drafts.

RIOS use:

```text
Capability Profile
→ Solicitation Scraping
→ Opportunity Scoring
→ Proposal Drafting
→ Commercialization Plan Generation
```

---

# Strategic Opportunity Context

## Whatcom County

Whatcom County is treated as a beachhead pilot for integrated county development intelligence.

Key opportunity themes:

- workforce housing
- underserved rural communities
- tribal alignment
- cross-border Canada/U.S. positioning
- clean energy infrastructure
- e-waste and materials recovery
- county executive engagement
- federal funding alignment

Relevant entities:

- Spectra Holdings
- Tiyo Energy
- MineTeck
- KlickSmartAI
- Lummi Nation
- Nooksack Tribe
- Whatcom County
- Bellingham
- Ferndale
- Blaine
- Birch Bay
- Everson / Nooksack

## Oklahoma Tribal Intelligence

Oklahoma is treated as a scalable tribal development ecosystem.

Key opportunity themes:

- tribal housing
- energy resilience
- infrastructure modernization
- workforce development
- economic development
- environmental recovery
- SBIR/STTR alignment
- federal and tribal partnership pathways

Priority tribal nations for research:

- Cherokee Nation
- Choctaw Nation of Oklahoma
- Chickasaw Nation
- Muscogee Creek Nation
- Osage Nation
- Citizen Potawatomi Nation
- Comanche Nation
- Quapaw Nation

Operating rule:

Tribal governments must be approached as sovereign partners, not simply as funding pathways.

## Justice40 / Disadvantaged Community Alignment

Justice40 should not be treated as a standalone grant program.

It should be treated as a disadvantaged-community alignment and scoring framework.

RIOS should use this logic:

```text
County / Tribal Need
→ Disadvantaged Community Indicators
→ Agency Program Alignment
→ Grant / SBIR Fit
→ Proposal Narrative
```

## APEX Accelerator Role

APEX Accelerators should be treated as a support and navigation layer for:

- government contracting readiness
- agency introductions
- SBIR/STTR navigation
- SAM.gov preparation
- procurement strategy
- county/state/federal opportunity alignment

For RIOS, APEX becomes a relationship and execution support node.

---

# Obsidian Vault

**Vault ID:** `1b9c01d85dcfdeb7`

The Obsidian vault at `~/wiki` is the live working copy. The GitHub repo is the sync layer — do not edit files directly on GitHub unless for emergency fixes.

| File / Folder | Purpose |
|---------------|---------|
| `hermes/directives.md` | Current operating rules for all LLMs |
| `clients/` | All client context and project history |
| `processes/` | Repeatable workflows and SOPs |
| `spectra/` | Spectra Holdings project intelligence |
| `sbir/` | SBIR/STTR opportunity intelligence |
| `grantfunding/` | Grant and funding intelligence |
| `rios/` | Relationship Intelligence Operating System |
| `graphify-out/graph.json` | Semantic knowledge graph output |

---

# Accessing the Graph

```bash
cd ~/wiki && graphify query "<your question>"
```

Or inspect:

```text
graphify-out/GRAPH_REPORT.md
```

for community clusters and entity relationships.

---

# Guiding Principle

```text
Hermes thinks.
GitHub remembers.
Graphify maps.
Pinecone understands.
DuckDB analyzes.
MotherDuck persists.
Claude reasons.
SendGrid delivers.
Vidyard personalizes.
Unipile listens.
RIOS learns.
```

---

# Contact

KlickSmartAI — Dennis Eng — Vancouver, BC
