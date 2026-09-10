# Tarnoc: what was done on Monday 7 September 2026

Start of day: `Tarnoc_v2_2026-09-01.xlsx` at commit `c7c6e65`. End of day: three workbooks at commit `a131f50`.

## Model changes, in order

1. **Profitability analysis.** Base lost money through 2029 because gross margin was under 10% (turbineketel sold below its tier-1 BOM, plus 10% commission). Tested eight levers; volume past the 5,000-unit tier and two-year BOM pricing were the only ones that mattered.
2. **BOM always priced on two-year volume.** The one-year / two-year switch was removed; COGS sets the tier on this year plus next year's units in both cases.
3. **Base ramp slowed** to Simon's targets: about 300 units in 2027, 1,200 in 2028, then tripling. Set through the base marketing table (EUR13k / 40k / 115k / 160k a month).
4. **Base made to work on EUR3m.** 2028 plus 2029 volume was 4,400, under the 5,000 tier; marketing in 2028-29 lifted to put it at 5,500 so 2028 gets the EUR7,069 BOM. Then more of the raise deployed: R&D hires 4 and 3 in 2027-28, one partner a month and half a rep a month in 2027, one field engineer per 600 units (was 750). Result: 354 / 1,350 / 4,122 / 7,418 units, EBITDA positive from 2028, cash low EUR0.57m, 81% of the raise used.
5. **Aggressive rebuilt around capex**, on Simon's instruction to spend on manufacturing and to use 90% of the EUR10m: two automated lines paid November 2026 and January 2027 (EUR3m each plus EUR3m tooling), 25 operators per line instead of 35, R&D 10/16/16/16, partners 3/5/7/8 a month, reps hired ahead, marketing EUR150k-380k a month. Result: 2,812 / 6,864 / 11,730 / 18,780 units, EUR321m revenue and EUR79m EBITDA in 2030, cash low EUR0.99m in January 2027, 90% used.
6. **In-house assembly saving added, then removed** at Simon's request. The BOM is charged in full on every unit; the lines add capacity, not a cost saving. The model cannot give in-house production a cost advantage until the client says what the assembly partner charges.
7. **Model renamed** to `Tarnoc_v2_2026-09-07.xlsx`; base case is the default on opening.
8. **Summary tab added as the front page**: what the model is, how units are calculated, live results table, both cases side by side, does it make sense, all 33 market-checked assumptions with verdicts, vulnerabilities, what is still needed from the client. Redone twice during the day as the numbers moved.
9. **Fork into two single-case workbooks** from the same build script (`MODE=base` and `MODE=aggr`): single Value column on Assumptions, no switch. The base workbook has no in-house lines, capex, tooling, operators or depreciation life anywhere; its Summary and research table carry only base content. The combined workbook is kept as the master.
10. Smaller: build-capacity block marked aggressive-only; "marketing spend per marketer" relabelled as a team-sizing ratio and set to EUR1.5m; capex shown negative on the Dashboard like other costs.

## Reviews and what they found

Two independent formula-level reviews (reports in `docs/tarnoc-v2-formula-review-2026-09-07.md` and `-pass2-`), plus a stress test of ten input shocks. Fixed:

- Dashboard revenue per person divided by an empty row (showed 0).
- Annual margin columns averaged monthly ratios (2026 gross margin showed 8% instead of 100%); now recomputed from annual totals.
- Annual opening cash took December's opening balance; annual cash flow did not tie.
- Months-of-cover always divided by 2028 opex; five Dashboard cells hardcoded October 2026 as the raise month.
- Receivables were charged on the subsidy; overheads, training and recruitment were not inflated although the label said they were.
- Funding dates matched on the exact day (a mid-month date silently deleted the round); now month-based, with a new check row that funding received equals the inputs.
- No warning when cash went negative or a check broke; cash, check rows and Dashboard funding cells now turn red.
- Pre-raise cash low was invisible; added. Marketing could be spent before the first sellable month; gated.
- Average cost per person understated in growth years; now cost over person-months.
- An unused "hiring starts from" input; six stale notes and labels; the Cover pointing at the wrong first tab.

Confirmed correct: all 60-month formula patterns, all cross-sheet links, all lookups, the units-sold gate, commission and service timing, capex lag, depreciation, tax with loss carry-forward, the frozen 2026 plan against the client's model to the euro, Excel and Google Sheets compatibility.

## A failure to record

Two of the audit's four phases (the shadow model and the identities check) crashed silently from about 09:30 to 11:45. A renamed label and a missing line break broke the shadow model; a SUM range broke the identities evaluator; the audit runner read an empty result as a pass. Every "audit passed" reported in that window covered only formula errors, balance sheet ties and structure. The runner now fails loudly when a phase crashes or returns nothing, both scripts are fixed, and the full four-phase audit passed on all three workbooks at end of day. The model itself was not wrong in that window; the check on it was.

## Decisions Simon made today

- BOM always on two-year volume. Base ramp 300 / 1,200 / tripling. Aggressive to about 20,000 units by 2030 with the money going into manufacturing capex, using at least 90% of the EUR10m. No in-house cost saving in the model. Field engineers on a richer ratio. Small R&D increase in base. Two separate workbooks.

## Still open

- Aggressive has six weeks of cash cover at its low; 90% use and 2-3 months of cover cannot both hold at EUR10m.
- From the client: supplier quotes and the two-year commitment; what the assembly partner charges per unit; the installer deal; a view on the direct-to-installer path and on 18,800 units.
- Model work: Drive upload of the current files; a sensitivity table; linking hiring to the raise date; other cost inflation still 10%; retiring model A.

Reference documents: `docs/tarnoc-v2-summary-2026-09-07.md` (how the model works, outcomes, vulnerabilities), `docs/tarnoc-assumptions-research-2026-09-04.md` (market evidence).

## Later on 7 September: whole people

Simon asked whether we can hire half a rep. We could not, and the model was doing it.

`Revenue Forecast` row 16 took the hire rate straight from the Assumptions table and row 17 accumulated it, so base 2027 ran 1.5, 2.0, 2.5 reps. Installer partners had the same problem in base 2028, where the signing rate is 1.5 a month. Base showed a fractional headcount in 33 of the 60 months, aggressive in 15. Reps and partners were the only rows affected; every ratio-driven role was already rounded.

Fixed by keeping the rate on row 16 (relabelled "Rep hiring rate", and row 19 "Partner signing rate") and flooring the running total on rows 17 and 20, so half a rep a month means one rep every second month. The shadow model in `scripts/audit_v2_shadow.py` was changed to match. All three workbooks rebuilt and re-audited, four phases, 114 of 114 rows agreeing.

Effect on the numbers, all in the base case: 2028 units 1,350 to 1,344, 2030 units 7,418 to 7,407, 2030 revenue EUR126.5m to EUR126.3m. Fewer rep-months means slightly lower cost, so 2027 EBITDA improves from -2.52m to -2.50m and 2028 from +0.84m to +0.86m. Cash low rises from EUR571k to EUR599k, cover from 2.2 to 2.3 months, and the raise used falls from 81% to 80%. Aggressive volumes and cash low are unchanged; 2029 and 2030 EBITDA rise by about EUR30k and EUR50k. The 2028 plus 2029 volume that clears the 5,000 tier is now 5,466 rather than 5,472.

Two stale figures in `docs/tarnoc-v2-summary-2026-09-07.md` were corrected at the same time: partner counts needed by 2029 (67 base and 181 aggressive, not 145 and 260) and aggressive headcount (90 in 2027 and 302 in 2030, not 89 and 289).

## The real problem, and the fix for it

Simon's point was that the half rep should never have reached him, and that he cannot present a model that produces mistakes of that kind. He is right, and the half rep was a symptom.

The audit had four phases: formula errors, an independent shadow model cell by cell, accounting identities, and structure. All four check whether the workbook is internally consistent. None of them asked whether the answer was possible. The shadow model reimplemented the same fractional-hiring logic, so it agreed with the workbook, and the audit passed.

A fifth set of checks was added inside phase 3, called REALITY CHECKS. They test what has to be true of the business whatever the formulas say:

- People, installer partners, partner managers, production lines and units are whole numbers. Every headcount row on Personnel, every unit row on Revenue Forecast and the three volume rows on COGS.
- Reps in post and partners on the books never fall, because the plan never fires anyone.
- Cash never goes below zero.
- Revenue per unit sold stays between EUR5k and EUR40k in any month we sell.
- Gross margin stays between -100% and 100%.
- People cost per head stays between EUR2k and EUR20k a month.
- Tax never exceeds the statutory rate on profit before tax.
- Share sold direct stays between 0% and 100%.
- The installed base equals cumulative units sold, because nothing is retired.

Run against the pre-fix workbook (commit `b2b3d8b`) the new phase fails it on seven rows, first month January 2027, which is the behaviour we want. Run against the rebuilt workbooks it passes.

It also found a second defect straight away that nobody had spotted: the TTK and Combi+ split multiplied units by 20% and 80%, so January 2027 sold 4.8 turbineketels and 19.2 Combi+ units. TTK is now rounded and Combi+ takes the remainder, so the two always add to units sold and both are whole. The shadow model was changed to match.

Effect of that second fix, base: 2027 revenue EUR5,995,461 to EUR5,994,199, 2028 EUR22,813,647 to EUR22,812,385, 2030 EUR126.29m to EUR126.28m, 2028 EBITDA EUR858,070 to EUR857,334, cash low EUR599,214 to EUR598,473, cover 2.34 to 2.33 months. Aggressive: 2027 revenue EUR47,610,111 to EUR47,612,635, 2028 EBITDA EUR22,782,769 to EUR22,801,049, cash low unchanged at EUR994,454. Volumes unchanged in both.

All three workbooks rebuilt and passed the full audit, now five phases of checks, 114 of 114 shadow rows agreeing.

## Phase 5: the input sweep

Every other phase tests one point in input space, the assumptions exactly as they are typed. A model can be correct there and wrong when the client triples the marketing budget. `scripts/audit_v2_sweep.py` samples 33 inputs across plausible ranges (marketing 0 to 5x, cost per lead 0.4 to 3x, close rates 5% to 95%, quota 0.25 to 2x, partner capacity, all prices, the service and upsell baskets, the staffing ratios, DSO 0 to 120 days, DPO 0 to 150, tax 0 to 40%, salary inflation 0 to 20%) and runs the model on every draw.

It separates two things that are not the same:

- **Model fault.** Something that cannot be true of any business: a fractional person, a count going backwards, an identity breaking, units above the constraint that set them, tax as a credit, a product split that does not add to units sold. This is a bug.
- **Plan fails.** The arithmetic is right and the business runs out of money. Not a bug, reported separately so the two are never confused.

Result: 2,000 draws on each of the base and aggressive workbooks, 4,000 in total, **zero model faults**. The plan runs out of cash in 73% of base draws and 75% of aggressive draws, which is what a EUR3m and a EUR10m raise should look like when the inputs are pushed that hard.

Two guards were built in after the sweep's own first version reported a confident pass off a broken baseline:

- **Baseline guard.** Seven assumption cells are themselves formulas (the Combi+ price, the product split, the upsell and service baskets). Read off a workbook that openpyxl built, they come back empty and every number after them is wrong. The sweep now recalculates in LibreOffice first and refuses to run unless the unperturbed draw matches the workbook's closing cash in all 60 months. It matches to 0.0000.
- **Self test.** A checker that never fires cannot be told apart from one that works. Before sweeping, the script takes the good run, breaks one number at a time in twelve different ways, and requires all twelve to be caught and the good model to raise nothing. All twelve are caught.

The sweep is now phase 5 of `scripts/audit_v2.py`, 300 draws by default, about 15 seconds on top of the rest. `SWEEP_DRAWS=2000` before anything goes to the client, `SWEEP_DRAWS=0` to skip.

What this does not cover, and should be said plainly: the sweep tests the logic, not the assumptions. A 50% BOM cost-down is either achievable or it is not, and no audit will ever settle that. Only a supplier quote will.

# 10 September 2026: scenario tab

Simon asked for a scenario analysis on its own tab in the base workbook: three scenarios, key outcomes side by side.

## Choosing what to flex

Before designing it I ran a one-at-a-time sensitivity, moving each input 20% each way and measuring the swing in 2030 EBITDA. Ranked:

| Input | 2030 EBITDA swing |
| --- | --- |
| BOM cost across the three tiers | EUR17.5m |
| Assembly partner capacity | EUR7.9m |
| Orders per partner per month | EUR5.8m |
| Partners signed per month | EUR5.3m |
| Turbineketel price | EUR4.7m |
| Close rate, lead quality | EUR4.3m each |
| Cost per lead | EUR4.0m |
| Marketing spend | EUR3.4m |
| Installer commission | EUR2.6m |
| Rep quota, units per partner, debtor days | nil |

Rep quota moves 2030 EBITDA by EUR284 and units per partner and debtor days by nothing, because demand is the binding constraint in every month of the base case and the plan uses 8% of its selling capacity. Those are not in the tab; a flat row would read as a broken model.

The sensitivity also showed the shape of the downside. A 20% cut to any single demand lever drops 2028 plus 2029 volume below 5,000, which loses the middle BOM tier, and the case then runs out of cash. It is a threshold, not a gradient.

## What was built

`scripts/build_scenarios.py`, run after the main build. It recalculates the workbook, runs the shadow model three times with different assumption sets, and writes a Scenarios tab as sheet 2 of the base workbook.

Eight rows of inputs in pale yellow (BOM cost-down achieved, marketing spend, cost per lead, close rate, partners signed, orders per partner, assembly capacity, turbineketel price), then volume, profit and cash blocks, then two native Excel charts (EBITDA by year as clustered columns, cash balance by month as lines) with their data written out in a labelled block below so the charts can be checked against numbers.

Results:

| | Downside | Plan | Upside |
| --- | --- | --- | --- |
| Units 2030 | 3,391 | 7,407 | 11,333 |
| 2028 plus 2029 volume | 2,428 | 5,466 | 9,915 |
| Clears the 5,000 tier | No | Yes | Yes |
| Gross margin 2030 | 15% | 37% | 37% |
| EBITDA 2030 | -1.3m | +33.6m | +55.1m |
| First profitable year | none by 2030 | 2028 | 2028 |
| Lowest cash after the raise | -4.57m | +0.60m | +1.16m |
| Months of cover | -7.6 | 2.3 | 4.3 |
| Needs more than EUR3m | Yes, EUR4.6m more | No | No |

## Two guards

The script refuses to write the tab unless the Plan column reproduces the live workbook on 2030 units, revenue and EBITDA. And row 39 in the tab recomputes the live model and subtracts the stored Plan column; it reads nil today and conditional formatting turns it red if it ever does not. That covers the one weakness of storing values rather than formulas.

The full five-phase audit passes on the workbook with the tab in it.

## A note on wording

Simon called out the phrase "15% is the tier it never escapes" in the mock-up as meaningless. He is right, and it was one of several. Every note in the tab now states a fact: what the number is, what the client's figure is, what the benchmark is, what happens below the threshold. No metaphors.
