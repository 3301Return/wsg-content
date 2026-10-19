#!/usr/bin/env python3
"""Images for drafts/draft-investment-banking-recruiting-timeline-2027-v1.md (October 11, 2026).

Run from the repo root:  python3 scripts/images/build_investment-banking-recruiting-timeline-2027.py
Idempotent: rewrites every PNG in published/assets/images/investment-banking-recruiting-timeline-2027/
and the folder's manifest.json. The draft is never edited; the coordinator inserts the image lines
from the manifest anchors with scripts/images/insert_images.py.

Every date and count comes from the draft. Before anything is drawn, the script reads the draft and
asserts each figure it uses is still there (the one-page cycle table, the fall 2026 program table,
the bulge bracket table, the Adventis counts, the Goldman January 1 chain, the private equity
on-cycle dates). A later edit to the draft fails the build loudly.

Banking format (images.md, October 7 and 8, 2026): black Arial text, no gridlines, no frames or
cell lines, direct labels, BANK_SERIES colors, a source line bottom-left. Dated images (01, 02, 03,
04, 05) carry "expected" items and must be regenerated at publish.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import *          # noqa: E402,F401,F403
from wsg_diagrams import canvas, finish, label, wrap, month_x, arrow  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.rcParams["text.parse_math"] = False
matplotlib.rcParams["axes.unicode_minus"] = False

SLUG = "investment-banking-recruiting-timeline-2027"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v1.md"
TEXT = DRAFT.read_text(encoding="utf-8")
LINES = TEXT.split("\n")
entries = []

EXPECTED = LIGHT_BLUE   # projected windows
POSTED = NAVY           # dates from a firm page or last cycle's record


def need(pattern, what):
    """Assert a figure is still in the draft (regex, dotall)."""
    assert re.search(pattern, TEXT, re.S), f"draft no longer says: {what}  [{pattern}]"


def table_row(first_cell):
    """The cells of the first markdown table row whose first cell is first_cell."""
    for line in LINES:
        if line.startswith(f"| {first_cell} |"):
            return [c.strip() for c in line.strip().strip("|").split("|")]
    raise AssertionError(f"no table row starting with {first_cell!r}")


def add(file, alt, caption, source, method, anchor):
    entries.append({"file": file, "alt": alt, "caption": caption, "source": source, "method": method, "anchor": anchor})


def assert_fits(fig, width_in, name):
    fig.canvas.draw()
    bb = fig.get_tightbbox(fig.canvas.get_renderer())
    assert bb.x0 >= -0.05 and bb.x1 <= width_in + 0.05, f"{name}: content spans {bb.x0:.2f} to {bb.x1:.2f} in on a {width_in} in canvas"


def source_line(ax, x, y, text, size=10):
    if not text.startswith("Source"):
        text = "Source: " + text
    ax.text(x, y, text, ha="left", va="top", fontsize=size, color=BLACK)


def text_table(header, rows, widths, out_path, title, source, size=11.5, row_pad=0.1, x0=0.35):
    """A table as a banking graphic with wrapped text cells: black text, bold header with a thin
    rule under it, no cell lines, no frame. widths are column widths in inches."""
    line_h = size * 1.25 / 72
    heights = []
    wrapped = []
    for row in rows:
        cells = [wrap(str(c), w - 0.12, size) for c, w in zip(row, widths)]
        wrapped.append(cells)
        heights.append(max(c.count("\n") + 1 for c in cells) * line_h + 2 * row_pad)
    head_h = line_h + 2 * row_pad
    W = max(11.0, x0 * 2 + sum(widths))
    H = 0.85 + head_h + sum(heights) + 0.55
    fig, ax = canvas(W, H)
    ax.text(x0, H - 0.35, title, ha="left", va="top", fontsize=16, fontweight="bold", color=BLACK)
    xs = []
    x = x0
    for w in widths:
        xs.append(x)
        x += w
    y = H - 0.85
    for xx, h in zip(xs, header):
        ax.text(xx + 0.04, y - head_h / 2, h, ha="left", va="center", fontsize=size, fontweight="bold", color=BLACK)
    y -= head_h
    ax.plot([x0, x0 + sum(widths)], [y, y], color=BLACK, lw=0.9)
    for cells, h in zip(wrapped, heights):
        for xx, c in zip(xs, cells):
            ax.text(xx + 0.04, y - h / 2, c, ha="left", va="center", fontsize=size, color=BLACK, linespacing=1.25)
        y -= h
    source_line(ax, x0, y - 0.3, source)
    assert_fits(fig, W, Path(out_path).name)
    finish(fig, out_path)


# ---------------------------------------------------------------- 01 the whole cycle
PERIODS = [  # (first cell of the cycle table row, start month index from Sep 2026, end month index inclusive, label, kind)
    ("September to November 2026", 0, 2, "Sophomore programs close; Evercore open September 8 or 9 to November 15", "posted"),
    ("November 2026 to January 2027", 2, 4, "Bulge brackets post, late November to January (expected)", "expected"),
    ("January to May 2027", 4, 8, "HireVue video interviews, first rounds, superdays; bulge bracket classes full by May", "posted"),
    ("June to September 2027", 9, 12, "Middle market postings stay open; second waves; London opens mid-August", "posted"),
    ("October 2027 to May 2028", 13, 20, "Junior year with an offer; internship prep", "posted"),
    ("June to August 2028", 21, 23, "Internship, nine to ten weeks; return offers in the final week", "posted"),
    ("August 2028 to January 2029", 23, 28, "Full-time postings September to October; private equity on-cycle in year one (expected)", "expected"),
]


def full_cycle_timeline():
    for first, *_ in PERIODS:
        table_row(first)
    need(r"The cycle runs about 22 months", "22 months")
    need(r"runs from September 8 or 9 \(the trackers differ by a day\) to November 15", "Evercore Sep 8 or 9 to Nov 15")
    need(r"classes essentially full by May", "classes full by May")
    need(r"London's Summer 2028 windows open in mid-August", "London mid-August")
    need(r"nine to ten weeks", "nine to ten weeks")
    need(r"Full-time postings for students without a return offer, September to October", "full-time Sep to Oct")

    W = 11
    label_w = 4.2
    row_h = 0.72
    n_rows = len(PERIODS)
    ya = 1.3
    H = 0.95 + n_rows * row_h + 0.2 + ya
    fig, ax = canvas(W, H, title="Investment banking recruiting for Summer 2028, by period")
    x0, x1 = label_w + 0.35, W - 0.35
    n_months = 29   # September 2026 to January 2029
    step = (x1 - x0) / n_months
    ax.plot([x0, x1], [ya, ya], color=BLACK, lw=0.9, zorder=2)
    ticks = {0: "Sep\n2026", 4: "Jan\n2027", 8: "May", 12: "Sep", 16: "Jan\n2028", 20: "May", 24: "Sep", 28: "Jan\n2029"}
    for i in range(n_months + 1):
        xa = x0 + i * step
        big = i in ticks
        ax.plot([xa, xa], [ya - (0.08 if big else 0.04), ya], color=BLACK, lw=0.9 if big else 0.6, zorder=2)
        if big:
            ax.text(xa, ya - 0.14, ticks[i], ha="center", va="top", fontsize=10.5, color=BLACK, linespacing=1.1)
    y = H - 0.95
    for first, s, e, text, kind in PERIODS:
        ym = y - row_h / 2
        label(ax, 0.35, y - 0.04, first, size=11, bold=True, ha="left", va="top", color=BLACK)
        label(ax, 0.35, y - 0.27, text, size=10, ha="left", va="top", color=BLACK, wrap_in=label_w - 0.1, linespacing=1.15)
        xa, xb = month_x(x0, step, s, 0.0), month_x(x0, step, e, 1.0)
        ax.plot([xa + 0.03, xb - 0.03], [ym, ym], color=POSTED if kind == "posted" else EXPECTED, lw=12,
                solid_capstyle="butt", zorder=3)
        y -= row_h
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], color=POSTED, lw=8, label="Dates from firm pages or last cycle"),
                       Line2D([0], [0], color=EXPECTED, lw=8, label="Expected, from tracker projections")],
              loc="lower left", bbox_to_anchor=(0.0, 0.42 / H), ncol=2, frameon=False, fontsize=10.5, labelcolor=BLACK)
    source_line(ax, 0.35, 0.4, "Firm pages and the Extern, Prospect Rock and Superday AI trackers, October 2026")
    assert_fits(fig, W, "01-full-cycle-timeline.png")
    finish(fig, OUT / "01-full-cycle-timeline.png")
    add("01-full-cycle-timeline.png",
        "Timeline from September 2026 to January 2029 with seven periods of the Summer 2028 investment banking recruiting cycle",
        "The cycle runs about 22 months, and the bulge bracket seats are decided between December 2026 and May 2027.",
        "Firm pages and the Extern, Prospect Rock and Superday AI trackers, October 2026",
        "Timeline drawn in matplotlib from the one-page cycle table in the draft; the bulge bracket and on-cycle windows are tracker projections and shown as expected",
        "**The cycle runs about 22 months from this fall to the retur")


# ---------------------------------------------------------------- 02 fall 2026 program deadlines
PROGRAMS = [  # (program as the draft's table names it, deadline shown, source shown, regex on the draft row)
    ("Jefferies IB Insight Day", "October 2, 2026", "Closed (Extern)", r"October 2, 2026"),
    ("Goldman Sachs Emerging Leaders Series", "Early October 2026", "Closed (firm page)", r"Closed in early October 2026"),
    ("Girls Who Invest 2027 Scholars", "October 15, 2026", "Program page", r"October 15, 2026"),
    ("William Blair Fast Track to Investment Banking", "October 18, 2026", "Extern", r"October 18, 2026"),
    ("Houlihan Lokey IB Insight Day", "October 19, 2026", "Extern", r"October 19, 2026"),
    ("Moelis Leadership Development Program", "October 22, 2026", "Extern", r"October 22, 2026"),
    ("Citi Early Identification", "October 23, 2026 (December cohort)", "Extern", r"October 23, 2026 for the December cohort"),
    ("Perella Weinberg US Advisory Prep Program", "October 25, 2026", "Extern", r"October 25, 2026"),
    ("Morgan Stanley Early Insights", "October 30, 2026", "Prospect Rock", r"October 30, 2026"),
    ("Lincoln International Sophomore Job Shadow", "October 30, 2026", "Extern", r"October 30, 2026"),
    ("Barclays Discovery Programme", "Not yet posted; last cycle November 7", "Expected", r"last cycle posted October 14 with a November 7 deadline"),
    ("Guggenheim Sophomore FOCUS", "Not yet posted; last cycle November 10", "Expected", r"last cycle's deadline was November 10"),
    ("JPMorganChase Fellowship", "November 2026 to mid-January 2027", "Expected", r"Expected to open in November 2026 and close in mid-January 2027"),
    ("MLT Career Prep", "December 1, 2026; final January 15, 2027", "Program page", r"General deadline December 1, 2026; final January 15, 2027"),
    ("Lazard Early Insights", "January 2027", "Expected", r"Expected January 2027"),
]


def program_deadlines_table():
    need(r"Seven sophomore programs close between October 18 and October 30, 2026", "seven programs Oct 18 to 30")
    need(r"as of October 11, 2026", "as of October 11, 2026")
    seven = [p for p in PROGRAMS if re.fullmatch(r"October (18|19|2\d|30), 2026.*", p[1])]
    assert len(seven) == 7, f"{len(seven)} programs close October 18 to 30, the draft says seven"
    for name, _, _, pat in PROGRAMS:
        row = table_row(name)
        assert re.search(pat, row[2]), f"{name}: draft deadline cell {row[2]!r} no longer matches {pat!r}"
    rows = [[p[0], p[1], p[2]] for p in PROGRAMS]
    text_table(["Program", "Deadline or window", "Status or source"], rows, [3.9, 3.3, 1.7],
               OUT / "02-fall-2026-program-deadlines.png",
               "Sophomore program deadlines, fall 2026, as of October 11, 2026",
               "Program pages and the Extern and Prospect Rock trackers, October 2026", size=11.5)
    add("02-fall-2026-program-deadlines.png",
        "Table of fifteen sophomore and insight programs with their fall 2026 deadlines and the source of each date",
        "Seven programs close between October 18 and October 30, 2026, and four more are expected in November and January.",
        "Program pages and the Extern and Prospect Rock trackers, October 2026",
        "Table graphic drawn in matplotlib from the fall 2026 program table in the draft; rows marked Expected are not yet posted",
        "**Seven sophomore programs close between October 18 and Octo")


# ---------------------------------------------------------------- 03 bulge bracket windows
BULGE = [  # (firm, opened as shown, closed as shown, expected as shown, regex on the draft's opened cell, regex on closed cell)
    ("Goldman Sachs", "Live by January 1, 2026 (reported)", "By spring 2026", "January 2027", r"live by January 1, 2026", r"By spring 2026"),
    ("JPMorgan", "December 2025 to March 2026, depending on the tracker", "By July 2026", "December 2026", r"December 2025 to March 2026", r"By July 2026"),
    ("Morgan Stanley", "January 1, 2026", "February 15, 2026", "January 2027", r"January 1, 2026", r"February 15, 2026"),
    ("Bank of America", "December 2025 to January 2026, rolling", "As filled", "January 2027", r"December 2025 to January 2026", r"As filled"),
    ("Citi", "December 2025 to January 2026", "January 2026", "December 2026", r"December 2025 to January 2026", r"January 2026"),
    ("Barclays", "December 2025 to January 2026", "January 2026", "Late November 2026", r"December 2025 to January 2026", r"January 2026"),
    ("UBS", "December 2025 to January 2026", "January 2026", "January 2027", r"December 2025 to January 2026", r"January 2026"),
    ("Deutsche Bank", "December 2025 to January 2026, plus a fall wave in August and September 2026", "January 2026; fall wave September", "Late November 2026",
     r"December 2025 to January 2026, plus a fall wave in August and September 2026", r"January 2026; fall wave in September"),
    ("Wells Fargo", "December 2025 to January 2026", "January 2026", "January 2027", r"December 2025 to January 2026", r"January 2026"),
    ("RBC", "Open by December 12, 2025", "January 30, 2026", "Not projected", r"Open by December 12, 2025", r"January 30, 2026"),
    ("Jefferies", "Late 2025 to early 2026", "Closed by fall 2026", "December 2026", r"Late 2025 to early 2026", r"Closed by fall 2026"),
]


def bulge_bracket_table():
    for firm, _, _, exp, pat_open, pat_close in BULGE:
        row = table_row(firm)
        assert len(row) == 4, row
        assert re.search(pat_open, row[1]), f"{firm} opened: {row[1]!r}"
        assert re.search(pat_close, row[2]), f"{firm} closed: {row[2]!r}"
        assert row[3] == exp, f"{firm} expected: {row[3]!r} vs {exp!r}"
    rows = [[f, o, c, e] for f, o, c, e, *_ in BULGE]
    text_table(["Firm", "Summer 2027 application opened", "Closed", "Summer 2028 (expected, Extern)"], rows, [1.7, 3.6, 2.0, 2.8],
               OUT / "03-summer-2027-bulge-bracket-windows.png",
               "Bulge bracket applications: Summer 2027 windows, Summer 2028 expected",
               "Prospect Rock, Extern, Superday AI, Vault, eFinancialCareers and Wall Street Oasis, October 2026", size=11.5)
    add("03-summer-2027-bulge-bracket-windows.png",
        "Table of eleven banks with their Summer 2027 application open and close dates and the expected Summer 2028 posting month",
        "Ten of the eleven banks opened in December 2025 or January 2026, and Extern expects the same months again.",
        "Prospect Rock, Extern, Superday AI, Vault, eFinancialCareers and Wall Street Oasis, October 2026",
        "Table graphic drawn in matplotlib from the bulge bracket table in the draft; the Summer 2028 column is Extern's projection and shown as expected",
        "The Summer 2027 columns come from Prospect Rock's Class of 2")


# ---------------------------------------------------------------- 04 Adventis counts
ACTUAL_2027 = {"Dec\n2025": 28, "Jan\n2026": 47}
FORECAST_2028 = {"Sep\n2026": 2, "Oct\n2026": 2, "Nov\n2026": 11, "Dec\n2026": 27, "Jan\n2027": 46}


def firms_posting_chart():
    need(r"For Summer 2027, 28 firms first posted in December 2025 and 47 in January 2026", "Adventis Summer 2027 actual")
    need(r"350 separate postings in January alone", "350 postings")
    need(r"is 2 firms in September 2026, 2 in October, 11 in November, 27 in December and 46 in January 2027", "Adventis Summer 2028 forecast")
    need(r"peaking at 349 in January 2027", "349 postings")
    months = ["Sep", "Oct", "Nov", "Dec", "Jan"]
    forecast = [2, 2, 11, 27, 46]
    actual = [None, None, None, 28, 47]
    assert forecast == list(FORECAST_2028.values()) and actual[3:] == list(ACTUAL_2027.values())
    fig, ax = new_figure(width=11, height=5.6)
    xs = list(range(5))
    w = 0.36
    a_bars = ax.bar([x - w / 2 for x in xs if actual[x] is not None], [v for v in actual if v is not None], width=w, color=GRAY, zorder=3,
                    label="Summer 2027, counted (December 2025 and January 2026)")
    f_bars = ax.bar([x + (w / 2 if actual[x] is not None else 0) for x in xs], forecast, width=w, color=NAVY, zorder=3, label="Summer 2028, Adventis forecast (September 2026 to January 2027)")
    bar_labels(ax, a_bars)
    bar_labels(ax, f_bars)
    style_axes(ax, title="Firms first posting Summer Analyst roles, by month")
    ax.set_xticks(xs)
    ax.set_xticklabels(months, fontsize=12)
    ax.set_ylim(0, 56)
    ax.set_xlim(-0.6, 4.6)
    ax.legend(loc="upper left", ncol=1, frameon=False, fontsize=11, labelcolor=BLACK)
    ax.text(0, 1.0, "Firms, counted in the month of their first posting", transform=ax.transAxes, ha="left", va="bottom", fontsize=11, color=BLACK)
    ax.set_title("Firms first posting Summer Analyst roles, by month", loc="left", pad=24, color=BLACK)
    add_source(fig, "Adventis, Class of 2029 recruiting hub, October 2026")
    finish(fig, OUT / "04-firms-posting-by-month.png")
    add("04-firms-posting-by-month.png",
        "Grouped bar chart of firms first posting Summer Analyst roles by month, Summer 2027 counted and Summer 2028 forecast",
        "Adventis forecasts 46 firms first posting in January 2027, against 47 in January 2026.",
        "Adventis, Class of 2029 recruiting hub, October 2026",
        "Grouped bars drawn in matplotlib from the Adventis counts in the draft (28 and 47 firms for Summer 2027; 2, 2, 11, 27 and 46 forecast for Summer 2028); the forecast is dated",
        "The volume numbers say the same thing. Adventis tracks a lit")


# ---------------------------------------------------------------- 05 Goldman chain
STEPS = [  # (date head, body)
    ("January 1, 2027", "Application submitted"),
    ("January 1 to 3", "HireVue invitation, hours to two days after applying"),
    ("By about January 10", "HireVue recorded; the invitation expires in about a week"),
    ("Late January to March", "Superday: three to five interviews of about 30 minutes"),
    ("March to April", "Offer (last cycle's timing, per Extern)"),
]


def goldman_sequence():
    need(r"January 1: submit\. January 1 to 3: HireVue invitation, since posters reported hours to two days\. "
         r"By about January 10: HireVue done, because the invitation expires in about a week\. "
         r"Late January to March: superday\. March to April: offer", "Goldman January 1 chain")
    need(r"Goldman's is three to five interviews of about 30 minutes each", "Goldman superday format")
    W, H = 11, 3.15
    fig, ax = canvas(W, H, title="One Goldman application on January 1, 2027: expected steps, from last cycle's gaps")
    n = len(STEPS)
    gap = 0.3
    bw = (W - 0.7 - gap * (n - 1)) / n
    bh = 1.55
    y = H - 0.85 - bh
    from matplotlib.patches import FancyBboxPatch
    for i, (head, body) in enumerate(STEPS):
        x = 0.35 + i * (bw + gap)
        fill = NAVY if i == 0 else LIGHT_BLUE
        ax.add_patch(FancyBboxPatch((x, y), bw, bh, boxstyle="round,pad=0,rounding_size=0.06", facecolor=fill, edgecolor=fill, zorder=2))
        tc = "white" if i == 0 else BLACK
        ax.text(x + bw / 2, y + bh - 0.22, head, ha="center", va="top", fontsize=12, fontweight="bold", color=tc, zorder=3)
        ax.text(x + bw / 2, y + bh / 2 - 0.2, wrap(body, bw - 0.25, 11), ha="center", va="center", fontsize=11, color=tc, linespacing=1.2, zorder=3)
        if i < n - 1:
            arrow(ax, (x + bw + 0.02, y + bh / 2), (x + bw + gap - 0.02, y + bh / 2), color=BLACK, lw=1.4, head=14)
    source_line(ax, 0.35, y - 0.3, "WSG, from last cycle's Goldman gaps reported by Wall Street Oasis posters and Extern, October 2026")
    assert_fits(fig, W, "05-goldman-application-to-offer.png")
    finish(fig, OUT / "05-goldman-application-to-offer.png")
    add("05-goldman-application-to-offer.png",
        "Five boxes from a January 1, 2027 Goldman application through HireVue and superday to a March or April offer",
        "A Goldman application on January 1 reaches the HireVue within days and an offer by March or April.",
        "WSG, from last cycle's Goldman gaps reported by Wall Street Oasis posters and Extern, October 2026",
        "Sequence diagram drawn in matplotlib from the Goldman January 1 chain in the draft; every step is a projection from last cycle and shown as expected",
        "Put the pieces together for one Goldman application on Janua")


# ---------------------------------------------------------------- 06 private equity on-cycle
EVENTS = [  # (date head, what happened, kind)
    ("June 4, 2025", "JPMorgan memo to incoming analysts: accept another job before joining or within 18 months, and your employment ends", "bank"),
    ("June 11, 2025", "Apollo: no interviews or offers this year for the class of 2027", "fund"),
    ("June 12, 2025", "General Atlantic: no interviews or offers this year for the class of 2027", "fund"),
    ("July 9, 2025", "Goldman banking juniors to certify every three months that they haven't accepted a job elsewhere (reported)", "bank"),
    ("January 5, 2026", "On-cycle restarts after a seven-month pause", "restart"),
    ("January 6, 2026", "Blackstone, Apollo, Carlyle, TPG, Silver Lake, General Atlantic, Hellman & Friedman and Warburg Pincus interviewing first-year analysts", "restart"),
]


def pe_oncycle_timeline():
    need(r"on June 4, 2025, JPMorgan's co-heads of global banking", "June 4 memo")
    need(r"within your first 18 months", "18 months")
    need(r"Apollo \(June 11\) and General Atlantic \(June 12\)", "June 11 and 12")
    need(r"on July 9, 2025, \[eFinancialCareers\]", "July 9")
    need(r"certify every three months", "every three months")
    need(r"restarted on Monday, January 5, 2026, after a seven-month pause", "January 5 restart")
    need(r"By January 6, Blackstone, Apollo, Carlyle, TPG, Silver Lake, General Atlantic, Hellman & Friedman and Warburg Pincus were interviewing", "January 6 firms")
    W = 11
    x_line, text_w, size = 2.6, 7.2, 11
    heights = []
    wrapped = []
    for _, body, _ in EVENTS:
        t = wrap(body, text_w, size)
        wrapped.append(t)
        heights.append(max(0.5, (t.count("\n") + 1) * size * 1.2 / 72) + 0.3)
    pause_h = 0.75   # the gap on the line between July 9 and January 5
    H = 0.95 + sum(heights) + pause_h + 0.75
    fig, ax = canvas(W, H, title="Private equity on-cycle recruiting, June 2025 to January 2026")
    colors = {"bank": MID_BLUE, "fund": MID_BLUE, "restart": NAVY}
    y = H - 1.05
    ys = []
    for i, ((head, body, kind), t, h) in enumerate(zip(EVENTS, wrapped, heights)):
        if i == 4:
            # the pause: a gray stretch of the line with its label
            ax.plot([x_line, x_line], [y, y - pause_h], color=GRAY, lw=5, solid_capstyle="butt", zorder=1)
            ax.text(x_line + 0.25, y - pause_h / 2, "Seven-month pause, no on-cycle interviews", ha="left", va="center", fontsize=size, color=BLACK, fontstyle="italic")
            y -= pause_h
        yc = y - 0.15
        ys.append(yc)
        ax.text(x_line - 0.25, yc, head, ha="right", va="top", fontsize=11.5, fontweight="bold", color=BLACK)
        ax.text(x_line + 0.25, yc, t, ha="left", va="top", fontsize=size, color=BLACK, linespacing=1.2)
        ax.plot([x_line], [yc - 0.09], marker="o", ms=10, color=colors[kind], markeredgecolor=SURFACE, markeredgewidth=1.5, zorder=4)
        y -= h
    ax.plot([x_line, x_line], [ys[0] - 0.09, ys[-1] - 0.09], color=BLACK, lw=1.0, zorder=0)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], marker="o", lw=0, ms=9, color=MID_BLUE, label="Banks and funds step back, summer 2025"),
                       Line2D([0], [0], marker="o", lw=0, ms=9, color=NAVY, label="On-cycle restarts, January 2026")],
              loc="lower left", bbox_to_anchor=(0.0, 0.42 / H), ncol=2, frameon=False, fontsize=10.5, labelcolor=BLACK)
    source_line(ax, 0.35, 0.4, "Fortune, Banking Dive and eFinancialCareers, citing Bloomberg and the Financial Times, June 2025 to January 2026")
    assert_fits(fig, W, "06-pe-on-cycle.png")
    finish(fig, OUT / "06-pe-on-cycle.png")
    add("06-pe-on-cycle.png",
        "Vertical timeline of six events from the June 2025 bank memos to the January 2026 on-cycle restart",
        "On-cycle recruiting paused after the June 2025 bank memos and restarted on January 5, 2026.",
        "Fortune, Banking Dive and eFinancialCareers, citing Bloomberg and the Financial Times, June 2025 to January 2026",
        "Timeline drawn in matplotlib from the private equity on-cycle paragraphs in the draft (June 4, 11, 12 and July 9, 2025; January 5 and 6, 2026)",
        "**Private equity on-cycle recruiting restarted on Monday, Ja")


# ---------------------------------------------------------------- manifest checks
def check_manifest():
    first_h2 = next(i for i, l in enumerate(LINES) if l.startswith("## "))
    for e in entries:
        for k in ("alt", "caption", "source", "method", "anchor"):
            for ch in (chr(0x2014), chr(0x2013), chr(0x2212)):
                assert ch not in e[k], f"dash in manifest {e['file']} {k}"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
        assert len(e["caption"].split()) < 20, f"caption of {e['file']} is {len(e['caption'].split())} words"
        assert len(e["anchor"]) <= 60
        hits = [i for i, l in enumerate(LINES) if l.strip().startswith(e["anchor"])]
        assert len(hits) == 1, f"anchor for {e['file']} matches {len(hits)} draft lines: {e['anchor']!r}"
        line = LINES[hits[0]]
        assert hits[0] > first_h2, f"anchor for {e['file']} is in the intro"
        assert not line.lstrip().startswith(("|", "-", ">", "* ")), f"anchor for {e['file']} is a table row, list item or quote"
    from PIL import Image
    for e in entries:
        im = Image.open(OUT / e["file"])
        assert im.width <= 2200, f"{e['file']} is {im.width} px wide"
    # no dashes in any string the build script draws
    src = Path(__file__).read_text(encoding="utf-8")
    for ch in (chr(0x2014), chr(0x2013), chr(0x2212)):
        assert ch not in src, "dash in the build script"


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    full_cycle_timeline()
    program_deadlines_table()
    bulge_bracket_table()
    firms_posting_chart()
    goldman_sequence()
    pe_oncycle_timeline()
    check_manifest()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT.relative_to(ROOT)}")
