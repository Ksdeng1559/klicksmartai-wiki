# LeadSniper 3.0 - Quick Deploy Guide

## 🚀 Ready to Deploy in 3 Steps

---

## Step 1: Get Your Gemini API Key (2 minutes)

1. Visit: https://aistudio.google.com/app/apikey
2. Sign in with Google
3. Click "Create API Key"
4. Copy the key

---

## Step 2: Choose Your Deployment Method

### Option A: Vercel (Easiest - 5 minutes)

**One-Click Deploy:**
1. Click: [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Deng1559/LeadSniper-3.0)
2. Connect your GitHub account
3. Add environment variable:
   - Name: `GEMINI_API_KEY`
   - Value: `your_api_key_from_step_1`
4. Click "Deploy"
5. Done! Your app will be live at: `https://your-project.vercel.app`

**Custom Domain (Optional):**
- Settings → Domains → Add your domain

---

### Option B: Netlify (Alternative - 5 minutes)

1. Click: [![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start)
2. Connect GitHub
3. Site settings → Environment variables
4. Add: `GEMINI_API_KEY` = your key
5. Deploy!

---

### Option C: Docker (Self-Hosted - 10 minutes)

```bash
# Clone and enter directory
cd LeadSniper-3.0

# Create .env.production
echo "GEMINI_API_KEY=your_key_here" > .env.production

# Build and run
docker-compose up -d

# Access at http://localhost:8080
```

---

## Step 3: Test Your Deployment

1. Open your deployed URL
2. Go to "Setup / Import" tab
3. Set Niche: `Plumber`
4. Set City: `Austin, TX`
5. Click "Find Leads"
6. If you see leads appear → ✅ SUCCESS!

---

## What You Get Out of the Box

✅ **Lead Generation:** Search local businesses by niche and location
✅ **AI Enrichment:** Auto-fill contact data, social media, owner names
✅ **SEO Audits:** Keyword opportunities and competitor analysis
✅ **Email Generator:** Personalized cold email creation
✅ **Call Scripts:** AI-generated phone scripts
✅ **CSV Import/Export:** Bulk lead processing
✅ **Reverse Lookup:** Find businesses from phone/email lists

---

## Quick Configuration (Optional)

### Add Your Branding

Edit `.env.production`:
```env
VITE_APP_NAME=Your Agency Name
```

### Enable DataForSEO (Better Data Quality)

1. Get API credentials: https://dataforseo.com
2. Add to environment variables:
```env
DATAFORSEO_LOGIN=your_login
DATAFORSEO_PASSWORD=your_password
```

---

## Pricing (Gemini AI)

**FREE TIER:** 60 requests/minute
- Perfect for testing and low-volume use
- Upgrade at: https://aistudio.google.com/pricing

---

## Troubleshooting

### "API Key Error"
- Check your environment variable is set correctly
- Verify the key at: https://aistudio.google.com/app/apikey

### "No Leads Found"
- The app will show simulation data as fallback
- This is normal if Google Maps API has issues

### "Build Failed"
```bash
# Clear cache and rebuild
rm -rf node_modules dist
npm install
npm run build
```

---

## Next Steps

1. ✅ **Test the app** with real searches
2. ✅ **Add your branding** (company name, offer)
3. ✅ **Try all features** (CSV import, email gen, etc.)
4. ⏸️  **Add Stripe** when ready to monetize (see STRIPE_INTEGRATION_PLAN.md)

---

## Support

- **Issues:** GitHub Issues
- **Documentation:** See TESTING_GUIDE.md
- **Stripe Setup:** See STRIPE_INTEGRATION_PLAN.md (when ready)

---

## Production Checklist

Before going live with customers:

- [ ] Custom domain configured
- [ ] HTTPS enabled (automatic on Vercel/Netlify)
- [ ] API key secured in environment variables
- [ ] Tested on mobile devices
- [ ] All features working
- [ ] Privacy policy added (if collecting user data)
- [ ] Terms of service added (if monetizing)

---

## Estimated Costs

**Development:** Free (already built!)
**Hosting:**
- Vercel/Netlify: Free tier or $20/month
- Docker/VPS: $5-10/month

**AI API:**
- Gemini: Free tier (60 req/min) → $0.00125/request after
- DataForSEO: Optional, ~$0.01/search

**Total:** $0-30/month to start

---

## When to Add Stripe

Wait until you:
1. ✅ Tested all features thoroughly
2. ✅ Have beta users interested
3. ✅ Validated pricing with potential customers
4. ✅ Built a small audience

**Then:** Follow `STRIPE_INTEGRATION_PLAN.md` for monetization

---

**Quick Deploy Time:** 5-10 minutes
**Production Ready:** Yes ✅
**Stripe Required:** No (add later)

**🎉 Your lead generation app is ready to launch!**
