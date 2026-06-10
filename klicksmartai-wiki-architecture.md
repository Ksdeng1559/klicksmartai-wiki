---
title: KlickSmartAI Wiki - Master Repository Architecture
created: 2026-06-10
updated: 2026-06-10
type: concept
tags: [technology, how-to, guide, research, memory]
sources: [https://github.com/Ksdeng1559/klicksmartai-wiki]
---

# KlickSmartAI Wiki - Master Repository

The production knowledge layer for all KlickSmartAI operations. **master is memory infrastructure, not a workspace** - the canonical source of truth for Hermes memory, Graphify indexing, and Pinecone vector retrieval.

**Repository:** https://github.com/Ksdeng1559/klicksmartai-wiki
**Owner:** Ksdeng1559 (Dennis Eng, Vancouver BC)
**Default branch:** `master` (production memory only)
**Created:** 2026-05-02 | **Last push:** 2026-06-10
**Stats:** 1 star | 1 contributor | 3 open issues

## Core Operating Principle

> **master is memory infrastructure, not a workspace.**

All new research, workflow design, project-specific intelligence, drafts, experiments, and system builds start on **non-master branches**.

## Branch Governance

| Branch | Purpose | Production Memory? |
|---|---|---|
| `master` | Production-approved memory | ✓ Yes (Hermes, Graphify, Pinecone) |
| `workflow/*` | Active project/system development | ✗ Isolated until reviewed |
| `research/*` | Raw discovery, unverified research | ✗ Never merge directly |
| `archive/*` | Inactive/historical material | ✗ Unless explicitly approved |

## wiki-llm Read-and-Merge Gate

Changes to `master` require **wiki-llm review** before promotion. Content must be:
- Stable, reusable, appropriate for default memory
- Free of misleading semantic associations
- NOT raw research or workflow-specific material

**Required approval statement:**

> wiki-llm has read and reviewed this change. This content is approved for production memory and may be merged into master.

## Knowledge Consolidation Lifecycle

```
research/* (raw) → workflow/* (active) → wiki-llm review → master → Graphify + Pinecone
```

1. Start in `research/*` (raw/unverified)
2. Promote to `workflow/*` (active system)
3. Review through wiki-llm governance
4. Promote to `master` only after production approval
5. Rebuild Graphify production indexing from approved `master`
6. Ingest Pinecone production vectors only from approved `master`

## Tech Stack

| Agent/System | Role |
|---|---|
| **Hermes** | Curator, executor, daily maintainer |
| **wiki-llm** | Read-and-merge governance reviewer |
| **Claude** | Coding, deep research, architecture |
| **ChatGPT** | Drafting, brainstorming, prototyping |
| **Gemini** | Multi-modal and long-context work |
| **Graphify** | Semantic graph indexing and entity mapping |
| **Pinecone** | Vector memory and semantic retrieval |
| **DuckDB** | Local analytics, scoring, research staging |
| **MotherDuck** | Cloud persistence and shared intelligence storage |

## Directory Structure

### Production-Memory Folders (master only)

| Folder | Purpose |
|---|---|
| `clients/` | Approved client context and history |
| `processes/` | Repeatable workflows and SOPs |
| `agents/` | Agent configs and skill references |
| `gtm/` | Approved go-to-market assets |
| `recruitment/` | Approved hiring workflows |
| `spectra/` | Approved Spectra Holdings context |
| `raw/` | Source material and drafts |
| `graphify-out/` | Generated graph output only |
| `hermes/` | Hermes operating directives |
| `architecture/` | System architecture docs |
| `concepts/` | Conceptual knowledge |
| `entities/` | Named entities (people, orgs, tools) |
| `frameworks/` | Reusable frameworks |
| `projects/` | Project-specific knowledge |
| `reference/` | Reference material |
| `strategic/` | Strategic planning docs |
| `templates/` | Document templates |
| `tech-debt/` | Known issues to address |
| `queries/` | Recurring research queries |
| `notes/` | General notes |
| `morning-briefings/` | Daily briefing templates |
| `census/` | Census data |
| `clips/` | Clipped content |
| `commercial-relationships/` | Business relationships |
| `drafts/` | Work-in-progress docs |
| `operations/` | Operational knowledge |
| `ops/` | DevOps/SRE knowledge |
| `research-corpus/` | Research source material |
| `research-pipeline/` | Research processing pipeline |
| `sbir/` | SBIR grant material |
| `rios/` | RIOS project |
| `grantfunding/` | Grant funding knowledge |
| `GrantFundingAI/` | Grant funding AI project |
| `gtm-engineer-resources/` | GTM engineering resources |
| `wiki/` | Sub-wikis |
| `SpectraHoldings/` / `Spectraholdings/` | Spectra Holdings content |
| `_meta/` | Metadata (hook logs, etc.) |

### Key Top-Level Files

- `README.md` - Master branch governance
- `AGENTS.md` - Graphify integration rules
- `SCHEMA.md` - Wiki page schema, frontmatter, taxonomy
- `index.md` - Master entity index
- `log.md` - Append-only action log
- `boss-raas-v3.md` - BOSS RaaS v3 framework
- `boss-sip-onboarding.md` - Subscriber Injection Profile onboarding
- `klick2client-os.md` - Klick2Client OS product definition v1.0
- `hermes-skills-hub.md` - Hermes skills reference
- `rios-north-star-architecture.md` - RIOS north star
- `san-antonio-housing-job-strategy.md` - SA housing job strategy
- `context7.md` - Context7 setup reference (added 2026-06-10)
- `agency-agents` - Agency agent list (no extension)

## Sync Sequence (Production-Memory Changes)

```
1. Develop outside master
2. Review with wiki-llm
3. Merge approved content into master
4. Update Graphify from master
5. Ingest Pinecone production namespace from master
6. Keep project-specific branches isolated
```

## Hermes Operating Directives (hermes/directives.md)

### Two-Layer Memory

1. **Ephemeral session context** - current conversation
2. **Permanent knowledge layer** - ~/wiki (2nd brain)

Always consult the wiki first. Always write learnings back.

### Multi-LLM Shared Knowledge

All LLMs share `~/wiki` as ground truth:
- **Hermes** (Nous/Hyper)
- **Claude** (Anthropic)
- **ChatGPT** (OpenAI)
- **Gemini** (Google)

Two-way GitHub sync keeps them aligned.

### Sync Order (Always)

1. **Wiki** - write to ~/wiki first
2. **Graphify** - `cd ~/wiki && graphify update .`
3. **GitHub** - two-way sync: fetch → merge → push

### Daily Cron (8:00 PM PST)

```
git fetch origin
git merge origin/master --no-edit
git add -A + commit (if changes)
git push origin master
```

**Merge conflicts → Telegram with conflicting files. Do NOT auto-resolve.**

**LLM Branching Rule:** Non-Hermes LLMs write to feature branches → open PR → Hermes reviews/merges. No direct force-push to master.

### Obsidian Vault

- **Vault ID:** `1b9c01d85dcfdeb7`
- **Local path:** `~/wiki` (this machine: `G:\AI-Applications\Hermes Agent\wiki\`)
- **GitHub:** `Ksdeng1559/klicksmartai-wiki`

The Obsidian vault is the live working copy. GitHub is the sync layer.

### Hermes Role

Curator + learner + continuous improver of the 2nd brain.

Every session:
1. Check wiki for relevant context before answering
2. Write back learnings, decisions, client context
3. Run graphify to update knowledge graph
4. Sync to GitHub to keep all LLMs aligned

## Memory Architecture (hermes/memory-architecture.md)

| Layer | Scope | Duration |
|---|---|---|
| **Ephemeral** | Current session context | Until session ends |
| **Permanent** | ~/wiki (2nd brain) | Forever |

### Upgrade Triggers (ephemeral → permanent)

- A fact is referenced 3+ times across sessions
- A client decision or project detail that affects future work
- A process that wasn't documented but should be
- A correction or preference the user stated

## Wiki Schema (SCHEMA.md)

### Conventions

- File names: lowercase, hyphens, no spaces
- Every page starts with YAML frontmatter
- Minimum 2 outbound `[[wikilinks]]` per page
- Always bump `updated` date on edits
- New pages added to `index.md`
- Every action appended to `log.md`

### Frontmatter

```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
---
```

### Tag Taxonomy

- People: person, public-figure, colleague
- Organizations: company, nonprofit, government, network
- Places: city, region, country
- Topics: finance, real-estate, technology, science, health, lifestyle, politics, law
- Concepts: how-to, guide, comparison, opinion, history, trend
- Meta: research, memory, notes, conversation

### Page Thresholds

- **Create** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing** when a source mentions something already covered
- **DON'T create** for passing mentions, minor details, one-off facts
- **Split** when a page exceeds ~200 lines
- **Archive** when fully superseded → `_archive/`, remove from index

## Hermes Skills Folder (hermes/skills/)

Specialized research skills auto-loaded for Spectra/North-Star work:
- `spectra-advertorial.md` - Advertorial content generation
- `spectra-census-research.md` - Census data research
- `spectra-county-official-briefing.md` - County official briefings
- `spectra-internal-brief.md` - Internal Spectra briefs
- `spectra-investor-brief.md` - Investor-facing briefs
- `spectra-social-intelligence.md` - Social media intelligence

## Klick2Client OS Overview (klick2client-os.md)

B2B client acquisition OS transforming LinkedIn authority into autonomous pipeline.

### 6-Layer Architecture

1. **Content Engine** - LinkedIn content → reusable assets
2. **Signal Intelligence** - Continuous prospect monitoring (Brave, Tavily, Gemini)
3. **Enrichment Layer** - Python scripts → Sales Battlecard
4. **LinkedIn Conversion Module** - Profile analysis, 3-touch sequence
5. **Lifecycle Engine** - 360-day parallel outreach (LinkedIn + Email via Unipile)
6. **Intelligence Feedback Loop** - Pre-send scoring + post-send tracking

### Pre-Send Quality Score (PSQ)

| Range | Meaning | Action |
|---|---|---|
| 90-100 | Highly specific, verifiable detail | Queue immediately |
| 75-89 | Good personalization | Queue |
| 60-74 | Moderate personalization | Regenerate once |
| <60 | Generic/template-like | Regenerate twice → queue red |

## Related

- [[context7]] - Context7 setup for future Hermes installs
- [[klicksmartai]] - Top-level entity
- [[dennis-eng]] - Owner profile
- [[graphify]] - Graph indexing system
- [[pinecone]] - Vector memory system
- [[hermes-agent]] - Local Hermes Agent setup

## Future Install Reference

For any new Hermes Agent install that should join this ecosystem:

1. Install Hermes with `WIKI_PATH=G:/path/to/local/wiki` (this machine: `G:\AI-Applications\Hermes Agent\wiki\`)
2. Clone `Ksdeng1559/klicksmartai-wiki` to that path
3. Configure daily cron for 8:00 PM PST sync (git fetch → merge → push)
4. Set up Graphify integration: `graphify update .` in wiki dir
5. Set up Pinecone production namespace pointing at `master`
6. Configure non-Hermes LLMs to write to feature branches (PRs only)
7. Install Context7 (see [[context7]]) to prevent API hallucination
8. Set up Obsidian vault with ID `1b9c01d85dcfdeb7`

## References

- [GitHub repo](https://github.com/Ksdeng1559/klicksmartai-wiki)
- [README.md on master](https://github.com/Ksdeng1559/klicksmartai-wiki/blob/master/README.md)
- [AGENTS.md](https://github.com/Ksdeng1559/klicksmartai-wiki/blob/master/AGENTS.md)
- [SCHEMA.md](https://github.com/Ksdeng1559/klicksmartai-wiki/blob/master/SCHEMA.md)
- [hermes/directives.md](https://github.com/Ksdeng1559/klicksmartai-wiki/blob/master/hermes/directives.md)
- [hermes/memory-architecture.md](https://github.com/Ksdeng1559/klicksmartai-wiki/blob/master/hermes/memory-architecture.md)
- [klick2client-os.md](https://github.com/Ksdeng1559/klicksmartai-wiki/blob/master/klick2client-os.md)
