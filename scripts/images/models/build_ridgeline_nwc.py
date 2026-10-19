#!/usr/bin/env python3
"""Build scripts/images/models/ridgeline-nwc.xlsx: the Ridgeline Outdoor Co. working capital
workbook behind the screenshots in "Net Working Capital: How to Explain It in an Interview".

Every number comes from the article's own tables (drafts/draft-net-working-capital-interview-v1.md).
Hardcodes are blue on pale yellow, everything else is a live formula, so the screenshots show
how the cells connect. Three sheets:

  NWC schedule        drivers, the Year 1 to Year 2 change table (section 3), DSO / DIO / DPO and
                      the cash conversion cycle (section 8), the days-based Year 3 projection
                      (section 10), and the Year 2 cash flow walk to unlevered free cash flow
                      (sections 4 and 5)
  Inventory walk      the "$10 of inventory, then sold for $15" three-statement walk (section 12)
  Working capital peg the $500 million sale with a $50 million peg (section 7)

Run from the repo root:  python3 scripts/images/models/build_ridgeline_nwc.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import (FMT_NUM, FMT_PCT, XL_FONT, XL_SIZE, header_bar, new_workbook, put,  # noqa: E402
                     set_widths, year_header)

OUT = ROOT / "scripts" / "images" / "models" / "ridgeline-nwc.xlsx"
FMT_DAYS = '0.0;(0.0);"-"'
FMT_DAYS_INT = '0;(0);"-"'
FMT_NUM2 = '#,##0.00;(#,##0.00);"-"'


def note(ws, ref, text):
    put(ws, ref, text, italic=True, color="52514E", size=9)


def title(ws, ref, text):
    put(ws, ref, text, bold=True, size=12)


def col_headers(ws, row, items, bold=True):
    """items: {"D": "Year 1", ...}; bottom border like year_header."""
    from openpyxl.styles import Alignment, Border, Font, Side
    thin = Side(style="thin", color="000000")
    for col, text in items.items():
        c = ws[f"{col}{row}"]
        c.value = text
        c.font = Font(name=XL_FONT, size=XL_SIZE, bold=bold)
        c.alignment = Alignment(horizontal="right", wrap_text=True)
        c.border = Border(bottom=thin)


def left(ws, ref):
    from openpyxl.styles import Alignment
    ws[ref].alignment = Alignment(horizontal="left")


def formula_label(ws, ref, text):
    """The formula written out as literal text in an adjacent cell, so the screenshot shows it."""
    c = put(ws, ref, " " + text, italic=True, color="52514E", align="left")
    c.data_type = "s"   # keep the leading "=" as text, not a live formula
    return c


# ------------------------------------------------------------------ sheet 1: NWC schedule
def build_schedule(wb):
    ws = wb.active
    ws.title = "NWC schedule"
    set_widths(ws, {"A": 2, "B": 50, "C": 2, "D": 12, "E": 12, "F": 12, "G": 16})
    ws.sheet_view.showGridLines = False

    title(ws, "B2", "Ridgeline Outdoor Co., net working capital model")
    note(ws, "B3", "$ millions. Blue cells on yellow are inputs from the article; black cells are formulas.")

    # Drivers -------------------------------------------------------------
    header_bar(ws, 5, 2, 7, "Drivers")
    year_header(ws, 6, 4, ["Year 1A", "Year 2A", "Year 3P"])
    put(ws, "B7", "Revenue")
    put(ws, "B8", "Cost of goods sold")
    put(ws, "B9", "Revenue growth")
    for col, rev, cogs in (("D", 1000, 600), ("E", 1050, 630), ("F", 1100, 660)):
        put(ws, f"{col}7", rev, kind="input", fmt=FMT_NUM)
        put(ws, f"{col}8", cogs, kind="input", fmt=FMT_NUM)
    put(ws, "E9", "=E7/D7-1", kind="formula", fmt=FMT_PCT)
    put(ws, "F9", "=F7/E7-1", kind="formula", fmt=FMT_PCT)

    # Change in NWC, Year 1 to Year 2 (article section 3 table) -----------
    header_bar(ws, 11, 2, 7, "Change in net working capital, Year 1 to Year 2")
    col_headers(ws, 12, {"D": "Year 1", "E": "Year 2", "F": "Change", "G": "Cash effect"})
    assets = [("Accounts receivable", 80, 95), ("Inventory", 120, 130), ("Prepaid expenses", 10, 10)]
    liabs = [("Accounts payable", 70, 75), ("Accrued expenses", 30, 30), ("Deferred revenue", 20, 20)]
    r = 13
    for name, y1, y2 in assets:
        put(ws, f"B{r}", name, indent=1)
        put(ws, f"D{r}", y1, kind="input", fmt=FMT_NUM)
        put(ws, f"E{r}", y2, kind="input", fmt=FMT_NUM)
        put(ws, f"F{r}", f"=E{r}-D{r}", kind="formula", fmt=FMT_NUM)
        put(ws, f"G{r}", f"=-F{r}", kind="formula", fmt=FMT_NUM)   # an asset going up uses cash
        r += 1
    put(ws, "B16", "Operating current assets", kind="total")
    for col in "DE":
        put(ws, f"{col}16", f"=SUM({col}13:{col}15)", kind="total", fmt=FMT_NUM)
    put(ws, "F16", "=E16-D16", kind="total", fmt=FMT_NUM)
    put(ws, "G16", "=-F16", kind="total", fmt=FMT_NUM)
    r = 17
    for name, y1, y2 in liabs:
        put(ws, f"B{r}", name, indent=1)
        put(ws, f"D{r}", y1, kind="input", fmt=FMT_NUM)
        put(ws, f"E{r}", y2, kind="input", fmt=FMT_NUM)
        put(ws, f"F{r}", f"=E{r}-D{r}", kind="formula", fmt=FMT_NUM)
        put(ws, f"G{r}", f"=F{r}", kind="formula", fmt=FMT_NUM)    # a liability going up frees cash
        r += 1
    put(ws, "B20", "Operating current liabilities", kind="total")
    for col in "DE":
        put(ws, f"{col}20", f"=SUM({col}17:{col}19)", kind="total", fmt=FMT_NUM)
    put(ws, "F20", "=E20-D20", kind="total", fmt=FMT_NUM)
    put(ws, "G20", "=F20", kind="total", fmt=FMT_NUM)
    put(ws, "B21", "Net working capital", kind="total")
    for col in "DE":
        put(ws, f"{col}21", f"={col}16-{col}20", kind="total", fmt=FMT_NUM)
    put(ws, "F21", "=E21-D21", kind="total", fmt=FMT_NUM)
    put(ws, "G21", "=-F21", kind="total", fmt=FMT_NUM)
    note(ws, "B22", "Parentheses mean cash going out: an asset going up uses cash, a liability going up frees it.")

    # Days and the Year 3 projection (sections 8 and 10) ------------------
    header_bar(ws, 24, 2, 7, "Cash conversion cycle, then the Year 3 projection from days")
    col_headers(ws, 25, {"D": "Year 1A", "E": "Year 2A", "F": "Year 3P", "G": "Formula (Year 2)"})
    left(ws, "G25")
    days = [
        (26, "Days sales outstanding, DSO (receivables / revenue x 365)", "{c}13/{c}7*365", 33),
        (27, "Days inventory outstanding, DIO (inventory / COGS x 365)", "{c}14/{c}8*365", 75),
        (28, "Days payable outstanding, DPO (payables / COGS x 365)", "{c}17/{c}8*365", 44),
    ]
    for row, label, expr, y3 in days:
        put(ws, f"B{row}", label, indent=1)
        for col in "DE":
            put(ws, f"{col}{row}", "=" + expr.format(c=col), kind="formula", fmt=FMT_DAYS)
        put(ws, f"F{row}", y3, kind="input", fmt=FMT_DAYS_INT)       # rounded whole days held flat
        formula_label(ws, f"G{row}", "=" + expr.format(c="E"))
    put(ws, "B29", "Cash conversion cycle (DSO plus DIO less DPO)", kind="total")
    for col in "DE":
        put(ws, f"{col}29", f"={col}26+{col}27-{col}28", kind="total", fmt=FMT_DAYS)
    put(ws, "F29", "=F26+F27-F28", kind="total", fmt=FMT_DAYS_INT)
    formula_label(ws, "G29", "=E26+E27-E28")
    pcts = [(30, "Prepaid expenses, % of revenue", "{c}15/{c}7"),
            (31, "Accrued expenses, % of revenue", "{c}18/{c}7"),
            (32, "Deferred revenue, % of revenue", "{c}19/{c}7")]
    for row, label, expr in pcts:
        put(ws, f"B{row}", label, indent=1)
        for col in "DE":
            put(ws, f"{col}{row}", "=" + expr.format(c=col), kind="formula", fmt=FMT_PCT)
        put(ws, f"F{row}", f"=E{row}", kind="formula", fmt=FMT_PCT)   # held at the Year 2 percent
        formula_label(ws, f"G{row}", "=" + expr.format(c="E"))
    note(ws, "B33", "Year 3 days are the Year 2 days rounded to whole days and held flat; the small items hold their Year 2 percent of revenue.")

    col_headers(ws, 34, {"D": "Year 1A", "E": "Year 2A", "F": "Year 3P", "G": "Formula (Year 3)"})
    left(ws, "G34")
    proj = [
        (35, "Accounts receivable", 13, "=F26/365*F7"),
        (36, "Inventory", 14, "=F27/365*F8"),
        (37, "Prepaid expenses", 15, "=F30*F7"),
        (38, "Accounts payable", 17, "=F28/365*F8"),
        (39, "Accrued expenses", 18, "=F31*F7"),
        (40, "Deferred revenue", 19, "=F32*F7"),
    ]
    for row, label, src, f3 in proj:
        put(ws, f"B{row}", label, indent=1)
        put(ws, f"D{row}", f"=D{src}", kind="formula", fmt=FMT_NUM)
        put(ws, f"E{row}", f"=E{src}", kind="formula", fmt=FMT_NUM)
        put(ws, f"F{row}", f3, kind="formula", fmt=FMT_NUM)
        formula_label(ws, f"G{row}", f3)
    put(ws, "B41", "Net working capital", kind="total")
    for col in "DEF":
        put(ws, f"{col}41", f"={col}35+{col}36+{col}37-{col}38-{col}39-{col}40", kind="total", fmt=FMT_NUM)
    put(ws, "B42", "Increase in net working capital (a use of cash)", kind="total")
    put(ws, "E42", "=E41-D41", kind="total", fmt=FMT_NUM)
    put(ws, "F42", "=F41-E41", kind="total", fmt=FMT_NUM)
    formula_label(ws, "G42", "=F41-E41")

    # Year 2 cash flow walk (sections 4 and 5) -----------------------------
    header_bar(ws, 44, 2, 7, "Year 2 cash flow: net income to cash from operations, EBIT to unlevered free cash flow")
    col_headers(ws, 45, {"E": "Year 2"})
    inputs = [(46, "EBIT", 100, FMT_NUM), (47, "Depreciation and amortization (inside EBIT)", 20, FMT_NUM),
              (48, "Interest expense", 20, FMT_NUM), (49, "Tax rate", 0.25, FMT_PCT),
              (50, "Capital expenditures", 25, FMT_NUM)]
    for row, label, val, fmt in inputs:
        put(ws, f"B{row}", label, indent=1)
        put(ws, f"E{row}", val, kind="input", fmt=fmt)
    rows = [
        (52, "Pre-tax income", "=E46-E48", "formula"),
        (53, "Less: taxes", "=-E52*E49", "formula"),
        (54, "Net income", "=E52+E53", "total"),
        (55, "Plus: depreciation and amortization", "=E47", "formula"),
        (56, "Less: increase in net working capital", "=-E42", "formula"),
        (57, "Cash flow from operations", "=SUM(E54:E56)", "total"),
        (59, "EBIT", "=E46", "formula"),
        (60, "Less: taxes at 25 percent", "=-E59*E49", "formula"),
        (61, "Net operating profit after tax", "=E59+E60", "total"),
        (62, "Plus: depreciation and amortization", "=E47", "formula"),
        (63, "Less: capital expenditures", "=-E50", "formula"),
        (64, "Less: increase in net working capital", "=-E42", "formula"),
        (65, "Unlevered free cash flow", "=SUM(E61:E64)", "total"),
    ]
    for row, label, f, kind in rows:
        put(ws, f"B{row}", label, kind=kind if kind == "total" else "label", indent=0 if kind == "total" else 1)
        put(ws, f"E{row}", f, kind=kind, fmt=FMT_NUM)
    return ws


# ------------------------------------------------------------------ sheet 2: inventory walk
def build_inventory_walk(wb):
    ws = wb.create_sheet("Inventory walk")
    set_widths(ws, {"A": 2, "B": 52, "C": 2, "D": 15, "E": 15, "F": 15})
    ws.sheet_view.showGridLines = False
    title(ws, "B2", "Inventory bought for cash, then sold: the three-statement walk")
    note(ws, "B3", "$. Blue cells are inputs; every other cell is a formula. Balance sheet lines are changes from the start.")

    header_bar(ws, 5, 2, 6, "Assumptions")
    put(ws, "B6", "Inventory bought for cash", indent=1)
    put(ws, "D6", 10, kind="input", fmt=FMT_NUM2)
    put(ws, "B7", "Sale price", indent=1)
    put(ws, "D7", 15, kind="input", fmt=FMT_NUM2)
    put(ws, "B8", "Tax rate", indent=1)
    put(ws, "D8", 0.25, kind="input", fmt=FMT_PCT)

    header_bar(ws, 10, 2, 6, "Income statement")
    col_headers(ws, 11, {"D": "Step 1: buy it", "E": "Step 2: sell it", "F": "Both steps"})
    put(ws, "B12", "Revenue", indent=1)
    put(ws, "D12", 0, kind="formula", fmt=FMT_NUM2)
    put(ws, "E12", "=D7", kind="formula", fmt=FMT_NUM2)
    put(ws, "B13", "Cost of goods sold", indent=1)
    put(ws, "D13", 0, kind="formula", fmt=FMT_NUM2)
    put(ws, "E13", "=-D6", kind="formula", fmt=FMT_NUM2)
    put(ws, "B14", "Pre-tax income", indent=1)
    put(ws, "B15", "Less: taxes", indent=1)
    put(ws, "B16", "Net income", kind="total")
    for col in "DE":
        put(ws, f"{col}14", f"={col}12+{col}13", kind="formula", fmt=FMT_NUM2)
        put(ws, f"{col}15", f"=-{col}14*$D$8", kind="formula", fmt=FMT_NUM2)
        put(ws, f"{col}16", f"={col}14+{col}15", kind="total", fmt=FMT_NUM2)
    for row in (12, 13, 14, 15):
        put(ws, f"F{row}", f"=D{row}+E{row}", kind="formula", fmt=FMT_NUM2)
    put(ws, "F16", "=D16+E16", kind="total", fmt=FMT_NUM2)

    header_bar(ws, 18, 2, 6, "Cash flow statement")
    put(ws, "B19", "Net income", indent=1)
    put(ws, "B20", "Less: increase in inventory (an asset going up uses cash)", indent=1)
    put(ws, "B21", "Cash from operations", kind="total")
    put(ws, "B22", "Net change in cash", kind="total")
    for col in "DEF":
        put(ws, f"{col}19", f"={col}16", kind="formula", fmt=FMT_NUM2)
        put(ws, f"{col}20", f"=-{col}26", kind="formula", fmt=FMT_NUM2)
        put(ws, f"{col}21", f"={col}19+{col}20", kind="total", fmt=FMT_NUM2)
        put(ws, f"{col}22", f"={col}21", kind="total", fmt=FMT_NUM2)

    header_bar(ws, 24, 2, 6, "Balance sheet (change from the starting position)")
    put(ws, "B25", "Cash", indent=1)
    put(ws, "B26", "Inventory", indent=1)
    put(ws, "B27", "Total assets", kind="total")
    put(ws, "B28", "Retained earnings (net income)", indent=1)
    put(ws, "B29", "Total liabilities and equity", kind="total")
    put(ws, "B30", "Balance check (assets less liabilities and equity)", indent=1)
    put(ws, "D26", "=D6", kind="formula", fmt=FMT_NUM2)
    put(ws, "E26", "=-D6", kind="formula", fmt=FMT_NUM2)
    put(ws, "F26", "=D26+E26", kind="formula", fmt=FMT_NUM2)
    for col in "DEF":
        put(ws, f"{col}25", f"={col}22", kind="formula", fmt=FMT_NUM2)
        put(ws, f"{col}27", f"={col}25+{col}26", kind="total", fmt=FMT_NUM2)
        put(ws, f"{col}28", f"={col}16", kind="formula", fmt=FMT_NUM2)
        put(ws, f"{col}29", f"={col}28", kind="total", fmt=FMT_NUM2)
        put(ws, f"{col}30", f"={col}27-{col}29", kind="formula", fmt="0.00")
    return ws


# ------------------------------------------------------------------ sheet 3: working capital peg
def build_peg(wb):
    ws = wb.create_sheet("Working capital peg")
    set_widths(ws, {"A": 2, "B": 50, "C": 2, "D": 14, "E": 14, "F": 14, "G": 2, "H": 20})
    ws.sheet_view.showGridLines = False
    title(ws, "B2", "Working capital peg: how closing net working capital moves the price")
    note(ws, "B3", "$ millions. Blue cells are inputs; the adjustment and final price are formulas.")

    header_bar(ws, 5, 2, 8, "Deal terms")
    put(ws, "B6", "Headline price (cash-free, debt-free)", indent=1)
    put(ws, "D6", 500, kind="input", fmt=FMT_NUM)
    put(ws, "B7", "Working capital peg (trailing twelve-month average NWC)", indent=1)
    put(ws, "D7", 50, kind="input", fmt=FMT_NUM)

    header_bar(ws, 9, 2, 8, "Closing adjustment, dollar for dollar against the peg")
    col_headers(ws, 10, {"D": "Closing NWC", "E": "Versus peg", "F": "Final price", "H": "Formula (final price)"})
    left(ws, "H10")
    cases = [(11, "Seller delivers less working capital than normal", 45),
             (12, "Seller delivers the peg", 50),
             (13, "Seller delivers more working capital than normal", 58)]
    for row, label, closing in cases:
        put(ws, f"B{row}", label, indent=1)
        put(ws, f"D{row}", closing, kind="input", fmt=FMT_NUM)
        put(ws, f"E{row}", f"=D{row}-$D$7", kind="formula", fmt=FMT_NUM)
        put(ws, f"F{row}", f"=$D$6+E{row}", kind="formula", fmt=FMT_NUM)
        formula_label(ws, f"H{row}", f"=$D$6+E{row}")
    return ws


def build(out=OUT):
    wb = new_workbook()
    wb.properties.creator = "Wall Street Guide"
    wb.properties.lastModifiedBy = "Wall Street Guide"
    build_schedule(wb)
    build_inventory_walk(wb)
    build_peg(wb)
    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)
    return out


if __name__ == "__main__":
    print(build())
