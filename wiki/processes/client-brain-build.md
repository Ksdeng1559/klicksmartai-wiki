---
title: "Client Brain Build — Intake → Knowledge Base → Continuous Improvement"
type: process
status: ACTIVE
created: 2026-08-28
owner: Dennis Eng (KlickSmartAI)
canonical_source: Notion "Client-Brain-Standard-Brand-Mission-Voice-and-Agent-Context" (page id `3ca9e94cf0a48165b3c8dff9b439409f`)
companion_skill: ~/.hermes/skills/productivity/client-brain-builder/
pilot_workspace: clients/veritas-developments/
layering: CBS knowledge layer lives INSIDE an ICM client workspace. It is a content substrate; the ICM skeleton (CLAUDE.md / IDENTITY.md / CONTEXT.md / _config/ / drafts/ / projects/ / deliverables/) is unchanged.
---

# Client Brain Build

A four-phase process that turns scattered intake material — transcriptions, scraped web pages, internal documents, Notion records — into a loadable, agent-ready client knowledge base. **Goal: continuous improvement, not one-shot capture.** Every cycle leaves the brain more accurate than the last.

> **Terminology.** **ICM** (KlickSmartAI shorthand) = **Interpretable / Interpretive Context Methodology** — the broader methodology for layered agent context. The 3-layer workspace pattern (Identity → Context → Config) is *one application* of ICM. The Client Brain Standard (CBS) used in this process is *another application* of the same methodology. When the user says "ICM workspace," they mean a workspace built on the methodology — not the specific 3-layer file layout. This process adds the CBS **knowledge layer** to an existing ICM workspace; it does not rebuild the workspace skeleton.

> ⚠ **Internal working knowledge only.** A client brain does not authorize external representation. Project economics, tenant status, financing terms, legal conclusions, and investment claims require verification + the applicable human approval before use with any investor, customer, partner, or the public.

---

## Why this exists

Without a standardized client context layer, every agent session either (a) starts cold and asks the same intake questions, or (b) loads stale fragments from MEMORY.md or conversation history. The fix is a **controlled, versioned substrate** that any agent can load in under 10 seconds and trust for the current task. The Notion canonical standard specifies the layout; this process specifies the *workflow* for building and maintaining it.

---

## The 4 phases

```
Phase 1: Discovery  →  Phase 2: Build  →  Phase 3: Validate  →  Phase 4: Operate
    │                      │                    │                     │
    ▼                      ▼                    ▼                     ▼
source inventory       CLIENT-BRAIN.md       client-review          monthly review
+ intake capture       + context/*.md        + 5 test assignments   + decision log
+ stakeholder map      + examples/ seeded    + cross-agent check     + version bump
```

### Phase 1 — Discovery

**Output:** `discovery-report-<client-slug>-<YYYY-MM-DD>.md` in the workspace root.

**Steps:**
1. **Identify the client owner + final approver.** Not the same person if the firm is founder-led and the principal is busy. Veritas: Dennis (writer) + David (approver, principal) + Daniel (relationship validator).
2. **Inventory authoritative sources.** Every place client knowledge currently lives:
   - Public: website, GitHub wikis, LinkedIn, regulatory filings, press releases, court records (property / UCC), third-party directories.
   - Semi-public: podcasts/webinars (transcripts), Zoom call recordings (transcripts), Facebook/Instagram public posts.
   - Internal: Notion workspace, CRM (Frappe, Attio, HubSpot), past deliverables, prior `drafts/`, prior `deliverables/`, prior intake forms.
   - Conversations: prior Hermes/ChatGPT sessions, prior email threads with the principal.
3. **Capture mission, outcomes, ICP, positioning, active offers.** Either from existing docs or from a short intake call. Ask: what does "good" look like for this client in 90 days?
4. **Collect 10–20 approved writing examples** the client already published or approved — emails, decks, web pages, investor memos. These seed `examples/approved/` and become the voice-of-record.
5. **Record compliance and privacy constraints.** Which jurisdictions? Which regulated activities? Which disclaimers are non-negotiable?

**Intake capture modes (mix freely):**
- **Transcription** — paste a Zoom/Teams call transcript, a podcast episode, or a recorded webinar; the skill extracts structured claims.
- **Web scraping** — feed a URL (use `scrapling` / `browser_exec` for JS-rendered sites; `web_extract` for static); the skill parses industry/positioning/service lines/team.
- **Document dump** — paste a Notion page export, a PDF, a DOCX; the skill chunks and classifies.
- **Structured interview** — a 20-question intake form (in the skill) the principal or proxy fills in.

**Notion source-of-truth rule (binding):** If a fact exists in both Notion and a markdown file, Notion wins. Markdown files are *controlled operational exports*. Never edit both — edit Notion, then run `client-brain-sync.py` to push.

### Phase 2 — Build

**Output:** `CLIENT-BRAIN.md` (router) + `context/{BRAND-VOICE, FACTS-AND-CLAIMS, COMPLIANCE, SERVICES-AND-OFFERS, SOURCES, DECISIONS}.md` + `examples/{approved, rejected}/`.

**Structure (canonical):**
```
<client-slug>/
├── CLIENT-BRAIN.md        # ≤ ~400 lines, loaded at every session start
├── context/
│   ├── BRAND-VOICE.md
│   ├── FACTS-AND-CLAIMS.md
│   ├── COMPLIANCE.md
│   ├── SERVICES-AND-OFFERS.md
│   ├── SOURCES.md
│   └── DECISIONS.md
├── examples/
│   ├── approved/
│   └── rejected/
├── skills/                # client-specific skills (optional)
├── deliverables/          # client-ready exports
├── research/              # raw research artifacts
├── drafts/                # AI work in progress (HITL gate)
├── projects/              # validated artifacts (source of truth)
└── archive/               # superseded context packs
```

**Build order (do not skip):**
1. **`CLIENT-BRAIN.md` (router) — write the 14 standard sections first.** Even if sections are sparse. This is the file every agent loads.
2. **`context/SOURCES.md` — link every authoritative system of record.** No content yet, just URLs/IDs/last-verified dates.
3. **`context/COMPLIANCE.md` — write the gates BEFORE any content.** Every other section is constrained by this.
4. **`context/BRAND-VOICE.md`** — derived from `examples/approved/` (which you populated in Phase 1 step 4).
5. **`context/FACTS-AND-CLAIMS.md` — every claim tagged Draft/Corroborated/Verified/Counsel-Approved + source_url_or_id + retrieved_at + expires_or_reverview_on.** The standard requires this evidence-governance layer (§13 of the Veritas brain). Don't ship "facts" without status.
6. **`context/SERVICES-AND-OFFERS.md`** — current offers, ICP, pricing status, qualification rules.
7. **`context/DECISIONS.md` — date/decision/owner/reason/supersedes.** Seed from prior VALIDATION_QUEUE rows. Every material change to the brain is logged here.
8. **`examples/rejected/`** — also seed this. Knowing what the client rejected is as load-bearing as knowing what they approved.

**File size discipline:**
- `CLIENT-BRAIN.md` ≤ ~400 lines (router stays router).
- Each `context/*.md` ≤ ~800 lines. If a file exceeds this, split it (`FACTS-AND-CLAIMS-projects.md`, `FACTS-AND-CLAIMS-team.md`).
- Total brain ≤ ~5,000 lines. Beyond that, the brain stops being loadable.

### Phase 3 — Validate

**Output:** `validation-report-<client-slug>-<YYYY-MM-DD>.md`.

**Definition of done (every box must tick):**
- [ ] Client identity + outcome explicit in `CLIENT-BRAIN.md` §1 + §2.
- [ ] Brand voice supported by ≥ 5 approved examples in `examples/approved/`.
- [ ] Every fact in `context/FACTS-AND-CLAIMS.md` has source + retrieved_at + status.
- [ ] Compliance rules + human-approval gates documented in `context/COMPLIANCE.md` and matched in `CLIENT-BRAIN.md` §8 + §10.
- [ ] Systems of record linked in `context/SOURCES.md`.
- [ ] Cross-client isolation tested (load Veritas brain, then Spectra brain, then KlickSmartAI self — verify no bleed).
- [ ] Context pack is versioned (`semver` in `CLIENT-BRAIN.md` frontmatter) + dated (`last_verified` + `review_frequency`).
- [ ] ChatGPT, Claude Code, and Hermes all pass the same 5 sample assignments (the Validation Questions below).
- [ ] Client owner approves the initial version.

**The 5 Validation Questions (run before any consequential deliverable):**
1. Which client workspace is active?
2. What is the intended business outcome + audience?
3. Which source contains the authoritative facts for this claim?
4. Which claims are approved for this use (status ≥ Verified)?
5. Who must approve the result before it ships?

If any answer is missing AND materially affects the output → pause for clarification.

**Test assignments (run all 5 in Phase 3, rerun in Phase 4 quarterly):**
1. *"Draft a one-paragraph elevator pitch for {client}."* — must use BRAND-VOICE only, no FABRICATED numbers.
2. *"List the 3 highest-value open opportunities for {client} this quarter."* — must cite SOURCES.md + DECISIONS.md.
3. *"What claim about {client}'s project economics can I use in a cold email today?"* — must consult FACTS-AND-CLAIMS.md status; reject anything below Counsel-Approved.
4. *"Write a Twitter/X post announcing {client}'s new project."* — must respect COMPLIANCE.md gates (Reg D, RESPA, license fee-splitting, etc.).
5. *"What did {client} decide last week?"* — must consult DECISIONS.md; reject anything older than `expires_or_reverview_on`.

### Phase 4 — Operate

**Cadence:** monthly review (or on material business change).

**Triggers for an out-of-cycle version bump:**
- New project / phase gate change (§16 stage gates).
- New compliance constraint (e.g., new jurisdiction, new regulated activity).
- Client approves a new voice sample (add to `examples/approved/`, bump version).
- Client rejects a sample (add to `examples/rejected/`, bump version, note in `DECISIONS.md`).
- Humanizer or agent model swap (rerun the 5 test assignments).
- Discovery that a load-bearing fact in `context/FACTS-AND-CLAIMS.md` was wrong (revert + log).

**The 1-way sync loop:**
```
Dennis approves change in Notion
            ↓
client-brain-sync.py runs (one-way Notion → markdown)
            ↓
semantic version incremented in CLIENT-BRAIN.md
            ↓
commit + checksum recorded
            ↓
distribution to ChatGPT / Claude Code / Hermes
            ↓
5 test assignments rerun
            ↓
superseded pack archived
```

**Never two-way edit.** A two-way sync creates ambiguity over which side is the canonical record. Notion = canonical (per standard); markdown = controlled operational export.

---

## Authority order (when sources conflict)

1. Current user instruction for the specific assignment.
2. Legal, compliance, privacy, and permission rules.
3. Approved client operating agreement + `CLIENT-BRAIN.md`.
4. Verified facts + claims register (`context/FACTS-AND-CLAIMS.md`).
5. Current brand + offer files (`context/BRAND-VOICE.md`, `SERVICES-AND-OFFERS.md`).
6. Dated decision log (`context/DECISIONS.md`).
7. General reusable skills (humanizer, etc.).
8. Agent defaults and assumptions.

A reusable skill may improve execution but cannot grant permission, replace verified client facts, or weaken a required disclaimer.

---

## Workflow + approval taxonomy (per client)

Every client brain defines three action classes:

| Class | Definition | Example |
|-------|------------|---------|
| **Green** | Agent may execute without human approval | Archive newsletter; ack receipt; routine internal task update |
| **Yellow** | Agent drafts; Dennis approves before execution | Investor/landowner/lender/tenant outreach; any proposal; any CRM material change |
| **Red** | Agent escalates; Dennis + (for relationship facts) relationship validator must approve | Securities-touching claims; return/IRR/lender-term figures; project stage advances; public economics |

Default Veritas taxonomy is in `context/COMPLIANCE.md` §10.

---

## Memory hygiene

- **Cross-workspace facts** (which LLM provider Dennis prefers, the wiki path convention) → MEMORY.md.
- **Client-specific facts** (David's phone number, Evermont rent comps) → that client's `CLIENT-BRAIN.md` + `context/FACTS-AND-CLAIMS.md`.
- **Never duplicate.** If a fact appears in both, the brain wins (more specific).

---

## Migration from older workspace patterns (ICM `_config/` knowledge content)

If the workspace predates this standard (Veritas does), don't delete the old files on day one. The migration is **hybrid, not in-place**, and is **content synthesis**, not a file move:

1. **Leave the ICM skeleton alone.** CLAUDE.md, IDENTITY.md, CONTEXT.md, drafts/, projects/, deliverables/, drafts-preview/, skills/ all keep working. They are *operational* (routing, gate, formatting) and are not replaced by CBS. `_config/` stays as the operational config layer.
2. **Create the new CBS knowledge layer alongside:** `CLIENT-BRAIN.md` + `context/{BRAND-VOICE, FACTS-AND-CLAIMS, COMPLIANCE, SERVICES-AND-OFFERS, SOURCES, DECISIONS}.md`.
3. **Synthesize, don't symlink blindly.** `_config/voice.md` is content for `context/BRAND-VOICE.md` — read the old file, re-author the new one with citation discipline. The old file keeps working in the meantime.
4. **Add a "Load order" section to `CLIENT-BRAIN.md`:** "After loading this file, agents MAY also load `_config/` files for legacy content not yet migrated. The canonical reference for brand voice, claims, compliance, services, sources, and decisions is the new layout."
5. **Run Phase 3 validation against both layouts; the CBS layout wins any conflict.**
6. **After one full Phase 4 cycle with no contradictions, archive the old `_config/*.md` files into `archive/_config_legacy_<date>/`** (do not delete — they remain auditable) and write a `BRIDGE.md` explaining the mapping.
7. **Update `IDENTITY.md`** (the legacy entry point) with a pointer to `CLIENT-BRAIN.md` and the `context/` folder.

This avoids the trap of "big bang migration day" where every active draft stops loading — and keeps the operational skeleton (which auto-loads on every Hermes/Claude Code session) untouched.

> **ICM clarification for migration:** `_config/` (voice.md, conventions.md, glossary.md, deliverables.md, gtm-skills.md, compliance.md) is the **operational config layer** of the ICM 3-layer pattern (Identity → Context → Config). It is *not* the knowledge substrate. The CBS *replaces* the knowledge content that was scattered through `_config/glossary.md` and `_config/voice.md`, but it does *not* replace the `_config/` folder — those files own per-deliverable skill bindings, voice rules for copy, conventions for naming, etc. that CBS does not cover.

---

## Reusable across clients (the test)

The standard is "reusable" when a brand-new client can be onboarded by following these 4 phases in sequence, with no client-specific rewrites of the process itself. The phase outputs are templated; only the *contents* are client-specific. If a phase requires more than ~2 hours of client-specific interpretation, simplify the phase.

**Goal: each new client brain takes ≤ 1 working day from intake to validated v1**, and improves continuously thereafter.

---

## Related artifacts

- **Skill:** `~/.hermes/skills/productivity/client-brain-builder/SKILL.md` — operational loader + scaffold script + sync script.
- **Canonical standard:** Notion `Client-Brain-Standard-Brand-Mission-Voice-and-Agent-Context` (`3ca9e94cf0a48165b3c8dff9b439409f`).
- **Pilot workspace:** `wiki/clients/veritas-developments/` — first workspace to migrate to the new layout.
- **Companion processes:**
  - `wiki/processes/seo-client-onboarding-sprint.md` — vertical-specific onboarding sprint (runs on top of this process).
  - `wiki/processes/seo-organic-growth-playbook.md` — content playbook built once the client brain exists.