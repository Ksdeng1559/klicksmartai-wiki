# IDC Recruitment A/B Tracking Sheet Specification

**Date:** May 6, 2026  
**Status:** HITL DRAFT — Awaiting Owner Approval  
**Project:** IDC Recruitment Agent (HUBERT-X)  
**Purpose:** Google Sheet to track every lead through the HUBERT-X pipeline: Lead → VP Assignment → Contact → Response → Meeting → Signed

---

## Sheet Structure

### Tab 1: `Pipeline`

| Column | Header | Type | Description |
|:---|:---|:---|:---|
| A | Lead ID | Text | Unique identifier (e.g., L001, L002) |
| B | Lead Name | Text | Full name |
| C | Current Firm | Text | Current employer/carrier |
| D | Designations | Text | CLU, CFP, ChFC, etc. |
| E | Est. GDC/Revenue | Currency | Estimated annual production |
| F | Pedigree Score | Dropdown | Tier 1 (Elite) / Tier 2 (Growth) / Tier 3 (Junior) |
| G | Sovereign Gap | Text | Specific observed gap at current firm |
| H | Assigned VP | Dropdown | VP-A (Infrastructure) / VP-B (Client Value) / VP-C (Economics) |
| I | Date Contacted | Date | First outreach date |
| J | Channel | Dropdown | LinkedIn / Email / Phone / Referral |
| K | Response? | Dropdown | Yes / No / Pending |
| L | Response Date | Date | Date of first response |
| M | Response Sentiment | Dropdown | Positive / Neutral / Negative / "Not Interested" |
| N | Meeting Booked? | Dropdown | Yes / No |
| O | Meeting Date | Date | Date of meeting |
| P | Meeting Outcome | Dropdown | Advancing / Not a Fit / Reschedule / Signed |
| Q | Advisor Signed? | Dropdown | Yes / No |
| R | Sign Date | Date | Contract signed date |
| S | Notes | Text | Freeform notes, conversation highlights |
| T | VP Success | Formula | Auto-calculated: If Q="Yes" then 1 else 0 |

---

### Tab 2: `VP Performance`

**Auto-populated from Pipeline data (via formulas or Apps Script)**

| Column | Header | Description |
|:---|:---|:---|
| A | VP | VP-A / VP-B / VP-C |
| B | Leads Assigned | COUNT of leads assigned to this VP |
| C | Responses | COUNT with Response = "Yes" |
| D | Response Rate | B / C as percentage |
| E | Meetings Booked | COUNT with Meeting Booked = "Yes" |
| F | Meeting Rate | E / C as percentage (of responses) |
| G | Advisors Signed | COUNT with Advisor Signed = "Yes" |
| H | Sign Rate | G / E as percentage (of meetings) |
| I | Overall Conversion | G / B as percentage (end-to-end) |
| J | Best Performing | Conditional formatting: green for highest overall conversion |

---

### Tab 3: `Batch Log`

| Column | Header | Description |
|:---|:---|:---|
| A | Batch # | B001, B002, etc. |
| B | Date Started | Date batch launched |
| C | Leads in Batch | Number of leads |
| D | VP-A Count | Leads assigned VP-A |
| E | VP-B Count | Leads assigned VP-B |
| F | VP-C Count | Leads assigned VP-C |
| G | Batch Responses | Total responses received |
| H | Batch Response Rate | % |
| I | Batch Meetings | Total meetings booked |
| J | Batch Signs | Total advisors signed |
| K | Key Learning | Qualitative insight from this batch |

---

## Automation Notes

1. **VP Assignment:** Can be initially manual; eventually driven by the Strategist agent.
2. **Response Tracking:** The Diplomat agent logs response sentiment.
3. **VP Performance:** Use Google Sheets formulas (`COUNTIFS`, `ARRAYFORMULA`) for auto-calculation, or an Apps Script for the dashboard.
4. **Weekly Report:** The Scientist agent scrapes this sheet every Monday to produce the Weekly Optimization Report.

---

## Google Sheet ID (to be created)

**Owner:** Dennis at KlickSmartAI  
**Folder:** IDC Recruitment / HUBERT-X  
**Initial State:** Empty `Pipeline` tab with headers; `VP Performance` and `Batch Log` tabs with headers.

---

## Next Steps

1. Approve this specification
2. Create the Google Sheet in the IDC project folder
3. Populate Tab 1 headers and Tab 2 formulas
4. Ingest Batch 1 (10 leads) from LinkedIn/Indeed/Explorium
5. Begin POC: Hunter → Strategist → Diplomat flow
