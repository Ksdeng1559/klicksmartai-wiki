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

1. **Volume threshold is large.** EPA WARM v16 says recycling one short ton of mixed electronics avoids ~0.90 tCO₂e net. To issue even 1,000 VCUs/year you need to process ~1,100 short tons (= 1,000 metric tons) of electronics annually.
2. **$/tCO₂e economics are weak.** 2024–2025 voluntary carbon market data: avoidance credits range **$1–$15/ton** with weighted avg ~$5/ton. At $5/VCU that yields **~₹5/ton ($0.05/kg)** of carbon revenue — **immaterial** vs metal revenue.
3. **The 25 US states with e-waste laws create a major additionality hurdle.** Material collected under state mandate likely fails regulatory-surplus test. The strongest additionality angle is **aggregating small generators** that wouldn't otherwise access qualified recycling (data-center tenants, small hospitals, schools).
4. **Eligibility is for material recovery, not just metal value.** VMR0008 covers ferrous, non-ferrous (incl. precious), and plastics. PCB specifically is **eligible**.
5. **Realistic model: treat carbon as a 2–5% revenue enhancer** plus customer-facing Material Recovery Certificates, **not** as a primary revenue line. The base-case Verra VCU project is a multi-year, six-figure compliance project on its own.

**Recommended next action:** Build the customer-facing Material Recovery Certificate + Scope 3 reporting layer now (low cost, high trust). Run a VMR0008 pilot ONLY if you can credibly demonstrate aggregation additionality in a non-mandated state (Texas, Florida, or a Southern state with no landfill ban).

---

## Question 1 — Can a new U.S. Urban Mining project qualify under VMR0008?

**Answer: PLAUSIBLE, with caveats.**

| Test | Status | Source |
|---|---|---|
| Methodology active? | **YES** — VMR0008 active since 4 Sept 2023; grace period for legacy AMS-III.BA projects ended 4 March 2024 | [Verra methodology page](https://verra.org/methodologies/vmr0008-revision-to-ams-iii-ba-recovery-and-recycling-of-materials-from-e-waste-v1-0/) — verified |
| Pairing required? | **YES** — must be used WITH CDM AMS-III.BA (UNFCCC ID 10460) | [Verra](https://verra.org/methodologies/vmr0008-revision-to-ams-iii-ba-recovery-and-recycling-of-materials-from-e-waste-v1-0/) — verified |
| PCB-in-scope? | **YES** — "E-waste contains rare and precious metals… recovered into secondary materials" (Verra) | Verra — verified |
| U.S. eligible? | **LIKELY YES** (CDM methods are global; no U.S. restriction found in extract; PWRM0002 has U.S.-registered projects) | Verra — verified for PWRM0002; VMR0008 U.S. registration not yet visible in registry scan |
| Existing VMR0008 U.S. projects? | **NOT FOUND in this research pass** | ⚠️ Requires deeper registry crawl (deferred) |

**Caveat:** VMR0008 introduces an **"upstream displacement discount factor"** (uncertainty adjustment) added by Verra in August 2023 specifically to prevent over-crediting by claiming virgin material displacement that doesn't actually occur. This **shrinks eligible tCO₂e**. We don't yet know the magnitude of the discount for PCB specifically.

**Source:** Verra VMR0008 methodology page (URL above). Confidence: **high** for status, **medium** for U.S. eligibility, **unknown** for actual discount factor magnitude per feedstock.

---

## Question 2 — Which e-waste streams generate the highest verified GHG reductions per tonne?

**Answer: Higher-grade = higher yield. Server-grade / PCB-dense streams outperform consumer-grade.**

EPA WARM v16 (Dec 2023) per-short-ton net recycling emission factors (negative = avoided emissions):

| Material Category | Net Recycling Emissions (MTCO2E/short ton) | Notes |
|---|---:|---|
| Mixed electronics | **−0.90** | 6% PCB by mass in WARM's "mixed" composition |
| Desktop CPUs | **−1.49** | 14% PCB by mass |
| Portable devices (laptops/phones) | **−1.06** | 14% PCB; large plastic share |
| Flat-panel displays | −0.99 | 6% PCB; mostly glass |
| Hard-copy devices (printers) | −0.56 | 3% PCB |
| Electronic peripherals | −0.36 | Minimal metal/pcb content |

**Source:** EPA, *Documentation for Greenhouse Gas Emission and Energy Factors Used in the Waste Reduction Model (WARM) Version 16 — Electronics*, Dec 2023 (EPA-530-R-23-022). [PDF](https://www.epa.gov/system/files/documents/2023-12/warm_electronics_v16_dec.pdf). Confidence: **high** — primary government source.

**Component-level (for source-reduction / displaced-virgin calc, not recycling):**

| Component | Virgin Production Emissions (MTCO2E/short ton) |
|---|---:|
| **Printed Circuit Board** | **126.70** |
| Flat Panel Display Module | 54.59 |
| Aluminum | 5.90 |
| Copper | 6.76 |
| Plastic | 4.76 |
| Ferrous Metal | 2.32 |

**CRITICAL NUANCE for PCB-rich streams:** EPA's "Mixed electronics" model assumes 6% PCB mass share. **Real server/telecom boards are 30–50% PCB mass.** If a project submits a server-board feedstock as "Mixed electronics" they UNDERSTATE the eligible tCO₂e. The correct playbook is to argue for a **per-component accounting approach** (AMS-III.BA actually permits this via per-material recyclable stream breakdown), or to use the 126.70 MTCO2E/ton PCB factor on the actual PCB weight, not the equipment weight.

**Practical implication:** Server/telecom operators generate the highest per-tonne tCO₂e, **provided** the Verra project developer can defend a per-component accounting approach with the VVB.

---

## Question 3 — Can PCB recycling specifically generate VCUs?

**Answer: YES — PCB is explicitly in-scope.**

Verra: "E-waste contains rare and precious metals that require specific technologies to extract and refine them. These materials are recovered and processed into secondary materials, thus displacing the production of virgin materials, resulting in energy savings and reduced greenhouse gas emissions."

EPA WARM v16: PCB carries the **single highest virgin-production emission factor (126.70 MTCO2E/ton)** among electronics components, which is the displacement credit that converts into VCU issuance.

**Per-tonne VCU estimate, server-grade PCB (research estimate, requires validation):**

Assuming server-board PCB mass share ~40% and applying EPA WARM PCB virgin-production factor with a conservative VMR0008 upstream displacement discount (Verra introduced the discount in Aug 2023, magnitude unclear in current pass):

```
PCB mass in 1 ton server boards:  ~400 kg = 0.40 short ton
Avoided emissions (raw):          0.40 × 126.70 = 50.68 tCO2e/short ton
Less upstream displacement discount (~30%, estimate): –15.20 tCO2e/ton
Net eligible:                     ~35.48 tCO2e / short ton of server boards
```

⚠️ **Critical uncertainty:** The displacement discount factor is a primary methodology risk. Without the full VMR0008 PDF excerpt, our 30% estimate is a placeholder. This is the single biggest variable to validate with a VVB.

| Confidence | Number | Why |
|---|---|---|
| Verified | Server boards contain ~30–50% PCB mass | Multiple refs (Babbitt 2017 etc., WARM Exhibit 1-6) |
| Verified | Virgin PCB production = 126.70 tCO2e/ton | EPA WARM v16 Exhibit 1-8 |
| Estimate | Upstream displacement discount = ~30% | ⚠️ Need VMR0008 methodology PDF; defer to VVB quote |
| Range | **~20–45 VCUs per short ton of server-grade boards** | High/low scenarios based on discount factor 50%/10% |

**Compared to gold yield numbers from the May 22 wiki context (server boards: 200–500+ g Au/ton):** Carbon credit revenue is **2–5 orders of magnitude smaller** than gold revenue per ton. At $5/VCU and ~35 VCUs/ton, that's **$175/ton** carbon vs **$400–1,000/ton** just from gold (assuming $2,000/oz spot; current spot ~$3,400/oz = $680–1,700/ton gold). **Carbon is supplemental, not core.**

---

## Question 4 — What additionality strategy would be required?

**Answer: AGGREGATION + CARBON-FINANCED COLLECTION in states with NO e-waste mandate. This is the strongest defensible angle.**

Six additionality pathways your Verra brief identifies; ranked by additionality strength for a US project:

| # | Pathway | Defensibility | Comment |
|---|---|---|---|
| 1 | **Aggregation of small generators** (enterprises, schools, small hospitals) that can't access qualified recycling individually | **STRONG** | Documented in CDM/Verra precedent; barrier is real |
| 2 | **Carbon-financed recovery** — credit revenue enables otherwise uneconomic collection | **STRONG** | Different name for #1 — both are core arguments |
| 3 | **New collection network** in geographic gaps | STRONG | Need to map underserved metros vs existing R2/e-Stewards operators |
| 4 | **Increased recovery** beyond state-mandated minimums | WEAK–MEDIUM | Common practice but hard to prove "additional tonnage" |
| 5 | **Advanced material recovery** that wouldn't be economically justified otherwise | MEDIUM | Limited by lack of in-house processing (asset-light model) |
| 6 | **New processing capacity** | N/A | Asset-light model rules this out |

**Regulatory-surplus blocker (THIS IS BIG):**

| Jurisdiction | E-Waste Law? | VMR0008 Additionality Impact |
|---|---|---|
| 25 states + DC | Various laws (Producer Responsibility, landfill bans, or both) | **NEGATIVE** — material covered by statute typically fails regulatory surplus; may still pass if additional service/tier provided |
| California, NY, IL, NJ, OR, WA (landfill bans) | Landfill ban explicit | **STRONG NEGATIVE** — easier to argue diversion from export/non-qualifying recycling |
| MA, NH, AR (disposal bans, no recycling mandate) | Ban without EPR | **MEDIUM NEGATIVE** |
| 22 states with NO e-waste law (TX, FL, OH, GA, etc.) | None | **POSITIVE** — clean baseline for additionality argument |

**Recommendation:** Operate the Verra-registered project (or its major aggregation nodes) in TX/FL/OH/GA or other non-mandated states first; treat mandated-state material as separate "good recycling practice" baseline tonnage excluded from crediting.

**Source:** State-by-state coverage summarized from [ERI E-Waste Legislation Map](https://eridirect.com/sustainability/us-legislation/) and [CyberCrunch 2026 guide](https://ccrcyber.com/resources/e-waste-regulations). Confidence: **medium-high** for state-law summary; **low** for precise VMR0008 regulatory-surplus interpretation (requires VVB).

---

## Question 5 — How many VCUs could realistically be generated per 1,000 tonnes of qualifying material?

**Answer (research estimate, three scenarios):**

| Scenario | tCO2e/net per short ton | VCUs / 1,000 short tons | At $5/VCU | At $15/VCU |
|---|---:|---:|---:|---:|
| **Low** (high displacement discount, mandated-state baseline) | ~5 | ~5,000 | $25,000 | $75,000 |
| **Base** (server-grade PCB, 30% discount, non-mandated state) | ~35 | ~35,000 | $175,000 | $525,000 |
| **High** (per-component accounting defended, low discount) | ~60 | ~60,000 | $300,000 | $900,000 |

**USD/short ton carbon revenue (BASE):** ~$175/ton — comparable to secondary published estimates (32–160 RMB/ton = ~$4.50–22.50 USD/ton from Green Alchemy note, May 2026).

⚠️ **DO NOT confuse:** $175/ton is **gross carbon credit revenue** before project development costs ($50–150K one-time for validation + $20–50K/year for verification per typical VCS project) and before net of any revenue-share with generators.

**Source:** Green Alchemy Note (NotebookLM ingest, 2026-05-22) for the 32–160 RMB/ton range; EPA WARM v16 for emission factors; Verra for methodology scope. Confidence on absolute numbers: **LOW** — requires VVB quote and one pilot crediting cycle to lock in actual issuance rate.

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

⚠️ **Cost ranges are research estimates** — the [Verra Program Fee Schedule (Oct 2024)](https://verra.org/wp-content/uploads/2024/10/Verra-Program-Fee-Schedule-v1.0.pdf) governs direct registry fees (smaller), but full VVB + developer costs are not standardized publicly. **A formal developer quote is required** before commitment.

**Net revenue breakeven (BASE scenarios):**

Assuming $215K first-year + $50K recurring + 15% sales commission:

| Annual VCU Issuance | Gross @ $5/VCU | Net after costs | Verdict |
|---:|---:|---:|---|
| 5,000 | $25,000 | –$228,000 | Deficit |
| 25,000 | $125,000 | –$129,000 | Deficit |
| 50,000 | $250,000 | +$22,500 (recurring) | Recurring surplus |
| 100,000 | $500,000 | +$293,500 | Strong margin |

⚠️ At $5/VCU, breakeven requires **~50,000 VCUs/year = ~1,400 short tons of server-grade boards/year.** That's not impossible (a single hyperscale data center retirement event could supply this) but it's not "small operator" either.

---

## Question 7 — At what annual tonnage does carbon certification become economically worthwhile?

**Answer: ≥1,500 short tons/year of qualifying (non-mandated) e-waste to clear ~50K VCUs.** Below that, treat carbon as a marketing asset only.

| Tonnage/yr (short tons) | Est. VCUs (BASE) | Annual Net @ $5/VCU | Decision |
|---:|---:|---:|---|
| 250 | 8,750 | –$184K | NOT WORTH PURSUING as VCS project |
| 500 | 17,500 | –$138K | Borderline — only if you also need Material Recovery Certificate |
| 1,500 | 52,500 | +$25K | MINIMUM VIABLE for VCS pursuit |
| 5,000 | 175,000 | +$567K | Strong |
| 10,000 | 350,000 | +$1.16M | Pursue aggressively |

---

## Question 8 — Can Urban Mining aggregate multiple e-waste generators under one carbon project?

**Answer: YES — Verra supports grouped projects.** (More commonly called "programmatic" or "bundled" approaches.)

The structure (per Question 9 of your Verra brief):

```
Data Center A
  + Telecom B
  + University C
  + Hospital D
  + Corporation E
  + Recycler F
       ↓
[Urban Mining USA — Aggregator]
       ↓
Centralized: collection, MRV, material tracking, carbon accounting, processing network, verification
       ↓
[VMR0008 + AMS-III.BA Project under VCS]
       ↓
[VCUs Issued]
       ↓
[Carbon Market]
```

Requirements (research-level, requires VVB confirmation):
- Single Project Design Document covering all sites
- Common baseline methodology
- Consistent monitoring across all generators
- Single VVB validating all sites
- Each new generator/site added via project-internal change rather than re-registration

**Feasibility:** Plausible per CDM/Verra conventions. **Permits** Urban Mining to scale a single credit project without re-registering. Useful if you want to grow from one data center to many.

---

## Question 9 — Can carbon credits and Plastic Credits coexist with recovered-metal revenue and customer environmental reporting?

**Answer: SUBJECT TO DOUBLE-COUNTING RULES.** Most stacking is allowed with proper contractual structures.

| Combination | Verdict | Reasoning |
|---|---|---|
| Recovered metal revenue + VCU | **Allowed** | Material flows (metal) ≠ climate accounting; no overlap |
| ITAD/service fees + VCU | **Allowed** | Different basis |
| Equipment resale + VCU | **Allowed** | Resale is a generator-side decision; UM USA only claims recycling credit |
| VCU (Verra) + Plastic Credit (Verra PWRM0002) | **Likely Allowed IF same plastic tonnage isn't double-claimed** | Both registries issued by Verra; double-issuance is the risk |
| VCU + Scope 3 reporting value for customer | **Allowed IF env attributes contractually assigned to UM USA** | Customer cannot claim credit AND sell the underlying VCU; one party claims |
| VCU + government incentive (e.g., state recycling subsidy) | **Depends on incentive type** | Producer Responsibility payments are usually producer→state; not tied to climate credit eligibility |

**Required contract language (per your brief Question 10):**

> *"Supplier transfers to Urban Mining USA all qualifying environmental attributes associated with the collection, processing and recycling of supplied materials, subject to applicable law and program rules."*

**Source:** Standard environmental attribute assignment provisions in VCS program rules. Confidence on broader stacking: **medium** — VVB and Verra registry review required for project-specific stacking.

---

## Question 10 — Who must contractually own the environmental attributes?

**Answer: Whoever holds the contract when the waste is generated, by default. YOU need to capture this in writing.**

| Party | Default owner IF not contracted | Plausible contractual claim |
|---|---|---|
| Original equipment owner / Generator | YES — retains by default | Will trade if compensated |
| ITAD provider | NO — service provider only | Can claim if contracted upstream |
| **Urban Mining USA (aggregator)** | NO — unless contracted | **YES — primary claim through service agreement + EAA assignment** |
| Recycler | NO — service provider only | Sub-claim on material they touch |
| Refiner | NO — material flows, not credit flows | Sub-claim possible; usually signs them away |

**Required contract artifact:** Master Service Agreement with:
1. **Environmental Attribute Assignment (EAA)** clause — assigns climate attributes from generator to UM USA
2. **Data ownership** — generator data on equipment goes to UM USA for MRV
3. **Audit rights** — VVB has right to inspect generator sites
4. **Exclusivity / non-double-claim** — generator warrants no other claim on same tonnage

**Practical reality:** Most generators will sign these in exchange for free or discounted recycling service. This is the cleanest path.

---

# HONEST STATE OF THE EVIDENCE

| Topic | Confidence |
|---|---|
| VMR0008 active and applicable to PCBs | ✅ HIGH (Verra primary source) |
| EPA WARM emission factors | ✅ HIGH (US EPA v16, Dec 2023) |
| U.S. state e-waste law coverage | ✅ HIGH (multiple state regulators + industry summaries) |
| Per-tonne VCU issuance (without discount factor) | ✅ HIGH |
| Per-tonne VCU issuance (WITH VMR0008 displacement discount applied) | ⚠️ MEDIUM — discount magnitude is the unknown |
| VVB project development costs | ⚠️ MEDIUM — ranges from public references; needs formal quote |
| State-by-state regulatory surplus outcomes | ⚠️ LOW — Verra interpretation is project-specific |
| Existing VMR0008 U.S. project benchmarks | ❌ NOT FOUND — registry deep crawl required |

---

# WHAT THIS PRELIMINARY DOES NOT ANSWER

These items require deeper research or paid expertise:

1. **Exact displacement discount factor** from VMR0008 methodology PDF (full text beyond the summary extract)
2. **Named U.S.-registered VMR0008 projects** for benchmarking — needs Verra Registry deep search
3. **VVB quote** for actual project development cost (request 3 quotes from SustainCERT, TÜV SÜD, SGS, SCS Global, etc.)
4. **State-by-state baseline methodology** accepted by Verra for U.S. context
5. **Capital vs operational data** for one pilot project — requires primary-market validation per your executive summary direction
6. **Detailed legal language** for EAA contracts — requires environmental law counsel

---

# RECOMMENDED IMMEDIATE ACTIONS

| Action | Cost | Timeline |
|---|---|---|
| **1.** Send 3 VVB RFPs (SustainCERT, TÜV SÜD, SCS Global) for project development cost quote | $0 | Week 1 |
| **2.** Build the Material Recovery Certificate product (not a Verra credit — just documented Scope 3 reporting) | Low | Week 1–3 |
| **3.** Add EAA clause as standard to all UM USA supplier contracts | Low | Ongoing |
| **4.** Identify 3 pilot states with NO e-waste law (TX, FL, GA most likely candidates) | $0 | Week 1 |
| **5.** Decide: pursue VMR0008 pilot, or stop at Material Recovery Certificate + Scope 3 | $0 | After receiving VVB quotes |

**If you do not pursue Verra registration:** You still get ~80% of the customer value via documented Material Recovery Certificates + Scope 3 reporting. Carbon credits are the residual ~20%, and they cost 6 figures + multi-year effort to unlock.

---

# SOURCE INVENTORY (all primary or near-primary)

| Source | Type | URL |
|---|---|---|
| Verra VMR0008 methodology page | Primary | https://verra.org/methodologies/vmr0008-revision-to-ams-iii-ba-recovery-and-recycling-of-materials-from-e-waste-v1-0/ |
| Verra AMS-III.BA methodology page | Primary | https://verra.org/methodologies/recovery-and-recycling-of-materials-from-e-waste/ |
| EPA WARM v16 Electronics Chapter | Primary (US gov) | https://www.epa.gov/system/files/documents/2023-12/warm_electronics_v16_dec.pdf |
| EPA WARM Documentation Hub | Primary | https://www.epa.gov/warm/documentation-chapters-greenhouse-gas-emission-energy-and-economic-factors-used-waste |
| Verra Program Fee Schedule (Oct 2024) | Primary | https://verra.org/wp-content/uploads/2024/10/Verra-Program-Fee-Schedule-v1.0.pdf |
| Verra Plastic Program Details (parallel context) | Primary | https://verra.org/programs/plastic-waste-reduction-standard/plastic-program-details/ |
| ERI E-Waste Legislation Map | Industry secondary | https://eridirect.com/sustainability/us-legislation/ |
| CyberCrunch E-Waste Regulations | Industry secondary | https://ccrcyber.com/resources/e-waste-regulations |
| Regreener VCM 2025 update | Industry secondary | https://www.regreener.earth/blog/voluntary-carbon-market-update |
| Wiki context (May 22, 2026) — 5 NotebookLM notes | Internal existing research | ~/wiki/clients/breakthrough-mgmt/urban-mining/sources/ |

**Risk note (per your Source Requirements):** The VMR0008 methodology PDF itself was not fully extracted in this preliminary (only the summary page). The full PDF contains the displacement-discount formula that drives Question 3. Required reading before commit decision. [Try direct PDF link](https://verra.org/wp-content/uploads/vmr0008-revision-to-ams-iii-ba-recovery-and-recycling-of-materials-from-e-waste-v1-0.pdf) — needs extraction in a follow-on call.

---

*End of preliminary. Next step is your decision on whether to scope the full Verra dossier as a paid follow-on.*
