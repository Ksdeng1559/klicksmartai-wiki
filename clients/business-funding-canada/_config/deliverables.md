---
type: Reference
title: "Business Funding Canada — Deliverables Map"
status: active
generated: 2026-10-02
verified: 2026-10-02
---

# Deliverables Map (Vertical Artifact Map)

> Vertical folder convention + per-vertical default Hermes skill binding.

| Vertical | Draft folder | Deliverable folder | File ext | Default skill | Notes |
|----------|--------------|--------------------|----------|---------------|-------|
| `website` | `drafts/website/` | `deliverables/website/` | `.md` (source) + `.html` (export) | `open-design-landing` | Primary site |
| `landing-page` | `drafts/landing-page/` | `deliverables/landing-page/` | `.md` + `.html` | `saas-landing` | Industry / solution / province landing pages |
| `content` | `drafts/content/` | `deliverables/content/` | `.md` | `blog-post` | Editorial — SMB financing education |
| `email` | `drafts/email/` | `deliverables/email/` | `.md` | `email-marketing` (transactional) / `cold-email` (outreach) | Lead nurture + partner outreach |
| `deck` | `drafts/deck/` | `deliverables/deck/` | `.md` + `.html` | `open-design-landing-deck` | Partner pitch, broker channel |
| `lead-magnet` | `drafts/lead-magnet/` | `deliverables/lead-magnet/` | `.md` + `.html` + `.pdf` | `lead-magnets` | Qualification worksheet, rate sheet, factoring 101 |
| `doc` | `drafts/doc/` | `deliverables/doc/` | `.md` + `.docx` | `docx` | Internal SOPs, partner agreements |
| `ad-creative` | `drafts/ad-creative/` | `deliverables/ad-creative/` | `.md` + image | `ad-creative` | Google/Meta ads — financial services (compliance-heavy) |

## Pre-researched competitor
- `research/competitors/accord-financial/2026-10-02/` — full Accord Financial sitemap scrape (35 .md files, 648 KB) + structured summary at `drafts/competitors/accord-financial-summary-2026-10-02.md`.

## File format defaults
- **Source of truth:** `.md` for every vertical.
- **HTML export:** `drafts-preview/<vertical>/` for preview; promoted to `deliverables/<vertical>/` after approval.
- **PDF / DOCX:** Only for verticals that need them (`lead-magnet`, `doc`).

## Promotion flow
1. Artifact `.md` lives in `drafts/<vertical>/<name>-<date>.md`.
2. Preview HTML lives in `drafts-preview/<vertical>/<name>-<date>.html`.
3. `drafts/VALIDATION_QUEUE.md` row tracks approval.
4. On approval: `.md` → `projects/<vertical>/`, `.html` → `deliverables/<vertical>/`.
5. For `lead-magnet` / `doc`: also produce final PDF/DOCX in `deliverables/<vertical>/`.