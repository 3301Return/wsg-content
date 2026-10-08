#!/usr/bin/env python3
"""Images for "Net Working Capital: How to Explain It in an Interview" (October 1, 2026 batch).

Run from the repo root:  python3 scripts/images/build_net-working-capital-interview.py

1. Rebuilds scripts/images/models/ridgeline-nwc.xlsx (build_ridgeline_nwc.py).
2. Recalculates it with LibreOffice and checks every screenshot number against the article's tables.
3. Renders four Excel-style screenshots and draws two charts into
   published/assets/images/net-working-capital-interview/, then writes manifest.json.

Idempotent: every output is overwritten.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
sys.path.insert(0, str(ROOT / "scripts" / "images" / "models"))
from wsg_viz import (AQUA, BLUE, GRID, ORANGE, TEXT_MUTED, TEXT_PRIMARY, TEXT_SECONDARY, new_figure,  # noqa: E402
                     recalc_values, render_range, save_figure, style_axes, write_manifest)
import build_ridgeline_nwc  # noqa: E402

SLUG = "net-working-capital-interview"
OUT = ROOT / "published" / "assets" / "images" / SLUG
XLSX = ROOT / "scripts" / "images" / "models" / "ridgeline-nwc.xlsx"
GRAY = "#c9c8c3"   # de-emphasis fill for the steps that are not the story


def cap_width(png, max_px=2200):
    """Tight bounding boxes can push a chart past 2200 px; scale it back down."""
    from PIL import Image
    im = Image.open(png)
    if im.width > max_px:
        im = im.resize((max_px, round(im.height * max_px / im.width)), Image.LANCZOS)
        im.save(png, "PNG", optimize=True, dpi=(200, 200))
    return png


# ------------------------------------------------------------------ 1 and 2: workbook and checks
def check_workbook():
    """Compare the recalculated workbook with the article's tables. Raises on any mismatch."""
    v = recalc_values(XLSX)
    s, inv, peg = v["NWC schedule"], v["Inventory walk"], v["Working capital peg"]
    expected = {
        # section 3 table: Year 1, Year 2, change, cash effect
        "D13": 80, "E13": 95, "F13": 15, "G13": -15,
        "D14": 120, "E14": 130, "F14": 10, "G14": -10,
        "D15": 10, "E15": 10, "F15": 0, "G15": 0,
        "D17": 70, "E17": 75, "F17": 5, "G17": 5,
        "D18": 30, "E18": 30, "D19": 20, "E19": 20,
        "D21": 90, "E21": 110, "F21": 20, "G21": -20,
        # section 1: operating current assets 210 and liabilities 120 in Year 1
        "D16": 210, "D20": 120,
        # section 8: Year 1 days (29, 73, 43 -> about 60) and section 10 Year 2 days (33.0, 75.3, 43.5)
        "D26": 29.2, "D27": 73.0, "D28": 42.6, "D29": 59.6,
        "E26": 33.0, "E27": 75.3, "E28": 43.5,
        # section 10 table: Year 3 projected
        "F35": 99.5, "F36": 135.6, "F37": 10.5, "F38": 79.6, "F39": 31.4, "F40": 21.0, "F41": 113.6, "F42": 3.6,
        "E42": 20,
        # sections 4 and 5: cash from operations 60, unlevered free cash flow 50
        "E54": 60, "E57": 60, "E61": 75, "E65": 50,
    }
    bad = []
    for ref, want in expected.items():
        got = s.get(ref)
        if got is None or round(float(got), 1) != round(float(want), 1):
            bad.append(("NWC schedule", ref, want, got))
    for ref, want in {"E16": 3.75, "D21": -10, "E21": 13.75, "F21": 3.75, "F25": 3.75, "F26": 0, "F28": 3.75,
                      "D30": 0, "E30": 0, "F30": 0}.items():
        got = inv.get(ref)
        if got is None or round(float(got), 2) != want:
            bad.append(("Inventory walk", ref, want, got))
    for ref, want in {"E11": -5, "F11": 495, "E12": 0, "F12": 500, "E13": 8, "F13": 508}.items():
        got = peg.get(ref)
        if got is None or round(float(got), 1) != want:
            bad.append(("Working capital peg", ref, want, got))
    # the small items hold their Year 2 percent of revenue, shown as 1.0%, 2.9%, 1.9%
    for ref, want in {"E30": 0.010, "E31": 0.029, "E32": 0.019}.items():
        if round(float(s[ref]), 3) != want:
            bad.append(("NWC schedule", ref, want, s[ref]))
    if bad:
        for b in bad:
            print("MISMATCH", b)
        raise SystemExit("workbook does not match the article; fix before rendering")
    print(f"workbook checks passed ({len(expected) + 16} cells match the article)")


# ------------------------------------------------------------------ 3: charts
def chart_ufcf_bridge(out):
    """Section 5: EBIT to unlevered free cash flow, Year 2, with the NWC step highlighted."""
    steps = [("EBIT", 100, "total"), ("Taxes\nat 25%", -25, "step"), ("NOPAT", 75, "total"),
             ("D&A", 20, "step"), ("Capex", -25, "step"), ("Increase\nin NWC", -20, "nwc"),
             ("Unlevered\nfree cash flow", 50, "total")]
    fig, ax = new_figure(height=6.0)
    running = 0.0
    xs = range(len(steps))
    for i, (label, val, kind) in zip(xs, steps):
        if kind == "total":
            bottom, height = 0.0, val
            running = val
            color = BLUE
        else:
            bottom = running if val >= 0 else running + val
            height = abs(val)
            running += val
            color = ORANGE if kind == "nwc" else GRAY
        ax.bar(i, height, bottom=bottom, width=0.52, color=color, linewidth=0)
        txt = f"{val:,.0f}" if kind == "total" else (f"+{val:,.0f}" if val > 0 else f"({abs(val):,.0f})")
        if kind == "total" or val > 0:      # label where the step ends: above for ups, below for downs
            ax.annotate(txt, (i, bottom + height), xytext=(0, 5), textcoords="offset points", ha="center",
                        va="bottom", fontsize=13, color=TEXT_PRIMARY, fontweight="bold" if kind != "step" else "normal")
        else:
            ax.annotate(txt, (i, bottom), xytext=(0, -5), textcoords="offset points", ha="center",
                        va="top", fontsize=13, color=TEXT_PRIMARY, fontweight="bold" if kind != "step" else "normal")
        if i < len(steps) - 1:   # hairline connector to the next bar
            ax.plot([i + 0.26, i + 1 - 0.26], [running, running], color=GRID, linewidth=1.0, zorder=0)
    # what free cash flow would have been with working capital flat
    ax.plot([6 - 0.3, 6 + 0.3], [70, 70], color=TEXT_SECONDARY, linewidth=1.6)
    ax.annotate("70 if NWC\nhad stayed flat", (6, 70), xytext=(0, 6), textcoords="offset points",
                ha="center", va="bottom", fontsize=11, color=TEXT_SECONDARY)
    ax.set_xticks(list(xs))
    ax.set_xticklabels([s[0] for s in steps], fontsize=12)
    ax.set_ylim(0, 118)
    ax.set_yticks([0, 25, 50, 75, 100])
    style_axes(ax, title="A $20 million NWC build takes almost a third of Ridgeline's free cash flow",
               ylabel="$ millions, Year 2")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=BLUE, label="Subtotal"), Patch(color=GRAY, label="Other adjustment"),
                       Patch(color=ORANGE, label="Increase in net working capital")],
              loc="upper right", ncol=3, bbox_to_anchor=(1.0, 1.0))
    return cap_width(save_figure(fig, out))


def chart_ccc_timeline(out):
    """Section 8: the cash conversion cycle as a timeline for Ridgeline and for Amazon's fiscal 2020."""
    # Ridgeline: 120 / 600 x 365, 80 / 1,000 x 365 and 70 / 600 x 365 from the article's section 8,
    # kept at one decimal so the pieces add up (the article rounds them to 73, 29, 43 and "about 60")
    cases = [
        ("Ridgeline Outdoor Co. (fictional): 73.0 + 29.2 minus 42.6 = 59.6 days, about 60",
         120 / 600 * 365, 80 / 1000 * 365, 70 / 600 * 365, "{:.1f}"),
        ("Amazon, fiscal 2020, from the 10-K: 37.2 + 23.2 minus 113.5 = negative 53.1 days",
         37.2, 23.2, 113.5, "{:.1f}"),
    ]
    fig, axes = new_figure(height=7.6, nrows=2, sharex=True)
    rows = ["Inventory held (DIO)", "Receivable outstanding (DSO)", "Payable outstanding (DPO)",
            "Cash conversion cycle"]
    ypos = [3, 2, 1, 0]
    h = 0.52
    for ax, (ttl, dio, dso, dpo, f) in zip(axes, cases):
        collect = dio + dso
        ccc = collect - dpo
        ax.barh(ypos[0], dio, left=0, height=h, color=BLUE, linewidth=0)
        ax.barh(ypos[1], dso, left=dio, height=h, color=ORANGE, linewidth=0)
        ax.barh(ypos[2], dpo, left=0, height=h, color=AQUA, linewidth=0)
        for y, start, width in ((ypos[0], 0, dio), (ypos[1], dio, dso), (ypos[2], 0, dpo)):
            ax.text(start + width / 2, y, f.format(width) + " days", ha="center", va="center", fontsize=12,
                    color="white", fontweight="bold")
        # the cycle: from paying the supplier to collecting from the customer
        lo, hi = sorted((dpo, collect))
        ax.plot([lo, hi], [ypos[3], ypos[3]], color=TEXT_PRIMARY, linewidth=2.2, solid_capstyle="butt")
        for x in (lo, hi):
            ax.plot([x, x], [ypos[3] - 0.18, ypos[3] + 0.18], color=TEXT_PRIMARY, linewidth=2.2)
        if ccc >= 0:
            label = f"{f.format(ccc)} days funded\nby Ridgeline"
        else:
            label = f"negative {f.format(-ccc)} days:\ncustomers' cash arrives first"
        ax.text(hi + 2, ypos[3], label, ha="left", va="center", fontsize=12, color=TEXT_PRIMARY)
        # event markers
        for x, text in ((0, "supplier delivers"), (dpo, f"pay supplier, day {f.format(dpo)}"),
                        (collect, f"collect from customer, day {f.format(collect)}")):
            ax.axvline(x, color=GRID, linewidth=1.0, zorder=0)
            ax.text(x + 1.2, 3.62, text, ha="left", va="bottom", fontsize=10.5, color=TEXT_MUTED)
        ax.set_yticks(ypos)
        ax.set_yticklabels(rows, fontsize=12)
        ax.set_ylim(-0.6, 4.1)
        ax.set_title(ttl, loc="left", fontsize=13, fontweight="bold", pad=8)
        ax.grid(False)
        ax.tick_params(length=0)
        ax.spines["left"].set_visible(False)
    axes[1].set_xlim(0, 160)
    axes[1].set_xlabel("Days after the supplier delivers the goods")
    axes[1].set_xticks(range(0, 161, 20))
    from matplotlib.patches import Patch
    fig.legend(handles=[Patch(color=BLUE, label="Days inventory outstanding"),
                        Patch(color=ORANGE, label="Days sales outstanding"),
                        Patch(color=AQUA, label="Days payable outstanding")],
               loc="upper left", ncol=3, bbox_to_anchor=(0.01, 0.955), frameon=False)
    fig.suptitle("Ridgeline funds every tent for 60 days, and Amazon holds its customers' cash for 53",
                 x=0.01, ha="left", fontsize=16, fontweight="bold", color=TEXT_PRIMARY, y=0.995)
    fig.tight_layout(rect=(0, 0, 1, 0.925))
    return cap_width(save_figure(fig, out))


# ------------------------------------------------------------------ main
def main():
    build_ridgeline_nwc.build(XLSX)
    check_workbook()
    OUT.mkdir(parents=True, exist_ok=True)
    entries = []

    render_range(XLSX, "NWC schedule", "B11:G22", OUT / "01-change-in-nwc-year-1-to-year-2.png")
    entries.append({
        "file": "01-change-in-nwc-year-1-to-year-2.png",
        "alt": "Spreadsheet of Ridgeline's operating assets and liabilities in Year 1 and Year 2 with change and cash effect columns",
        "caption": "The same table in a sheet: receivables and inventory up 25, payables up 5, and the 20 of net working capital build shows up as 20 of cash out.",
        "method": "workbook scripts/images/models/ridgeline-nwc.xlsx, sheet NWC schedule, range B11:G22",
        "anchor": "| **Net working capital** | **90** | **110** | **+20** | **(20)** |"[:60],
    })

    chart_ufcf_bridge(OUT / "02-nwc-to-unlevered-fcf-bridge.png")
    entries.append({
        "file": "02-nwc-to-unlevered-fcf-bridge.png",
        "alt": "Waterfall chart from EBIT of 100 through taxes, D&A, capex and the working capital build to free cash flow of 50",
        "caption": "Free cash flow would have been 70 with working capital flat; the 20 that went into receivables and inventory is the orange bar.",
        "method": "chart from the article's section 5 table (unlevered free cash flow, Year 2) and the 'if NWC had stayed flat' sentence after it",
        "anchor": "Now change one thing. If net working capital had stayed flat, free cash flow would be 70."[:60],
    })

    render_range(XLSX, "Working capital peg", "B5:H13", OUT / "03-working-capital-peg.png")
    entries.append({
        "file": "03-working-capital-peg.png",
        "alt": "Spreadsheet showing a 500 million price and 50 million peg with closing working capital of 45, 50 and 58 giving final prices of 495, 500 and 508",
        "caption": "Every dollar of closing working capital above or below the 50 peg moves the 500 price by a dollar, and the formula is one addition.",
        "method": "workbook scripts/images/models/ridgeline-nwc.xlsx, sheet Working capital peg, range B5:H13",
        "anchor": "| 58 | +8 | 508 |"[:60],
    })

    chart_ccc_timeline(OUT / "04-cash-conversion-cycle-timeline.png")
    entries.append({
        "file": "04-cash-conversion-cycle-timeline.png",
        "alt": "Two timelines of inventory, receivable and payable days showing Ridgeline's 60 day cycle and Amazon's negative 53 day cycle",
        "caption": "Read each panel left to right from the day the supplier delivers: Ridgeline pays on day 43 and collects on day 102, while Amazon collects on day 60 and pays on day 114.",
        "method": "chart from the article's section 8 figures: Ridgeline DSO 29, DIO 73, DPO 43; Amazon fiscal 2020 DSO 23.2, DIO 37.2, DPO 113.5 from the article's Amazon table",
        "anchor": "Amazon collected from customers about 23 days after a sale on average"[:60],
    })

    render_range(XLSX, "NWC schedule", "B24:G42", OUT / "05-days-method-year-3-projection.png")
    entries.append({
        "file": "05-days-method-year-3-projection.png",
        "alt": "Spreadsheet computing DSO, DIO and DPO for two years, then projecting Year 3 receivables, inventory and payables from rounded days with formulas shown",
        "caption": "The days come out of the Year 2 actuals, get rounded to 33, 75 and 44 as inputs, and the Year 3 balances are one formula each: days over 365 times revenue or cost of goods sold.",
        "method": "workbook scripts/images/models/ridgeline-nwc.xlsx, sheet NWC schedule, range B24:G42 (formula column G holds the formula text next to each row)",
        "anchor": "| **Increase (use of cash)** | | | **3.6** |"[:60],
    })

    render_range(XLSX, "Inventory walk", "B5:F30", OUT / "06-inventory-three-statement-walk.png")
    entries.append({
        "file": "06-inventory-three-statement-walk.png",
        "alt": "Spreadsheet walking 10 dollars of inventory bought for cash and then sold for 15 through the income statement, cash flow statement and balance sheet",
        "caption": "Step 1 never touches the income statement, step 2 is where the cost and the profit both appear, and the balance check row stays at zero in every column.",
        "method": "workbook scripts/images/models/ridgeline-nwc.xlsx, sheet Inventory walk, range B5:F30",
        "anchor": "The follow-up is usually \"now it sells for $15, with a 25 percent tax rate.\""[:60],
    })

    write_manifest(OUT, entries)
    for e in entries:
        for k in ("alt", "caption", "method", "anchor"):
            assert "\u2014" not in e[k] and "\u2013" not in e[k], f"dash in manifest {e['file']} {k}"
    print(f"wrote {len(entries)} images and manifest.json to {OUT}")


if __name__ == "__main__":
    main()
