#!/usr/bin/env python3
"""Images for drafts/draft-centerview-partners-career-guide-v1.md (October 5, 2026).

Run from the repo root:  python3 scripts/images/build_centerview-partners-career-guide.py
Idempotent: rewrites every PNG in published/assets/images/centerview-partners-career-guide/ and the
folder's manifest.json. The draft is never edited; the coordinator inserts the image lines from the
manifest anchors with scripts/images/insert_images.py.

Every figure comes from the draft. Derived figures are recomputed here from the draft's own inputs
and asserted against the numbers the draft prints before anything is drawn:
  - Question 1 accretion: 10.0, 4.4, 3.4 and 5.6 percent from the stated net income, shares, price,
    6 percent debt, 25 percent tax and $40 million of synergies
  - Question 2 paper LBO: the rounded whiteboard table (EBITDA, interest, tax, free cash flow, debt),
    the unrounded 3.154x and 25.8 percent, and the 320 + 283 = 603 value bridge
The Paramount timeline carries a "today" marker and an expected closing date, so image 06 is dated
and must be regenerated at publish.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import *          # noqa: E402,F401,F403
from wsg_diagrams import *     # noqa: E402,F401,F403

SLUG = "centerview-partners-career-guide"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v1.md"
entries = []


def add(file, alt, caption, method, anchor):
    entries.append({"file": file, "alt": alt, "caption": caption, "method": method, "anchor": anchor})


def assert_fits(fig, width_in, name):
    """The tight bounding box must stay inside the canvas, or finish() shrinks the whole picture to fit."""
    fig.canvas.draw()
    bb = fig.get_tightbbox(fig.canvas.get_renderer())
    assert bb.x0 >= -0.05 and bb.x1 <= width_in + 0.05, f"{name}: content spans {bb.x0:.2f} to {bb.x1:.2f} in on a {width_in} in canvas"


def half_up(x, nd=0):
    from decimal import ROUND_HALF_UP, Decimal
    q = Decimal(1).scaleb(-nd)
    return float(Decimal(str(x)).quantize(q, rounding=ROUND_HALF_UP))


# ---------------------------------------------------------------- the draft's numbers, recomputed
def accretion_scenarios():
    ni_a, shares_a, px = 500.0, 200.0, 50.0
    ni_t, price = 100.0, 1600.0
    rate, tax, syn = 0.06, 0.25, 40.0
    base_eps = ni_a / shares_a
    assert base_eps == 2.50 and px / base_eps == 20.0

    def deal(cash_share, synergies):
        debt = price * cash_share
        new_shares = price * (1 - cash_share) / px
        ni = ni_a + ni_t + synergies * (1 - tax) - debt * rate * (1 - tax)
        eps = ni / (shares_a + new_shares)
        return ni, shares_a + new_shares, eps, eps / base_eps - 1

    scen = {
        "Half cash, half stock, with synergies": deal(0.5, syn),
        "Half cash, half stock, no synergies": deal(0.5, 0.0),
        "All stock, no synergies": deal(0.0, 0.0),
        "All cash, no synergies": deal(1.0, 0.0),
    }
    # what the draft prints
    want = {
        "Half cash, half stock, with synergies": (594, 216, "2.75", "10.0"),
        "Half cash, half stock, no synergies": (564, 216, "2.61", "4.4"),
        "All stock, no synergies": (600, 232, "2.59", "3.4"),
        "All cash, no synergies": (528, 200, "2.64", "5.6"),
    }
    for k, (ni, sh, eps, acc) in scen.items():
        w_ni, w_sh, w_eps, w_acc = want[k]
        assert abs(ni - w_ni) < 1e-9 and abs(sh - w_sh) < 1e-9, (k, ni, sh)
        assert f"{half_up(eps, 2):.2f}" == w_eps, (k, eps)
        assert f"{half_up(acc * 100, 1):.1f}" == w_acc, (k, acc)
    # the shortcut: target yield 6.25 cents, stock 5 cents, after-tax debt 4.5 cents; breakeven at $2 billion
    assert ni_t / price == 0.0625 and abs(1 / 20 - 0.05) < 1e-12 and abs(rate * (1 - tax) - 0.045) < 1e-12
    assert ni_t * 20 == 2000
    return {k: half_up(v[3] * 100, 1) for k, v in scen.items()}


PAPER_TABLE = {   # the draft's Question 2 table, rounded at each step
    1: (88, 78, 25, 53, 13, 40, 320),
    2: (96, 86, 22, 64, 16, 48, 272),
    3: (104, 94, 19, 75, 19, 56, 216),
    4: (112, 102, 15, 87, 22, 65, 151),
    5: (120, 110, 11, 99, 25, 74, 77),
}


def paper_lbo():
    ebitda0, mult, lev, rate, tax, growth, da = 80, 8, 4.5, 0.07, 0.25, 8, 10
    price, debt0 = mult * ebitda0, lev * ebitda0
    equity = price - debt0
    assert (price, debt0, equity) == (640, 360, 280)
    # whiteboard version: round to the nearest million at every line
    debt, rows = debt0, {}
    for y in range(1, 6):
        e = ebitda0 + growth * y
        ebit = e - da
        intr = half_up(rate * debt)
        pti = ebit - intr
        tx = half_up(pti * tax)
        ni = pti - tx
        debt = debt - ni
        rows[y] = (e, ebit, int(intr), int(pti), int(tx), int(ni), int(debt))
    assert rows == PAPER_TABLE, rows
    exit_ev = mult * rows[5][0]
    exit_eq = exit_ev - rows[5][6]
    assert (exit_ev, exit_eq) == (960, 883)
    assert f"{half_up(exit_eq / equity, 2):.2f}" == "3.15"
    # unrounded model: 3.154x and 25.8 percent
    debt_u = debt0
    for y in range(1, 6):
        e = ebitda0 + growth * y
        debt_u -= (e - da - rate * debt_u) * (1 - tax)
    moic_u = (exit_ev - debt_u) / equity
    irr_u = moic_u ** (1 / 5) - 1
    assert f"{half_up(moic_u, 3):.3f}" == "3.154", moic_u
    assert f"{half_up(irr_u * 100, 1):.1f}" == "25.8", irr_u
    # the value bridge: EBITDA growth at a constant 8x, plus debt paydown, ties to the equity gain
    ebitda_growth = (rows[5][0] - ebitda0) * mult
    paydown = debt0 - rows[5][6]
    assert (ebitda_growth, paydown) == (320, 283)
    assert equity + ebitda_growth + paydown == exit_eq and exit_eq - equity == 603
    return {"debt": [int(debt0)] + [rows[y][6] for y in range(1, 6)], "ebitda": [ebitda0] + [rows[y][0] for y in range(1, 6)],
            "equity": equity, "ebitda_growth": ebitda_growth, "paydown": paydown, "exit_eq": exit_eq,
            "moic_u": moic_u, "irr_u": irr_u}


# ---------------------------------------------------------------- 01 the six mandates
def deals_chart():
    deals = [  # (label, value $bn, how the draft states the size, date)
        ("Paramount Skydance\nacquires Warner Bros. Discovery", 110.0, "$110 billion enterprise value", "Feb 27, 2026"),
        ("Equity Residential\nmerger with AvalonBay", 69.0, "about $69 billion enterprise value", "May 21, 2026"),
        ("Kenvue\nsale to Kimberly-Clark", 48.7, "about $48.7 billion enterprise value", "Nov 3, 2025"),
        ("Verona Pharma\nsale to Merck", 10.0, "about $10 billion", "Jul 9, 2025"),
        ("Intra-Cellular Therapies\nsale to Johnson & Johnson", 14.6, "about $14.6 billion equity value", "Jan 13, 2025"),
        ("H.J. Heinz sale to Berkshire\nHathaway and 3G Capital", 28.0, "$28 billion including debt", "Feb 14, 2013"),
    ]
    fig, ax = new_figure(width=11, height=6.4)
    ys = list(range(len(deals)))[::-1]
    ax.barh(ys, [d[1] for d in deals], height=0.56, color=BLUE, zorder=3)
    for y, (name, v, how, date) in zip(ys, deals):
        ax.annotate(f"{how}", (v, y), xytext=(6, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=11.5, color=TEXT_PRIMARY)
    ax.set_yticks(ys)
    ax.set_yticklabels([f"{d[0]}\nannounced {d[3]}" for d in deals], fontsize=10.5, linespacing=1.2)
    ax.set_xlim(0, 160)
    ax.set_xticks([0, 25, 50, 75, 100, 125])
    ax.set_xticklabels(["$0", "$25B", "$50B", "$75B", "$100B", "$125B"])
    style_axes(ax, title="Six Centerview mandates, from a $10 billion biotech sale to a $110 billion media takeover", ygrid_only=False)
    ax.grid(True, axis="x")
    ax.grid(False, axis="y")
    ax.spines["left"].set_visible(False)
    ax.text(0, -0.13, "Deal size as each press release or merger filing states it; enterprise value, equity value and \"including debt\" are different measures, so read the label, not only the bar.",
            transform=ax.transAxes, ha="left", va="top", fontsize=10.5, color=TEXT_SECONDARY, style="italic", wrap=False)
    fig.subplots_adjust(left=0.27, right=0.98, bottom=0.14, top=0.9)
    finish(fig, OUT / "01-six-mandates-by-size.png")
    add("01-six-mandates-by-size.png",
        "Horizontal bar chart of six Centerview mandates by deal size, from Verona Pharma to Paramount and Warner Bros. Discovery",
        "Centerview's role on all six is spelled out in the press release or merger filing, and the sizes run from $10 billion to $110 billion.",
        "Chart from the section 1 deals table in the draft (figures from each deal's press release or 8-K, tagged [VERIFY] there); each bar is labeled with the size measure the draft gives",
        "[VERIFY: each row against the cited press release or 8-K; Pa")


# ---------------------------------------------------------------- 02 pay
def pay_chart():
    rows = [  # (label, low, high, point, kind)
        ("Bulge bracket first-year base", 110, 120, None, "bb"),
        ("Centerview first-year base\n(Financial News, January 2022)", 130, 130, 130, "cv"),
        ("Bulge bracket first-year all-in,\nmid-bucket bonus", 160, 180, None, "bb"),
        ("Centerview analyst all-in, average\n(Litquidity 2023 survey)", 205, 205, 205, "cv"),
        ("Centerview analyst total pay,\nself-reported (Wall Street Oasis, 42 entries)", 135, 390, 226, "cv"),
    ]
    fig, ax = new_figure(width=11, height=5.8)
    ys = list(range(len(rows)))[::-1]
    for y, (name, lo, hi, pt, kind) in zip(ys, rows):
        col = BLUE if kind == "cv" else TEXT_MUTED
        if hi > lo:
            ax.plot([lo, hi], [y, y], color=col, lw=9, solid_capstyle="round", alpha=0.55 if kind == "cv" else 0.9, zorder=3)
        if pt is not None:
            ax.plot([pt], [y], marker="o", ms=12, color=col, markeredgecolor=SURFACE, markeredgewidth=2, zorder=4)
        if kind == "bb":
            txt = f"${lo}K to ${hi}K"
            ax.annotate(txt, (hi, y), xytext=(12, 0), textcoords="offset points", ha="left", va="center", fontsize=11.5, color=TEXT_PRIMARY)
        elif hi > lo:
            ax.annotate(f"about ${pt}K average; range ${lo}K to ${hi}K", (pt, y), xytext=(0, 13), textcoords="offset points",
                        ha="left", va="bottom", fontsize=11.5, color=TEXT_PRIMARY)
        else:
            ax.annotate(f"${pt}K" if pt == 130 else f"about ${pt}K", (pt, y), xytext=(12, 0), textcoords="offset points",
                        ha="left", va="center", fontsize=11.5, color=TEXT_PRIMARY)
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=10.5, linespacing=1.2)
    ax.set_xlim(90, 420)
    ax.set_ylim(-0.6, len(rows) - 0.3)
    ax.set_xticks([100, 150, 200, 250, 300, 350, 400])
    ax.set_xticklabels([f"${v}K" for v in [100, 150, 200, 250, 300, 350, 400]])
    style_axes(ax, title="The gap between Centerview and a bulge bracket is roughly a bulge bracket bonus", ygrid_only=False)
    ax.grid(True, axis="x")
    ax.grid(False, axis="y")
    ax.spines["left"].set_visible(False)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], color=BLUE, marker="o", ms=10, lw=6, alpha=0.8, label="Centerview (reported figures)"),
                       Line2D([0], [0], color=TEXT_MUTED, lw=6, label="Bulge bracket, for comparison")],
              loc="upper left", bbox_to_anchor=(0.0, -0.1), ncol=2, frameon=False)
    ax.text(0, -0.24, "Not shown: the $200,000 retention bonus Bloomberg reported in 2021 for analysts promoted to associate who stay two more years. "
            "Centerview publishes none of these figures.", transform=ax.transAxes, ha="left", va="top", fontsize=10.5,
            color=TEXT_SECONDARY, style="italic", wrap=True)
    fig.subplots_adjust(left=0.33, right=0.98, bottom=0.27, top=0.9)
    finish(fig, OUT / "02-analyst-pay-reported.png")
    add("02-analyst-pay-reported.png",
        "Range chart comparing reported Centerview analyst base and all-in pay with bulge bracket first-year pay",
        "Centerview's base is $20,000 above a bulge bracket's, and the reported all-in figures sit well above a bulge bracket's $160,000 to $180,000.",
        "Chart from the section 3 pay stack table and the paragraph under it (Financial News, Litquidity via eFinancialCareers, Wall Street Oasis, all tagged [VERIFY] in the draft)",
        "Read the table from the bottom up. A bulge bracket first-yea")


# ---------------------------------------------------------------- 03 accretion
def accretion_chart(acc):
    labels = ["Half cash, half stock,\nwith $40M of synergies", "Half cash, half stock,\nno synergies", "All stock,\nno synergies", "All cash,\nno synergies"]
    keys = ["Half cash, half stock, with synergies", "Half cash, half stock, no synergies", "All stock, no synergies", "All cash, no synergies"]
    vals = [acc[k] for k in keys]
    assert vals == [10.0, 4.4, 3.4, 5.6], vals
    eps = ["$2.75", "$2.61", "$2.59", "$2.64"]
    fig, ax = new_figure(width=10.5, height=5.7)
    bars = ax.bar(range(4), vals, width=0.55, color=[BLUE, AQUA, AQUA, AQUA], zorder=3)
    for b, e in zip(bars, eps):
        ax.annotate(f"{b.get_height():.1f}% accretive\nEPS {e}", (b.get_x() + b.get_width() / 2, b.get_height()), ha="center",
                    va="bottom", xytext=(0, 4), textcoords="offset points", fontsize=12, color=TEXT_PRIMARY, linespacing=1.2)
    style_axes(ax, title="Every mix accretes, and cash accretes more than stock: 4.5 cents of cost beats 5", ylabel="Change in the acquirer's EPS versus $2.50, percent")
    ax.set_xticks(range(4))
    ax.set_xticklabels(labels, fontsize=11.5)
    ax.set_ylim(0, 13)
    ax.set_yticks([0, 2, 4, 6, 8, 10, 12])
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=BLUE, label="The deal as set up (with synergies)"), Patch(color=AQUA, label="The follow-ups (no synergies)")],
              loc="upper right", ncol=1)
    finish(fig, OUT / "03-accretion-by-mix.png")
    add("03-accretion-by-mix.png",
        "Bar chart of acquirer EPS accretion for four financing mixes: 10.0, 4.4, 3.4 and 5.6 percent",
        "The target earns 6.25 cents per dollar of price, more than either stock at 5 cents or after-tax debt at 4.5, so every mix accretes and all cash accretes most.",
        "Chart from the Question 1 table and follow-ups in section 6; every scenario recomputed in this script from the stated inputs and asserted against the draft",
        "Without synergies, pro forma net income is 564, EPS is $2.61")


# ---------------------------------------------------------------- 04 paper LBO paydown
def paydown_chart(p):
    years = ["Close", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]
    x = list(range(6))
    fig, ax = new_figure(width=10.5, height=5.6)
    ax.plot(x, p["debt"], color=BLUE, marker="o", label="Debt, end of year", zorder=3)
    ax.plot(x, p["ebitda"], color=ORANGE, marker="o", label="EBITDA", zorder=3)
    for xi, d, e in zip(x, p["debt"], p["ebitda"]):
        above_d = d > e   # the label of the higher line goes above it, the lower one below, so the Year 5 crossover stays clear
        ax.annotate(f"{d}", (xi, d), xytext=(0, 9 if above_d else -10), textcoords="offset points", ha="center",
                    va="bottom" if above_d else "top", fontsize=12, color=TEXT_PRIMARY)
        ax.annotate(f"{e}", (xi, e), xytext=(0, -10 if above_d else 9), textcoords="offset points", ha="center",
                    va="top" if above_d else "bottom", fontsize=12, color=TEXT_SECONDARY)
    style_axes(ax, title="All free cash flow repays debt: 360 at close, 77 after five years", ylabel="$ millions")
    ax.set_xticks(x)
    ax.set_xticklabels(years)
    ax.set_ylim(0, 420)
    ax.set_xlim(-0.35, 5.35)
    ax.legend(loc="upper right", ncol=2)
    finish(fig, OUT / "04-paper-lbo-debt-paydown.png")
    add("04-paper-lbo-debt-paydown.png",
        "Line chart of the paper LBO's debt falling from 360 to 77 while EBITDA rises from 80 to 120",
        "Interest shrinks as the debt does, so each year more of the cash goes to principal, and the paydown speeds up from 40 to 74 a year.",
        "Chart from the Question 2 table in section 6, recomputed in this script with rounding at each line and asserted against the draft",
        "Figures rounded to the nearest million at each step, which i")


# ---------------------------------------------------------------- 05 value bridge
def bridge_chart(p):
    fig, ax = new_figure(width=10.5, height=5.8)
    steps = [("EBITDA growth\n(80 to 120 at 8x)", float(p["ebitda_growth"])), ("Debt paydown\n(360 to 77)", float(p["paydown"])),
             ("Multiple change\n(8x in, 8x out)", 0.0)]
    end = waterfall(ax, steps, float(p["equity"]), "Sponsor equity\nin", "Sponsor equity\nat exit", fmt="${:,.0f}M", neg_fmt="(${:,.0f}M)",
                    ylabel="$ millions", title="The $603 million gain is $320 million of EBITDA growth and $283 million of debt paydown",
                    legend_loc="upper left")
    assert end == p["exit_eq"] == 883
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=TEXT_MUTED, label="Sponsor equity"), Patch(color=BLUE, label="Adds to equity")],
              loc="upper left", ncol=2, frameon=False)
    ax.grid(False, axis="x")
    ax.tick_params(length=0)
    ax.set_ylim(0, 1020)
    ax.set_yticks([0, 200, 400, 600, 800, 1000])
    finish(fig, OUT / "05-paper-lbo-value-bridge.png")
    add("05-paper-lbo-value-bridge.png",
        "Waterfall chart from $280 million of sponsor equity to $883 million at exit through EBITDA growth and debt paydown",
        "Two sources and no multiple expansion: $280 million plus $320 million plus $283 million is the $883 million the sponsor takes out, and it ties.",
        "Waterfall from the Question 2 follow-up in section 6 (320 + 283 = 603), recomputed in this script and asserted",
        "The follow-up to expect: where did the return come from? Thr")


# ---------------------------------------------------------------- 06 Paramount timeline
def paramount_timeline():
    W, H = 11, 6.5
    fig, ax = canvas(W, H, title="Paramount and Warner Bros. Discovery: ten months from hostile bid to close")
    months = ["Nov\n2025", "Dec", "Jan\n2026", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
    x0, x1, ya = 0.4, W - 2.15, 3.0
    n = len(months)
    step = (x1 - x0) / n
    ax.plot([x0, x1], [ya, ya], color=TEXT_SECONDARY, lw=1.4, zorder=2)
    for i in range(n + 1):
        xa = x0 + i * step
        ax.plot([xa, xa], [ya - 0.06, ya + 0.06], color=TEXT_SECONDARY, lw=1.0, zorder=2)
    for i, m in enumerate(months):   # month labels on a white halo, so leader lines pass behind them
        ax.text(x0 + (i + 0.5) * step, ya - 0.14, m, ha="center", va="top", fontsize=10, color=TEXT_SECONDARY, zorder=6,
                linespacing=1.1, bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.0))

    def mx(mi, frac):
        return month_x(x0, step, mi, frac)

    events = [  # (x, head, body, above?, level, kind)
        (mx(1, 5 / 31), "Dec 5, 2025", "WBD board endorses a\n$27.75 a share Netflix deal\nfor its studio and\nstreaming business", False, 1, "other"),
        (mx(1, 8 / 31), "Dec 8, 2025", "Paramount launches an\nall-cash hostile offer at\n$30 a share, advised by\nCenterview and RedBird", True, 1, "deal"),
        (mx(3, 0.8), "Late February", "Netflix declines\nto raise", False, 2, "other"),
        (mx(3, 27 / 28), "Feb 27, 2026", "Signed deal at $31 a share;\n$110 billion enterprise value", True, 2, "deal"),
        (mx(5, 23 / 30), "Apr 23, 2026", "Shareholders\napprove", True, 1, "deal"),
        (mx(7, 0.5), "June 2026", "Justice Department\nclears the deal", False, 1, "other"),
        (mx(8, 0.5), "July 2026", "Twelve state attorneys\ngeneral sue", True, 2, "other"),
        (mx(11, 0.06), "Early October 2026", "Settlement approved,\nclearing the deal to close", True, 1, "deal"),
    ]
    colors = {"deal": BLUE, "other": ORANGE}
    for x, head, body, above, level, kind in events:
        nb = body.count("\n") + 1
        body_h = nb * 10 * 1.15 / 72
        if above:
            y_body = ya + 0.32 + 1.45 * (level - 1)
            ax.plot([x, x], [ya, y_body - 0.05], color=LINE, lw=1.0, zorder=1)
            label(ax, x + 0.06, y_body, body, size=10, color=TEXT_SECONDARY, ha="left", va="bottom", linespacing=1.15)
            label(ax, x + 0.06, y_body + body_h + 0.06, head, size=10.5, bold=True, ha="left", va="bottom")
        else:
            y_head = ya - 0.72 - 1.2 * (level - 1)
            ax.plot([x, x], [ya, y_head + 0.05], color=LINE, lw=1.0, zorder=1)
            label(ax, x + 0.06, y_head, head, size=10.5, bold=True, ha="left", va="top")
            label(ax, x + 0.06, y_head - 0.22, body, size=10, color=TEXT_SECONDARY, ha="left", va="top", linespacing=1.15)
        ax.plot([x], [ya], marker="o", ms=10, color=colors[kind], markeredgecolor=SURFACE, markeredgewidth=2, zorder=4)
    # today and the expected close, with the note to the right of the axis
    tx, cx = mx(11, 5 / 31), mx(11, 6 / 31)
    ax.plot([tx, tx], [ya - 0.1, ya - 1.55], color=TEXT_MUTED, lw=1.2, zorder=1)
    ax.plot([cx], [ya], marker="D", ms=11, color=TEXT_PRIMARY, markerfacecolor=SURFACE, markeredgewidth=2, zorder=5)
    label(ax, tx + 0.1, ya - 1.05, "Today, October 5, 2026", size=10, color=TEXT_MUTED, italic=True, ha="left", va="center")
    label(ax, tx + 0.1, ya - 1.3, "Closing expected October 6, 2026; the combined company to be called Skydance", size=10,
          color=TEXT_PRIMARY, ha="left", va="top", wrap_in=W - tx - 0.35)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], marker="o", lw=0, ms=10, color=BLUE, label="Paramount's deal moves forward"),
                       Line2D([0], [0], marker="o", lw=0, ms=10, color=ORANGE, label="The rival bid, regulators and the lawsuit"),
                       Line2D([0], [0], marker="D", lw=0, ms=10, color=TEXT_PRIMARY, markerfacecolor=SURFACE, markeredgewidth=2,
                              label="Expected close (verify at publish)")],
              loc="lower left", bbox_to_anchor=(0.02, 0.0), ncol=3, frameon=False, fontsize=10.5)
    assert_fits(fig, W, "06-paramount-timeline.png")
    finish(fig, OUT / "06-paramount-timeline.png")
    add("06-paramount-timeline.png",
        "Timeline from December 2025 to October 2026 of Paramount's hostile bid, signed deal, approvals, lawsuit and expected close",
        "A hostile bid against a signed deal, a board process, a shareholder vote, two regulators and a lawsuit, and the close is expected the day after this guide's date check.",
        "Timeline drawn in matplotlib from the Paramount paragraph in section 1 (dates tagged [VERIFY] in the draft); the October 6 close is shown as expected",
        "The Paramount deal is worth a minute because it's the kind o")


# ---------------------------------------------------------------- manifest checks
def check_manifest():
    lines = DRAFT.read_text(encoding="utf-8").split("\n") if DRAFT.exists() else None
    for e in entries:
        for k in ("alt", "caption", "method", "anchor"):
            for ch in ("\u2014", "\u2013", "\u2212"):
                assert ch not in e[k], f"dash in manifest {e['file']} {k}"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
        if lines is not None:
            hits = [l for l in lines if l.strip().startswith(e["anchor"])]
            assert len(hits) == 1, f"anchor for {e['file']} matches {len(hits)} draft lines: {e['anchor']!r}"
    from PIL import Image
    for e in entries:
        im = Image.open(OUT / e["file"])
        assert im.width <= 2200, f"{e['file']} is {im.width} px wide"


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    acc = accretion_scenarios()
    p = paper_lbo()
    print(f"checks: accretion {acc}; paper LBO table, exit equity 883, 3.15x rounded, {p['moic_u']:.3f}x and "
          f"{p['irr_u'] * 100:.1f}% unrounded, bridge 280 + 320 + 283 = 883 all match the draft")
    deals_chart()
    pay_chart()
    accretion_chart(acc)
    paydown_chart(p)
    bridge_chart(p)
    paramount_timeline()
    check_manifest()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT.relative_to(ROOT)}")
