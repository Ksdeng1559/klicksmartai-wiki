# Veritas Developments — Workspace Identity

> Jackson County, MO real-estate developer. Active engagement: deal-loan structure, investor flywheel (webinars), and CRM build.

**Corporate entity:** Veritas Development Group LLC
**Web property:** `veritasdevelopmentgroupllc.com` (LLC marketing site — Stage 0 SEO, see `drafts/openseo-site-audit-veritasdevelopmentgroupllc-2026-08-26.md`)

This is a **client workspace** inside the KlickSmartAI wiki. It follows the
ICM 3-layer pattern (Identity → Context → Config) and obeys the wiki
source-of-truth rule: **AI-generated content ALWAYS lands in `drafts/`** first;
nothing moves to `projects/` or `deliverables/` until David Poole + Daniel Bailey
confirm (HITL gate). The `wiki-source-of-truth-governance` skill enforces this.

---

## Folder Map

```
veritas-developments/
├── IDENTITY.md            # you are here — Layer 0 (workspace map + rules)
├── CONTEXT.md             # Layer 1 — task routing table
├── README.md              # human-facing overview (mirrors IDENTITY.md)
├── _config/               # Layer 3 — voice, conventions, glossary, artifact map
│   ├── voice.md
│   ├── conventions.md
│   ├── deliverables.md    # vertical artifact map (per-vertical folder + Hermes skill)
│   ├── gtm-skills.md      # GTM use-case bindings (signal-based outbound, ABM, cold outreach, etc.)
│   ├── glossary.md
│   └── compliance.md      # Reg D 506(b), securities-touching language
├── _archive_README_v1.md  # previous structure (kept for traceability)
├── projects/              # Layer 4 — validated deliverables (source of truth)
│   ├── prime-lees-summit.md
│   ├── stonehaven-estates.md
│   ├── co-sponsor-gp-target-list.md
│   ├── growth-program-pilot-plan.md
│   ├── prime-lees-summit-co-sponsor-brief.md
│   ├── website/           # NEW — per-vertical folder (post-2026-08-22)
│   ├── landing-page/
│   ├── content/
│   ├── email/
│   ├── video-ad/
│   ├── ad-creative/
│   ├── deck/
│   ├── lead-magnet/
│   └── README.md
├── drafts/                # Layer 4 — AI work in progress (pre-HITL)
│   ├── VALIDATION_QUEUE.md
│   ├── (flat files: legacy validated drafts)
│   ├── website/           # NEW — per-vertical folder
│   ├── landing-page/
│   ├── content/
│   ├── email/
│   ├── video-ad/
│   ├── ad-creative/
│   ├── deck/
│   ├── lead-magnet/
│   └── README.md
├── deliverables/          # Layer 4 — client-ready exports
│   ├── (flat files: legacy completed exports)
│   ├── website/
│   ├── landing-page/
│   ├── content/
│   ├── email/
│   ├── video-ad/
│   ├── ad-creative/
│   ├── deck/
│   ├── lead-magnet/
│   └── README.md
├── drafts-preview/        # Layer 4 — HTML previews of drafts/ (auto-built)
│   ├── website/
│   ├── landing-page/
│   ├── content/
│   ├── email/
│   ├── video-ad/
│   ├── ad-creative/
│   ├── deck/
│   ├── lead-magnet/
│   └── README.md
└── skills/                # client-specific skills (optional)
    └── README.md
```

**Per-vertical convention (post-2026-08-22):** NEW deliverables land in the vertical subfolder matching the artifact type (e.g. `drafts/landing-page/`, `deliverables/video-ad/`). See `_config/deliverables.md` for the full artifact-type map (folder, file format, default Hermes skill per vertical). Existing flat files in the parent `drafts/`, `projects/`, `deliverables/` are legacy validated work and stay where they are.

---

## Stage Map (Quick-mode — virtual stages defined in CONTEXT.md)

Default pipeline for any Veritas deliverable:

```
01_intake → 02_research → 03_draft → 04_review → 05_publish
   |            |            |          |            |
drafts/      drafts/      drafts/    drafts/      projects/  +  deliverables/
                                                          (HITL gate at 04→05)
```

When a deliverable touches a relationship assumption (David, Daniel, or any
named contact), the HITL gate requires **two approvers**: the substantive owner
(Dennis + David) **and** a relationship validator (Daniel). This is encoded in
`drafts/VALIDATION_QUEUE.md`.

For client-specific multi-stage pipelines (e.g. a recurring Jackson County
intelligence refresh), graduate to **Full-mode ICM** with physical
`projects/<pipeline>/stages/NN_*/CONTEXT.md` contracts. Not yet warranted.

---

## Raw Source Locations

| Source | Path | Contents |
|--------|------|----------|
| Jackson County, MO intel package | `deliverables/` (2026-08-10) | Census, housing, CRE, investor leads, KCCLT memo, vacancy pilot |
| Owner-provided site plan renders | external (2026-08-10) | Prime Lee's Summit + Stonehaven Estates site plans |

---

## Rules

1. **Source-of-truth gate.** AI-generated content ALWAYS lands in `drafts/` first. Never write directly to `projects/` or `deliverables/`. The `wiki-source-of-truth-governance` skill enforces this.
2. **Two-approver HITL for relationship assumptions.** Any deliverable that names David Poole, Daniel Bailey, or any other specific contact requires (a) Dennis + David approval on substance, and (b) Daniel's confirmation on relationship facts. Track this in `drafts/VALIDATION_QUEUE.md`.
3. **Routing first.** At session start, read `CONTEXT.md` to identify which folder to enter; read the relevant project's `README.md` only when entering that project.
4. **Voice follows `_config/voice.md`.** Direct, data-cited, evidence-led. No marketing fluff. No unverifiable claims.
5. **Citations required.** Every external claim carries the URL inline. Census data, county records, etc. must be reproducible.
6. **No autonomous sends.** No client communication (email, Slack, LinkedIn, etc.) goes out without an explicit "send it" from Dennis. Drafts only — never auto-send.
7. **Escalate uncertainty.** When a stage cannot complete (missing input, ambiguous spec, conflicting source, unverifiable relationship claim), stop and ask. Do not invent.

---

## Escalation

| Situation | Action |
|-----------|--------|
| Draft names a person or relationship | Add row to `drafts/VALIDATION_QUEUE.md`; wait for Dennis + David + Daniel before promoting |
| Need more source material from client | Draft outreach to David, save to `drafts/outreach/`, wait for Dennis |
| Deliverable touches Reg D / securities | Consult `_config/compliance.md` first; flag any forward-looking statements |
| New multi-stage pipeline proposed | Propose design in `drafts/` first; promote to `projects/<pipeline>/` only after Dennis approves the design |
| Conflict with voice.md or compliance.md | Pause; flag the conflict; ask Dennis which to honor |

---

## Memory hygiene

Durable facts about this client go in:
- `_config/` for voice, conventions, glossary, compliance (workspace-level)
- MEMORY.md (user profile / cross-workspace) for client-wide preferences only
- Never duplicate the same fact across `_config/` and MEMORY.md — pick one source of truth.
