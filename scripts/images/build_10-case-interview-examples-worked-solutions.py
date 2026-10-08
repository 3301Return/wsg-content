#!/usr/bin/env python3
"""Images for drafts/draft-10-case-interview-examples-worked-solutions-v1.md (October 1, 2026).

Run from the repo root:  python3 scripts/images/build_10-case-interview-examples-worked-solutions.py
Idempotent: rewrites every PNG in published/assets/images/10-case-interview-examples-worked-solutions/
and the manifest.

Every number in the charts and trees comes from the article's own data tables and worked math.
The one photo is Enrico Fermi's Los Alamos badge photo from Wikimedia Commons, public domain
(US Department of Energy work, Los Alamos National Laboratory); the file page's license template
is {{PD-USGov-DOE}}. A local copy sits in scripts/images/sources/ so the build runs offline; if it
is missing the script downloads the 330 px rendition from upload.wikimedia.org.
"""
import shutil
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, "scripts/images")
from wsg_viz import *          # noqa: E402,F401
from wsg_diagrams import *     # noqa: E402,F401

OUT = Path("published/assets/images/10-case-interview-examples-worked-solutions")
OUT.mkdir(parents=True, exist_ok=True)
entries = []

FERMI_PAGE = "https://commons.wikimedia.org/wiki/File:Enrico_Fermi_ID_badge.png"
FERMI_FILE = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Enrico_Fermi_ID_badge.png/330px-Enrico_Fermi_ID_badge.png"
FERMI_SRC = Path("scripts/images/sources/enrico-fermi-id-badge-commons-330px.png")


def add(file, alt, caption, method, anchor):
    entries.append({"file": file, "alt": alt, "caption": caption, "method": method, "anchor": anchor})


# ---------------------------------------------------------------- 01 Fermi badge photo
def fermi_photo():
    from PIL import Image, PngImagePlugin
    if not FERMI_SRC.exists():
        FERMI_SRC.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(FERMI_FILE, headers={"User-Agent": "WSGImagesBot/1.0 (wallstreetguide.net; editorial image sourcing)"})
        with urllib.request.urlopen(req, timeout=120) as r, open(FERMI_SRC, "wb") as fh:
            shutil.copyfileobj(r, fh)
    im = Image.open(FERMI_SRC).convert("RGB")
    # the Commons file is small (351 px wide); double it for article width without inventing detail beyond resampling
    im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
    meta = PngImagePlugin.PngInfo()
    meta.add_text("Software", "Wall Street Guide")
    meta.add_text("Source", FERMI_PAGE)
    meta.add_text("Copyright", "Public domain, US Department of Energy work (Los Alamos National Laboratory)")
    im.save(OUT / "01-enrico-fermi-los-alamos-badge.png", "PNG", optimize=True, pnginfo=meta)
    add("01-enrico-fermi-los-alamos-badge.png",
        "Black and white wartime Los Alamos identity badge photo of physicist Enrico Fermi, badge number G 24",
        "Enrico Fermi, whose paper-scrap estimate of the Trinity blast is the habit every sizing case below tests. Photo: Los Alamos National Laboratory, public domain, via Wikimedia Commons.",
        f"Photo from Wikimedia Commons, {FERMI_PAGE}, license PD-USGov-DOE (public domain, US Department of Energy work; source Los Alamos National Laboratory); file rendition {FERMI_FILE}, resampled to twice its pixel size",
        "**Market sizing cases grade the chain of assumptions and the")


# ---------------------------------------------------------------- 02 airline issue tree
def airline_tree():
    branches = [("Revenue: up $30M", ["Passengers: 4.0M to 4.2M, up 5 percent (all of the revenue gain)",
                                      "Average fare: $150 both years, flat while a competitor raised fares on six routes"]),
                ("Costs: up $70M", ["Fuel: up $54.5M. Price effect $42M (105M gallons at 40 cents more); volume effect $12.5M (5M more gallons at $2.50)",
                                    "Crew and staff: up $12M, an 8 percent raise from a new pilot contract",
                                    "Maintenance, airport fees, aircraft ownership: up $3.5M"])]
    box_h, gap = 0.74, 0.14
    W = 11
    H = round(tree_height(branches, box_h, gap) + 0.9 + 1.1, 2)
    fig, ax = canvas(W, H, title="Airline case: the tree a strong candidate draws, with the numbers that fell out of it")
    issue_tree(ax, "Why did operating profit fall from $60M to $20M while revenue grew 5 percent?", branches,
               canvas_h=H, x0=0.35, root_w=2.4, branch_w=2.0, leaf_w=5.5, box_h=box_h, gap=gap, leaf_size=11.5)
    label(ax, 0.35, 0.5, "Without the fuel price rise the airline would have earned $62M, slightly more than two years ago. First hypothesis: fuel got more expensive while fares stayed put. Confirmed.",
          size=11.5, color=TEXT_SECONDARY, italic=True, va="center", wrap_in=W - 0.8)
    finish(fig, OUT / "02-airline-profitability-issue-tree.png")
    add("02-airline-profitability-issue-tree.png",
        "Issue tree splitting the airline's $40 million profit drop into revenue up $30 million and costs up $70 million",
        "The profit tree for case 1: revenue rose $30 million on volume alone, and $42 million of the $70 million cost increase is the fuel price.",
        "Issue tree drawn in matplotlib from the case 1 structure paragraph, data table and math",
        "**Structure:** Profit is revenue minus cost, so a 5 percent ")


# ---------------------------------------------------------------- 03 airline cost bridge
def airline_bridge():
    fig, ax = new_figure(width=11, height=5.8)
    steps = [("More passengers (5 percent, fare flat)", 30.0),
             ("Fuel price (105M gallons at 40 cents more)", -42.0),
             ("More fuel burned (5M gallons at $2.50)", -12.5),
             ("Crew and staff (new pilot contract)", -12.0),
             ("Maintenance, fees, ownership", -3.5)]
    end = waterfall(ax, steps, 60.0, "Operating profit two years ago", "Operating profit today", fmt="${:,.1f}M",
                    ylabel="$ millions", title="The fuel price alone cost the airline $42 million, more than the whole $40 million profit drop",
                    ymin=0, legend_loc="upper right")
    assert abs(end - 20.0) < 1e-9, end
    ax.set_ylim(0, 105)
    ax.set_yticks([0, 20, 40, 60, 80, 100])
    finish(fig, OUT / "03-airline-cost-bridge.png")
    add("03-airline-cost-bridge.png",
        "Waterfall chart from $60 million of operating profit to $20 million, with fuel price as the largest step",
        "Walk the bridge and the story is one bar: the 40 cent fuel price rise took $42 million, and everything else the airline did netted out to a $2 million gain.",
        "Waterfall from the case 1 data table and math list (revenue, fuel price and volume effects, crew, other costs)",
        "- **A 16 percent rise in the price of fuel cost the airline ")


# ---------------------------------------------------------------- 04 EV charging issue tree
def ev_tree():
    branches = [("Is the market attractive?", ["EVs are about 3 percent of cars in the region today, projected to reach about 10 percent in five years",
                                               "Who else is building chargers along the same roads"]),
                ("Can the client win?", ["Highway sites, 24-hour stores, restrooms and food for a 30-minute wait; owns about 80 percent of its sites"]),
                ("Do the unit economics work?", ["$600,000 per site (four chargers at $150,000); $12.90 of contribution per session; $30,000 of fixed cost a year",
                                                 "Utilization: 3 sessions per charger per day today at the busiest sites, projected 8 in five years"]),
                ("What could go wrong?", ["Utilization that lags, electricity rate structures and demand charges, charger standards changing"])]
    box_h, gap = 0.68, 0.12
    W = 11
    H = round(tree_height(branches, box_h, gap) + 0.9 + 1.1, 2)
    fig, ax = canvas(W, H, title="EV charging case: four questions, and the one number the whole decision hangs on")
    issue_tree(ax, "Should 1,200 Midwest convenience stores install DC fast chargers, and if so where and how many?", branches,
               canvas_h=H, x0=0.35, root_w=2.4, branch_w=2.1, leaf_w=5.4, box_h=box_h, gap=gap, leaf_size=11.5)
    label(ax, 0.35, 0.5, "The swing variable is sessions per charger per day: a five-year payback needs 8, nearly triple today's traffic.",
          size=11.5, color=TEXT_SECONDARY, italic=True, va="center", wrap_in=W - 0.8)
    finish(fig, OUT / "04-ev-charging-market-entry-issue-tree.png")
    add("04-ev-charging-market-entry-issue-tree.png",
        "Issue tree for the EV charging market entry case: market, right to win, unit economics, and risks",
        "The market entry tree for case 3 ends at one number, sessions per charger per day, and the recommendation is built around learning it.",
        "Issue tree drawn in matplotlib from the case 3 structure paragraph and data table",
        "**Structure:** Four questions. Is the market attractive: how")


# ---------------------------------------------------------------- 05 EV unit economics
def ev_economics():
    fig, axes = new_figure(width=11, height=5.6, ncols=2, gridspec_kw={"width_ratios": [1, 1.6]})
    fig.suptitle("A charging site clears a five-year payback only at 8 sessions per charger per day",
                 x=0.01, ha="left", fontsize=16, fontweight="bold", color=TEXT_PRIMARY)
    # left: margin per session stack
    ax = axes[0]
    ax.bar([0], [10.50], width=0.5, color=BLUE, zorder=3, label="Electricity: 35 kWh at 30 cents margin")
    ax.bar([0], [2.40], bottom=[10.50 + 0.08], width=0.5, color=SEQ_BLUE[2], zorder=3, label="In-store spend: $8 at 30 percent margin")
    ax.annotate("$10.50", (0, 5.25), ha="center", va="center", fontsize=13, color="white", zorder=5)
    ax.annotate("$2.40", (0, 10.58 + 1.2), ha="center", va="center", fontsize=12, color=TEXT_PRIMARY, zorder=5)
    ax.annotate("$12.90 per session", (0, 13.1), ha="center", va="bottom", fontsize=13, color=TEXT_PRIMARY, fontweight="bold")
    style_axes(ax, title="Contribution per session")
    ax.title.set_fontsize(13.5)
    ax.set_xlim(-0.6, 0.6)
    ax.set_xticks([])
    ax.set_ylim(0, 15.5)
    ax.set_yticks([])
    ax.spines["left"].set_visible(False)
    ax.grid(False)
    ax.legend(loc="upper left", bbox_to_anchor=(-0.05, -0.04), ncol=1, frameon=False, fontsize=11)
    # right: annual contribution after fixed cost at 3 vs 8 sessions
    ax = axes[1]
    labels = ["3 sessions per charger per day\n(today's busiest sites)", "8 sessions per charger per day\n(projected in five years)"]
    vals = [26502, 120672]
    bars = ax.bar(range(2), vals, width=0.5, color=BLUE, zorder=3)
    for b, pb, vt in zip(bars, ["Payback: 22.6 years", "Payback: 5.0 years"], ["$26,502", "about $120,700"]):
        ax.annotate(vt, (b.get_x() + b.get_width() / 2, b.get_height()), ha="center", va="bottom",
                    xytext=(0, 4), textcoords="offset points", fontsize=12.5, color=TEXT_PRIMARY, fontweight="bold",
                    bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.5), zorder=5)
        ax.annotate(pb, (b.get_x() + b.get_width() / 2, b.get_height()), ha="center", va="bottom", xytext=(0, 22),
                    textcoords="offset points", fontsize=11.5, color=TEXT_SECONDARY, zorder=5)
    ax.axhline(120000, color=ORANGE, lw=2.2, zorder=2)
    ax.annotate("$120,000 a year pays back\n$600,000 in five years", (-0.45, 120000), ha="left", va="top", xytext=(0, -6),
                textcoords="offset points", fontsize=11.5, color=TEXT_PRIMARY, zorder=5)
    style_axes(ax, title="Site contribution a year after $30,000 of fixed cost")
    ax.title.set_fontsize(13.5)
    ax.set_xticks(range(2))
    ax.set_xticklabels(labels, fontsize=11.5)
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylim(0, 150000)
    ax.set_yticks([0, 50000, 100000, 150000])
    ax.set_yticklabels(["$0", "$50K", "$100K", "$150K"])
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], color=ORANGE, lw=2.2, label="Five-year payback line")], loc="upper left", frameon=False)
    fig.subplots_adjust(top=0.82, bottom=0.2, wspace=0.18, left=0.04, right=0.99)
    finish(fig, OUT / "05-ev-charging-unit-economics.png")
    add("05-ev-charging-unit-economics.png",
        "Two charts: $12.90 of contribution per charging session, and yearly site contribution at 3 versus 8 daily sessions",
        "Each session earns $12.90, so a site clears the $120,000 a year that a five-year payback needs only at 8 sessions per charger per day, not today's 3.",
        "Charts from the case 3 data table (per site, four chargers) and the math list (margin per session, 3 and 8 session cases, break-even)",
        "- **A site pays back in five years only at about 8 sessions ")


# ---------------------------------------------------------------- 06 M&A issue tree
def ma_tree():
    branches = [("What is the target worth on its own?", ["EBITDA $60M at 14x (recent snack deals) = $840M standalone, against a $1.2B price (20x): $360M more than it is worth alone"]),
                ("What extra value does this buyer create?", ["Cost synergies: distribution from 8 to 3 percent of $400M saves $20M; overhead $10M; $30M a year",
                                                               "Revenue synergies: 15,000 new stores at $8,000 = $120M of revenue, $24M of EBITDA at a 20 percent margin"]),
                ("What could go wrong?", ["Integration ($50M one-time), cannibalizing the client's own pretzels, paying for synergies before they exist"]),
                ("What else could $1.2B do?", ["A buyback, or two smaller brands, on the same capital"])]
    box_h, gap = 0.72, 0.12
    W = 11
    H = round(tree_height(branches, box_h, gap) + 0.9 + 1.1, 2)
    fig, ax = canvas(W, H, title="Snack M&A case: standalone value, synergies, risks, and the question most candidates skip")
    issue_tree(ax, "Should a $2B chips and pretzels maker pay $1.2B for a $400M revenue popcorn brand?", branches,
               canvas_h=H, x0=0.35, root_w=2.4, branch_w=2.2, leaf_w=5.3, box_h=box_h, gap=gap, leaf_size=11.5)
    label(ax, 0.35, 0.5, "Break-even: $1.25B all-in at 14x needs $89.3M of EBITDA, so $29.3M of synergies just to get the client's money back.",
          size=11.5, color=TEXT_SECONDARY, italic=True, va="center", wrap_in=W - 0.8)
    finish(fig, OUT / "06-snack-ma-issue-tree.png")
    add("06-snack-ma-issue-tree.png",
        "Issue tree for the popcorn acquisition case: standalone value, cost and revenue synergies, risks, alternatives",
        "The acquisition tree for case 4: the price sits $360 million above standalone value, and the synergies have to cover the gap.",
        "Issue tree drawn in matplotlib from the case 4 structure paragraph, data table and math",
        "**Structure:** Three questions decide an acquisition. What i")


# ---------------------------------------------------------------- 07 software pricing tiers
def pricing_tiers():
    import numpy as np
    fig, axes = new_figure(width=11, height=5.8, ncols=2, gridspec_kw={"width_ratios": [1.1, 1]})
    fig.suptitle("Matching at $12 costs $48 million a year with certainty; three tiers net about $10 million",
                 x=0.01, ha="left", fontsize=16, fontweight="bold", color=TEXT_PRIMARY)

    def money(v, pos=None):
        return "(${:,.0f}M)".format(-v) if v < 0 else "${:,.0f}M".format(v)
    from matplotlib.ticker import FuncFormatter
    # left: the three options
    ax = axes[0]
    opts = ["Match the $12 price\nacross the board", "Hold price and lose\nevery small customer", "Three tiers:\n$12, $20, $30"]
    vals = [-48.0, -12.0, 10.2]
    bars = ax.bar(range(3), vals, width=0.52, color=[RED, RED, BLUE], zorder=3)
    for b, v in zip(bars, vals):
        txt = "(${:,.1f}M)".format(-v) if v < 0 else "+${:,.1f}M".format(v)
        ax.annotate(txt, (b.get_x() + b.get_width() / 2, v), ha="center", va="top" if v < 0 else "bottom",
                    xytext=(0, -4 if v < 0 else 4), textcoords="offset points", fontsize=12.5, color=TEXT_PRIMARY, fontweight="bold")
    ax.axhline(0, color=TEXT_SECONDARY, lw=1.0, zorder=2)
    style_axes(ax, title="Annual revenue impact of each option")
    ax.title.set_fontsize(13.5)
    ax.set_xticks(range(3))
    ax.set_xticklabels(opts, fontsize=11.5)
    ax.set_ylim(-58, 20)
    ax.set_yticks([-50, -40, -30, -20, -10, 0, 10, 20])
    ax.yaxis.set_major_formatter(FuncFormatter(money))
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=RED, label="Revenue lost"), Patch(color=BLUE, label="Revenue gained"),
                       Patch(color=TEXT_MUTED, label="Net of the three-tier move")], loc="lower right", frameon=False)
    # right: inside the three-tier move (waterfall)
    ax = axes[1]
    steps = [("Downgrades: 100,000 seats from $20 to $12", -9.6), ("Upgrades: 75,000 seats from $20 to $30", 9.0),
             ("New starter customers: 15,000 at 5 seats", 10.8)]
    run = 0.0
    xs = np.arange(4)
    bottoms, heights, colors = [], [], []
    for _, d in steps:
        bottoms.append(run if d >= 0 else run + d); heights.append(abs(d)); colors.append(BLUE if d >= 0 else RED)
        run += d
    bottoms.append(0); heights.append(run); colors.append(TEXT_MUTED)
    ax.bar(xs, heights, bottom=bottoms, width=0.52, color=colors, zorder=3)
    lvl = 0.0
    for i, (_, d) in enumerate(steps):
        ax.plot([xs[i] + 0.26, xs[i + 1] - 0.26], [lvl + d, lvl + d], color=LINE, lw=1.0, zorder=2)
        lvl += d
    for i, (_, d) in enumerate(steps):
        if d < 0:   # label below the bottom of a falling step
            ax.annotate("(${:,.1f}M)".format(-d), (xs[i], bottoms[i]), ha="center", va="top", xytext=(0, -4), textcoords="offset points",
                        fontsize=12, color=TEXT_PRIMARY, bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.5), zorder=5)
        else:
            ax.annotate("+${:,.1f}M".format(d), (xs[i], bottoms[i] + heights[i]), ha="center", va="bottom", xytext=(0, 4),
                        textcoords="offset points", fontsize=12, color=TEXT_PRIMARY, bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.5), zorder=5)
    ax.annotate("+${:,.1f}M".format(run), (xs[3], run), ha="center", va="bottom", xytext=(0, 4), textcoords="offset points",
                fontsize=12.5, color=TEXT_PRIMARY, fontweight="bold")
    assert abs(run - 10.2) < 1e-9, run
    ax.axhline(0, color=TEXT_SECONDARY, lw=1.0, zorder=2)
    style_axes(ax, title="Inside the three-tier move")
    ax.title.set_fontsize(13.5)
    ax.set_xticks(xs)
    ax.set_xticklabels(["Downgrades\n(100,000 seats,\n$20 to $12)", "Upgrades\n(75,000 seats,\n$20 to $30)", "New starter\ncustomers\n(15,000 at 5 seats)", "Net"], fontsize=10.5)
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(-14, 16)
    ax.set_yticks([-10, -5, 0, 5, 10, 15])
    ax.yaxis.set_major_formatter(FuncFormatter(money))
    fig.subplots_adjust(top=0.82, bottom=0.22, wspace=0.28, left=0.07, right=0.99)
    finish(fig, OUT / "07-software-pricing-three-options.png")
    add("07-software-pricing-three-options.png",
        "Two charts: annual revenue impact of matching, holding, or adding tiers, and the parts of the three-tier move",
        "The blanket cut gives up $48 million a year on day one; three tiers lose $9.6 million on downgrades and win it back twice over on upgrades and new starters.",
        "Charts from the case 5 data table and math list (match, worst case, three-tier downgrades, upgrades, new customers, net)",
        "- **Matching the competitor costs $48 million a year with ce")


# ---------------------------------------------------------------- 08 tire market sizing funnel
def tire_funnel():
    W, H = 11, 7.0
    fig, ax = canvas(W, H, title="From 335 million people to 280 million tires in four links, then a check against the industry's count")
    from matplotlib.patches import Polygon
    stages = [
        ("US population", "About 335 million", "Start from a number you know."),
        ("Light vehicles on the road", "About 280 million", "Roughly 0.85 vehicles per person."),
        ("Vehicles replacing a set this year", "70 million", "A tire lasts 48,000 miles at 12,000 miles a year, so 4 years; 280 million divided by 4."),
        ("Replacement tires sold", "280 million a year", "70 million sets times 4 tires."),
    ]
    cx, top, band_h, gap = 3.2, H - 1.1, 0.95, 0.12
    widths = [5.4, 4.5, 3.6, 2.7]
    cols = [SEQ_BLUE[6], SEQ_BLUE[7], SEQ_BLUE[9], SEQ_BLUE[11]]
    y = top
    for (head, num, note), w, col in zip(stages, widths, cols):
        w_next = w - 0.9
        ax.add_patch(Polygon([(cx - w / 2, y), (cx + w / 2, y), (cx + w_next / 2, y - band_h), (cx - w_next / 2, y - band_h)],
                             closed=True, facecolor=col, edgecolor=SURFACE, linewidth=2, zorder=3))
        ax.text(cx, y - band_h / 2 + 0.17, num, ha="center", va="center", fontsize=15, color="white", fontweight="bold", zorder=4)
        ax.text(cx, y - band_h / 2 - 0.2, head, ha="center", va="center", fontsize=11, color="white", zorder=4)
        label(ax, cx + widths[0] / 2 + 0.35, y - band_h / 2, note, size=11.5, ha="left", va="center", wrap_in=W - (cx + widths[0] / 2 + 0.35) - 0.4)
        y -= band_h + gap
    # sanity checks
    yb = y - 0.15
    text_box(ax, 0.35, yb - 1.2, W - 0.7, 1.2, "", fill=PALE_GRAY, radius=0.08)
    label(ax, 0.55, yb - 0.3, "Sanity checks", size=12.5, bold=True, va="center")
    label(ax, 0.55, yb - 0.78, "Industry count: the US Tire Manufacturers Association forecast about 260 million replacement passenger and light truck tires for 2025, so the estimate is about 8 percent high.  "
          "Second method: about 20,000 tire-selling locations times 40 tires a day times 300 days = 240 million. Same neighborhood.",
          size=11, va="center", wrap_in=W - 1.2)
    finish(fig, OUT / "08-tire-market-sizing-funnel.png")
    add("08-tire-market-sizing-funnel.png",
        "Funnel from 335 million people to 280 million vehicles to 70 million sets to 280 million replacement tires a year",
        "The top-down chain for case 6 has four links, and the two checks at the bottom land within 10 percent of the estimate.",
        "Funnel drawn in matplotlib from the case 6 assumptions table, math list and sanity checks",
        "- **About 280 million replacement tires a year, within 10 pe")


# ---------------------------------------------------------------- 09 car wash returns
def car_wash_returns():
    fig, axes = new_figure(width=11, height=5.8, ncols=2, gridspec_kw={"width_ratios": [1, 1.25]})
    fig.suptitle("The car wash deal returns 4.0x in the base case and 1.6x if half the new sites never get built",
                 x=0.01, ha="left", fontsize=16, fontweight="bold", color=TEXT_PRIMARY)
    # left: equity in vs equity out
    ax = axes[0]
    labels = ["Equity invested", "Equity at exit,\nbase case", "Equity at exit,\ndownside"]
    vals = [60, 238, 97]
    bars = ax.bar(range(3), vals, width=0.52, color=[TEXT_MUTED, BLUE, BLUE], zorder=3)
    for b, v, sub in zip(bars, vals, ["", "4.0x, about 32% IRR", "1.6x, about 10% IRR"]):
        ax.annotate("${:,.0f}M".format(v), (b.get_x() + b.get_width() / 2, v), ha="center", va="bottom", xytext=(0, 4),
                    textcoords="offset points", fontsize=12.5, color=TEXT_PRIMARY, fontweight="bold")
        if sub:
            ax.annotate(sub, (b.get_x() + b.get_width() / 2, v), ha="center", va="bottom", xytext=(0, 22),
                        textcoords="offset points", fontsize=11.5, color=TEXT_SECONDARY)
    style_axes(ax, title="Equity in and out, $ millions")
    ax.title.set_fontsize(13.5)
    ax.set_xticks(range(3))
    ax.set_xticklabels(labels, fontsize=11.5)
    ax.set_ylim(0, 300)
    ax.set_yticks([0, 100, 200, 300])
    ax.set_yticklabels(["$0", "$100M", "$200M", "$300M"])
    # right: MOIC by scenario against the 3x hurdle
    ax = axes[1]
    scen = ["Base case\n(20 sites, 2,500\nmembers, 9x exit)", "New sites take\nfour years to ramp", "Exit at 8x\ninstead of 9x", "Downside\n(10 sites, flat\nmembership, 8x)"]
    moic = [4.0, 3.6, 3.3, 1.6]
    irr = ["32% IRR", "", "27% IRR", "10% IRR"]
    bars = ax.bar(range(4), moic, width=0.52, color=[BLUE, BLUE, BLUE, BLUE], zorder=3)
    for b, m, r in zip(bars, moic, irr):
        ax.annotate("{:.1f}x".format(m), (b.get_x() + b.get_width() / 2, m), ha="center", va="bottom", xytext=(0, 4),
                    textcoords="offset points", fontsize=12.5, color=TEXT_PRIMARY, fontweight="bold",
                    bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.5), zorder=5)
        if r:
            ax.annotate(r, (b.get_x() + b.get_width() / 2, m), ha="center", va="bottom", xytext=(0, 22),
                        textcoords="offset points", fontsize=11.5, color=TEXT_SECONDARY, zorder=5)
    ax.axhline(3.0, color=ORANGE, lw=2.2, zorder=2)
    ax.annotate("Hurdle: 3x\n(25% a year)", (3.45, 3.0), ha="right", va="top", xytext=(0, -5),
                textcoords="offset points", fontsize=11.5, color=TEXT_PRIMARY, zorder=5)
    style_axes(ax, title="Multiple of invested capital by scenario")
    ax.title.set_fontsize(13.5)
    ax.set_xticks(range(4))
    ax.set_xticklabels(scen, fontsize=10.5)
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(0, 5.2)
    ax.set_yticks([0, 1, 2, 3, 4, 5])
    ax.set_yticklabels(["0x", "1x", "2x", "3x", "4x", "5x"])
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], color=ORANGE, lw=2.2, label="The fund's return target")], loc="upper right", frameon=False)
    fig.subplots_adjust(top=0.82, bottom=0.24, wspace=0.22, left=0.07, right=0.99)
    finish(fig, OUT / "09-car-wash-returns-by-scenario.png")
    add("09-car-wash-returns-by-scenario.png",
        "Two charts: $60 million of equity becoming $238 million or $97 million, and MOIC by scenario against a 3x hurdle",
        "Three of the four cases clear the fund's 3x hurdle; the one that doesn't is the one where the new sites never get built, which is why diligence goes there.",
        "Charts from the case 10 math list (financing, exit, base and downside returns) and the recommendation's 3.6x and 3.3x sensitivities",
        "- **The base case returns 4.0x and a 32 percent IRR, but wit")


if __name__ == "__main__":
    fermi_photo()
    airline_tree()
    airline_bridge()
    ev_tree()
    ev_economics()
    ma_tree()
    pricing_tiers()
    tire_funnel()
    car_wash_returns()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT}")
