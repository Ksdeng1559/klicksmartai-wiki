# NCF Pilot Run Log — Org Profile Intelligence Workflow

**Status:** Stages 1–5 complete. Stage 6 (NotebookLM) proposed. Stage 7 partial.  
**Workflow:** See [org-profile-intelligence.md](org-profile-intelligence.md)  
**Owner:** Dennis Eng / Hermes Agent

---

## Problem

Current NCF org profile (wiki/entities/ncf-national-christian-foundation.md) was built from scraped web pages via Ollama Cloud + Claude synthesis. It captures surface-level brand and language patterns but lacks:

- Source-grounded answers to specific strategic questions
- Analysis against NCF grant program docs, annual reports, advisor materials
- Live queryable corpus Hermes can hit before drafting outreach
- Spectra alignment analysis (workforce housing, manufacturing jobs, community restoration, MCF model)

---

## Proposed Architecture

```
Stage 1 — Source Collection
  scrape.py (existing) → NCF web pages as markdown
  + NCF PDFs: annual reports, grant program docs, advisor channel materials
  + Spectra alignment tree (workforce housing, manufacturing, community impact, MCF)

Stage 2 — NotebookLM Notebook (via MCP)
  notebook_create → "NCF Domain Analysis — Spectra Alignment"
  source_add (url)  → NCF web pages
  source_add (file) → any PDFs collected
  source_add (text) → Spectra alignment tree + wiki profile

Stage 3 — Domain Analysis Queries
  notebook_query → structured answers to defined question set (see below)
  Export answers → JSON → update wiki/entities/ncf-national-christian-foundation.md

Stage 4 — Wiki + Graph Update
  Rebuild ncf-national-christian-foundation.md with NotebookLM-sourced insights
  Add spectra-holdings-group.md Alignment section
  Rerun graphify on wiki/entities/ to update knowledge graph
```

---

## Query Set (Domain Analysis)

Run these against the NotebookLM notebook after sources are loaded:

### NCF Grant Priorities
1. What specific community impact areas does NCF fund or prioritize grants toward?
2. Does NCF fund or support workforce housing initiatives? What language do they use?
3. Does NCF fund economic restoration, job creation, or manufacturing-related causes?
4. What types of organizations receive grants from NCF Giving Funds?

### Spectra Alignment
5. How does NCF's community restoration mission align with workforce housing and manufacturing job creation?
6. What NCF language and framing best maps to Spectra's MCF model (capital vehicle for community outcomes)?
7. Which NCF funding vehicles (Giving Fund DAF, supporting organizations, impact investing) could flow capital into an MCF structure?

### Advisor Channel
8. How does NCF's advisor channel work — what is the grant flow from HNW donor → advisor → NCF → recipient org?
9. What makes an organization a credible grant recipient through the NCF advisor channel?

### Outreach Intelligence
10. What signals in NCF's recent initiatives or leadership themes indicate openness to structured capital vehicles?
11. What stewardship language should Hermes use when positioning Spectra's MCF as a Kingdom-aligned investment?

---

## MCP Tools Required

```
mcp__notebooklm-mcp__notebook_create
mcp__notebooklm-mcp__source_add
mcp__notebooklm-mcp__notebook_query
mcp__notebooklm-mcp__notebook_describe
mcp__notebooklm-mcp__download_artifact  (optional — audio overview)
```

---

## NCF Source URLs to Add

- https://www.ncfgiving.com/
- https://www.ncfgiving.com/about/
- https://www.ncfgiving.com/solutions/
- https://www.ncfgiving.com/stories/
- https://www.ncfgiving.com/advisors/ (if exists)
- Any NCF annual report PDFs (pull manually)
- NCF grant program pages

---

## Output

- Updated `wiki/entities/ncf-national-christian-foundation.md` — Section 9 Spectra Alignment fully populated
- Updated `wiki/entities/spectra-holdings-group.md` — NCF alignment section grounded in sourced analysis
- NotebookLM notebook ID saved to wiki/references for future Hermes queries
- Graphify rebuild on wiki/entities/

---

## Dependencies

- NotebookLM MCP authenticated (run `nlm login` if cookies expired)
- NCF scrape.py has already run — raw pages cached in outputs/research/ncf-profile/raw/
- Spectra alignment tree defined (workforce housing, manufacturing jobs, community impact, MCF model)
