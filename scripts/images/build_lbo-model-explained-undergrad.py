#!/usr/bin/env python3
"""Images for drafts/draft-lbo-model-explained-undergrad-v1.md (October 1, 2026).

Run from the repo root:  python3 scripts/images/build_lbo-model-explained-undergrad.py
Idempotent. Steps:
  1. rebuild scripts/images/models/targetco-lbo.xlsx (scripts/images/models/build_targetco_lbo.py)
  2. recalculate it with LibreOffice and check every printed value against the article's tables
     (sources and uses, operating model, cash flow, debt schedule, Year 1 average-balance figures,
     returns, both sensitivity grids, the paper LBO); the script stops on any mismatch
  3. render the Excel screenshots and draw the three charts into
     published/assets/images/lbo-model-explained-undergrad/
  4. write that folder's manifest.json
"""
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
sys.path.insert(0, str(ROOT / "scripts" / "images" / "models"))
from wsg_viz import (BLUE, DIVERGING, GRID, ORANGE, SURFACE, TEXT_MUTED, TEXT_PRIMARY, TEXT_SECONDARY,  # noqa: E402
                     bar_labels, new_figure, recalc_values, render_range, save_figure, style_axes, write_manifest)
import build_targetco_lbo as model  # noqa: E402

SLUG = "lbo-model-explained-undergrad"
OUT = ROOT / "published" / "assets" / "images" / SLUG
XLSX = model.OUT_XLSX
RED = DIVERGING[2]


# ---------------------------------------------------------------- 1. build
def build_workbook():
    path, R, P = model.build()
    print(f"built {path.relative_to(ROOT)}")
    return R, P


# ---------------------------------------------------------------- 2. check against the article
def f1(x):
    """One decimal, half up, with parentheses for negatives, the way the article prints it."""
    d = Decimal(str(x)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)
    s = f"{abs(d):,.1f}"
    return f"({s})" if d < 0 else s


def pct1(x):
    return str(Decimal(str(x * 100)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)) + "%"


def mult2(x):
    return str(Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)) + "x"


def mult1(x):
    return str(Decimal(str(x)).quantize(Decimal("0.1"), rounding=ROUND_HALF_UP)) + "x"


def i0(x):
    return str(Decimal(str(x)).quantize(Decimal("1"), rounding=ROUND_HALF_UP))


# The article's tables, transcribed from the draft (Section 5 and Section 7).
ARTICLE = {
    "sources_uses": {
        "uses": ["850.0", "150.0", "20.0", "10.0", "20.0", "1,050.0"],
        "sources": ["0.0", "450.0", "150.0", "450.0", "1,050.0"],
        "check": "0.0", "leverage": "6.0x", "equity_pct": "42.9%",
    },
    "operating": {
        "rev": ["500.0", "530.0", "561.8", "595.5", "631.2", "669.1"],
        "growth_row": [None, "6.0%", "6.0%", "6.0%", "6.0%", "6.0%"],
        "margin": ["20.0%", "20.5%", "21.0%", "21.5%", "22.0%", "22.5%"],
        "ebitda": ["100.0", "108.7", "118.0", "128.0", "138.9", "150.6"],
        "da": ["(15.0)", "(15.9)", "(16.9)", "(17.9)", "(18.9)", "(20.1)"],
        "ebit": ["85.0", "92.8", "101.1", "110.2", "119.9", "130.5"],
        "int_tlb": [None, "(36.0)", "(33.6)", "(30.6)", "(26.8)", "(22.3)"],
        "int_notes": [None, "(13.5)", "(13.5)", "(13.5)", "(13.5)", "(13.5)"],
        "fee_am": [None, "(2.0)", "(2.0)", "(2.0)", "(2.0)", "(2.0)"],
        "ebt": [None, "41.3", "52.0", "64.1", "77.6", "92.7"],
        "taxes": [None, "(10.3)", "(13.0)", "(16.0)", "(19.4)", "(23.2)"],
        "ni": [None, "30.9", "39.0", "48.1", "58.2", "69.5"],
    },
    "cash_flow": {
        "cf_ni": ["30.9", "39.0", "48.1", "58.2", "69.5"],
        "cf_da": ["15.9", "16.9", "17.9", "18.9", "20.1"],
        "cf_fee": ["2.0", "2.0", "2.0", "2.0", "2.0"],
        "cf_capex": ["(15.9)", "(16.9)", "(17.9)", "(18.9)", "(20.1)"],
        "cf_nwc": ["(3.0)", "(3.2)", "(3.4)", "(3.6)", "(3.8)"],
        "cfads": ["29.9", "37.8", "46.7", "56.6", "67.7"],
        "cf_mand": ["(4.5)", "(4.5)", "(4.5)", "(4.5)", "(4.5)"],
        "cf_sweep": ["(25.4)", "(33.3)", "(42.2)", "(52.1)", "(63.2)"],
        "cf_change": ["0.0", "0.0", "0.0", "0.0", "0.0"],
        "cash_end": ["20.0", "20.0", "20.0", "20.0", "20.0"],
    },
    "debt": {
        "tlb_beg": ["450.0", "420.1", "382.2", "335.5", "278.9"],
        "tlb_mand": ["(4.5)", "(4.5)", "(4.5)", "(4.5)", "(4.5)"],
        "tlb_sweep": ["(25.4)", "(33.3)", "(42.2)", "(52.1)", "(63.2)"],
        "tlb_end": ["420.1", "382.2", "335.5", "278.9", "211.2"],
        "nt_end": ["150.0", "150.0", "150.0", "150.0", "150.0"],
        "rv_end": ["0.0", "0.0", "0.0", "0.0", "0.0"],
        "debt_end": ["570.1", "532.2", "485.5", "428.9", "361.2"],
        "lev": ["5.25x", "4.51x", "3.79x", "3.09x", "2.40x"],
        "cov": ["2.19x", "2.50x", "2.90x", "3.44x", "4.20x"],
    },
    "year1_average_balance": {"alt_int": "34.8", "alt_cfads": "30.9", "alt_end": "419.1"},
    "returns": {"ret_ebitda": "150.6", "ret_mult": "10.0x", "ret_ev": "1,505.5", "ret_debt": "(361.2)", "ret_cash": "20.0",
                "ret_equity": "1,164.3", "ret_invested": "450.0", "moic": "2.59x", "irr": "20.9%", "irr_fn": "20.9%"},
    "grid_entry_exit": [
        ["28.1%", "32.3%", "36.0%", "39.4%", "42.4%"],
        ["19.8%", "23.7%", "27.2%", "30.3%", "33.2%"],
        ["13.9%", "17.6%", "20.9%", "23.9%", "26.6%"],
        ["9.4%", "13.0%", "16.2%", "19.0%", "21.7%"],
        ["5.8%", "9.3%", "12.4%", "15.1%", "17.7%"],
    ],
    "grid_lev_year": [
        ["17.7%", "17.5%", "17.3%", "17.0%", "16.6%"],
        ["19.4%", "19.2%", "18.8%", "18.4%", "18.0%"],
        ["21.9%", "21.5%", "20.9%", "20.4%", "19.9%"],
        ["25.5%", "24.8%", "24.0%", "23.2%", "22.4%"],
    ],
    "paper": {
        "pe": ["110", "120", "130", "140", "150"],
        "pebit": ["90", "100", "110", "120", "130"],
        "pint": ["40", "37", "33", "28", "23"],
        "pebt": ["50", "63", "77", "92", "107"],
        "pni": ["37.5", "47", "58", "69", "80"],
        "pfcf": ["40", "45", "60", "70", "80"],
        "pdebt_end": ["460", "415", "355", "285", "205"],
        "exit": {"x_ev": "1,200", "x_debt": "205", "x_equity": "995", "x_in": "300", "moic_rounded": "3.3x", "irr_rounded": "27.1%",
                 "moic_exact": "3.30x", "irr_exact": "27.0%"},
    },
}


def check_against_article(R, P):
    vals = recalc_values(XLSX)
    L, Q = vals["LBO"], vals["Paper LBO"]
    problems = []

    def cmp(where, got, want):
        if want is None:
            return
        if got != want:
            problems.append(f"{where}: workbook {got!r} vs article {want!r}")

    def lbo(name, col):
        return L.get(f"{col}{R[name]}")

    # sources and uses
    su = ARTICLE["sources_uses"]
    for name, want in zip(["u_eq", "u_debt", "u_txn", "u_fin", "u_cash", "u_total"], su["uses"]):
        cmp(f"S&U uses {name}", f1(lbo(name, "D")), want)
    for name, want in zip(["s_rev", "s_tlb", "s_notes", "s_equity", "s_total"], su["sources"]):
        cmp(f"S&U sources {name}", f1(lbo(name, "I")), want)
    cmp("S&U check", f1(lbo("su_check", "D")), su["check"])
    cmp("S&U leverage", mult1(lbo("su_lev", "D")), su["leverage"])
    cmp("S&U equity pct", pct1(lbo("su_check", "I")), su["equity_pct"])
    # operating model (D = Year 0 .. I = Year 5)
    for name, wants in ARTICLE["operating"].items():
        for col, want in zip("DEFGHI", wants):
            got = lbo(name, col)
            if want is None:
                continue
            cmp(f"operating {name} {col}", pct1(got) if "%" in want else f1(got), want)
    # cash flow (E..I)
    for name, wants in ARTICLE["cash_flow"].items():
        for col, want in zip("EFGHI", wants):
            cmp(f"cash flow {name} {col}", f1(lbo(name, col)), want)
    # debt schedule (E..I)
    for name, wants in ARTICLE["debt"].items():
        for col, want in zip("EFGHI", wants):
            got = lbo(name, col)
            cmp(f"debt {name} {col}", mult2(got) if want.endswith("x") else f1(got), want)
    # Year 1 average balance
    for name, want in ARTICLE["year1_average_balance"].items():
        cmp(f"average balance {name}", f1(lbo(name, "E")), want)
    # returns
    for name, want in ARTICLE["returns"].items():
        got = lbo(name, "D")
        if want.endswith("%"):
            got = pct1(got)
        elif want.endswith("x") and name == "moic":
            got = mult2(got)
        elif want.endswith("x"):
            got = mult1(got)
        else:
            got = f1(got)
        cmp(f"returns {name}", got, want)
    # grids
    for i, wants in enumerate(ARTICLE["grid_entry_exit"]):
        for col, want in zip("EFGHI", wants):
            cmp(f"grid entry/exit row {i} {col}", pct1(L.get(f"{col}{R['s1_first'] + i}")), want)
    cmp("grid entry/exit corner", pct1(L.get(f"D{R['s1_corner']}")), "20.9%")
    for i, wants in enumerate(ARTICLE["grid_lev_year"]):
        for col, want in zip("EFGHI", wants):
            cmp(f"grid leverage/year row {i} {col}", pct1(L.get(f"{col}{R['s2_first'] + i}")), want)
    cmp("grid leverage/year corner", pct1(L.get(f"D{R['s2_corner']}")), "20.9%")
    # paper LBO
    pa = ARTICLE["paper"]
    for name in ["pe", "pebit", "pint", "pebt", "pni", "pfcf", "pdebt_end"]:
        for j, (col, want) in enumerate(zip("DEFGH", pa[name])):
            got = Q.get(f"{col}{P[name]}")
            got = abs(got)
            got = f1(got) if (name == "pni" and j == 0) else i0(got)
            cmp(f"paper {name} {col}", got, want)
    ex = pa["exit"]
    exit_ev = Q.get("D%d" % P["x_ev"])
    cmp("paper exit EV", f"{int(round(exit_ev)):,}", ex["x_ev"])
    cmp("paper exit debt", i0(abs(Q.get(f"D{P['x_debt']}"))), ex["x_debt"])
    cmp("paper exit equity", i0(Q.get(f"D{P['x_equity']}")), ex["x_equity"])
    cmp("paper equity in", i0(Q.get(f"D{P['x_in']}")), ex["x_in"])
    cmp("paper MOIC rounded", mult1(Q.get(f"D{P['x_moic']}")), ex["moic_rounded"])
    cmp("paper IRR rounded", pct1(Q.get(f"D{P['x_irr']}")), ex["irr_rounded"])
    cmp("paper MOIC exact", mult2(Q.get(f"E{P['x_moic']}")), ex["moic_exact"])
    cmp("paper IRR exact", pct1(Q.get(f"E{P['x_irr']}")), ex["irr_exact"])
    # no error cells anywhere
    for sheet, cells in vals.items():
        for ref, v in cells.items():
            if isinstance(v, str) and (v.startswith("#") or v.startswith("Err")):
                problems.append(f"{sheet}!{ref} shows {v}")
    if problems:
        print("WORKBOOK DOES NOT MATCH THE ARTICLE:")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print("workbook checks: sources and uses, operating model, cash flow, debt schedule, Year 1 average balance, "
          "returns, both sensitivity grids and the paper LBO all match the article")
    return vals


# ---------------------------------------------------------------- 3a. screenshots
def render_hidden(xlsx, sheet, cell_range, out_png, hide_rows=(), hide_cols=()):
    """render_range on a temp copy with some rows or columns hidden (LibreOffice skips them in print)."""
    import shutil
    import tempfile
    from openpyxl import load_workbook
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "hidden.xlsx"
        shutil.copy(xlsx, tmp)
        wb = load_workbook(tmp)
        ws = wb[sheet]
        for r in hide_rows:
            ws.row_dimensions[r].hidden = True
        for c in hide_cols:
            ws.column_dimensions[c].hidden = True
        wb.save(tmp)
        return render_range(tmp, sheet, cell_range, out_png)


def render_screenshots(R, P):
    shots = {
        "02-sources-and-uses.png": ("LBO", f"B{R['su_header']}:I{R['su_end']}", {}),
        "03-operating-model.png": ("LBO", f"B{R['om_header']}:I{R['om_end']}", {}),
        "04-cash-flow-to-debt-paydown.png": ("LBO", f"B{R['cf_header']}:I{R['cf_end']}", {}),
        "05-debt-schedule.png": ("LBO", f"B{R['ds_header']}:I{R['ds_end']}",
                                 {"hide_rows": list(range(R["circ_echo"], R["alt_end"] + 1))}),
        "07-interest-formula-closeup.png": ("LBO", f"B{R['tlb_label']}:J{R['alt_end']}", {"hide_cols": ["F", "G", "H", "I"]}),
        "08-returns.png": ("LBO", f"B{R['ret_header']}:I{R['ret_end']}", {}),
        "10-sensitivity-entry-exit.png": ("LBO", f"B{R['s1_header']}:I{R['s1_end']}", {}),
        "11-sensitivity-leverage-exit-year.png": ("LBO", f"B{R['s2_header']}:I{R['s2_end']}", {}),
        "12-paper-lbo.png": ("Paper LBO", f"B{P['s1_header']}:H{P['ex_end']}", {}),
    }
    for fname, (sheet, rng, kw) in shots.items():
        out = OUT / fname
        if kw:
            render_hidden(XLSX, sheet, rng, out, **kw)
        else:
            render_range(XLSX, sheet, rng, out)
        print(f"rendered {fname}  ({sheet}!{rng})")
    return {k: v[1] for k, v in shots.items()}


# ---------------------------------------------------------------- 3b. charts
def esc(s):
    """Escape dollar signs so matplotlib never reads a pair of them as mathtext."""
    return s.replace("$", r"\$")


def chart_hilton_timeline():
    """Horizontal timeline of the intro's dated Hilton figures (the article's own numbers)."""
    fig, ax = new_figure(width=11.0, height=5.6)
    HI, LO = 2.1, 0.7   # label levels above and below the line
    events = [
        (2007 + 6 / 12, "Jul 2007", "Blackstone buys Hilton\nfor $26 billion, with\n$5.7 billion of equity", "deal", HI),
        (2008 + 8.5 / 12, "Sep 2008", "Lehman Brothers fails,\nbusiness travel dries up", "crisis", -HI),
        (2009 + 6 / 12, "2009", "Blackstone writes its\nstake down about 70%", "crisis", LO),
        (2010 + 3.5 / 12, "Apr 2010", "$819 million more equity;\ndebt cut from $20 billion\nto $16 billion", "crisis", -LO),
        (2013 + 11.5 / 12, "Dec 2013", "Hilton IPO, the largest\nhotel IPO on record", "deal", HI),
        (2018 + 4.5 / 12, "May 2018", "Last shares sold; total\nprofit about $14 billion", "deal", -HI),
    ]
    color = {"deal": BLUE, "crisis": ORANGE}
    ax.axhline(0, color="#b9b8b3", lw=1.6, zorder=1)
    for x, date, text, kind, y in events:
        ax.plot([x, x], [0, y], color="#c9c8c3", lw=1.0, zorder=1)
        ax.scatter([x], [0], s=150, color=color[kind], edgecolor=SURFACE, linewidth=2, zorder=3)
        lines = text.count("\n") + 1
        if y > 0:   # description sits on the leader, the bold date above it
            ax.text(x, y, esc(text), ha="center", va="bottom", fontsize=11.5, color=TEXT_SECONDARY, linespacing=1.2)
            ax.text(x, y + 0.30 * lines + 0.06, date, ha="center", va="bottom", fontsize=12.5, fontweight="bold", color=TEXT_PRIMARY)
        else:       # bold date hangs from the leader, the description under it
            ax.text(x, y, date, ha="center", va="top", fontsize=12.5, fontweight="bold", color=TEXT_PRIMARY)
            ax.text(x, y - 0.36, esc(text), ha="center", va="top", fontsize=11.5, color=TEXT_SECONDARY, linespacing=1.2)
    ax.set_xlim(2006.0, 2019.7)
    ax.set_ylim(-3.45, 3.45)
    ax.set_yticks([])
    ax.set_xticks(range(2007, 2019))
    ax.spines["left"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.grid(False)
    ax.tick_params(axis="x", length=0, labelsize=11.5, pad=6)
    ax.set_title(esc("Eleven years from a $26 billion buyout to a $14 billion profit"), loc="left", pad=14)
    from matplotlib.lines import Line2D
    handles = [Line2D([], [], marker="o", linestyle="", markersize=10, color=BLUE, label="Buy, IPO, sell"),
               Line2D([], [], marker="o", linestyle="", markersize=10, color=ORANGE, label="The crisis years")]
    ax.legend(handles=handles, loc="upper right", bbox_to_anchor=(1.0, 0.98), ncol=1)
    return save_figure(fig, OUT / "01-hilton-timeline.png")


def chart_debt_by_year(vals, R):
    """Stacked bars of the two tranches at close and each year end, from the debt schedule."""
    L = vals["LBO"]
    cols = "DEFGHI"
    tlb = [L[f"{c}{R['tlb_end']}"] for c in cols]
    notes = [L[f"{c}{R['nt_end']}"] for c in cols]
    total = [a + b for a, b in zip(tlb, notes)]
    lev = [L[f"{c}{R['lev']}"] for c in cols]
    labels = ["Close", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]
    fig, ax = new_figure(width=11.0, height=6.0)
    x = list(range(len(labels)))
    w = 0.46
    ax.bar(x, tlb, width=w, color=BLUE, label="Term Loan B (paid down by the sweep)", edgecolor=SURFACE, linewidth=2, zorder=2)
    ax.bar(x, notes, width=w, bottom=tlb, color=ORANGE, label="Senior notes (bullet, no paydown)", edgecolor=SURFACE, linewidth=2, zorder=2)
    for i, t in enumerate(total):
        ax.annotate(f"{t:,.1f}", (i, t), ha="center", va="bottom", xytext=(0, 4), textcoords="offset points",
                    fontsize=12, color=TEXT_PRIMARY, fontweight="bold")
    # the two ends carry the leverage multiple the article quotes (6.0x at close, 2.40x in Year 5)
    ax.annotate(f"{lev[0]:.1f}x EBITDA", (0, total[0]), ha="center", va="bottom", xytext=(0, 21), textcoords="offset points",
                fontsize=11, color=TEXT_SECONDARY)
    ax.annotate(f"{lev[5]:.2f}x EBITDA", (5, total[5]), ha="center", va="bottom", xytext=(0, 21), textcoords="offset points",
                fontsize=11, color=TEXT_SECONDARY)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(0, 720)
    ax.set_yticks(range(0, 701, 100))
    import matplotlib.ticker as mticker
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, p: f"{v:,.0f}"))
    style_axes(ax, title="Five years of cash sweep take total debt from 6.0x to 2.4x EBITDA", ylabel=esc("$ millions, end of year"))
    ax.legend(loc="upper right", ncol=1)
    return save_figure(fig, OUT / "06-debt-balance-by-year.png")


def chart_value_bridge(vals, R):
    """Waterfall from sponsor equity at close to exit equity, the Section 5 bridge."""
    L = vals["LBO"]
    equity_in = L[f"D{R['ret_invested']}"]
    ebitda_growth = (L[f"D{R['ret_ebitda']}"] - L[f"D{R['ltm_ebitda']}"]) * L[f"D{R['entry_mult']}"]
    debt_paydown = L[f"E{R['debt_total']}"] - (-L[f"D{R['ret_debt']}"])   # 600.0 less debt at exit
    multiple = (L[f"D{R['ret_mult']}"] - L[f"D{R['entry_mult']}"]) * L[f"D{R['ret_ebitda']}"]
    fees = -(L[f"D{R['txn_fees']}"] + L[f"D{R['fin_fees']}"])
    exit_equity = L[f"D{R['ret_equity']}"]
    assert abs(equity_in + ebitda_growth + debt_paydown + multiple + fees - exit_equity) < 0.05, "bridge does not tie"
    steps = [
        ("Sponsor equity\nat close", equity_in, "total"),
        ("EBITDA growth\n(50.6 x 10.0x)", ebitda_growth, "up"),
        ("Debt paydown\n(600.0 to 361.2)", debt_paydown, "up"),
        ("Exit multiple\n(10.0x in, 10.0x out)", multiple, "up"),
        ("Fees paid at close\n(never recovered)", fees, "down"),
        ("Exit equity\nvalue", exit_equity, "total"),
    ]
    fig, ax = new_figure(width=11.0, height=6.2)
    colors = {"total": TEXT_SECONDARY, "up": BLUE, "down": RED}
    running = 0.0
    w = 0.5
    for i, (label, v, kind) in enumerate(steps):
        if kind == "total":
            bottom, height = 0.0, v
            running = v
        else:
            bottom = running if v >= 0 else running + v
            height = abs(v)
            running += v
        ax.bar(i, height, width=w, bottom=bottom, color=colors[kind], edgecolor=SURFACE, linewidth=2, zorder=2)
        top = bottom + height
        txt = f"({abs(v):,.1f})" if kind == "down" else f"{v:,.1f}"
        ax.annotate(txt, (i, top), ha="center", va="bottom", xytext=(0, 4), textcoords="offset points",
                    fontsize=12.5, color=TEXT_PRIMARY, fontweight="bold")
        if i < len(steps) - 1:
            ax.plot([i + w / 2, i + 1 - w / 2], [running, running], color="#b9b8b3", lw=1.0, zorder=1)
    ax.set_xticks(range(len(steps)))
    ax.set_xticklabels([s[0] for s in steps], fontsize=11.5)
    ax.set_ylim(0, 1500)
    ax.set_yticks(range(0, 1401, 200))
    import matplotlib.ticker as mticker
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, p: f"{v:,.0f}"))
    style_axes(ax, title="Two-thirds of the gain is EBITDA growth, one-third is debt paydown", ylabel=esc("$ millions"))
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=BLUE, label="Adds to equity"), Patch(color=RED, label="Reduces equity"),
                       Patch(color=TEXT_SECONDARY, label="Equity value")], loc="upper left", ncol=3)
    return save_figure(fig, OUT / "09-value-creation-bridge.png")


# ---------------------------------------------------------------- 4. manifest
def manifest(ranges):
    wb = "scripts/images/models/targetco-lbo.xlsx"
    entries = [
        {"file": "01-hilton-timeline.png",
         "alt": "Timeline of Blackstone's Hilton buyout from July 2007 to the May 2018 exit with six dated events",
         "caption": "Hilton went from a $26 billion buyout to a 70 percent writedown to a $14 billion profit in eleven years, and every step of that story is a line in the model.",
         "method": "Chart drawn from the dated figures in the article's introduction (as written in the draft, including the figures still under VERIFY tags)",
         "anchor": "Why borrow so much? Because debt makes the equity work harde"},
        {"file": "02-sources-and-uses.png",
         "alt": "Excel screenshot of the TargetCo sources and uses table with the sponsor equity plug and a zero check cell",
         "caption": "Sponsor equity is the plug, so the check cell under the table reads 0.0 and the equity line moves whenever a fee or a loan does.",
         "method": f"Workbook {wb}, sheet LBO, range {ranges['02-sources-and-uses.png']}",
         "anchor": "| **Total uses** | **1,050.0** | **Total sources** | **1,050"},
        {"file": "03-operating-model.png",
         "alt": "Excel screenshot of the TargetCo operating model from revenue to net income over five projected years",
         "caption": "Revenue runs off one growth cell, EBITDA off a margin that steps up each year, and the two interest lines flow in from the debt schedule further down the sheet.",
         "method": f"Workbook {wb}, sheet LBO, range {ranges['03-operating-model.png']}",
         "anchor": "| Net income |  | 30.9 | 39.0 | 48.1 | 58.2 | 69.5 |"},
        {"file": "04-cash-flow-to-debt-paydown.png",
         "alt": "Excel screenshot of the cash flow block from net income to cash available for debt repayment and ending cash",
         "caption": "Net income is not the cash: D&A and the fee amortization come back, capex and the working capital build come out, and the line that is left is what the lenders get.",
         "method": f"Workbook {wb}, sheet LBO, range {ranges['04-cash-flow-to-debt-paydown.png']}",
         "anchor": "| Ending cash (minimum cash $20) | 20.0 | 20.0 | 20.0 | 20.0"},
        {"file": "05-debt-schedule.png",
         "alt": "Excel screenshot of the TargetCo debt schedule by tranche with term loan paydown, notes, revolver and leverage ratios",
         "caption": "Each tranche gets its own block: the term loan takes the mandatory 1 percent and then the whole sweep, the notes sit at $150.0 million collecting their coupon, and the revolver draw stays at zero because no year runs short.",
         "method": f"Workbook {wb}, sheet LBO, range {ranges['05-debt-schedule.png']} with the Circ and Year 1 average balance rows hidden",
         "anchor": "| EBITDA / cash interest | 2.19x | 2.50x | 2.90x | 3.44x | 4"},
        {"file": "06-debt-balance-by-year.png",
         "alt": "Stacked bar chart of TargetCo term loan and senior notes balances falling from 600 to 361 over five years",
         "caption": "The notes never move, so every dollar of paydown comes out of the term loan and total debt falls from 6.0x to 2.4x EBITDA.",
         "method": "Chart from the Section 5 debt schedule table (term loan and notes ending balances, total debt to EBITDA)",
         "anchor": "The term loan ends Year 1 at $450.0 minus $4.5 minus $25.44,"},
        {"file": "07-interest-formula-closeup.png",
         "alt": "Excel close-up of the term loan block with Year 1 formulas for the cash sweep and the Circ interest toggle",
         "caption": "The sweep is a MIN against the balance left, and the interest line is an IF on the Circ cell that swaps the beginning balance for the average, which is what moves Year 1 interest from 36.0 to 34.8.",
         "method": f"Workbook {wb}, sheet LBO, range {ranges['07-interest-formula-closeup.png']} with Years 2 to 5 hidden and the Year 1 formulas written as text in column J",
         "anchor": "Here is the term loan block with its Year 1 formulas written"},
        {"file": "08-returns.png",
         "alt": "Excel screenshot of the returns block with exit value, exit equity, MOIC of 2.59x and IRR of 20.9 percent",
         "caption": "Exit EBITDA times the same 10.0x, less the debt still outstanding, plus cash, is the equity; the MOIC formula and Excel's IRR function land on the same 20.9 percent.",
         "method": f"Workbook {wb}, sheet LBO, range {ranges['08-returns.png']}",
         "anchor": "| IRR (5 years) | 20.9% |"},
        {"file": "09-value-creation-bridge.png",
         "alt": "Waterfall chart bridging 450 of sponsor equity to 1,164 of exit equity through EBITDA growth, debt paydown and fees",
         "caption": "EBITDA growth and debt paydown explain all of the $714.3 million gain, the exit multiple adds nothing, and the $30.0 million of fees never comes back.",
         "method": "Chart from the Section 5 returns discussion (EBITDA growth $505.5, debt paydown $238.8, multiple $0.0, fees $30.0)",
         "anchor": "Where did the $714.3 million of equity gain come from? EBITD"},
        {"file": "10-sensitivity-entry-exit.png",
         "alt": "Excel screenshot of the IRR sensitivity grid for entry multiple against exit multiple, 8.0x to 12.0x",
         "caption": "Read down the 10.0x column: paying one turn less at entry adds about six points of IRR, more than any operating lever in this model.",
         "method": f"Workbook {wb}, sheet LBO, range {ranges['10-sensitivity-entry-exit.png']} (values computed in build_targetco_lbo.py the way the article's writer did, laid out as a data table)",
         "anchor": "| 12.0x | 5.8% | 9.3% | 12.4% | 15.1% | 17.7% |"},
        {"file": "11-sensitivity-leverage-exit-year.png",
         "alt": "Excel screenshot of the IRR sensitivity grid for leverage from 4.0x to 7.0x against exit years three to seven",
         "caption": "Each extra turn of leverage adds two to four points of IRR, while each extra year of holding trims it even as the MOIC keeps rising.",
         "method": f"Workbook {wb}, sheet LBO, range {ranges['11-sensitivity-leverage-exit-year.png']} (values computed in build_targetco_lbo.py the way the article's writer did, laid out as a data table)",
         "anchor": "| 7.0x | 25.5% | 24.8% | 24.0% | 23.2% | 22.4% |"},
        {"file": "12-paper-lbo.png",
         "alt": "Excel screenshot of the paper LBO with purchase price, five years of rounded cash flow and the exit returns",
         "caption": "The same five steps on one sheet: interest rounded to the nearest million, free cash flow to the nearest five, and the answer still lands within a tenth of a point of the exact 27.0 percent.",
         "method": f"Workbook {wb}, sheet Paper LBO, range {ranges['12-paper-lbo.png']}",
         "anchor": "| 5 | 150 | 130 | 23 | 107 | 80 | 80 | 205 |"},
    ]
    # anchors come from the draft itself when the image line is already in it: the first 60 characters
    # of the last non-blank line above the image line (the hardcoded values above are the fallback)
    draft = ROOT / "drafts" / "draft-lbo-model-explained-undergrad-v1.md"
    if draft.exists():
        lines = draft.read_text(encoding="utf-8").split("\n")
        for e in entries:
            idx = next((i for i, l in enumerate(lines) if l.startswith(f"![{e['alt']}](")), None)
            if idx is not None:
                j = idx - 1
                while j >= 0 and not lines[j].strip():
                    j -= 1
                if j >= 0:
                    e["anchor"] = lines[j][:60]
    for e in entries:
        for k in ("alt", "caption", "method", "anchor"):
            assert "—" not in e[k] and "–" not in e[k], f"dash in manifest {e['file']} {k}"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
    write_manifest(OUT, entries)
    print(f"wrote {OUT.relative_to(ROOT)}/manifest.json with {len(entries)} entries")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    R, P = build_workbook()
    vals = check_against_article(R, P)
    ranges = render_screenshots(R, P)
    chart_hilton_timeline()
    chart_debt_by_year(vals, R)
    chart_value_bridge(vals, R)
    manifest(ranges)


if __name__ == "__main__":
    main()
