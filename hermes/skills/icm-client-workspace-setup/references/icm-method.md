# ICM Workspace Architect — Method Reference

> **Attribution:** This document is the canonical method description for **ICM (Interpretable Context Methodology)**, authored by Van Clief & McDermott. The original lives at [github.com/RinDig/icm-architect](https://github.com/RinDig/icm-architect) (cloned locally at `G:\AI-Applications\icm-architect`) and the paper is at [arxiv.org/abs/2603.16021](https://arxiv.org/abs/2603.16021).
>
> This file is a **verbatim copy** bundled with the KlickSmartAI scaffolder `icm-client-workspace-setup` so the method is colocated with the skill that applies it. If the upstream evolves, update the canonical repo first, then refresh this file. If they diverge, the upstream wins.

---

## Use this method when

Structuring repeatable workflows, client knowledge bases, organizational context maps, or repositories/vaults that later agents must change safely. **Do not use it** for a one-off note that can be handled by a saved prompt.

## Core idea

**The workspace is the orchestration layer:**

- folders carry sequence and context scope;
- short Markdown routing files tell an agent where to go next;
- Markdown artifacts carry visible, editable state;
- a person reviews meaningful outputs before work advances.

The goal is a workspace that a **cold agent can open and understand without loading the entire folder tree**.

## Choose the form first

| Form | Use when |
|---|---|
| **Pipeline** | The same sequence repeatedly produces a deliverable. |
| **Umbrella** | Several pipelines share rules, brand, or reference material. |
| **Record library** | Clients, people, cases, or projects accumulate over time. |
| **Knowledge bundle** | The product is navigable knowledge, such as a client brain. |
| **Context map** | The subject is an organization: teams, processes, data, and governance. |
| **System map** | Later agents must safely edit an existing repository or vault. |

**Forms may compose.** Keep a small routing catalog at each level rather than explaining all lower-level internals from the root.

## Invariants

1. **One folder, one job.** A folder represents one workflow step or one kind of record.
2. **Small entry file.** Root `CLAUDE.md` or `AGENTS.md` is a routing catalog, preferably under 60 lines. Link to content; do not duplicate it.
3. **Number execution order.** Use `01_intake`, `02_research`, and so on where sequence matters.
4. **Explicit folder contracts.** Each working folder contains `CONTEXT.md` stating inputs, process, outputs, and the human review action.
5. **Factory separate from product.** Rules, templates, voice, schemas, and compliance live apart from run-specific artifacts.
6. **Human-gated outputs.** Every intermediate output can be read and edited. The next stage only starts after approval or revision.
7. **Load selectively.** Read the entry file, current contract, declared inputs, and required references — never the whole workspace by default.
8. **One home per fact.** Use Markdown and frontmatter. Link rather than copy information.
9. **Filesystem is state.** Status is derived from outputs and frontmatter. Generated indexes are rebuilt, not hand-edited.
10. **Instantiate from templates.** New work starts by copying a defined template rather than a blank page.

## Build mode

1. Identify the repeating unit of work, desired outcome, stable references, and human review pauses.
2. Choose the smallest viable form and structure. Do not create speculative stages, empty misc folders, or depth with no operating purpose.
3. Create the root routing file and root `CONTEXT.md`.
4. Add only real stages or hubs. Give each a `CONTEXT.md`.
5. Put stable instructions in `_shared/` or `_config/`; put reusable blank starters in `_templates/`.
6. Run the **walk test** before declaring the workspace ready.

### Minimal pipeline structure

```
workspace/
├── CLAUDE.md              # short routing catalog
├── CONTEXT.md             # pipeline overview
├── _shared/               # stable rules, voice, sources, schemas
├── _templates/            # blank starters
└── stages/
    ├── 01_intake/
    │   ├── CONTEXT.md
    │   └── output/
    ├── 02_research/
    │   ├── CONTEXT.md
    │   └── output/
    └── 03_deliver/
        ├── CONTEXT.md
        └── output/
```

### Root routing file template

```markdown
# {Workspace name}

{One sentence: what this workspace is and what leaves it.}

## Route

| Need | Go to | Stop when |
|---|---|---|
| Start a run | `stages/01_intake/CONTEXT.md` | its output is human-reviewed |
| Continue an approved run | next numbered stage | its output is human-reviewed |
| Check status | stage `output/` folders | report what exists |
| Configure durable rules | `setup/questionnaire.md` | answers are stored in `_shared/` |

> Do not proceed to another stage until a person has approved or revised the last output.
```

### Stage contract template

```markdown
# {NN}_{stage-name}

## Inputs

- Working: `{exact prior output path}`
- Reference: `{exact stable reference path}`

**Do not load:** {irrelevant stages, prior runs, or broad folders}.

## Process

1. Read the stated inputs.
2. Complete this stage's one job: {job}.
3. Apply {specific hard constraints}.

## Outputs

- `{artifact}.md` → `output/`

## Human check

{One concrete review action. The reviewer edits the output in place if needed.}
```

## Restructure mode

1. **Inventory** before touching anything. Classify each file as `catalog`, `contract`, `factory`, `product`, or `proposed archive`.
2. Identify the existing hidden form: pipeline, record library, knowledge bundle, context map, or system map.
3. Before proposing a move, check in-workspace links, relative-path links, symlinks, and external consumers (scripts, repos, configs, scheduled jobs).
4. Present a **migration map** for approval: old path → proposed path → role → referrers → collision risks.
5. **Copy first**, verify file count and content hashes, update every live reference, then remove the source only after successful verification.
6. Never silently delete. Propose `_archive/` separately and only after reference integrity is confirmed.

### Reference-integrity rules

- A file with a live referrer is held in place or moved only with all its referrers updated in the same approved change.
- Check destinations case-insensitively before a copy or rename; `context.md` and `CONTEXT.md` collide on common client systems.
- Ask the owner about external path consumers. A workspace search cannot prove these are absent.

## System-map mode

Use this when Hermes or later agents must safely change a repository or vault. The source tree remains authoritative; the map cites it and never becomes a duplicate specification.

```
map/
├── CLAUDE.md
├── CONTEXT.md
├── _meta/schema.md
├── _templates/{object,process}.md
├── objects/_index.md
├── processes/             # create only after verified nouns exist
└── effects/CONTEXT.md     # create only when an impact index is warranted
```

**Build in this order:** inventory → catalog → verified object cards → real process cards → change-impact index → re-verification.

Every object card must:
- cite its owning source,
- explain why its present shape matters,
- list first-order **Hits** and **Does not hit**,
- identify reader/writer surfaces.

Mark a card **verified** only with dated source citations. Label obsolete or unconnected concepts as **ghost**, not live.

### Object card template

```markdown
---
type: object
universe: live
status: stub
entity: {owning source path}
---

# {Name}

{One sentence; name both product term and code/file term if they differ.}

## Why this shape
{The load-bearing reason.}

## Shape
- {keys, constraints, or owning files}

Citation: `{path}:{line}`

## If you change this
- **Hits:**
- **Does not hit:**

## Surfaces
| Surface | Role |
|---|---|
| {human, app, or agent} | {reads/writes} |
```

## Walk test

Before completion, test the workspace as a **cold agent**:

1. From the root and at most two additional reads, can it say where it is and where to act?
2. From any stage, does `CONTEXT.md` name exact inputs, the job, outputs, and a human check?
3. Can status be derived from output files and frontmatter alone?
4. Does any routing file contain a long content payload that should live elsewhere?
5. Does any material fact have more than one authoritative home?
6. After restructuring, do all previously live references still resolve?
7. In a system map, can one object card identify the source and first-order change impact?

**If the walk test fails, change the structure — not the explanation length.**

## Portability

`CLAUDE.md` is a conventional entry filename, not a model dependency. Write all instructions in model-neutral language. If another environment requires `AGENTS.md` or a different entry file, generate a byte-identical copy or a one-line pointer to the canonical catalog. Never maintain separate routing documents manually.
