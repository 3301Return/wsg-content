#!/usr/bin/env python3
"""Images for drafts/draft-investment-banking-analyst-salary-2027-v1.md (October 5, 2026).

Run from the repo root:  python3 scripts/images/build_investment-banking-analyst-salary-2027.py
Idempotent. Steps:
  1. rebuild scripts/images/models/analyst-takehome.xlsx (scripts/images/models/build_analyst_takehome.py)
  2. recalculate it with LibreOffice and check every printed value against the article's section 4
     tables (federal brackets, New York City brackets, the gross-to-net table) and the two New York
     State figures in the text ($10,760 schedule, $568 benefit); stop on any mismatch
  3. re-run the article's numbers script (scripts/images/models/numbers_investment-banking-analyst-salary-2027.py)
     and check its output against every article table a chart is drawn from (sections 2, 4, 6, 7, 8, 9)
  4. render the two workbook screenshots and draw the six charts into
     published/assets/images/investment-banking-analyst-salary-2027/
  5. write that folder's manifest.json (file, alt, caption, method, anchor)

Nothing here edits the draft. The coordinator inserts the image lines with
scripts/images/insert_images.py from the manifest's anchors.
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
sys.path.insert(0, str(ROOT / "scripts" / "images" / "models"))
from wsg_viz import (AQUA, BLUE, DIVERGING, ORANGE, SURFACE, TEXT_MUTED, TEXT_PRIMARY, TEXT_SECONDARY,  # noqa: E402
                     YELLOW, new_figure, recalc_values, render_range, save_figure, style_axes, write_manifest)
import build_analyst_takehome as model  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.rcParams["text.parse_math"] = False      # "$200,000" must never be read as mathtext
matplotlib.rcParams["axes.unicode_minus"] = False   # no Unicode minus signs anywhere

SLUG = "investment-banking-analyst-salary-2027"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v1.md"
XLSX = model.OUT_XLSX
RED = DIVERGING[2]
GRAY = "#b9b8b3"
GRAY_LIGHT = "#d9d8d4"
N = model.load_numbers()   # the article's numbers script, imported (no printing)
money, pct = N.money, N.pct


# ---------------------------------------------------------------- the article's tables, transcribed
ARTICLE = {
    # section 2: tier -> (AN1, AN2, AN3, bonus range, all-in range)
    "tiers": {
        "Bulge bracket": ("$110,000", "$125,000", "$135,000", "$45,000 to $100,000", "$155,000 to $210,000"),
        "Elite boutique": ("$120,000", "$130,000", "$140,000", "$50,000 to $110,000", "$170,000 to $230,000"),
        "Middle market": ("$105,000", "$115,000", "$125,000", "$35,000 to $75,000", "$140,000 to $180,000"),
        "Regional boutique": ("$90,000", "$100,000", "$110,000", "$15,000 to $50,000", "$105,000 to $140,000"),
    },
    # section 4: federal slices (dollars in slice, tax), then the total row
    "fed_slices": [("$12,400", "$1,240"), ("$38,000", "$4,560"), ("$55,300", "$12,166"), ("$78,200", "$18,768")],
    "fed_total": ("$183,900", "$36,734"),
    "nyc_slices": [("$12,000", "$369"), ("$13,000", "$489"), ("$25,000", "$955"), ("$142,000", "$5,504")],
    "nyc_total": ("$192,000", "$7,317"),
    "summary": {
        "base": "$120,000", "bonus": "$80,000", "gross": "$200,000", "std": "$16,100", "fed_taxable": "$183,900",
        "fed": "$36,734", "ss": "$11,439", "medicare": "$2,900", "addl": "$0", "ny_taxable": "$192,000",
        "nys": "$11,328", "nyc": "$7,317", "total_tax": "$69,718", "net": "$130,282", "net_share": "65.1%",
        "eff": "34.9%", "monthly": "$10,857",
    },
    "ny_schedule": "$10,760", "ny_benefit": "$568",
    # section 6: withheld, actual
    "bonus": {
        "fed": ("$17,600", "$19,164"), "ss": ("$4,960", "$3,999"), "med": ("$1,160", "$1,160"),
        "nys": ("$9,360", "$5,148"), "nyc": ("$3,400", "$3,101"),
        "total": ("45.6% = $36,480", "40.7% = $32,572"), "keep": ("$43,520", "$47,428"),
    },
    # section 7: city -> (fed, fica, state, city, sdi, total, net, monthly, eff, gap)
    "cities": {
        "NYC": ("$36,734", "$14,339", "$11,328", "$7,317", "$0", "$69,718", "$130,282", "$10,857", "34.9%", "$0"),
        "Charlotte": ("$36,734", "$14,339", "$7,471", "$0", "$0", "$58,544", "$141,456", "$11,788", "29.3%", "$11,174"),
        "Houston": ("$36,734", "$14,339", "$0", "$0", "$0", "$51,073", "$148,927", "$12,411", "25.5%", "$18,645"),
        "San Francisco": ("$36,734", "$14,339", "$14,211", "$0", "$2,600", "$67,884", "$132,116", "$11,010", "33.9%", "$1,834"),
    },
    # section 8: column -> (rent, utilities, transit, groceries, going out, insurance, flights, total, left, rate)
    "budget_takehome": "$10,114",
    "budget": {
        "Shared, careful": ("$2,500", "$200", "$152", "$600", "$400", "$100", "$250", "$4,202", "$5,912", "58.5%"),
        "Shared, typical": ("$2,500", "$200", "$152", "$900", "$1,000", "$100", "$400", "$5,252", "$4,862", "48.1%"),
        "Studio, typical": ("$3,800", "$250", "$152", "$900", "$1,000", "$100", "$400", "$6,602", "$3,512", "34.7%"),
    },
    # section 9: year -> (base, bonus, all-in, taxes, net, eff, step)
    "years": {
        "First-year analyst": ("$110,000", "$75,000", "$185,000", "$64,434", "$120,566", "34.8%", ""),
        "Second-year analyst": ("$125,000", "$100,000", "$225,000", "$79,727", "$145,273", "35.4%", "$24,708"),
        "Third-year analyst": ("$135,000", "$130,000", "$265,000", "$99,395", "$165,605", "37.5%", "$20,332"),
        "First-year associate (direct promote)": ("$175,000", "$120,000", "$295,000", "$113,614", "$181,386", "38.5%", "$15,781"),
    },
}

YEAR_INPUTS = {
    "First-year analyst": (110_000, 75_000),
    "Second-year analyst": (125_000, 100_000),
    "Third-year analyst": (135_000, 130_000),
    "First-year associate (direct promote)": (175_000, 120_000),
}
BUDGET_INPUTS = {
    "Shared, careful": (2_500, 200, 152, 600, 400, 100, 250),
    "Shared, typical": (2_500, 200, 152, 900, 1_000, 100, 400),
    "Studio, typical": (3_800, 250, 152, 900, 1_000, 100, 400),
}


# ---------------------------------------------------------------- 1 and 2. workbook
def build_and_check_workbook():
    path, R = model.build()
    print(f"built {path.relative_to(ROOT)}")
    vals = recalc_values(XLSX)
    T = vals["Take-home"]
    problems = []

    def cmp(where, got, want):
        if got != want:
            problems.append(f"{where}: workbook {got!r} vs article {want!r}")

    for i, (dollars, tax) in enumerate(ARTICLE["fed_slices"]):
        row = R["fed_first"] + i
        cmp(f"federal slice {i + 1} dollars", money(T[f"G{row}"]), dollars)
        cmp(f"federal slice {i + 1} tax", money(T[f"H{row}"]), tax)
    for row in range(R["fed_first"] + 4, R["fed_last"] + 1):   # the three untouched brackets
        cmp(f"federal row {row} untouched", money(T.get(f"H{row}", 0)), "$0")
    cmp("federal total dollars", money(T[f"G{R['fed_total']}"]), ARTICLE["fed_total"][0])
    cmp("federal total tax", money(T[f"H{R['fed_total']}"]), ARTICLE["fed_total"][1])
    for i, (dollars, tax) in enumerate(ARTICLE["nyc_slices"]):
        row = R["nyc_first"] + i
        cmp(f"NYC slice {i + 1} dollars", money(T[f"G{row}"]), dollars)
        cmp(f"NYC slice {i + 1} tax", money(T[f"H{row}"]), tax)
    cmp("NYC total dollars", money(T[f"G{R['nyc_total']}"]), ARTICLE["nyc_total"][0])
    cmp("NYC total tax", money(T[f"H{R['nyc_total']}"]), ARTICLE["nyc_total"][1])
    S = ARTICLE["summary"]
    for name, key in [("base", "base"), ("bonus", "bonus"), ("gross", "gross"), ("std", "std"), ("fed_taxable", "fed_taxable"),
                      ("fed_total", "fed"), ("ss", "ss"), ("med", "medicare"), ("addl", "addl"), ("ny_taxable", "ny_taxable"),
                      ("nys_tax", "nys"), ("nyc_total", "nyc"), ("total_tax", "total_tax"), ("net", "net"), ("monthly", "monthly")]:
        cmp(f"summary {key}", money(T.get(f"H{R[name]}", 0)), S[key])
    cmp("summary net share", pct(T[f"H{R['net_share']}"]), S["net_share"])
    cmp("summary effective rate", pct(T[f"H{R['eff']}"]), S["eff"])
    cmp("NY schedule reference", money(T[f"H{R['ny_sched']}"]), ARTICLE["ny_schedule"])
    cmp("NY phased-out benefit", money(T[f"H{R['ny_benefit']}"]), ARTICLE["ny_benefit"])
    cmp("NY schedule sheet total", money(vals["NY schedule"]["H15"]), ARTICLE["ny_schedule"])
    for sheet, cells in vals.items():
        for ref, v in cells.items():
            if isinstance(v, str) and (v.startswith("#") or v.startswith("Err")):
                problems.append(f"{sheet}!{ref} shows {v}")
    if problems:
        print("WORKBOOK DOES NOT MATCH THE ARTICLE:")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print("workbook checks: federal bracket table, NYC bracket table, gross-to-net table, NY schedule and benefit all match the article")
    return R


# ---------------------------------------------------------------- 3. the numbers script against the chart tables
def check_numbers_script():
    """Every chart is drawn from the numbers script's output, so that output must match the article first."""
    problems = []

    def cmp(where, got, want):
        if got != want:
            problems.append(f"{where}: script {got!r} vs article {want!r}")

    # section 2 tiers
    for tier, (b1, b2, b3, lo, mid, hi) in N.PAY_SCALE.items():
        want = ARTICLE["tiers"][tier]
        cmp(f"tier {tier} bases", (money(b1), money(b2), money(b3)), want[:3])
        cmp(f"tier {tier} bonus range", f"{money(lo)} to {money(hi)}", want[3])
        cmp(f"tier {tier} all-in range", f"{money(b1 + lo)} to {money(b1 + hi)}", want[4])
    # section 4 gross to net
    r = N.take_home(120_000, 80_000, "NYC")
    S = ARTICLE["summary"]
    cmp("S4 fed", money(r["fed"]), S["fed"]); cmp("S4 ss", money(r["ss"]), S["ss"]); cmp("S4 medicare", money(r["medicare"]), S["medicare"])
    cmp("S4 state", money(r["state"]), S["nys"]); cmp("S4 city", money(r["local"]), S["nyc"])
    cmp("S4 total", money(r["total_tax"]), S["total_tax"]); cmp("S4 net", money(r["net"]), S["net"])
    # section 6 bonus
    bonus, base = 80_000, 120_000
    w = {"fed": N.FED_SUPP_WITHHOLDING * bonus, "ss": N.SS_RATE * bonus, "med": N.MEDICARE_RATE * bonus,
         "nys": N.NYS_SUPP_WITHHOLDING * bonus, "nyc": N.NYC_SUPP_WITHHOLDING * bonus}
    with_b, without_b = N.take_home(base, bonus, "NYC"), N.take_home(base, 0, "NYC")
    a = {"fed": with_b["fed"] - without_b["fed"], "ss": with_b["ss"] - without_b["ss"],
         "med": (with_b["medicare"] + with_b["addl_medicare"]) - (without_b["medicare"] + without_b["addl_medicare"]),
         "nys": with_b["state"] - without_b["state"], "nyc": with_b["local"] - without_b["local"]}
    for k in ("fed", "ss", "med", "nys", "nyc"):
        cmp(f"S6 {k}", (money(w[k]), money(a[k])), ARTICLE["bonus"][k])
    tw, ta = sum(w.values()), sum(a.values())
    cmp("S6 total", (f"{pct(tw / bonus)} = {money(tw)}", f"{pct(ta / bonus)} = {money(ta)}"), ARTICLE["bonus"]["total"])
    cmp("S6 keep", (money(bonus - tw), money(bonus - ta)), ARTICLE["bonus"]["keep"])
    # section 7 cities
    res = {c: N.take_home(120_000, 80_000, c) for c in ARTICLE["cities"]}
    for c, want in ARTICLE["cities"].items():
        x = res[c]
        got = (money(x["fed"]), money(x["ss"] + x["medicare"] + x["addl_medicare"]), money(x["state"]), money(x["local"]),
               money(x["sdi"]), money(x["total_tax"]), money(x["net"]), money(x["net_monthly"]), pct(x["eff_rate"]),
               money(x["net"] - res["NYC"]["net"]))
        cmp(f"S7 {c}", got, want)
    # section 8 budget
    b = N.take_home(120_000, 80_000, "NYC", k401_pct=0.06, health=N.HEALTH_PREMIUM_SINGLE)
    cmp("S8 take-home per month", money(b["net_monthly"]), ARTICLE["budget_takehome"])
    for col, items in BUDGET_INPUTS.items():
        total = sum(items)
        left = b["net_monthly"] - total
        got = tuple(money(v) for v in items) + (money(total), money(left), pct(left / b["net_monthly"]))
        cmp(f"S8 {col}", got, ARTICLE["budget"][col])
    # section 9 years
    prev = None
    for label, (bs, bn) in YEAR_INPUTS.items():
        x = N.take_home(bs, bn, "NYC")
        step = "" if prev is None else money(x["net"] - prev)
        got = (money(bs), money(bn), money(x["gross"]), money(x["total_tax"]), money(x["net"]), pct(x["eff_rate"]), step)
        cmp(f"S9 {label}", got, ARTICLE["years"][label])
        prev = x["net"]
    if problems:
        print("NUMBERS SCRIPT DOES NOT MATCH THE ARTICLE:")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print("numbers script checks: sections 2, 4, 6, 7, 8 and 9 tables all reproduce")
    return {"base_case": r, "with_deductions": b, "cities": res, "bonus_withheld": w, "bonus_actual": a}


# ---------------------------------------------------------------- 4a. screenshots
def render_screenshots(R):
    shots = {
        "02-federal-bracket-math.png": f"B{R['pay_header']}:H{R['fica_total']}",
        "03-new-york-state-and-city-tax.png": f"B{R['nys_header']}:H{R['th_end']}",
    }
    for fname, rng in shots.items():
        render_range(XLSX, "Take-home", rng, OUT / fname)
        print(f"rendered {fname}  (Take-home!{rng})")
    return shots


# ---------------------------------------------------------------- 4b. charts
def k(v):
    return f"${v / 1000:,.0f}k"


def chart_base_by_tier():
    """Horizontal bars: first-year base by tier, with the first-year bonus range floating on top of it."""
    tiers = list(N.PAY_SCALE.keys())
    fig, ax = new_figure(width=11.0, height=5.6)
    ys = list(range(len(tiers)))[::-1]
    h = 0.52
    for y, tier in zip(ys, tiers):
        b1, _, _, lo, _, hi = N.PAY_SCALE[tier]
        ax.barh(y, b1, height=h, color=BLUE, zorder=3)
        ax.barh(y, hi - lo, left=b1 + lo, height=h, color=ORANGE, zorder=3)
        ax.plot([b1, b1 + lo], [y, y], color=ORANGE, lw=1.2, ls=(0, (2, 3)), zorder=2)
        ax.text(b1 - 3_000, y, f"{money(b1)} base", ha="right", va="center", fontsize=12, color="white", fontweight="bold", zorder=4)
        ax.text(b1 + hi + 3_000, y, f"all-in {money(b1 + lo)} to {money(b1 + hi)}", ha="left", va="center", fontsize=11.5,
                color=TEXT_PRIMARY, zorder=4)
    ax.set_yticks(ys)
    ax.set_yticklabels(tiers, fontsize=12.5)
    ax.set_xlim(0, 300_000)
    ax.set_xticks(range(0, 300_001, 50_000))
    ax.set_xticklabels([k(v) for v in range(0, 300_001, 50_000)])
    style_axes(ax, title="Base is set by your bank's tier; the bonus range is where the spread comes from",
               xlabel="First-year pay, 2026 scale", ygrid_only=False)
    ax.grid(True, axis="x"); ax.grid(False, axis="y")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=BLUE, label="First-year base"), Patch(color=ORANGE, label="First-year bonus range (bottom to top bucket)")],
              loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=2)
    return save_figure(fig, OUT / "01-first-year-base-by-tier.png")


def chart_gross_to_net(r):
    steps = [
        ("Gross pay", r["gross"], "total"),
        ("Federal\nincome tax", -r["fed"], "down"),
        ("Social Security\nand Medicare", -(r["ss"] + r["medicare"] + r["addl_medicare"]), "down"),
        ("New York\nState", -r["state"], "down"),
        ("New York\nCity", -r["local"], "down"),
        ("Take-home", r["net"], "net"),
    ]
    assert abs(sum(v for _, v, kd in steps if kd == "down") + r["gross"] - r["net"]) < 0.01
    fig, ax = new_figure(width=11.0, height=6.2)
    colors = {"total": GRAY, "down": RED, "net": BLUE}
    running, w = 0.0, 0.56
    for i, (label, v, kind) in enumerate(steps):
        if kind in ("total", "net"):
            bottom, height = 0.0, v
            running = v
        else:
            bottom, height = running + v, -v
            running += v
        ax.bar(i, height, width=w, bottom=bottom, color=colors[kind], edgecolor=SURFACE, linewidth=2, zorder=3)
        top = bottom + height
        txt = money(v) if kind != "down" else f"({money(-v)})"
        ax.annotate(txt, (i, top), ha="center", va="bottom", xytext=(0, 4), textcoords="offset points",
                    fontsize=12.5, color=TEXT_PRIMARY, fontweight="bold" if kind != "down" else "normal")
        if kind == "down":
            ax.annotate(f"{pct(-v / r['gross'])} of gross", (i, top), ha="center", va="bottom", xytext=(0, 20),
                        textcoords="offset points", fontsize=10.5, color=TEXT_SECONDARY)
        if i < len(steps) - 1:
            ax.plot([i + w / 2, i + 1 - w / 2], [running, running], color=GRAY, lw=1.0, zorder=2)
    ax.set_xticks(range(len(steps)))
    ax.set_xticklabels([s[0] for s in steps], fontsize=11.5)
    ax.set_ylim(0, 230_000)
    ax.set_yticks(range(0, 200_001, 50_000))
    ax.set_yticklabels([k(v) for v in range(0, 200_001, 50_000)])
    style_axes(ax, title="A $200,000 analyst in New York City keeps $130,282, about 65 cents of each dollar",
               ylabel="Dollars a year, single filer, 2026 rules")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=GRAY, label="Gross pay"), Patch(color=RED, label="Tax taken out"), Patch(color=BLUE, label="Take-home")],
              loc="upper right", ncol=3)
    return save_figure(fig, OUT / "04-gross-to-net-new-york.png")


def chart_four_cities(res):
    order = sorted(res.keys(), key=lambda c: -res[c]["net"])
    names = {"NYC": "New York", "Charlotte": "Charlotte", "Houston": "Houston", "San Francisco": "San Francisco"}
    fig, ax = new_figure(width=11.0, height=5.6)
    ys = list(range(len(order)))[::-1]
    h = 0.56
    for y, c in zip(ys, order):
        x = res[c]
        segs = [
            (x["net"], BLUE, "net"),
            (x["fed"] + x["ss"] + x["medicare"] + x["addl_medicare"], GRAY_LIGHT, "fed"),
            (x["state"], ORANGE, "state"),
            (x["local"] + x["sdi"], AQUA, "city"),
        ]
        left = 0.0
        for v, color, kind in segs:
            if v <= 0:
                continue
            ax.barh(y, v, left=left, height=h, color=color, edgecolor=SURFACE, linewidth=2, zorder=3)
            mid = left + v / 2
            if kind == "net":
                ax.text(mid, y, f"{money(v)} take-home", ha="center", va="center", fontsize=12.5, color="white", fontweight="bold", zorder=4)
            elif kind == "fed":
                ax.text(mid, y, f"{money(v)} federal", ha="center", va="center", fontsize=11.5, color=TEXT_PRIMARY, zorder=4)
            left += v
        gap = x["net"] - res["NYC"]["net"]
        detail = []
        detail.append(f"state {money(x['state'])}" if x["state"] else "no state income tax")
        if x["local"]:
            detail.append(f"city {money(x['local'])}")
        elif x["sdi"]:
            detail.append(f"disability insurance {money(x['sdi'])}")
        else:
            detail.append("no city tax")
        tag = ", ".join(detail) + "\n" + ("the baseline" if c == "NYC" else f"{money(gap)} more than New York")
        ax.text(left + 2_500, y, tag, ha="left", va="center", fontsize=11, color=TEXT_SECONDARY, linespacing=1.3)
    ax.set_yticks(ys)
    ax.set_yticklabels([names[c] for c in order], fontsize=12.5)
    ax.set_xlim(0, 262_000)
    ax.set_xticks(range(0, 200_001, 50_000))
    ax.set_xticklabels([k(v) for v in range(0, 200_001, 50_000)])
    style_axes(ax, title="The same $200,000 keeps $18,645 more in Houston than in New York, all of it state and city tax",
               xlabel="Where $200,000 of gross pay goes, single filer, 2026 rules", ygrid_only=False)
    ax.grid(True, axis="x"); ax.grid(False, axis="y")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=BLUE, label="Take-home"), Patch(color=GRAY_LIGHT, label="Federal income tax plus Social Security and Medicare (identical everywhere)"),
                       Patch(color=ORANGE, label="State income tax"), Patch(color=AQUA, label="City income tax or state disability insurance")],
              loc="upper center", bbox_to_anchor=(0.5, -0.16), ncol=2, fontsize=11)
    return save_figure(fig, OUT / "05-same-pay-four-cities.png")


def chart_bonus_withholding(w, a):
    keys = ["fed", "ss", "med", "nys", "nyc"]
    labels = ["Federal\nincome tax", "Social\nSecurity", "Medicare", "New York\nState", "New York\nCity"]
    fig, ax = new_figure(width=11.0, height=6.0)
    import numpy as np
    x = np.arange(len(keys))
    bw = 0.36
    b1 = ax.bar(x - bw / 2, [w[k_] for k_ in keys], width=bw, color=BLUE, label="Withheld from the bonus check", zorder=3,
                edgecolor=SURFACE, linewidth=2)
    b2 = ax.bar(x + bw / 2, [a[k_] for k_ in keys], width=bw, color=ORANGE, label="Tax the bonus actually adds for the year", zorder=3,
                edgecolor=SURFACE, linewidth=2)
    for bars in (b1, b2):
        for b in bars:
            ax.annotate(money(b.get_height()), (b.get_x() + b.get_width() / 2, b.get_height()), ha="center", va="bottom",
                        xytext=(0, 4), textcoords="offset points", fontsize=11.5, color=TEXT_PRIMARY)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=12)
    ax.set_ylim(0, 23_000)
    ax.set_yticks(range(0, 20_001, 5_000))
    ax.set_yticklabels([k(v) for v in range(0, 20_001, 5_000)])
    tw, ta = sum(w.values()), sum(a.values())
    style_axes(ax, ylabel="Per $80,000 bonus, New York City first-year")
    ax.set_title(f"Payroll withholds {money(tw)} from an $80,000 bonus; the bonus's real tax is {money(ta)}", loc="left", pad=34)
    ax.legend(loc="upper right", ncol=1)
    ax.text(0, 1.02, f"New York State takes 11.70% on the check against the 5.9% owed, so {money(tw - ta)} comes back at filing",
            transform=ax.transAxes, fontsize=11.5, color=TEXT_SECONDARY, ha="left", va="bottom")
    return save_figure(fig, OUT / "06-bonus-withheld-vs-actual-tax.png")


def chart_three_years():
    labels = ["First-year\nanalyst", "Second-year\nanalyst", "Third-year\nanalyst", "First-year\nassociate"]
    rows = [N.take_home(bs, bn, "NYC") for bs, bn in YEAR_INPUTS.values()]
    fig, ax = new_figure(width=11.0, height=6.2)
    import numpy as np
    x = np.arange(len(rows))
    bw = 0.36
    b1 = ax.bar(x - bw / 2, [r["gross"] for r in rows], width=bw, color=BLUE, label="All-in pay (base plus bonus)", zorder=3,
                edgecolor=SURFACE, linewidth=2)
    b2 = ax.bar(x + bw / 2, [r["net"] for r in rows], width=bw, color=ORANGE, label="Take-home after New York taxes", zorder=3,
                edgecolor=SURFACE, linewidth=2)
    for bars, bold in ((b1, False), (b2, True)):
        for b in bars:
            ax.annotate(money(b.get_height()), (b.get_x() + b.get_width() / 2, b.get_height()), ha="center", va="bottom",
                        xytext=(0, 4), textcoords="offset points", fontsize=11.5, color=TEXT_PRIMARY,
                        fontweight="bold" if bold else "normal")
    for i, r in enumerate(rows):
        ax.text(i, -40_000, f"{pct(r['eff_rate'])} effective rate", ha="center", va="top", fontsize=10.5, color=TEXT_SECONDARY)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=12)
    ax.set_ylim(0, 335_000)
    ax.set_yticks(range(0, 300_001, 50_000))
    ax.set_yticklabels([k(v) for v in range(0, 300_001, 50_000)])
    style_axes(ax, title="Gross pay rises $40,000 a year through the program; take-home rises $20,000 to $25,000",
               ylabel="Bulge bracket, middle-to-upper bucket, New York City")
    ax.legend(loc="upper left", ncol=1)
    return save_figure(fig, OUT / "07-gross-vs-take-home-by-year.png")


def chart_monthly_budget(b):
    cols = list(BUDGET_INPUTS.keys())
    take = b["net_monthly"]
    segs = []
    for c in cols:
        rent, util, transit, food, out, ins, flights = BUDGET_INPUTS[c]
        other = util + transit + ins + flights
        left = take - sum(BUDGET_INPUTS[c])
        segs.append([("Rent", rent, ORANGE), ("Food and going out", food + out, AQUA), ("Utilities, transit, insurance, flights home", other, YELLOW),
                     ("Left over to save", left, BLUE)])
    fig, ax = new_figure(width=10.0, height=6.4)
    w = 0.5
    for i, parts in enumerate(segs):
        bottom = 0.0
        for name, v, color in parts:
            ax.bar(i, v, width=w, bottom=bottom, color=color, edgecolor=SURFACE, linewidth=2, zorder=3)
            if v >= 650:
                bold = name.startswith("Left")
                ax.text(i, bottom + v / 2, money(v), ha="center", va="center", fontsize=12 if bold else 11.5,
                        color="white" if color in (BLUE, ORANGE) else TEXT_PRIMARY, fontweight="bold" if bold else "normal", zorder=4)
            bottom += v
        ax.annotate(f"{money(take)} take-home", (i, bottom), ha="center", va="bottom", xytext=(0, 4), textcoords="offset points",
                    fontsize=11, color=TEXT_SECONDARY)
    ax.set_xticks(range(len(cols)))
    ax.set_xticklabels(cols, fontsize=12.5)
    ax.set_ylim(0, 12_000)
    ax.set_yticks(range(0, 10_001, 2_000))
    ax.set_yticklabels([money(v) for v in range(0, 10_001, 2_000)])
    style_axes(ax, title="Sharing an apartment leaves $4,862 to $5,912 a month; a studio leaves $3,512",
               ylabel="Per month, after the 6% 401(k) deferral and health premium")
    from matplotlib.patches import Patch
    handles = [Patch(color=BLUE, label="Left over to save"), Patch(color=YELLOW, label="Utilities, transit, insurance, flights home"),
               Patch(color=AQUA, label="Food and going out"), Patch(color=ORANGE, label="Rent")]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, fontsize=11)
    return save_figure(fig, OUT / "08-monthly-budget-three-ways.png")


# ---------------------------------------------------------------- 5. manifest
def manifest(shots):
    wb = "scripts/images/models/analyst-takehome.xlsx"
    entries = [
        {"file": "01-first-year-base-by-tier.png",
         "alt": "Horizontal bar chart of first-year analyst base salary by bank tier with the bonus range shown beside each base",
         "caption": "Base is fixed by tier, from $90,000 at a regional boutique to $120,000 at an elite boutique, and the orange bonus range is where two analysts on the same base end up $55,000 apart.",
         "method": "Chart from the section 2 tier table (first-year base, first-year bonus range, first-year all-in range)",
         "anchor": "| Regional boutique | $90,000 | $100,000 | $110,000 | $15,000 to $50,000 | $105,000 to $140,000 |"[:60]},
        {"file": "02-federal-bracket-math.png",
         "alt": "Excel screenshot of the federal income tax bracket math and payroll taxes for a 200,000 dollar New York analyst",
         "caption": "Only the first four brackets touch $183,900 of taxable income, so the three rows above them show a dash, and the slices add to $36,734 before Social Security and Medicare take another $14,339.",
         "method": f"Workbook {wb}, sheet Take-home, range {shots['02-federal-bracket-math.png']} (live MIN and MAX slice formulas)",
         "anchor": "| Total federal income tax |  | $183,900 | $36,734 |"[:60]},
        {"file": "03-new-york-state-and-city-tax.png",
         "alt": "Excel screenshot of the New York State flat rate, the city bracket table and the take-home block",
         "caption": "The schedule would charge $10,760, but worksheet 7 taxes all $192,000 at a flat 5.9 percent for $11,328, the city adds $7,317 on its four slices, and the sheet lands on the same $130,282.",
         "method": f"Workbook {wb}, sheet Take-home, range {shots['03-new-york-state-and-city-tax.png']} (the schedule figure links from the NY schedule sheet)",
         "anchor": "| Total NYC tax |  | $192,000 | $7,317 |"[:60]},
        {"file": "04-gross-to-net-new-york.png",
         "alt": "Waterfall chart from 200,000 dollars of gross pay through federal, payroll, state and city taxes to 130,282 of take-home",
         "caption": "Federal income tax is the biggest bar at 18.4 percent of gross, and the two New York bars together are the $18,645 that a Houston analyst never pays.",
         "method": "Chart from the section 4 gross-to-net table (federal $36,734, Social Security and Medicare $14,339, New York State $11,328, New York City $7,317, take-home $130,282)",
         "anchor": "| Take-home per month | $10,857 |"[:60]},
        {"file": "05-same-pay-four-cities.png",
         "alt": "Stacked horizontal bars splitting 200,000 dollars of pay into take-home and taxes in Houston, Charlotte, San Francisco and New York",
         "caption": "The gray federal block is identical in all four cities, so every dollar of difference sits in the orange and green state and city segments on the right.",
         "method": "Chart from the section 7 four-city table (federal, Social Security and Medicare, state, city, state disability insurance, take-home, gap versus New York)",
         "anchor": "| Gap versus New York (a year) | $0 | $11,174 | $18,645 | $1,834 |"[:60]},
        {"file": "06-bonus-withheld-vs-actual-tax.png",
         "alt": "Paired bar chart of what payroll withholds from an 80,000 dollar bonus against the tax it actually adds, by line",
         "caption": "Federal is under-withheld because 22 percent is less than the 24 percent bracket, New York State is over-withheld by almost half, and the net $3,908 comes back as a refund.",
         "method": "Chart from the section 6 withholding table (withheld $17,600, $4,960, $1,160, $9,360, $3,400; actual $19,164, $3,999, $1,160, $5,148, $3,101)",
         "anchor": "| Bonus you keep | $43,520 | $47,428 |"[:60]},
        {"file": "07-gross-vs-take-home-by-year.png",
         "alt": "Grouped bar chart of all-in pay against take-home for first, second and third-year analysts and a first-year associate",
         "caption": "Each $40,000 step in gross pay becomes $24,708, then $20,332, then $15,781 of take-home, because every raise lands in higher brackets and New York phases out its lower rates as you climb.",
         "method": "Chart from the section 9 pay-by-year table (all-in $185,000 to $295,000, take-home $120,566 to $181,386, effective rates 34.8 to 38.5 percent)",
         "anchor": "| First-year associate (direct promote) | $175,000 | $120,000 | $295,000 | $113,614 | $181,386 | 38.5% | $15,781 |"[:60]},
        {"file": "08-monthly-budget-three-ways.png",
         "alt": "Stacked bar chart splitting a 10,114 dollar monthly take-home into rent, food, other costs and savings for three living setups",
         "caption": "Rent is the only line that moves the savings number by more than a few hundred dollars, and switching from a shared apartment to a studio costs $1,350 a month of it.",
         "method": "Chart from the section 8 budget table (take-home $10,114; rent, utilities, transit, groceries, going out, insurance and flights by column; left over $5,912, $4,862 and $3,512)",
         "anchor": "| Saved in a year (cash only) | $70,939 | $58,339 | $42,139 |"[:60]},
    ]
    check_entries(entries)
    write_manifest(OUT, entries)
    print(f"wrote {OUT.relative_to(ROOT)}/manifest.json with {len(entries)} entries")


def check_entries(entries):
    bad = ("\u2014", "\u2013", "\u2212")
    for e in entries:
        for key in ("alt", "caption", "method", "anchor"):
            assert not any(ch in e[key] for ch in bad), f"dash in manifest {e['file']} {key}"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
        assert (OUT / e["file"]).exists(), f"missing image {e['file']}"
    if DRAFT.exists():
        lines = [l.strip() for l in DRAFT.read_text(encoding="utf-8").split("\n")]
        for e in entries:
            if not any(l.startswith(e["anchor"]) for l in lines):
                print(f"  WARNING: anchor for {e['file']} not found in the draft: {e['anchor']!r}")


def check_pngs():
    """Every PNG at most 2200 px wide (bbox_inches='tight' can add a few pixels to a chart)."""
    from PIL import Image
    for png in sorted(OUT.glob("*.png")):
        im = Image.open(png)
        if im.width > 2200:
            im = im.convert("RGB").resize((2200, round(im.height * 2200 / im.width)), Image.LANCZOS)
            im.save(png, "PNG", optimize=True, dpi=(200, 200))
        assert Image.open(png).width <= 2200, f"{png.name} is too wide"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    R = build_and_check_workbook()
    data = check_numbers_script()
    shots = render_screenshots(R)
    chart_base_by_tier()
    chart_gross_to_net(data["base_case"])
    chart_four_cities(data["cities"])
    chart_bonus_withholding(data["bonus_withheld"], data["bonus_actual"])
    chart_three_years()
    chart_monthly_budget(data["with_deductions"])
    check_pngs()
    manifest(shots)


if __name__ == "__main__":
    main()
