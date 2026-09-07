# Tarnoc v2: how the model works, outcomes, vulnerabilities

Written 2026-09-07, end of day. Replaces `tarnoc-v2-summary-2026-09-04.md`.
Model: `models/Tarnoc_v2_2026-09-07.xlsx` at commit `98a119b`. Build: `scripts/build_tarnoc_v2.py`. Check: `python3 scripts/audit_v2.py models/Tarnoc_v2_2026-09-07.xlsx`.
The Drive copy `Tarnoc_v2_2026-09-03.xlsx` is behind everything since 3 September; upload the local file as a new version before sharing.

## How it works

Monthly, January 2026 to December 2030. Two cases on one switch (Assumptions E5): base with a EUR3m raise, aggressive with EUR10m. The file opens on base and on a Summary tab that carries this text and a live results table.

Every figure is calculated from the Assumptions tab. The only typed numbers are the assumptions, the committed 2026 plan (OPEX rows 38-43, January to October) and the back-office headcount (Personnel row 17).

Units sold in a month = the lowest of three numbers:
1. Demand = marketing spend / EUR120 per lead x 50% qualified x 40% won, plus installer partners on the books x the orders they bring in themselves (1 a month each in 2027, 2, 3, then 4 by 2030). No marketing before the first sellable month, January 2027.
2. Selling capacity = reps x 20 units a month for the direct share, partners x 8 a month for the rest. Direct share 80% in 2027, 50% in 2028, 35% in 2029, 30% in 2030.
3. Build capacity = assembly partner (650 a month base, 1,000 aggressive) plus 1,000 a month per in-house line once producing. Base has no lines. Aggressive pays for two automated lines in November 2026 and January 2027 (EUR3m each plus EUR3m tooling), producing from November 2027 and January 2028.

Revenue = units x price (EUR8,526 turbineketel, EUR13,836 Combi+, 20/80 mix) + upsell + installation passed through at cost + service contracts on the installed base (88% attach, EUR60 to 200 a year).

Cost of sales = BOM at the volume tier (EUR9,984 below 5,000 units, EUR7,069 from 5,000, EUR4,998 from 10,000) + outdoor unit + shipping + upsell cost + installation + service parts + 10% commission on channel sales. The tier is set on this year plus next year's units, in both cases: a two-year volume commitment to the supplier. The BOM is charged in full on every unit whether the partner or an own line builds it; the lines add capacity, not a cost saving.

Headcount is calculated from drivers: reps and partner managers from the sales plan, support from installed base, supply chain and order desk from units, trainers from partners signed, field engineers at one per 600 units on contract, operators at 25 per running line. R&D hires and the back office are typed per year.

Working capital: DSO 20, DPO 45, no inventory (the client's figures). Wages +5% a year, other costs +10%.

## Main outcomes

| | Base, EUR3m | Aggressive, EUR10m |
| --- | --- | --- |
| Units 2027 / 2028 / 2029 / 2030 | 350 / 1,350 / 4,100 / 7,400 | 2,800 / 6,900 / 11,700 / 18,800 |
| Revenue 2030 | EUR127m | EUR321m |
| Gross margin 2027 / 2028 / 2029 / 2030 | 10% / 25% / 37% / 37% | 28% / 38% / 37% / 37% |
| EBITDA 2027 / 2028 / 2029 / 2030 | -2.5m / +0.8m / +18m / +34m | +4.8m / +23m / +45m / +79m |
| Headcount end 2030 | 95 | 301 |
| Cash low after the raise | EUR0.6m, Dec 2027, about 2 months of opex | EUR1.0m, Jan 2027, about 6 weeks of opex |
| Share of the raise used | 81% | 90% |
| Cash end 2030 | EUR43m | EUR123m |

Gross margin steps from about 10% to 25% the year two-year volume passes 5,000 units, and to 37% past 10,000. In base that happens in 2028 and 2029; in aggressive in 2027 and 2028.

## Does it make sense

Mechanically, yes. Both cases pass the full audit: no formula errors, balance sheet ties in every month, funding received equals the funding inputs, 116 rows agree with an independent re-implementation, every cross-sheet link lands where it should. Two independent formula-level reviews on 7 September found 20-odd defects, all fixed; their reports are in `docs/`.

Commercially, it holds together on one condition and has three soft spots.

The condition: the supplier prices the BOM on two-year volume. Without that, 2027 and 2028 are priced at EUR9,984 a unit, both cases lose a year of margin, and base does not close on EUR3m.

The soft spots:
1. Base turns on about 500 units. 2028 plus 2029 volume is 5,500 against the 5,000 tier. Below it, 2028 costs EUR2,900 more per unit, EBITDA 2028 goes back to about -3m and cash below zero.
2. Aggressive spends EUR9m on lines that, as modelled, save nothing. The BOM is the same whichever line builds the unit, so the lines cost operators, facility and capex for capacity the plan barely uses until 2030. The investor question is "why build" and the answer has to be strategic (control, quality, independence from one partner) or a partner fee the client has not yet told us.
3. Aggressive is profitable in its first selling year (EUR4.8m in 2027 on 2,800 units) because two-year volume puts 2027 straight into the second BOM tier. That is what the arithmetic says; it is also the kind of first year an investor will not believe without the supplier contract in hand.

## Assumptions to be careful with

1. BOM cost-down from EUR9,984 to EUR4,998 (50%). Learning-curve evidence for heat pumps supports about 30%. No supplier quote yet. Everything rests on this.
2. Two-year volume pricing. See above.
3. Service attach 88%. Market data: 76% of new buyers hold a contract.
4. Rep quota 20 units a month. HVAC and solar benchmarks 6 to 10. Matters in 2027-28.
5. 20% lead-to-order at EUR600 of marketing per customer. The client's number, at the top of published benchmarks.
6. No warranty reserve beyond the 3% inside the BOM. Peers carry 1.5 to 3.5% of revenue.
7. Direct share falling to 30% by 2030 needs 145 (base) to 260 (aggressive) active installer partners by 2029.
8. Aggressive headcount: 16 to 89 people in 2027, 289 by 2030 at EUR1.1m revenue per head. Incumbents run EUR200-330k; outsourced assembly and pass-through installation explain some of the gap, not all.

## Where the plan is vulnerable

- Base: the 5,000-unit cliff in 2028 and two months of cash cover in December 2027. Base now hires 4 and 3 R&D engineers in 2027-28, signs 1 partner a month in 2027, hires 0.5 reps a month in 2027 and runs one field engineer per 600 units (81% of the raise used, Simon's instruction of 2026-09-07).
- Aggressive: six weeks of cash cover in January 2027 after EUR9m of capex, with the first unit sold that same month. Any slip in the raise, the lines or the launch and the plan needs more money. Simon asked for both 90% use of the raise and 2-3 months of cover; at EUR10m only one can hold.
- Both: the turbineketel sells below its tier-1 BOM. A forced price cut makes the first tier worse.
- Service prices for the turbineketel (EUR60 and EUR90 a year) sit below the Dutch market. Upside if raised.

## Still needed from the client

1. Supplier quotes behind the three BOM tiers, and confirmation the supplier will price on a two-year volume commitment.
2. What the assembly partner charges per unit and whether it is inside the BOM tiers.
3. Confirmation of the installer deal: 10% of the unit price on top of the installation fee.
4. A view on the direct-to-installer shift (80 / 50 / 35 / 30% direct) and on 18,800 units by 2030 for the aggressive case.

## To do

Decisions:
1. Aggressive raise: EUR10m with six weeks of cover, or EUR11-12m with 2-3 months.
2. Warranty reserve back in or not; service prices; attach rate.

Model work, not started:
3. Upload the current file to Drive as a new version of `Tarnoc_v2_2026-09-03.xlsx` (Simon drags it in).
4. Sensitivity table on the Dashboard: 2028+2029 volume against the 5,000 tier, close rate, orders per partner, raise size.
5. Link the Personnel back-office row and R&D hiring to the raise date, so a slipped raise slips the hiring.
6. Other cost inflation is 10% a year; research supports 3-5%. Left on instruction.
7. Retire model A once the client has been walked from A to B; update `docs/tarnoc-handover-2026-09-02.md`.

Evidence for every assumption: `docs/tarnoc-assumptions-research-2026-09-04.md`. Formula reviews: `docs/tarnoc-v2-formula-review-2026-09-07.md` and `-pass2-`.
