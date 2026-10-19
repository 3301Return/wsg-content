#!/usr/bin/env python3
"""Build scripts/images/models/targetco-lbo.xlsx: the TargetCo LBO from the article
"LBO Model Explained: What an Undergrad Actually Needs to Know" (October 1, 2026), with live formulas.

Sheet "LBO": one worksheet in the order the article's Section 3 recommends for a timed test:
transaction assumptions, debt terms, operating assumptions, sources and uses (with the check cell),
operating model, cash flow to debt paydown, debt schedule by tranche (term loan with a MIN cash
sweep, bullet notes, a revolver with a MAX draw), the Circ toggle on the interest line, a Year 1
average-balance block, returns (MOIC and IRR, plus the IRR function on the equity cash flows) and
the two sensitivity grids. The grids are written as values computed here the same way the article's
writer computed them (run_case below), laid out like an Excel data table with the corner cell linked
to the IRR.

Sheet "Paper LBO": the Section 7 paper LBO, the out-loud rounded version the article tabulates,
with an exact (unrounded) version underneath for the check the article quotes.

Run from the repo root:  python3 scripts/images/models/build_targetco_lbo.py
Idempotent: rewrites the workbook every time.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import (FILL_SUBTLE, FMT_INT, FMT_MULT, FMT_MULT2, FMT_PCT, XL_FONT, XL_SIZE,  # noqa: E402
                     header_bar, new_workbook, put, set_widths)

OUT_XLSX = ROOT / "scripts" / "images" / "models" / "targetco-lbo.xlsx"

# Banker format that prints zeros as 0.0 (the article's tables print 0.0, not a dash).
FMT_NUM_Z = '#,##0.0;(#,##0.0);0.0'
FMT_YEAR = '"Year "0'
FMT_ZERO = '0'
FMT_INT_Z = '#,##0;(#,##0);0'
FMT_YEAR0 = '"Year "0" (LTM)"'

# ---------------------------------------------------------------- the article's inputs
A = dict(
    ltm_ebitda=100.0, ltm_rev=500.0, entry_mult=10.0, exist_debt=150.0, exist_cash=0.0,
    txn_fees=20.0, fin_fees=10.0, fee_years=5, min_cash=20.0, exit_mult=10.0, exit_year=5,
    tlb_turns=4.5, tlb_rate=0.08, tlb_amort=0.01, tlb_sweep=1.0,
    notes_turns=1.5, notes_rate=0.09, notes_amort=0.0, notes_sweep=0.0,
    revolver_commit=75.0, revolver_drawn=0.0,
    growth=0.06, margin_step=0.005, da_pct=0.03, capex_pct=0.03, nwc_pct=0.10, tax=0.25,
)


# ---------------------------------------------------------------- sensitivity engine (writer's method)
def irr_from_moic(moic, years):
    return moic ** (1 / years) - 1


def run_case(entry_m, exit_m, lev_turns=6.0, hold=5):
    """IRR and MOIC for one grid cell, computed the way the article's writer did: debt split 75/25
    between term loan and notes, financing fees scaled with the debt ($10.0 on $600.0), fee
    amortization of fees/5 in every year of the hold, all cash available paying down the term loan."""
    ltm_ebitda, existing_debt = A["ltm_ebitda"], A["exist_debt"]
    ev_ = ltm_ebitda * entry_m
    debt_ = ltm_ebitda * lev_turns
    tlb_ = debt_ * 0.75
    notes_ = debt_ * 0.25
    fin_fees = A["fin_fees"] * debt_ / 600.0
    uses_ = (ev_ - existing_debt) + existing_debt + A["txn_fees"] + fin_fees + A["min_cash"]
    eq_ = uses_ - debt_
    rev_p, tlb_b, cash_ = A["ltm_rev"], tlb_, A["min_cash"]
    margin0 = A["ltm_ebitda"] / A["ltm_rev"]
    ebitda_y = None
    for y in range(1, hold + 1):
        rev = rev_p * (1 + A["growth"])
        ebitda_y = rev * (margin0 + A["margin_step"] * y)
        da = rev * A["da_pct"]
        ebit = ebitda_y - da
        interest = tlb_b * A["tlb_rate"] + notes_ * A["notes_rate"]
        ebt = ebit - interest - fin_fees / 5
        ni = ebt * (1 - A["tax"])
        cfads = ni + da + fin_fees / 5 - rev * A["capex_pct"] - (rev - rev_p) * A["nwc_pct"]
        pay = min(cfads, tlb_b)
        tlb_b -= pay
        cash_ += cfads - pay
        rev_p = rev
    eq_exit = ebitda_y * exit_m - (tlb_b + notes_) + cash_
    m = eq_exit / eq_
    return m, irr_from_moic(m, hold)


ENTRIES = [8.0, 9.0, 10.0, 11.0, 12.0]
EXITS = [8.0, 9.0, 10.0, 11.0, 12.0]
LEVS = [4.0, 5.0, 6.0, 7.0]
HOLDS = [3, 4, 5, 6, 7]


def grid_entry_exit():
    return [[run_case(en, ex)[1] for ex in EXITS] for en in ENTRIES]


def grid_lev_year():
    return [[run_case(10.0, 10.0, lv, h)[1] for h in HOLDS] for lv in LEVS]


# ---------------------------------------------------------------- sheet helpers
YEAR_COLS = ["D", "E", "F", "G", "H", "I"]   # Year 0 (LTM) .. Year 5
PROJ_COLS = YEAR_COLS[1:]                     # Year 1 .. Year 5
COL_IDX = {c: i for i, c in enumerate("ABCDEFGHIJ")}


def prev_col(c):
    return "ABCDEFGHIJ"[COL_IDX[c] - 1]


def bold_label(ws, ref, text):
    put(ws, ref, text, bold=True)


def year_row(ws, row, with_year0=True, close_label=None):
    """Year header: numeric year values with a 'Year N' format so formulas can use the number."""
    from openpyxl.styles import Alignment, Border, Font, Side
    thin = Side(style="thin", color="000000")
    cols = YEAR_COLS if with_year0 else PROJ_COLS
    years = list(range(0, 6)) if with_year0 else list(range(1, 6))
    for col, y in zip(cols, years):
        c = ws[f"{col}{row}"]
        c.value = y
        c.number_format = FMT_YEAR0 if y == 0 else FMT_YEAR
        c.font = Font(name=XL_FONT, size=XL_SIZE, bold=True)
        c.alignment = Alignment(horizontal="right")
        c.border = Border(bottom=thin)
    if close_label and not with_year0:
        c = ws[f"D{row}"]
        c.value = close_label
        c.font = Font(name=XL_FONT, size=XL_SIZE, bold=True)
        c.alignment = Alignment(horizontal="right")
        c.border = Border(bottom=thin)


def formula_label(ws, ref, text):
    """Write a formula's text into a cell as a plain string (for the formula close-up column)."""
    c = put(ws, ref, text, italic=True, color="52514E")
    c.data_type = "s"
    return c


# ---------------------------------------------------------------- build
def build(out_path=OUT_XLSX):
    from openpyxl.styles import Font
    from openpyxl.workbook.defined_name import DefinedName

    wb = new_workbook()
    wb.properties.creator = "Wall Street Guide"
    wb.properties.lastModifiedBy = "Wall Street Guide"
    wb.properties.title = "TargetCo LBO model"
    ws = wb.active
    ws.title = "LBO"
    set_widths(ws, {"A": 2, "B": 54, "C": 2, "D": 12, "E": 12, "F": 12, "G": 12, "H": 12, "I": 12, "J": 62})
    ws.sheet_view.showGridLines = False

    R = {}   # row map, name -> row number

    put(ws, "B2", "TargetCo LBO model", bold=True, size=12)
    put(ws, "B3", "$ in millions, fiscal year ending December 31. Blue on yellow = typed input, black = formula.", italic=True)

    # ---- transaction assumptions
    header_bar(ws, 5, 2, 9, "TRANSACTION ASSUMPTIONS")
    rows = [
        ("ltm_ebitda", "LTM EBITDA", A["ltm_ebitda"], "input", FMT_NUM_Z),
        ("ltm_rev", "LTM revenue", A["ltm_rev"], "input", FMT_NUM_Z),
        ("ltm_margin", "LTM EBITDA margin", "=D{ltm_ebitda}/D{ltm_rev}", "formula", FMT_PCT),
        ("entry_mult", "Entry multiple (x LTM EBITDA)", A["entry_mult"], "input", FMT_MULT),
        ("ev", "Enterprise value", "=D{ltm_ebitda}*D{entry_mult}", "formula", FMT_NUM_Z),
        ("exist_debt", "Existing debt (repaid at close)", A["exist_debt"], "input", FMT_NUM_Z),
        ("exist_cash", "Existing excess cash (cash-free, debt-free deal)", A["exist_cash"], "input", FMT_NUM_Z),
        ("eq_price", "Equity purchase price (EV less net debt)", "=D{ev}-D{exist_debt}+D{exist_cash}", "formula", FMT_NUM_Z),
        ("txn_fees", "Transaction fees (advisory, legal), expensed at close", A["txn_fees"], "input", FMT_NUM_Z),
        ("fin_fees", "Financing fees, capitalized and amortized", A["fin_fees"], "input", FMT_NUM_Z),
        ("fee_years", "Financing fee amortization period (years)", A["fee_years"], "input", FMT_INT),
        ("min_cash", "Minimum cash funded at close", A["min_cash"], "input", FMT_NUM_Z),
        ("exit_mult", "Exit multiple (x EBITDA)", A["exit_mult"], "input", FMT_MULT),
        ("exit_year", "Exit year", A["exit_year"], "input", FMT_YEAR),
        ("circ", "Circ toggle (1 = average balance interest, 0 = beginning)", 0, "input", FMT_ZERO),
    ]
    r = 6
    for name, label, value, kind, fmt in rows:
        R[name] = r
        r += 1
    for name, label, value, kind, fmt in rows:
        put(ws, f"B{R[name]}", label)
        v = value.format(**R) if isinstance(value, str) else value
        put(ws, f"D{R[name]}", v, kind=kind, fmt=fmt)
    wb.defined_names["Circ"] = DefinedName("Circ", attr_text=f"LBO!$D${R['circ']}")
    r += 1

    # ---- debt terms
    header_bar(ws, r, 2, 9, "DEBT TERMS"); r += 1
    R["dt_hdr"] = r
    for col, text in zip("DEFGH", ["x EBITDA", "$ amount", "Rate", "Amort. a year", "Cash sweep"]):
        put(ws, f"{col}{r}", text, bold=True, align="right", border_bottom=True)
    r += 1
    R["tlb"] = r
    put(ws, f"B{r}", "Term Loan B (seven year, floating rate)")
    put(ws, f"D{r}", A["tlb_turns"], kind="input", fmt=FMT_MULT)
    put(ws, f"E{r}", f"=D{r}*$D${R['ltm_ebitda']}", kind="formula", fmt=FMT_NUM_Z)
    put(ws, f"F{r}", A["tlb_rate"], kind="input", fmt=FMT_PCT)
    put(ws, f"G{r}", A["tlb_amort"], kind="input", fmt=FMT_PCT)
    put(ws, f"H{r}", A["tlb_sweep"], kind="input", fmt='0%')
    r += 1
    R["notes"] = r
    put(ws, f"B{r}", "Senior notes (fixed, bullet at maturity, no prepayment)")
    put(ws, f"D{r}", A["notes_turns"], kind="input", fmt=FMT_MULT)
    put(ws, f"E{r}", f"=D{r}*$D${R['ltm_ebitda']}", kind="formula", fmt=FMT_NUM_Z)
    put(ws, f"F{r}", A["notes_rate"], kind="input", fmt=FMT_PCT)
    put(ws, f"G{r}", A["notes_amort"], kind="input", fmt=FMT_PCT)
    put(ws, f"H{r}", A["notes_sweep"], kind="input", fmt='0%')
    r += 1
    R["revolver"] = r
    put(ws, f"B{r}", "Revolver commitment (undrawn at close)")
    put(ws, f"E{r}", A["revolver_commit"], kind="input", fmt=FMT_NUM_Z)
    r += 1
    R["debt_total"] = r
    put(ws, f"B{r}", "Total debt at close", kind="total")
    put(ws, f"D{r}", f"=D{R['tlb']}+D{R['notes']}", kind="total", fmt=FMT_MULT)
    put(ws, f"E{r}", f"=E{R['tlb']}+E{R['notes']}", kind="total", fmt=FMT_NUM_Z)
    r += 2

    # ---- operating assumptions
    header_bar(ws, r, 2, 9, "OPERATING ASSUMPTIONS"); r += 1
    for name, label, value, fmt in [
        ("growth", "Revenue growth a year", A["growth"], FMT_PCT),
        ("margin_step", "EBITDA margin step a year (percentage points)", A["margin_step"], FMT_PCT),
        ("da_pct", "D&A, % of revenue", A["da_pct"], FMT_PCT),
        ("capex_pct", "Capex, % of revenue", A["capex_pct"], FMT_PCT),
        ("nwc_pct", "Net working capital, % of revenue", A["nwc_pct"], FMT_PCT),
        ("tax", "Tax rate", A["tax"], FMT_PCT),
    ]:
        R[name] = r
        put(ws, f"B{r}", label)
        put(ws, f"D{r}", value, kind="input", fmt=fmt)
        r += 1
    r += 1

    # ---- sources and uses
    R["su_header"] = r
    header_bar(ws, r, 2, 9, "SOURCES AND USES"); r += 1
    put(ws, f"B{r}", "Uses", bold=True, border_bottom=True)
    put(ws, f"D{r}", "$ millions", bold=True, align="right", border_bottom=True)
    put(ws, f"F{r}", "Sources", bold=True, border_bottom=True)
    put(ws, f"G{r}", "", border_bottom=True)
    put(ws, f"H{r}", "x EBITDA", bold=True, align="right", border_bottom=True)
    put(ws, f"I{r}", "$ millions", bold=True, align="right", border_bottom=True)
    r += 1
    R["u_eq"] = r; R["s_rev"] = r
    put(ws, f"B{r}", "Purchase of equity (EV less net debt)")
    put(ws, f"D{r}", f"=D{R['eq_price']}", kind="formula", fmt=FMT_NUM_Z)
    put(ws, f"F{r}", "Revolver (undrawn at close)")
    put(ws, f"I{r}", A["revolver_drawn"], kind="input", fmt=FMT_NUM_Z)
    r += 1
    R["u_debt"] = r; R["s_tlb"] = r
    put(ws, f"B{r}", "Repay existing debt")
    put(ws, f"D{r}", f"=D{R['exist_debt']}", kind="formula", fmt=FMT_NUM_Z)
    put(ws, f"F{r}", "Term Loan B")
    put(ws, f"H{r}", f"=I{r}/$D${R['ltm_ebitda']}", kind="formula", fmt=FMT_MULT)
    put(ws, f"I{r}", f"=E{R['tlb']}", kind="formula", fmt=FMT_NUM_Z)
    r += 1
    R["u_txn"] = r; R["s_notes"] = r
    put(ws, f"B{r}", "Transaction fees")
    put(ws, f"D{r}", f"=D{R['txn_fees']}", kind="formula", fmt=FMT_NUM_Z)
    put(ws, f"F{r}", "Senior notes")
    put(ws, f"H{r}", f"=I{r}/$D${R['ltm_ebitda']}", kind="formula", fmt=FMT_MULT)
    put(ws, f"I{r}", f"=E{R['notes']}", kind="formula", fmt=FMT_NUM_Z)
    r += 1
    R["u_fin"] = r; R["s_equity"] = r
    put(ws, f"B{r}", "Financing fees")
    put(ws, f"D{r}", f"=D{R['fin_fees']}", kind="formula", fmt=FMT_NUM_Z)
    put(ws, f"F{r}", "Sponsor equity (plug)")
    r += 1
    R["u_cash"] = r
    put(ws, f"B{r}", "Cash to balance sheet")
    put(ws, f"D{r}", f"=D{R['min_cash']}", kind="formula", fmt=FMT_NUM_Z)
    r += 1
    R["u_total"] = r; R["s_total"] = r
    put(ws, f"B{r}", "Total uses", kind="total")
    put(ws, f"D{r}", f"=SUM(D{R['u_eq']}:D{R['u_cash']})", kind="total", fmt=FMT_NUM_Z)
    put(ws, f"F{r}", "Total sources", kind="total")
    put(ws, f"G{r}", "", kind="total")
    put(ws, f"H{r}", "", kind="total")
    put(ws, f"I{r}", f"=SUM(I{R['s_rev']}:I{R['s_equity']})", kind="total", fmt=FMT_NUM_Z)
    # the plug, written now that the totals row is known
    put(ws, f"I{R['s_equity']}", f"=D{R['u_total']}-SUM(I{R['s_rev']}:I{R['s_notes']})", kind="formula", fmt=FMT_NUM_Z)
    r += 1
    R["su_check"] = r
    put(ws, f"B{r}", "Check: sources less uses (should read 0.0)", italic=True)
    put(ws, f"D{r}", f"=I{R['s_total']}-D{R['u_total']}", kind="formula", fmt=FMT_NUM_Z)
    put(ws, f"F{r}", "Sponsor equity, % of total sources", italic=True)
    put(ws, f"I{r}", f"=I{R['s_equity']}/I{R['s_total']}", kind="formula", fmt=FMT_PCT)
    r += 1
    R["su_lev"] = r
    put(ws, f"B{r}", "Total debt / LTM EBITDA", italic=True)
    put(ws, f"D{r}", f"=(I{R['s_rev']}+I{R['s_tlb']}+I{R['s_notes']})/D{R['ltm_ebitda']}", kind="formula", fmt=FMT_MULT)
    R["su_end"] = r
    r += 2

    # ---- operating model
    R["om_header"] = r
    header_bar(ws, r, 2, 9, "OPERATING MODEL"); r += 1
    R["om_years"] = r
    year_row(ws, r, with_year0=True); r += 1
    om = ["rev", "growth_row", "margin", "ebitda", "da", "ebit", "int_tlb", "int_notes", "fee_am", "ebt", "taxes", "ni"]
    for name in om:
        R[name] = r
        r += 1
    R["om_end"] = r - 1
    r += 1

    # ---- cash flow to debt paydown
    R["cf_header"] = r
    header_bar(ws, r, 2, 9, "CASH FLOW TO DEBT PAYDOWN"); r += 1
    R["cf_years"] = r
    year_row(ws, r, with_year0=False, close_label="Close"); r += 1
    cf = ["cf_ni", "cf_da", "cf_fee", "cf_capex", "cf_nwc", "cfads", "cf_mand", "cf_sweep", "cf_rev", "cf_change", "cash_beg", "cash_end", "cash_check"]
    for name in cf:
        R[name] = r
        r += 1
    R["cf_end"] = r - 1
    r += 1

    # ---- debt schedule
    R["ds_header"] = r
    header_bar(ws, r, 2, 9, "DEBT SCHEDULE"); r += 1
    R["ds_years"] = r
    year_row(ws, r, with_year0=False, close_label="Close"); r += 1
    ds = ["tlb_label", "tlb_beg", "tlb_mand", "tlb_avail", "tlb_sweep", "tlb_end", "tlb_int", "circ_echo",
          "alt_label", "alt_int", "alt_cfads", "alt_end", "blank1",
          "nt_label", "nt_beg", "nt_rep", "nt_end", "nt_int", "blank2",
          "rv_label", "rv_beg", "rv_draw", "rv_rep", "rv_end", "blank3",
          "debt_end", "lev", "cov", "debt_check"]
    for name in ds:
        R[name] = r
        r += 1
    R["ds_end"] = r - 1
    r += 1

    # ---- returns
    R["ret_header"] = r
    header_bar(ws, r, 2, 9, "RETURNS"); r += 1
    ret = ["ret_year", "ret_ebitda", "ret_mult", "ret_ev", "ret_debt", "ret_cash", "ret_equity", "ret_invested", "moic", "irr",
           "blank4", "cfl_years", "cfl", "irr_fn"]
    for name in ret:
        R[name] = r
        r += 1
    R["ret_end"] = r - 1
    r += 1

    # ---- sensitivities
    R["s1_header"] = r; r += 1
    R["s1_note"] = r; r += 1
    R["s1_corner"] = r; r += 1
    R["s1_first"] = r; r += len(ENTRIES)
    R["s1_end"] = r - 1
    r += 1
    R["s2_header"] = r; r += 1
    R["s2_note"] = r; r += 1
    R["s2_corner"] = r; r += 1
    R["s2_first"] = r; r += len(LEVS)
    R["s2_end"] = r - 1

    # ================================================================ fill the year blocks
    F = {}   # formula text for the close-up column, keyed by row name (Year 1 column E)

    def write_row(name, label, year0=None, proj=None, kind="formula", fmt=FMT_NUM_Z, label_kind="label", bold=False, italic=False, indent=0):
        """year0: value or formula template for column D; proj: template for E..I with {c} = this column,
        {p} = previous column. Templates use {name} for row numbers."""
        row = R[name]
        put(ws, f"B{row}", label, kind=label_kind, bold=bold, italic=italic, indent=indent)
        if year0 is not None:
            is_formula = isinstance(year0, str) and year0.startswith("=")
            v = year0.format(c="D", p="C", **R) if is_formula else year0
            put(ws, f"D{row}", v, kind=kind if is_formula else "input", fmt=fmt)
        if proj is not None:
            for c in PROJ_COLS:
                v = proj.format(c=c, p=prev_col(c), **R) if isinstance(proj, str) else proj
                put(ws, f"{c}{row}", v, kind=kind, fmt=fmt)
            F[name] = proj.format(c="E", p="D", **R) if isinstance(proj, str) else str(proj)

    # operating model
    write_row("rev", "Revenue", year0="=D{ltm_rev}", proj="={p}{rev}*(1+$D${growth})")
    write_row("growth_row", "Revenue growth", proj="={c}{rev}/{p}{rev}-1", fmt=FMT_PCT, italic=True)
    write_row("margin", "EBITDA margin", year0="=D{ltm_margin}", proj="={p}{margin}+$D${margin_step}", fmt=FMT_PCT, italic=True)
    write_row("ebitda", "EBITDA", year0="=D{rev}*D{margin}", proj="={c}{rev}*{c}{margin}", kind="total")
    write_row("da", "Less: D&A (3% of revenue)", year0="=-D{rev}*$D${da_pct}", proj="=-{c}{rev}*$D${da_pct}")
    write_row("ebit", "EBIT", year0="=D{ebitda}+D{da}", proj="={c}{ebitda}+{c}{da}", kind="total")
    write_row("int_tlb", "Less: Term Loan B interest (8% on beginning balance)", proj="=-{c}{tlb_int}")
    write_row("int_notes", "Less: Senior notes interest (9% on $150.0)", proj="=-{c}{nt_int}")
    write_row("fee_am", "Less: Financing fee amortization ($10.0 over 5 years)", proj="=-IF({c}${om_years}<=$D${fee_years},$D${fin_fees}/$D${fee_years},0)")
    write_row("ebt", "Pre-tax income", proj="={c}{ebit}+{c}{int_tlb}+{c}{int_notes}+{c}{fee_am}", kind="total")
    write_row("taxes", "Less: Taxes (25%, never below zero)", proj="=-MAX(0,{c}{ebt}*$D${tax})")
    write_row("ni", "Net income", proj="={c}{ebt}+{c}{taxes}", kind="total")

    # cash flow to debt paydown
    write_row("cf_ni", "Net income", proj="={c}{ni}")
    write_row("cf_da", "Plus: D&A", proj="=-{c}{da}")
    write_row("cf_fee", "Plus: Financing fee amortization (non-cash)", proj="=-{c}{fee_am}")
    write_row("cf_capex", "Less: Capex (3% of revenue)", proj="=-{c}{rev}*$D${capex_pct}")
    write_row("cf_nwc", "Less: Increase in net working capital (10% of revenue growth)", proj="=-({c}{rev}-{p}{rev})*$D${nwc_pct}")
    write_row("cfads", "Cash available for debt repayment", proj="=SUM({c}{cf_ni}:{c}{cf_nwc})", kind="total")
    write_row("cf_mand", "Less: Mandatory Term Loan B amortization (1% of $450.0)", proj="={c}{tlb_mand}")
    write_row("cf_sweep", "Less: Cash sweep to Term Loan B", proj="={c}{tlb_sweep}")
    write_row("cf_rev", "Plus: Revolver draw / (repayment)", proj="={c}{rv_draw}+{c}{rv_rep}")
    write_row("cf_change", "Change in cash", proj="=SUM({c}{cfads}:{c}{cf_rev})", kind="total")
    write_row("cash_beg", "Beginning cash", proj="={p}{cash_end}")
    write_row("cash_end", "Ending cash (minimum cash $20.0)", year0="=D{min_cash}", proj="={c}{cash_beg}+{c}{cf_change}", kind="total")
    put(ws, f"B{R['cash_check']}", "Check: cash at or above the minimum", italic=True)
    for c in PROJ_COLS:
        put(ws, f"{c}{R['cash_check']}", f'=IF({c}{R["cash_end"]}>=$D${R["min_cash"]}-0.001,"OK","SHORT")', kind="formula", align="right", italic=True)

    # debt schedule: term loan
    bold_label(ws, f"B{R['tlb_label']}", "Term Loan B (8.0%, 1% mandatory amortization, 100% sweep)")
    write_row("tlb_beg", "Beginning balance", proj="={p}{tlb_end}", indent=1)
    write_row("tlb_mand", "Less: Mandatory amortization (1% of the original $450.0)", proj="=-MIN({c}{tlb_beg},$E${tlb}*$G${tlb})", indent=1)
    write_row("tlb_avail", "Cash above minimum after mandatory amortization",
              proj="=MAX(0,{c}{cash_beg}+{c}{cfads}+{c}{tlb_mand}+{c}{cf_rev}-$D${min_cash})", indent=1, italic=True)
    write_row("tlb_sweep", "Less: Cash sweep (MIN of cash available and balance left)", proj="=-MIN({c}{tlb_avail},{c}{tlb_beg}+{c}{tlb_mand})*$H${tlb}", indent=1)
    write_row("tlb_end", "Ending balance", year0="=E{tlb}", proj="={c}{tlb_beg}+{c}{tlb_mand}+{c}{tlb_sweep}", kind="total", indent=1)
    write_row("tlb_int", "Interest (Circ 1 = average balance, 0 = beginning balance)",
              proj="=IF(Circ=1,AVERAGE({c}{tlb_beg},{c}{tlb_end}),{c}{tlb_beg})*$F${tlb}", indent=1)
    put(ws, f"B{R['circ_echo']}", "Circ toggle (named cell D{} in the assumptions)".format(R["circ"]), italic=True, indent=1)
    put(ws, f"E{R['circ_echo']}", "=Circ", kind="formula", fmt=FMT_ZERO, italic=True)
    F["circ_echo"] = "=Circ"
    bold_label(ws, f"B{R['alt_label']}", "Year 1 with Circ = 1 (average balance, iteration on)")
    put(ws, f"B{R['alt_int']}", "Term Loan B interest, average balance", indent=1)
    put(ws, f"E{R['alt_int']}", f"=AVERAGE(E{R['tlb_beg']},E{R['alt_end']})*$F${R['tlb']}", kind="formula", fmt=FMT_NUM_Z)
    F["alt_int"] = f"=AVERAGE(E{R['tlb_beg']},E{R['alt_end']})*$F${R['tlb']}"
    put(ws, f"B{R['alt_cfads']}", "Cash available for debt repayment", indent=1)
    alt_cfads = (f"=(E{R['ebit']}+E{R['int_notes']}+E{R['fee_am']}-E{R['alt_int']})*(1-$D${R['tax']})"
                 f"+E{R['cf_da']}+E{R['cf_fee']}+E{R['cf_capex']}+E{R['cf_nwc']}")
    put(ws, f"E{R['alt_cfads']}", alt_cfads, kind="formula", fmt=FMT_NUM_Z)
    F["alt_cfads"] = alt_cfads
    put(ws, f"B{R['alt_end']}", "Term Loan B, ending balance", indent=1)
    alt_end = (f"=E{R['tlb_beg']}+E{R['tlb_mand']}-MIN(MAX(0,E{R['cash_beg']}+E{R['alt_cfads']}+E{R['tlb_mand']}-$D${R['min_cash']}),"
               f"E{R['tlb_beg']}+E{R['tlb_mand']})*$H${R['tlb']}")
    put(ws, f"E{R['alt_end']}", alt_end, kind="formula", fmt=FMT_NUM_Z)
    F["alt_end"] = alt_end

    # senior notes
    bold_label(ws, f"B{R['nt_label']}", "Senior notes (9.0% fixed, bullet at maturity, no prepayment)")
    write_row("nt_beg", "Beginning balance", proj="={p}{nt_end}", indent=1)
    write_row("nt_rep", "Less: Repayment", proj="=-MIN({c}{nt_beg},$E${notes}*$G${notes})", indent=1)
    write_row("nt_end", "Ending balance", year0="=E{notes}", proj="={c}{nt_beg}+{c}{nt_rep}", kind="total", indent=1)
    write_row("nt_int", "Interest expense (9.0% on beginning balance)", proj="={c}{nt_beg}*$F${notes}", indent=1)

    # revolver
    bold_label(ws, f"B{R['rv_label']}", "Revolver ($75.0 commitment)")
    write_row("rv_beg", "Beginning balance", proj="={p}{rv_end}", indent=1)
    write_row("rv_draw", "Draw to cover a cash shortfall (MAX of 0 and shortfall)",
              proj="=MAX(0,$D${min_cash}-({c}{cash_beg}+{c}{cfads}+{c}{tlb_mand}))", indent=1)
    write_row("rv_rep", "Less: Repayment (first claim on spare cash)",
              proj="=-MIN({c}{rv_beg},MAX(0,{c}{cash_beg}+{c}{cfads}+{c}{tlb_mand}-$D${min_cash}))", indent=1)
    write_row("rv_end", "Ending balance", year0="=I{s_rev}", proj="={c}{rv_beg}+{c}{rv_draw}+{c}{rv_rep}", kind="total", indent=1)

    # totals and ratios
    write_row("debt_end", "Total debt, ending", year0="=D{tlb_end}+D{nt_end}+D{rv_end}", proj="={c}{tlb_end}+{c}{nt_end}+{c}{rv_end}", kind="total")
    write_row("lev", "Total debt / EBITDA", year0="=D{debt_end}/D{ebitda}", proj="={c}{debt_end}/{c}{ebitda}", fmt=FMT_MULT2, italic=True)
    write_row("cov", "EBITDA / cash interest", proj="={c}{ebitda}/({c}{tlb_int}+{c}{nt_int})", fmt=FMT_MULT2, italic=True)
    put(ws, f"B{R['debt_check']}", "Check: no debt balance below zero", italic=True)
    for c in PROJ_COLS:
        put(ws, f"{c}{R['debt_check']}", f'=IF(MIN({c}{R["tlb_end"]},{c}{R["nt_end"]},{c}{R["rv_end"]})<-0.001,"ERROR","OK")',
            kind="formula", align="right", italic=True)

    # formula close-up column (Year 1 formulas as text)
    put(ws, f"J{R['tlb_label']}", "Formula (Year 1 column)", bold=True, border_bottom=True)
    for name in ["tlb_beg", "tlb_mand", "tlb_avail", "tlb_sweep", "tlb_end", "tlb_int", "circ_echo", "alt_int", "alt_cfads", "alt_end"]:
        formula_label(ws, f"J{R[name]}", F[name])

    # returns
    put(ws, f"B{R['ret_year']}", "Exit year")
    put(ws, f"D{R['ret_year']}", f"=D{R['exit_year']}", kind="formula", fmt=FMT_YEAR)
    put(ws, f"B{R['ret_ebitda']}", "Exit year EBITDA")
    put(ws, f"D{R['ret_ebitda']}", f"=INDEX($E${R['ebitda']}:$I${R['ebitda']},1,$D${R['exit_year']})", kind="formula", fmt=FMT_NUM_Z)
    put(ws, f"B{R['ret_mult']}", "Exit multiple")
    put(ws, f"D{R['ret_mult']}", f"=D{R['exit_mult']}", kind="formula", fmt=FMT_MULT)
    put(ws, f"B{R['ret_ev']}", "Exit enterprise value")
    put(ws, f"D{R['ret_ev']}", f"=D{R['ret_ebitda']}*D{R['ret_mult']}", kind="formula", fmt=FMT_NUM_Z)
    put(ws, f"B{R['ret_debt']}", "Less: Total debt at exit")
    put(ws, f"D{R['ret_debt']}", f"=-INDEX($E${R['debt_end']}:$I${R['debt_end']},1,$D${R['exit_year']})", kind="formula", fmt=FMT_NUM_Z)
    put(ws, f"B{R['ret_cash']}", "Plus: Cash at exit")
    put(ws, f"D{R['ret_cash']}", f"=INDEX($E${R['cash_end']}:$I${R['cash_end']},1,$D${R['exit_year']})", kind="formula", fmt=FMT_NUM_Z)
    put(ws, f"B{R['ret_equity']}", "Exit equity value", kind="total")
    put(ws, f"D{R['ret_equity']}", f"=SUM(D{R['ret_ev']}:D{R['ret_cash']})", kind="total", fmt=FMT_NUM_Z)
    put(ws, f"B{R['ret_invested']}", "Sponsor equity invested (from sources and uses)")
    put(ws, f"D{R['ret_invested']}", f"=I{R['s_equity']}", kind="formula", fmt=FMT_NUM_Z)
    put(ws, f"B{R['moic']}", "MOIC (exit equity / equity invested)", bold=True)
    put(ws, f"D{R['moic']}", f"=D{R['ret_equity']}/D{R['ret_invested']}", kind="formula", fmt=FMT_MULT2, bold=True)
    put(ws, f"B{R['irr']}", "IRR (MOIC ^ (1 / years) less 1)", bold=True)
    put(ws, f"D{R['irr']}", f"=D{R['moic']}^(1/D{R['ret_year']})-1", kind="formula", fmt=FMT_PCT, bold=True)
    year_row(ws, R["cfl_years"], with_year0=False, close_label="Close")
    put(ws, f"B{R['cfl']}", "Sponsor equity cash flows (equity in as a negative)")
    put(ws, f"D{R['cfl']}", f"=-D{R['ret_invested']}", kind="formula", fmt=FMT_NUM_Z)
    for c in PROJ_COLS:
        put(ws, f"{c}{R['cfl']}", f"=IF({c}${R['cfl_years']}=$D${R['exit_year']},$D${R['ret_equity']},0)", kind="formula", fmt=FMT_NUM_Z)
    put(ws, f"B{R['irr_fn']}", "IRR check (Excel IRR function on the cash flows above)", italic=True)
    put(ws, f"D{R['irr_fn']}", f"=IRR(D{R['cfl']}:I{R['cfl']})", kind="formula", fmt=FMT_PCT, italic=True)

    # sensitivity 1: entry vs exit multiple
    header_bar(ws, R["s1_header"], 2, 9, "SENSITIVITY: IRR, ENTRY MULTIPLE VS EXIT MULTIPLE (data table)")
    put(ws, f"B{R['s1_note']}", "Leverage fixed at 6.0x LTM EBITDA, exit at the end of Year 5, same operating case. The corner cell links to the IRR.", italic=True)
    put(ws, f"B{R['s1_corner']}", "Entry multiple (down), exit multiple (across)", bold=True)
    put(ws, f"D{R['s1_corner']}", f"=D{R['irr']}", kind="formula", fmt=FMT_PCT, bold=True, border_bottom=True)
    for c, ex in zip(PROJ_COLS, EXITS):
        put(ws, f"{c}{R['s1_corner']}", ex, kind="input", fmt=FMT_MULT, bold=True, border_bottom=True)
    g1 = grid_entry_exit()
    for i, en in enumerate(ENTRIES):
        row = R["s1_first"] + i
        put(ws, f"D{row}", en, kind="input", fmt=FMT_MULT, bold=True)
        for j, c in enumerate(PROJ_COLS):
            base = (en == A["entry_mult"] and EXITS[j] == A["exit_mult"])
            put(ws, f"{c}{row}", g1[i][j], kind="formula", fmt=FMT_PCT, bold=base, fill=FILL_SUBTLE if base else None)

    # sensitivity 2: leverage vs exit year
    header_bar(ws, R["s2_header"], 2, 9, "SENSITIVITY: IRR, LEVERAGE VS EXIT YEAR (data table)")
    put(ws, f"B{R['s2_note']}", "Entry and exit both at 10.0x. Debt splits 75% term loan and 25% notes at each level, financing fees scale with the debt.", italic=True)
    put(ws, f"B{R['s2_corner']}", "Leverage, x LTM EBITDA (down), exit year (across)", bold=True)
    put(ws, f"D{R['s2_corner']}", f"=D{R['irr']}", kind="formula", fmt=FMT_PCT, bold=True, border_bottom=True)
    for c, h in zip(PROJ_COLS, HOLDS):
        put(ws, f"{c}{R['s2_corner']}", h, kind="input", fmt=FMT_YEAR, bold=True, border_bottom=True)
    g2 = grid_lev_year()
    for i, lv in enumerate(LEVS):
        row = R["s2_first"] + i
        put(ws, f"D{row}", lv, kind="input", fmt=FMT_MULT, bold=True)
        for j, c in enumerate(PROJ_COLS):
            base = (lv == 6.0 and HOLDS[j] == A["exit_year"])
            put(ws, f"{c}{row}", g2[i][j], kind="formula", fmt=FMT_PCT, bold=base, fill=FILL_SUBTLE if base else None)

    # ================================================================ paper LBO sheet
    P = {}
    ps = wb.create_sheet("Paper LBO")
    set_widths(ps, {"A": 2, "B": 50, "C": 2, "D": 11, "E": 11, "F": 11, "G": 11, "H": 11})
    ps.sheet_view.showGridLines = False
    put(ps, "B2", "Paper LBO, the five-minute interview version", bold=True, size=12)
    put(ps, "B3", "$ in millions. Interest on the beginning balance, rounded to the nearest million; free cash flow to the nearest five.", italic=True)
    header_bar(ps, 5, 2, 8, "STEP 1: PURCHASE PRICE AND EQUITY CHECK")
    P["s1_header"] = 5
    left = [
        ("p_ebitda", "LTM EBITDA", 100.0, "input", FMT_INT_Z),
        ("p_growth", "EBITDA growth a year ($)", 10.0, "input", FMT_INT_Z),
        ("p_entry", "Entry multiple", 8.0, "input", FMT_MULT),
        ("p_ev", "Enterprise value (purchase price)", "=D{p_ebitda}*D{p_entry}", "formula", FMT_INT_Z),
        ("p_lev", "Debt (x EBITDA)", 5.0, "input", FMT_MULT),
        ("p_debt", "Debt", "=D{p_ebitda}*D{p_lev}", "formula", FMT_INT_Z),
        ("p_equity", "Equity check (price less debt)", "=D{p_ev}-D{p_debt}", "total", FMT_INT_Z),
    ]
    right = [
        ("p_rate", "Interest rate", 0.08, "input", '0%'),
        ("p_da", "D&A a year", 20.0, "input", FMT_INT_Z),
        ("p_capex", "Capex a year", 20.0, "input", FMT_INT_Z),
        ("p_tax", "Tax rate", 0.25, "input", '0%'),
        ("p_exit", "Exit multiple (after Year 5)", 8.0, "input", FMT_MULT),
    ]
    r = 6
    for name, _, _, _, _ in left:
        P[name] = r; r += 1
    for i, (name, _, _, _, _) in enumerate(right):
        P[name] = 6 + i
    for name, label, value, kind, fmt in left:
        put(ps, f"B{P[name]}", label, kind="total" if kind == "total" else "label")
        v = value.format(**P) if isinstance(value, str) else value
        put(ps, f"D{P[name]}", v, kind=kind, fmt=fmt)
    for name, label, value, kind, fmt in right:
        put(ps, f"F{P[name]}", label)
        put(ps, f"H{P[name]}", value, kind=kind, fmt=fmt)
    r = P["p_equity"] + 2

    header_bar(ps, r, 2, 8, "STEPS 2 AND 3: YEAR 1 CASH FLOW, THEN YEARS 2 TO 5 (rounded as you go)"); r += 1
    P["yr_hdr"] = r
    from openpyxl.styles import Alignment, Border, Side
    thin = Side(style="thin", color="000000")
    PC = ["D", "E", "F", "G", "H"]
    for i, c in enumerate(PC):
        cell = ps[f"{c}{r}"]
        cell.value = i + 1
        cell.number_format = FMT_YEAR
        cell.font = Font(name=XL_FONT, size=XL_SIZE, bold=True)
        cell.alignment = Alignment(horizontal="right")
        cell.border = Border(bottom=thin)
    r += 1
    names = ["pe", "pda", "pebit", "pdebt_beg", "pint", "pebt", "pni", "pfcf", "pdebt_end"]
    for n in names:
        P[n] = r; r += 1
    P["tbl_end"] = r - 1

    def prow(name, label, tmpl, kind="formula", fmt=FMT_NUM_Z, first=None, italic=False, per_cell_fmt=None):
        put(ps, f"B{P[name]}", label, kind="total" if kind == "total" else "label", italic=italic)
        for i, c in enumerate(PC):
            t = first if (i == 0 and first is not None) else tmpl
            v = t.format(c=c, p=PC[i - 1] if i else "C", **P)
            put(ps, f"{c}{P[name]}", v, kind=kind, fmt=(per_cell_fmt[i] if per_cell_fmt else fmt))

    prow("pe", "EBITDA (grows $10 a year)", "=$D${p_ebitda}+$D${p_growth}*{c}${yr_hdr}", fmt=FMT_INT_Z)
    prow("pda", "Less: D&A", "=-$H${p_da}", fmt=FMT_INT_Z)
    prow("pebit", "EBIT", "={c}{pe}+{c}{pda}", kind="total", fmt=FMT_INT_Z)
    prow("pdebt_beg", "Debt, beginning of year", "={p}{pdebt_end}", first="=$D${p_debt}", italic=True, fmt=FMT_INT_Z)
    prow("pint", "Less: Interest (8% of beginning debt, rounded)", "=-ROUND({c}{pdebt_beg}*$H${p_rate},0)", fmt=FMT_INT_Z)
    prow("pebt", "Pre-tax income", "={c}{pebit}+{c}{pint}", kind="total", fmt=FMT_INT_Z)
    prow("pni", "Net income (75% of pre-tax)", "={c}{pebt}*(1-$H${p_tax})",
         per_cell_fmt=[FMT_NUM_Z, '#,##0;(#,##0);0', '#,##0;(#,##0);0', '#,##0;(#,##0);0', '#,##0;(#,##0);0'])
    prow("pfcf", "Free cash flow (NI plus D&A less capex, rounded to nearest 5)",
         "=MROUND({c}{pni}-{c}{pda}-$H${p_capex},5)", fmt='#,##0;(#,##0);0')
    prow("pdebt_end", "Debt, end of year (all free cash flow pays down debt)", "={c}{pdebt_beg}-{c}{pfcf}", kind="total", fmt=FMT_INT_Z)
    r = P["tbl_end"] + 2

    header_bar(ps, r, 2, 8, "STEPS 4 AND 5: EXIT AND RETURNS"); r += 1
    P["ex_hdr"] = r
    put(ps, f"D{r}", "Out loud", bold=True, align="right", border_bottom=True)
    put(ps, f"E{r}", "Exact", bold=True, align="right", border_bottom=True)
    r += 1
    ex = ["x_ebitda", "x_mult", "x_ev", "x_debt", "x_equity", "x_in", "x_moic", "x_irr"]
    for n in ex:
        P[n] = r; r += 1
    P["ex_end"] = r - 1
    r += 1

    # exact block (unrounded) below, for the check the article quotes
    header_bar(ps, r, 2, 8, "EXACT VERSION, NO ROUNDING (the check behind the out-loud answer)"); r += 1
    P["q_hdr"] = r
    for i, c in enumerate(PC):
        cell = ps[f"{c}{r}"]
        cell.value = i + 1
        cell.number_format = FMT_YEAR
        cell.font = Font(name=XL_FONT, size=XL_SIZE, bold=True)
        cell.alignment = Alignment(horizontal="right")
        cell.border = Border(bottom=thin)
    r += 1
    for n in ["qe", "qebit", "qdebt_beg", "qint", "qebt", "qni", "qfcf", "qdebt_end"]:
        P[n] = r; r += 1
    prow("qe", "EBITDA", "=$D${p_ebitda}+$D${p_growth}*{c}${q_hdr}")
    prow("qebit", "EBIT (EBITDA less D&A)", "={c}{qe}-$H${p_da}")
    prow("qdebt_beg", "Debt, beginning of year", "={p}{qdebt_end}", first="=$D${p_debt}", italic=True)
    prow("qint", "Less: Interest (8% of beginning debt)", "=-{c}{qdebt_beg}*$H${p_rate}")
    prow("qebt", "Pre-tax income", "={c}{qebit}+{c}{qint}", kind="total")
    prow("qni", "Net income (75% of pre-tax)", "={c}{qebt}*(1-$H${p_tax})")
    prow("qfcf", "Free cash flow (net income plus D&A less capex)", "={c}{qni}+$H${p_da}-$H${p_capex}")
    prow("qdebt_end", "Debt, end of year", "={c}{qdebt_beg}-{c}{qfcf}", kind="total")

    # exit block, both columns
    put(ps, f"B{P['x_ebitda']}", "Year 5 EBITDA")
    put(ps, f"D{P['x_ebitda']}", f"=H{P['pe']}", kind="formula", fmt=FMT_INT_Z)
    put(ps, f"E{P['x_ebitda']}", f"=H{P['qe']}", kind="formula", fmt=FMT_INT_Z)
    put(ps, f"B{P['x_mult']}", "Exit multiple")
    put(ps, f"D{P['x_mult']}", f"=$H${P['p_exit']}", kind="formula", fmt=FMT_MULT)
    put(ps, f"E{P['x_mult']}", f"=$H${P['p_exit']}", kind="formula", fmt=FMT_MULT)
    put(ps, f"B{P['x_ev']}", "Exit enterprise value")
    put(ps, f"D{P['x_ev']}", f"=D{P['x_ebitda']}*D{P['x_mult']}", kind="formula", fmt=FMT_INT_Z)
    put(ps, f"E{P['x_ev']}", f"=E{P['x_ebitda']}*E{P['x_mult']}", kind="formula", fmt=FMT_INT_Z)
    put(ps, f"B{P['x_debt']}", "Less: Debt remaining after Year 5")
    put(ps, f"D{P['x_debt']}", f"=-H{P['pdebt_end']}", kind="formula", fmt=FMT_INT_Z)
    put(ps, f"E{P['x_debt']}", f"=-H{P['qdebt_end']}", kind="formula", fmt=FMT_NUM_Z)
    put(ps, f"B{P['x_equity']}", "Exit equity value", kind="total")
    put(ps, f"D{P['x_equity']}", f"=D{P['x_ev']}+D{P['x_debt']}", kind="total", fmt=FMT_INT_Z)
    put(ps, f"E{P['x_equity']}", f"=E{P['x_ev']}+E{P['x_debt']}", kind="total", fmt=FMT_NUM_Z)
    put(ps, f"B{P['x_in']}", "Equity check at entry")
    put(ps, f"D{P['x_in']}", f"=$D${P['p_equity']}", kind="formula", fmt=FMT_INT_Z)
    put(ps, f"E{P['x_in']}", f"=$D${P['p_equity']}", kind="formula", fmt=FMT_INT_Z)
    put(ps, f"B{P['x_moic']}", "MOIC", bold=True)
    put(ps, f"D{P['x_moic']}", f"=D{P['x_equity']}/D{P['x_in']}", kind="formula", fmt=FMT_MULT, bold=True)
    put(ps, f"E{P['x_moic']}", f"=E{P['x_equity']}/E{P['x_in']}", kind="formula", fmt=FMT_MULT2, bold=True)
    put(ps, f"B{P['x_irr']}", "IRR over 5 years (MOIC ^ (1/5) less 1)", bold=True)
    put(ps, f"D{P['x_irr']}", f"=D{P['x_moic']}^(1/5)-1", kind="formula", fmt=FMT_PCT, bold=True)
    put(ps, f"E{P['x_irr']}", f"=E{P['x_moic']}^(1/5)-1", kind="formula", fmt=FMT_PCT, bold=True)

    # iterative calculation on, so the Circ toggle and the Year 1 average-balance block calculate
    wb.calculation.iterate = True
    wb.calculation.iterateCount = 100
    wb.calculation.iterateDelta = 0.00001
    wb.calculation.fullCalcOnLoad = True

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out_path)
    return out_path, R, P


if __name__ == "__main__":
    path, R, P = build()
    print(f"wrote {path}")
    print("LBO rows:", {k: v for k, v in R.items()})
    print("Paper LBO rows:", {k: v for k, v in P.items()})
