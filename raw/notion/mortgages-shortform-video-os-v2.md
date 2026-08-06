# Source: Notion (page 3a89e94c-f0a4-8117-b809-d36404b26465)

**Version 2.0 update — short-form video production stack**  
**Primary creation engine:** HyperFrames MCP  
**Primary repurposing engine:** OpusClip MCP  
**Research and prioritization:** BC Mortgage Search Intelligence / DataForSEO / live SERP evidence  
**Publishing control:** Human compliance approval before release
> **Platform decision:** HyperFrames is the default engine for creating new, branded mortgage Shorts from structured Search Intelligence briefs. OpusClip is used when an existing long-form recording, webinar, interview, calculator demonstration, or market update must be converted into several short-form clips. The original open-source AutoShorts repositories remain optional prototypes and fallback references rather than the primary production stack.
# Executive production model — v2.0
**Search Intelligence decides what to say. HyperFrames designs the visual explanation. OpusClip repurposes long-form recordings. Human review protects accuracy. LeadSniperAI and the CRM measure business outcomes.**
## Standard workflow
**DataForSEO + live SERPs + PAA + Search Console → validated borrower question → approved mortgage content brief → HyperFrames Short or master recording → OpusClip variations where appropriate → compliance review → YouTube Shorts / Instagram Reels / LinkedIn → matching landing page or calculator → CRM attribution → qualified and funded outcomes.**
## Tool selection rules
<table header-row="true">
<tr>
<td>Content situation</td>
<td>Primary tool</td>
<td>Reason</td>
</tr>
<tr>
<td>Create a new Short from a keyword, PAA question, calculator, comparison, or borrower problem</td>
<td>HyperFrames MCP</td>
<td>Creates controlled, branded animations, captions, charts, timelines, comparisons, and calls to action from a structured brief.</td>
</tr>
<tr>
<td>Turn an existing Dennis recording, webinar, interview, Zoom call, or long YouTube video into several clips</td>
<td>OpusClip MCP</td>
<td>Finds strong moments, reframes footage, adds captions, creates platform variants, and supports distribution workflows.</td>
</tr>
<tr>
<td>Create a presenter-led master video</td>
<td>Dennis recording or HeyGen avatar workflow</td>
<td>Builds authority and provides source footage for repurposing.</td>
</tr>
<tr>
<td>Create an experimental faceless stock-footage video</td>
<td>SaarD00 generator</td>
<td>Useful for inexpensive testing, but not the preferred branded production system.</td>
</tr>
<tr>
<td>Build a fully self-hosted clipping product</td>
<td>Divyaprakash AutoShorts fork</td>
<td>Useful only when white-label ownership and local infrastructure justify the engineering effort.</td>
</tr>
</table>
# HyperFrames short-form creation system
## Primary use cases
- Mortgage myth versus fact
- Borrower problem and possible pathway
- A lender versus B lender versus private lender
- GDS and TDS visual explanations
- Rental offset, add-back, surplus, and deficit examples
- Construction-draw timelines
- Self-employed income and business-cash-flow explanations
- CRA debt and home-equity pathway explanations
- Mortgage renewal and bank-decline options
- Consumer-proposal recovery timelines
- Commercial, construction, and investor financing explainers
- BC market and policy updates after factual verification
## Required reusable templates
1. **Borrower Problem → Pathway** — one urgent situation, explanation, limitation, and CTA.
2. **Myth vs. Fact** — correct one mortgage misconception without sensational language.
3. **Three Options** — compare three legitimate pathways and show who each may suit.
4. **Calculation Explainer** — animate a simple GDS, TDS, rental-income, or equity example.
5. **Process Timeline** — show steps, documents, decision points, and estimated sequence without promising timing.
6. **Product Comparison** — compare A lender, B lender, private lender, refinance, second mortgage, or home-equity options.
7. **Borrower Scenario** — anonymized educational case with assumptions clearly labelled.
8. **FAQ / PAA Answer** — answer one validated search question in 30–45 seconds.
9. **Local BC Insight** — connect a financing issue to a validated city or regional context.
10. **CTA Explainer** — demonstrate the relevant calculator, assessment, or application pathway.
## HyperFrames MCP production prompt
```plain text
Create a professional 9:16 short-form mortgage education video for Mortgages by Dennis Eng in British Columbia, Canada.

Use only the supplied approved facts and assumptions. Do not invent rates, lender policies, qualification thresholds, tax conclusions, legal conclusions, savings claims, approval outcomes, or market data.

Audience: [borrower audience]
Primary keyword: [validated keyword]
Search intent: [intent]
Borrower problem: [plain-language situation]
Approved facts: [fact list]
Target duration: [30–45 seconds]
Target URL: [landing page]
CTA: [one action]
Required disclaimer: [approved wording]
Template: [problem-pathway / myth-fact / comparison / calculation / timeline / FAQ]

Visual requirements:
- Clear opening hook in the first 2 seconds
- Mobile-safe animated captions
- Branded typography and restrained motion
- One visual idea per scene
- Use diagrams, number animation, comparisons, and timelines where they improve understanding
- Keep critical text inside mobile-safe margins
- Include the Mortgages by Dennis Eng end card and approved CTA
- Maintain a calm, credible, advisory tone

Return and render:
1. Scene plan
2. Spoken script
3. On-screen text
4. Visual composition
5. Captions
6. End card
7. Compliance notes
8. 9:16 MP4 preview
```
# OpusClip repurposing system
## Source assets
- Five-to-twelve-minute mortgage explainers
- Webinars and workshops
- Podcast and interview appearances
- Screen-recorded mortgage calculators
- Market updates
- Construction-financing presentations
- Self-employed qualification lessons
- Commercial mortgage case discussions
- Frequently asked question sessions
## Clip extraction categories
Replace generic entertainment scoring with mortgage-specific value signals:
- Strong borrower problem statement
- Surprising but verified fact
- Clear lender comparison
- Useful numerical example
- Common documentation mistake
- Myth correction
- Practical next step
- Strong standalone answer
- Credible borrower story
- Clear CTA with adequate context
## OpusClip MCP prompt
```plain text
Analyze this approved mortgage master video and create five standalone clips between 30 and 55 seconds.

Prioritize moments that contain a complete and accurate answer, a strong borrower problem, a useful comparison, a simple calculation, or a practical next step.

Exclude clips that:
- depend on missing earlier context,
- contain unverified rates or thresholds,
- imply guaranteed approval,
- make legal or tax conclusions,
- criticize a lender unfairly,
- disclose confidential borrower information.

For each selected clip:
- reframe to 9:16,
- keep the speaker centred,
- remove unnecessary pauses without changing meaning,
- add professional mobile-safe captions,
- add a keyword-aligned title card,
- add the approved Mortgages by Dennis Eng end card,
- output a review copy before scheduling.
```
# Short-form video content brief — v2.0
Every production brief must include:
<table header-row="true">
<tr>
<td>Field</td>
<td>Required value</td>
</tr>
<tr>
<td>Campaign ID</td>
<td>Unique keyword or content-cluster identifier</td>
</tr>
<tr>
<td>Primary keyword</td>
<td>Validated keyword or clearly labelled hypothesis</td>
</tr>
<tr>
<td>Supporting queries</td>
<td>PAA, related searches, Search Console queries, or CRM questions</td>
</tr>
<tr>
<td>Search intent</td>
<td>Informational, commercial, transactional, comparison, local, or problem-aware</td>
</tr>
<tr>
<td>Borrower audience</td>
<td>Self-employed, homeowner, investor, builder, senior, commercial owner, or another defined group</td>
</tr>
<tr>
<td>Borrower problem</td>
<td>One plain-language problem</td>
</tr>
<tr>
<td>Approved facts</td>
<td>Facts reviewed before script generation</td>
</tr>
<tr>
<td>Assumptions</td>
<td>Any numerical or scenario assumptions explicitly labelled</td>
</tr>
<tr>
<td>Prohibited claims</td>
<td>Rates, guarantees, universal rules, tax conclusions, or other restricted statements</td>
</tr>
<tr>
<td>Video template</td>
<td>Selected reusable HyperFrames composition or OpusClip workflow</td>
</tr>
<tr>
<td>Duration</td>
<td>Normally 30–45 seconds; maximum 60 seconds unless platform strategy requires otherwise</td>
</tr>
<tr>
<td>Target page</td>
<td>Matching landing page, guide, calculator, or assessment</td>
</tr>
<tr>
<td>CTA</td>
<td>One measurable next action</td>
</tr>
<tr>
<td>Disclosure</td>
<td>Approved compliance wording</td>
</tr>
<tr>
<td>Confidence</td>
<td>Verified, supported inference, strategic hypothesis, or insufficient data</td>
</tr>
<tr>
<td>Reviewer</td>
<td>Named human approval owner</td>
</tr>
</table>
# Short-form video acceptance criteria
A video is ready for publication only when:
- [ ] It answers one clear borrower question.
- [ ] Its keyword and target page are documented.
- [ ] Every factual claim comes from the approved brief.
- [ ] Numerical examples label assumptions.
- [ ] Spoken words and captions communicate the same meaning.
- [ ] Captions remain readable on a mobile screen.
- [ ] The hook is relevant rather than sensational.
- [ ] The video avoids guaranteed approval, guaranteed savings, or universal lender rules.
- [ ] The CTA matches the borrower’s intent.
- [ ] The disclosure is present where required.
- [ ] The landing page is active and mobile-friendly.
- [ ] UTM parameters and campaign ID are assigned.
- [ ] A human reviewer has approved the final render.
# Recommended production cadence
## Weekly operating rhythm
- **Monday:** Pull Search Intelligence, PAA, Search Console, and CRM questions; select three priority topics.
- **Tuesday:** Build and approve structured briefs.
- **Wednesday:** Produce three HyperFrames Shorts or record one master video.
- **Thursday:** Create OpusClip variants where source footage exists; complete compliance review.
- **Friday:** Publish approved videos, update website answer blocks, and record campaign URLs.
## Initial monthly output
- 8–12 new HyperFrames Shorts
- 2 master videos recorded by Dennis or produced with a presenter workflow
- 6–12 OpusClip derivatives from those master assets
- 4 transcript-derived website answer blocks
- 2 updated landing pages or calculator explanations
# Measurement framework
Measure business outcomes by video and keyword cluster:
- Three-second hold rate
- Average watch time
- Completion rate
- Replays and saves
- Profile visits
- Landing-page clicks
- Calculator starts
- Assessment starts
- Qualified leads
- Advisor conversations
- Applications
- Funded mortgages
- Revenue attributed to campaign
- Assisted conversions
- Search ranking or Search Console movement for the supported page
## Decision rules
- High views and low clicks: strengthen CTA and page alignment.
- Strong retention and low completion: shorten the middle section.
- Low retention in the first three seconds: replace the hook, not the entire topic.
- Strong saves and shares: create a deeper master video and supporting guide.
- Qualified leads from a low-volume term: raise its commercial priority despite low search demand.
- No engagement after three materially different hooks: pause or merge the topic.
- Strong video engagement but weak landing-page conversion: improve the page or assessment before increasing output.
# Final platform recommendation
**Default:** HyperFrames MCP for net-new, search-driven short-form video.  
**Use OpusClip MCP:** when long-form source footage exists and several derivatives are needed.  
**Use Dennis or HeyGen presenter workflows:** for authority-building master videos.  
**Retain the two GitHub AutoShorts repositories:** as experimental references, fallback tools, and potential future components of a self-hosted LeadSniperAI video product.
The proprietary advantage should remain in the Search Intelligence, mortgage fact controls, reusable branded templates, compliance workflow, landing-page alignment, and funded-outcome attribution—not in rebuilding commodity video rendering before volume justifies it.
---
**Document owner:** Dennis Eng / Growth Operations  
**Brand:** Mortgages by Dennis Eng  
**Market:** British Columbia, Canada  
**Primary channels:** YouTube Shorts, Instagram Reels, TikTok, LinkedIn video  
**Production engine:** SaarD00/AI-Youtube-Shorts-Generator  
**Status:** Ready for pilot
> **Operating principle:** Every Short must originate from validated borrower intent, support a specific search cluster, answer one clear question, and direct the viewer to the most relevant page, calculator, or assessment.
# 1. Purpose
Build a repeatable AutoShorts production system that converts current Search Engine Intelligence into short-form mortgage videos for [**mortgagesbydenniseng.ca**](http://mortgagesbydenniseng.ca).
The system connects:
**DataForSEO and live SERP evidence → content opportunity → approved mortgage brief → AutoShorts production → compliance review → distribution → landing page → lead capture → CRM attribution.**
The objective is not to manufacture generic viral content. The objective is to create high-intent, searchable, reusable video assets that increase qualified mortgage applications and strengthen topical authority in Google and AI search.
# 2. Strategic alignment
This operating system follows the existing BC Mortgage Search Intelligence principles:
- Qualified borrower intent is more important than raw traffic.
- Search metrics must not be invented.
- Page and video decisions should use live SERP evidence.
- Low-volume topics may be prioritized when commercial value is high.
- Content should begin with the borrower’s situation before discussing a product.
- Each asset requires a clear CTA and measurable business outcome.
- Unsupported approval, rate, savings, tax, or qualification claims are prohibited.
- City-specific videos require validated local relevance.
# 3. Business outcomes
## Primary outcomes
- Generate qualified mortgage assessments.
- Support rankings for priority money pages.
- Win People Also Ask and AI-answer visibility.
- Build authority in alternative, self-employed, construction, refinance, and financial-recovery mortgages.
- Increase branded search for Dennis Eng and “Story Over Score.”
- Build retargeting audiences from high-intent video engagement.
## Video-to-revenue pathway
**Short → relevant landing page → calculator or assessment → Atomic CRM / LeadSniperAI → advisor follow-up → funded mortgage.**
# 4. Priority video clusters
## Tier 1 — Immediate revenue
1. Private Mortgage BC
2. Home Equity Loan BC
3. Mortgage Refinance BC
4. Second Mortgage BC
5. Reverse Mortgage BC
6. Bank Declined Mortgage
7. Mortgage to Pay CRA Debt
8. Tax Arrears Mortgage
9. Bad Credit Mortgage
10. Mortgage Renewal Alternatives
## Tier 2 — Differentiation
1. B Lender Mortgage BC
2. Self-Employed Mortgage BC
3. Bank-Statement Mortgage
4. Low Reported Income Mortgage
5. Mortgage for Incorporated Business Owners
6. Mortgage After Consumer Proposal
7. Mortgage After Bankruptcy
8. Alt-to-Prime Mortgage Recovery
## Tier 3 — High-value financing
1. Construction Financing BC
2. Development Financing BC
3. SSMUH and Multiplex Financing
4. Commercial Mortgage BC
5. Commercial Refinance BC
6. Rental Portfolio Financing
7. Investor Mortgage Qualification
8. Bridge Financing
# 5. Story Over Score video framework
Every Short should follow this narrative sequence:
1. **Borrower problem:** State the real-life situation in plain language.
2. **Why it happens:** Explain the lender or qualification issue.
3. **Possible pathway:** Present one or more legitimate financing approaches.
4. **Important limitation:** Clarify that approval depends on the complete file.
5. **Next step:** Send the viewer to the relevant assessment, calculator, guide, or consultation.
## Approved opening patterns
- “Your bank declined the mortgage, but that does not always mean the file is finished.”
- “Strong business cash flow does not always appear as high taxable income.”
- “Owing CRA can affect a mortgage application, but the solution depends on equity, income, and the property.”
- “Construction financing works differently from a regular purchase mortgage.”
- “A low credit score is only one part of the lending decision.”
# 6. Search Intelligence intake
A topic may enter production only after the following fields are completed:
<table header-row="true">
<tr>
<td>Field</td>
<td>Requirement</td>
</tr>
<tr>
<td>Primary keyword</td>
<td>Exact validated keyword or approved strategic hypothesis</td>
</tr>
<tr>
<td>Search intent</td>
<td>Transactional, commercial, informational, local, comparison, problem-aware</td>
</tr>
<tr>
<td>Borrower situation</td>
<td>Plain-language problem being solved</td>
</tr>
<tr>
<td>Search volume</td>
<td>DataForSEO value or “not yet verified”</td>
</tr>
<tr>
<td>CPC</td>
<td>DataForSEO value or “not yet verified”</td>
</tr>
<tr>
<td>Keyword difficulty</td>
<td>DataForSEO value or “not yet verified”</td>
</tr>
<tr>
<td>SERP format</td>
<td>Service page, guide, video, forum, calculator, comparison, local result</td>
</tr>
<tr>
<td>PAA question</td>
<td>Live question where available</td>
</tr>
<tr>
<td>Target webpage</td>
<td>Existing or planned URL</td>
</tr>
<tr>
<td>CTA</td>
<td>Assessment, calculator, guide, call, application</td>
</tr>
<tr>
<td>Confidence</td>
<td>Verified, supported inference, strategic hypothesis, insufficient data</td>
</tr>
<tr>
<td>Compliance owner</td>
<td>Person responsible for factual review</td>
</tr>
</table>
# 7. Video opportunity scoring
Score each proposed Short out of 100:
<table>
<tr>
<td>Factor</td>
<td>Weight</td>
</tr>
<tr>
<td>---</td>
<td>---:</td>
</tr>
<tr>
<td>Commercial intent</td>
<td>25</td>
</tr>
<tr>
<td>Relevance to current money page</td>
<td>20</td>
</tr>
<tr>
<td>Borrower urgency</td>
<td>15</td>
</tr>
<tr>
<td>SERP or PAA opportunity</td>
<td>15</td>
</tr>
<tr>
<td>Conversion pathway clarity</td>
<td>10</td>
</tr>
<tr>
<td>Search demand</td>
<td>5</td>
</tr>
<tr>
<td>Local relevance</td>
<td>5</td>
</tr>
<tr>
<td>Repurposing value</td>
<td>5</td>
</tr>
</table>
## Production tiers
- **80–100:** Produce immediately.
- **65–79:** Add to the next publishing sprint.
- **50–64:** Produce only as supporting content.
- **Below 50:** Hold, merge, or discard.
# 8. AutoShorts technical workflow
## Base repository
`https://github.com/SaarD00/AI-Youtube-Shorts-Generator`
## Current production components
- Gemini for script generation
- Edge-TTS for narration
- Pexels for stock footage
- FFmpeg for assembly and rendering
- Optional branded avatar footage
- Vertical MP4 output
## Required environment
- Python 3.10+
- Git
- FFmpeg
- Gemini API key
- Pexels API key
- Virtual Python environment
## Repository setup
```bash

git clone https://github.com/SaarD00/AI-Youtube-Shorts-Generator.git
cd AI-Youtube-Shorts-Generator
python -m venv .venv
```
Windows activation:
```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Environment file:
```javascript
GEMINI_API_KEY=your_key
PEXELS_API_KEY=your_key
GEMINI_MODEL=gemini-2.0-flash
```
Generate a video:
```bash
python main.py
```
Expected output:
```plain text
assets/final/final_short.mp4
```
# 9. Required modifications before commercial use
## Must-have upgrades
1. **Structured content brief input** rather than a single unrestricted topic.
2. **Subtitle generation** with mobile-safe caption placement.
3. **Mortgage fact lock** so the model uses approved facts only.
4. **Unique output filenames** based on keyword, date, and campaign.
5. **Batch CSV or database processing.**
6. **Brand templates** for Mortgages by Dennis Eng.
7. **Human approval gate** before publishing.
8. **Metadata output** for title, description, hashtags, CTA, and landing page.
9. **Analytics identifiers** for campaign and keyword attribution.
10. **Approved media library** to reduce irrelevant stock footage.
## Recommended folder structure
```plain text
assets/
  brand/
    logo/
    fonts/
    colours/
    disclaimers/
  avatar/
  approved-footage/
    homes/
    construction/
    business-owners/
    rental-properties/
    bc-locations/
  generated/
  final/
  archive/
briefs/
metadata/
reports/
```
# 10. Structured brief specification
Each video should be generated from a JSON brief:
```json
{
  "brand": "Mortgages by Dennis Eng",
  "campaign": "B Lender Mortgage BC",
  "primary_keyword": "b lender mortgage bc",
  "search_intent": "commercial investigation",
  "borrower_problem": "The bank declined the mortgage because the borrower did not meet prime guidelines.",
  "approved_facts": [
    "B lenders may consider borrowers who fall outside prime-lender guidelines.",
    "Pricing, fees and qualification vary by lender and borrower profile.",
    "An exit strategy should be considered before accepting alternative financing."
  ],
  "prohibited_claims": [
    "guaranteed approval",
    "lowest rate",
    "everyone qualifies"
  ],
  "target_duration_seconds": 40,
  "target_url": "/b-lender-mortgage-bc/",
  "cta": "Complete the mortgage options assessment.",
  "required_disclaimer": "Mortgage approval and terms depend on the complete application and lender guidelines.",
  "confidence": "supported inference"
}
```
# 11. Script specification
## Target duration
- Standard: 30–45 seconds
- Maximum: 60 seconds
- Spoken pace: approximately 120–150 words per minute
- One core question per video
## Script architecture
- **0–3 seconds:** Hook
- **3–10 seconds:** Borrower problem
- **10–25 seconds:** Explanation
- **25–35 seconds:** Possible pathway
- **35–45 seconds:** Limitation and CTA
## Script requirements
- Use Canadian mortgage terminology.
- Use plain language.
- Avoid unexplained acronyms.
- Avoid quoting unverified rates or approval thresholds.
- Avoid presenting lender policies as universal.
- Avoid legal, tax, or financial guarantees.
- Include one clear CTA.
- Ensure the spoken script and on-screen text are consistent.
# 12. Master generation prompt
```plain text
Create a 35–45 second vertical mortgage education video for Mortgages by Dennis Eng in British Columbia, Canada.

Use only the approved facts in the supplied content brief. Do not invent rates, lender policies, qualification thresholds, legal conclusions, tax conclusions, or guarantees.

Start with the borrower’s real-life problem. Explain why the issue happens, identify a legitimate financing pathway, state an important limitation, and end with the specified CTA.

Return:
1. Spoken script
2. Eight short scenes
3. On-screen caption for each scene
4. Visual search phrase for each scene
5. YouTube Shorts title
6. Description
7. Five relevant hashtags
8. Compliance review notes
9. Target landing page

Keep the tone calm, credible, practical, and non-judgmental. Use the Story Over Score positioning without criticizing banks or lenders.
```
# 13. Search-to-video content mapping
<table header-row="true">
<tr>
<td>Search cluster</td>
<td>Short concept</td>
<td>Target destination</td>
</tr>
<tr>
<td>B Lender Mortgage BC</td>
<td>“What happens after a bank mortgage decline?”</td>
<td>`/b-lender-mortgage-bc/`</td>
</tr>
<tr>
<td>Self-Employed Mortgage BC</td>
<td>“Why taxable income may not tell the whole story”</td>
<td>`/self-employed-mortgage-bc/`</td>
</tr>
<tr>
<td>Mortgage to Pay CRA Debt</td>
<td>“Can home equity be used to address CRA debt?”</td>
<td>`/mortgage-to-pay-cra-debt/`</td>
</tr>
<tr>
<td>Mortgage After Consumer Proposal</td>
<td>“Can you get a mortgage after a consumer proposal?”</td>
<td>`/mortgage-after-consumer-proposal/`</td>
</tr>
<tr>
<td>Construction Financing BC</td>
<td>“Why construction loans are released in draws”</td>
<td>`/construction-financing-bc/`</td>
</tr>
<tr>
<td>Rental Property Mortgage</td>
<td>“How rental income may be treated by lenders”</td>
<td>Rental income calculator or investor page</td>
</tr>
<tr>
<td>Home Equity Loan BC</td>
<td>“Three reasons homeowners access equity”</td>
<td>`/home-equity-loan-bc/`</td>
</tr>
<tr>
<td>Reverse Mortgage BC</td>
<td>“How homeowners may access equity in retirement”</td>
<td>`/reverse-mortgage-bc/`</td>
</tr>
<tr>
<td>Commercial Mortgage BC</td>
<td>“What lenders review in a commercial mortgage”</td>
<td>`/commercial-mortgage-bc/`</td>
</tr>
<tr>
<td>Mortgage Renewal Alternatives</td>
<td>“What to do when a lender will not renew”</td>
<td>Renewal assessment page</td>
</tr>
</table>
# 14. Initial 15-video pilot
## Sprint A — Immediate revenue
1. What is a private mortgage in BC?
2. What happens when a bank declines your mortgage?
3. Can home equity be used to consolidate debt?
4. What is a second mortgage?
5. What are mortgage renewal alternatives?
## Sprint B — Differentiation
1. What is a B lender mortgage?
2. Why self-employed borrowers may show low taxable income
3. How business bank statements may support a mortgage application
4. Mortgage options after a consumer proposal
5. How an alternative mortgage exit strategy works
## Sprint C — High-value niches
1. How construction mortgage draws work
2. Financing a multiplex or SSMUH project
3. How lenders may treat rental income
4. What lenders review for a commercial mortgage
5. Bridge financing explained in plain language
# 15. Distribution rules
## YouTube Shorts
- Use the primary keyword naturally in the title.
- Link the relevant website page in the description.
- Add a pinned comment with the CTA.
- Place the Short into a topic-specific playlist.
- Reuse the transcript as a supporting FAQ or article section where appropriate.
## Instagram and TikTok
- Use borrower-language hooks rather than technical product names alone.
- Add subtitles because many viewers watch without sound.
- Place the landing page in the profile or campaign link hub.
- Avoid excessive hashtags.
## LinkedIn
- Reframe self-employed, commercial, construction, and investor videos for business-owner audiences.
- Add a short written insight and a question that invites relevant discussion.
# 16. SEO and AIO reuse
Every approved video should create a reusable content package:
- Short-form video
- Full transcript
- 40–60 word direct answer
- Landing-page FAQ
- Schema-ready question and answer
- YouTube title and description
- Social captions
- Email nurture snippet
- Internal-link suggestion
- AI-search answer block
The webpage remains the canonical source. The video supports discovery and engagement but should not create a competing thin page.
# 17. Compliance and quality gate
A video cannot be published until all items are approved:
- [ ] Keyword and search intent validated
- [ ] Target page selected
- [ ] Approved facts supplied
- [ ] Rates and fees omitted or verified
- [ ] No approval guarantee
- [ ] No universal lender-policy statement
- [ ] No unsupported legal or tax conclusion
- [ ] Required disclaimer included
- [ ] Captions reviewed
- [ ] Visuals are relevant and licensed
- [ ] CTA is accurate
- [ ] Landing page is live and tracked
- [ ] Final human approval completed
# 18. Tracking and attribution
Each video record should contain:
- Video ID
- Primary keyword
- Search cluster
- Target page
- Platform
- Publish date
- Campaign UTM
- Views
- Three-second views
- Average watch time
- Completion rate
- Saves and shares
- Website clicks
- Assessment starts
- Qualified leads
- Applications
- Funded mortgages
- Revenue attribution
## UTM example
```plain text
?utm_source=youtube&utm_medium=shorts&utm_campaign=b_lender_bc&utm_content=bank_declined_01
```
# 19. Performance decision rules
## Keep and expand
- Strong completion rate
- Meaningful website clicks
- Assessment starts or qualified leads
- Search impressions for the target cluster
- High saves, shares, or comments containing borrower questions
## Rewrite the hook
- Viewers leave within the first three seconds
- Topic is commercially relevant but retention is weak
## Improve the CTA or landing page
- Video retention is strong but clicks or assessment starts are weak
## Merge or retire
- Repeated low retention
- No meaningful search or commercial alignment
- Topic duplicates another stronger asset
# 20. 30-day implementation plan
## Week 1 — Foundation
- Clone and test the AutoShorts repository.
- Create branded folders and naming rules.
- Define approved disclaimers and factual boundaries.
- Select five Tier 1 topics using current Search Engine Intelligence.
- Confirm destination pages and tracking links.
## Week 2 — Prototype
- Add structured brief support.
- Add subtitles.
- Add unique filenames and metadata output.
- Produce three internal test videos.
- Complete mortgage and brand review.
## Week 3 — Pilot production
- Produce five approved Shorts.
- Publish across YouTube, Instagram, and TikTok.
- Add transcripts and FAQs to relevant webpages.
- Record baseline performance.
## Week 4 — Optimization
- Review hook retention, completion, clicks, and lead quality.
- Improve visual search phrases and CTAs.
- Approve the next ten videos.
- Document reusable templates.
# 21. Acceptance criteria
The first release is successful when:
- Five videos have been generated from structured search briefs.
- Every video maps to a validated keyword cluster and landing page.
- Captions and branding render correctly in vertical format.
- No unsupported mortgage claim appears in the output.
- Each asset includes metadata and campaign tracking.
- Human approval is recorded before publication.
- Website clicks and assessment starts can be attributed by video.
# 22. Current confidence and data status
- **Verified:** Brand, target market, priority borrower journeys, website strategy, and Search Intelligence methodology.
- **Supported inference:** Short-form video can support discovery, PAA-style answers, topical authority, and landing-page engagement when tied to validated topics.
- **Strategic hypothesis:** Specific platform performance, lead cost, and funded-loan contribution require pilot testing.
- **Insufficient data:** Final video production order should be updated after the latest DataForSEO metrics and live SERP evidence are applied.
# 23. Next execution action
Select the first five Tier 1 keywords from the Search Intelligence database, complete a structured brief for each, and run a controlled AutoShorts pilot before enabling batch production or automatic publishing.
<page url="https://app.notion.com/p/3a89e94cf0a481c8a80ef1420bdaf8b5">HyperFrames Mortgage Video Starter Kit — Mortgages by Dennis Eng</page>
