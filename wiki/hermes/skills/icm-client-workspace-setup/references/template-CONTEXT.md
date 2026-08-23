# <client_name> — Routing

## What do you want to do?

### Workspace-level
| Task | Go to | Load first |
|------|-------|------------|
| Understand this workspace | `IDENTITY.md` | — |
| Run a new intake / discovery cycle | `drafts/` | `IDENTITY.md`, `_config/voice.md` |
| Continue work on a draft | `drafts/<draft-name>.md` (or `drafts/<vertical>/<draft>.md`) | `drafts/VALIDATION_QUEUE.md` (check gating) |
| Promote a validated draft | `projects/<artifact>.md` (or `projects/<vertical>/`) | `_config/compliance.md` if present, the draft itself |
| Build a client-ready export | `deliverables/` (or `deliverables/<vertical>/`) | the source artifact in `projects/` |
| Generate an HTML preview | `drafts-preview/build.py` (or `drafts-preview/<vertical>/`) | the draft's `.md` source |
| Apply a multi-stage pipeline | propose in `drafts/` first | `IDENTITY.md` |
| Change voice / conventions | `_config/` | `IDENTITY.md` |
| Update glossary | `_config/glossary.md` | the new term + citation |
| Update artifact-type map | `_config/deliverables.md` | the new vertical + default skill |
| Reach a principal or partner | **STOP** — draft outreach to Dennis first; never auto-send |

### Per-vertical (if `verticals` declared at scaffold time)
| Vertical | Folder convention | Default Hermes skill |
|----------|-------------------|----------------------|
| `website` | `drafts/website/`, `deliverables/website/<site>/` | `open-design-landing` |
| `landing-page` | `drafts/landing-pages/`, `deliverables/landing-pages/` | `saas-landing` |
| `content` | `drafts/content/`, `deliverables/content/` | `blog-post` |
| `email` | `drafts/emails/`, `deliverables/emails/` | `email-marketing` (or `cold-email`) |
| `video-ad` | `drafts/video-ads/`, `deliverables/video-ads/` | `hyperframes` or `video-shortform` |
| `ad-creative` | `drafts/ads/`, `deliverables/ads/` | `ad-creative` |
| `deck` | `drafts/decks/`, `deliverables/decks/` | `open-design-landing-deck` |
| `lead-magnet` | `drafts/lead-magnets/`, `deliverables/lead-magnets/` | `lead-magnets` |
| `doc` | `drafts/docs/`, `deliverables/docs/` | `docx` |
| `tech` | `drafts/tech/`, `deliverables/tech/` (code) | depends on stack |

---

## Session Start Protocol

1. Read `IDENTITY.md` — workspace map, stage map, rules.
2. Identify the task from the table above.
3. If the task touches a relationship assumption, open `drafts/VALIDATION_QUEUE.md` and confirm the draft is approved before doing anything.
4. If the task is a new deliverable, read `_config/voice.md` and (if present) `_config/compliance.md` before drafting.
5. Write all intermediate and final artifacts into the appropriate folder (drafts/, projects/, or deliverables/) — never directly into the workspace root.

---

## Pipeline — Default Client Deliverable (Virtual Stages)

### Stage 01 — Intake
- **Purpose:** Capture the request — what deliverable, for whom, by when.
- **Inputs:** Dennis brief, prior related drafts, related deliverables.
- **Process:** (1) Read the brief. (2) Identify which `_config/` files apply. (3) List the inputs needed. (4) Confirm with Dennis before proceeding.
- **Outputs:** `drafts/<name>/00_intake.md` with brief summary, source list, and routing decisions.
- **Routing:** Next stage = 02_research. On-failure: stop and ask.

### Stage 02 — Research
- **Purpose:** Gather verifiable evidence. Public sources only unless Dennis authorizes otherwise.
- **Inputs:** Stage 01 intake, prior `deliverables/`, prior `projects/`.
- **Process:** (1) Pull public sources (census / county records / filings / vendor docs). (2) Cite every URL. (3) Avoid unverifiable relationship claims.
- **Outputs:** `drafts/<name>/01_research.md` with cited findings.
- **Routing:** Next stage = 03_draft. On-failure: stop and ask.

### Stage 03 — Draft
- **Purpose:** Compile structured deliverable from research, following `_config/voice.md`.
- **Inputs:** Stage 01 + 02 outputs, `_config/voice.md`, `_config/compliance.md` (if regulated).
- **Process:** (1) Compile per the brief. (2) Inline citations. (3) Mark every relationship assumption with `[VALIDATE: <contact>]`.
- **Outputs:** `drafts/<name>/<name>-<date>.md` (Markdown source).
- **Routing:** Next stage = 04_review.

### Stage 04 — Review
- **Purpose:** Add to `drafts/VALIDATION_QUEUE.md` with required approvers. Build HTML preview if appropriate.
- **Inputs:** Stage 03 output.
- **Process:** (1) Add a row to `VALIDATION_QUEUE.md` (file, type, approvers, status). (2) If HTML preview helps, run any preview builder. (3) Wait for approvals.
- **Outputs:** `drafts/<name>/HANDOFF.md` summarizing the review state.
- **Routing:** Next stage = 05_publish (only after HITL approval).

### Stage 05 — Publish
- **Purpose:** Promote validated artifact from `drafts/` → `projects/` (source of truth) and `deliverables/` (client-ready export).
- **Inputs:** Approved draft + Dennis's explicit go-ahead.
- **Process:** (1) Move/copy the source `.md` to `projects/`. (2) Build or copy the final export to `deliverables/`. (3) Remove the row from `VALIDATION_QUEUE.md`.
- **Outputs:** `projects/<artifact>.md` + `deliverables/<artifact>.{md,html,pdf}`.
- **Routing:** Pipeline complete.

---

## Active projects (current state)

_No projects yet — start with a draft in `drafts/`, promote after Dennis approves._

(Project table goes here once projects exist.)
