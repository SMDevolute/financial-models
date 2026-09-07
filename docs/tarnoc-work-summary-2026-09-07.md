# Tarnoc: everything done so far

Written 2026-09-07. Covers the whole engagement, from the first model in June to
the three workbooks that exist today. For how the current model works, read
`docs/tarnoc-v2-summary-2026-09-07.md`. For the detail of the last working day,
read `docs/tarnoc-worklog-2026-09-07.md`.

## Phase 1, June 2026: fixing the client's own model

Starting point was the client's workbook in the dataroom
(`Tarnoc Financial Model 26/6/2026`), rebuilt locally as `Tarnoc_LIVE_*`.

- Put in COGS tiering on volume, first on a single year, then on this year plus
  next year (the two-year supplier commitment).
- Made the unit ramp self-solving instead of typed in three places.
- Fixed the 2029 revenue subtotals and the 2029 personnel salaries, which had
  been overwritten.
- Linked the 2029 unit figures back to the Assumptions tab.
- Fixed the CLA balance sheet line, made headcount date-aware, made the
  installed base cumulative.
- Built the house style system (`scripts/house_style.py`) so every model looks
  designed rather than auto-generated.

Result: `Tarnoc_LIVE_2026-06-30_final_service+installedbase+CLA-fix.xlsx`.

## Phase 2, August 2026: the Combi decision and the EUR10m case

- Dropped the plain Combi product, leaving the turbineketel and the Combi+.
  Snapshots kept either side of that change.
- Added a notes column to every row so a dataroom reader can see what each row
  does.
- Explained the January 2028 cash dip in the How-to-read tab: it is a timing
  artifact of the 1 January BOM tier step against 45-day supplier terms, not a
  hole in the plan.
- Built the EUR10m aggressive case as a switch on the existing model, not a
  separate file (`Assumptions D82` case, `D83` BOM tier basis). All four switch
  combinations checked, balance sheet tied in every column.

Weakness of that version: units were four typed numbers. The model did correct
arithmetic on an assertion, and nothing in it explained how the company sells
22,000 units or whether it could build them.

## Phase 3, 1 September: units become an output

Built a Growth Engine that calculates units month by month as the smallest of
demand, selling capacity and build capacity, and records which of the three
stopped the sale. Headcount became a calculated result of the same drivers.
The plan also changed shape: selling shifts from direct to an installer
channel, because 22,000 units through a direct sales floor would need about 90
reps.

Two files from this point on:
- `Tarnoc_LIVE_2026-09-01_growth-engine.xlsx`, the client's original workbook
  extended. Kept as the bridge back to what they already know. Call it model A.
- `Tarnoc_v2_*.xlsx`, rebuilt from scratch, monthly January 2026 to December
  2030. Model B, and the one that goes forward.

## Phase 4, 3 to 4 September: model B made defensible

- Market research on every assumption, five passes with sources, written up in
  `docs/tarnoc-assumptions-research-2026-09-04.md`. Thirty-three assumptions
  checked against published data, each with a verdict.
- Acted on the research: wages 5% a year, flat cost per lead, direct share
  falling 100 / 80 / 50 / 35 / 30 percent, aggressive case brought down from
  22,000 to about 15,000 units.
- Removed the ramps and quota attainment that made the model hard to follow.
  Reps and partners start with the first sellable month.
- Installer partners now bring in their own orders as well as taking
  commission; the installer earns 10% of the unit price on channel sales.
- Field service engineers put on the payroll; the warranty reserve dropped so
  COGS matches the structure the client uses.
- Back office headcount typed on the Personnel tab as ordinary rows.
- The turbineketel corrected everywhere: it is a turbine heat pump, not a
  boiler.
- Uploaded to Drive as `Tarnoc_v2_2026-09-03.xlsx`; the earlier Drive copy
  renamed ARCHIVE because someone had typed over a formula and cascaded 879
  errors through it.

## Phase 5, 7 September: profitability, the fork, and two reviews

Full detail in `docs/tarnoc-worklog-2026-09-07.md`. The short version:

- Found why base lost money to 2029: gross margin under 10%, because the
  turbineketel sells below its first-tier BOM and pays 10% commission. Tested
  eight levers. Only volume past the 5,000-unit tier and two-year BOM pricing
  moved it.
- BOM now always priced on two-year volume; the switch was removed.
- Base ramp slowed to your targets, about 300 units in 2027 and 1,200 in 2028,
  then tripling, and made to work on EUR3m with 81% of the raise deployed.
- Aggressive rebuilt around manufacturing capex on your instruction: two
  automated lines, EUR9m including tooling, about 18,800 units by 2030, 90% of
  the EUR10m used.
- The in-house cost saving was added and then removed at your request. The BOM
  is charged in full on every unit; the lines add capacity, not a cheaper unit.
- A Summary tab added as the front page of each workbook.
- Forked into three files from one build script: base only, aggressive only,
  and the combined master.
- Two independent formula-level reviews plus a ten-shock stress test found
  about twenty defects, all fixed. Reports in
  `docs/tarnoc-v2-formula-review-2026-09-07.md` and the pass-2 file.
- Two of the audit's four phases had been failing silently for about two hours
  that morning; the runner now fails loudly when a phase crashes or returns
  nothing. All three workbooks passed the full four-phase audit at end of day.

## What exists now

| File | What it is |
| --- | --- |
| `models/Tarnoc_v2_2026-09-07.xlsx` | Both cases on a switch. The master. |
| `models/Tarnoc_v2_base_2026-09-07.xlsx` | Base only, EUR3m, single Value column, no capex or in-house lines anywhere. |
| `models/Tarnoc_v2_aggressive_2026-09-07.xlsx` | Aggressive only, EUR10m. |
| `models/Tarnoc_LIVE_2026-09-01_growth-engine.xlsx` | Model A, the client's original workbook extended. To be retired. |
| `scripts/build_tarnoc_v2.py` | Builds all three. `MODE=both\|base\|aggr`. |
| `scripts/audit_v2.py` | Four-phase check: recalculation, independent shadow model, identities, structure. |

Copies of the base and aggressive files also sit in `~/Desktop/Tarnoc/`.

## Numbers as they stand

| | Base, EUR3m | Aggressive, EUR10m |
| --- | --- | --- |
| Units 2027 / 2028 / 2029 / 2030 | 350 / 1,350 / 4,100 / 7,400 | 2,800 / 6,900 / 11,700 / 18,800 |
| Revenue 2030 | EUR127m | EUR321m |
| EBITDA 2027 / 2028 / 2029 / 2030 | -2.5m / +0.8m / +18m / +34m | +4.8m / +23m / +45m / +79m |
| Cash low after the raise | EUR0.6m, Dec 2027 | EUR1.0m, Jan 2027 |
| Share of the raise used | 81% | 90% |

## Still open

Your decisions:
1. Aggressive raise size. EUR10m gives six weeks of cash cover at the low
   point; EUR11-12m gives two to three months. You asked for 90% deployment and
   two to three months of cover. At EUR10m only one of those can hold.
2. Warranty reserve back in or not, service prices, and the 88% service attach
   rate.

From the client:
3. Supplier quotes behind the three BOM tiers, and confirmation the supplier
   will price on a two-year volume commitment. Everything rests on this.
4. What the assembly partner charges per unit.
5. Confirmation of the installer deal at 10% of the unit price.
6. A view on the direct-to-installer shift and on 18,800 units by 2030.

Model work not started:
7. Upload the current files to Drive as a new version. The Drive copy is from
   3 September.
8. Sensitivity table on the Dashboard: 2028 plus 2029 volume against the 5,000
   tier, close rate, orders per partner, raise size.
9. Link back-office and R&D hiring to the raise date, so a slipped raise slips
   the hiring.
10. Other cost inflation is 10% a year; the research supports 3 to 5%. Left at
    10% on your instruction.
11. Retire model A once the client has been walked from A to B.
