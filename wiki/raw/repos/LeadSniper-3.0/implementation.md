# Contact Intelligence Expansion - Implementation Guide

## Goal

Expand the Contact Intelligence UI to display comprehensive enrichment data with enhanced **email scraping** and **decision maker discovery** in a new modal window.

---

## Implementation Tasks

### 1. Create Contact Intelligence Modal

**File**: [`components/ContactIntelligenceModal.tsx`](file:///g:/AI%20-%20Coding%20Projects/LeadSniper/LeadSniper-3.0/components/ContactIntelligenceModal.tsx) (NEW)

Create a reusable modal component to display enrichment data in organized sections:

#### Modal Sections

- **Executive Summary**: Company description and key stats
- **Qualification Signals** (if available):
  - Client Sentiment Score (from multi-source reviews: Google, Yelp, etc.)
  - Growth Signals (expansion mentions, new locations, increased review velocity)
  - Hiring Signals (job postings, staffing needs from reviews)
  - Operational Friction (callback issues, response gaps from review analysis)
  - Owner Engagement Score (review responses, profile updates)
- **Decision Makers**: List of key people (CEO, Founder) with LinkedIn/Email
- **Hiring Intelligence**: Recent job postings and roles
- **News Room**: Recent articles and sentiment analysis
- **Competitive Landscape**: List of competitors and advantages
- **Tech Stack**: Detected technologies
- **Enhanced Contact Graph**: Display discovered emails/phones with:
  - Email confidence scores (High/Medium/Low)
  - Verification status badges (Validated/Found/Inferred)
  - Generic vs. specific email indicators

---

### 2. Enhance Email Scraping Service

**File**: [`services/contactIntelligenceService.ts`](file:///g:/AI%20-%20Coding%20Projects/LeadSniper/LeadSniper-3.0/services/contactIntelligenceService.ts) (MODIFY)

#### Update `scrapeWebsiteForContacts` Function

- Scrape multiple pages (not just homepage):
  - `/contact`
  - `/about`
  - `/team`
- Extract emails from all pages and deduplicate
- Add email validation (format checking, disposable email detection)

#### Add Email Confidence Scoring

- Score emails based on where found:
  - **High**: Contact page, Team page
  - **Medium**: Footer, About page
  - **Low**: Homepage only
- Flag email types:
  - **Generic**: `info@`, `contact@`, `support@`
  - **Specific**: `firstname@`, `firstname.lastname@`
- Add verification status:
  - `found` - Scraped from website
  - `inferred` - Generated variant
  - `validated` - Externally verified

---

### 3. Update AuditPanel Component

**File**: [`components/AuditPanel.tsx`](file:///g:/AI%20-%20Coding%20Projects/LeadSniper/LeadSniper-3.0/components/AuditPanel.tsx) (MODIFY)

#### Changes Required

1. Import `enrichContactIntelligenceFull` from `contactIntelligenceService`
2. Update `handleEnrich` function:
   - Call `enrichContactIntelligenceFull` instead of basic enrichment
   - Store full intelligence in lead state
3. Add state management:
   - `showIntelModal` (boolean) - controls modal visibility
4. Add UI elements:
   - "View Intelligence Report" button in Contact Intelligence card
   - Opens modal when clicked
   - Pass enriched lead data to modal

---

### 4. Update CSV Export

**File**: [`services/leadLogic.ts`](file:///g:/AI%20-%20Coding%20Projects/LeadSniper/LeadSniper-3.0/services/leadLogic.ts) (MODIFY)

#### Update `exportLeadsToCsv` Function

Add new columns to CSV export:

| Column Name         | Data Source                                     | Example                                |
| ------------------- | ----------------------------------------------- | -------------------------------------- |
| `Enrichment Score`  | `lead.contactIntelligence.enrichmentScore`      | `85`                                   |
| `Discovered Emails` | `lead.contactIntelligence.additionalEmails`     | `john@company.com, info@company.com`   |
| `Decision Maker`    | `lead.decisionMaker.fullName` + `jobTitle`      | `John Smith - CEO`                     |
| `Decision Maker Email` | `lead.decisionMaker.email`                   | `john@company.com`                     |
| `Email Status`      | `lead.decisionMaker.emailStatus`                | `verified/catch_all/unverified`        |
| `Social Profiles`   | `lead.socials.linkedin`, `lead.socials.facebook`| LinkedIn, Facebook URLs                |

---

## Verification Plan

### Manual Testing Steps

1. **Open a lead** in the Dashboard
2. **Click "Deep Search"** (or "Find Socials" button)
3. **Wait for enrichment** processing
4. **Verify enrichment data** appears in Contact Intelligence card
5. **Click "View Intelligence Report"** button
6. **Verify modal opens** and displays:
   - Qualification signals
   - Decision maker info with verified email
   - Enhanced email list with confidence scores
7. **Export CSV**
8. **Verify new columns** appear with enrichment data

### Expected Behavior

- Modal displays comprehensive enrichment data
- Emails show confidence badges (High/Medium/Low)
- Verification status visible (Validated/Found/Inferred)
- CSV export includes all new enrichment columns
- Decision maker email prominently displayed when found

---

## Technical Notes

### Type Definitions

Ensure `types.ts` includes:

```typescript
interface ContactIntelligenceResult {
  additionalEmails: Array<{
    email: string;
    confidence: "high" | "medium" | "low";
    status: "validated" | "found" | "inferred";
    isGeneric: boolean;
  }>;
  decisionMaker?: {
    fullName: string;
    email?: string;
    emailStatus: 'verified' | 'catch_all' | 'unverified' | 'invalid';
    jobTitle?: string;
    linkedinUrl?: string;
    confidence: 'high' | 'medium' | 'low';
  };
  // ... existing fields
}
```

### Decision Maker Discovery

- Uses Apify actors for lead enrichment
- Two provider options available:
  - **Local Business Search**: Best for service businesses (plumbers, dentists, etc.)
  - **B2B Lead Finder**: Best for professional services, tech companies
- Email verification built into enrichment flow

---

## Status

- **Planning**: ✅ Complete
- **Implementation**: ⏳ Pending
- **Testing**: ⏳ Pending
- **Deployment**: ⏳ Pending

---

## Next Session Checklist

- [ ] Create `ContactIntelligenceModal.tsx` component
- [ ] Enhance email scraping in `contactIntelligenceService.ts`
- [ ] Update `AuditPanel.tsx` to use modal
- [ ] Add new CSV columns in `leadLogic.ts`
- [ ] Test enrichment flow end-to-end
- [ ] Verify CSV export includes new data
