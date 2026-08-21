# Google Maps Grounding Test Guide

## Quick Start

### 1. Set Your API Key

Edit `.env.local` and add your Gemini API key:

```bash
GEMINI_API_KEY=AIza...your_actual_key_here
```

Get your key from: https://aistudio.google.com/app/apikey

### 2. Run the Test

```bash
cd LeadSniper-3.0
npx tsx test-grounding.ts
```

## Expected Output

### Geocoding Phase
```
🗺️ Google Maps Grounding enabled for Austin, TX at (30.2672, -97.7431)
```

This confirms that:
- ✅ City was successfully geocoded
- ✅ Coordinates are being passed to the Google Maps tool
- ✅ Location grounding is active

### Lead Results with Grounding

```
📌 Lead #1: ABC Plumbing Service
   Rating: 4.5 ⭐ (127 reviews)
   City: Austin, TX
   Website: https://abcplumbing.com
   Phone: (512) 555-0123
   Bucket: The Hidden Gem
   Owner: John Smith
   Unique Angle: Family owned since 1990

   🗺️  GROUNDING METADATA:
      📍 Coordinates: 30.2672, -97.7431
      🔗 Maps URI: https://maps.google.com/?cid=12345...
      🏷️  Place ID: ChIJ...abc123
   ───────────────────────────────────────────────────────────
```

### Summary Statistics

```
📊 Summary Statistics:
   Total Leads: 15
   Leads with Grounding Metadata: 15 (100.0%)
   Leads with Coordinates: 15 (100.0%)
   Leads with Maps URI: 12 (80.0%)
   Average Rating: 4.3 ⭐
```

## What This Tests

### ✅ Geocoding Service
- Converts "Austin, TX" → coordinates (30.2672, -97.7431)
- Uses caching to avoid redundant API calls
- Handles errors gracefully

### ✅ Google Maps Grounding
- Passes coordinates via `toolConfig.retrievalConfig.latLng`
- Enables location-aware business searches
- Returns more accurate, localized results

### ✅ Metadata Extraction
- Captures place IDs from Google Maps
- Stores map URIs for direct linking
- Preserves coordinates for each lead

### ✅ Integration Points
All three main functions are tested:
1. `searchBusinesses()` - Initial search
2. `enrichSingleLead()` - Individual lead enrichment
3. `enrichLeadsFromContacts()` - Reverse lookup

## Customizing the Test

Edit `test-grounding.ts` to test different scenarios:

```typescript
// Change search parameters
const niche = 'dentist';  // Try: dentist, lawyer, restaurant
const city = 'San Francisco, CA';  // Any city
const focus = 'crisis';  // Options: any, crisis, growth, reactivation
```

## Troubleshooting

### Error: "GEMINI_API_KEY not configured"
- Check that `.env.local` exists
- Verify the API key is not the placeholder value
- Ensure no spaces around the `=` sign

### Error: "Failed to geocode city"
- City name must be specific (e.g., "Austin, TX" not just "Austin")
- Check internet connectivity
- Verify API key has Google Maps tool access enabled

### No grounding metadata in results
- This is normal for some API responses
- Coordinates will still be stored even if Maps URI is missing
- Try running the test multiple times

## Next Steps

Once testing is successful, you can:

1. **Display Maps Links**: Use `groundingMetadata.mapsUri` in UI
2. **Show Coordinates**: Display location pins on a map
3. **Filter by Distance**: Calculate distances using coordinates
4. **Geo-Analytics**: Analyze lead distribution by location

## Benefits Confirmed

After successful testing, you'll have confirmed:

- ✅ More accurate location-based searches
- ✅ Richer metadata for each business
- ✅ Better data quality with coordinates
- ✅ Future-ready for map visualizations
- ✅ Performance optimized with caching
