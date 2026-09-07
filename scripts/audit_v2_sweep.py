"""
sweep.py -- run the model at thousands of different input points, not just the
base case, and check that it still behaves.

Every other phase of the audit tests one point in input space: the assumptions
exactly as they are typed today. A model can be right there and wrong when the
client triples the marketing budget or halves the close rate. This sweeps the
inputs across plausible ranges and asserts, on every draw, the things that must
hold whatever the inputs are.

Two kinds of finding, and they are not the same thing:

  MODEL FAULT   something that cannot be true of any business: a fractional
                person, a count that goes backwards, an identity that breaks,
                units above the constraint that set them. This is a bug.

  PLAN FAILS    the arithmetic is right and the business runs out of money or
                loses money. Not a bug. Reported separately so the two are
                never confused.

Usage:
    python3 scripts/audit_v2_sweep.py <workbook> [draws] [seed]
"""
import json, os, random, runpy, sys, math

SHADOW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'audit_v2_shadow.py')
RAW = sys.argv[1]
DRAWS = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
SEED = int(sys.argv[3]) if len(sys.argv) > 3 else 20260907
YEARS = [2026, 2027, 2028, 2029, 2030]

# ---- what gets perturbed, and how far ------------------------------------
# (label, kind, low, high) as a multiplier on the base value unless noted.
SINGLE_MULT = [
    ('Cost per lead',                              0.4, 3.0),
    ('Quota per rep',                              0.25, 2.0),
    ('Units per partner per month',                0.25, 2.5),
    ('Assembly partner capacity',                  0.15, 4.0),
    ('Turbineketel list price',                    0.7, 1.4),
    ('Combi+ price (ketel plus outdoor unit)',     0.7, 1.4),
    ('Outdoor unit, Combi+ only',                  0.6, 1.6),
    ('Installation, TTK',                          0.5, 2.0),
    ('Installation, Combi+',                       0.5, 2.0),
    ('Upsell revenue per unit sold',               0.0, 3.0),
    ('Upsell cost per unit sold',                  0.0, 3.0),
    ('Service revenue per installed unit per year', 0.0, 4.0),
    ('Service cost per installed unit per year',   0.0, 4.0),
    ('Units per supply chain and logistics FTE',   0.4, 3.0),
    ('Installed units per support agent',          0.4, 3.0),
    ('Installed units one field engineer can look after', 0.3, 3.0),
    ('Units per order desk FTE',                   0.4, 3.0),
    ('Partners per partner manager',               0.3, 3.0),
    ('Opening cash at Jan-2026',                   0.2, 3.0),
]
SINGLE_ABS = [                       # sampled directly, not as a multiplier
    ('Lead to qualified',                          0.05, 0.95),
    ('Qualified to won',                           0.05, 0.95),
    ('Share of the installed base on a contract',  0.0,  1.0),
    ('Installer partner commission, share of unit price', 0.0, 0.30),
    ('TTK share of units',                         0.0,  1.0),   # Combi+ takes the rest
    ('Days sales outstanding',                     0.0,  120.0),
    ('Days payable outstanding',                   0.0,  150.0),
    ('Annual salary increase',                     0.0,  0.20),
    ('Corporate income tax rate',                  0.0,  0.40),
]
YEAR_MULT = [
    ('Marketing spend',                            0.0, 5.0),
    ('Reps hired per month',                       0.0, 5.0),
    ('Installer partners signed per month',        0.0, 5.0),
    ('Orders an installer partner brings in per month', 0.0, 4.0),
]
YEAR_ABS = [
    ('Share of units sold direct',                 0.05, 1.0),
]

# ---- the workbook must be recalculated first -------------------------------
# Seven assumption cells are themselves formulas (the Combi+ price, the product
# split, the upsell and service baskets). Read straight off a workbook built by
# openpyxl they come back empty, and every number after them is wrong. So
# recalculate into a temp copy and sweep that.
import subprocess, tempfile, shutil
SOFFICE = shutil.which('soffice') or '/Applications/LibreOffice.app/Contents/MacOS/soffice'
TMP = tempfile.mkdtemp(prefix='sweep_')
subprocess.run([SOFFICE, '--headless', '--norestore', '--convert-to', 'xlsx',
                '--outdir', TMP, RAW], capture_output=True, timeout=600)
PATH = os.path.join(TMP, os.path.basename(RAW))
if not os.path.exists(PATH):
    sys.exit('could not recalculate the workbook in LibreOffice')

def run_shadow(overrides):
    env = dict(os.environ)
    env['SHADOW_OVERRIDES_JSON'] = json.dumps(overrides)
    env['SHADOW_QUIET'] = '1'
    old_env, old_argv = os.environ.copy(), sys.argv[:]
    os.environ.update(env)
    sys.argv = [SHADOW, PATH, '1']
    try:
        g = runpy.run_path(SHADOW, run_name='__shadow_sweep__')
    finally:
        os.environ.clear(); os.environ.update(old_env); sys.argv = old_argv
    return g

# base values, read once, so multipliers have something to multiply
BASE = run_shadow({})
import openpyxl
AS = openpyxl.load_workbook(PATH, data_only=True)['Assumptions']
LBL = {}
for r in range(1, 200):
    b = AS.cell(r, 2).value
    if isinstance(b, str):
        LBL.setdefault(b.strip(), r)
SINGLE = not any(k.startswith('Case   1 = Base') for k in LBL)
VALCOL, YOFF = (4, 1) if SINGLE else (6, 3)
def base_single(lbl):
    v = AS.cell(LBL[lbl], VALCOL).value
    return v if isinstance(v, (int, float)) else 0.0
def base_year(lbl):
    return [AS.cell(LBL[lbl] + YOFF, 4 + k).value or 0.0 for k in range(5)]

WHOLE_KEYS = ['rep_hc', 'ptr_hc', 'pm', 'units', 'ttk_u', 'cmb_u', 'ib_close',
              'hc_rep', 'hc_pm', 'hc_tr', 'hc_desk', 'hc_mkt', 'hc_sm', 'hc_sc',
              'hc_sup', 'hc_esc', 'hc_rnd', 'hc_tech', 'hc_tot']

def faults(S, taxr):
    """Things that cannot be true of any business, whatever the inputs."""
    out = []
    NM = len(S['units'])
    for k in WHOLE_KEYS:
        if k not in S: continue
        for i in range(NM):
            v = S[k][i]
            if not math.isfinite(v):
                out.append(f'{k} is not a number in month {i+1}'); break
            if abs(v - round(v)) > 1e-6:
                out.append(f'{k} is fractional in month {i+1}: {v}'); break
    for k in ('rep_hc', 'ptr_hc', 'ib_close'):
        for i in range(1, NM):
            if S[k][i] < S[k][i-1] - 1e-6:
                out.append(f'{k} falls in month {i+1}: {S[k][i-1]} to {S[k][i]}'); break
    for i in range(NM):
        if S['units'][i] < -1e-6:
            out.append(f'negative units in month {i+1}'); break
        cap = min(S['demand'][i], S['scap'][i], S['bcap'][i])
        if S['units'][i] > cap + 0.5:
            out.append(f'units above the constraint in month {i+1}: '
                       f'{S["units"][i]} vs {cap:.1f}'); break
    for i in range(NM):
        if S['r_tot'][i] < -1e-6:
            out.append(f'negative revenue in month {i+1}'); break
        if S['f44'][i] < -1e-6 or S['f50'][i] < -1e-6:
            out.append(f'negative receivables or payables in month {i+1}'); break
        if S['f22'][i] > 1e-6:
            out.append(f'tax is a credit in month {i+1}'); break
        if S['f21'][i] > 0 and -S['f22'][i] > S['f21'][i]*taxr + 1.0:
            out.append(f'tax above the statutory rate in month {i+1}'); break
    # identities that must hold at every point in input space
    for i in range(NM):
        if abs(S['ib_close'][i] - sum(S['units'][:i+1])) > 0.02:
            out.append(f'installed base is not cumulative units in month {i+1}'); break
        if abs(S['f54'][i] - sum(S['f23'][:i+1])) > 0.02:
            out.append(f'retained earnings is not cumulative net income in month {i+1}'); break
        if abs(S['f40'][i] - (S['f39'][i] + S['f38'][i])) > 0.02:
            out.append(f'closing cash does not reconcile in month {i+1}'); break
        if abs(S['ttk_u'][i] + S['cmb_u'][i] - S['units'][i]) > 1e-6:
            out.append(f'product split does not add to units sold in month {i+1}'); break
        if S['r_tot'][i] > 0 and S['units'][i] > 0:
            rpu = S['r_tot'][i]/S['units'][i]
            if not (500 <= rpu <= 200000):
                out.append(f'revenue per unit is {rpu:,.0f} in month {i+1}'); break
    return out

def plan_outcome(S):
    lo = min(S['f40'])
    return {'cash_low': lo, 'insolvent': lo < -0.02,
            'units_total': sum(S['units']),
            'ebitda_2030': sum(S['f16'][48:60])}

# ---- guard: the unperturbed draw must reproduce the workbook ---------------
# Without this the sweep can run thousands of draws off a broken baseline and
# report a confident pass, which is the exact failure this whole phase exists
# to stop.
import openpyxl as _ox
_chk = _ox.load_workbook(PATH, data_only=True)['Financial Statements']
_wb_cash = [_chk.cell(40, 5 + i).value or 0.0 for i in range(60)]
_sh_cash = BASE['S']['f40']
_worst = max(abs(a - b) for a, b in zip(_wb_cash, _sh_cash))
if _worst > 0.02:
    sys.exit(f'baseline check failed: the shadow disagrees with the workbook by '
             f'{_worst:,.2f} on closing cash before any input is perturbed. '
             f'Nothing below would mean anything, so stopping.')
print(f'baseline check: shadow matches the workbook to {_worst:.4f} on closing cash')

# ---- self test: prove the fault detector detects ---------------------------
# A checker that never fires is indistinguishable from a checker that works.
# Take the good run, break one number at a time in each way the detector is
# meant to catch, and require every break to be caught.
def selftest(S0, taxr):
    import copy
    cases = [
        ('fractional person',      lambda S: S['rep_hc'].__setitem__(20, S['rep_hc'][20] + 0.5)),
        ('fractional unit',        lambda S: S['units'].__setitem__(20, S['units'][20] + 0.4)),
        ('headcount goes backwards', lambda S: S['ptr_hc'].__setitem__(30, -1.0)),
        ('units above the constraint', lambda S: S['units'].__setitem__(30, S['units'][30] + 500)),
        ('negative revenue',       lambda S: S['r_tot'].__setitem__(30, -1.0)),
        ('negative receivables',   lambda S: S['f44'].__setitem__(30, -1.0)),
        ('tax as a credit',        lambda S: S['f22'].__setitem__(30, 1.0)),
        ('installed base breaks',  lambda S: S['ib_close'].__setitem__(30, S['ib_close'][30] + 7)),
        ('retained earnings breaks', lambda S: S['f54'].__setitem__(30, S['f54'][30] + 100)),
        ('cash does not reconcile', lambda S: S['f40'].__setitem__(30, S['f40'][30] + 100)),
        ('product split breaks',   lambda S: S['ttk_u'].__setitem__(30, S['ttk_u'][30] + 1)),
        ('a number is not a number', lambda S: S['units'].__setitem__(30, float('nan'))),
    ]
    missed = []
    for name, breakit in cases:
        S = copy.deepcopy(S0)
        breakit(S)
        if not faults(S, taxr):
            missed.append(name)
    clean = faults(copy.deepcopy(S0), taxr)
    return missed, clean

_missed, _clean = selftest(BASE['S'], base_single('Corporate income tax rate'))
if _clean:
    sys.exit(f'self test failed: the detector fires on the good model: {_clean}')
if _missed:
    sys.exit(f'self test failed: these breakages went undetected: {_missed}')
print(f'self test: 12 deliberate breakages, all 12 detected; no false alarm on the good model')

rng = random.Random(SEED)
taxr_base = base_single('Corporate income tax rate')
fault_draws, insolvent, zero_vol = [], 0, 0
print(f'sweeping {RAW}')
print(f'{DRAWS} draws, seed {SEED}, {len(SINGLE_MULT)+len(SINGLE_ABS)+len(YEAR_MULT)+len(YEAR_ABS)} inputs perturbed\n')

for d in range(DRAWS):
    ov = {'single': {}, 'year': {}}
    for lbl, lo, hi in SINGLE_MULT:
        if lbl in LBL:
            ov['single'][lbl] = base_single(lbl) * rng.uniform(lo, hi)
    for lbl, lo, hi in SINGLE_ABS:
        if lbl in LBL:
            ov['single'][lbl] = rng.uniform(lo, hi)
    # keep the relationships the workbook itself enforces between assumptions
    if 'TTK share of units' in ov['single'] and 'Combi+ share of units' in LBL:
        ov['single']['Combi+ share of units'] = 1.0 - ov['single']['TTK share of units']
    if {'Turbineketel list price', 'Outdoor unit, Combi+ only'} <= set(ov['single']):
        ov['single']['Combi+ price (ketel plus outdoor unit)'] = (
            ov['single']['Turbineketel list price'] + ov['single']['Outdoor unit, Combi+ only'])
    for lbl, lo, hi in YEAR_MULT:
        if lbl in LBL:
            b = base_year(lbl)
            ov['year'][lbl] = [(v or 0.0) * rng.uniform(lo, hi) for v in b]
    for lbl, lo, hi in YEAR_ABS:
        if lbl in LBL:
            ov['year'][lbl] = [rng.uniform(lo, hi) for _ in range(5)]
    g = run_shadow(ov)
    S = g['S']
    taxr = ov['single'].get('Corporate income tax rate', taxr_base)
    f = faults(S, taxr)
    o = plan_outcome(S)
    if f:
        fault_draws.append((d, f, ov))
        if len(fault_draws) <= 5:
            print(f'  MODEL FAULT  draw {d}: ' + '; '.join(f[:3]))
    if o['insolvent']:
        insolvent += 1
    if o['units_total'] < 1:
        zero_vol += 1
    if (d+1) % 250 == 0:
        print(f'  {d+1} draws, {len(fault_draws)} model faults, '
              f'{insolvent} draws where the plan runs out of cash')

print(f'\n--- RESULT over {DRAWS} draws ---')
print(f'  model faults          {len(fault_draws)}')
print(f'  plan runs out of cash {insolvent}  ({insolvent/DRAWS:.0%} of draws, not a bug)')
print(f'  draws selling nothing {zero_vol}')
if fault_draws:
    d, f, ov = fault_draws[0]
    print('\n  first faulting draw, inputs:')
    for k, v in sorted(ov['single'].items()):
        print(f'    {k:<52} {v:,.4f}')
    for k, v in sorted(ov['year'].items()):
        print(f'    {k:<52} ' + ', '.join(f'{x:,.2f}' for x in v))
    print('  faults: ' + '; '.join(f))
print('\n' + ('SWEEP PASSED' if not fault_draws else f'SWEEP FAILED: {len(fault_draws)} draws'))
sys.exit(1 if fault_draws else 0)
