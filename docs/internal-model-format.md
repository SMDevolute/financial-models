# Evolute Internal Financial Model — Standard Format

The house format for all Evolute internal financial models. Reference build:
**"Evolute Financial Model 2027–2030"**
(`1p6r-lTWFvrTmX-FL0JdMfSLNWcnN3RGo9a8Kq4xtp4o`), with the canonical template copy
**"Evolute — Internal Model Format (TEMPLATE)"** kept in the same Drive folder.

Adapted from the Blue Heart Energy build-up system, using Evolute's original
Income-Statement framework.

## Tab structure (build-up order)
1. **Cover** — name, currency, basis, confidentiality, contents.
2. **How to read me** — structure, how to use, revenue logic, staffing notes.
3. **Assumptions** — the single source of truth. *Every* input lives here; no
   driver or assumption sits on any other tab. **Organise by business line**, not
   by "flat vs by-year": each revenue line gets ONE coherent block holding all
   its parameters together (retainer, length, fee, deal size, close rate). For
   Evolute: a **Growth Capital** block, an **M&A** block, a shared **Deal flow**
   block (total deals + mix), then **Sourcing & compensation**, **Personnel**,
   **OPEX**. Each block carries its own year header for its by-year rows.
4. **Revenue forecast** — strictly revenue. Per business line (e.g. Growth
   Capital, M&A): new deals → live projects → retainer → closings → success
   fees → totals → partner share → net revenue. **Deals must be whole numbers** —
   spread annual deals into integer monthly starts via cumulative rounding
   (`ROUND(annual*m/12) - ROUND(annual*(m-1)/12)`), never as fractions. Fractional
   deals produce nonsense (e.g. 0.17 of a live project paying retainer). Live
   projects = rolling sum over the engagement length; retainer = live × monthly
   rate; success fee on close (start + length) × close rate.
5. **Personnel** — headcount schedule (driven by live projects) + salary/comp
   build-up → total personnel.
6. **OPEX** — operating-cost schedule (FTE-scaled where appropriate).
7. **Financial Statements** — the **original Evolute Income-Statement
   framework** (do not condense): Revenues (Retainer / Closing fees / [Less:
   partner share] / Total) · Personnel (Gross salary / Bonus / Employer taxes /
   Contractors / Strategic Advisory / Other people costs / Total) · Gross profit
   · Other OPEX (Rent / Software / Office / Marketing & Sales / Travel / SG&A /
   Other / Total) · RX allocation · Total costs · EBITDA + margin · EBITDA
   without success fee + margin. It only *sources* values from the sub-tabs.
8. **Dashboard** — annual summary (revenue, EBITDA, margin, headcount, deals).

## Column convention
- **B** = line-item label, **C** = optional detail, **E** = unit (`€` / `#` / `%`).
- **Monthly columns run left→right from column F** (e.g. Jan 2027 … Dec 2030).
- **Annual roll-up columns at the far right** (one per year), built with
  `SUMPRODUCT((YEAR($F$3:$BA$3)=<year>)*<row>)` for flows, year-end (Dec) value
  for stocks/headcount. **No hidden YEAR helper rows.**
- The **Financial Statements** tab keeps Evolute's original layout (months from
  column **C**, annual columns to the right). It maps to the F-start sub-tabs
  with a fixed +3 column offset.

## Formula conventions
- Inputs live only on Assumptions; all other tabs reference it.
- By-year drivers use `INDEX/MATCH` on the year against the Assumptions year
  header. **Single-value assumptions (one cell, column C) must be referenced
  with an absolute `$C$n` — never via the year lookup, or 2028+ silently reads
  empty cells and returns 0.**
- Must work in **both Excel and Google Sheets** (see
  formulas-excel-gsheets-compatible memory) — avoid Google-only functions.

## Styling (house style)
- Arial; navy section-header bars (#10182D, white bold); bold subtotal rows on
  light grey; `€#,##0;(€#,##0)` with parenthesised negatives; `0.0%` for
  margins; `#,##0` for counts; month headers `mmm yy`; year headers plain `0`
  (never currency/date); freeze header rows + label columns.

## Verification checklist (always run before "done")
- Zero formula errors across all tabs.
- Annual columns tie exactly to the sum of their monthly columns (spot-check
  ≥2 years per statement).
- Year/number formats render correctly (years are not currency or 1900-era dates).
- Headline plan (revenue / EBITDA / headcount) reconciles end-to-end.
