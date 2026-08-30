# Open Knowledge Format (OKF) — KlickSmartAI Profile

> **Attribution:** This document adapts [Open Knowledge Format v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) (Google Cloud Platform, Aug 2026) for the KlickSmartAI wiki + ICM client-workspace pattern. **The canonical spec lives upstream.** When OKF evolves to v0.3+, refresh the canonical first, then update this profile. If they diverge, upstream wins.
>
> **Why this exists:** Our ICM client workspaces (e.g. Veritas) are already structured the way OKF describes — directory of `.md` files, with `CLAUDE.md`/`IDENTITY.md`/`CONTEXT.md` for progressive disclosure. OKF gives us **vendor-neutral frontmatter** so any LLM (Claude, ChatGPT, Hermes, Gemini, Mistral, anything that reads markdown) can ingest a client workspace as a knowledge graph without installing any of our skills. This profile pins how we apply the spec.

---

## 1. What OKF gives us (in one paragraph)

OKF makes five questions answerable from frontmatter alone:

1. **What is this?** → `type` (and optional `title` / `description`)
2. **Where did it come from?** → `sources[]` with credibility signals
3. **How much should I trust it?** → `verified` (human-reviewed > machine-confirmed > unverified) and `generated.by`
4. **Is it still true?** → `stale_after` and `status` (draft | stable | deprecated)
5. **Is it callable?** → For `type: Attested Computation`, `parameters[]` + `executor` + `attester` — the contract that turns a `.md` into a function

That last one is what unlocks "any skill becomes a callable function." A Playbook with parameters + an executor reference IS callable from any LLM — no Hermes skill install needed.

## 2. Bundle structure (how a client workspace IS an OKF bundle)

```
<client-slug>/
├── index.md                  # NEW — bundle manifest (was CLAUDE.md's role; see §4)
├── CLAUDE.md                 # Hermes/Claude adapter (still loadable, but type-tagged)
├── IDENTITY.md               # type: Client Workspace
├── CONTEXT.md                # type: Client Engagement
├── README.md                 # human-facing overview
├── _config/
│   ├── voice.md              # type: Reference
│   ├── conventions.md        # type: Reference
│   ├── deliverables.md       # type: Reference (vertical artifact map)
│   ├── gtm-skills.md         # type: SkillBinding
│   ├── glossary.md           # type: Glossary
│   └── compliance.md         # type: Compliance (only if compliance_mode != 'none')
├── drafts/<vertical>/        # type per draft (Lead Magnet, Email Sequence, Playbook, ...)
├── projects/<vertical>/      # validated; status: stable
├── deliverables/<vertical>/  # client-ready exports
├── drafts-preview/<vertical>/# HTML previews
└── sop/                      # NEW — company knowledge (Special SOPs and friends)
    └── <sop-name>.md         # type: Playbook
```

A bundle MUST, per §11 of the OKF v0.2 spec:
- have every non-reserved `.md` file with parseable YAML frontmatter carrying `type`
- use `index.md` and `log.md` only as reserved filenames (for their OKF meanings)
- tolerate missing optional frontmatter without rejecting the bundle

## 3. KlickSmartAI type vocabulary

OKF v0.2 §4.1 says `type` is not centrally registered — producers SHOULD pick descriptive self-explanatory values. Our vocabulary, with examples:

| `type` | When | Example file | Notes |
|---|---|---|---|
| `Client Workspace` | The bundle root | `IDENTITY.md` | One per client |
| `Client Engagement` | Layer 1 routing | `CONTEXT.md` | The "what leaves this workspace" page |
| `Reference` | Stable rules / voice / glossary / conventions | `_config/voice.md` | Usually `status: stable`; rarely changes |
| `SkillBinding` | Per-client skill roster | `_config/gtm-skills.md` | Maps use-case → skill name; rewrites when tooling changes |
| `Compliance` | Reg D 506(b) / privacy / HIPAA stubs | `_config/compliance.md` | `status: stable`, `verified` by counsel when present |
| `Glossary` | Domain terms | `_config/glossary.md` | Add to it as research surfaces new terms |
| `Playbook` | A Special SOP, runbook, or multi-step procedure | `sop/cdfi-outreach-7-touch.md` | Body = steps; callable when `parameters[]` exists |
| `Lead Magnet` | `drafts/lead-magnet/*.md` | TAM list, county brief | `status: draft` until validated |
| `Email Sequence` | `drafts/email/*.md` | Cold outreach cadence | `status: draft` until preflight passes |
| `Landing Page` | `drafts/landing-page/*.md` | Founder page, deck | `status: draft` until VALIDATION_QUEUE approves |
| `Content Article` | `drafts/content/*.md` | Blog, FAQ | |
| `Deck` | `drafts/deck/*.md` | Investor deck | |
| `Ad Creative` | `drafts/ad-creative/*.md` | Hook + body + visual brief | |
| `Video Ad` | `drafts/video-ad/*.md` | Script + storyboard | |
| `Website` | `drafts/website/*.md` | Page spec | |
| `Attested Computation` | Runnable, attestable procedure | `sop/youtube-subtitle-attestation.md` | Adds `runtime` + `parameters[]` + `executor` + `attester` |
| `Notebook` | An open question / WIP research | `intelligence/<task-slug>/notebook.md` | |
| `Source Material` | A transcript, dataset, or doc that other concepts cite | `intelligence/<task>/sources/*.md` | |

**Convention:** keep `type` short, Title-Case, no special chars. New types are fine — consumers MUST tolerate unknown types per OKF §11. Add to this table when you mint one.

## 4. The bundle-root entry: index.md vs CLAUDE.md

OKF §8 lets a bundle-root `index.md` carry `okf_version: "0.2"` in its only-allowed frontmatter. We adopt that — **`index.md` is the OKF manifest; `CLAUDE.md` stays as the Hermes/Claude adapter** that auto-loads on folder entry.

A bundle-root `index.md` for a client workspace should look like:

```markdown
---
okf_version: "0.2"
manifest:
  client: veritas-developments
  version: 2026-08-29
  generator: icm-client-workspace-setup v1.0.0
---

# Veritas Development Group LLC — Bundle Index

> Progressive disclosure: read this file, then read `IDENTITY.md`, then `CONTEXT.md`. That is enough orientation to act.

## Knowledge graph (top level)

* [Identity](IDENTITY.md) — who is the client, principals, engagement
* [Context](CONTEXT.md) — what leaves this workspace, current pipeline stage
* [Configuration](_config/) — voice, conventions, compliance, GTM bindings
  * [Voice](_config/voice.md) — type: Reference
  * [GTM Skills](_config/gtm-skills.md) — type: SkillBinding
  * [Compliance](_config/compliance.md) — type: Compliance
* [Drafts](drafts/) — AI work in progress, pre-validation
* [Projects](projects/) — validated source-of-truth deliverables
* [Deliverables](deliverables/) — client-ready exports
* [SOPs](sop/) — Special SOPs and runbooks

## How to ingest this bundle

Any LLM that reads markdown can ingest by following:
1. This `index.md` (manifest)
2. [`IDENTITY.md`](IDENTITY.md) (who/why)
3. Any concept via path-aware markdown link (the graph is self-describing)

No skill install required. No API gateway. If the consumer can read YAML frontmatter, it can read OKF.
```

**`CLAUDE.md` keeps its current role** (Hermes/Claude folder-entry adapter pointing at IDENTITY.md / CONTEXT.md / VALIDATION_QUEUE.md). Do NOT delete CLAUDE.md — agents still auto-load it.

## 5. Frontmatter required + recommended

Every non-reserved `.md` file in the workspace MUST carry at minimum:

```yaml
---
type: <Type from §3 vocabulary>
---
```

That's the OKF v0.2 conformance floor (§11).

**Recommended for any concept an external LLM might load:**

```yaml
---
type: Playbook                            # from §3 vocabulary
title: CDFI 7-touch outreach cadence      # human-readable
description: Sequential cadence for faith-aligned CDFIs; verified against Reg D 506(b).
tags: [sop, cdfi, cold-outreach]         # optional, recommended for search
status: stable                            # draft | stable | deprecated — default stable if absent
generated: { by: human:dennis, at: 2026-08-29T14:00:00Z }
verified:
  - { by: human:david_poole, at: 2026-08-29T14:00:00Z }
  - { by: human:daniel_bailey, at: 2026-08-29T14:00:00Z }
sources:
  - id: reg-d-506b-rule
    resource: /_config/compliance.md
    title: Reg D 506(b) compliance overlay
stale_after: 2027-08-29T00:00:00Z        # optional
---
```

**Trust tier** (derived by the consumer, OKF §5.3): unverified → machine-confirmed → **human-reviewed** (any `verified` entry with `human:` prefix).

## 6. Actor convention (KlickSmartAI profile)

Per OKF §7, we adopt `<producer>/<version>` for agents, `human:<id>` for people, `process:<id>` for automated processes. Our local catalog:

**People (humans):**
- `human:dennis` — KlickSmartAI founder; gates all paid runs and client comms
- `human:david_poole` — Veritas Founder & Principal; gate for Veritas relationship-touching drafts
- `human:daniel_bailey` — Veritas Co-founder & RE advisor; gate for Veritas RE advisory content
- `human:<id>` — every named client principal; mint as needed

**Agents:**
- `kimi-k3/<version>` — primary model
- `deepseek-chat/<version>` — fallback model
- `reference_agent/<model>` — when an agent generates reference content for downstream bundles

**Processes:**
- `process:seo-weekly-audit` — weekly SEO audit pipeline
- `process:deepline-credit-reconciler` — nightly Deepline credit reconciliation
- `process:<id>` — mint for any automated pipeline that needs a stable identity in OKF

**Why the `human:` prefix matters:** consumers key trust tier off it. If you forget the prefix on a person-authored draft, the consumer will treat it as machine-confirmed and may promote it externally under the wrong trust signal. **Don't omit `human:` for hand-authored content.**

## 7. The source-of-truth gate = OKF lifecycle

Our existing gate (`drafts/` → `projects/` → `deliverables/`) maps onto OKF §5.4 `status` cleanly:

| Workspace location | OKF status | Trust tier | Notes |
|---|---|---|---|
| `drafts/<vertical>/*.md` | `status: draft` | unverified or `verified: human:dennis` | Pre-HITL |
| `projects/<vertical>/*.md` | `status: stable` | human-reviewed (Dennis + relevant client reviewer) | Source of truth |
| `deliverables/<vertical>/*` | `status: stable` | human-reviewed | Client-ready export |
| `_config/*.md` | `status: stable` | human-reviewed by Dennis | Stable rules |
| `sop/*.md` (Special SOP) | `status: stable` | human-reviewed by the SOP owner | |
| `intelligence/<task>/WIP.md` | `status: draft` | unverified | Open research |
| Deprecated content | `status: deprecated` | any | Kept for links / history |

OKF v0.2 says absent `status` ⇒ `stable`. We deliberately set `status: draft` on every draft so consumers (and agents) can tell at a glance what's source-of-truth vs AI-WIP.

## 8. Cross-linking convention

Per OKF §6: bundle-relative paths beginning with `/` are recommended (stable when documents move within their subdirectory). We adopt that.

```markdown
See [Identity](/IDENTITY.md) for principals.
See the [Reg D overlay](/_config/compliance.md) §3 for accredited-investor gating.
This SOP cites the [CDFI TAM list](/intelligence/cdfi-tam-2026-08-22/notebook.md).
```

When citing a source listed in frontmatter `sources[]`, use a markdown footnote keyed to `sources[].id`:

```markdown
Founder relationships are pre-existing substantive relationships under Reg D 506(b).[^reg-d-overlay]

[^reg-d-overlay]: /_config/compliance.md §3
```

The footnote label is the join key into `sources[]`. Consumers resolve attribution through the matching entry, not by parsing footnote prose (per OKF §5.1).

## 9. "Any skill becomes a callable function" — the pattern

This is the payoff. A consumer (Claude Code, ChatGPT, a script — anything that reads the bundle) can:

1. Open `index.md` → see the bundle manifest
2. Walk frontmatter `type` filter → find all `type: Playbook` or `type: Attested Computation`
3. For each, read `parameters[]` + `executor` to learn the call signature
4. Invoke: supply values for the named parameters, follow the `executor.resource` to run, return a receipt
5. Verify: read `attester.resource` and run the deterministic attester against the receipt

**Minimal example — a callable SOP:**

```markdown
---
type: Playbook
title: CDFI 7-touch outreach — call signature
description: Run the 7-touch CDFI outreach cadence for a named lead list.
parameters:
  - { name: leads_csv, type: string, required: true, description: "path to CSV with name, email, organization, tier columns" }
  - { name: tier_filter, type: string, required: false, description: "tier values to include (default: 1,2)" }
  - { name: cadence_start, type: date, required: true, description: "ISO date for touch 1" }
executor:
  resource: /sop/run-cdfi-cadence.py
  receipt: [lead_ids_processed, touch_log, draft_paths, validation_queue_row]
attester:
  resource: /sop/attesters/verify-cdfi-cadence.py
generated: { by: human:dennis, at: 2026-08-29T14:00:00Z }
verified:
  - { by: human:david_poole, at: 2026-08-29T14:00:00Z }
stale_after: 2027-02-28T00:00:00Z
sources:
  - id: reg-d-overlay
    resource: /_config/compliance.md
    title: Reg D 506(b) compliance overlay
  - id: cdfi-tam-2026-08-22
    resource: /intelligence/cdfi-tam-2026-08-22/notebook.md
    title: CDFI TAM list (2026-08-22)
---

# CDFI 7-touch outreach — call signature

You are the cadence runner. The user supplies leads_csv + cadence_start. Optional tier_filter.

## Pre-conditions
- Reg D 506(b) overlay honored (pre-existing relationships only).[^reg-d-overlay]
- Every lead has name + email + organization + tier ≥ 1 in the source CSV.
- VALIDATION_QUEUE row created before touch 1 fires.

## Steps
1. Load leads_csv. Filter by tier_filter (default tiers 1, 2).
2. For each lead, build 7-touch email cadence:
   - Touch 1: handshake (Day 0)
   - Touch 2: signal acknowledgment (Day 3)
   - ...

## Receipt format
Touch 1..7 draft paths in `drafts/email/<lead-slug>/`, plus the VALIDATION_QUEUE.md row.
```

A ChatGPT or Claude or Hermes — none of which has KlickSmartAI skills installed — can read this file, understand the inputs, look at `executor.resource`, run the cadence, and check `attester.resource` for compliance. The folder becomes the knowledge graph, and any LLM is the consumer.

## 10. Verifying OKF conformance

For a workspace to be **conformant**, per OKF §11:

1. Every non-reserved `.md` file has parseable YAML frontmatter
2. Every frontmatter carries a non-empty `type`
3. Reserved filenames (`index.md`, `log.md`) follow §8 / §9 conventions

Lightweight check we can use anywhere:

```bash
ROOT=/home/denni/wiki/clients/<slug>
# every .md except index.md / log.md must have YAML frontmatter
ok=1
while IFS= read -r f; do
  case "$(basename "$f")" in
    index.md|log.md) continue ;;
  esac
  first=$(head -n1 "$f")
  [ "$first" = "---" ] || { echo "MISSING-FRONTMATTER: $f"; ok=0; continue; }
  # frontmatter must have 'type:'
  awk 'BEGIN{c=0} /^---$/ {c++; next} c==1 {print}' "$f" | grep -q '^type:' || { echo "MISSING-type: $f"; ok=0; }
done < <(find "$ROOT" -name '*.md' -type f)
[ $ok = 1 ] && echo "OKF conformant: $ROOT"
```

This is the same gate the ICM walk test runs (in spirit). Run it before declaring a workspace OKF-portable.

## 11. What does NOT change

We adopt OKF as a **frontmatter convention, not a structural refactor.** Everything we already have keeps working:

- ICM folder structure — unchanged
- `CLAUDE.md` — unchanged (still auto-loaded by Hermes/Claude); just gains a sister `index.md`
- `IDENTITY.md`, `CONTEXT.md` — unchanged content; gain frontmatter
- `_config/*.md` — unchanged content; gain frontmatter per file
- Per-vertical `drafts/` `projects/` `deliverables/` — unchanged folders; gain frontmatter per file
- `VALIDATION_QUEUE.md` — stays as the source-of-truth gate ledger
- `references/icm-method.md` — already a verbatim copy; gains OKF frontmatter if reused as a concept

The cost is **per-file frontmatter blocks.** The benefit is **any LLM on the planet can ingest a Veritas workspace** as a typed, attested, trust-tiered knowledge graph — without installing a single skill.

## 12. Versioning

- We target OKF v0.2.
- A workspace declares its target by setting `okf_version: "0.2"` in the bundle-root `index.md` frontmatter (only place frontmatter is permitted in `index.md`, per OKF §8 + §12).
- When OKF bumps to v0.3+, refresh the canonical spec first, then update this profile, then sweep client workspaces if the conformance floor changes.

## 13. References

- **Canonical OKF v0.2 spec:** [github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) (1,006 lines, Aug 2026)
- Our KlickSmartAI profile: this file
- ICM method: `references/icm-method.md` (bundled with `icm-client-workspace-setup`)
- Client Brain Standard: `references/client-brain-standard.md` (sister content layer — OKF covers its structural frontmatter; CBS covers the citation discipline)
