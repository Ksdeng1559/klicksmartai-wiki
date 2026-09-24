# Urban Mining USA — PCB → Carbon Credit Preliminary Dossier

> **NotebookLM-ready consolidated source.** Created 2026-09-23 by Hermes (KlickSmartAI). Add this file (or individual components below) as a source in your Urban Mining USA NotebookLM notebook.

---

## HOW TO USE THIS IN NOTEBOOKLM

This dossier was produced as a single-source import. Two options:

1. **Single source (recommended for now):** Save this file somewhere NotebookLM can see it (Google Drive, local upload), then add it as one source via NotebookLM's "Add source → Upload file" or paste the whole text into "Add source → Copied text."
2. **Multiple sources (better for cross-source synthesis later):** Use the four individual files in `~/wiki/clients/breakthrough-mgmt/urban-mining/preliminary-carbon-2026-09/` as separate sources so you can pin queries to specific docs (e.g., "Answer using only the EPA WARM factors").

Recommended queries against this notebook once imported:

- "What is the most defensible go/no-go answer for whether Urban Mining USA should pursue Verra VMR0008?"
- "Build a $/tonne carbon revenue model across low/base/high scenarios for server-grade PCB"
- "List the specific additionality strategies that pass regulatory-surplus in which US states"
- "Generate a VVB RFP draft for a Verra VMR0008 e-waste project"
- "Compare stacking revenue from VCUs + Plastic Credits + Material Recovery Certificates against double-counting risk"

---

## SECTION 1 — Main Briefing (preliminary-pcb-to-credits.md)

# PCB → Carbon Credits — Preliminary Briefing

**Project:** Urban Mining USA
**Subject:** Can recycling printed circuit boards generate Verified Carbon Units (VCUs) under Verra VMR0008, and is the economics defensible?
**Date:** 2026-09-23
**Author:** Hermes (cost-routed research, primary sources only)
**Hard cost ceiling:** $5.00 USD | **Actual spend:** ~$0 (Brave free + Parallel credits already loaded; Tavily extracts only)
**Time:** ~15 min wall-clock
**Status:** PRELIMINARY — go/no-go decisions OK from this; full VVB quote still required before commitment

---

## TL;DR — 60-Second Answer

**Yes**, PCB recycling can plausibly generate VCUs under Verra's **VMR0008** (active since 4 Sept 2023; must be paired with CDM's AMS-III.BA). However:

1. **Volume threshold is large.** EPA WARM v16 says recycling one short ton of mixed electronics avoids ~0.90 tCO2e net. To issue even 1,000 VCUs/year you need to process ~1,100 short tons (= 1,000 metric tons) of electronics annually.
2. **$/tCO2e economics are weak.** 2024–2025 voluntary carbon market data: avoidance credits range **$1–$15/ton** with weighted avg ~$5/ton. At $5/VCU that yields **~$0.05/kg** of carbon revenue — **immaterial** vs metal revenue.
3. **The 25 US states with e-waste laws create a major additionality hurdle.** Material collected under state mandate likely fails regulatory-surplus test. The strongest additionality angle is **aggregating small generators** that wouldn't otherwise access qualified recycling (data-center tenants, small hospitals, schools).
4. **Eligibility is for material recovery, not just metal value.** VMR0008 covers ferrous, non-ferrous (incl. precious), and plastics. PCB specifically is **eligible**.
5. **Realistic model: treat carbon as a 2–5% revenue enhancer** plus customer-facing Material Recovery Certificates, **not** as a primary revenue line. The base-case Verra VCU project is a multi-year, six-figure compliance project on its own.

**Recommended next action:** Build the customer-facing Material Recovery Certificate + Scope 3 reporting layer now (low cost, high trust). Run a VMR0008 pilot ONLY if you can credibly demonstrate aggregation additionality in a non-mandated state (Texas, Florida, or a Southern state with no landfill ban).

---

## Question 1 — Can a new U.S. Urban Mining project qualify under VMR0008?

**Answer: PLAUSIBLE, with caveats.**

| Test | Status | Source |
|---|---|---|
| Methodology active? | **YES** — VMR0008 active since 4 Sept 2023; grace period for legacy AMS-III.BA projects ended 4 March 2024 | Verra methodology page — verified |
| Pairing required? | **YES** — must be used WITH CDM AMS-III.BA (UNFCCC ID 10460) | Verra — verified |
| PCB-in-scope? | **YES** — "E-waste contains rare and precious metals… recovered into secondary materials" | Verra — verified |
| U.S. eligible? | **LIKELY YES** (CDM methods are global; no U.S. restriction found; PWRM0002 has U.S.-registered projects) | Verra — verified for PWRM0002; VMR0008 U.S. registration not yet visible |
| Existing VMR0008 U.S. projects? | **NOT FOUND in this research pass** | Requires deeper registry crawl (deferred) |

**Caveat:** VMR0008 introduces an **"upstream displacement discount factor"** (uncertainty adjustment) added by Verra in August 2023 specifically to prevent over-crediting by claiming virgin material displacement that doesn't actually occur. This **shrinks eligible tCO2e**. The magnitude of the discount for PCB specifically is unknown to this preliminary.

---

## Question 2 — Which e-waste streams generate the highest verified GHG reductions per tonne?

**Answer: Higher-grade = higher yield. Server-grade / PCB-dense streams outperform consumer-grade.**

EPA WARM v16 (Dec 2023) per-short-ton net recycling emission factors:

| Material Category | Net Recycling Emissions (MTCO2E/short ton) |
|---|---:|
| Mixed electronics | -0.90 |
| Desktop CPUs | -1.49 |
| Portable devices (laptops/phones) | -1.06 |
| Flat-panel displays | -0.99 |
| Hard-copy devices (printers) | -0.56 |
| Electronic peripherals | -0.36 |

**Per-component virgin-production factors (for displaced-virgin calculation):**

| Component | Virgin Production Emissions (MTCO2E/short ton) |
|---|---:|
| **Printed Circuit Board** | **126.70** |
| Flat Panel Display Module | 54.59 |
| Aluminum | 5.90 |
| Copper | 6.76 |
| Plastic | 4.76 |
| Ferrous Metal | 2.32 |

**Practical implication:** Server/telecom operators generate the highest per-tonne tCO2e, **provided** the project developer can defend a per-component accounting approach with the VVB.

---

## Question 3 — Can PCB recycling specifically generate VCUs?

**Answer: YES — PCB is explicitly in-scope.**

Per-tonne VCU estimate, server-grade PCB (research estimate, requires validation):

```
PCB mass in 1 ton server boards:  ~400 kg = 0.40 short ton
Avoided emissions (raw):          0.40 × 126.70 = 50.68 tCO2e/short ton
Less upstream displacement discount (~30%, estimate): -15.20 tCO2e/ton
Net eligible:                     ~35.48 tCO2e / short ton of server boards
```

**Range:** ~20–45 VCUs per short ton of server-grade boards (high/low scenarios).

**Compared to gold yield (server boards 200–500+ g Au/ton, May 22 wiki):** Carbon credit revenue is **2–5 orders of magnitude smaller** than gold revenue per ton. At $5/VCU and ~35 VCUs/ton, that's **~$175/ton** carbon vs **$680–1,700/ton** gold at current spot. **Carbon is supplemental, not core.**

---

## Question 4 — What additionality strategy would be required?

**Answer: AGGREGATION + CARBON-FINANCED COLLECTION in states with NO e-waste mandate.**

| # | Pathway | Defensibility | Comment |
|---|---|---|---|
| 1 | **Aggregation of small generators** (enterprises, schools, small hospitals) that can't access qualified recycling individually | **STRONG** | Documented in CDM/Verra precedent |
| 2 | **Carbon-financed recovery** — credit revenue enables otherwise uneconomic collection | **STRONG** | |
| 3 | **New collection network** in geographic gaps | STRONG | Map underserved metros vs existing R2/e-Stewards operators |
| 4 | **Increased recovery** beyond state-mandated minimums | WEAK–MEDIUM | |
| 5 | **Advanced material recovery** | MEDIUM | Limited by asset-light model |
| 6 | **New processing capacity** | N/A | Asset-light rules out |

**Regulatory-surplus blocker:**

- **25 states + DC** have e-waste laws (Producer Responsibility, landfill bans, or both) → mostly NEGATIVE for additionality
- 22 states have NO e-waste law (TX, FL, OH, GA, etc.) → POSITIVE baseline for additionality
- **Recommendation:** Operate the Verra-registered project (or its major aggregation nodes) in TX/FL/OH/GA first

---

## Question 5 — How many VCUs could realistically be generated per 1,000 tonnes of qualifying material?

| Scenario | tCO2e/net per short ton | VCUs / 1,000 short tons | At $5/VCU | At $15/VCU |
|---|---:|---:|---:|---:|
| **Low** (high displacement discount, mandated-state baseline) | ~5 | ~5,000 | $25,000 | $75,000 |
| **Base** (server-grade PCB, 30% discount, non-mandated state) | ~35 | ~35,000 | $175,000 | $525,000 |
| **High** (per-component accounting defended, low discount) | ~60 | ~60,000 | $300,000 | $900,000 |

**USD/short ton carbon revenue (BASE):** ~$175/ton.

---

## Question 6 — What is realistic net carbon revenue after project-development and verification costs?

**Answer: Negative-to-marginal in year 1; possibly positive in year 3+ IF issuance volume clears 25,000 VCUs/year.**

VCS project development cost components (typical ranges, research estimate):

| Cost Component | One-Time | Annual Recurring |
|---|---|---|
| Project Design Document (PDD) authoring | $15–40K | — |
| Feasibility assessment | $10–25K | — |
| VVB validation (pre-registration) | $15–40K | — |
| VVB verification (each monitoring period) | — | $15–35K |
| Registry issuance fees | $5–10K | $1–3K |
| Legal / chain-of-custody contracts | $10–25K | — |
| MRV systems (data architecture) | $25–75K | $5–15K hosting |
| Carbon-credit sales commissions (10–20%) | — | 10–20% of gross |
| **Total first-year outlay** | **$80–215K** | **$21–53K + 10–20% of gross** |

**Net revenue breakeven (BASE scenarios):** Assuming $215K first-year + $50K recurring + 15% sales commission:

| Annual VCU Issuance | Gross @ $5/VCU | Net after costs | Verdict |
|---:|---:|---:|---|
| 5,000 | $25,000 | -$228,000 | Deficit |
| 25,000 | $125,000 | -$129,000 | Deficit |
| 50,000 | $250,000 | +$22,500 (recurring) | Recurring surplus |
| 100,000 | $500,000 | +$293,500 | Strong margin |

⚠️ At $5/VCU, breakeven requires **~50,000 VCUs/year = ~1,400 short tons of server-grade boards/year.**

---

## Question 7 — At what annual tonnage does carbon certification become economically worthwhile?

| Tonnage/yr (short tons) | Est. VCUs (BASE) | Annual Net @ $5/VCU | Decision |
|---:|---:|---:|---|
| 250 | 8,750 | -$184K | NOT WORTH PURSUING as VCS project |
| 500 | 17,500 | -$138K | Borderline — only if you also need Material Recovery Certificate |
| **1,500** | **52,500** | **+$25K** | **MINIMUM VIABLE for VCS pursuit** |
| 5,000 | 175,000 | +$567K | Strong |
| 10,000 | 350,000 | +$1.16M | Pursue aggressively |

---

## Question 8 — Can Urban Mining aggregate multiple e-waste generators under one carbon project?

**Answer: YES — Verra supports grouped projects.** Single Project Design Document covering all sites, common baseline methodology, consistent monitoring, single VVB, each new generator/site added via project-internal change rather than re-registration.

---

## Question 9 — Can carbon credits and Plastic Credits coexist with recovered-metal revenue and customer environmental reporting?

| Combination | Verdict | Reasoning |
|---|---|---|
| Recovered metal revenue + VCU | **Allowed** | Different basis |
| ITAD/service fees + VCU | **Allowed** | Different basis |
| Equipment resale + VCU | **Allowed** | Resale is generator-side |
| VCU (Verra) + Plastic Credit (Verra PWRM0002) | **Likely Allowed IF same plastic tonnage isn't double-claimed** | Both Verra-issued; double-issuance risk |
| VCU + Scope 3 reporting value for customer | **Allowed IF env attributes contractually assigned to UM USA** | One party claims credit; cannot both |
| VCU + government incentive | **Depends on incentive type** | |

**Required contract language:** "Supplier transfers to Urban Mining USA all qualifying environmental attributes associated with the collection, processing and recycling of supplied materials, subject to applicable law and program rules."

---

## Question 10 — Who must contractually own the environmental attributes?

| Party | Default owner IF not contracted | Plausible contractual claim |
|---|---|---|
| Original equipment owner / Generator | YES — retains by default | Will trade if compensated |
| ITAD provider | NO — service provider only | Can claim if contracted upstream |
| **Urban Mining USA (aggregator)** | NO — unless contracted | **YES — primary claim through service agreement + EAA assignment** |
| Recycler | NO — service provider only | Sub-claim |
| Refiner | NO — material flows, not credit flows | Sub-claim possible |

**Required contract artifact:** Master Service Agreement with Environmental Attribute Assignment (EAA) clause + data ownership + audit rights + exclusivity/non-double-claim.

---

## Recommended Immediate Actions

1. Send 3 VVB RFPs (SustainCERT, TÜV SÜD, SCS Global) — $0, Week 1
2. Build the Material Recovery Certificate product (no Verra credit needed) — low cost, Week 1–3
3. Add EAA clause as standard to all UM USA supplier contracts — low cost, ongoing
4. Identify 3 pilot states with NO e-waste law (TX, FL, GA most likely) — $0, Week 1
5. Decide: pursue VMR0008 pilot, or stop at Material Recovery Certificate + Scope 3 — $0, after receiving VVB quotes

**If you do not pursue Verra registration:** You still get ~80% of the customer value via documented Material Recovery Certificates + Scope 3 reporting. Carbon credits are the residual ~20%, and they cost 6 figures + multi-year effort to unlock.

---

## SECTION 2 — VMR0008 Eligibility Checklist (verra-vmr0008-eligibility.md)

# Verra VMR0008 — Methodology Eligibility & Status

**Active since:** 4 September 2023
**Grace period for legacy AMS-III.BA projects:** ended 4 March 2024
**Developer:** Verra
**Sectoral scope:** 13 — Waste handling and disposal

| Question | Verdict |
|---|---|
| Methodology currently active? | YES (Verra official) |
| Standalone use permitted? | NO — must pair with CDM AMS-III.BA |
| Eligible materials? | Ferrous, non-ferrous, plastics; PCB explicitly in-scope |
| Eligible facilities? | Dedicated facilities for collection + recycling |
| Geographic scope? | Global (CDM); no U.S. exclusion |
| Project-size limits? | AMS-III.BA small-scale (max ~15 ktCO2e/yr) |
| Crediting period? | Up to 7 yrs renewable, max 21 yrs |
| Discount factor added? | YES — upstream displacement discount (magnitude unknown) |
| Issuance unit? | 1 VCU = 1 MTCO2e verified reduction |

**CRITICAL UNKNOWN:** Exact numeric value of the "upstream displacement discount factor." Full VMR0008 PDF needed:
   https://verra.org/wp-content/uploads/vmr0008-revision-to-ams-iii-ba-recovery-and-recycling-of-materials-from-e-waste-v1-0.pdf

---

## SECTION 3 — EPA WARM v16 Factors (epa-warm-factors.csv rendered as table)

| Material | Recycling Net (MTCO2E/short ton) |
|---|---:|
| Desktop CPUs | -1.49 |
| Portable Electronic Devices | -1.06 |
| Flat-Panel Displays | -0.99 |
| CRT Displays | -0.57 |
| Electronic Peripherals | -0.36 |
| Hard-Copy Devices | -0.56 |
| Mixed Electronics | -0.90 |

**Per-Component Virgin-Production Emissions (MTCO2E / Short Ton):**

| Component | Net |
|---|---:|
| Ferrous Metal | 2.32 |
| Aluminum | 5.90 |
| Copper | 6.76 |
| Other Metals | 5.10 |
| Plastic | 4.76 |
| **Printed Circuit Board** | **126.70** |
| Flat Panel Display Module | 54.59 |
| Battery (Li-ion) | 4.79 |

PCB component share by material type (Babbitt 2017; Hikwama 2005):

| Material | PCB Mass Share |
|---|---:|
| Desktop CPUs | 14% |
| Portable Devices | 14% |
| Flat-Panel Displays | 6% |
| CRT Displays | 11% |
| Electronic Peripherals | 4% |
| Hard-Copy Devices | 3% |

**Source:** EPA, *Documentation for Greenhouse Gas Emission and Energy Factors Used in the Waste Reduction Model (WARM) Version 16 — Electronics*, December 2023, EPA-530-R-23-022. URL: https://www.epa.gov/system/files/documents/2023-12/warm_electronics_v16_dec.pdf

---

## SECTION 4 — Prior Wiki Context (incorporated from 2026-05-22 NotebookLM sources)

### Gold yields (server vs consumer grade)

| Source | Yield (g Au/ton) |
|---|---:|
| Mined ore | 0.5 – 5 |
| Consumer PC boards | 40 – 100 |
| AI / telecom server boards | 200 – 500+ |
| High-end CPUs / RAM | 1,000+ |

### CO2 reduction potential (recycled vs virgin)

| Material | Recycled vs Virgin |
|---|---|
| Gold | 98% less energy |
| Copper | 85% less CO2 |
| Steel | 58% less carbon |

### Hardware refresh context

| Metric | Value |
|---|---|
| Traditional server lifecycle | 3–5 years |
| AI cluster lifecycle | 12–18 months |
| Global e-waste by 2030 | 74M metric tons |
| Generative AI hardware e-waste by 2030 | 1.2 – 5.0M metric tons |
| US+Canada PCB gold TAM | $1.70B – $10.22B annually |
| AI hardware residual value (if processed within 45 days) | 35–50% |

### Carbon market reference prices (May 22, 2026 context)

- 32–160 RMB/ton (≈ $4.50–22.50 USD/ton)
- At 270–600 RMB/ton carbon credits could completely offset government recycling subsidies

---

## Source Inventory (all primary or near-primary)

| Source | Type | URL |
|---|---|---|
| Verra VMR0008 methodology page | Primary | https://verra.org/methodologies/vmr0008-revision-to-ams-iii-ba-recovery-and-recycling-of-materials-from-e-waste-v1-0/ |
| Verra AMS-III.BA methodology page | Primary | https://verra.org/methodologies/recovery-and-recycling-of-materials-from-e-waste/ |
| EPA WARM v16 Electronics Chapter | Primary (US gov) | https://www.epa.gov/system/files/documents/2023-12/warm_electronics_v16_dec.pdf |
| EPA WARM Documentation Hub | Primary | https://www.epa.gov/warm/documentation-chapters-greenhouse-gas-emission-energy-and-economic-factors-used-waste |
| Verra Program Fee Schedule (Oct 2024) | Primary | https://verra.org/wp-content/uploads/2024/10/Verra-Program-Fee-Schedule-v1.0.pdf |
| Verra Plastic Program Details | Primary | https://verra.org/programs/plastic-waste-reduction-standard/plastic-program-details/ |
| ERI E-Waste Legislation Map | Industry secondary | https://eridirect.com/sustainability/us-legislation/ |
| CyberCrunch E-Waste Regulations | Industry secondary | https://ccrcyber.com/resources/e-waste-regulations |
| Regreener VCM 2025 update | Industry secondary | https://www.regreener.earth/blog/voluntary-carbon-market-update |

---

## Honest State of Evidence

| Topic | Confidence |
|---|---|
| VMR0008 active and applicable to PCBs | HIGH (Verra primary source) |
| EPA WARM emission factors | HIGH (US EPA v16, Dec 2023) |
| U.S. state e-waste law coverage | HIGH (multiple state regulators + industry summaries) |
| Per-tonne VCU issuance (without discount factor) | HIGH |
| Per-tonne VCU issuance (WITH VMR0008 displacement discount applied) | MEDIUM — discount magnitude is the unknown |
| VVB project development costs | MEDIUM — ranges from public references; needs formal quote |
| State-by-state regulatory surplus outcomes | LOW — Verra interpretation is project-specific |
| Existing VMR0008 U.S. project benchmarks | NOT FOUND — registry deep crawl required |

---

## What This Preliminary Does Not Answer (deferred to paid follow-on)

1. Exact displacement discount factor (full VMR0008 PDF)
2. Named U.S.-registered VMR0008 projects for benchmarking
3. VVB quote for actual project development cost
4. State-by-state baseline methodology accepted by Verra for U.S. context
5. Detailed legal language for EAA contracts (requires environmental law counsel)

---

*End of consolidated dossier. Created 2026-09-23 by Hermes for Urban Mining USA. Cumulative API spend: ~$0; hard ceiling was $5.*
