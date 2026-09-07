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
