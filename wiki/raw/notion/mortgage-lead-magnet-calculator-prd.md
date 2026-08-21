# Source: Notion (page 3a39e94c-f0a4-811d-8143-cf8912f86e01)

## Product overview
**Product:** Mortgages by Dennis Eng Calculator Suite  
**Domain:** [mortgagesbydenniseng.ca](http://mortgagesbydenniseng.ca)  
**Status:** Proposed  
**Primary market:** British Columbia, with priority on Metro Vancouver  
**Primary objective:** Convert anonymous website visitors into qualified mortgage opportunities by giving them immediate, transparent, scenario-specific value before asking for a full mortgage application.
The calculator suite contains three core diagnostic tools:
1. **Self-Employed Mortgage Qualification Calculator** — compares tax-document income with bank-statement and business-cash-flow evidence.
2. **As-Is vs As-Complete Construction Value Calculator** — evaluates construction feasibility, leverage, equity, value creation, and exit risk.
3. **Debt Refinance Savings Calculator** — compares current high-interest monthly debt pressure with a consolidated mortgage scenario.
A **Free Property Valuation and Mortgage Equity Report** acts as the front-door lead magnet and routes users into the most relevant calculator.
The governing product principle is:
> Give the borrower a useful preliminary answer first, then ask for the information required to complete a professional mortgage review.
---
## 1. Business problem
Most mortgage websites ask visitors to book a call or complete a full application before demonstrating value. This creates friction, especially for borrowers who:
- do not know whether they qualify;
- have complex self-employed income;
- are considering a construction or development project;
- are under pressure from high monthly debt payments;
- do not know how much equity they can access;
- have already been declined by a bank;
- are not ready to speak with a broker until they understand the potential outcome.
The calculator suite reduces this trust gap by providing a structured preliminary assessment while clearly separating an educational estimate from lender approval.
---
## 2. Product vision
The calculators should function as **diagnostic lead magnets**, not simple payment widgets.
Each calculator must:
- solve a real borrower problem;
- explain the assumptions behind the result;
- identify missing information;
- show possible financing pathways without promising approval;
- create a structured lead record in Atomic CRM;
- recommend the next best action;
- support English first, with future Cantonese and Mandarin adaptations;
- generate a web report and optional downloadable PDF summary;
- support SEO landing pages, local pages, articles, and paid campaigns.
The calculators should feed a shared decision layer:
```plain text
Visitor input
    ↓
Preliminary calculation
    ↓
Scenario classification
    ↓
Missing-document check
    ↓
Likely lender pathway
    ↓
Atomic CRM opportunity
    ↓
Dennis review and follow-up
```
---
## 3. Target users
### 3.1 Self-employed borrower
- incorporated business owner;
- sole proprietor;
- contractor;
- commission earner;
- real-estate professional;
- seasonal or variable-income borrower;
- borrower whose reported taxable income understates business cash flow.
### 3.2 Construction borrower
- owner-builder;
- custom-home borrower;
- small builder or developer;
- laneway-house or coach-house project;
- duplex, multiplex, or SSMUH project;
- purpose-built rental project;
- investor completing a renovation or value-add project.
### 3.3 Debt-refinance borrower
- homeowner carrying high-interest credit cards;
- homeowner with CRA debt;
- borrower with unsecured loans or lines of credit;
- borrower renewing from a private or second mortgage;
- borrower seeking lower monthly payments;
- borrower with equity across one or more properties.
---
## 4. Product architecture
### 4.1 Front-door lead magnet
**Free Property Valuation and Mortgage Equity Report**
Primary promise:
> See what your property may be worth, how much equity may be available, and which mortgage strategy may improve your position.
The report should collect the minimum information required to provide value:
- property address;
- property type;
- owner-occupied or rental;
- estimated value or automated valuation range;
- current mortgage balance;
- HELOC, second-mortgage, or other registered debt;
- current mortgage payment and maturity date;
- borrower objective.
The report then routes the visitor to:
- self-employed income review;
- construction feasibility review;
- debt-refinance review;
- general equity-access review;
- multiple-property portfolio review.
### 4.2 Shared services
The three calculators should use common platform services:
- mortgage-payment engine;
- amortization engine;
- LTV and equity engine;
- scenario comparison engine;
- document-readiness engine;
- lender-pathway rules engine;
- PDF/report generator;
- Atomic CRM integration;
- analytics and attribution;
- consent and privacy controls;
- save-and-resume capability.
---
## 5. Calculator 1 — Self-Employed Mortgage Qualification Calculator
### 5.1 Public-facing name
**Tax Documents vs Bank Statements Mortgage Calculator**
Alternative title:
**Business Income Mortgage Calculator**
### 5.2 User question
> Do my tax documents or my business bank statements show a stronger mortgage-qualifying income?
### 5.3 Core outcome
The calculator compares two preliminary income-recognition methods:
1. tax-document method;
2. bank-statement or business-cash-flow method.
It must not suggest that tax deductions create a tax or mortgage advantage. It should explain that legitimate deductions may reduce taxable income and that some alternative lenders may review additional business evidence.
### 5.4 Required inputs
#### Borrower profile
- province;
- purchase, refinance, renewal, or equity takeout;
- property value or purchase price;
- requested mortgage amount;
- down payment or current secured debt;
- estimated credit range;
- years in business;
- business structure.
#### Tax-document method
- T1 Line 15000 income;
- reported business income;
- T4 or T4A income;
- salary from corporation;
- dividends received;
- two-year income history;
- eligible addbacks;
- other recurring personal income.
#### Bank-statement method
- six- or twelve-month review period;
- total business deposits;
- transfers between owned accounts;
- loan proceeds;
- GST, PST, or other tax collections;
- refunds and one-time deposits;
- non-business deposits;
- operating-expense ratio;
- existing business debt payments;
- salary or dividends already counted elsewhere.
#### Personal obligations
- property taxes;
- heating estimate;
- condo fees;
- credit cards;
- loans and lines of credit;
- vehicle payments;
- support obligations;
- existing mortgage payments.
### 5.5 Core calculations
```plain text
Tax-document recognized income =
Documented personal income
+ eligible addbacks
+ permitted business-income adjustments
```
```plain text
Eligible business deposits =
Gross deposits
− transfers
− loan proceeds
− tax collections
− refunds
− non-recurring deposits
```
```plain text
Estimated business cash flow =
Eligible business deposits × (1 − expense ratio)
```
```plain text
Bank-statement recognized income =
Estimated business cash flow
− existing business debt obligations
− income already counted elsewhere
```
### 5.6 Results
Display side-by-side:
- recognized annual income;
- recognized monthly income;
- estimated mortgage range;
- estimated purchase-price range;
- estimated refinance capacity;
- income-method difference;
- documentation confidence;
- missing documents;
- likely review path.
### 5.7 Scenario classifications
- conventional review may be suitable;
- alternative-income review recommended;
- bank-statement evidence may strengthen the file;
- equity-based solution may be required;
- additional documentation required;
- human review required.
### 5.8 Primary CTA
**Get My Business Income Review**
### 5.9 CRM output
- borrower objective;
- tax-document income;
- bank-statement income;
- income gap;
- requested mortgage;
- estimated LTV;
- credit range;
- years in business;
- documentation readiness;
- likely lender pathway;
- missing documents;
- lead score;
- consent and attribution.
---
## 6. Calculator 2 — As-Is vs As-Complete Construction Value Calculator
### 6.1 Public-facing name
**Construction Financing Feasibility Calculator**
Alternative title:
**As-Is vs As-Complete Value Calculator**
### 6.2 User question
> Does the current property value, project budget, completed value, and borrower contribution support the requested construction financing?
### 6.3 Core outcome
The calculator evaluates:
- current equity;
- remaining project cost;
- requested financing;
- loan-to-cost;
- as-complete LTV;
- development margin;
- contingency;
- cost-overrun risk;
- value-decline risk;
- completion and exit strategy.
### 6.4 Required inputs
#### Property and land
- current property value;
- land purchase price;
- current appraised value;
- existing mortgage and registered debt;
- acquisition costs;
- work completed to date;
- property location and type.
#### Project budget
- hard costs;
- soft costs;
- architecture and engineering;
- permits and municipal fees;
- development charges;
- interest reserve;
- lender, broker, legal, appraisal, and inspection fees;
- marketing or sales costs;
- contingency percentage;
- sunk costs;
- borrower equity already invested.
#### Construction profile
- project type;
- square footage;
- number of units;
- cost per square foot;
- estimated rents;
- construction timeline;
- permit status;
- builder experience;
- fixed-price or cost-plus contract;
- pre-sales where applicable.
#### Financing request
- requested construction facility;
- debt to be refinanced;
- borrower cash contribution;
- land equity contribution;
- requested interest reserve;
- planned exit.
### 6.5 Core calculations
```plain text
Total project cost =
Land or current property basis
+ hard costs
+ soft costs
+ financing costs
+ contingency
```
```plain text
Net as-is equity =
As-is value
− existing mortgages
− other registered debt
```
```plain text
Required financing =
Remaining project costs
+ debt to be repaid
+ interest reserve
− borrower cash contribution
```
```plain text
Loan-to-cost =
Requested construction loan ÷ total project cost
```
```plain text
As-complete LTV =
Total debt at completion ÷ as-complete value
```
```plain text
Development margin =
As-complete value − total project cost
```
```plain text
Equity cushion =
As-complete value − total debt at completion
```
### 6.6 Stress tests
The calculator must test:
- base budget;
- 5%, 10%, and 15% cost overruns;
- base completed value;
- 5%, 10%, and 15% value declines;
- delayed completion;
- increased interest reserve;
- reduced borrower contribution.
### 6.7 Results
- as-is value;
- net current equity;
- total project cost;
- remaining cost to complete;
- requested facility;
- loan-to-cost;
- as-complete value;
- as-complete LTV;
- development margin;
- contingency adequacy;
- equity cushion;
- estimated exit requirement;
- stress-test results;
- missing documents;
- preliminary risk flags.
### 6.8 Scenario classifications
- strong preliminary feasibility;
- potentially financeable with adjustments;
- additional borrower equity may be required;
- budget or completed value requires validation;
- alternative or private construction review recommended;
- insufficient margin under current assumptions.
### 6.9 Primary CTA
**Request a Construction Financing Review**
### 6.10 CRM output
- as-is value;
- as-complete value;
- existing debt;
- project cost;
- requested facility;
- LTC;
- as-complete LTV;
- project margin;
- contingency;
- permit status;
- builder experience;
- exit strategy;
- stress-test result;
- missing documents;
- lead score.
---
## 7. Calculator 3 — Debt Refinance Savings Calculator
### 7.1 Public-facing name
**Should I Refinance My Debt Into My Mortgage?**
Alternative title:
**Debt Refinance Savings Calculator**
### 7.2 User question
> How much monthly pressure could refinancing reduce, and what would the longer-term cost be?
### 7.3 Core outcome
The calculator compares:
- current mortgage and debt payments;
- proposed consolidated mortgage payment;
- monthly cash-flow relief;
- annual cash-flow improvement;
- refinance costs;
- break-even period;
- total interest impact;
- equity used;
- accelerated repayment alternative.
### 7.4 Required inputs
#### Property and mortgage
- estimated property value;
- mortgage balance;
- current mortgage rate;
- remaining amortization and term;
- current payment;
- estimated prepayment penalty;
- property taxes and condo fees;
- HELOC or second mortgage;
- maturity date.
#### Debts to consolidate
For each debt:
- debt type;
- balance;
- interest rate;
- minimum payment;
- actual payment;
- remaining term where known.
Supported categories:
- credit cards;
- personal loans;
- unsecured lines of credit;
- vehicle loans;
- CRA debt;
- consumer-proposal payout;
- private or second mortgages;
- judgments or collections where financeable.
#### Proposed refinance
- proposed mortgage rate;
- proposed amortization;
- proposed mortgage amount;
- lender and broker fees;
- legal, appraisal, discharge, and registration fees;
- optional cash reserve.
### 7.5 Core calculations
```plain text
Current monthly debt burden =
Existing mortgage payment
+ all selected debt payments
```
```plain text
Debt consolidation amount =
Selected debt balances
+ mortgage penalty
+ refinance costs
```
```plain text
New mortgage amount =
Existing mortgage balance
+ consolidation amount
+ optional cash reserve
```
```plain text
New LTV =
New mortgage amount ÷ property value
```
```plain text
Monthly payment relief =
Current total monthly payments
− proposed mortgage payment
```
```plain text
Break-even months =
Total refinance costs ÷ monthly payment relief
```
### 7.6 Three scenarios
1. **Maximum monthly relief** — lowest required payment, with long-term cost warning.
2. **Balanced repayment** — improves cash flow while limiting amortization extension.
3. **Accelerated debt elimination** — borrower keeps paying near the former amount to reduce principal faster.
### 7.7 Stress tests
- proposed rate;
- proposed rate plus 1%;
- proposed rate plus 2%;
- 20-, 25-, and 30-year amortization where available;
- annual lump-sum payments;
- borrower continues previous total payment;
- borrower returns to minimum payment;
- new revolving debt is added after consolidation.
### 7.8 Results
- current total debt;
- current total monthly payments;
- weighted debt rate;
- proposed new mortgage;
- proposed payment;
- monthly and annual relief;
- new LTV;
- refinance costs;
- break-even period;
- estimated interest difference;
- equity used;
- accelerated payoff estimate;
- risk and suitability warnings.
### 7.9 Scenario classifications
- strong cash-flow improvement;
- potentially beneficial with accelerated repayment;
- refinance costs may outweigh the benefit;
- equity or qualification review required;
- alternative or private refinance review recommended.
### 7.10 Primary CTA
**Get My Debt Refinance Review**
### 7.11 CRM output
- property value;
- current mortgage;
- total selected debt;
- current monthly burden;
- proposed mortgage;
- new payment;
- monthly relief;
- break-even period;
- current and proposed LTV;
- weighted debt rate;
- proposed mortgage rate;
- credit range;
- borrower objective;
- urgency;
- likely lender path;
- missing documents;
- lead score.
---
## 8. Property valuation and available-equity report
### 8.1 Purpose
The property report is the easiest entry point because the visitor can begin with an address and mortgage balance rather than a full financial application.
### 8.2 Core calculations
```plain text
Gross equity =
Estimated property value − all registered secured debt
```
```plain text
Conservative refinance capacity =
Estimated property value × 65%
```
```plain text
Standard planning capacity =
Estimated property value × 75%
```
```plain text
Upper reference capacity =
Estimated property value × 80%
```
```plain text
Estimated accessible equity =
Selected refinance capacity
− current mortgage
− HELOC and other registered debt
− estimated refinance costs
```
The 75% LTV scenario is the default planning estimate. The 65% and 80% scenarios are shown as conservative and upper reference ranges. No scenario is presented as an approval.
### 8.3 Multiple-property analysis
For each property:
```plain text
Property available equity =
Property value × selected LTV
− secured debt
− estimated costs
```
```plain text
Combined portfolio equity =
Sum of available equity across selected properties
```
The report should explain that owning multiple properties does not automatically permit a higher LTV. The advantage is the ability to review combined equity, rental income, debt servicing, and possible cross-property strategies.
### 8.4 Report sections
1. estimated property-value range;
2. current secured debt;
3. gross equity;
4. accessible-equity range;
5. refinance scenarios at 65%, 75%, and 80%;
6. debt-consolidation opportunity;
7. monthly-payment comparison;
8. multiple-property summary;
9. likely financing pathways;
10. required documents;
11. recommended next step.
### 8.5 Primary CTA
**Get My Free Property Equity Report**
---
## 9. Website front-door placement
### 9.1 Homepage hero
The homepage should contain one primary front-door CTA:
**Get Your Free Property Equity Report**
Supporting copy:
> See what your property may be worth, how much equity may be available, and whether refinancing, alternative income review, or construction financing could improve your options.
Secondary CTA:
**Explore Mortgage Calculators**
The hero should not present three equally weighted choices before the visitor understands the offer. The property report is the default entry point and asks a short routing question after the initial property details.
### 9.2 Routing question
After the property step:
**What would you like to understand?**
- How much equity can I access?
- Can my business income help me qualify?
- Can my construction project be financed?
- Could refinancing lower my monthly debt payments?
### 9.3 Calculator hub
Recommended URL:
`/mortgage-calculators/`
Page sections:
- free property equity report;
- self-employed income calculator;
- construction feasibility calculator;
- debt refinance calculator;
- educational disclaimer;
- privacy and consent;
- contact option.
### 9.4 Contextual page placement
#### Self-employed pages
Place the self-employed calculator:
- above the first major CTA;
- after the income-document explanation;
- in the final CTA section;
- inside relevant articles about tax write-offs, bank statements, stated income, and incorporated borrowers.
Recommended embed CTA:
**Compare My Tax Income and Business Cash Flow**
#### Construction pages
Place the construction calculator:
- on the construction-financing pillar;
- laneway-house page;
- owner-builder page;
- progress-draw page;
- CMHC MLI Select and purpose-built rental content where appropriate.
Recommended embed CTA:
**Test My Project’s Preliminary Financing Feasibility**
#### Refinance and debt pages
Place the debt calculator:
- on debt-consolidation pages;
- refinance pages;
- CRA debt pages;
- renewal-declined pages;
- home-equity pages;
- private and second-mortgage pages.
Recommended embed CTA:
**Compare My Current Payments With a Refinance**
#### Local pages
Local pages should use the property equity report as the principal CTA, with localized copy rather than duplicating calculator logic.
### 9.5 Sticky and mobile placement
On mobile:
- sticky bottom CTA after the user scrolls beyond the hero;
- CTA text limited to one clear action;
- save-and-resume using email or secure link;
- avoid opening a long form in a modal;
- preserve progress between steps.
Recommended mobile CTA:
**Get My Free Equity Report**
---
## 10. User experience requirements
### 10.1 Form design
- progressive disclosure;
- one question group per screen;
- visible progress indicator;
- plain-language explanations;
- optional advanced fields;
- immediate validation;
- save-and-resume;
- accessible keyboard and mobile controls;
- no unnecessary account creation before results.
### 10.2 Result design
Each result should include:
- headline finding;
- assumptions used;
- current-versus-proposed comparison;
- range rather than false precision;
- positive factors;
- risk flags;
- missing documents;
- possible lender paths;
- clear next step;
- option to email or download the report.
### 10.3 Trust requirements
- explain how each estimate is calculated;
- show data-source date where applicable;
- disclose that valuation is not an appraisal;
- avoid approval language;
- explain fees and assumptions;
- identify when a human review is required;
- use secure handling for personal and financial data.
---
## 11. Lead capture and qualification
### 11.1 Progressive lead capture
The user should receive an initial result before being required to provide extensive personal details.
Recommended sequence:
1. property or scenario inputs;
2. preliminary range shown;
3. email requested to save and receive full report;
4. phone number optional until consultation request;
5. explicit consent for follow-up;
6. document upload offered only after the user chooses professional review.
### 11.2 Lead scoring
Lead score inputs:
- estimated equity;
- requested mortgage amount;
- LTV;
- urgency;
- mortgage maturity date;
- documentation readiness;
- borrower objective;
- credit range;
- income method;
- property type;
- construction feasibility;
- monthly payment pain;
- multi-property ownership;
- consent and engagement.
Suggested lead classes:
- report-only visitor;
- assessment lead;
- qualified consultation lead;
- advisor-ready opportunity;
- application-ready opportunity.
---
## 12. Atomic CRM integration
Every calculator submission should create or update:
- contact;
- property record;
- mortgage opportunity;
- calculator session;
- scenario summary;
- source page and campaign;
- consent record;
- recommended follow-up task.
The CRM should receive both raw inputs and normalized outputs so Dennis can review the reasoning without asking the borrower to repeat information.
Recommended automation:
```plain text
Calculator completed
    ↓
Lead classified
    ↓
Personalized report emailed
    ↓
Atomic CRM opportunity created
    ↓
High-intent lead alert
    ↓
Follow-up sequence by scenario
```
---
## 13. Analytics and measurement
Track:
- calculator starts;
- completion rate;
- drop-off by step;
- report-delivery rate;
- consultation requests;
- document-upload starts;
- qualified opportunities;
- applications;
- funded mortgages;
- revenue by calculator;
- source page and keyword;
- assisted conversions;
- mobile versus desktop completion;
- English versus future language versions.
Primary product KPIs:
- calculator completion rate;
- report-to-consultation conversion;
- consultation-to-application conversion;
- application-to-funded conversion;
- cost per qualified opportunity;
- funded volume influenced by calculators.
---
## 14. SEO requirements
Each calculator must have an indexable explanatory landing page containing:
- immediate answer;
- who the tool is for;
- methodology;
- inputs required;
- example scenario;
- limitations;
- FAQs;
- calculator interface;
- consultation CTA.
Recommended URLs:
- `/mortgage-calculators/`
- `/property-equity-report/`
- `/self-employed-mortgage-calculator/`
- `/construction-value-calculator/`
- `/debt-refinance-calculator/`
The calculator interface should not be the only indexable content. Server-render the explanatory content and key results framework for SEO and accessibility.
---
## 15. Compliance, privacy, and disclosures
Every tool must clearly state:
- results are educational estimates;
- results are not mortgage approval or a commitment to lend;
- property value is not a formal appraisal;
- lender guidelines vary;
- rates, fees, and qualification are subject to change;
- self-employed content is not tax or legal advice;
- construction values and budgets require professional validation;
- refinancing unsecured debt into a mortgage secures that debt against the home;
- longer amortization may reduce payments while increasing total interest;
- final advice requires a licensed mortgage review.
Sensitive data requirements:
- encryption in transit and at rest;
- minimum necessary data collection;
- explicit consent;
- retention rules;
- deletion request process;
- secure document upload;
- role-based access;
- audit log for report generation and CRM transfer.
---
## 16. Technical requirements
### 16.1 Front end
- Astro-compatible calculator pages;
- responsive multi-step forms;
- server-rendered explanatory content;
- client-side calculations for instant feedback where safe;
- server-side recalculation before report generation;
- accessible form labels and error messages;
- mobile-first performance.
### 16.2 Calculation service
- versioned formulas;
- configurable lender and planning assumptions;
- scenario engine;
- auditable input and output record;
- unit tests for every formula;
- no approval decision generated by the calculator;
- human-review override and notes.
### 16.3 Integrations
- Atomic CRM;
- email delivery;
- analytics;
- secure report storage;
- optional valuation-data provider;
- optional lender-policy rules layer;
- future connection to Mortgage CoPilot.
---
## 17. MVP scope
### Phase 1 — Front door and equity report
- homepage CTA;
- property and mortgage inputs;
- 65%, 75%, and 80% equity scenarios;
- single-property report;
- debt-calculator routing;
- Atomic CRM lead creation;
- email report;
- analytics.
### Phase 2 — Debt refinance calculator
- multiple debt entries;
- payment and interest comparison;
- three repayment scenarios;
- break-even calculation;
- refinance report;
- contextual placement across refinance content.
### Phase 3 — Self-employed calculator
- tax-document method;
- bank-statement method;
- configurable expense ratio;
- recognized-income comparison;
- documentation readiness;
- contextual placement across self-employed content.
### Phase 4 — Construction calculator
- as-is and as-complete analysis;
- LTC and LTV;
- budget and value stress tests;
- preliminary draw-planning support;
- contextual placement across construction content.
### Phase 5 — Portfolio and language expansion
- multiple-property analysis;
- cross-property strategy review;
- Cantonese and Mandarin content adaptations;
- deeper lender-policy integration;
- personalized Mortgage CoPilot recommendations.
---
## 18. Acceptance criteria
The PRD is implemented successfully when:
- the homepage has one clear property-equity front-door CTA;
- all three calculators have dedicated landing pages;
- each calculator generates a useful result before a full application;
- calculations are reproducible and unit tested;
- every result distinguishes estimate from approval;
- each completed report creates a structured Atomic CRM opportunity;
- high-intent leads are routed to Dennis promptly;
- result pages show assumptions, risks, and next steps;
- users can save, email, and download their report;
- all calculator events are tracked;
- contextual CTAs appear on relevant pillar, local, and supporting pages;
- privacy, consent, and disclosure requirements are met;
- mobile completion is practical without opening a full application form.
---
## 19. Success metrics
Initial 90-day targets should be treated as pilot benchmarks and validated with real traffic:
- 8% or higher homepage visitor-to-calculator start rate;
- 45% or higher calculator completion rate;
- 20% or higher completed-report-to-consultation rate;
- 30% or higher consultation-to-application rate for qualified leads;
- measurable funded-volume attribution by calculator;
- lower cost per qualified opportunity than generic contact-form leads;
- increased assisted conversions from SEO content.
---
## 20. Final strategic principle
> The calculators should not sell a mortgage before understanding the borrower. They should reveal the borrower’s income, equity, project, or payment problem clearly enough that the right financing conversation can begin with trust and useful evidence.
