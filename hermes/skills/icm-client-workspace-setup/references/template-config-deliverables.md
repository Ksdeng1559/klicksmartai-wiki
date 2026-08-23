# Deliverables — <client_name>

This file is the **canonical artifact-type map** for <client_name>. It tells the agent (and the user) where to put each kind of deliverable, and which Hermes / Claude Code skill to invoke.

## Artifact Type Map

| Type | Draft location | Deliverable location | File format | Default Hermes skill | Files also |
|------|----------------|----------------------|-------------|----------------------|------------|
| **Website** (multi-page) | `drafts/websites/<site-name>-<date>.md` + `.html` | `deliverables/websites/<site-name>/` | HTML + ZIP | `open-design-landing` (structure) or `open-design-landing-deck` (decks) | `sitemap.xml`, `README.md` |
| **Landing page** (single) | `drafts/landing-pages/<name>-<date>.md` + `.html` | `deliverables/landing-pages/<name>.html` | HTML | `saas-landing` (default) — alternate `kami-landing` (print-grade), `waitlist-page` (pre-launch) | single `.html`, optional `og-image.png` |
| **Long-form content** (blog, article) | `drafts/content/<article-name>-<date>.md` | `deliverables/content/<article-name>-<date>.html` + `.md` | Markdown source + HTML render | `blog-post` (default) — alternate `article-magazine`, `magazine-poster` (poster-style) | `.png` hero, optional `.docx` for press |
| **Email** (campaign, single) | `drafts/emails/<email-name>-<date>.md` | `deliverables/emails/<email-name>.html` (or `.txt`) | Markdown + HTML render | `email-marketing` (product launch) / `cold-email` (cold outbound) / `emails` (sequence) | subject + preview + body |
| **Video ad** (long-form brand) | `drafts/video-ads/<campaign>-<date>.md` (storyboard) + `.html` (key-frames) | `deliverables/video-ads/<campaign>/` | HyperFrames project or Remotion project | `hyperframes` (long-form composition) — alternate `video-shortform` (≤30s), `venice-video` (AI gen), `fal-video-edit` | `.mp4` final, storyboard.md, frame PNGs |
| **Video — short form** (≤30s) | `drafts/video-ads/<name>-<date>.md` | `deliverables/video-ads/<name>.mp4` (or HyperFrames web preview) | `.mp4` + HyperFrames `.json` | `video-shortform` | storyboard md |
| **Ad creative — static** (social/banner) | `drafts/ads/<name>-<date>.md` (brief + copy) + image assets | `deliverables/ads/<name>/` | Image (PNG/JPG) + Copy `.md` | `ad-creative` | copy `.md`, image assets |
| **Sales deck** / Pitch deck | `drafts/decks/<deck-name>-<date>.md` + `.html` | `deliverables/decks/<deck-name>.html` | HTML or PDF | `open-design-landing-deck` (Atelier Zero style) — alt `swiss-international`, `pitch-deck` | `slides.html`, optional `pdf` |
| **Lead magnet** | `drafts/lead-magnets/<name>-<date>.md` | `deliverables/lead-magnets/<name>.html` (or `.pdf`) | HTML/PDF | `lead-magnets` (concept) — alt `pdf` skill, `digital-eguide` (2-spread preview) | landing page, lead form, thank-you page |
| **Webhook / CRM / Newsletter** technical | `drafts/tech/<feature>-<date>.md` | `deliverables/tech/<feature>/` (code) | `.json`/`.py`/`.yaml`/`.md` | `webhook-subscriptions`, `linear`, `airtable` etc. (depends on stack) | code + tests |

## Voice & tone per vertical (inherits from `_config/voice.md`)

- **Websites / landing pages**: tight, benefit-led, scannable; one CTA per page.
- **Long-form content**: evidence-led, every claim cited, dense paragraphs OK.
- **Email**: subject ≤ 60ch, preview ≤ 100ch, body scannable; one CTA.
- **Video ads**: emotional hook in first 3 seconds; CTA in last 5.
- **Sales decks**: data-first; one message per slide.

Override these in `drafts/<vertical>/voice.md` when the client gives specific direction.

## Compliance routing

For each draft, the agent reads `_config/compliance.md` (if present). Vertical-specific notes:
- **Securities-touching (Reg D 506(b))**: investor-facing landing pages, decks, video ads that reference fundraising.
- **PII / privacy**: lead-magnet forms, customer-facing emails, CRM records.
- **Healthcare**: any medical/clinical claim in content or video.

When in doubt, mark `[COMPLIANCE: securities]` at the top of the draft and pause.

## Source-of-truth gate for non-text deliverables

- **HTML / video / image** deliverables still originate as `.md` in `drafts/<vertical>/` (the markdown source IS the prompt + spec).
- Generated HTML / video output goes in `drafts/<vertical>/` next to the source until HITL.
- On promotion, copy both `.md` (source) and final `.html`/`.mp4` into `deliverables/<vertical>/`. The `.md` stays in `projects/` as source of truth, the rendered artifact in `deliverables/`.

## Promotion convention

1. Approved `.md` source → `projects/<vertical>/<artifact>.md` (or a per-vertical subdirectory if many)
2. Rendered deliverable (`.html`, `.mp4`, etc.) → `deliverables/<vertical>/<artifact>.<ext>`
3. Remove the row from `drafts/<vertical>/VALIDATION_QUEUE.md`
4. Add an entry to `projects/README.md` if the artifact is significant (e.g. a launched site or campaign)
