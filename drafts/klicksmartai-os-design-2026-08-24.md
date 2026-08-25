# KlickSmartAI OS — Design Report
**Status:** Draft for HITL review
**Author:** Hermes (Chief of Staff)
**Date:** 2026-08-24
**Goal:** Give Dennis a single document to design the **operating system that runs client workspaces** — not a per-client product, but the chassis every client workspace plugs into.

---

## 0. Executive Summary

**One sentence:** KlickSmartAI OS is a **filesystem-first, agent-native, HITL-gated** workspace chassis that gives every KlickSmartAI client the same six-layer operating model — Intake → IDENTITY → SIP (voice) → _config (rules) → Skills → Output — while keeping the per-client binding (GTM skills, compliance overlay, reviewers) fully client-owned.

**Why now:** You already have the prototype. The Veritas workspace (`clients/veritas-developments/`) is the **reference implementation**. It has `IDENTITY.md`, `CONTEXT.md`, `_config/voice.md`, `_config/compliance.md`, `_config/gtm-skills.md`, `_config/deliverables.md`, `CLAUDE.md`, `drafts/` → `projects/` → `deliverables/`, a `VALIDATION_QUEUE.md` HITL gate, and 8 verticals with default-skill bindings. **The job is to (a) generalize the pattern, (b) codify the onboarding, (c) name the layers, and (d) make the HITL gate enforceable everywhere.**

**Three design decisions baked in:**
1. **The filesystem is the OS.** No new runtime, no new database. Folders + plain markdown + a single Google Sheet for cross-client task tracking.
2. **Two layers, not one.** A **chassis** (universal, owned by KlickSmartAI) and a **binding** (per-client, owned by the client reviewer + Dennis). The chassis never changes for a client; the binding is the only thing they customize.
3. **HITL is non-negotiable and structural.** The `drafts/` → HITL → `projects/`/`deliverables/` gate is the OS's safety system. Paid runs route through `gtm-enrichment-planner` + Deepline CLI; investor-touching outreach routes through `cold-email-preflight` + compliance overlay.

**Recommended build path:** Charter doc (this file) → `os-chassis` skill → `client-onboard` skill → run the chassis against the existing 11 clients to retrofit them → ship the **KlickSmartAI OS — Charter + Onboarding Pack** as a public-facing asset.

---

## 1. What Problem Does KlickSmartAI OS Solve?

### 1a. The current pain (verified against the wiki, 2026-08-24)

You have **11 client workspaces** in `~/wiki/clients/`. Their structures are wildly inconsistent:

| Client | Has IDENTITY.md | Has CONTEXT.md | Has _config/ | Has gtm-skills.md | Has VALIDATION_QUEUE | Has AGENTS.md |
|---|---|---|---|---|---|---|
| veritas-developments | ✅ | ✅ | ✅ (6 files) | ✅ | ✅ | ✅ (CLAUDE.md) |
| spectra-holdings (lowercase) | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| wattbricks | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| idc-insurance | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| leadsniper-3.0 | ❌ (README.md) | ❌ | ❌ | ❌ | ❌ | ❌ |
| breakthrough-mgmt | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| dare2dream-mortgage | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| eng-and-company | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| insurance-direct-canada | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| tiyo-energy | (empty) | — | — | — | — | — |
| SpectraHoldings (capital S, deprecated) | (separate doc-tree) | — | — | — | — | ✅ |

**Only Veritas is OS-shaped.** Everything else is a folder of artifacts. The good news: that means the pattern works. The bad news: it doesn't scale — every new client is a from-scratch re-design, every existing client needs retrofitting, and you can't tell at a glance which clients are in what state.

### 1b. The 15-day usage pattern (from `hermes insights`)

Across 170 sessions / 6,539 messages / 3,335 tool calls in the last 15 days:
- **Top skill: `b2b-outreach-intelligence-pipeline`** (29 loads, **25 edits**) — the most-edited skill in the window. The pipeline you actually run is evolving in place.
- **`google-workspace` (38)** is the most-loaded skill — Gmail/Drive/Sheets is the daily ops backbone.
- **`chief-of-staff-briefing` (29)** + 138 cron sessions + 7AM cron peak — the CoS morning-briefing cadence is functioning.
- **`icm-client-workspace-setup` (26)** — you onboard new clients frequently. The OS must make that **one-shot + repeatable + standardized**.

**Implication:** every minute you spend retrofitting existing clients manually is a minute stolen from new client onboarding. **KlickSmartAI OS is the answer to: "I want to add a 12th client in 30 minutes, not 3 hours."**

### 1c. What "OS" actually means here

It does **not** mean a runtime, a SaaS product, a CLI, or a code framework. It means:

> **A standardized filesystem chassis + a small set of universal skills + a HITL gate** that any KlickSmartAI client workspace plugs into. The chassis is KlickSmartAI IP. The binding is client-owned.

This is **ICM (Interpretable Context Methodology)** formalized as a product. The Aug 22 ICM draft already recommended it for the wiki root + 2 clients. **KlickSmartAI OS is the production version of that recommendation.**

---

## 2. The Six-Layer Architecture

Every client workspace has the same six layers. **Layers 1, 2, 5 are universal chassis (KlickSmartAI owns).** **Layers 3, 4, 6 are client-owned bindings.**

```
┌────────────────────────────────────────────────────────────────────────────┐
│ Layer 6 — OUTPUT (client-owned)                                            │
│   drafts/  →  projects/  →  deliverables/  +  drafts-preview/  +  VALIDATION_QUEUE.md │
│   "What the client receives. Always HITL-gated."                            │
├────────────────────────────────────────────────────────────────────────────┤
│ Layer 5 — SKILLS (chassis, with client binding)                              │
│   _config/gtm-skills.md  +  /gtm-enrichment-planner  +  universal skill stack │
│   "Which skills are bound for this client. What is blocked. HITL cost gate." │
├────────────────────────────────────────────────────────────────────────────┤
│ Layer 4 — COMPLIANCE OVERLAY (client-owned)                                 │
│   _config/compliance.md  +  Reg D 506(b) / CASL / FINRA / HIPAA / etc.       │
│   "What we cannot say, where we cannot send, who must approve."             │
├────────────────────────────────────────────────────────────────────────────┤
│ Layer 3 — SIP / VOICE (client-owned)                                        │
│   _config/voice.md  +  _config/glossary.md  +  (optional) SIP.json          │
│   "How the client sounds. What words they use. What tone. What ICP pain vocabulary." │
├────────────────────────────────────────────────────────────────────────────┤
│ Layer 2 — ROUTING (chassis)                                                 │
│   CONTEXT.md  +  CLAUDE.md / AGENTS.md                                       │
│   "Where do I go for what task? What is the session-start protocol?"         │
├────────────────────────────────────────────────────────────────────────────┤
│ Layer 1 — IDENTITY (chassis)                                                │
│   IDENTITY.md  +  README.md                                                  │
│   "What is this workspace? What are its folders and rules?"                 │
├────────────────────────────────────────────────────────────────────────────┤
│ Layer 0 — INTAKE (chassis — KlickSmartAI discovery process)                  │
│   /workspace-intake form  +  vertical detection  +  ICP extraction           │
│   "How did this client get here. Who approves onboarding."                  │
└────────────────────────────────────────────────────────────────────────────┘
```

### 2a. Layer 0 — Intake (chassis, KlickSmartAI-owned)

**Purpose:** convert a new opportunity into a structured onboarding package.
**Inputs:** client name, domain, vertical, contact, deal stage.
**Outputs:** `drafts/intake/<client>.md` + row in master Google Sheet + CRM record.
**Skill:** `workspace-intake` (NEW — to be built).
**Owner:** KlickSmartAI (Dennis).
**HITL gate:** Dennis approval before workspace scaffold is created.

### 2b. Layer 1 — Identity (chassis)

**Purpose:** tell any agent "where am I."
**Files (canonical templates):**
- `IDENTITY.md` — workspace map (folders + rules), ~800 tokens. The hero file.
- `README.md` — human-readable overview, 1 page.
**Universal rules (always present):**
1. AI-generated client content → `drafts/` first, never `projects/` or `deliverables/`.
2. HITL gate: `drafts/VALIDATION_QUEUE.md` is the source of truth for promotion.
3. Never auto-send client outreach.
4. Skills in `~/.hermes/skills/` > ad-hoc code.
5. Cron outputs → `outputs/cron/` (per workspace convention).
**Skill:** `client-workspace-scaffold` (NEW — derived from existing `icm-client-workspace-setup`).
**Reference impl:** `clients/veritas-developments/IDENTITY.md` is the canonical example.

### 2c. Layer 2 — Routing (chassis)

**Purpose:** tell any agent "where do I go for what."
**Files:**
- `CONTEXT.md` — task → destination table (~300 tokens).
- `CLAUDE.md` / `AGENTS.md` — auto-generated Hermes/Claude adapter (loads the right files in order).
**Key principle:** routing is **virtual stages by default** (like Veritas's 5-stage pipeline: intake → research → draft → review → publish). Only promote to **physical stage folders** when a pipeline repeats ≥3 times.
**Skill:** `client-workspace-scaffold` (shared with Layer 1).
**Reference impl:** `clients/veritas-developments/CONTEXT.md` + `CLAUDE.md`.

### 2d. Layer 3 — SIP / Voice (client-owned)

**Purpose:** the client sounds like the client, not like a vendor.
**Files:**
- `_config/voice.md` — tone rules, register, sentence-level patterns.
- `_config/glossary.md` — domain terms (CDFI, MCF, CLT, AUM, …).
- `_config/conventions.md` — file naming, version rules, citation style.
- (Optional, for Financial Services verticals) `_config/SIP.json` — the BOSS-SIP persona layer.
**Skill:** `voice-loader` (skill that reads `_config/voice.md` and injects it into every draft).
**Reference impl:** Veritas has all four. Wattbricks has none.
**Note:** BOSS-SIP is the canonical persona format for Financial Services clients. It can be adopted (or simplified) for non-FS verticals.

### 2e. Layer 4 — Compliance Overlay (client-owned)

**Purpose:** state the rules that block certain actions.
**Files:**
- `_config/compliance.md` — what the client cannot do (Reg D 506(b) for Veritas, FINRA for IDC Insurance, HIPAA for any healthcare vertical, CASL for any Canadian client, etc.).
**Universal chassis rule:** if `_config/compliance.md` is missing, **the workspace defaults to "all compliance modes on"** — the safest fallback. Agents must read it before any investor-facing, healthcare-touching, or cross-border communication.
**Skill:** `compliance-preflight` (NEW — derived from `cold-email-preflight` but generalized).

### 2f. Layer 5 — Skills (chassis + client binding)

**Purpose:** bind universal GTM skills to this client's use cases, block what should be blocked.
**Files:**
- `_config/gtm-skills.md` — use-case → skill bindings + role bindings + blocked + overrides.
- `_config/deliverables.md` — vertical → folder convention → default skill (Veritas's 8-vertical map is the prototype).
**Universal chassis stack (every workspace inherits):**
- `gtm-enrichment-planner` — 5-layer orchestration (Plan → Discover → Enrich → Score → Outreach).
- `gtm-enrichment-planner` HITL approval format — every paid run.
- `compliance-preflight` — every external send.
- `wiki-source-of-truth-governance` — every `drafts/` → `projects/` promotion.
- `voice-loader` — every draft (loads `_config/voice.md`).
**Client-specific overrides ALWAYS win** (per Veritas's documented runtime rule).
**Skill:** `gtm-enrichment-planner` (already exists; the binding file is the per-client layer).

### 2g. Layer 6 — Output (chassis structure, client-owned content)

**Purpose:** every artifact the workspace produces has a folder.
**Canonical structure:**
```
drafts/                    ← AI-generated, NEVER ship until HITL
  VALIDATION_QUEUE.md      ← HITL gate ledger
  <vertical>/              ← flat files at drafts/ root are legacy validated work
  intake/                  ← Layer 0 outputs land here
projects/                  ← source of truth (promoted from drafts/ after HITL)
deliverables/              ← client-ready exports (built from projects/)
drafts-preview/            ← HTML/MD previews for HITL review (build.py + styles.css)
outputs/cron/              ← automated run outputs (subagent logs, etc.)
archive/                   ← deprecated work, kept for traceability
```
**Skill:** `wiki-source-of-truth-governance` (already exists — enforces the gate).
**Reference impl:** Veritas has all six folders + VALIDATION_QUEUE + drafts-preview/build.py.

---

## 3. The HITL Gate (Non-Negotiable, Structural)

The OS's safety system. Three gates, all structural — meaning they live in the file system, not in agent prompts.

### Gate 1 — Onboarding Gate (Layer 0 → Layer 1)
- New client workspace cannot be created without Dennis + designated client reviewer approval.
- Approval lives in: `intake/<client>-approval.md` (signed off before scaffold is built).

### Gate 2 — Promotion Gate (Layer 6 `drafts/` → `projects/`/`deliverables/`)
- No file moves from `drafts/` to `projects/` or `deliverables/` without a row in `drafts/VALIDATION_QUEUE.md` with status = APPROVED.
- Required approvers per file type:
  - **Marketing collateral** → Dennis
  - **Investor / capital-facing** → Dennis + David Poole (Veritas) / Daniel Bailey (Veritas RE) / equivalent
  - **Reg D 506(b) / securities** → Dennis + compliance reviewer
  - **Healthcare (HIPAA)** → Dennis + compliance reviewer
  - **Cross-border (CASL/CAN-SPAM)** → Dennis + compliance reviewer
- Skill enforcement: `wiki-source-of-truth-governance` rejects the move if no row exists.

### Gate 3 — Spend Gate (any paid API call)
- Every paid run (Deepline / LeadSniper / Clay / Hunter / Apollo / Tavily-deep / Exa / Parallel.ai) routes through `gtm-enrichment-planner` HITL approval format (Plan → Discover → Enrich → Score → Outreach), with credit-cost + scope + cap pre-disclosed.
- Dennis replies "yes" / "proceed" before any spend.
- Per Veritas's runtime rule: **Deepline CLI `plays` only — NEVER `tools execute`**.

### What the gate is NOT
- It's not a chat prompt. It's not "ask nicely before sending." It's a folder structure + a `VALIDATION_QUEUE.md` ledger + a skill that rejects non-conforming moves.
- It scales because it's structural — any agent (Hermes, Claude Code, a subagent) inherits the same rules by reading the same files.

---

## 4. Onboarding Flow (the chassis in action)

The new-client flow is **structured, HITL-gated, and one-shot.** Takes 30–60 minutes for the chassis; the binding (SIP/voice/GTM skills) is the next 2–4 hours.

### Step 1 — Intake (Layer 0, ~15 min)
**Inputs (Dennis provides):**
- Client name + slug (filesystem-safe)
- Domain + vertical (mortgage / insurance / wealth / real estate dev / community dev / SaaS / etc.)
- Primary contact + their role
- Deal stage (lead → proposal → signed → live)
- Compliance modes required (Reg D / FINRA / CASL / HIPAA / etc.)
- Existing client reviewer (the person who approves draft promotion on their behalf)

**Outputs:**
- `wiki/clients/<slug>/intake/<slug>-intake-YYYY-MM-DD.md` — captured brief
- Row added to master Google Sheet (`KlickSmartAI Task Sheet`) with status = `intake_complete`
- CRM record (when CRM is wired)

**Skill:** `workspace-intake` (NEW — see §6).

### Step 2 — Scaffold (Layers 1 + 2, ~30 min)
**Inputs:** completed intake file.
**Outputs (auto-generated):**
```
wiki/clients/<slug>/
├── IDENTITY.md          ← from template, populated with intake data
├── CONTEXT.md           ← from template, routing table stub
├── CLAUDE.md            ← auto-generated Hermes/Claude adapter
├── AGENTS.md            ← symlink/inherits from wiki AGENTS.md (graphify rules)
├── README.md            ← human-readable overview
├── drafts/
│   ├── VALIDATION_QUEUE.md   ← empty ledger with header
│   └── intake/<slug>-intake-YYYY-MM-DD.md   ← moved from intake/
├── projects/            ← empty
├── deliverables/        ← empty
├── drafts-preview/      ← empty (build.py + styles.css copied from chassis template)
└── outputs/cron/        ← empty
```

**Skill:** `client-workspace-scaffold` (NEW — derived from existing `icm-client-workspace-setup`, plus template files in `os-chassis/templates/`).

### Step 3 — Bind (Layers 3 + 4 + 5, ~2–4 hours)
**Inputs:** vertical detection, discovery call notes (if any), prior client artifacts.
**Outputs (per-client binding — client-owned):**
```
_config/
├── voice.md             ← tone, register, sentence patterns
├── glossary.md          ← domain terms
├── conventions.md       ← file naming, version rules
├── compliance.md        ← required compliance modes + blocked phrases
├── gtm-skills.md        ← use-case bindings + role bindings + blocked + overrides
└── deliverables.md      ← vertical → folder → default skill map
```
**Note:** if `_config/compliance.md` is missing, the workspace defaults to **all modes on** — safest. If `_config/gtm-skills.md` is missing, the workspace inherits the universal chassis stack with no overrides.

**Skill:** `client-binding-builder` (NEW — runs the SIP discovery questions from BOSS-SIP, maps answers to the binding files).

### Step 4 — Promote (HITL, Gate 2)
- Dennis + client reviewer review `drafts/intake/<slug>-intake-YYYY-MM-DD.md` + the scaffold files.
- Add a row to `drafts/VALIDATION_QUEUE.md` with status = APPROVED.
- Move/copy the intake artifact to `projects/intake/<slug>-intake-YYYY-MM-DD.md`.
- Workspace is now LIVE — agents can begin producing deliverables.

### Step 5 — First Deliverable (the chassis in production)
- Pick one existing artifact (or new request) and run it through the pipeline.
- Use `client-workspace-scaffold --first-deliverable <slug>` to invoke the scaffold skill with a default artifact type (e.g., "company snapshot" or "ICP brief").
- Review the output in `drafts-preview/`, then promote through `VALIDATION_QUEUE.md`.

---

## 5. Retrofitting the 11 Existing Clients

You don't have to rebuild from scratch. The retrofit is **additive** and **non-breaking**.

| Client | Missing | Retrofit action | Time |
|---|---|---|---|
| **veritas-developments** | nothing | — | — (reference impl) |
| **spectra-holdings (lc)** | IDENTITY.md, CONTEXT.md, _config/, VALIDATION_QUEUE | Run scaffold; write IDENTITY.md from `SpectraHoldings/index.md` + `SpectraHoldings/AGENTS.md`; adapt the gtm-skills.md binding from BOSS-SIP + Spectra's 8-agent system | ~3 hrs |
| **wattbricks** | All OS layers | Run scaffold; bind from `topical-authority-plan.md` (vertical = SEO/content); compliance = none | ~2 hrs |
| **idc-insurance** | All OS layers | Run scaffold; vertical = insurance; compliance = FINRA + state-level; SIP = use BOSS-SIP framework | ~3 hrs |
| **leadsniper-3.0** | All OS layers | Run scaffold; vertical = SaaS (internal product, not a client per se); compliance = none | ~2 hrs |
| **breakthrough-mgmt** | All OS layers | Run scaffold; vertical = community dev (urban mining); compliance = none | ~2 hrs |
| **dare2dream-mortgage** | All OS layers | Run scaffold; vertical = mortgage; compliance = state-level; SIP via BOSS-SIP | ~2 hrs |
| **eng-and-company** | All OS layers | Run scaffold; vertical = real estate dev; compliance = BC TOD / municipal | ~2 hrs |
| **insurance-direct-canada** | All OS layers | Run scaffold; vertical = insurance; compliance = provincial + IIROC | ~2 hrs |
| **tiyo-energy** | All (empty folder) | Run scaffold; vertical = energy / waste-to-value; intake first | ~3 hrs |
| **SpectraHoldings (capital S)** | Deprecated duplicate | **Archive** with a `DEPRECATED — use `clients/spectra-holdings/`` README.md redirect; do not retrofit | ~30 min |

**Total retrofit:** ~22 hrs of focused work across 2–3 days. The biggest wins are the 4 most-active clients (spectra-lc, veritas, wattbricks, idc-insurance) — those are where the OS pays back fastest.

### Archive vs delete

**Archive** anything you want to keep as historical record (move to `clients/_archive/<slug>/`). **Delete** only on explicit Dennis approval. The chassis skill should never auto-delete client folders.

---

## 6. What Needs to Be Built

### 6a. New skills (chassis-owned, KlickSmartAI IP)

| Skill | Purpose | Trigger | Depends on |
|---|---|---|---|
| **`os-chassis`** | The umbrella skill. Lists the 6 layers, the chassis stack, the HITL gates, the retrofit procedure. | When user says "OS", "chassis", "onboard", or invokes `/os-chassis` | — |
| **`workspace-intake`** | Layer 0 intake form. Captures the 7 fields (name, slug, domain, vertical, contact, deal stage, compliance modes). Writes to `drafts/intake/`. | New client opportunity | `os-chassis` |
| **`client-workspace-scaffold`** | Layers 1 + 2 scaffold. Creates IDENTITY.md, CONTEXT.md, CLAUDE.md, AGENTS.md, README.md, the 6 folders, and VALIDATION_QUEUE.md from templates. | Intake approved | `os-chassis`, `workspace-intake` |
| **`client-binding-builder`** | Layers 3 + 4 + 5 binding. Runs BOSS-SIP discovery questions; emits voice.md, glossary.md, conventions.md, compliance.md, gtm-skills.md, deliverables.md. | Scaffold approved | `os-chassis`, `boss-sip-onboarding` (skill form), `gtm-enrichment-planner` |
| **`voice-loader`** | Reads `_config/voice.md` + `_config/glossary.md` + `_config/SIP.json` and injects into every draft. | Any draft-producing skill | `os-chassis` |
| **`compliance-preflight`** | Reads `_config/compliance.md` and rejects any draft that violates it. Generalized from `cold-email-preflight`. | Any external send | `os-chassis`, `cold-email-preflight` |
| **`client-retrofit`** | Runs the retrofit procedure (table in §5) against an existing non-OS-shaped workspace. Asks Dennis for confirmation per client. | When user invokes `/os-chassis retrofit <slug>` | `os-chassis`, `client-workspace-scaffold` |

### 6b. Template files (chassis-owned)

```
os-chassis/
├── templates/
│   ├── IDENTITY.md.template
│   ├── CONTEXT.md.template
│   ├── CLAUDE.md.template
│   ├── AGENTS.md.template
│   ├── README.md.template
│   ├── drafts/VALIDATION_QUEUE.md.template
│   ├── drafts-preview/build.py.template
│   ├── drafts-preview/styles.css.template
│   └── _config/
│       ├── voice.md.template
│       ├── glossary.md.template
│       ├── conventions.md.template
│       ├── compliance.md.template
│       ├── gtm-skills.md.template
│       └── deliverables.md.template
├── references/
│   ├── six-layer-architecture.md        ← this report, slimmed
│   ├── retrofit-procedure.md            ← §5 of this report
│   └── hitl-gate-spec.md                ← §3 of this report
└── scripts/
    └── scaffold.py                      ← generates the workspace from templates + intake
```

### 6c. Skill patches (existing skills to update)

| Skill | Patch |
|---|---|
| `icm-client-workspace-setup` | Add a pointer to `os-chassis` for the full pattern. Keep ICM-specific framing but defer the chassis to `os-chassis`. |
| `wiki-source-of-truth-governance` | Add the structural gate (`drafts/VALIDATION_QUEUE.md` row required for promotion) explicitly to the skill body. |
| `gtm-enrichment-planner` | Add the per-client `_config/gtm-skills.md` resolution rule (already documented in Veritas; codify it as a skill step). |
| `klicksmartai-os-schematic` (existing) | The "for a new client" version of the same intent. **Rename/deprecate** or merge into `os-chassis`. Both currently exist; the merge prevents skill duplication. |
| `project/klicksmartai-os-schematic` (in `~/.hermes/skills/`) | Same — migrate content to `os-chassis/schematic-mode/` and delete the duplicate. |

### 6d. Master tracking

Add one **Master OS Registry** to the wiki root:
- `wiki/KLICKSMARTAI-OS-REGISTRY.md` — one row per client with columns: `slug | stage | os-shaped? | missing-layers | retrofit-priority | last-touched`.
- Cross-linked from each client's `IDENTITY.md` (`# Parent OS: KlickSmartAI OS — see [registry](../../KLICKSMARTAI-OS-REGISTRY.md)`).
- This is the one document you check to know the fleet state.

### 6e. Cron schedule additions

- **`os-health-check`** — weekly cron (Mondays 8 AM). Reads `KLICKSMARTAI-OS-REGISTRY.md`, walks each client's `IDENTITY.md`, checks for missing layers, posts a delta summary to your morning briefing.
- **`os-retrofit-reminder`** — one-shot reminders per retrofit target (3 weeks from kickoff).

---

## 7. Open Design Questions (Need Your Decision)

These are the decisions that block implementation. Each has a recommended default; flag any you want to override.

### Q1 — Charter scope: KlickSmartAI-internal-only or client-facing deliverable?
**Default:** internal-only at v1 (chassis is KlickSmartAI IP). Client-facing "KlickSmartAI OS — Client Charter Pack" comes at v2.
**Why:** the binding files contain client-specific compliance + reviewer info that shouldn't leak.

### Q2 — Single skill (`os-chassis`) or 7 skills (per §6a)?
**Default:** 1 umbrella + 5 satellite skills (collapse `voice-loader` into `os-chassis` — it's a 30-line helper, not a skill).
**Why:** fewer skills = less namespace pollution. Skill discovery is the failure mode; consolidation wins.

### Q3 — `_config/` (Veritas convention) vs `config/` vs `.config/`
**Default:** `_config/` (already established by Veritas).
**Why:** the leading underscore is a visual signal in `ls` — easy to spot at a glance. Other conventions exist but none are better.

### Q4 — Per-client Google Sheet tab or single shared sheet?
**Default:** single shared sheet (`KlickSmartAI Task Sheet`), per-client section via named range.
**Why:** you already have one master sheet per memory. Adding tabs per client = fragmentation.

### Q5 — Where does the chassis live on disk?
**Default:** `wiki/_meta/os-chassis/` (templates + scripts) + `~/.hermes/skills/os-chassis/SKILL.md` (the skill entry point).
**Why:** templates are wiki content (visible to all agents, versionable in Git); the skill is a runtime entry point.

### Q6 — Compatibility with Claude Code?
**Default:** generate both `CLAUDE.md` (Claude Code entry) and `AGENTS.md` (Hermes entry). Each is a 5-line pointer to the same files.
**Why:** per your memory, you want Hermes + Claude Code treated symmetrically.

### Q7 — What about the deprecated `SpectraHoldings/` (capital S) directory?
**Default:** archive with a redirect README. Don't auto-delete.
**Why:** historical record + traceability. Some docs reference it.

### Q8 — Master registry file location?
**Default:** `wiki/KLICKSMARTAI-OS-REGISTRY.md` (one row per client).
**Why:** sits at the wiki root, visible to all agents, one document to grep.

### Q9 — When does a workspace get a `_meta/` folder vs `_config/`?
**Default:** `_config/` for client-facing config; `_meta/` for chassis templates and internal-only references.
**Why:** keeps the boundary clear — `_config/` is the binding (client-readable), `_meta/` is the chassis (KlickSmartAI-internal).

### Q10 — Versioning the chassis
**Default:** semver on the chassis skill (`os-chassis` v1.0.0 at launch). Each template file gets a header `# Chassis v1.0.0 — do not edit for client-specific; clone instead`.
**Why:** prevents drift. If a client needs a non-standard layout, they should fork the template, not edit the chassis.

---

## 8. Build Sequence (4-Week Plan)

| Week | Deliverable | HITL gate |
|---|---|---|
| **W1 — Charter** | This document approved | Dennis signs off on §1–§7 |
| **W1 — Chassis skill v0.1** | `os-chassis` skill + 5 templates + `scaffold.py` script | Dennis approves scaffold output on a test slug |
| **W2 — Intake + Scaffold** | `workspace-intake` + `client-workspace-scaffold` skills; test against `tiyo-energy` (currently empty) | Dennis confirms scaffold matches §2 |
| **W2 — Binding** | `client-binding-builder` skill; test against `dare2dream-mortgage` (small, FS-vertical) | Dennis confirms binding files match BOSS-SIP shape |
| **W3 — Retrofit high-value clients** | spectra-holdings (lc), wattbricks, idc-insurance retrofitted in parallel | Dennis reviews each `IDENTITY.md` |
| **W3 — Master registry + cron** | `KLICKSMARTAI-OS-REGISTRY.md` + `os-health-check` cron | Dennis sees weekly fleet report |
| **W4 — Retrofit the rest + retro doc** | 4 remaining clients + `os-retrofit-reminder` cron + retro doc | Dennis confirms fleet is OS-shaped |
| **W4 — Launch** | Public-facing "KlickSmartAI OS — Charter" doc (Google Doc) + announcement | Dennis approves the launch asset |

**Stop after each week. Don't start the next week without HITL.**

---

## 9. What This Report Does NOT Cover (Deferred)

These came up during research; explicitly out of scope for v1, deferred:

- **Multi-tenant shared agents** — when 2+ clients in the same vertical run the same pipeline, the chassis should support a shared `vertical-stack/` directory. Deferred to v2.
- **Cross-client analytics** — weekly KPIs across all clients (meetings booked, deals closed, outreach sent) — needs a unified Supabase schema. Deferred to v2.
- **Client portal** — a read-only web view of each client's `projects/` + `deliverables/` for the client reviewer to approve drafts without seeing Hermes/Claude internals. Deferred to v2.
- **CRM sync** — the chassis should eventually write to a CRM (HubSpot / Pipedrive / Onyx). Currently each client has its own CRM pattern. Deferred.
- **Compliance certification** — a third-party audit of the chassis's HITL gate (probably overkill for v1).
- **Public "OS schematic" deliverable** — turning `klicksmartai-os-schematic` into a sellable GDoc deliverable for prospect demos. Deferred to v2.

---

## 10. Sources & Verifications

All claims in this report verified against:

- **Existing OS-shaped workspace:** `~/wiki/clients/veritas-developments/` (IDENTITY.md, CONTEXT.md, CLAUDE.md, _config/{voice,compliance,conventions,glossary,gtm-skills,deliverables}.md, drafts/VALIDATION_QUEUE.md, drafts-preview/build.py)
- **Existing chassis skills:** `~/.hermes/skills/icm-client-workspace-setup/`, `~/.hermes/skills/wiki-source-of-truth-governance/`, `~/.hermes/skills/gtm-enrichment-planner/`, `~/.hermes/skills/project/klicksmartai-os-schematic/SKILL.md`
- **Existing patterns:** `~/wiki/drafts/icm-implementation-plan-2026-08-22.md`, `~/wiki/boss-sip-onboarding.md`, `~/wiki/boss-raas-v3.md`, `~/wiki/klicksmartai-wiki-architecture.md`, `~/wiki/klick2client-os.md`, `~/wiki/rios-north-star-architecture.md`
- **Fleet inventory:** `ls ~/wiki/clients/` (11 workspaces, Aug 24 2026 snapshot)
- **Usage data:** `hermes insights --days 15` (170 sessions, 6,539 messages, 3,335 tool calls, Aug 10–24 2026)

**Unverified assumptions (flagged):**
- Dennis's preferred chassis naming (`_config/` vs `config/`). Veritas uses `_config/`; assumed canonical.
- Whether `os-chassis` should be one skill or seven. Default = umbrella + 5 satellites.
- Whether to archive or delete the deprecated `SpectraHoldings/` directory. Default = archive with redirect.

---

## 11. Next Step

**This document is the charter.** Read it. If you agree with §1, §2, §3, and §7's defaults, reply `proceed to build` and I'll:

1. Write the `os-chassis` skill (`~/.hermes/skills/os-chassis/SKILL.md`) + 5 template files + `scaffold.py` script
2. Test the scaffold against `tiyo-energy` (currently empty — safest test target)
3. Walk you through the resulting workspace for HITL approval before any retrofit work begins

If you want changes to any of §1–§7, reply with the section number and what to change. If you want to skip the charter phase and go straight to retrofitting the 4 high-value clients, say so and I'll proceed in that order.

**Estimate to v1 ship:** 4 weeks. **Cost:** ~22 hrs of focused work + the existing cron footprint. **Maintenance:** ~30 min/week once live (one cron health-check + occasional binding updates).
