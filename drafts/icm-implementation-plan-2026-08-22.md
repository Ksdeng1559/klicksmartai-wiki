# ICM Implementation Plan — KlickSmartAI Wiki + Hermes

**Status:** Draft (pre-HITL)
**Author:** Hermes (Chief of Staff)
**Date:** 2026-08-22
**Sources verified:**
- Paper: arXiv 2603.16021 — *Interpretable Context Methodology: Folder Structure as Agent Architecture* (Van Clief & McDermott, Eduba/Edinburgh)
- Repo (paper + spec): github.com/RinDig/Interpretable-Context-Methodology
- Skills: github.com/ktnCodes/icm-template — `/icm-scaffold`, `/icm-sync`, `/icm-context-scaffold`
- Adjacent: Karpathy LLM-Wiki (raw → compile → wiki → Q&A), Obsidian, Hermes native features

---

## TL;DR

ICM is **folder structure as orchestration**. Numbered stage folders + plain markdown contracts replace multi-agent frameworks. One Hermes session walks the tree, reading only the context each stage needs (2–8k focused tokens vs 30–50k monolithic). For KlickSmartAI, it slots in cleanly because the wiki already has folder conventions, skills, memory providers, and Cron — ICM formalizes what we're already doing and gives us a HITL-gated pipeline for client deliverables.

**Recommended posture:** adopt **Quick-mode ICM (3 layers)** on the wiki root and on two high-value client workspaces (`spectra-holdings`, `veritas-developments`); pilot **Full-mode ICM (5 layers)** on one repeatable pipeline (the county intelligence deliverable). Skip a wholesale refactor — earn complexity.

---

## 1. What ICM actually is (research summary)

### Core claim
The filesystem is the orchestration layer. Numbered folders = stages. Markdown files = stage contracts. A single agent (or Hermes session) reads the right files at the right moment. **The LLM is a compiler, not a chatbot.** Conversations happen at human review gates between stages, not during execution.

### Five-layer context hierarchy (paper §3)

| Layer | File | Question | Budget | Changes |
|-------|------|----------|--------|---------|
| 0 | `IDENTITY.md` / `CLAUDE.md` / `AGENTS.md` | "Where am I?" | ~800 tok | Only when structure changes |
| 1 | root `CONTEXT.md` | "Where do I go?" | ~300 tok | When stages added/removed |
| 2 | Stage `CONTEXT.md` | "What do I do?" | 200–500 tok | When stage process changes |
| 3 | `_config/`, `references/` | "What rules apply?" | 500–2k per stage | Configured once |
| 4 | `output/` | "What am I working with?" | varies | New every run |

### Five design principles (paper §2)
1. **One stage, one job** — research stage doesn't also draft
2. **Plain text as the interface** — markdown only, no binaries
3. **Layered context loading** — prevent pollution, don't compress after the fact
4. **Every output is an edit surface** — humans can read/edit/save between stages
5. **Configure the factory, not the product** — set up once, produce repeatedly

### Why it works (cited in paper)
- Liu et al., *Lost in the Middle*: LLMs degrade when relevant info is buried in long contexts. ICM loads 2–8k focused tokens.
- Karpathy LLM-Wiki pattern (raw → compile → wiki → Q&A) maps directly to ICM stages. ICM stages are essentially "compile" steps that emit wiki-grade artifacts.
- Unix philosophy: programs that do one thing, plain-text interfaces, composable pipelines.

### Where it fits — and where it doesn't
**Good for:** sequential, reviewable, repeatable, knowledge-heavy pipelines (Karpathy archetype).
**Not for:** real-time multi-agent collaboration, high-concurrency systems, complex automated branching. Use a framework for those.

---

## 2. Gap analysis: KlickSmartAI wiki vs ICM-native

| ICM layer | Current wiki state | Action |
|-----------|---------------------|--------|
| Layer 0 — Identity | `AGENTS.md` (graphify rules only, 411 chars) | **Add** a project-level IDENTITY with folder map + workflow map. Keep AGENTS.md as the agent-load entry point. |
| Layer 1 — Routing | None at root; `index.md` exists but isn't a routing table | **Add** `CONTEXT.md` at wiki root with a Task → Destination table |
| Layer 2 — Stage contracts | None; some `clients/<x>/projects/<y>/README.md` come close | **Wrap** each active client deliverable as a stage folder (or virtual stage in CONTEXT.md) |
| Layer 3 — References | `frameworks/`, `concepts/`, `_meta/` — partial match | **Promote** to `_config/` (cross-cutting voice/conventions/glossary) and `references/` (per-stage) |
| Layer 4 — Outputs | `clients/`, `drafts/`, `morning-briefings/`, `cron_outputs/` | **Keep**; add stage-numbered subfolders where a pipeline repeats |
| Skills | `hermes/skills/` (local) + 800+ in skill library | **Map** mechanical steps to skills; add 3 ICM skills from ktnCodes/icm-template |
| HITL gate | `wiki-source-of-truth-governance` skill enforces drafts/ → HITL → projects | **Already correct**; ICM outputs must land in `drafts/` until validated |
| Memory providers | Honcho (MCP :44547), built-in MEMORY.md, fact_store | **Wire** to durable preferences (voice, conventions) per the paper's Layer 3 guidance |
| Cron | `outputs/cron/schedule.md` | **Use** for nightly ICM pipeline runs (e.g. county census compilation) |
| Profile isolation | multiple profiles (default, work, …) | **Use** so research/content/ops workspaces don't collide |

**Net:** the wiki has the substrate. ICM is a 5–10% missing layer — wiring + a couple of canonical files.

---

## 3. Three implementation options

### Option A — Quick mode on the wiki only (recommended starter)

**Scope:** add Layer 0 + Layer 1 + `_config/` to the wiki root. No new stage folders. No client refactor.

**Files created (4):**
```
/home/denni/wiki/
├── IDENTITY.md                       # Layer 0 — project map + rules (~800 tok)
├── CONTEXT.md                        # Layer 1 — task routing table (~300 tok)
└── _config/
    ├── voice.md                      # tone for AI-generated content
    ├── conventions.md                # file/folder naming, version rules
    └── glossary.md                   # domain terms (CDFI, MCF, CLT, ICM, …)
```

**Time:** ~1 hour. No client impact. Reversible.

**Why:** gives every Hermes session an immediate map of the wiki ("where am I?") and a routing table ("where do I go?"). Backwards-compatible with the existing `AGENTS.md` (which stays as the agent-load entry point — IDENTITY.md is for humans / new sessions).

---

### Option B — Quick mode on the wiki + 2 client workspaces

**Scope:** Option A **plus** wrap `spectra-holdings` and `veritas-developments` as ICM sub-workspaces. Each gets its own `IDENTITY.md` + `CONTEXT.md` + `_config/`. Their existing `projects/`, `deliverables/`, `drafts/` stay untouched.

**Files added (8):**
```
/home/denni/wiki/clients/spectra-holdings/
├── IDENTITY.md                       # client workspace map
└── CONTEXT.md                        # task → stage routing

/home/denni/wiki/clients/veritas-developments/
├── IDENTITY.md
└── CONTEXT.md

# Same 3 _config/ files as Option A, but client-scoped:
/home/denni/wiki/clients/spectra-holdings/_config/{voice,conventions,glossary}.md
/home/denni/wiki/clients/veritas-developments/_config/{voice,conventions,glossary}.md
```

**Time:** ~3 hours. Low client risk (additive only). Visible value on next deliverable.

**Why:** Spectra (county intelligence) and Veritas (developer content) are the two most repeatable, multi-stage client workflows. ICM gives them an explicit stage model with review gates.

---

### Option C — Full mode ICM pilot on Spectra's county pipeline (Option B + 5-layer pipeline)

**Scope:** Option B **plus** build the actual 5-layer county intelligence pipeline:

```
clients/spectra-holdings/pipelines/county-intelligence/
├── IDENTITY.md
├── CONTEXT.md
├── stages/
│   ├── 01_census_compile/        # raw → structured (Karpathy "compile")
│   │   ├── CONTEXT.md            # stage contract
│   │   ├── references/           # census API docs, prior reports
│   │   └── output/
│   ├── 02_investor_brief/        # compiled data → investor doc
│   │   ├── CONTEXT.md
│   │   ├── references/           # voice.md, Reg D 506(b) compliance
│   │   └── output/
│   ├── 03_county_official_brief/
│   │   └── …
│   └── 04_publish/               # wiki gate → drafts/ → HITL → projects/
│       └── …
├── _config/
│   ├── voice.md                  # investor-tone vs official-tone
│   ├── conventions.md
│   ├── glossary.md
│   └── compliance-regd506b.md    # Layer 3 critical reference
└── skills/
    └── advance-county-stage/     # mechanical: cd + read CONTEXT + execute + handoff
```

Plus 3 imported skills from ktnCodes/icm-template:
- `/icm-scaffold` — generate the ICM layer on any project
- `/icm-sync` — keep IDENTITY/CONTEXT in sync with disk
- `/icm-context-scaffold` — fill missing CONTEXT.md files

**Time:** ~1 day of focused work. Requires Dennis validation at each stage boundary.

**Why:** Spectra's county pipeline is **the** Karpathy archetype in our portfolio: raw sources (Census API, county records) → compiled structured articles → wiki-grade investor/official briefs → HITL-validated published deliverables. This is exactly what ICM was designed for, and it's already partially scaffolded.

---

## 4. Recommended path: A → B → C in three HITL gates

| Gate | Deliverable | Validation | Time |
|------|-------------|------------|------|
| **Gate 1 — Quick mode on wiki root** | IDENTITY.md, root CONTEXT.md, 3 _config/ files | Dennis reads IDENTITY.md + runs `/icm-context-scaffold lint` to confirm coverage | ~1 hr |
| **Gate 2 — Sub-workspaces for 2 clients** | Client-level IDENTITY/CONTEXT/_config | Dennis scans the routing table — does every common task have a row? | ~3 hrs |
| **Gate 3 — Full-mode pipeline on Spectra county** | Working 5-layer pipeline; one Whatcom-county-equivalent run end-to-end | Dennis reviews one stage's output before authorizing the next | ~1 day |

**Stop after each gate.** Do not start Gate 3 until Gates 1 and 2 have been run in production for ≥2 weeks. ICM earns its complexity.

---

## 5. Concrete recipe for the first deliverable (Gate 1)

These are the literal files I'd produce — shown here so you can decide on tone/scope before I write them.

### 5a. `/home/denni/wiki/IDENTITY.md` (Layer 0)

```markdown
# KlickSmartAI Wiki — Identity

> The primary knowledge repo for all agents. Wikis and skills land here; deliverables ship to `drafts/` first, then `projects/` after HITL validation.

## Folder Map
[full tree with inline comments — Layer 0/1/2/3/4 annotations]
## Raw Source Locations
[external folders feeding into the wiki, e.g. Notion, Obsidian vault]
## Stage Map
[virtual stages: research → draft → review → publish]
## Rules
1. AI-generated client content → drafts/, NEVER projects/ until HITL.
2. Treat root CONTEXT.md as the routing table.
3. Each active client has a sub-workspace IDENTITY.md.
4. Skills in ~/.hermes/skills/ > ad-hoc code.
5. Cron outputs → outputs/cron/ — never inline.
```

### 5b. `/home/denni/wiki/CONTEXT.md` (Layer 1)

```markdown
# Routing

| Task | Go to | Load first |
|------|-------|------------|
| Understand this wiki | this file | IDENTITY.md |
| Run Spectra pipeline | clients/spectra-holdings/CONTEXT.md | client IDENTITY.md |
| Run Veritas pipeline | clients/veritas-developments/CONTEXT.md | client IDENTITY.md |
| Morning briefing | cron/morning-briefing/SKILL.md | IDENTITY.md |
| Add a new client | wiki-source-of-truth-governance skill | IDENTITY.md |
| Generate a deliverable | the relevant client CONTEXT.md | client IDENTITY.md |
```

### 5c. `/home/denni/wiki/_config/voice.md`

```markdown
# Voice

Tone: direct, concise, structured. Match Dennis's reply style — short sentences, no fluff, table-driven.
Length: lead with answer; supporting detail after. No preambles.
Citations: every claim from a search result carries the URL inline.
Hedging: never guess. Use "unknown" or escalate. Label assumptions explicitly.
HITL: drafts → Dennis → projects. Never bypass.
```

### 5d. Mechanical imports

```bash
# 3 skills from ktnCodes/icm-template, scoped to this profile
mkdir -p ~/.hermes/skills/icm-scaffold ~/.hermes/skills/icm-sync ~/.hermes/skills/icm-context-scaffold
# (clone repo, copy SKILL.md into each — non-destructive)
```

---

## 6. Risk + open questions

| Risk | Mitigation |
|------|------------|
| IDENTITY.md drift — gets out of sync as wiki grows | Adopt `/icm-sync` as a weekly cron |
| Layer 0/1/2 files balloon past token budget | Add `_index.md` per `_config/` and `references/` folder once they exceed ~10 files |
| Stages that should be combined stay split | Audit at Gate 2: any two stages that always run together without review → merge |
| HITL drift — agents publish to projects/ directly | Existing wiki-source-of-truth-governance skill is the enforcement layer; ICM does not change it |
| Memory duplication — same conventions written to MEMORY.md and _config/voice.md | Convention: durable user prefs → MEMORY.md; workspace conventions → `_config/`. Skill `wiki-source-of-truth-governance` enforces. |

**Open questions for you:**
1. Quick mode (Option A) sound right as the first move, or do you want to jump to B / C?
2. For the Spectra county pipeline (Option C), which county is the pilot? Whatcom WA is already done; Bexar TX was started. Pick a 3rd?
3. Should the imported ktnCodes skills live under `~/.hermes/skills/icm-*` (cross-project) or under `/home/denni/wiki/hermes/skills/` (wiki-scoped)? Cross-project is the ktnCodes default; wiki-scoped keeps everything in the repo.

---

## 7. What I'm asking you to approve

Reply with one of:
- `proceed to build gate 1` — I write the 4 files (Option A)
- `proceed to build gate 2` — I do A + the 2 client sub-workspaces (Option B)
- `proceed to build gate 3` — I do A + B + the Spectra 5-layer pipeline (Option C)
- `yes` + your own scope — e.g. "yes but skip Veritas for now"

Per the wiki source-of-truth rule (2026-08-22), this plan sits in `drafts/` until you sign off. Nothing will touch `clients/`, `projects/`, or your actual repo configs without an unambiguous go.

---

## Appendix — file list this plan references

- Paper: <https://arxiv.org/abs/2603.16021>
- Repo (spec): <https://github.com/RinDig/Interpretable-Context-Methodology>
- Skills template: <https://github.com/ktnCodes/icm-template>
- Adjacent: <https://github.com/RinDig/icm-architect>
- KlickSmartAI wiki root: `/home/denni/wiki/`
- Current wiki AGENTS.md (graphify rules only): `/home/denni/wiki/AGENTS.md`
- Existing governance skill: `wiki-source-of-truth-governance`
