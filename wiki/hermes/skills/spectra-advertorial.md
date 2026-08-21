---
name: spectra-advertorial
description: Write a faith-framed advertorial for Spectra Holdings MCF pipeline. Feeds on census data from spectra-census-research.
trigger: /spectra-advertorial
---

# /spectra-advertorial

Write a faith-framed advertorial for Spectra Holdings Master Credit Facility pipeline.

## Prerequisites

Run `/spectra-census-research <county>, <state> --deliverable advertorial` first to populate the census data file at `census/<county>-<state-abbrev>.md`.

## Usage

```
/spectra-advertorial <county>, <state>
```

## Input

| Input | Description |
|-------|-------------|
| `county` | County name |
| `state` | Two-letter state code |

## Workflow

### 1. Read Census Data

Read `census/<county>-<state-abbrev>.md`. Pull:
- Human impact numbers (homeless count, poverty rate, cost-burdened households)
- Specific quotes or findings that paint the human picture
- Local context that makes the community real to readers
- CDFI and faith-based organization presence

### 2. Structure the Advertorial

**Header block:**
```
title: "<County Name, ST> — The Housing Crisis and the Harvest"
client: Spectra Holdings Group
scope: <City / County>
audience: Faith Community | Foundation Donors | Local Churches
tags: [<county>, <state>, advertorial, faith, housing, cdfi, spectra-holdings]
```

**Document sections:**

1. **Opening — The Harvest (Matthew 9:37 lead)**
   - Open with the Scripture as the lens: "The harvest is plentiful, but the workers are few"
   - Immediately pivot to the local human reality — this is not abstract
   - Set the scene: name the county, name the crisis in human terms

2. **The People Behind the Numbers**
   - Translate statistics into faces
   - Who are the families being priced out?
   - Which communities are most affected?
   - K-12 homeless students, elderly on fixed incomes, young families
   - If available, pull a specific story or quote from local sources

3. **The Crisis on the Ground**
   - Housing affordability gap (use the numbers but put them in context)
   - Eviction rate and displacement
   - Homelessness baseline
   - What it looks like to lose housing in this community specifically

4. **Why the Church? Why Now?**
   - Faith-based impact: Matthew 25:35–46 — "I was homeless and you sheltered me"
   - Community development as evangelism — the gospel has hands and feet
   - Local church / CDFI partnership opportunity
   - Call out any existing faith-based housing orgs in the county

5. **The Opportunity to Act**
   - What a gift to Spectra MCF accomplishes
   - Patient capital, CDFI-aligned, permanently affordable
   - How every dollar multiplies (leverage, recycled capital)
   - Specific prayer needs for the community
   - Specific partnership or donation ask

6. **Closing — The Harvest (callback)**
   - Return to Matthew 9:37 — close the loop
   - The workers who are few can become many
   - The harvest is ready; the question is whether the church will show up

### 3. Writing Standards

- **Tone:** Warm, hopeful, kingdom-minded, relational — not clinical or salesy
- **Lead with story, not statistics** — the reader should feel the human weight before they see a number
- **Scripture is the frame** — weave it in, but don't force it. Let it inform the lens, not decorate the text
- **Concrete call to action** — don't end with inspiration; end with an invitation to participate
- **Local specificity** — avoid generic "housing crisis" language. Make it about this county, these people, this moment
- **Max length:** 4–6 pages

### 4. Output

Save to: `clients/spectra-holdings/deliverables/<county>-<state>-advertorial.md`

After saving:
```
cd ~/wiki && git add -A && git commit -m "deliverable: <county> advertorial" && git push origin master
```

---

## Pitfalls

- **Don't lead with statistics** — the reader's heart closes before their mind opens. Story first, data second
- **Don't preach** — testify, don't preach. The Scripture should illuminate, not lecture
- **Don't make the ask before the relationship** — build the human connection before the dollar ask
- **Don't over-spiritualize** — "God will provide" without grounded action is not a strategy. Connect prayer to concrete steps
- **Don't use stale or vague numbers** — "many families" is not a number. Use the census data but translate it to human terms

---

## Verification Steps

1. Census data read — human impact numbers extracted
2. Opens with Scripture or a human story (not a statistic)
3. All 6 sections present and in correct order
4. At least one specific human impact angle (not just generic housing crisis)
5. Call to action is concrete (not vague inspiration)
6. Faith framing is natural, not forced
7. Output saved to correct path
8. Git committed and pushed
