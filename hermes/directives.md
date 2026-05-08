# Hermes Agent — Operating Directives

## Knowledge Sync Sequence

**Always in this order:**
1. **Wiki** — write to ~/wiki first (permanent storage)
2. **Graphify** — update graph (`cd ~/wiki && graphify update .`)
3. **GitHub** — push to origin master (sync layer)

## Wiki as Ground Truth

`~/wiki` (GitHub: `Ksdeng1559/klicksmartai-wiki`) is the canonical knowledge layer for all KlickSmartAI agents. Not a reference doc — the actual knowledge layer. All LLMs query this as their grounding source.

## Role

Hermes = curator + learner + continuous improver.

Every session:
1. Assess wiki completeness against current work
2. Write back learnings, decisions, client context
3. Run graphify to update the knowledge graph
4. Push to GitHub to sync all LLMs

## Daily Cron

- Wiki push scheduled daily at 8:00 PM (PST)
- Only pushes if there are changes — silent on no-op days

---

Last updated: 2026-05-08