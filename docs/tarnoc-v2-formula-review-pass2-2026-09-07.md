# Second independent review — Tarnoc_v2_2026-09-01.xlsx

Reviewer: no involvement in the build, no involvement in the first review.
Method: all formulas dumped from the live file; the workbook recalculated with LibreOffice
headless in 19 configurations (base, aggressive, both switches, and 16 single-input stress
tests); every recalculated workbook scanned for error values, non-nil balance checks,
negative headcount, negative units and constraint breaches; Dashboard, Summary,
"How to read me", Cover, all BT notes and all Assumptions J notes read against the formulas.

**File note.** `models/Tarnoc_v2_2026-09-01.xlsx` was overwritten at 10:36 while this review
was running. The change was the addition of one new tab, **Summary** (10 tabs now, not 9),
which is the first tab and the workbook's active tab. Nothing else changed: a cell-by-cell
diff of the pre-10:36 and post-10:36 files shows 92 added cells, all on Summary, and zero
changes anywhere else. Everything below refers to the current file (md5 02ae9b39…).
The first review and the review brief both describe a 9-tab workbook and neither covers
Summary; Summary is therefore reviewed here for the first time.

Scope confirmed: monthly E..BL (Jan-2026 to Dec-2030), annual BN..BR (2026..2030), notes BT.
Row 3 dates are byte-identical across Financial Statements, Revenue Forecast, COGS, OPEX and
Personnel. Annual geometry BN=E:P, BO=Q:AB, BP=AC:AN, BQ=AO:AZ, BR=BA:BL on every row.

---

## (A) Fixes verified

### A1 — Dashboard revenue per person divides by an empty row — **FIXED**
```
D26 = IFERROR(D14/D24,0)      (E26..H26 same pattern)
```
Row 24 is "Total headcount" (`=Personnel!BN20`). Recalculated base: 6,674 / 408,589 /
852,005 / 1,216,417 / 1,444,688. Aggressive: 6,674 / 370,053 / 729,945 / 803,424 / 1,010,825.
The cell now works. The first review's B6 objection stands: at EUR1.44m per head against the
note's Viessmann EUR276k the comparison in J26 is still not like-for-like.

### A2 — Annual margin rows averaged monthly ratios — **FIXED**
```
'Financial Statements'!BN9  = IFERROR(BN8/BN6,0)
'Financial Statements'!BN17 = IFERROR(BN16/BN6,0)
'Financial Statements'!BN24 = IFERROR(BN23/BN6,0)
OPEX!BN35                   = IFERROR(BN33/'Revenue Forecast'!BN50,0)
```
All four recompute from annual totals across BN..BR. Recalculated base 2027 gross margin
9.73% (was 9.72%), EBITDA margin -19.87% (was -20.18%), opex/revenue 29.60%. 2026 now
returns the arithmetically correct 100.0% / -1634.2% / 1734.2%. See new defect **B9** — the
arithmetic is right but the presentation is not.

Four further ratio rows that the first review did not list also recompute correctly from
annual totals, so the pattern was applied consistently:
```
'Revenue Forecast'!BN24 = IFERROR(BN34/BN22,0)      selling capacity used
'Revenue Forecast'!BN35 = IFERROR(BN34/BN31,0)      build capacity used
'Revenue Forecast'!BN51 = IFERROR((BN50-BN49)/BN34,0)   revenue per unit
COGS!BN21 = IFERROR(('Revenue Forecast'!BN50-BN19)/'Revenue Forecast'!BN34,0)
```
`Personnel!BN31` was also changed and is the one that is wrong — see **B5**.

### A3 — Annual opening cash took December — **FIXED**
```
BN39 = E39   BO39 = Q39   BP39 = AC39   BQ39 = AO39   BR39 = BA39
```
Recalculated base: 853,120 / 2,701,812 / 1,367,128 / 238,791 / (250,725).
Annual `row40 − row39 − row38` is now 0.00 in all five years in both cases. The EUR15.6m
2030 hole is gone.

### A4 — Dashboard "months of operating cost" hardcoded 2028 — **FIXED**
```
D53 = IFERROR(D37/(-HLOOKUP(YEAR(D38),'Financial Statements'!$BN$3:$BR$14,12,FALSE)/12),0)
```
Index 12 into a range starting at row 3 lands on row 14 "Total operating expenses". Correct.
Aggressive now reads 9.79 months (2027 opex, low point Dec-2027) against the 4.24 the first
review found. Base reads -0.39 (see **B3**).

One consequence worth knowing: when the low point falls in 2026 the divisor becomes the
frozen 2026 plan. With both switches at 2 the low point is Dec-2026 and D53 reads
**40.2 months**, which is arithmetically what the formula asks for and economically
meaningless, because 2026 opex is EUR154k a month and 2028 opex is EUR1.2m a month.

### A5 — Dashboard pinned column N as the raise month — **FIXED**
```
D37 = MIN(INDEX('Financial Statements'!$E$40:$BL$40,
            MATCH(Assumptions!$F$140,'Financial Statements'!$E$3:$BL$3,0))
        : INDEX('Financial Statements'!$E$40:$BL$40,60))
D38 = INDEX('Financial Statements'!$E$3:$BL$3, MATCH(D37, <same window>,0)
        + MATCH(Assumptions!$F$140,'Financial Statements'!$E$3:$BL$3,0) - 1)
D50 = INDEX('Financial Statements'!$E$40:$BL$40,
            MATCH(Assumptions!$F$140,'Financial Statements'!$E$3:$BL$3,0))
D52 = IFERROR(D51/SUM(INDEX('Financial Statements'!$E$35:$BL$35, MATCH(...))
        : INDEX('Financial Statements'!$E$35:$BL$35,60)),0)
```
All four now follow `Assumptions!F140`. Verified: moving the second round to 2026-11-01 moves
D50 from 3,003,312 to 2,852,562; moving it to 2027-03-01 moves it to 2,686,064. The `+9`
offset is gone. The window-start logic itself, however, is the source of new defect **B4**,
and the unguarded `MATCH` is the source of **B1**. The `60` end-of-range is a new hardcode
(3 cells) replacing the old `9`.

### A6 — Receivables calculated on revenue including the subsidy — **FIXED**
```
E44 = Assumptions!$F$19/30*(E6-'Revenue Forecast'!E49)
```
BT44 note updated to "on trading revenue only; the subsidy is a cash receipt, not an invoice".
Recalculated: L44 (Aug-2026 receivables) = 0.00, L29 = 0.00, M29 = 0.00. The EUR71,188
misplacement is gone.

### A7 — Escalator applied to only 4 of 9 cost lines — **FIXED**
```
OPEX!E13 = 'Revenue Forecast'!E19*Assumptions!$F$130*(1+Assumptions!$F$135)^(YEAR(E$3)-2026)
OPEX!E22 = Personnel!E20*(Assumptions!$F$126+$F$127+$F$128)*(1+Assumptions!$F$135)^(YEAR(E$3)-2026)
OPEX!F23 = MAX(0,Personnel!F20-Personnel!E20)*Assumptions!$F$129*(1+Assumptions!$F$135)^(YEAR(F$3)-2026)
```
All three now carry the escalator, so all nine lines under `Assumptions!B135` are covered.
BT22 updated to "inflated like every other cost".

**This fix changes the answer.** Base-case 2030 opex rises from the first review's figures
to EUR12,003,403 and the base case now runs out of cash: cash at Dec-2029 is
**-EUR250,725**, with Nov-2029 at -EUR91,828. Before the fix D53 read +0.69 months, implying
a low point of about +EUR279k. The new Summary tab (B50) states this outcome explicitly, so
it is disclosed, but see **B2** and **B3** — nothing inside the calculating model flags it.

### A8 — "working capital loan" rate charged on the convertible loan — **FIXED (label)**
`Assumptions!B12` now reads "Interest on the convertible loan". The label matches the
instrument. The related open item the first review raised is unchanged: `Financial
Statements` row 51 only ever accretes draws, the loan is never converted and never repaid,
and interest is expensed as cash rather than accrued. Recalculated interest EUR1,250/month
from Aug-2026, 2026 total EUR6,250, EUR15,000 a year thereafter.

### A9 — OPEX O38:BL43 typed zeros carrying the input fill — **FIXED**
Rows 38-43 now hold exactly ten values each (E..N, Jan to Oct 2026) and the pale-yellow fill
FFFFF2CC stops at column N. O38:BL43 are empty with no fill. Verified for all six rows.

### A10 — Hardcoded constants inside grid formulas — **NOT FIXED**
| Constant | First review | Now | Where |
|---|---|---|---|
| `2026` | 420 | **599** | OPEX 13, 17, 18, 22, 23, 25, 26; Personnel 26, 27, 28 |
| `30` | 180 | 180 | Financial Statements 44, 45, 50 |
| `9` | 1 | 0 | removed from Dashboard D38 |
| `60` | 0 | **3** | Dashboard D37, D38, D52 (last-column index) |
| `32` | — | 120 | COGS 6, 7 HLOOKUP row index (see **B20**) |
| `1000000` | — | 120 | Revenue Forecast 22 sentinel (intentional) |

The offending `9` is gone. The `2026` exponent base grew by 179 cells because the A7 fix
added the escalator to three more OPEX rows, and `30` is untouched. Severity is unchanged
(low): the values are correct today, the maintenance exposure is larger than before.

**Nine of ten fixed. A10 not fixed. No fix is wrong.**

---

## (B) New defects

### B1 — Funding dates use exact equality with no arrival check; an off-grid date silently deletes the round — HIGH
```
'Financial Statements'!E35 = IF(E$3=Assumptions!$F$138,Assumptions!$F$139,0)
                           + IF(E$3=Assumptions!$F$140,Assumptions!$F$141,0)
'Financial Statements'!E36 = IF(E$3=Assumptions!$F$143,Assumptions!$F$142,0)
```
Test: `Assumptions!F140` set to 2026-10-15 (a plausible "money in mid-October" edit).
Recalculated: **no equity is raised at all**. Cash falls to -EUR298,188 at Dec-2026 and
-EUR3,250,725 by Dec-2029, 40 months negative, and the balance sheet check still reads 0.00
in every column because equity and cash both drop by the same EUR3m. The same happens with
2031-01-01 (a date past the horizon).

Simultaneously **13 cells return `#N/A`** — `Dashboard!D37, D38, D41, D42, D43, D44, D45,
D46, D47, D50, D51` and `Summary!C31, D31` — while `Dashboard!D52` and `D53`, which are
wrapped in `IFERROR`, read **0.0%** and **0.0 months**. A reader sees eleven errors and two
plausible-looking zeros.

Why it matters: the whole model exists to justify a raise, and a one-character edit to the
raise date removes the raise with no check anywhere. There is no cell comparing equity
actually received to `F139+F141`, or loan received to `F142`.

Fix: (i) change rows 35 and 36 to a month-window test, e.g.
`IF(AND(YEAR(E$3)=YEAR(Assumptions!$F$140),MONTH(E$3)=MONTH(Assumptions!$F$140)),...)`,
the pattern row 61 already uses for capex; (ii) add a check row
`=SUM(E35:BL35)-(Assumptions!F139+Assumptions!F141)` and the same for the loan; (iii) wrap
the Dashboard `MATCH` calls so the block degrades to a message rather than `#N/A`.

### B2 — No negative-cash check, and the shipped base case is negative — MEDIUM-HIGH
Base case as shipped: `Financial Statements` AY40 = -91,828 (Nov-2029) and AZ40 = -250,725
(Dec-2029). There is no check row for minimum cash, no conditional formatting anywhere in the
workbook (verified: zero conditional formatting rules on all ten tabs), no overdraft facility
and no interest charged on a negative balance. `Dashboard!D34` checks only that the balance
sheet balances, which it does at any cash value.

The only statement of the problem is static text on the new Summary tab (B50, "Base on EUR3m
runs out of cash at the end of 2029"), which does not recalculate. Twelve of the nineteen
recalculations in this review produced negative cash. In all twelve, no calculating cell in
the workbook reported it.

Fix: add a check row on `Financial Statements` (`=MIN(E40:BL40)` with a flag when negative)
and surface it on the Dashboard next to D34, alongside `MIN(Personnel!E20:BL20)` and
`MIN('Revenue Forecast'!E34:BL34)`.

### B3 — The "IS THE RAISE THE RIGHT SIZE" block reads as nonsense once cash goes negative — MEDIUM
Base case, as shipped:
```
D46  Cash still in the bank at the low point          (EUR250,725)
D52  Share of the raise the plan actually uses        108.5%    note J52: "well under 100% means the raise is bigger than this plan needs"
D53  Months of operating cost left at the low point   (0.4)     note J53: "Three months or more is comfortable"
```
`D51` ("Most of the raise ever drawn down") reads EUR3,254,037 against a EUR3,000,000 raise.
None of the three labels or the two notes can be read literally. Fix: floor the ratio and the
months at the point cash goes negative and replace the value with an explicit shortfall line
(`= -D37` when D37 < 0, labelled "Extra funding needed at the low point").

### B4 — D37's window starts at the raise month, so a pre-raise cash hole is invisible to the whole money block — MEDIUM-HIGH
`D37` takes the minimum of row 40 from `MATCH(Assumptions!$F$140,…)` to column 60. Any month
before the second round is outside the window, so `D37`, `D38`, `D41`-`D47`, `D50`-`D53` and
`Summary!C31, D31, C32` cannot see it.

Proven by two stress tests:
- **Test (g)**, aggressive with in-house line 1 producing from 2027-01-01: the EUR3.5m capex
  falls in Jan-2026 against EUR853,120 of opening cash. Cash is negative for nine months,
  Jan-2026 to Sep-2026, low **-EUR3,223,598**. The Dashboard reports `D37` = +EUR1,719,298
  (Dec-2027), `D52` = 47.8% and `D53` = 2.2 months. Nothing anywhere reports the nine-month,
  EUR3.2m hole. The answer to the brief's question is: **the model does not handle it, and it
  breaks silently.**
- **Test (a2)**, second round moved to 2027-03-01: cash is negative Nov-2026 to Feb-2027,
  low -EUR298,188, while `D52` reads 97.9% ("under 100%, so the raise is big enough").

Fix: run the window from column E, or add a separate "lowest cash before the raise" line.

### B5 — `Personnel!BN31:BR31` "Average cost per person" mixes an average-of-year numerator with a year-end denominator — MEDIUM
```
BN31 = IFERROR(BN29/12/BN20,0)      monthly: E31 = IFERROR(E29/E20,0)
```
`BN29` is the twelve-month people-cost total, `BN20` is December headcount. The result is not
a cost per person in any month.
| | 2026 | 2027 | 2028 | 2029 | 2030 |
|---|---|---|---|---|---|
| BN31 base | 6,219 | 5,963 | 6,445 | 6,546 | 6,845 |
| Dec actual base | 6,219 | 6,646 | 7,062 | 7,396 | 7,723 |
| BN31 aggressive | 6,219 | **3,369** | 6,006 | 5,808 | 6,649 |
| Dec actual aggressive | 6,219 | 6,134 | 6,643 | 6,800 | 7,212 |

The aggressive 2027 figure of **EUR3,369 a month is impossible**: the lowest loaded cost on
`Assumptions!D116:D123` is EUR4,800. It happens because headcount goes 16 → 77 during the
year (35 production operators arrive in Nov-2027) while the numerator averages the whole year.
BT31 documents the construction ("the year's people cost over twelve, per head at December"),
which does not make the number usable.
Fix: `=IFERROR(BN29/12/AVERAGE(E20:P20),0)`, or take December over December
(`=IFERROR(P29/P20,0)`).

### B6 — `Assumptions!F14` "Hiring starts from" is referenced by no formula — MEDIUM
A scan of every formula on all ten tabs finds zero references to `Assumptions!F14`, `D14` or
`E14`. Its note J14 reads "the month after the raise lands. Nothing changes in the committed
2026 plan before it", which describes behaviour the cell does not produce. What actually gates
hiring is `F13` (first month we can sell, reps and partners) and `F15` (committed 2026 plan
holds until, opex handover). A user who moves F14 sees no change anywhere.
Fix: delete the row, or point `Revenue Forecast` 16 and 19 at it instead of F13.

### B7 — The "first month we can sell" gate is not applied to marketing spend — MEDIUM
`Revenue Forecast` rows 16, 19 and 34 are gated by `IF(E$3<Assumptions!$F$13,0,…)`. Row 6
(marketing spend) is not: `=HLOOKUP(YEAR(E$3),Assumptions!$D$47:$H$50,4,FALSE)`.
**Test (c)**, F13 set to 2028-01-01: 2027 spends **EUR336,000** of marketing, generates 560
funnel orders and 572 units of demand, and sells zero units. `OPEX!BO12` charges the full
EUR336,000. The money is spent and the leads discarded with no warning.
Fix: gate row 6 the same way, or add a "demand not served" line (see **B14**).

### B8 — `Assumptions!J44` contradicts the model and two other notes on service labour — MEDIUM
`Assumptions!J44` (against F44, service cost per installed unit per year):
> "this is the field labour, so service engineers are not charged again in Personnel"

`Personnel!E18` sizes field service engineers and `Personnel!E28` charges them at
`Assumptions!$F$123` = EUR6,500/month. Base 2030: 16 engineers, EUR1.48m of salary. So they
*are* charged in Personnel. `COGS!BT17` says "parts, consumables and travel per contract …
the engineers are on Personnel" and `How to read me!C32` says the same. J44 is the odd one
out and is the note a reader consults when deciding whether service labour is double counted.
Fix: rewrite J44 to match COGS BT17.

### B9 — Ratio rows are arithmetically correct but meaningless for 2026 — MEDIUM-LOW
2026 has no trading: revenue is the EUR106,782 subsidy and COGS is nil. After the A2 fix the
ratio rows read, for 2026, in both cases:
```
Dashboard D16  Gross margin       100.0%
Dashboard D19  EBITDA margin    (1,634.2%)
'Financial Statements' BN24        (1,640.0%)
OPEX BN35  opex / revenue        1,734.2%
Summary C27  Gross margin         100.0%
```
The Dashboard and the front Summary tab both lead with "gross margin 100.0%" for a year with
no product sold. Fix: suppress the ratio when `'Revenue Forecast'!BN34 = 0`, e.g.
`=IF('Revenue Forecast'!BN34=0,"n/a",IFERROR(BN8/BN6,0))`.

### B10 — `Summary!B38` numbers do not match the model — MEDIUM-LOW
> "Spending 50% more on marketing in 2028-29 takes base volume past 5,000 units in 2029 and
> swings that year's EBITDA from -2.9m to +12.7m."

Recalculated (base marketing F48 = 105,000, G48 = 180,000): 2029 units 5,152 (past 5,000, ✓),
2029 EBITDA moves from **-EUR3,226,023** to **+EUR12,347,396**. The text says -2.9m and
+12.7m. Both legs are stale by about EUR0.3m, consistent with having been written before the
A7 escalator fix. `B35`, `B36` and `B37` were re-checked against recalculation and are all
correct (B37: base with E6=2 gives EBITDA +EUR2,941,163 in 2028 and a cash low of
EUR1,367,128, i.e. "about EUR1.4m").

### B11 — `Summary` rows 31 and 32 put horizon-wide figures inside the year grid, in the wrong font — LOW-MEDIUM
`Summary!C24:G24` are the year headers 2026..2030.
```
C31 = Dashboard!D37   lowest cash over the whole horizon, sitting under "2026"
D31 = Dashboard!D38   the month it happens, sitting under "2027"
C32 = Dashboard!D53   months of cover, sitting under "2026"
```
A reader of the live results table will take -EUR250,725 as a 2026 number and Dec-2029 as a
2027 number. `Summary!D31` and `C32` are also the only two cells in the workbook set in
Calibri (every other cell is Geist or Arial), so they were added without styling.
Fix: move rows 31 and 32 below the year table, or merge/left-align them across C:G.

### B12 — `Assumptions!F104` label, note and mechanism disagree — LOW-MEDIUM
`B104` = "R&D engineers carried into 2027", `J104` = "the roster at the end of the committed
2026 plan", `J122` = "the blended cost of the seven engineers already in post", and the value
is 10. `Personnel!E16 = Assumptions!$F$104 + SUMIF(...)` applies it **from January 2026**, so
it is really "R&D engineers in post at Jan-2026". Three descriptions, two numbers (10 and 7),
one cell. Carried over from the first review's B13 and still unresolved.

### B13 — No sources-equals-uses check behind `Dashboard!J47` — LOW
`J47` says "ties to total money available". D43 = SUM(D40:D42) and D47 = SUM(D44:D46) do tie
(base 4,453,120 both; aggressive 11,453,120 both) but no cell computes the difference, so a
future break is silent. Carried over from the first review's B14.

### B14 — The direct/channel mix is a hard cap and unmet demand is invisible — LOW-MEDIUM
`'Revenue Forecast'!E22 = MIN(IFERROR(E18/E15,1000000),IFERROR(E21/(1-E15),1000000))`.
**Test (d)**, installer partners signed per month set to zero in all years: units sold go
469 (2027) → 192 (2028) → 144 (2029) → **132 (2030)** while marketing spend rises to
EUR2,040,000 and demand to 3,448 units. Volume *falls* as spend rises, because with one
partner the channel leg caps total sales at `8/(1-0.30)` = 11.4 units a month in 2030. Cash
reaches -EUR16,518,980. The mechanism is documented on BT22, but no line anywhere reports
demand generated and not served, so the Dashboard shows a collapsing business with no
explanation of why. Fix: add `'Revenue Forecast'` row "Demand not served = row12 - row34"
and put it on the Dashboard.

### B15 — Annual units sold can exceed annual demand through per-month rounding — LOW
`E34 = IF(E$3<Assumptions!$F$13,0,ROUND(MIN(E12,E22,E31),0))` rounds each month, and the
annual column sums the rounded months. **Test (b)** (marketing base row zeroed): `BO34` = 54
units against `BO12` = 51 units of demand. Immaterial in euros (up to 6 units a year) but the
Dashboard can show units sold above the demand that produced them.

### B16 — `COGS` row 21 and `'Revenue Forecast'` row 51 use different revenue bases — LOW
```
'Revenue Forecast'!BN51 = IFERROR((BN50-BN49)/BN34,0)                     excludes the subsidy
COGS!BN21 = IFERROR(('Revenue Forecast'!BN50-BN19)/'Revenue Forecast'!BN34,0)   includes it
```
Two adjacent per-unit metrics on different bases. Nil impact at current inputs because 2026
units are zero and the subsidy is 2026-only, but it becomes live the moment `F13` or `F17`
moves. Fix: subtract `'Revenue Forecast'!BN49` in COGS row 21 as well.

### B17 — The balance-sheet check is set in near-invisible grey and nothing anywhere is conditional — LOW
`'Financial Statements'!E58:BL58` and `BN58:BR58` are font FFCCCCCC on a white ground. The
workbook has **zero** conditional formatting rules on all ten tabs. `How to read me!C9` says
"Check row. Must read nil", but a check that broke would change from a pale grey 0.00 to a
pale grey number. House standard is that a broken check should be loud.

### B18 — `Cover!B18` and the tab order disagree — LOW
`Cover!B18` reads "Read the How to read me tab first." The workbook now opens on **Summary**
(`activeTab=0`, `sheetId=1`, first in tab order), which is two tabs before Cover and three
before How to read me. Cover does not mention Summary at all, and `Cover!C15` "Units: whole
euros" does not cover the fractional partner and headcount rows (Dashboard row 9 shows 106.6
partners on a `#,##0.0` format).

### B19 — `Dashboard!J44` describes only the aggressive case — LOW
> "two assembly lines plus tooling, each paid twelve months before it produces"

In the shipped base case `D44` = EUR0 and `Assumptions!D82`/`D83` are 2035-01-01, i.e. there
are no in-house lines. The note also calls them "assembly lines", which invites confusion
with the assembly *partner* on `Assumptions!B81`, a different thing. `Dashboard!J45`
("plus the receivables and stock the ramp ties up") is also loose: DIO is 0 so there is no
stock, and payables are a source of cash inside the same figure.

### B20 — `COGS` rows 6 and 7 depend on a magic row index into another tab's annual block — LOW
```
COGS!E6 = IFERROR(HLOOKUP(YEAR(E$3),'Revenue Forecast'!$BN$3:$BR$34,32,FALSE),0)
```
Index 32 counts from row 3, so it lands on `'Revenue Forecast'` row 34 "Units sold". 120 cells
use it. Inserting any row in `'Revenue Forecast'` between rows 3 and 34 silently repoints the
BOM tier driver at the wrong row with no `#REF!`. Fix: `MATCH("Units sold",'Revenue
Forecast'!$B$3:$B$34,0)` or a named range.

### B21 — `Assumptions!J47` misdescribes how demand is combined — LOW
> "fills the demand the installer partners do not bring in themselves"

`'Revenue Forecast'!E12 = E10+E11` adds the funnel orders to the partner orders. Marketing
does not top up to a target; the two are additive. `How to read me!C24` states it correctly.

### B22 — Sign convention on the Dashboard is inconsistent — LOW
`D17` "Operating expenses" shows -EUR12,003,403 (reads `'Financial Statements'!BR14`, a
negative row) while `D30` "Capital expenditure" shows +EUR3,500,000 (reads row 61, a positive
row). Both are costs, on the same tab, in the same currency format.

### B23 — Year headers are typed in 56 places — LOW
`Assumptions` D47:H47, D56:H56, D60:H60, D64:H64, D68:H68, D99:H99 (30 cells) are typed
2026..2030 and the HLOOKUPs match against them; `BN3:BR3` on five grid tabs (25 cells) and
`Dashboard!D3:H3` (5 cells) are typed too, and the Dashboard reads BN..BR by direct
reference. Moving the model's first year means editing 60 cells plus the 599 `2026` exponent
bases from A10.

### B24 — Presentation housekeeping — LOW
No freeze panes on `Assumptions` (143 rows, so the Base/Aggressive/Live header at row 8
scrolls away), `Dashboard` or `Summary`. No print orientation and no fit-to-width set on any
of the ten tabs. `Summary` has no checks area. The workbook is set in Geist (10,249 cells)
with Arial for notes and units (322 cells); the project convention in
`scripts/house_style.py` is Arial, so Geist is either a deliberate rebrand or a drift — worth
confirming, since Geist is not installed by default and will fall back on most machines.

---

## (C) Text that no longer matches the model

| Where | Statement | What the model does |
|---|---|---|
| `Assumptions!J44` | service cost per unit "is the field labour, so service engineers are not charged again in Personnel" | `Personnel!18` sizes them and `Personnel!28` pays them EUR6,500/month; `COGS!BT17` and `How to read me!C32` say the opposite (**B8**) |
| `Assumptions!J14` | "Hiring starts from … the month after the raise lands. Nothing changes in the committed 2026 plan before it" | `F14` is referenced by no formula at all (**B6**) |
| `Assumptions!J104` vs `J122` | "the roster at the end of the committed 2026 plan" (10) vs "the seven engineers already in post" (EUR5,700) | one cell, `F104` = 10, applied from Jan-2026, so it is neither (**B12**) |
| `Assumptions!J47` | marketing "fills the demand the installer partners do not bring in themselves" | demand is additive: row 12 = row 10 + row 11 (**B21**) |
| `Assumptions!J82` | "Aggressive: paid for in November 2026, the first month after the raise lands" | true only while `F140` = 2026-10-01 and `E82` = 2027-11-01; nothing links them |
| `OPEX!BT44` | "The drivers take over from November, the month after the raise lands" | the handover is `F15`, an independent input; move `F140` to 2027-03-01 and the sentence is false while the model still hands over in November |
| `Dashboard!J52` | "well under 100% means the raise is bigger than this plan needs" | reads 108.5% in the shipped base case; the note has nothing to say about >100% (**B3**) |
| `Dashboard!J53` | "Three months or more is comfortable" | reads -0.4 months in the shipped base case (**B3**) |
| `Dashboard!J44` | "two assembly lines plus tooling" | base case has none; the phrase also collides with the assembly partner (**B19**) |
| `Dashboard!J45` | "the receivables and stock the ramp ties up" | DIO = 0, so there is no stock; payables offset inside the same number (**B19**) |
| `Dashboard!J47` | "ties to total money available" | it does tie, but no cell checks it (**B13**) |
| `Dashboard!J26` | "Viessmann runs at about EUR276k and Vaillant about EUR200k" | the cell now works and reads EUR1.44m; revenue includes a EUR3,600/unit installation pass-through and assembly is outsourced, so the comparison flatters Tarnoc ~5x |
| `Personnel!BT8` | "every partner has to be trained and certified before selling anything" | `ROUND` gives 0 installer trainers through 2027 base with 6 partners signed |
| `Personnel!BT31` | "the year's people cost over twelve, per head at December" | accurate description of a construction that produces an impossible EUR3,369/month in aggressive 2027 (**B5**) |
| `How to read me!C4` | inputs "live on Assumptions, plus the back-office headcount row on Personnel" | omits `OPEX` rows 38-43, which `C13` and `Summary!B7` both list |
| `Summary!B38` | 2029 base EBITDA "-2.9m to +12.7m" | recalculates to -3.23m and +12.35m (**B10**) |
| `Summary!B21` | "R&D hires and the back office are typed per year" | R&D hires are per year (`D100:H100`); the back office is typed per month (`Personnel!E17:BL17`, 60 cells) |
| `Summary!B15` | "1,000 a month per in-house line … (aggressive case only)" | `F84` = 1,000 in both cases; the base case simply never has a line. Correct in effect, loose in wording |
| `Cover!B18` | "Read the How to read me tab first" | the workbook opens on `Summary`, which the Cover does not mention (**B18**) |
| `Cover!C15` | "Units: whole euros" | partner counts and headcount are formatted `#,##0.0`; Dashboard row 9 shows 106.6 partners |

Checked and found still accurate: `How to read me` C13, C14, C15, C16, C19, C20, C23-C27,
C31, C32, C33 (EUR9,984 / EUR7,069 / EUR4,998 match `Assumptions!E93:E95`), C34, C35;
`Cover` C12, C13, C14; `Summary` B6-B9, B12-B14, B18-B20, B35, B36, B37, B41-B47, B50-B54,
B56-B59; `Assumptions` J5, J6, J9, J11, J13, J15, J21, J26, J27, J52 (120/0.2 = 600), J54,
J56, J60, J64, J68, J74, J76, J77, J81, J87, J88, J89, J106, J107, J108, J113, J141;
all BT notes on `Financial Statements`, `Revenue Forecast`, `COGS` and `OPEX` except
`OPEX!BT44`.

---

## (D) Stress test results

All tests on copies. Column "errors" counts cells returning `#…`; "BS check" is the worst
month of `'Financial Statements'` row 58; "min cash" is the minimum of row 40 over 60 months.

| Test | Input changed | errors | BS check | min cash | Verdict |
|---|---|---|---|---|---|
| baseline base | — | 0 | 0.00 | **-250,725** (Dec-29) | Model consistent; **the shipped base case is EUR251k short**. Disclosed only in static Summary text (**B2**) |
| baseline aggressive | E5 = 2 | 0 | 0.00 | 276,402 | Acceptable |
| (a1) | F140 → 2026-11-01 | 0 | 0.00 | -250,725 | **Acceptable.** D50 correctly moves to 2,852,562 (end Nov-26); A5 fix holds. But `F14`/`F15` and the notes that call November "the month after the raise" do not move with it (**C**) |
| (a2) | F140 → 2027-03-01 | 0 | 0.00 | -298,188 | **Defect (B4).** Cash negative Nov-26 to Feb-27 while `D52` reads 97.9% and `D53` reads -0.4; the pre-raise hole is outside D37's window |
| (a3, extra) | F140 → 2026-10-15 | **13** | 0.00 | -3,250,725 | **Defect (B1).** The EUR3m round is never received; 13 `#N/A`; D52/D53 read 0.0%/0.0 |
| (a4, extra) | F140 → 2031-01-01 | **13** | 0.00 | -3,250,725 | Same as above |
| (b) | marketing Base D48:H48 = 0 | 0 | 0.00 | -4,749,021 | **Acceptable mechanically.** Units 0/54/402/1,602/4,113, all from partner-brought orders. Two marketers still on payroll with no budget (`Personnel!10` floor `F105`). 34 negative months, unflagged (**B2**). Annual units 54 > annual demand 51 (**B15**) |
| (c) | F13 → 2028-01-01 | 0 | 0.00 | -858,033 | **Defect (B7).** 2027 revenue 0, units 0, but EUR336,000 of marketing spent and 560 orders generated and discarded. 2027 gross margin displays 0.0% |
| (d) | partners signed D65:H65 = 0 | 0 | 0.00 | -16,518,980 | **Acceptable as designed, fragile (B14).** Units *fall* 469 → 132 as spend rises to EUR2.04m, because the channel leg of the mix cap collapses selling capacity to 137/yr. No "demand not served" line |
| (e) | DSO 60, DPO 0 | 0 | 0.00 | -22,318,553 | **Acceptable.** Correct direction and magnitude; receivables 3x, payables nil. No errors, BS still balances, cash flow still articulates |
| (f) | E5 = 2 and E6 = 2 | 0 | 0.00 | 276,402 | **Acceptable.** GM 27.6/38.2/37.1/36.8%, cash 98.6m at 2030. Note `D53` = 40.2 months because the low point falls in Dec-2026 and the divisor is the frozen 2026 plan (**A4** commentary) |
| (g) | E5 = 2, E82 → 2027-01-01 | 0 | 0.00 | **-3,223,598** | **Defect (B4). The model does not handle it and breaks silently.** EUR3.5m capex lands Jan-2026 against EUR853k of cash; nine negative months Jan-Sep 2026; Dashboard reports D37 = +1,719,298, D52 = 47.8%, D53 = 2.2 months and says nothing |
| (h1) | TTK share = 1.0 | 0 | 0.00 | -21,086,296 | **Acceptable.** Gross margin goes negative (-11.2 / -13.2 / -14.2% in 2027-29) because the TTK sells at EUR8,526 against a EUR9,984 tier-1 BOM. Correct economics, correctly displayed. No division by `F28` anywhere |
| (h2) | TTK share = 0.0 | 0 | 0.00 | 276,402 | **Acceptable.** All Combi+; base becomes cash-positive throughout; GM 13.1/11.0/9.9/26.3% |
| (i) | Personnel E17:BL17 = 0 | 0 | 0.00 | 276,402 | **Acceptable.** Headcount 13/20/31/50/79; the base case becomes solvent (low +276,402), which shows the shipped base case is inside EUR251k of the back-office line alone |
| (j) | opening cash = 0 | 0 | 0.00 | -1,103,845 | **Acceptable.** 22 negative months from Jan-2026; `D40` = 0, `D43` = 3,600,000, block still ties; `E53` opening equity correctly becomes 0 and the balance check holds |
| (extra) | base marketing +50% 2028-29 | 0 | 0.00 | 276,402 | Verifies `Summary!B38`; the text's numbers are stale (**B10**) |
| (extra) | E6 = 2, base | 0 | 0.00 | 1,367,128 | Verifies `Summary!B37`; correct |

Across all nineteen recalculations: no negative headcount, no negative units, no month where
units sold exceeds demand, selling capacity or build capacity, and the balance-sheet check
reads 0.00 in every column of every case. The only error values found are the 13 `#N/A`
in tests (a3) and (a4).

---

## (E) Checked and correct

**Dashboard row-by-row.** Every one of the 24 populated rows resolves to a target row whose
label matches its own, and every annual reference is the right aggregation for the quantity:
flows from `SUM` columns (D14 → `'Financial Statements'!BN6`, D17 → BN14, D18 → BN16,
D20 → BN23, D29 → BN35, D30 → BN61), stocks and headcount from December pick-ups (D7 →
`'Revenue Forecast'!BN41` = P41, D9 → BN20 = P20, D23 → `Personnel!BN18` = P18, D24 → BN20,
D31 → `'Financial Statements'!BN40` = P40), ratios from recomputed annual rows (D8 →
`'Revenue Forecast'!BN35`, D16 → BN9, D19 → BN17), and D6, D10, D26, D32, D34 computed
in place. No hardcoded values anywhere on the tab. `D34`'s two-sided worst-month test
`MAX(ABS(MIN(...)),ABS(MAX(...)))` is the right construction and reads 0.00 in every case
tested. `D53`'s HLOOKUP index 12 lands on row 14. `D41`, `D42`, `D44`, `D45` all use
`SUMIF(row3,"<="&D38,…)` consistently, so the money block is internally closed:
D44+D45+D46 = D43 exactly in every case tested.

**Every ratio row recomputes from totals.** Gross margin (`'Financial Statements'` BN9),
EBITDA margin (BN17), net margin (BN24), opex share of revenue (`OPEX` BN35), selling capacity
used (`'Revenue Forecast'` BN24), build capacity used (BN35), revenue per unit (BN51) and
gross profit per unit (`COGS` BN21) are all built from the annual numerator and the annual
denominator, not from an average of monthly ratios. `Personnel` BN31 is the one exception and
is defect **B5**. Rate rows that should be averaged are averaged: `'Revenue Forecast'` 8 and
15, `COGS` 9 and 10.

**Input convention.** Every cell carrying the pale-yellow input fill FFFFF2CC holds a typed
value; no formula cell is filled yellow; and every typed number in the grid outside the two
declared input areas (`OPEX` 38-43 columns E..N, `Personnel` 17) is a year header on a lookup
table, correctly left unfilled. `Assumptions` E5 and E6 are filled as inputs.

**Assumptions live cells.** All 70 `Live` cells in column F are
`IF(Assumptions!$E$5=2,E<own row>,D<own row>)`; all six `Live (per case)` year rows (50, 59,
63, 67, 71, 102) read their own block across D..H. The derived cells F25, F29, F35, F36, F43,
F44, F45 recompute correctly from their own tables (F43 = 0.2 × (0.34×60+0.54×90) + 0.8 ×
(0.34×150+0.54×200) = EUR159.0; F45 = 0.88).

**Grid mechanics.** All 60 monthly columns of every row on the five grid tabs share one
pattern; the seventeen rows with a distinct first-month formula are all legitimate opening
balances. Sign convention on the statements is consistent (COGS, opex, depreciation, interest,
tax and capex all negative in the P&L and cash flow; receivables, payables and inventory
positive on the balance sheet from a negative COGS row). Working-capital movement rows 29, 30,
31 carry the right sign and telescope from zero. Capex leads production by
`EDATE(<producing date>, -F87)`. The three-way `MIN` gate on units sold, the 1,000,000
sentinel in the mix cap, the tiered `VLOOKUP`s with `TRUE`, the five year-table `HLOOKUP`s
with index 4 and `FALSE`, the tax-loss roll-forward and the installed-base roll all behave as
the first review described; re-verified by recalculation.

**Excel / Google Sheets compatibility.** Nineteen functions: ABS, AND, AVERAGE, EDATE,
HLOOKUP, IF, IFERROR, INDEX, MATCH, MAX, MIN, MONTH, ROUND, SUM, SUMIF, SUMPRODUCT, VLOOKUP,
YEAR, plus `INDEX(...):INDEX(...)` range construction newly introduced on Dashboard D37, D38
and D52. All are available in both Excel and Google Sheets, including the `INDEX:INDEX` form
and `SUMIF` with `"<="&<date cell>`. No `_xlfn.` prefixes, no volatile functions, no array
formulas, no dynamic-array spilling, no defined names, no data validation. Gridlines are off
on all ten tabs. `Dashboard!D32`'s `MIN('Financial Statements'!E40:'Financial Statements'!P40)`
form is unusual but legal in both. No compatibility defects.
