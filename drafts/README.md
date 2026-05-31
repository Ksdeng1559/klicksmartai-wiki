# Garrett Health District Residences

**417 | 419 | [Adjacent Parcel] Garrett Street, Sapperton, New Westminster, BC**

---

## What's in this repo

| File | Description |
|------|-------------|
| `garrett-health-district-dom.md` | Developer Opportunity Memorandum — the pitch document for prospective developer partners |
| `garrett-street-feasibility.md` | Full feasibility study — planning, market, scenarios, financials, risks, recommendation |
| `garrett-health-district-residences-rlv.xlsx` | Residual Land Value Model — 5-sheet Excel workbook with sensitivity analysis |
| `app.py` | Flask web app — interactive RLV calculator |
| `templates/index.html` | DOM as a polished single-page web app |
| `Dockerfile` | Container definition |
| `docker-compose.yml` | Container orchestration |

---

## TL;DR

- **Site:** 3-lot assembly, ~15,000 sqft, RS zoned, Sapperton, New Westminster
- **Location:** 400m from Royal Columbian Hospital, 550m from Sapperton SkyTrain Station
- **Concept:** 6–8 storey purpose-built rental, healthcare workforce housing
- **TOD:** Tier 3 (BC legislation) — 3.0 FSR / 8 storeys entitlement
- **Verdict:** PROCEED WITH CAUTION — strong fundamentals, needs developer partner and non-market capital
- **Upside (Option B — Landowner Partnership):** ~$6.5–7.5M to landowners vs. ~$4.0–5.5M on a straight sale

---

## Running the Web App

### Option 1 — Docker (recommended)

```bash
git clone https://github.com/Ksdeng1559/garrett-health-district.git
cd garrett-health-district
docker compose up -d
# Open http://localhost:5000
```

### Option 2 — Local Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
# Open http://localhost:5000
```

---

## Financial Model

Open `garrett-health-district-residences-rlv.xlsx` in Excel or LibreOffice.

Sheets:
1. **Summary** — key outputs, scenario comparison
2. **6-Storey Model** — full input/output waterfall
3. **8-Storey Model** — full input/output waterfall
4. **Sensitivity** — cap rate × construction cost matrix
5. **Residual Land Value** — step-by-step calculation

**Key finding:** At base case ($430/sqft construction, 5.75% exit cap rate), residual land value is constrained. The project reaches viability through CMHC MLI Select financing, BC Housing co-investment, and DCL waiver — all achievable given the healthcare housing positioning.

---

## Capital Structure

| Option | Landowner Return | Complexity | Risk |
|--------|-----------------|-----------|------|
| Sell individually | ~$2.5M | Low | Low |
| Assemble + sell | $4.0–5.5M | Medium | Low |
| **Landowner Partnership** | **$6.5–7.5M** | **High** | **Medium** |

---

## Approval Pathway

- Current zoning: RS (single detached only)
- Rezoning required for all scenarios
- BC TOD legislation mandates Council consider 3.0 FSR / 8 storeys at Tier 3
- No public hearing required (Bill 44 — ≥50% residential)
- Estimated timeline: 18–24 months from application to permit

---

## Docker Deployment

```bash
# Build the image
docker build -t garrett-health-district:latest .

# Run
docker run -d --name garrett-health-district -p 5000:5000 garrett-health-district:latest
```

Or use `docker compose up -d` for the full stack with health check.

---

## Key Contacts

- **Prepared by:** Dennis — Landowner Representative
- **Date:** May 30, 2026
- **Confidentiality:** Recipients only — do not distribute without prior written consent
