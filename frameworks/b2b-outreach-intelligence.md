# B2B Outreach Infrastructure & Intelligence Framework

## Overview
This framework defines the integration of delivery infrastructure, high-quality lead data, and AI-driven signal analysis to execute high-conversion B2B outbound campaigns, specifically tailored for the IDC Group Benefits vertical.

## 1. The Infrastructure Layer (The Plumbing)
**Provider:** InboxKit (`www.inboxkit.com`)
**Goal:** Maximum deliverability, zero domain burning.

### Setup Specification
- **Mailbox Diversification:** Utilize a mix of Google Workspace, Microsoft 365, and Azure mailboxes to distribute risk.
- **Domain Strategy:** Use "lookalike" domains (e.g., `idc-connect.com`) rather than the primary corporate domain.
- **Deliverability Guardrails:**
    - Use **InfraGuard** for blacklist and DNS monitoring.
    - Implement **Inbox Placement Tests** to verify "Primary" tab landing.
    - Programmatic scaling via API to spin up/down mailboxes based on campaign volume.

## 2. The Data Layer (The Source)
**Primary Source:** Scott's Directories & Explorium AI
**Model:** This layer is provided as a **paid service** to the client, covering the cost of data acquisition and enrichment.

**Process:**
- **Ingestion:** Load high-fidelity B2B lists from Scott's Directories.
- **Enrichment (Explorium):** 
    - **Match:** Map entries to unique `business_id`s.
    - **Filter:** Apply granular firmagraphics (Company size, Revenue, Growth) to ensure ICP alignment.
    - **Verify:** Cross-reference and secure verified contact details.
- **Pre-Flight Verification:** Final validation via InboxKit Email Verifier API to eliminate bounces.

## 3. The Intelligence Layer (The Signal Sweep)
Before dispatch, every domain undergoes a "Signal Sweep" to identify specific business pain points.

### A. Growth & Headcount Signals
- **Hiring Velocity:** Analyze active job postings $\rightarrow$ Signal: "War for Talent" $\rightarrow$ Angle: Benefits as a recruitment magnet.
- **Growth Spikes:** Search for headcount increases $\rightarrow$ Signal: Strained existing plans $\rightarrow$ Angle: Scaling benefit infrastructure.
- **M&A Activity:** Identify recent acquisitions $\rightarrow$ Signal: Plan reconciliation nightmare $\rightarrow$ Angle: Consolidation and optimization.

### B. Firmagraphics & Vertical Analysis
- **Industry Mapping:** Segment by vertical (e.g., Manufacturing vs. Tech).
- **Vertical Pain Points:** Align benefit offerings to industry-specific stressors (e.g., safety/disability for blue-collar, mental health/flexibility for white-collar).

### C. Sentiment & Review Analysis
- **Gap Detection:** Scrape Glassdoor, Indeed, and Reddit for domain-specific mentions of "benefits," "insurance," or "health care."
- **The "Complaint" Trigger:** Identify specific dissatisfaction (e.g., "dental is poor") to use as a direct hook in the outreach.

## 4. Execution Workflow (Hermes Orchestration)
1. **Ingest:** Load lead from Scott's Directories.
2. **Analyze:** Run the Signal Sweep $\rightarrow$ Generate **Signal Card**.
3. **Draft:** Generate a hyper-personalized email based on the detected signal (not a template).
4. **Route:** Assign to a healthy, warmed-up InboxKit mailbox.
5. **Dispatch:** Send and monitor for engagement/replies.
6. **Sustain:** Monitor domain health via webhooks; auto-rotate domains if reputation dips.
