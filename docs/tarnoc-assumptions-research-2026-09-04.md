# Tarnoc v2: market evidence for the model's assumptions

Date: 2026-09-04. Five research passes (channel, marketing, service, manufacturing, people), each against public Dutch and European sources, all cited by URL in the detailed sections below. Verdicts are on the values in `models/Tarnoc_v2_2026-09-01.xlsx` as of commit `4408009`.

"Mine" means an assumption Claude introduced when rebuilding the model. "Client" means it was carried over from the client's original workbook; those are flagged, not changed.

## Summary of verdicts

| Area | Assumption | Model | Whose | Verdict | Evidence says |
| --- | --- | --- | --- | --- | --- |
| Channel | Installer commission | 10% of boiler price | mine | supported as a fee | Loyalty and referral schemes pay 4-10%; if installers buy and resell they expect 20-30% trade margin |
| Channel | Partner can sell per month | 8 | mine | supported for a mid-sized firm | Certification norm 80 installs a year per monteur |
| Channel | Orders a partner brings in per month | 1, 2, 3, 4 (2027-30) | mine | looks high | 0.5-1 in year one, 2-3 by year four; 4 only for top partners |
| Channel | Partners per partner manager | 18 | mine | low vs incumbents, fine for onboarding | 15-25 early, 40-80 at steady state |
| Channel | Partners trained per trainer per year, cost | 40, EUR3,500 | mine | throughput low, cost fine | 40-80 a year; EUR1,500-2,500 plus a demo pool |
| Channel | Rep quota | 20 closes a month | mine | looks high | US HVAC comfort advisors 8-10, top decile 11-17; solar 2-3 in year one |
| Channel | Direct share path | 80% to 35% (base), 70% to 15% (aggr) | mine | no precedent | Brands are installer-led from day one or stay mostly direct; 70-90% direct 2027, 40-60% 2030 |
| Marketing | Cost per lead | EUR120 | mine | supported | Exclusive heat-pump leads EUR130-280 NL/BE, EUR50-350 DE; range EUR90-180 |
| Marketing | Lead to order | 50% x 40% = 20%, EUR600 per order | mine | looks high | 8-15% lead to order; EUR900-1,800 per marketing-won order in 2027-28 |
| Marketing | Cost per lead falls 10% per doubling of installed base | from 250 units | mine | magnitude unsupported | Paid CPL is set by ad auctions and rose for Enpal and US solar; referrals are what get cheaper |
| Marketing | Marketing team | 2 + 1 per EUR3m spend | mine | looks low | 1 per EUR1-1.5m of media, or a 10-12% agency line |
| Marketing | Marketing as share of revenue | 1-3% | result | looks low | HVAC 6% (10-15% in growth), NIBE selling 14.6%; 6-10% early, 3-5% later |
| Marketing | Aggressive volume 2030 | 29,600 units | mine | looks high | NL sells 43k hybrids and 425k boilers a year; Quatt reached about 12k a year in year four at a fifth of the price |
| Service | Boilers one engineer looks after | 750 | mine | supported | 600-900 at 4.5-5.5 visits a day incl. breakdowns |
| Service | Contract attach rate | 88% | client | looks high | 76% of new-boiler buyers hold a contract (Panteia/ACM 2025); 65-80% |
| Service | Boiler contract price | EUR60 / 90 a year ex VAT | client | looks low | Dutch basic tiers EUR96-132 incl. VAT, comfort EUR156-290; EUR75-95 / 130-190 ex VAT |
| Service | Hybrid contract price | EUR150 / 200 | client | supported | Market EUR140-363 incl. VAT |
| Service | Contract direct cost | EUR30-40 boiler, 75-100 hybrid | client | supported, low for parts-inclusive premium | Premium EUR40-70 / 80-130 in years 1-3 |
| Service | Support agent per installed units; escalation | 1:2,500; 1:15,000 | mine | supported at maturity, light early | 1:1,500-2,000 in 2027-29 |
| Service | Warranty reserve | none (3% inside BOM) | mine (removed) | looks low | Ariston accrues 1.4-1.6% of revenue with a 3.6% provision, Daikin 2.4%; 2.5-4% of hardware revenue on early cohorts, 1-1.5% later |
| Manufacturing | In-house line | 1,000/month, EUR2.5m + 1m, 12 months | mine | supported | EUR292 per unit of annual capacity vs peers EUR250-600 |
| Manufacturing | Operators per line; facility | 35; EUR90k/month | mine | high; high | Intergas/Remeha 1.2-1.9 h/unit vs 4.8; facility EUR40-75k |
| Manufacturing | Assembly partner capacity | 650 / 1,000 a month | mine | supported as a line rate | Partners commit capacity with take-or-pay, not output; add a 6-12 month ramp |
| Manufacturing | BOM cost-down | EUR9,984 to 4,998 (50%) | client | looks high | Learning rates 3-17% per doubling; the 5k to 10k step alone is 29% for one doubling; tier 3 EUR5,800-6,800 |
| Manufacturing | Supply chain FTE per units; order desk | 1:900; 1:3,000 | mine | fits start-up scale; supported | Core of 3-4 then 1 per 1,500-2,500 |
| Manufacturing | DSO / DPO / DIO | 20 / 45 / 0-30 days | mine | DSO low, DPO fine, DIO 0 no precedent | Peers DSO 45-72, DIO 92-131; suggest 30-45 / 45-60 / 20-45 |
| Manufacturing | Depreciation | 8 years | mine | supported for line, long for tooling | Tooling 3-5 years |
| Manufacturing | Inbound shipping per outdoor unit | EUR100 | client | supported, conservative | EUR40-60 full container, EUR80-120 groupage |
| People | Loaded cost per month | rep 7,500; PM 8,000; trainer/desk/mkt 7,000; ops 5,000; support 4,800; back office 7,000; R&D 5,700; engineer 6,500 | mine (R&D, engineer client) | right in total, mis-distributed | Rep 5,000-6,600 unless car included; support 3,700-4,600; leadership low for executives |
| People | Wage growth; other cost inflation | 8%; 10% a year | mine | both high | CPB 3.2-4.2% wages; CPI 2.1-3%; suggest 4-5.5% and 3-5% |
| People | Office / IT / travel per head; recruitment | 700 / 250 / 300; EUR8,000 | mine | supported | NFC Index EUR760 per FTE; recruitment avg EUR4,494, agency 15-25% of salary |
| People | Finance and legal | EUR7,000 a month | mine | fine to 2027, low after | Audit, patents, rounds: EUR12-20k a month from 2028 |
| People | Tax | 25.8%, losses carried forward | mine | correct | 19% band on first EUR200k omitted, worth at most EUR13.6k a year |
| People | R&D team, aggressive | 48 by 2030 | mine | looks low | 60-90 at EUR500m revenue, or an explicit outsourced engineering line |
| People | Back office, aggressive | 8 for 340 staff | mine | looks low | 14-22; HR alone needs 4-6 |
| People | Revenue per head, aggressive | EUR1.5m | result | looks high | Incumbents EUR175-333k; outsourced assembly justifies EUR400-700k |

## What this means for the model

Six of my assumptions flatter the plan and should change: the funnel conversion (20% to about 12%, which roughly doubles cost per marketing-won order), the rep quota (20 to about 10), partner-sourced orders (slower ramp), the missing warranty reserve, wage and cost inflation (too high, which cuts the other way), and working capital (DSO and DIO too generous to cash). The aggressive volume path is the biggest single stretch: 29,600 units in 2030 is 70% of today's Dutch hybrid market.

Three client inputs carry more weight than any of mine and should be raised with the client rather than changed by us: the 50% BOM cost-down, the 88% service attach rate, and the boiler service prices, which are below the market.

Proposed changes, in order of effect on the numbers:

1. Funnel: lead to qualified 40%, qualified to won 30% (12% lead to order, about EUR1,000 per marketing-won order). Remove the cost-per-lead improvement. Raise marketing to hold base volume.
2. Aggressive case: partner signing 2, 4, 6, 7 a month, marketing sized to land near 15,000 units in 2030; R&D hires 3, 8, 10, 10; back office 3, 5, 8, 11, 14; line facility EUR60k a month.
3. Rep quota 10 a month.
4. Partner-sourced orders 0.5, 1, 2, 3 a month for 2027-30.
5. Warranty reserve back in at 3% of hardware revenue.
6. Wage growth 5%, other cost inflation 4%.
7. DSO 30 days, DIO 30 days in both cases.
8. Support agent EUR4,500, sales rep EUR6,500 a month.

Items 1, 3, 4 and 5 cut the base case; 6 and 8 help it. Net effect is to be measured after the change, but the base case on a one-year BOM basis will not survive it without a larger raise.

---


---

# Tarnoc channel assumptions: market evidence

Date: 2026-09-04. Scope: the seven sales-channel assumptions in the Tarnoc model (Turbineketel EUR 8,526 ex VAT; Combi+ about EUR 13,800 ex VAT; Dutch launch 2027). Sources are public web pages and reports fetched today. Where a number is my own calculation from cited inputs, it is labelled "calculation". Where I could not find a source, it is labelled "not verified".

Two structural facts that affect several assumptions:

- In the Dutch boiler market the installer buys the appliance (via a wholesaler such as Technische Unie, Rensa or Wasco) and resells it inside a total quote. The manufacturer does not pay the installer a commission; the installer earns a trade discount off list plus a mark-up. DNV for ACM (2023): "de aanschaf van een cv-ketel(combinatie) verloopt in de meeste gevallen via de installatiebedrijven ... Eindgebruikers hebben zelden of niet direct contact met de ketelfabrikanten." https://www.acm.nl/system/files/documents/openbare-versie-dnv-rapport-cv-ketel-marktonderzoek-2023.pdf (p. 5)
- Consumer purchase channel for a new combi boiler (Panteia for ACM, survey Aug-Sep 2025, n=439): local installer 36%, own energy supplier 23%, national provider (Warmgarant, Feenstra, Intergas) 19%, internet seller 9%, regional provider 7%, other 6%. The 2022-23 wave (n=418) had local installer 51%, regional 16%, energy companies 13%, internet 13%. The local installer share is falling; national fleets are growing. https://www.acm.nl/system/files/documents/rapport-panteia-2024-2025.pdf (section 3.4) and https://www.installatie.nl/nieuws/consument-koopt-ketel-vooral-lokaal/

---

## 1. Installer partner commission: 10% of boiler price per unit sold through the channel

**Model value:** 10% of the boiler price (EUR 853 on the Turbineketel, about EUR 1,380 on Combi+), paid on top of the installation fee the installer charges the homeowner.

**Evidence**

Netherlands, traditional trade discount:
- DNV/ACM 2023: "Ketelfabrikanten hebben aangegeven 20% korting op toestellen en onderdelen te verlenen aan installatiebedrijven, maar installateurs blijken deze korting vaak niet, of slechts in beperkte mate aan hun klanten door te geven." The report concerns 1,000 kW commercial boilers, but the statement about the manufacturer-to-installer discount is general. https://www.acm.nl/system/files/documents/openbare-versie-dnv-rapport-cv-ketel-marktonderzoek-2023.pdf (pp. 5, 9)
- Belgian trade forum (anecdotal, installers posting): 35-40% off list for larger installation firms, given as cascading discounts (for example -20% then -15%). https://www.bouwinfo.be/bouwforum/threads/percentage-korting-dat-sanitairman-krijgt-bij-aankoop.244271/

Netherlands, loyalty programmes (paid in points, on top of the trade margin):
- Vaillant "TEAM Vaillant" spaarprogramma: points per registered product via the vSCAN app, redeemable in a shop (example: 1,130 points for a flue-gas analyser). No euro value per point published. https://www.vaillant.nl/professioneel/
- Remeha spaarprogramma (MijnRemeha): points per registered boiler, redeemable for tools, outings or boilers; "na één of enkele registraties zijn veel items te bestellen". No euro value published. https://www.remeha.nl/zakelijk/mijn-remeha/hoe-werkt-het and https://touchincentive.com/cases/remeha/
- Intergas Xpert: free e-learning, certificates, marketing support, promotions. No cash reward published. https://intergasxpert.nl/

UK, loyalty programmes with published values:
- Baxi Works: 2,800 points per boiler registration; a promotion paid 6,250 points for 5 boilers and stated 6,250 points = GBP 187, so 1 point is about GBP 0.03 and a standard boiler registration is worth about GBP 84 (calculation). A 2023-24 cashback promotion paid GBP 300 per 3 qualifying boilers (GBP 100 per boiler). https://www.baxi.co.uk/professional/lp/get-started-get-rewarded, https://www.installeronline.co.uk/news/baxis-new-promotion-helps-installers-cover-the-cost-of-gas-safe-renewal/, https://www.cityplumbing.co.uk/content/baxi-cashback
- Worcester Bosch VAULT: GBP 50 of points for 1 install rising to GBP 700 for 15 installs (about GBP 47 per boiler). https://my.worcester-bosch.co.uk/professional/loyalty-signup, https://www.mrcentralheating.co.uk/blog/worcester-rewards-scheme
- Against a UK trade price of roughly GBP 800-1,200 for these boilers (not verified), loyalty rewards are worth about 4-10% of trade price, and they sit on top of the installer's normal margin.

Referral fees paid by direct-selling heat-pump brands:
- Quatt (Netherlands, sells and installs itself): non-installer referral partners earn "tot EUR 400" per completed installation on a product priced EUR 5,099 including installation, about 8% (calculation). Installer partners who buy and install Quatt themselves are promised "minimaal EUR 2.000 per geïnstalleerde warmtepomp" of margin, which includes the installation work. https://www.quatt.io/zakelijk/partner-programma, https://www.quatt.io/zakelijk/installatie-partner
- Octopus Energy (UK): installers earn GBP 75 per customer referred to an Octopus tariff; this is a tariff referral, not a product commission. https://octopus.energy/octopus-trusted-partners/

US HVAC cross-check:
- Distributor margin 15-25%; dealer equipment mark-up 25-50%. The dealer's income comes from mark-up, not from a manufacturer commission. https://www.acdirect.com/blog/why-hvac-contractors-double-equipment-price/, https://www.sharewillow.com/blog/hvac-profit-margins

**Verdict:** Supported as a number, with a structural caveat. 10% is below the 20-40% trade margin an installer earns when it buys and resells a boiler, but above the 4-10% that loyalty and referral schemes pay (Baxi about GBP 84-100 per boiler, Quatt EUR 400 per unit). In absolute euros, EUR 853 per Turbineketel is more than an installer typically earns on the appliance in a gas boiler job (20% of a EUR 1,200-1,500 trade price is EUR 240-300). The risk is not the percentage but the model: installers who are used to owning the customer and the quote may resist a referral role at any percentage. If Tarnoc later moves to installers buying and reselling, the discount has to be 20-30% off list.

**Suggested range:** 8-15% if Tarnoc keeps the customer contract and pays the installer a fee; 20-30% trade discount if the installer buys and resells. Keep the 10% for the base case but add a scenario at 20% for the years when installers carry most of the volume.

---

## 2. Units per installer partner per month of one new brand

**Model value:** capacity 8 units per month per partner; self-generated orders 1 per month in year 1 rising to 4 per month in year 4.

**Evidence**

Productivity of one installing technician:
- The Dutch certification-scheme cost estimate assumes one monteur installs 80 boilers per year (10 hours each) and services about 800 per year (1 hour each). That is 6-7 installs per month for a full-time installing monteur. https://www.installatie.nl/artikelen/wettelijke-erkenning-faqs/
- HeatTransformers (Dutch heat-pump installer): 200-300 heat pumps per month with 20-25 in-house installers plus partner installers, about 80 staff; this is roughly 10 units per in-house installer per month with partners taking part of the work (calculation). https://demakersvanmorgen.com/dankzij-digitale-verkoop-en-voorbereiding-bijna-100-akkoord-op-offertes/

Market volume and installer base:
- 2025: over 425,000 gas boilers and about 126,000 heat pumps sold in the Netherlands (of which over 40,000 hybrid). Boilers -7%, heat pumps +13% versus 2024. https://propertynl.com/Nieuws/Warmtepomp-blijft-fors-achter-bij-cv-ketel/0fbf308d-0e7b-4f3c-a7aa-96d35b6b8a60
- 2022: about 440,000 boilers; first half 2023: 160,000 versus 233,000 a year earlier (manufacturer figures). https://www.installatie.nl/nieuws/afzet-cv-ketels-maakt-duikvlucht/
- Heat pumps 2023 about 150,000, 2024 about 110,000 excluding air-to-air (hybrid about 40,000, all-electric about 70,000 of which about 50,000 new build). https://www.studium.nl/nieuws/verkooptrends-warmtepompen-2023-2025-nederland-residentieel/ CBS counts 393,000 in 2024 including air-to-air units. https://www.cbs.nl/nl-nl/maatwerk/2025/17/verkoopcijfers-warmtepompen-2022-2024
- Installation sector (all disciplines, citing Techniek Nederland and CBS): 53 firms over 250 staff, 639 firms with 25-250 staff, 7,553 firms under 25 staff, about 37,000 self-employed; 190,000 workers. https://installatie-shop.nl/blogs/nieuws/installatietechniek-statistieken-2025-complete-overzicht-van-de-nederlandse-branche
- Calculation: about 550,000 heating appliances per year across roughly 8,200 firms with staff gives an average of about 5-6 appliances per firm per month, but volume is concentrated: 42% of consumer boilers are bought from energy suppliers or national providers (Panteia 2025), so a typical local firm with a few monteurs installs perhaps 2-6 boilers per month and a mid-sized regional firm installs tens.

Share to one new brand:
- Intergas claims about 40% of the Dutch boiler market; most installers carry one or two preferred brands (dealer sites list Nefit, Intergas, Remeha, Vaillant as the standard set). https://stookcentrale.nl/cv-ketel-informatie/cv-ketel-kiezen/
- Weheat works with over 200 installation firms; Quatt reports 20,000+ installations in total; neither publishes per-installer volumes. https://www.weheat.nl/, https://www.quatt.io/zakelijk/installatie-partner
- No published data on how many units of a new brand an installer sells per month.

**Verdict:** Capacity of 8 per month is supported if the partner dedicates one full-time monteur to Tarnoc; it is high for a small local firm's share of one new brand. The self-generated ramp of 1 to 4 per month is plausible for an engaged mid-sized partner but looks high as an average across all partners, because the Turbineketel is a EUR 8.5-14k ticket that displaces a EUR 2-3k boiler job and needs a different sales conversation. Expect a skew: a minority of partners will do most of the volume.

**Suggested range:** capacity 4-8 per month (small firms 2-4, mid-sized 8-15). Self-generated: 0.5-1 per month in year 1, 2-3 per month by year 4 for the average partner; keep 4 for a top-partner case. Consider modelling two partner tiers.

---

## 3. Installer partners per channel manager: 18

**Model value:** 18 partner firms per partner manager.

**Evidence**

- Remeha Netherlands lists 8 regional residential account managers (2 per region in 4 regions) plus 1 national residential manager and a sales desk, for the whole Dutch installer base; separate teams of 5 (utility), 4 (housing corporations) and 1 (key accounts). https://www.remeha.nl/zakelijk/klantenservice/accountmanagers
- Nefit Bosch Netherlands lists 11 regional account managers for installers and wholesalers plus 1 sales manager. https://www.nefit-bosch.nl/professioneel/installateurs/contact/contactpersonen/
- Number of installer firms per brand is not published. With roughly 8,200 installation firms with staff and each big brand active in a large share of them, each incumbent account manager covers several hundred firms (calculation, not verified). Wholesalers handle ordering, stock and credit, so the manufacturer's account manager does relationship and promotion work only.
- US HVAC territory manager job description: visits assigned accounts and recruits new dealers within a 60-mile radius "on a weekly, bi-weekly, and/or monthly basis, depending on the size and/or potential of the account". No ratio published. https://growinghvac.com/job/territory-manager-2/
- Carrier has over 5,000 dealers, Trane about 3,500; territory-manager counts are not published. https://hvacmaintenancepro.com/equipment-guides/trane-carrier-lennox-hvac-comparison/
- Quatt assigns "een vaste contactpersoon" per installer partner and offers on-site support at the first installation. https://www.quatt.io/zakelijk/installatie-partner

**Verdict:** Looks low compared with incumbents (hundreds of firms per account manager) but is defensible for a launch phase where the manager recruits, trains, joins first installs and co-sells. The cost consequence is large: at 18 partners per manager and EUR 8,000 per month, each partner carries about EUR 5,300 per year of manager cost, which needs 6-7 units per partner per year just to cover at a 10% commission-equivalent.

**Suggested range:** 15-25 per manager in the first two years (onboarding mode); 40-80 once partners are active and a partner portal, wholesaler stock and a sales desk exist; incumbents run 200 or more. Model the ratio as rising over time rather than fixed.

---

## 4. Trainer throughput 40 new partners per year; EUR 3,500 training plus demo unit per partner

**Model values:** one installer trainer onboards 40 partners per year; each new partner costs EUR 3,500 including a demo unit.

**Evidence**

- Remeha: product trainings for installers are "kosteloos aangeboden", full-day sessions 09:00-15:00 at several training centres, EUR 50 per person charged only for late cancellation or no-show; e-learning first, then a practical workshop of about 2 hours (Skills E-cademy). https://www.remeha.nl/zakelijk/trainingen, https://www.remeha.nl/zakelijk/trainingen/skills-e-cademy
- Intergas Xpert: free online training with certificates plus on-location trainings and events. https://intergasxpert.nl/gratis-online-training
- Daikin Academy Netherlands: three training locations (Heerenveen, Breukelen, Capelle aan den IJssel), learning paths per product; prices are behind the My Daikin login. https://www.daikin.nl/nl_nl/daikin-academy.html
- Vaillant: training and certification via myVaillantPro; no prices public. https://www.vaillant.nl/professioneel/
- Quatt: monthly installation trainings at the Quatt Lab; on-site support at a partner's first installation. https://www.quatt.io/zakelijk/installatie-partner
- Aira Academy (Sheffield, UK): capacity to train 100 people per month; over 500 trained since May 2024 (about 30-40 per month realised); external courses from GBP 190 per person. https://www.installeronline.co.uk/green-energy/aira-opens-training-facilities-to-independent-installers/
- Panasonic UK paid installers GBP 500 in vouchers (one per company) for completing Level 3 heat-pump training and a first Aquarea install (2023), which shows manufacturers subsidise rather than charge for onboarding. https://phpionline.co.uk/news/panasonic-launches-training-reward-for-installers-switching-to-heat-pumps/
- No manufacturer publishes a cost per onboarded partner or a demo-unit policy.

**Verdict:** Trainer throughput of 40 per year looks low for classroom training (one group day of 8-10 people per month would do it in 4-5 days). It is realistic only if the trainer also supervises each partner's first one or two installations on site (1-2 days per partner), which is what Quatt does and what a novel appliance needs. The EUR 3,500 per partner is plausible for training time, travel and materials but does not cover a full demo unit at cost: if the Turbineketel's unit cost is EUR 4,000 or more, a free demo unit alone exceeds the budget. Check the model's unit cost against this line.

**Suggested range:** 40-80 partners per trainer per year (40 if first-install supervision is included, 80+ if classroom only). Cost EUR 1,500-2,500 per partner for training and first-install support, plus the demo unit at cost or as a loaner from a rotating pool of 5-10 units (a pool is cheaper than one unit per partner).

---

## 5. Direct sales rep quota: 20 boilers per month per fully productive rep

**Model value:** 20 closed sales per month per rep for EUR 8.5-14k systems sold to homeowners in an in-home or remote consultative sale.

**Evidence**

US HVAC comfort advisors (closest analogue: in-home replacement sale, USD 6-15k ticket):
- Close rates 35-45% of completed appointments industry average, 60-70% for top performers; a dedicated comfort advisor closes 50-65% where a service technician closes 25-35%. https://acquidex.com/intel/hvac/playbook, https://revenueify.today/industry-sales-training/hvac-sales-training/
- Compensation 5-10% of sold revenue (or 8-12% of gross profit) plus USD 45-60k base; fully loaded USD 85-140k per advisor. https://acquidex.com/intel/hvac/playbook
- Volume: the Acquidex playbook's worked example uses 4 leads per week; at 50-65% close that is about 8-10 systems per month for a full-time advisor (calculation). A commission-only job ad asks for a track record above USD 2M per year, which at USD 10-15k per ticket is 11-17 systems per month for a top rep (calculation). https://bebee.com/us/jobs/hvac-comfort-advisor-electrical-power-source-fresno-fresno-ca--theirstack-740313965

Residential solar (EUR 16k ticket, leads supplied, in-home sale):
- Year-1 reps 2-3 deals per month; years 2-3 4-6; year 5+ 5-8; top 10% 8-12 deals per month. Commission accelerators step at 6 and 9 sales per month. https://www.surgepv.com/blog/solar-sales-commission-guide
- Close rates on appointments sat: 10-20% new reps, 20-30% average, 30-45% top. https://www.grademyclose.com/blog/solar-sales-closing-rate-average

Netherlands:
- HeatTransformers: 70% conversion among customers who pay EUR 49 for advice, near 100% on issued quotes, after moving to a digital pre-qualification process (photos and data uploaded by the customer); 200-300 installs per month company-wide. Number of sales advisors not published. https://demakersvanmorgen.com/dankzij-digitale-verkoop-en-voorbereiding-bijna-100-akkoord-op-offertes/
- Dutch sustainability sales roles (solar, heat pumps, insulation): commission-based pay of EUR 3,750-10,000 per month depending on performance; appointments pre-set by an inside team; weekly targets. https://nl.indeed.com/q-sales-adviseur-duurzame-energie-vacatures.html, https://huisenverduurzaming.nl/vacatures

**Verdict:** Looks high. 20 closes per month is one close per working day. At a 35-45% close rate that requires 45-60 consultations per month, or 2-3 per working day including travel and follow-up, which is beyond what in-home HVAC and solar reps sustain (8-12 per month for good reps, 12-17 for the top decile). 20 is reachable only with remote video consultations, marketing-generated warm leads, a separate technical survey team, and a product that sells as a 1:1 boiler swap without a building survey.

**Suggested range:** 6-10 per month for an in-home consultative process; 10-15 with remote selling and a lead engine; 20 as a stretch case only. Also model a 6-9 month ramp to full productivity (the solar data show year-1 reps at a third of mature output).

---

## 6. Loaded employer cost: sales rep EUR 7,500 per month; partner manager EUR 8,000 per month

**Model values:** fully loaded monthly cost including employer taxes, car and expenses, Netherlands 2026.

**Evidence**

Employer on-costs:
- Loonbox 2026 worked example: EUR 3,500 gross becomes EUR 4,124 with holiday pay 8%, WW 2.74%, Zvw 6.10%, WIA/WGA about 1%, and EUR 4,430 with a 15% pension contribution, a factor of about 1.27. https://loonbox.nl/kennisbank/wat-kost-een-medewerker-2026/
- Other 2026 guides put mandatory on-costs at 20-35% and the all-in factor for a permanent employee around 1.38; including secondary benefits and overhead 140-160% of gross. https://www.job-planet.nl/hoe-hoog-zijn-de-werkgeverslasten-in-2026/, https://www.ondernemenmetpersoneel.nl/orienteren/personeelskosten/werkgeverslasten-berekenen-2026, https://www.deel.com/blog/employer-costs-for-an-employee-in-the-netherlands/

Salaries:
- Accountmanager warmtepompen (junior, via agency): EUR 2,500-3,500 gross per month. https://www.ymatch.nl/vacatures/accountmanager-warmtepompen/
- HVAC account managers in the best-paid segments (industrial cooling, data centres): EUR 70,000-120,000+ per year; heat pumps and sustainable HVAC described as strong-growth demand; total pay includes bonus and company car. https://voltys.nl/werken-in-de-hvac-sector-waar-verdien-je-het-meest-als-accountmanager-en-hoe-maak-je-discreet-de-volgende-stap
- Field sales representative, Netherlands average: about EUR 60,000 per year (ERI). https://www.erieri.com/salary/job/field-sales-representative/netherlands
- Sales representative, Amsterdam: about EUR 69,000 per year (Glassdoor). https://www.glassdoor.com/Salaries/amsterdam-sales-representative-salary-SRCH_IL.0,9_IM1112_KO10,30.htm
- Account manager median base EUR 81k and OTE EUR 131k (RepVue; skewed to tech). https://www.repvue.com/salaries/account-manager/NL
- Dutch sustainability field sales: EUR 3,750-10,000 per month on commission. https://nl.indeed.com/q-sales-adviseur-duurzame-energie-vacatures.html
- Company car: no public cost benchmark found; a mid-range business lease including fuel and insurance is typically EUR 700-1,000 per month (not verified).

Calculation:
- Sales rep: EUR 3,800 base + EUR 1,500 average commission = EUR 5,300 gross x 1.30 = EUR 6,900 + car EUR 800 + phone/laptop/expenses EUR 200 = about EUR 7,900 per month.
- Partner manager: EUR 5,000 base + EUR 800 bonus = EUR 5,800 x 1.30 = EUR 7,540 + car EUR 800 + expenses EUR 200 = about EUR 8,500 per month.

**Verdict:** Supported. Both figures are inside the plausible band; the partner manager figure is at the low end if Tarnoc hires people with heating-sector networks (incumbent account managers are on EUR 60-80k plus bonus and car).

**Suggested range:** sales rep EUR 6,500-9,000 per month loaded (commission-heavy plans push the top end up with volume); partner manager EUR 7,500-10,000 per month loaded.

---

## 7. Share of units sold direct vs via installers: base 80% direct in 2027 falling to 35% in 2030; aggressive 70% to 15%

**Model values:** as above.

**Evidence**

How the market buys today:
- Panteia/ACM 2025: local installer 36%, own energy supplier 23%, national provider 19%, internet 9%, regional 7%, other 6% (n=439). In 2022-23: local installer 51%. https://www.acm.nl/system/files/documents/rapport-panteia-2024-2025.pdf, https://www.installatie.nl/nieuws/consument-koopt-ketel-vooral-lokaal/
- DNV/ACM: purchases run through installers; end users rarely contact manufacturers. https://www.acm.nl/system/files/documents/openbare-versie-dnv-rapport-cv-ketel-marktonderzoek-2023.pdf
- UK academic estimate for gas-boiler distribution: 79% via contractor/installers who buy from merchants. https://wrap.warwick.ac.uk/97391

How new heating brands have split:
- Weheat (NL, founded 2020): sells only through 200+ installer firms; the consumer does a savings check online and is matched to an installer who quotes. Installer-led from day one. https://www.weheat.nl/
- Quatt (NL): direct-to-consumer sales and own installation ("product development, sales, and installation all in-house"); later added installer partners who buy direct and referral partners paid up to EUR 400; 20,000+ installations. The published material does not give the direct/partner split. https://blueearth.capital/news/blue-earth-capital-leads-e-25m-growth-funding-round-in-quatt-a-leader-in-smart-heat-pumps/, https://www.quatt.io/zakelijk/installatie-partner, https://www.quatt.io/zakelijk/partner-programma
- Aira (SE/DE/IT/UK): direct-to-consumer with own hubs; EUR 200M sales, 1,200 staff, 18 operational hubs, four training academies; in the UK it employs its own engineers and also trains independents. It has stayed direct. https://climatedrift.substack.com/p/can-aira-crack-europes-82b-heat-pump, https://www.theecoexperts.co.uk/heat-pumps/aira-review-best-heat-pump-installer, https://www.installeronline.co.uk/green-energy/aira-opens-training-facilities-to-independent-installers/
- Octopus Energy (UK): own sales and installation, with "Trusted Partners" (Heat Geek network, 2,000+ engineers on its platform) taking jobs Octopus cannot serve. https://octopus.energy/octopus-trusted-partners/
- HeatTransformers (NL): own sales, 20-25 in-house installers plus partner installers for coverage. https://demakersvanmorgen.com/dankzij-digitale-verkoop-en-voorbereiding-bijna-100-akkoord-op-offertes/
- Itho Daalderop: works through wholesalers and installers, including via the 50five platform. https://www.installatie.nl/nieuws/webshop-gaat-warmtepomp-verkopen/
- Tarnoc itself: first commercial unit installed June 2026 in Middelburg through a heritage adviser (Monumentencoach); about 50 systems pre-sold. https://www.installatie.nl/nieuws/tarnoc-turbineketel-hogetemperatuur-warmtepomp-zonder-buitenunit/

**Verdict:** No evidence found for the specific transition path. The two observed patterns are: (a) installer-led from day one (Weheat, Itho Daalderop, the incumbents), or (b) direct-led brands that stay mostly direct and add partners at the margin (Quatt, Aira, Octopus). No brand publicly reports going from 80% direct to 35% direct in three years. The base case is therefore a hybrid without a public precedent; that does not make it wrong, but the shift depends on the installer economics in assumption 1 and the ramp in assumption 2, and Quatt's experience suggests a direct brand keeps a large direct share for longer than the aggressive case assumes. The aggressive case (15% direct by 2030) is the incumbent model and would require installers to own the quote, which in turn needs a 20-30% trade margin, not 10%.

**Suggested range:** 2027: 70-90% direct. 2030: 40-60% direct in the base case; 20-35% only in a case where the commission is raised to a trade-discount level and partner count grows to several hundred. Tie the channel split to the number of active partners times units per partner (assumption 2) rather than setting it as an independent percentage.

---

## What I could not verify

- Euro value of Vaillant and Remeha loyalty points per registered boiler in the Netherlands (not published).
- Number of installer firms per brand (denominator for assumption 3).
- Training prices of Vaillant and Daikin academies in the Netherlands (behind partner logins).
- Company-car cost benchmark for 2026 (used EUR 700-1,000 per month as an assumption).
- Any brand's realised direct/partner unit split over time (Quatt, Aira and Octopus do not publish it).
- Web search quota ran out during this task; the remaining checks were done with direct page fetches. A follow-up with fresh search budget could target: Techniek Nederland or InstallQ counts of CO-certified firms; Worcester Bosch accredited-installer counts versus its area sales team; Dutch job ads with explicit closes-per-month targets.


---

# Tarnoc marketing-funnel assumptions: market evidence

Date: 2026-09-04. Prepared for the Tarnoc B.V. model (gas boiler EUR 8,526 ex VAT; hybrid boiler + heat pump about EUR 13,800 ex VAT; Netherlands; sales start 2027).

Method: web search (about 45 queries) plus direct reads of the cited pages. Where a figure comes from a vendor blog or a lead-gen agency, that is stated; those figures are indicative, not audited. Where I could not find evidence, I say so.

Two context points that affect every section:

- Dutch price anchor. Consumer sites quote a hybrid heat pump at EUR 4,500 to 7,000 installed (incl. VAT, before ISDE subsidy) and Quatt sells its hybrid from about EUR 2,699 after subsidy (Homedeal, https://www.homedeal.nl/warmtepomp/hybride-warmtepomp-kosten/; Duurzaam Ondernemen on Quatt, https://www.duurzaam-ondernemen.nl/forse-groei-voor-scale-up-quatt/). Tarnoc's hybrid at EUR 13,800 ex VAT (about EUR 16,700 incl. VAT) is 2 to 3 times the market anchor. That lowers conversion and raises cost per order compared with the benchmarks below, which come from cheaper products.
- Market direction. Dutch hybrid heat pump sales fell in 2024 and again in 2025 (45,000 to 43,000 units) after the hybrid mandate was dropped and the ISDE subsidy was cut; the 2026 forecast range is 21,000 to 74,000 (Dutch New Energy Research via Solar Magazine, https://solarmagazine.nl/nieuws-zonne-energie/i43515/trendrapport-verkoop-warmtepompen-stijgt-maar-onzekerheid-blijft-groot).

---

## 1. Cost per marketing lead: EUR 120

**Model value:** EUR 120 per homeowner enquiry, generated by Tarnoc's own performance marketing (so an exclusive lead).

**Evidence**

Netherlands and Belgium:
- Shared marketplace leads (Solvari, Bobex, Werkspot, Homedeal, Slimster): EUR 22 to 38 per lead (Yobuz comparison, Belgium/NL, https://www.yobuz.be/2026/03/27/solvari-vs-exclusieve-leads-vergelijking/) and EUR 40 to 80 per lead shared with about three installers (Warmtepomp-weetjes, https://warmtepomp-weetjes.nl/warmtepomp-leads-kopen/). Homedeal sends each request to 4 installers (https://www.homedeal.nl/warmtepomp/kosten-warmtepomp-installatie/).
- Exclusive leads bought from an agency: EUR 130 to 280 per lead (Yobuz, same source).
- Self-generated via Google Ads: one Dutch lead-gen site states CPCs of EUR 15 to 38 for construction/installation keywords and "EUR 140 or more for one usable lead" (Warmtepomp-weetjes, same URL; vendor claim). General Dutch CPC benchmarks put service trades at EUR 1.50 to 4 per click (Empowers, https://www.empowers.nl/blogs/google-ads/sea-cpc-benchmarks-per-branche-nederland); I found no published CPC for the exact keywords "warmtepomp" or "cv-ketel".
- Vivortis advertises exclusive heat pump leads "from EUR 5" with a 20-lead monthly minimum; no price list is public (https://vivortis.nl/warmtepomp-leads-kopen). Deklantenwerving, WarmeLeads and Homedeal do not publish installer prices.

Germany (heat pumps):
- EUR 40 to 350 per lead; shared portal about EUR 60, exclusive pre-qualified EUR 250+ (Anfragenfluss, https://anfragenfluss.de/neuigkeiten/waermepumpen-lead-kosten-2026).
- EUR 50 to 120 per lead typical; example of EUR 80 per lead (Leadfluss, https://www.leadfluss.de/blog/waermepumpen-leads-kaufen).
- Meta funnel campaign: EUR 49 per verified-phone lead, small sample (13 leads for EUR 640) (Marketingexperten, https://www.marketingexperten.de/blog/waermepumpen-leads-generieren).
- Enpal sells its surplus heat pump leads to installers in packs of 20/50/100; prices behind login (https://shop.enpal.pro/products/warmepumpen-leads).

US HVAC (replacement tickets USD 7,800 to 14,800, closest analogue for ticket size):
- Google Ads blended CPL USD 104, non-branded USD 149 (SearchLight, 816 contractors, Jan 2026, cited by WebFX, https://www.webfx.com/blog/home-services/hvac-marketing-benchmarks/). Industry average CPL USD 153 (same).
- Google Ads H1 2026: USD 190 to 335 per lead (99calls, https://99calls.com/blog/google-ads-lead-costs-hvac-2026).
- Local Services Ads USD 72 to 95 (WebFX) or USD 113 to 180 (RS Gonzales, https://rsgonzales.com/blog/hvac-cost-per-lead-benchmarks-2026/); high-intent search USD 30 to 90 (Contractor Magazine, https://www.contractormag.com/management/best-practices/article/55395612/mastering-lead-cost-benchmarks-for-plumbing-hvac-success).

Solar (proxy): exclusive purchased leads convert 8 to 15 percent at an effective CPA of USD 750 to 2,000, implying USD 100 to 200 per lead (SurgePV, https://www.surgepv.com/blog/solar-customer-acquisition-cost).

**Verdict:** Supported. EUR 120 sits in the middle of the exclusive-lead range in NL, DE and US HVAC.

**Suggested range:** EUR 90 to 180 for an exclusive, self-generated lead in 2027; EUR 25 to 80 if part of the volume comes from shared marketplaces (but those convert at 3 to 9 percent, see section 2). Expect CPL to rise, not fall, in a year when many competitors buy the same keywords (German solar CPCs reportedly rose about 45 percent in 2025; see section 3).

---

## 2. Funnel: 50 percent qualified, 40 percent qualified-to-won, 20 percent lead-to-order, about EUR 600 per marketing-won order

**Model value:** 20 percent of leads become orders; EUR 120 / 0.20 = EUR 600 marketing cost per order.

**Evidence on lead-to-order**

- Germany, heat pumps: shared portal lead 5 percent lead-to-order (EUR 1,200 per order); exclusive pre-qualified lead 20 percent (EUR 1,250 per order) (Anfragenfluss, https://anfragenfluss.de/neuigkeiten/waermepumpen-lead-kosten-2026). Leadfluss example: 2 orders from 10 leads at EUR 80 = 20 percent, EUR 400 per order (https://www.leadfluss.de/blog/waermepumpen-leads-kaufen). Both are lead-vendor figures.
- Belgium/NL, home improvement: 28 percent of shared leads have real purchase intent vs 78 percent of exclusive leads; solar shared 5.1 percent vs exclusive 58 percent of leads reached; cost per acquired customer EUR 412 (shared) vs EUR 349 (exclusive) (Yobuz, https://www.yobuz.be/2026/03/27/solvari-vs-exclusieve-leads-vergelijking/). Products are cheaper than Tarnoc's.
- Netherlands: "of ten quote requests an installer receives, seven are not serious" (Warmtepomp-weetjes, https://warmtepomp-weetjes.nl/warmtepomp-leads-kopen/), which matches a 30 percent qualified rate for shared leads.
- UK, Octopus Energy: over 200,000 heat pump enquiries in 2024 (https://octopus.energy/press/hot-property-200000-homeowners-eye-octopus-heat-pumps/) against about 18,000 installs in 2025 and roughly 22,000 cumulative by end 2024 (Axiom Eco Homes summary of Octopus and MCS data, https://axiomecohomes.co.uk/how-many-heat-pumps-have-octopus-installed/). Enquiry-to-install is therefore in the order of 5 to 10 percent, with a GBP 7,500 grant and a remote quote process. This is the best like-for-like data point for a remote-consultation, EUR 8k to 15k product.
- UK, installer survey: 45 percent of installers say customers do not proceed after a quote because prices are too high; 27 percent say the customer took a cheaper quote (Nesta, https://www.nesta.org.uk/report/how-to-install-more-heat-pumps-insights-from-a-survey-of-heating-engineers/). No overall quote-to-install rate is published.
- US HVAC: lead-to-job 25 to 40 percent for high-intent search leads (Contractor Magazine, URL above); in-home appointment close rates 25 percent (technician sells) to 60 to 70 percent (dedicated comfort advisor), 50 percent when financing is always offered vs 38 percent when not; LSA appointments close 31 to 40 percent, referral appointments 55 to 65 percent (ServiceTitan and ACHR survey figures summarised at https://www.servicetitan.com/blog/hvac-sales-process and https://pipelineon.com/blog/hvac-sales-process/). Web install leads book at 53 to 63 percent (Data-Driven Trades, small sample, https://thedatadriventrades.substack.com/p/how-do-install-leads-convert-on-hvac). Note these are replacement leads from homeowners whose system has failed, so intent is higher than for a discretionary hybrid upgrade.
- US solar (discretionary, USD 15k to 30k ticket): lead-to-sale 8 to 15 percent for Google Ads and exclusive leads, 5 to 12 percent for Meta, 3 to 5 percent shared leads, 29 to 37 percent referrals; effective CPA USD 1,000 to 3,000 for Google Ads (SurgePV, https://www.surgepv.com/blog/solar-customer-acquisition-cost). Sunrun sales and marketing cost per watt was USD 0.69 to 0.77 in 2019 to 2020, i.e. USD 5,000 to 6,000 per 8 kW system (pv magazine, https://www.pv-magazine.com/2020/02/28/sunrun-installs-record-capacity-in-q4-while-cutting-customer-acquisition-costs/). Enpal's CAC is reported above USD 5,000 in FY2025 (secondary source, not verified: https://yourgrowthpartner.io/blog/customer-acquisition-cost-benchmarks/).

**Verdict:** Looks high. A 20 percent lead-to-order rate is the top of the range reported by lead vendors for exclusive, phone-qualified heat pump leads, and roughly double the enquiry-to-install rate Octopus achieves with a grant and a market-level price. The 50 percent qualified rate is fine for exclusive leads; the 40 percent qualified-to-won rate needs a dedicated sales advisor and financing to be reachable for a product priced 2 to 3 times the market anchor. EUR 600 per marketing-won order is below every heating benchmark found (DE EUR 1,200 to 1,250; solar USD 1,000 to 3,000+); only US emergency-replacement HVAC and cheap Belgian home-improvement categories reach EUR 350 to 600.

**Suggested range:** lead-to-order 8 to 15 percent (qualified 45 to 55 percent, qualified-to-won 20 to 30 percent) for exclusive digital leads with a remote consultation; 3 to 6 percent for shared marketplace leads. Cost per marketing-won order EUR 900 to 1,800 in 2027 to 2028, improving toward EUR 700 to 1,200 as referrals and brand search grow. Use 20 percent only as an upside case.

---

## 3. Cost per lead falls 10 percent per doubling of installed base, from 250 units

**Model value:** learning-curve style decline in CPL driven by brand awareness and referrals, first step at 250 installed units.

**Evidence**

- Referral leads are cheaper and convert better: solar referral CPA USD 300 to 600 vs digital leads USD 800 to 1,500 and door-to-door USD 1,500 to 3,000 (VA Horizon summary of Wood Mackenzie data, https://www.vahorizon.site/solar/blog/solar-cac-statistics/); referral CPA USD 500 to 1,000 vs Google Ads USD 1,000 to 3,000, referrals convert 29 to 37 percent vs 8 to 15 percent for paid search (SurgePV, https://www.surgepv.com/blog/solar-customer-acquisition-cost). HVAC referral appointments close 55 to 65 percent vs 31 to 40 percent for paid LSA leads (Pipelineon/ServiceTitan, URLs in section 2).
- Referral yield: one vendor claims a satisfied solar customer produces 2 to 3 neighbour referrals over 12 months if the installer maintains contact, and that "doubling referral volume can cut acquisition costs by nearly 50 percent" (SurgePV, vendor claim, no data disclosed).
- Industry-level CAC did fall with scale for a while: US residential solar CAC fell about 10 percent from 2024 to 2025 to a five-year low of USD 0.60/W, but Wood Mackenzie forecasts a 40 percent rise to USD 0.84/W in 2026 as the market shrinks and competition for leads intensifies (https://www.woodmac.com/news/opinion/us-residential-solar-customer-acquisition-costs-set-to-spike-40-in-2026-before-gradual-decline/). Companies with a high share of referral and organic inbound are said to be insulated; those buying leads absorb the full increase (VA Horizon, URL above).
- Sunrun, the largest US residential solar company, reduced sales and marketing cost from USD 0.77/W to USD 0.69/W (about 10 percent) between Q2 2019 and Q4 2019 while growing volume; earlier in 2019 costs had risen year on year (pv magazine, https://www.pv-magazine.com/2020/02/28/sunrun-installs-record-capacity-in-q4-while-cutting-customer-acquisition-costs/; pv magazine USA, https://pv-magazine-usa.com/2019/08/07/everything-is-growing-at-sunrun-including-customer-acquisition-costs/). So scale did not guarantee falling CAC even for the market leader.
- Enpal (Germany, about 1,000 to 1,100 million EUR revenue) is reported to have seen CAC rise in 2025 as digital CPCs rose about 45 percent (secondary source, not verified: https://yourgrowthpartner.io/blog/customer-acquisition-cost-benchmarks/). Enpal spent EUR 19.7 million gross on TV alone in the first seven months of 2024 (DWDL/AEOS, https://www.dwdl.de/aeos/98977/solarunicorn_enpal_investiert_weiter_kraeftig_in_tvwerbung/), which shows the largest player still buys brand awareness rather than receiving it free.
- Quatt runs a friend-referral scheme (EUR 100 discount for the buyer, EUR 50 voucher for the referrer) and neighbourhood collective discounts up to EUR 500 (https://support.quatt.io/nl/articles/10319072-hoe-werkt-het-vriendenkorting-programma; https://www.quatt.io/waarom-quatt/hybride-warmtepomp/prijs-collectief). Quatt does not publish its referral share.
- I found no published study that links customer acquisition cost to installed base for heating products, and no company that discloses the share of heat pump orders coming from referrals.

**Verdict:** Direction supported, magnitude and mechanics not evidenced. Referrals are clearly the cheapest channel, and referral volume scales with installed base. But (a) the effect shows up as a rising share of low-cost referral orders in the blended CAC, not as a lower price for a paid lead; paid CPL is set by auction competition and can rise while the installed base grows (solar 2026, Enpal 2025). (b) Starting at 250 units is too early: 250 customers at a 10 to 20 percent annual referral rate yields 25 to 50 leads a year, which is not enough to move CPL. (c) A 10 percent per doubling curve from 250 to 60,000 units (about 8 doublings) cuts CPL by 57 percent, which no source supports for paid media.

**Suggested treatment:** keep paid CPL flat in real terms (or rising 0 to 5 percent a year) and add a referral channel: referral orders per year = installed base at start of year x 3 to 6 percent (conservative reading of "2 to 3 referrals per customer" with 10 to 15 percent of those converting), at a cost of EUR 150 to 300 per referred order (voucher plus handling). Blended CAC then falls by roughly 10 percent per doubling only once referrals reach 15 to 25 percent of orders, which happens at a few thousand installed units, not 250. If the single-curve approach must stay, start it at 2,000 to 5,000 units and floor the CPL at 60 percent of the starting value.

---

## 4. Marketing team: 2 marketers floor plus 1 per EUR 3 million of annual marketing spend

**Model value:** 2 FTE at low spend; 3 FTE at EUR 3 million; 4 FTE at EUR 6 million.

**Evidence**

- Team size by revenue band (cross-industry, 2026 survey compilation): median 3 marketers at USD 1 to 10 million revenue, 11 at USD 10 to 50 million, 26 at USD 50 to 250 million (Flint, https://www.flint.com/articles/marketing-team-headcount-revenue-ratio-statistics; Digital Applied, https://www.digitalapplied.com/blog/marketing-team-structure-2026-headcount-benchmarks).
- Labour share of the marketing budget: 35 to 40 percent of total marketing budget is in-house staff (Flint, same source); mid-market firms run about 70 percent of marketing spend in-house, 22 percent via agencies, 8 percent freelancers (CMO Council 2026 via Digital Applied, same URL). In D2C businesses that live on paid acquisition, performance marketing roles are 30 to 35 percent of marketing headcount (Digital Applied).
- Heating scale-ups do not publish marketing headcount. Quatt has about 300 to 350 staff, of which 70 employed and 50 freelance installers, at roughly 12,000 units a year (Installatie.nl, https://www.installatie.nl/techniek/warmtepompen/quatt-gaat-verder-dan-warmtepomp-ook-thuisbatterij-ems-en-overstap-naar-propaan/; MT/Sprout, https://mtsprout.nl/groei/quatt-levert-na-warmtepomp-nu-ook-thuisbatterij-en-energie-wij-bouwen-wat-we-cool-vinden). Thermondo has over 1,000 staff, 600+ tradespeople, at a few thousand heat pumps a year (https://www.thermondo.de/unternehmen/presse/pressemitteilungen/10000-installierte-waermepumpen-von-thermondo/). Aira has 1,200 staff at a EUR 200 million run-rate (Global Venturing, https://globalventuring.com/corporate/energy-and-natural-resources/the-big-deal-aira-home-series-b/). Non-installer overhead at these companies is in the hundreds; marketing plus sales is a material part of it, but no split is disclosed.
- Applied to the model: at EUR 3 million spend the model has 3 FTE, about EUR 250,000 to 300,000 loaded, or 9 to 10 percent of total marketing cost. Benchmarks put labour at 35 to 40 percent when content, brand, CRM and design are done in-house; a pure media-buying team with an agency can run at 10 to 15 percent labour plus an agency fee of 8 to 15 percent of media.

**Verdict:** Looks low if the team is meant to run creative, website, CRM, lead qualification and channel marketing to installers in-house; roughly right only if an agency fee (8 to 15 percent of media) is added elsewhere in the model and lead qualification sits in the sales cost line.

**Suggested range:** floor 2 to 3 FTE, plus 1 FTE per EUR 1 to 1.5 million of annual media spend (so 4 to 5 FTE at EUR 3 million, 6 to 8 at EUR 6 million), or keep the current headcount and add an agency/production line of 10 to 12 percent of media spend. Add a separate line for installer channel marketing (partner manager) once installers bring in half the orders.

---

## 5. Marketing spend as a share of revenue: about 1 to 3 percent, EUR 150 to 580 per unit

**Model value:** blended paid marketing at 1 to 3 percent of revenue, EUR 150 to 580 per unit sold once installers bring about half of orders.

**Evidence**

Manufacturers (selling through installers, so most demand generation is B2B and brand):
- NIBE Industrier 2024: selling expenses SEK 5,898 million on net sales SEK 40,521 million = 14.6 percent (2023: 12.9 percent); Climate Solutions is SEK 26,037 million of sales (NIBE year-end report 2024, https://www.nibegroup.com/download/18.19fa117e194a6feb97e332c/1739474819197/GB-Q4-24.pdf, income statement page). Selling expenses include the sales force and distribution, not only marketing.
- Lennox International 2024: SG&A USD 730.6 million on USD 5,341 million = 13.7 percent (10-K, https://www.sec.gov/Archives/edgar/data/1069202/000162828025004859/lii-20241231.htm).
- Vaillant, Viessmann, BDR Thermea (Remeha) are private and do not disclose marketing cost.

Direct-to-consumer heating and solar scale-ups:
- Enpal: EUR 19.7 million gross TV spend in January to July 2024 alone, on about EUR 890 million 2024 revenue; annualised TV alone is about 3.5 to 4 percent of revenue before digital, print and sales staff (DWDL/AEOS, https://www.dwdl.de/aeos/98977/solarunicorn_enpal_investiert_weiter_kraeftig_in_tvwerbung/; revenue from Enpal press release, https://www.corporate.enpal.com/pressemitteilungen/enpal-erzielt-2025-rekordumsatz-und-setzt-weiter-auf-starkes-wachstum). Enpal's adjusted EBITDA margin was 2.3 percent in 2023 (pv magazine, https://www.pv-magazine.de/2024/08/22/enpal-kann-umsatz-2023-mehr-als-verdoppeln-ebitda-dagegen-kaum-steigern/), consistent with heavy acquisition spend.
- 1KOMMA5 reported "higher selling expenses" as a drag on 2024 profit at EUR 520 million revenue; no percentage disclosed (Solarserver, https://www.solarserver.de/2025/02/17/1komma5-steigert-umsatz-2024-auf-520-millionen-euro/).
- Thermondo: EBITDA minus EUR 8.2 million on EUR 104 million revenue in 2022 during its heat pump build-up (https://www.thermondo.de/unternehmen/presse/pressemitteilungen/thermondo-teilt-Ergebnisse-aus-Befragung-und-Installations-Daten/thermondo-erzielt-3-Prozent-Marktanteil-im-Waermepumpen-Markt/).
- Residential solar: CAC "as high as 30 percent" of sale value, 15 percent for long-tail installers (Bodhi, https://www.bodhi.solar/blog/why-is-solar-customer-acquisition-cost-cac-so-high). Sunrun sales and marketing at USD 0.69/W is roughly 20 percent of a USD 3.3/W system (pv magazine, URL in section 3).
- Octopus Energy: GBP 75 million invested in its heat pump rollout including manufacturing and training; marketing not separated (https://octopus.energy/press/hot-property-200000-homeowners-eye-octopus-heat-pumps/).

Installers/contractors (the closest analogue to Tarnoc's D2C half):
- HVAC contractors spend about 6 percent of revenue on marketing and advertising on average (ACCA Contractor of the Future study, cited via https://servicelinepro.com/hvac-marketing-budget-2026/); recommended 5 to 10 percent, 10 to 15 percent in growth mode or when entering new markets (BDR, https://www.bdrco.com/blog/hvac-marketing-budget/; WebFX says "typically 7 percent", https://www.webfx.com/blog/home-services/hvac-marketing-benchmarks/).

Per unit: at 8 to 15 percent lead-to-order and EUR 90 to 180 CPL (section 2), marketing-won orders cost EUR 900 to 1,800 each. If half of orders come via installers at near-zero marketing cost, the blended figure is EUR 450 to 900 per unit, or 3 to 8 percent of a EUR 8.5k to 13.8k ticket.

**Verdict:** Looks low. 1 to 3 percent of revenue matches a mature manufacturer's advertising line, not a company that must generate half its own orders online in a launch phase. Every D2C heating or solar comparator found spends well above 5 percent of revenue on acquisition; manufacturers' selling expenses run 13 to 15 percent including sales staff.

**Suggested range:** 6 to 10 percent of revenue (EUR 700 to 1,200 per unit) in 2027 to 2028 while the brand is unknown; 3 to 5 percent (EUR 350 to 600 per unit) from 2029 onward if installers really bring half the orders and referrals reach 15 to 25 percent. If installers receive a discount or bonus for bringing customers, that is a channel cost and should be shown next to marketing, not netted away.

---

## 6. Volume sanity check: 2,200 (2027), 8,500 (2028), 16,700 (2029), 29,600 (2030), mostly hybrids

**Model value:** aggressive case, Netherlands only.

**Evidence: market size**

- Gas boilers (cv-ketels): 440,000 sold in 2022; H1 2023 down a third (Installatie.nl citing the boiler manufacturers, https://www.installatie.nl/nieuws/afzet-cv-ketels-maakt-duikvlucht/); about 425,000 in 2025, down 7 percent on 2024 (Vereniging Warmtepompen via Warmte365, https://www.warmte365.nl/nieuws/warmtepompmarkt-groeit-maar-blijft-ver-achter-bij-kabinetsdoel-2030-66A9B1AE.html). Historic run-rate 425,000 to 450,000 a year (2017 to 2021) (Installatie.nl, https://www.installatie.nl/nieuws/verkoop-cv-ketels-naar-recordhoogte/; Vastgoed Actueel, https://vastgoedactueel.nl/voor-het-eerst-minder-cv-ketels-verkocht/).
- Residential heat pumps excluding air-to-air: 126,000 (2022), 178,000 (2023), 125,000 (2024) (CBS via Vakblad Warmtepompen, https://www.vakbladwarmtepompen.nl/30142/verkoop-warmtepompen-in-2024-fors-gedaald); 136,000 in 2025, of which 86,000 all-electric and 43,000 hybrid; 2024 split 73,000 all-electric and 45,000 hybrid (Dutch New Energy Research Trendrapport 2026 via Solar Magazine, https://solarmagazine.nl/nieuws-zonne-energie/i43515/trendrapport-verkoop-warmtepompen-stijgt-maar-onzekerheid-blijft-groot). Hybrids sold 2022 to 2024 in total: 128,000 (CBS, https://www.cbs.nl/nl-nl/maatwerk/2025/17/verkoopcijfers-warmtepompen-2022-2024). Q1 2025 alone had 20,000 hybrids before the ISDE cut (Vereniging Warmtepompen, https://warmte-pompen.nl/verkoopcijfers-60-groei-verkoop-warmtepompen-begin-2025/), so annual volume is policy-sensitive.
- 2026 forecast: hybrids 21,000 to 74,000; all-electric 79,000 to 130,000 (DNE, same Solar Magazine URL).
- Combined boiler plus hybrid plus all-electric market: about 560,000 to 570,000 appliances a year. Installed base: about 800,000 heat pumps (Warmte365) and roughly 7 million gas-heated homes.

**Model volumes as market share (against 2025 volumes)**

| Year | Model units | Share of hybrid segment (43k) | Share of boiler + hybrid (468k) | Share of all heating appliances (about 565k) |
|---|---|---|---|---|
| 2027 | 2,200 | 5% | 0.5% | 0.4% |
| 2028 | 8,500 | 20% | 1.8% | 1.5% |
| 2029 | 16,700 | 39% | 3.6% | 3.0% |
| 2030 | 29,600 | 69% | 6.3% | 5.2% |

**Evidence: what fast entrants reached in 3 to 4 years**

- Quatt (NL, founded 2021, D2C hybrid, own installers, price about EUR 2,699 after subsidy): 3,000 installed by Sep 2023, about 4,500 in its first year of volume sales, 150 a week in 2023 to 2024, 15,000 installed and 1,000 a month by May 2025 (Duurzaam Ondernemen, https://www.duurzaam-ondernemen.nl/forse-groei-voor-scale-up-quatt/; EW Installatietechniek, https://www.ew-installatietechniek.nl/artikelen/quatt-verovert-op-gewiekste-wijze-de-warmtepompmarkt; Installatie.nl, URL in section 4). At 12,000 a year Quatt holds roughly a quarter to a third of the Dutch hybrid segment in its fourth year, and it now sells through installer partners as well. Its year-1 to year-4 path (about 4,500; 8,000 to 10,000; 12,000) is close to the model's 2027 to 2028 numbers, at a price one fifth of Tarnoc's.
- Octopus Energy (UK, started 2021 to 2022): 40,000 cumulative installs by end 2025, 18,000 in 2025, about 12 percent of MCS installs in England and Wales or 15 percent of grant-funded installs (Axiom Eco Homes summary, https://axiomecohomes.co.uk/how-many-heat-pumps-have-octopus-installed/; UK MCS total about 75,000 in 2025, https://ecosavinghub.co.uk/data/uk-heat-pump-statistics-2026/). Octopus is the country's largest energy retailer with millions of existing customers to market to.
- Thermondo (DE, heat pumps since June 2022): 3,000+ installed and 3 percent market share by December 2023; about 3,500 installs in 2023 vs a 10,000 plan; 10,000 cumulative by August 2025, "three-digit" weekly installs (Thermondo press releases, https://www.thermondo.de/unternehmen/presse/pressemitteilungen/thermondo-teilt-Ergebnisse-aus-Befragung-und-Installations-Daten/thermondo-erzielt-3-Prozent-Marktanteil-im-Waermepumpen-Markt/ and https://www.thermondo.de/unternehmen/presse/pressemitteilungen/10000-installierte-waermepumpen-von-thermondo/). German heat pump market: 299,000 units in 2025.
- Aira (SE/DE/IT/UK, commercial launch June 2023): EUR 200 million revenue run-rate, 1,200 staff, EUR 544 million raised; installation count not disclosed (Global Venturing, https://globalventuring.com/corporate/energy-and-natural-resources/the-big-deal-aira-home-series-b/). At EUR 12k to 15k per system that implies roughly 13,000 to 17,000 systems a year across four countries (my estimate).
- Enpal (DE): 31,000 PV systems and heat pumps commissioned in 2023 after 6 years of operation and about EUR 900 million revenue (pv magazine, URL in section 5).

**Verdict:** 2027 and 2028 are plausible for a well-funded D2C player (Quatt's first two years were similar, in a hybrid market that was then growing). 2029 and 2030 look high: 16,700 and 29,600 hybrids would be 39 to 69 percent of today's Dutch hybrid segment, and the best-funded new entrants found (Quatt, Octopus, Thermondo) reached 12 to 30 percent of their segment after four years with prices at or below market. The model's volumes are only reachable if (a) the hybrid segment returns to 70,000+ a year (top of the 2026 forecast range), or (b) the gas boiler line takes 3 to 5 percent of the 425,000-unit boiler replacement market, or (c) sales extend outside the Netherlands.

**Suggested range:** base case 1,000 to 2,000 (2027), 4,000 to 6,000 (2028), 7,000 to 10,000 (2029), 10,000 to 15,000 (2030), with hybrids capped at 20 to 30 percent of the forecast hybrid segment. Keep 29,600 as an aggressive case only with an explicit split showing how many are boilers (share of 425k) versus hybrids (share of 43k to 74k), and flag the dependence on ISDE subsidy and hybrid policy.

---

## Sources not obtained

- Google Ads CPC for the exact Dutch keywords "warmtepomp", "hybride warmtepomp", "cv-ketel vervangen": no public benchmark found; Keyword Planner would give this directly.
- Marketing headcount at Quatt, Aira, Octopus, Thermondo: not disclosed.
- Referral share of orders at any heat pump company: not disclosed.
- Vaillant, Viessmann, BDR Thermea marketing spend: private companies, not disclosed.
- Enpal CAC above USD 5,000: appears only in secondary CAC-benchmark blogs; not traceable to Enpal filings.


---

# Tarnoc after-sales assumptions: market evidence

Date: 2026-09-04. Prices below are per year. Dutch consumer prices are quoted as published (incl. 21% VAT) and converted to ex VAT where compared with the model. Web search budget ran out part-way; where a page could not be opened the source is marked "search snippet only".

Method note: Feenstra, Energiewacht and Techniek Nederland block automated page reads (HTTP 403). Feenstra figures come from third-party pages quoting Feenstra; Energiewacht figures from an older Consumentenbond survey; Techniek Nederland productivity norms were not found (wage tables are members-only).

---

## 1. Field engineer workload: 750 boilers per engineer, 3–4 visits per day

**Model value:** 750 contracted boilers per engineer; one annual service per boiler; 3–4 visits per working day plus breakdowns.

**Evidence**

- Time per maintenance visit, Netherlands: 45–60 minutes for a normal condensing boiler; longer for dirty or old units. Kiwa FAQ: https://www.kiwa.com/nl/nl/specials/veelgestelde-vragen-onderhoudscheck-gasinstallaties/ ; Spoedservice: https://spoedserviceduurzaamverwarmen.nl/hoe-lang-duurt-cv-ketel-onderhoud/ ; Feenstra (via De Margaretha guide) says the first inspection-plus-service visit averages one hour: https://demargaretha.nl/blog/post/68218/...
- Hybrid heat pump service: 45–60 minutes per visit (Alpha Ventilatie): https://alphaventilatie.nl/duurzaam-huis/hybride-warmtepomp/onderhoud/
- Dutch service technicians: "depending on complexity, 6–8 addresses per day" (search snippet only; page https://www.werkenbijsfi.nl/blog/wat-doet-een-servicemonteur-cv/ now returns 404). A Ymatch vacancy sets 1 boiler installation per day as the installer norm: https://www.ymatch.nl/vacatures/cv-monteur-service-onderhoud-ook-zzp/
- UK: a gas service engineer job advert states "8 to 10 services per day" (search snippet only; https://findajob.dwp.gov.uk/details/16426343 returned 503). UK annual service takes about 30–60 minutes and costs GBP 85–140: https://www.boilerguide.co.uk/gas-boiler/service
- British Gas / Centrica 2025: 2,939,000 Home Services customers (contract or on-demand) served by "over 6,000 Gas Safe registered engineers" (Uswitch) to about 7,000 engineers (Centrica 2023 annual report). That is roughly 420–490 customers per engineer, but HomeCare includes unlimited repair call-outs, plumbing, drains and electrics and the engineers also install boilers. UK Home Services operating margin 6.8% on GBP 114m profit implies about GBP 1.7bn revenue, about GBP 570 per customer. Sources: Centrica 2025 preliminary results PDF https://www.centrica.com/media/ixbk5mql/centrica-plc-2025-preliminary-results-announcement.pdf ; Uswitch https://www.uswitch.com/boilers/guides/british-gas-homecare/ ; Centrica AR 2023 https://www.centrica.com/investors/results-reports-and-presentations/annual-report-2023/
- US HVAC (residential, mixed repair and maintenance): industry average 3.8 completed calls per truck per day, top shops 5.2; "residential PM routes should hit 6–8"; general range 3–6 calls a day. https://www.atlasunchained.com/trades-contractors/close-calls-per-truck-gap/ ; https://hvacservicebellevue.com/resources/how-many-service-calls-does-hvacr-typically-do-a-day/ ; MarginPlug: healthy target 3–5 service calls per tech per day, 70%+ billable utilisation: https://www.marginplug.com/blog/hvac-revenue-per-technician-benchmark/
- Breakdown frequency (drives extra visits): Which? 2021 survey of 8,001 owners found about 3 in 10 annually-serviced boilers needed a repair in their first six years (about 5% a year); Fair Fix puts full breakdowns at about 0.5% of boilers a year. https://landlordknowledge.co.uk/english-households-spend-32m-annually-on-boiler-repairs/ ; https://smart-plan.com/blog/uk-boiler-repair-costs-statistics/ . Consumentenbond panel: a quarter of 10,000+ respondents had a three-way valve fail at some point on their current boiler: https://www.consumentenbond.nl/cv-ketel/cv-ketel-onderhoud
- Many Dutch contracts service every 2 years, not annually: Feenstra Basis, Eneco Basis and Extra, Essent (all every 24 months); Radar 2022 survey of 13,961 contract holders: 57% annual, 39% biennial, 3% less often. https://radar.avrotros.nl/artikel/duur-onderhoudscontract-voor-cv-is-niet-altijd-beter-52587
- Capacity arithmetic (my calculation, not a source): 38-hour week, 25 holidays plus about 13 ADV days, 5% sickness gives about 200 field days a year. At 5 jobs a day that is 1,000 jobs; at 3.5 jobs a day, 700 jobs. 750 annual services plus a 10–20% call-out rate (75–150 visits, higher than mature brands because the product is new) needs 825–900 visits, i.e. 4.1–4.5 visits per field day.

**Verdict:** Supported on the boilers-per-engineer ratio; the visits-per-day figure of 3–4 is low against market norms (NL 6–8 addresses, UK 8–10 services, US 3.8–5.2 mixed calls). The two assumptions are internally inconsistent: 3–4 visits a day over 200 field days only covers the annual services and leaves no capacity for breakdowns. Either raise visits per day to 4.5–5.5 or accept that 750 is the ceiling only once route density is high.

**Suggested range:** 600–900 boilers per engineer with annual servicing and a 10–20% call-out rate; 1,000–1,400 if servicing moves to every 2 years for newer units, as most Dutch providers do. Visits per field day: 3–4 in 2027–2028 while the installed base is thin and travel long, 5–6 at maturity. Hybrid systems count as roughly 1.3–1.5 boiler-equivalents (longer visit, more components).

---

## 2. Attach rate: 88% on a paid contract (34% basic, 54% premium)

**Model value:** 88% of installed units on a contract; of these 34% basic, 54% premium (share of installed base). In contract terms: 39% basic, 61% premium.

**Evidence**

- Panteia for ACM, 2025 (online panel, 948 respondents, of which 439 bought a new CW4 combi boiler in 2024–2025): 76% of new-boiler buyers have a maintenance contract, 22% do not, 2% do not know. Contract mix among 507 contract holders: basis 47%, comfort 26%, comfort plus 16%, all-in 9%, other/unknown 2%. Main reasons for no contract (n=170): still under warranty 30%, too expensive 16%, do it myself 14%, call when needed 10%, not arranged yet 10%. https://www.acm.nl/system/files/documents/openbare-versie-panteia-eindrapport-inzicht-in-de-kosten-voor-aanschaf-en-installatie-nieuwe-cv-combiketel.pdf
- Earlier Panteia/ACM wave (buyers in 2022–2023, 418 respondents): one in three boiler owners has no contract; mix 47% basic, 27% comfort, 11% comfort plus, 13% all-in (search snippet via installatie.nl): https://www.installatie.nl/nieuws/consument-koopt-ketel-vooral-lokaal/
- Radar (AVROTROS) March 2022, 13,961 contract holders: 45% have their contract with a local installer, 13% Feenstra, 10% Energiewacht, a few hundred each with Eneco and Essent. https://radar.avrotros.nl/artikel/duur-onderhoudscontract-voor-cv-is-niet-altijd-beter-52587
- NLE survey (about 1,000 homeowners): 7% have never had their boiler maintained; Onderzoeksraad 2015: 86% of households have regular or ad-hoc maintenance. https://www.installatie.nl/nieuws/430-000-ketels-nooit-onderhouden/
- UK context: Centrica's protection portfolio retention 87% (2025), and only about 7% of 600,000 free "membership" sign-ups converted to a paid protection contract. https://www.centrica.com/media/ixbk5mql/centrica-plc-2025-preliminary-results-announcement.pdf
- Manufacturers make the guarantee conditional on an annual service (Worcester Bosch: guarantee valid only if serviced annually by a certified engineer; Vaillant heat pump Cover & Care requires registration within 30 days). https://www.worcester-bosch.co.uk/guarantee-terms-and-conditions ; https://www.vaillant.co.uk/service/heat-pump-cover-care-packages/

**Verdict:** Looks high. The Dutch market ceiling for new-boiler buyers is about 76% on any contract, and the manufacturer or installer only captures the part sold at the point of sale. Two factors could push Tarnoc above market: it is the only party able to service a novel appliance, and it can make the warranty conditional on a service contract. The premium share (61% of contracts) is above the market's 51% (comfort + comfort plus + all-in) but the gap is small.

**Suggested range:** Base case 65–80% attach, stress case 55%, upside 85–90% only if the warranty is tied to the contract or the first year is bundled into the purchase price. Premium share of contracts 45–60%.

---

## 3. Contract prices

**Model value (ex VAT):** boiler basic EUR 60, premium EUR 90; hybrid basic EUR 150, premium EUR 200. Incl. 21% VAT: EUR 72.60 / 108.90 / 181.50 / 242.

**Evidence, boiler contracts (consumer prices incl. VAT, per year)**

| Provider | Tier | Price/yr | Service interval | Includes |
|---|---|---|---|---|
| Feenstra | Basis | EUR 96–101 (EUR 8.02–8.45/month) + one-off inspection EUR 50–75 | every 2 years | 24/7 breakdown line, call-out and labour at maintenance; labour and parts at breakdowns billed |
| Feenstra | Middenklasse | EUR 156 (12.98/month) | | + labour at breakdowns |
| Feenstra | All-in | EUR 163–240 (13.59–19.99/month) | | + parts |
| Eneco ServiceGemak | Basis | EUR 113 (9.44/month) | every 2 years | call-out, labour, parts at breakdown |
| Eneco | Extra | EUR 201 (16.78/month) | every 2 years | parts up to EUR 150/yr, EUR 300 off replacement |
| Eneco | Compleet | EUR 290 (24.14/month) | annual | parts up to EUR 500/yr |
| Essent | Budget | EUR 132 (11.00/month) | every 24 months | call-out, no labour at maintenance |
| Essent | Standaard | EUR 194 (16.19/month) | every 24 months | |
| Essent | Premium | EUR 254 (21.20/month), boilers under 5 years | every 24 months | parts up to EUR 275 per call |
| Breman | Basis / Comfort / All-in | from EUR 62 (5.20/month); yearly maintenance add-on +EUR 6.75/month (EUR 81/yr) | | maintenance materials to EUR 30; All-in parts to EUR 300; 24-month minimum |
| Energiewacht | Comfort | EUR 120–126 (older Consumentenbond survey) | 18–24 months | call-out and labour at breakdowns |
| Consumentenbond price survey (undated, Nuon-era so about 2018–2019), 103 contracts nationwide | | median EUR 101, mean EUR 104, range EUR 54–167 | mostly 12 months | mostly excl. parts |
| Panteia/ACM 2025, consumer-reported average | Basis / Comfort / Comfort plus / All-in / all | EUR 160 / 224 / 215 / 257 / 195 (2025 wave: 145 / 226 / 191 / 284 / 186) | | |
| Radar 2022, 13,961 contract holders | | 60% of annual payers pay EUR 60–110, 29% pay EUR 110–180; 41% of monthly payers pay EUR 10–15/month | | |
| Generic price guides 2026 | Basic / Service / All-in | EUR 50–90 / 70–130 / 130–200 (Homedeal); EUR 70–90 / 120–150 / 180–200 (Werkspot) | | |

Sources: https://demargaretha.nl/blog/post/68218/de-complete-gids-voor-feenstra-cv-ketel-onderhoudscontracten-technische-specificaties-voorwaarden-en-kostenanalyses/ ; https://www.eneco.nl/energieproducten/cv-onderhoud/ ; https://www.essent.nl/cv-ketels/onderhoud ; https://www.breman.nl/particulier/producten/service-en-onderhoud/ ; https://www.consumentenbond.nl/binaries/content/assets/cbhippowebsite/tests/cv-ketel/cv-ketel-onderhoud-prijspeiling.pdf ; Panteia/ACM PDF above ; https://radar.avrotros.nl/artikel/duur-onderhoudscontract-voor-cv-is-niet-altijd-beter-52587 ; https://www.homedeal.nl/cv-ketel/cv-ketel-onderhoud/ ; https://www.werkspot.nl/verwarming/prijzen-kosten/cv-ketel-onderhoud . Eneco raised its basic tariff from EUR 9.85 to 13.45/month in 2018 (Radar): https://radar.avrotros.nl/uitzendingen/gemist/item/eneco-verhoogt-tarieven-voor-onderhoud-aan-cv-ketels-niet-iedereen-blij/

Note: the big-brand "basis" tiers service every 2 years. An annual-service basic tier is worth more than Feenstra Basis.

**Evidence, hybrid heat pump contracts (incl. VAT, per year)**

| Provider | Price/yr | Interval | Includes |
|---|---|---|---|
| MDW Techniek | EUR 139.76 (11.65/month) | annual | maintenance labour and call-out; repairs EUR 127 first hour then EUR 91/hour; parts excluded |
| Holland Warmte | EUR 168.50 | every 2 years | breakdown call-out free; labour and parts billed outside warranty |
| Alpha Ventilatie | EUR 150 (12.50/month); one-off visit EUR 149 | annual | labour discounts, 24/7 line |
| Hoppenbrouwers | EUR 198 (HP only) / EUR 363 (HP + boiler) all-in | every 2 years | all parts and labour; 12-year term |
| Guides | EUR 150–300 (contract incl. boiler), EUR 180–280 (WattSlimmer) | | |
| UK Vaillant Cover & Care (heat pump) | GBP 295–312 (about EUR 345–365) | annual | service, breakdowns, parts, extended guarantee |
| UK British Gas HomeCare Basic (boiler) | from GBP 19–28/month (about EUR 265–390) | annual | unlimited repairs, parts |

Sources: https://mdwtechniek.nl/onderhoud/hybride-warmtepomp ; https://www.hollandwarmte.nl/shop/servicecontract/onderhoud-hybride-warmtepomp-servicecontract/ ; https://alphaventilatie.nl/duurzaam-huis/hybride-warmtepomp/onderhoud/ ; https://www.hoppenbrouwerstechniek.nl/particulier/service-abonnement-warmtepomp/ ; https://wattslimmer.nl/kennisbank/wat-kost-het-onderhoud-van-een-warmtepomp-per-jaar/ ; https://www.vaillant.co.uk/service/heat-pump-cover-care-packages/ ; https://selectra.co.uk/energy/providers/british-gas/homecare

**Verdict**

- Boiler basic EUR 60 ex VAT (EUR 73 incl.): looks low. It sits at the bottom of the Dutch market and below every national brand, while offering annual (not biennial) servicing. Panteia's consumer-reported basic average is EUR 160 incl. VAT.
- Boiler premium EUR 90 ex VAT (EUR 109 incl.): looks low. Market comfort/all-in tiers run EUR 156–290 incl. VAT.
- Hybrid basic EUR 150 ex VAT (EUR 182 incl.): supported, mid-market.
- Hybrid premium EUR 200 ex VAT (EUR 242 incl.): supported for a comfort tier; all-in with parts sells at EUR 300–365 incl. VAT.

**Suggested range (ex VAT):** boiler basic EUR 75–95 (annual service, call-out included), boiler premium EUR 130–190 (labour plus capped parts); hybrid basic EUR 140–180, hybrid premium EUR 220–300. A EUR 8,526 appliance buyer is unlikely to be price-sensitive at these levels; underpricing the contract gives away margin.

---

## 4. Contract direct cost (parts, consumables, travel; wages separate)

**Model value:** boiler EUR 30–40 per contract-year; hybrid EUR 75–100.

**Evidence**

- Providers' own parts caps signal expected exposure: Breman maintenance materials up to EUR 30; Eneco Extra parts up to EUR 150/yr and Compleet up to EUR 500/yr; Essent Premium up to EUR 275 per call; Dutch comfort-plus contracts cover parts up to EUR 275 per event (Panteia definitions). Sources as in section 3.
- Repair incidence: about 5% of annually serviced boilers need a repair each year in years 1–6 (Which? 2021, 3 in 10 over six years); 0.5% full breakdowns a year (Fair Fix). Sources in section 1.
- UK repair costs 2026 (Checkatrade via Smart Plan): average repair GBP 300 (range 120–750); diverter valve GBP 150–300, fan GBP 200–350, PCB GBP 250–450, heat exchanger GBP 350–500+; labour GBP 50–80/hour. https://smart-plan.com/blog/uk-boiler-repair-costs-statistics/
- Dutch labour rates for repair visits: MDW EUR 127 first hour, EUR 91/hour after (incl. VAT). https://mdwtechniek.nl/onderhoud/hybride-warmtepomp
- Travel: Dutch mileage reimbursement norm EUR 0.23/km (Ymatch vacancy). Own estimate: 750 visits x 25 km average = about 19,000 km a year; at a full vehicle cost of EUR 0.35–0.45/km that is EUR 6,600–8,500 per engineer, about EUR 9–11 per contract-year if the van is not already in the engineer's loaded cost.
- Manufacturer warranty spend as a proxy for early-life failure cost: Ariston Group accrued 1.4–1.6% of revenue (section 7). Applied to a EUR 8,526 boiler that is EUR 120–135 over the warranty period, or EUR 25–65 a year over a 2–5 year warranty, borne by the warranty line rather than the contract.

**Own build-up (per contract-year, ex VAT):**
- Boiler basic (labour and call-out only): consumables at service EUR 5–15, travel EUR 9–11, admin/scheduling EUR 3–5: EUR 17–31.
- Boiler premium (parts included): add 10–20% call-out incidence x EUR 100–200 average part = EUR 10–40: EUR 27–71.
- Hybrid: longer visit, refrigerant check, more expensive parts (fans, PCBs, sensors, compressor risk): basic EUR 30–50, all-in EUR 70–130.

**Verdict:** Boiler EUR 30–40 supported for a blended basic/premium mix once failure rates are at mature-brand levels; looks low for the premium tier in the first two years of a new product if parts are covered. Hybrid EUR 75–100 supported for a comfort tier, low for a true all-in.

**Suggested range:** boiler basic EUR 20–30, boiler premium EUR 40–70 (years 1–3), falling toward EUR 30–50 at maturity; hybrid basic EUR 35–50, hybrid premium EUR 80–130. If the model's engineer loaded cost already includes the van, remove the travel component (EUR 9–11).

---

## 5. Customer support staffing: 1 agent per 2,500 units, 1 escalation engineer per 15,000 units

**Model value:** as stated.

**Evidence**

- tado (smart thermostats, about 1 million homes, 5.5 million devices): about 10,000 support contacts per month off-peak and 11,000 per week in peak season, i.e. roughly 250,000–300,000 contacts a year, or 0.25–0.3 contacts per home per year, six languages. https://www.intercom.com/customers/tado-fin ; https://www.tado.com/en/press/tado-connects-over-5-5-million-smart-thermostats-and-reaches-profitability
- Ariston Group (boilers, heat pumps, water heaters; EUR 2.6bn revenue): "more than 300,000 incoming calls managed in its European call center in 2024", 96% answered, 17-second average wait. Installed base not disclosed. Ariston Group Annual Report 2024 (PDF fetched from ariston.com; section "B2C support through dedicated Call Centers").
- Centrica Home Services: complaints per UK customer 4.8% a year (2025). https://www.centrica.com/media/ixbk5mql/centrica-plc-2025-preliminary-results-announcement.pdf
- Agent throughput benchmarks: 300–500 tickets per agent per month for moderately complex asynchronous work, 200–350 for phone/chat; 20–30 phone calls per shift; 60–100+ emails a day; add 20–35% shrinkage. Customer-to-rep ratios: SaaS 1:250–500, technical support organisations 1:250, e-commerce 1:350–600 orders per month per rep. https://www.companysights.com/resources/what-is-the-right-customer-service-team-size-benchmarks-by-company-size-revenue-and-industry ; https://gigabpo.com/how-many-customer-service-reps-per-customer-do-you-need/ ; Jitbit (1,000 companies): 21 tickets per agent per day average https://www.jitbit.com/news/2266-average-customer-support-metrics-from-1000-companies/
- No published staffing ratio per installed unit for heating manufacturers or connected-home hardware companies was found.

**Own arithmetic:** 2,500 units x 1.5 contacts per unit per year (service booking, breakdown report, app or billing question) = 3,750 contacts a year = about 310 a month, inside the 200–500 per agent range. At 3 contacts per unit per year (manual scheduling, novel product, first heating season) the same agent carries 625 a month, which is too many for phone-heavy work. Escalation: a tier-2 to tier-1 ratio of 1:4 to 1:6 at one agent per 2,500 units gives one escalation engineer per 10,000–15,000 units.

**Verdict:** Supported at maturity if service scheduling is app-driven or automated; looks light for 2027–2029 when contact rates per unit are highest and volumes are too small to staff fractionally. The escalation ratio is consistent with normal tier-2 ratios but has no direct external benchmark.

**Suggested range:** 1 agent per 1,500–2,000 units in the first two years (minimum 2 agents for coverage), 1 per 2,500–3,500 at maturity with self-service. Escalation engineers 1 per 10,000–15,000 units, minimum 1 from launch.

---

## 6. Loaded employer cost 2026: engineer EUR 6,500/month, support agent EUR 4,800/month

**Model value:** as stated (assumed to be total employer cost per month, 12 months).

**Evidence**

- Gross pay, service engineer (cao Metaal & Techniek / Technisch Installatiebedrijf applies): starter group C about EUR 2,857, experienced group F EUR 3,480, senior group H EUR 4,041 per month (38-hour week, March 2026 tables). Cao increases: +3% 1 March 2026, +EUR 115/month 1 March 2027, one-off EUR 132 in November 2026. https://www.mijntechcarriere.nl/posts/servicemonteur/wat-verdient-een-servicemonteur ; https://salaristabel.nl/artikelen/cao-metaal-techniek-salaris-2026 ; https://www.maatt.nl/blog/nieuwe-cao-metaal-techniek-2026-2028-makkelijke-taal/
- Market data: Indeed average servicemonteur CV EUR 3,342/month (April 2026); Profield EUR 2,800–3,200 starters, 3,200–3,800 mid, 3,800–4,500 senior; Ymatch vacancy EUR 3,000–3,800 plus 8.33% holiday pay and EUR 0.23/km. https://nl.indeed.com/career/servicemonteur-cv/salaries ; https://www.profield.nl/blogs/hoeveel-verdient-een-servicemonteur-in-2026/ ; https://www.ymatch.nl/vacatures/cv-monteur-service-onderhoud-ook-zzp/
- Gross pay, customer service agent: junior EUR 2,500–2,900, medior 2,900–3,300, senior/specialist 3,300–3,800+; market averages EUR 2,935–3,148; technical/software support pays more. https://go-office.nl/kennisbank/carriere/salaris-medewerker-klantenservice/ ; https://nl.indeed.com/career/medewerker-klantenservice/salaries
- Employer on-costs 2026: holiday pay 8%; WW 2.74% (permanent) / 7.74% (flexible); Zvw 6.10%; WIA/Whk about 1%; total 120–135% of gross excluding pension, 130–145% including pension. Worked example: EUR 3,500 gross costs EUR 4,124 excl. pension, about EUR 4,430 incl. pension. https://loonbox.nl/kennisbank/wat-kost-een-medewerker-2026/
- PMT pension 2026 (mandatory for installation firms): 27.98% of salary above the EUR 19,172 franchise, employer share minimum 63.26% (17.70 points). https://www.salaris-informatie.nl/images/stories/premies/2026/pmt-feiten-en-cijfers_2026.pdf
- On-call (storingsdienst) and overtime: 0.78–1.12% of monthly salary per hour under the cao.

**Own build-up**

Engineer at EUR 3,600 gross: holiday pay EUR 288; social charges about 10% EUR 360; PMT employer share 17.7% x (3,600 x 12.96 / 12 − 1,598) about EUR 405; on-call and overtime allowances EUR 150–300; total wage cost about EUR 4,800–4,950. Van (lease, fuel, insurance, tools) EUR 800–1,000; phone, tablet, clothing, training EUR 150–250. All-in EUR 5,750–6,200.

Support agent at EUR 3,000 gross: holiday pay EUR 240; social charges EUR 300; pension EUR 300–330; total wage cost about EUR 3,850–3,900; workplace, software seats, telephony EUR 200–300; all-in EUR 4,050–4,200.

**Verdict:** Engineer EUR 6,500 supported if it includes van, tools and on-call pay (upper end; comfortable for a senior engineer or a tight labour market). Support agent EUR 4,800 looks high for a standard agent; it is right for a technical support specialist at EUR 3,500 gross.

**Suggested range:** engineer EUR 5,700–6,500 all-in including vehicle (EUR 4,700–5,300 without vehicle); support agent EUR 4,000–4,600 all-in; escalation engineer EUR 5,500–6,500.

---

## 7. Warranty: no separate reserve, BOM carries a 3% yield-and-warranty allowance

**Model value:** no warranty reserve; 3% of BOM covers yield loss and warranty.

**Evidence**

- Ariston Group (boilers, heat pumps, water heaters; closest listed comparator): warranty accruals charged to P&L EUR 36.9m in 2024 on EUR 2,632.7m revenue (1.40%), EUR 50.3m in 2023 on EUR 3,091.8m (1.63%). Warranty provision balance EUR 94.9m at end-2024 (3.6% of revenue), utilisation EUR 42.6m in 2024 (1.6% of revenue). Method: historical/statistical data on warranty work and units still under warranty. Ariston Group Annual Report 2024, Notes 1.5 and 3.3 (PDF fetched; https://www.aristongroup.com investors section).
- Daikin (FY ended 31 March 2025): provision for product warranties JPY 112,835m against net sales JPY 4,752,335m, a balance of 2.4% of one year's sales (multi-year cover; annual charge not disclosed). https://www.daikin.com/-/media/Project/Daikin/daikin_com/investor/financial/Financial-Data/Financial-Data-2025-pdf.pdf
- Warranty Week, 58 US HVAC and appliance manufacturers: HVAC claims 0.93% and accruals 1.10% of sales in 2025, 23-year averages 0.90% / 0.94%; appliances 1.27% / 1.29% in 2025, long-run 1.92% / 1.83%. https://www.warrantyweek.com/archive/ww20260625.html ; https://www.warrantyweek.com/archive/ww20180329.html
- NIBE: describes standard warranties, extended-warranty contracts up to six years and one-year service contracts, but the interim and year-end reports fetched do not disclose warranty provision amounts. https://www.nibegroup.com/download/18.19fa117e194a6feb97e332c/1739474819197/GB-Q4-24.pdf
- Vaillant, Viessmann (now Carrier), Bosch Home Comfort: no warranty-cost disclosure found. Vaillant is private and its German filings were not accessible; Bosch reports only at group level.
- Guarantee lengths in the market: Worcester Bosch 5–12 years, Viessmann up to 14 years on Vitodens when installed by accredited engineers; Vaillant heat pump packages extend guarantees to 5–10 years for GBP 295–312 a year. https://www.boxt.co.uk/boilers/guides/worcester-boiler-warranty ; https://www.vaillant.co.uk/service/heat-pump-cover-care-packages/
- Failure evidence for established brands: 3 in 10 serviced boilers need a repair within six years (Which? 2021, section 1).

**Verdict:** Looks low. Mature manufacturers spend 1.0–1.6% of revenue on warranty; Ariston, the closest comparator, ran 1.4–1.6% in 2023–2024 and holds a provision of 3.6% of revenue. A 3% allowance on BOM (if BOM is 40–50% of price) equals 1.2–1.5% of revenue and also has to absorb production yield loss, so the warranty share is below the mature-brand rate. A first-generation appliance from a new manufacturer with a multi-year guarantee should carry more, not less, than a mature brand.

**Suggested range:** separate warranty reserve of 2.5–4.0% of hardware revenue for the 2027–2029 cohorts, stepping down to 1.0–1.5% once field failure data exists. Keep the 3% BOM allowance for yield only, or split it explicitly. Model the balance-sheet provision at roughly 2–3 years of expected claims.

---

## Sources not obtainable

- Feenstra product pages (403); figures taken from third-party summaries dated 2025–2026.
- Energiewacht tariff lists 2024–2026 (403).
- Techniek Nederland cao tables and any productivity norm (members-only).
- UK job advert with "8–10 services per day" (503) and Dutch "6–8 addresses per day" (404): search snippets only.
- Vaillant, Viessmann, Bosch warranty disclosures: not published at segment level.


---

# Tarnoc: market evidence for manufacturing, supply-chain and working-capital assumptions

Date of research: 4 September 2026. Web search was capped mid-task (session budget reached), so some items rest on company reports pulled directly (NIBE, Ariston, Daikin, Bosch annual reports; EPA and IRENA PDFs) rather than on secondary searches. Items marked "not verified" are my own derivations or rules of thumb that I could not confirm with a source in this session.

Derived ratios below use: DSO = trade receivables / sales x 365; DIO = inventories / cost of sales x 365; DPO = trade payables / cost of sales x 365.

---

## 1. In-house assembly line

**Model value:** 1,000 units/month (12,000/yr) per line; EUR 2.5m capex per line + EUR 1.0m one-off tooling and automation (EUR 3.5m total, EUR 292 per unit of annual capacity); 12 months from payment to first production; 35 production operators per line (343 units per operator per year, about 4.8 labour-hours per unit at 1,650 hours/FTE); EUR 90,000/month facility and maintenance per line (EUR 1.08m/yr).

**Evidence**

Capex per unit of annual capacity, recent European heat-pump plants:

| Plant | Capex | Capacity (units/yr) | Capex per unit of capacity | Headcount | Units per employee per yr | Source |
|---|---|---|---|---|---|---|
| Vaillant, Senica (SK), greenfield | EUR 120m | 300,000 | EUR 400 | 600 | 500 | [Vaillant Group](https://www.vaillant-group.com/news-stories/vaillant-group-opens-mega-factory-for-heat-pumps.html), [Renewable Matter](https://www.renewablematter.eu/en/vaillant-heat-pumps-europe), [pv magazine](https://www.pv-magazine.com/2023/03/15/german-manufacturer-opens-heat-pump-factory-in-slovakia/) |
| Daikin, Ksawerow/Lodz (PL), greenfield | EUR 300m | 800,000 to 900,000 | EUR 330 to 375 | 1,000 (2025) to 3,000 (2030) | 280 to 850 | [Daikin press release](https://www.daikin.com/press/2022/20220708), [Daikin Europe](https://www.daikin.eu/en_us/press-releases/daikin-europe-invests-300-million-in-new-polish-heat-pump-heatin.html) |
| Aira, Wroclaw (PL), ex-Volvo site | EUR 300m | 500,000 | EUR 600 | up to 2,000 over a decade | 250 | [Aira](https://www.airahome.com/en-gb/news/aira-factory-poland), [Installer Online](https://www.installeronline.co.uk/news/aira-to-invest-e300-million-in-polish-heat-pump-production-site-to-manufacture-up-to-500000-heat-pumps-a-year/) |
| Bosch, Aveiro (PT), expansion | EUR 100m | 150,000 rising to 400,000 | EUR 250 to 670 | 300 new jobs | 500 to 1,300 | [Cooling Post](https://www.coolingpost.com/world-news/bosch-to-invest-100m-in-portuguese-heat-pump-factory/), [Portugal Connect](http://www.portugal-connect.com/2022/05/18/bosch-to-create-300-jobs-in-aveiro-heat-pump-factory/) |
| Bosch, Dobromierz (PL), greenfield | ~EUR 225m (PLN 1.2bn) | not disclosed | n/a | 500 by 2027 | n/a | [pv magazine](https://www.pv-magazine.com/2023/04/24/bosch-to-open-heat-pump-factory-in-poland/), [Invest in Wroclaw](https://invest-in-wroclaw.pl/powerful-investment-of-bosch-70-km-from-wroclaw-they-will-build-a-modern-heat-pump-factory) |
| Viessmann, Legnica (PL), 50,000 m2 | > EUR 200m | not disclosed | n/a | +150 on 1,500 existing | n/a | [pv magazine](https://www.pv-magazine.com/2022/07/15/viessmann-builds-heat-pump-factory-in-poland/) |
| Ideal Heating, Hull (UK), line inside existing site | GBP 12m (GBP 5.2m grant + GBP 6.8m own) | 115,000 by 2030 | ~GBP 105 (equipment only, building existed) | n/a | n/a | [Insider Media](https://www.insidermedia.com/news/national/ideal-heating-awarded-multimillion-pound-funding-set-to-boost-uk-heat-pump-production), [Hull & Humber Chamber](https://www.hull-humber-chamber.co.uk/articles/market-leader-ideal-heating-launches-first-uk-heat-pump-production-line-at-hull-site-as-part-of-60m-net-zero-drive) |
| Vaillant, Belper (UK), moved HP assembly into existing site | ~GBP 4m | not disclosed | n/a | 70, rising to 300 | n/a | [UK Parliament written evidence](https://committees.parliament.uk/writtenevidence/109872/pdf/) |

Line rates and staffing at Dutch/UK plants:

- Intergas, Coevorden: 5,500 boilers/week (about 285,000/yr) on 16 lines with 330 employees in total (2020), i.e. about 860 units per employee per year across all functions, or about 1.9 labour-hours per unit. The 2018 hall added 8 lines for a target of 500,000 units on 19 lines, i.e. roughly 26,000 units per line per year (2,200/month/line). The trade press notes that Dutch boiler production "is mainly assembly of parts". Sources: [Installatie.nl, how a boiler is made](https://www.installatie.nl/nieuws/zo-wordt-een-cv-ketel-gemaakt/), [Installatie.nl, Intergas expands](https://www.installatie.nl/nieuws/intergas-breidt-ketelproductie-uit/), [RTV Drenthe](https://www.rtvdrenthe.nl/nieuws/147883/ondernemen-in-drenthe-we-gaan-naar-een-productie-van-300000-cv-ketels-per-jaar-in-coevorden).
- Remeha, Apeldoorn (hybrid heat pump, Elga Ace): 50,000 units in 2023, capacity 140,000/yr from 2024, "a total production staff of 100 employees", building rented not owned. Announced 2022, production from 1 July 2023, opened 28 August 2023 (about 12 to 15 months). That is 1,400 units per production employee per year at capacity, about 1.2 labour-hours per unit. Sources: [Remeha](https://www.remeha.nl/actueel/remeha-opent-grootste-warmtepompfabriek-van-nederland), [Omroep Gelderland](https://www.gld.nl/nieuws/7997420/apeldoorn-heeft-nu-de-grootste-warmtepompfabriek-van-nederland), [Solar Magazine](https://solarmagazine.nl/nieuws-zonne-energie/i28346/remeha-komend-jaar-start-productie-hybride-warmtepomp-in-apeldoorn).
- Octopus Energy / RED, Craigavon (Cosy 6, R290 monobloc): one line produced about 600 units/month in mid-2025; a second line takes this to about 1,200/month; the factory is 30,000 sq ft (about 2,800 m2); the 2022 target of 1,000/month by end-2022 was missed by roughly two years. 100 new jobs were planned by 2024. Sources: [The Reengineer factory visit](https://www.thereengineer.pro/p/what-i-saw-at-octopuss-heat-pump), [Octopus press release](https://octopus.energy/press/octopus-energy-invests-in-northern-irish-heat-pump-experts-to-build-thousands-of-heat-pumps-a-month/), [Irish News](https://www.irishnews.com/business/2022/04/13/news/octopus-investment-in-craigavon-heat-pump-specialist-to-bring-100-green-jobs-2641398/).
- Nefit Bosch, Deventer: 180,000 boilers/yr (2011 data); production moved to Portugal from 2022. Source: [Installatie.nl](https://www.installatie.nl/nieuws/gasketel-verdwijnt-bij-nefit-deventer/).

Lead time from decision to production: Aira 12 months (acquired 2023, inaugurated June 2024, existing building); Remeha 12 to 15 months (rented building); Vaillant Senica and Bosch Dobromierz roughly 20 to 24 months (greenfield). Sources as above.

**Verdict**

- Capex EUR 292 per unit of capacity: **supported**. Sits inside the EUR 250 to 600 range of full plants, and above the ~GBP 105 of a line dropped into an existing building (Ideal). For a leased building with a single line, EUR 2.5m + EUR 1.0m is on the generous side, which is appropriate for a first line and a novel product.
- 1,000 units/month per line: **supported**. Octopus runs 600/month per line for a heat pump; Intergas runs roughly 1,500 to 2,200/month per boiler line.
- 12 months to first production: **supported** for a line in a leased building. Greenfield sites take 20 to 24 months. Octopus took about two years longer than announced to reach 1,000/month; a ramp curve after first production is needed.
- 35 operators per line (4.8 labour-hours per unit): **looks high** against Intergas (1.9 h/unit, all staff) and Remeha (1.2 h/unit, production staff), but the Turbineketel adds a turbine, generator, power electronics and balancing to a boiler, and a first line has no learning behind it. Reasonable as a year-one figure; should fall.
- EUR 90,000/month facility and maintenance: **looks high**. Floor area at comparable plants is 0.08 to 0.44 m2 per unit of annual capacity, so 12,000 units needs roughly 2,500 to 5,000 m2. Dutch industrial rent of EUR 60 to 100 per m2 per year (not verified this session) gives EUR 0.15 to 0.5m/yr; maintenance at 3 to 5% of EUR 3.5m capex adds EUR 0.1 to 0.18m; energy and services perhaps EUR 0.1m. Total EUR 0.4 to 0.8m/yr.

**Suggested range:** capex EUR 2.5 to 4.0m per 12,000-unit line all-in (supported as is); 12 to 15 months to first production plus a 6 to 9 month ramp to nameplate; 25 to 35 operators in year one falling to 18 to 25 once stable (2.5 to 3.5 h/unit); facility and maintenance EUR 40,000 to 75,000/month.

---

## 2. Assembly partner (contract manufacturer) capacity

**Model value:** contracted capacity 650 units/month (base) / 1,000 units/month (aggressive) at an external assembly partner, for a novel micro-turbine boiler.

**Evidence**

- Single-line output at small heat-pump plants: Octopus/RED 600/month on one line, 1,200/month on two ([The Reengineer](https://www.thereengineer.pro/p/what-i-saw-at-octopuss-heat-pump)). Boiler lines at Intergas: roughly 1,500 to 2,200/month per line ([Installatie.nl](https://www.installatie.nl/nieuws/zo-wordt-een-cv-ketel-gemaakt/)). So 650 to 1,000/month is one line's worth of work, not a stretch for a partner with an existing HVAC or box-build operation.
- Outsourced production is the norm for Dutch heat-pump start-ups: Quatt has its hybrid heat pump built by an Asian partner while keeping design and software in-house ([MT/Sprout](https://mtsprout.nl/impact/quatt-warmtepomp-hybride), [Duurzaaminvesteren](https://www.duurzaaminvesteren.nl/projecten/quatt-bv)).
- European EMS/box-build contract manufacturers (Zollner, GPV, Scanfil, Kitron, Neways, NOTE, Videoton and others) typically require 500 to 1,000-unit minimums for validation builds with 6 to 8 week lead times, and want "predictable capacity" from production-stage customers ([PCB and Assembly guide](https://pcbandassembly.com/blog/top-10-electronics-contract-manufacturers-for-european-oems/)).
- Contract structure: capacity reservation contracts ask the customer to pay a fee or non-refundable deposit before the manufacturer adds capacity; take-or-pay clauses set a minimum quarterly volume with a shortfall payment, sometimes with over/under carry-forward; typical initial terms run three years with annual renewal ([ScienceDirect, capacity reservation contracts](https://www.sciencedirect.com/science/article/abs/pii/S037722170500901X), [Law Insider, manufacturing capacity clauses](https://www.lawinsider.com/clause/manufacturing-capacity), [STR Holdings 8-K supply agreement](https://www.sec.gov/Archives/edgar/data/1473597/000117184319005127/f8k_080219.htm)).
- Ramp risk: Octopus announced 1,000/month by end-2022 and was at 600/month per line in mid-2025 ([Octopus press release](https://octopus.energy/press/octopus-energy-invests-in-northern-irish-heat-pump-experts-to-build-thousands-of-heat-pumps-a-month/), [The Reengineer](https://www.thereengineer.pro/p/what-i-saw-at-octopuss-heat-pump)).

**What I could not verify:** no public contract-manufacturing announcement for a micro-turbine boiler exists. Micro-turbine assembly needs high-speed rotor balancing, recuperator brazing and power-electronics test, which general HVAC or box-build partners do not normally have. The turbine module would likely come as a tested sub-assembly from a specialist (or from Tarnoc), with the partner doing boiler-level assembly and test.

**Verdict:** **supported as a line rate; looks high as a contracted commitment without a ramp.** Partners commit to capacity, not output: the customer typically carries a rolling 12-month forecast, a firm 3 to 6 month order window, a minimum volume with shortfall payment, and pays NRE (fixtures, test rigs, line set-up).

**Suggested range:** contracted nameplate 500 to 1,000/month is plausible; model actual output ramping from 100 to 200/month at start of production to nameplate over 6 to 12 months; include one-off NRE/tooling at the partner (EUR 0.3 to 1.0m, my estimate, not verified) and a take-or-pay minimum of 60 to 80% of contracted volume.

---

## 3. BOM cost-down with volume

**Model value:** EUR 9,984 per boiler below 5,000 units/yr; EUR 7,069 from 5,000 (minus 29%); EUR 4,998 from 10,000 (minus 50% versus tier 1, minus 29% versus tier 2), possibly on a two-year volume commitment.

**Evidence**

Learning rates (cost reduction per doubling of cumulative output):

- Heat pumps: review of historic trends finds equipment-cost learning rates in the 3 to 10% range for the UK to 2035, 18 to 26% for ground-source heat pumps in Switzerland and the Netherlands, a negative rate (minus 3.3%) for installed cost in Great Britain, and a high case of 30% to 2050 for installed cost globally. EHPA modelling gives about 39% cost reduction by 2030 as cumulative sales double ([Applied Energy 2024, "Reducing heat pump installed costs"](https://www.sciencedirect.com/science/article/pii/S0306261924013977); page returned 403 on direct fetch, figures taken from the search abstract).
- UKERC: equipment cost of air-source heat pumps expected to fall 17% by 2030, installation cost 31%, total 20% ([pv magazine](https://www.pv-magazine.com/2023/04/21/installed-heat-pump-costs-to-fall-by-20-by-2030-says-uk-research-institute/)).
- IEA: a vertically integrated, high-volume manufacturing base (China) produces heat pumps at 35 to 50% lower levelised cost than other regions; this is the gap between hundreds of thousands and millions of units, not between 5,000 and 10,000 ([IEA Heat Pump Monitor 2026](https://www.iea.org/reports/heat-pump-monitor-2026/key-findings)).
- General manufacturing: Wright's original aircraft figure is 15% per doubling; solar PV about 20% ([Our World in Data](https://ourworldindata.org/learning-curve)). Learning rates are an empirical tendency that weakens when input costs dominate ([Construction Physics](https://www.construction-physics.com/p/how-accurate-are-learning-curves)).
- Cost structure: raw materials and purchased parts are 70 to 80% of operating cost in a heat-pump plant ([IMARC plant report](https://www.imarcgroup.com/heat-pump-manufacturing-plant-project-report)). Purchased-part prices respond to order volume and tooling amortisation, not only to learning.

Micro-turbines specifically:

- US EPA CHP catalogue: micro-turbine equipment cost falls with unit size, from USD 2,690/kW at 30 kW to USD 1,710/kW at 1,000 kW; a 100% increase in size gives about an 80% increase in capital cost. This is scale in size, not volume; there is no public volume learning curve for micro-turbines ([EPA Catalog of CHP Technologies, micro-turbines](https://www.epa.gov/sites/default/files/2015-07/documents/catalog_of_chp_technologies_section_5._characterization_-_microturbines.pdf)).
- Capstone's late-1990s target of about USD 500/kW installed for a 30 kW unit, and the DOE Advanced Microturbine programme goal of under USD 500/kW, were not reached; micro-turbines remained roughly double the cost of reciprocating engines ([Gas Turbine World](https://gasturbineworld.co.uk/capstone-microturbine/), [EPA catalogue](https://www.epa.gov/sites/default/files/2015-07/documents/catalog_of_chp_technologies_section_5._characterization_-_microturbines.pdf)). Turbine wheels, recuperators and high-speed generators are the cost-stubborn parts.

Arithmetic check: if cumulative output is about 3,000 units when tier 1 pricing applies and about 30,000 when tier 3 is reached, that is about 3.3 doublings. A 50% total cut requires a learning rate of about 19% per doubling; a 15% rate gives about 41%; a 10% rate gives about 29%. A one-step 29% cut between the 5,000 and 10,000 tiers (one doubling of the annual run rate) is far above any observed heat-pump learning rate; it can only come from supplier price breaks and design changes landing at the same time.

**Verdict:** **looks high.** A 29% cut from tier 1 to tier 2 is defensible as the prototype-to-production step (tooling amortised, quotes moving from hundreds to thousands of pieces). The further 29% from 5,000 to 10,000 per year is not supported by observed rates; 50% in total needs a design-for-manufacture redesign alongside volume, and the turbine module will fall more slowly than the boiler parts.

**Suggested range:** tier 2 at EUR 7,000 to 7,500 (supported); tier 3 at EUR 5,800 to 6,800 (minus 32 to 42% versus tier 1) as base; EUR 5,000 only as an upside case tied to a redesign. Apply tier prices with a lag of one to two quarters after the volume is reached, and keep the turbine sub-assembly on a flatter curve (minus 20 to 30% total) than sheet metal, heat exchanger and controls.

---

## 4. Supply-chain, logistics and order-desk staffing

**Model value:** supply chain and logistics 1 FTE per 900 units/yr; order desk 1 FTE per 3,000 units/yr. At 12,000 units that is about 13 + 4 = 17 FTE, plus 35 operators, so about 230 units per FTE in operations.

**Evidence**

- Intergas: 330 employees for about 285,000 units/yr across all functions including R&D and sales, about 860 units per employee ([Installatie.nl](https://www.installatie.nl/nieuws/zo-wordt-een-cv-ketel-gemaakt/)).
- Vaillant Senica: 600 employees for 300,000 units, 500 per employee, in a plant that includes a logistics hub ([Renewable Matter](https://www.renewablematter.eu/en/vaillant-heat-pumps-europe)).
- Aira Wroclaw: up to 2,000 jobs for 500,000 units, 250 per employee at full headcount ([Aira](https://www.airahome.com/en-gb/news/aira-factory-poland)).
- Daikin Ksawerow: 1,000 jobs (2025) to 3,000 (2030) for 800,000 to 900,000 units, 280 to 850 per employee ([Daikin](https://www.daikin.eu/en_us/press-releases/daikin-europe-invests-300-million-in-new-polish-heat-pump-heatin.html)).
- Remeha Apeldoorn: 100 production staff for 140,000 units; supply chain is shared with the boiler plant and not disclosed separately ([Remeha](https://www.remeha.nl/actueel/remeha-opent-grootste-warmtepompfabriek-van-nederland)).
- Octopus/RED: about 100 new jobs for 7,000 to 14,000 units/yr, roughly 100 to 150 per employee, the closest analogue to a start-up scale ([Irish News](https://www.irishnews.com/business/2022/04/13/news/octopus-investment-in-craigavon-heat-pump-specialist-to-bring-100-green-jobs-2641398/)).

No source splits supply-chain headcount from the rest. The comparison is therefore total plant headcount per unit.

**Verdict:** **looks high against mature plants, in line with start-up scale.** Tarnoc's all-in operations figure (about 230 units per FTE at 12,000 units) sits between Octopus (100 to 150) and Aira/Daikin at full headcount (250 to 850). With an assembly partner doing production, 1 per 900 for supply chain alone is generous but covers supplier development for a new product, which is heavier than steady-state buying. Order desk at 1 per 3,000 is consistent with mature ratios.

**Suggested range:** supply chain and logistics: a fixed core of 3 to 4 FTE, then 1 FTE per 1,500 to 2,500 units/yr above about 3,000 units (equivalent to 1 per 900 at low volume, thinning as volume grows). Order desk: 1 per 2,500 to 4,000 units (supported).

---

## 5. Working capital

**Model value:** DSO 20 days; DPO 45 days; DIO 0 days (base) / 30 days (aggressive).

**Evidence** (derived from company reports; figures as published)

| Company, year | Sales | Trade receivables | Inventories | Trade payables | Cost of sales | DSO | DIO | DPO | Source |
|---|---|---|---|---|---|---|---|---|---|
| NIBE Industrier, 2024 (SEK m) | 40,521 | 5,424 | 10,644 | 3,115 | 29,547 | 49 | 131 | 38 | [NIBE Annual Report 2024](https://www.nibegroup.com/download/18.763f7ff195ce49f6161f70/1744610041919/GB-NIBE-AR-2024-W.pdf), pp. 120 and balance-sheet notes |
| NIBE, 2025 (SEK m) | 40,841 | n/a (current receivables 7,026) | 9,167 | n/a | 27,976 | ~50 to 63 | 120 | n/a | [NIBE Year-end report 2025](https://www.nibegroup.com/download/18.7a7a546d19c4da3cab34/1770881343351/12-2-GB-Q4-25.pdf) |
| Ariston Group, 2025 (EUR m) | 2,707 | 351.5 | 511.0 | 544.0 | not shown by function | 45.4 (reported) | inventories 18.9% of revenue, about 69 days of revenue (roughly 95 to 100 days on cost, my estimate) | 90.0 (reported) | [Ariston Annual Report 2025](https://www.aristongroup.com/content/dam/aristongroup/downloads/corporate-publications/Ariston%20Group_Annual%20Report%202025.pdf), operating working capital section |
| Daikin Industries, FY to March 2025 (JPY m) | 4,752,335 | 856,542 | 1,052,868 | 362,159 | 3,125,647 | 66 | 123 | 42 | [Daikin Financial Data 2025](https://www.daikin.com/-/media/Project/Daikin/daikin_com/investor/financial/Financial-Data/Financial-Data-2025-pdf.pdf?rev=-1&hash=FA0DE32DB9B2578220FAB45E6877C819) |
| Bosch Group (all sectors), 2025 (EUR m) | 90,969 | 17,964 | 15,887 | 13,164 | 63,307 | 72 | 92 | 76 | [Bosch Annual Report 2025](https://assets.bosch.com/media/global/bosch_group/our_figures/pdf/bosch-annual-report-2025.pdf) |
| Vaillant GmbH, 2023 | not verifiable: the Bundesanzeiger filing is a scanned PDF without a text layer ([lobbyregister PDF](https://www.lobbyregister.bundestag.de/media/1d/d8/616447/EA_Vaillant-GmbH_31-12-2023-Bilanz-GuV-und-Anhang-komprimiert.pdf)) | | | | | | | | |

Bosch Home Comfort does not publish a separate balance sheet; the Bosch figure is group-wide. NIBE's 2025 report notes "focused efforts to reduce high inventory levels continued" and that distributor inventories of heat pumps were being run down, so 2023 to 2025 DIO is above NIBE's normal level.

Start-up context: Quatt takes a EUR 99 deposit and "fully pre-finances the heat pump, installation materials and installation" until the installation is done ([MT/Sprout](https://mtsprout.nl/impact/quatt-warmtepomp-hybride)), which means the start-up, not the customer, carries the receivable and the inventory until commissioning.

**Verdict**

- DSO 20: **looks low.** Every HVAC maker in the table is at 45 to 72 days because they sell through wholesalers and installers on trade terms. 20 days is only reachable if end customers pay on or before delivery (deposit plus balance on commissioning) and installers are paid by Tarnoc rather than buying the unit.
- DPO 45: **supported.** Range across peers is 38 to 90 days; an assembly partner will want 30 to 45 days from a start-up, component suppliers 30 to 60.
- DIO 0 (base): **no evidence found for any HVAC maker below about 90 days; looks low.** Even with the partner holding work-in-progress, Tarnoc owns finished units between the partner and the customer, service spares, and imported outdoor units that spend 5 to 8 weeks at sea (Asia to Rotterdam) and need safety stock. 30 days (aggressive case) is already the lean end.

**Suggested range:** DSO 30 to 45 days if selling via installers/wholesalers; 10 to 20 only under a consumer-prepay model. DPO 45 to 60. DIO 20 to 45 days in the base case (pipeline stock for imported outdoor units alone is 30 to 60 days of that product's cost), 60 to 90 once Tarnoc runs its own line and holds component stock.

---

## 6. Depreciation life: 8 years straight line for assembly lines and tooling

**Model value:** 8 years straight line for both the line and the tooling/automation.

**Evidence**

- Bosch: plant and equipment 8 to 11 years; other equipment, fixtures and furniture 3 to 25 years; buildings 10 to 50 years ([Bosch Annual Report 2025](https://assets.bosch.com/media/global/bosch_group/our_figures/pdf/bosch-annual-report-2025.pdf), note on property, plant and equipment, table T37).
- NIBE: machinery and equipment depreciated at 10 to 33% per year (3 to 10 years); buildings 2 to 7%; capitalised development 4 to 6 years ([NIBE Annual Report 2024](https://www.nibegroup.com/download/18.763f7ff195ce49f6161f70/1744610041919/GB-NIBE-AR-2024-W.pdf), p. 153).
- Ariston: plant and machinery 6.0 to 15.5% per year (about 6.5 to 17 years); industrial and commercial equipment 10 to 25% (4 to 10 years); buildings 1.8 to 3% ([Ariston Annual Report 2025](https://www.aristongroup.com/content/dam/aristongroup/downloads/corporate-publications/Ariston%20Group_Annual%20Report%202025.pdf), accounting policies).
- Daikin: machinery and equipment 5 to 15 years; buildings 15 to 50 years ([Daikin Financial Data 2025](https://www.daikin.com/-/media/Project/Daikin/daikin_com/investor/financial/Financial-Data/Financial-Data-2025-pdf.pdf?rev=-1&hash=FA0DE32DB9B2578220FAB45E6877C819), note 2h).

**Verdict:** **supported for the assembly line** (all four peers include 8 years in their machinery range). **Looks long for product-specific tooling and automation**, which peers put at 3 to 10 years and which becomes obsolete when the product design changes.

**Suggested range:** line equipment 8 to 10 years; tooling, fixtures and test rigs specific to the Turbineketel 3 to 5 years; leasehold improvements over the lease term.

---

## 7. Inbound shipping: EUR 100 per outdoor heat-pump unit

**Model value:** EUR 100 per outdoor unit (client's figure), for a 50 to 100 kg unit delivered into the Netherlands.

**Evidence**

- Drewry World Container Index, 3 September 2026: Shanghai to Rotterdam USD 4,092 per 40 ft container (down 5% on the week); composite USD 4,465 ([Drewry WCI](https://www.drewry.co.uk/supply-chain-advisors/supply-chain-expertise/world-container-index-assessed-by-drewry)). Rates exclude origin and destination terminal handling.
- Add-ons: terminal handling EUR 100 to 300 per container; bunker adjustment 10 to 20% of base; insurance 1 to 2% of cargo value; European full-truckload haulage EUR 1.0 to 1.5 per km; LCL "can double costs for partial loads" ([FreightAmigo 2026 cost guide](https://www.freightamigo.com/en/blog/logistics/container-shipping-cost-calculator-free-tool-for-sea-and-road-rates-in-2026/)).

Derivation (my arithmetic, not from a source): a monobloc outdoor unit of 50 to 100 kg ships in a carton of roughly 0.5 to 0.7 m3, so a 40 ft high-cube (about 60 m3 usable) holds 85 to 120 units, well under the weight limit. Ocean freight is then USD 34 to 48 (EUR 31 to 44) per unit at today's spot rate. Terminal handling, customs brokerage and a 100 to 200 km truck leg to a Dutch warehouse add roughly EUR 600 to 1,200 per container, EUR 5 to 15 per unit. Full-container total: about EUR 40 to 60 per unit. LCL or part loads: EUR 80 to 120. Import duty and VAT are not freight and are excluded. If the outdoor unit is sourced in Europe and moves by road, one unit per pallet in groupage inside NL/DE/PL is typically EUR 40 to 90 per pallet (my estimate; the pallet-rate search was not available this session).

**Verdict:** **supported, at the conservative end.** EUR 100 covers full-container sea freight from Asia with a margin for rate spikes (the Red Sea surcharge period pushed Asia to Europe rates to about USD 7,000 to 8,000 per 40 ft in 2024) and covers European road groupage.

**Suggested range:** EUR 45 to 65 per unit for full-container sea freight at 2026 rates; EUR 80 to 120 for LCL or small road consignments; keep EUR 100 as a prudent planning figure.

---

## 8. Loaded employer cost, Netherlands 2026: EUR 5,000/month for operators and supply-chain staff

**Model value:** EUR 5,000 per month (EUR 60,000 per year) fully loaded, for production operators and supply-chain staff alike.

**Evidence**

- CAO Metaal & Techniek 2026 (the collective agreement that covers most Dutch installation and metal-assembly employers): monthly gross scale from EUR 2,422 (lowest, group A) to EUR 5,292 (highest, group J) from 1 March 2026, a 3% rise on 1 March 2026 and a further EUR 115/month on 1 March 2027; 8% holiday allowance; pension via PMT; no fixed year-end bonus ([Salaristabel.nl](https://salaristabel.nl/artikelen/cao-metaal-techniek-salaris-2026), [Salaris-informatie.nl](https://www.salaris-informatie.nl/cao-sector/metaal-en-techniek-kleinmetaal)).
- Job grading: production and assembly workers ("Montage assistent", "Productieassistent") fall in groups A to C; skilled technicians B to F. Hourly rates from 1 July 2026 run from EUR 14.99 at A/2 (EUR 15.74 including the 5.01% ATV allowance) to EUR 32.13 at J/11 ([Flexpedia CAO Metaal & Techniek scales](https://www.flexpedia.nl/kennis/branches/cao-metaal-techniek/salarisschalen/)).
- Eurostat 2025: Netherlands whole-economy hourly labour cost EUR 47.9 (third highest in the EU after Luxembourg and Denmark); EU average EUR 34.9, euro area EUR 38.2; non-wage costs are 24.8% of total labour cost in the EU and 25.6% in the euro area ([Eurostat news release, 31 March 2026](https://ec.europa.eu/eurostat/web/products-eurostat-news/w/ddn-20260331-2)). The Netherlands-specific non-wage share and the industry-only rate were not in the fetched page.

Derivation (my arithmetic): an operator in group B/C with a few function years earns about EUR 17.5 to 19.5 per hour, or EUR 2,900 to 3,200 gross per month at 164 hours. Adding 8% holiday allowance and employer contributions of roughly 25 to 30% (PMT pension employer share, WW, WIA/WGA, ZVW, plus ATV; the 25 to 30% is the usual Dutch rule of thumb and was not verified against a source this session) gives a loading factor of about 1.35 to 1.40, so EUR 3,900 to 4,500 per month, or EUR 4,300 to 4,900 with shift premiums, training and recruitment. Supply-chain planners and buyers (groups E to G, EUR 3,600 to 4,600 gross) load to EUR 4,900 to 6,400. The Eurostat economy-wide figure (EUR 47.9 x about 1,650 hours = about EUR 6,600 per month) is an upper bound that includes high-paid sectors.

**Verdict:** **supported as a blended figure.** Slightly high for line operators on their own (EUR 4,000 to 4,900), slightly low for experienced supply-chain professionals (EUR 5,000 to 6,400). Since the model applies one rate to both, EUR 5,000 is a fair average, and it leaves room for the 2027 CAO step.

**Suggested range:** operators EUR 4,000 to 4,900/month loaded; supply-chain and order-desk staff EUR 4,800 to 6,400/month loaded; blended EUR 4,800 to 5,400. Index at 3 to 4% per year (CAO 2026 to 2028 path).

---

## Sources not obtainable this session

- Vaillant Group consolidated balance sheet (Bundesanzeiger filing is a scanned image).
- Bosch Home Comfort stand-alone working capital (not published separately from the Bosch Group).
- Ariston cost of sales by function (income statement is by nature), so Ariston DIO is estimated from inventories as % of revenue.
- Applied Energy 2024 heat-pump learning-rate paper (publisher page returned 403; figures taken from the search abstract).
- A verified 2026 Dutch employer on-cost percentage and Dutch pallet-groupage tariffs (web search budget exhausted).


---

# Tarnoc B.V. – market evidence for people-cost, overhead and general financial assumptions

Scope: Netherlands, 2026 price level, loaded employer cost per month (gross salary + holiday allowance + employer social charges + pension, and car/expenses where stated). Research date: 4 September 2026. Sources are public web pages; salary-survey PDFs from Berenschot, Robert Walters and Michael Page are download-gated and were not read, so role salaries rely on aggregator sites (Indeed, Werkzoeken, Nationale Beroepengids, Jobted, Glassdoor, Talent.com) plus CAO and CBS data.

## Conversion used throughout: gross salary to loaded cost

Evidence:
- LoonBox (2026): employer cost is 120–135% of gross salary excluding pension, 130–145% including pension. Components: holiday allowance 8%, Awf/WW 2.74% (low rate), Zvw employer levy 6.10%, WIA/WGA about 1%, pension 10–20% of pension base. Worked example: EUR 3,500 gross becomes EUR 4,430 with a 15% pension (+26.6%). https://loonbox.nl/kennisbank/wat-kost-een-medewerker-2026/
- Job Planet (2026): holiday reserve 8.33%, Awf low 2.74%, Aof about 6.18%, Whk 1–3%, Zvw 6.51%; total employer charges 30–40% on top of gross; EUR 3,000 gross becomes EUR 3,900–4,200. https://www.job-planet.nl/hoe-hoog-zijn-de-werkgeverslasten-in-2026/
- Ondernemen met Personeel (2026): about 37% on top of gross; EUR 4,000 gross becomes about EUR 5,480. https://www.ondernemenmetpersoneel.nl/orienteren/personeelskosten/werkgeverslasten-berekenen-2026
- CBS: labour cost per worked hour averaged EUR 48 in 2025 (all sectors); wages per hour +5.5%, labour cost per hour +5.8% in 2025. Average annual wage per employee (headcount, including part-timers) EUR 40,800. https://www.cbs.nl/nl-nl/nieuws/2025/42/loonkosten-per-gewerkt-uur-6-procent-hoger-in-2024 and https://www.cbs.nl/nl-nl/visualisaties/dashboard-arbeidsmarkt/ontwikkeling-cao-lonen/jaarloon-werknemers-per-bedrijfstak

Working assumption in this note: loaded cost = 1.30 x gross monthly salary (gross salary excluding holiday allowance). Range 1.27–1.38 depending on pension scheme and Whk premium. Company car (EUR 700–900/month lease plus EUR 100–300 fuel, see section 3) is on top when applicable.

Implied gross monthly salary behind each model figure at 1.30:

| Role | Model loaded EUR/month | Implied gross EUR/month | Implied gross EUR/year (x12.96 incl. 8% holiday pay) |
|---|---|---|---|
| Sales rep | 7,500 | 5,770 | 74,800 |
| Partner (channel) manager | 8,000 | 6,150 | 79,700 |
| Trainer / order desk / marketing | 7,000 | 5,385 | 69,800 |
| Supply chain / production operator | 5,000 | 3,845 | 49,800 |
| Customer support agent | 4,800 | 3,690 | 47,800 |
| Leadership and back office (blended) | 7,000 | 5,385 | 69,800 |
| R&D engineer (blended) | 5,700 | 4,385 | 56,800 |
| Field service engineer | 6,500 | 5,000 | 64,800 |

---

## 1. Loaded employer cost per month by role

### 1a. Sales rep – model EUR 7,500

Evidence (gross, per month, full-time, excluding bonus):
- Indeed: account manager average EUR 3,847. https://nl.indeed.com/career/accountmanager/salaries
- Werkzoeken: EUR 3,575. https://www.werkzoeken.nl/salaris/accountmanager/
- Jobted: EUR 3,830. https://www.jobted.nl/salaris/accountmanager
- Maandag: range EUR 2,800–5,500 at 40 hours, excluding bonus. https://www.maandag.com/nl-nl/blog/accountmanager-salaris-in-2026
- Company car: EUR 450–650/month mid-class, EUR 700–900/month for a EUR 45k car, plus EUR 100–300 fuel. https://watkanikleasen.nl/blog/leasevormen-vergelijken/wat-kost-operational-lease-zakelijk-per-maand and https://www.lizy.nl/blog/zakelijk-leasebudget

Reading: a market-average account manager at EUR 3,900 gross loads to about EUR 5,050. Adding a lease car (EUR 800 incl. fuel) and a 15% variable gives about EUR 6,600. The model's EUR 7,500 implies a EUR 5,770 base with no car and no bonus, or a EUR 4,600 base plus car plus bonus. That is a senior B2B technical sales profile, not a market-average rep.

Verdict: looks high for an average rep; supported only if the figure is meant as on-target earnings including car and bonus for experienced B2B sellers into installers and wholesalers.
Suggested range: EUR 5,500–7,500 loaded per month including car and variable pay; EUR 5,000–6,000 if car and bonus are booked elsewhere.

### 1b. Partner (channel) manager – model EUR 8,000

Evidence:
- Glassdoor: partner manager average EUR 5,207 gross/month, annual EUR 54,816–68,880. https://www.glassdoor.nl/Salarissen/partner-manager-salarissen-SRCH_KO0,15.htm
- Talent.com: EUR 79,500/year (about EUR 6,625/month). https://nl.talent.com/salary?job=partner+manager
- Brand New Sales: channel manager base EUR 55,000–85,000/year excluding variable; total package about EUR 100,000 with bonus. https://brandnewsales.nl/functies/channel-manager/

Reading: a EUR 70,000 base loads to about EUR 91,000/year (EUR 7,600/month); with a EUR 15–20k bonus and a car the package is EUR 9,000–10,000/month. The model's EUR 8,000 sits between a base-only and an all-in view.

Verdict: supported.
Suggested range: EUR 7,000–9,500 loaded per month (upper end if car and bonus included).

### 1c. Installer trainer / order desk / marketing staff – model EUR 7,000

Evidence (gross per month):
- Technical trainer: EUR 3,750–4,500 (Jobbird); trainer average EUR 3,635–4,083 (Werkzoeken, Jooble). https://career.jobbird.com/nl/beroepengids/onderwijs/trainer and https://www.werkzoeken.nl/salaris/trainer/
- Order desk / binnendienst: EUR 2,915 (order administration, Werkzoeken), EUR 2,950 (commercieel medewerker binnendienst, WR), EUR 3,254 (medewerker binnendienst, Indeed). https://www.werkzoeken.nl/salaris/medewerker-orderadministratie/ and https://nl.indeed.com/career/medewerker-binnendienst/salaries
- Marketing: marketing medewerker EUR 3,382–3,400; marketing manager EUR 4,375–4,645; senior marketing manager at agencies EUR 6,000–8,500. https://nl.indeed.com/career/marketing-medewerker/salaries and https://www.werkzoeken.nl/salaris/marketing-manager/

Reading: a blend of one trainer (EUR 4,200), order desk staff (EUR 3,100) and marketing (EUR 3,400 staff / EUR 4,500 manager) gives a blended gross of about EUR 3,700–4,000, i.e. EUR 4,800–5,200 loaded. The model's EUR 7,000 implies EUR 5,385 gross, which is a senior marketing manager level for every person in the group.

Verdict: looks high (by roughly 30–40%).
Suggested range: EUR 4,800–5,800 loaded per month blended; EUR 6,500–7,500 only for a marketing lead or head of training.

### 1d. Supply chain and production operator – model EUR 5,000

Evidence:
- Production operator average EUR 2,890 gross/month (Indeed, 33.7k data points). https://nl.indeed.com/career/productiemedewerker/salaries
- Logistics employee EUR 2,535–3,021 (Werkzoeken, Nationale Beroepengids, Indeed). https://www.nationaleberoepengids.nl/salaris/logistiek-medewerker
- CAO Metaal en Techniek 2026–2028: starting scales EUR 2,350–4,250 gross/month (2025), +3% on 1 March 2026, +EUR 115/month on 1 March 2027, one-off EUR 500 (June 2026) and EUR 132 (Nov 2026). https://www.salaris-informatie.nl/cao-sector/metaal-en-techniek-kleinmetaal and https://precisionpartner.nl/nieuwe-cao-metaal-techniek-2026-2028/

Reading: an operator at EUR 3,000 gross loads to EUR 3,900; a supply-chain planner or buyer at EUR 4,000–4,500 gross loads to EUR 5,200–5,850. If the group is mostly operators and warehouse staff, EUR 5,000 is about 20% high; if half are planners/buyers/quality staff it is right.

Verdict: supported for a mixed supply-chain team; looks high for assembly and warehouse operators alone.
Suggested range: EUR 4,000–5,200 loaded per month blended.

### 1e. Customer support agent – model EUR 4,800

Evidence:
- Indeed EUR 3,062; Nationale Beroepengids EUR 2,900–3,150; Werkzoeken EUR 2,480; Topvacaturebank EUR 2,602; senior/specialist from EUR 3,300 (Go-Office). https://nl.indeed.com/career/medewerker-klantenservice/salaries and https://www.nationaleberoepengids.nl/salaris/klantenservice and https://go-office.nl/kennisbank/carriere/salaris-medewerker-klantenservice/

Reading: first-line support at EUR 2,900 gross loads to EUR 3,770; technical second-line support at EUR 3,400 loads to EUR 4,400. The model's EUR 4,800 implies EUR 3,690 gross, a senior technical-support level.

Verdict: looks high for a standard agent; acceptable if the team is technical second-line support that diagnoses boilers and heat pumps remotely.
Suggested range: EUR 3,700–4,500 loaded per month.

### 1f. Leadership and back office (CEO/CFO/finance/HR/IT/legal, blended) – model EUR 7,000

Evidence:
- Creandum study of 500 European start-up founders (reported by MT/Sprout, 2024): median CEO EUR 60,000, CFO EUR 72,000, CTO EUR 69,000, COO EUR 57,000, CRO EUR 90,000; by stage: seed EUR 75,000, Series A EUR 120,000, Series B EUR 140,000; Benelux founder median EUR 62,000. https://mtsprout.nl/groei/startup-salaris-oprichter
- Robert Half 2026: CFO EUR 147,211–220,125 (larger companies). https://www.roberthalf.com/nl/nl/baan-details/cfo
- Financieel directeur average EUR 5,620 gross/month (range 4,780–6,465) (Werkzoeken); MKB director EUR 7,074/month (Jooble). https://www.werkzoeken.nl/salaris/financieel-directeur/ and https://nl.jooble.org/salary/directeur-mkb
- Michael Page CFO guidance: EUR 62–71k (<5 yrs), 71–84k (5–10 yrs), 84–122k (10+ yrs). https://www.michaelpage.nl/advice/loopbaanadvies/loopbaanontwikkeling/hoeveel-verdient-een-financieel-directeur-cfo

Reading: a Series A/B CEO and CFO at EUR 120–140k each load to EUR 13,000–15,000/month. Finance, HR and office staff at EUR 3,500–5,000 gross load to EUR 4,500–6,500. A team of 3 in 2026 (CEO, CFO, one generalist) blends to about EUR 10,000; a team of 8 in 2030 (2–3 executives, 5–6 staff) blends to about EUR 7,500–8,500 in 2026 money.

Verdict: supported as a blended figure for 2028–2030; looks low for 2026–2027 when the group is 3–4 people and mostly executives.
Suggested range: EUR 7,000–9,000 loaded per month blended, or model executives (EUR 12,000–15,000) and staff (EUR 4,500–6,500) separately.

### 1g. R&D engineer – model EUR 5,700 (client's blended figure)

Evidence:
- R&D engineer average EUR 3,920 gross/month, range 3,335–4,510 (Werkzoeken). https://www.werkzoeken.nl/salaris/rd-engineer/
- Comaen 2026: junior EUR 3,000–3,500, medior 3,500–3,800, senior 3,800–4,200, team lead 4,200–4,500+; higher in hightech/scale-ups and in Brainport, often plus bonus. https://www.comaen.nl/blog/wat-verdient-een-rd-engineer/
- Mechanical engineer average EUR 3,978–4,075 gross/month, range 3,465–4,690 (Indeed, Werkzoeken). https://nl.indeed.com/career/engineer-werktuigbouwkunde/salaries
- Robert Walters and Michael Page 2026 guides exist but are download-gated; not read. https://www.robertwalters.nl/en/our-services/salary-survey.html and https://www.michaelpage.nl/en/news-insights/studies/salary-benchmark

Reading: the model implies EUR 4,385 gross, above the aggregator averages (EUR 3,900–4,100) and at the top of the published senior band. It fits a team weighted to senior mechanical, thermal, electronics and embedded engineers. Aggregator sites under-represent senior specialist pay; senior embedded/controls engineers in the Randstad and Brainport are commonly offered EUR 5,000–6,500 gross, which would load to EUR 6,500–8,500.

Verdict: supported for the existing team; likely low for the senior specialists hired from 2027 on (controls, refrigeration, certification).
Suggested range: EUR 5,500–6,500 loaded for the blended existing team; EUR 6,500–8,000 for new senior hires.

### 1h. Field service engineer – model EUR 6,500

Evidence:
- Servicemonteur verwarmingstechniek average EUR 3,110 gross/month, range 2,645–3,580 (Werkzoeken). https://www.werkzoeken.nl/salaris/servicemonteur-verwarmingstechniek/
- CV monteur EUR 2,985–3,205; installatiemonteur EUR 2,800–3,100 (Indeed, MijnTechCarriere). https://nl.indeed.com/carrieregids/salaris/salaris-cv-monteur and https://www.mijntechcarriere.nl/posts/installatiemonteur/wat-verdient-een-installatiemonteur
- Heat-pump specialists earn EUR 500–800/month more; warmtepompmonteur EUR 35,000–55,000/year (WattSlimmer, Strevon). https://wattslimmer.nl/kennisbank/hoeveel-verdient-een-warmtepompmonteur-per-jaar/ and https://strevon.nl/kennisbank/beroepen/wat-verdient-een-installatiemonteur/
- Service van: operational lease of a compact van is in the EUR 450–650/month band plus fuel EUR 100–300 (same lease sources as 1a).

Reading: a heat-pump-qualified service engineer at EUR 3,800 gross loads to EUR 4,950; add a van with fuel (EUR 750), tools and standby/overtime allowance (EUR 300–500) gives EUR 6,000–6,200.

Verdict: supported if van, tools and standby pay are inside the figure; looks high (by about 15–20%) if the van is booked under travel or fleet.
Suggested range: EUR 5,500–6,500 loaded per month including van; EUR 4,800–5,500 excluding van.

### Cross-check against national averages

CBS labour cost of EUR 48 per worked hour times about 1,500 worked hours per full-time year gives about EUR 72,000 per FTE, or EUR 6,000 per month, as the national all-sector average for a full-timer. The model's headcount-weighted blend (mostly R&D, supply chain, support and field staff) works out near EUR 6,000. The overall payroll is therefore in the plausible band; the issue is distribution: the commercial and support roles are priced above market while engineers and executives are priced at or below.

---

## 2. Annual salary increase 8%; other operating costs +10% per year

Evidence:
- CBS: CAO wages +5.0% in 2025 (one of the highest in 40 years), +4.5% year on year in Q1 2026; private companies +4.9%. https://www.cbs.nl/nl-nl/nieuws/2026/01/cao-lonen-stijgen-in-2025-met-5-0-procent and https://nieuws.nl/economie/cao-lonen-stijgen-met-45-procent-in-eerste-kwartaal
- CPB Centraal Economisch Plan March 2026: contract wages +4.0% (2026), +3.5% (2027); CPI 2.3% (2026), 2.1% (2027). https://www.cpb.nl/system/files/cpbmedia/CPB_Raming-centraal-economisch-plan-2026.pdf
- CPB August 2026 update: CAO wages +4.2% (2026), +3.8% (2027); inflation about 3% in both years because of energy prices. https://www.salarisvanmorgen.nl/2026/08/16/cpb-koopkracht-daalt-in-2027-cao-loongroei-blijft-boven-inflatie/
- CPB medium-term outlook to 2034 (March 2026): contract wages (companies) average 3.2% per year 2027–2030; wage rate per hour (loonvoet bedrijven) 3.6%; CPI 2.3%; HICP 2.2%. https://www.cpb.nl/raming/actualisatie-verkenning-middellange-termijn-tot-en-met-2034-maart-2026
- AWVN: average wage agreement in CAOs for calendar 2026 is 3.18% (2025: 3.76%). https://www.awvn.nl/cao/nieuws/maandbericht-loonontwikkeling-2026/
- CAO Metaal en Techniek 2026–2028: +3% (Mar 2026), +EUR 115/month (Mar 2027, about 3%), plus one-offs. https://precisionpartner.nl/nieuwe-cao-metaal-techniek-2026-2028/
- Facility costs (NFC Index): +11% in 2023, +5.9% in 2025 to EUR 637/m2, driven by wages in facility services. https://fmn.nl/nieuws/1218-nfc-index-maakt-bekend-exploitatiekosten-kantoren-stijgen-tot-recordhoogte and https://www.smartwp.nl/nieuws/20260902-nieuwe-nfc-index-2025

Reading: the forecast path for wages is about 4% in 2026, 3.5–3.8% in 2027 and 3.2–3.6% a year 2028–2030. Adding 1–1.5 points for promotions and seniority drift (incidental wage growth) gives 4.5–5.5%. The model's 8% is roughly double the forecast every year; compounded over 2026–2030 it lifts 2030 payroll by about 15% versus a 5% path. For other operating costs, forecast CPI is 2.1–3% and even facility services, the fastest-rising overhead category, ran 6–11%. 10% is well above any published forecast.

Verdict: both look high.
Suggested range: salaries 4–5.5% per year (5% is a defensible single number that includes seniority drift); other operating costs 3–5% per year (up to 6% for facilities).

---

## 3. Overheads per person per month

### 3a. Offices and facilities – model EUR 700

Evidence:
- NFC Index 2025 (corporate offices, all facility costs incl. rent, services, energy, cleaning, security, ICT workplace): EUR 637 per m2 rentable area; 14.3 m2 per FTE; 22.6 m2 per workplace; 0.69 workplaces per FTE. That is EUR 9,100 per FTE per year (EUR 760/month) or EUR 14,400 per workplace (EUR 1,200/month). https://www.smartwp.nl/nieuws/20260902-nieuwe-nfc-index-2025
- Office rent: EUR 130–200 per m2 per year outside prime; EUR 300–500 all-in in Amsterdam/Utrecht prime; service costs EUR 30–80 per m2; energy EUR 20–50 per m2 (Deskfinder, Schoeman, Spring). https://deskfinder.nl/wat-kosten-kantoorruimtes-in-nederland-in-2025/ and https://www.schoeman.nl/news/wat-zijn-redelijke-huurprijzen-voor-kantoorruimte-in-2025
- Flex office: about EUR 600 per desk per month in Utrecht. https://co-office.nu/en/news/hoeveel-kost-het-om-een-kantoorruimte-te-huren/

Reading: a secondary-location office with lab and workshop at 20–25 m2 per person, all-in EUR 250–350 per m2, gives EUR 420–730 per person per month. The NFC corporate benchmark is EUR 760 per FTE.

Verdict: supported.
Suggested range: EUR 550–850 per person per month. The main risk is not the rate but lumpiness: a lab, test rig space and a warehouse are step costs and do not scale linearly with headcount.

### 3b. IT and software – model EUR 250 (EUR 3,000 per year)

Evidence:
- SMB IT spend USD 1,000–2,500 per employee per year at about 100 employees; USD 2,000–5,000 for smaller firms (IT Budget Calculator). https://itbudgetcalculator.com/by-company-size
- Cledara 2025: average SaaS spend USD 4,830 per employee per year; 0–20 employee firms about USD 8,000 (Mekari summary). https://expense.mekari.com/en/blog/average-software-spend-per-employee-statistics
- VendorBenchmark 2026: USD 12,000–22,000 per employee for 250–1,000-employee enterprises (US, software-heavy sample). https://vendorbenchmark.com/blog/software-spend-per-employee-benchmark
- Gartner: small businesses pay about 2.3x more per employee than enterprises for equivalent capability (cited in the same sources).

Reading: EUR 3,000 per person covers a laptop on a 3-year cycle (EUR 50/month), Microsoft 365 or Google Workspace (EUR 15–25), ERP and CRM seats (EUR 50–150 for the users who need them), telecom and MSP support. It does not cover engineering tools (CAD, simulation, PLM at EUR 300–1,000 per seat per month) or a product cloud/IoT back end, which belong in R&D or COGS.

Verdict: supported at the lean end for general staff; low if engineering software and device connectivity are meant to sit here.
Suggested range: EUR 200–350 per person per month for general IT; add EUR 500–1,000 per engineer per month for CAD/PLM/test software.

### 3c. Travel – model EUR 300 (EUR 3,600 per year per head)

Evidence:
- US benchmarks: USD 11,200 per business traveller per year in mid-market firms, USD 18,400 in Fortune 1000; USD 1,549 per trip for medium firms (GBTA / Engine / Zippia). https://engine.com/blog/business-travel-data-trends and https://www.zippia.com/advice/business-travel-statistics/
- No Dutch per-employee travel benchmark was found.

Reading: only sales, partner managers, trainers and leadership travel meaningfully; engineers and support staff do not. If 25–30% of staff are travellers at EUR 8,000–10,000 a year, the blended figure is EUR 200–250 per head per month. If lease cars for sales staff are not in the salary figures they need to be here (EUR 800–1,100 per car per month).

Verdict: supported as a blended figure; check where company cars are booked.
Suggested range: EUR 150–350 per person per month blended, excluding lease cars.

### 3d. Recruitment – model EUR 8,000 per net new hire

Evidence:
- Intelligence Group / Werf& Recruitment Kengetallen: average cost per hire EUR 4,494 across 109 corporates (all-in incl. internal recruiter cost); earlier waves EUR 3,818 (2021) and EUR 4,088 (2020). https://www.werf-en.nl/werving-werknemer-kost-gemiddeld-4-494-euro/ and https://recruitingroundtable.nl/recruitment-kengetallen-onderzoek/
- Headfirst 2026: junior EUR 3,000–6,000, mid EUR 6,000–12,000, senior/management EUR 15,000–30,000+; agency fee 15–25% of gross annual salary (EUR 7,500–12,500 for a EUR 50k hire); hidden onboarding and productivity cost adds 30–50%. https://www.headfirst.nl/blog/cost-per-hire-in-nederland-berekenen-en-verlagen-in-2026/
- Werkzoeken: scarce technical roles cost 3–5x the average. https://www.werkzoeken.nl/blog/recruitment/marketing/250_hoe-bereken-je-de-cost-per-hire/

Reading: a hardware scale-up hiring engineers, technical sales and field engineers, partly through agencies, will average above the national EUR 4,500 figure. EUR 8,000 matches one agency placement at 15–20% on a EUR 45–55k salary, or a mix of agency and direct hires.

Verdict: supported. Two structural notes: (1) the model charges recruitment only on net new hires, so replacement hires for attrition (10–15% a year is typical) are not costed; (2) a growth to 340 staff in the aggressive case implies an in-house recruiter or two, whose salaries are a fixed cost rather than a per-hire cost.
Suggested range: EUR 6,000–12,000 per hire; apply to gross hires (net new plus 10–15% replacement).

---

## 4. Other fixed monthly costs

### 4a. Finance and legal – model EUR 7,000/month (EUR 84k/year)

Evidence:
- Accountant fees: bookkeeping and VAT EUR 150–400/month for a small company; corporate tax return and filing EUR 750–2,000; MKB annual accounts from EUR 3,500; statutory audit from EUR 12,000 (Consultant.nl, Boekhouders.nl, Acc Online). https://www.consultant.nl/categories/accountant/wat-kost-een-accountant and https://acconline.nl/kosten-accountant-per-jaar/
- Audit becomes mandatory when two of three thresholds are met for two consecutive years (revenue > EUR 15m, assets > EUR 7.5m, > 50 employees), which the base case crosses around 2028. https://wrkd.nl/diensten/controleverklaring
- Legal hourly rates EUR 80–140 for standard work (Lawsy, 2026); specialised corporate counsel is higher. https://lawsy.nl/kosten-vergelijkingen
- No public benchmark was found for total annual legal spend at a Series A/B hardware scale-up (financing rounds, patents, supply agreements, distribution contracts).

Reading: in 2026–2027 (16–30 staff, no audit) EUR 40–60k a year covers accounting, payroll and routine legal. From 2028 an audit (EUR 15–30k), patent maintenance and filings (EUR 10–30k), financing-round legal (EUR 30–80k per round) and international distribution contracts push the total to EUR 120–250k a year.

Verdict: supported for 2026–2027; looks low for 2028–2030 as a flat figure, and clearly low for the aggressive case.
Suggested range: EUR 4,000–6,000/month in 2026–2027 rising to EUR 12,000–20,000/month by 2030 (base) and EUR 25,000+/month (aggressive).

### 4b. Other general – model EUR 5,000/month (EUR 60k/year)

Evidence: no direct benchmark found. The category normally holds insurance (general and product liability, D&O, property), bank charges, memberships (Techniek Nederland), subscriptions and office consumables. Product-liability cover for a gas appliance and heat-pump manufacturer is the largest item and scales with units in the field and revenue; premiums could not be researched within this session's search budget.

Verdict: no evidence found; the amount is plausible for 2026–2027 and probably low once revenue and installed base grow.
Suggested range: EUR 4,000–6,000/month early, scaling to about 0.3–0.5% of revenue for insurance-led costs later.

### 4c. Ongoing development EUR 8,000/month and third-party product development EUR 10,000/month (EUR 216k/year combined)

Evidence: none found within this session. Certification of a gas appliance and a hybrid heat pump (CE under the Gas Appliances Regulation and Ecodesign, KIWA/Gastec or DVGW type approval, EN 15502 testing, ErP labelling, electrical safety and EMC, refrigerant safety) requires paid test-lab time and re-certification for each variant and each target market; these are project costs of tens of thousands of euros per variant rather than a flat monthly run rate. Prototype tooling and pilot batches are also lumpy.

Verdict: no evidence found. The combined EUR 216k a year is a reasonable placeholder for a single-product company but does not reflect the step costs of certifying new variants and export markets, and in the aggressive case (multiple variants, several countries) it is very likely low.
Suggested range: keep EUR 15,000–20,000/month as a base run rate and add explicit certification and tooling projects (EUR 50,000–200,000 each) per new variant or market.

---

## 5. Corporate income tax and loss carry-forward; convertible loan interest

Evidence:
- 2026 rates: 19% on the first EUR 200,000 of taxable profit, 25.8% above (unchanged from 2025). https://www.mkbservicedesk.nl/belastingen/vennootschapsbelasting/verliesverrekening-vpb and https://www.informer.nl/belastingen/ondernemen/vennootschapsbelasting
- Loss relief since 1 January 2022: carry-back one year; carry-forward unlimited in time; in any year losses offset the first EUR 1m of taxable profit in full and 50% of the taxable profit above EUR 1m. Belastingdienst and Taxence. https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/winst/vennootschapsbelasting/verrekenen_van_verliezen/verrekenen_van_verliezen and https://www.taxence.nl/nieuws/nieuwe-verliesverrekeningsregels-wet-vpb-per-1-januari-2022/
- Convertible loans in the Netherlands typically carry 4–10% interest; subordinated investor loans 8% or more; five-year terms are common (Investeerders.nl, Firm24). https://www.investeerders.nl/converteerbare-lening/ and https://www.firm24.com/kennisbank/article/converteerbare-obligatie-startup/

Reading:
- The 25.8% rate is the correct top rate. The model ignores the 19% band on the first EUR 200k, which overstates tax by at most EUR 13,600 a year; immaterial once profits are large.
- "Unlimited carry-forward with a 50% cap above EUR 1m" is the correct rule if implemented as: losses used in year t = min(loss stock, EUR 1m + 50% x max(0, taxable profit − EUR 1m)). Check that the cap is applied to taxable profit before loss relief and that the unused balance rolls forward.
- 5% on a EUR 300k convertible is inside the market band, at the low end. Interest of EUR 15k a year is far below the EUR 1m earnings-stripping threshold, so it is fully deductible.
- Not in the model but relevant: the WBSO R&D wage-cost credit and the innovation box (9% effective rate on qualifying profit) are standard for a Dutch hardware developer and would reduce both payroll cost and the tax rate. Worth flagging rather than assuming.

Verdict: supported (rate and loss rule); minor omission of the 19% band; interest rate supported.
Suggested range: keep 25.8% with the 19% band added; convertible interest 5–8%.

---

## 6. R&D team size: 10 in 2027 rising to 21 (base) or 48 (aggressive) by 2030

Evidence on comparators:
- Intergas (Coevorden, owned by Rheem): about 500 staff in total, over 300 in Coevorden; revenue reported at EUR 145m; R&D expansion phase 1 created 12 workstations, a 3D-print area and a technical space; the engineering and documentation team is 10 specialists. Total R&D headcount not disclosed. https://werkenbijintergas.nl/ons-bedrijf and https://www.installatie.nl/nieuws/intergas-wordt-amerikaans/ and https://theorg.com/org/intergas-verwarming/offices/hq
- BDR Thermea (Remeha, Baxi, De Dietrich): EUR 1.9bn revenue, about 6,500 staff, 15 R&D centres on three continents. https://www.bdrthermeagroup.com/en/about-us
- Vaillant Group: EUR 3.2bn revenue and about 16,000 staff (2024); EUR 3.8bn and 17,500 staff (2023). R&D headcount not disclosed. https://en.wikipedia.org/wiki/Vaillant_Group and https://www.vaillant-group.com/news-storys/vaillant-group-in-schwierigem-marktumfeld-weiter-gewachsen.html
- Quatt (Amsterdam): about 300 staff in early 2026, 350 reported in May 2025; 15,000 units installed by May 2025; own Amsterdam lab; EBITDA-positive target for 2025. Engineering team size not disclosed. https://mtsprout.nl/groei/quatt-levert-na-warmtepomp-nu-ook-thuisbatterij-en-energie-wij-bouwen-wat-we-cool-vinden and https://www.duurzaam-ondernemen.nl/forse-groei-voor-scale-up-quatt/
- Aira (Stockholm): about 1,000–1,150 staff (Revelio, 2025–2026); an "Engineering Design" team of 11 is listed on The Org, which is one sub-team, not total R&D. https://www.reveliolabs.com/companies/aira-group/employees and https://theorg.com/org/airahome/teams/engineering-design
- Octopus Energy Cosy hub and pods were developed in-house by a London team; size not disclosed. https://www.theengineer.co.uk/content/news/octopus-raises-the-temperature-with-cosy-heat-pump

Reading: no comparator publishes R&D headcount at Tarnoc's scale. Ratios that can be inferred: at incumbents R&D is a small share of a workforce dominated by manufacturing and service (BDR runs 15 R&D centres for 6,500 staff; Intergas has an R&D department in the low tens for 500 staff). The model's base case has R&D at 23% of headcount in 2030 (21 of 90) and the aggressive case at 14% (48 of 338). For a company that must own boiler combustion, hydraulics, refrigeration, electronics, firmware, app and cloud, and certify several variants for several markets, 21 engineers in 2030 is lean but workable with contract design houses (which is what the "third-party product development" line implies). 48 engineers at EUR 505m revenue is 10% of revenue per engineer at EUR 10m, which is far leaner than any incumbent; it only works if variants and markets are few.

Verdict: base case supported (lean); aggressive case looks low relative to the product and market scope that EUR 505m of revenue implies.
Suggested range: base 20–28 engineers by 2030; aggressive 60–90 by 2030, or explicit outsourced engineering spend of EUR 3–6m a year in place of the difference.

---

## 7. Back office: 3 people in 2026 rising to 8 by 2030 for 90 (base) or 340 (aggressive) staff

Evidence:
- HR ratio: 1.4–1.7 HR staff per 100 employees on average; 1.7–3.0 per 100 in organisations under 250 staff; technology firms 0.8–1.2 (AIHR, Acorn, CompanySights). https://www.aihr.com/blog/hr-to-employee-ratio/ and https://www.companysights.com/resources/hr-to-employee-ratio-benchmarking-guide
- G&A cost share: Series A companies 15–25% of revenue, Series B 12–18% (Pegacorn); SaaS opex benchmarks show G&A at 10–20% of opex (Parsa Saljoughian). https://www.pegacorngroup.com/insights/ga-budget-startup/ and https://medium.com/parsa-vc/operating-expense-benchmarks-for-saas-startups-e49697abf3ed
- No published back-office headcount ratio specific to hardware scale-ups was found.

Reading: for 90 staff, a back office of CEO, CFO, controller/AP, HR generalist, office/IT manager and one more (8 total including leadership) is 9% of headcount and in line with the HR ratio (1–2 HR people) and normal finance staffing (2–3). For 340 staff, the same ratios imply HR 4–6, finance 5–7 (AR/AP, payroll, controller, FP&A), IT 2–3, legal/compliance 1–2, plus 3–4 executives: 15–22 people, or 10–15 with payroll, IT and legal outsourced (which raises the fixed-cost lines in section 4).

Verdict: base case supported; aggressive case looks low (8 people, 2.4% of headcount).
Suggested range: base 7–10 by 2030; aggressive 14–22 by 2030, or 10–14 with the outsourcing costs added in section 4.

---

## 8. Revenue per employee: aggressive case EUR 1.5m per head in 2030 (EUR 505m, 338 staff)

Evidence (latest public figures, revenue per employee computed from them):

| Company | Revenue | Employees | Revenue per employee | Model | Source |
|---|---|---|---|---|---|
| Vaillant Group (2024) | EUR 3.2bn | ~16,000 | ~EUR 200k | own factories, service | https://en.wikipedia.org/wiki/Vaillant_Group |
| Vaillant Group (2023) | EUR 3.8bn | 17,500 | ~EUR 217k | | https://www.vaillant-group.com/news-storys/vaillant-group-in-schwierigem-marktumfeld-weiter-gewachsen.html |
| Viessmann Climate Solutions (2023, at acquisition) | ~EUR 4bn | ~12,000 | ~EUR 333k | own factories | https://www.corporate.carrier.com/news/news-articles/carrier-schliesst-uebernahme-von-viessmann-climate-solutions-ab.html |
| NIBE Industrier (2025) | just under SEK 40bn (~EUR 3.6bn) | 20,500 average | ~EUR 175k | own factories | https://www.inderes.fi/en/releases/nibe-industrier-ab-publ-year-end-report-2025 |
| BDR Thermea (Remeha) | EUR 1.9bn | ~6,500 | ~EUR 290k | own factories | https://www.bdrthermeagroup.com/en/about-us |
| Intergas | EUR 145m | ~500 | ~EUR 290k | own factory, Coevorden | https://www.installatie.nl/nieuws/intergas-wordt-amerikaans/ and https://werkenbijintergas.nl/ons-bedrijf |
| Quatt (2025) | not disclosed | 300–350 | not computable (order of EUR 200k if ~10k units a year at EUR 6–7k) | outsourced manufacturing, own installation | https://mtsprout.nl/groei/quatt-levert-na-warmtepomp-nu-ook-thuisbatterij-en-energie-wij-bouwen-wat-we-cool-vinden |
| Aira (2025) | EUR 200m run-rate | ~1,100 | ~EUR 180k | own installation | https://www.esgtoday.com/heat-pump-startup-aira-raises-174-million-to-decarbonize-residential-heating/ and https://www.reveliolabs.com/companies/aira-group/employees |
| Enpal (2025) | > EUR 1.1bn | 5,000–7,100 | ~EUR 155–220k | own installation | https://www.corporate.enpal.com/pressemitteilungen/enpal-erzielt-2025-rekordumsatz-und-setzt-weiter-auf-starkes-wachstum |
| 1KOMMA5 (2024) | EUR 520m | ~2,500 | ~EUR 208k | own installation | https://www.solarserver.de/2025/02/17/1komma5-steigert-umsatz-2024-auf-520-millionen-euro/ |
| Dyson (2024) | GBP 6.6bn | 18,015 | ~GBP 366k (~EUR 430k) | asset-light consumer hardware | https://www.dyson.co.uk/discover/news/press-releases/dyson-financial-results-2024 and https://www.reveliolabs.com/companies/dyson/employees |
| Apple (FY2025) | | | ~USD 2.5m | fully outsourced assembly, software and services margin | https://9to5mac.com/2025/11/20/apple-generates-2-4-million-per-employee-but-is-only-third-in-tech-ranking/ |

Notes on data quality: Owler's USD 2.5bn and Revelio's 1,855 employees for BDR Thermea conflict with the company's own page (EUR 1.9bn, 6,500) and were not used. Intergas revenue is from a 2019 acquisition article; the year is uncertain. Quatt has not published revenue.

Reading: heating-equipment incumbents with their own factories run EUR 175k–333k per head; installer-integrated heat-pump scale-ups run EUR 150k–220k. Outsourcing assembly removes factory labour, which is roughly 40–50% of an incumbent's headcount, so an asset-light heating brand could plausibly reach EUR 400k–600k per head. Dyson, a design-led hardware brand with contract and own Asian manufacturing, reaches about EUR 430k. Only Apple-type companies with dominant software and services margins exceed EUR 1m. The model's EUR 1.5m per head is 4–8 times the incumbent range and about 3.5 times Dyson. Two further points: (1) EUR 505m implies roughly 50,000–80,000 units a year, which requires sales, partner management, quality, supply chain, warranty and second-line service staff that scale with volume regardless of who assembles; (2) if installation revenue is passed through the P&L, revenue is inflated relative to Tarnoc's own value added, which flatters revenue per head further and argues for measuring gross profit per head instead.

Verdict: looks high.
Suggested range: EUR 400k–700k revenue per employee for an outsourced-assembly heating brand at scale. At EUR 505m that implies 700–1,250 staff; at 338 staff it implies EUR 135m–240m of revenue. If installation pass-through is kept in revenue, benchmark on gross profit per head (incumbents: roughly EUR 60k–100k) instead.

---

## Summary of verdicts

| # | Assumption | Verdict | Suggested range |
|---|---|---|---|
| 1a | Sales rep EUR 7,500 | Looks high unless OTE incl. car | EUR 5,500–7,500 incl. car and bonus |
| 1b | Partner manager EUR 8,000 | Supported | EUR 7,000–9,500 |
| 1c | Trainer/order desk/marketing EUR 7,000 | Looks high | EUR 4,800–5,800 blended |
| 1d | Supply chain/production EUR 5,000 | Supported for mixed team; high for operators only | EUR 4,000–5,200 |
| 1e | Customer support EUR 4,800 | Looks high | EUR 3,700–4,500 |
| 1f | Leadership/back office EUR 7,000 | Supported blended; low in 2026–27 | EUR 7,000–9,000 |
| 1g | R&D engineer EUR 5,700 | Supported for current team; low for new senior hires | EUR 5,500–6,500 / 6,500–8,000 |
| 1h | Field service EUR 6,500 | Supported incl. van; high excl. van | EUR 5,500–6,500 incl. van |
| 2 | Wages +8%/yr; other opex +10%/yr | Both look high | 4–5.5% wages; 3–5% opex |
| 3a | Office EUR 700/person | Supported | EUR 550–850 |
| 3b | IT EUR 250/person | Supported (lean); low if engineering tools included | EUR 200–350 + engineering tools |
| 3c | Travel EUR 300/person | Supported; check where cars are booked | EUR 150–350 |
| 3d | Recruitment EUR 8,000/hire | Supported; apply to gross hires | EUR 6,000–12,000 |
| 4a | Finance and legal EUR 7,000/month | Supported early; low from 2028 | EUR 4–6k rising to 12–20k+ |
| 4b | Other general EUR 5,000/month | No evidence found; plausible early | EUR 4–6k, scaling with revenue |
| 4c | Development EUR 18,000/month combined | No evidence found; misses certification step costs | Base run rate + per-variant projects |
| 5 | CIT 25.8%, loss rules, 5% convertible | Supported; 19% band omitted | Add 19% band; 5–8% interest |
| 6 | R&D 21 (base) / 48 (aggressive) in 2030 | Base supported; aggressive looks low | 20–28 / 60–90 |
| 7 | Back office 8 in 2030 | Base supported; aggressive looks low | 7–10 / 14–22 |
| 8 | EUR 1.5m revenue per head | Looks high | EUR 400–700k per head |

