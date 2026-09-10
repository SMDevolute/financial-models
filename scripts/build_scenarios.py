"""
build_scenarios.py -- add a Scenarios tab to a built Tarnoc workbook.

    python3 scripts/build_scenarios.py models/Tarnoc_v2_base_2026-09-07.xlsx

Three sets of assumptions, run through the model, written side by side. The
figures are stored values, exact and computed from the full monthly model, not
a simplified re-derivation. Row 39 recomputes the live base case and compares
it with the stored Plan column, so a stale table shows itself.

Run this after scripts/build_tarnoc_v2.py, on the base workbook and on the
combined one. The aggressive workbook has no base case, so it is skipped.
"""
import datetime as dt
import json
import os
import runpy
import shutil
import subprocess
import sys
import tempfile

import openpyxl
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.chart.marker import Marker
from openpyxl.drawing.line import LineProperties
from openpyxl.formatting.rule import FormulaRule
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter as gl

HERE = os.path.dirname(os.path.abspath(__file__))
SHADOW = os.path.join(HERE, 'audit_v2_shadow.py')
SOFFICE = shutil.which('soffice') or '/Applications/LibreOffice.app/Contents/MacOS/soffice'

# ---- house style, same constants as build_tarnoc_v2.py ---------------------
FONT, NOTE_FONT = 'Geist', 'Arial'
INK, WHITE = 'FF000000', 'FFFFFFFF'
GREY, RED = 'FF999999', 'FFFF0000'
FILL_BLACK, FILL_SUB, FILL_INPUT = 'FF000000', 'FFF3F3F3', 'FFFFF2CC'
FILL_SUBSEC = 'FFEFEFEF'
NUM = r'#,##0;\(#,##0\);\-'
NUM1 = r'#,##0.0;\(#,##0.0\);\-'
PCT = '0%'
SERIES_COLOUR = {'Downside': 'C00000', 'Plan': '000000', 'Upside': '7F7F7F'}
NAMES = ('Downside', 'Plan', 'Upside')

def f(bold=False, italic=False, color=INK, size=10, name=FONT):
    return Font(name=name, size=size, bold=bold, italic=italic, color=color)

def fill(rgb):
    return PatternFill('solid', fgColor=rgb)

R = Alignment(horizontal='right')
L = Alignment(horizontal='left', vertical='center')

# ---------------------------------------------------------------------------
# the three scenarios
# ---------------------------------------------------------------------------
# Plan is the workbook as it stands. Downside and Upside move six drivers, the
# six that actually change the base case. Rep quota, units per partner and
# debtor days are left alone because demand is the binding constraint in every
# month, so moving them changes nothing.
MKT_PLAN = [0, 13000, 40000, 115000, 160000]

SCENARIOS = {
    'Downside': {
        'single': {'Cost per lead': 150, 'Qualified to won': 0.32,
                   'Turbineketel list price': 8000.0},
        'year': {'Marketing spend': [round(v * 0.7) for v in MKT_PLAN],
                 'Installer partners signed per month': [0, 0.75, 1.1, 2.2, 2.9],
                 'Orders an installer partner brings in per month': [0, 0.6, 1.2, 1.8, 2.4]},
        'cell': [['Tier 2', 5, 8486.0], ['Tier 3', 5, 6989.0]],
    },
    'Plan': {},
    'Upside': {
        'single': {'Cost per lead': 100, 'Qualified to won': 0.45,
                   'Assembly partner capacity': 1000.0},
        'year': {'Marketing spend': [round(v * 1.4) for v in MKT_PLAN],
                 'Installer partners signed per month': [0, 1.25, 1.9, 3.75, 4.75],
                 'Orders an installer partner brings in per month': [0, 1.4, 2.8, 4.2, 5.6]},
    },
}

# what each scenario shows in the WHAT CHANGES block, as displayed
SHOWN = {
    'BOM cost-down achieved by 2030':        {'Downside': '30%', 'Plan': '50%', 'Upside': '50%'},
    'Marketing spend a month, 2027 to 2030': {'Downside': '9k to 112k', 'Plan': '13k to 160k',
                                              'Upside': '18k to 224k'},
    'Cost per lead':                          {'Downside': 150, 'Plan': 120, 'Upside': 100},
    'Close rate, qualified to won':           {'Downside': 0.32, 'Plan': 0.40, 'Upside': 0.45},
    'Partners signed a month, 2027 to 2030':  {'Downside': '0.8 to 2.9', 'Plan': '1.0 to 3.8',
                                              'Upside': '1.3 to 4.8'},
    'Orders each partner brings a month':     {'Downside': '0.6 to 2.4', 'Plan': '1 to 4',
                                              'Upside': '1.4 to 5.6'},
    'Assembly partner capacity a month':      {'Downside': 650, 'Plan': 650, 'Upside': 1000},
    'Turbineketel list price':                {'Downside': 8000, 'Plan': 8526, 'Upside': 8526},
}
SHOWN_FMT = {'Cost per lead': NUM, 'Close rate, qualified to won': PCT,
             'Assembly partner capacity a month': NUM, 'Turbineketel list price': NUM}

RAISE_MONTH = 9          # October 2026, the month the equity lands


def run_model(path, overrides):
    os.environ['SHADOW_OVERRIDES_JSON'] = json.dumps(overrides)
    os.environ['SHADOW_QUIET'] = '1'
    old = sys.argv[:]
    sys.argv = [SHADOW, path, '1']
    try:
        return runpy.run_path(SHADOW, run_name='__scenarios__')['S']
    finally:
        sys.argv = old
        os.environ.pop('SHADOW_OVERRIDES_JSON', None)
        os.environ.pop('SHADOW_QUIET', None)


def outcomes(S):
    yr = lambda k, i: sum(S[k][12 * i:12 * i + 12])
    units = [yr('units', i) for i in range(5)]
    rev = [yr('r_tot', i) for i in range(5)]
    gp = [yr('f8', i) for i in range(5)]
    ebitda = [yr('f16', i) for i in range(5)]
    cash = S['f40']
    post = cash[RAISE_MONTH:]
    low = min(post)
    low_i = RAISE_MONTH + post.index(low)
    opex_m = abs(yr('f14', low_i // 12)) / 12
    at_raise = cash[RAISE_MONTH]
    return dict(
        units=units, rev=rev, ebitda=ebitda, cash=cash,
        ib=S['ib_close'][-1], twoyr=units[2] + units[3],
        gm30=(gp[4] / rev[4] if rev[4] else 0.0),
        low=low, low_i=low_i,
        cover=(low / opex_m if opex_m else 0.0),
        used=((at_raise - low) / at_raise if at_raise else 0.0),
        first_profit=next((2026 + i for i, e in enumerate(ebitda) if e > 0), None),
        short=(-low if low < 0 else 0.0),
    )


def month_name(i):
    return dt.date(2026 + i // 12, i % 12 + 1, 1).strftime('%b %Y')


def build(path):
    tmp = tempfile.mkdtemp(prefix='scen_')
    subprocess.run([SOFFICE, '--headless', '--norestore', '--convert-to', 'xlsx',
                    '--outdir', tmp, path], capture_output=True, timeout=900)
    calc = os.path.join(tmp, os.path.basename(path))
    if not os.path.exists(calc):
        sys.exit('could not recalculate the workbook in LibreOffice')

    res = {n: outcomes(run_model(calc, SCENARIOS[n])) for n in NAMES}

    # the stored Plan column must equal the workbook it came from
    live = openpyxl.load_workbook(calc, data_only=True)['Dashboard']
    for row, key, idx in ((6, 'units', 4), (14, 'rev', 4), (18, 'ebitda', 4)):
        want = live.cell(row, 8).value or 0.0            # column H = 2030
        got = res['Plan'][key][idx]
        if abs(want - got) > 0.02:
            sys.exit(f'Plan column does not reproduce the workbook on Dashboard row {row}: '
                     f'{got:,.2f} vs {want:,.2f}')
    print(f'  Plan column reproduces the workbook on units, revenue and EBITDA')

    wb = openpyxl.load_workbook(path)
    if 'Scenarios' in wb.sheetnames:
        del wb['Scenarios']
    ws = wb.create_sheet('Scenarios', 1)
    ws.sheet_view.showGridLines = False
    for cl, w in (('A', 3), ('B', 46), ('C', 16), ('D', 16), ('E', 16), ('F', 2), ('G', 62)):
        ws.column_dimensions[cl].width = w
    NOTE = 'G'

    def bar(r, text, heads=True):
        ws.cell(r, 2, text).font = f(bold=True, color=WHITE)
        for c in range(2, 8):
            ws.cell(r, c).fill = fill(FILL_BLACK)
        if heads:
            for k, n in enumerate(NAMES):
                c = ws.cell(r, 3 + k, n)
                c.font = f(bold=True, color=WHITE)
                c.alignment = R

    def row(r, label, vals, fmt=NUM, indent=False, kind='plain', note=None, colours=None):
        c = ws.cell(r, 2, ('    ' if indent else '') + label)
        c.font = f(bold=(kind in ('total', 'check')))
        if kind == 'input':
            band = FILL_INPUT
        elif kind == 'total':
            band = FILL_SUB
        elif kind == 'ratio':
            band = FILL_SUBSEC
        elif kind == 'check':
            band = 'FFF7F7F7'
        else:
            band = None
        if band:
            for cc in range(2, 6):
                ws.cell(r, cc).fill = fill(band)
        for k, n in enumerate(NAMES):
            cell = ws.cell(r, 3 + k, vals[n])
            col = (colours or {}).get(n, INK)
            cell.font = f(bold=(kind in ('total', 'check')), color=col)
            cell.alignment = R
            if isinstance(vals[n], (int, float)):
                cell.number_format = fmt
        if note:
            nc = ws.cell(r, 7, note)
            nc.font = f(italic=True, color=GREY, size=9, name=NOTE_FONT)
            nc.alignment = L

    # ---- header ----
    ws['B1'] = 'Tarnoc B.V.  Scenario analysis, base case'
    for cl in 'BCDEFG':
        ws[f'{cl}1'].fill = fill(FILL_BLACK)
    ws['B1'].font = f(bold=True, color=WHITE)
    ws['B2'] = ('Three sets of assumptions run through the same model. The yellow cells are '
                'what changes. All figures in euros.')
    ws['B2'].font = f(italic=True, color=GREY, size=9, name=NOTE_FONT)

    bar(4, 'WHAT CHANGES')
    notes_changes = {
        'BOM cost-down achieved by 2030': 'Sets the tier 2 and tier 3 prices. There is no supplier quote for any of the three tiers.',
        'Marketing spend a month, 2027 to 2030': 'Downside is 70% of the plan, upside is 140%.',
        'Cost per lead': "The client's figure is EUR120.",
        'Close rate, qualified to won': 'Published benchmarks for this kind of sale run 20% to 40%.',
        'Partners signed a month, 2027 to 2030': 'The plan reaches 113 partners on the books by the end of 2030.',
        'Orders each partner brings a month': "No contract behind this. It is the client's estimate.",
        'Assembly partner capacity a month': 'At 650 a month the partner limits volume in 2030.',
        'Turbineketel list price': 'The tier 1 BOM for this unit is EUR9,984.',
    }
    r = 5
    for label, vals in SHOWN.items():
        row(r, label, vals, fmt=SHOWN_FMT.get(label, NUM), kind='input',
            note=notes_changes[label])
        r += 1

    bar(14, 'VOLUME')
    for k, y in enumerate((2027, 2028, 2029, 2030)):
        row(15 + k, f'Units sold {y}' if k == 0 else str(y),
            {n: round(res[n]['units'][k + 1]) for n in NAMES}, indent=(k > 0))
    row(19, 'Installed base at the end of 2030', {n: round(res[n]['ib']) for n in NAMES})
    row(20, '2028 plus 2029 volume', {n: round(res[n]['twoyr']) for n in NAMES}, kind='ratio',
        note='This figure sets the BOM price tier for 2028.')
    row(21, 'Clears the 5,000-unit tier',
        {n: ('Yes' if res[n]['twoyr'] >= 5000 else 'No') for n in NAMES}, kind='check',
        note='Below 5,000 the 2028 BOM is EUR9,984 a unit instead of EUR7,069.',
        colours={n: (INK if res[n]['twoyr'] >= 5000 else RED) for n in NAMES})

    bar(23, 'PROFIT')
    row(24, 'Revenue 2030', {n: round(res[n]['rev'][4]) for n in NAMES})
    row(25, 'Gross margin 2030', {n: res[n]['gm30'] for n in NAMES}, fmt=PCT, kind='ratio',
        note='The downside stays below 5,000 units, so it is charged the tier 1 BOM in every year.')
    for k, y in enumerate((2027, 2028, 2029)):
        row(26 + k, f'EBITDA {y}' if k == 0 else str(y),
            {n: round(res[n]['ebitda'][k + 1]) for n in NAMES}, indent=(k > 0))
    row(29, 'EBITDA 2030', {n: round(res[n]['ebitda'][4]) for n in NAMES}, kind='total')
    row(30, 'First profitable year',
        {n: (res[n]['first_profit'] or 'none by 2030') for n in NAMES}, fmt='0', kind='check',
        note='The downside makes a loss in all five years.',
        colours={n: (INK if res[n]['first_profit'] else RED) for n in NAMES})

    bar(32, 'CASH AND THE RAISE')
    row(33, 'Lowest cash after the raise', {n: round(res[n]['low']) for n in NAMES},
        colours={n: (INK if res[n]['low'] >= 0 else RED) for n in NAMES})
    row(34, 'the month it happens', {n: month_name(res[n]['low_i']) for n in NAMES}, indent=True)
    row(35, 'Months of operating cost that covers', {n: res[n]['cover'] for n in NAMES},
        fmt=NUM1, kind='ratio', note='Investors typically expect two to three months.',
        colours={n: (INK if res[n]['cover'] >= 0 else RED) for n in NAMES})
    row(36, 'Share of the EUR3m raise the plan uses', {n: res[n]['used'] for n in NAMES},
        fmt=PCT, kind='ratio')
    row(37, 'Needs more than the EUR3m raise',
        {n: (f'Yes, EUR{res[n]["short"]/1e6:,.1f}m more' if res[n]['short'] > 0 else 'No')
         for n in NAMES}, kind='check',
        note=f'The downside is EUR{res["Downside"]["short"]/1e6:,.1f}m short at its lowest point, '
             f'in {month_name(res["Downside"]["low_i"])}.',
        colours={n: (RED if res[n]['short'] > 0 else INK) for n in NAMES})

    # ---- staleness guard ----
    ws.cell(39, 2, 'Check   stored Plan column less the live model, must be nil').font = f(bold=True)
    for cc in range(2, 6):
        ws.cell(39, cc).fill = fill('FFF7F7F7')
    chk = ws.cell(39, 4, '=ROUND(Dashboard!H6-D18,0)+ROUND(Dashboard!H14-D24,0)'
                         '+ROUND(Dashboard!H18-D29,0)')
    chk.font = f(bold=True)
    chk.alignment = R
    chk.number_format = NUM
    ws.conditional_formatting.add('D39', FormulaRule(formula=['ABS($D$39)>0.5'],
                                                     font=Font(name=FONT, size=10, bold=True,
                                                               color=RED)))
    nc = ws.cell(39, 7, 'Turns red if an assumption is changed and the scenarios are not rebuilt. '
                        'Rebuild with scripts/build_scenarios.py.')
    nc.font = f(italic=True, color=GREY, size=9, name=NOTE_FONT)
    nc.alignment = L
    ws.cell(40, 2, f'Scenarios computed {dt.date.today().strftime("%-d %B %Y")} from '
                   f'{os.path.basename(path)}.').font = f(italic=True, color=GREY, size=9,
                                                          name=NOTE_FONT)

    # ---- chart data, written plainly so the charts can be checked ----
    D0 = 84
    ws.cell(D0 - 1, 2, 'CHART DATA').font = f(bold=True, color=WHITE)
    for c in range(2, 8):
        ws.cell(D0 - 1, c).fill = fill(FILL_BLACK)
    ws.cell(D0, 2, 'EBITDA by year').font = f(bold=True)
    for k, n in enumerate(NAMES):
        c = ws.cell(D0, 3 + k, n); c.font = f(bold=True); c.alignment = R
    for k, y in enumerate((2027, 2028, 2029, 2030)):
        ws.cell(D0 + 1 + k, 2, y).font = f()
        for j, n in enumerate(NAMES):
            c = ws.cell(D0 + 1 + k, 3 + j, round(res[n]['ebitda'][k + 1]))
            c.number_format = NUM; c.font = f()

    C0 = D0 + 7
    ws.cell(C0, 2, 'Cash balance by month').font = f(bold=True)
    for k, n in enumerate(NAMES):
        c = ws.cell(C0, 3 + k, n); c.font = f(bold=True); c.alignment = R
    for i in range(60):
        ws.cell(C0 + 1 + i, 2, month_name(i)).font = f()
        for j, n in enumerate(NAMES):
            c = ws.cell(C0 + 1 + i, 3 + j, round(res[n]['cash'][i]))
            c.number_format = NUM; c.font = f()

    # ---- charts ----
    bc = BarChart()
    bc.type = 'col'
    bc.grouping = 'clustered'
    bc.title = 'EBITDA by year, euros'
    bc.height, bc.width = 8.2, 15.5
    bc.y_axis.numFmt = '#,##0'
    bc.gapWidth = 60
    bc.overlap = -10
    data = Reference(ws, min_col=3, max_col=5, min_row=D0, max_row=D0 + 4)
    cats = Reference(ws, min_col=2, min_row=D0 + 1, max_row=D0 + 4)
    bc.add_data(data, titles_from_data=True)
    bc.set_categories(cats)
    for s, n in zip(bc.series, NAMES):
        s.graphicalProperties.solidFill = SERIES_COLOUR[n]
        s.graphicalProperties.line.solidFill = SERIES_COLOUR[n]
    ws.add_chart(bc, 'B42')

    lc = LineChart()
    lc.title = 'Cash balance by month, euros'
    lc.height, lc.width = 8.2, 15.5
    lc.y_axis.numFmt = '#,##0'
    ldata = Reference(ws, min_col=3, max_col=5, min_row=C0, max_row=C0 + 60)
    lcats = Reference(ws, min_col=2, min_row=C0 + 1, max_row=C0 + 60)
    lc.add_data(ldata, titles_from_data=True)
    lc.set_categories(lcats)
    for s, n in zip(lc.series, NAMES):
        s.graphicalProperties.line = LineProperties(solidFill=SERIES_COLOUR[n], w=20000)
        s.marker = Marker(symbol='none')
        s.smooth = False
    ws.add_chart(lc, 'B62')

    ws.freeze_panes = 'C5'
    wb.save(path)
    print(f'  Scenarios tab written to {path}')
    for n in NAMES:
        o = res[n]
        print(f'    {n:9s} units 2030 {o["units"][4]:>7,.0f}  2yr {o["twoyr"]:>6,.0f}  '
              f'EBITDA30 {o["ebitda"][4]:>13,.0f}  cash low {o["low"]:>12,.0f}  '
              f'cover {o["cover"]:>5.1f}')
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    for p in sys.argv[1:]:
        print(os.path.basename(p))
        build(os.path.abspath(p))
