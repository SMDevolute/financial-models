# Tarnoc, where we got to on 1 September and what is next

## Two models now exist. Know which is which.

**A. The patched existing model**
`models/Tarnoc_LIVE_2026-09-01_growth-engine.xlsx`
Your original workbook with a Growth Engine tab bolted on and 189 people added to
the Personnel tab. Same tabs, same wiring, monthly to 2028 with annual 2029.
Built by `scripts/build_tarnoc_growth_engine.py` then `scripts/expand_tarnoc_personnel.py`.

**B. The rebuild from scratch**
`models/Tarnoc_v2_2026-09-01.xlsx`
New model, your house design, monthly Jan-2026 to Dec-2030, no annual-only columns.
Built by `scripts/build_tarnoc_v2.py`, audited by `scripts/audit_v2.py`.
**This is the one to work on.**

## What changed today

Units sold used to be four numbers typed into the Assumptions tab. In both models
they are now an output. Every month the model works out how many people want a
boiler, how many we can sell, and how many we can build, sells the smallest of the
three, and writes down which one bit.

The organisation is an output too. Ten teams, each sized by whatever creates its
work: support by installed base, buyers by units, trainers by partners signed,
operators per production line, finance and IT at one per nine staff.

No market size or market share anywhere. Marketing spend runs the funnel instead.

2026 is not remodelled. January to October is your committed plan held fixed, line
by line, and it reconciles to the euro. The raise moved to October. Nothing is sold
before January 2027 and nobody is hired before November 2026.

The raise now draws down EUR9.13m of the EUR10m, up from EUR8.44m. The extra went
into the channel rather than more plant, because selling capacity was what limited
the plan in 34 of 60 months.

## Where model B stands

| | 2026 | 2027 | 2028 | 2029 | 2030 |
| --- | --- | --- | --- | --- | --- |
| Units, aggressive | 0 | 1,433 | 8,691 | 16,046 | 27,965 |
| Revenue | EUR107k | EUR24.2m | EUR147.4m | EUR273.2m | EUR477.3m |
| EBITDA | (EUR1.90m) | (EUR3.71m) | EUR24.27m | EUR81.39m | EUR150.98m |
| Headcount | 23 | 55 | 155 | 264 | 364 |
| Capex | 0 | EUR3.5m | EUR2.5m | 0 | 0 |
| Cash at year end | EUR9.55m | EUR1.54m | EUR14.95m | EUR70.50m | EUR175.61m |

Cash never goes negative in the aggressive case. Lowest point before the raise is
EUR276,402 in September 2026. Lowest point after it is EUR873,740 in January 2028.

Audit passes: zero formula errors, balance sheet ties to 0.0000 in all 65 columns
across all four switch settings, and 14,160 cells agree with an independent Python
reimplementation of the whole model.

## To do, roughly in the order it matters

**Decisions only you and the client can make**

1. **Only 0.6 months of cash cover at the low point.** January 2028 has EUR874k in
   the bank against about EUR1.4m a month of cost. Deploying 91% of the raise and
   keeping a sensible buffer are in tension. Raise more than EUR10m, slow the 2027
   hiring, or accept it knowingly. It should be a decision, not an accident.
2. **The base case does not work.** It draws down 130% of a EUR3m raise and goes to
   minus EUR889k in December 2028. Either it raises more or it stops being called a
   plan.
3. **The BOM cost-down is the load-bearing assumption.** EUR9,984 to EUR7,069 to
   EUR4,998 across the volume tiers is a 50% unit cost cut, and essentially all of
   the profit in the later years comes from crossing the second step. Now that
   volume is defensible, this is where a VC will push hardest. It needs supplier
   quotes behind it.
4. **Sign off the volume plan** with the client, including that 2027 is now derived
   rather than asserted.

**Model work**

5. **Revenue per person is still about EUR1.19m in 2030**, against Viessmann at
   EUR276k and Vaillant at EUR200k. Some of the gap is real because components are
   bought in and installation is passed through. Worth one more pass on the
   organisation ratios before this goes out.
6. **Decide which model goes forward.** Keeping both current is waste. My view is
   B, with A kept only as the bridge back to what the client already knows.
7. **Model A stops at 2029.** If it stays in use, the headline 2030 year needs
   adding to its financial statements.
8. **Sensitivity table.** Nothing in either model flexes the two or three
   assumptions a VC will lean on: BOM tier, cost per lead, units per partner.

**Housekeeping, carried over and still open**

9. Get the chosen model into Drive. Too big for the connector inline: open the
   working copy, then File, Import, Upload, Replace spreadsheet, which keeps the
   link. Check first whether the live sheet has been edited since 31 August,
   because importing will overwrite it.
10. Rename the stale Drive copy to `ARCHIVE 2026-08-19 pre-drop-combi (do not use)`.
11. Model A only: Pitchdeck dashboard B4 and B5 COGS wiring, and the possible 2028
    service cost double count in COGS BE20, about EUR79.5k.

## Two things found today that were already in your file

**The .xlsx had been rendering broken in Excel.** 72 formulas stored bare `IFNA(`
instead of `_xlfn.IFNA`. Google Sheets tolerates it, Excel does not, and it
cascaded through roughly 1,300 cells including the whole P&L, the balance sheet and
both dashboards. Anyone who downloaded from the dataroom saw a wall of `#NAME?`.
Fixed in model A, and model B does not use the function at all.

**The 2026 plan has no headroom.** The existing model reaches EUR7,062 in October
2026, right before the raise. That is not a modelling artefact, it is the plan.

## How to check the work

    python3 scripts/audit_v2.py models/Tarnoc_v2_2026-09-01.xlsx

Four phases: recalculation and error sweep, an independent shadow model compared
cell by cell, accounting identities and sign conventions, and structure. Exits
non-zero if anything fails. Run it after any change.
