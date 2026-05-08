# Instructions for Claude Coworker: Generate Presentation from Topical Authority Report

## Objective

Using the completed Topical Authority Research Report for Insurance Direct Canada, generate a production-ready PowerPoint presentation for the KlickSmartAI sales team.

---

## Source Files

| File | Path |
|------|------|
| Research Report (full) | `~/wiki/research-pipeline/outputs/topical-authority-research-insurancedirectcanada-life-insurance-wealth-2026-04-20.md` |
| Slide Deck (markdown) | `~/wiki/research-pipeline/outputs/powerpoint-deck-insurancedirectcanada-topical-authority-2026-04-20.md` |
| Google Doc (formatted) | `https://docs.google.com/document/d/1Y0tr-5X2etb27sXwOZjNSkm_8Et3dB_qLCGzo14F8TE/edit` |

---

## Step-by-Step Instructions

### Step 1: Read the Research Report

Open and thoroughly read the research report. Key sections to absorb:

- **Domain Score: 6.5/10** — Insurance Direct Canada (insurancedirectcanada.com), 27-year domain, $2B coverage sold, 12,000 clients, Burnaby BC
- **IDC Financials (from Kevan Penonzek):**
  - Close rate: 35% (lead to closing)
  - Average commission: $1,200/policy
  - Top producer: $15,000–$18,000/month net to agent
  - New agents: start at 40 leads/month, taper to 30
  - Veteran agents: 20–30 leads/month (depending on existing client block size)
  - Top performers: handle 75%+ of IDC workload
- **ROI Math:**
  - Position 1 for "term life insurance" = ~8,800 extra organic clicks/month
  - Full 8-keyword cluster = ~24,000 extra clicks/month
  - 0.5% visitor-to-lead conversion × 35% close rate = 42 extra policies/month
  - Additional annual first-year commission: ~$608,000
  - Break-even: +10 extra policies/year
  - Conservative ROI: ~50x
- **Content Gaps (P1 priority):**
  - Infinite Banking Concept / Become Your Own Bank
  - COLI (Corporate-Owned Life Insurance)
  - Irrevocable Trust strategies
  - Whole Life cash value acceleration
  - Critical Illness Rider strategy
  - Life insurance in a TRUST structure
- **YouTube Research:**
  - "Become Your Own Bank" = 795,480 views — top content gap
  - "Millionaires Build Wealth Using Life Insurance" = 213,073 views
  - "Life Insurance in a TRUST" = 129,282 views
  - Term life "How Much Do I Need?" = 157,277 views
- **Market Data:**
  - PolicyMe 2026: $500K coverage sweet spot
  - 30-year term dominates ages 18–44
  - 50%+ of applicants have a medical condition
  - 73% of insurance CEOs treating AI as top priority (KPMG 2026)

---

### Step 2: Review the Slide Deck Markdown

The file `powerpoint-deck-insurancedirectcanada-topical-authority-2026-04-20.md` is the **source of truth for slide structure**. It contains:

**11 Slides:**
1. **Title Slide** — "Topical Authority Strategy: Insurance Direct Canada"
2. **The Problem** — 35% close rate, thin organic presence, $500K–$608K commission opportunity
3. **What Is Topical Authority?** — E-E-A-T framework, HubSpot model
4. **Where IDC Stands Today** — Domain Score 6.5/10, content gaps
5. **The Opportunity** — 24,000 extra clicks/mo, 8-keyword cluster
6. **Keyword Priority Map** — 8 target keywords with monthly Canada search volume
7. **26-Week Action Plan** — 3 phases: Foundation (1–42), Build (43–98), Scale (99–180)
8. **Layer 5: Content Brief Engine** — 12 SEO briefs, 5 advertorial articles, 26-week publishing calendar
9. **Investment & ROI** — $19,500 total investment, ~$608K annual commission potential, ~50x ROI
10. **Next Steps** — Immediate actions for the KlickSmartAI team
11. **CTA** — Contact / follow-up slide

Each slide has **speaker notes** in the markdown.

---

### Step 3: Generate the PowerPoint File

**Recommended approach:** Use Python with `python-pptx` to generate a real `.pptx` file.

**Installation:**
```bash
pip install python-pptx
```

**Slide design guidelines:**

| Element | Specification |
|---------|--------------|
| Color scheme | Dark navy (#1a2744) background for title/section slides, white for content |
| Accent color | Gold/amber (#f59e0b) for highlights and CTAs |
| Font | Helvetica or Arial (system default) |
| Title font size | 32–36pt |
| Body font size | 18–24pt |
| Logo | Include KlickSmartAI branding if available |

**Key slide requirements:**

- **Slide 2 (The Problem):** Must include the 35% close rate, $1,200 avg commission, and $15K–$18K top producer stat prominently
- **Slide 9 (Investment & ROI):** Must show the $608K annual commission potential and 50x ROI in large font
- **Slide 7 (Action Plan):** Phases 1–4 marked ✅ COMPLETED should be visually distinct
- **All slides:** Include speaker notes pulled from the markdown source
- **Slide 11 (CTA):** KlickSmartAI contact info — Dennis E., @klicksmartsai_bot, KlickSmartAI.com

---

### Step 4: Save the Output

Save the generated `.pptx` file to:
```
~/wiki/research-pipeline/outputs/presentations/
```

Filename format:
```
IDC-Topical-Authority-Presentation-YYYY-MM-DD.pptx
```

For example:
```
IDC-Topical-Authority-Presentation-2026-04-20.pptx
```

---

## Quality Checklist

Before delivering, verify:

- [ ] All 11 slides are present and in correct order
- [ ] Financial stats (35% close rate, $1,200 commission, $608K opportunity) appear on correct slides
- [ ] Speaker notes included on every slide
- [ ] ROI math is accurate (50x, break-even at +10 policies/year)
- [ ] 26-week (180-day) timeline is consistent — no references to "12 weeks" remain
- [ ] CTA slide includes KlickSmartAI branding and contact
- [ ] File opens cleanly in PowerPoint / Google Slides / Keynote

---

## If Using Google Slides Instead

1. Go to `https://docs.google.com/presentation/u/0/create`
2. Create blank presentation
3. Copy content from each slide of the markdown deck into a new slide
4. Apply the navy/gold color scheme manually
5. Download as `.pptx` and save to the outputs folder above

---

## Contact for Clarification

If any data in the report is unclear or needs verification before generating:
- **Owner:** Dennis E. (@klicksmartsai_bot on Telegram)
- **Source doc:** `https://docs.google.com/document/d/1Y0tr-5X2etb27sXwOZjNSkm_8Et3dB_qLCGzo14F8TE/edit`
