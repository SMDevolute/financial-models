"""
audit_v2.py -- full correctness audit of the Tarnoc v2 model.

    python3 scripts/audit_v2.py models/Tarnoc_v2_2026-09-07.xlsx

Four phases, run against a real LibreOffice recalculation, not against openpyxl's
view of the formulas:

  1. Recalculate both cases and look for formula
     errors and a balance sheet that does not tie.
  2. Compare the workbook against an independent Python reimplementation of the
     whole model, cell by cell. Any disagreement is a bug in one of them.
  3. Check the accounting identities and sign conventions that a shadow model
     cannot catch, because a shadow can share the same wrong intent.
  4. Check the structure: no stray hardcodes, every cross-sheet reference lands
     on the row it claims, the live column reads its own row, no orphans.

Exits non-zero if anything fails.
"""
import os, subprocess, sys, tempfile, shutil
import openpyxl

SOFFICE = '/Applications/LibreOffice.app/Contents/MacOS/soffice'
HERE = os.path.dirname(os.path.abspath(__file__))
ERRS = ('#REF!', '#VALUE!', '#DIV/0!', '#NAME?', '#N/A', '#NULL!', '#NUM!', 'Err:')
CASE_CELL, CHECK_ROWS = 'E5', (58, 59)


def recalc(path, outdir):
    os.makedirs(outdir, exist_ok=True)
    subprocess.run([SOFFICE, '--headless', '--norestore', '--convert-to', 'xlsx',
                    '--outdir', outdir, path], check=True, capture_output=True)
    return os.path.join(outdir, os.path.basename(path))


def variant(src, tmp, case):
    wb = openpyxl.load_workbook(src)
    wb['Assumptions'][CASE_CELL] = case
    p = os.path.join(tmp, f'v_{case}.xlsx')
    wb.save(p)
    return recalc(p, os.path.join(tmp, f'o{case}'))


def phase1(recalced):
    print('PHASE 1  formula errors and the balance sheet check')
    ok = True
    for case, path in sorted(recalced.items()):
        v = openpyxl.load_workbook(path, data_only=True)
        errs = [f'{ws.title}!{c.coordinate}={c.value}' for ws in v for row in ws.iter_rows()
                for c in row if isinstance(c.value, str) and any(e in c.value for e in ERRS)]
        fs = v['Financial Statements']
        chk = [fs.cell(r, c).value for r in CHECK_ROWS for c in range(2, fs.max_column + 1)]
        worst = max((abs(x) for x in chk if isinstance(x, (int, float))), default=0.0)
        good = not errs and worst < 0.01
        ok &= good
        print(f'  {"pass" if good else "FAIL"}  case {case}: '
              f'{len(errs)} errors, worst balance check {worst:.4f}')
        for e in errs[:5]:
            print('        ', e)
    return ok


def run(script, args, keep=('MISMATCH', 'FAIL', 'agree', 'ALL ', 'FAILURES')):
    r = subprocess.run([sys.executable, os.path.join(HERE, script)] + args,
                       capture_output=True, text=True)
    out = [l for l in r.stdout.splitlines() if any(k in l for k in keep)]
    for l in out:
        print('  ' + l.strip())
    if r.returncode != 0 or not out:
        print(f'  FAIL  {script} crashed or produced no result')
        print('  ' + (r.stderr.strip().splitlines() or ['no stderr'])[-1])
        return False
    return 'FAIL' not in r.stdout and 'MISMATCH' not in r.stdout


def main():
    src = os.path.abspath(sys.argv[1])
    tmp = tempfile.mkdtemp(prefix='audit_v2_')
    try:
        ws = openpyxl.load_workbook(src)['Assumptions']
        has_switch = any(isinstance(ws.cell(r, 2).value, str) and ws.cell(r, 2).value.startswith('Case   1 = Base')
                         for r in range(1, 12))
        if has_switch:
            recalced = {c: variant(src, tmp, c) for c in (1, 2)}
        else:                      # single-case workbook: nothing to switch, recalculate as is
            recalced = {0: recalc(src, os.path.join(tmp, 'o0'))}
        ok = phase1(recalced)
        print('\nPHASE 2  independent shadow model, cell by cell')
        for case in sorted(recalced):
            print(f'  case {case}:' if case else '  single case:')
            ok &= run('audit_v2_shadow.py', [recalced[case], str(case)])
        print('\nPHASE 3  accounting identities, signs and operating logic')
        for case in sorted(recalced, reverse=True):
            ok &= run('audit_v2_identities.py', [recalced[case]])
        print('\nPHASE 4  structure')
        ok &= run('audit_v2_structure.py', [src])
        print('\n' + ('AUDIT PASSED' if ok else 'AUDIT FAILED'))
        sys.exit(0 if ok else 1)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    main()
