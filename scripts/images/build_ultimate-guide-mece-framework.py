#!/usr/bin/env python3
"""Images for drafts/draft-ultimate-guide-mece-framework-v1.md (October 5, 2026).

Run from the repo root:  python3 scripts/images/build_ultimate-guide-mece-framework.py
Idempotent: rewrites every PNG in published/assets/images/ultimate-guide-mece-framework/ and the manifest.

Every tree is the article's own indented bullet list drawn as boxes, and every number on a branch or a
chart is recomputed here from the article's inputs and asserted against the figure the article states
before anything is drawn. No workbook: the article has no model, only trees and three small exhibits.
"""
import sys
from pathlib import Path

sys.path.insert(0, "scripts/images")
from wsg_viz import *          # noqa: E402,F401
from wsg_diagrams import *     # noqa: E402,F401

OUT = Path("published/assets/images/ultimate-guide-mece-framework")
OUT.mkdir(parents=True, exist_ok=True)
entries = []

TREE_COLS = dict(col_w=(2.1, 2.4, 3.1, 3.1))


def add(file, alt, caption, method, anchor):
    assert 10 <= len(alt.split()) <= 20, (file, len(alt.split()))
    for s in (alt, caption, method, anchor):
        assert not any(ch in s for ch in ("\u2014", "\u2013", "\u2212")), s   # no em, en or minus dashes
    entries.append({"file": file, "alt": alt, "caption": caption, "method": method, "anchor": anchor})


def close(a, b, tol=1e-6):
    return abs(a - b) <= tol


def tree_figure(title, root, out_name, note=None, col_w=(2.1, 2.4, 3.1, 3.1), col_labels=None,
                note_h=0.0, min_w=0.0, **kw):
    """Size a canvas for a nested tree, draw the title, the tree and an optional italic note at the bottom.
    A title wider than the tree is wrapped onto two lines rather than running off the canvas."""
    W, Ht = tree_extent(root, col_w=col_w, **kw)
    W = max(W, min_w)
    title_w = len(title) * 18 * 0.47 / 72      # bold Arial at 18 pt averages about 0.47 em per character
    if title_w > W - 0.45:
        title = wrap(title, W - 0.7, 18, bold=True)
    title_lines = title.count("\n") + 1
    top_pad = 0.55 + 0.32 * title_lines + (0.3 if col_labels else 0.0)
    note_space = note_h if note else 0.0
    H = round(Ht + top_pad + 0.35 + note_space, 2)
    fig, ax = canvas(W, H, title=title)
    nested_tree(ax, root, y_top=H - top_pad, col_w=col_w, col_labels=col_labels, **kw)
    if note:
        label(ax, 0.35, note_space / 2 + 0.1, note, size=11.5, color=TEXT_SECONDARY, italic=True, va="center",
              wrap_in=W - 0.8)
    finish(fig, OUT / out_name)
    return W, H


# ---------------------------------------------------------------- 01 festival: overlap, gap, MECE
def festival():
    """Section 1. Three ways to sort ticket stubs by age, drawn as intervals on an age line."""
    W, H = 11, 6.3
    fig, ax = canvas(W, H, title="The same four boxes three ways: two fail a test, the third passes both")
    x0, x1 = 2.5, 10.2            # the age line, 0 to 70 (50 and over runs to the edge)
    amin, amax = 0, 70

    def ax_x(age):
        return x0 + (age - amin) / (amax - amin) * (x1 - x0)

    from matplotlib.patches import FancyBboxPatch

    rows = [
        ("Overlap", "under 18, 18 to 30, 30 to 50, 50 and over",
         [(0, 18, "Under 18"), (18, 31, "18 to 30"), (30, 51, "30 to 50"), (50, 70, "50 and over")],
         "A 30-year-old's stub fits box two and box three. Same for every 50-year-old.", RED),
        ("Gap", "under 18, 20 to 29, 30 to 49, 50 and over",
         [(0, 18, "Under 18"), (20, 30, "20 to 29"), (30, 50, "30 to 49"), (50, 70, "50 and over")],
         "An 18-year-old or a 19-year-old fits no box, so those stubs pile up on the floor.", RED),
        ("MECE", "under 18, 18 to 29, 30 to 49, 50 and over",
         [(0, 18, "Under 18"), (18, 30, "18 to 29"), (30, 50, "30 to 49"), (50, 70, "50 and over")],
         "Every age lands in exactly one box, and the four boxes hold everyone.", "#008300"),
    ]
    y = H - 1.25
    row_h, bar_h = 1.55, 0.42
    for verdict, spec, boxes, why, vcol in rows:
        label(ax, 0.35, y - bar_h / 2, verdict, size=14, bold=True, color=vcol, va="center")
        label(ax, 0.35, y - bar_h / 2 - 0.34, spec, size=10.5, color=TEXT_SECONDARY, va="center", wrap_in=2.0)
        for i, (a, b, name) in enumerate(boxes):
            xa, xb = ax_x(a), ax_x(b)
            fill = BLUE if i % 2 == 0 else SEQ_BLUE[9]
            yb = y - bar_h
            ax.add_patch(FancyBboxPatch((xa + 0.01, yb), xb - xa - 0.02, bar_h, boxstyle="round,pad=0,rounding_size=0.05",
                                        facecolor=fill, edgecolor=SURFACE, linewidth=1.5, zorder=3 + i))
            ax.text((xa + xb) / 2, yb + bar_h / 2, name, ha="center", va="center", fontsize=11, color="white",
                    fontweight="bold", zorder=10)
            if b == 70:
                ax.annotate("", xy=(xb + 0.25, yb + bar_h / 2), xytext=(xb, yb + bar_h / 2),
                            arrowprops=dict(arrowstyle="-|>", color=fill, lw=2, mutation_scale=14), zorder=4)
        if verdict == "Overlap":
            for age in (30, 50):
                xa, xb = ax_x(age), ax_x(age + 1)
                ax.add_patch(FancyBboxPatch((xa, y - bar_h - 0.06), xb - xa, bar_h + 0.12, boxstyle="round,pad=0,rounding_size=0.0",
                                            facecolor="white", edgecolor=RED, linewidth=2, hatch="////", zorder=6))
                ax.text((xa + xb) / 2, y + 0.11, f"Age {age}: two boxes", ha="center", va="bottom", fontsize=10.5, color=RED, zorder=6)
        if verdict == "Gap":
            xa, xb = ax_x(18), ax_x(20)
            ax.add_patch(FancyBboxPatch((xa, y - bar_h), xb - xa, bar_h, boxstyle="round,pad=0,rounding_size=0.0",
                                        facecolor="white", edgecolor=RED, linewidth=2, hatch="////", zorder=4))
            ax.text((xa + xb) / 2, y + 0.11, "Ages 18 and 19: no box", ha="center", va="bottom", fontsize=10.5, color=RED, zorder=6)
        label(ax, x0, y - bar_h - 0.3, why, size=11, color=TEXT_SECONDARY, va="center", wrap_in=x1 - x0 + 0.5)
        y -= row_h
    # age axis
    ya = y + row_h - bar_h - 0.62
    ax.plot([x0, x1 + 0.25], [ya, ya], color=TEXT_SECONDARY, lw=1.2, zorder=2)
    for age in (0, 10, 18, 30, 40, 50, 60):
        xa = ax_x(age)
        ax.plot([xa, xa], [ya - 0.05, ya + 0.05], color=TEXT_SECONDARY, lw=1.0)
        ax.text(xa, ya - 0.1, str(age), ha="center", va="top", fontsize=10.5, color=TEXT_SECONDARY)
    ax.text(x1 + 0.25, ya - 0.1, "age", ha="right", va="top", fontsize=10.5, color=TEXT_SECONDARY)
    finish(fig, OUT / "01-festival-overlap-gap-mece.png")
    add("01-festival-overlap-gap-mece.png",
        "Three rows of festival age boxes: one overlaps at 30 and 50, one skips 18 and 19, one is MECE",
        "Sort the same 1,000 ticket stubs three ways and the test is visible: the first set claims 30-year-olds twice, the second has no box for an 18-year-old, and only the third passes both.",
        "Diagram drawn in matplotlib from the three age sorts in section 1 (overlap, gap, MECE)",
        "The version that works is under 18, 18 to 29, 30 to 49, 50 a")


# ---------------------------------------------------------------- 02 cut by formula
def formula_tree():
    root = N("Profit = Revenue minus Cost", [
        N("Revenue = Price × Volume", [N("Volume = Number of customers × Purchases per customer")]),
        N("Cost = Fixed cost + Variable cost", [N("Variable cost = Volume × Cost per unit")]),
    ])
    tree_figure("Cut by formula: the equation names the branches, so nothing can hide outside it", root,
                "02-cut-by-formula-tree.png", col_w=(2.2, 2.6, 3.4), gaps=(0.0, 0.5, 0.2),
                note="A bakery's revenue fell from $1.2 million to $1.08 million at $4 a loaf both years: 300,000 loaves became 270,000. The price branch closes in two sentences and the whole problem sits in volume.",
                note_h=0.9)
    assert close(1_200_000 / 4, 300_000) and close(1_080_000 / 4, 270_000)
    add("02-cut-by-formula-tree.png",
        "Tree splitting profit into revenue and cost, each broken into its own formula",
        "A formula tree is MECE by construction: profit splits into revenue and cost, revenue into price and volume, and the bakery example closes the price branch in two sentences.",
        "Tree drawn in matplotlib from the cut-by-formula bullet list in section 3 and the bakery example beneath it",
        "- Variable cost = Volume × Cost per unit")


# ---------------------------------------------------------------- 03 cut by process: the order funnel
def order_funnel():
    visits, cart, start, pay = 1_000_000, 0.10, 0.50, 0.90
    base = visits * cart * start * pay
    now = visits * cart * 0.40 * pay
    assert close(base, 45_000) and close(now, 36_000), (base, now)
    W, H = 11, 5.7
    fig, ax = canvas(W, H, title="Cut by process: walk the order through four steps and the leak shows itself")
    steps = [("Step 1", "Visits to the site", "traffic"), ("Step 2", "Adds an item to the cart", "product page"),
             ("Step 3", "Starts checkout", "cart page"), ("Step 4", "Completes payment", "checkout page")]
    bw, bh, gap = 1.78, 1.0, 0.36
    x = 0.35
    y_box = H - 1.85
    base_vals = ["1,000,000 visits", "10 percent: 100,000", "50 percent: 50,000", "90 percent: 45,000 orders"]
    now_vals = ["1,000,000 visits", "10 percent: 100,000", "40 percent: 40,000", "90 percent: 36,000 orders"]
    label(ax, 0.35, y_box - bh - 0.42, "Baseline month", size=12, bold=True, va="center")
    label(ax, 0.35, y_box - bh - 1.02, "This month", size=12, bold=True, va="center")
    for i, (step, what, where) in enumerate(steps):
        leak = i == 2
        text_box(ax, x, y_box - bh, bw, bh, f"{step}\n{what}\n({where})", fill=ORANGE if leak else BLUE,
                 text_color="white", size=12, bold=False, linespacing=1.3)
        label(ax, x + bw / 2, y_box - bh - 0.42 - 0.3, base_vals[i], size=11.5, ha="center", va="center")
        label(ax, x + bw / 2, y_box - bh - 1.02 - 0.3, now_vals[i], size=11.5, ha="center", va="center",
              bold=leak, color=ORANGE if leak else TEXT_PRIMARY)
        if i < len(steps) - 1:
            arrow(ax, (x + bw + 0.04, y_box - bh / 2), (x + bw + gap - 0.04, y_box - bh / 2), color=TEXT_SECONDARY, lw=1.8)
        x += bw + gap
    # after the order
    text_box(ax, x, y_box - bh, 1.65, bh, "After the order: delivery, returns, repeat purchase", fill=PALE_GRAY,
             size=11, linespacing=1.3, pad_in=0.1)
    arrow(ax, (x - gap + 0.04, y_box - bh / 2), (x - 0.04, y_box - bh / 2), color=TEXT_SECONDARY, lw=1.8)
    # formula line under the title
    label(ax, 0.35, H - 0.95, "Orders = Visits × Add-to-cart rate × Checkout-start rate × Payment-completion rate",
          size=12.5, color=TEXT_SECONDARY, va="center")
    label(ax, 0.35, 0.5, "Three of the four rates held. The share of cart holders who start checkout fell from 50 percent to 40 percent, so the 9,000 missing orders leak on the cart page, and you know that before anyone mentions a shipping fee.",
          size=11.5, color=TEXT_SECONDARY, italic=True, va="center", wrap_in=W - 0.8)
    finish(fig, OUT / "03-cut-by-process-order-funnel.png")
    add("03-cut-by-process-order-funnel.png",
        "Four step order process with baseline and current month numbers, the checkout start step highlighted as the leak",
        "Lay the two months side by side step by step and only one rate moved: checkout starts fell from 50 to 40 percent, which is the whole 9,000 order gap.",
        "Process diagram drawn in matplotlib from the cut-by-process bullet list and the online retailer example in section 3; orders recomputed as 1,000,000 × 0.10 × 0.50 × 0.90 and × 0.40",
        "An online retailer gets 1,000,000 visits a month. 10 percent")


# ---------------------------------------------------------------- 04 cut by segment: sneaker revenue
def segment_tree():
    stores, wholesale, online, us, intl = 200, 300, 100, 70, 30
    assert stores + wholesale + online == 600 and us + intl == online
    root = N("Revenue of a sneaker brand: $600 million", [
        N("The brand's own stores: $200 million"),
        N("Wholesale, sold through other retailers: $300 million"),
        N("Online, direct to the customer: $100 million", [
            N("United States: $70 million"),
            N("International: $30 million"),
        ]),
    ])
    tree_figure("Cut by segment: one dimension per level, and every level sums to the one above", root,
                "04-cut-by-segment-revenue-tree.png", col_w=(2.2, 3.4, 2.6), gaps=(0.0, 0.3, 0.16),
                sizes=(13.5, 12, 11.5), bold_depth=0, center_depth=0,
                col_labels=["", "Level 1: by channel", "Level 2: by geography"],
                note="$200 million plus $300 million plus $100 million is the $600 million on top; $70 million plus $30 million is the $100 million above them. The sum test passes at both levels.",
                note_h=0.9)
    add("04-cut-by-segment-revenue-tree.png",
        "Tree splitting $600 million of sneaker revenue by channel, then the online channel by geography",
        "Channel on one level and geography on the next: the three channels add to $600 million and the two regions add to the $100 million of online sales above them.",
        "Tree drawn in matplotlib from the cut-by-segment bullet list in section 3; the sums are checked in the build script",
        "- International: $30 million")


# ---------------------------------------------------------------- 05 cut by opposites: airline on-time rate
def opposites_tree():
    root = N("Why did a regional airline's on-time rate fall from 85 percent to 75 percent?", [
        N("Causes inside the airline (things it controls)", [
            N("Crew scheduling: crews timing out, late connections between flights"),
            N("Maintenance: planes held at the gate for repairs"),
            N("Turnaround: boarding, fueling, and baggage running long"),
            N("The schedule itself: too little time planned between flights"),
        ]),
        N("Causes outside the airline (things it doesn't control)", [
            N("Weather"),
            N("Air traffic control delays"),
            N("Airport congestion and gate availability"),
            N("Late inbound planes from partner airlines"),
        ]),
    ])
    tree_figure("Cut by opposites: every late flight's first cause was the airline's decision or it wasn't", root,
                "05-cut-by-opposites-airline-tree.png", col_w=(2.3, 2.5, 4.6), gaps=(0.0, 0.4, 0.13),
                note="Airlines code every delay to a reason, so the data to split the two branches exists; the next level has to be named causes you can test, or 'external' is just 'everything else' wearing a name.",
                note_h=0.9)
    add("05-cut-by-opposites-airline-tree.png",
        "Tree splitting an airline's on-time decline into causes inside the airline and causes outside it",
        "Inside versus outside gets you to full coverage in one line, and the four named causes under each branch are what make it a structure instead of a label.",
        "Tree drawn in matplotlib from the cut-by-opposites bullet list in section 3",
        "- Late inbound planes from partner airlines")



# ---------------------------------------------------------------- shared money formatter for bridges
class Money:
    """'$11.25M' or '$3.6M': the article's own precision, no trailing zeros, parentheses for a decrease."""
    def __init__(self, paren=False, unit="M"):
        self.paren, self.unit = paren, unit

    def format(self, v):
        txt = f"{v:,.2f}".rstrip("0").rstrip(".")
        if "." not in txt:
            txt = f"{v:,.1f}"
        return f"(${txt}{self.unit})" if self.paren else f"${txt}{self.unit}"


# ---------------------------------------------------------------- restaurant numbers (tree 1), recomputed from the inputs
def restaurant_numbers():
    n, cov0, cov1, chk0, chk1 = 150, 60_000, 57_000, 25.0, 26.0
    rev0, rev1 = n * cov0 * chk0 / 1e6, n * cov1 * chk1 / 1e6
    vol_effect = -(cov0 - cov1) * n * chk0 / 1e6
    price_effect = (chk1 - chk0) * n * cov1 / 1e6
    costs0 = {"Food and beverage": 67.5, "Labor": 72.0, "Occupancy": 27.0, "Other": 36.0}
    costs1 = {"Food and beverage": 71.1, "Labor": 77.6, "Occupancy": 28.4, "Other": 36.6}
    tc0, tc1 = sum(costs0.values()), sum(costs1.values())
    op0, op1 = rev0 - tc0, rev1 - tc1
    hrs0, hrs1, w0, w1 = 4.80, 4.85, 15.0, 16.0
    assert close(rev0, 225.0) and close(rev1, 222.3), (rev0, rev1)
    assert close(vol_effect, -11.25) and close(price_effect, 8.55) and close(vol_effect + price_effect, -2.7)
    assert close(tc0, 202.5) and close(tc1, 213.7) and close(tc1 - tc0, 11.2)
    assert close(op0, 22.5) and close(op1, 8.6) and close(op0 - op1, 13.9)
    assert close(hrs0 * w0, 72.0) and close(hrs1 * w1, 77.6)
    assert close((w1 - w0) * hrs1, 4.85) and close((hrs1 - hrs0) * w0, 0.75)
    assert abs(op1 / rev1 - 0.039) < 0.0005 and close(op0 / rev0, 0.10)
    return dict(rev0=rev0, rev1=rev1, vol=vol_effect, price=price_effect, costs0=costs0, costs1=costs1,
                tc0=tc0, tc1=tc1, op0=op0, op1=op1)


# ---------------------------------------------------------------- 06 tree 1: restaurant profit
def restaurant_tree():
    r = restaurant_numbers()
    root = N("Operating profit fell $13.9 million, from $22.5 million to $8.6 million", [
        N("Revenue fell $2.7 million, from $225.0 million to $222.3 million", [
            N("Volume: covers (meals served) per restaurant fell from 60,000 to 57,000 a year"),
            N("Price: the average check rose from $25 to $26"),
        ]),
        N("Costs rose $11.2 million, from $202.5 million to $213.7 million", [
            N("Food and beverage: $67.5 million to $71.1 million, up $3.6 million"),
            N("Labor: $72.0 million to $77.6 million, up $5.6 million", [
                N("Hours worked: 4.80 million to 4.85 million"),
                N("Wage rate: $15.00 to $16.00 an hour"),
            ]),
            N("Occupancy (rent, utilities, insurance): $27.0 million to $28.4 million, up $1.4 million"),
            N("Other (marketing, supplies, head office): $36.0 million to $36.6 million, up $0.6 million"),
        ]),
    ])
    tree_figure("Tree 1: profit by formula on top, by cost line underneath, and every level sums to the one above", root,
                "06-restaurant-profit-tree.png", col_w=(2.0, 2.2, 3.3, 2.3), col_gap=0.34, x0=0.3,
                sizes=(13, 12, 11.5, 11.5), gaps=(0.0, 0.4, 0.14, 0.1),
                note="Revenue: minus $11.25 million of volume plus $8.55 million of price is minus $2.7 million. Costs: $3.6 + $5.6 + $1.4 + $0.6 = $11.2 million. Labor: $4.85 million of wage rate plus $0.75 million of hours is $5.6 million. Every branch ties to the number above it.",
                note_h=1.0)
    add("06-restaurant-profit-tree.png",
        "Issue tree for a restaurant chain's $13.9 million profit drop: revenue down $2.7 million, costs up $11.2 million by line",
        "Every line on the chain's profit and loss statement has one home in this tree, and the labor branch splits again into hours and wage rate so you can see which part the client controls.",
        "Tree drawn in matplotlib from the tree 1 bullet list in section 5; every figure recomputed from the data table (150 restaurants, covers, check, cost lines, hours, wage) and asserted",
        "- Other (marketing, supplies, head office): $36.0 million to")


# ---------------------------------------------------------------- 07 tree 1: profit bridge
def restaurant_bridge():
    r = restaurant_numbers()
    fig, ax = new_figure(width=11, height=5.9)
    steps = [("Fewer covers (450,000 at the old $25 check)", r["vol"]),
             ("Higher check ($1 more on 8.55 million covers)", r["price"]),
             ("Food and beverage", -(r["costs1"]["Food and beverage"] - r["costs0"]["Food and beverage"])),
             ("Labor (wage rate $4.85M, hours $0.75M)", -(r["costs1"]["Labor"] - r["costs0"]["Labor"])),
             ("Occupancy", -(r["costs1"]["Occupancy"] - r["costs0"]["Occupancy"])),
             ("Other", -(r["costs1"]["Other"] - r["costs0"]["Other"]))]
    end = waterfall(ax, steps, r["op0"], "Operating profit two years ago", "Operating profit today",
                    fmt=Money(), neg_fmt=Money(paren=True), ylabel="$ millions",
                    title="Costs took $11.2 million of the $13.9 million profit drop, and labor alone $5.6 million",
                    ymin=0, legend_loc="upper right")
    assert close(end, 8.6), end
    ax.set_ylim(0, 36)
    ax.set_yticks([0, 10, 20, 30])
    finish(fig, OUT / "07-restaurant-profit-bridge.png")
    add("07-restaurant-profit-bridge.png",
        "Waterfall from $22.5 million of operating profit to $8.6 million: volume, price, then four cost lines",
        "Walk the bridge left to right and the revenue branch nearly nets out, so the $13.9 million drop is mostly the four cost lines, with labor the biggest of them.",
        "Waterfall from the tree 1 math list in section 5 (volume and price effects, the four cost line changes); start, steps and end asserted against the data table",
        "- Food cost per cover: $67.5 million ÷ 9.0 million = $7.50; ")


# ---------------------------------------------------------------- dishwasher numbers (tree 2)
def dishwasher_numbers():
    units, avg, prem_share, prem_price = 8e6, 800, 0.15, 1500
    prem_units = units * prem_share
    assert close(units * avg, 6.4e9) and close(prem_units, 1.2e6) and close(prem_units * prem_price, 1.8e9)
    gm, fixed, invest = 0.28, 45e6, 120e6
    rev10 = 150_000 * prem_price; gp10 = rev10 * gm; op10 = gp10 - fixed
    rev15 = 225_000 * prem_price; gp15 = rev15 * gm; op15 = gp15 - fixed
    assert close(rev10, 225e6) and close(gp10, 63e6) and close(op10, 18e6)
    assert close(rev15, 337.5e6) and close(gp15, 94.5e6) and close(op15, 49.5e6)
    assert abs(invest / op10 - 6.7) < 0.05 and abs(invest / op15 - 2.4) < 0.05
    return dict(op10=op10, op15=op15, pb10=invest / op10, pb15=invest / op15)


# ---------------------------------------------------------------- 08 and 09 tree 2: market entry, in two halves
def dishwasher_trees():
    dishwasher_numbers()
    q1 = ("Is the market worth entering?", [
        "Size: about 8 million dishwashers sold a year at an average $800, so $6.4 billion; premium is 15 percent of units, 1.2 million units at about $1,500, so $1.8 billion",
        "Growth: premium growing about 5 percent a year, so roughly 1.5 million units by year five",
        "Competition: who holds premium today, and how they'd respond to a new entrant",
        "Customers: what US buyers want (24-inch width, a third rack, drying performance, fast repairs)"])
    q2 = ("Can the client win there?", [
        "Product fit: does the European lineup fit US kitchens and habits",
        "Brand: awareness among US buyers is close to zero today",
        "Distribution: appliance chains, kitchen designers, home builders",
        "Service: repairs within days, parts stocked in the US"])
    q3 = ("Does the math work?", [
        "Revenue at a 10 percent premium share in year five: 150,000 units × $1,500 = $225 million",
        "Gross margin: 28 percent in the US after shipping and import costs, against 35 percent at home, so $63 million",
        "Fixed US costs: sales team, marketing, service network, about $45 million a year",
        "Operating profit in year five: $63 million minus $45 million = $18 million",
        "Investment to get there: about $120 million over five years (early losses, warehouses, showrooms, service)",
        "Payback: $120 million ÷ $18 million = about 6.7 years, counted from year five"])
    q4 = ("How would they enter, and what could go wrong?", [
        "Build it alone, partner with a US retailer, or buy a small US brand",
        "Risks: tariffs, a price response from incumbents, early service failures that kill the brand"])
    root_text = "Should the client enter the US premium dishwasher market?"
    folded = (PALE_GRAY, TEXT_SECONDARY, None)

    def build(open_qs, closed_qs, closed_note):
        kids = []
        for q, leaves in open_qs:
            kids.append(N(q, [N(l) for l in leaves]))
        for q, _ in closed_qs:
            kids.append(N(q + closed_note, fill=folded[0], text_color=folded[1], bold=False))
        return kids

    # part 1: questions 1 and 2 open, 3 and 4 folded
    root = N(root_text, build([q1, q2], [q3, q4], " (opened in the next tree)"))
    tree_figure("Tree 2, first half: is the prize real, and can the client take it?", root, "08-dishwasher-entry-tree-market-and-win.png",
                col_w=(2.2, 2.4, 5.4), gaps=(0.0, 0.36, 0.13), sizes=(13, 12, 11.5),
                note="Four questions, four branches: is the prize real, can we take it, is it worth taking, and how. One fact can serve two questions, but the questions themselves don't overlap.",
                note_h=0.9)
    add("08-dishwasher-entry-tree-market-and-win.png",
        "Market entry issue tree, first half: market size and growth questions, and whether the client can win in the US",
        "The first two questions of the entry tree: the premium segment is $1.8 billion, and the client's brand awareness in the US is close to zero.",
        "Tree drawn in matplotlib from the tree 2 bullet list in section 5 (branches 1 and 2, with branches 3 and 4 shown folded); the $6.4 billion, 1.2 million unit and $1.8 billion figures recomputed and asserted",
        "- Risks: tariffs, a price response from incumbents, early se")
    # part 2: questions 3 and 4 open, 1 and 2 folded
    root = N(root_text, build([q3, q4], [q1, q2], " (opened in the tree above)"))
    kids = root["children"]
    root["children"] = kids[2:] + kids[:2]     # keep the article's order: 1, 2 folded on top, then 3 and 4 open
    tree_figure("Tree 2, second half: the math at a 10 percent share, and how to enter", root, "09-dishwasher-entry-tree-math-and-entry.png",
                col_w=(2.2, 2.4, 5.4), gaps=(0.0, 0.36, 0.13), sizes=(13, 12, 11.5),
                note="At a 15 percent share the same branch gives $337.5 million of revenue, $94.5 million of gross profit, $49.5 million of operating profit and a 2.4-year payback. Five points of share turn a weak deal into a strong one.",
                note_h=0.9)
    add("09-dishwasher-entry-tree-math-and-entry.png",
        "Market entry issue tree, second half: the year five math at a 10 percent share, and entry mode and risks",
        "The math branch pays back in 6.7 years at a 10 percent share and 2.4 years at 15, so the case turns on the share question, which lives in the branch above.",
        "Tree drawn in matplotlib from the tree 2 bullet list and math list in section 5 (branches 3 and 4, with 1 and 2 folded); revenue, gross profit, operating profit and payback recomputed and asserted for both share cases",
        "- Year five at 15 percent share: 225,000 units × $1,500 = $3")


# ---------------------------------------------------------------- dental numbers (tree 3)
def dental_numbers():
    pts, vis, rpv = 100_000, 2.0, 600
    today = pts * vis * rpv / 1e6
    l1 = pts * 2.2 * rpv / 1e6
    l2 = 105_000 * 2.2 * rpv / 1e6
    l3 = 105_000 * 2.2 * 620 / 1e6
    assert close(today, 120.0) and close(today / 40, 3.0)
    assert close(l1, 132.0) and close(l2, 138.6) and close(l3, 143.22)
    d1, d2, d3 = l1 - today, l2 - l1, l3 - l2
    assert close(d1, 12.0) and close(d2, 6.6) and close(d3, 4.62) and close(d1 + d2 + d3, 23.22)
    gap = 150 - l3
    assert close(gap, 6.78) and abs(gap / 1.5 - 4.5) < 0.03
    new = 5 * 1.5
    assert close(l3 + new, 150.72)
    return dict(today=today, d1=d1, d2=d2, d3=d3, new=new, total=l3 + new, gap=gap)


# ---------------------------------------------------------------- 10 tree 3: dental growth
def dental_tree():
    dental_numbers()
    root = N("Grow revenue from $120 million to $150 million (plus $30 million)", [
        N("Revenue from the 40 practices they own today ($120 million now)", [
            N("More active patients (100,000 today, 2,500 per practice)", [
                N("More new patients in: referrals, online booking, joining more insurance networks"),
                N("Fewer patients lost: reminders, a better visit"),
            ]),
            N("More visits per patient (2.0 a year today)", [
                N("Recall compliance: getting the patient back for the second cleaning of the year"),
            ]),
            N("More revenue per visit ($600 today)", [
                N("Treatment accepted at the visit (fillings, crowns, aligners) versus a cleaning alone"),
                N("Price and insurance contracts"),
            ]),
        ]),
        N("Revenue from practices they don't own yet ($0 now)", [
            N("Open new practices"),
            N("Buy existing practices"),
        ]),
    ])
    tree_figure("Tree 3: opposites on top (own today versus don't), the revenue formula underneath", root,
                "10-dental-growth-tree.png", col_w=(2.0, 2.3, 2.6, 3.3), col_gap=0.34, x0=0.3,
                sizes=(13, 12, 11.5, 11.5), gaps=(0.0, 0.4, 0.16, 0.1),
                note="Sized: visits per patient 2.0 to 2.2 adds $12.0 million; patients 100,000 to 105,000 adds $6.6 million; revenue per visit $600 to $620 adds $4.62 million; five new practices at $1.5 million add $7.5 million. Total $150.72 million.",
                note_h=1.0)
    add("10-dental-growth-tree.png",
        "Growth issue tree for a dental chain: existing practices split by patients, visits and revenue per visit, plus new practices",
        "The top split is opposites and the existing-practice branch is the revenue formula, so any dollar of new revenue has exactly one home in this tree.",
        "Tree drawn in matplotlib from the tree 3 bullet list in section 5; the lever sizes in the note recomputed from the math list (100,000 patients, 2.0 visits, $600) and asserted",
        "- Buy existing practices")


# ---------------------------------------------------------------- 11 tree 3: lever bridge
def dental_levers():
    import numpy as np
    d = dental_numbers()
    fig, ax = new_figure(width=11, height=5.9)
    labels = ["Revenue today", "Recall: visits per patient 2.0 to 2.2", "Patients: 100,000 to 105,000",
              "Revenue per visit: $600 to $620", "Five new practices at $1.5 million each", "Year three"]
    steps = [d["d1"], d["d2"], d["d3"], d["new"]]
    xs = np.arange(len(labels))
    bottoms = [0]; heights = [d["today"]]; colors = [TEXT_MUTED]
    run = d["today"]
    for st in steps:
        bottoms.append(run); heights.append(st); colors.append(BLUE); run += st
    bottoms.append(0); heights.append(run); colors.append(TEXT_MUTED)
    assert close(run, 150.72)
    ax.bar(xs, heights, bottom=bottoms, width=0.62, color=colors, zorder=3)
    lvl = d["today"]
    for i, st in enumerate(steps):
        ax.plot([xs[i] + 0.31, xs[i + 1] - 0.31], [lvl, lvl], color=LINE, lw=1.0, zorder=2); lvl += st
    ax.plot([xs[-2] + 0.31, xs[-1] - 0.31], [lvl, lvl], color=LINE, lw=1.0, zorder=2)
    m = Money()
    ax.annotate(m.format(d["today"]), (xs[0], d["today"]), ha="center", va="bottom", xytext=(0, 4), textcoords="offset points",
                fontsize=12, fontweight="bold", color=TEXT_PRIMARY)
    for i, st in enumerate(steps):
        ax.annotate("+" + m.format(st), (xs[i + 1], bottoms[i + 1]), ha="center", va="top", xytext=(0, -4),
                    textcoords="offset points", fontsize=12, color=TEXT_PRIMARY)
    ax.annotate(m.format(run), (xs[-1], run), ha="center", va="bottom", xytext=(0, 4), textcoords="offset points",
                fontsize=12, fontweight="bold", color=TEXT_PRIMARY)
    ax.axhline(150, color=ORANGE, lw=2.2, zorder=2)
    ax.set_xticks(xs)
    ax.set_xticklabels([wrap(l, 1.3, 11) for l in labels], fontsize=11)
    ax.set_ylim(0, 185)
    ax.set_yticks([0, 50, 100, 150])
    ax.set_ylabel("$ millions")
    ax.set_title("Recall is the biggest lever and the cheapest; five acquisitions close the last $6.78 million", loc="left", pad=14)
    from matplotlib.patches import Patch
    from matplotlib.lines import Line2D
    ax.legend(handles=[Patch(color=TEXT_MUTED, label="Total"), Patch(color=BLUE, label="Lever (added revenue)"),
                       Line2D([0], [0], color=ORANGE, lw=2.2, label="The $150 million target")],
              loc="upper left", ncol=3, frameon=False, bbox_to_anchor=(0, 1.02))
    style_axes(ax)
    finish(fig, OUT / "11-dental-lever-bridge.png")
    add("11-dental-lever-bridge.png",
        "Bridge from $120 million of dental revenue to $150.72 million through four sized levers and a target line",
        "Size the levers before you rank them: recall adds $12 million for almost no money, and the acquisitions the owners called about add $7.5 million for the most capital and risk in the tree.",
        "Bridge drawn in matplotlib from the tree 3 math list in section 5 (today, three existing-practice levers, five new practices, total); every step recomputed from the inputs and asserted",
        "- Gap to the target: $150 million minus $143.22 million = $6")


# ---------------------------------------------------------------- operating room numbers (tree 4)
def or_numbers():
    rooms, hrs, days, use = 8, 10, 250, 0.55
    staffed = rooms * hrs * days
    in_use = staffed * use
    idle = staffed - in_use
    target = staffed * 0.75
    assert staffed == 20_000 and close(in_use, 11_000) and close(idle, 9_000) and close(target - in_use, 4_000)
    late = round(20 * rooms * days / 60)
    turnover = 20 * 3 * rooms * days / 60
    blocks, cancel = 4_500, 800
    end_day = idle - late - turnover - blocks - cancel
    assert late == 667 and close(turnover, 2_000) and close(end_day, 1_033)
    assert close(late + turnover + blocks + cancel + end_day, 9_000)
    assert close(3_000 + 1_000, 4_000)
    return dict(idle=idle, late=late, turnover=turnover, blocks=blocks, cancel=cancel, end_day=end_day)


# ---------------------------------------------------------------- 12 tree 4: operating rooms
def or_tree():
    o = or_numbers()
    root = N("9,000 idle operating room hours a year (20,000 staffed hours minus 11,000 hours of surgery)", [
        N("Before the first case, 667 hours: the first patient arrives after the scheduled start (late starts)"),
        N("Between cases, 2,000 hours: cleaning and set-up ('turnover') runs longer than the standard"),
        N("Reserved but unused, 4,500 hours: surgeons hold reserved time ('blocks') they don't fill, and release it too late for anyone else to use"),
        N("Cancelled on the day, 800 hours: the patient isn't ready, there's no bed for afterward, or the surgeon is unavailable"),
        N("End of day, 1,033 hours: a gap too short to fit another case"),
    ])
    tree_figure("Tree 4: an idle hour has to sit at one of five moments in the day, and there's no sixth", root,
                "12-operating-room-idle-hours-tree.png", col_w=(2.6, 7.2), gaps=(0.0, 0.16), sizes=(13, 11.5),
                bold_depth=0, center_depth=0,
                note="Late starts: 20 minutes × 8 rooms × 250 days = 667 hours. Turnover: 20 excess minutes × 3 turnovers × 8 rooms × 250 days = 2,000 hours. End of day is what's left: 9,000 minus 667 minus 2,000 minus 4,500 minus 800 = 1,033. The five branches add back to 9,000.",
                note_h=1.0)
    add("12-operating-room-idle-hours-tree.png",
        "Process issue tree splitting 9,000 idle operating room hours into five moments in the day, each with its hours",
        "A process cut is MECE because an empty hour has to happen at one of these five moments, and sizing each branch shows that the loudest complaint, late starts, is the smallest bucket.",
        "Tree drawn in matplotlib from the tree 4 bullet list in section 5; the hours on each branch recomputed from the math list (8 rooms, 10 hours, 250 days, 20 minutes, three turnovers) and asserted to sum to 9,000",
        "- End of day: a gap too short to fit another case")


# ---------------------------------------------------------------- 13 tree 4: idle hours by bucket
def or_chart():
    import numpy as np
    o = or_numbers()
    rows = [("Reserved but unused blocks", o["blocks"], 3_000), ("Turnover running over the standard", o["turnover"], 1_000),
            ("End-of-day gaps", o["end_day"], 0), ("Same-day cancellations", o["cancel"], 0), ("Late starts", o["late"], 0)]
    total = sum(r[1] for r in rows)
    assert close(total, 9_000)
    fig, ax = new_figure(width=11, height=5.6)
    ys = np.arange(len(rows))[::-1]
    rec = [r[2] for r in rows]
    rem = [r[1] - r[2] for r in rows]
    ax.barh(ys, rec, color=BLUE, height=0.58, zorder=3, label="Recovered by the plan (4,000 hours)")
    ax.barh(ys, rem, left=[x + (8 if x else 0) for x in rec], color=SEQ_BLUE[2], height=0.58, zorder=3, label="Still idle")
    for y, (name, hrs, r) in zip(ys, rows):
        ax.annotate(f"{hrs:,.0f} hours ({hrs / total * 100:.0f}%)", (hrs + (8 if r else 0), y), ha="left", va="center",
                    xytext=(6, 0), textcoords="offset points", fontsize=12, color=TEXT_PRIMARY)
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=12)
    ax.set_xlim(0, 5_600)
    ax.set_xticks([0, 1_000, 2_000, 3_000, 4_000, 5_000])
    ax.set_xticklabels(["0", "1,000", "2,000", "3,000", "4,000", "5,000"])
    ax.set_xlabel("Idle hours a year (9,000 in total)")
    ax.set_title("Unused blocks are half the idle time; late starts, the loudest complaint, are 7 percent", loc="left", pad=14)
    style_axes(ax, ygrid_only=False)
    ax.grid(True, axis="x"); ax.grid(False, axis="y")
    ax.legend(loc="lower right", frameon=False)
    ax.annotate("Releasing unfilled blocks 14 days out recovers two thirds of this branch (3,000 hours);\nhalving the turnover excess recovers 1,000 more. Together: the 4,000 hours the COO asked for.",
                (0.0, -0.3), xycoords="axes fraction", ha="left", va="top", fontsize=11, color=TEXT_SECONDARY, fontstyle="italic")
    fig.subplots_adjust(left=0.27, right=0.98, top=0.86, bottom=0.3)
    finish(fig, OUT / "13-operating-room-idle-hours-by-bucket.png", tight=True)
    add("13-operating-room-idle-hours-by-bucket.png",
        "Horizontal bar chart of 9,000 idle operating room hours by bucket, with the 4,000 hours the plan recovers shaded",
        "Size each bucket of waste before anyone proposes a fix: unused blocks hold 4,500 of the 9,000 hours, and the late starts every meeting argues about hold 667.",
        "Bar chart from the tree 4 math list in section 5 (667, 2,000, 4,500, 800, 1,033 hours) and the recommendation's 3,000 plus 1,000 recovery; totals asserted",
        "- Check: 667 + 2,000 + 4,500 + 800 + 1,033 = 9,000. The bran")


# ---------------------------------------------------------------- 14 drill 1: coffee chain, not MECE versus MECE
def coffee_side_by_side():
    products = ["Drinks (coffee, tea, cold drinks)", "Food (pastries, sandwiches)", "Packaged goods (beans, mugs, gift cards)"]
    root = N("Coffee chain revenue", [
        N("In store (walk-in orders at the counter)", [N(p) for p in products]),
        N("Drive-through", [N(p) for p in products]),
        N("App orders, picked up or delivered", [N(p) for p in products]),
    ])
    kw = dict(col_w=(1.35, 1.7, 2.25), col_gap=0.28, sizes=(12, 11.5, 11), gaps=(0.0, 0.26, 0.09), min_h=(0.9, 0.5, 0.42),
              pad_v=0.09, pad_in=0.1, x0=5.05)
    _, tree_h = tree_extent(root, **kw)
    W = 11
    H = round(tree_h + 1.95 + 0.4, 2)
    fig, ax = canvas(W, H, title="Drill 1: the flat list counts a latte twice; one dimension per level gives it one home")
    # left: the common attempt
    lx, bw, bh, gap = 2.55, 1.75, 0.5, 0.22
    label(ax, 0.35, H - 1.05, "A common attempt (not MECE)", size=12.5, bold=True, color=RED, va="center")
    label(ax, 0.35, H - 1.38, "coffee, cold drinks, food, mobile orders", size=11, color=TEXT_SECONDARY, va="center")
    names = ["Coffee", "Cold drinks", "Food", "Mobile orders"]
    tops = {}
    y = H - 1.85
    for nm in names:
        text_box(ax, lx, y - bh, bw, bh, nm, fill=PALE_BLUE, size=12, bold=True)
        tops[nm] = y - bh / 2
        y -= bh + gap
    items = [("A latte ordered on the app", ["Coffee", "Mobile orders"]), ("An iced coffee", ["Coffee", "Cold drinks"])]
    iy = [tops["Coffee"] + 0.0, tops["Cold drinks"] - 0.55]
    for (txt, hits), yy in zip(items, iy):
        text_box(ax, 0.35, yy - 0.3, 1.9, 0.6, txt, fill="white", edge=RED, text_color=RED, size=11, lw=1.5)
        for h in hits:
            arrow(ax, (0.35 + 1.9, yy), (lx, tops[h]), color=RED, lw=1.5, head=14, connection="arc3,rad=0.0")
    label(ax, 0.35, y - 0.25, "Coffee is a drink, so two branches overlap, and a mobile order for a latte lives in two places. Channel and product are different dimensions and belong on different levels.",
          size=11, color=TEXT_SECONDARY, italic=True, va="top", wrap_in=4.0)
    # divider
    ax.plot([4.75, 4.75], [0.4, H - 0.9], color=GRID, lw=1.2)
    # right: the MECE tree
    label(ax, 5.05, H - 1.05, "A MECE tree (one dimension per level)", size=12.5, bold=True, color="#008300", va="center")
    nested_tree(ax, root, y_top=H - 1.95, col_labels=["", "Level 1: by channel", "Level 2: by product"], **kw)
    finish(fig, OUT / "14-coffee-chain-not-mece-versus-mece.png")
    add("14-coffee-chain-not-mece-versus-mece.png",
        "A flat list giving an app latte two boxes, beside a tree with channel above product",
        "Drop a real order into each structure: the flat list gives a latte ordered on the app two homes, and the tree with channel above product gives it one.",
        "Diagram drawn in matplotlib from drill 1 in section 10 (the MECE tree and the common non-MECE attempt)",
        'A common non-MECE attempt: "coffee, cold drinks, food, mobil')


# ---------------------------------------------------------------- 15 drill 2: emergency room
def er_tree():
    root = N("Wait time rose", [
        N("More patients arriving (demand)", [
            N("More arrivals overall"),
            N("The same arrivals bunched into the same hours"),
        ]),
        N("Fewer staffed spots to see them (capacity)", [
            N("Fewer doctors and nurses per shift"),
            N("Beds closed"),
        ]),
        N("Each patient taking longer in the room (process)", [
            N("A sicker mix, so each patient needs more time"),
            N("Slow check-in and triage (the first quick assessment that ranks patients by urgency)"),
            N("Slow test results (imaging, bloodwork)"),
        ]),
        N("Patients who can't leave the ER (outflow)", [
            N("Admitted patients waiting for a bed upstairs, blocking an ER bed"),
        ]),
    ])
    tree_figure("Drill 2: a waiting line grows for four reasons, and the fourth is the one the flat list misses", root,
                "15-emergency-room-wait-tree.png", col_w=(1.9, 2.5, 4.9), gaps=(0.0, 0.34, 0.12), sizes=(13, 12, 11.5),
                note="The common attempt, 'understaffing, flu season, slow doctors, bad triage', mixes a cause of arrivals with two process items and one capacity item, and nothing in it covers patients stuck waiting for a bed upstairs, which is often the real answer.",
                note_h=1.0)
    add("15-emergency-room-wait-tree.png",
        "Issue tree for rising emergency room wait times: demand, capacity, process and outflow, with causes under each",
        "The formula behind any queue gives four branches, and the outflow branch (patients admitted but stuck in the ER) is the one a list of complaints leaves out.",
        "Tree drawn in matplotlib from drill 2 in section 10",
        "- Admitted patients waiting for a bed upstairs, blocking an ")


# ---------------------------------------------------------------- 16 drill 3: gym costs
def gym_tree():
    rev = 5_000 * 40 * 12
    var = 5_000 * 90
    profit = rev - 1_500_000 - var
    assert rev == 2_400_000 and var == 450_000 and profit == 450_000
    root = N("Gym costs", [
        N("Fixed: the same whether 1,000 or 5,000 people show up ($1.5 million)", [
            N("Rent"),
            N("Equipment leases and replacement"),
            N("Salaried staff (manager, front desk)"),
            N("Insurance and software"),
        ]),
        N("Variable: rises with members and visits ($90 per member per year, $450,000 at 5,000 members)", [
            N("Hourly staff and class instructors"),
            N("Utilities, towels, cleaning, supplies"),
            N("Card processing fees on each payment"),
        ]),
    ])
    tree_figure("Drill 3: opposites on top (fixed versus variable), cost lines underneath", root,
                "16-gym-costs-tree.png", col_w=(1.7, 2.7, 3.3), gaps=(0.0, 0.36, 0.12), sizes=(13, 12, 11.5),
                note="Quick numbers: 5,000 members × $40 a month × 12 = $2.4 million of revenue. $2.4 million minus $1.5 million of fixed cost minus $0.45 million of variable cost = $450,000 of profit. The common attempt ('rent, staff, equipment, marketing, electricity, cleaning') is a flat list where 'staff' straddles both branches.",
                note_h=1.1)
    add("16-gym-costs-tree.png",
        "Issue tree for a gym's costs: fixed lines and variable lines, with the article's quick numbers on the branches",
        "Fixed versus variable is a real pair of opposites, so every cost line has one branch, and 'staff' in the flat list fails because it sits in both.",
        "Tree drawn in matplotlib from drill 3 in section 10; revenue, variable cost and profit in the note recomputed from the quick numbers and asserted",
        "Quick numbers: 5,000 members × $40 a month × 12 = $2.4 milli")


# ---------------------------------------------------------------- 17 drill 10: trucking fuel bill
def trucking_tree():
    miles, mpg, price = 10e6, 6.5, 3.80
    gal = miles / mpg
    bill = gal * price
    assert abs(gal / 1e6 - 1.54) < 0.005 and abs(bill / 1e6 - 5.85) < 0.005, (gal, bill)
    loaded = miles * 0.85
    miles2 = loaded / 0.90
    gal2 = miles2 / mpg
    bill2 = gal2 * price
    assert abs(miles2 / 1e6 - 9.44) < 0.005 and abs(gal2 / 1e6 - 1.45) < 0.005 and abs(bill2 / 1e6 - 5.52) < 0.005
    save_empty = bill - bill2
    assert abs(save_empty - 320_000) < 10_000, save_empty        # the article says roughly $320,000
    bill3 = miles2 / 7.0 * price
    save_mpg = bill2 - bill3
    assert abs(save_mpg - 390_000) < 10_000, save_mpg            # the article says another $390,000 or so
    root = N("Fuel cost = gallons × price per gallon", [
        N("Gallons = miles driven ÷ miles per gallon", [
            N("Miles driven", [
                N("Loaded miles (paid)"),
                N("Empty miles (driving to the next load, unpaid)"),
            ]),
            N("Miles per gallon", [
                N("The truck: engine spec, tires, maintenance, aerodynamics"),
                N("The driver: speed, idling, braking"),
            ]),
        ]),
        N("Price per gallon", [
            N("Where and when the fleet fills up, bulk contracts, fuel hedging"),
        ]),
    ])
    tree_figure("Drill 10: the formula on top says which lever is worth the most before anyone argues", root,
                "17-trucking-fuel-cost-tree.png", col_w=(1.9, 2.3, 1.9, 3.4), col_gap=0.34, x0=0.3,
                sizes=(13, 12, 11.5, 11.5), gaps=(0.0, 0.4, 0.2, 0.1), min_h=(0.9, 0.62, 0.5, 0.46),
                note="Quick numbers: 10 million miles ÷ 6.5 miles per gallon = about 1.54 million gallons × $3.80 = about $5.85 million. Empty miles from 15 to 10 percent of the total saves roughly $320,000; raising miles per gallon from 6.5 to 7.0 saves another $390,000 or so.",
                note_h=1.0)
    add("17-trucking-fuel-cost-tree.png",
        "Issue tree for a trucking fuel bill: gallons split into miles driven and miles per gallon, plus price",
        "Driver training and newer trucks both move miles per gallon, better routes move miles driven and fuel cards move price, and the formula on top is what lets you size them against each other.",
        "Tree drawn in matplotlib from drill 10 in section 10; the quick numbers in the note recomputed from 10 million miles, 6.5 miles per gallon and $3.80 and asserted against the article's rounded figures",
        "Quick numbers: 10 million miles ÷ 6.5 miles per gallon = abo")


if __name__ == "__main__":
    festival()
    formula_tree()
    order_funnel()
    segment_tree()
    opposites_tree()
    restaurant_tree()
    restaurant_bridge()
    dishwasher_trees()
    dental_tree()
    dental_levers()
    or_tree()
    or_chart()
    coffee_side_by_side()
    er_tree()
    gym_tree()
    trucking_tree()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT}")
