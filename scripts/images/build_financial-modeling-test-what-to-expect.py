#!/usr/bin/env python3
"""Images for "Financial Modeling Test: What to Expect and How to Practice" (WSG, October 5, 2026).

Run from the repo root:  python3 scripts/images/build_financial-modeling-test-what-to-expect.py

1. Rebuilds scripts/images/models/torvik-dcf.xlsx (live formulas, eight tabs) through
   scripts/images/models/build_torvik_dcf.py and asserts the LibreOffice recalculated values
   against every table in section 5 of the article (Tables 1 to 13 of the numbers script), with
   the scenario switch flipped to Bear and Bull on temp copies.
2. Renders the Excel screenshots in the article's build order (Steps 1 to 13), the scenario switch
   close-up and the formula close-up.
3. Draws three charts from the article's own tables: the five formats by length (section 2), the
   enterprise value to equity value bridge (section 5, Step 11), the two-hour time budget (section 6).
   The chart inputs are parsed from the draft's tables (read only) and asserted.
4. Writes published/assets/images/financial-modeling-test-what-to-expect/manifest.json.

Idempotent: every output is overwritten in place. The draft is never edited; the coordinator runs
scripts/images/insert_images.py with the manifest's anchors.
"""
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
sys.path.insert(0, str(ROOT / "scripts" / "images" / "models"))
from wsg_viz import *  # noqa: E402,F401
import build_torvik_dcf as model  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.rcParams["axes.unicode_minus"] = False
matplotlib.rcParams["text.parse_math"] = False

SLUG = "financial-modeling-test-what-to-expect"
OUT = ROOT / "published" / "assets" / "images" / SLUG
XLSX = model.OUT
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v1.md"
GRAY = "#8a8984"

entries = []


# ---------------------------------------------------------------- helpers
DRAFT_LINES = DRAFT.read_text(encoding="utf-8").split("\n")


def anchor_of(prefix):
    """The first 60 characters of the unique draft line that starts with prefix (asserted unique)."""
    hits = [l.strip() for l in DRAFT_LINES if l.strip().startswith(prefix)]
    assert len(hits) == 1, (prefix, len(hits))
    return hits[0][:60]


def add(file, alt, caption, method, anchor_prefix):
    text = alt + caption + method
    for ch in ("—", "–", "−"):
        assert ch not in text, ("dash or minus sign", file)
    assert 10 <= len(alt.split()) <= 20, ("alt text length", file, len(alt.split()))
    assert (OUT / file).exists(), file
    entries.append({"file": file, "alt": alt, "caption": caption, "method": method,
                    "anchor": anchor_of(anchor_prefix)})


def cap_width(path, max_w=2200):
    from PIL import Image
    im = Image.open(path)
    if im.width > max_w:
        im = im.convert("RGB").resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
        im.save(path, "PNG", optimize=True)
    return path


def render(sheet, cell_range, name, hide_rows=(), hide_cols=(), out=None):
    """render_range on a temp copy, optionally with rows or columns hidden for a close-up."""
    out = out or (OUT / name)
    from openpyxl import load_workbook
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "render.xlsx"
        shutil.copy(XLSX, tmp)
        if hide_rows or hide_cols:
            wb = load_workbook(tmp)
            ws = wb[sheet]
            for r in hide_rows:
                ws.row_dimensions[r].hidden = True
            for c in hide_cols:
                ws.column_dimensions[c].hidden = True
            wb.save(tmp)
        render_range(str(tmp), sheet, cell_range, str(out))
    print(f"rendered {Path(out).name}  ({sheet}!{cell_range})")
    return out


def stack(parts, out, gap=36):
    """Stack rendered PNGs top to bottom, left aligned, white gap between, on a white page."""
    from PIL import Image
    ims = [Image.open(p).convert("RGB") for p in parts]
    w = max(i.width for i in ims)
    h = sum(i.height for i in ims) + gap * (len(ims) - 1)
    page = Image.new("RGB", (w, h), (255, 255, 255))
    y = 0
    for im in ims:
        page.paste(im, (0, y))
        y += im.height + gap
    page.save(out, "PNG", optimize=True)
    return cap_width(out)


def draft_table(first_header_cell):
    """Rows of every draft table whose header row starts with first_header_cell (read only)."""
    rows, on = [], False
    for l in DRAFT_LINES:
        s = l.strip()
        if s.startswith(f"| {first_header_cell} |"):
            on = True
            continue
        if on:
            if not s.startswith("|"):
                on = False
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if not cells[0].startswith("---"):
                rows.append(cells)
    assert rows, first_header_cell
    return rows


# ---------------------------------------------------------------- charts
def chart_formats():
    """Section 2's five formats on one log time axis: a floating bar from the shortest to the longest
    time the table states. Ranges are parsed from the draft's table and asserted."""
    rows = {r[0]: r[1] for r in draft_table("Format")}
    MIN = {"minutes": 1, "hours": 60, "days": 1440}
    fmts = []
    for name, span in rows.items():
        m = re.fullmatch(r"(\d+) to (\d+) (minutes|hours|days)", span)
        assert m, span
        fmts.append((name, int(m.group(1)) * MIN[m.group(3)], int(m.group(2)) * MIN[m.group(3)], span))
    want = {"Paper LBO": (20, 30), "Timed Excel LBO": (60, 120), "Timed three statement plus DCF or LBO": (120, 240),
            "Take-home case": (1440, 7200), "Live build on a shared screen": (30, 90)}
    assert {n: (a, b) for n, a, b, _ in fmts} == want, fmts
    fmts.sort(key=lambda t: (t[1], t[2]))
    short = {"Timed three statement plus DCF or LBO": "Timed three statement\nplus DCF or LBO",
             "Live build on a shared screen": "Live build on a\nshared screen"}
    fig, ax = new_figure(width=11.0, height=5.6)
    ys = list(range(len(fmts)))[::-1]
    for y, (name, a, b, span) in zip(ys, fmts):
        hl = name == "Timed three statement plus DCF or LBO"
        ax.barh(y, b - a, left=a, height=0.5, color=ORANGE if hl else BLUE, linewidth=0)
        ax.annotate(span, (b, y), xytext=(8, 0), textcoords="offset points", va="center", ha="left",
                    fontsize=12, color=TEXT_PRIMARY)
    ax.set_xscale("log")
    ticks = [15, 30, 60, 120, 240, 480, 1440, 7200]
    ax.set_xticks(ticks)
    ax.set_xticklabels(["15 min", "30 min", "1 hr", "2 hr", "4 hr", "8 hr", "1 day", "5 days"])
    ax.minorticks_off()
    ax.set_xlim(12, 30000)
    ax.set_yticks(ys)
    ax.set_yticklabels([short.get(n, n) for n, *_ in fmts], fontsize=12.5)
    ax.set_ylim(-0.6, len(fmts) - 0.4)
    style_axes(ax, title="The format sets the clock, from 20 minutes on paper to five days at home")
    ax.grid(True, axis="x")
    ax.grid(False, axis="y")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=ORANGE, label="The format the worked example in section 5 uses"),
                       Patch(color=BLUE, label="The other four formats")],
              loc="upper center", bbox_to_anchor=(0.45, -0.1), ncol=2)
    ax.text(0.0, -0.24, "Time axis is logarithmic. The take-home runs on calendar days, not working hours.",
            transform=ax.transAxes, fontsize=10.5, color=TEXT_MUTED, ha="left", va="top")
    return cap_width(save_figure(fig, OUT / "01-five-formats-by-length.png"))


def chart_bridge():
    """Step 11: present values to enterprise value to equity value, from Table 11 (asserted)."""
    t = model.TABLES[11]["rows"]

    def num(label):
        s = t[label][0].replace(",", "").replace("$", "")
        return -float(s.strip("()")) if s.startswith("(") else float(s)

    pv, pvtv, ev = num("Sum of present values, FY2026E to FY2030E"), num("Present value of terminal value"), num("Enterprise value")
    debt, cash, nci, eq = num("Less: total debt"), num("Plus: cash"), num("Less: noncontrolling interest"), num("Equity value")
    assert abs(pv + pvtv - ev) < 0.051 and abs(ev + debt + cash + nci - eq) < 0.051
    # the same figures as the draft's table, checked line by line
    dt = {r[0]: r[1] for r in draft_table("Line") if r[0] in t}
    for label in ("Sum of present values, FY2026E to FY2030E", "Present value of terminal value", "Enterprise value",
                  "Less: total debt", "Plus: cash", "Less: noncontrolling interest", "Equity value",
                  "Implied share price ($)"):
        assert dt[label] == t[label][0], (label, dt.get(label), t[label][0])
    steps = [("PV of UFCF,\n2026E to 2030E", pv, "flow"), ("PV of\nterminal value", pvtv, "flow"),
             ("Enterprise\nvalue", ev, "total"), ("Less:\ntotal debt", debt, "flow"), ("Plus:\ncash", cash, "flow"),
             ("Less:\nnoncontrolling\ninterest", nci, "flow"), ("Equity\nvalue", eq, "total")]
    fig, ax = new_figure(width=11.0, height=6.2)
    bottoms, heights, colors, run = [], [], [], 0.0
    for label, v, kind in steps:
        if kind == "total":
            bottoms.append(0.0); heights.append(v); colors.append(GRAY); run = v
        else:
            bottoms.append(run if v >= 0 else run + v); heights.append(abs(v)); colors.append(BLUE if v >= 0 else ORANGE)
            run += v
    x = list(range(len(steps)))
    ax.bar(x, heights, bottom=bottoms, color=colors, width=0.62, linewidth=0)
    run = 0.0
    for i, (label, v, kind) in enumerate(steps[:-1]):
        run = v if kind == "total" else run + v
        ax.plot([i + 0.31, i + 0.69], [run, run], color=GRID, linewidth=1.0, zorder=1)
    for i, (label, v, kind) in enumerate(steps):
        top = bottoms[i] + heights[i]
        text = f"{v:,.1f}" if v >= 0 else f"({abs(v):,.1f})"
        if kind == "flow" and v > 0:
            text = "+" + text
        ax.annotate(text, (i, top), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom",
                    fontsize=12, color=TEXT_PRIMARY, fontweight="bold" if kind == "total" else "normal")
    share = t["Terminal value as a share of enterprise value"][0]
    assert share == "76.1%", share
    ax.annotate(f"{share}\nof EV", (1, pv + pvtv / 2), ha="center", va="center", fontsize=12,
                color="white", fontweight="bold")
    ax.annotate(f"{t['Implied share price ($)'][0]}\na share", (6, eq / 2),
                ha="center", va="center", fontsize=12, color="white", fontweight="bold")
    from matplotlib.ticker import FuncFormatter
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.0f}"))
    ax.set_xticks(x)
    ax.set_xticklabels([s[0] for s in steps], fontsize=11)
    ax.set_xlim(-0.55, len(steps) - 0.45)
    ax.set_ylim(0, 3000)
    style_axes(ax, title="Three quarters of Torvik's value sits in the terminal value", ylabel="$ millions")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=BLUE, label="Adds value"), Patch(color=ORANGE, label="Subtracts value"),
                       Patch(color=GRAY, label="Subtotal")], loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=3)
    return cap_width(save_figure(fig, OUT / "15-value-bridge.png"))


def chart_time_budget():
    """Section 6's time budget as an unrolled stacked bar: each block starts where the last one ends,
    on one 0:00 to 2:00 clock. Clock ranges parsed from the draft's table and asserted."""
    rows = draft_table("Clock")

    def mins(s):
        h, m = s.split(":")
        return int(h) * 60 + int(m)

    spans = []
    for r in rows:
        a, b = r[0].split(" to ")
        spans.append((mins(a), mins(b)))
    names = ["Read the prompt, list the outputs", "Inputs tab and scenario switch", "Operating build",
             "Working capital and PP&E", "Cost of debt, beta, WACC", "DCF to the share price", "Checks",
             "Sensitivity grid, flip the switch", "Formatting pass", "Save, reopen"]
    assert len(spans) == len(names) == 10
    assert spans[0][0] == 0 and spans[-1][1] == 120
    assert all(spans[i][1] == spans[i + 1][0] for i in range(len(spans) - 1)), spans
    assert [b - a for a, b in spans] == [8, 17, 20, 13, 12, 20, 8, 10, 9, 3], spans
    fig, ax = new_figure(width=11.0, height=6.4)
    ys = list(range(len(spans)))[::-1]
    for y, (a, b), name in zip(ys, spans, names):
        dcf = name.startswith("DCF")
        ax.barh(y, b - a, left=a, height=0.62, color=ORANGE if dcf else BLUE, linewidth=0)
        clock = f"{a // 60}:{a % 60:02d} to {b // 60}:{b % 60:02d}"
        ax.annotate(f"{b - a} min, {clock}", (b, y), xytext=(6, 0), textcoords="offset points", va="center",
                    ha="left", fontsize=11, color=TEXT_SECONDARY)
    ax.set_yticks(ys)
    ax.set_yticklabels(names, fontsize=12)
    ax.set_xticks([0, 15, 30, 45, 60, 75, 90, 105, 120])
    ax.set_xticklabels(["0:00", "0:15", "0:30", "0:45", "1:00", "1:15", "1:30", "1:45", "2:00"])
    ax.set_xlim(0, 145)
    ax.set_ylim(-0.6, len(spans) - 0.4)
    style_axes(ax, title="Have the DCF finished by 1:30, then spend the last half hour checking it")
    ax.grid(True, axis="x")
    ax.grid(False, axis="y")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=ORANGE, label="The DCF, the block that has to be done"),
                       Patch(color=BLUE, label="Every other block")],
              loc="upper center", bbox_to_anchor=(0.4, -0.08), ncol=2)
    return cap_width(save_figure(fig, OUT / "17-time-budget.png"))


# ---------------------------------------------------------------- main
def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.png"):
        old.unlink()
    print("building workbook")
    model.build()
    assert not model.no_dashes(XLSX), model.no_dashes(XLSX)
    mismatches, vals = model.check_against_article(XLSX)
    assert not mismatches, mismatches

    I, S, D, C = model.INP, model.SCH, model.DCF, model.COV

    print("drawing chart: formats")
    chart_formats()
    add("01-five-formats-by-length.png",
        "Horizontal range chart of the five modeling test formats by time, from paper LBO to take-home case",
        "Four of the five formats fit inside an afternoon, and the one to plan your prep around is the two to four "
        "hour three statement build with a valuation on top.",
        "chart from the section 2 formats table (Time column), log time axis",
        "| Live build on a shared screen | 30 to 90 minutes |")

    print("rendering screenshots")
    render("Inputs", f"B1:E{I['capex']}", "02-historicals-and-ratios.png")
    add("02-historicals-and-ratios.png",
        "Excel Inputs tab with Torvik's 2023 to 2025 income statement, margins, tax rate, D&A, EBITDA and capex",
        "Only the blue cells are typed. Every subtotal is a SUM and every ratio underneath is a formula, which is "
        "what lets you project the ratios instead of the dollars.",
        f"workbook torvik-dcf.xlsx, tab Inputs, range B1:E{I['capex']}",
        "| Capex (from the cash flow statement) | 48.0 | 50.0 | 54.0 |")

    render("Inputs", f"B{I['hdr2']}:E{I['m_am']}", "03-segment-build.png")
    add("03-segment-build.png",
        "Excel segment build with revenue, growth and mix for pumps, valves and controls, and aftermarket",
        "The check row under total revenue reads 0.0 in every year, and the growth rows show the story: aftermarket "
        "grows about 9 percent while pumps grow about 4.",
        f"workbook torvik-dcf.xlsx, tab Inputs, range B{I['hdr2']}:E{I['m_am']}",
        "| Aftermarket Parts and Service mix | 24.4% | 25.2% | 25.9% |")

    with tempfile.TemporaryDirectory() as td:
        a = render("Cover", f"B{C['hdr_switch']}:F{C['note'] - 1}", "", out=Path(td) / "a.png")
        b = render("Inputs", f"B{I['hdr3']}:I{I['a_pumps_live']}", "", out=Path(td) / "b.png",
                   hide_cols=("H",))
        stack([a, b], OUT / "04-scenario-switch.png")
    add("04-scenario-switch.png",
        "Close-up of the scenario switch cell on the Cover tab and the pumps growth row that reads it",
        "One cell on the Cover tab holds a 2 for Base. The live pumps row runs a CHOOSE on that cell, so it shows "
        "the Base numbers, and every projection points at the live row.",
        f"workbook torvik-dcf.xlsx, tab Cover range B{C['hdr_switch']}:F{C['switch']} stacked over tab Inputs range "
        f"B{I['hdr3']}:I{I['a_pumps_live']} (column H hidden)",
        "This is the block the scenario switch reads.")

    render("Inputs", f"B{I['hdr3']}:G{model.INP_LAST}", "05-assumptions-block.png")
    add("05-assumptions-block.png",
        "Excel assumptions block with Bear, Base and Bull rows and a shaded live row for each driver",
        "Three typed rows per driver and a fourth shaded row that picks one. The fixed drivers at the bottom, days, "
        "D&A, capex and tax, don't change with the scenario.",
        f"workbook torvik-dcf.xlsx, tab Inputs, range B{I['hdr3']}:G{model.INP_LAST}",
        "| Tax rate on EBIT (all cases) | 25.0% | 25.0% | 25.0% |")

    render("DCF", f"B1:J{D['capex']}", "06-operating-build.png")
    add("06-operating-build.png",
        "Excel operating build for 2023 to 2030 from segment revenue down to EBITDA and capex",
        "Historical columns are green links back to the Inputs tab and projected columns are black formulas. Revenue "
        "growth fades from 5.7 to 3.9 percent while EBITDA margin climbs to 19.0.",
        f"workbook torvik-dcf.xlsx, tab DCF, range B1:J{D['capex']}",
        "| Capex | 48.0 | 50.0 | 54.0 | 57.1 |")

    render("Schedules", f"B1:K{S['nwcpct']}", "07-working-capital.png")
    add("07-working-capital.png",
        "Excel working capital schedule with receivables, inventory, payables, net working capital and days from 2022 to 2030",
        "The bold (increase) / decrease row is the one that feeds free cash flow, and it's negative every year because "
        "a growing balance ties up cash.",
        f"workbook torvik-dcf.xlsx, tab Schedules, range B1:K{S['nwcpct']}",
        "| NWC as a percent of revenue |")

    render("Schedules", f"B{S['hdr_ppe']}:K{S['dapct']}", "08-ppe-roll-forward.png")
    add("08-ppe-roll-forward.png",
        "Excel PP&E roll-forward: beginning balance plus capex less depreciation equals ending balance, 2023 to 2030",
        "Four rows and one formula: 384.0 plus 48.0 minus 40.0 lands on 392.0 in 2023, and each ending balance "
        "becomes the next year's beginning.",
        f"workbook torvik-dcf.xlsx, tab Schedules, range B{S['hdr_ppe']}:K{S['dapct']}",
        "| D&A as a percent of revenue | 3.3% | 3.3% | 3.3% | 3.3% |")

    render("Cost of debt", f"B1:F{model.COD['note']}", "09-cost-of-debt.png")
    add("09-cost-of-debt.png",
        "Excel cost of debt tab with two tranches, weights by principal, 6.03 percent pre-tax and 4.52 percent after tax",
        "Weight each tranche by principal, add up principal times rate, divide by total debt: 6.03 percent before "
        "tax and 4.52 after.",
        f"workbook torvik-dcf.xlsx, tab Cost of debt, range B1:F{model.COD['note']}",
        "| After-tax cost of debt at a 25% tax rate |")

    render("Beta", f"B1:H{model.BET['relever']}", "10-beta.png")
    add("10-beta.png",
        "Excel beta tab with five peer betas unlevered, the 0.968 median and Torvik relevered at 1.096",
        "Unlever each peer, take the median of the five, then put Torvik's own 0.175 debt to equity back in to get "
        "a 1.096 beta.",
        f"workbook torvik-dcf.xlsx, tab Beta, range B1:H{model.BET['relever']}",
        "| Torvik relevered beta |")

    render("WACC", f"B1:C{model.WAC['wacc']}", "11-wacc.png")
    add("11-wacc.png",
        "Excel WACC tab building a 9.98 percent cost of equity and a 9.16 percent WACC",
        "Five inputs and one weighted average. The green cells are links to the Beta, Cost of debt and Cover tabs, so "
        "each one traces back to where it came from.",
        f"workbook torvik-dcf.xlsx, tab WACC, range B1:C{model.WAC['wacc']}",
        "| WACC | 9.16% |")

    render("DCF", f"B{D['hdr_fcf']}:J{D['pv']}", "12-ufcf-and-present-value.png")
    add("12-ufcf-and-present-value.png",
        "Excel block from EBIT to unlevered free cash flow, mid-year discount periods, discount factors and present values",
        "Tax is on EBIT, the working capital line comes in negative from the Schedules tab, and the mid-year periods "
        "run 0.50 to 4.50, so the five present values sum to 627.9.",
        f"workbook torvik-dcf.xlsx, tab DCF, range B{D['hdr_fcf']}:J{D['pv']}",
        "| Present value of UFCF |")

    render("DCF", f"B{D['hdr_fcf']}:L{D['pv']}", "13-formula-closeup.png",
           hide_cols=("C", "D", "E", "G", "H", "I", "J", "K"))
    add("13-formula-closeup.png",
        "Close-up of the 2026 unlevered free cash flow column in Excel with each row's formula written beside it",
        "What F2 would show in the 2026E column: tax is minus EBIT times the tax rate cell, working capital is a link, "
        "and the discount factor reads the WACC tab, with no typed number inside any formula.",
        f"workbook torvik-dcf.xlsx, tab DCF, rows {D['hdr_fcf']} to {D['pv']}, columns B, F and L "
        "(other year columns hidden; column L holds the 2026E formulas as text)",
        "Walk 2026E. EBIT is 211.1.")

    render("DCF", f"B{D['hdr_tv']}:C{D['evltm']}", "14-terminal-value-and-bridge.png")
    add("14-terminal-value-and-bridge.png",
        "Excel terminal value and bridge from enterprise value to equity value to a 38.45 dollar share price",
        "The terminal value is discounted five full years at 0.6450 even though the cash flows use mid-year, and "
        "the Gordon growth rows underneath bracket the answer at $34.67.",
        f"workbook torvik-dcf.xlsx, tab DCF, range B{D['hdr_tv']}:C{D['evltm']}",
        "| Current EV / LTM EBITDA (market, for reference) | 10.8x |")

    print("drawing chart: value bridge")
    chart_bridge()
    add("15-value-bridge.png",
        "Waterfall chart from present values and terminal value to enterprise value of 2,622.2 and equity value of 2,307.2",
        "The five years of cash flow are worth 627.9 and the terminal value 1,994.3, which is why the exit multiple "
        "is the assumption a grader argues with first.",
        "chart from the section 5, Step 11 terminal value and bridge table",
        "Then the bridge from the whole company to the shareholders.")

    render("Sensitivity", f"B1:H{model.SEN['first'] + 4}", "16-sensitivity-grid.png")
    add("16-sensitivity-grid.png",
        "Excel sensitivity grid of implied share price by WACC down the side and exit multiple across",
        "The shaded center cell matches the DCF at $38.45, and a half turn of multiple moves the price about twice "
        "as far as a half point of WACC.",
        f"workbook torvik-dcf.xlsx, tab Sensitivity, range B1:H{model.SEN['first'] + 4} (body written as values, "
        "labeled as a data table)",
        "| 10.16% | $33.40 |")

    print("drawing chart: time budget")
    chart_time_budget()
    add("17-time-budget.png",
        "Timeline bar chart of the two-hour modeling test budget, block by block, with the DCF from 1:10 to 1:30",
        "Lay the budget on one clock and the order is the point: the DCF is finished at 1:30, and everything after "
        "it is checking, sensitivities and cleanup.",
        "chart from the section 6 time budget table (Clock column)",
        "| 1:57 to 2:00 | Save with the filename the prompt asked for.")

    write_manifest(OUT, entries)
    from PIL import Image
    for e in entries:
        im = Image.open(OUT / e["file"])
        assert im.width <= 2200, (e["file"], im.width)
    print(f"wrote {len(entries)} images and manifest to {OUT}")


if __name__ == "__main__":
    main()
