# OKF Type Vocabulary — KlickSmartAI Profile

**Upstream rule (OKF v0.2 §4.1, authoritative):** type values are **not** centrally registered. Producers SHOULD pick values that are descriptive and self-explanatory; consumers MUST tolerate unknown types gracefully. **Never reject a document for an unrecognized type.** This glossary is a starting menu drawn from KlickSmartAI bundles in production (Veritas, others) — not a registry. New bundles may invent new types freely; pick something a human reader can guess from the name.

This document collects the types the KlickSmartAI OKF v0.2 bundles use in practice, the per-vertical content types for client-engagement folders, and the classification priority order the migrator follows.

[... middle unchanged ...]

## Anti-patterns (per OKF upstream guardrails)

- **Don't make up a "Registry" or "Catalog" type for a folder index.** `index.md` is reserved and has its own §8 structure; it doesn't carry `type:`.
- **Don't invent a "Confidence" or "Trust" type.** Trust is derived from `verified.by` per OKF §5.3, never stored as a type or a numeric score.
- **Don't use namespaced types like `org:Metric` or `client:Playbook`.** Plain `Metric` and `Playbook` work; the folder path encodes the namespace.
- **Don't inherit upstream's "BigQuery Table", "API Endpoint", "Metric" examples verbatim** unless the concept actually describes those exact things. They are upstream examples, not part of the vocabulary.

## Canonical OKF §3 vocabulary (the base)

| Type | Use for | Status default | Verified default |
|---|---|---|---|
| `Index` | Bundle-root `index.md` (bundle manifest) | `stable` | primary reviewer |
| `Client Workspace` | `IDENTITY.md` (workspace identity card) | `stable` | primary reviewer |
| `Client Engagement` | `CONTEXT.md` (engagement-level context) | `stable` | primary reviewer |
| `Reference` | Catch-all for reference docs (voice, conventions, deliverables, READMEs) | `stable` | primary reviewer |
| `Compliance` | Regulatory overlay (Reg D 506(b), GDPR, HIPAA, FINRA) | `stable` | counsel or primary reviewer |
| `Glossary` | Term glossary (definitions, abbreviations, domain vocabulary) | `stable` | primary reviewer |
| `SkillBinding` | Skill-binding files (`_config/gtm-skills.md`, `_config/seo-skills.md`) | `stable` | primary reviewer + skill author |
| `Playbook` | Callable SOP (`parameters[]` + `executor` + `attester`) | `stable` | SOP author + named reviewer |
| `Concept` | Abstract idea without an underlying asset | varies | varies |
| `Attested Computation` | Sanctioned computation (script + attester test) | `stable` | computation author |
| `Archived` | Legacy / superseded content (read-only, deprecated) | `deprecated` | (none) |

## Per-vertical content types (drafts/)

These are used for content artifacts inside `drafts/` and `drafts-preview/`. They map to OKF §3's "per-vertical type" extension — OKF §11 explicitly allows consumers to tolerate unknown types, so adding new ones does not break ingestion.

| Type | Use for |
|---|---|
| `Lead Magnet` | PDF / spreadsheet / checklist offered in exchange for an email |
| `Email Sequence` | Multi-step email outreach cadence |
| `Email Draft` | Single email draft |
| `Email Campaign` | One-shot broadcast campaign |
| `Email Template` | Reusable email template with merge fields |
| `Landing Page` | Single landing page (long-form copy + design spec) |
| `Content Article` | Long-form blog / LinkedIn / Medium article |
| `Deck` | Slide deck (PowerPoint / Keynote / HTML PPT) |
| `Ad Creative` | Single paid ad creative (image + copy + placement) |
| `Video Ad` | Short-form video ad (TikTok / Reels / YouTube Shorts) |
| `Website` | Multi-page website specification |

## Per-deliverable types (projects/ + deliverables/)

| Type | Use for |
|---|---|
| `Reference` | Default for client-facing deliverables that don't fit a more specific type |
| `Investor Brief` | Reg D / 506(b) investor outreach |
| `County Intelligence Report` | Spectra county-level MCF intelligence |
| `Co-Sponsor Brief` | Multi-party co-sponsor coordination document |
| `Partnership Memo` | CDFI / partnership documentation |

When a deliverable doesn't fit any of these, use `Reference` and add a tag indicating the content domain.

## Classification priority order

When migrating a bundle, classify each file by following these rules in order:

1. **Reserved filenames** (`index.md`, `log.md`) → leave alone.
2. **Known exceptions** (from interview Q4, recorded in `index.md` body) → leave alone.
3. **Pre-existing OKF-conformant files** (first line `---` + has top-level `type:`) → leave alone.
4. **Pre-existing non-OKF frontmatter** (first line `---` but no top-level `type:`) → insert `type:` as first key (preserve all other fields).
5. **All other files** → classify by path pattern:

| Path pattern | Type | Status | Verified |
|---|---|---|---|
| `<root>/README.md` | `Reference` | `stable` | primary reviewer |
| `<root>/_archive_*` or any path containing `deprecated` / `-old` | `Archived` | `deprecated` | (none) |
| `<root>/_config/voice*.md` | `Reference` | `stable` | primary reviewer |
| `<root>/_config/conventions.md` | `Reference` | `stable` | primary reviewer |
| `<root>/_config/deliverables.md` | `Reference` | `stable` | primary reviewer |
| `<root>/_config/glossary.md` | `Glossary` | `stable` | primary reviewer |
| `<root>/_config/compliance.md` | `Compliance` | `stable` | primary reviewer |
| `<root>/_config/gtm-skills.md` | `SkillBinding` | `stable` | primary reviewer + skill author |
| `<root>/_config/seo-skills.md` | `SkillBinding` | `stable` | primary reviewer + skill author |
| `<root>/_config/okf-bundle.md` | `Reference` | `stable` | primary reviewer |
| `<root>/_config/*.md` (any other) | `Reference` | `stable` | primary reviewer |
| `<root>/sop/*.md` | `Playbook` (if callable) or `Reference` | `stable` | SOP author + named reviewer |
| `<root>/drafts/<vertical>/README.md` | `Reference` | `stable` | primary reviewer |
| `<root>/drafts/<vertical>/<file>.md` (content) | per-vertical type | `draft` | (none — not yet reviewed) |
| `<root>/projects/<vertical>/README.md` | `Reference` | `stable` | primary reviewer |
| `<root>/projects/<vertical>/<file>.md` (content) | per-vertical type | `stable` | primary reviewer + client reviewer |
| `<root>/deliverables/<vertical>/README.md` | `Reference` | `stable` | primary reviewer |
| `<root>/deliverables/<vertical>/<file>.md` | per-vertical type | `stable` | primary reviewer + client reviewer |
| `<root>/drafts-preview/...` | mirror of drafts/ | `draft` | (none) |
| `<root>/projects-preview/...` | mirror of projects/ | `stable` | primary reviewer |
| `<root>/skills/...` | `Reference` | `stable` | primary reviewer |
| **Catch-all** | `Reference` | per content review | per content review |

## Title derivation rule

When migrating a file with no frontmatter, derive the `title:` field from the filename:

- Take the filename stem (without `.md`)
- Replace `_` and `-` with spaces
- Title-case the result

Examples:
- `drafts/email-sequence-1.md` → `Email Sequence 1`
- `projects/prime-lees-summit-co-sponsor-brief.md` → `Prime Lees Summit Co Sponsor Brief`
- `_config/voice-styles.md` → `Voice Styles`

If a more descriptive title is needed, hand-edit after migration.

## Description derivation rule

Extract the first non-heading paragraph from the file body, truncate to 150 chars. Strip markdown links (keep label) and emphasis markers.

If the file has no usable first paragraph, use `(no description)` as a placeholder and hand-edit later.

## Status field semantics

| Status | Meaning | Trust tier requirement |
|---|---|---|
| `draft` | Work in progress; not yet reviewed | Unverified OK |
| `stable` | Reviewed and approved for use | Human-reviewed (`verified[].by` starts with `human:`) |
| `deprecated` | Superseded by newer content; kept for history | (none — consumers should warn or skip) |

Promoting a file from `draft` → `stable` requires:
1. `verified[]` populated with at least one `human:` entry.
2. `generated.by` updated to the reviewing human.
3. The change recorded in the bundle's `log.md` (if present).

## Verified actor convention

OKF §5.4 defines three actor prefixes:

| Prefix | Use for |
|---|---|
| `human:<name>` | A specific human (e.g. `human:dennis`, `human:david_poole`) |
| `<producer>/<version>` | An agent (e.g. `okf-workspace-conformance/1.0.0`) |
| `process:<id>` | An automated process (e.g. `process:nightly-audit`) |

**Rule:** if a human wrote the file but the migration script wrote the frontmatter, the `generated.by` should still be the human (the script is the assistant, not the author). Reserve `agent:` for files where the agent produced the entire content.

## Tags convention

Tags are a free-form list of lowercase-kebab identifiers. Use them for cross-cutting concerns:

- `reg-d-506b` for compliance-tagged content
- `cdf-fund` for CDFI-related content
- `email-sequence` for email cadences
- `cold-outreach` for outbound campaigns
- `county-intelligence` for Spectra-style county research
- `faith-framed` for faith-framed investment content
- `drafts`, `projects`, `deliverables` to mark file role
- `vertical:<slug>` to mark the vertical (e.g. `vertical:jackson-county-mo`)

Consumers SHOULD tolerate unknown tags (OKF §11).
