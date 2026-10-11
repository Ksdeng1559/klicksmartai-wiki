# KlickSmartAI Knowledge Wiki

Shared knowledge layer for approved KlickSmartAI operating knowledge, agent memory, Graphify indexing, and future Pinecone vector retrieval.

> **If you are an LLM agent reading this for the first time** — jump to [Agent Onboarding: What To Pull](#agent-onboarding-what-to-pull). It tells you exactly which files matter for your role (Hermes Agent, Claude Code, ChatGPT, Grok, Gemini, etc.) and which to ignore. Do **not** read the whole repo — this wiki is ~3,500 files, and most of it is irrelevant to your task.

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

## wiki-llm Read-and-Merge Gate

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

## Graphify and Pinecone Scope

Graphify production indexing should use `master` as the clean production source.

Workflow branches may have separate Graphify indexes for project-specific reasoning.

Pinecone production ingestion should use a production namespace sourced from `master`.

Workflow branches should use separate Pinecone namespaces when vector retrieval is needed for project-specific work.

## Consolidation Path

Research and project knowledge should follow this lifecycle:

1. Start in a `research/*` branch when the material is raw or unverified.
2. Promote to a `workflow/*` branch when the material becomes part of an active system or project.
3. Review through wiki-llm read-and-merge governance.
4. Promote to `master` only after production memory approval.
5. Rebuild Graphify production indexing from approved `master`.
6. Ingest Pinecone production vectors only from approved `master`.

## Operating Principle

> master is memory infrastructure, not a workspace.

## Branch Roles

### master

Production-approved memory only. Used for Hermes, wiki-llm, Graphify production graph indexing, and Pinecone production ingestion.

### workflow/*

Active development and project intelligence branches. These branches may be consolidated into `master` later after review.

### research/*

Raw discovery and unverified research. Research branches should not merge directly into `master`.

### archive/*

Inactive or historical material. Archive branches should not feed production memory unless explicitly approved.

## Stack

| Agent / System | Role |
|---|---|
| Hermes | Curator, executor, daily maintainer |
| wiki-llm | Read-and-merge governance reviewer |
| Claude | Coding, deep research, architecture |
| ChatGPT | Drafting, brainstorming, prototyping |
| Gemini | Multi-modal and long-context work |
| Graphify | Semantic graph indexing and entity mapping |
| Pinecone | Vector memory and semantic retrieval |
| DuckDB | Local analytics, scoring, and research staging |
| MotherDuck | Cloud persistence and shared intelligence storage |

## Sync Sequence

All approved production-memory changes follow this order:

1. Develop outside `master`.
2. Review with wiki-llm.
3. Merge approved content into `master`.
4. Update Graphify from `master`.
5. Ingest Pinecone production namespace from `master`.
6. Keep project-specific branches isolated until approved for consolidation.

## Directory Structure

Core production-memory folders may include:

- `clients/` for approved client context and history
- `processes/` for repeatable workflows and SOPs
- `agents/` for agent configs and skill references
- `gtm/` for approved go-to-market assets
- `recruitment/` for approved hiring workflows
- `spectra/` for approved Spectra Holdings context
- `raw/` for source material and drafts
- `graphify-out/` for generated graph output only
- `hermes/` for Hermes operating directives

Project-specific or experimental systems such as SBIR, RIOS, GrantFundingAI, and Spectra capital stack intelligence should remain in `workflow/*` branches until reviewed and consolidated.

## Agent Onboarding: What To Pull

This section is the only thing most LLM agents need to read. Everything else on this page is governance and is only relevant to the human maintainer (Dennis) or the `wiki-llm` reviewer agent.

### Snapshot Strategy

Do **not** crawl the repo. Pull the smallest set of files that gives you:

1. **Identity of the operator** (who you are working for)
2. **Operating constraints** (what you can/can't do, channels, escalation)
3. **The current task context** (active client, project, deliverable)
4. **The stack + integration points** (where data lives, how to retrieve it)

Each agent role below lists exactly the files that satisfy those four needs for that role. Order matters — read top to bottom.

### Hermes Agent (executor, daily ops, memory owner)

Hermes runs in WSL, has shell + filesystem + cron + skills, and is the system's executive layer. Pull these in order:

| # | file | why |
|---|---|---|
| 1 | `hermes/directives.md` | Hermes operating directives — non-negotiable protocols (HITL, task management, silence-by-default) |
| 2 | `hermes/config-and-health-baseline.md` | Live system state, ports, processes, env vars, baseline health |
| 3 | `hermes/skills-hub.md` | Index of every installed skill and when to use each |
| 4 | `klick2client-os.md` | Service positioning + delivery stack (the business Hermes is operating) |
| 5 | `entities-and-projects-index.md` | Master index of every active client and project |
| 6 | `index.md` | Wiki-level index: people, projects, capital sources |
| 7 | `AGENTS.md` | Repo-level agent rules (graphify, schema, sync) |
| 8 | `hermes/skills/` (only the skill the current task invokes) | Skill bodies — load on demand, not all at once |

**Skip entirely:** `clients/*/drafts/`, `raw/`, `clips/`, `graphify-out/`, anything under `wiki/` mirror, anything in `_archive/`.

### Claude Code (coding, deep research, architecture)

Claude Code typically has repo access. Pull these for context, then read source code directly:

| # | file | why |
|---|---|---|
| 1 | `AGENTS.md` | Repo-level agent rules |
| 2 | `klicksmartai-wiki-architecture.md` | How the wiki is organized and why |
| 3 | `SCHEMA.md` | Schema conventions for any structured artifact you write |
| 4 | `entities-and-projects-index.md` | Which entities and projects exist before you create a new one |
| 5 | `klick2client-os.md` | The business model and stack — needed for any deliverable |
| 6 | The specific `clients/<slug>/` workspace for the active task | Read `STATUS.md` first if present, then `_meta/`, then the current draft |
| 7 | `hermes/skills/hermes-agent/SKILL.md` (only if asked to configure/modify Hermes) | When the task is about Hermes itself |

**Skip:** governance sections of `README.md`, mirror folders under `wiki/`, `clips/`, `raw/articles/`.

### ChatGPT (drafting, brainstorming, prototyping, long-form copy)

ChatGPT typically receives content via paste or file upload. The right snapshot is small and self-contained:

| # | file | why |
|---|---|---|
| 1 | `klick2client-os.md` | What KlickSmartAI is, who Dennis is, voice, positioning |
| 2 | `entities-and-projects-index.md` | Which client/project the task is about (filter to one) |
| 3 | The single `clients/<slug>/STATUS.md` or top-of-workspace brief | Current state of the active engagement |
| 4 | `processes/` SOP relevant to the task type (if any) | Repeatable workflow + tone + acceptance criteria |

**Skip:** everything under `hermes/`, `clips/`, `raw/`, `graphify-out/`, `wiki/` mirror, anything with `STATUS.md` referencing "deprecated" or "archived".

### Grok / Gemini / other general-purpose LLM (ad-hoc Q&A, no persistent context)

Treat these as stateless. Pull the smallest possible briefing:

| # | file | why |
|---|---|---|
| 1 | `klick2client-os.md` | One-page business briefing |
| 2 | `klick2client-os.md#active-clients` (or `entities-and-projects-index.md` filtered) | Which client the question is about |
| 3 | The single active draft or deliverable referenced in the question | The actual artifact under discussion |

**If you can't get the active draft** (e.g. user asks about a client not in the index), say so explicitly. Do **not** hallucinate a client from directory name matching.

### wiki-llm (governance reviewer)

The only role that reads the full repo. Pull in this order:

1. The PR / branch diff (not the whole repo)
2. `entities-and-projects-index.md` to know what already exists
3. `SCHEMA.md` to validate structural conformance
4. `AGENTS.md` to validate workflow rules
5. `graphify-out/GRAPH_REPORT.md` to check for god-node drift and unintended connections
6. The governance section of this README (above) to validate promotion criteria

### Common Snapshots (paste-able briefs)

For ad-hoc pasting into ChatGPT/Grok, the following one-page briefs are the highest-leverage snapshots:

- **"Who is Dennis / what is KlickSmartAI"** → `klick2client-os.md`
- **"What is the current client portfolio"** → `entities-and-projects-index.md`
- **"How is the wiki organized"** → `klicksmartai-wiki-architecture.md`
- **"What is Hermes doing today"** → `hermes/config-and-health-baseline.md` + `index.md`
- **"What was the last research output for client X"** → `clients/<slug>/STATUS.md` then most recent dated draft under `clients/<slug>/drafts/`

### Anti-patterns (don't do these)

- ❌ `find . -name "*.md" | xargs cat` — pulls drafts, mirror, archive, raw research
- ❌ Reading `graphify-out/graph.json` — 50+ MB, not human-readable, not for LLM context
- ❌ Treating `clips/` or `raw/articles/` as authoritative — those are inspiration/reference, not memory
- ❌ Creating a new file in `clients/<slug>/` without reading `clients/<slug>/_meta/` first
- ❌ Trusting file timestamps over `STATUS.md` — the most recent file is often a working draft, not the canonical one

## Contact

KlickSmartAI — Dennis Eng — Vancouver, BC
