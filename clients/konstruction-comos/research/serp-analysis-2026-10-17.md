# KommercialConnect SERP Analysis — 2026-10-17

## Project
- **OpenSEO Project:** KommercialConnect
- **Project ID:** `7f4bbe03-f30f-4eeb-b648-d64985be70a1`
- **URL:** http://127.0.0.1:3005/p/7f4bbe03-f30f-4eeb-b648-d64985be70a1
- **Market:** 2124/en (default) — SERP scans run at 20114 (BC)
- **Tool:** `get_serp_results` via OpenSEO MCP

## Top 5 Keywords Scanned (by opportunity = vol × CPC)

| Keyword | Vol | KD | CPC | Top-10 commercial lenders? |
|---|---|---|---|---|
| bc loans | 1,300 | 6 | $9.01 | **0** (loanbeaver only @ #10) |
| commercial construction financing | 110 | 8 | $13.69 | **3** (Swoop, LendCity, Greenbox) |
| construction financing canada | 140 | 1 | $10.16 | **0** (CMHC + blogs/lawyers) |
| construction mortgage bc | 90 | 0 | $13.53 | **0** (BC mortgage brokers dominate) |
| commercial construction loan | 90 | 8 | $7.62 | **1** (Dominion Lending @ #6) |

## Key Insight: BC Commercial Construction SERP is Under-Served

Across the **5 keywords × top 10 = 50 organic positions**, only **5 (10%)** are taken by commercial lenders. The rest is split between:

- **Student loan content** (dominates `bc loans` — StudentAid BC, UBC, BCIT, UFV, VIU, VCC)
- **Mortgage brokers** (dominates `construction mortgage bc` — axiumcap, satbirbhullar, rowansmith, sandhusran, BMO)
- **Government & institutional** (BDC, CMHC, MCAP, First National, Practical Law, Forbes)
- **Generic SEO content** (blogs, Facebook, "how it works" pages, renovation contractors in Ontario)

## What This Means for KommercialConnect

1. **The opportunity is real.** There's almost no commercial construction lender actively serving the BC SERP for these 5 keywords. A focused SEO + content push could rank in the top 5 for all of them.

2. **Two SEO competitors worth studying:**
   - `rowansmith.ca` — "Construction Mortgage Vancouver BC | 2026 Guide" (ranked #7 for `construction mortgage bc`). Has a dedicated landing page for the BC term. Study their page structure.
   - `satbirbhullar.ca` — multiple BC construction mortgage ranks. Another mortgage broker with a content lead-gen play.

3. **Don't write content for "bc loans"** — the SERP intent is student loans. Google's serving studentaidbc.ca at #1. A commercial lender page for "bc loans" will be confused for student content. Better to write for **"construction business loan"** or **"commercial construction loan bc"** (long-tail, no student intent collision).

4. **Long-tail expansion** (next research batch) should focus on:
   - `construction loan vancouver` (10/mo now, will grow with content)
   - `construction loan kelowna`, `construction loan victoria`, `construction loan surrey`, `construction loan burnaby` (zero vol now but no commercial competitors in SERP for those city+term combinations)
   - `multi family construction loan bc`
   - `townhouse construction loan vancouver`
   - `rezoning financing vancouver`
   - `permit financing vancouver`

## Saved Artifacts

- `/home/denni/wiki/clients/konstruction-comos/research/openseo-keyword-metrics-2026-10-17.json` — DataForSEO metrics for 14 keywords
- `/home/denni/wiki/clients/konstruction-comos/research/openseo-serp-scans-2026-10-17.json` — Full SERP data (5 keywords × 20 results each)
- OpenSEO tags applied: `kommercial-connect-2026-10-17, construction, bc, fresh-metrics, serp-scanned-2026-10-17`

## Open Questions for the Client

1. **Domain for KommercialConnect:** None set in OpenSEO. Is it `kommercialconnect.com`? `clearconnect.com`? `konstruction.com`? (Lovable URL is `clearconnectcom.lovable.app` — placeholder.)
2. **Service area:** Is the lead-gen target Lower Mainland only, or all of BC? That changes whether we prioritize `vancouver` / `surrey` / `burnaby` (sub-100/mo now) or `kelowna` / `victoria` / `nanaimo` (zero vol, blue ocean).
3. **Content cadence:** Is there a content team in place to publish 2-3 SEO articles/month targeting these terms, or do we need to scope that work?
4. **Existing pages:** Does KommercialConnect already have any landing pages? If yes, which URLs should we SEO-audit (`run_site_audit`) first?

## Next Steps Recommended

- [ ] Set the project domain in OpenSEO (need domain from client)
- [ ] Run a `run_site_audit` if a domain exists
- [ ] Pull a PAA (People Also Ask) expansion on top 3 commercial keywords
- [ ] Run `find_serp_competitors` for the top 3 SERPs to map the full competitor graph
- [ ] Schedule monthly `get_keyword_metrics` re-check on the 14 saved keywords to track movement
