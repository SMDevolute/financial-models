# Tarnoc v2: how the model works, outcomes, vulnerabilities

Written 2026-09-04 (Friday), for re-reading on Monday 2026-09-07.
Model: `models/Tarnoc_v2_2026-09-07.xlsx`. Updated 2026-09-07 after the formula review (`docs/tarnoc-v2-formula-review-2026-09-07.md`): ten defects fixed, of which one changed the numbers (per-person overheads, training and recruitment now inflate like every other cost). Figures below are as of that fix. Build: `scripts/build_tarnoc_v2.py`. Check with `python3 scripts/audit_v2.py models/Tarnoc_v2_2026-09-07.xlsx`.
Drive copy `Tarnoc_v2_2026-09-03.xlsx` is behind by every change made on 2026-09-04; upload the local file as a new version before sharing.

## How it works

Monthly, January 2026 to December 2030. Two cases on one switch (Assumptions E5): base (EUR3m raise) and aggressive (EUR10m raise). The file opens on base. The BOM price tier is set on this year plus next year's volume in both cases (a two-year volume commitment to the supplier); the earlier one-year/two-year switch was removed on 2026-09-07.

Units sold per month = the lowest of three calculated numbers:
1. Demand = marketing spend / EUR120 per lead x 50% qualified x 40% won, plus installer partners on the books x orders they bring in themselves (1 a month each in 2027, 4 by 2030).
2. Selling capacity = reps x 20 units a month, for the direct share of sales; partners x 8 units a month, for the rest. Direct share: 80% in 2027, 50% in 2028, 35% in 2029, 30% in 2030.
3. Build capacity = assembly partner (650 a month base, 1,000 aggressive) plus 1,000 a month per in-house line once producing. Aggressive has two automated lines from November 2027 and January 2028 (EUR3m each plus EUR3m tooling, paid twelve months ahead); base has none. The BOM is the same whether the partner or an own line builds the unit, so the lines add capacity, not a cost saving (an in-house saving was added and removed on 2026-09-07 at Simon's request).

Revenue = units x price (EUR8,526 turbineketel, EUR13,836 Combi+, 20/80 mix) + upsell + installation (passed straight through to the installer at cost) + service contracts on the installed base (88% attach, EUR60-200 a year).

COGS = BOM by volume tier (EUR9,984 below 5,000 units a year, EUR7,069 to 10,000, EUR4,998 above) + outdoor unit + shipping + upsell cost + installation + service parts + 10% commission on channel sales.

Headcount is calculated from drivers: reps and partner managers from the sales plan, support from installed base, supply chain and order desk from units, trainers from partners signed, field engineers at one per 750 units on contract, operators at 35 per line. R&D hires (Assumptions) and back office (typed on Personnel row 17) are set per year.

2026 is the committed plan, held fixed to October. Working capital: DSO 20, DPO 45, no inventory. Wages +5% a year, other costs +10%.

## Main outcomes

| | Base | Aggressive |
| --- | --- | --- |
| Units 2027 / 2028 / 2029 / 2030 | 310 / 1,200 / 3,900 / 7,200 | 2,800 / 6,900 / 11,700 / 18,800 |
| Revenue 2030 | EUR123m | EUR321m |
| EBITDA | positive from 2028 (EUR1m, 17m, 34m) | positive from 2027 (EUR5m, 23m, 45m, 80m) |
| Headcount 2030 | 85 | 289 |
| Lowest cash after raise | EUR0.9m, Dec 2027 (4 months of opex) | EUR1.0m, Jan 2027 (6 weeks of opex; 90% of the raise used) |

Gross margin steps from under 10% to 25% the year two-year volume passes 5,000 units and to 37% past 10,000. In base that is 2028 and 2029; in aggressive 2027 and 2028.

## Assumptions to be careful with

1. BOM cost-down. EUR9,984 to EUR4,998 is a 50% cut. Learning-curve evidence for heat pumps supports about 30%. Until volume passes 5,000 a year, a turbineketel sells for less than it costs to build. This is the single assumption the whole case rests on, and it has no supplier quote behind it yet.
2. Service attach at 88%. Market data says 76% of new buyers take a contract. Service is a large share of later-year profit.
3. Rep quota of 20 units a month. HVAC and solar benchmarks are 6-10. Only matters while direct is the main channel (2027-28).
4. 20% lead-to-order at EUR600 per customer. The client's current number, and defensible for a product priced below installed heat pumps, but above most published benchmarks.
5. No warranty reserve beyond the 3% inside the BOM. Peers carry 1.5-3.5% of revenue. A new product in its first years will cost more, not less.
6. Direct share falling to 30% by 2030 requires 145 active partners in 2029; every one has to be signed, trained and selling.

## Where the model is vulnerable

- Base on EUR3m holds EUR0.9m at its low (Dec 2027). It works only because 2028 plus 2029 volume is 5,100 units, 100 over the 5,000 tier; below that, 2028 costs EUR2,900 more per unit and the case goes negative again. It needs a bigger raise, the two-year BOM basis, or the marketing push that takes 2029 volume past 5,000 units (options and their effect are under To do, item 1).
- Both cases are loss-making per unit until the second BOM tier. If the tier is reached a year late, base runs out of cash and aggressive loses about EUR15m of cumulative EBITDA.
- Aggressive spends EUR9m on two lines before the first sale, hires about 75 people in 2027 and signs 36 installers that year. The numbers work; the execution risk is not in the model. The client has not said what the assembly partner charges per unit, so the model cannot yet give in-house production a cost advantage.
- The client's prices are unchanged from his original model. If the market forces a lower price, gross margin at tier 1 goes further negative.
- Service pricing (EUR60/90 a year for the turbineketel) is below the Dutch market. That is upside if raised, but the current numbers understate what is possible.

## To do

Decisions for Simon and the client:
1. Raise sizes: EUR3m funds the base case with about four months of cover at the low. Aggressive now uses 90% of the EUR10m (EUR9m of it capex in Nov 2026 and Jan 2027) and has six weeks of cover in January 2027; Simon asked for 2-3 months of cover and for 90% use, which cannot both hold at EUR10m. Options tested 2026-09-07: marketing +50% in 2028-29 (2029 volume crosses 5,000, EBITDA 2029 swings from -2.9m to +12.7m, low point EUR1.4m); two-year BOM basis (EBITDA 2028 +3.1m, low EUR1.4m); both plus faster partner signing (low EUR1.8m, uses 1.2m of the 3m). Without one of these the raise needs to be about EUR4.5m.
2. Supplier quotes behind the BOM tiers, and whether the supplier will price on a two-year volume commitment (switch E6).
3. Confirm the installer deal: 10% of unit price on top of the installation fee, or a trade discount if installers buy and resell (research says 20-30% in that case).
4. Confirm the direct-to-installer path (80/50/35/30% direct). Research says brands that go installer-led usually still hold 40-60% direct in year four.
5. Aggressive line 2 (capex EUR2.5m, paid July 2028): at 15,100 units a year the plan has 36,000 of build capacity. Keep it to deploy the EUR10m, or drop it.
6. Service contract prices for the turbineketel (EUR60/90) sit below the Dutch market (EUR96-290 incl. VAT). Raise them or leave as is.
7. Warranty reserve: back in at 2.5-4% of hardware revenue for early cohorts, or stay with the 3% inside the BOM.

Model work, not started:
8. Upload the current local file to Drive as a new version of `Tarnoc_v2_2026-09-03.xlsx` (Simon drags it in; the connector cannot take the file size).
9. Sensitivity table on the Dashboard: BOM tier timing, close rate, orders per partner, raise size.
10. Optional smoothing of the aggressive ramp: start line 1 at half staffing and ramp operators with output; sign partners 2/3/5/7 a month instead of 2/4/6/7.
11. Other cost inflation is still 10% a year; research supports 3-5%. Left as is on Simon's instruction to change wages only.
12. Update `docs/tarnoc-handover-2026-09-02.md`, whose numbers are from 2026-09-01.
13. Retire model A (`Tarnoc_LIVE_2026-09-01_growth-engine.xlsx`) once the client has been walked from A to B.

Full evidence for every assumption: `docs/tarnoc-assumptions-research-2026-09-04.md`.
