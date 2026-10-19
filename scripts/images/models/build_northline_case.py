#!/usr/bin/env python3
"""Build scripts/images/models/northline-case.xlsx: the Northline Foods on-time delivery case from
"Deloitte Strategy & Operations Career Guide" (drafts/draft-deloitte-strategy-and-operations-career-guide-v1.md),
worked as a small sheet with live formulas.

Every input is a number the draft states (deliveries a week, on-time rates, $150 a late delivery,
40 trucks at 50 deliveries a week, loading minutes, 30 minutes a stop, the two levers and their costs).
Everything else is a formula, so the screenshots show how the case's numbers tie. One sheet, four blocks:

  Step two     the cost of late deliveries, last year against this year (the draft's first table)
  Step three   fleet capacity, utilization and the deliveries lost to the longer loading time
  Step four    the two levers and the capacity they recover (the draft's second table)
  Payback      late deliveries at 96 percent on time, the annual saving, net of the trucks and the one-time fix

Run from the repo root:  python3 scripts/images/models/build_northline_case.py
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import (XL_FONT, XL_SIZE, header_bar, new_workbook, put, set_widths)  # noqa: E402

OUT_XLSX = ROOT / "scripts" / "images" / "models" / "northline-case.xlsx"
FMT_INT = '#,##0;(#,##0);"-"'
FMT_USD = '"$"#,##0;("$"#,##0);"-"'
FMT_PCT0 = '0%'
FMT_PCT1 = '0.0%'
FMT_MIN = '0" min"'


def note(ws, ref, text):
    put(ws, ref, text, italic=True, color="52514E", size=9)


def col_headers(ws, row, items):
    from openpyxl.styles import Alignment, Border, Font, Side
    thin = Side(style="thin", color="000000")
    for col, text in items.items():
        c = ws[f"{col}{row}"]
        c.value = text
        c.font = Font(name=XL_FONT, size=XL_SIZE, bold=True)
        c.alignment = Alignment(horizontal="right", wrap_text=True)
        c.border = Border(bottom=thin)


def build():
    wb = new_workbook()
    wb.properties.creator = "Wall Street Guide"
    wb.properties.lastModifiedBy = "Wall Street Guide"
    ws = wb.active
    ws.title = "Northline case"
    set_widths(ws, {"A": 2, "B": 46, "C": 2, "D": 15, "E": 15, "F": 15})
    ws.sheet_view.showGridLines = False
    R = {}

    put(ws, "B2", "Northline Foods, on-time delivery case", bold=True, size=12)
    note(ws, "B3", "Blue cells on yellow are the numbers the interviewer gives you; black cells are formulas.")

    # Step two: size the problem ---------------------------------------------------------
    R["s2_header"] = 5
    header_bar(ws, 5, 2, 6, "Step two: the cost of late deliveries")
    col_headers(ws, 6, {"D": "Last year", "E": "This year"})
    put(ws, "B7", "Deliveries a week")
    put(ws, "D7", 1750, kind="input", fmt=FMT_INT)
    put(ws, "E7", 2000, kind="input", fmt=FMT_INT)
    put(ws, "B8", "On-time rate")
    put(ws, "D8", 0.96, kind="input", fmt=FMT_PCT0)
    put(ws, "E8", 0.88, kind="input", fmt=FMT_PCT0)
    put(ws, "B9", "Late deliveries a week", indent=1)
    put(ws, "D9", "=D7*(1-D8)", kind="formula", fmt=FMT_INT)
    put(ws, "E9", "=E7*(1-E8)", kind="formula", fmt=FMT_INT)
    put(ws, "B10", "Cost per late delivery (credits, redelivery, spoilage)")
    put(ws, "D10", 150, kind="input", fmt=FMT_USD)
    put(ws, "E10", 150, kind="input", fmt=FMT_USD)
    put(ws, "B11", "Weekly cost of late deliveries", indent=1)
    put(ws, "D11", "=D9*D10", kind="formula", fmt=FMT_USD)
    put(ws, "E11", "=E9*E10", kind="formula", fmt=FMT_USD)
    put(ws, "B12", "Weeks a year")
    put(ws, "D12", 52, kind="input", fmt=FMT_INT)
    put(ws, "E12", 52, kind="input", fmt=FMT_INT)
    put(ws, "B13", "Annual cost of late deliveries", kind="total")
    put(ws, "D13", "=D11*D12", kind="total", fmt=FMT_USD)
    put(ws, "E13", "=E11*E12", kind="total", fmt=FMT_USD)
    put(ws, "B14", "Increase in the annual cost (the number the CFO remembers)", italic=True)
    put(ws, "E14", "=E13-D13", kind="formula", fmt=FMT_USD)
    R["s2_end"] = 14

    # Step three: capacity ------------------------------------------------------------------
    R["s3_header"] = 16
    header_bar(ws, 16, 2, 6, "Step three: capacity and the loading problem")
    col_headers(ws, 17, {"D": "Last year", "E": "This year"})
    put(ws, "B18", "Trucks")
    put(ws, "D18", 40, kind="input", fmt=FMT_INT)
    put(ws, "E18", 40, kind="input", fmt=FMT_INT)
    put(ws, "B19", "Deliveries each truck can handle a week")
    put(ws, "D19", 50, kind="input", fmt=FMT_INT)
    put(ws, "E19", 50, kind="input", fmt=FMT_INT)
    put(ws, "B20", "Fleet capacity (deliveries a week)", indent=1)
    put(ws, "D20", "=D18*D19", kind="formula", fmt=FMT_INT)
    put(ws, "E20", "=E18*E19", kind="formula", fmt=FMT_INT)
    put(ws, "B21", "Utilization (demand over capacity)", indent=1)
    put(ws, "D21", "=D7/D20", kind="formula", fmt=FMT_PCT1)
    put(ws, "E21", "=E7/E20", kind="formula", fmt=FMT_PCT1)
    put(ws, "B22", "Loading time per truck per day (minutes)")
    put(ws, "D22", 40, kind="input", fmt=FMT_MIN)
    put(ws, "E22", 55, kind="input", fmt=FMT_MIN)
    put(ws, "B23", "Extra loading minutes per truck per day", indent=1)
    put(ws, "E23", "=E22-D22", kind="formula", fmt=FMT_MIN)
    put(ws, "B24", "Loading days a week")
    put(ws, "E24", 5, kind="input", fmt=FMT_INT)
    put(ws, "B25", "Truck-hours a week lost to loading", indent=1)
    put(ws, "E25", "=E23*E24*E18/60", kind="formula", fmt=FMT_INT)
    put(ws, "B26", "Minutes per delivery stop")
    put(ws, "E26", 30, kind="input", fmt=FMT_MIN)
    put(ws, "B27", "Deliveries a week lost to loading", indent=1)
    put(ws, "E27", "=E25*60/E26", kind="formula", fmt=FMT_INT)
    put(ws, "B28", "Effective capacity this year (deliveries a week)", kind="total")
    put(ws, "E28", "=E20-E27", kind="total", fmt=FMT_INT)
    put(ws, "B29", "Demand this year, for comparison", italic=True)
    put(ws, "E29", "=E7", kind="formula", fmt=FMT_INT)
    R["s3_end"] = 29

    # Step four: the levers -----------------------------------------------------------------
    R["s4_header"] = 31
    header_bar(ws, 31, 2, 6, "Step four: two levers, cheapest first")
    col_headers(ws, 32, {"D": "Deliveries a week", "E": "One-time cost", "F": "Annual cost"})
    put(ws, "B33", "Re-slot the chilled pick, stage pallets the night before")
    put(ws, "D33", "=E27", kind="formula", fmt=FMT_INT)
    put(ws, "E33", 120000, kind="input", fmt=FMT_USD)
    put(ws, "F33", 0, kind="input", fmt=FMT_USD)
    put(ws, "B34", "Lease three trucks with drivers")
    put(ws, "D34", "=D35*D19", kind="formula", fmt=FMT_INT)
    put(ws, "E34", 0, kind="input", fmt=FMT_USD)
    put(ws, "F34", "=D35*D36", kind="formula", fmt=FMT_USD)
    put(ws, "B35", "Trucks leased", indent=1)
    put(ws, "D35", 3, kind="input", fmt=FMT_INT)
    put(ws, "B36", "Lease cost per truck with driver, a year", indent=1)
    put(ws, "D36", 150000, kind="input", fmt=FMT_USD)
    put(ws, "B37", "Combined", kind="total")
    put(ws, "D37", "=D33+D34", kind="total", fmt=FMT_INT)
    put(ws, "E37", "=E33+E34", kind="total", fmt=FMT_USD)
    put(ws, "F37", "=F33+F34", kind="total", fmt=FMT_USD)
    put(ws, "B38", "Capacity after both levers (deliveries a week)", indent=1)
    put(ws, "D38", "=E28+D37", kind="formula", fmt=FMT_INT)
    put(ws, "B39", "Utilization after both levers", indent=1)
    put(ws, "D39", "=E7/D38", kind="formula", fmt=FMT_PCT1)
    R["s4_end"] = 39

    # The payback ---------------------------------------------------------------------------
    R["pb_header"] = 41
    header_bar(ws, 41, 2, 6, "The payback if on-time delivery returns to 96 percent")
    put(ws, "B42", "Target on-time rate")
    put(ws, "D42", 0.96, kind="input", fmt=FMT_PCT0)
    put(ws, "B43", "Late deliveries a week at the target", indent=1)
    put(ws, "D43", "=E7*(1-D42)", kind="formula", fmt=FMT_INT)
    put(ws, "B44", "Annual cost of lateness at the target", indent=1)
    put(ws, "D44", "=D43*E10*E12", kind="formula", fmt=FMT_USD)
    put(ws, "B45", "Annual saving against today", kind="total")
    put(ws, "D45", "=E13-D44", kind="total", fmt=FMT_USD)
    put(ws, "B46", "Less: annual truck leases", indent=1)
    put(ws, "D46", "=-F37", kind="formula", fmt=FMT_USD)
    put(ws, "B47", "Net annual saving, the company keeps", kind="total")
    put(ws, "D47", "=D45+D46", kind="total", fmt=FMT_USD)
    put(ws, "B48", "Less: one-time loading fix", indent=1)
    put(ws, "D48", "=-E37", kind="formula", fmt=FMT_USD)
    put(ws, "B49", "Year one net saving", kind="total")
    put(ws, "D49", "=D47+D48", kind="total", fmt=FMT_USD)
    R["pb_end"] = 49

    OUT_XLSX.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUT_XLSX)
    return OUT_XLSX, R


if __name__ == "__main__":
    path, _ = build()
    print(f"wrote {path.relative_to(ROOT)}")
