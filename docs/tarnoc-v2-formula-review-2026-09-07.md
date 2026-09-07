# Independent review — Tarnoc_v2_2026-09-01.xlsx

Reviewer: no involvement in the build. Method: every formula on all nine tabs dumped and
normalised to R1C1 relative form to test that all 60 monthly columns of each row share one
pattern; every cross-sheet reference resolved to the label of its target row; the workbook
recalculated with LibreOffice headless in both cases (Assumptions E5 = 1 and E5 = 2) and the
resulting numbers re-derived by hand where they matter.

Scope confirmed: 60 monthly columns E..BL (Jan-2026 to Dec-2030), annual columns BN..BR
(2026..2030), notes in BT. Row 3 date headers are byte-identical across Financial Statements,
Revenue Forecast, COGS, OPEX and Personnel, so column alignment between tabs is sound.

---

## (A) Confirmed defects

### A1. Dashboard `D26:H26` "Revenue per person" divides by an empty row — HIGH

```
D26 = IFERROR(D14/D25,0)
```

Row 25 of Dashboard is completely empty (B25 through H25 are `None`). The headcount row is
row 24 (`=Personnel!BN20`). The division is by a blank cell, `#DIV/0!` is swallowed by the
`IFERROR`, and the metric reads **0 in all five years, in both cases**. The note in J26
("Viessmann runs at about EUR276k and Vaillant about EUR200k") invites the reader to compare
against a number that is structurally nil.

Recalculated: D26:H26 = 0,0,0,0,0 (base) and 0,0,0,0,0 (aggressive). True 2030 base value
would be 125,687,821 / 87 = EUR1.44m per person — which is itself implausible and would have
been caught had the cell worked (see B6).

Fix: `D26 = IFERROR(D14/D24,0)`, copied across E26:H26.

### A2. Annual margin rows average monthly ratios instead of recomputing — HIGH

Affected cells: `Financial Statements` BN9:BR9 (Gross margin), BN17:BR17 (EBITDA margin),
BN24:BR24 (Net margin); `OPEX` BN35:BR35 (Operating expenses as a share of revenue).
Pattern in all of them:

```
BN9 = IFERROR(AVERAGE(E9:P9),0)
```

Each monthly cell is itself a ratio with `IFERROR(...,0)`, so a zero-revenue month contributes
a 0 to the average rather than being excluded. Recalculated, base case:

| Year | GM reported | GM true | EBITDA mgn reported | EBITDA mgn true | Opex/rev reported | Opex/rev true |
|---|---|---|---|---|---|---|
| 2026 | 8.3% | **100.0%** | -2.5% | **-1634.2%** | 10.9% | **1734.2%** |
| 2027 | 9.72% | 9.73% | -20.18% | -19.45% | 29.89% | 29.18% |
| 2028 | 7.58% | 7.58% | -7.84% | -7.79% | 15.42% | 15.37% |
| 2029 | 6.55% | 6.55% | -4.30% | -4.24% | 10.84% | 10.79% |
| 2030 | 24.02% | 24.02% | 15.04% | 15.05% | 8.98% | 8.97% |

2026 is wrong by three orders of magnitude (only one of twelve months has revenue: the
EUR106,782 subsidy in August). 2027 EBITDA margin is out by 73bp. Both errors are relayed
verbatim to the Dashboard at `D16:H16` and `D19:H19`, which are the headline margin lines a
reader sees first.

Fix: recompute from the annual totals, e.g. `BN9 = IFERROR(BN8/BN6,0)`, `BN17 = IFERROR(BN16/BN6,0)`,
`BN24 = IFERROR(BN23/BN6,0)`, `OPEX!BN35 = IFERROR(BN33/'Revenue Forecast'!BN50,0)`.

### A3. `Financial Statements` BN39:BR39 takes December's opening cash as the year's opening cash — MEDIUM

```
BN39 = P39      BO39 = AB39      BP39 = AN39      BQ39 = AZ39      BR39 = BL39
```

Row 39 is "Cash at the start of the month" — a period-opening balance, not a stock at
period end. The annual column must take the FIRST month of the year, not the last. As built,
BN39 = 2,852,562 (cash at the start of December 2026) when the cash at the start of 2026 is
853,120. Consequence: the annual cash flow statement does not articulate. End cash minus
start cash minus movement in cash, by year:

```
2026  -1,999,442      2027  +1,140,120      2028  +832,808      2029  +22,168      2030  -15,568,169
```

A reader tying BN38 (movement) to BN40 - BN39 finds a EUR15.6m hole in 2030.

Fix: `BN39 = E39`, `BO39 = Q39`, `BP39 = AC39`, `BQ39 = AO39`, `BR39 = BA39`.
(BN40:BR40, the closing balance, correctly takes December and needs no change.)

### A4. Dashboard `D53` hardcodes 2028 opex regardless of when the low point falls — MEDIUM

```
D53 = IFERROR(D37/(-'Financial Statements'!BP14/12),0)
```

`BP14` is the 2028 annual operating expense column. `D37` is the lowest cash balance after
the raise and `D38` already identifies the month it happens. The two are not connected.

- Base case: low point Dec-2029; D53 reads **0.69 months**; using the 2029 opex column (BQ14)
  gives 0.44 months.
- Aggressive case: low point Dec-2027; D53 reads **4.24 months**; using the 2027 opex column
  (BO14) gives 10.2 months — a 2.4x error on the metric the note calls the funding test
  ("a plan of this size wants three months or more here").

Fix: drive the divisor off the year of `D38`, e.g.
`=IFERROR(D37/(-HLOOKUP(YEAR(D38),'Financial Statements'!$BN$3:$BR$14,12,FALSE)/12),0)`.

### A5. Dashboard `D37`, `D50`, `D52` hardcode column N as "the month the raise lands" — MEDIUM

```
D37 = MIN('Financial Statements'!$N$40:$BL$40)
D50 = 'Financial Statements'!N40
D52 = IFERROR(D51/SUM('Financial Statements'!N35:BL35),0)
```

Column N is October 2026 only because `Assumptions!F140` currently says 2026-10-01. Nothing
ties these three cells to that input. Move the second round by one month and all three
silently misreport: D50 would show the pre-raise balance, D37 would include a pre-raise
month, and D52 would divide by both rounds instead of the second. `D38` (the month of the low
point) shares the same window and the same `+9` offset (`MATCH(...)+9`), which is arithmetically
correct for a window starting at N but breaks with it.

Also note `D51` and `D52` are then wrong in the same way, since they are built on D50 and D37.

Fix: derive the start column with `MATCH(Assumptions!F140,'Financial Statements'!$E$3:$BL$3,0)`
and use `OFFSET`/`INDEX` windows, or at minimum add a visible note that these four cells are
pinned to an October-2026 raise.

### A6. Receivables are calculated on revenue that includes the subsidy — MEDIUM-LOW

```
E44 = Assumptions!$F$19/30*E6
```

Row 6 is total revenue, which includes row 49 of Revenue Forecast, the EUR106,782 subsidy
booked in August 2026 (`Assumptions!F16`/`F17`). At DSO 20 this parks **EUR71,188 of
receivables** on the August 2026 balance sheet and pushes two-thirds of the subsidy cash into
September. Recalculated: `L29` (movement in receivables, Aug-2026) = -71,188, `M29` = +71,188,
`L44` = 71,188. The Assumptions label is "Subsidy received", i.e. a cash event, so a
receivable against it is not intended.

The same base also includes the installation pass-through, which is arguably fine, but the
subsidy is not.

Fix: base row 44 on trading revenue only — `=Assumptions!$F$19/30*(E6-'Revenue Forecast'!E49)`.

### A7. `Assumptions!F135` "Annual increase on the costs above" is applied to only 4 of the 9 cost lines above it — MEDIUM-LOW

The escalator is used in exactly four places, all with `(1+Assumptions!$F$135)^(YEAR(E$3)-2026)`:
OPEX rows 17 (Ongoing development, F133), 18 (Third party product development, F134),
25 (Finance and legal, F131), 26 (Other general, F132).

It is **not** applied to:
- `Assumptions!F126` Offices and facilities per person, `F127` IT and software per person,
  `F128` Travel per person — consumed flat by `OPEX!E22 = Personnel!E20*(F126+F127+F128)`.
- `Assumptions!F130` Installer training and demo unit per new partner — consumed flat by
  `OPEX!E13`.
- `Assumptions!F129` Recruitment per net new hire — consumed flat by `OPEX!F23`.

The label sits under all nine rows and claims all of them. At 10% a year over five years the
per-person overhead lines are understated by ~46% by 2030 (EUR1,250/person/month held flat
instead of rising to EUR1,830).

Fix: either apply the escalator to rows 22, 13 and 23 of OPEX, or rename `Assumptions!B135`
to name the four lines it actually touches.

### A8. `Assumptions!B12` is labelled "working capital loan" but the rate is charged on the convertible loan — LOW

`Financial Statements!F20 = -E51*Assumptions!$F$12/12`, where row 51 is "Loan outstanding",
fed only by row 36 "Loan drawn" = `Assumptions!F142` "Convertible loan drawn". There is no
working capital facility anywhere in the model. The rate row and the instrument row describe
different things.

Related, and worth a decision rather than a fix: the convertible loan is never converted and
never repaid (row 51 only ever accretes draws), and the interest is expensed and treated as
paid in cash rather than accrued into the balance. Interest recalculates correctly at
EUR1,250/month from August 2026 (5% on 300k, charged on the opening balance), 2026 total
EUR6,250, 2027 onward EUR15,000 — the arithmetic is right, the instrument is just never
resolved.

### A9. OPEX `O38:BL43` are typed zeros carrying the pale-yellow input fill — LOW

The frozen 2026 block occupies rows 38-43, columns E..N (January to October). Columns
O..BL of those six rows hold typed `0` and are filled `FFFFF2CC`, the same pale yellow the
"How to read me" legend and `Assumptions!B2` declare as "the only cells to change". Those 300
cells are never read: `OPEX!E6`, `E7`, `E8`, `E14`, `E19`, `E27` only consult rows 38-43 when
`E$3<=Assumptions!$F$15` (2026-10-01). A user typing a November 2026 cost into `O38` would see
no effect anywhere and get no warning.

Fix: clear the fill on O38:BL43, or blank the cells.

### A10. Hardcoded constants inside grid formulas — LOW

Beyond the permitted set (0, 1, 12, 100, 1000000, lookup indexes, dates):

| Constant | Count | Where | Comment |
|---|---|---|---|
| `2026` | 420 | OPEX 17, 18, 25, 26; Personnel 26, 27, 28 | inflation/salary base year, typed into every cell rather than read from a cell |
| `30` | 180 | Financial Statements 44, 45, 50 | days-per-month divisor for DSO/DPO/DIO |
| `9` | 1 | Dashboard D38 | MATCH offset, pinned to the window starting at column N (see A5) |

The `2026` exponent base is currently correct (`(1+rate)^(YEAR-2026)` gives no uplift in 2026,
which is what the frozen plan requires), but if the model's first year ever moves, 420 cells
have to move with it.

Function inventory, for portability: ABS, AND, AVERAGE, EDATE, HLOOKUP, IF, IFERROR, INDEX,
MATCH, MAX, MIN, MONTH, ROUND, SUM, SUMIF, SUMPRODUCT, VLOOKUP, YEAR. No `_xlfn.` prefixes
anywhere; no IFNA, XLOOKUP, LET or LAMBDA. All eighteen behave identically in Excel and Google
Sheets, EDATE included. **No compatibility defects.**

---

## (B) Questionable modelling choices that are not bugs

**B1. The balance sheet check is a tautology.** `E58 = E48-E56` is the right expression, and
Dashboard `D34 = MAX(ABS(MIN(E58:BL58)),ABS(MAX(E58:BL58)))` is the right way to surface the
worst month. But cash (row 43) is derived from the cash flow, which is derived from net income
plus the same working-capital deltas that define receivables, inventory and payables; share
capital is opening cash plus cumulative raises; retained earnings is cumulative net income.
Substituting the wiring, assets minus liabilities and equity reduces to zero identically for
any values of tax, depreciation, DSO or revenue. The check reads nil (confirmed: 0.00 in all
60 months in both cases) and would keep reading nil with the tax line deleted. It confirms the
plumbing, not the numbers. A reconciliation that would bite — e.g. cumulative revenue less
cumulative cash receipts less closing receivables — is not present.

**B2. The opening balance sheet is a plug.** `E53 = Assumptions!$F$9+E35` sets opening equity
equal to opening cash (853,120) with no opening PPE, receivables, payables or accumulated
deficit. Defensible as a modelling simplification, and the note says so, but the January 2026
balance sheet is not Tarnoc's actual balance sheet.

**B3. Tax is computed monthly and losses only run one way.** `F22 = -IF(F21>0,MAX(0,F21-E64)*rate,0)`
with the pool rolled by `F64 = MAX(0,E64-MAX(0,F21))+MAX(0,-F21)`. The mechanics are correct
and tie out — 2030 tax recalculates to EUR2,560,560, exactly (18,901,861 - 8,977,211 carried
losses) x 25.8%. Two live simplifications: a profitable month inside a loss-making year would
pay tax that the year never gets back, and the Dutch 19% first bracket to EUR200k and the 50%
cap on loss utilisation above EUR1m are not modelled. Neither bites at current inputs (no
month in 2026-2029 has positive PBT), so this is exposure, not error.

**B4. Depreciation runs from the payment date, not the in-service date.** `F19 = -E63/(F90*12)`
starts the month after cash goes out, twelve months before the line can build anything. Also,
production operators (`Personnel!E13 = 'Revenue Forecast'!E29*F88`) and facility cost
(`OPEX!E24 = 'Revenue Forecast'!E29*F89`) both switch on only when the line starts producing,
so the twelve-month commissioning period carries depreciation but no staff and no facility
cost. In the aggressive case that is 3.5m of capex in November 2026 depreciating from December
2026 with the line idle until November 2027.

**B5. In-house assembly buys capacity but no unit-cost advantage.** COGS uses one BOM
(`Assumptions!D93:F95`) whether the unit is built by the assembly partner or on an owned line.
The EUR3.5m line 1 plus 35 operators plus EUR90k/month of facility earn their return only
indirectly, by lifting volume across a BOM tier. No partner assembly fee is saved. Worth
stating explicitly, because it is the whole economic case for the aggressive capex.

**B6. Revenue per person is not a like-for-like comparison.** Once A1 is fixed, base 2030
reads EUR1.44m per head against the note's Viessmann EUR276k and Vaillant EUR200k. Tarnoc's
revenue includes the installation pass-through (EUR3,600 a unit, ~21% of revenue per unit) and
the company outsources assembly for most of the horizon while the comparators employ their
assembly workforce. The metric as constructed will always flatter Tarnoc by a wide margin.

**B7. Headcount uses ROUND, not ROUNDUP, so early roles round away.** `Revenue Forecast!E23 = ROUND(E20/F78,0)`
gives **0 partner managers through all of 2027 with up to 7 partners on the books**
(7/18 = 0.39). `Personnel!E8 = ROUND('Revenue Forecast'!E19*12/F109,0)` gives **0 installer
trainers throughout 2027** (0.5 partners/month x 12 / 40 = 0.15), while the note on that row
says "every partner has to be trained and certified before selling anything". Customer support,
technical escalation, order desk, supply chain and field service all round the same way. Both
totals are correct at scale (2030 base: 6 partner managers on 106.6 partners) but the early
years staff the channel at zero.

**B8. Fractional people and fractional partners flow straight into cost.** Reps in post reach
1.25 FTE in January 2027 and installer partners 106.6 by December 2030. The rates are the
inputs (0.25 FTE/month, 3.8 partners/month), so this is intentional, but the Personnel tab
charges 1.25 x EUR7,500 and the Dashboard reports "Installer partners at year end 106.6".

**B9. Installed base never churns and service contracts renew forever.** `E41 = E7+E34` with no
attrition and no contract expiry. A unit sold in 2027 pays EUR69-159 of service revenue every
year to 2030 at a 88% attach rate that never decays.

**B10. Payables are calculated on COGS only.** `E50 = Assumptions!$F$20/30*-E7`. All operating
expense, including EUR11.3m of 2030 opex, is treated as paid in the month incurred. This is
conservative (it understates cash) but it means the DPO input governs less than half of the
cost base.

**B11. Rate rows are summed in the annual columns.** `Revenue Forecast` rows 18, 21, 22, 28,
30, 31 are labelled "units/mo" in column C and their BN..BR cells are `SUM` of twelve months,
so the annual figure is units per year under a per-month label. Same on `Personnel` rows 26-29
("EUR/mo", annual column is a twelve-month total). The arithmetic is the sensible one; the
unit labels are not.

**B12. The case switch flexes only seven inputs.** Comparing D and E across all of Assumptions,
the aggressive case changes marketing spend (48/49), reps hired (61/62), partners signed
(65/66), assembly partner capacity (81), the two in-house line dates (82/83), R&D hiring
(100/101) and the second round amount (141). Direct-sales share (57/58) and orders per partner
(69/70) have identical base and aggressive rows despite carrying the full year-table structure,
and the upsell basket (32-34), service table (39-42) and BOM tiers (93-95) have no case
variants at all. Nothing is wrong; the switch just does less than the tab's layout implies.

**B13. Notes disagree with each other on the R&D roster.** `Assumptions!J104` describes 10
engineers carried into 2027 as "the roster at the end of the committed 2026 plan"; `J122`
prices the R&D engineer at EUR5,700 as "the blended cost of the seven engineers already in
post". Ten and seven cannot both be right.

**B14. Dashboard rows 43 and 47 tie but nothing checks that they tie.** The "where the money
goes" block is algebraically closed — D44+D45+D46 must equal D43 given the wiring — and it does
(both 4,453,120 base, both 11,453,120 aggressive). The note in J47 says "ties to total money
available" but there is no cell computing the difference, so a future break would be silent.

**B15. The subsidy is booked as revenue.** `Revenue Forecast!E49` sits inside "Total revenue"
(row 50), so 2026 revenue is EUR106,782 of grant income. Row 51 correctly strips it out of
revenue per unit, and Financial Statements row 6 does not. Grant income below the gross profit
line would be more conventional.

---

## (C) Checked and found correct

**Formula consistency.** All 60 monthly columns of every row on the five grid tabs share one
normalised pattern. Seventeen rows carry a distinct first-month formula, and every one of them
is a legitimate opening-balance or prior-month-reference case (Financial Statements 19, 20, 22,
29, 30, 31, 39, 51, 53, 54, 62, 63, 64; Revenue Forecast 7, 17, 20; OPEX 23). No row breaks
mid-series. No stray typed number anywhere in the monthly or annual grid outside the two
declared input areas (OPEX 38-43 and Personnel 17).

**Annual column geometry.** BN = E:P, BO = Q:AB, BP = AC:AN, BQ = AO:AZ, BR = BA:BL on every
row of every tab — twelve months each, no overlap, no gap. December pick-ups for stocks
resolve to P, AB, AN, AZ, BL correctly.

**Aggregation by row type.** Flows summed, stocks and headcount taken at December (Financial
Statements 43-56, 62-64; Revenue Forecast 7, 17, 20, 23, 29, 41; COGS 6-8; Personnel 6-20),
prices and rates averaged rather than summed. The one row that gets the wrong end of the year
is Financial Statements 39 (A3); the four ratio rows that should be recomputed rather than
averaged are A2. Everything else is right.

**Assumptions live cells.** Every one of the 70 `Live` cells in column F is
`IF(Assumptions!$E$5=2,E<own row>,D<own row>)` — no cell points at another row's base or
aggressive value. Every `Live (per case)` row in the six year tables (50, 59, 63, 67, 71, 102)
is `IF($E$5=2,<row above>,<two rows above>)` across D..H, reading its own block. The derived
cells (F25 Combi+ price, F29 Combi+ share, F35/F36 upsell, F43/F44 service, F45 contract share)
compute from their own tables and are internally consistent — F43 = 0.2 x (0.34x60+0.54x90) +
0.8 x (0.34x150+0.54x200) = EUR159.0, F45 = 0.34+0.54 = 88%, and the 88% is applied only once
(to field service headcount), not double-counted against the attach rates already inside F43
and F44.

**Cross-sheet references.** All 160 distinct cross-sheet targets resolve to a row whose label
matches the caller's intent. Spot checks that matter: Financial Statements 6 to Revenue Forecast
50 "Total revenue"; 7 to COGS 19 "Total cost of goods sold"; 11/12/13 to OPEX 30/31/32 R&D,
S&M, G&A respectively; OPEX 6/7/8 to Personnel 26/27/28 in the same order; COGS 13/14 to
Revenue Forecast 39/40 TTK and Combi+ units. The only label mismatch found is A8.

**Lookup ranges, indexes and match modes.** The five year-table HLOOKUPs
(`Revenue Forecast` 6, 11, 15, 16, 19) all use `$D$<hdr>:$H$<hdr+3>` with index 4 — the Live
row — and `FALSE` for exact year match. Correct. The two COGS HLOOKUPs into
`'Revenue Forecast'!$BN$3:$BR$34` use index 32, which lands on row 34 "Units sold", with
`FALSE`. Correct. The two BOM VLOOKUPs use `TRUE` for the tiered lookup: `COGS!E9` reads
`$D$93:$E$95` index 2 (TTK cost) and `E10` reads `$D$93:$F$95` index 3 (Outdoor unit) — right
column each time, thresholds ascending 0 / 5000 / 10000 so approximate match is valid.
Recalculated tier behaviour: base 2027 key 579 to EUR9,984; base 2030 key 7,367 to EUR7,069;
aggressive 2030 key 15,144 to EUR4,998. Tier basis switch E6 = 1 reads row 6 only, E6 = 2 adds
row 7, and the last-year fallback works (`COGS!BA7` returns 7,367 from `IFERROR(...,E6)` when
the 2031 lookup fails).

**Units sold gate and the three-way MIN.**
`E34 = IF(E$3<Assumptions!$F$13,0,ROUND(MIN(E12,E22,E31),0))`. Zero before January 2027,
then the smallest of demand, selling capacity and build capacity. Verified binding constraint
switches: January 2027 base takes selling capacity (31.2 vs demand 48.2, build 650); September
2030 base takes build capacity (650 vs demand 664, selling 817). The mix cap in row 22,
`MIN(IFERROR(E18/E15,1000000),IFERROR(E21/(1-E15),1000000))`, handles the 2026 division by
zero (direct share = 100%) via the 1,000,000 sentinel correctly.

**Commission, service and installed base timing.** `COGS!E18` applies the rate to
(TTK revenue + Combi+ revenue) x (1 - direct share) — channel share only, system price only,
no installation, upsell or service in the base. Verified: January 2027 = (52,858.8 + 343,121.4)
x 0.2 x 0.1 = EUR7,919.6, matching the recalculated cell. Service revenue (`Revenue Forecast!E48`)
and service cost (`COGS!E17`) both read row 7, the installed base at the start of the month —
consistent with each other and correctly zero in January 2027. Installed base rolls
`E41 = E7+E34` and `F7 = E41`, no leakage.

**Frozen 2026 block handover.** All six consuming formulas use `IF(E$3<=Assumptions!$F$15,...)`
with F15 = 2026-10-01, so the ten typed months (E..N) are used and November takes over. Verified
by rebuilding November 2026 opex from the drivers by hand: 57,000 R&D people + 21,500 S&M people
+ 21,000 G&A people + 18,000 R&D other + 0 S&M other + 32,000 G&A other = EUR149,500, matching
the recalculated `O14`.

**Personnel cost coverage.** All twelve headcount rows (6-10, 12-18) are costed exactly once:
row 16 in Personnel 26, rows 6-10 in 27, rows 12, 13, 14, 15, 17, 18 in 28. Total headcount
row 20 = row 11 + row 19 picks up all twelve with no double count and no omission. Salary
inflation exponent `(1+F10)^(YEAR-2026)` gives no uplift in 2026 and compounds from 2027, which
is what the frozen plan requires.

**Capex timing and the lead-time lag.** `Financial Statements!E61` pays for each line
`EDATE(<producing date>, -F87)` = twelve months before it produces, with the one-off tooling
attached to line 1 only. Recalculated aggressive: EUR3,500,000 in column O (Nov-2026) against
a line 1 producing date of Nov-2027, EUR2,500,000 in column AI (Jul-2028) against Jul-2029.
Correct. Base case sets both dates to 2035, so capex is legitimately zero inside the horizon.
Depreciation ties: 2026 EUR36,458 (one month of 3.5m/96), 2027 EUR437,500 (twelve months),
2028 EUR567,708 (seven months at 36,458 plus five at 62,500). All three re-derived by hand.

**Equity, loan and retained earnings roll-forwards.** Recalculated: EUR300,000 in May 2026
(column I) and EUR3,000,000 in October (column N) against Assumptions 138-141; EUR300,000 loan
in July (column K) against 142-143; share capital steps 853,120 to 1,153,120 to 4,153,120 and
holds; the loan draw correctly does not touch share capital; retained earnings rolls
`F54 = E54+F23` to -1,751,308 at December 2026, matching the sum of twelve monthly net income
figures.

**Working capital mechanics.** Movement rows 29, 30, 31 carry the right sign (an increase in
receivables is a cash outflow, an increase in payables an inflow) and telescope from zero in
the first month. Payables = DPO/30 x COGS produces the right sign from a negative COGS row.
DIO = 0 so inventory is nil throughout, as the note claims.

**Dashboard wiring.** Every figure is a link or a formula against another tab's annual column —
no hardcoded values. All row targets match their labels. `D34`'s worst-month logic
(`MAX(ABS(MIN(...)),ABS(MAX(...)))`) is the correct two-sided test and reads 0.00. `D38`'s
`MATCH(...)+9` offset is arithmetically right for a window starting at column N. The remaining
Dashboard defects are A1, A4 and A5.

**Excel / Google Sheets compatibility.** Clean. Eighteen functions, all natively available in
both, no `_xlfn.` prefixes, no volatile functions, no array formulas, no dynamic-array
spilling. EDATE (240 uses) behaves identically in Sheets. Gridlines are off on all nine tabs
and the pale-yellow input convention matches the "How to read me" legend everywhere except
A9.
