#!/usr/bin/env python3
"""Images for drafts/draft-mbb-salary-breakdown-2026-v2.md (October 11, 2026; pointed at v2 October 12, 2026).

Run from the repo root:  python3 scripts/images/build_mbb-salary-breakdown-2026.py
Idempotent. Every number is read from the draft's own tables at run time (regex on the
table rows), so the pictures match whatever the draft says when the script runs. The
parse asserts that every row it needs exists and that the arithmetic ties (components add
to totals, bracket slices times rates equal the tax, gross less taxes equals take-home).
A mismatch stops the build.

Six images in the banking format (black Arial text, no gridlines, no frames, direct labels,
BANK_SERIES colors, a source line bottom-left) into published/assets/images/mbb-salary-breakdown-2026/:

  01  stacked horizontal bars: first-year base, maximum bonus and signing bonus by firm
  02  floating-range ladder: total cash by level at the three firms
  03  range bars: MBB vs investment banking total cash, year one and year three, with per-hour pay
  04  two bar panels: undergraduate base and bonus cap, MBB vs tier 2 and Big 4 strategy
  05  table graphic: the federal bracket math on the New York example
  06  waterfall: gross pay to take-home in New York City, with the monthly figure

The two tax images (05, 06) are built last, from a fresh read of the draft, because a QA
agent may correct the take-home figures while this runs. All six are dated (2026 pay and
2026 tax rules) and carry regenerate_at_publish: true in the manifest.

Nothing here edits the draft. The coordinator inserts the image lines with
scripts/images/insert_images.py from the manifest's anchors (each one a table row).
"""
import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import (BLACK, GRAY, MID_BLUE, NAVY, SURFACE, add_source, bank_table,  # noqa: E402
                     new_figure, save_figure, style_axes, write_manifest)

import matplotlib  # noqa: E402
matplotlib.rcParams["text.parse_math"] = False      # "$112,000" must never be read as mathtext
matplotlib.rcParams["axes.unicode_minus"] = False   # no Unicode minus signs anywhere
from matplotlib.patches import Patch  # noqa: E402

SLUG = "mbb-salary-breakdown-2026"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v2.md"
CONNECTOR = "#b9b8b3"
BAD_CHARS = ("—", "–", "−")
entries = []

# Source lines (set format: "Source: {outlet}, {topic}, {month year}.")
SRC_MC = "Source: Management Consulted, 2026 consulting salary report, 2026."
SRC_LADDER = ("Source: Management Consulted, 2026 consulting salary report, 2026; Hacking the Case Interview, "
              "firm salary pages, June 2026; StrategyCase, MBB salaries, August 2026.")
SRC_BANKING = ("Source: Management Consulted, 2026 consulting salary report, 2026; Mergers & Inquisitions, "
               "2026 investment banker salary report, 2026.")
SRC_IRS = "Source: IRS Revenue Procedure 2025-32, 2026 tax year."
SRC_TAX = "Source: IRS Revenue Procedure 2025-32 and New York Form IT-2105-I, 2026 tax year."


# ---------------------------------------------------------------- text and number helpers
def clean(s):
    """Every string a reader sees passes through here: no em or en dashes, no Unicode minus."""
    assert not any(ch in s for ch in BAD_CHARS), f"dash in image text: {s!r}"
    return s


def money(v):
    return f"${v:,.0f}"


def first_dollars(cell):
    """'$112,000' -> 112000; 'Up to $22,000 (HTCI: ...)' -> 22000; '$1.5 million+' -> 1500000."""
    m = re.search(r"\$([\d,]+(?:\.\d+)?)(\s*million)?", cell)
    assert m, f"no dollar figure in {cell!r}"
    v = float(m.group(1).replace(",", ""))
    if m.group(2):
        v *= 1_000_000
    return int(round(v))


def dollar_range(cell):
    """'$110,000 to $112,000' -> (110000, 112000); a single figure -> (v, v)."""
    nums = re.findall(r"\$[\d,]+(?:\.\d+)?(?:\s*million)?", cell)
    assert nums, f"no dollar figure in {cell!r}"
    vals = [first_dollars(n) for n in nums]
    return (vals[0], vals[1]) if " to " in cell and len(vals) > 1 else (vals[0], vals[0])


def bar_value(cell):
    """The figure to draw for a tier 2 table cell: the range if the cell is 'A to B', the first
    figure if a parenthesis follows it, zero if there is no dollar figure ('None until year three')."""
    head = cell.split("(")[0]
    if "$" not in head:
        return 0, 0
    return dollar_range(head)


def tables_in(text):
    """All markdown tables in the draft as lists of rows (lists of cell strings), separator rows dropped."""
    tables, cur = [], []
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                continue
            cur.append(cells)
        elif cur:
            tables.append(cur)
            cur = []
    if cur:
        tables.append(cur)
    return tables


def table(text, first_header):
    hits = [t for t in tables_in(text) if t and t[0] and t[0][0] == first_header]
    assert len(hits) == 1, f"expected one draft table headed {first_header!r}, found {len(hits)}"
    return hits[0]


def row(tbl, label):
    hits = [r for r in tbl[1:] if r[0].startswith(label)]
    assert len(hits) == 1, f"expected one row starting {label!r} in the table headed {tbl[0][0]!r}, found {len(hits)}"
    return hits[0]


# ---------------------------------------------------------------- figure helpers
def hbar_axes(ax):
    """Horizontal-bar banking style: category labels on the left, no value axis, one thin baseline at zero."""
    style_axes(ax, value_axis=True)     # value_axis=True keeps the y ticks, which carry the categories here
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_visible(True)
    ax.spines["left"].set_color(BLACK)
    ax.spines["left"].set_linewidth(0.8)
    ax.tick_params(axis="y", length=0, pad=8)


def fig_title(fig, title, subtitle=None):
    """Bold title (and a plain unit line under it) flush with the left edge of everything drawn."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    boxes = [ax.get_tightbbox(r) for ax in fig.axes]
    x0 = min(b.x0 for b in boxes)
    y1 = max(b.y1 for b in boxes)
    fx, fy = fig.transFigure.inverted().transform((x0, y1))
    y = fy + 0.025
    if subtitle:
        fig.text(fx, y, clean(subtitle), ha="left", va="bottom", fontsize=11.5, color=BLACK)
        y += 0.05
    fig.text(fx, y, clean(title), ha="left", va="bottom", fontsize=16, fontweight="bold", color=BLACK)


def fig_note(fig, ax, text, fontsize=11):
    """A plain note under the chart, flush with the left edge of everything drawn (same edge as the title
    and the source). Added as an axes child so add_source() lands below it."""
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    boxes = [a.get_tightbbox(r) for a in fig.axes]
    x0 = min(b.x0 for b in boxes)
    y0 = min(b.y0 for b in boxes)
    fx, fy = fig.transFigure.inverted().transform((x0, y0))
    ax.text(fx, fy - 0.025, clean(text), transform=fig.transFigure, ha="left", va="top", fontsize=fontsize,
            color=BLACK, linespacing=1.5)


def save(fig, name):
    """save_figure, then enforce the 2,200 px width cap (bbox_inches='tight' can add a few pixels)."""
    out = save_figure(fig, OUT / name)
    from PIL import Image
    im = Image.open(out)
    if im.width > 2200:
        im = im.convert("RGB").resize((2200, round(im.height * 2200 / im.width)), Image.LANCZOS)
        im.save(out, "PNG", optimize=True, dpi=(200, 200))
    print(f"rendered {name}")
    return out


def add(file, alt, caption, source, method, anchor):
    entries.append({"file": file, "alt": clean(alt), "caption": clean(caption), "source": clean(source),
                    "method": clean(method), "anchor": clean(anchor), "regenerate_at_publish": True})


# ---------------------------------------------------------------- 01: first-year cash by firm
def chart_first_year_cash(text):
    t = table(text, "Component")
    firms = t[0][1:]
    assert firms == ["McKinsey Business Analyst", "BCG Associate", "Bain Associate Consultant"], firms
    base = [first_dollars(c) for c in row(t, "Base salary")[1:]]
    bonus = [first_dollars(c) for c in row(t, "Performance bonus")[1:]]
    sign = [first_dollars(c) for c in row(t, "Signing bonus")[1:]]
    total = [first_dollars(c) for c in row(t, "Total cash, best case")[1:]]
    for f, b, p, s, tot in zip(firms, base, bonus, sign, total):
        assert b + p + s == tot, f"{f}: {b} + {p} + {s} != {tot} in the draft's best-case row"

    fig, ax = new_figure(width=11, height=5.2)
    ys = [2, 1, 0]
    h = 0.52
    for y, b, p, s, tot in zip(ys, base, bonus, sign, total):
        ax.barh(y, b, height=h, color=NAVY, edgecolor=SURFACE, linewidth=1.5, zorder=3)
        ax.barh(y, p, left=b, height=h, color=MID_BLUE, edgecolor=SURFACE, linewidth=1.5, zorder=3)
        ax.barh(y, s, left=b + p, height=h, color=GRAY, edgecolor=SURFACE, linewidth=1.5, zorder=3)
        ax.text(b / 2, y, money(b), ha="center", va="center", color="white", fontsize=12, fontweight="bold", zorder=4)
        ax.text(b + p / 2, y, money(p), ha="center", va="center", color="white", fontsize=11.5, zorder=4)
        ax.text(b + p + s / 2, y + h / 2 + 0.05, money(s), ha="center", va="bottom", color=BLACK, fontsize=10.5, zorder=4)
        ax.text(tot + 2_500, y, money(tot), ha="left", va="center", color=BLACK, fontsize=12.5, fontweight="bold")
    ax.set_yticks(ys)
    ax.set_yticklabels([clean(f.replace(" ", "\n", 1)) for f in firms], fontsize=12.5)
    ax.set_xlim(0, 170_000)
    ax.set_ylim(-0.6, 2.7)
    hbar_axes(ax)
    ax.legend(handles=[Patch(color=NAVY, label="Base salary"), Patch(color=MID_BLUE, label="Maximum performance bonus"),
                       Patch(color=GRAY, label="Signing bonus")],
              loc="upper left", bbox_to_anchor=(0, -0.03), ncol=3, frameon=False, fontsize=11.5)
    fig_title(fig, "First-year cash at McKinsey, BCG and Bain, 2026",
              "Undergraduate hires, best case: base, maximum bonus and signing bonus, dollars a year")
    add_source(fig, SRC_MC)
    save(fig, "01-first-year-cash-by-firm.png")
    add("01-first-year-cash-by-firm.png",
        "Stacked horizontal bars of 2026 first-year base, maximum bonus and signing bonus at McKinsey, BCG and Bain",
        f"Best-case first-year cash is {money(total[0])} at McKinsey, {money(total[1])} at BCG and {money(total[2])} at Bain.",
        SRC_MC,
        "Chart from the undergrad side-by-side table in the draft (base salary, performance bonus cap, signing bonus); "
        "the three segments are asserted to add to the table's best-case total row",
        "| Total cash, best case | $135,000 | $137,000 | $139,500 |"[:60])


# ---------------------------------------------------------------- 02: the pay ladder
def chart_ladder(text):
    t = table(text, "Level (years in)")
    firms = t[0][1:]
    assert firms == ["McKinsey", "BCG", "Bain"], firms
    levels = ["Analyst level (0 to 3)", "Post-MBA level (3 to 6)", "Manager level (6 to 8)", "Junior partner level (8 to 11)"]
    rows = [row(t, lv) for lv in levels]
    partner = row(t, "Partner (11+)")
    data = [[dollar_range(c) for c in r[1:]] for r in rows]
    for r, ranges in zip(rows, data):
        for lo, hi in ranges:
            assert 0 < lo <= hi, f"bad range in ladder row {r[0]!r}"

    fig, ax = new_figure(width=11, height=6.6)
    n = len(levels)
    offs, colors = [0.27, 0.0, -0.27], [NAVY, MID_BLUE, GRAY]
    for gi, ranges in enumerate(data):
        yg = n - 1 - gi
        for off, color, (lo, hi) in zip(offs, colors, ranges):
            y = yg + off
            ax.barh(y, hi - lo, left=lo, height=0.22, color=color, edgecolor=color, linewidth=0.8, zorder=3)
            ax.text(hi + 7_000, y, f"{money(lo)} to {money(hi)}", ha="left", va="center", fontsize=10.5, color=BLACK)
    ticks = []
    for r in rows:
        m = re.fullmatch(r"(.+?) \((.+)\)", r[0])
        ticks.append(clean(f"{m.group(1)}\n({m.group(2)} years in)"))
    ax.set_yticks(list(range(n))[::-1])
    ax.set_yticklabels(ticks, fontsize=12)
    ax.set_xlim(0, 830_000)
    ax.set_ylim(-0.6, n - 0.4)
    hbar_axes(ax)
    ax.legend(handles=[Patch(color=c, label=f) for c, f in zip(colors, firms)], loc="upper right", frameon=False, fontsize=12)
    note = (f"{partner[0].replace('(11+)', '(11+ years in)')}, not drawn: McKinsey {partner[1]}, BCG {partner[2]}, "
            f"Bain {partner[3]}.")
    fig_note(fig, ax, note)
    fig_title(fig, "Total cash by level at McKinsey, BCG and Bain, 2026",
              "Base plus bonus, dollars a year, years counted from an undergraduate start; the range spans three pay trackers")
    add_source(fig, SRC_LADDER)
    save(fig, "02-pay-ladder-by-level.png")
    an_lo, an_hi = min(r[0] for r in data[0]), max(r[1] for r in data[0])
    pm_lo, pm_hi = min(r[0] for r in data[1]), max(r[1] for r in data[1])
    add("02-pay-ladder-by-level.png",
        "Range chart of total cash at four levels from analyst to junior partner at McKinsey, BCG and Bain",
        f"Total cash goes from {money(an_lo)} to {money(an_hi)} at the analyst level to {money(pm_lo)} to {money(pm_hi)} at the post-MBA level.",
        SRC_LADDER,
        "Chart from the pay ladder table in the draft (total cash ranges by level and firm); the partner row is quoted in a note "
        "under the chart because its upper end would flatten the other four levels",
        "| Partner (11+) | $700,000 to $1.5 million+ | $700,000 to $2 million+ | $650,000 to $1.5 million+ |"[:60])


# ---------------------------------------------------------------- 03: MBB vs investment banking
def chart_mbb_vs_banking(text):
    t = table(text, "Year")
    assert t[0] == ["Year", "MBB (total cash)", "Investment banking (total cash)", "Gap"], t[0]
    r1, r3 = row(t, "Year one"), row(t, "Year three")
    groups = [("Year one", r1), ("Year three", r3)]
    for _, r in groups:
        (mlo, mhi), (blo, bhi), (glo, ghi) = dollar_range(r[1]), dollar_range(r[2]), dollar_range(r[3])
        assert (blo - mlo, bhi - mhi) == (glo, ghi), f"gap column does not match the ranges in {r[0]!r}"
    m = re.search(r"At \$([\d,]+) for a (\d+)-hour week over (\d+) weeks, an MBB analyst earns about \$(\d+) an hour; "
                  r"at \$([\d,]+) for an? (\d+)-hour week, a banking analyst earns about \$(\d+)", text)
    per_hour = None
    if m:
        m_pay, m_hrs, wks, m_rate, b_pay, b_hrs, b_rate = m.groups()
        m_pay, b_pay, m_hrs, b_hrs, wks = int(m_pay.replace(",", "")), int(b_pay.replace(",", "")), int(m_hrs), int(b_hrs), int(wks)
        assert round(m_pay / (m_hrs * wks)) == int(m_rate), "MBB per-hour figure in the draft does not reproduce"
        assert round(b_pay / (b_hrs * wks)) == int(b_rate), "banking per-hour figure in the draft does not reproduce"
        per_hour = (f"MBB: about ${m_rate} an hour ({money(m_pay)}, {m_hrs} hours a week, {wks} weeks)\n"
                    f"Banking: about ${b_rate} an hour ({money(b_pay)}, {b_hrs} hours a week, {wks} weeks)")

    fig, ax = new_figure(width=11, height=5.8)
    centers = [3.0, 1.0]
    h, off = 0.5, 0.35
    tick_pos, tick_lab = [], []
    for (name, r), yc in zip(groups, centers):
        for col, color, lab, dy in ((1, NAVY, "MBB", off), (2, GRAY, "Investment banking", -off)):
            lo, hi = dollar_range(r[col])
            y = yc + dy
            ax.barh(y, hi - lo, left=lo, height=h, color=color, zorder=3)
            ax.text(hi + 5_000, y, f"{money(lo)} to {money(hi)}", ha="left", va="center", fontsize=11.5, color=BLACK)
            tick_pos.append(y)
            tick_lab.append(lab)
        ax.text(4_000, yc + off + h / 2 + 0.3, name, ha="left", va="center", fontsize=12.5, fontweight="bold", color=BLACK)
        ax.text(365_000, yc, f"Gap: {r[3]}", ha="left", va="center", fontsize=11.5, color=BLACK)
    ax.set_yticks(tick_pos)
    ax.set_yticklabels([clean(l) for l in tick_lab], fontsize=12)
    ax.set_xlim(0, 470_000)
    ax.set_ylim(0.2, 4.3)
    hbar_axes(ax)
    if per_hour:
        fig_note(fig, ax, per_hour, fontsize=11.5)
    fig_title(fig, "MBB vs investment banking: total cash, year one and year three", "Base plus bonus, dollars a year, 2026")
    add_source(fig, SRC_BANKING)
    save(fig, "03-mbb-vs-investment-banking.png")
    add("03-mbb-vs-investment-banking.png",
        "Range bars of MBB and investment banking total cash in year one and year three, with per-hour pay",
        f"Banking pays {r1[3]} more than MBB in year one and {r3[3]} more in year three.",
        SRC_BANKING,
        "Chart from the MBB vs investment banking table in the draft (total cash ranges and the gap column, which is asserted "
        "to equal the difference of the ranges); the per-hour line is parsed from the hours paragraph and its arithmetic rechecked",
        "| Year three | $150,000 to $175,000 | $200,000 to $270,000 | $50,000 to $95,000 |"[:60])


# ---------------------------------------------------------------- 04: MBB vs tier 2 and Big 4
def chart_tier2(text):
    t = table(text, "Firm")
    assert t[0] == ["Firm", "Base", "Performance bonus cap", "Signing bonus"], t[0]
    rows = t[1:]
    assert len(rows) == 8 and rows[0][0] == "McKinsey, BCG, Bain", [r[0] for r in rows]

    def label_text(cell, width):
        s = cell.replace(" (plus ", ", plus ").rstrip(")")
        return clean(textwrap.fill(s, width))

    fig, axes = new_figure(width=11, height=6.4, ncols=2, sharey=True,
                           gridspec_kw={"width_ratios": [1, 1.12], "wspace": 0.1})
    ys = list(range(len(rows)))[::-1]
    panels = ((axes[0], 1, 205_000, "Base salary", 30), (axes[1], 2, 54_000, "Maximum performance bonus", 24))
    for ax, col, xmax, title, wrap_w in panels:
        for y, r in zip(ys, rows):
            lo, hi = bar_value(r[col])
            color = NAVY if r[0].startswith("McKinsey") else GRAY
            if hi > 0:
                ax.barh(y, hi, height=0.58, color=color, zorder=3)
            ax.text(hi + xmax * 0.012, y, label_text(r[col], wrap_w), ha="left", va="center", fontsize=10.5,
                    color=BLACK, linespacing=1.15)
        ax.set_xlim(0, xmax)
        hbar_axes(ax)
        ax.set_title(clean(title), loc="left", fontsize=13, pad=8, color=BLACK)
    axes[0].set_yticks(ys)
    axes[0].set_yticklabels([clean(r[0]) for r in rows], fontsize=12)
    axes[0].set_ylim(-0.6, len(rows) - 0.4)
    axes[1].tick_params(labelleft=False)
    fig_title(fig, "Undergraduate base and bonus cap by firm, 2026",
              "Dollars a year; McKinsey, BCG and Bain in navy, tier 2 and Big 4 strategy firms in gray")
    add_source(fig, SRC_MC)
    save(fig, "04-mbb-vs-tier-2-base-and-bonus.png")
    others = [bar_value(r[1]) for r in rows[1:]]
    o_lo, o_hi = min(v[0] for v in others), max(v[1] for v in others)
    add("04-mbb-vs-tier-2-base-and-bonus.png",
        "Two bar panels of 2026 undergraduate base salary and bonus cap at MBB and seven other strategy firms",
        f"Tier 2 and Big 4 strategy bases run {money(o_lo)} to {money(o_hi)} against {rows[0][1]} at MBB.",
        SRC_MC,
        "Chart from the tier 2 and Big 4 table in the draft (base and performance bonus cap columns; range cells drawn to "
        "their upper end and labeled with the range; profit-sharing notes kept in the labels)",
        "| McKinsey, BCG, Bain | $110,000 to $112,000 | $18,000 to $22,500 | $5,000 |"[:60])


# ---------------------------------------------------------------- 05: federal bracket table (built last, fresh read)
def table_federal(text):
    t = table(text, "Taxable income slice")
    assert t[0] == ["Taxable income slice", "Rate", "Dollars in slice", "Tax"], t[0]
    body = t[1:]
    assert len(body) == 5 and body[-1][0].startswith("Total federal income tax"), [r[0] for r in body]
    slices, total = body[:-1], body[-1]
    for s in slices:
        rate = float(s[1].rstrip("%")) / 100
        d, tax = first_dollars(s[2]), first_dollars(s[3])
        assert abs(round(d * rate) - tax) <= 1, f"bracket row {s[0]!r}: {d} x {rate} != {tax}"
    tot_d, tot_tax = first_dollars(total[2]), first_dollars(total[3])
    assert sum(first_dollars(s[2]) for s in slices) == tot_d, "bracket slices do not add to the taxable income total"
    assert sum(first_dollars(s[3]) for s in slices) == tot_tax, "bracket taxes do not add to the federal total"
    gross = first_dollars(row(table(text, "Line"), "Gross pay")[1])
    std = re.search(r"standard deduction for a single filer, \$([\d,]+)", text)
    if std:
        assert gross - int(std.group(1).replace(",", "")) == tot_d, "gross less the standard deduction is not the taxable total"
    rows = [[clean(c) for c in s] for s in slices] + [[clean(total[0]), "", total[2], total[3]]]
    bank_table(["Taxable income slice", "Rate", "Dollars in slice", "Tax"], rows, OUT / "05-federal-bracket-math.png",
               total_rows=(len(rows) - 1,), title=clean(f"Federal income tax on {money(tot_d)} of taxable income, 2026"),
               source=SRC_IRS)
    print("rendered 05-federal-bracket-math.png")
    add("05-federal-bracket-math.png",
        f"Table of 2026 federal tax brackets applied to {tot_d:,} dollars of taxable income, four slices and a total",
        f"The four slices add to {money(tot_tax)} of federal income tax on {money(gross)} of gross pay.",
        SRC_IRS,
        "Table graphic from the federal bracket table in the draft (slice, rate, dollars in slice, tax); each slice's tax "
        "is asserted to equal dollars times rate and the slices to add to the total row",
        "| $0 to $12,400 | 10% | $12,400 | $1,240 |"[:60])


# ---------------------------------------------------------------- 06: New York take-home waterfall (built last, fresh read)
def chart_take_home(text):
    t = table(text, "Line")
    assert t[0] == ["Line", "Amount"], t[0]
    get = lambda label: row(t, label)[1]  # noqa: E731
    base, bonus, gross = first_dollars(get("Base salary")), first_dollars(get("Performance bonus")), first_dollars(get("Gross pay"))
    fed, ss, med = first_dollars(get("Federal income tax")), first_dollars(get("Social Security")), first_dollars(get("Medicare"))
    nys, nyc = first_dollars(get("New York State tax")), first_dollars(get("New York City tax"))
    total, net = first_dollars(get("Total taxes")), first_dollars(get("Take-home pay"))
    share, monthly = get("Take-home as a share of gross"), first_dollars(get("Take-home per month"))
    assert base + bonus == gross, "base plus bonus is not the gross pay row"
    assert abs(fed + ss + med + nys + nyc - total) <= 1, "the five taxes do not add to the total taxes row"
    assert abs(gross - total - net) <= 1, "gross less total taxes is not the take-home row"
    assert abs(round(net / 12) - monthly) <= 1, "take-home per month is not take-home divided by 12"
    assert f"{net / gross * 100:.1f}%" == share, f"take-home share {share!r} is not take-home over gross"

    steps = [("Gross pay", gross, "total"), ("Federal\nincome tax", fed, "cut"), ("Social\nSecurity", ss, "cut"),
             ("Medicare", med, "cut"), ("New York\nState tax", nys, "cut"), ("New York\nCity tax", nyc, "cut"),
             ("Take-home\npay", net, "total")]
    fig, ax = new_figure(width=11, height=6.2)
    run, w = 0, 0.58
    for i, (lab, v, kind) in enumerate(steps):
        if kind == "total":
            bottom, height = 0, v
            run = v
        else:
            bottom, height = run - v, v
            run -= v
        ax.bar(i, height, bottom=bottom, width=w, color=NAVY if kind == "total" else GRAY, zorder=3)
        txt = money(v) if kind == "total" else f"({money(v)})"
        ax.annotate(txt, (i, bottom + height), xytext=(0, 4), textcoords="offset points", ha="center", va="bottom",
                    fontsize=12, color=BLACK, fontweight="bold" if kind == "total" else "normal")
        if i < len(steps) - 1:
            ax.plot([i + w / 2, i + 1 - w / 2], [run, run], color=CONNECTOR, lw=0.9, zorder=2)
    assert run == net
    ax.set_xticks(range(len(steps)))
    ax.set_xticklabels([clean(s[0]) for s in steps], fontsize=11.5)
    ax.set_ylim(0, gross * 1.2)
    ax.set_xlim(-0.6, len(steps) - 0.4)
    style_axes(ax)
    ax.text(0.99, 0.97, clean(f"Take-home per month: {money(monthly)}\nTake-home as a share of gross: {share}"),
            transform=ax.transAxes, ha="right", va="top", fontsize=12, color=BLACK, linespacing=1.5)
    fig_title(fig, "Gross pay to take-home, New York City, 2026",
              f"Single filer, {money(base)} base and {money(bonus)} bonus, 2026 tax rules, dollars a year")
    add_source(fig, SRC_TAX)
    save(fig, "06-new-york-take-home.png")
    add("06-new-york-take-home.png",
        f"Waterfall chart from {gross:,} dollars of gross pay through five taxes to {net:,} dollars of take-home in New York",
        f"Taxes take {money(total)} of the {money(gross)}, leaving {money(net)} a year, or {money(monthly)} a month.",
        SRC_TAX,
        "Waterfall from the gross-to-net table in the draft (gross pay, the five tax lines, take-home, take-home per month "
        "and share of gross); the taxes are asserted to add to the total and gross less taxes to equal take-home",
        "| Gross pay | $124,000 |"[:60])


# ---------------------------------------------------------------- manifest
def check_manifest(text):
    lines = [l.strip() for l in text.split("\n")]
    from PIL import Image
    for e in entries:
        for k in ("alt", "caption", "source", "method", "anchor"):
            assert not any(ch in e[k] for ch in BAD_CHARS), f"dash in manifest {e['file']} {k}"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
        assert len(e["caption"].split()) <= 20, f"caption of {e['file']} is over 20 words"
        assert e["source"].startswith("Source:"), f"source of {e['file']} must start with 'Source:'"
        hits = [l for l in lines if l.startswith(e["anchor"])]
        assert len(hits) == 1, f"anchor for {e['file']} matches {len(hits)} draft lines: {e['anchor']!r}"
        im = Image.open(OUT / e["file"])
        assert im.width <= 2200, f"{e['file']} is {im.width} px wide"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    text = DRAFT.read_text(encoding="utf-8")
    chart_first_year_cash(text)
    chart_ladder(text)
    chart_mbb_vs_banking(text)
    chart_tier2(text)
    # The tax images last, from a fresh read: a QA agent may be correcting the take-home figures.
    text = DRAFT.read_text(encoding="utf-8")
    table_federal(text)
    chart_take_home(text)
    entries.sort(key=lambda e: e["file"])
    check_manifest(text)
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
