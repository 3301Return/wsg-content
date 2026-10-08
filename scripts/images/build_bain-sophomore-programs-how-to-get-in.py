#!/usr/bin/env python3
"""Images for drafts/draft-bain-sophomore-programs-how-to-get-in-v1.md (October 5, 2026).

Run from the repo root:  python3 scripts/images/build_bain-sophomore-programs-how-to-get-in.py
Idempotent: rewrites every PNG in published/assets/images/bain-sophomore-programs-how-to-get-in/
and the folder's manifest.json. The draft is never edited; the coordinator inserts the image
lines from the manifest anchors with scripts/images/insert_images.py.

Every date, office count and program detail comes from the draft itself (the four program
sections, the Class of 2029 timeline table and the "weeks between" plan). Windows the draft
tags [VERIFY] or calls "expected" are drawn as expected, so images 01 and 03 are dated and
must be regenerated at publish.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import *          # noqa: E402,F401,F403
from wsg_diagrams import *     # noqa: E402,F401,F403

SLUG = "bain-sophomore-programs-how-to-get-in"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v1.md"
entries = []


def assert_fits(fig, width_in, name):
    """The tight bounding box must stay inside the canvas, or finish() shrinks the whole picture to fit."""
    fig.canvas.draw()
    bb = fig.get_tightbbox(fig.canvas.get_renderer())
    assert bb.x0 >= -0.05 and bb.x1 <= width_in + 0.05, f"{name}: content spans {bb.x0:.2f} to {bb.x1:.2f} in on a {width_in} in canvas"


def add(file, alt, caption, method, anchor):
    entries.append({"file": file, "alt": alt, "caption": caption, "method": method, "anchor": anchor})


# ---------------------------------------------------------------- helpers
def quarter_axis(ax, y, x0, x1, n_months, labels, size=11):
    """A month axis with a tick every month and a label on the months given in labels {index: text}."""
    step = (x1 - x0) / n_months
    ax.plot([x0, x1], [y, y], color=TEXT_SECONDARY, lw=1.4, zorder=2)
    for i in range(n_months + 1):
        xa = x0 + i * step
        big = i in labels
        ax.plot([xa, xa], [y - (0.09 if big else 0.05), y + (0.09 if big else 0.05)], color=TEXT_SECONDARY,
                lw=1.2 if big else 0.8, zorder=2)
        if big:
            ax.text(xa, y - 0.17, labels[i], ha="center", va="top", fontsize=size, color=TEXT_SECONDARY)
    return step


def diamond(ax, x, y, color=BLUE, ms=11):
    ax.plot([x], [y], marker="D", ms=ms, color=color, zorder=4)


def bar(ax, x_start, x_end, y, color=ORANGE, lw=9):
    ax.plot([x_start, x_end], [y, y], color=color, lw=lw, solid_capstyle="round", alpha=0.85, zorder=3)


# ---------------------------------------------------------------- 01 Class of 2029 timeline
def class_of_2029_timeline():
    W, H = 11, 8.3
    fig, ax = canvas(W, H, title="A sophomore's Bain year: one November deadline, a winter weekend, then the ACI")
    x0, x1, ya = 0.5, W - 0.4, 1.35
    n = 24   # October 2026 to September 2028
    labels = {0: "Oct\n2026", 3: "Jan\n2027", 6: "Apr", 9: "Jul", 12: "Oct", 15: "Jan\n2028", 18: "Apr", 21: "Jul", 24: "Oct\n2028"}
    step = quarter_axis(ax, ya, x0, x1, n, labels)

    def mx(mi, frac=0.5):
        return month_x(x0, step, mi, frac)

    # today marker (the draft's "status on October 5, 2026" column)
    tx = mx(0, 5 / 31)
    ax.plot([tx, tx], [ya, H - 0.95], color=LINE, lw=1.2, zorder=1)
    label(ax, tx + 0.1, H - 1.0, "Today, October 5, 2026", size=10.5, color=TEXT_MUTED, ha="left", va="center", italic=True)

    lanes_y = [H - 1.45, H - 2.0, H - 2.55, H - 3.1, H - 3.65, H - 4.2, H - 4.9, H - 5.6, H - 6.35]
    # 1 Kickstart (posted, closed today)
    diamond(ax, mx(0, 5 / 31), lanes_y[0])
    label(ax, mx(0, 5 / 31) + 0.2, lanes_y[0], "Consulting Kickstart (virtual, three October sessions): registration closed October 5, 2026",
          size=11, ha="left", va="center")
    # 2 the one application
    bar(ax, mx(0, 0.5), mx(1, 30 / 30), lanes_y[1], color=BLUE)
    label(ax, mx(1, 1.0) + 0.2, lanes_y[1], "One application for BEL, CREW and First Forward: opens mid-October, closes November 30, 2026, 11:59 pm Pacific",
          size=11, ha="left", va="center", wrap_in=7.6)
    # 3 HireVue
    bar(ax, mx(2, 0.0), mx(2, 0.7), lanes_y[2], color=ORANGE)
    label(ax, mx(2, 0.7) + 0.2, lanes_y[2], "HireVue video prompts after November 30 (recorded answers, no live interview; timing not published)",
          size=11, ha="left", va="center", wrap_in=7.2)
    # 4 to 6 the three in-person programs (dates posted)
    programs = [(3, 28 / 31, "First Forward, January 28 to 29, 2027 (1.5 days, US offices only)"),
                (4, 4 / 28, "BEL, February 4 to 5, 2027 (1.5 days, US and Canadian offices)"),
                (4, 18 / 28, "CREW, February 18 to 19, 2027 (1.5 days, US and Canadian offices)")]
    for (mi, frac, text), y in zip(programs, lanes_y[3:6]):
        diamond(ax, mx(mi, frac), y)
        label(ax, mx(mi, frac) + 0.2, y, text, size=11, ha="left", va="center")
    # 7 ACI application window (expected)
    bar(ax, mx(5, 0.0), mx(10, 1.0), lanes_y[6], color=ORANGE)
    label(ax, mx(10, 1.0) + 0.2, lanes_y[6], "Associate Consultant Intern application for Summer 2028: expected to open in spring 2027 "
          "(last cycle's deadlines fell on March 29 and August 31)", size=11, ha="left", va="center", wrap_in=4.3)
    # 8 assessment and interviews (expected)
    bar(ax, mx(6, 0.0), mx(10, 1.0), lanes_y[7], color=ORANGE)
    label(ax, mx(10, 1.0) + 0.2, lanes_y[7], "Spring to summer 2027: digital assessment, then two rounds of case interviews (expected)",
          size=11, ha="left", va="center", wrap_in=4.3)
    # 9 the internship itself and the full-time decision
    bar(ax, mx(20, 0.0), mx(22, 1.0), lanes_y[8], color=BLUE)
    label(ax, mx(20, 0.0) - 0.2, lanes_y[8], "ACI summer 2028: 10 weeks on a case team, $9,000 a month in the US. "
          "Full-time offer decision at the end of the internship; start after graduation in 2029", size=11, ha="right", va="center", wrap_in=6.2)

    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], marker="D", color=BLUE, lw=0, ms=10, label="Posted date (verify on bain.com)"),
                       Line2D([0], [0], color=BLUE, lw=8, label="Posted window"),
                       Line2D([0], [0], color=ORANGE, lw=8, label="Expected, projected from last cycle (not yet posted)")],
              loc="lower left", bbox_to_anchor=(0.02, 0.0), ncol=3, frameon=False, fontsize=11)
    assert_fits(fig, W, "01-class-of-2029-timeline.png")
    finish(fig, OUT / "01-class-of-2029-timeline.png")
    add("01-class-of-2029-timeline.png",
        "Timeline from October 2026 to Summer 2028 showing Bain's sophomore program dates and the expected ACI window",
        "The only firm deadline in front of a sophomore today is November 30, and the ACI window that matters is expected a few weeks after the February programs.",
        "Timeline drawn in matplotlib from the Class of 2029 table in the draft; the ACI windows carry [VERIFY] tags and are shown as expected",
        "| Full-time Associate Consultant | Offer decision at the end")


# ---------------------------------------------------------------- 02 the four programs side by side
ROWS = [
    ("When", ["February 4 to 5, 2027 (1.5 days)",
              "February 18 to 19, 2027 (1.5 days)",
              "January 28 to 29, 2027 (1.5 days)",
              "October 2026, three virtual sessions"]),
    ("Format", ["In person in a Bain office: interactive sessions, case discussions, workshops, networking and social events",
                "Same shape as BEL, with Women at Bain members on how they built their careers",
                "Same shape; no prior business experience needed, in Bain's own words",
                "Webinar series with recruiters and recent hires. No office visit, no case, no interview"]),
    ("Where", ["14 US and Canadian offices. Denver, Los Angeles and Seattle picks attend in Los Angeles; Montreal and Toronto picks in Toronto",
               "Same 14 offices. Denver, Los Angeles and Seattle picks attend in Seattle; Montreal and Toronto picks in Toronto",
               "14 US offices only (no Montreal or Toronto). Denver, Los Angeles and Seattle picks attend in Denver",
               "Online. The form asks for your top three office preferences"]),
    ("Built around", ["Black at Bain and Familia at Bain",
                      "Women at Bain",
                      "First at Bain (first generation and lower income)",
                      "No affinity group framing"]),
    ("Who can apply", ["Second-years finishing a four-year degree in the US or Canada by winter 2028 or spring 2029, with an interest in connecting with those groups",
                       "Second-years on the same window, with an interest in connecting with Women at Bain",
                       "Second-years on the same window who are first in their family to finish a four-year degree, or grew up in a lower-income household. Either one counts",
                       "Second-years at four-year universities in the US or Canada. No background requirement"]),
    ("How you're selected", ["One shared application (resume, optional cover letter, transcript, test scores, three office preferences), closes November 30, 2026. Then HireVue video prompts. No interviews",
                             "Same application, same deadline, same HireVue step",
                             "Same application, same deadline, same HireVue step",
                             "Registration form, closed October 5, 2026, 11:59 pm Pacific"]),
    ("What it leads to", ["No promised fast track. The FAQ tells unsuccessful applicants to apply to the ACI",
                          "Same FAQ answer as BEL",
                          "Same FAQ answer as BEL",
                          "Bain's words: built to set up a foundation for future Bain recruiting processes"]),
]
COLS = ["BEL (Building Entrepreneurial Leaders)", "CREW (Connecting and Resourcing Empowered Women)", "First Forward", "Consulting Kickstart"]


def program_comparison():
    W = 11
    size, label_w, col_w, gap, pad = 10.5, 1.4, 2.17, 0.08, 0.1
    # row heights from the wrapped text
    heights = []
    for _, cells in ROWS:
        n = max(wrap(c, col_w - 2 * pad - 0.1, size).count("\n") + 1 for c in cells)
        heights.append(n * size * 1.28 / 72 + 2 * pad + 0.04)
    head_h = 0.72
    H = 0.75 + head_h + sum(heights) + gap * (len(ROWS) + 1) + 0.55
    fig, ax = canvas(W, H, title="Four Bain programs: three winter weekends and one October webinar series")
    x_label = 0.3
    x_cols = [x_label + label_w + gap + i * (col_w + gap) for i in range(4)]
    y = H - 0.85
    for i, head in enumerate(COLS):
        fill = BLUE if i < 3 else SEQ_BLUE[11]
        text_box(ax, x_cols[i], y - head_h, col_w, head_h, head, fill=fill, text_color="white", size=11.5, bold=True, radius=0.06)
    y -= head_h + gap
    for (row_label, cells), h in zip(ROWS, heights):
        label(ax, x_label + label_w - 0.05, y - h / 2, row_label, size=11, bold=True, ha="right", va="center", wrap_in=label_w - 0.1)
        for i, cell in enumerate(cells):
            fill = PALE_BLUE if i < 3 else PALE_GRAY
            text_box(ax, x_cols[i], y - h, col_w, h, cell, fill=fill, size=size, ha="left", pad_in=pad + 0.05, radius=0.04)
        y -= h + gap
    label(ax, x_label, y - 0.12, "Details as posted on bain.com and checked on October 5, 2026; the three in-person programs are not internships and are not paid. "
          "Bain's real internship for this class is the Associate Consultant Intern role, applied for in spring 2027 for Summer 2028.",
          size=10, color=TEXT_SECONDARY, italic=True, ha="left", va="top", wrap_in=W - 0.6)
    assert_fits(fig, W, "02-four-programs-compared.png")
    finish(fig, OUT / "02-four-programs-compared.png")
    add("02-four-programs-compared.png",
        "Grid comparing Bain's BEL, CREW, First Forward and Consulting Kickstart by dates, format, offices, eligibility and selection",
        "BEL, CREW and First Forward are the same day and a half aimed at three communities with one application, and Kickstart is the free webinar series that already closed.",
        "Text graphic drawn in matplotlib from the four program sections of the draft (dates, offices, eligibility, selection, FAQ wording)",
        "**Every Bain program a US sophomore can apply to is one of f")


# ---------------------------------------------------------------- 03 the weeks between
PLAN = [
    ("October to November 2026", 0.0, 2.0,
     "Resume to one page with a number on every leadership line. Three offices chosen for real reasons. Cover letter after two coffee chats. Submit before Thanksgiving. Record four practice HireVue answers"),
    ("December 2026", 2.0, 3.0,
     "Start live cases with a partner: two a week, one profitability and one market sizing, ten minutes of mental math a day. Work Bain's Coffee Shop Co. and FashionCo cases"),
    ("January to February 2027", 3.0, 5.0,
     "Program weekend if you got one, thank-you notes within a day, three cases a week either way. Draft the ACI cover letter with the names from the weekend"),
    ("March 2027", 5.0, 6.0,
     "Sova's sample questions once untimed and once timed. Submit the ACI application in the first window"),
    ("Spring to summer 2027", 6.0, 10.0,
     "Assessment, first round, final round. An offer means Summer 2028 on a case team"),
]


def weeks_between():
    W = 11
    size, text_w = 10, 3.05
    # row heights from the wrapped descriptions
    heights = []
    for head, s, e, body in PLAN:
        n = wrap(body, text_w, size).count("\n") + 1
        heights.append(0.3 + n * size * 1.22 / 72 + 0.16)
    marker_zone = 2.55          # diamonds, their labels and the two brackets, above the axis
    ya = 1.1
    H = 0.85 + sum(heights) + marker_zone + ya + 0.1
    fig, ax = canvas(W, H, title="The weeks between: start casing in December, not after the program")
    x0, x1 = 3.55, W - 0.35
    months = ["Oct\n2026", "Nov", "Dec", "Jan\n2027", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
    step = month_axis(ax, months, ya, x0, x1, size=10.5)

    def mx(mi, frac=0.5):
        return month_x(x0, step, mi, frac)

    y = H - 0.85
    for (head, s, e, body), row_h in zip(PLAN, heights):
        ytop = y
        label(ax, 0.3, ytop - 0.04, head, size=11.5, bold=True, ha="left", va="top")
        label(ax, 0.3, ytop - 0.3, body, size=size, color=TEXT_SECONDARY, ha="left", va="top", wrap_in=text_w, linespacing=1.22)
        ymid = ytop - row_h / 2
        bar(ax, mx(s, 0.0) + 0.04, mx(e, 0.0) - 0.04, ymid, color=BLUE, lw=14)
        ax.plot([x0, x1], [ytop - row_h, ytop - row_h], color=GRID, lw=0.8, zorder=0)
        y -= row_h
    # the marker lane: the three program dates and the expected ACI first deadline
    ym = ya + 1.0
    label(ax, 0.3, ym + 0.12, "Dates on the page", size=11.5, bold=True, ha="left", va="center")
    label(ax, 0.3, ym - 0.14, "Program dates are posted; the ACI first deadline is projected from last cycle's March 29 and not yet posted",
          size=size, color=TEXT_SECONDARY, ha="left", va="top", wrap_in=text_w, linespacing=1.22)
    x_ff, x_bel, x_crew, x_aci = mx(3, 28 / 31), mx(4, 4 / 28), mx(4, 18 / 28), mx(5, 26 / 31)
    for x, col in [(x_ff, BLUE), (x_bel, BLUE), (x_crew, BLUE), (x_aci, ORANGE)]:
        diamond(ax, x, ym, color=col)
        ax.plot([x, x], [ya, ym], color=GRID, lw=1.0, zorder=0)
    # First Forward to the left of its diamond, CREW to the right, BEL and the ACI deadline below
    label(ax, x_ff - 0.14, ym + 0.42, "First Forward\nJan 28 to 29", size=10, ha="right", va="center", linespacing=1.15)
    ax.plot([x_ff, x_ff], [ym + 0.14, ym + 0.42], color=LINE, lw=1.0, zorder=1)
    ax.plot([x_ff - 0.1, x_ff], [ym + 0.42, ym + 0.42], color=LINE, lw=1.0, zorder=1)
    label(ax, x_crew + 0.14, ym + 0.42, "CREW\nFeb 18 to 19", size=10, ha="left", va="center", linespacing=1.15)
    ax.plot([x_crew, x_crew], [ym + 0.14, ym + 0.42], color=LINE, lw=1.0, zorder=1)
    ax.plot([x_crew, x_crew + 0.1], [ym + 0.42, ym + 0.42], color=LINE, lw=1.0, zorder=1)
    label(ax, x_bel, ym - 0.2, "BEL\nFeb 4 to 5", size=10, ha="center", va="top", linespacing=1.15)
    label(ax, x_aci, ym - 0.2, "ACI first deadline\nlate March (expected)", size=10, ha="center", va="top", linespacing=1.15)
    # the gaps, as brackets above the labels
    for (xa, xb, yb, text) in [(x_crew, x_aci, ym + 0.85, "about five weeks from CREW"), (x_bel, x_aci, ym + 1.2, "about seven weeks from BEL")]:
        ax.plot([xa, xa, xb, xb], [yb - 0.08, yb, yb, yb - 0.08], color=TEXT_SECONDARY, lw=1.2, zorder=2)
        label(ax, (xa + xb) / 2, yb + 0.04, text, size=10, color=TEXT_SECONDARY, ha="center", va="bottom", italic=True)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], color=BLUE, lw=8, label="What to do, from the plan in the draft"),
                       Line2D([0], [0], marker="D", color=BLUE, lw=0, ms=10, label="Posted program date"),
                       Line2D([0], [0], marker="D", color=ORANGE, lw=0, ms=10, label="Expected (projected from last cycle)")],
              loc="lower left", bbox_to_anchor=(0.01, 0.0), ncol=3, frameon=False, fontsize=10.5)
    assert_fits(fig, W, "03-weeks-between-plan.png")
    finish(fig, OUT / "03-weeks-between-plan.png")
    add("03-weeks-between-plan.png",
        "Timeline from October 2026 to July 2027 with the five-step plan and the short gap before the ACI deadline",
        "Five to eight weeks separate an early 2027 program from the expected ACI deadline, so the December cases are the ones that count.",
        "Timeline drawn in matplotlib from the five-step plan and the program dates in the draft; the late March ACI deadline is projected from the 2026 pattern and marked expected",
        "- **Spring to summer 2027.** Assessment, first round, final ")


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
    class_of_2029_timeline()
    program_comparison()
    weeks_between()
    check_manifest()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT.relative_to(ROOT)}")
