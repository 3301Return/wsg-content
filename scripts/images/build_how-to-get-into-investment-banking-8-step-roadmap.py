#!/usr/bin/env python3
"""Images for drafts/draft-how-to-get-into-investment-banking-8-step-roadmap-v1.md (October 11, 2026).

Run from the repo root:  python3 scripts/images/build_how-to-get-into-investment-banking-8-step-roadmap.py
Idempotent: rewrites every PNG in published/assets/images/how-to-get-into-investment-banking-8-step-roadmap/
and the folder's manifest.json. The draft is never edited; the coordinator inserts the image lines from
the manifest anchors with scripts/images/insert_images.py.

Every number comes from the draft text. Before anything is drawn, the script reads the draft and
asserts each figure it uses (regex on the draft), so a later edit to the draft fails the build loudly.
Banking format throughout (images.md, October 7, 2026): black Arial text, no gridlines, no boxes or
frames on charts, direct labels, BANK_SERIES colors, source in the bottom-left corner.

Image 03 is a dated table of program deadlines and carries "expected" rows; regenerate it at publish.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import *          # noqa: E402,F401,F403
from wsg_diagrams import canvas, finish, label, wrap, text_box, arrow  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.rcParams["text.parse_math"] = False      # "$700,000" must never be read as mathtext
matplotlib.rcParams["axes.unicode_minus"] = False   # no Unicode minus signs anywhere

SLUG = "how-to-get-into-investment-banking-8-step-roadmap"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v1.md"
TEXT = DRAFT.read_text(encoding="utf-8")
LINES = [l.strip() for l in TEXT.split("\n")]
entries = []
TODAY = "October 11, 2026"


def in_draft(pattern, what):
    """Assert a figure is in the draft text (regex, dotall)."""
    assert re.search(pattern, TEXT, flags=re.S), f"draft no longer says {what!r} (pattern {pattern!r})"


def anchor_for(start):
    """The first 60 characters, verbatim, of the one draft line that starts with `start`."""
    hits = [l for l in LINES if l.startswith(start)]
    assert len(hits) == 1, f"anchor start {start!r} matches {len(hits)} draft lines"
    return hits[0][:60]


def add(file, alt, caption, source, method, anchor):
    entries.append({"file": file, "alt": alt, "caption": caption, "source": source, "method": method, "anchor": anchor})


def assert_fits(fig, width_in, name):
    fig.canvas.draw()
    bb = fig.get_tightbbox(fig.canvas.get_renderer())
    assert bb.x0 >= -0.05 and bb.x1 <= width_in + 0.05, f"{name}: content spans {bb.x0:.2f} to {bb.x1:.2f} in on a {width_in} in canvas"


# ---------------------------------------------------------------- the draft's numbers, asserted
def check_draft():
    # 01 applications
    in_draft(r"about 2,600 interns from more than 360,000 applicants in 2025, a 0\.7 percent rate", "Goldman 2025")
    in_draft(r"stayed under 1 percent in 2026 with a class of about 2,500", "Goldman 2026")
    in_draft(r"about 240,000 applications for fewer than 2,000 internships in 2026, about 0\.8 percent", "Bank of America 2026")
    # 02 schools
    in_draft(r"nearly 10,500 entry-level Investment Banking Analysts at 16 banks", "College Transitions total")
    in_draft(r"NYU led with 386, Michigan had 296, Cornell 279, and Baruch.{0,60}placed 168 analysts, 11th", "school counts")
    # 03 deadlines
    in_draft(r"Houlihan Lokey.{0,80}Insight Day: apply by October 19, 2026", "Houlihan Lokey October 19")
    in_draft(r"Moelis Leadership Development Program\]\([^)]*\): October 22, 2026", "Moelis October 22")
    in_draft(r"Citi Early Identification.{0,200}closes October 23, 2026", "Citi October 23")
    in_draft(r"Morgan Stanley Early Insights.{0,120}registration closes October 30, 2026, with virtual sessions on November 2 and 5", "Morgan Stanley October 30")
    in_draft(r"JPMorganChase Fellowship Program.{0,400}November 11, 2025 to January 13, 2026, so expect it to open in November", "JPMorganChase window")
    in_draft(r"Barclays Discovery Programme.{0,160}posted October 14 with a November 7 deadline", "Barclays November 7")
    in_draft(r"Goldman Sachs Emerging Leaders Series.{0,200}closed October 4, 2026", "Goldman Emerging Leaders October 4")
    in_draft(r"Girls Who Invest.{0,300}final deadline for 2027 was October 15, 2026", "Girls Who Invest October 15")
    in_draft(r"MLT Career Prep.{0,200}final deadline January 15, 2027", "MLT January 15")
    in_draft(r"SEO Career.{0,200}typically closes in mid-April", "SEO mid-April")
    in_draft(r"Wall Street Bound.{0,120}apply by December 15 for the January 2027 cohort", "Wall Street Bound December 15")
    # 04 funnel
    in_draft(r"get a 10 to 25 percent reply rate\. About half of the people who reply will take a call\. So 100 emails produce 10 to 25 replies and 5 to 12 calls", "funnel numbers")
    # 05 postings by month
    in_draft(r"counted 28 firms posting their first Summer 2027 analyst application in December 2025 and 44 more in January 2026", "Adventis counts")
    in_draft(r"By May 2026, Prospect Rock reported bulge-bracket classes \"essentially full", "classes full by May")
    # 06 sequence
    in_draft(r"a resume screen, then the HireVue from step 6, then a first-round interview with one or two bankers, then the superday", "process order")
    in_draft(r"Goldman's version takes about 30 minutes, usually four to six questions", "HireVue length")
    in_draft(r"completion window across banks runs three to seven days", "HireVue window")
    in_draft(r"\"between two and five interviews for campus hires", "Goldman superday count")
    in_draft(r"four to six back-to-back sessions", "Prospect Rock superday count")
    in_draft(r"Offers follow the superday, often within days", "offer timing")
    in_draft(r"Apply on a Monday and you may be recording answers by Friday", "Monday to Friday")


# ---------------------------------------------------------------- 01 intern applications
def applications_chart():
    rows = [  # (bank and year, applications, apps label, interns, interns label, rate)
        ("Goldman Sachs, 2025", 360_000, "more than 360,000 applications", 2_600, "about 2,600 interns", "0.7 percent accepted"),
        ("Bank of America, 2026", 240_000, "about 240,000 applications", 2_000, "fewer than 2,000 internships", "about 0.8 percent accepted"),
    ]
    fig, ax = new_figure(width=11, height=5.2)
    h = 0.34
    ys = [2.0, 0.8]
    for y, (name, apps, apps_lbl, interns, int_lbl, rate) in zip(ys, rows):
        ax.barh(y + h / 2 + 0.03, apps, height=h, color=NAVY, zorder=3)
        ax.barh(y - h / 2 - 0.03, interns, height=h, color=GRAY, zorder=3)
        ax.annotate(apps_lbl, (apps, y + h / 2 + 0.03), xytext=(6, 0), textcoords="offset points", ha="left", va="center", fontsize=12, color=BLACK)
        ax.annotate(f"{int_lbl}: {rate}", (interns, y - h / 2 - 0.03), xytext=(6, 0), textcoords="offset points", ha="left", va="center",
                    fontsize=12, color=BLACK)
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=12.5)
    ax.set_xlim(0, 500_000)
    ax.set_ylim(0.2, 2.7)
    ax.set_xticks([])
    style_axes(ax, title="Intern applications and intern class size, Goldman Sachs and Bank of America")
    ax.set_yticks(ys)
    ax.set_yticklabels([r[0] for r in rows], fontsize=12.5)
    ax.spines["bottom"].set_visible(False)
    ax.text(0, 1.0, "Goldman Sachs 2026: applications not disclosed, class of about 2,500, under 1 percent accepted",
            transform=ax.transAxes, ha="left", va="bottom", fontsize=11, color=BLACK)
    ax.set_title("Intern applications and intern class size, Goldman Sachs and Bank of America", loc="left", pad=30, color=BLACK)
    add_source(fig, "Source: Fortune, Goldman Sachs intern class, June 2025 and June 2026; Business Insider, Bank of America internships, 2026")
    finish(fig, OUT / "01-goldman-intern-applications.png")
    add("01-goldman-intern-applications.png",
        "Bar chart of intern applications against intern class size at Goldman Sachs in 2025 and Bank of America in 2026",
        "Goldman Sachs accepted 0.7 percent of intern applicants in 2025 and Bank of America about 0.8 percent in 2026.",
        "Fortune, Goldman Sachs intern class, June 2025 and June 2026; Business Insider, Bank of America internships, 2026",
        "Bar chart drawn in matplotlib from the figures in the 'How hard is it' section of the draft (360,000 and 2,600; 240,000 and 2,000; 2026 class of 2,500), tagged [VERIFY] there",
        anchor_for("Very hard by the numbers"))


# ---------------------------------------------------------------- 02 feeder schools
def schools_chart():
    schools = [("NYU", 386), ("Michigan", 296), ("Cornell", 279), ("Baruch (11th of 16 banks' feeders)", 168)]
    fig, ax = new_figure(width=11, height=4.6)
    ys = list(range(len(schools)))[::-1]
    colors = [GRAY, GRAY, GRAY, NAVY]
    bars = ax.barh(ys, [s[1] for s in schools], height=0.56, color=colors, zorder=3)
    for y, (name, v) in zip(ys, schools):
        ax.annotate(f"{v:,}", (v, y), xytext=(6, 0), textcoords="offset points", ha="left", va="center", fontsize=12.5, color=BLACK)
    ax.set_yticks(ys)
    ax.set_yticklabels(["NYU (1st)", "Michigan (2nd)", "Cornell (3rd)", "Baruch (11th)"], fontsize=12.5)
    ax.set_xlim(0, 460)
    ax.set_xticks([])
    style_axes(ax, title="Entry-level Investment Banking Analysts on LinkedIn, by school")
    ax.set_yticks(ys)
    ax.set_yticklabels(["NYU (1st)", "Michigan (2nd)", "Cornell (3rd)", "Baruch (11th)"], fontsize=12.5)
    ax.spines["bottom"].set_visible(False)
    ax.text(0, 1.0, "Count of nearly 10,500 analysts at 16 banks", transform=ax.transAxes, ha="left", va="bottom", fontsize=11, color=BLACK)
    ax.set_title("Entry-level Investment Banking Analysts on LinkedIn, by school", loc="left", pad=30, color=BLACK)
    add_source(fig, "Source: College Transitions, top feeder schools for banking, April 2025")
    finish(fig, OUT / "02-top-feeder-schools.png")
    add("02-top-feeder-schools.png",
        "Horizontal bar chart of entry-level Investment Banking Analysts by school: NYU 386, Michigan 296, Cornell 279, Baruch 168",
        "NYU leads with 386 analysts, and Baruch, a public college, places 168, 11th on the list.",
        "College Transitions, top feeder schools for banking, April 2025",
        "Horizontal bars drawn in matplotlib from the four school counts the draft gives in the target-school section (386, 296, 279, 168 and the 10,500 total)",
        anchor_for("No. Goldman's 2024 intern class came from"))


# ---------------------------------------------------------------- 03 fall 2026 program deadlines (dated)
DEADLINES = [  # (program, who it is for, deadline, status)
    ("Goldman Sachs Emerging Leaders Series", "Sophomores", "October 4, 2026", "Closed"),
    ("Girls Who Invest", "First-years and sophomores", "October 15, 2026", "Closed"),
    ("Houlihan Lokey Insight Day", "Sophomores", "October 19, 2026", "Open"),
    ("Moelis Leadership Development Program", "Sophomores", "October 22, 2026", "Open"),
    ("Citi Early Identification", "Sophomores", "October 23, 2026", "Open"),
    ("Morgan Stanley Early Insights", "Sophomores", "October 30, 2026", "Open"),
    ("Barclays Discovery Programme", "Two years from graduation", "November 7 (expected)", "Last cycle: posted October 14"),
    ("JPMorganChase Fellowship Program", "Sophomores", "Opens in November (expected)", "Last cycle: November 11 to January 13"),
    ("Wall Street Bound", "Underrepresented students", "December 15, 2026", "Open"),
    ("MLT Career Prep", "Sophomores", "January 15, 2027", "Open"),
    ("SEO Career", "First-years through juniors", "Mid-April (rolling)", "Open"),
]


def deadlines_table():
    header = ["Program", "Who can apply", "Deadline", "Status"]
    widths = [3.5, 2.3, 2.7, 3.0]
    col_align = ["left", "left", "left", "left"]
    size = 12
    row_h, head_h = 0.44, 0.5
    W = 0.35 * 2 + sum(widths)
    H = 0.95 + head_h + row_h * len(DEADLINES) + 0.95
    fig, ax = canvas(W, H, title=f"Sophomore program deadlines, fall 2026 (as of {TODAY})")
    xs, x = [], 0.35
    for w in widths:
        xs.append(x)
        x += w
    y = H - 0.95
    for i, h in enumerate(header):
        ax.text(xs[i], y - head_h / 2, h, ha="left", va="center", fontsize=size, fontweight="bold", color=BLACK)
    y -= head_h
    ax.plot([0.35, W - 0.35], [y, y], color=BLACK, lw=0.9)
    for row in DEADLINES:
        for i, cell in enumerate(row):
            ax.text(xs[i], y - row_h / 2, cell, ha="left", va="center", fontsize=size, color=BLACK)
        y -= row_h
    label(ax, 0.35, y - 0.12, f"Dates as posted on each firm's page or on Extern and Prospect Rock as of {TODAY}; rows marked expected are projected from last cycle.",
          size=10, color=BLACK, ha="left", va="top", wrap_in=W - 0.7)
    label(ax, 0.35, 0.3, "Source: Firm careers pages, Extern and Prospect Rock, October 2026", size=10, color=BLACK, ha="left", va="bottom")
    assert_fits(fig, W, "03-fall-2026-program-deadlines.png")
    finish(fig, OUT / "03-fall-2026-program-deadlines.png")
    add("03-fall-2026-program-deadlines.png",
        "Table of eleven freshman and sophomore banking program deadlines for fall 2026, with who can apply and status",
        "Four sophomore programs close between October 19 and October 30, 2026, and two expected windows follow in November.",
        "Firm careers pages, Extern and Prospect Rock, October 2026",
        "Table graphic drawn in matplotlib from the program list in step 3 of the draft (every date tagged [VERIFY] there); Barclays and JPMorganChase are shown as expected",
        anchor_for("The banks run short programs"))


# ---------------------------------------------------------------- 04 networking funnel
def funnel_chart():
    stages = [  # (label, left width share, right note)
        ("100 emails sent", 1.0, "to analysts and associates"),
        ("10 to 25 replies", 0.25, "10 to 25 percent reply rate"),
        ("5 to 12 calls", 0.12, "about half of the people who reply"),
    ]
    W, H = 11, 5.4
    fig, ax = canvas(W, H, title="Networking emails to replies to calls, per 100 emails")
    full_w, x_left, y = 5.2, 0.5, H - 1.15
    bar_h, gap = 0.9, 0.3
    colors = [NAVY, MID_BLUE, LIGHT_BLUE]
    for (txt, share, note), col in zip(stages, colors):
        w = full_w * share
        ax.add_patch(matplotlib.patches.Rectangle((x_left, y - bar_h), w, bar_h, facecolor=col, edgecolor=col, zorder=3))
        ax.text(x_left + w + 0.15, y - bar_h / 2 + 0.14, txt, ha="left", va="center", fontsize=14, fontweight="bold", color=BLACK)
        ax.text(x_left + w + 0.15, y - bar_h / 2 - 0.16, note, ha="left", va="center", fontsize=11.5, color=BLACK)
        y -= bar_h + gap
    label(ax, 0.35, 0.3, "Source: Mergers & Inquisitions, investment banking networking guide", size=10, color=BLACK, ha="left", va="bottom")
    assert_fits(fig, W, "04-networking-funnel.png")
    finish(fig, OUT / "04-networking-funnel.png")
    add("04-networking-funnel.png",
        "Funnel diagram showing 100 networking emails leading to 10 to 25 replies and 5 to 12 calls",
        "Every 100 emails to the right bankers produce 10 to 25 replies and 5 to 12 calls.",
        "Mergers & Inquisitions, investment banking networking guide",
        "Funnel drawn in matplotlib from the reply rate (10 to 25 percent) and call rate (about half of repliers) in step 4 of the draft",
        anchor_for("**Mergers & Inquisitions puts the reply rate"))


# ---------------------------------------------------------------- 05 firms posting by month
def postings_chart():
    months = [("December 2025", 28), ("January 2026", 44)]
    fig, ax = new_figure(width=11, height=5.2)
    xs = [0, 1]
    bars = ax.bar(xs, [m[1] for m in months], width=0.5, color=[MID_BLUE, NAVY], zorder=3)
    bar_labels(ax, bars, fmt="{:,.0f} firms", fontsize=13)
    ax.set_xticks(xs)
    ax.set_xticklabels([m[0] for m in months], fontsize=12.5)
    ax.set_xlim(-0.6, 1.6)
    ax.set_ylim(0, 56)
    style_axes(ax, title="Firms posting their first Summer 2027 analyst application, by month")
    ax.text(1.0, 1.0, "By May 2026, bulge-bracket classes were essentially full (Prospect Rock)", transform=ax.transAxes,
            ha="right", va="bottom", fontsize=11, color=BLACK)
    ax.set_title("Firms posting their first Summer 2027 analyst application, by month", loc="left", pad=30, color=BLACK)
    add_source(fig, "Source: Adventis, Class of 2028 recruiting timeline, updated September 1, 2026")
    finish(fig, OUT / "05-firms-posting-by-month.png")
    add("05-firms-posting-by-month.png",
        "Bar chart of firms posting their first Summer 2027 analyst application: 28 in December 2025, 44 in January 2026",
        "Adventis counted 28 firms posting in December 2025 and 44 more in January 2026.",
        "Adventis, Class of 2028 recruiting timeline, updated September 1, 2026",
        "Bar chart drawn in matplotlib from the two Adventis counts in step 7 of the draft (28 and 44), tagged [VERIFY] there",
        anchor_for("Here's what that looked like last cycle"))


# ---------------------------------------------------------------- 06 application to offer
def process_sequence():
    steps = [  # (box text, note under the box)
        ("Application", "Submitted the day the portal opens"),
        ("Resume screen", ""),
        ("HireVue", "Recorded video, about 30 minutes, four to six questions; three to seven days to complete"),
        ("First round", "One or two bankers"),
        ("Superday", "Two to five interviews at Goldman Sachs; four to six at a typical bank"),
        ("Offer", "Often within days of the superday"),
    ]
    W, H = 11, 4.0
    fig, ax = canvas(W, H, title="From application to offer at a bulge bracket")
    n = len(steps)
    box_w, box_h, gap = 1.45, 0.62, 0.3
    total = n * box_w + (n - 1) * gap
    x = (W - total) / 2
    y_box = H - 2.0
    for i, (txt, note) in enumerate(steps):
        text_box(ax, x, y_box, box_w, box_h, txt, fill=LIGHT_BLUE, text_color=BLACK, size=12.5, bold=True, radius=0.05)
        if note:
            label(ax, x + box_w / 2, y_box - 0.12, note, size=10, color=BLACK, ha="center", va="top", wrap_in=box_w + 0.2, linespacing=1.2)
        if i < n - 1:
            arrow(ax, (x + box_w + 0.03, y_box + box_h / 2), (x + box_w + gap - 0.03, y_box + box_h / 2), color=BLACK, lw=1.4, head=14)
        x += box_w + gap
    # the gap the draft names: application on a Monday, HireVue answers by Friday
    xa = (W - total) / 2 + box_w / 2
    xh = (W - total) / 2 + 2 * (box_w + gap) + box_w / 2
    yb = y_box + box_h + 0.22
    ax.plot([xa, xa, xh, xh], [yb - 0.08, yb, yb, yb - 0.08], color=BLACK, lw=1.0, zorder=2)
    label(ax, (xa + xh) / 2, yb + 0.05, "Apply on a Monday, record HireVue answers by Friday", size=10.5, color=BLACK, ha="center", va="bottom")
    label(ax, 0.35, 0.2, "Source: Goldman Sachs students page; Leland, June 2026; Prospect Rock, July 2026", size=10, color=BLACK, ha="left", va="bottom")
    assert_fits(fig, W, "06-application-to-offer.png")
    finish(fig, OUT / "06-application-to-offer.png")
    add("06-application-to-offer.png",
        "Sequence diagram of six steps from application through resume screen, HireVue, first round and superday to offer",
        "The HireVue arrives with a three to seven day window, and offers often follow the superday within days.",
        "Goldman Sachs students page; Leland, June 2026; Prospect Rock, July 2026",
        "Sequence drawn in matplotlib from the process paragraph in step 7 and the HireVue paragraph in step 6 of the draft (figures tagged [VERIFY] there)",
        anchor_for("What happens after you submit"))


# ---------------------------------------------------------------- manifest checks
def check_manifest():
    bad = tuple(chr(c) for c in (0x2014, 0x2013, 0x2212))
    for e in entries:
        for k in ("alt", "caption", "source", "method", "anchor"):
            assert not any(ch in e[k] for ch in bad), f"dash in manifest {e['file']} {k}"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
        assert len(e["caption"].split()) <= 20, f"caption of {e['file']} is over 20 words"
        hits = [l for l in LINES if l.startswith(e["anchor"])]
        assert len(hits) == 1, f"anchor for {e['file']} matches {len(hits)} draft lines: {e['anchor']!r}"
        idx = LINES.index(hits[0])
        first_h2 = next(i for i, l in enumerate(LINES) if l.startswith("## "))
        assert idx > first_h2, f"anchor for {e['file']} is in the intro"
        assert not hits[0].startswith(("|", "- ", ">")), f"anchor for {e['file']} is a table row, list item or quote"
    # no dashes in any string drawn on the images
    src = Path(__file__).read_text(encoding="utf-8")
    assert not any(ch in src for ch in bad), "dash character in the build script"
    from PIL import Image
    for e in entries:
        im = Image.open(OUT / e["file"])
        assert im.width <= 2200, f"{e['file']} is {im.width} px wide"


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    check_draft()
    print("draft checks: every figure used in the six images is still in the draft text")
    applications_chart()
    schools_chart()
    deadlines_table()
    funnel_chart()
    postings_chart()
    process_sequence()
    check_manifest()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT.relative_to(ROOT)}")
