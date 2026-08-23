# _config/deliverables.md — Veritas Development Vertical Map

This file is the **canonical artifact-type map** for Veritas Development Group LLC. It tells the agent (and the user) where to put each kind of deliverable, and which Hermes skill to invoke.

## Artifact Type Map

| Type | Draft location | Deliverable location | File format | Default Hermes skill | Files also |
|------|----------------|----------------------|-------------|----------------------|------------|
| **Website** (multi-page) | `drafts/website/<site-name>-<date>.md` + `.html` | `deliverables/website/<site-name>/` | HTML + ZIP | `open-design-landing` | `sitemap.xml`, `README.md` |
| **Landing page** (single) | `drafts/landing-page/<name>-<date>.md` + `.html` | `deliverables/landing-page/<name>.html` | HTML | `saas-landing` (default) — alt `kami-landing`, `waitlist-page` | single `.html`, `og-image.png` |
| **Long-form content** (blog, advertorial, investor brief) | `drafts/content/<article-name>-<date>.md` | `deliverables/content/<article-name>-<date>.html` + `.md` | Markdown + HTML render | `blog-post` (default) — alt `article-magazine` | `.png` hero |
| **Email** (campaign, outreach) | `drafts/email/<email-name>-<date>.md` | `deliverables/email/<email-name>.html` | Markdown + HTML render | `email-marketing` (product launch) / `cold-email` (cold outreach) — alt `cold-email-4-sequence` for multi-touch | subject + preview + body |
| **Video ad** (long-form brand) | `drafts/video-ad/<campaign>-<date>.md` (storyboard) + `.html` (key-frames) | `deliverables/video-ad/<campaign>/` | HyperFrames project or Remotion project | `hyperframes` (long-form composition) — alt `video-shortform` (≤30s), `venice-video` | `.mp4` final, storyboard.md |
| **Video — short form** (≤30s) | `drafts/video-ad/<name>-<date>.md` | `deliverables/video-ad/<name>.mp4` (or HyperFrames web preview) | `.mp4` + HyperFrames `.json` | `video-shortform` | storyboard md |
| **Ad creative — static** (social, banner) | `drafts/ad-creative/<name>-<date>.md` (brief + copy) + image assets | `deliverables/ad-creative/<name>/` | Image (PNG/JPG) + Copy `.md` | `ad-creative` | copy `.md`, image assets |
| **Sales deck** / Investor brief | `drafts/deck/<deck-name>-<date>.md` + `.html` | `deliverables/deck/<deck-name>.html` | HTML or PDF | `open-design-landing-deck` (Atelier Zero style) — alt `swiss-international`, `pitch-deck` | `slides.html`, optional `pdf` |
| **Lead magnet** (PDF/HTML resource) | `drafts/lead-magnet/<name>-<date>.md` | `deliverables/lead-magnet/<name>.html` (or `.pdf`) | HTML/PDF | `lead-magnets` (concept) — alt `pdf` skill, `digital-eguide` (2-spread preview) | landing page, lead form |
| **Internal research doc** (legacy) | `drafts/<research-name>-<date>.md` (flat) | `projects/<artifact>.md` | Markdown | depends on doc type | flat files at the parent `drafts/` / `projects/` / `deliverables/` |

## Vertical-specific voice rules

- **Website / landing pages**: tight, benefit-led, scannable; one CTA per page. Sales-investor landing pages reference fund mandate + portfolio.
- **Long-form content (advertorials, investor briefs)**: evidence-led, every claim cited, dense paragraphs OK.
- **Email (outreach)**: subject ≤ 60ch, preview ≤ 100ch, body scannable; one CTA.
- **Video ads (webinars, brand)**: emotional hook in first 3 seconds; CTA in last 5 (signup → webinar).
- **Sales decks (investor)**: data-first; one message per slide. Reg D 506(b) language on investor slides.
- **Lead magnets**: educational, "trust-through-evidence," 80% worked example / 20% theory.

Override these in `drafts/<vertical>/voice.md` when Veritas gives specific direction.

## Compliance routing

For each draft, the agent reads `_config/compliance.md`. Vertical-specific notes:
- **Securities-touching (Reg D 506(b))**: investor-facing landing pages, decks, video ads that reference fundraising. Any `drafts/deck/`, `drafts/landing-page/` mentioning capital or returns.
- **Privacy / PII**: lead-magnet forms, customer-facing emails, CRM records.

When in doubt, mark `[COMPLIANCE: securities]` at the top of the draft and pause for David/Dennis review.

## Source-of-truth gate for non-text deliverables

- **HTML / video / image** deliverables still originate as `.md` in `drafts/<vertical>/`.
- Generated HTML / video output goes in `drafts/<vertical>/` next to the source until HITL.
- On promotion, copy both `.md` (source) and final `.html`/`.mp4` into `deliverables/<vertical>/`.
- The `.md` stays in `projects/<vertical>/` (or `projects/` for legacy flat files) as source of truth.

## Promotion convention

1. Approved `.md` source → `projects/<vertical>/<artifact>.md` (or `projects/` for legacy flat files).
2. Rendered deliverable (`.html`, `.mp4`, etc.) → `deliverables/<vertical>/<artifact>.<ext>`.
3. Remove the row from `drafts/VALIDATION_QUEUE.md`.
4. Add entry to `projects/README.md` if the artifact is significant (e.g. a launched site or campaign).