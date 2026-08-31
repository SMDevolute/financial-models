# Tarnoc — to-do (2026-09-01)

## Where we left off (2026-08-31)
Built the €10M aggressive case as a **toggled** model, not a fork:
`models/Tarnoc_LIVE_2026-08-31_10m-aggressive.xlsx` (built by
`scripts/build_tarnoc_10m_case.py` from the live Drive sheet).

Switches on **Assumptions D82 / D83**:
- `D82` Case: 1 = Base €3m, 2 = Aggressive €10m
- `D83` BOM tier basis: 1 = year's own volume, 2 = this year + next

| Scenario | EBITDA 2027/28/29 (€m) |
| --- | --- |
| Base, 2yr tier (= the dataroom model, exact match) | −2.45 / +2.43 / +17.14 |
| Base, 1yr tier | −2.45 / −2.23 / −1.21 |
| Aggressive, 1yr tier (ships as default) | −1.34 / +17.12 / +66.08 |

Aggressive 2029: revenue €188.5m, net income €47.7m, end cash €62.4m.
Verified: zero formula errors, BS ties to 0.00 in every column, all four
switch combinations.

## Open items
1. **Get the file into Drive.** Connector upload can't take a 392K file inline.
   Route that keeps the existing link: open the working copy →
   File → Import → Upload → Replace spreadsheet.
   Working copy: https://docs.google.com/spreadsheets/d/1v2L3pv4kLDOTKnu7bEbKBLsHiOm94lYSdtMcMZ_CP7Y/edit
2. **Min cash €7k in Oct-2026**, just before the equity injection. Pre-existing,
   not introduced by this build, but uncomfortably tight — decide whether to
   pull the raise forward or add a buffer.
3. **€10m is never fully drawn** — 2027 ends with €5.8m. Either the raise is
   bigger than this plan needs, or the plan should be more aggressive still
   (faster hiring, earlier facility). Investor will ask.
4. **Demand credibility**: 1,800 units in 2027 (3x) and 22,000 by 2030. Capital
   buys reps and capacity, not demand. Needs a bottom-up sanity check
   (reps × ramped quota) before this goes to anyone.
5. **Volume plan sign-off** from the client on the aggressive figures.
6. **Blended 8yr depreciation life** — split into tooling (7yr) vs building
   (10yr) if anyone pushes on it.
7. **Scratch note still in the live dataroom sheet's How-to-read tab**
   ("Questions for vin… check prics of ttk and combi… VAT?"). Dataroom viewers
   can see it. Remove or move.
8. **Stale Drive copy**: `Copy of Tarnoc Financial Model 26/6/2026 (in dataroom)`
   is an Aug-19 pre-drop-combi snapshot sitting next to the live file. Agreed to
   rename it `ARCHIVE 2026-08-19 pre-drop-combi (do not use)` — not done yet.
9. **Carried over, still open**: Pitchdeck dashboard B4/B5 COGS wiring;
   possible 2028 service-cost double-count in COGS BE20 (~€79.5k).

## Corrections logged
- The Pitchdeck dashboard was **right**; the How-to-read narrative was the stale
  one (it claimed −3.3 / +0.7 / +11.6). Narrative text now refreshed.
- The `26/6/2026 (in dataroom)` file was the correct one to edit — the dataroom
  link resolves to its file ID. Editing it was not a mistake.
