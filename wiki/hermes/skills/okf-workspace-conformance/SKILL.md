---
name: okf-workspace-conformance
description: >-
  Migrate an existing folder of markdown into a conformant Open Knowledge Format
  (OKF v0.2) bundle — vendor-neutral, git-friendly, ingestable by any LLM
  without an SDK. Use when the user wants to (1) make a wiki/vault/notes folder
  "agent-readable," "OKF-conformant," "portable knowledge graph," (2) classify
  existing files by purpose and add minimal frontmatter, (3) audit whether a
  folder is OKF §11 conformant, (4) build callable Playbook SOPs, or (5) apply
  KlickSmartAI's HITL/provenance overlay on top of a basic OKF bundle. Bundles
  authored under icm-architect's `Knowledge bundle` form get OKF frontmatter
  added to their concept nodes. Pairs with the upstream `okf-knowledge-format`
  skill — defers to it on spec questions (only `type` is always-required; never
  reject a file for missing optional fields). KlickSmartAI-specific addition:
  the 7-question pre-migration interview + the HITL-gate trust overlay.
version: 1.0.0
created: 2026-08-29
revised: 2026-08-29
status: ACTIVE
owner: Dennis Eng / KlickSmartAI
canonical_spec: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md
paired_skill: okf-knowledge-format  # upstream; defer to it on spec questions
canonical_process: wiki/hermes/skills/icm-client-workspace-setup  # for new workspaces
---

# OKF Workspace Conformance

Migrate an existing folder of markdown into a conformant **Open Knowledge Format v0.2** bundle — the vendor-neutral, git-friendly, markdown+YAML-frontmatter spec from Google Cloud (`GoogleCloudPlatform/open-knowledge-format`). Any LLM (ChatGPT/Claude/Gemini/Hermes) can ingest the result without installing a skill or SDK.

## When to use this skill

**Use when:**

- A wiki, vault, notes folder, or doc set exists and the user wants it OKF-conformant.
- A folder built with `icm-architect`'s **Knowledge bundle** form needs OKF frontmatter added to its concept nodes.
- The user says "make this agent-readable," "OKF-conformant," "portable knowledge graph," "knowledge catalog," or asks for callable Playbooks.
- The user wants the KlickSmartAI HITL/provenance overlay (interview, trust tiers, validation queue) on top of plain OKF.

**Don't use when:**

- The user is **building** a workspace from scratch → use `icm-client-workspace-setup` (Step 2.5 already creates OKF-conformant `index.md`/`CLAUDE.md` from day 1; only run this skill on the legacy content).
- The user just wants to add frontmatter to **one** file → edit it directly, don't run a migration.
- The user wants a **runtime** for Attested Computations (the executor/attester code) — OKF defers that to the user's own systems; this skill only helps author the contract correctly.
- The folder is already 100% OKF-conformant (run `check-conformance.sh` first to confirm).

## Relationship to upstream `okf-knowledge-format`

This skill **does not replace** the upstream `okf-knowledge-format` skill — it's a KlickSmartAI wrapper that adds:

| Concern | Upstream skill | This skill |
|---|---|---|
| Bundle structure + concept authoring | authoritative | references |
| "What fields are required?" (only `type`) | authoritative | references |
| Attested Computation contract authoring | authoritative | references, defers to user's runtime |
| Auditing an existing bundle | authoritative | references |
| 7-question pre-migration interview | — | **adds** (KlickSmartAI-specific) |
| `clarify`-driven intake for new clients | — | **adds** |
| Path-pattern-based classifier | — | **adds** (`scripts/migrate-frontmatter.py`) |
| HITL-gate trust overlay (verified.by human:dennis + validation queue) | — | **adds** |
| Conformance check shell script | prose only | **adds** (`scripts/check-conformance.sh`) |
| Callable Playbook authoring recipe | brief mention | **adds** (`references/callable-playbook-pattern.md`) |

**Rule of deference:** If the upstream skill and this skill disagree, **upstream wins on spec questions** (what's required, what counts as conformant). This skill wins on workflow questions (when to interview, how to gate HITL).

## Relationship to `icm-architect`

Two orthogonal concerns:

- **icm-architect** answers *where does this file live and what stage produced it* — folder numbering, stage contracts, human gates, the six forms.
- **OKF** answers *what does this specific knowledge file look like* — frontmatter fields, how it links to other concepts, how a consumer judges whether to trust it.

If a folder was built with `icm-architect`'s `Knowledge bundle` form (concept nodes with typed frontmatter), this skill can add OKF's provenance/trust/lifecycle fields on top. Don't fight `icm-architect`'s folder convention — OKF's bundle structure and ICM's `Knowledge bundle` skeleton are meant to nest, per the upstream skill.

## Quick reference: what OKF §11 actually requires

Per upstream OKF v0.2 §11, a bundle is conformant if and only if:

1. Every non-reserved `.md` file has a parseable YAML frontmatter block.
2. Every frontmatter block has a non-empty `type` field.
3. `index.md` and `log.md`, where present, follow §8/§9.

**That is it.** `title`, `description`, `resource`, `tags`, `sources`, `generated`, `verified`, `status`, `stale_after`, `Attested Computation` — **all optional, all additive.** A concept carrying just `type: Foo` is fully conformant.

**Never reject a bundle for missing optional fields, unknown `type` values, unknown extra keys, or broken cross-links.** This is the upstream skill's guardrail and KlickSmartAI adopts it.

The KlickSmartAI overlay (`verified`, `generated`, `sources` blocks with `human:dennis` actors) is an **opinion, not a requirement.** Apply it when the workspace is client-facing or agent-managed; skip it for static reference material.

## Workflow

### 1. Interview (run once per workspace, before any migration)

Use the `clarify` tool to lock seven decisions that shape the migration. **Do not skip** — every "I'll figure it out as I go" decision costs a re-run later.

| # | Question | Why it matters |
|---|---|---|
| 1 | **Type vocabulary style** — pick short descriptive strings (`Metric`, `API Endpoint`, `Playbook`) per OKF default, or use the KlickSmartAI extended set (`Client Workspace`, `VAL Queue Row`, `SkillBinding`, etc.)? | Determines whether the workspace leans vendor-neutral or KlickSmartAI-canonical. |
| 2 | **Primary reviewer** — who signs off on promoted content (default `human:dennis` for KlickSmartAI)? | Goes into every `verified.by`. |
| 3 | **Secondary reviewers** — for client workspaces, who else signs off (e.g. `human:david` and `human:daniel` for Veritas)? | Client-engagement files need co-approval per the validation queue. |
| 4 | **Documented exceptions** — any files that MUST skip OKF (e.g. `CLAUDE.md` regenerated by graphify, auto-generated `index.md` catalogs)? | Prevents the migrator from clobbering these. |
| 5 | **Callable SOPs** — which SOPs are agents supposed to be able to invoke as Playbooks (with `parameters[]` + `executor` + `attester`)? | Drives Playbook authoring in step 4. |
| 6 | **Trust tier policy** — strict (every concept needs `generated` + `verified`) or loose (only drafts/deliverables need verification)? | Drives whether to overlay the KlickSmartAI HITL fields. |
| 7 | **Bundle-root `index.md` content** — should it be a directory listing (OKF §8 default), a knowledge-graph ingestion manifest, or both? | Determines the entry surface for external LLMs. |

Record the answers in a scratch file like `_okf-interview.md` at the bundle root before running migration — it's the migration config.

### 2. Classify each file

Walk the bundle and assign a `type:` value per file. Use `scripts/migrate-frontmatter.py` (in `--dry-run` first) — its default rules handle the common cases:

| Path pattern | `type` | `status` |
|---|---|---|
| `IDENTITY.md` (root) | `Client Workspace` | `stable` |
| `CONTEXT.md` (root) | `Client Workspace` | `stable` |
| `README.md` (root) | `Reference` | `stable` |
| `_config/*` | `Reference` (or `Compliance`/`Glossary`/`SkillBinding` by inspection) | `stable` |
| `sop/*` | `Playbook` | `stable` |
| `drafts/**` | (per-content; default `Reference`) | `draft` |
| `projects/**` | (per-content; default `Client Engagement`) | `stable` |
| `deliverables/**` | (per-content; default `Deliverable`) | `stable` |
| `*.archived.md` | `Archived` | `deprecated` |

**Override defaults when you have content knowledge** — a `_config/compliance.md` is `Compliance`, not `Reference`; a `_config/gtm-skills.md` is `SkillBinding`, not `Reference`.

**Don't force a closed taxonomy.** OKF v0.2 explicitly says type values are not centrally registered — pick descriptive strings, don't hunt for a canonical list.

### 3. Migrate frontmatter

```bash
# 1. Dry-run first (always)
python3 scripts/migrate-frontmatter.py /path/to/bundle --dry-run

# 2. Apply (idempotent — re-run anytime)
python3 scripts/migrate-frontmatter.py /path/to/bundle

# 3. Verify
bash scripts/check-conformance.sh /path/to/bundle
```

The migrator is **idempotent** — running it twice on the same bundle is a no-op. It handles three cases:

1. **No frontmatter** → inserts a YAML block (default = MINIMAL: `type` + `title` + `description` + `status` + `tags`; with `--strict`, also `okf_version` + `generated` + `verified` + `stale_after` + `sources` where applicable).
2. **Existing non-OKF frontmatter** (e.g. legacy `title`/`date`/`client` blocks) → preserves existing keys and inserts `type:` as the first key. Does NOT touch existing fields, even in `--strict` mode.
3. **Already-OKF frontmatter** → reports `ALREADY-CONFORMANT`, no edit.

**Default mode** (minimal) matches upstream OKF v0.2 §11 exactly — only `type` is required, so emitted blocks are sparse. Use this for static reference bundles, internal vaults, or when adopting OKF for the first time.

**`--strict` mode** adds the KlickSmartAI HITL overlay (`okf_version` + `generated` + `verified` with `human:dennis` actor by default). Use this for client-facing or agent-managed bundles where trust tier signals matter.

### 4. Author callable Playbooks (SOPs)

If the interview surfaced callable SOPs, author each as a `type: Playbook` concept with a parameters block, executor, and attester. See `references/callable-playbook-pattern.md` for the full recipe and a worked example (`sop/cdfi-7-touch-outreach.md`).

### 5. Verify conformance

```bash
bash scripts/check-conformance.sh /path/to/bundle
# Exits 0 if conformant; 1 if any file violates §11.
# Reserved filenames (index.md, log.md, CLAUDE.md) are excluded.
# Documented exceptions (from interview #4) are listed as EXCEPTION, not ERROR.
```

### 6. Add `index.md` and `log.md` (where they earn their keep)

Don't scaffold `index.md` for a 2-file folder. Add one when the bundle root has ≥5 concepts OR when external LLMs need a discovery surface. Template: see upstream skill's `assets/templates/index.md`.

`log.md` is per-directory chronological history (date-headed, newest-first). Append to it on every promotion event.

## Pitfalls (do these things and you'll be sorry)

1. **Don't bulk-rewrite content** — proposal before edit. Upstream skill is explicit: "bulk-rewriting a client's existing docs without a review pass is a good way to silently break something they relied on."
2. **Don't demand fields beyond `type`** to call something conformant. A first-pass catalog of static reference material doesn't need `generated`/`verified` blocks.
3. **Don't invent a credibility score.** OKF records signals (`author`, `usage_count`, `last_modified`); consumers infer trust. Never store a subjective score.
4. **`stale_after` is an absolute instant, not a TTL.** Always ISO 8601 with explicit UTC offset (`2026-12-31T00:00:00-07:00`), never "expires in 90 days."
5. **Attested Computation is a standalone concept, not a frontmatter block inside a Metric doc.** A Metric links to it; doesn't inline the computation contract.
6. **Don't clobber `CLAUDE.md`** — for KlickSmartAI workspaces it's regenerated by `graphify` and is a documented exception (rationale lives in `index.md`).
7. **Don't write ad-hoc OKF scripts** — always use `scripts/migrate-frontmatter.py`. The classifier rule set lives there in one place; ad-hoc scripts drift.
8. **Don't rename `index.md` or `log.md`** — those are reserved filenames at every level of the hierarchy per OKF §3.1.
9. **Don't use relative links** — prefer bundle-relative absolute (`/tables/customers.md`) over `../tables/customers.md` so concepts survive moves.
10. **Don't bypass the interview.** Type vocabulary + primary reviewer + secondary reviewers + exceptions + callable SOPs + trust tier policy + index.md style — every "I'll figure it out as I go" decision costs a re-run.

## Verification checklist

Before declaring a workspace OKF-conformant, verify:

- [ ] `check-conformance.sh` exits 0 on the bundle root.
- [ ] Every documented exception is listed in `index.md` with a one-sentence rationale.
- [ ] Every callable SOP (from interview #5) is a `type: Playbook` concept with `parameters[]` + `executor` + `attester`.
- [ ] Every `deliverables/` file has `verified.by: human:<primary-reviewer>` and a non-empty `sources[]`.
- [ ] `index.md` exists at the bundle root (if ≥5 concepts) and follows OKF §8.
- [ ] `log.md` exists at the bundle root (if any promotions have happened) and follows OKF §9.
- [ ] The migrator reports `0 INSERT, 0 INSERTED-TYPE, N ALREADY-CONFORMANT` on re-run (idempotency proof).
- [ ] An external LLM (ChatGPT web, Claude.ai) can ingest the bundle root and correctly summarize the workspace structure without any skill installation.

## Companion files

- `scripts/check-conformance.sh` — OKF §11 conformance check (re-runnable)
- `scripts/migrate-frontmatter.py` — bulk-migrator (idempotent, `--dry-run`, `--strict`)
- `references/okf-type-vocabulary.md` — KlickSmartAI extended type glossary + classification priority
- `references/callable-playbook-pattern.md` — Playbook authoring recipe with worked example

## Sources

- OKF v0.2 spec: https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md (Google Cloud Platform, Apache 2.0)
- Upstream skill: `okf-knowledge-format` (paste from `icm-architect` repo — not yet checked in)
- Method: Interpretable Context Methodology (Van Clief & McDermott, arXiv:2603.16021)
