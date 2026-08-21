---
title: Hermes Agent Skills Hub
created: 2026-04-26
updated: 2026-08-05
type: summary
tags: [how-to, technology, guide]
sources: [https://hermes-agent.nousresearch.com/docs/reference/skills-catalog, https://hermes-agent.nousresearch.com/docs/skills]
---

# Hermes Agent Skills Hub

Source: [hermes-agent.nousresearch.com/docs/skills](https://hermes-agent.nousresearch.com/docs/skills) — live hub (88k+ skills across registries, client-rendered) + [Bundled Skills Catalog](https://hermes-agent.nousresearch.com/docs/reference/skills-catalog) (server-rendered, canonical).

**Bundled catalog:** 71 skills · 13 categories (2026-08-05 snapshot)
**Local install (`~/.hermes/skills/`):** 474 skills · 21 categories

The docs hub is a dynamic SPA that fetches its catalog client-side from the live registry — it does not expose a static API. `agentskills.io` is a separate Mintlify doc site (its `/.well-known/skills/index.json` lists only its own 1 skill). The **Bundled Skills Catalog** reference page is the authoritative server-rendered source.

## Bundled Skills Catalog (71)

Hermes ships these built-in skills, copied into `~/.hermes/skills/` on install. Sync respects local deletions/user edits; restore a missing one with `hermes skills reset <name> --restore`.

### apple (4)

| Skill | Description | Path |
|---|---|---|
| apple-notes | Manage Apple Notes via memo CLI: create, search, edit. | `apple/apple-notes` |
| apple-reminders | Apple Reminders via remindctl: add, list, complete. | `apple/apple-reminders` |
| findmy | Track Apple devices/AirTags via FindMy.app on macOS. | `apple/findmy` |
| imessage | Send and receive iMessages/SMS via the imsg CLI on macOS. | `apple/imessage` |

### autonomous-ai-agents (5)

| Skill | Description | Path |
|---|---|---|
| claude-code | Delegate coding to Claude Code CLI (features, PRs). | `autonomous-ai-agents/claude-code` |
| codex | Delegate coding to OpenAI Codex CLI (features, PRs). | `autonomous-ai-agents/codex` |
| computer-use | Drive the user's desktop in the background — clicking, typing, scrolling, dragging — without stealing the cursor, keyboard focus, or switching virtual desktops / Spaces. Cross-platform: macOS, Windows, Linux. Works with any tool-capable... | `autonomous-ai-agents/computer-use` |
| hermes-agent | Use, configure, theme, extend, and orchestrate Hermes Agent. | `autonomous-ai-agents/hermes-agent` |
| opencode | Delegate coding to OpenCode CLI (features, PR review). | `autonomous-ai-agents/opencode` |

### creative (16)

| Skill | Description | Path |
|---|---|---|
| architecture-diagram | Dark-themed SVG architecture/cloud/infra diagrams as HTML. | `creative/architecture-diagram` |
| ascii-art | ASCII art: pyfiglet, cowsay, boxes, image-to-ascii. | `creative/ascii-art` |
| ascii-video | ASCII video: convert video/audio to colored ASCII MP4/GIF. | `creative/ascii-video` |
| baoyu-infographic | Infographics: 21 layouts x 21 styles (信息图, 可视化). | `creative/baoyu-infographic` |
| claude-design | Design one-off HTML artifacts (landing, deck, prototype). | `creative/claude-design` |
| comfyui | Generate images, video, and audio via diffusion workflows. | `creative/comfyui` |
| design-md | Author/validate/export Google's DESIGN.md token spec files. | `creative/design-md` |
| excalidraw | Hand-drawn Excalidraw JSON diagrams (arch, flow, seq). | `creative/excalidraw` |
| humanizer | Humanize text: strip AI-isms and add real voice. | `creative/humanizer` |
| manim-video | Manim CE animations: 3Blue1Brown math/algo videos. | `creative/manim-video` |
| p5js | p5.js sketches: gen art, shaders, interactive, 3D. | `creative/p5js` |
| popular-web-designs | 54 real design systems (Stripe, Linear, Vercel) as HTML/CSS. | `creative/popular-web-designs` |
| pretext | Build creative browser demos with DOM-free text layout. | `creative/pretext` |
| sketch | Throwaway HTML mockups: 2-3 design variants to compare. | `creative/sketch` |
| songwriting-and-ai-music | Songwriting craft and Suno AI music prompts. | `creative/songwriting-and-ai-music` |
| touchdesigner-mcp | Control TouchDesigner via twozero MCP. | `creative/touchdesigner-mcp` |

### email (1)

| Skill | Description | Path |
|---|---|---|
| himalaya | Himalaya CLI: IMAP/SMTP email from terminal. | `email/himalaya` |

### github (6)

| Skill | Description | Path |
|---|---|---|
| codebase-inspection | Inspect codebases w/ pygount: LOC, languages, ratios. | `github/codebase-inspection` |
| github-auth | GitHub auth setup: HTTPS tokens, SSH keys, gh CLI login. | `github/github-auth` |
| github-code-review | Review PRs: diffs, inline comments via gh or REST. | `github/github-code-review` |
| github-issues | Create, triage, label, assign GitHub issues via gh or REST. | `github/github-issues` |
| github-pr-workflow | GitHub PR lifecycle: branch, commit, open, CI, merge. | `github/github-pr-workflow` |
| github-repo-management | Clone/create/fork repos; manage remotes, releases. | `github/github-repo-management` |

### media (3)

| Skill | Description | Path |
|---|---|---|
| gif-search | Search/download GIFs from Tenor via curl + jq. | `media/gif-search` |
| songsee | Audio spectrograms/features (mel, chroma, MFCC) via CLI. | `media/songsee` |
| youtube-content | YouTube transcripts to summaries, threads, blogs. | `media/youtube-content` |

### mlops (5)

| Skill | Description | Path |
|---|---|---|
| evaluating-llms-harness | lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.). | `mlops/evaluation/evaluating-llms-harness` |
| huggingface-hub | HuggingFace hf CLI: search/download/upload models, datasets. | `mlops/huggingface-hub` |
| llama-cpp | llama.cpp local GGUF inference + HF Hub model discovery. | `mlops/inference/llama-cpp` |
| serving-llms-vllm | vLLM: high-throughput LLM serving, OpenAI API, quantization. | `mlops/inference/serving-llms-vllm` |
| weights-and-biases | W&B: log ML experiments, sweeps, model registry, dashboards. | `mlops/evaluation/weights-and-biases` |

### note-taking (1)

| Skill | Description | Path |
|---|---|---|
| obsidian | Read, search, create, and edit notes in the Obsidian vault. | `note-taking/obsidian` |

### productivity (11)

| Skill | Description | Path |
|---|---|---|
| airtable | Airtable REST API via curl. Records CRUD, filters, upserts. | `productivity/airtable` |
| docx | Create, read, edit Word .docx documents and templates. | `productivity/docx` |
| google-workspace | Gmail, Calendar, Drive, Docs, Sheets via gws CLI or Python. | `productivity/google-workspace` |
| maps | Geocode, POIs, routes, timezones via OpenStreetMap/OSRM. | `productivity/maps` |
| nano-pdf | Edit text in existing PDFs via natural-language prompts. | `productivity/nano-pdf` |
| notion | Notion API + ntn CLI: pages, databases, markdown, Workers. | `productivity/notion` |
| ocr-and-documents | Extract text from PDFs/scans (pymupdf, marker-pdf). | `productivity/ocr-and-documents` |
| pdf | Create, merge, split, fill, and secure PDF files. | `productivity/pdf` |
| powerpoint | Create, read, edit .pptx decks, slides, notes, templates. | `productivity/powerpoint` |
| teams-meeting-pipeline | Teams meeting summaries, job replay, Graph subscriptions. | `productivity/teams-meeting-pipeline` |
| xlsx | Create, read, edit Excel .xlsx spreadsheets and CSVs. | `productivity/xlsx` |

### research (6)

| Skill | Description | Path |
|---|---|---|
| arxiv | Search arXiv papers by keyword, author, category, or ID. | `research/arxiv` |
| blogwatcher | Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool. | `research/blogwatcher` |
| grounded-citations | Ground answers and documents in cited, verifiable sources. | `research/grounded-citations` |
| llm-wiki | Karpathy's LLM Wiki: build/query interlinked markdown KB. | `research/llm-wiki` |
| polymarket | Query Polymarket: markets, prices, orderbooks, history. | `research/polymarket` |
| research-paper-writing | Write ML papers for NeurIPS/ICML/ICLR: design→submit. | `research/research-paper-writing` |

### smart-home (1)

| Skill | Description | Path |
|---|---|---|
| openhue | Control Philips Hue lights, scenes, rooms via OpenHue CLI. | `smart-home/openhue` |

### social-media (1)

| Skill | Description | Path |
|---|---|---|
| xurl | X/Twitter via xurl CLI: raw post search, posting, DM, media. | `social-media/xurl` |

### software-development (11)

| Skill | Description | Path |
|---|---|---|
| dogfood | Exploratory QA of web apps: find bugs, evidence, reports. | `software-development/dogfood` |
| hermes-agent-skill-authoring | Author in-repo SKILL.md files: frontmatter and structure. | `software-development/hermes-agent-skill-authoring` |
| inspecting-hermes-desktop-dom | Read the live Hermes desktop DOM/CSS over CDP. | `software-development/inspecting-hermes-desktop-dom` |
| node-inspect-debugger | Debug Node.js via --inspect + Chrome DevTools Protocol CLI. | `software-development/node-inspect-debugger` |
| plan | Write a markdown plan to .hermes/plans/; no execution. | `software-development/plan` |
| python-debugpy | Debug Python: pdb REPL + debugpy remote (DAP). | `software-development/python-debugpy` |
| requesting-code-review | Pre-commit review: security scan, quality gates, auto-fix. | `software-development/requesting-code-review` |
| simplify-code | Parallel 4-agent cleanup of recent code changes. | `software-development/simplify-code` |
| spike | Throwaway experiments to validate an idea before build. | `software-development/spike` |
| systematic-debugging | 4-phase root cause debugging: understand bugs before fixing. | `software-development/systematic-debugging` |
| test-driven-development | TDD: enforce RED-GREEN-REFACTOR, tests before code. | `software-development/test-driven-development` |

## Local Install Notes

**474 skills installed locally** (vs 71 bundled) — the difference (413) is community/registry skills, templates (HyperFrames, PPT decks, Figma), and marketing/research extras added over time.

### Bundled but NOT installed locally (10)

These ship with Hermes but are missing from this profile's `~/.hermes/skills/` — mostly macOS-only (Apple) or GitHub-workflow skills not yet restored:

- `apple-notes`
- `apple-reminders`
- `findmy`
- `github-auth`
- `github-code-review`
- `github-issues`
- `github-pr-workflow`
- `github-repo-management`
- `imessage`
- `openhue`

Restore any with: `hermes skills reset <name> --restore`
