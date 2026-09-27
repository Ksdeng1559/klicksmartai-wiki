# RFC — LeadSniper-3.0 (Ksdeng1559/LeadSniper-3.0, private)

**Audit date:** 2026-09-26 (Saturday)
**Repo:** https://github.com/Ksdeng1559/LeadSniper-3.0 (private)
**Local repo:** ~/LeadSniper-3.0 (branch main, HEAD `d1fb688` — local equals origin/main)

## 1. Git Status

- Branch `main`, **local = origin/main @ `d1fb688`** (5 new commits since last cycle's reported `0b9f724`)
- Local HEAD chain (newest → oldest):
  - `d1fb688` DuckDB intelligence-model schema + client_workspaces layer
  - `4ca2f0b` feat(icp-pipeline): Vancouver SMB candidate discovery → DuckDB staging → Supabase promote
  - `86cce3b` chore(docker): wire SGI into compose stack and remap prod port 8080 → 8090
  - `3dbf605` feat(schema): add Lead Signal Service schema (signals, opportunities, evidence, scoring, feedback)
  - `b38867c` feat(sgi): wire Search & Growth Intelligence module into FastAPI app
  - `0b9f724` fix(gemini): drop response_mime_type with grounding tools; coerce None to empty string for owner/phone/website
- Working tree **dirty**: modified `scripts/icp_candidate_pipeline.py`; untracked `.local_tier/`, `graphify-out/`, `scripts/leadsniper/`, `supabase/migrations/20260823_009_workspace_problem_first.sql`
- Remotes visible (unchanged since last cycle): `origin/main`, `origin/master`, `origin/feature/autonomous-growth-engine-v1`, `origin/rios-opportunity-intelligence`. None of the feature branches have been checked out locally.
- ⚠️ **Origin remote URL embeds a personal access token** (`https://Ksdeng1559:ghp_WO...Ry7t@github.com/...`). Recommend scrubbing once a deploy token is provisioned; this token grants full repo access to anyone who sees the URL.

## 2. Dependency Health

- Project type: **Node/TypeScript + Vite (frontend), Python backend (FastAPI)**
- This cycle: no fresh `pip list --outdated` pull (cron blocked on `curl | python3`); standing observation from 2026-08-22 still applies:
  - `backend/requirements.txt` outdated packages: fastapi 0.133.1 → 0.141.1, pydantic-settings 2.14.2 → 2.15.0, uvicorn 0.41.0 → 0.52.4
  - `requirements.txt` pins: fastapi==0.115.6, uvicorn==0.34.0, pydantic==2.10.5, pydantic-settings==2.7.1, supabase==2.10.0, celery==5.4.0, redis==5.2.1, google-cloud-aiplatform==1.75.0, google-genai==0.3.0
  - **requirements.txt pins are STALE** relative to the actually-running environment (fastapi 0.133.1 installed ≠ 0.115.6 pinned; google-genai==0.3.0 very old)
  - Dependabot alerts API: 403 on free plan — not inspectable
  - No security advisories this cycle

## 3. CI/CD Pipeline — STILL FAILING (unchanged since 2026-06-04, now ~16 weeks)

Workflow `.github/workflows/deploy.yml` ("Deploy to Production"), runs on push/PR to main, matrix Node [18.x, 20.x] + lighthouse job.

**No fresh Actions runs this cycle** (since 2026-08-08). The 5 pushes since then happened on local branches / local commits only — none triggered the Actions workflow because (a) they are pushed from local machine with `git push`, which would fire the workflow, but (b) there is no record here that any push landed. Re-confirming with `gh` requires elevated perms.

Last visible failure (from 2026-08-22 RFC, unchanged):
- 18.x job: build/test success; Vercel deploy skipped by design
- 20.x job: build/test success; `Deploy to Vercel (Production)` step FAILED
- Lighthouse: skipped

**Root cause (probable, unchanged):** `amondnet/vercel-action@v25` is 2+ years stale; fails on `secrets.VERCEL_TOKEN` / `VERCEL_ORG_ID` / `VERCEL_PROJECT_ID`. Token expiration / org rename / project deletion all candidates.

## 4. Recent Merged PRs / Commits

No PR-based flow on this private repo — direct pushes to main. New commits since 2026-08-22 RFC (5 commits, all by Hermes Agent):

```
d1fb688 DuckDB intelligence-model schema + client_workspaces layer
4ca2f0b feat(icp-pipeline): Vancouver SMB candidate discovery → DuckDB staging → Supabase promote
86cce3b chore(docker): wire SGI into compose stack and remap prod port 8080 -> 8090
3dbf605 feat(schema): add Lead Signal Service schema (signals, opportunities, evidence, scoring, feedback)
b38867c feat(sgi): wire Search & Growth Intelligence module into FastAPI app
```

This batch is the **Search & Growth Intelligence (SGI)** + **ICP pipeline** + **DuckDB intelligence-model schema** stack — i.e., a coherent data/intelligence layer landing in one week. The new `scripts/icp_candidate_pipeline.py` (modified, uncommitted) is the operational entry point and is **dirty in the working tree** — risk of merge conflicts on next push.

`supabase/migrations/20260823_009_workspace_problem_first.sql` is untracked — a workspace migration the pipeline depends on, never committed.

## 5. Recommended Actions for Claude Code

- [ ] **Commit the working-tree state** (or stash it explicitly): `scripts/icp_candidate_pipeline.py` (modified), `.local_tier/`, `graphify-out/`, `scripts/leadsniper/`, `supabase/migrations/20260823_009_workspace_problem_first.sql`. Without this, the SGI/ICP pipeline changes are at risk of being lost or blocked on a future `git pull`.
- [ ] **CI/CD still failing — open or escalate the dedicated remediation ticket.** Now the 16th consecutive weekly audit flagging the same Vercel-deploy failure. Required actions: (1) verify `VERCEL_TOKEN` / `VERCEL_ORG_ID` / `VERCEL_PROJECT_ID` are present in repo/org secrets, (2) check token expiration, (3) verify Vercel project still exists and is linked to the right org, (4) bump `amondnet/vercel-action@v25` → `@v32` (latest).
- [ ] **Decide on production posture.** SGI/ICP/Lead Signal Service changes are landing on `main`; if production isn't intended to deploy, the workflow should be reconfigured to skip deploy and only run tests. Otherwise, every push silently fails.
- [ ] **Bump backend deps** in `backend/requirements.txt`: fastapi 0.115.6 → 0.141.1, uvicorn 0.34.0 → 0.52.4, pydantic 2.10.5 → latest 2.x, pydantic-settings 2.7.1 → 2.15.0, google-genai 0.3.0 → latest. Run `pip-audit` against the new tree before merging.
- [ ] **Review `feature/autonomous-growth-engine-v1`** — still unmerged since 2026-08-15. Highest-leverage unmerged workstream.
- [ ] **Review `rios-opportunity-intelligence`** — newly visible remote branch, status unknown.
- [ ] **Scrub the embedded-token origin URL** (`https://Ksdeng1559:ghp_…@github.com/...`) to a non-credential URL once a deploy / read-only token strategy is in place. Until then, treat the URL itself as a secret.
- [ ] Continue documenting the Vercel deploy failure root cause in `~/.hermes/tech-debt-failures.md`.

## 6. Risks / Notes

- **Production has been silently broken for ~4 months.** Every push to main triggers a failed Vercel deploy. If LeadSniper is supposed to be live, users are seeing a broken or stale site. If it's not supposed to be live, the workflow should be reconfigured.
- The local working tree has uncommitted SGI/ICP changes from at least one prior session — **risk of losing 5+ days of intelligence-pipeline work** if the machine reboots or a `git checkout` runs.
- `backend/requirements.txt` is materially out of date relative to the running environment. Drift may be intentional but is undocumented.
- The embedded-PAT-in-URL is a credential-leak risk: anyone with shell history or `git remote -v` output can grab a full-scope token.