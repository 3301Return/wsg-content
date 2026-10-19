#!/usr/bin/env python3
"""Build scripts/images/models/torvik-dcf.xlsx for the WSG article
"Financial Modeling Test: What to Expect and How to Practice" (October 5, 2026).

The section 5 worked example, a two-hour DCF modeling test on Torvik Flow Systems (a fictional
mid-cap industrial), rebuilt with live formulas on eight tabs:

  Cover         company, valuation date, the scenario switch cell (1 Bear, 2 Base, 3 Bull), a live
                outputs block, the scenario summary (Table 13, values from a data table on the
                switch), the color key and the tab list
  Inputs        historical income statement and ratios (Table 1), segment build with the check
                cell (Table 2), the assumptions block with Bear / Base / Bull rows and a live row
                per driver that reads the switch through CHOOSE (Table 3)
  Schedules     working capital by days (Table 5), PP&E roll-forward (Table 6)
  Cost of debt  tranches, weights, weighted pre-tax and after-tax cost (Table 7)
  Beta          peer betas unlevered, median, relevered for Torvik (Table 8)
  WACC          CAPM cost of equity, after-tax cost of debt, market value weights (Table 9)
  DCF           operating build (Table 4), unlevered free cash flow and present values with the
                mid-year convention (Table 10), terminal value by exit multiple with the Gordon
                growth cross-check and the bridge to the share price (Table 11), plus a column
                carrying each row's 2026E formula as text for the formula close-up
  Sensitivity   implied share price, WACC down and exit multiple across, axes built off step
                cells, body values computed here (Excel evaluates the data table live; LibreOffice
                does not, so the values are written) (Table 12)

Column A is a narrow margin, labels sit in column B, years run across from column C, each block
has its own year header. Blue hardcodes on pale yellow, black formulas, green cross-sheet links.

Every number comes from scripts/images/models/numbers_financial-modeling-test-what-to-expect.py,
whose printed tables are the article's tables. After saving, check_against_article() recalculates
the workbook with LibreOffice and compares every table cell at the article's display precision,
then flips the switch to Bear and Bull on a temp copy and checks the Cover outputs against
Table 13.

Run from the repo root:  python3 scripts/images/models/build_torvik_dcf.py
Idempotent: rewrites the workbook every time.
"""
import contextlib
import importlib.util
import io
import shutil
import sys
import tempfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import (FILL_SUBTLE, XL_FONT, XL_SIZE, header_bar, new_workbook, put,  # noqa: E402
                     recalc_values, set_widths)

OUT = ROOT / "scripts" / "images" / "models" / "torvik-dcf.xlsx"
NUMBERS = ROOT / "scripts" / "images" / "models" / "numbers_financial-modeling-test-what-to-expect.py"

# ---------------------------------------------------------------- number formats (zeros print as 0.0, never a dash)
F_NUM = '#,##0.0;(#,##0.0);0.0'
F_PCT = '0.0%;(0.0%);0.0%'
F_PCT2 = '0.00%;(0.00%);0.00%'
F_PCT0 = '0%'
F_USD = '"$"#,##0.00;("$"#,##0.00);"$"0.00'
F_MULT = '0.0"x"'
F_BETA = '0.000'
F_DE2 = '0.00'
F_DE3 = '0.000'
F_DF = '0.0000'
F_DAYS1 = '0.0'
F_DAYS0 = '0'
F_FRAC = '0.00'
F_DATE = 'mmmm d, yyyy'
F_SWITCH = '0'
GRAY = "52514E"

HIST = ["2023A", "2024A", "2025A"]
PROJ = ["2026E", "2027E", "2028E", "2029E", "2030E"]
ALL = HIST + PROJ
HIST_COLS = ["C", "D", "E"]            # Inputs historical blocks
PROJ_COLS = ["C", "D", "E", "F", "G"]  # Inputs assumptions block
ALL_COLS = list("CDEFGHIJ")            # DCF: 2023A .. 2030E
WC_COLS = list("CDEFGHIJK")            # Schedules: 2022A .. 2030E
DCF_PROJ = list("FGHIJ")
TO_INPUTS = dict(zip(DCF_PROJ, PROJ_COLS))          # DCF projected column -> Inputs assumptions column
TO_SCHED = dict(zip(ALL_COLS, WC_COLS[1:]))         # DCF column -> Schedules column (2022A sits in C)
FCOL_DCF = "L"                                      # formula text column on the DCF tab
FCOL_INP = "I"                                      # formula text column on the Inputs tab

SEGMENTS = ["Pumps", "Valves and Controls", "Aftermarket Parts and Service"]
SEG_KEYS = ["pumps", "vc", "am"]
SCENARIOS = ["Bear", "Base", "Bull"]


# ---------------------------------------------------------------- the article's numbers
def load_numbers():
    """Import the numbers script (it prints the article's tables on import; capture them)."""
    spec = importlib.util.spec_from_file_location("torvik_numbers", NUMBERS)
    mod = importlib.util.module_from_spec(spec)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        spec.loader.exec_module(mod)
    return mod, buf.getvalue()


def parse_tables(text):
    """{table number: {"title": ..., "header": [...], "rows": {label: [cells...]}}} from the printout."""
    tables, cur = {}, None
    for line in text.split("\n"):
        if line.startswith("### Table "):
            num = int(line.split()[2].rstrip("."))
            cur = tables[num] = {"title": line[4:], "header": None, "rows": {}}
        elif cur is not None and line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if cells[0].startswith("---"):
                continue
            if cur["header"] is None:
                cur["header"] = cells
            else:
                cur["rows"][cells[0]] = cells[1:]
        elif cur is not None and line.strip() == "" and cur["header"] is not None and cur["rows"]:
            cur = None
    return tables


N, PRINTOUT = load_numbers()
TABLES = parse_tables(PRINTOUT)


# ---------------------------------------------------------------- row maps
INP = dict(
    hdr1=4, rev=5, cogs=6, gp=7, sga=8, ebit=9, intexp=10, ebt=11, tax=12, ni=13, shares=14, eps=15,
    growth=16, gm=17, sgapct=18, ebitm=19, etr=20, da=21, ebitda=22, ebitdam=23, capex=24,
    hdr2=26, s_pumps=27, s_vc=28, s_am=29, s_tot=30, s_chk=31, g_pumps=32, g_vc=33, g_am=34,
    m_pumps=35, m_vc=36, m_am=37,
    hdr3=39, switch=40,
)
_r = 41
for _k in SEG_KEYS + ["gm", "sga"]:
    for _sc in ["bear", "base", "bull", "live"]:
        INP[f"a_{_k}_{_sc}"] = _r
        _r += 1
for _k in ["dapct", "capexpct", "dso", "dio", "dpo", "accr", "defrev", "taxrate"]:
    INP[f"a_{_k}"] = _r
    _r += 1
INP_LAST = _r - 1   # 68

SCH = dict(hdr_wc=4, rev=5, cogs=6, ar=7, inv=8, ap=9, accr=10, defrev=11, nwc=12, dnwc=13, dso=14, dio=15,
           dpo=16, nwcpct=17, hdr_ppe=19, beg=20, capex=21, da=22, end=23, capexpct=24, dapct=25)
COD = dict(hdr=4, colhdr=5, tlb=6, notes=7, total=8, taxrate=9, aftertax=10, note=11)
BET = dict(hdr=4, colhdr=5, p0=6, p1=7, p2=8, p3=9, p4=10, median=11, mean=12, torvik=13, relever=14)
WAC = dict(hdr=4, rf=5, erp=6, beta=7, ke=8, kd=9, kd_at=10, price=11, shares=12, mcap=13, debt=14, we=15,
           wd=16, wacc=17)
DCF = dict(
    hdr_op=4, pumps=5, vc=6, am=7, rev=8, growth=9, cogs=10, gp=11, gm=12, sga=13, ebit=14, ebitm=15, da=16,
    ebitda=17, ebitdam=18, capex=19,
    hdr_fcf=21, ebit2=22, tax=23, nopat=24, da2=25, capex2=26, nwc=27, ufcf=28, frac=29, period=30, df=31, pv=32,
    hdr_tv=34, sumpv=35, ebitda30=36, mult=37, tv=38, tvdf=39, pvtv=40, ev=41, tvshare=42, debt=43, cash=44,
    nci=45, equity=46, shares=47, px=48, price=49, upside=50, px_eoy=51, impg=52, g=53, tvg=54, impmult=55,
    pxg=56, evltm=57,
)
SEN = dict(hdr=4, note=5, wstep=6, mstep=7, corner=9, first=10)
COV = dict(title=2, sub=3, hdr_setup=5, valdate=6, fye=7, units=8, price=9, shares=10, hdr_switch=12, switch=13,
           note=14, hdr_out=16, o_rev=17, o_ebitda=18, o_wacc=19, o_ev=20, o_px=21, o_upside=22, hdr_sum=24,
           sum_hdr=25, sum_bear=26, sum_base=27, sum_bull=28, hdr_key=30, key_input=31, key_formula=32,
           key_link=33, hdr_tabs=35, tabs=36)

SHEETS = ["Cover", "Inputs", "Schedules", "Cost of debt", "Beta", "WACC", "DCF", "Sensitivity"]


def xref(sheet, cell):
    """A cross-sheet reference, quoted when the sheet name has a space."""
    return f"'{sheet}'!{cell}" if " " in sheet else f"{sheet}!{cell}"


def block_header(ws, row, text, years=None, first_col="C", last_col_idx=None, extra=None):
    """A navy section bar with the block title in B and the year labels (white, bold) across."""
    from openpyxl.styles import Alignment, Font
    from openpyxl.utils import column_index_from_string
    last = last_col_idx or (column_index_from_string(first_col) + (len(years) if years else 1) - 1)
    if extra:
        last = max([last] + [column_index_from_string(c) for c in extra])
    header_bar(ws, row, 2, last, text)
    if years:
        start = column_index_from_string(first_col)
        for i, y in enumerate(years):
            c = ws.cell(row=row, column=start + i, value=y)
            c.font = Font(name=XL_FONT, size=XL_SIZE, bold=True, color="FFFFFF")
            c.alignment = Alignment(horizontal="right")
    if extra:
        for col, text2 in extra.items():
            c = ws[f"{col}{row}"]
            c.value = text2
            c.font = Font(name=XL_FONT, size=XL_SIZE, bold=True, color="FFFFFF")


def ftext(ws, ref, text):
    """A formula written as plain text (gray italic) for the formula close-ups."""
    c = put(ws, ref, text, italic=True, color=GRAY, align="left", indent=1)
    c.data_type = "s"
    return c


def title(ws, text, units="$ millions, except per share data. Fiscal year ends December 31."):
    put(ws, "B1", text, bold=True, size=12)
    put(ws, "B2", units, italic=True, color=GRAY)


# ---------------------------------------------------------------- sheets
def write_cover(ws):
    from openpyxl.styles import Alignment
    set_widths(ws, {"A": 2, "B": 46, "C": 13, "D": 13, "E": 13, "F": 13, "G": 13, "H": 13, "I": 13})
    put(ws, f"B{COV['title']}", "Torvik Flow Systems", bold=True, size=14)
    put(ws, f"B{COV['sub']}", "Mid-cap industrial: pumps, valves and controls, aftermarket parts and service. "
        "A fictional company built for a two-hour DCF modeling test.", italic=True, color=GRAY)
    block_header(ws, COV["hdr_setup"], "VALUATION SETUP", last_col_idx=9)
    put(ws, f"B{COV['valdate']}", "Valuation date")
    put(ws, f"C{COV['valdate']}", date(2025, 12, 31), kind="input", fmt=F_DATE, align="right")
    put(ws, f"B{COV['fye']}", "Fiscal year end")
    put(ws, f"C{COV['fye']}", "December 31", kind="input", align="right")
    put(ws, f"B{COV['units']}", "Units")
    put(ws, f"C{COV['units']}", "$ millions, except per share data", kind="input", align="right")
    put(ws, f"B{COV['price']}", "Share price on the valuation date ($)")
    put(ws, f"C{COV['price']}", N.PRICE, kind="input", fmt=F_USD)
    put(ws, f"B{COV['shares']}", "Diluted shares (millions)")
    put(ws, f"C{COV['shares']}", N.diluted_shares, kind="input", fmt=F_NUM)

    block_header(ws, COV["hdr_switch"], "SCENARIO SWITCH", last_col_idx=9)
    put(ws, f"B{COV['switch']}", "Scenario switch (1 = Bear, 2 = Base, 3 = Bull)", bold=True)
    put(ws, f"C{COV['switch']}", 2, kind="input", fmt=F_SWITCH, bold=True)
    put(ws, f"D{COV['switch']}", f'=CHOOSE(C{COV["switch"]},"Bear","Base","Bull")', kind="formula", bold=True,
        align="left", indent=1)
    put(ws, f"B{COV['note']}", "Every growth and margin assumption on the Inputs tab reads this cell through a "
        "CHOOSE. Flip it and nothing else changes.", italic=True, color=GRAY)

    block_header(ws, COV["hdr_out"], "OUTPUTS, LIVE FROM THE DCF TAB (CURRENT SCENARIO)", last_col_idx=9)
    put(ws, f"B{COV['o_rev']}", "FY2030E revenue")
    put(ws, f"C{COV['o_rev']}", f"={xref('DCF', 'J' + str(DCF['rev']))}", kind="link", fmt=F_NUM)
    put(ws, f"B{COV['o_ebitda']}", "FY2030E EBITDA")
    put(ws, f"C{COV['o_ebitda']}", f"={xref('DCF', 'J' + str(DCF['ebitda']))}", kind="link", fmt=F_NUM)
    put(ws, f"B{COV['o_wacc']}", "WACC")
    put(ws, f"C{COV['o_wacc']}", f"={xref('WACC', 'C' + str(WAC['wacc']))}", kind="link", fmt=F_PCT2)
    put(ws, f"B{COV['o_ev']}", "Enterprise value")
    put(ws, f"C{COV['o_ev']}", f"={xref('DCF', 'C' + str(DCF['ev']))}", kind="link", fmt=F_NUM)
    put(ws, f"B{COV['o_px']}", "Implied share price ($)", bold=True)
    put(ws, f"C{COV['o_px']}", f"={xref('DCF', 'C' + str(DCF['px']))}", kind="link", fmt=F_USD, bold=True)
    put(ws, f"B{COV['o_upside']}", "Implied upside / (downside) vs the current price")
    put(ws, f"C{COV['o_upside']}", f"={xref('DCF', 'C' + str(DCF['upside']))}", kind="link", fmt=F_PCT)

    block_header(ws, COV["hdr_sum"], "SCENARIO SUMMARY (data table on the switch cell; values shown)",
                 last_col_idx=9)
    heads = ["Scenario", "FY2030E revenue", "FY2030E EBITDA margin", "FY2030E EBITDA", "FY2030E UFCF",
             "Enterprise value", "Implied share price", "vs $38.00"]
    for col, h in zip("BCDEFGHI", heads):
        c = put(ws, f"{col}{COV['sum_hdr']}", h, bold=True, border_bottom=True, align="left" if col == "B" else "right")
        c.alignment = Alignment(horizontal="left" if col == "B" else "right", wrap_text=True, vertical="bottom")
    ws.row_dimensions[COV["sum_hdr"]].height = 28
    for sc, key in zip(SCENARIOS, ["sum_bear", "sum_base", "sum_bull"]):
        m = N.run(sc)
        v = N.value(m)
        row = COV[key]
        put(ws, f"B{row}", sc, bold=(sc == "Base"))
        vals = [(m["revenue"][-1], F_NUM), (m["ebitda"][-1] / m["revenue"][-1], F_PCT), (m["ebitda"][-1], F_NUM),
                (m["ufcf"][-1], F_NUM), (v["ev"], F_NUM), (v["px"], F_USD), (v["px"] / N.PRICE - 1, F_PCT)]
        for col, (val, fmt) in zip("CDEFGHI", vals):
            put(ws, f"{col}{row}", val, kind="formula", fmt=fmt, bold=(sc == "Base"),
                fill=FILL_SUBTLE if sc == "Base" else None)

    block_header(ws, COV["hdr_key"], "COLOR KEY", last_col_idx=9)
    put(ws, f"B{COV['key_input']}", "Blue on pale yellow: typed input (the pack's numbers and the assumptions)",
        kind="input")
    put(ws, f"B{COV['key_formula']}", "Black: formula", kind="formula")
    put(ws, f"B{COV['key_link']}", "Green: link to another tab", kind="link")

    block_header(ws, COV["hdr_tabs"], "TABS, IN BUILD ORDER", last_col_idx=9)
    tabs = [
        ("Inputs", "historical income statement and ratios, segment build, assumptions block (Bear / Base / Bull)"),
        ("Schedules", "working capital by days, PP&E roll-forward"),
        ("Cost of debt", "tranches, weights, weighted pre-tax and after-tax cost"),
        ("Beta", "peer betas unlevered, median, relevered for Torvik"),
        ("WACC", "cost of equity by CAPM, after-tax cost of debt, market value weights"),
        ("DCF", "operating build, unlevered free cash flow, present values, terminal value, bridge to share price"),
        ("Sensitivity", "implied share price, WACC down and exit multiple across"),
    ]
    for i, (name, what) in enumerate(tabs):
        put(ws, f"B{COV['tabs'] + i}", name, bold=True)
        put(ws, f"C{COV['tabs'] + i}", what, color=GRAY)
    ws.sheet_view.showGridLines = False


def write_inputs(ws):
    set_widths(ws, {"A": 2, "B": 54, "C": 11, "D": 11, "E": 11, "F": 11, "G": 11, "H": 2, FCOL_INP: 44})
    title(ws, "Torvik Flow Systems: Inputs")
    R = INP
    # ---- historical income statement and ratios (Table 1)
    block_header(ws, R["hdr1"], "HISTORICAL INCOME STATEMENT AND RATIOS", HIST)
    hist_inputs = dict(rev=N.revenue_h, cogs=N.cogs_h, sga=N.sga_h, intexp=N.interest_h, tax=N.tax_h,
                       da=N.da_h, capex=N.capex_h)
    labels = dict(rev="Revenue", cogs="Cost of sales", gp="Gross profit", sga="SG&A", ebit="EBIT",
                  intexp="Interest expense", ebt="Pretax income", tax="Taxes", ni="Net income",
                  shares="Diluted shares (millions)", eps="Diluted EPS ($)", growth="Revenue growth",
                  gm="Gross margin", sgapct="SG&A as a percent of revenue", ebitm="EBIT margin",
                  etr="Effective tax rate", da="D&A (from the cash flow statement)", ebitda="EBITDA",
                  ebitdam="EBITDA margin", capex="Capex (from the cash flow statement)")
    totals = {"gp", "ebit", "ebt", "ni", "ebitda"}
    for key, text in labels.items():
        put(ws, f"B{R[key]}", text, bold=key in totals)
    for i, c in enumerate(HIST_COLS):
        p = HIST_COLS[i - 1] if i else None
        for key, vals in hist_inputs.items():
            put(ws, f"{c}{R[key]}", vals[i], kind="input", fmt=F_NUM)
        put(ws, f"{c}{R['shares']}", N.diluted_shares, kind="input", fmt=F_NUM)
        put(ws, f"{c}{R['gp']}", f"=SUM({c}{R['rev']}:{c}{R['cogs']})", kind="total", fmt=F_NUM)
        put(ws, f"{c}{R['ebit']}", f"=SUM({c}{R['gp']}:{c}{R['sga']})", kind="total", fmt=F_NUM)
        put(ws, f"{c}{R['ebt']}", f"=SUM({c}{R['ebit']}:{c}{R['intexp']})", kind="total", fmt=F_NUM)
        put(ws, f"{c}{R['ni']}", f"=SUM({c}{R['ebt']}:{c}{R['tax']})", kind="total", fmt=F_NUM)
        put(ws, f"{c}{R['eps']}", f"={c}{R['ni']}/{c}{R['shares']}", kind="formula", fmt=F_USD)
        if p:
            put(ws, f"{c}{R['growth']}", f"={c}{R['rev']}/{p}{R['rev']}-1", kind="formula", fmt=F_PCT)
        put(ws, f"{c}{R['gm']}", f"={c}{R['gp']}/{c}{R['rev']}", kind="formula", fmt=F_PCT)
        put(ws, f"{c}{R['sgapct']}", f"=-{c}{R['sga']}/{c}{R['rev']}", kind="formula", fmt=F_PCT)
        put(ws, f"{c}{R['ebitm']}", f"={c}{R['ebit']}/{c}{R['rev']}", kind="formula", fmt=F_PCT)
        put(ws, f"{c}{R['etr']}", f"=-{c}{R['tax']}/{c}{R['ebt']}", kind="formula", fmt=F_PCT)
        put(ws, f"{c}{R['ebitda']}", f"={c}{R['ebit']}+{c}{R['da']}", kind="total", fmt=F_NUM)
        put(ws, f"{c}{R['ebitdam']}", f"={c}{R['ebitda']}/{c}{R['rev']}", kind="formula", fmt=F_PCT)

    # ---- segment build (Table 2)
    block_header(ws, R["hdr2"], "SEGMENT REVENUE BUILD", HIST)
    for seg, key in zip(SEGMENTS, SEG_KEYS):
        put(ws, f"B{R['s_' + key]}", seg)
        put(ws, f"B{R['g_' + key]}", f"{seg} growth")
        put(ws, f"B{R['m_' + key]}", f"{seg} mix")
    put(ws, f"B{R['s_tot']}", "Total revenue", bold=True)
    put(ws, f"B{R['s_chk']}", "Check: segment total minus reported revenue (should read 0.0)", italic=True)
    for i, c in enumerate(HIST_COLS):
        p = HIST_COLS[i - 1] if i else None
        for seg, key in zip(SEGMENTS, SEG_KEYS):
            put(ws, f"{c}{R['s_' + key]}", N.seg_hist[seg][i], kind="input", fmt=F_NUM)
            if p:
                put(ws, f"{c}{R['g_' + key]}", f"={c}{R['s_' + key]}/{p}{R['s_' + key]}-1", kind="formula", fmt=F_PCT)
            put(ws, f"{c}{R['m_' + key]}", f"={c}{R['s_' + key]}/{c}${R['s_tot']}", kind="formula", fmt=F_PCT)
        put(ws, f"{c}{R['s_tot']}", f"=SUM({c}{R['s_pumps']}:{c}{R['s_am']})", kind="total", fmt=F_NUM)
        put(ws, f"{c}{R['s_chk']}", f"={c}{R['s_tot']}-{c}{R['rev']}", kind="formula", fmt=F_NUM, italic=True,
            fill=FILL_SUBTLE)

    # ---- assumptions block (Table 3) with the live rows
    block_header(ws, R["hdr3"], "ASSUMPTIONS: BEAR, BASE, BULL AND LIVE ROWS", PROJ,
                 extra={FCOL_INP: "Formula in the 2026E column"})
    put(ws, f"B{R['switch']}", "Scenario switch (from Cover: 1 = Bear, 2 = Base, 3 = Bull)", bold=True)
    put(ws, f"C{R['switch']}", f"={xref('Cover', 'C' + str(COV['switch']))}", kind="link", fmt=F_SWITCH, bold=True)
    put(ws, f"D{R['switch']}", f"={xref('Cover', 'D' + str(COV['switch']))}", kind="link", bold=True, align="left", indent=1)
    ftext(ws, f"{FCOL_INP}{R['switch']}", f"=Cover!C{COV['switch']}   (one cell, read by every live row)")
    drivers = [("pumps", "Pumps growth", "Pumps"), ("vc", "Valves and Controls growth", "Valves and Controls"),
               ("am", "Aftermarket Parts and Service growth", "Aftermarket Parts and Service"),
               ("gm", "Gross margin", "gm"), ("sga", "SG&A as a percent of revenue", "sga")]
    for key, text, nkey in drivers:
        for sc in SCENARIOS:
            row = R[f"a_{key}_{sc.lower()}"]
            put(ws, f"B{row}", f"{text}, {sc}")
            for c, v in zip(PROJ_COLS, N.SCEN[sc][nkey]):
                put(ws, f"{c}{row}", v, kind="input", fmt=F_PCT)
        row = R[f"a_{key}_live"]
        put(ws, f"B{row}", f"{text}, live", bold=True)
        for c in PROJ_COLS:
            bear, base, bull = (R[f"a_{key}_{s}"] for s in ("bear", "base", "bull"))
            put(ws, f"{c}{row}", f"=CHOOSE($C${R['switch']},{c}{bear},{c}{base},{c}{bull})", kind="formula",
                fmt=F_PCT, bold=True, fill=FILL_SUBTLE)
        bear, base, bull = (R[f"a_{key}_{s}"] for s in ("bear", "base", "bull"))
        ftext(ws, f"{FCOL_INP}{row}", f"=CHOOSE($C${R['switch']},C{bear},C{base},C{bull})")
    fixed = [("dapct", "D&A as a percent of revenue (all cases)", N.DA_PCT, F_PCT),
             ("capexpct", "Capex as a percent of revenue (all cases)", N.CAPEX_PCT, F_PCT),
             ("dso", "Receivable days, DSO (all cases)", N.DSO, F_DAYS0),
             ("dio", "Inventory days, DIO (all cases)", N.DIO, F_DAYS0),
             ("dpo", "Payable days, DPO (all cases)", N.DPO, F_DAYS0),
             ("accr", "Accrued liabilities as a percent of revenue", N.ACCRUED_PCT, F_PCT),
             ("defrev", "Deferred revenue as a percent of revenue", N.DEFREV_PCT, F_PCT),
             ("taxrate", "Tax rate on EBIT (all cases)", N.TAX_RATE, F_PCT)]
    for key, text, v, fmt in fixed:
        row = R[f"a_{key}"]
        put(ws, f"B{row}", text)
        for c in PROJ_COLS:
            put(ws, f"{c}{row}", v, kind="input", fmt=fmt)
    ws.sheet_view.showGridLines = False


def write_schedules(ws):
    set_widths(ws, {"A": 2, "B": 44, **{c: 10 for c in WC_COLS}})
    title(ws, "Torvik Flow Systems: Schedules")
    R = SCH
    years9 = ["2022A"] + ALL
    block_header(ws, R["hdr_wc"], "WORKING CAPITAL BY DAYS", years9)
    put(ws, f"B{R['rev']}", "Revenue (from the DCF tab)", italic=True, color=GRAY)
    put(ws, f"B{R['cogs']}", "Cost of sales (from the DCF tab)", italic=True, color=GRAY)
    labels = dict(ar="Accounts receivable", inv="Inventory", ap="Accounts payable", accr="Accrued liabilities",
                  defrev="Deferred revenue", nwc="Net working capital", dnwc="(Increase) / decrease in NWC",
                  dso="DSO (days)", dio="DIO (days)", dpo="DPO (days)", nwcpct="NWC as a percent of revenue")
    for key, text in labels.items():
        put(ws, f"B{R[key]}", text, bold=key in ("nwc", "dnwc"))
    hist = N.wc_hist
    for i, c in enumerate(WC_COLS):
        yr_i = i - 1                      # index into ALL (2023A = 0); 2022A -> -1
        dcf_c = ALL_COLS[yr_i] if yr_i >= 0 else None
        inp_c = TO_INPUTS.get(dcf_c)      # Inputs assumptions column for projected years
        if dcf_c:
            put(ws, f"{c}{R['rev']}", f"={xref('DCF', dcf_c + str(DCF['rev']))}", kind="link", fmt=F_NUM, italic=True)
            put(ws, f"{c}{R['cogs']}", f"={xref('DCF', dcf_c + str(DCF['cogs']))}", kind="link", fmt=F_NUM, italic=True)
        if yr_i < 3:   # 2022A .. 2025A balances typed from the pack
            put(ws, f"{c}{R['ar']}", hist["Accounts receivable"][i], kind="input", fmt=F_NUM)
            put(ws, f"{c}{R['inv']}", hist["Inventory"][i], kind="input", fmt=F_NUM)
            put(ws, f"{c}{R['ap']}", hist["Accounts payable"][i], kind="input", fmt=F_NUM)
            put(ws, f"{c}{R['accr']}", hist["Accrued liabilities"][i], kind="input", fmt=F_NUM)
            put(ws, f"{c}{R['defrev']}", hist["Deferred revenue"][i], kind="input", fmt=F_NUM)
            if dcf_c:
                put(ws, f"{c}{R['dso']}", f"={c}{R['ar']}/{c}{R['rev']}*365", kind="formula", fmt=F_DAYS1)
                put(ws, f"{c}{R['dio']}", f"={c}{R['inv']}/-{c}{R['cogs']}*365", kind="formula", fmt=F_DAYS1)
                put(ws, f"{c}{R['dpo']}", f"={c}{R['ap']}/-{c}{R['cogs']}*365", kind="formula", fmt=F_DAYS1)
        else:          # projected: days and percentages from the Inputs tab, reversed
            put(ws, f"{c}{R['dso']}", f"={xref('Inputs', inp_c + str(INP['a_dso']))}", kind="link", fmt=F_DAYS1)
            put(ws, f"{c}{R['dio']}", f"={xref('Inputs', inp_c + str(INP['a_dio']))}", kind="link", fmt=F_DAYS1)
            put(ws, f"{c}{R['dpo']}", f"={xref('Inputs', inp_c + str(INP['a_dpo']))}", kind="link", fmt=F_DAYS1)
            put(ws, f"{c}{R['ar']}", f"={c}{R['rev']}*{c}{R['dso']}/365", kind="formula", fmt=F_NUM)
            put(ws, f"{c}{R['inv']}", f"=-{c}{R['cogs']}*{c}{R['dio']}/365", kind="formula", fmt=F_NUM)
            put(ws, f"{c}{R['ap']}", f"=-{c}{R['cogs']}*{c}{R['dpo']}/365", kind="formula", fmt=F_NUM)
            put(ws, f"{c}{R['accr']}", f"={c}{R['rev']}*{xref('Inputs', inp_c + str(INP['a_accr']))}",
                kind="formula", fmt=F_NUM)
            put(ws, f"{c}{R['defrev']}", f"={c}{R['rev']}*{xref('Inputs', inp_c + str(INP['a_defrev']))}",
                kind="formula", fmt=F_NUM)
        put(ws, f"{c}{R['nwc']}", f"={c}{R['ar']}+{c}{R['inv']}-{c}{R['ap']}-{c}{R['accr']}-{c}{R['defrev']}",
            kind="total", fmt=F_NUM)
        if dcf_c:
            p = WC_COLS[i - 1]
            put(ws, f"{c}{R['dnwc']}", f"={p}{R['nwc']}-{c}{R['nwc']}", kind="formula", fmt=F_NUM, bold=True)
            put(ws, f"{c}{R['nwcpct']}", f"={c}{R['nwc']}/{c}{R['rev']}", kind="formula", fmt=F_PCT)

    # ---- PP&E roll-forward (Table 6); 2022A ending balance typed, the roll starts in 2023A
    block_header(ws, R["hdr_ppe"], "PP&E ROLL-FORWARD", years9)
    put(ws, f"B{R['beg']}", "Beginning net PP&E")
    put(ws, f"B{R['capex']}", "Plus: capex", indent=1)
    put(ws, f"B{R['da']}", "Less: depreciation and amortization", indent=1)
    put(ws, f"B{R['end']}", "Ending net PP&E", bold=True)
    put(ws, f"B{R['capexpct']}", "Capex as a percent of revenue")
    put(ws, f"B{R['dapct']}", "D&A as a percent of revenue")
    put(ws, f"C{R['end']}", N.PPE_2022, kind="input", fmt=F_NUM, bold=True)
    for i, c in enumerate(WC_COLS[1:], start=1):
        p = WC_COLS[i - 1]
        dcf_c = ALL_COLS[i - 1]
        put(ws, f"{c}{R['beg']}", f"={p}{R['end']}", kind="formula", fmt=F_NUM)
        put(ws, f"{c}{R['capex']}", f"={xref('DCF', dcf_c + str(DCF['capex']))}", kind="link", fmt=F_NUM)
        put(ws, f"{c}{R['da']}", f"=-{xref('DCF', dcf_c + str(DCF['da']))}", kind="link", fmt=F_NUM)
        put(ws, f"{c}{R['end']}", f"=SUM({c}{R['beg']}:{c}{R['da']})", kind="total", fmt=F_NUM)
        put(ws, f"{c}{R['capexpct']}", f"={c}{R['capex']}/{c}{R['rev']}", kind="formula", fmt=F_PCT)
        put(ws, f"{c}{R['dapct']}", f"=-{c}{R['da']}/{c}{R['rev']}", kind="formula", fmt=F_PCT)
    ws.sheet_view.showGridLines = False


def write_cost_of_debt(ws):
    set_widths(ws, {"A": 2, "B": 44, "C": 12, "D": 12, "E": 12, "F": 16})
    title(ws, "Torvik Flow Systems: Cost of debt")
    R = COD
    block_header(ws, R["hdr"], "COST OF DEBT", last_col_idx=6)
    for col, text in zip("BCDEF", ["Tranche", "Principal", "Weight", "Rate", "Principal x rate"]):
        put(ws, f"{col}{R['colhdr']}", text, bold=True, border_bottom=True, align="left" if col == "B" else "right")
    for key, (name, principal, rate) in zip(["tlb", "notes"], N.TRANCHES):
        r = R[key]
        put(ws, f"B{r}", name)
        put(ws, f"C{r}", principal, kind="input", fmt=F_NUM)
        put(ws, f"D{r}", f"=C{r}/C${R['total']}", kind="formula", fmt=F_PCT)
        put(ws, f"E{r}", rate, kind="input", fmt=F_PCT2)
        put(ws, f"F{r}", f"=C{r}*E{r}", kind="formula", fmt=F_NUM)
    r = R["total"]
    put(ws, f"B{r}", "Total debt and weighted pre-tax cost", bold=True)
    put(ws, f"C{r}", f"=SUM(C{R['tlb']}:C{R['notes']})", kind="total", fmt=F_NUM)
    put(ws, f"D{r}", f"=SUM(D{R['tlb']}:D{R['notes']})", kind="total", fmt=F_PCT)
    put(ws, f"E{r}", f"=F{r}/C{r}", kind="total", fmt=F_PCT2)
    put(ws, f"F{r}", f"=SUM(F{R['tlb']}:F{R['notes']})", kind="total", fmt=F_NUM)
    put(ws, f"B{R['taxrate']}", "Tax rate (from the Inputs tab)")
    put(ws, f"E{R['taxrate']}", f"={xref('Inputs', 'C' + str(INP['a_taxrate']))}", kind="link", fmt=F_PCT0)
    put(ws, f"B{R['aftertax']}", "After-tax cost of debt at a 25% tax rate", bold=True)
    put(ws, f"E{R['aftertax']}", f"=E{R['total']}*(1-E{R['taxrate']})", kind="formula", fmt=F_PCT2, bold=True)
    put(ws, f"B{R['note']}", "Tie: historical interest expense of 24.0 a year against 400.0 of debt at 6.03% "
        "is 24.1, within rounding.", italic=True, color=GRAY)
    ws.sheet_view.showGridLines = False


def write_beta(ws):
    set_widths(ws, {"A": 2, "B": 40, "C": 12, "D": 11, "E": 12, "F": 9, "G": 9, "H": 14})
    title(ws, "Torvik Flow Systems: Beta", "Peers are fictional. Debt and equity value in $ millions.")
    R = BET
    block_header(ws, R["hdr"], "PEER BETAS, UNLEVERED AND RELEVERED", last_col_idx=8)
    for col, text in zip("BCDEFGH", ["Company", "Levered beta", "Debt", "Equity value", "D / E", "Tax rate",
                                    "Unlevered beta"]):
        put(ws, f"{col}{R['colhdr']}", text, bold=True, border_bottom=True, align="left" if col == "B" else "right")
    for i, (name, beta, d, e, t) in enumerate(N.PEERS):
        r = R[f"p{i}"]
        put(ws, f"B{r}", name)
        put(ws, f"C{r}", beta, kind="input", fmt=F_DE2)
        put(ws, f"D{r}", d, kind="input", fmt=F_NUM)
        put(ws, f"E{r}", e, kind="input", fmt=F_NUM)
        put(ws, f"F{r}", f"=D{r}/E{r}", kind="formula", fmt=F_DE2)
        put(ws, f"G{r}", t, kind="input", fmt=F_PCT0)
        put(ws, f"H{r}", f"=C{r}/(1+(1-G{r})*F{r})", kind="formula", fmt=F_BETA)
    put(ws, f"B{R['median']}", "Median unlevered beta", bold=True)
    put(ws, f"H{R['median']}", f"=MEDIAN(H{R['p0']}:H{R['p4']})", kind="total", fmt=F_BETA)
    put(ws, f"B{R['mean']}", "Mean unlevered beta (for reference)", italic=True)
    put(ws, f"H{R['mean']}", f"=AVERAGE(H{R['p0']}:H{R['p4']})", kind="formula", fmt=F_BETA, italic=True)
    r = R["torvik"]
    put(ws, f"B{r}", "Torvik debt to equity (400.0 / market cap)")
    put(ws, f"D{r}", f"={xref('Cost of debt', 'C' + str(COD['total']))}", kind="link", fmt=F_NUM)
    put(ws, f"E{r}", f"={xref('WACC', 'C' + str(WAC['mcap']))}", kind="link", fmt=F_NUM)
    put(ws, f"F{r}", f"=D{r}/E{r}", kind="formula", fmt=F_DE3)
    put(ws, f"G{r}", f"={xref('Inputs', 'C' + str(INP['a_taxrate']))}", kind="link", fmt=F_PCT0)
    put(ws, f"B{R['relever']}", "Torvik relevered beta", bold=True)
    put(ws, f"H{R['relever']}", f"=H{R['median']}*(1+(1-G{r})*F{r})", kind="total", fmt=F_BETA)
    ws.sheet_view.showGridLines = False


def write_wacc(ws):
    set_widths(ws, {"A": 2, "B": 46, "C": 13})
    title(ws, "Torvik Flow Systems: WACC")
    R = WAC
    block_header(ws, R["hdr"], "WACC", last_col_idx=3)
    rows = [
        ("rf", "Risk-free rate (from the pack)", N.RISK_FREE, "input", F_PCT2),
        ("erp", "Equity risk premium (from the pack)", N.ERP, "input", F_PCT2),
        ("beta", "Relevered beta", f"={xref('Beta', 'H' + str(BET['relever']))}", "link", F_BETA),
        ("ke", "Cost of equity = risk-free + beta times ERP", f"=C{R['rf']}+C{R['beta']}*C{R['erp']}", "formula", F_PCT2),
        ("kd", "Pre-tax cost of debt", f"={xref('Cost of debt', 'E' + str(COD['total']))}", "link", F_PCT2),
        ("kd_at", "After-tax cost of debt", f"={xref('Cost of debt', 'E' + str(COD['aftertax']))}", "link", F_PCT2),
        ("price", "Share price on the valuation date ($)", f"={xref('Cover', 'C' + str(COV['price']))}", "link", F_USD),
        ("shares", "Diluted shares (millions)", f"={xref('Cover', 'C' + str(COV['shares']))}", "link", F_NUM),
        ("mcap", "Equity value (market cap)", f"=C{R['price']}*C{R['shares']}", "formula", F_NUM),
        ("debt", "Total debt", f"={xref('Cost of debt', 'C' + str(COD['total']))}", "link", F_NUM),
        ("we", "Equity weight", f"=C{R['mcap']}/(C{R['mcap']}+C{R['debt']})", "formula", F_PCT),
        ("wd", "Debt weight", f"=C{R['debt']}/(C{R['mcap']}+C{R['debt']})", "formula", F_PCT),
        ("wacc", "WACC", f"=C{R['we']}*C{R['ke']}+C{R['wd']}*C{R['kd_at']}", "total", F_PCT2),
    ]
    for key, text, value, kind, fmt in rows:
        put(ws, f"B{R[key]}", text, bold=(key == "wacc"))
        put(ws, f"C{R[key]}", value, kind=kind, fmt=fmt)
    ws.sheet_view.showGridLines = False


def write_dcf(ws):
    set_widths(ws, {"A": 2, "B": 56, **{c: 10 for c in ALL_COLS}, "K": 2, FCOL_DCF: 44})
    title(ws, "Torvik Flow Systems: DCF")
    R = DCF
    wacc = xref("WACC", f"$C${WAC['wacc']}")
    # ---- operating build (Table 4)
    block_header(ws, R["hdr_op"], "OPERATING BUILD", ALL, extra={FCOL_DCF: "Formula in the 2026E column"})
    labels = dict(pumps="Pumps", vc="Valves and Controls", am="Aftermarket Parts and Service", rev="Total revenue",
                  growth="Revenue growth", cogs="Cost of sales", gp="Gross profit", gm="Gross margin", sga="SG&A",
                  ebit="EBIT", ebitm="EBIT margin", da="D&A", ebitda="EBITDA", ebitdam="EBITDA margin", capex="Capex")
    for key, text in labels.items():
        put(ws, f"B{R[key]}", text, bold=key in ("rev", "gp", "ebit", "ebitda"))
    seg_rows = {"pumps": INP["s_pumps"], "vc": INP["s_vc"], "am": INP["s_am"]}
    for i, c in enumerate(ALL_COLS):
        p = ALL_COLS[i - 1] if i else None
        if c in HIST_COLS:   # historical: green links to the Inputs tab
            for key, srow in seg_rows.items():
                put(ws, f"{c}{R[key]}", f"={xref('Inputs', c + str(srow))}", kind="link", fmt=F_NUM)
            put(ws, f"{c}{R['cogs']}", f"={xref('Inputs', c + str(INP['cogs']))}", kind="link", fmt=F_NUM)
            put(ws, f"{c}{R['sga']}", f"={xref('Inputs', c + str(INP['sga']))}", kind="link", fmt=F_NUM)
            put(ws, f"{c}{R['da']}", f"={xref('Inputs', c + str(INP['da']))}", kind="link", fmt=F_NUM)
            put(ws, f"{c}{R['capex']}", f"={xref('Inputs', c + str(INP['capex']))}", kind="link", fmt=F_NUM)
        else:                # projected: last year times one plus the live growth rate, margins off revenue
            ic = TO_INPUTS[c]
            for key in ("pumps", "vc", "am"):
                put(ws, f"{c}{R[key]}", f"={p}{R[key]}*(1+{xref('Inputs', ic + str(INP['a_' + key + '_live']))})",
                    kind="formula", fmt=F_NUM)
            put(ws, f"{c}{R['cogs']}", f"=-{c}{R['rev']}*(1-{xref('Inputs', ic + str(INP['a_gm_live']))})",
                kind="formula", fmt=F_NUM)
            put(ws, f"{c}{R['sga']}", f"=-{c}{R['rev']}*{xref('Inputs', ic + str(INP['a_sga_live']))}",
                kind="formula", fmt=F_NUM)
            put(ws, f"{c}{R['da']}", f"={c}{R['rev']}*{xref('Inputs', ic + str(INP['a_dapct']))}",
                kind="formula", fmt=F_NUM)
            put(ws, f"{c}{R['capex']}", f"={c}{R['rev']}*{xref('Inputs', ic + str(INP['a_capexpct']))}",
                kind="formula", fmt=F_NUM)
        put(ws, f"{c}{R['rev']}", f"=SUM({c}{R['pumps']}:{c}{R['am']})", kind="total", fmt=F_NUM)
        if p:
            put(ws, f"{c}{R['growth']}", f"={c}{R['rev']}/{p}{R['rev']}-1", kind="formula", fmt=F_PCT)
        put(ws, f"{c}{R['gp']}", f"={c}{R['rev']}+{c}{R['cogs']}", kind="total", fmt=F_NUM)
        put(ws, f"{c}{R['gm']}", f"={c}{R['gp']}/{c}{R['rev']}", kind="formula", fmt=F_PCT)
        put(ws, f"{c}{R['ebit']}", f"={c}{R['gp']}+{c}{R['sga']}", kind="total", fmt=F_NUM)
        put(ws, f"{c}{R['ebitm']}", f"={c}{R['ebit']}/{c}{R['rev']}", kind="formula", fmt=F_PCT)
        put(ws, f"{c}{R['ebitda']}", f"={c}{R['ebit']}+{c}{R['da']}", kind="total", fmt=F_NUM)
        put(ws, f"{c}{R['ebitdam']}", f"={c}{R['ebitda']}/{c}{R['rev']}", kind="formula", fmt=F_PCT)
    for key in ("pumps", "vc", "am", "rev", "growth", "cogs", "gp", "gm", "sga", "ebit", "ebitm", "da", "ebitda",
                "ebitdam", "capex"):
        ftext(ws, f"{FCOL_DCF}{R[key]}", ws[f"F{R[key]}"].value)

    # ---- unlevered free cash flow and present value (Table 10)
    block_header(ws, R["hdr_fcf"], "UNLEVERED FREE CASH FLOW AND PRESENT VALUE", ALL,
                 extra={FCOL_DCF: "Formula in the 2026E column"})
    labels = dict(ebit2="EBIT", tax="Less: taxes on EBIT at 25%", nopat="NOPAT", da2="Plus: D&A", capex2="Less: capex",
                  nwc="Less: increase in NWC", ufcf="Unlevered free cash flow",
                  frac="Year fraction from the valuation date", period="Discount period (mid-year)",
                  df="Discount factor at 9.16% WACC", pv="Present value of UFCF")
    for key, text in labels.items():
        put(ws, f"B{R[key]}", text, bold=key in ("nopat", "ufcf", "pv"),
            indent=1 if key in ("tax", "da2", "capex2", "nwc") else 0)
    for i, c in enumerate(ALL_COLS):
        put(ws, f"{c}{R['ebit2']}", f"={c}{R['ebit']}", kind="formula", fmt=F_NUM)
        rate = xref("Inputs", c + str(INP["etr"])) if c in HIST_COLS else xref("Inputs", TO_INPUTS[c] + str(INP["a_taxrate"]))
        put(ws, f"{c}{R['tax']}", f"=-{c}{R['ebit2']}*{rate}", kind="formula", fmt=F_NUM)
        put(ws, f"{c}{R['nopat']}", f"={c}{R['ebit2']}+{c}{R['tax']}", kind="total", fmt=F_NUM)
        put(ws, f"{c}{R['da2']}", f"={c}{R['da']}", kind="formula", fmt=F_NUM)
        put(ws, f"{c}{R['capex2']}", f"=-{c}{R['capex']}", kind="formula", fmt=F_NUM)
        put(ws, f"{c}{R['nwc']}", f"={xref('Schedules', TO_SCHED[c] + str(SCH['dnwc']))}", kind="link", fmt=F_NUM)
        put(ws, f"{c}{R['ufcf']}", f"=SUM({c}{R['nopat']}:{c}{R['nwc']})", kind="total", fmt=F_NUM)
        if c in DCF_PROJ:
            p = ALL_COLS[i - 1]
            put(ws, f"{c}{R['frac']}", 1.0, kind="input", fmt=F_FRAC)
            if c == "F":
                put(ws, f"{c}{R['period']}", f"={c}{R['frac']}/2", kind="formula", fmt=F_FRAC)
            else:
                put(ws, f"{c}{R['period']}", f"={p}{R['period']}+({p}{R['frac']}+{c}{R['frac']})/2", kind="formula",
                    fmt=F_FRAC)
            put(ws, f"{c}{R['df']}", f"=1/(1+{wacc})^{c}{R['period']}", kind="formula", fmt=F_DF)
            put(ws, f"{c}{R['pv']}", f"={c}{R['ufcf']}*{c}{R['df']}", kind="total", fmt=F_NUM)
    for key in ("ebit2", "tax", "nopat", "da2", "capex2", "nwc", "ufcf", "period", "df", "pv"):
        ftext(ws, f"{FCOL_DCF}{R[key]}", ws[f"F{R[key]}"].value)
    ftext(ws, f"{FCOL_DCF}{R['frac']}", "Input: 1.00, the valuation date is the fiscal year end")

    # ---- terminal value and the bridge (Table 11)
    block_header(ws, R["hdr_tv"], "TERMINAL VALUE TO SHARE PRICE", last_col_idx=3)
    put(ws, f"C{R['hdr_tv']}", "Value", kind="header", align="right")
    debt_ref = xref("Cost of debt", "C" + str(COD["total"]))
    rows = [
        ("sumpv", "Sum of present values, FY2026E to FY2030E", f"=SUM(F{R['pv']}:J{R['pv']})", "total", F_NUM),
        ("ebitda30", "FY2030E EBITDA", f"=J{R['ebitda']}", "formula", F_NUM),
        ("mult", "Exit multiple", N.EXIT_MULTIPLE, "input", F_MULT),
        ("tv", "Terminal value at the end of FY2030", f"=C{R['ebitda30']}*C{R['mult']}", "formula", F_NUM),
        ("tvdf", "Discount factor, 5.0 years", f"=1/(1+{wacc})^SUM(F{R['frac']}:J{R['frac']})", "formula", F_DF),
        ("pvtv", "Present value of terminal value", f"=C{R['tv']}*C{R['tvdf']}", "formula", F_NUM),
        ("ev", "Enterprise value", f"=C{R['sumpv']}+C{R['pvtv']}", "total", F_NUM),
        ("tvshare", "Terminal value as a share of enterprise value", f"=C{R['pvtv']}/C{R['ev']}", "formula", F_PCT),
        ("debt", "Less: total debt", f"=-{debt_ref}", "link", F_NUM),
        ("cash", "Plus: cash", N.CASH, "input", F_NUM),
        ("nci", "Less: noncontrolling interest", -N.NCI, "input", F_NUM),
        ("equity", "Equity value", f"=C{R['ev']}+C{R['debt']}+C{R['cash']}+C{R['nci']}", "total", F_NUM),
        ("shares", "Diluted shares (millions)", f"={xref('Cover', 'C' + str(COV['shares']))}", "link", F_NUM),
        ("px", "Implied share price ($)", f"=C{R['equity']}/C{R['shares']}", "total", F_USD),
        ("price", "Current share price ($)", f"={xref('Cover', 'C' + str(COV['price']))}", "link", F_USD),
        ("upside", "Implied upside / (downside)", f"=C{R['px']}/C{R['price']}-1", "formula", F_PCT),
        ("px_eoy", "Implied share price with end-of-year discounting ($)",
         f"=(SUMPRODUCT(F{R['ufcf']}:J{R['ufcf']}/(1+{wacc})^(F{R['period']}:J{R['period']}+F{R['frac']}:J{R['frac']}/2))"
         f"+C{R['pvtv']}+C{R['debt']}+C{R['cash']}+C{R['nci']})/C{R['shares']}", "formula", F_USD),
        ("impg", "Gordon cross-check: implied perpetual growth in the 9.5x multiple",
         f"=(C{R['tv']}*{wacc}-J{R['ufcf']})/(C{R['tv']}+J{R['ufcf']})", "formula", F_PCT2),
        ("g", "Gordon cross-check: perpetual growth rate", N.TERMINAL_G, "input", F_PCT),
        ("tvg", "Gordon cross-check: terminal value at 2.5% growth",
         f"=J{R['ufcf']}*(1+C{R['g']})/({wacc}-C{R['g']})", "formula", F_NUM),
        ("impmult", "Gordon cross-check: implied exit multiple", f"=C{R['tvg']}/C{R['ebitda30']}", "formula", F_MULT),
        ("pxg", "Gordon cross-check: implied share price at 2.5% growth ($)",
         f"=(C{R['sumpv']}+C{R['tvg']}*C{R['tvdf']}+C{R['debt']}+C{R['cash']}+C{R['nci']})/C{R['shares']}",
         "formula", F_USD),
        ("evltm", "Current EV / LTM EBITDA (market, for reference)",
         f"=({xref('WACC', 'C' + str(WAC['mcap']))}+{xref('WACC', 'C' + str(WAC['debt']))}-C{R['cash']}-C{R['nci']})"
         f"/E{R['ebitda']}", "formula", F_MULT),
    ]
    for key, text, value, kind, fmt in rows:
        put(ws, f"B{R[key]}", text, bold=key in ("ev", "equity", "px"))
        put(ws, f"C{R[key]}", value, kind=kind, fmt=fmt, bold=key in ("ev", "equity", "px"))
    ws.sheet_view.showGridLines = False


def sensitivity_grid():
    """Implied share price for each (WACC, exit multiple) pair, computed the way the article's script did."""
    waccs = [N.WACC + k * N.WACC_STEP for k in (-2, -1, 0, 1, 2)]
    mults = [N.EXIT_MULTIPLE + k * N.MULT_STEP for k in (-2, -1, 0, 1, 2)]
    body = [[N.value(N.base, wacc=w, mult=mu)["px"] for mu in mults] for w in waccs]
    return waccs, mults, body


def write_sensitivity(ws):
    set_widths(ws, {"A": 2, "B": 40, "C": 12, "D": 11, "E": 11, "F": 11, "G": 11, "H": 11})
    title(ws, "Torvik Flow Systems: Sensitivity", "Implied share price ($) by WACC (down) and exit multiple (across).")
    R = SEN
    block_header(ws, R["hdr"], "SENSITIVITY: IMPLIED SHARE PRICE, WACC (DOWN) VS EXIT MULTIPLE (ACROSS)", last_col_idx=8)
    put(ws, f"B{R['note']}", "Body: an Excel data table, WACC as the column input, exit multiple as the row input. "
        "Values shown.", italic=True, color=GRAY)
    put(ws, f"B{R['wstep']}", "WACC step (down the side)")
    put(ws, f"C{R['wstep']}", N.WACC_STEP, kind="input", fmt=F_PCT2)
    put(ws, f"B{R['mstep']}", "Exit multiple step (across the top)")
    put(ws, f"C{R['mstep']}", N.MULT_STEP, kind="input", fmt=F_MULT)
    corner = R["corner"]
    put(ws, f"B{corner}", "WACC (down) / exit multiple (across)", bold=True, border_bottom=True)
    put(ws, f"C{corner}", f"={xref('DCF', 'C' + str(DCF['px']))}", kind="link", fmt=F_USD, bold=True, border_bottom=True)
    mult_ref = xref("DCF", f"$C${DCF['mult']}")
    wacc_ref = xref("WACC", f"$C${WAC['wacc']}")
    for j, col in enumerate("DEFGH"):
        k = j - 2
        f = f"={mult_ref}" if k == 0 else f"={mult_ref}{'+' if k > 0 else '-'}{abs(k)}*$C${R['mstep']}"
        put(ws, f"{col}{corner}", f, kind="formula", fmt=F_MULT, bold=True, border_bottom=True)
    waccs, mults, body = sensitivity_grid()
    for i in range(5):
        row = R["first"] + i
        k = i - 2
        f = f"={wacc_ref}" if k == 0 else f"={wacc_ref}{'+' if k > 0 else '-'}{abs(k)}*$C${R['wstep']}"
        put(ws, f"C{row}", f, kind="formula", fmt=F_PCT2, bold=True)
        for j, col in enumerate("DEFGH"):
            center = (i == 2 and j == 2)
            put(ws, f"{col}{row}", body[i][j], kind="formula", fmt=F_USD, bold=center, fill=FILL_SUBTLE if center else None)
    ws.sheet_view.showGridLines = False


def build(out=OUT):
    wb = new_workbook()
    wb.properties.creator = "Wall Street Guide"
    wb.properties.lastModifiedBy = "Wall Street Guide"
    wb.properties.title = "Torvik Flow Systems DCF (modeling test example)"
    ws = wb.active
    ws.title = "Cover"
    write_cover(ws)
    write_inputs(wb.create_sheet("Inputs"))
    write_schedules(wb.create_sheet("Schedules"))
    write_cost_of_debt(wb.create_sheet("Cost of debt"))
    write_beta(wb.create_sheet("Beta"))
    write_wacc(wb.create_sheet("WACC"))
    write_dcf(wb.create_sheet("DCF"))
    write_sensitivity(wb.create_sheet("Sensitivity"))
    from openpyxl.workbook.properties import CalcProperties
    wb.calculation = CalcProperties(fullCalcOnLoad=True)
    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)
    return out


# ---------------------------------------------------------------- checks against the article's tables
def _f1(x):
    return N.f1(x)


def _pct(x):
    return N.pct(x)


def _pct2(x):
    return N.pct(x, 2)


def _pct0(x):
    return N.pct(x, 0)


def _usd(x):
    return N.money2(x)


def _mult(x):
    return f"{N.rnd(x, 1):.1f}x"


def _beta(x):
    return f"{N.rnd(x, 3):.3f}"


def _de2(x):
    return f"{N.rnd(x, 2):.2f}"


def _de3(x):
    return f"{N.rnd(x, 3):.3f}"


def _df(x):
    return f"{N.rnd(x, 4):.4f}"


def _days1(x):
    return f"{x:.1f}"


def _days0(x):
    return f"{x:.0f}"


def _frac(x):
    return f"{x:.2f}"


def _lev(x):
    return f"{x:.2f}"


def check_list():
    """[(table, label, sheet, [cells...], formatter)] covering every article table cell."""
    C = []

    def add(table, label, sheet, cells, fmt):
        C.append((table, label, sheet, cells, fmt))

    def cols(row, letters):
        return [f"{c}{row}" for c in letters]

    # Table 1 and 2: Inputs, historical columns C..E
    t1 = [("Revenue", "rev", _f1), ("Cost of sales", "cogs", _f1), ("Gross profit", "gp", _f1), ("SG&A", "sga", _f1),
          ("EBIT", "ebit", _f1), ("Interest expense", "intexp", _f1), ("Pretax income", "ebt", _f1),
          ("Taxes", "tax", _f1), ("Net income", "ni", _f1), ("Diluted shares (millions)", "shares", _f1),
          ("Diluted EPS ($)", "eps", _usd), ("Revenue growth", "growth", _pct), ("Gross margin", "gm", _pct),
          ("SG&A as a percent of revenue", "sgapct", _pct), ("EBIT margin", "ebitm", _pct),
          ("Effective tax rate", "etr", _pct), ("D&A (from the cash flow statement)", "da", _f1),
          ("EBITDA", "ebitda", _f1), ("EBITDA margin", "ebitdam", _pct),
          ("Capex (from the cash flow statement)", "capex", _f1)]
    for label, key, fmt in t1:
        add(1, label, "Inputs", cols(INP[key], HIST_COLS), fmt)
    for seg, key in zip(SEGMENTS, SEG_KEYS):
        add(2, seg, "Inputs", cols(INP["s_" + key], HIST_COLS), _f1)
        add(2, f"{seg} growth", "Inputs", cols(INP["g_" + key], HIST_COLS), _pct)
        add(2, f"{seg} mix", "Inputs", cols(INP["m_" + key], HIST_COLS), _pct)
    add(2, "Total revenue", "Inputs", cols(INP["s_tot"], HIST_COLS), _f1)
    # Table 3: assumptions block (and the live rows against the Base rows, the switch being at 2)
    for key, text in [("pumps", "Pumps growth"), ("vc", "Valves and Controls growth"),
                      ("am", "Aftermarket Parts and Service growth"), ("gm", "Gross margin"),
                      ("sga", "SG&A as a percent of revenue")]:
        for sc in SCENARIOS:
            add(3, f"{text}, {sc}", "Inputs", cols(INP[f"a_{key}_{sc.lower()}"], PROJ_COLS), _pct)
        add(3, f"{text}, Base", "Inputs", cols(INP[f"a_{key}_live"], PROJ_COLS), _pct)
    for key, label, fmt in [("dapct", "D&A as a percent of revenue (all cases)", _pct),
                            ("capexpct", "Capex as a percent of revenue (all cases)", _pct),
                            ("dso", "Receivable days, DSO (all cases)", _days0),
                            ("dio", "Inventory days, DIO (all cases)", _days0),
                            ("dpo", "Payable days, DPO (all cases)", _days0),
                            ("accr", "Accrued liabilities as a percent of revenue", _pct),
                            ("defrev", "Deferred revenue as a percent of revenue", _pct),
                            ("taxrate", "Tax rate on EBIT (all cases)", _pct)]:
        add(3, label, "Inputs", cols(INP["a_" + key], PROJ_COLS), fmt)
    # Table 4: DCF operating build, C..J
    for label, key, fmt in [("Pumps", "pumps", _f1), ("Valves and Controls", "vc", _f1),
                            ("Aftermarket Parts and Service", "am", _f1), ("Total revenue", "rev", _f1),
                            ("Revenue growth", "growth", _pct), ("Cost of sales", "cogs", _f1),
                            ("Gross profit", "gp", _f1), ("Gross margin", "gm", _pct), ("SG&A", "sga", _f1),
                            ("EBIT", "ebit", _f1), ("EBIT margin", "ebitm", _pct), ("D&A", "da", _f1),
                            ("EBITDA", "ebitda", _f1), ("EBITDA margin", "ebitdam", _pct), ("Capex", "capex", _f1)]:
        add(4, label, "DCF", cols(DCF[key], ALL_COLS), fmt)
    # Table 5: Schedules working capital, C..K (2022A..2030E)
    for label, key, fmt in [("Accounts receivable", "ar", _f1), ("Inventory", "inv", _f1),
                            ("Accounts payable", "ap", _f1), ("Accrued liabilities", "accr", _f1),
                            ("Deferred revenue", "defrev", _f1), ("Net working capital", "nwc", _f1),
                            ("(Increase) / decrease in NWC", "dnwc", _f1), ("DSO (days)", "dso", _days1),
                            ("DIO (days)", "dio", _days1), ("DPO (days)", "dpo", _days1),
                            ("NWC as a percent of revenue", "nwcpct", _pct)]:
        add(5, label, "Schedules", cols(SCH[key], WC_COLS), fmt)
    # Table 6: PP&E, D..K (2023A..2030E)
    for label, key, fmt in [("Beginning net PP&E", "beg", _f1), ("Plus: capex", "capex", _f1),
                            ("Less: depreciation and amortization", "da", _f1), ("Ending net PP&E", "end", _f1),
                            ("Capex as a percent of revenue", "capexpct", _pct),
                            ("D&A as a percent of revenue", "dapct", _pct)]:
        add(6, label, "Schedules", cols(SCH[key], WC_COLS[1:]), fmt)
    # Table 7: cost of debt
    add(7, "Term loan B", "Cost of debt", [f"C{COD['tlb']}", f"D{COD['tlb']}", f"E{COD['tlb']}"], [_f1, _pct, _pct2])
    add(7, "Senior notes", "Cost of debt", [f"C{COD['notes']}", f"D{COD['notes']}", f"E{COD['notes']}"], [_f1, _pct, _pct2])
    add(7, "Total debt and weighted pre-tax cost", "Cost of debt",
        [f"C{COD['total']}", f"D{COD['total']}", f"E{COD['total']}"], [_f1, _pct, _pct2])
    add(7, "After-tax cost of debt at a 25% tax rate", "Cost of debt", [None, None, f"E{COD['aftertax']}"],
        [None, None, _pct2])
    # Table 8: beta
    for i, (name, *_rest) in enumerate(N.PEERS):
        r = BET[f"p{i}"]
        add(8, name, "Beta", [f"C{r}", f"D{r}", f"E{r}", f"F{r}", f"G{r}", f"H{r}"], [_lev, _f1, _f1, _de2, _pct0, _beta])
    add(8, "Median unlevered beta", "Beta", [None] * 5 + [f"H{BET['median']}"], [None] * 5 + [_beta])
    add(8, "Mean unlevered beta (for reference)", "Beta", [None] * 5 + [f"H{BET['mean']}"], [None] * 5 + [_beta])
    r = BET["torvik"]
    add(8, "Torvik debt to equity (400.0 / market cap)", "Beta", [None, f"D{r}", f"E{r}", f"F{r}", f"G{r}", None],
        [None, _f1, _f1, _de3, _pct0, None])
    add(8, "Torvik relevered beta", "Beta", [None] * 5 + [f"H{BET['relever']}"], [None] * 5 + [_beta])
    # Table 9: WACC
    for label, key, fmt in [("Risk-free rate (from the pack)", "rf", _pct2), ("Equity risk premium (from the pack)", "erp", _pct2),
                            ("Relevered beta", "beta", _beta), ("Cost of equity = risk-free + beta times ERP", "ke", _pct2),
                            ("Pre-tax cost of debt", "kd", _pct2), ("After-tax cost of debt", "kd_at", _pct2),
                            ("Share price on the valuation date ($)", "price", _usd), ("Diluted shares (millions)", "shares", _f1),
                            ("Equity value (market cap)", "mcap", _f1), ("Total debt", "debt", _f1),
                            ("Equity weight", "we", _pct), ("Debt weight", "wd", _pct), ("WACC", "wacc", _pct2)]:
        add(9, label, "WACC", [f"C{WAC[key]}"], fmt)
    # Table 10: DCF cash flow block, C..J
    for label, key, fmt in [("EBIT", "ebit2", _f1), ("Less: taxes on EBIT at 25%", "tax", _f1), ("NOPAT", "nopat", _f1),
                            ("Plus: D&A", "da2", _f1), ("Less: capex", "capex2", _f1), ("Less: increase in NWC", "nwc", _f1),
                            ("Unlevered free cash flow", "ufcf", _f1), ("Year fraction from the valuation date", "frac", _frac),
                            ("Discount period (mid-year)", "period", _frac), ("Discount factor at 9.16% WACC", "df", _df),
                            ("Present value of UFCF", "pv", _f1)]:
        add(10, label, "DCF", cols(DCF[key], ALL_COLS), fmt)
    # Table 11: terminal value and the bridge
    for label, key, fmt in [("Sum of present values, FY2026E to FY2030E", "sumpv", _f1), ("FY2030E EBITDA", "ebitda30", _f1),
                            ("Exit multiple", "mult", _mult), ("Terminal value at the end of FY2030", "tv", _f1),
                            ("Discount factor, 5.0 years", "tvdf", _df), ("Present value of terminal value", "pvtv", _f1),
                            ("Enterprise value", "ev", _f1), ("Terminal value as a share of enterprise value", "tvshare", _pct),
                            ("Less: total debt", "debt", _f1), ("Plus: cash", "cash", _f1),
                            ("Less: noncontrolling interest", "nci", _f1), ("Equity value", "equity", _f1),
                            ("Diluted shares (millions)", "shares", _f1), ("Implied share price ($)", "px", _usd),
                            ("Current share price ($)", "price", _usd), ("Implied upside / (downside)", "upside", _pct),
                            ("Implied share price with end-of-year discounting ($)", "px_eoy", _usd),
                            ("Gordon growth cross-check: implied perpetual growth in the 9.5x multiple", "impg", _pct2),
                            ("Gordon growth cross-check: terminal value at 2.5% growth", "tvg", _f1),
                            ("Gordon growth cross-check: implied exit multiple", "impmult", _mult),
                            ("Gordon growth cross-check: implied share price at 2.5% growth ($)", "pxg", _usd),
                            ("Current EV / LTM EBITDA (market, for reference)", "evltm", _mult)]:
        add(11, label, "DCF", [f"C{DCF[key]}"], fmt)
    # Table 12: sensitivity grid, axes and body
    waccs, mults, _ = sensitivity_grid()
    for i, w in enumerate(waccs):
        row = SEN["first"] + i
        add(12, _pct2(w), "Sensitivity", [f"{c}{row}" for c in "DEFGH"], _usd)
    # Table 13: the Cover's scenario summary
    for sc, key in zip(SCENARIOS, ["sum_bear", "sum_base", "sum_bull"]):
        add(13, sc, "Cover", [f"{c}{COV[key]}" for c in "CDEFGHI"], [_f1, _pct, _f1, _f1, _f1, _usd, _pct])
    return C


def _compare(vals, checks, tables, where=""):
    mismatches, n = [], 0
    for table, label, sheet, cells, fmt in checks:
        expected = tables[table]["rows"].get(label)
        if expected is None:
            mismatches.append((where, table, label, "row not in the table"))
            continue
        fmts = fmt if isinstance(fmt, list) else [fmt] * len(cells)
        for cell, exp, f in zip(cells, expected, fmts):
            if cell is None or f is None or exp == "":
                if cell is not None and f is not None and exp == "":
                    continue   # a blank in the article, a value in the sheet (2022A memo columns)
                continue
            got = vals[sheet].get(cell)
            n += 1
            if not isinstance(got, (int, float)):
                mismatches.append((where, table, label, cell, exp, got))
                continue
            shown = f(got)
            if shown != exp:
                mismatches.append((where, table, label, cell, exp, shown))
    return mismatches, n


def check_against_article(xlsx=OUT, verbose=True):
    """Recalculate with LibreOffice; compare every article table cell at display precision; then flip
    the switch to Bear and Bull on temp copies and check the Cover's live outputs against Table 13."""
    vals = recalc_values(xlsx)
    mismatches, n = _compare(vals, check_list(), TABLES, "Base")
    # the sensitivity axes read off the step cells
    for j, (col, mu) in enumerate(zip("DEFGH", TABLES[12]["header"][1:])):
        got = vals["Sensitivity"].get(f"{col}{SEN['corner']}")
        n += 1
        if _mult(got) != mu:
            mismatches.append(("Base", 12, "multiple axis", col, mu, got))
    for i, label in enumerate(TABLES[12]["rows"]):
        got = vals["Sensitivity"].get(f"C{SEN['first'] + i}")
        n += 1
        if _pct2(got) != label:
            mismatches.append(("Base", 12, "WACC axis", i, label, got))
    corner = vals["Sensitivity"].get(f"C{SEN['corner']}")
    n += 1
    if _usd(corner) != TABLES[11]["rows"]["Implied share price ($)"][0]:
        mismatches.append(("Base", 12, "corner cell", corner))
    # the Inputs check cell and the live Cover outputs
    for c in HIST_COLS:
        n += 1
        if abs(vals["Inputs"].get(f"{c}{INP['s_chk']}", 1)) > 1e-9:
            mismatches.append(("Base", 2, "segment check cell", c, vals["Inputs"].get(f"{c}{INP['s_chk']}")))
    # flip the switch
    from openpyxl import load_workbook
    for switch, sc in ((1, "Bear"), (2, "Base"), (3, "Bull")):
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td) / "flip.xlsx"
            wb = load_workbook(xlsx)
            wb["Cover"][f"C{COV['switch']}"].value = switch
            wb.save(tmp)
            v = recalc_values(tmp)
        exp = TABLES[13]["rows"][sc]
        got = [v["Cover"].get(f"C{COV[k]}") for k in ("o_rev", "o_ebitda", "o_wacc", "o_ev", "o_px", "o_upside")]
        shown = [_f1(got[0]), _f1(got[1]), _pct2(got[2]), _f1(got[3]), _usd(got[4]), _pct(got[5])]
        want = [exp[0], exp[2], TABLES[9]["rows"]["WACC"][0], exp[4], exp[5], exp[6]]
        n += len(want)
        for s, w, k in zip(shown, want, ("revenue", "EBITDA", "WACC", "EV", "price", "upside")):
            if s != w:
                mismatches.append((sc, 13, k, w, s))
        name = v["Cover"].get(f"D{COV['switch']}")
        n += 1
        if name != sc:
            mismatches.append((sc, 13, "switch label", sc, name))
    if verbose:
        print(f"compared {n} cells against the article's tables; mismatches: {len(mismatches)}")
        for m in mismatches:
            print("  MISMATCH", m)
    return mismatches, vals


def no_dashes(xlsx=OUT):
    """No em dash, en dash or Unicode minus in any cell label of the workbook."""
    from openpyxl import load_workbook
    bad = []
    wb = load_workbook(xlsx)
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and any(ch in c.value for ch in "—–−"):
                    bad.append((ws.title, c.coordinate, c.value))
    return bad


if __name__ == "__main__":
    path = build()
    print("built", path)
    assert not no_dashes(path), no_dashes(path)
    mm, _ = check_against_article(path)
    assert not mm, "workbook disagrees with the article"
