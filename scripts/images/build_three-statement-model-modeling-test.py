#!/usr/bin/env python3
"""Images for "Three Statement Model: How to Build One for a Modeling Test" (WSG, October 1, 2026).

Run from the repo root:  python3 scripts/images/build_three-statement-model-modeling-test.py

1. Rebuilds scripts/images/models/three-statement-test.xlsx (live formulas) and asserts the
   LibreOffice recalculated values against every table in section 9 of the article.
2. Renders the Excel screenshots (drivers, income statement, balance sheet, cash flow statement,
   schedules, revolver block, check row, toggle, formula close-up, two error pattern sheets).
3. Draws two charts from the article's own numbers (the 2026 cash waterfall, the check row patterns).
4. Writes published/assets/images/three-statement-model-modeling-test/manifest.json.

Idempotent: every output is overwritten in place.
"""
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
sys.path.insert(0, str(ROOT / "scripts" / "images" / "models"))
from wsg_viz import *  # noqa: E402,F401
import build_three_statement as model  # noqa: E402

SLUG = "three-statement-model-modeling-test"
OUT = ROOT / "published" / "assets" / "images" / SLUG
XLSX = model.OUT
R = model.R

entries = []


def add(file, alt, caption, method, anchor):
    assert "\u2014" not in alt + caption + method and "\u2013" not in alt + caption + method, "no dashes"
    entries.append({"file": file, "alt": alt, "caption": caption, "method": method, "anchor": anchor[:60]})


def cap_width(path, max_w=2200):
    """The brief caps PNGs at 2200 px wide; matplotlib's tight bbox can overshoot by a little."""
    from PIL import Image
    im = Image.open(path)
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
        im.save(path, "PNG", optimize=True)
    return path


def render(sheet, cell_range, name, hidden_rows=()):
    """render_range, optionally on a temp copy with some rows hidden (so a close-up can show
    the rows that matter without the ones in between)."""
    out = OUT / name
    if not hidden_rows:
        return render_range(str(XLSX), sheet, cell_range, str(out))
    from openpyxl import load_workbook
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "hidden.xlsx"
        wb = load_workbook(XLSX)
        ws = wb[sheet]
        for r in hidden_rows:
            ws.row_dimensions[r].hidden = True
        wb.save(tmp)
        return render_range(str(tmp), sheet, cell_range, str(out))


# ---------------------------------------------------------------- charts
def chart_waterfall():
    """2026 cash flow waterfall from the article's cash flow statement and balance sheet tables."""
    import matplotlib.pyplot as plt
    steps = [  # (label, value, kind) kind: total | flow
        ("Net\nincome", 83.7, "total"),
        ("D&A", 44.0, "flow"),
        ("Higher\nreceivables", -10.6, "flow"),
        ("Higher\ninventory", -8.5, "flow"),
        ("Higher\npayables", 4.2, "flow"),
        ("Cash from\noperations", 112.8, "total"),
        ("Capex", -55.0, "flow"),
        ("Term loan\namortization", -30.0, "flow"),
        ("Dividends", -20.9, "flow"),
        ("Net change\nin cash", 6.9, "total"),
        ("Beginning\ncash", 80.0, "flow"),
        ("Ending\ncash", 86.9, "total"),
    ]
    # arithmetic check against the article: flows must land on each total
    run = 0.0
    for label, v, kind in steps:
        if kind == "total":
            assert abs(run - v) < 0.051 or label == "Net\nincome", (label, run, v)
            run = v
        else:
            run += v
    GRAY = "#8a8984"
    fig, ax = new_figure(width=11.5, height=6.4)
    fig.subplots_adjust(left=0.06, right=0.995, top=0.9, bottom=0.2)
    bottoms, heights, colors = [], [], []
    run = 0.0
    for label, v, kind in steps:
        if kind == "total":
            bottoms.append(0.0); heights.append(v); colors.append(GRAY); run = v
        else:
            bottoms.append(run if v >= 0 else run + v); heights.append(abs(v)); colors.append(BLUE if v >= 0 else ORANGE)
            run += v
    x = list(range(len(steps)))
    bars = ax.bar(x, heights, bottom=bottoms, color=colors, width=0.62, linewidth=0)
    # connectors between consecutive bars (hairline, recessive)
    run = 0.0
    for i, (label, v, kind) in enumerate(steps[:-1]):
        run = v if kind == "total" else run + v
        ax.plot([i + 0.31, i + 0.69], [run, run], color=GRID, linewidth=1.0, zorder=1)
    # value labels: every step is a line the reader re-adds from the article, so each gets its figure
    for i, (label, v, kind) in enumerate(steps):
        top = bottoms[i] + heights[i]
        text = f"{v:,.1f}" if kind == "total" else (f"+{v:,.1f}" if v >= 0 else f"{v:,.1f}")
        ax.annotate(text, (i, top), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom",
                    fontsize=11.5, color=TEXT_PRIMARY, fontweight="bold" if kind == "total" else "normal")
    ax.set_xticks(x)
    ax.set_xticklabels([s[0] for s in steps], fontsize=10)
    ax.set_xlim(-0.55, len(steps) - 0.45)
    ax.set_ylim(0, 140)
    style_axes(ax, title="Net income of 83.7 becomes only 6.9 of new cash in 2026", ylabel="$ millions")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=BLUE, label="Adds cash"), Patch(color=ORANGE, label="Uses cash"),
                       Patch(color=GRAY, label="Subtotal")], loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=3)
    ax.text(0.0, -0.26, "Revolver draw and repayment are both zero in 2026. The working capital bars are the year over year increases.",
            transform=ax.transAxes, fontsize=10.5, color=TEXT_MUTED, ha="left", va="top")
    return cap_width(save_figure(fig, OUT / "12-cash-waterfall-2026.png"))


def chart_check_patterns():
    """The two check row patterns from section 6: constant 12.0 and growing 44.0, 91.5, 141.9."""
    years = ["2026E", "2027E", "2028E"]
    constant = [12.0, 12.0, 12.0]
    growing = [44.0, 91.5, 141.9]
    fig, ax = new_figure(height=5.8)
    kw = dict(marker="o", markersize=9, markeredgecolor=SURFACE, markeredgewidth=2, linewidth=2.4)
    ax.plot(years, growing, color=ORANGE, label="Growing gap: a recurring link missing or wrong sign", **kw)
    ax.plot(years, constant, color=BLUE, label="Constant gap: a one time break, usually in year one", **kw)
    for xi, v in zip(years, growing):
        ax.annotate(f"{v:,.1f}", (xi, v), xytext=(0, 10), textcoords="offset points", ha="center", fontsize=12,
                    color=TEXT_PRIMARY)
    ax.annotate("44.0 is 2026 D&A exactly, so D&A is the missing link", ("2026E", 44.0), xytext=(14, -22),
                textcoords="offset points", ha="left", fontsize=11, color=TEXT_SECONDARY)
    ax.annotate("12.0", ("2028E", 12.0), xytext=(0, 10), textcoords="offset points", ha="center", fontsize=12,
                color=TEXT_PRIMARY)
    ax.set_ylim(0, 165)
    ax.set_xlim(-0.25, 2.25)
    style_axes(ax, title="A flat gap is a one time break, a rising gap is a missing recurring link",
               ylabel="Balance check, $ millions")
    ax.legend(loc="upper left")
    return cap_width(save_figure(fig, OUT / "06-check-patterns.png"))


# ---------------------------------------------------------------- main
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    print("building workbook")
    model.build()
    mismatches, checks, vals = model.check_against_article(XLSX)
    assert not mismatches, mismatches
    assert all(abs(v) < 1e-9 for v in checks["Model"]), checks
    assert [round(v, 1) for v in checks["Error constant"]] == [12.0] * 4, checks
    assert [round(v, 1) for v in checks["Error growing"]] == [0.0, 44.0, 91.5, 141.9], checks

    print("rendering screenshots")
    # Section 5, step 2: the two supporting schedules, formulas visible
    render("Model", "B36:I48", "01-schedules.png")
    add("01-schedules.png",
        "Excel PP&E and working capital schedules with the 2026 formulas shown beside each row",
        "The two schedules under the income statement, with each row's 2026 formula beside it: the PP&E roll is beginning plus capex minus D&A, and receivables are revenue times DSO over 365.",
        "workbook three-statement-test.xlsx, sheet Model, range B36:I48",
        "**Step 2: the two supporting schedules.** Two small tables under the income statement.")

    # Section 5, step 5: the check row close-up (total assets, total liabilities and equity, check)
    render("Model", "B50:I62", "02-balance-check-row.png", hidden_rows=list(range(51, 55)) + list(range(56, 61)))
    add("02-balance-check-row.png",
        "Close-up of the balance check row in Excel: total assets minus total liabilities and equity, 0.0 in every year",
        "The check row is one subtraction, total assets minus total liabilities and equity, and it reads 0.0 in every year before the revolver is even built.",
        "workbook three-statement-test.xlsx, sheet Model, rows 50, 55, 61 and 62 of B:I (rows between hidden)",
        "**Step 5: cash back to the balance sheet.** Ending cash equals last year's cash")

    # Section 5, step 6: the debt and revolver block
    render("Model", "B83:I93", "03-revolver-block.png")
    add("03-revolver-block.png",
        "Excel debt and revolver block showing cash before revolver, the MAX draw formula, the MIN repayment formula and ending balances",
        "The revolver block in the sheet: cash before the revolver is 16.4 in 2027, so the MAX formula draws 33.6, and in 2028 the MIN formula repays 19.0 of it.",
        "workbook three-statement-test.xlsx, sheet Model, range B83:I93",
        "**Step 6: the revolver plug.** A revolver is a revolving credit line")

    # Section 6: the two error patterns
    render("Error constant", "B50:I62", "04-error-constant.png")
    add("04-error-constant.png",
        "Balance sheet in Excel with net PP&E mistyped as 412.0, so the check row reads 12.0 in every year",
        "The constant pattern: 2025 net PP&E was typed as 412.0 instead of 400.0, and the check row carries the same 12.0 into every projected year.",
        "workbook three-statement-test.xlsx, sheet Error constant (2025A net PP&E typed as 412.0), range B50:I62",
        "**A constant difference in every projected year means a one-time break, usually in the first year.**")
    render("Error growing", "B50:I62", "05-error-growing.png")
    add("05-error-growing.png",
        "Balance sheet in Excel where the PP&E roll never subtracts D&A, so the check row reads 44.0, 91.5 and 141.9",
        "The growing pattern: the PP&E roll never subtracts D&A, so the check row grows by each year's D&A, 44.0, then 91.5, then 141.9.",
        "workbook three-statement-test.xlsx, sheet Error growing (PP&E roll drops the D&A term), range B50:I62",
        "**A growing difference means a recurring link is missing or has the wrong sign.**")

    print("drawing charts")
    chart_check_patterns()
    add("06-check-patterns.png",
        "Line chart of two balance check patterns: a flat line at 12.0 and a rising line from 44.0 to 141.9",
        "Read the shape before the number: a flat line means something broke once, and a line that climbs by about the same amount each year means a recurring link is missing.",
        "chart from section 6 (constant 12.0 case and growing 44.0, 91.5, 141.9 case)",
        "The procedure, in order. Read the check row and classify the pattern.")

    # Section 7: the toggle close-up (toggle cell plus the interest expense row that reads it)
    render("Model", "B4:I30", "07-toggle-closeup.png", hidden_rows=list(range(6, 21)) + list(range(22, 29)))
    add("07-toggle-closeup.png",
        "Close-up of the circularity toggle cell set to 0 and the interest expense formula that reads it",
        "The toggle sits at the top of the drivers block, and interest expense reads it: with a 0 in D5 the IF picks beginning debt and the model has no circular reference.",
        "workbook three-statement-test.xlsx, sheet Model, rows 4, 5, 21, 29 and 30 of B:I (rows between hidden)",
        "**The toggle.** Put a cell at the top of the assumptions block labeled")

    # Section 9: the worked example, one screenshot per table
    render("Model", "B1:G19", "08-drivers.png")
    add("08-drivers.png",
        "Excel drivers block for the worked example: growth, margins, days, tax, interest rates, amortization, payout and minimum cash by year",
        "The whole model hangs off this block: blue cells are typed assumptions, the 2025A column is the historical ratio each one is based on, and the toggle at the top stays at 0.",
        "workbook three-statement-test.xlsx, sheet Model, range B1:G19",
        "| Circularity toggle | n/a | 0 | 0 | 0 |")
    render("Model", "B21:G34", "09-income-statement.png")
    add("09-income-statement.png",
        "Excel income statement for 2025A to 2028E from revenue of 1,000.0 down to net income of 98.5 and dividends",
        "The same income statement in the sheet: costs are negative, every subtotal is a SUM, and only the 2025A column is typed in blue.",
        "workbook three-statement-test.xlsx, sheet Model, range B21:G34",
        "| Dividends (25% payout) | -18.8 | -20.9 | -23.2 | -24.6 |")
    render("Model", "B50:G62", "10-balance-sheet.png")
    add("10-balance-sheet.png",
        "Excel balance sheet for 2025A to 2028E with the revolver at 33.6 in 2027 and a 0.0 check row",
        "The balance sheet with the check row underneath: cash lands on the 50.0 minimum in 2027 and 2028 because the revolver is doing its job, and the check reads 0.0 across.",
        "workbook three-statement-test.xlsx, sheet Model, range B50:G62",
        "| Balance check (assets minus liabilities and equity) | 0.0 | 0.0 | 0.0 | 0.0 |")
    render("Model", "B64:G81", "11-cash-flow-statement.png")
    add("11-cash-flow-statement.png",
        "Excel cash flow statement for 2026E to 2028E with operating, investing and financing sections and ending cash",
        "The cash flow statement with beginning and ending cash rows added, so the 2026 ending cash of 86.9 is visibly 80.0 plus the 6.9 net change.",
        "workbook three-statement-test.xlsx, sheet Model, range B64:G81",
        "| Memo: cash before revolver | 86.9 | 16.4 | 69.0 |")
    chart_waterfall()
    add("12-cash-waterfall-2026.png",
        "Waterfall chart of 2026 cash flow from net income of 83.7 through each flow to ending cash of 86.9",
        "Walk the 2026 column as a bridge: operations bring in 112.8, capex, amortization and dividends take 105.9 of it back out, and cash ends the year 6.9 higher at 86.9.",
        "chart from the section 9 cash flow statement and balance sheet tables, 2026E column",
        "2026: net income 83.7, plus D&A 44.0, minus the 10.6 increase in receivables")

    # Section 13: formula close-up (the three links the grader checks with F2)
    render("Model", "B64:I80", "13-formula-closeup.png", hidden_rows=list(range(71, 78)))
    add("13-formula-closeup.png",
        "Close-up of cash flow statement rows in Excel with the formulas that link net income, D&A and ending cash",
        "What F2 shows the grader: net income is a reference to the income statement, D&A is a reference and not a typed 44, and ending cash is beginning cash plus the net change.",
        "workbook three-statement-test.xlsx, sheet Model, rows 64 to 70 and 78 to 80 of B:I (rows between hidden)",
        "Then they press F2 on three or four cells in the cash flow statement")

    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT}")


if __name__ == "__main__":
    main()
