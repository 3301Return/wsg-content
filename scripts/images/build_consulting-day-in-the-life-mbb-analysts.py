#!/usr/bin/env python3
"""Images for drafts/draft-consulting-day-in-the-life-mbb-analysts-v3.md (October 11, 2026; v3 October 12, 2026).

Run from the repo root:  python3 scripts/images/build_consulting-day-in-the-life-mbb-analysts.py
Idempotent. Steps:
  1. read the v3 draft and assert, with regexes, every number, time and name an image uses
     (the table in section 6, the Leland times in sections 2 to 5, the team sizes in section 1,
     the plant-cost example, the study rhythm in section 4); the build stops on the first mismatch
  2. draw five images in the banking format (black Arial text, no gridlines, no boxes or frames,
     direct labels, BANK_SERIES colors, a source line bottom-left) into
     published/assets/images/consulting-day-in-the-life-mbb-analysts/
  3. write that folder's manifest.json (file, alt, caption, source, method, anchor,
     regenerate_at_publish); the draft itself is never touched

Every string a reader sees went through the plain-language and humanizer passes in
.claude-skill/images.md before it was written here. Image 06 (McKinsey headcount and AI agents)
was cut in v3 with the headcount passage it illustrated; numbering keeps the gap.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import *          # noqa: E402,F401,F403
from wsg_diagrams import *     # noqa: E402,F401,F403

import matplotlib  # noqa: E402
matplotlib.rcParams["text.parse_math"] = False
matplotlib.rcParams["axes.unicode_minus"] = False
from matplotlib.patches import FancyBboxPatch, Patch  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402

SLUG = "consulting-day-in-the-life-mbb-analysts"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v3.md"
SRC_ARTICLE = "Source: WSG analysis of the figures in this article."
entries = []

# ---------------------------------------------------------------- 1. the draft's numbers, asserted
WEEK_SPLIT = [
    # label on the chart, percent, hours, the exact table row in the draft
    ("Data analysis and Excel modeling", 28, 18, "| Data analysis and Excel modeling | 28 percent | About 18 |"),
    ("Building pages", 22, 14, "| Building pages | 22 percent | About 14 |"),
    ("Client meetings and interviews", 15, 10, "| Client meetings and interviews | 15 percent | About 10 |"),
    ("Team check-ins and problem-solving sessions", 12, 8, "| Internal team syncs and problem-solving sessions | 12 percent | About 8 |"),
    ("Research and reading", 11, 7, "| Research and reading | 11 percent | About 7 |"),
    ("Travel, email and admin", 12, 8, "| Travel, email and admin | 12 percent | About 8 |"),
]

CHECKS = [
    # section 6 table
    *[(re.escape(row), f"week-split table row: {row}") for _, _, _, row in WEEK_SPLIT],
    (r"Hours in a 65-hour week", "the table's 65-hour column"),
    # Monday (section 2)
    (r"5:00 to 5:45", "Monday morning routine"), (r"5:45 to 6:45", "Monday transit and email"),
    (r"6:45 to 8:15", "Monday airport and flight"), (r"on site by about 1 p\.m\.", "Monday on site"),
    (r"check-in and dinner at 6 to 8 p\.m\.", "Monday dinner"), (r"evening work at 8 to 11:30 p\.m\.", "Monday evening work"),
    (r"lays out the week backward from Thursday", "Monday plan backward from Thursday"),
    # Tuesday and Wednesday (section 3)
    (r"7 a\.m\. wake-up, team breakfast", "Tuesday wake-up"), (r"check-in at 8:30", "Tuesday check-in"),
    (r"check-in is fifteen minutes", "check-in length"), (r"1 to 2 p\.m\. with the associate partner", "problem-solving session"),
    (r"dinner with the team from 5:30 to 9 p\.m\. and a work session from 9 to 11:30 p\.m\.", "Wednesday evening"),
    # Thursday (section 4)
    (r"Ten to twelve hours, part of it on a plane", "Thursday length"),
    (r"Thursday morning is the last pass on the deck", "Thursday morning"),
    (r"pre-wire is a short one-on-one meeting with one or two of the client executives", "pre-wire"),
    (r"the partner presents and the engagement manager handles the detail", "who presents"),
    # Friday (section 5)
    (r"8 to 9 a\.m\. start, work until noon, lunch, scheduling and networking from 1 to 4 p\.m\., wrap-up to 5:30, and out the door by 5:45", "Friday times"),
    # the team (section 1)
    (r"three to six people", "team size"), (r"two to four consultants and analysts", "consultant count"),
    (r"half a day to a day a week", "partner time"), (r"two to six months", "study length"),
    (r"one person owns procurement, another owns manufacturing, a third owns overhead", "workstreams"),
    (r"project leader at BCG, a manager at Bain", "manager titles"),
    # the pyramid example (section 3)
    (r"The Midwest plant costs 22 percent more per unit than the other three, and overtime explains most of the gap", "so-what"),
    (r"scrap rates doubled last year", "scrap"), (r"two or three reasons", "reason count"),
    (r"monthly cost by plant, split into labor, materials and overhead, January 2024 through June 2026", "data request"),
    # the study rhythm (sections 1, 3 and 4)
    (r"twelve-week study", "twelve-week study"), (r"every three or four weeks", "SteerCo rhythm"), (r"a final one at the end", "final SteerCo"),
    (r"weekly client steering committee", "weekly SteerCo on some studies"),
    (r"four or five empty titles, and your job for the next three weeks is to make them true or replace them", "ghost deck titles"),
    (r"back half of a study, it's common for the analyst to present", "back half"),
    (r"days before a SteerCo are the hardest days", "run-up"), (r"write down on day one what you think the answer is", "day-one hypothesis"),
    (r"steering committee in weeks four, eight and twelve", "SteerCo weeks on the timeline"),
    (r"Barbara Minto's book", "pyramid principle attribution"),
    (r"the title is the answer and the chart is the evidence", "pyramid on a page"),
]


def check_draft():
    text = DRAFT.read_text(encoding="utf-8")
    missing = [what for pat, what in CHECKS if not re.search(pat, text)]
    if missing:
        print("DRAFT DOES NOT CONTAIN WHAT THE IMAGES SHOW:")
        for m in missing:
            print("  " + m)
        sys.exit(1)
    print(f"draft checks: {len(CHECKS)} numbers, times and names found in {DRAFT.name}")
    return text


def add(file, alt, caption, source, method, anchor, dated=False):
    entries.append({"file": file, "alt": alt, "caption": caption, "source": source, "method": method,
                    "anchor": anchor[:60], "regenerate_at_publish": dated})


def assert_fits(fig, width_in, name):
    fig.canvas.draw()
    bb = fig.get_tightbbox(fig.canvas.get_renderer())
    assert bb.x0 >= -0.05 and bb.x1 <= width_in + 0.05, f"{name}: content spans {bb.x0:.2f} to {bb.x1:.2f} in on a {width_in} in canvas"


def canvas_source(ax, text, x=0.35, y=0.3):
    """Source line for a diagram canvas: flush with the canvas's 0.35 in left margin (add_source() reads
    the axes box, which on a canvas is the whole figure, so it would land at the paper's edge)."""
    ax.text(x, y, text, ha="left", va="bottom", fontsize=10, color=BLACK)


def left_title(fig, ax, title, subtitle=None, title_size=16, sub_size=11.5):
    """Title (and unit subtitle) flush with the left edge of everything the axes draws, tick labels included,
    so it lines up with add_source() below. Call after the chart is drawn, before add_source()."""
    fig.canvas.draw()
    bb = ax.get_tightbbox(fig.canvas.get_renderer())
    inv = fig.transFigure.inverted()
    fx0, _ = inv.transform((bb.x0, bb.y0))
    _, fy1 = inv.transform((bb.x1, bb.y1))
    y = fy1 + 0.035
    if subtitle:
        fig.text(fx0, y, subtitle, fontsize=sub_size, color=TEXT_SECONDARY, ha="left", va="bottom")
        y += 0.065
    fig.text(fx0, y, title, fontsize=title_size, fontweight="bold", color=BLACK, ha="left", va="bottom")


def plain_box(ax, x, y, w, h, fill, edge=None, lw=1.0, radius=0.06, z=3):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={radius}", facecolor=fill,
                                edgecolor=edge or fill, linewidth=lw, zorder=z))


# ---------------------------------------------------------------- 01. the case team
def team_diagram():
    W, H = 11, 7.0
    fig, ax = canvas(W, H, title="A case team on a cost study")
    label(ax, 0.35, H - 0.78, "Three to six people on one client question, usually for two to six months.",
          size=11.5, color=TEXT_SECONDARY, ha="left", va="top")

    def person(x, y, w, h, name, sub, fill, text_color=BLACK, sub_color=TEXT_SECONDARY, name_size=13, sub_size=10.5):
        plain_box(ax, x, y, w, h, fill)
        sub_t = wrap(sub, w - 0.3, sub_size)
        n2 = sub_t.count("\n") + 1
        sub_h = n2 * sub_size * 1.2 / 72
        block_h = name_size * 1.2 / 72 + 0.08 + sub_h
        top = y + h / 2 + block_h / 2
        label(ax, x + w / 2, top, name, size=name_size, bold=True, ha="center", va="top", color=text_color)
        label(ax, x + w / 2, top - name_size * 1.2 / 72 - 0.08, sub_t, size=sub_size, color=sub_color, ha="center", va="top", linespacing=1.2)

    # partner
    pw, ph = 4.2, 1.05
    px, py = (W - pw) / 2, 4.75
    person(px, py, pw, ph, "Partner", "Owns the client relationship. Checks the answer half a day to a day a week.", PALE_BLUE)
    # engagement manager
    ew, eh = 4.6, 1.15
    ex, ey = (W - ew) / 2, 3.1
    person(ex, ey, ew, eh, "Engagement Manager", "Runs the team every day: sets the plan, reviews every page. Called a project leader at BCG and a manager at Bain.", PALE_BLUE)
    arrow(ax, (W / 2, py), (W / 2, ey + eh), color=TEXT_SECONDARY, lw=1.6, head=14)
    # consultants
    cw, ch, gap = 3.1, 1.25, 0.5
    total = 3 * cw + 2 * gap
    cx0 = (W - total) / 2
    cy = 1.25
    people = [("Consultant", "Owns the procurement workstream", PALE_GRAY, BLACK, TEXT_SECONDARY),
              ("Consultant", "Owns the manufacturing workstream", PALE_GRAY, BLACK, TEXT_SECONDARY),
              ("Business Analyst (you)", "Owns the overhead workstream", NAVY, "white", "#dfe8f3")]
    bus_y = ey - 0.42
    ax.plot([W / 2, W / 2], [ey, bus_y], color=LINE, lw=1.6, zorder=1)
    ax.plot([cx0 + cw / 2, cx0 + 2 * (cw + gap) + cw / 2], [bus_y, bus_y], color=LINE, lw=1.6, zorder=1)
    for i, (name, sub, fill, tcol, scol) in enumerate(people):
        x = cx0 + i * (cw + gap)
        person(x, cy, cw, ch, name, sub, fill, text_color=tcol, sub_color=scol)
        ax.plot([x + cw / 2, x + cw / 2], [bus_y, cy + ch], color=LINE, lw=1.6, zorder=1)
    label(ax, W / 2, cy - 0.3, "Each workstream has its own interviews, its own data and its own pages in the final deck.",
          size=11, color=TEXT_SECONDARY, ha="center", va="top")
    canvas_source(ax, SRC_ARTICLE, y=0.35)
    assert_fits(fig, W, "01-case-team.png")
    finish(fig, OUT / "01-case-team.png")
    add("01-case-team.png",
        "Diagram of a consulting case team: a partner, an engagement manager and three consultants each owning one workstream",
        "The partner checks the answer weekly, the engagement manager runs the team daily, and each consultant owns one workstream.",
        SRC_ARTICLE,
        "Diagram drawn in matplotlib from the three-layer team description and the cost-study workstreams in section 1",
        "The engagement manager breaks the question into workstreams.")


# ---------------------------------------------------------------- 02. the client-site week
CAT = {
    "client": (NAVY, "white", "Client interviews and meetings"),
    "pages": (MID_BLUE, "white", "Excel and pages"),
    "team": (LIGHT_BLUE, BLACK, "Team sessions"),
    "other": (GRAY, BLACK, "Travel, meals, email"),
}
# (start hour, end hour, category, time label printed in bold or None, activity text or None)
WEEK = {
    "Monday": [
        (5.0, 5.75, "other", "5:00", "Morning routine"),
        (5.75, 6.75, "other", "5:45", "Transit and email"),
        (6.75, 8.25, "other", "6:45", "Airport and flight"),
        (8.25, 13.0, "other", None, "In the air, then the drive from the airport and lunch"),
        (13.0, 14.25, "team", "About 1:00", "Team room: plan the week backward from Thursday"),
        (14.25, 15.5, "client", None, "First interview with a client manager"),
        (15.5, 16.5, "pages", None, "Send the data request"),
        (16.5, 18.0, "team", None, "Call with an expert inside the firm"),
        (18.0, 20.0, "other", "6:00 to 8:00", "Hotel check-in and dinner"),
        (20.0, 23.5, "pages", "8:00 to 11:30", "Evening work with the team: first version of the pages"),
    ],
    "Tuesday": [
        (7.0, 8.5, "other", "7:00", "Wake up, team breakfast"),
        (8.5, 8.75, "team", None, None),
        (8.75, 13.0, "client", "8:30", "Team check-in (15 minutes), then client interviews"),
        (13.0, 14.0, "team", "1:00 to 2:00", "Problem-solving session"),
        (14.0, 17.5, "pages", None, "Excel: turn Monday's data into one chart per page"),
        (17.5, 19.5, "other", None, "Dinner"),
        (19.5, 23.5, "pages", None, "Pages"),
    ],
    "Wednesday": [
        (7.0, 8.5, "other", None, "Wake up, team breakfast"),
        (8.5, 8.75, "team", None, None),
        (8.75, 13.0, "client", None, "Team check-in, then interviews"),
        (13.0, 17.5, "pages", None, "Excel and pages for Thursday's meeting"),
        (17.5, 21.0, "other", "5:30 to 9:00", "Dinner with the team"),
        (21.0, 23.5, "pages", "9:00 to 11:30", "Work session on the deck"),
    ],
    "Thursday": [
        (8.0, 10.5, "pages", None, "Last pass on the deck: check every number, build backup pages"),
        (10.5, 12.0, "client", None, "Walk one or two client executives through the findings privately"),
        (13.0, 15.0, "client", None, "Client meeting: the partner presents, the analyst holds the backup pages"),
        (15.0, 15.75, "team", None, "Last team check-in"),
        (15.75, 19.5, "other", None, "Drive to the airport, fly home"),
    ],
    "Friday": [
        (8.0, 12.0, "pages", "8:00 or 9:00 to noon", "Wrap the study: clean up pages, send the client follow-ups, file expenses; training or recruiting"),
        (12.0, 13.0, "other", "12:00", "Lunch with other analysts"),
        (13.0, 16.0, "team", "1:00 to 4:00", "Scheduling and networking: tell the staffing manager what study you want next, coffee with a partner"),
        (16.0, 17.5, "other", "4:00 to 5:30", "Wrap-up"),
    ],
}
DAY_SUB = {"Monday": "Travel day", "Tuesday": "Client site", "Wednesday": "Client site",
           "Thursday": "Client meeting, fly home", "Friday": "Home office"}


def week_grid():
    W, H = 11, 11.6
    fig, ax = canvas(W, H, title="A client-site week, Monday to Friday")
    label(ax, 0.35, H - 0.78, "Times shown come from the Leland schedule; blocks without a time are approximate.",
          size=11.5, color=TEXT_SECONDARY, ha="left", va="top")
    y_top, y_bot = H - 1.75, 1.75
    h0, h1 = 5.0, 24.0
    per_hour = (y_top - y_bot) / (h1 - h0)
    yh = lambda h: y_top - (h - h0) * per_hour
    x_left, col_w, col_gap = 0.95, 1.92, 0.09
    size = 9.2
    # hour labels down the left, no lines
    for h in range(6, 24, 2):
        txt = {12: "noon"}.get(h, f"{h} a.m." if h < 12 else f"{h - 12} p.m.")
        label(ax, x_left - 0.12, yh(h), txt, size=9.5, color=TEXT_SECONDARY, ha="right", va="center")
        ax.plot([x_left - 0.08, x_left - 0.02], [yh(h), yh(h)], color=LINE, lw=1.0, zorder=1)
    label(ax, x_left - 0.12, yh(5), "5 a.m.", size=9.5, color=TEXT_SECONDARY, ha="right", va="center")
    problems = []
    for d, day in enumerate(WEEK):
        x = x_left + d * (col_w + col_gap)
        label(ax, x + col_w / 2, y_top + 0.42, day, size=12, bold=True, ha="center", va="bottom")
        label(ax, x + col_w / 2, y_top + 0.36, DAY_SUB[day], size=10, color=TEXT_SECONDARY, ha="center", va="top")
        for start, end, cat, when, what in WEEK[day]:
            fill, tcol, _ = CAT[cat]
            top, bot = yh(start), yh(end)
            assert not when or len(when) <= 24, f"{day} {start}: time label too long for the column: {when!r}"
            ax.add_patch(FancyBboxPatch((x, bot + 0.02), col_w, top - bot - 0.04, boxstyle="round,pad=0,rounding_size=0.04",
                                        facecolor=fill, edgecolor=fill, linewidth=0.8, zorder=3))
            if not what:
                continue
            lh = size * 1.18 / 72

            def layout(time_on_own_line):
                out = []
                if when and time_on_own_line:
                    out.append((when, True))
                    body = what
                elif when:
                    body = f"{when} {what}"
                else:
                    body = what
                for ln in wrap(body, col_w - 0.2, size).split("\n"):
                    out.append((ln, False))
                return out

            lines = layout(True)
            if len(lines) * lh + 0.08 > top - bot:
                lines = layout(False)       # the time goes inline when the block is too short for its own line
            need = len(lines) * lh + 0.08
            if need > top - bot:
                problems.append(f"{day} {start}-{end}: needs {need:.2f} in, has {top - bot:.2f} in: {what!r}")
            yy = (top + bot) / 2 + (len(lines) * lh) / 2 - lh / 2
            for ln, bold in lines:
                ax.text(x + col_w / 2, yy, ln, ha="center", va="center", fontsize=size, color=tcol,
                        fontweight="bold" if bold else "normal", zorder=4)
                yy -= lh
    # Thursday length note, Friday close
    tx = x_left + 3 * (col_w + col_gap)
    label(ax, tx + col_w / 2, yh(19.5) - 0.12, "10 to 12 hours, part of it on a plane", size=9.2, color=TEXT_SECONDARY,
          ha="center", va="top", italic=True, wrap_in=col_w)
    fx = x_left + 4 * (col_w + col_gap)
    label(ax, fx + col_w / 2, yh(17.5) - 0.12, "5:45 out the door", size=9.2, color=TEXT_SECONDARY, ha="center", va="top", italic=True)
    if problems:
        print("WEEK GRID TEXT DOES NOT FIT:")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    handles = [Patch(facecolor=CAT[k][0], edgecolor=CAT[k][0], label=CAT[k][2]) for k in ("client", "pages", "team", "other")]
    ax.legend(handles=handles, loc="lower left", bbox_to_anchor=(0.03, 1.3 / H), ncol=4, frameon=False, fontsize=10.5,
              handlelength=1.4, columnspacing=1.6)
    canvas_source(ax, "Source: Leland, a day in the life of a management consultant, February 2026, and WSG analysis.", y=0.9)
    assert_fits(fig, W, "02-client-site-week.png")
    finish(fig, OUT / "02-client-site-week.png")
    add("02-client-site-week.png",
        "Weekly calendar grid of a consultant's Monday to Friday showing travel, interviews, Excel work, team sessions and meetings",
        "Monday starts at 5 a.m. with a flight, the client-site evenings run to 11:30 p.m., and Friday ends by 5:45.",
        "Source: Leland, a day in the life of a management consultant, February 2026, and WSG analysis.",
        "Calendar drawn in matplotlib from the Leland times quoted in sections 2 to 5; blocks without a printed time are placed approximately",
        "On a travel study, Monday starts at 5 a.m. A former McKinsey")


# ---------------------------------------------------------------- 03. the pyramid principle
def pyramid():
    W, H = 11, 6.9
    fig, ax = canvas(W, H, title="Pyramid principle: the plant cost example")
    label(ax, 0.35, H - 0.78, "On a page, the title is the answer and the chart is the evidence.", size=11.5, color=TEXT_SECONDARY, ha="left", va="top")
    lx, cx0, cx1 = 0.35, 2.35, 10.7
    cw = cx1 - cx0

    def level(y, h, name, sub):
        label(ax, lx, y + h / 2 + 0.1, name, size=12.5, bold=True, ha="left", va="bottom")
        label(ax, lx, y + h / 2 + 0.02, sub, size=10, color=TEXT_SECONDARY, ha="left", va="top", wrap_in=1.8, linespacing=1.2)

    # answer
    ay, ah = 4.55, 1.0
    level(ay, ah, "Answer", "the page title")
    text_box(ax, cx0, ay, cw, ah, "The Midwest plant costs 22 percent more per unit than the other three, and overtime explains most of the gap.",
             fill=NAVY, text_color="white", size=12.5, bold=True, radius=0.06)
    # reasons
    ry, rh, rgap = 2.95, 0.85, 0.45
    rw = (cw - rgap) / 2
    level(ry, rh, "Reasons", "two or three, no overlap")
    reasons = ["Overtime hours per unit are higher at the Midwest plant", "Scrap rates doubled last year"]
    rxs = [cx0, cx0 + rw + rgap]
    for rx, txt in zip(rxs, reasons):
        text_box(ax, rx, ry, rw, rh, txt, fill=PALE_BLUE, size=11.5, bold=True, radius=0.06)
    # evidence
    ey, eh, egap = 1.25, 1.05, 0.25
    ew = (rw - egap) / 2
    level(ey, eh, "Evidence", "interviews and data")
    evidence = [["Monthly labor cost by plant, January 2024 to June 2026", "Interview: the plant manager on overtime"],
                ["Materials cost by plant over the same months", "Interview: the plant manager on scrap"]]
    for rx, pair in zip(rxs, evidence):
        exs = [rx, rx + ew + egap]
        for exx, txt in zip(exs, pair):
            text_box(ax, exx, ey, ew, eh, txt, fill=PALE_GRAY, size=10.5, radius=0.06)
        # reason -> its two evidence boxes
        mid = ry - 0.2
        ax.plot([rx + rw / 2, rx + rw / 2], [ry, mid], color=LINE, lw=1.6, zorder=1)
        ax.plot([exs[0] + ew / 2, exs[1] + ew / 2], [mid, mid], color=LINE, lw=1.6, zorder=1)
        for exx in exs:
            ax.plot([exx + ew / 2, exx + ew / 2], [mid, ey + eh], color=LINE, lw=1.6, zorder=1)
    # answer -> reasons
    mid = ay - 0.25
    ax.plot([cx0 + cw / 2, cx0 + cw / 2], [ay, mid], color=LINE, lw=1.6, zorder=1)
    ax.plot([rxs[0] + rw / 2, rxs[1] + rw / 2], [mid, mid], color=LINE, lw=1.6, zorder=1)
    for rx in rxs:
        ax.plot([rx + rw / 2, rx + rw / 2], [mid, ry + rh], color=LINE, lw=1.6, zorder=1)
    canvas_source(ax, SRC_ARTICLE, y=0.7)
    assert_fits(fig, W, "03-pyramid-principle.png")
    finish(fig, OUT / "03-pyramid-principle.png")
    add("03-pyramid-principle.png",
        "Three-level pyramid diagram with one answer on top, two reasons below it and four evidence boxes underneath",
        "The answer is the page title, the reasons sit under it, and the evidence sits under each reason.",
        SRC_ARTICLE,
        "Diagram drawn in matplotlib from the pyramid principle paragraph and its Midwest plant example in section 3",
        "The second is the pyramid principle, from Barbara Minto's book")


# ---------------------------------------------------------------- 04. a twelve-week study
def study_timeline():
    W, H = 11, 6.4
    fig, ax = canvas(W, H, title="A twelve-week study, week by week")
    label(ax, 0.35, H - 0.78, "An example study; the firms run them for two to six months.", size=11.5, color=TEXT_SECONDARY, ha="left", va="top")
    lx = 0.35
    x0, x1 = 2.55, 10.7
    n = 12
    step = (x1 - x0) / n
    wx = lambda w, frac=0.5: x0 + (w - 1 + frac) * step
    base_y = 2.45
    ax.plot([x0, x1], [base_y, base_y], color=TEXT_SECONDARY, lw=1.4, zorder=2)
    for w in range(1, n + 1):
        ax.plot([wx(w, 0), wx(w, 0)], [base_y - 0.06, base_y + 0.06], color=TEXT_SECONDARY, lw=1.0, zorder=2)
        label(ax, wx(w), base_y - 0.14, str(w), size=10.5, color=TEXT_SECONDARY, ha="center", va="top")
    ax.plot([x1, x1], [base_y - 0.06, base_y + 0.06], color=TEXT_SECONDARY, lw=1.0, zorder=2)
    label(ax, lx, base_y - 0.14, "Week", size=10.5, color=TEXT_SECONDARY, ha="left", va="top")
    # the work band
    by, bh = base_y + 0.2, 1.0
    label(ax, lx, by + bh / 2, "The work", size=12, bold=True, ha="left", va="center")
    text_box(ax, wx(1, 0), by, 3 * step - 0.05, bh, "Weeks 1 to 3: write the day-one hypothesis, build the ghost deck, make your four or five page titles true or replace them",
             fill=NAVY, text_color="white", size=9.8, radius=0.05, pad_in=0.1)
    text_box(ax, wx(4, 0) + 0.05, by, 9 * step - 0.05, bh, "Interviews and Excel by day, pages by night; the hypothesis changes as the facts come in",
             fill=PALE_BLUE, size=10.5, radius=0.05)
    # Thursday meetings
    ty = by + bh + 0.5
    label(ax, lx, ty, "Thursday client meeting", size=12, bold=True, ha="left", va="center", wrap_in=2.0, linespacing=1.15)
    for w in range(1, n + 1):
        ax.plot([wx(w, 4 / 7)], [ty], marker="o", ms=7, color=MID_BLUE, zorder=4)
    # steering committees
    sy = ty + 0.75
    label(ax, lx, sy, "Steering committee", size=12, bold=True, ha="left", va="center", wrap_in=2.0, linespacing=1.15)
    for w, txt in ((4, "Week 4"), (8, "Week 8"), (12, "Week 12, final")):
        xm = wx(w, 4 / 7)
        ax.plot([xm - 0.55, xm - 0.08], [sy, sy], color=GRAY, lw=7, solid_capstyle="butt", zorder=3)
        ax.plot([xm], [sy], marker="D", ms=10, color=NAVY, zorder=4)
        label(ax, xm, sy + 0.17, txt, size=10, ha="center", va="bottom")
    label(ax, x0, sy - 0.17, "Gray: the run-up days, the hardest of the study", size=9.5, color=TEXT_SECONDARY, ha="left", va="top", italic=True)
    label(ax, x1, sy - 0.17, "Every four weeks here, with a final one at the end; weekly on some studies", size=9.5, color=TEXT_SECONDARY, ha="right", va="top", italic=True)
    # back half bracket
    yb = base_y - 0.45
    ax.plot([wx(7, 0), wx(7, 0), wx(12, 1), wx(12, 1)], [yb + 0.12, yb, yb, yb + 0.12], color=TEXT_SECONDARY, lw=1.2, zorder=2)
    label(ax, wx(9, 1), yb - 0.08, "Back half: the analyst presents their own workstream pages", size=10, color=TEXT_SECONDARY, ha="center", va="top")
    canvas_source(ax, SRC_ARTICLE, y=1.15)
    assert_fits(fig, W, "04-twelve-week-study.png")
    finish(fig, OUT / "04-twelve-week-study.png")
    add("04-twelve-week-study.png",
        "Timeline of a twelve-week consulting study with weekly Thursday client meetings and steering committees in weeks four, eight and twelve",
        "Steering committees fall every three or four weeks, with a final one in week twelve.",
        SRC_ARTICLE,
        "Timeline drawn in matplotlib from the twelve-week study, the steering committee rhythm and the ghost deck paragraphs in sections 1, 3 and 4",
        "Every study runs on a rhythm of client meetings, and the bigg")


# ---------------------------------------------------------------- 05. how the week splits
def week_split_chart():
    fig, ax = new_figure(width=11, height=5.2)
    fig.subplots_adjust(left=0.33, right=0.99, top=0.97, bottom=0.03)
    labels = [r[0] for r in WEEK_SPLIT]
    pcts = [r[1] for r in WEEK_SPLIT]
    hours = [r[2] for r in WEEK_SPLIT]
    assert sum(pcts) == 100, "the week-split percentages must add to 100"
    ys = list(range(len(labels)))[::-1]
    bars = ax.barh(ys, pcts, height=0.6, color=NAVY, zorder=3)
    for y, p, h in zip(ys, pcts, hours):
        ax.text(p + 0.6, y, f"{p}% (about {h} hours)", ha="left", va="center", fontsize=12, color=BLACK)
    ax.set_yticks(ys)
    ax.set_yticklabels(labels, fontsize=12.5)
    ax.set_xlim(0, 40)
    ax.set_xticks([])
    for side in ("top", "right", "bottom"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_visible(True)
    ax.spines["left"].set_color(BLACK)
    ax.spines["left"].set_linewidth(0.8)
    ax.tick_params(length=0, colors=BLACK)
    left_title(fig, ax, "A junior consultant's 65-hour week by activity", "Percent of the week; hours in parentheses")
    add_source(fig, "Source: Hacking the Case Interview, day in the life of a McKinsey consultant, June 2026.")
    finish(fig, OUT / "05-week-split.png")
    add("05-week-split.png",
        "Horizontal bar chart splitting a junior consultant's week across six activities, in percent and hours",
        "Excel takes 28 percent of the week, pages 22 percent, and client meetings and interviews 15 percent.",
        "Source: Hacking the Case Interview, day in the life of a McKinsey consultant, June 2026.",
        "Chart from the section 6 table (six activities, percent of the week, hours in a 65-hour week)",
        "| Travel, email and admin | 12 percent | About 8 |")


# ---------------------------------------------------------------- manifest checks
def check_manifest(draft_text):
    lines = [l.strip() for l in draft_text.split("\n")]
    bad = ("\u2014", "\u2013", "\u2212")   # em dash, en dash, Unicode minus
    from PIL import Image
    for e in entries:
        for k in ("alt", "caption", "source", "method", "anchor"):
            assert not any(ch in e[k] for ch in bad), f"dash in manifest {e['file']} {k}"
        assert e["source"].startswith("Source:"), f"{e['file']} source line must start with 'Source:'"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
        assert len(e["caption"].split()) <= 20, f"caption of {e['file']} is over 20 words"
        hits = [l for l in lines if l.startswith(e["anchor"])]
        assert len(hits) == 1, f"anchor for {e['file']} matches {len(hits)} draft lines: {e['anchor']!r}"
        im = Image.open(OUT / e["file"])
        assert im.width <= 2200, f"{e['file']} is {im.width} px wide"
        assert im.info.get("dpi", (0, 0))[0] >= 199, f"{e['file']} lost its 200 dpi tag"
        assert not im.info.get("exif"), f"{e['file']} carries EXIF"


def finalize_pngs():
    """Re-save every PNG at 200 dpi with only the house author tag (finish() drops the dpi when it resizes)."""
    from PIL import Image
    from PIL.PngImagePlugin import PngInfo
    from PIL import ImageChops
    for png in sorted(OUT.glob("*.png")):
        im = Image.open(png).convert("RGB")
        # trim the white margin to a uniform 0.15 in (30 px) on every side; a diagram canvas otherwise keeps
        # its full height under the source line because the axes box counts toward the tight bounding box
        bbox = ImageChops.difference(im, Image.new("RGB", im.size, (255, 255, 255))).getbbox()
        if bbox:
            pad = 30
            im = im.crop((max(bbox[0] - pad, 0), max(bbox[1] - pad, 0), min(bbox[2] + pad, im.width), min(bbox[3] + pad, im.height)))
        meta = PngInfo()
        meta.add_text("Software", "Wall Street Guide")
        meta.add_text("Author", "Wall Street Guide")
        im.save(png, "PNG", optimize=True, dpi=(200, 200), pnginfo=meta)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    text = check_draft()
    team_diagram()
    week_grid()
    pyramid()
    study_timeline()
    week_split_chart()
    finalize_pngs()
    entries.sort(key=lambda e: e["file"])
    check_manifest(text)
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
