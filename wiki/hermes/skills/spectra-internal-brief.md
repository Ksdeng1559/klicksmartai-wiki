---
name: spectra-internal-brief
description: Write an internal brief for Spectra Holdings MCF pipeline. Feeds on census data from spectra-census-research.
trigger: /spectra-internal-brief
---

# /spectra-internal-brief

Write an internal operations brief for Spectra Holdings Master Credit Facility pipeline.

## Prerequisites

Run `/spectra-census-research <county>, <state> --deliverable internal-brief` first to populate the census data file at `census/<county>-<state-abbrev>.md`.

## Usage

```
/spectra-internal-brief <county>, <state>
```

## Input

| Input | Description |
|-------|-------------|
| `county` | County name |
| `state` | Two-letter state code |

## Workflow

### 1. Read Census Data

Read `census/<county>-<state-abbrev>.md`. Extract:
- All 8 census sections
- MCF intervention thesis
- Local partner mentions
- Open data gaps

### 2. Structure the Brief

**Header block:**
```
title: "<County Name, ST> — Internal Brief"
client: Spectra Holdings Group (Internal)
scope: <City / County / Metro Area>
audience: Dennis Eng | KlickSmartAI Internal Use Only
tags: [<county>, <state>, internal-brief, mcf, spectra-holdings]
```

**Document sections:**

1. **Status Summary** (top — always)
   - Pipeline stage: Prospect | Qualified | Active | Pending Commitment | Closed
   - Data completeness: % of census sections populated
   - What stage is this county in the MCF pipeline?
   - Date added, date last updated

2. **Key Facts at a Glance**
   - Table: population, median income, median home, affordability gap, homeless count, housing deficit
   - Delta flag: which metrics changed since last brief
   - Color code: 🟢 improved | 🟡 unchanged | 🔴 worsened

3. **Market Assessment**
   - Housing supply situation (structural deficit, oversupply, balanced)
   - Demand drivers
   - Competitive landscape (who else is doing CDFI-style financing here?)
   - Political/regulatory environment (Zoning? Rent control? State preemption?)

4. **Data Gaps**
   - What data is missing or stale?
   - What's the plan to fill it?
   - Who owns that research task?

5. **Local Partner Assessment**
   - CDFIs active in county
   - Developer partners identified
   - Kulshan CLT model replicable here? (Y/N/Partial)
   - Warm intros to local partners needed?

6. **Action Items**
   - Prioritized list of next steps
   - Owner assigned to each (Dennis, external partner, etc.)
   - Deadline where known
   - Blockers

7. **MCF Fit Assessment**
   - How well does this county fit the MCF thesis?
   - Affordability gap: is it structural or cyclical?
   - Scale: is this a pilot ($1–5M) or platform play ($10M+)?
   - Timeline to first deployment

8. **Risk Register**
   - Top 3 risks specific to this county
   - Probability: Low | Medium | High
   - Mitigation strategy for each

---

### 3. Writing Standards

- **Tone:** Concise, operational, no padding
- **Tables over prose** — use tables for all metric comparisons
- **Delta flags** — always flag what changed since the last brief
- **Action items have owners** — if it doesn't have a name on it, it's not an action item
- **No faith framing** — this is internal operations, not external comms
- **Be honest about gaps** — "unknown" is a valid answer. Don't invent data
- **Max length:** 6 pages

### 4. Output

Save to: `clients/spectra-holdings/deliverables/<county>-<state>-internal-brief.md`

After saving:
```
cd ~/wiki && git add -A && git commit -m "deliverable: <county> internal brief" && git push origin master
```

---

## Pitfalls

- **Don't write prose where a table works** — internal briefs are read quickly; tables scan better
- **Don't skip the risk register** — if you're not flagging risk internally, you're not doing your job
- **Don't leave action items ownerless** — if no one owns it, it won't get done
- **Don't use stale data without flagging it** — mark each stale data point: "data as of 2023 — needs update"
- **Don't mix investor framing with internal framing** — internal briefs should be blunt, not polished for external audiences

---

## Verification Steps

1. Census data file read and all 8 sections extracted
2. All 8 brief sections present and in correct order
3. Status summary is at the top
4. Action items have owners (or "Dennis" assigned)
5. Data gaps are flagged
6. Risk register is present and honest
7. Output saved to correct path
8. Git committed and pushed
