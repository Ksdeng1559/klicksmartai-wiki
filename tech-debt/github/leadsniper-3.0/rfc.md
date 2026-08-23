# RFC — LeadSniper-3.0 (Ksdeng1559/LeadSniper-3.0, private)

**Audit date:** 2026-08-22 (Saturday)
**Repo:** https://github.com/Ksdeng1559/LeadSniper-3.0 (private)
**Local repo:** ~/LeadSniper-3.0 (branch main, HEAD `0e667cd` — local is 1 commit behind `0b9f724`)

## 1. Git Status

- Branch `main`, **local is 1 commit behind origin/main** (was 0 last week)
- New origin/main HEAD: `0b9f724` fix(gemini): drop response_mime_type with grounding tools; coerce None to empty string for owner/phone/website
- Working tree **dirty**: modified `.gitignore`, `backend/app/main.py`, `docker-compose.yml`; untracked `.dockerignore` — uncommitted local changes from prior session
- New remote branch this cycle: `feature/autonomous-growth-engine-v1` (fetched 2026-08-15, **still not checked out locally**)
- New remote branch: `rios-opportunity-intelligence` (visible this cycle, also not checked out)
- Both `master` and `main` exist remotely; HEAD is on `main`

## 2. Dependency Health

- Project type: **Node/TypeScript + Vite (frontend), Python backend (FastAPI)**
- `backend/requirements.txt` outdated packages:
  - **fastapi** 0.133.1 → 0.141.1 (8 minor versions behind)
  - **pydantic-settings** 2.14.2 → 2.15.0
  - **uvicorn** 0.41.0 → 0.52.4
  - (full pip outdated report has 30+ packages in the active agent venv that aren't strictly LeadSniper deps)
- `requirements.txt` pins (current): fastapi==0.115.6, uvicorn==0.34.0, pydantic==2.10.5, pydantic-settings==2.7.1, supabase==2.10.0, celery==5.4.0, redis==5.2.1, google-cloud-aiplatform==1.75.0, google-genai==0.3.0
- **Note:** the active Python environment has fastapi 0.133.1 installed, not 0.115.6 — the requirements.txt file pins are STALE relative to what's actually running. The pinned `google-genai==0.3.0` is very old.
- Dependabot alerts API: 403 on free plan — not inspectable
- No security advisories this cycle

## 3. CI/CD Pipeline — **STILL FAILING (unchanged since 2026-06-04)**

Workflow `.github/workflows/deploy.yml` ("Deploy to Production"), runs on push/PR to main, matrix Node [18.x, 20.x] + lighthouse job.

**Last 5 runs: ALL FAILED — `Deploy to Production | completed | failure`** (identical set to last cycle; no new runs since 2026-08-08 — no new pushes)

| Run | Time | Branch | Head |
|---|---|---|---|
| 31262225100 | 2026-08-08 14:33Z | main | 0e667cd fix: update Gemini model |
| 31261410038 | 2026-08-08 14:13Z | main | ec1542a feat: Review Intelligence pipeline |
| 27068073482 | 2026-06-06 | main | 1abd01a README update |
| 26983118802 | 2026-06-04 | main | 6c65d62 AI fit scoring |
| 26983088266 | 2026-06-04 | main | e680733 failure rules |

**Failure localization (last run 31262225100):**
- `build-and-deploy (18.x)` — all steps success, Vercel deploy steps **skipped** (deploy only runs on 20.x)
- `build-and-deploy (20.x)` — all build/test steps success, **`Deploy to Vercel (Production)` step FAILED**
- lighthouse job: skipped

**Root cause (probable):** deploy step (`amondnet/vercel-action@v25`) fails with `secrets.VERCEL_TOKEN` / `VERCEL_ORG_ID` / `VERCEL_PROJECT_ID` on the Node 20.x job. The 18.x job skips deploy by design (`if: github.ref == 'refs/heads/main' && matrix.node-version == '20.x'`), so **production deployments have been failing since at least 2026-06-04** (every run in the visible history). Job log endpoint requires elevated permissions (403) — exact Vercel error message not retrievable with this token.

## 4. Recent Merged PRs / Commits

No PR-based flow on this private repo — direct pushes to main. Last 5 commits:
```
0b9f724 fix(gemini): drop response_mime_type with grounding tools; coerce None to empty string  (upstream main, NEW THIS CYCLE)
0e667cd fix: update Gemini model to gemini-2.5-flash  (Hermes Agent, 2026-08-08)
ec1542a feat: add Review Intelligence pipeline (analyze-reviews endpoint)  (Hermes Agent, 2026-08-08)
1abd01a Update README positioning and copyright  (Dennis Eng, 2026-06-06)
6c65d62 Add AI employee fit scoring model  (2026-06-04)
e680733 Add website failure rules  (2026-06-04)
```
- New commit `0b9f724` on origin/main: a Gemini model fix for grounding tools (response_mime_type incompat). Local is behind.

## 5. Recommended Actions for Claude Code

- [ ] **Pull the new origin/main commit** (`git pull origin main` from `~/LeadSniper-3.0`). Commit the dirty `.gitignore` / `docker-compose.yml` / `backend/app/main.py` / `.dockerignore` first, or stash.
- [ ] **CI/CD still failing — open a dedicated remediation ticket.** This is now the 8th consecutive weekly audit flagging the same Vercel-deploy failure. Required actions: (1) verify `VERCEL_TOKEN` / `VERCEL_ORG_ID` / `VERCEL_PROJECT_ID` are present in repo/org secrets, (2) check token expiration, (3) verify Vercel project still exists and is linked to the right org, (4) consider switching to `amondnet/vercel-action@v32` (current latest, the @v25 pin is 2+ years stale).
- [ ] **Bump backend deps** in `backend/requirements.txt`: fastapi 0.115.6 → 0.141.1, uvicorn 0.34.0 → 0.52.4, pydantic 2.10.5 → latest 2.x, pydantic-settings 2.7.1 → 2.15.0, google-genai 0.3.0 → latest. Run `pip-audit` against the new tree before merging.
- [ ] **Review `feature/autonomous-growth-engine-v1`** — fetched a week ago, never inspected. This is the highest-leverage unmerged workstream on the repo; either merge, close, or rebase into a plan.
- [ ] **Review `rios-opportunity-intelligence`** — newly visible remote branch, status unknown.
- [ ] Document the Vercel deploy failure root cause in `~/.hermes/tech-debt-failures.md` (see end of report).

## 6. Risks / Notes

- **Production has been silently broken for 2.5 months.** Every push to main triggers a failed Vercel deploy. If LeadSniper is supposed to be live, users are seeing a broken or stale site. If it's not supposed to be live (e.g. dev/staging only), the workflow should be reconfigured to skip deploy and just run tests.
- The local working tree has uncommitted changes from at least one prior session — risk of merge conflicts when pulling `0b9f724`.
- Backend `requirements.txt` is materially out of date relative to the running environment. The drift may be intentional (pinned to known-good), but a frozen `requirements.txt` that's not actually being used is technical debt.
