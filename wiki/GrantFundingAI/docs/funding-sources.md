# Grant Funding Sources

Comprehensive reference for federal, state, tribal, and impact capital funding sources relevant to the GrantFundingAI system.

---

## 1. Grant Intelligence Reference Sources

### Grants Office

- https://www.grantsoffice.com/
- https://www.grantsoffice.com/Learn-from-Us/Guidance-for-Grantseekers
- https://www.grantsoffice.com/Learn-from-Us/Grant-News?category=290
- https://www.grantsoffice.com/Work-with-Us/For-Grantseekers
- https://communities.grantsoffice.com/s/

**Use cases:** Grant strategy education, opportunity trend monitoring, modeling the grant intelligence platform lifecycle.

> Grants Office demonstrates that successful grant seeking is a lifecycle process, not a one-time grant search.

---

## 2. Primary Federal Funding Portals

### Grants.gov

- https://www.grants.gov/

**Recommended fields to capture:**

| Field | Description |
|-------|-------------|
| Opportunity title | Program name |
| Opportunity number | Unique ID |
| Agency / Program office | Funding body |
| Eligibility | Who can apply |
| Deadline | Due date |
| Award ceiling | Max funding amount |
| Match requirement | Cost-share required |
| Funding instrument | Grant, cooperative agreement, etc. |
| Project category | Program area |
| Fit score | Relevance to project |
| Readiness gaps | What is missing |

### SBIR.gov

- https://www.sbir.gov/

**Best-fit technologies:** Waste-to-energy, solar and storage, housing technology, construction materials, AI grant intelligence, infrastructure analytics, climate resilience systems, public-sector decision support tools.

**Recommended fields to capture:**

| Field | Description |
|-------|-------------|
| Agency | Issuing agency |
| Topic number | Solicitation ID |
| Phase | I, II, or III |
| Technical objective | What the agency wants |
| Commercialization requirement | Market pathway |
| Research partner requirement | STTR requirement |
| Budget limit | Max award |
| Submission window | Open/close dates |
| Fit score | Technology alignment |

### SAM.gov

- https://sam.gov/

> SAM.gov should be monitored alongside grants because some opportunities may be better structured as pilots, procurement contracts, public-private partnerships, or vendor opportunities.

**Recommended fields to capture:** Notice ID, Agency, Department, Opportunity type, NAICS code, Set-aside status, Response deadline, Contact, Procurement stage, Relevance to project.

---

## 3. Federal Agencies to Monitor

### Department of Energy — DOE

Best fit: Clean energy, energy storage, grid resilience, community energy, renewable power, waste-to-energy, industrial decarbonization, building efficiency.

### Environmental Protection Agency — EPA

Best fit: Environmental justice, waste reduction, pollution prevention, climate resilience, circular economy, brownfield redevelopment, community environmental benefit.

### Department of Agriculture — USDA

Best fit: Rural development, rural energy, community facilities, agricultural waste conversion, rural infrastructure, economic development.

### Department of Housing and Urban Development — HUD

Best fit: Affordable housing, community development, CDBG programs, disaster recovery, housing resilience, neighborhood revitalization.

### Small Business Administration — SBA

Best fit: SBIR/STTR coordination, small business support, technical assistance, capital readiness, procurement readiness.

### Department of Defense — DoD

Best fit: Dual-use R&D, SBIR/STTR defense topics, C-sUAS and related critical technology areas.

### National Science Foundation — NSF

Best fit: Broad deep technology, AI, materials, engineering, Fast-track review for high-potential commercialization.

---

## 4. State, County, and Local Sources

### State Programs

**Use cases:** Energy incentives, housing programs, economic development, matching funds, infrastructure programs, resilience programs.

**Recommended fields:** State agency, Program name, Eligible applicants, Funding size, Match requirement, Local partner requirement, Application window, Project fit.

### County Programs

**Use cases:** Local infrastructure priorities, county economic development, letters of support, pilot sites, public-private partnerships, matching funds.

**County intelligence fields:** Housing need, waste burden, energy burden, infrastructure gaps, economic development priorities, tribal alignment, opportunity zones, local agency contacts, funding programs.

---

## 5. Tribal Funding Sources

**Use cases:** Tribal housing, tribal energy, broadband, transportation, waste management, infrastructure resilience, workforce development, economic development.

> Tribal funding should be treated as a dedicated opportunity layer because many federal programs prioritize tribal governments, tribal partnerships, underserved communities, energy resilience, broadband, housing, and infrastructure.

---

## 6. Foundation and Impact Capital Sources

### Community Development Financial Institutions — CDFIs

> CDFIs can provide implementation capital after grants reduce risk, validate feasibility, or fund planning.

### Donor-Advised Funds and Faith-Based Capital

**Use cases:** Mission-aligned capital, faith-based housing support, disaster relief alignment, community resilience, catalytic capital.

> Donor-advised and faith-based capital can supplement grants where community impact, housing, resilience, or disaster relief alignment is strong.

### Impact Investors and Family Offices

> Impact capital should be mapped after the grant strategy clarifies risk reduction, public support, and measurable community benefit.

---

## 7. Funding Source Classification

Every funding source should be classified using this structure:

| Field | Description |
|-------|-------------|
| Source type | SBIR, grant, contract, state program, county program, tribal program, CDFI, foundation, investor |
| Agency / institution | Funding body |
| Applicant type | Small business, county, nonprofit, tribe, university, developer, public-private partnership |
| Project fit | Housing, energy, waste, AI, infrastructure, resilience |
| Funding role | Planning, R&D, pilot, implementation, match, leverage, debt, equity |
| Deadline | Due date or rolling |
| Readiness impact | What must be true before applying |
| Capital stack role | Where this funding fits in the project stack |

---

## 8. Example Source-to-Project Match

**Input:** Whatcom County waste-to-energy + solar/storage + modular housing pilot. Partners: Spectra, Tiyo Energy, tribal partner, university partner.

```
SBIR Phase I       → technology validation
DOE                → clean energy / resilience
EPA                → waste reduction / environmental justice
USDA               → rural development / community facilities
HUD                → housing / community development
County funds       → local support / pilot site
CDFI               → implementation debt
Donor-advised funds → catalytic impact capital
Private investors  → scale capital
```

---

## 9. Operating Principle

Do not treat a grant as the whole solution. Treat each source as one layer in a larger funding strategy:

```
Grant + SBIR + Contract + County Support + CDFI + Impact Capital + Private Capital
```

The Funding Intelligence OS continuously connects:

```
Sources ↔ Problems ↔ Technologies ↔ Communities ↔ Agencies ↔ Partners
↔ Capital Stacks ↔ Proposals ↔ Outcomes
```