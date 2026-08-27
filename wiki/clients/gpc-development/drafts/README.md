# drafts/

**AI work in progress — pre-HITL.**

Every AI-generated artifact for GPC Development lands here first. Nothing in this folder is canonical until Dennis reviews it.

## Structure

```
drafts/seo/
├── <phase>-<date>-<topic>.md      # AI work in progress
├── <phase>-<date>-<topic>.html    # (optional) preview rendered by the skill
└── VALIDATION_QUEUE.md            # what's pending review
```

## The gate

For every artifact, the workflow is:

```
agent writes drafts/seo/<artifact>.md
      │
      ▼
agent adds row to drafts/seo/VALIDATION_QUEUE.md (status: pending)
      │
      ▼
agent reports back to Dennis: "Draft at <path>. Awaiting review."
      │
      ▼
Dennis replies: "approve" / "revise" / "kill"
      │
      ▼
On approve → openseo-data-export skill → projects/seo/ + deliverables/seo/
On revise → agent updates the draft + updates VALIDATION_QUEUE row
On kill → agent archives or deletes the draft
```

## What lives here

| Phase | Example filename |
|---|---|
| Plan | (no draft — cost plan presented inline in chat) |
| Discover (PAA) | `paa-2026-08-26-vancouver-gc.md` |
| Discover (keywords) | `keywords-2026-08-26-vancouver-gc.md` |
| Discover (SERP) | `serp-2026-08-26-vancouver-gc.md` |
| Discover (domain) | `domain-2026-08-26-gpc-vs-competitors.md` |
| Enrich (content) | `content-2026-08-26-services-page.md` |
| Score (audit) | `audit-2026-08-26-gpc.md` |
| Score (rank) | `rank-tracking-setup-2026-08-26.md` |
| Outreach (analytics) | `analytics-2026-08-26-monthly.md` |
| Outreach (local) | `local-2026-08-26-gpc-gbp.md` |
| Outreach (export) | (operates on existing drafts) |

## Currently

| File | Status | Notes |
|---|---|---|
| `audit-quote-2026-08-26-gpc-development.md` | pending Dennis review | Will move to `clients/open-seo/drafts/seo/` (parent) until this workspace is fully populated — see TO MOVE below |

## TO MOVE

The audit quote sheet was written before this workspace existed. It currently lives at `/home/denni/wiki/clients/open-seo/drafts/seo/audit-quote-2026-08-26-gpc-development.md`. Once Dennis approves CLAUDE.md (and the workspace becomes fully active), move it here. Until then, the file stays in the parent workspace.
