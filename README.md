# KlickSmartAI Knowledge Wiki

Shared knowledge layer for approved KlickSmartAI operating knowledge, agent memory, Graphify indexing, and future Pinecone vector retrieval.

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

## Contact

KlickSmartAI — Dennis Eng — Vancouver, BC
