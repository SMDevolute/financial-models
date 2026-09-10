"""
build_scenarios.py -- add a Scenarios tab to a built Tarnoc workbook.

    python3 scripts/build_scenarios.py models/Tarnoc_v2_base_2026-09-07.xlsx

Three sets of assumptions, run through the model, written side by side. The
figures are stored values, exact and computed from the full monthly model, not
a simplified re-derivation. Row 39 recomputes the live base case and compares
it with the stored Plan column, so a stale table shows itself.

Run this after scripts/build_tarnoc_v2.py, on the base and aggressive
workbooks. The row that recomputes the live model and subtracts the stored Plan
column turns red if the two ever part company.
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
# Plan is the workbook as it stands. Downside and Upside move the drivers that
# actually change the case, expressed as multipliers on whatever the workbook
# holds, so the same definitions work for base and aggressive.
#
# Deliberately absent: rep quota, units per partner and debtor days move both
# cases by nothing, because demand is the lowest of the three constraints in
# almost every month. Assembly partner capacity is in the base tab (it limits
# base volume from August 2030) and out of the aggressive tab (the in-house
# lines mean it never binds there, and it moves aggressive EBITDA by nil).

MULT = {
    'Downside': dict(mkt=0.70, cpl=1.25, close=0.80, ptr=0.75, ord=0.60,
                     ttk=0.94, tier2=0.85, tier3=0.70, cap=1.00),
    'Plan':     dict(mkt=1.00, cpl=1.00, close=1.00, ptr=1.00, ord=1.00,
                     ttk=1.00, tier2=None, tier3=None, cap=1.00),
    'Upside':   dict(mkt=1.40, cpl=0.83, close=1.13, ptr=1.25, ord=1.40,
                     ttk=1.00, tier2=None, tier3=None, cap=1.54),
}

L_MKT = 'Marketing spend'
L_PTR = 'Installer partners signed per month'
L_ORD = 'Orders an installer partner brings in per month'
L_CPL = 'Cost per lead'
L_CLOSE = 'Qualified to won'
L_TTK = 'Turbineketel list price'
L_CAP = 'Assembly partner capacity'


class Book:
    """Read the plan's own assumption values, by label, as the shadow does."""

    def __init__(self, path):
        self.AS = openpyxl.load_workbook(path, data_only=True)['Assumptions']
        self.LBL = {}
        for r in range(1, 200):
            b = self.AS.cell(r, 2).value
            if isinstance(b, str):
                self.LBL.setdefault(b.strip(), r)
        single = not any(k.startswith('Case   1 = Base') for k in self.LBL)
        self.VALCOL, self.YOFF = (4, 1) if single else (6, 3)

    def single(self, label):
        return self.AS.cell(self.LBL[label], self.VALCOL).value

    def year(self, label):
        return [self.AS.cell(self.LBL[label] + self.YOFF, 4 + k).value or 0.0 for k in range(5)]

    def tier(self, name):
        return self.AS.cell(self.LBL[name], 5).value


def overrides_for(bk, name, has_lines):
    m = MULT[name]
    if name == 'Plan':
        return {}
    ov = {'single': {}, 'year': {}, 'cell': []}
    ov['single'][L_CPL] = round(bk.single(L_CPL) * m['cpl'])
    ov['single'][L_CLOSE] = round(bk.single(L_CLOSE) * m['close'], 3)
    ov['single'][L_TTK] = round(bk.single(L_TTK) * m['ttk'])
    if not has_lines and m['cap'] != 1.0:
        ov['single'][L_CAP] = round(bk.single(L_CAP) * m['cap'])
    ov['year'][L_MKT] = [round(v * m['mkt']) for v in bk.year(L_MKT)]
    ov['year'][L_PTR] = [round(v * m['ptr'], 2) for v in bk.year(L_PTR)]
    ov['year'][L_ORD] = [round(v * m['ord'], 2) for v in bk.year(L_ORD)]
    if m['tier2']:
        t1 = bk.tier('Tier 1')
        ov['cell'] = [['Tier 2', 5, round(t1 * m['tier2'])],
                      ['Tier 3', 5, round(t1 * m['tier3'])]]
    return ov


def rng(vals):
    """A year table shown as its 2027 and 2030 ends."""
    def sh(v):
        return f'{v/1000:,.0f}k' if v >= 1000 else f'{v:,.2f}'.rstrip('0').rstrip('.')
    return f'{sh(vals[1])} to {sh(vals[4])}'


def shown_rows(bk, has_lines):
    """The WHAT CHANGES block: label -> {scenario: displayed value}, plus format and note."""
    t1 = bk.tier('Tier 1')
    rows = []
    rows.append(('BOM cost-down achieved by 2030',
                 {'Downside': '30%', 'Plan': '50%', 'Upside': '50%'}, None,
                 f'Sets the tier 2 and tier 3 prices. Tier 1 is EUR{t1:,.0f}. '
                 f'There is no supplier quote for any of the three tiers.'))
    rows.append(('Marketing spend a month, 2027 to 2030',
                 {n: rng([round(v * MULT[n]['mkt']) for v in bk.year(L_MKT)]) for n in NAMES},
                 None, 'Downside is 70% of the plan, upside is 140%.'))
    rows.append((L_CPL,
                 {n: round(bk.single(L_CPL) * MULT[n]['cpl']) for n in NAMES}, NUM,
                 f"The client's figure is EUR{bk.single(L_CPL):,.0f}."))
    rows.append(('Close rate, qualified to won',
                 {n: round(bk.single(L_CLOSE) * MULT[n]['close'], 3) for n in NAMES}, PCT,
                 'Published benchmarks for this kind of sale run 20% to 40%.'))
    rows.append(('Partners signed a month, 2027 to 2030',
                 {n: rng([round(v * MULT[n]['ptr'], 2) for v in bk.year(L_PTR)]) for n in NAMES},
                 None, 'Downside signs 75% of the plan, upside 125%.'))
    rows.append(('Orders each partner brings a month',
                 {n: rng([round(v * MULT[n]['ord'], 2) for v in bk.year(L_ORD)]) for n in NAMES},
                 None, "No contract behind this. It is the client's estimate."))
    if not has_lines:
        rows.append(('Assembly partner capacity a month',
                     {n: round(bk.single(L_CAP) * MULT[n]['cap']) for n in NAMES}, NUM,
                     'At 650 a month the partner limits volume from August 2030.'))
    rows.append(('Turbineketel list price',
                 {n: round(bk.single(L_TTK) * MULT[n]['ttk']) for n in NAMES}, NUM,
                 f'The tier 1 BOM for this unit is EUR{t1:,.0f}.'))
    return rows


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

    bk = Book(calc)
    has_lines = 'Capacity per in-house line' in bk.LBL
    case = 'aggressive' if has_lines else 'base'
    raise_amt = bk.single('Second round, amount') or 0.0

    res = {n: outcomes(run_model(calc, overrides_for(bk, n, has_lines))) for n in NAMES}

    # the stored Plan column must reproduce the workbook it came from
    live = openpyxl.load_workbook(calc, data_only=True)['Dashboard']
    for drow, key in ((6, 'units'), (14, 'rev'), (18, 'ebitda')):
        want = live.cell(drow, 8).value or 0.0            # column H = 2030
        got = res['Plan'][key][4]
        if abs(want - got) > 0.02:
            sys.exit(f'Plan column does not reproduce the workbook on Dashboard row {drow}: '
                     f'{got:,.2f} vs {want:,.2f}')
    print('  Plan column reproduces the workbook on units, revenue and EBITDA')

    wb = openpyxl.load_workbook(path)
    if 'Scenarios' in wb.sheetnames:
        del wb['Scenarios']
    ws = wb.create_sheet('Scenarios', 1)
    ws.sheet_view.showGridLines = False
    for cl, w in (('A', 3), ('B', 46), ('C', 16), ('D', 16), ('E', 16), ('F', 2), ('G', 62)):
        ws.column_dimensions[cl].width = w

    def bar(r, text):
        ws.cell(r, 2, text).font = f(bold=True, color=WHITE)
        for c in range(2, 8):
            ws.cell(r, c).fill = fill(FILL_BLACK)
        for k, n in enumerate(NAMES):
            c = ws.cell(r, 3 + k, n)
            c.font = f(bold=True, color=WHITE)
            c.alignment = R

    def row(r, label, vals, fmt=NUM, indent=False, kind='plain', note=None, colours=None):
        c = ws.cell(r, 2, ('    ' if indent else '') + label)
        c.font = f(bold=(kind in ('total', 'check')))
        band = {'input': FILL_INPUT, 'total': FILL_SUB,
                'ratio': FILL_SUBSEC, 'check': 'FFF7F7F7'}.get(kind)
        if band:
            for cc in range(2, 6):
                ws.cell(r, cc).fill = fill(band)
        for k, n in enumerate(NAMES):
            cell = ws.cell(r, 3 + k, vals[n])
            cell.font = f(bold=(kind in ('total', 'check')),
                          color=(colours or {}).get(n, INK))
            cell.alignment = R
            if isinstance(vals[n], (int, float)) and fmt:
                cell.number_format = fmt
        if note:
            nc = ws.cell(r, 7, note)
            nc.font = f(italic=True, color=GREY, size=9, name=NOTE_FONT)
            nc.alignment = L

    ws['B1'] = f'Tarnoc B.V.  Scenario analysis, {case} case'
    for cl in 'BCDEFG':
        ws[f'{cl}1'].fill = fill(FILL_BLACK)
    ws['B1'].font = f(bold=True, color=WHITE)
    ws['B2'] = ('Three sets of assumptions run through the same model. The yellow cells are '
                'what changes. All figures in euros.')
    ws['B2'].font = f(italic=True, color=GREY, size=9, name=NOTE_FONT)

    r = 4
    bar(r, 'WHAT CHANGES'); r += 1
    for label, vals, fmt, note in shown_rows(bk, has_lines):
        row(r, label, vals, fmt=fmt, kind='input', note=note)
        r += 1

    r += 1
    bar(r, 'VOLUME'); r += 1
    for k, y in enumerate((2027, 2028, 2029, 2030)):
        row(r, f'Units sold {y}' if k == 0 else str(y),
            {n: round(res[n]['units'][k + 1]) for n in NAMES}, indent=(k > 0))
        r += 1
    UNITS30 = r - 1
    row(r, 'Installed base at the end of 2030', {n: round(res[n]['ib']) for n in NAMES}); r += 1
    row(r, '2028 plus 2029 volume', {n: round(res[n]['twoyr']) for n in NAMES}, kind='ratio',
        note='This figure sets the BOM price tier for 2028.'); r += 1
    row(r, 'Clears the 5,000-unit tier',
        {n: ('Yes' if res[n]['twoyr'] >= 5000 else 'No') for n in NAMES}, kind='check',
        note='Below 5,000 the 2028 BOM is charged at the tier 1 price.',
        colours={n: (INK if res[n]['twoyr'] >= 5000 else RED) for n in NAMES}); r += 2

    bar(r, 'PROFIT'); r += 1
    row(r, 'Revenue 2030', {n: round(res[n]['rev'][4]) for n in NAMES}); REV30 = r; r += 1
    misses = [n for n in NAMES if res[n]['twoyr'] < 5000]
    row(r, 'Gross margin 2030', {n: res[n]['gm30'] for n in NAMES}, fmt=PCT, kind='ratio',
        note=('A case that never passes 5,000 units is charged the tier 1 BOM in every year.'
              if misses else
              'All three clear the volume tiers. The downside margin is lower because its '
              'BOM cost-down is 30% rather than 50%.'))
    r += 1
    for k, y in enumerate((2027, 2028, 2029)):
        row(r, f'EBITDA {y}' if k == 0 else str(y),
            {n: round(res[n]['ebitda'][k + 1]) for n in NAMES}, indent=(k > 0),
            colours={n: (RED if res[n]['ebitda'][k + 1] < 0 else INK) for n in NAMES})
        r += 1
    row(r, 'EBITDA 2030', {n: round(res[n]['ebitda'][4]) for n in NAMES}, kind='total',
        colours={n: (RED if res[n]['ebitda'][4] < 0 else INK) for n in NAMES})
    EB30 = r; r += 1
    row(r, 'First profitable year',
        {n: (res[n]['first_profit'] or 'none by 2030') for n in NAMES}, fmt='0', kind='check',
        colours={n: (INK if res[n]['first_profit'] else RED) for n in NAMES}); r += 2

    bar(r, 'CASH AND THE RAISE'); r += 1
    row(r, 'Lowest cash after the raise', {n: round(res[n]['low']) for n in NAMES},
        colours={n: (INK if res[n]['low'] >= 0 else RED) for n in NAMES}); r += 1
    row(r, 'the month it happens', {n: month_name(res[n]['low_i']) for n in NAMES},
        indent=True); r += 1
    row(r, 'Months of operating cost that covers', {n: res[n]['cover'] for n in NAMES},
        fmt=NUM1, kind='ratio', note='Investors typically expect two to three months.',
        colours={n: (INK if res[n]['cover'] >= 0 else RED) for n in NAMES}); r += 1
    row(r, f'Share of the EUR{raise_amt/1e6:,.0f}m raise the plan uses',
        {n: res[n]['used'] for n in NAMES}, fmt=PCT, kind='ratio'); r += 1
    short = res['Downside']['short']
    row(r, f'Needs more than the EUR{raise_amt/1e6:,.0f}m raise',
        {n: (f'Yes, EUR{res[n]["short"]/1e6:,.1f}m more' if res[n]['short'] > 0 else 'No')
         for n in NAMES}, kind='check',
        note=(f'The downside is EUR{short/1e6:,.1f}m short at its lowest point, in '
              f'{month_name(res["Downside"]["low_i"])}.' if short > 0 else
              'All three scenarios stay inside the raise.'),
        colours={n: (RED if res[n]['short'] > 0 else INK) for n in NAMES}); r += 2

    CHK = r
    ws.cell(CHK, 2, 'Check   stored Plan column less the live model, must be nil').font = f(bold=True)
    for cc in range(2, 6):
        ws.cell(CHK, cc).fill = fill('FFF7F7F7')
    chk = ws.cell(CHK, 4, f'=ROUND(Dashboard!H6-D{UNITS30},0)+ROUND(Dashboard!H14-D{REV30},0)'
                          f'+ROUND(Dashboard!H18-D{EB30},0)')
    chk.font = f(bold=True); chk.alignment = R; chk.number_format = NUM
    ws.conditional_formatting.add(f'D{CHK}', FormulaRule(
        formula=[f'ABS($D${CHK})>0.5'],
        font=Font(name=FONT, size=10, bold=True, color=RED)))
    nc = ws.cell(CHK, 7, 'Turns red if an assumption is changed and the scenarios are not '
                         'rebuilt. Rebuild with scripts/build_scenarios.py.')
    nc.font = f(italic=True, color=GREY, size=9, name=NOTE_FONT); nc.alignment = L
    ws.cell(CHK + 1, 2, f'Scenarios computed {dt.date.today().strftime("%-d %B %Y")} from '
                        f'{os.path.basename(path)}.').font = f(italic=True, color=GREY, size=9,
                                                               name=NOTE_FONT)

    # ---- chart data, written out so the charts can be checked ----
    D0 = CHK + 45
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

    bc = BarChart()
    bc.type = 'col'; bc.grouping = 'clustered'
    bc.title = 'EBITDA by year, euros'
    bc.height, bc.width = 8.2, 15.5
    bc.y_axis.numFmt = '#,##0'; bc.gapWidth = 60; bc.overlap = -10
    bc.add_data(Reference(ws, min_col=3, max_col=5, min_row=D0, max_row=D0 + 4),
                titles_from_data=True)
    bc.set_categories(Reference(ws, min_col=2, min_row=D0 + 1, max_row=D0 + 4))
    for s, n in zip(bc.series, NAMES):
        s.graphicalProperties.solidFill = SERIES_COLOUR[n]
        s.graphicalProperties.line.solidFill = SERIES_COLOUR[n]
    ws.add_chart(bc, f'B{CHK + 3}')

    lc = LineChart()
    lc.title = 'Cash balance by month, euros'
    lc.height, lc.width = 8.2, 15.5
    lc.y_axis.numFmt = '#,##0'
    lc.add_data(Reference(ws, min_col=3, max_col=5, min_row=C0, max_row=C0 + 60),
                titles_from_data=True)
    lc.set_categories(Reference(ws, min_col=2, min_row=C0 + 1, max_row=C0 + 60))
    for s, n in zip(lc.series, NAMES):
        s.graphicalProperties.line = LineProperties(solidFill=SERIES_COLOUR[n], w=20000)
        s.marker = Marker(symbol='none'); s.smooth = False
    ws.add_chart(lc, f'B{CHK + 23}')

    ws.freeze_panes = 'C5'
    wb.save(path)
    print(f'  Scenarios tab written to {path} ({case} case)')
    for n in NAMES:
        o = res[n]
        print(f'    {n:9s} units 2030 {o["units"][4]:>7,.0f}  2yr {o["twoyr"]:>7,.0f}  '
              f'EBITDA30 {o["ebitda"][4]:>14,.0f}  cash low {o["low"]:>13,.0f}  '
              f'cover {o["cover"]:>6.1f}')
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    for p in sys.argv[1:]:
        print(os.path.basename(p))
        build(os.path.abspath(p))
