#!/usr/bin/env python3
"""Images for "Asset Management Interview Prep: What They Actually Ask Undergrads" (October 1, 2026).

Run from the repo root:  python3 scripts/images/build_asset-management-interview-prep-undergrads.py

Charts only, all drawn from the article's own figures:
  01  passive versus active U.S. fund assets at the end of 2023 (Morningstar via CNBC, as the article cites)
  02  the seven-part stock pitch structure from section 3
  03  the DCF sensitivity grid for Harlow Dental Supply, computed from the section 4 cash flow table
      with the article's own terminal value method (checked against its $51, $37 and $40 figures)
  04  price against market yield for the 5-year 5 percent bond in section 6 ($958 and $1,045 marked)

Writes published/assets/images/asset-management-interview-prep-undergrads/ and its manifest.json.
Idempotent: every output is overwritten.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import (BLUE, GRID, SEQ_BLUE, SURFACE, TEXT_MUTED, TEXT_PRIMARY, TEXT_SECONDARY, new_figure,  # noqa: E402
                     save_figure, style_axes, write_manifest)

SLUG = "asset-management-interview-prep-undergrads"
OUT = ROOT / "published" / "assets" / "images" / SLUG
GRAY = "#c9c8c3"      # de-emphasis fill
GRAY_SOFT = "#f0efec"  # neutral box fill for the diagram


def cap_width(png, max_px=2200):
    from PIL import Image
    im = Image.open(png)
    if im.width > max_px:
        im = im.resize((max_px, round(im.height * max_px / im.width)), Image.LANCZOS)
        im.save(png, "PNG", optimize=True, dpi=(200, 200))
    return png


# ------------------------------------------------------------------ the article's arithmetic
def bond_price(y, coupon=50.0, years=5, face=1000.0):
    return sum(coupon / (1 + y) ** t for t in range(1, years + 1)) + face / (1 + y) ** years


HARLOW_UFCF = [368, 398, 424, 438, 453]   # section 4 DCF table, $ millions, Years 1 to 5
HARLOW_NET_DEBT, HARLOW_SHARES = 1200, 150


def harlow_value(r, g):
    """Value per share: five years of cash flow plus a Gordon terminal value, discounted at r."""
    pv = sum(cf / (1 + r) ** t for t, cf in enumerate(HARLOW_UFCF, 1))
    tv = HARLOW_UFCF[-1] * (1 + g) / (r - g)
    ev = pv + tv / (1 + r) ** 5
    return (ev - HARLOW_NET_DEBT) / HARLOW_SHARES


def check_numbers():
    """The article's own figures must fall out of the same arithmetic before anything is drawn."""
    assert round(bond_price(0.06)) == 958, bond_price(0.06)
    assert round(bond_price(0.04)) == 1045, bond_price(0.04)
    assert round(bond_price(0.05)) == 1000
    assert round(harlow_value(0.075, 0.03)) == 51, harlow_value(0.075, 0.03)
    assert round(harlow_value(0.085, 0.025)) == 37, harlow_value(0.085, 0.025)
    assert round(harlow_value(0.085, 0.03)) == 40, harlow_value(0.085, 0.03)
    print("article figures reproduce: bond $958 / $1,045, DCF $51 / $37 / $40")


# ------------------------------------------------------------------ charts
def chart_passive_active(out):
    labels = ["Passive funds", "Active funds"]
    values = [13.29, 13.23]
    fig, ax = new_figure(width=8.0, height=5.4)
    bars = ax.bar(labels, values, width=0.3, color=[BLUE, GRAY], linewidth=0)
    ax.set_xlim(-0.6, 1.6)
    for b, v in zip(bars, values):
        ax.annotate(f"${v:.2f} trillion", (b.get_x() + b.get_width() / 2, v), xytext=(0, 6),
                    textcoords="offset points", ha="center", va="bottom", fontsize=13, color=TEXT_PRIMARY,
                    fontweight="bold")
    ax.set_ylim(0, 15.5)
    ax.set_yticks([0, 5, 10, 15])
    style_axes(ax, title="Passive funds passed active in 2023, by about $60 billion",
               ylabel="U.S. fund assets at the end of 2023, $ trillions")
    ax.text(0, -0.11, "Morningstar data as reported by CNBC, January 2024", transform=ax.transAxes,
            fontsize=11, color=TEXT_MUTED, ha="left", va="top")
    return cap_width(save_figure(fig, out))


def chart_pitch_structure(out):
    parts = [
        ("1", "The one-line thesis", "Stock, direction, target, time frame and the reason, in one sentence", False),
        ("2", "What the business does", "How it makes money, who pays it and roughly how big it is, in two sentences", False),
        ("3", "Why the market is wrong", "What consensus believes, what you believe with a number, and why the gap exists", True),
        ("4", "Valuation", "Two methods that agree, with the arithmetic shown", False),
        ("5", "What gets the market to notice", "Two or three observable things you would watch each quarter", False),
        ("6", "Risks and the downside case", "The two biggest risks, and a number on what the stock is worth if you are wrong", True),
        ("7", "What would make you change your mind", "A selling rule written before you buy, and what would not change it", True),
    ]
    from matplotlib.patches import FancyBboxPatch
    fig, ax = new_figure(width=11, height=8.2)
    ax.set_axis_off()
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    n = len(parts)
    top, bottom = 91.0, 5.5
    slot = (top - bottom) / n
    box_h = slot * 0.78
    for i, (num, title, desc, key) in enumerate(parts):
        y_top = top - i * slot
        y0 = y_top - box_h
        mid = y0 + box_h / 2
        fill = BLUE if key else GRAY_SOFT
        ink = "white" if key else TEXT_PRIMARY
        sub = "#dce9fa" if key else TEXT_SECONDARY
        ax.add_patch(FancyBboxPatch((3, y0), 94, box_h, boxstyle="round,pad=0,rounding_size=1.2",
                                    facecolor=fill, edgecolor="none"))
        ax.text(6, mid, f"Part {num}", ha="left", va="center", fontsize=12.5, color=sub, fontweight="bold")
        ax.text(16, mid + box_h * 0.19, title, ha="left", va="center", fontsize=14.5, color=ink, fontweight="bold")
        ax.text(16, mid - box_h * 0.22, desc, ha="left", va="center", fontsize=11.5, color=ink if key else TEXT_SECONDARY)
        if i < n - 1:   # a short connector to the next part
            ax.annotate("", xy=(9, y0 - slot * 0.22 + 0.3), xytext=(9, y0 - 0.3),
                        arrowprops=dict(arrowstyle="-|>", color=TEXT_MUTED, lw=1.4, mutation_scale=12))
    ax.text(3, 97, "The seven parts of a long-only stock pitch, in the order you say them", ha="left", va="center",
            fontsize=16, fontweight="bold", color=TEXT_PRIMARY)
    ax.add_patch(FancyBboxPatch((3, 0.8), 2.2, 2.2, boxstyle="round,pad=0,rounding_size=0.5", facecolor=BLUE, edgecolor="none"))
    ax.text(6.4, 1.9, "Parts 3, 6 and 7 are where long-only interviews are decided, so they get the most prep time",
            ha="left", va="center", fontsize=11.5, color=TEXT_SECONDARY)
    return cap_width(save_figure(fig, out))


def chart_dcf_heatmap(out):
    rates = [0.065, 0.07, 0.075, 0.08, 0.085]
    growths = [0.02, 0.025, 0.03, 0.035, 0.04]
    grid = [[harlow_value(r, g) for g in growths] for r in rates]
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("wsg_seq_blue", SEQ_BLUE)
    fig, ax = new_figure(width=9.5, height=6.4)
    vmin, vmax = 30, 100
    im = ax.imshow(grid, cmap=cmap, vmin=vmin, vmax=vmax, aspect="auto")
    # the surface gap between cells
    for k in range(1, 5):
        ax.axhline(k - 0.5, color=SURFACE, linewidth=3)
        ax.axvline(k - 0.5, color=SURFACE, linewidth=3)
    for i, r in enumerate(rates):
        for j, g in enumerate(growths):
            v = grid[i][j]
            frac = (v - vmin) / (vmax - vmin)
            ax.text(j, i, f"${v:,.0f}", ha="center", va="center", fontsize=15,
                    color="white" if frac > 0.42 else TEXT_PRIMARY, fontweight="bold")
    # base case cell (7.5 percent, 3 percent) gets an ink outline
    from matplotlib.patches import Rectangle
    ax.add_patch(Rectangle((2 - 0.5, 2 - 0.5), 1, 1, fill=False, edgecolor=TEXT_PRIMARY, linewidth=2.5, zorder=5))
    ax.text(2, 2 + 0.36, "base case", ha="center", va="center", fontsize=10.5, color=TEXT_PRIMARY)
    ax.set_xticks(range(5))
    ax.set_xticklabels([f"{g:.1%}" for g in growths])
    ax.set_yticks(range(5))
    ax.set_yticklabels([f"{r:.1%}" for r in rates])
    ax.grid(False)
    ax.tick_params(length=0)
    for sp in ax.spines.values():
        sp.set_visible(False)
    ax.set_xlabel("Terminal growth rate")
    ax.set_ylabel("Discount rate")
    ax.set_title("Two inputs you can't observe move the DCF value from \\$34 to \\$95 a share", loc="left", pad=30)
    ax.text(0, 1.02, "Harlow Dental Supply (fictional), value per share today; the stock trades at \\$40",
            transform=ax.transAxes, fontsize=11.5, color=TEXT_SECONDARY, ha="left", va="bottom")
    cb = fig.colorbar(im, ax=ax, fraction=0.04, pad=0.03)
    cb.set_label("Value per share ($)", color=TEXT_SECONDARY)
    cb.outline.set_visible(False)
    cb.ax.tick_params(length=0, colors=TEXT_SECONDARY)
    return cap_width(save_figure(fig, out))


def chart_bond_price_yield(out):
    import numpy as np
    ys = np.linspace(0.01, 0.10, 181)
    ps = [bond_price(y) for y in ys]
    fig, ax = new_figure(width=10, height=6.0)
    ax.plot(ys * 100, ps, color=BLUE, linewidth=2.4)
    pts = [(0.04, "$1,045 at 4%", (10, 8)), (0.05, "$1,000 at 5%, issued at par", (10, 8)), (0.06, "$958 at 6%", (10, 8))]
    for y, label, off in pts:
        p = bond_price(y)
        ax.plot(y * 100, p, marker="o", markersize=10, color=BLUE, markeredgecolor=SURFACE, markeredgewidth=2)
        ax.annotate(label, (y * 100, p), xytext=off, textcoords="offset points", fontsize=12.5,
                    color=TEXT_PRIMARY, fontweight="bold", ha="left", va="bottom")
    ax.axhline(1000, color=GRID, linewidth=1.0, zorder=0)
    ax.set_xlim(1, 10)
    ax.set_ylim(750, 1250)
    ax.set_xticks(range(1, 11))
    ax.set_xticklabels([f"{x}%" for x in range(1, 11)])
    ax.set_yticks([800, 900, 1000, 1100, 1200])
    ax.set_yticklabels([f"${v:,}" for v in (800, 900, 1000, 1100, 1200)])
    style_axes(ax, title="One point of yield moves a 5-year 5 percent bond about \\$42 to \\$45",
               xlabel="Market yield", ylabel="Price of a \\$1,000 bond paying \\$50 a year for 5 years")
    return cap_width(save_figure(fig, out))


# ------------------------------------------------------------------ main
def main():
    check_numbers()
    OUT.mkdir(parents=True, exist_ok=True)
    entries = []

    chart_passive_active(OUT / "01-passive-vs-active-fund-assets-2023.png")
    entries.append({
        "file": "01-passive-vs-active-fund-assets-2023.png",
        "alt": "Bar chart of U.S. fund assets at end of 2023, passive funds 13.29 trillion dollars and active funds 13.23 trillion",
        "caption": "Passive funds held $13.29 trillion of U.S. fund assets at the end of 2023 against $13.23 trillion in active funds, by Morningstar's count as reported by CNBC in January 2024.",
        "method": "chart from the article's figures ($13.29 trillion passive, $13.23 trillion active, end of 2023, Morningstar via CNBC), which carry a VERIFY tag in the draft",
        "anchor": "No, but it's hard in a different way. A bulge bracket bank hires hundreds"[:60],
    })

    chart_pitch_structure(OUT / "02-seven-part-stock-pitch-structure.png")
    entries.append({
        "file": "02-seven-part-stock-pitch-structure.png",
        "alt": "Diagram of the seven parts of a stock pitch in order, with parts three, six and seven highlighted in blue",
        "caption": "Say the seven parts in this order; the blue ones are where a long-only interviewer spends the most time, and where most undergrads have the least.",
        "method": "diagram from the article's section 3 structure (parts 1 to 7)",
        "anchor": "Every strong pitch answers the same seven questions. Learn the order"[:60],
    })

    chart_dcf_heatmap(OUT / "03-dcf-sensitivity-discount-rate-terminal-growth.png")
    entries.append({
        "file": "03-dcf-sensitivity-discount-rate-terminal-growth.png",
        "alt": "Heatmap of DCF value per share across discount rates from 6.5 to 8.5 percent and terminal growth from 2 to 4 percent",
        "caption": "The base case is $51 at 7.5 percent and 3 percent growth; move one row down and one column left to 8.5 and 2.5 percent and the same cash flows are worth $37, below the $40 price.",
        "method": "grid computed from the article's section 4 DCF table (unlevered free cash flow of 368, 398, 424, 438 and 453, terminal value at year 5 cash flow times one plus growth over the rate less growth, net debt 1.2 billion, 150 million shares); the article's $51, $37 and $40 cells reproduce",
        "anchor": "Say the sensitivity out loud too. At an 8.5 percent discount rate"[:60],
    })

    chart_bond_price_yield(OUT / "04-bond-price-vs-yield-5-year-5-percent.png")
    entries.append({
        "file": "04-bond-price-vs-yield-5-year-5-percent.png",
        "alt": "Line chart of a 5-year 5 percent bond's price falling as market yield rises, with 1,045, 1,000 and 958 dollars marked",
        "caption": "The same one point move in yields takes $42 off the price going up and adds $45 coming down; duration, in the next section, is the shortcut for that slope.",
        "method": "curve computed with standard bond math (annual $50 coupons, $1,000 face, 5 years, price equals the present value of coupons and principal at the market yield); the article's $958 at 6 percent and $1,045 at 4 percent reproduce",
        "anchor": "Price and yield move in opposite directions, and here's the mechanism."[:60],
    })

    write_manifest(OUT, entries)
    for e in entries:
        for k in ("alt", "caption", "method", "anchor"):
            assert "\u2014" not in e[k] and "\u2013" not in e[k], f"dash in manifest {e['file']} {k}"
    print(f"wrote {len(entries)} images and manifest.json to {OUT}")


if __name__ == "__main__":
    main()
