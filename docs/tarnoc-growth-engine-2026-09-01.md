# Tarnoc — the €10M case, rebuilt as an operating plan

**Model:** `models/Tarnoc_LIVE_2026-09-01_growth-engine.xlsx`
**Built by:** `scripts/build_tarnoc_growth_engine.py`, then `scripts/expand_tarnoc_personnel.py`
**Checked by:** `scripts/verify_model.py` (recalculates in LibreOffice, all four switch settings)
**Date:** 2026-09-01

---

## What was wrong with the previous version

The 31-Aug aggressive case was arithmetically clean and strategically empty.
`Assumptions!D21:G21` held four typed numbers — 1,800 / 5,200 / 11,000 / 22,000
units — and everything downstream was correct arithmetic performed on an
assertion. Nothing in the model explained *how* the company sells 22,000 units,
whether it could build them, or who does the selling. Three specific holes:

1. **No demand build.** Units were an input. A VC asks "where does volume come
   from" and the model had no answer.
2. **No capacity constraint anywhere.** Nothing stopped the model selling
   22,000 units out of a business with one assembly partner.
3. **The org didn't scale with the plan.** 16 hires were pulled forward, but
   total headcount was *identical* in both cases — 51 people either way. At a
   plausible 20 units/rep/month, a direct sales motion needs ~92 reps to move
   1,833 units a month. The plan had 16.

Point 3 is the one that matters. It isn't a staffing oversight — it means the
€10M case cannot be a bigger version of the current business.

---

## What the rebuild does

A new **Growth Engine** tab computes units month by month, Jan-2027 to Dec-2030:

```
demand        = marketing spend / cost per lead x lead-qual% x qual-won%
sales capacity= ramped reps x quota x attainment
                + productive installer partners x units per partner
build capacity= assembly partner + in-house lines live
market ceiling= serviceable market x maximum allowed share

UNITS SOLD    = the smallest of those four
```

For every single month the tab **writes down which of the four stopped us selling more**. `Assumptions!D21:G21`
now reads that output. Units are a consequence of the plan, not an input to it.

Every driver sits on the Assumptions tab (rows 130–181) with a **Base column, an
Aggressive column and a live column** driven by the existing case switch (D82),
so the two plans are readable side by side.

### The business change the model now expresses

**Selling shifts from direct to an enabled installer channel.** The direct share
falls from 70% (2027) to 15% (2030). Partner managers replace quota carriers:
12 reps and 26 partners in 2027 becomes 33 reps, 290 partners and 12 partner
managers by 2030. That is the only shape in which 22,000 units is reachable
without a 90-person sales floor.

**Manufacturing shifts from partner to in-house.** The assembly partner carries
the ramp at 1,000 units/month; in-house line 1 goes live Jul-2028 and line 2
Jul-2029, each at 1,000 units/month. Capex is derived from those dates — a line
is paid for **12 months before it can build anything**, which is precisely why
the raise has to happen now. €3.5m in 2027, €2.5m in 2028. The previous version's
flat €5.5m was invented by me and had no schedule behind it.

**The org above the existing roster is costed.** Reps and partner managers that
the Growth Engine requires *beyond* the people already in the Personnel tab flow
into OPEX as an explicit line, so growth is not free. Only the excess is charged,
so nothing is double counted.

---

## The TAM argument was being made against the wrong market

A turbineketel replaces a gas boiler one-for-one. So the market is **the ~400,000
gas boilers replaced in the Netherlands every year** (8.2m homes), not the
~125,000 heat pumps sold in 2024. That single reframe is the difference between
a plan that reads as impossible and one that reads as conservative:

| | Against heat pumps | Against boiler replacements |
| --- | --- | --- |
| 22,000 units in 2030 | ~15% national share | **~3.5% of serviceable market** |

Implied market share is now a row on the face of the model and on the Diligence
tab. It never leaves the reader guessing.

---

## What the rebuilt model says

Units are now derived. They land close to what was previously asserted — which is
the useful result, because they were arrived at independently:

| Case | 2027 | 2028 | 2029 | 2030 |
| --- | --- | --- | --- | --- |
| Aggressive — **derived** | 1,040 | 5,537 | 11,385 | 21,960 |
| Aggressive — previously typed in | 1,800 | 5,200 | 11,000 | 22,000 |
| Base — **derived** | 606 | 1,721 | 3,844 | 6,552 |
| Base — dataroom plan | 600 | 1,600 | 3,600 | 7,200 |

**2027 is the honest correction: 1,040, not 1,800.** We run out of salespeople and installers — reps
and partners are still ramping. The original 2027 was not achievable.

Both cases, own-year BOM tier (the conservative basis, and the shipped default):

| | 2027 | 2028 | 2029 |
| --- | --- | --- | --- |
| **Aggressive (€10m)** | | | |
| Units sold | 1,040 | 5,537 | 11,385 |
| Revenue | €17.7m | €94.5m | €195.0m |
| Gross profit | €1.8m | €25.9m | €80.7m |
| Total OPEX | €6.1m | €16.3m | €31.6m |
| EBITDA | −€4.28m | +€9.64m | +€49.06m |
| Ending cash | €1.32m | €5.75m | €39.41m |
| Headcount on payroll | 48 | 132 | 240 |
| Revenue per employee | €377k | €695k | €756k |
| **Base (€3m)** | | | |
| Units sold | 606 | 1,721 | 3,844 |
| Revenue | €10.3m | €29.4m | €65.9m |
| Gross profit | €1.1m | €3.1m | €7.6m |
| EBITDA | −€4.12m | −€4.85m | −€4.80m |
| Ending cash | −€0.94m | −€4.61m | −€5.63m |
| Headcount on payroll | 38 | 54 | 81 |

Verified across all four switch combinations: **zero formula errors, balance
sheet ties to 0.0000 in every column.**

---

## The organisation, rebuilt — inside the Personnel tab

The first pass fixed the volume story and left the cost story alone: 69 people
producing €195m of revenue, **€2.8m each**, which no hardware manufacturer
achieves (Viessmann ~€276k, Vaillant ~€200k).

The second pass sized the organisation but put it in the wrong place — a cost
block on a new tab, bypassing the Personnel roster. That was wrong. **Every
person now sits in the Personnel tab as an ordinary row**: 189 new rows, 57 to
245, continuing the existing numbering, using the same columns and the same
monthly cost formula as the rows already there. Cost reaches the P&L through the
`SUMIF` summary block and OPEX rows 6–8 exactly as it always did. The summary and
headcount blocks moved down to rows 250–260 and their ranges were widened to
`$C$3:$C$245`; every reference to them in OPEX and the Growth Engine was
repointed.

Each new row carries a **case-dependent start date**, the pattern already used on
rows 28–55:

```
=IF(Assumptions!$D$82=2, DATE(2029,7,1), DATE(2035,1,1))
```

so one roster serves both scenarios. A 2035 date means that person is only hired
in the aggressive case.

The Growth Engine still *sizes* the organisation — that is what it is for — but it
no longer employs anyone. It now reports "required vs actually in Personnel", and
that gap reads **zero** in both cases.

| Function added | Rows | Base by Dec-29 | Aggressive by Dec-29 |
| --- | --- | --- | --- |
| Sales | 18 | 6 | 18 |
| Partner managers | 3 | 1 | 3 |
| Installer trainers | 3 | 1 | 3 |
| Order desk | 5 | 2 | 5 |
| Marketing | 1 | 1 | 1 |
| Supply chain & logistics | 14 | 3 | 14 |
| Production operators | 70 | 0 | 70 |
| Customer support | 8 | 3 | 8 |
| Technical escalation | 2 | 1 | 2 |
| Quality & certification | 7 | 3 | 7 |
| Finance / HR / IT / legal | 19 | 2 | 19 |
| R&D engineers | 39 | 7 | 39 |
| **Total** | **189** | **30** | **189** |

Headcount on payroll: **38 / 54 / 81** in the base case and **48 / 132 / 240** in
the aggressive case for 2027 / 2028 / 2029. Field service technicians (22 by 2029)
are shown as a check but deliberately not added to Personnel, because their labour
is already inside the ~50% cost on service contracts and would otherwise be paid
for twice.

Non-personnel costs that scale are the only things left on the Growth Engine, and
they flow into the existing OPEX department totals: facilities, IT and travel per
head; recruitment per hire; installer training and a demo unit per new partner
(€3,500); plant facility and maintenance per live line; €400k per country entered;
and a €200-per-unit warranty reserve on top of the 3% in the BOM — that one sits
in COGS, so it hits gross margin where it belongs.

---

## Findings the rebuild surfaced

**1. A pre-existing defect that would show as `#NAME?` in Excel.** 72 formulas
stored bare `IFNA(` instead of `_xlfn.IFNA`. Google Sheets tolerates this, which
is why nobody noticed — but opened as .xlsx in Excel or LibreOffice, COGS row 7
errors and cascades through roughly 1,300 cells including the whole P&L, balance
sheet and both dashboards. **If anyone in the dataroom downloaded the model as
Excel, they saw a broken file.** Now swapped to `IFERROR`, which needs no prefix.

**2. The base plan's 2030 is not buildable.** At 400 units/month the assembly
partner tops out at 4,800 a year, against a 7,200 plan. Base contracted capacity
is now set to 650/month — which makes it an explicit commitment to negotiate
rather than a hidden impossibility.

**3. Marketing spend was generating demand the company cannot serve.** On my
first pass the funnel produced 47,486 orders in 2030 against sellable capacity
of 22,136 — about half the marketing budget buying nothing. Spend is now tuned
so demand tracks capacity with a modest cushion.

**4. €10m is now closer to right, but still not fully drawn.** With the real cost
of the organisation in, the aggressive case ends 2027 with €1.6m and 2029 with
€41.2m — against €3.2m and €59.9m before the cost rebuild. The raise gets a lot
more use than it did, and 2027 is genuinely tight. It is still not fully
consumed; be ready for the question.

**5. Minimum cash is €7,062 in Oct-2026**, immediately before the equity
injection. Pre-existing and unchanged by this work, but that is a rounding error
away from insolvency. Pull the raise forward or add a bridge.

---

## The biggest remaining risk — and it is not volume any more

**The BOM cost-down is now the single load-bearing assumption.** The turbineketel
BOM falls €9,984 → €7,069 → €4,998 across the volume tiers: a **50% unit cost
reduction** from 1,000 to 10,000 units. Essentially all of the 2029 profitability
comes from crossing that second tier. It is the client's own supplier assumption
and I have not touched it, but now that volume is defensible this is where a VC
will push hardest. It needs supplier quotes behind it.

Secondary: the `D83` tier-basis switch still swings 2028 EBITDA by €12m
(+€17.3m on the year's own volume vs +€29.9m on this-year-plus-next). Two-year
tiering means committing to next year's volume with the supplier. If that
commitment isn't contracted, the own-year basis is the honest one — which is why
it ships as the default.

---

## Still open

- **Get the file into Drive.** Connector can't take it inline. Open the working
  copy → File → Import → Upload → Replace spreadsheet, which keeps the link.
- **Financial statements stop at 2029**; the Growth Engine and Diligence tab run
  to 2030. The headline 22,000-unit year is therefore not in the P&L. Extending
  the FS grid is a contained but real piece of work — worth doing before this
  goes out if 2030 is the pitch year.
- Client sign-off on the derived volumes, and on the 2027 correction to ~1,040.
- Stale Drive copy still needs renaming to `ARCHIVE 2026-08-19 pre-drop-combi`.
- Pitchdeck dashboard B4/B5 COGS wiring; possible 2028 service-cost double-count
  in COGS BE20 (~€79.5k).

## Sources for the external anchors

- NL heat pump volumes 2023–2025: [IIF/IIR](https://iifiir.org/en/news/policy-support-drives-11-growth-in-heat-pump-uptake-across-europe-in-2025), [JRC](https://publications.jrc.ec.europa.eu/repository/bitstream/JRC137131/JRC137131_027.pdf)
- ~400k gas boilers/yr, 8.2m dwellings: [CE Delft](https://cedelft.eu/publications/standardisation-of-heating-installations/)
- HVAC CPL and close-rate benchmarks: [BaaDigi](https://www.baadigi.com/tools/benchmarks/hvac), [DUO Digital](https://goduo.co/blog/hvac-marketing-benchmarks-2026/)
- B2B rep ramp ~5.7 months: [Lative](https://lative.ai/blog/sales-ramp-time/)
- Product/company: [Tarnoc](https://tarnoc.nl/en/)
