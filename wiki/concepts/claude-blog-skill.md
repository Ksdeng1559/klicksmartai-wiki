---
title: Claude Blog Skill
type: concept
domain: content
source: https://youtu.be/AeLC4iutG8w
status: pending-install
tags: [concept, blogging, content-creation, claude-code, seo, ai-citations, writing]
related: [claude-code, writing-plans]
last_reviewed: 2026-04-19
---

# Claude Blog Skill

Comprehensive blog creation skill for Claude Code. Write research-backed, top-ranking blog articles using slash commands.

**Dual optimized for:**
- Google rankings
- AI citations (ChatGPT, Perplexity, AI Overviews)

**Status:** Saved — pending installation into Claude Code skills directory.

---

## Installation

One terminal command paste. When ready:

1. Copy install command from skill page or video description
2. Paste into terminal
3. Press Enter

**Skill directory:** `~/.hermes/skills/productivity/claude-blog/`
**Transcript:** `~/.hermes/skills/productivity/claude-blog/references/video-transcript.md`

---

## Core Commands

| Command | What it does |
|---------|-------------|
| `/blog write` | Interactive blog article creation |
| `/blog audit` | Full website blog audit |

### `/blog write` — Interactive Questions

1. **Topic** — e.g. "AI blogs in 2026 and how to avoid AI slop"
2. **Audience** — General readers | Business professionals | Developer/Technicians | Marketers
3. **Word count** — e.g. "3000+ words"
4. **Output format** — HTML | WordPress (MCP) | Shopify (agent) | Any CMS

---

## How It Works — 3 Phases

### Phase 1: Planning
Claude builds a to-do list:
```
Phase 1.5 → Select content template
Phase 2   → Research statistics and images
Phase 3   → Generate outline → Write article → Quality check → Deliver
```

### Phase 2: Research (Offline, Trusted Sources)
Bypasses generic scraping. Pulls from **tiered sources:**

| Tier | Sources |
|------|---------|
| 1 | Government websites, educational sites |
| 2 | Wikipedia |
| 3 | Reddit, YouTube, open-source blogs |

**Also:** Pexels/Pixabay for images, SVG chart generation inline.

### Phase 3: Write + Quality Score
Delivers a complete blog:
- Cover image, title + subtitle
- H2 sections with embedded images, SVG charts, quotes, external links
- FAQ, tags, metadata
- Topical authority structure
- **Quality score out of 100** (demo started at 72/100)

---

## Post-Generation: Human Review Loop

Claude generates. You review and prompt fixes:

| Prompt | Action |
|--------|--------|
| `"Add internal links from [site]"` | Embeds internal links |
| `"Fix the overlapping chart"` | Corrects chart rendering |
| `"Increase quality score from 72 to 90"` | Refines article upward |
| `"Add personality and style"` | Injects human voice |
| `"Connect to Frankenstein Pro"` | Auto-embeds internal links |

**Core principle:** Human expertise is the final quality gate. Don't just publish.

---

## Output Formats

| Format | Method |
|--------|--------|
| HTML | Default — shows exact rendered output |
| WordPress | Via MCP connection |
| Shopify | Via dedicated agent |
| Any CMS | Via custom prompt |

---

## Benchmarks (2025-2026)

Useful stats for blog content on AI slop:

- **52%** of English articles published online were AI-generated in 2025 (Graphite, 65K articles)
- **5.44x** more organic traffic for human-written vs. AI content
- **82%** — how often ChatGPT cites human-written content
- "Tipping point reached: machines are outwriting humans"

---

## Why It Matters

Most AI blogs are unresearched, generic slop. This skill:
1. Grounds every article in real research from trusted tiered sources
2. Uses human expertise as the final quality layer
3. Produces content that ranks on Google AND gets cited by AI Overviews
4. Helps make the internet more trustworthy

---

## Source

- Video: https://youtu.be/AeLC4iutG8w
- Host: Daniel — AI Marketing Hub
- Full transcript: `~/.hermes/skills/productivity/claude-blog/references/video-transcript.md`
- Skill file: `~/.hermes/skills/productivity/claude-blog/SKILL.md`
