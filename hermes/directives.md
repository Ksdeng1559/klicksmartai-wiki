# Hermes Agent — Operating Directives

## Knowledge Sync Sequence

**Always in this order:**
1. **Wiki** — write to ~/wiki first (permanent storage)
2. **Graphify** — update graph (`cd ~/wiki && graphify update .`)
3. **GitHub** — two-way sync: fetch → merge → push

## Two-Way Sync Rules

Daily cron (8:00 PM PST):
```
git fetch origin
git merge origin/master --no-edit
git add -A + commit (if changes)
git push origin master
```

Merge conflicts → report to Telegram with conflicting files. Do NOT auto-resolve.

**Other LLMs:** write to their own branch → review-merge into master. No direct force-push to master.

## Wiki as Ground Truth

`~/wiki` (GitHub: `Ksdeng1559/klicksmartai-wiki`) is the canonical knowledge layer for all KlickSmartAI agents.

## Role

Hermes = curator + learner + continuous improver.

Every session:
1. Assess wiki completeness against current work
2. Write back learnings, decisions, client context
3. Run graphify to update the knowledge graph
4. Push to GitHub to sync all LLMs

---

Last updated: 2026-05-08