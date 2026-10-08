#!/usr/bin/env python3
"""Images for drafts/draft-growth-equity-interview-guide-undergrads-v1.md (October 5, 2026).

Run from the repo root:  python3 scripts/images/build_growth-equity-interview-guide-undergrads.py
Idempotent. Steps:
  1. rebuild scripts/images/models/harborline-screen.xlsx (scripts/images/models/build_harborline_screen.py)
  2. recalculate it with LibreOffice and check every value against the article's tables, cell for
     cell as the article prints them: section 7 (ARR bridge, growth and retention, cost inputs, unit
     economics), section 8 (entry EV to ARR), section 9 (the round, the cap table), section 11
     (exits, payouts, MOIC and IRR, who gets what, the $500.0 million price check); stop on any mismatch
  3. render the five workbook screenshots and draw the comparison diagram, the MOIC chart and the
     Bear case exit waterfall into published/assets/images/growth-equity-interview-guide-undergrads/
  4. write that folder's manifest.json (file, alt, caption, method, anchor)

Nothing here edits the draft. The coordinator inserts the image lines with
scripts/images/insert_images.py from the manifest's anchors.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
sys.path.insert(0, str(ROOT / "scripts" / "images" / "models"))
from wsg_viz import (AQUA, BLUE, DIVERGING, ORANGE, SURFACE, TEXT_MUTED, TEXT_PRIMARY, TEXT_SECONDARY,  # noqa: E402
                     new_figure, recalc_values, render_range, save_figure, style_axes, write_manifest)
from wsg_diagrams import PALE_BLUE, PALE_GRAY, canvas, finish, label, text_box  # noqa: E402
import build_harborline_screen as model  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.rcParams["text.parse_math"] = False
matplotlib.rcParams["axes.unicode_minus"] = False

SLUG = "growth-equity-interview-guide-undergrads"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v1.md"
XLSX = model.OUT_XLSX
RED = DIVERGING[2]
GRAY = "#b9b8b3"


# ---------------------------------------------------------------- formatting, the way the article prints
def m(x):
    s = f"{abs(x):,.1f}"
    return f"(${s})" if round(x, 1) < 0 else f"${s}"


def pct(x, d=1):
    s = f"{abs(x) * 100:.{d}f}%"
    return f"({s})" if round(x * 100, d) < 0 else s


def mult(x, d=1):
    return f"{x:.{d}f}x"


def dollars(x):
    return f"${x:,.0f}"


def shares(x):
    return f"{x:,.0f}"


# ---------------------------------------------------------------- the article's tables, transcribed from the draft
ARTICLE = {
    "bridge": {"begin": "$40.0", "churn": "($4.0)", "exp": "$6.0", "new": "$18.0", "end": "$60.0", "net_new": "$20.0", "gross_new": "$24.0"},
    "retention": {"growth": "50.0%", "grr": "90.0%", "nrr": "105.0%"},
    "inputs": {"rev": "$50.0", "gm": "76.0%", "gp": "$38.0", "sm": "$20.0", "burn": "$5.0", "arr_cust": "$60,000", "cust": "1,000", "new_cust": "300"},
    "unit": {"cac": "$66,667", "payback": "13.2 months", "ltv": "$456,000", "ltv_cac": "6.8x", "magic": "1.00x", "burn_mult": "0.25x",
             "fcf": "(10.0%)", "r40": "40"},
    "deal": {"inv": "$100.0", "post": "$600.0", "pre": "$500.0", "own": "16.67%", "ev_arr": "10.0x", "pre_sh": "50,000,000",
             "pps": "$10.00", "new_sh": "10,000,000", "post_sh": "60,000,000"},
    # holder rows: shares before, % before, shares after, % after
    "cap": [("30,000,000", "60.0%", "30,000,000", "50.00%"), ("15,000,000", "30.0%", "15,000,000", "25.00%"),
            ("5,000,000", "10.0%", "5,000,000", "8.33%"), ("0", "0.0%", "10,000,000", "16.67%"),
            ("50,000,000", "100.0%", "60,000,000", "100.00%")],
    "scenarios": [("$90.0", "8.4%", "3.0x", "$270.0", "$45.0"), ("$240.0", "32.0%", "7.0x", "$1,680.0", "$280.0"),
                  ("$360.0", "43.1%", "9.0x", "$3,240.0", "$540.0")],
    "payout": [("$270.0", "$45.0", "$100.0", "$100.0", "preference", "$128.3"),
               ("$1,680.0", "$280.0", "$100.0", "$280.0", "convert to common", "$363.3"),
               ("$3,240.0", "$540.0", "$100.0", "$540.0", "convert to common", "$623.3")],
    "moic": [("0.45x", "(14.8%)", "1.00x", "0.0%", "1.28x", "5.1%"), ("2.80x", "22.9%", "2.80x", "22.9%", "3.63x", "29.4%"),
             ("5.40x", "40.1%", "5.40x", "40.1%", "6.23x", "44.2%")],
    "who": [("$270.0", "$100.0", "$170.0", "63.0%"), ("$1,680.0", "$280.0", "$1,400.0", "83.3%"), ("$3,240.0", "$540.0", "$2,700.0", "83.3%")],
    "price_check": {"own": "20.00%", "pay": "$336.0", "moic": "3.36x"},   # section 11, step 6: "20 percent ... $336.0 million, 3.36x"
}


# ---------------------------------------------------------------- 1 and 2. build and check
def build_and_check():
    path, M, D, R, G = model.build()
    print(f"built {path.relative_to(ROOT)}")
    vals = recalc_values(XLSX)
    Mt, Dl, Rt = vals["Metrics"], vals["Deal"], vals["Returns"]
    problems = []

    def cmp(where, got, want):
        if got != want:
            problems.append(f"{where}: workbook {got!r} vs article {want!r}")

    for k, want in ARTICLE["bridge"].items():
        cmp(f"bridge {k}", m(Mt[f"D{M[k]}"]), want)
    for k, want in ARTICLE["retention"].items():
        cmp(f"retention {k}", pct(Mt[f"D{M[k]}"]), want)
    fmt_in = {"rev": m, "gm": pct, "gp": m, "sm": m, "burn": m, "arr_cust": dollars, "cust": shares, "new_cust": shares}
    for k, want in ARTICLE["inputs"].items():
        cmp(f"input {k}", fmt_in[k](Mt[f"D{M[k]}"]), want)
    fmt_ue = {"cac": dollars, "payback": lambda v: f"{v:.1f} months", "ltv": dollars, "ltv_cac": mult,
              "magic": lambda v: mult(v, 2), "burn_mult": lambda v: mult(v, 2), "fcf": pct, "r40": lambda v: f"{v:.0f}"}
    for k, want in ARTICLE["unit"].items():
        cmp(f"unit economics {k}", fmt_ue[k](Mt[f"D{M[k]}"]), want)
    fmt_d = {"inv": m, "post": m, "pre": m, "own": lambda v: pct(v, 2), "ev_arr": mult, "pre_sh": shares,
             "pps": lambda v: f"${v:.2f}", "new_sh": shares, "post_sh": shares}
    for k, want in ARTICLE["deal"].items():
        cmp(f"deal {k}", fmt_d[k](Dl[f"D{D[k]}"]), want)
    for i, want in enumerate(ARTICLE["cap"]):
        row = D["cap_first"] + i
        got = (shares(Dl.get(f"D{row}", 0)), pct(Dl.get(f"E{row}", 0)), shares(Dl[f"F{row}"]), pct(Dl[f"G{row}"], 2))
        cmp(f"cap table row {i + 1}", got, want)
    cmp("founders shortcut", pct(Dl[f"G{D['cap_check']}"], 2), "50.00%")
    for i, want in enumerate(ARTICLE["scenarios"]):
        row = R["sc_first"] + i
        cmp(f"scenario row {i + 1}", (m(Rt[f"D{row}"]), pct(Rt[f"E{row}"]), mult(Rt[f"F{row}"]), m(Rt[f"G{row}"]), m(Rt[f"H{row}"])), want)
    for i, want in enumerate(ARTICLE["payout"]):
        row = R["po_first"] + i
        cmp(f"payout row {i + 1}", (m(Rt[f"D{row}"]), m(Rt[f"E{row}"]), m(Rt[f"F{row}"]), m(Rt[f"G{row}"]), Rt[f"H{row}"], m(Rt[f"I{row}"])), want)
    for i, want in enumerate(ARTICLE["moic"]):
        row = R["mo_first"] + i
        got = tuple(mult(Rt[f"{c}{row}"], 2) if c in "DFH" else pct(Rt[f"{c}{row}"]) for c in "DEFGHI")
        cmp(f"MOIC and IRR row {i + 1}", got, want)
    for i, want in enumerate(ARTICLE["who"]):
        row = R["wg_first"] + i
        cmp(f"who gets what row {i + 1}", (m(Rt[f"D{row}"]), m(Rt[f"E{row}"]), m(Rt[f"F{row}"]), pct(Rt[f"G{row}"])), want)
    pc = ARTICLE["price_check"]
    cmp("price check ownership", pct(Rt[f"E{R['pc_own']}"], 2), pc["own"])
    cmp("price check payout", m(Rt[f"E{R['pc_pay']}"]), pc["pay"])
    cmp("price check MOIC", mult(Rt[f"E{R['pc_moic']}"], 2), pc["moic"])
    # the numbers script agrees with the same cells (it is the article's source)
    for name, r_ in G["results"].items():
        i = [s[0] for s in G["scenarios"]].index(name)
        cmp(f"numbers script {name} participating", m(r_["participating"]), m(Rt[f"I{R['po_first'] + i}"]))
        cmp(f"numbers script {name} non-participating", m(r_["non_part"]), m(Rt[f"G{R['po_first'] + i}"]))
    for sheet, cells in vals.items():
        for ref, v in cells.items():
            if isinstance(v, str) and (v.startswith("#") or v.startswith("Err")):
                problems.append(f"{sheet}!{ref} shows {v}")
    if problems:
        print("WORKBOOK DOES NOT MATCH THE ARTICLE:")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print("workbook checks: ARR bridge, retention, cost inputs, unit economics, the round, the cap table, exits, payouts, "
          "MOIC and IRR, who gets what and the $500.0 million price check all match the article")
    return M, D, R, vals


# ---------------------------------------------------------------- 3a. screenshots
def render_screenshots(M, D, R):
    shots = {
        "02-arr-bridge-and-retention.png": ("Metrics", f"B{M['bridge_header']}:F{M['bridge_end']}"),
        "03-unit-economics.png": ("Metrics", f"B{M['ue_header']}:F{M['ue_end']}"),
        "04-round-and-cap-table.png": ("Deal", f"B{D['terms_header']}:G{D['cap_end']}"),
        "05-preference-formulas.png": ("Returns", f"B{R['fx_header']}:I{R['fx_end']}"),
        "06-exits-payouts-moic-irr.png": ("Returns", f"B{R['sc_header']}:I{R['mo_end']}"),
    }
    for fname, (sheet, rng) in shots.items():
        render_range(XLSX, sheet, rng, OUT / fname)
        print(f"rendered {fname}  ({sheet}!{rng})")
    return shots


# ---------------------------------------------------------------- 3b. charts
def diagram_three_strategies():
    """Venture, growth equity and buyout on four rows, every cell a phrase from section 1."""
    W, H = 11.0, 7.0
    fig, ax = canvas(W, H, title="Growth equity sits between venture and buyout")
    label(ax, 0.35, H - 0.88, "Venture pays for the chance that a product works; growth equity pays for proof that it already does.",
          size=12.5, color=TEXT_SECONDARY, va="top")
    x0, lw, cw, gap = 0.35, 1.45, 2.85, 0.12
    cols = [("Venture", PALE_GRAY, TEXT_PRIMARY),
            ("Growth equity", BLUE, "white"),
            ("Buyout", PALE_GRAY, TEXT_PRIMARY)]
    rows = [
        ("Company", ["A seed or Series A company: a team and an idea, product not yet proved",
                     "Real revenue, usually tens of millions, often growing 25 percent or more, profitable or close",
                     "A company growing 5 percent a year can still produce a 20 percent return"]),
        ("Stake", ["A Series A investor might own 20 percent",
                   "Usually 10 to 40 percent; the founder keeps control (Harborline: 16.67 percent)",
                   "Most or all of the equity; the firm can replace the CEO"]),
        ("Debt", [None,
                  "Usually none: the firm writes a check and no bank is involved",
                  "Borrowed money pays a big share of the price, and the company carries the loan"]),
        ("Returns come from", ["Most bets lose money and one big winner pays for the rest, so some positions need 20x or more",
                               "Revenue growth with the exit multiple holding; 3x and a 25 percent IRR is a normal target",
                               "Paying the loan down from cash flow and widening margins"]),
    ]
    top = H - 1.45
    hh = 0.55
    for j, (name, fill, ink) in enumerate(cols):
        cx = x0 + lw + gap + j * (cw + gap)
        text_box(ax, cx, top - hh, cw, hh, name, fill=fill, text_color=ink, size=14, bold=True)
    rh, rgap = 1.12, 0.1
    y = top - hh - rgap
    for rlabel, cells in rows:
        text_box(ax, x0, y - rh, lw, rh, rlabel, fill=SURFACE, edge=SURFACE, size=12.5, bold=True, ha="left", pad_in=0.02)
        for j, txt in enumerate(cells):
            cx = x0 + lw + gap + j * (cw + gap)
            fill = PALE_BLUE if j == 1 else PALE_GRAY
            if txt is None:
                text_box(ax, cx, y - rh, cw, rh, "Not covered in this guide", fill=SURFACE, edge=GRAY, size=11, text_color=TEXT_MUTED, lw=0.8)
            else:
                text_box(ax, cx, y - rh, cw, rh, txt, fill=fill, size=11.5)
        y -= rh + rgap
    return finish(fig, OUT / "01-venture-growth-buyout.png")


def chart_moic(vals, R):
    Rt = vals["Returns"]
    names = ["Bear", "Base", "Bull"]
    series = [("As plain common (no preference)", "D", BLUE), ("1x non-participating preferred", "F", ORANGE),
              ("1x participating preferred", "H", AQUA)]
    import numpy as np
    x = np.arange(len(names))
    bw = 0.26
    fig, ax = new_figure(width=11.0, height=6.2)
    for k, (lab, col, color) in enumerate(series):
        ys = [Rt[f"{col}{R['mo_first'] + i}"] for i in range(3)]
        bars = ax.bar(x + (k - 1) * bw, ys, width=bw, color=color, label=lab, edgecolor=SURFACE, linewidth=2, zorder=3)
        for b, v in zip(bars, ys):
            ax.annotate(f"{v:.2f}x", (b.get_x() + b.get_width() / 2, v), ha="center", va="bottom", xytext=(0, 4),
                        textcoords="offset points", fontsize=11.5, color=TEXT_PRIMARY)
    ax.axhline(1.0, color=TEXT_MUTED, lw=1.2, zorder=2, label="1.0x line: the firm gets its money back")
    ax.set_xticks(x)
    exits = [Rt["G%d" % (R["sc_first"] + i)] for i in range(3)]
    ax.set_xticklabels([f"{n} case\n{m(e)} million exit" for n, e in zip(names, exits)], fontsize=12)
    ax.set_ylim(0, 7.2)
    ax.set_yticks(range(0, 8))
    ax.set_yticklabels([f"{v}.0x" for v in range(0, 8)])
    style_axes(ax, title="The preference lifts the Bear case from 0.45x to 1.00x and leaves Base and Bull alone",
               ylabel="MOIC on the $100.0 million check, five-year hold")
    ax.legend(loc="upper left", ncol=1)
    return save_figure(fig, OUT / "07-moic-by-scenario.png")


def chart_bear_waterfall(vals, R):
    Rt = vals["Returns"]
    i = 0   # Bear row
    equity = Rt[f"D{R['po_first'] + i}"]
    to_pref = Rt[f"G{R['po_first'] + i}"]
    as_common = Rt[f"E{R['po_first'] + i}"]
    to_common = Rt[f"F{R['wg_first'] + i}"]
    share = Rt[f"G{R['wg_first'] + i}"]
    assert abs(equity - to_pref - to_common) < 1e-9
    steps = [("Equity value\nat exit", equity, "total"),
             ("1x preference, paid\nto the growth investor first", -to_pref, "down"),
             ("Left for founders,\nearlier VCs and employees", to_common, "net")]
    fig, ax = new_figure(width=10.0, height=6.0)
    colors = {"total": GRAY, "down": ORANGE, "net": BLUE}
    w = 0.5
    running = 0.0
    for k, (lab, v, kind) in enumerate(steps):
        if kind in ("total", "net"):
            bottom, height = 0.0, v
            running = v
        else:
            bottom, height = running + v, -v
            running += v
        ax.bar(k, height, width=w, bottom=bottom, color=colors[kind], edgecolor=SURFACE, linewidth=2, zorder=3)
        txt = f"({m(-v)})" if kind == "down" else m(v)
        ax.annotate(txt, (k, bottom + height), ha="center", va="bottom", xytext=(0, 4), textcoords="offset points",
                    fontsize=13, color=TEXT_PRIMARY, fontweight="bold")
        if k < len(steps) - 1:
            ax.plot([k + w / 2, k + 1 - w / 2], [running, running], color=GRAY, lw=1.0, zorder=2)
    # what the investor would have taken as plain common, marked inside the preference bar's span
    ax.plot([1 - w / 2, 1 + w / 2], [equity - as_common, equity - as_common], color=TEXT_PRIMARY, lw=1.6, zorder=4)
    ax.annotate(f"As plain common it would\nhave taken only {m(as_common)}", (1 + w / 2, equity - as_common), xytext=(14, -6),
                textcoords="offset points", ha="left", va="top", fontsize=11, color=TEXT_SECONDARY)
    ax.text(2, to_common - 14, f"{pct(share)} of\nthe exit", ha="center", va="top", fontsize=12, color="white", zorder=5)
    ax.set_xticks(range(len(steps)))
    ax.set_xticklabels([s[0] for s in steps], fontsize=12)
    ax.set_ylim(0, 320)
    ax.set_yticks(range(0, 301, 50))
    ax.set_yticklabels([f"${v:,}" for v in range(0, 301, 50)])
    style_axes(ax, title="In the Bear case the preference pays first, so the firm gets its $100.0 million back",
               ylabel="$ millions, Harborline sold for $270.0 million")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=GRAY, label="Exit equity value"), Patch(color=ORANGE, label="Paid to the preferred"),
                       Patch(color=BLUE, label="Paid to the common holders")], loc="upper right", ncol=1)
    return save_figure(fig, OUT / "08-bear-case-exit-waterfall.png")


# ---------------------------------------------------------------- 4. manifest
def manifest(shots):
    wb = "scripts/images/models/harborline-screen.xlsx"
    entries = [
        {"file": "01-venture-growth-buyout.png",
         "alt": "Comparison diagram of venture, growth equity and buyout by company stage, stake size, debt and source of returns",
         "caption": "Read across the Debt row: buyout borrows to pay the price, growth equity usually writes an all-equity check, so the only lever left is the revenue line.",
         "method": "Diagram from the article's section 1 text (stage, stake, debt and returns for each strategy, phrased as the article states them; the venture debt cell is marked as not covered)",
         "anchor": "**Buyout returns come from debt and margin; growth equity returns come from the revenue line.**"[:60]},
        {"file": "02-arr-bridge-and-retention.png",
         "alt": "Excel screenshot of the Harborline ARR bridge from 40 to 60 million with growth, gross and net retention",
         "caption": "Ending ARR is a SUM of the four bridge lines, and each retention figure is a ratio of two of them, which is why the bridge is the first thing an investor asks for.",
         "method": f"Workbook {wb}, sheet Metrics, range {shots['02-arr-bridge-and-retention.png'][1]}",
         "anchor": "| Net revenue retention | 105.0% | (40.0 minus 4.0 plus 6.0) divided by 40.0 |"[:60]},
        {"file": "03-unit-economics.png",
         "alt": "Excel screenshot of Harborline's cost inputs and unit economics, from CAC and payback to the Rule of 40",
         "caption": "Every metric in the lower block is a formula on the inputs above it, so changing churn or sales spend, as the week 2 drill asks, moves all eight at once.",
         "method": f"Workbook {wb}, sheet Metrics, range {shots['03-unit-economics.png'][1]}",
         "anchor": "| Rule of 40 score | 40 | 50.0% growth plus (10.0%) margin |"[:60]},
        {"file": "04-round-and-cap-table.png",
         "alt": "Excel screenshot of the Harborline Series C round terms and the cap table before and after the investment",
         "caption": "Price per share is pre-money over the old share count, and the founders' 60 percent becomes 50 percent without selling a share, the same answer as 60 percent times 500 over 600.",
         "method": f"Workbook {wb}, sheet Deal, range {shots['04-round-and-cap-table.png'][1]}",
         "anchor": "| Total | 50,000,000 | 100.0% | 60,000,000 | 100.00% |"[:60]},
        {"file": "05-preference-formulas.png",
         "alt": "Excel close-up of the Bear case payout row with each liquidation preference formula written out beside its value",
         "caption": "The non-participating payout is one line, the bigger of the preference and the as-converted share, capped at what the company sold for; participating adds the share on top of the preference.",
         "method": f"Workbook {wb}, sheet Returns, range {shots['05-preference-formulas.png'][1]} (the Bear row's formulas written as text beside their live values)",
         "anchor": "| Bull | $3,240.0 | $540.0 | $100.0 | $540.0 | convert to common | $623.3 |"[:60]},
        {"file": "06-exits-payouts-moic-irr.png",
         "alt": "Excel screenshot of the three Harborline exit scenarios, the payout to the preferred, and MOIC and IRR",
         "caption": "Only the blue inputs change between rows, ARR in year 5 and the exit multiple, and everything from equity value to the 22.9 percent Base case IRR follows from those two cells.",
         "method": f"Workbook {wb}, sheet Returns, range {shots['06-exits-payouts-moic-irr.png'][1]}",
         "anchor": "| Bull | 5.40x | 40.1% | 5.40x | 40.1% | 6.23x | 44.2% |"[:60]},
        {"file": "07-moic-by-scenario.png",
         "alt": "Grouped bar chart of MOIC in the Bear, Base and Bull cases as common, non-participating and participating preferred",
         "caption": "The orange bars match the blue ones in Base and Bull and only rise in Bear, while the green participating bars sit higher in every case, which is the $83.3 million founders fight over.",
         "method": "Chart from the section 11 MOIC and IRR table (0.45x, 2.80x, 5.40x as common; 1.00x, 2.80x, 5.40x non-participating; 1.28x, 3.63x, 6.23x participating)",
         "anchor": "**A 1x preference turns a 0.45x outcome into a 1.00x outcome and leaves the 2.80x"[:60]},
        {"file": "08-bear-case-exit-waterfall.png",
         "alt": "Waterfall chart of a 270 million Bear case exit, with 100 million to the preferred first and 170 million left",
         "caption": "At a $270.0 million sale the preference takes $100.0 million off the top instead of the $45.0 million the firm's 16.67 percent would have earned, and the common holders split the $170.0 million left.",
         "method": "Chart from the section 11 who-gets-what table, Bear row ($270.0 equity value, $100.0 to the preferred, $170.0 and 63.0 percent to the common), with the $45.0 as-common payout from the step 4 table",
         "anchor": "| Bull | $3,240.0 | $540.0 | $2,700.0 | 83.3% |"[:60]},
    ]
    bad = ("\u2014", "\u2013", "\u2212")
    lines = [l.strip() for l in DRAFT.read_text(encoding="utf-8").split("\n")] if DRAFT.exists() else []
    for e in entries:
        for key in ("alt", "caption", "method", "anchor"):
            assert not any(ch in e[key] for ch in bad), f"dash in manifest {e['file']} {key}"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
        assert (OUT / e["file"]).exists(), f"missing image {e['file']}"
        if lines and not any(l.startswith(e["anchor"]) for l in lines):
            print(f"  WARNING: anchor for {e['file']} not found in the draft: {e['anchor']!r}")
    write_manifest(OUT, entries)
    print(f"wrote {OUT.relative_to(ROOT)}/manifest.json with {len(entries)} entries")


def check_pngs():
    from PIL import Image
    for png in sorted(OUT.glob("*.png")):
        im = Image.open(png)
        if im.width > 2200:
            im = im.convert("RGB").resize((2200, round(im.height * 2200 / im.width)), Image.LANCZOS)
            im.save(png, "PNG", optimize=True, dpi=(200, 200))
        assert Image.open(png).width <= 2200, f"{png.name} is too wide"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    M, D, R, vals = build_and_check()
    shots = render_screenshots(M, D, R)
    diagram_three_strategies()
    chart_moic(vals, R)
    chart_bear_waterfall(vals, R)
    check_pngs()
    manifest(shots)


if __name__ == "__main__":
    main()
