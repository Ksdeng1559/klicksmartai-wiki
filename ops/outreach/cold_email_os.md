# Cold Email Outreach OS: SOP & Agent Specification

## 🎯 Goal
Establish a high-scale, high-deliverability outbound engine that leverages AI agents to automate the "Factory" (infrastructure) and the "Machine" (execution). The system supports two primary modes: **Mass B2B Scaling** (Volume/ROI) and **HNWI Strategic Engagement** (Quality/Trust).

## 🏗️ Phase 1: The Factory (Infrastructure SOP)
*Goal: Reach the inbox without burning domains.*

### 1. Domain & Account Architecture
- **Root Domain:** Keep `klicksmartai.com` for business use only.
- **Burner Domains:** Purchase 20-50 secondary domains (e.g., `get[brand].ai`, `[brand]labs.io`).
- **Scaling:** 2-3 inboxes per domain.
- **Provider:** Premium Google Workspace or Microsoft 365 resellers only.

### 2. Technical Setup Checklist
- [ ] **DNS Configuration:** SPF, DKIM, and DMARC configured for every domain.
- [ ] **Forwarding:** All burner domains redirect to the root domain.
- [ ] **Warm-up:** 14-21 day mandatory warm-up period via Smartlead.
- [ ] **Health Ratio:** Maintain 1:1 ratio of cold emails to warm-up emails.

### 3. Deliverability Guardrails
- **Format:** Plain text only. No HTML, images, or links in initial touch.
- **Spintax:** Use randomized greetings and sign-offs.
- **Bounce Rate:** Strictly $<3\%$ using a verification tool (Million Verifier/Lead Magic).
- **Burn Threshold:** If reply rates drop below 0.65%, nuke the domain and replace.

---

## ✍️ Phase 2: The Machine (Creative & Execution SOP)
*Goal: High-conversion, low-friction engagement.*

### Variant A: Mass B2B Scaling (The Volume Play)
*Focus: Efficiency, ROI, and Pattern Interruption.*

**1. The 5-Block Copywriting Framework**
Every email must be $\le 55$ words and written at a 3rd-5th grade level.
1. **Relevance Line:** Specific "Why now" hook.
2. **Pain Point:** Poke the bear (optional).
3. **Offer Statement:** Novelty + Ease + Safety + Opportunity.
4. **Social Proof:** Tangible numbers/case studies.
5. **Low-Friction CTA:** "Open to learning more?" (No calendar links).
6. **P.S. Opt-Out:** Polite exit.

**2. The Outreach Sequence**
- **Touch 1:** Cold Email (The 5-Block approach).
- **Touch 2:** Follow-up (48 hours later).
- **Omnichannel Bump:** LinkedIn connection request immediately after Touch 1.

### Variant B: HNWI Strategic Engagement (The Trust Play)
*Focus: Discretion, Wealth Signals, and Exclusivity for Financial Planning.*

**1. The "Recent Trigger" Framework**
Anchor communications to a liquidity event (Funding, Acquisition, C-Suite promotion, or luxury asset purchase).
- **Tone:** Sophisticated, concise, professional, and non-transactional.
- **Vocabulary:** Use "Legacy," "Tax Optimization," and "Family Governance" instead of "Retirement Planning" or "Budgeting."

**2. High-Trust Acquisition Tactics**
- **Wealth Radar:** Monitor corporate ownership changes, Series A/B rounds, and company exits to time the reach-out.
- **COI Brokerage:** Prioritize "warm" introductions via Centers of Influence (Private Bankers, Trust Attorneys, Tax Advisors).
- **Gated Value:** Lead with bespoke research or an exclusive insight (e.g., private market reports or a custom tax-efficiency guide).
- **Social Selling:** Profile optimization $\rightarrow$ Strategic engagement with their content $\rightarrow$ Low-pressure reach-out.

**3. Response Protocol**
- **Speed:** Reply to positive leads in $<5$ minutes.
- **Booking:** Avoid calendar links. Suggest two specific times (e.g., "Tuesday at 2 PM or Wed at 10 AM") to minimize friction.
- **Discretion:** Use secure, professional communication channels; avoid aggressive follow-up cadences.

---

## 📹 Phase 3: Multi-Channel Expansion (Video & Social)
*Goal: Move from "Text" to "Trust" using visual and social signals.*

### 1. Video Outreach (The Trust Accelerator)
- **Universal VSL:** Record a generic high-quality video (under 90s) focusing on authenticity.
- **Dynamic Personalization:** Use tools (Loom/Pitchlane) to overlay the prospect's website or LinkedIn profile.
- **The GIF Hook:** Use an animated GIF of the video in the email to spike CTR.
- **Tactic:** Send the video as a "Taster" of the value you provide.

### 2. LinkedIn Strategic Integration
- **The Bump:** "Just sent you an email regarding [Trigger Event]" $\rightarrow$ Puts a face to the name.
- **Bespoke Engagement:** Interact with the prospect's content *before* the first email to move from "Cold" to "Luke-warm."

---

## 🤖 Phase 4: Agent Specification (The "Outbound Agent")
*Goal: Automate the manual steps of the SOP.*

### 1. Agent Capabilities (Required Toolsets)
- **Lead Harvesting:** Integrate with Clay/Apollo to scrape and segment ICPs.
- **Wealth Radar:** Monitor corporate filings/news for HNWI liquidity events.
- **Identity Intelligence:** Use LLMs to find specific "Relevance" hooks from LinkedIn/News.
- **Copy Generation:** Apply 5-Block (B2B) or Trigger-based (HNWI) frameworks using NotebookLM.
- **Quality Control:** Audit bounce rates and reply rates; alert owner when a domain is "burnt."
- **Inbox Management:** Monitor Unified Inbox $\rightarrow$ Identify "Positive" vs "Negative" $\rightarrow$ Draft responses for review.

### 2. Agent Logic Flow
`Lead Scrape` $\rightarrow$ `Personalization Research` $\rightarrow$ `Copywriting` $\rightarrow$ `Verification` $\rightarrow$ `Smartlead Queue` $\rightarrow$ `Response Monitoring`.

### 3. Success Metrics (KPIs)
- **Open Rate:** $\sim 30\%$.
- **Positive Reply Rate:** $1.5\% - 2\%$.
- **Bounce Rate:** $<3\%$.
- **Meeting Rate:** 5-10/week.
