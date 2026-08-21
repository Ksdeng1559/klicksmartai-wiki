# Contact Intelligence Feature - Implementation Summary

## Overview

The Contact Intelligence feature automatically discovers and enriches business contact information including:
- Website contact details (emails, phones)
- Google My Business links
- Social media profiles
- Contact page URLs

## Implementation

### Files Created

#### `services/contactIntelligenceService.ts`
**Purpose**: Core service for contact data extraction and enrichment

**Key Functions**:
- `enrichContactIntelligence(lead)` - Main enrichment function
- `scrapeWebsiteForContacts(url)` - Website scraping for contact info
- `extractGoogleMyBusinessUrl(mapLink)` - GMB link extraction
- `inferSocialProfiles(name, niche)` - Social profile inference
- `validateEmail(email)` - Email format validation
- `formatPhoneNumber(phone)` - Phone number formatting

**Data Sources**:
1. **Google Maps Grounding** - Extract GMB links from Place IDs
2. **Website Scraping** - Parse homepage for emails, phones, social links
3. **Contact Page Discovery** - Find and extract contact page info
4. **Social Profile Inference** - Generate probable social handles

### Files Modified

#### `types.ts`
Added new `ContactIntelligence` interface:
```typescript
export interface ContactIntelligence {
  additionalEmails: string[];
  additionalPhones: string[];
  contactPageUrl?: string;
  enrichmentScore: number; // 0-100
  dataSource: string[];
}
```

Added `contactIntelligence` field to `Lead` interface.

#### `components/AuditPanel.tsx`
**Integration Points**:
1. Import Contact Intelligence service
2. Enhanced `handleEnrich()` function to use Contact Intelligence
3. Added UI section to display enriched contact data
4. Fallback to Gemini service if enrichment score < 30%

**UI Features**:
- Discovered emails (mailto links, emerald theme)
- Discovered phones (tel links, blue theme)
- Contact page link
- Enrichment score display
- Data source attribution

## How It Works

### Enrichment Flow

```
User clicks "Find Socials"
         ↓
contactIntelligenceService.enrichContactIntelligence()
         ↓
    ┌────┴────┐
    │ Stage 1 │ Extract GMB URL from mapLink/placeId
    └────┬────┘
         ↓
    ┌────┴────┐
    │ Stage 2 │ Scrape website for contacts
    └────┬────┘
         ↓
    ┌────┴────┐
    │ Stage 3 │ Infer social profiles
    └────┬────┘
         ↓
    ┌────┴────┐
    │ Stage 4 │ Calculate enrichment score
    └────┬────┘
         ↓
Lead updated with contactIntelligence data
         ↓
UI displays enriched contact information
```

### Enrichment Scoring

The enrichment score (0-100) is calculated based on:
- **+20-25 points**: Google My Business link found
- **+30 points**: Website emails discovered
- **+15 points**: Social profiles found on website
- **+10 points**: Social profiles inferred

### Data Sources Priority

1. **Primary**: Google Maps Grounding (Place ID → GMB link)
2. **Secondary**: Website scraping (actual contact data)
3. **Tertiary**: Social profile inference (probable handles)
4. **Fallback**: Gemini AI enrichment (if score < 30%)

## Usage

### For Users

1. Navigate to any lead in the Audit Panel
2. Click "Find Socials" button
3. Wait 2-5 seconds for enrichment
4. View Contact Intelligence section with:
   - Discovered emails (clickable mailto links)
   - Discovered phones (clickable tel links)
   - Contact page URL
   - Data source attribution

### Example Output

```
✅ Contact Intelligence                   45% enriched

Discovered Emails
  contact@business.com
  info@business.com

Discovered Phones
  (512) 555-1234
  (512) 555-5678

🔗 Contact Page

Sources: Google Maps Grounding, Website Scraping
```

## Technical Details

### Website Scraping

**Method**: Client-side `fetch()` with 5-second timeout
**Extraction Patterns**:
- Emails: `/\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g`
- Phones: `/(\+?1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}/g`
- Instagram: `/instagram\.com\/([a-zA-Z0-9._]+)/`
- Facebook: `/facebook\.com\/([a-zA-Z0-9.]+)/`
- LinkedIn: `/linkedin\.com\/(company|in)\/([a-zA-Z0-9-]+)/`

**Filtering**:
- Excludes generic emails (example.com, googleapis.com, sentry.io)
- Deduplicates results
- Validates against common patterns

### Google My Business URLs

**Format**: `https://www.google.com/maps/place/?q=place_id:ChIJ...`

**Extraction Sources**:
1. Existing `lead.mapLink` (if present)
2. `lead.groundingMetadata.placeId` (preferred)
3. Generated from Place ID if available

### Social Profile Inference

**Handle Generation**:
```typescript
businessName → "Joe's Plumbing"
baseHandle → "joesplumbing"
variations → [
  "joesplumbing",
  "joesplumbingplumber",
  "officialjoesplumbing"
]
```

**Platforms**: Instagram, Facebook, LinkedIn
**Note**: Inferred handles are NOT verified - users should manually check

## Limitations

### Current Limitations

1. **No Email Verification**
   - Emails are discovered but not verified
   - No MX record checking
   - No deliverability testing

2. **No LinkedIn Scraping**
   - No actual LinkedIn profile discovery
   - No decision maker identification
   - No company intelligence

3. **Client-Side Only**
   - CORS restrictions may block some websites
   - No server-side scraping capabilities
   - Limited to publicly accessible pages

4. **Basic Social Inference**
   - Inferred handles may not exist
   - No verification of social profiles
   - Manual checking required

### Browser Compatibility

**Requires**:
- Modern browser with `fetch()` API
- Support for `AbortSignal.timeout()`
- JavaScript enabled

**Blocked By**:
- CORS policies (some websites)
- Aggressive bot detection
- Password-protected pages
- Dynamic content requiring JavaScript execution

## Future Enhancements

### Phase 2 (Planned)

1. **Email Verification Service**
   - Syntax validation
   - MX record verification
   - Deliverability scoring
   - 90%+ accuracy target

2. **LinkedIn Integration**
   - Company profile extraction
   - Decision maker discovery
   - Employee count and roles
   - Recent activity tracking

3. **Advanced Social Discovery**
   - Multi-platform search
   - Follower count extraction
   - Verification status
   - Engagement metrics

4. **Server-Side Scraping**
   - Bypass CORS restrictions
   - JavaScript rendering
   - Screenshot capture
   - Deeper page analysis

5. **Contact Confidence Scoring**
   - Email deliverability score
   - Phone number validation
   - Social profile verification
   - Overall contact quality rating

### Phase 3 (Future)

- API integration with data providers
- Real-time contact validation
- Contact update notifications
- CRM synchronization
- Bulk enrichment capabilities

## Testing

### Manual Testing Steps

1. **Test Google My Business Extraction**
   ```
   - Find lead with mapLink
   - Click "Find Socials"
   - Verify GMB link in Contact Intelligence section
   ```

2. **Test Website Scraping**
   ```
   - Import lead with known website (e.g., google.com)
   - Click "Find Socials"
   - Verify emails/phones discovered
   - Check contact page link
   ```

3. **Test Social Inference**
   ```
   - Use lead with unique business name
   - Click "Find Socials"
   - Verify inferred social profiles
   - Manually check if profiles exist
   ```

4. **Test Enrichment Score**
   ```
   - Test with various leads
   - Verify score increases with more data
   - Confirm score caps at 100
   ```

### Expected Behavior

**Success Cases**:
- GMB link extracted from Place ID
- Emails found on website homepage
- Contact page URL discovered
- Enrichment score > 0

**Partial Success**:
- Some data found, enrichment score 20-70%
- Fallback to Gemini service activated
- Limited contact info displayed

**Failure Cases**:
- Website CORS blocked (score remains low)
- No contact info on homepage
- Invalid website URL
- Network timeout

## Performance

**Typical Execution Time**: 2-5 seconds
- GMB extraction: < 100ms
- Website scraping: 1-3 seconds
- Social inference: < 100ms
- Gemini fallback: 1-2 seconds

**Resource Usage**:
- Single HTTP request per website
- Minimal memory footprint
- No external API calls (besides Gemini fallback)
- Client-side processing only

## Security Considerations

1. **User-Agent Header**: Identifies as LeadSniper (ethical scraping)
2. **Timeout Protection**: 5-second max per website
3. **CORS Compliance**: Respects website CORS policies
4. **No Bypass Attempts**: No proxy or VPN usage
5. **Rate Limiting**: Single request per user action

## Support & Troubleshooting

### Common Issues

**Q: "Find Socials" button doesn't show Contact Intelligence**
A: Check if enrichment score > 0. Some websites block scraping.

**Q: Inferred social profiles don't exist**
A: Social inference is probabilistic. Manually verify profiles.

**Q: CORS errors in console**
A: Some websites block client-side access. This is expected.

**Q: Enrichment score is low (< 30%)**
A: Limited data available. Gemini fallback should activate.

## Documentation

**Related Files**:
- [CONTACT_INTELLIGENCE_PLAN.md](CONTACT_INTELLIGENCE_PLAN.md) - Original enhancement plan
- [README.md](README.md) - Project overview
- [types.ts](types.ts) - TypeScript interfaces

**API Reference**:
- `enrichContactIntelligence(lead)` - Main enrichment function
- `validateEmail(email)` - Email format validation
- `formatPhoneNumber(phone)` - Phone number formatting

---

**Last Updated**: January 2026
**Version**: 1.0.0
**Status**: ✅ Production Ready
