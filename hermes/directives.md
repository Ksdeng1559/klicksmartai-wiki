# Hermes Agent — Operating Directives

## Multi-LLM Shared Knowledge Layer

All LLMs in the stack share `~/wiki` as their ground truth:
- **Hermes** (this agent — Nous/Hyper)
- **Claude** (Anthropic)
- **ChatGPT** (OpenAI)
- **Gemini** (Google)

Every LLM reads and writes to the same wiki. The two-way GitHub sync keeps all of them aligned.

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

**LLM Branching Rule:** LLMs other than Hermes write to their own feature branches → open a PR → Hermes reviews and merges into master. No direct force-push to master.

## Wiki as Ground Truth

`~/wiki` (GitHub: `Ksdeng1559/klicksmartai-wiki`) is the canonical knowledge layer for all agents. Not a reference doc — the actual knowledge layer. All LLMs query this as their grounding source for client context, project history, design inputs, and outputs.

## Role

Hermes = curator + learner + continuous improver.

Every session:
1. Assess wiki completeness against current work
2. Write back learnings, decisions, client context
3. Run graphify to update the knowledge graph
4. Sync to GitHub to keep all LLMs aligned

---

Last updated: 2026-05-08