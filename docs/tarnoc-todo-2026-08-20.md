# Tarnoc — to-do for tomorrow (2026-08-20)

Model state tonight: TTK + Combi+ only, volumes 600/1,800/3,600/7,200, EBITDA −3.3/+0.7/+11.6 €m, cash trough −€248k Jan/Feb-2028 (artifact of the Jan-1 BOM tier step meeting 45-day supplier terms).

## Decisions needed (Simon / client)
1. ~~**Jan-2028 cash dip**~~ **DONE 2026-08-20**: B36 rewritten — dip explained as a timing artifact (Jan-1 tier step vs 45-day supplier terms; cash benefit lags P&L by ~45 days; effective trough ≈ 0). Old "working-capital buffer" wording removed.
2. **Volume plan sign-off** — 600/1,800/3,600/7,200 is what the dataroom now shows; client should bless it.
3. **Notes columns** — the grey "what this row does" annotations are visible to dataroom viewers. Keep visible or hide the columns?

## Model work queued
4. Pitchdeck dashboard tab: B4/B5 Financials rows only partly wired (COGS points at the TTK-only row, not all years covered) — fix and re-check both dashboards against the new volumes.
5. Possible 2028 service-cost double-count: COGS BE20 adds 2027's total on top of its monthly sum (revenue side doesn't). ~€79.5k. Decide fix or leave.
6. FS BF36 hardcodes 5% instead of Assumptions!C11 (harmless while loan balance is 0) — decide fix or leave.
7. Refresh "How to read me" summary if any input changes (rows 34–37 are static text).

## Housekeeping
8. Commit today's model backups in `models/` to git (branch `tarnoc-combi-model`): pre/post drop-combi and pre/post row-notes snapshots, plus the older untracked Evolute files.
