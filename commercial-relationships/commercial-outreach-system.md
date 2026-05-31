# COMMERCIAL LENDING OUTREACH SYSTEM
## Executive Summary Routing Engine
### For: Garrett Health District Residences

---

## SYSTEM OVERVIEW

**Purpose:** Automate targeted outreach of executive summaries to:
1. Bank BDMs (LinkedIn + email)
2. Commercial mortgage brokers (direct relationships)
3. Alternative lenders (credit unions, BDC, CMHC)
4. Institutional debt funds

**Workflow:**
```
SIGNAL → PERSONA MATCH → TEMPLATE SELECT → TARGET IDENTIFICATION → OUTREACH DRAFT → HITL APPROVAL → DELIVERY → TRACKING
```

**Key Principle:** Human‑in‑the‑loop (HITL) on all external communications. System drafts, human approves before sending.

---

## MODULE 1: TARGET IDENTIFICATION STRATEGY

### A. Bank BDM Discovery (LinkedIn Focus)

**Search Queries:**
1. Site:linkedin.com "Commercial Real Estate" "Business Development Manager" RBC
2. Site:linkedin.com "CRE" "BDM" "Toronto"
3. Site:linkedin.com "Commercial Mortgage" "Manager" "CIBC"
4. Site:linkedin.com "Real Estate Finance" "Senior Manager" "BMO"

**Filters:**
- Location: Toronto, Vancouver, Calgary
- Company: RBC, TD, CIBC, BMO, Scotia, NBC
-B Title: "Business Development Manager", "Director Commercial Real Estate", "VP CRE"

**Output Format (CSV):**
```
Name,Title,Company,Location,LinkedIn URL,Email (if found),Persona Tier,Last Contact,Status
```

### B. Commercial Broker Discovery

**Sources:**
1. Google: "commercial mortgage broker New Westminster BC"
2. Google: "CRE broker Vancouver"
3. Industry directories: Mortgage Architects, Dominion Lending Centres
4. LinkedIn: "Commercial Mortgage Broker" "Vancouver"

**Filters:**
- Specialization: Commercial real estate
- Location: BC (priority), then Canada‑wide
- Company size: Independent or boutique (more responsive)

### C. Alternative Lender Contacts

**Pre‑Defined Contacts:**
1. **CMHC:** Business Development contacts by region
2. **BDC:** Real Estate Finance account managers
3. **Credit Unions:** Vancity, Coast Capital, Envision CRE lenders
4. **BC Housing:** Development finance contacts

**Research Method:**
- Company websites → "Contact our lending team"
. LinkedIn: company pages → "Employees" → filter by "lending", "finance", "underwriting"

---

## MODULE 2: OUTREACH TEMPLATES

### LinkedIn Connection Request Message

**Template A (Bank BDM):**
```
Hi [First Name],

I'm reaching out because you specialize in commercial real estate lending for healthcare‑anchored projects.

We're structuring financing for Garrett Health District Residences — a 75‑unit purpose‑built rental 550m from Sapperton SkyTrain, anchored by 2,000+ Royal Columbian Hospital healthcare workers.

The project qualifies for CMHC MLI Select (DSCR 1.35 at 65% LTV). Would you be open to reviewing the executive summary?

Best,
[Your Name]
```

**Template B (Commercial Broker):**
```
Hi [First Name],

I noticed your expertise in commercial mortgage financing in BC.

We have a complete submission package for Garrett Health District Residences — a 75‑unit healthcare‑worker rental in Sapperton with CMHC eligibility.

The package includes credit memo, RLV model, and lender match list — ready for your network. Interested in reviewing?

Best,
[Your Name]
```

### LinkedIn Follow‑Up (After Connection)

**Template:**
```
Thanks for connecting, [First Name].

Attached is the 1‑page executive summary on Garrett Health District Residences. Key highlights:
1. DSCR 1.35 (with CMHC MLI Select at 5.0%)
2. LTV 65%
3. 2,000+ healthcare worker demand anchor
4. Municipal DCL waiver support

Full credit memo available if you'd like to review.

Best,
[Your Name]
```

### Email Outreach (If Email Found)

**Subject:** Garrett Health District — 75‑unit healthcare housing @ Sapperton SkyTrain

**Body (Bank BDM):**
```
Hi [First Name],

I'm reaching out because you work with healthcare‑anchored commercial real estate projects.

Garrett Health District Residences is a 75‑unit purpose‑built rental located 550m from Sapperton SkyTrain Station and 400m from the $2B Royal Columbian Hospital expansion.

The project qualifies for CMHC MLI Select financing, producing:
- DSCR: 1.35
.
- LTV: 65%
- Loan request: $16M construction + mini‑perm

Attached is the 1‑page executive summary. Full credit memo available for review.

Would this be worth a brief discussion?

Best,
[Your Name]
```

**Body (Commercial Broker):**
```
Hi [First Name],

I understand you work with commercial mortgage submissions in BC.

We have a turnkey submission package for Garrett Health District Residences — a 75‑unit healthcare‑worker rental in Sapperton that qualifies for CMHC MLI Select.

The package includes:
1. Complete credit memo (12‑page)
2. Residual Land Value model (Excel)
3. Lender match list (CMHC + bank + credit union)
4. Conditions checklist

This saves 20+ hours of packaging time. Interested in reviewing?

Best,
[Your Name]
```

---

## MODULE 3: CRM TRACKING SYSTEM

### File Structure
```
/home/denni/wiki/commercial-relationships/
├── targets/
│   ├── bdm-list.csv
│   ├── broker-list.csv  
│   ├── lender-list.csv
│   └── institutional-list.csv
├── outreach/
│   ├── sent/
│   ├── pending/
│   └── responses/
├── templates/
│   ├── linkedin-connection.md
│   ├── linkedin-followup.md
│   ├── email-bdm.md
│   └── email-broker.md
└── system/
    ├── workflow.md
    └── tracking.md
```

### CSV Schema (bdm-list.csv)
```csv
id,first_name,last_name,title,company,location,linkedin_url,email,source,persona_tier,last_contact_date,contact_method,response_status,notes
1,John,Smith,BDM Commercial Real Estate,RBC,Toronto,https://linkedin.com/in/johnsmith,john.smith@rbc.com,LinkedIn Search,Tier 1,2026‑05‑30,LinkedIn Connection,Sent,"Interested in healthcare projects"
```

### Status Tracking
```
PENDING → DRAFTED → AWAITING_APPROVAL → SENT → RESPONDED → FOLLOW_UP → CLOSED
```

---

## MODULE 4: EXECUTIVE SUMMARY ATTACHMENTS

### One‑Pager Requirements

**Bank BDM Version (Page 1 only):**
```
GARRETT HEALTH DISTRICT RESIDENCES
Executive Summary — Bank BDM

KEY METRICS
Loan Request: $16,000,000
DSCR: 1.35 (with CMHC MLI Select)
LTV: 65%
Project Value: $24,780,000
Location: 550m to Sapperton SkyTrain

HEALTHCARE DEMAND ANCHOR
• 2,000+ Royal Columbian Hospital staff within 400m
• $2B hospital expansion (Phase 2‑3)
• Sub‑1% vacancy risk

FINANCING STRUCTURE
• CMHC MLI Select eligible (5.0% rate)
• Municipal DCL waiver application
• BC Housing co‑investment opportunity

CONTACT
[Your Name]
[Your Title]
[Phone]
[Email]
```

**Broker Version (Page 1 only):**
```
GARRETT HEALTH DISTRICT RESIDENCES
Turnkey Submission Package — Commercial Broker

PACKAGE INCLUDES:
1. Complete credit memo (12‑page)
2. Residual Land Value model (Excel)
3. Lender match list (ranked 1‑5)
4. Conditions checklist
5. Appraiser/environmental contacts

TIME SAVED: 20+ hours of packaging

BEST LENDER FITS:
1. CMHC MLI Select — Primary (5.0% rate)
2. Bank CRE — Secondary (with CMHC backing)
3. Credit Union — Tertiary (community impact)

COMMISSION STRUCTURE:
Standard commercial mortgage brokerage fees apply

CONTACT
[Your Name]
[Your Title]
[Phone]
[Email]
```

---

## MODULE 5: HUMAN‑IN‑THE‑LOOP WORKFLOW

### Step‑by‑Step Approval Process

**1. Target Identification (Auto)**
- System searches LinkedIn, directories
  
**2. Draft Outreach (Auto)**
- System generates personalized message using template

**3. Human Review (Manual)**
- Review: name, company, personalization accuracy
- Edit: adjust tone, add specific references

**4. Approval (Manual)**
- Explicit "APPROVE" or "SEND" command required
"Looks good" is NOT approval — must be "send it", "approved", "go ahead"

**5. Delivery (Auto after Approval)**
 - LinkedIn connection request or message
- Email (if address available)

**6. Tracking (Auto)**
- Log date, method, message content
++ Update status in CRM

### Approval Triggers
```
ACTION                  REQUIRES APPROVAL?
─────────────────────────────────────────────
Search targets          NO
Draft message           YES (before sending)
Send LinkedIn request   YES
Send follow‑up          YES
Send email              YES
Update CRM status       NO
```

---

## MODULE 6: SEARCH AUTOMATION SCRIPTS

### LinkedIn Search via Web Search

**Python Script (conceptual):**
```python
# Pseudocode for LinkedIn profile discovery
queries = [
    'site:linkedin.com "Commercial Real Estate" "Business Development Manager" RBC',
    'site:linkedin.com "CRE" "BDM" "Toronto"',
    'site:linkedin.com "Commercial Mortgage" "Manager" "CIBC"'
]

for query in queries:
    results = web_search(query, limit=10)
    extract_profiles(results)
    save_to_csv()
```

### Commercial Broker Directory Search

**Sources:**
1. Mortgage Architects directory
2. Dominion Lending Centres commercial specialists
3. Google Maps: "commercial mortgage broker" Vancouver

**Extraction Pattern:**
- Company name
- Broker name
-B Contact info
- Specialization (commercial vs. residential)

---

## MODULE 7: INTEGRATION WITH KLICKSMARTAI SYSTEMS

### Signal Pipeline Connection
```
WEALTH WIRE RADAR → COMMERCIAL OUTREACH ENGINE
Signal Detection → Persona Match → Template Selection → Draft Generation
```

### CRM Data Flow
```
OUTREACH SYSTEM → HERMES RELATIONSHIP TRACKER → GOOGLE SHEETS
Contact details → Status updates → Pipeline tracking
```

### Task Management Integration
```
GOOGLE SHEET "Tasks" → OUTREACH ACTIONS
"Contact BDM at RBC" → Draft message → Approval → Send
```

---

## IMMEDIATE IMPLEMENTATION STEPS

### Phase 1: Setup Foundations (1 day)
1. Create target CSV files with sample data
2. Create outreach templates in /templates/
3. Build one‑pager executive summaries
4. Establish HITL workflow documentation

### Phase 2: Target Discovery (2 days)
1. LinkedIn searches for 20 BDMs
2. Broker directory research (15 brokers)
3. Compile into CSV with personas
4. Categorize by tier (Tier 1‑3)

### Phase 3: Draft & Approval Cycle (3 days)
1. Draft 10 LinkedIn connection requests
2. Human review + approval
3. Send approved requests
4. Track responses

### Phase 4: Scale & Automate (1 week)
1. Build Python script for LinkedIn search
2. Create automated draft generation
3. Integrate with Hermes task management
4. Build response tracking dashboard

---

## EXPECTED OUTPUTS

### Week 1:
- 20‑30 qualified BDM contacts identified
- 10‑15 commercial broker contacts
- 5‑10 outreach messages approved and sent

### Week 2:
- 3‑5 responses from BDMs/brokers
- 2‑3 lender introductions
- 1‑2 submission packages delivered

### Week 3:
- First lender underwriting review initiated
-TCMHC MLI Select application started

---

## SUCCESS METRICS

| Metric | Target |
|--------|--------|
| LinkedIn connection acceptance rate | ≥30% |
| Email response rate | ≥15% |
| Submission package requests | ≥5 |
| Lender underwriting reviews initiated | ≥2 |
| Days to first lender meeting | ≤21 |

---
**System Ready for Implementation**