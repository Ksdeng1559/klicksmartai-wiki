---
name: spectra-county-official-briefing
description: Write a briefing for county officials on housing and social conditions affecting constituents. For government relations, advocacy, and partnership outreach.
trigger: /spectra-county-official-briefing
---

# /spectra-county-official-briefing

Write a briefing for county officials on housing conditions and social impact affecting constituents.

## Prerequisites

Run `/spectra-census-research <county>, <state> --deliverable county-official-briefing` first to populate the census data file at `census/<county>-<state-abbrev>.md`.

## Usage

```
/spectra-county-official-briefing <county>, <state>
```

## Input

| Input | Description |
|-------|-------------|
| `county` | County name |
| `state` | Two-letter state code |

---

## What This Is

A **county official briefing** is a government-relations document that:
- Briefs a county commissioner, mayor, housing authority director, or city council member
- Focuses on the housing and social conditions their constituents face
- Positions Spectra Holdings / KlickSmartAI as a resource and partner — not a vendor
- Creates a foundation for policy conversation, CDFI partnership, or public-private financing
- Is factual, local, and constituent-centered — not a sales document

---

## Workflow

### 1. Read Census Data

Read `census/<county>-<state-abbrev>.md`. Extract:
- Constituent impact metrics (homeless count, poverty rate, cost-burdened, eviction)
- Specific populations affected (elderly, children, disabled, workforce)
- Housing supply deficits and affordability gaps
- CDFI and financing landscape
- Local partner ecosystem

### 2. Structure the Briefing

**Header block:**
```
title: "<County Name, ST> — Constituent Housing Briefing"
client: Spectra Holdings Group / KlickSmartAI
scope: <County Name, State>
audience: County Officials | Housing Authority | City Council
tags: [[county]], [[state]], county-briefing, government-relations, housing, spectra-holdings]
created: [[DATE]]
```

**Document sections:**

1. **Opening — The Constituent Reality**
   - Lead with what constituents are experiencing, not what the data says
   - Specific numbers in human terms: "On any given night, [X] of your constituents are homeless"
   - Set the scene: this is about the people in their district

2. **The Housing Situation**
   - Affordability: what a typical working family can afford vs. what's available
   - Rental market: vacancy rate, rent growth, displacement
   - Homeownership: median home price vs. median household income
   - Housing deficit: the structural gap in units
   - This is not a personal failure — it's a systemic failure

3. **The Human Cost**
   - Homelessness: PIT count, sheltered vs. unsheltered, YoY trend
   - Eviction: filings per year, geography of filings
   - K-12 homeless students
   - Elderly and disabled on fixed incomes being priced out
   - Working families: the "missing middle" — too much income to qualify for affordable housing, too little to afford market rate

4. **Who Is Being Left Behind**
   - Income tier analysis: who can afford market rate vs. who can't
   - Racial disparity in housing outcomes (if data supports — be careful with framing)
   - Geographic concentration: which neighborhoods are most affected
   - Vulnerable populations: seniors, disabled, children, workforce

5. **What Your Constituents Are Asking For**
   - Affordable housing (by a significant margin over current supply)
   - Stability: not being displaced from community
   - Economic mobility: housing near jobs, transit, schools
   - Dignity: housing that allows families to thrive, not just survive

6. **What Is Needed — The Financing Gap**
   - Current public investment vs. what's required
   - Why existing financing is insufficient
   - CDFI and patient capital as a complement to public subsidy
   - How MCF-type financing works in this context

7. **How Spectra Holdings / KlickSmartAI Can Help**
   - Who we are and what we do
   - Why we're here: partnership, not transaction
   - Current work in the county or region
   - Specific offer: financing, technical assistance, CDFI bridge capital
   - What we're asking for: listening session, intro to housing authority, policy conversation — not an ask for money

8. **Appendix — Data Summary**
   - Key metrics table with sources
   - Contact information

### 3. Writing Standards

- **Tone:** Respectful, factual, partner-minded — you're approaching them as a peer who has done the homework, not a vendor with a pitch
- **Lead with constituents, not organization** — this briefing is about the people in their district, not about Spectra
- **Local specificity is everything** — generic national housing stats are not useful. The official needs to see their district, their constituents, their numbers
- **Be factual and source everything** — officials deal with advocacy documents all the time. Yours stands out because it's sourced and honest
- **Don't ask for their money** — this is not a grant proposal. You're offering resources and partnership. The ask is for their time and a conversation
- **Acknowledge what the county is already doing** — find it and name it. Partnership requires respect for what's already in motion
- **Max length:** 6–8 pages

### 4. Output

Save to: `clients/spectra-holdings/deliverables/<county>-<state>-county-official-briefing.md`

After saving:
```
cd ~/wiki && git add -A && git commit -m "deliverable: <county> county official briefing" && git push origin master
```

---

## Pitfalls

- **Don't lead with the organization** — the briefing is about constituents, not Spectra. The organization is a resource, not the subject
- **Don't make it a sales document** — officials can smell advocacy documents. Make this a resource they can use
- **Don't overstate the ask** — you're not asking them to fund anything. You're offering to be a partner and a resource
- **Don't ignore what's already being done** — acknowledge existing county programs and CDFIs. Find where they overlap, not where they fail
- **Don't use jargon** — translate "LIHTC", "CDFI", "MCF" into plain language or explain on first use

---

## Verification Steps

1. Census data read — constituent impact metrics extracted
2. All 8 sections present in correct order
3. Opens with constituent reality, not organizational intro
4. Local data specificity throughout
5. Partnership framing — no sales tone
6. Acknowledges existing county efforts
7. Clear but modest ask (meeting, intro, conversation)
8. Sources cited in appendix
9. Output saved to correct path
10. Git committed and pushed
