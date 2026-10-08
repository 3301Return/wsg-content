#!/usr/bin/env python3
"""Images for "The Three Financial Statements: How They Link and How to Explain It"
(WSG, October 5, 2026 batch).

Run from the repo root:  python3 scripts/images/build_three-financial-statements-how-they-link.py

1. Rebuilds scripts/images/models/lantern-bikes.xlsx (build_lantern_bikes.py) with live formulas
   and asserts the LibreOffice recalculated values against every table in sections 4, 5 and 6.
2. Renders the Excel screenshots: the $10 depreciation walk, five of the ten scenario tables,
   the three Lantern Bikes statements, the balance check close-up and a formula close-up.
3. Draws two diagrams (the six links, the walk order) and the Year 2 cash bridge from the
   article's own numbers.
4. Writes published/assets/images/three-financial-statements-how-they-link/manifest.json with
   an anchor per image (the first 60 characters of the draft line each image follows).

Idempotent: every output is overwritten in place. The draft itself is never touched here.
"""
import json
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
sys.path.insert(0, str(ROOT / "scripts" / "images" / "models"))
from wsg_viz import (BLUE, GRID, ORANGE, TEXT_MUTED, TEXT_PRIMARY, TEXT_SECONDARY,  # noqa: E402
                     new_figure, render_range, save_figure, style_axes, write_manifest)
from wsg_diagrams import (LINE, PALE_BLUE, PALE_GRAY, RED, arrow, canvas, finish, label, text_box,  # noqa: E402
                          waterfall, wrap)
import build_lantern_bikes as model  # noqa: E402

SLUG = "three-financial-statements-how-they-link"
OUT = ROOT / "published" / "assets" / "images" / SLUG
XLSX = model.OUT
R = model.R
BAD_CHARS = ("\u2014", "\u2013", "\u2212")   # em dash, en dash, Unicode minus

entries = []


def add(file, alt, caption, method, anchor):
    for text in (alt, caption, method, anchor):
        assert not any(ch in text for ch in BAD_CHARS), f"dash in manifest text for {file}: {text!r}"
    words = len(alt.split())
    assert 10 <= words <= 20, f"alt text for {file} has {words} words, wants 10 to 20"
    entries.append({"file": file, "alt": alt, "caption": caption, "method": method, "anchor": anchor[:60]})


def render(sheet, cell_range, name, hidden_rows=(), hidden_cols=(), widths=None):
    """render_range on a temp copy with some rows or columns hidden (so a close-up can show
    the rows that matter without the ones in between) and, for the close-ups, narrower columns."""
    out = OUT / name
    if not hidden_rows and not hidden_cols and not widths:
        return render_range(str(XLSX), sheet, cell_range, str(out))
    from openpyxl import load_workbook
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "hidden.xlsx"
        wb = load_workbook(XLSX)
        ws = wb[sheet]
        for r in hidden_rows:
            ws.row_dimensions[r].hidden = True
        for c in hidden_cols:
            ws.column_dimensions[c].hidden = True
        for c, w in (widths or {}).items():
            ws.column_dimensions[c].width = w
        wb.save(tmp)
        return render_range(str(tmp), sheet, cell_range, str(out))


def scenario_rows(name):
    first, last = model.SCENARIO_RANGES[name]
    return f"B{first}:F{last}"


# ---------------------------------------------------------------- diagram 1: the six links
def diagram_six_links(out):
    """The article's six links as three statement columns and six arrow rows, each carrying
    Lantern Bikes' Year 2 number (section 2 and the section 6 'six links' table)."""
    W, H = 13.2, 8.9
    fig, ax = canvas(W, H)
    label(ax, 0.35, H - 0.4, "The six links, with Lantern Bikes' Year 2 numbers on each one", size=18, bold=True,
          va="top")
    label(ax, 0.35, H - 0.82, "$ millions. Each row is one link; the arrows show which statement hands the number to the next.",
          size=12, color=TEXT_SECONDARY, va="top")
    # columns
    left_x, left_w = 0.35, 1.65
    col_w, gap = 3.2, 0.55
    col_x = [left_x + left_w + 0.2, 0, 0]
    col_x[1] = col_x[0] + col_w + gap
    col_x[2] = col_x[1] + col_w + gap
    head_y, head_h = H - 1.75, 0.62
    for x, name in zip(col_x, ["Income statement", "Cash flow statement", "Balance sheet"]):
        text_box(ax, x, head_y, col_w, head_h, name, fill=BLUE, text_color="white", size=13.5, bold=True)
    # rows: (link name, IS cell, CFS cell, BS cell, arrows) arrows: list of (from_col, to_col)
    rows = [
        ("1. Net income",
         "Bottom line: net income 45",
         "Top line: starts at 45",
         "Retained earnings 110, plus 45,\nminus 12 of dividends, is 143",
         [(0, 1), (1, 2)]),
        ("2. D&A",
         "Expense: D&A (30), inside EBIT",
         "Added back: +30,\nno cash left this year",
         "Net PP&E down 30",
         [(0, 1), (1, 2)]),
        ("3. Capex",
         None,
         "Investing outflow: capex (40)",
         "Net PP&E up 40\n(300 + 40 minus 30 = 310)",
         [(1, 2)]),
        ("4. Working capital",
         None,
         "Operations: (10), (5), +6, +2,\na net (7)",
         "AR up 10, inventory up 5,\npayables up 6, accrued up 2",
         [(2, 1)]),
        ("5. Debt",
         "Interest only: 10, which is 5%\nof the 200 of beginning debt",
         "Financing outflow: debt repaid (20)",
         "Long-term debt 200 to 180",
         [(1, 2)]),
        ("6. Ending cash",
         None,
         "Last line: ending cash 36\n(40 minus 4)",
         "First line: cash 36",
         [(1, 2)]),
    ]
    row_h, pitch = 0.82, 1.0
    y = head_y - 0.3 - row_h
    for name, is_t, cf_t, bs_t, arrows in rows:
        label(ax, left_x + 0.05, y + row_h / 2, name, size=13, bold=True, va="center")
        cells = [is_t, cf_t, bs_t]
        for i, (x, t) in enumerate(zip(col_x, cells)):
            if t is None:
                label(ax, x + col_w / 2, y + row_h / 2, "not here", size=12, color=TEXT_MUTED, ha="center",
                      va="center", italic=True)
            else:
                fill = PALE_GRAY if (name.startswith("5") and i == 0) else PALE_BLUE
                text_box(ax, x, y, col_w, row_h, t, fill=fill, size=11.8, pad_in=0.14)
        for a, b in arrows:
            if b > a:
                p1 = (col_x[a] + col_w + 0.03, y + row_h / 2)
                p2 = (col_x[b] - 0.03, y + row_h / 2)
            else:
                p1 = (col_x[a] - 0.03, y + row_h / 2)
                p2 = (col_x[b] + col_w + 0.03, y + row_h / 2)
            arrow(ax, p1, p2, color=TEXT_SECONDARY, lw=2.0, head=16)
        y -= pitch
    label(ax, 0.35, 0.3, "Parentheses mean the line went down. Link 4 runs right to left: the cash flow statement reads the balance sheet changes.",
          size=11, color=TEXT_MUTED, va="center")
    return finish(fig, out)


# ---------------------------------------------------------------- diagram 2: the walk order
def diagram_walk_order(out):
    """Section 3: income statement, then cash flow statement, then balance sheet, each handing
    the next the number it needs (Lantern Bikes' 45 and 36)."""
    W, H = 12.4, 4.4
    fig, ax = canvas(W, H)
    label(ax, 0.35, H - 0.4, "Walk the statements in the order each one hands the next its number", size=18,
          bold=True, va="top")
    box_w, box_h, gap = 3.1, 1.8, 1.25
    x0 = (W - (3 * box_w + 2 * gap)) / 2
    y0 = 1.3
    boxes = [
        ("1. Income statement", "Revenue 500 down to net income 45. Accrual basis: profit when earned, not when paid."),
        ("2. Cash flow statement", "Starts at net income 45, adds back D&A, fixes working capital, then investing and financing, and ends at cash 36."),
        ("3. Balance sheet", "Cash 36, net PP&E 310, retained earnings 143. Then the check: assets 501 = liabilities 258 + equity 243."),
    ]
    from matplotlib.patches import FancyBboxPatch
    for i, (head, body) in enumerate(boxes):
        x = x0 + i * (box_w + gap)
        ax.add_patch(FancyBboxPatch((x, y0), box_w, box_h, boxstyle="round,pad=0,rounding_size=0.08",
                                    facecolor=PALE_BLUE, edgecolor=PALE_BLUE, zorder=3))
        ax.add_patch(FancyBboxPatch((x, y0 + box_h - 0.5), box_w, 0.5, boxstyle="round,pad=0,rounding_size=0.08",
                                    facecolor=BLUE, edgecolor=BLUE, zorder=3))
        label(ax, x + box_w / 2, y0 + box_h - 0.25, head, size=13.5, bold=True, color="white", ha="center",
              va="center")
        label(ax, x + box_w / 2, y0 + (box_h - 0.5) / 2, wrap(body, box_w - 0.3, 11.5), size=11.5, ha="center",
              va="center")
    hand = ["hands over\nnet income 45", "hands over\nending cash 36"]
    for i, t in enumerate(hand):
        xa = x0 + (i + 1) * box_w + i * gap
        ya = y0 + (box_h - 0.5) / 2
        arrow(ax, (xa + 0.05, ya), (xa + gap - 0.05, ya), color=TEXT_SECONDARY, lw=2.2, head=18)
        label(ax, xa + gap / 2, ya + 0.16, t, size=11, ha="center", va="bottom", color=TEXT_SECONDARY)
    label(ax, 0.35, 0.6, "Start on the balance sheet and you have to guess the cash line, and the guess is what breaks the balance. "
                         "In this order every number is ready when you need it.",
          size=11.5, color=TEXT_SECONDARY, va="center", wrap_in=W - 0.7)
    return finish(fig, out)


# ---------------------------------------------------------------- chart: the Year 2 cash bridge
def chart_cash_bridge(out):
    """Beginning cash to ending cash from the article's 'Why Lantern Bikes' cash fell by 4' table."""
    steps = [("Net income", 45), ("D&A added back", 30), ("Working capital build", -7), ("Capex", -40),
             ("Debt repaid", -20), ("Dividends", -12)]
    # the article's running totals: 45, 75, 68, 28, 8, (4)
    run, article = 0, [45, 75, 68, 28, 8, -4]
    for (_, d), want in zip(steps, article):
        run += d
        assert run == want, (run, want)
    assert 40 + run == 36
    fig, ax = new_figure(width=11.0, height=6.2)
    waterfall(ax, steps, start=40, start_label="Beginning cash", end_label="Ending cash", fmt="{:,.0f}",
              neg_fmt="({:,.0f})", ylabel="$ millions", title="Lantern Bikes earned 45 and still ended Year 2 with 4 less cash",
              label_size=12.5, ymin=0)
    ax.set_ylim(0, 130)
    ax.text(0.0, -0.2, "Net income plus D&A minus the working capital build is cash from operations of 68; "
                       "capex, the debt repayment and the dividend take 72 back out.",
            transform=ax.transAxes, fontsize=10.5, color=TEXT_MUTED, ha="left", va="top")
    return finish(fig, out)


# ---------------------------------------------------------------- main
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    print("building workbook")
    model.build(XLSX)
    mismatches, vals = model.check_against_article(XLSX)
    assert not mismatches, mismatches
    lb = vals["Lantern Bikes"]
    assert lb[f"D{R['check']}"] == 0 and lb[f"E{R['check']}"] == 0, "balance check is not zero"
    assert lb[f"E{R['cash']}"] == lb[f"E{R['endcash']}"] == 36, "ending cash does not tie"

    print("drawing diagrams")
    # Section 2: the six links, after the Link 6 paragraph
    diagram_six_links(OUT / "01-six-links.png")
    add("01-six-links.png",
        "Diagram of the six links between the income statement, cash flow statement and balance sheet with Lantern Bikes' numbers",
        "Six rows, six links: net income and D&A start on the income statement, capex, debt and ending cash run from the cash flow statement to the balance sheet, and working capital runs the other way.",
        "diagram drawn with wsg_diagrams from the section 2 link paragraphs and the section 6 six links table",
        "**Link 6: the last line of the cash flow statement is the first line of the balance sheet.**")

    # Section 3: the walk order, after the paragraph that explains it
    diagram_walk_order(OUT / "02-walk-order.png")
    add("02-walk-order.png",
        "Three boxes in a row showing the walk order from income statement to cash flow statement to balance sheet",
        "The order is forced by the hand-offs: the income statement produces the 45 the cash flow statement starts from, and the cash flow statement produces the 36 the balance sheet needs.",
        "diagram drawn with wsg_diagrams from section 3 and the Lantern Bikes figures in section 6",
        "Start with the income statement because it produces net income, and net income is the first line")

    print("rendering screenshots")
    # Section 4: the $10 depreciation walk, after its table
    render("Depreciation walk", "B4:G28", "03-depreciation-walk.png")
    add("03-depreciation-walk.png",
        "Spreadsheet of the ten dollar depreciation walk at 25 and 40 percent tax rates with formulas shown beside each row",
        "The same walk in a sheet: taxes are pre-tax income times the rate, the add-back is the depreciation line, and cash lands at 2.5, which is 10 times 25 percent.",
        "workbook lantern-bikes.xlsx, sheet Depreciation walk, range B4:G28 (column G holds the 25 percent formula as text)",
        "| Balance check (assets minus liabilities and equity) | 0 | 0 |")

    # Section 5: five of the ten scenarios, each after its own table
    scen = [
        ("Inventory goes up by $10, bought on credit", "04-scenario-inventory-on-credit.png",
         "Spreadsheet of the inventory bought on credit scenario where inventory and payables both rise by 10 and cash is unchanged",
         "Two working capital lines that cancel: inventory up is cash out, payables up is cash in, so cash from operations is 0 and both sides of the balance sheet rise by 10.",
         "| Cash flow statement: change in accounts payable (liability up, cash in) | 10 |"),
        ("$100 of capex, paid in cash", "05-scenario-capex.png",
         "Spreadsheet of the 100 of capex scenario with cash down 100, net PP&E up 100 and no income statement effect",
         "Capex never visits the income statement in the year it is spent: the 100 leaves through investing and reappears as PP&E, so total assets do not move.",
         "| Cash flow statement: capital expenditures (investing) | (100) |"),
        ("Raise $100 of debt", "06-scenario-raise-debt.png",
         "Spreadsheet of the raise 100 of debt scenario with a financing inflow, cash up 100 and long-term debt up 100",
         "Borrowing is a financing line and a balance sheet line only: cash and debt both rise by 100, and the interest shows up on next year's income statement.",
         "| Cash flow statement: debt issued (financing) | 100 |"),
        ("$20 of deferred revenue collected", "07-scenario-deferred-revenue.png",
         "Spreadsheet of the 20 of deferred revenue scenario with cash up 20 and deferred revenue up 20 as a liability",
         "A liability going up is a source of cash: the 20 arrives in operations before any revenue is booked, and it sits in deferred revenue until the work is done.",
         "| Cash flow statement: change in deferred revenue (liability up, cash in) | 20 |"),
        ("Sell equipment with a $30 book value for $40", "08-scenario-equipment-sale.png",
         "Spreadsheet of the equipment sale scenario with the 10 gain backed out of operations and 40 of proceeds in investing",
         "The trap in a sheet: net income is up 7.5, the 10 gain is backed out of operations, the full 40 of proceeds lands in investing, and cash ends up 37.5.",
         "| Cash flow statement: proceeds from sale of equipment (investing) | 40 |"),
    ]
    for name, file, alt, caption, anchor in scen:
        render("Scenarios", scenario_rows(name), file)
        first, last = model.SCENARIO_RANGES[name]
        add(file, alt, caption, f"workbook lantern-bikes.xlsx, sheet Scenarios, range B{first}:F{last} (column F holds each formula as text)",
            anchor)

    # Section 6: the three Lantern Bikes statements, each after its table
    render("Lantern Bikes", f"B{R['is_hdr']}:G{R['ni']}", "09-lantern-income-statement.png", hidden_cols=("D", "F"))
    add("09-lantern-income-statement.png",
        "Spreadsheet of Lantern Bikes' Year 2 income statement from revenue of 500 down to net income of 45",
        "The income statement in the sheet: costs are negative, every subtotal is a sum, and interest is 5 percent of the 200 of debt on the Year 1 balance sheet.",
        f"workbook lantern-bikes.xlsx, sheet Lantern Bikes, rows {R['is_hdr']} to {R['ni']} of columns B, E and G",
        "| Net income | 45 | Link 1: top of the CFS and into retained earnings |")
    render("Lantern Bikes", f"B{R['cf_hdr']}:G{R['endcash']}", "10-lantern-cash-flow-statement.png", hidden_cols=("D", "F"))
    add("10-lantern-cash-flow-statement.png",
        "Spreadsheet of Lantern Bikes' Year 2 cash flow statement from net income of 45 to ending cash of 36",
        "Net income 45 at the top, the four working capital lines netting to minus 7, operations at 68, then capex, the debt repayment and the dividend, and ending cash of 36.",
        f"workbook lantern-bikes.xlsx, sheet Lantern Bikes, rows {R['cf_hdr']} to {R['endcash']} of columns B, E and G",
        "| Ending cash | 36 | Link 6: becomes cash on the Year 2 balance sheet |")
    render("Lantern Bikes", f"B{R['bs_hdr']}:G{R['check']}", "11-lantern-balance-sheet.png")
    add("11-lantern-balance-sheet.png",
        "Spreadsheet of Lantern Bikes' Year 1 and Year 2 balance sheet with a change column and a zero check row",
        "Year 1 is typed in blue, every Year 2 line is a formula off the Year 1 balance and a cash flow line, and the check row reads 0 in both years.",
        f"workbook lantern-bikes.xlsx, sheet Lantern Bikes, range B{R['bs_hdr']}:G{R['check']}",
        "| Balance check (assets minus L+E) | 0 | 0 |  | Must be 0 |")

    # Section 6: the cash bridge, after the 'Why Lantern Bikes' cash fell by 4' table
    chart_cash_bridge(OUT / "12-cash-bridge-year-2.png")
    add("12-cash-bridge-year-2.png",
        "Waterfall from beginning cash of 40 through net income, D&A, working capital, capex and financing to ending cash of 36",
        "Read it left to right from the 40 Lantern Bikes started with: profit and the D&A add-back lift it to 115, then working capital, capex, the debt repayment and the dividend bring it down to 36.",
        "waterfall chart from the section 6 table 'Why Lantern Bikes' cash fell by 4 in a year it earned 45' plus the beginning cash of 40",
        "| Dividends | (12) | (4) |")

    # Section 6: the balance check close-up, after the 'Now the balance check' paragraph
    hide = [r for r in range(R['cash'], R['check']) if r not in (R['ta'], R['tle'])]
    render("Lantern Bikes", f"B{R['bs_hdr']}:I{R['check']}", "13-balance-check-closeup.png", hidden_rows=hide,
           hidden_cols=("G", "H"), widths={"B": 34, "I": 20})
    add("13-balance-check-closeup.png",
        "Close-up of the balance check row in Excel: total assets minus total liabilities and equity, zero in both years",
        "The check is one subtraction, total assets minus total liabilities and equity, and it reads 0 in both years because every link was carried through with its sign.",
        f"workbook lantern-bikes.xlsx, sheet Lantern Bikes, rows {R['bs_hdr']}, {R['ta']}, {R['tle']} and {R['check']} of columns B, D, E, F and I (rows between hidden)",
        "Now the balance check, which is the part interviewers watch.")

    # Section 6: the formula close-up (net income into the CFS, ending cash onto the balance sheet)
    keep = {R['is_hdr'], R['ni'], R['cf_hdr'], R['cf_ni'], R['netchg'], R['begcash'], R['endcash'], R['bs_hdr'],
            R['cash'], R['re'], R['check']}
    hide = [r for r in range(R['is_hdr'], R['check'] + 1) if r not in keep]
    render("Lantern Bikes", f"B{R['is_hdr']}:I{R['check']}", "14-formula-closeup-links.png", hidden_rows=hide,
           hidden_cols=("F", "G", "H"), widths={"B": 34, "I": 20})
    add("14-formula-closeup-links.png",
        "Excel close-up of the formulas linking net income into the cash flow statement and ending cash onto the balance sheet",
        "What the links look like as formulas: net income on the cash flow statement is a reference to the income statement, cash on the balance sheet is a reference to ending cash, and retained earnings add net income and subtract the dividend.",
        f"workbook lantern-bikes.xlsx, sheet Lantern Bikes, rows {sorted(keep)} of columns B, D, E and I (rows between hidden)",
        "If you want to build the same thing yourself, this is the exercise")

    write_manifest(OUT, entries)
    # every PNG at most 2200 px wide, and no dashes anywhere in the manifest
    from PIL import Image
    for e in entries:
        im = Image.open(OUT / e["file"])
        assert im.width <= 2200, (e["file"], im.width)
    text = (OUT / "manifest.json").read_text(encoding="utf-8")
    assert not any(ch in text for ch in BAD_CHARS), "dash in manifest"
    print(f"wrote {len(entries)} images and manifest.json to {OUT}")


if __name__ == "__main__":
    main()
