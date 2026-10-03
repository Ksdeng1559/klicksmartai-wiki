---
type: Client Engagement
title: "Business Funding Canada — Routing"
status: active
generated: 2026-10-02
verified: 2026-10-02
---

# Business Funding Canada — Routing

## What do you want to do?

### Workspace-level
| Task | Go to | Load first |
|------|-------|------------|
| Understand this workspace | `IDENTITY.md` | — |
| Run a new intake / discovery cycle | `drafts/` | `IDENTITY.md`, `_config/voice.md`, `_config/compliance.md` |
| Continue work on a draft | `drafts/<draft-name>.md` | `drafts/VALIDATION_QUEUE.md` |
| Promote a validated draft | `projects/<artifact>.md` | `_config/compliance.md`, the draft itself |
| Build a client-ready export | `deliverables/` | the source artifact in `projects/` |
| Generate an HTML preview | `drafts-preview/` | the draft's `.md` source |
| Change voice / conventions | `_config/` | `IDENTITY.md` |
| Update glossary | `_config/glossary.md` | the new term + citation |
| Reach a lender, partner, or SMB lead | **STOP** — draft outreach to Dennis first; never auto-send |
| Look at Accord Financial competitor data | `research/competitors/accord-financial/2026-10-02/` | the README inside |

### Per-vertical (declared at scaffold time)
| Vertical | Folder convention | Default Hermes skill |
|----------|-------------------|----------------------|
| `website` | `drafts/website/`, `deliverables/website/` | `open-design-landing` |
| `landing-page` | `drafts/landing-page/`, `deliverables/landing-page/` | `saas-landing` |
| `content` | `drafts/content/`, `deliverables/content/` | `blog-post` |
| `email` | `drafts/email/`, `deliverables/email/` | `email-marketing` / `cold-email` |
| `deck` | `drafts/deck/`, `deliverables/deck/` | `open-design-landing-deck` |
| `lead-magnet` | `drafts/lead-magnet/`, `deliverables/lead-magnet/` | `lead-magnets` |
| `doc` | `drafts/doc/`, `deliverables/doc/` | `docx` |
| `ad-creative` | `drafts/ad-creative/`, `deliverables/ad-creative/` | `ad-creative` |

See `_config/deliverables.md` for the artifact-type map.

---

## Session Start Protocol

1. Read `IDENTITY.md` — workspace map, stage map, rules.
2. Identify the task from the table above.
3. If touching a relationship assumption (lender, principal, partner), open `drafts/VALIDATION_QUEUE.md` first.
4. New deliverable → read `_config/voice.md` AND `_config/compliance.md`.
5. Write all intermediate and final artifacts into the appropriate folder.

---

## Pipeline — Default Client Deliverable (Virtual Stages)

### Stage 01 — Intake
- Brief summary, source list, routing decisions → `drafts/<name>/00_intake.md`.

### Stage 02 — Research
- Public sources only (no real borrower / SMB data). Cite URLs. → `drafts/<name>/01_research.md`.

### Stage 03 — Draft
- Compile per brief + voice + compliance. Mark relationship assumptions. → `drafts/<name>/<artifact>-<date>.md`.

### Stage 04 — Review
- Add row to `drafts/VALIDATION_QUEUE.md`. Optional HTML preview. → `drafts/<name>/HANDOFF.md`.

### Stage 05 — Publish (HITL)
- On Dennis's explicit approval: `.md` → `projects/`, exports → `deliverables/`. Remove queue row.

---

## Active projects (current state)

| Project | Stage | Surface | Notes |
|---------|-------|---------|-------|
| (none) | — | — | Scaffold only. First deliverable TBD. |

---

## Next steps (suggested)

1. Approve CLAUDE.md (blocked — protected file, needs explicit "yes").
2. Define the **wedge** — which of the 9 verticals is this site's first play? (Accord covers all 9; pick one underserved by Accord or build a clear "we-do-the-thing-Accord-doesn't" angle.)
3. Define voice direction (Dennis to provide).
4. Build first landing page → `drafts/landing-page/`.
5. Build first 3 content articles → `drafts/content/`.