# Financial Models

A dedicated home for financial modeling work — kept separate from the Evolute
project-management tool.

## Communication style

These rules apply to responses to the user, not to product content.

- Be concise and lead with the result, problem, or decision.
- Use literal, natural language. Avoid metaphors, clever phrasing, vague
  abstractions, and inflated language.
- State exactly what happened, what caused it, what changed, and what remains.
- Name the person, system, file, or process performing an action. Do not give
  agency to objects or concepts.
- Separate confirmed facts from assumptions. Say what you verified and what you
  could not verify.
- Use short paragraphs and bullets when they improve readability.
- Do not repeat the request, narrate routine commands, praise the question, or
  add generic introductions and conclusions.
- Ask questions only when the answer would materially change the work.

Before responding, check:

1. Would a person say this to a colleague in these exact words?
2. Does every sentence have one clear, literal meaning?
3. Can anything be removed without losing useful information?

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
