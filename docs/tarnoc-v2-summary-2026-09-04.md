# Tarnoc v2: how the model works, outcomes, vulnerabilities

Written 2026-09-04 (Friday), for re-reading on Monday 2026-09-07.
Model: `models/Tarnoc_v2_2026-09-01.xlsx` at commit `c4f4c96`. Build: `scripts/build_tarnoc_v2.py`. Check with `python3 scripts/audit_v2.py models/Tarnoc_v2_2026-09-01.xlsx`.
Drive copy `Tarnoc_v2_2026-09-03.xlsx` is behind by every change made on 2026-09-04; upload the local file as a new version before sharing.

## How it works

Monthly, January 2026 to December 2030. Two cases on one switch (Assumptions E5): base (EUR3m raise) and aggressive (EUR10m raise). The file opens on base. A second switch (E6) sets whether the BOM price tier is based on this year's volume or on this year plus next.

Units sold per month = the lowest of three calculated numbers:
1. Demand = marketing spend / EUR120 per lead x 50% qualified x 40% won, plus installer partners on the books x orders they bring in themselves (1 a month each in 2027, 4 by 2030).
2. Selling capacity = reps x 20 units a month, for the direct share of sales; partners x 8 units a month, for the rest. Direct share: 80% in 2027, 50% in 2028, 35% in 2029, 30% in 2030.
3. Build capacity = assembly partner (650 a month base, 1,000 aggressive) plus 1,000 a month per in-house line once producing. Aggressive has lines from November 2027 and July 2029; base has none.

Revenue = units x price (EUR8,526 turbineketel, EUR13,836 Combi+, 20/80 mix) + upsell + installation (passed straight through to the installer at cost) + service contracts on the installed base (88% attach, EUR60-200 a year).

COGS = BOM by volume tier (EUR9,984 below 5,000 units a year, EUR7,069 to 10,000, EUR4,998 above) + outdoor unit + shipping + upsell cost + installation + service parts + 10% commission on channel sales.

Headcount is calculated from drivers: reps and partner managers from the sales plan, support from installed base, supply chain and order desk from units, trainers from partners signed, field engineers at one per 750 units on contract, operators at 35 per line. R&D hires (Assumptions) and back office (typed on Personnel row 17) are set per year.

2026 is the committed plan, held fixed to October. Working capital: DSO 20, DPO 45, no inventory. Wages +5% a year, other costs +10%.

## Main outcomes

| | Base | Aggressive |
| --- | --- | --- |
| Units 2030 | 7,400 | 15,100 |
| Revenue 2030 | EUR126m | EUR259m |
| EBITDA | negative until 2030 (EUR19m) | positive from 2028, EUR64m in 2030 |
| Headcount 2030 | 87 | 256 |
| Lowest cash after raise | EUR0.3m, Dec 2029 | EUR5.1m, Dec 2027 |

On the two-year BOM basis, base EBITDA turns positive in 2028 and the cash low rises to about EUR1.4m.

## Assumptions to be careful with

1. BOM cost-down. EUR9,984 to EUR4,998 is a 50% cut. Learning-curve evidence for heat pumps supports about 30%. Until volume passes 5,000 a year, a turbineketel sells for less than it costs to build. This is the single assumption the whole case rests on, and it has no supplier quote behind it yet.
2. Service attach at 88%. Market data says 76% of new buyers take a contract. Service is a large share of later-year profit.
3. Rep quota of 20 units a month. HVAC and solar benchmarks are 6-10. Only matters while direct is the main channel (2027-28).
4. 20% lead-to-order at EUR600 per customer. The client's current number, and defensible for a product priced below installed heat pumps, but above most published benchmarks.
5. No warranty reserve beyond the 3% inside the BOM. Peers carry 1.5-3.5% of revenue. A new product in its first years will cost more, not less.
6. Direct share falling to 30% by 2030 requires 145 active partners in 2029; every one has to be signed, trained and selling.

## Where the model is vulnerable

- Base case on EUR3m has no margin for error: 0.4 months of costs at the low point. Any slip in volume, cost-down or timing puts it below zero.
- Both cases are loss-making per unit until the second BOM tier. If the tier is reached a year late, base runs out of cash and aggressive loses about EUR15m of cumulative EBITDA.
- Aggressive needs 60 hires in 2027, a factory line, and 25 installers signed in the same year. The numbers work; the execution risk is not in the model.
- The client's prices are unchanged from his original model. If the market forces a lower price, gross margin at tier 1 goes further negative.
- Service pricing (EUR60/90 a year for the turbineketel) is below the Dutch market. That is upside if raised, but the current numbers understate what is possible.

## To do

Decisions for Simon and the client:
1. Base raise: EUR3m gives 0.4 months of cover at the low point. Raise more (about EUR4.3m gives 2-3 months), hire slower, or accept it knowingly.
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
