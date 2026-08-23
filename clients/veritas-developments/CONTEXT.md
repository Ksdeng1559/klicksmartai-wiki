# Veritas Developments — Routing

## What do you want to do?

| Task | Go to | Load first |
|------|-------|------------|
| Understand this workspace | `IDENTITY.md` | — |
| Run a new intake / discovery cycle | `drafts/` (or `drafts/<vertical>/`) | `IDENTITY.md`, `_config/voice.md`, `_config/deliverables.md` |
| Continue work on a draft | `drafts/<draft-name>.md` (or `drafts/<vertical>/<draft>.md`) | `drafts/VALIDATION_QUEUE.md` (check gating) |
| Promote a validated draft | `projects/<artifact>.md` (or `projects/<vertical>/`) | `_config/compliance.md`, the draft itself |
| Build a client-ready export | `deliverables/` (or `deliverables/<vertical>/`) | the source artifact in `projects/` |
| Generate an HTML preview | `drafts-preview/build.py` (or `drafts-preview/<vertical>/`) | the draft's `.md` source |
| Apply a multi-stage pipeline | propose in `drafts/` first | `IDENTITY.md` |
| Change voice / conventions | `_config/` | `IDENTITY.md` |
| Update glossary | `_config/glossary.md` | the new term + citation |
| Update artifact-type map | `_config/deliverables.md` | the new vertical + default skill |
| Update GTM skill bindings | `_config/gtm-skills.md` | the new use-case + HITL gate |
| Reach David or Daniel | **STOP** — draft outreach to Dennis first; never auto-send |

### Veritas verticals (per `_config/deliverables.md`)
| Vertical | Folder convention | Default Hermes skill |
|----------|-------------------|----------------------|
| `website` | `drafts/website/`, `deliverables/website/` | `open-design-landing` |
| `landing-page` | `drafts/landing-page/`, `deliverables/landing-page/` | `saas-landing` |
| `content` | `drafts/content/`, `deliverables/content/` | `blog-post` (advertorials / investor briefs) |
| `email` | `drafts/email/`, `deliverables/email/` | `cold-email-4-sequence` (7-touch playbook) / `email-marketing` |
| `video-ad` | `drafts/video-ad/`, `deliverables/video-ad/` | `hyperframes` or `video-shortform` (webinars) |
| `ad-creative` | `drafts/ad-creative/`, `deliverables/ad-creative/` | `ad-creative` |
| `deck` | `drafts/deck/`, `deliverables/deck/` | `open-design-landing-deck` (investor pitch) |
| `lead-magnet` | `drafts/lead-magnet/`, `deliverables/lead-magnet/` | `lead-magnets` |

**Rule:** NEW deliverables (post-2026-08-22) use the per-vertical subfolders. Existing flat files at `drafts/`, `projects/`, `deliverables/` (Kulshan-county-intelligence, growth-program-pilot-plan, prime-lees-summit, stonehaven-estates, etc.) stay where they are — legacy validated artifacts.

---

## Session Start Protocol

1. Read `IDENTITY.md` — workspace map, stage map, rules.
2. Identify the task from the table above.
3. If the task touches a relationship assumption, open `drafts/VALIDATION_QUEUE.md` and confirm the draft is approved before doing anything.
4. If the task is a new deliverable, read `_config/voice.md` and `_config/compliance.md` before drafting.
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
- **Inputs:** Stage 01 intake, prior `deliverables/` for Jackson County, MO intel.
- **Process:** (1) Pull census / county records / public filings. (2) Cite every URL. (3) Avoid unverifiable relationship claims.
- **Outputs:** `drafts/<name>/01_research.md` with cited findings.
- **Routing:** Next stage = 03_draft. On-failure: stop and ask.

### Stage 03 — Draft
- **Purpose:** Compile structured deliverable from research, following `_config/voice.md`.
- **Inputs:** Stage 01 + 02 outputs, `_config/voice.md`, `_config/compliance.md` (if Reg D / financial).
- **Process:** (1) Compile per the brief. (2) Inline citations. (3) Mark every relationship assumption with `[VALIDATE: <contact>]`.
- **Outputs:** `drafts/<name>/<name>-<date>.md` (Markdown source).
- **Routing:** Next stage = 04_review.

### Stage 04 — Review
- **Purpose:** Add to `drafts/VALIDATION_QUEUE.md` with required approvers. Build HTML preview if appropriate.
- **Inputs:** Stage 03 output.
- **Process:** (1) Add a row to `VALIDATION_QUEUE.md` (file, type, approvers, status). (2) If HTML preview helps, run `drafts-preview/build.py`. (3) Wait for approvals.
- **Outputs:** `drafts/<name>/HANDOFF.md` summarizing the review state.
- **Routing:** Next stage = 05_publish (only after HITL approval).

### Stage 05 — Publish
- **Purpose:** Promote validated artifact from `drafts/` → `projects/` (source of truth) and `deliverables/` (client-ready export).
- **Inputs:** Approved draft + Dennis's explicit go-ahead.
- **Process:** (1) Move/copy the source `.md` to `projects/<project>/`. (2) Build or copy the final export to `deliverables/`. (3) Remove the row from `VALIDATION_QUEUE.md`.
- **Outputs:** `projects/<project>/<artifact>.md` + `deliverables/<artifact>.{md,html,pdf}`.
- **Routing:** Pipeline complete.

---

## Active projects (current state)

| Project | Location | Status |
|---------|----------|--------|
| Prime Lee's Summit | `projects/prime-lees-summit.md` | Active development (David) |
| Stonehaven Estates | `projects/stonehaven-estates.md` | Active development (David) |
| Co-sponsor GP target list | `projects/co-sponsor-gp-target-list.md` | Validated |
| Growth program pilot plan | `projects/growth-program-pilot-plan.md` | Validated |
| Prime Lee's Summit co-sponsor brief | `projects/prime-lees-summit-co-sponsor-brief.md` | Validated |

Project files are flat in `projects/` (no per-project subdirectories yet). Graduate to subdirectories when a project accumulates a multi-file pipeline.

---

## GTM skills (per `_config/gtm-skills.md`)

Veritas GTM = the **investor flywheel** (CDFIs, family offices, Christian foundations). 7 use-cases bound:

| Use-case | Default skill | HITL gate |
|----------|---------------|-----------|
| Signal-based outbound | `buying-signals-6` + `signal-interpreter` | Dennis + David |
| Automated lead qualification | `score` + `account-tier-scoring` | Dennis |
| Contact data enrichment | `gtm-enrichment-planner` (always first) + `find-qualified-titles` + `never-guess-an-email` | **Dennis approves credit spend** |
| AI ABM targeting | `linkedin-abm-1to1-few-many` + `account-intelligence-analyst` | Dennis + David |
| AI-powered cold outreach | `cold-email-4-sequence` + `cold-email-preflight` | **Reg D 506(b) screen every send** |
| Intent-based prospecting | `buying-signals-6` + `signal-interpreter` | Dennis |
| AI SDR motion | `sdr-outbound-rules` + `reach-out` + `cold-email-4-sequence` | Dennis + David |

**Paid provider gate:** Deepline / LeadSniper / Clay require the `gtm-enrichment-planner` HITL approval BEFORE any paid run. No exceptions.

**Reg D 506(b) overlay:** every investor-facing draft starts with `[COMPLIANCE: securities]`. Run `cold-email-preflight` before any send.

See `_config/gtm-skills.md` for full bindings, role mappings, and per-use-case procedure.

