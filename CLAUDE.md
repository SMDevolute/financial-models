# Financial Models

A dedicated home for financial modeling work — kept separate from the Evolute
project-management tool.

## Working here
- Use the **`financial-modeler`** subagent (defined in
  `.claude/agents/financial-modeler.md`) for any modeling task: 3-statement
  models, DCF/LBO valuations, fundraise & cap-table models, unit economics,
  forecasts, scenario/sensitivity analysis.
- The user is non-technical on tooling and wants things *done*, not handed back
  as setup steps. Install any needed packages and execute — don't write
  tutorials. Verify outputs yourself.

## Layout
- `models/` — finished/working model files (`.xlsx`, sheets, notebooks).
- `data/`   — input data, exports, source numbers.
- `docs/`   — assumptions memos and write-ups that accompany a model.
- `scripts/`— reusable Python build scripts (e.g. openpyxl model generators).

## Conventions
- Excel output should carry **live formulas** (built via Python + `openpyxl`),
  not pre-computed numbers, so inputs can be flexed.
- **Always style via `scripts/house_style.py`** so models look designed, not
  auto-generated (gridlines off, Arial, navy section bars, parenthesised
  negatives, blue inputs / black formulas / green links, zebra banding, freeze
  panes). `scripts/demo_model.py` → `models/demo_styled_model.xlsx` is the
  reference. The palette is themed to Evolute's brand in `house_style.PALETTE`.
- Every model has an assumptions block and a checks area (BS balances, CF ties,
  sources = uses). State currency, units, and fiscal calendar.
