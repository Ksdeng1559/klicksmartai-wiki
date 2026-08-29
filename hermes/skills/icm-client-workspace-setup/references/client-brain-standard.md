# Client Brain Standard (KlickSmartAI) — condensed knowledge bank

> **Source:** Notion page `3ca9e94cf0a48165b3c8dff9b439409f` (canonical URL: `https://brindle-guppy-146.notion.site/Client-Brain-Standard-Brand-Mission-Voice-and-Agent-Context-3ca9e94cf0a48165b3c8dff9b439409f`).
> **Retrieved:** 2026-08-28 via Notion API (`GET /v1/blocks/{id}/children?page_size=100`, paginated). **Do not re-fetch via `web_extract` — Notion share-link is bot-gated.**
> **Status:** Binding contract for all new client workspaces after 2026-08-28. Supersedes earlier ad-hoc `_config/voice.md` patterns for new clients; existing workspaces must migrate on next touch.

---

## Why this standard exists

A client workspace has many sources of truth: Notion, GitHub wikis, the company website, transcripts of calls, the client themselves. Without a canonical structure, the agent mixes layers — quoting a casual meeting note as if it were counsel-approved, or using a draft webpage as if it were published copy. The **Client Brain Standard** (CBS) defines the file layout, authority order, and operating model that prevents this.

The CBS is **the migration target** for workspaces still using the older ICM 3-layer pattern. See the parent skill's "Backporting / migrating" section + `references/backporting-existing-clients.md` for the procedure.

---

## The contract at a glance

### File layout (replaces bare `IDENTITY.md`/`CONTEXT.md`)

```
~/wiki/clients/<slug>/
├── CLIENT-BRAIN.md            # Short router — points at context/ files
├── CLAUDE.md                  # Hermes + Claude Code entry-point (auto-loaded)
├── README.md                  # Human-facing overview
└── context/
    ├── BRAND-VOICE.md         # Tone, audience, dos/don'ts, samples
    ├── FACTS-AND-CLAIMS.md    # Every load-bearing claim, with evidence tags
    ├── COMPLIANCE.md          # Reg D / RESPA / license / broker-dealer etc.
    ├── SERVICES-AND-OFFERS.md # What the client sells, to whom, at what
    ├── SOURCES.md             # Provenance ledger — every URL/id/owner/retrieved_at
    └── DECISIONS.md           # Decision register — what was decided, by whom, when
```

**The router rule:** `CLIENT-BRAIN.md` is intentionally short. It is a *table of contents* that tells the agent which file holds which knowledge, with a one-line summary of each. The agent opens the specific context file only when a task needs it. This keeps CLAUDE.md / IDENTITY.md-style files from becoming god files.

### The 8-tier authority order (binding)

When sources conflict, this is the resolution order — higher tier wins:

| Tier | Source | Agent behavior |
|------|--------|----------------|
| 1 | **Current user instruction** in this conversation | Follow literally until superseded |
| 2 | **Legal / compliance / regulatory** (SEC, RESPA, state bar, FDA…) | Hard constraint; refuse to violate even on user instruction if tier 1 conflicts |
| 3 | **Approved agreement + CLIENT-BRAIN.md** (signed contract + the brain itself) | The client's own canonical truth |
| 4 | **Verified facts** in `FACTS-AND-CLAIMS.md` with status `Verified` or `Counsel Approved` | Cite as fact |
| 5 | **Brand voice + services** in `BRAND-VOICE.md` / `SERVICES-AND-OFFERS.md` | Use for client-facing copy |
| 6 | **Decisions** in `DECISIONS.md` | Honor as binding for the engagement |
| 7 | **Reusable skills** (playbooks, intake flows, deliverable templates) | Apply when relevant |
| 8 | **Agent defaults** (training data, common practice) | Lowest priority — only when no higher-tier source covers the question |

**Practical rule:** if the agent is about to assert a fact and cannot trace it to tier 4+, it must say so explicitly ("Not in FACTS-AND-CLAIMS.md; based on agent default") or hold the assertion until verified.

### Action taxonomy (Green / Yellow / Red)

Every agent action falls into one of three bands:

- **Green** — autonomous: research, score, prepare drafts, summarize sources, draft copy into `drafts/`. No approval needed.
- **Yellow** — draft + present + wait: anything that produces client-facing copy, calls/meetings, internal CRM updates. Dennis must approve before the artifact is promoted from `drafts/` to `projects/`.
- **Red** — explicit human approval required, every time: send any communication, sign any agreement, make any financial commitment, change compliance status, advance a project stage, delete records, represent the client externally in any form.

**The hard rule:** no agent action may bypass the band it's in. Even on user instruction, a Red action cannot be auto-executed — the agent must surface the proposed action and wait for the second, unambiguous approval.

### The 4-phase process

1. **Discovery** — gather sources (transcription, web scraping, knowledge-base assembly). Output: raw intake bundle.
2. **Build** — synthesize the intake into the `context/*.md` files. Draft everything into `drafts/` first, never write to `context/` directly.
3. **Validate** — Dennis reviews each `context/*.md` against `FACTS-AND-CLAIMS.md` for citation discipline. Promote from `drafts/` to `context/` only on explicit approval.
4. **Operate** — agent reads `CLIENT-BRAIN.md` (router) + the specific `context/*.md` files as needed for each task. Every new claim still goes through Discovery → Build → Validate.

### Notion ↔ markdown sync

Notion is the **human-edited source** for client knowledge; markdown in `~/wiki/clients/<slug>/context/*.md` is the **controlled operational export**. The sync is:

- **One-way: Notion → markdown.** Notion wins; markdown is regenerated from it.
- **Version bump required** when the export changes. The brain records `last_synced_at` + a version number on every page.
- **Markdown edits are forbidden outside the export.** If something in markdown is wrong, fix it in Notion and re-export. This prevents drift.
- The export script pattern lives at `scripts/export-client-brain.py` (see paired skill).

### Citation discipline (the bit most agents skip)

Every load-bearing claim in `context/*.md` must be tagged:

```markdown
- [claim text]{source: <url|id>, owner: <person>, retrieved_at: <ISO>, effective_date: <ISO>, status: Draft|Corroborated|Verified|Counsel Approved, approved_for_external_use: true|false, expires_or_reverify_on: <ISO>}
```

No bare assertions. "Veritas has 22 years of experience" without a source is not a fact the agent may repeat externally.

---

## Migration from the older ICM pattern

Existing clients (Veritas, GPC, OpenSEO internal) use:

```
~/wiki/clients/<slug>/
├── IDENTITY.md                # Workspace map + rules
├── CONTEXT.md                 # Pipeline routing
├── CLAUDE.md                  # Hermes adapter
├── _config/
│   ├── voice.md
│   ├── conventions.md
│   ├── deliverables.md
│   ├── gtm-skills.md
│   ├── glossary.md
│   └── compliance.md
└── projects/, drafts/, deliverables/, drafts-preview/, skills/
```

**Mapping to CBS:**

| Old | New | Notes |
|-----|-----|-------|
| `IDENTITY.md` | `CLIENT-BRAIN.md` (router) + small section in `CLAUDE.md` | CBS treats the router as separate from the adapter |
| `CONTEXT.md` | absorbed into `CLIENT-BRAIN.md` | Pipeline is now part of the brain router |
| `_config/voice.md` | `context/BRAND-VOICE.md` | |
| `_config/conventions.md` | small section in `CLIENT-BRAIN.md` | |
| `_config/glossary.md` | embedded in `context/SERVICES-AND-OFFERS.md` | |
| `_config/compliance.md` | `context/COMPLIANCE.md` | CBS adds citation tags |
| `_config/deliverables.md` | `context/SERVICES-AND-OFFERS.md` | Merged with services |
| `_config/gtm-skills.md` | embedded in `CLAUDE.md` (operational) | CBS separates operational from knowledge |
| _(new)_ | `context/FACTS-AND-CLAIMS.md` | The key new file — every claim tagged |
| _(new)_ | `context/SOURCES.md` | Provenance ledger |
| _(new)_ | `context/DECISIONS.md` | Decision register |

**Migration is non-destructive.** Old `_config/` files remain valid as content sources; the new `context/*.md` files are *synthesized from them*. Move on next workspace touch — do not bulk-migrate unless the user requests.

---

## Pilot workspaces

The standard recommends running two pilots to stress-test it:

- **Veritas Development** — high-complexity (multi-tier authority, Reg D, RESPA, broker-dealer concerns, securities-touching decisions). Good stress test for the citation discipline and the action taxonomy.
- **KlickSmartAI (self)** — low-complexity, single-principal (Dennis), no compliance regime. Good stress test for the router pattern and the Notion↔markdown sync.

A new client (Acme, etc.) should be built on CBS from day one. A legacy client should migrate on next touch.

---

## When to invoke the paired skill

The paired skill is `client-brain-builder`. Invoke it when:

- User says "build the brain for X" / "set up the client knowledge base" / "intake the transcript into the workspace"
- A new client is being onboarded and the CBS router (`CLIENT-BRAIN.md`) does not exist
- The user pastes a transcript, calls a meeting recording, or points at a source URL and says "add this to the brain"
- The agent is about to write into `context/` directly (it shouldn't — should route through Discovery → Build → Validate)

Do NOT invoke for: scaffolding a workspace without knowledge content (use `icm-client-workspace-setup`); SEO-specific intake (use `client-onboarding-sprint`); pure structural edits to existing `context/*.md` files (use `patch` directly after verifying authority tier).

---

## Key references in this standard

- The 8-tier authority order is the spine — every judgment hangs off it.
- The action taxonomy (Green/Yellow/Red) is the second spine — every agent action hangs off it.
- The citation discipline is the third spine — every assertion hangs off it.
- The Notion↔markdown sync is operational plumbing, not a doctrinal statement.
