#!/usr/bin/env python3
"""Images for drafts/draft-consulting-fit-interview-stories-you-need-ready-v2.md (October 11, 2026; pointed at v2 October 12).

Run from the repo root:  python3 scripts/images/build_consulting-fit-interview-stories-you-need-ready.py
Idempotent. Steps:
  1. read the draft and check every number and phrase an image uses against the draft text
     (the format table's minutes, the PEI timing sentence, the four follow-up types and their
     sample questions, the club recruiting story, the story grid rows); stop on any mismatch
  2. draw five images in the banking format into
     published/assets/images/consulting-fit-interview-stories-you-need-ready/
       01 fit minutes per first-round interview by firm (range bars; dated, regenerate at publish)
       02 the four kinds of follow-up question, one sample each (diagram)
       03 time per part of a McKinsey PEI answer (range columns)
       04 the five-part story skeleton filled with the club recruiting example (diagram)
       05 the story-to-firm grid (table graphic; dimension names verified at publish)
  3. write that folder's manifest.json (file, alt, caption, source, method, anchor, regenerate_at_publish)

Nothing here edits the draft. The coordinator inserts the image lines with
scripts/images/insert_images.py from the manifest's anchors.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import *          # noqa: E402,F401,F403
from wsg_diagrams import *     # noqa: E402,F401,F403

import matplotlib  # noqa: E402
matplotlib.rcParams["text.parse_math"] = False      # "$9K" must never be read as mathtext
matplotlib.rcParams["axes.unicode_minus"] = False   # no Unicode minus signs anywhere

SLUG = "consulting-fit-interview-stories-you-need-ready"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v2.md"
TEXT = DRAFT.read_text(encoding="utf-8")
LINES = TEXT.split("\n")
entries = []
problems = []

SRC_FORMATS = "Source: Hacking the Case Interview, CaseCoach, PrepLounge and StrategyCase interview guides, October 2026."
SRC_FOLLOWUPS = "Source: Hacking the Case Interview, PEI follow-up question types, June 2026."
SRC_TIMING = "Source: Hacking the Case Interview, McKinsey PEI answer timing, June 2026."
SRC_WSG = "Source: WSG analysis of the firm pages and trackers cited in this article."


# ---------------------------------------------------------------- the numbers and phrases, checked against the draft
def want(cond, msg):
    if not cond:
        problems.append(msg)


def table_row(first_cell):
    hits = [l for l in LINES if l.startswith(f"| {first_cell} |")]
    want(len(hits) == 1, f"table row for {first_cell!r}: {len(hits)} matches")
    return hits[0] if hits else ""


def cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]


# 01: minutes of fit questions per first-round interview, from the format table's "How long" column
FIT = [  # firm, low, high, label on the bar, phrase that must be in the draft's "How long" cell
    ("McKinsey", 10, 20, "10 to 20 min", "10 to 20 minutes"),
    ("BCG", 10, 15, "10 to 15 min", "10 to 15 minutes"),
    ("Bain", 10, 15, "10 to 15 min where the office runs it", "10 to 15 minutes where it runs"),
    ("Oliver Wyman", 15, 15, "about 15 min", "About 15 minutes"),
    ("L.E.K.", 5, 10, "5 to 10 min", "5 to 10 minutes in round one"),
]
for firm, lo, hi, _, phrase in FIT:
    c = cells(table_row(firm))
    want(len(c) >= 4 and phrase in c[3], f"format table, {firm}: 'How long' cell does not say {phrase!r}")

# 03: the PEI timing sentence
TIMING = [("Summary", 10, 15, "10 to 15 sec"), ("Problem", 30, 45, "30 to 45 sec"),
          ("Actions", 120, 180, "2 to 3 min"), ("Result", 30, 45, "30 to 45 sec")]
want(re.search(r"about 10 to 15 seconds of summary, 30 to 45 seconds of problem, two to three minutes of actions "
               r"and 30 to 45 seconds of result", TEXT) is not None, "PEI timing sentence changed")

# 02: the four follow-up types and one sample question each (all from the leadership story's follow-up list)
FOLLOWUPS = [
    ("Factual check", "the facts: what happened and when",
     "How did you know, in week four, that the change was working?"),
    ("Decision probe", "why you chose that over the alternative",
     "Why did you take on the hard subjects yourself instead of assigning them?"),
    ("Interpersonal probe", "what the other person said",
     "What exactly did the two experienced tutors say when they pushed back?"),
    ("Reflection probe", "what you'd do differently",
     "If one of the two had refused, what would you have done?"),
]
for kind in ("factual checks", "decision probes", "interpersonal probes", "reflection probes"):
    want(kind in TEXT, f"follow-up type {kind!r} not in the draft")
for _, _, q in FOLLOWUPS:
    want(q in TEXT, f"sample question not in the draft: {q!r}")
want("10 to 25 follow-up questions" in TEXT, "McKinsey's 10 to 25 follow-ups changed")
want("two or three probes per story" in TEXT, "BCG's two or three probes changed")

# 04: the club recruiting story (the one worked example with all five parts)
SKELETON = [
    ("1. Setup", "two sentences",
     "Ran the club's fall recruiting drive.\nSkipped the activities fair and put the time into a social media "
     "campaign; applications came in at about half the year before."),
    ("2. Your role", "one sentence", "In charge of the recruiting drive. Skipping the fair was your call."),
    ("3. Actions", "in detail",
     "Deadline day count: 40 applications against 85 the year before.\nTold the club president that night and "
     "asked for an extra week.\nSpent the week at tables outside the business school, three hours a day, with "
     "two other members."),
    ("4. Result", "with a number", "Final count about 70, up from 40 at the deadline."),
    ("5. One thing you'd do differently", "",
     "Ran the fair and the online campaign both the next year.\nWrote a one-page handoff so the fair never got "
     "skipped again."),
]
for phrase in ("skip the activities fair", "social media campaign", "about half the previous year",
               "40 against 85", "told the club's president that night", "asked for an extra week",
               "three hours a day with two other members", "final count landed at about 70",
               "ran the fair and the online campaign both", "one-page handoff",
               "a two-sentence setup, a one-sentence statement of your role, the actions in detail, "
               "a result with a number, and one thing you'd do differently",
               "the actions are the only part of the story the interviewer can score"):
    want(phrase in TEXT, f"recruiting story or five-part sentence changed: {phrase!r}")

# 05: the story grid, condensed to note form; every word of four letters or more must be in the draft's row
GRID_HEADER = ["Story", "McKinsey PEI dimension (second tag)", "BCG quality", "Bain prompt", "Oliver Wyman, L.E.K., Kearney"]
GRID = [
    ("1. Leadership", "Leadership (Drive, if you pushed through resistance)", "Collaborative Mindset",
     "A time you showed leadership; what you'd bring to a case team", "Kearney: leadership and teamwork"),
    ("2. Persuasion", "Connection (Leadership)", "Collaborative Mindset, Integrity",
     "Overcome resistance to implement a solution", "L.E.K.: changed your mind on new evidence, told from the other side"),
    ("3. Failure", "Growth (Drive, for the recovery)", "Drive (how you recovered)",
     "The experience you wish you could do over", "L.E.K.: a time you were wrong about something important"),
    ("4. Team conflict", "Leadership or Connection", "Collaborative Mindset",
     "A team conflict and how you resolved it", "Kearney: conflict resolution"),
    ("5. Initiative", "Drive (Growth, if you had to change course)", "Drive",
     "Initiative on a problem that wasn't assigned to you", "Oliver Wyman: initiative"),
    ("6. Analytical problem", "Drive, if it involved setbacks (otherwise not scored in the PEI)",
     "Intellectual Curiosity, Creative Thinking", "Most proud accomplishment",
     "Oliver Wyman: data and analytical skills; L.E.K.: evaluating a company"),
]
for row in GRID:
    draft_row = table_row(row[0]).lower()
    for cell in row[1:]:
        for tok in re.findall(r"[A-Za-z]{4,}", cell):
            want(tok.lower() in draft_row, f"grid row {row[0]!r}: {tok!r} is not in the draft's row")
want(re.search(r"\| Story \| McKinsey PEI dimension \| BCG quality \| Bain prompt \| Tier 2 \(OW, L\.E\.K\., Kearney\) \|", TEXT)
     is not None, "grid header changed")

if problems:
    print("IMAGES DO NOT MATCH THE DRAFT:")
    for p in problems:
        print("  " + p)
    sys.exit(1)
print("draft checks: format table minutes, PEI timing, follow-up types and samples, recruiting story, grid rows all match")


# ---------------------------------------------------------------- helpers
def add(file, alt, caption, source, method, anchor, dated=False):
    entries.append({"file": file, "alt": alt, "caption": caption, "source": source, "method": method,
                    "anchor": anchor, "regenerate_at_publish": dated})


def assert_fits(fig, width_in, name):
    fig.canvas.draw()
    bb = fig.get_tightbbox(fig.canvas.get_renderer())
    assert bb.x0 >= -0.05 and bb.x1 <= width_in + 0.05, f"{name}: content spans {bb.x0:.2f} to {bb.x1:.2f} in on a {width_in} in canvas"


def anchor_for(prefix):
    hits = [l for l in LINES if l.strip().startswith(prefix)]
    assert len(hits) == 1, f"anchor {prefix!r} matches {len(hits)} draft lines"
    return hits[0].strip()[:60]


def diagram_source(ax, text, x=0.35, y=0.22):
    """Source line on a diagram canvas, flush with the content margin (add_source lands on the figure edge there)."""
    ax.text(x, y, text, ha="left", va="center", fontsize=10, color=BLACK)


def range_legend(ax, loc):
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=NAVY, label="Low end of the range"), Patch(color=LIGHT_BLUE, label="High end of the range")],
              loc=loc, ncol=1, frameon=False, fontsize=11, handlelength=1.4, handleheight=0.9, labelcolor=BLACK)


def text_right_edge(fig, ax, t):
    """x (data coords) of a text artist's right edge, measured by the renderer."""
    fig.canvas.draw()
    bb = t.get_window_extent(fig.canvas.get_renderer())
    return ax.transData.inverted().transform((bb.x1, bb.y0))[0]


# ---------------------------------------------------------------- 01: fit minutes by firm (horizontal bars, range cap)
def fit_minutes_chart():
    fig, ax = new_figure(width=11, height=5.0)
    n = len(FIT)
    ys = list(range(n))[::-1]
    for y, (firm, lo, hi, lab, _) in zip(ys, FIT):
        ax.barh(y, lo, height=0.5, color=NAVY, zorder=3)
        if hi > lo:
            ax.barh(y, hi - lo, left=lo, height=0.5, color=LIGHT_BLUE, zorder=3)
        ax.text(hi + 0.4, y, lab, ha="left", va="center", fontsize=12.5, color=BLACK)
    ax.set_xlim(0, 30)
    ax.set_ylim(-0.7, n - 0.3)
    style_axes(ax, title="Minutes of fit questions in a first-round interview, 2026", value_axis=False)
    ax.set_yticks(ys)                      # style_axes clears y ticks for vertical bars; put the firm names back
    ax.set_yticklabels([f[0] for f in FIT], fontsize=13)
    ax.set_xticks([])
    range_legend(ax, "lower right")
    fig.subplots_adjust(left=0.14, right=0.98, top=0.86, bottom=0.08)
    add_source(fig, SRC_FORMATS)
    assert_fits(fig, 11, "01")
    finish(fig, OUT / "01-fit-minutes-by-firm.png")
    add("01-fit-minutes-by-firm.png",
        "Horizontal bar chart of fit interview minutes per first-round interview at McKinsey, BCG, Bain, Oliver Wyman and L.E.K.",
        "McKinsey gives fit 10 to 20 minutes per first-round interview; L.E.K. gives it 5 to 10.",
        SRC_FORMATS,
        "Bars from the 'How long' column of the format table in the draft (McKinsey 10 to 20, BCG 10 to 15, Bain 10 to 15 where it runs, Oliver Wyman about 15, L.E.K. 5 to 10); navy to the low end, light blue to the high end; Kearney is not fixed and is left out",
        anchor_for("| L.E.K. | Behavioral discussion |"), dated=True)


# ---------------------------------------------------------------- 02: four kinds of follow-up question (diagram)
def followup_diagram():
    W, H = 11, 6.85
    fig, ax = canvas(W, H, title="Four kinds of follow-up question in the fit interview")
    label(ax, 0.35, H - 0.78, "Sample questions for a story about running a 12-person tutoring program",
          size=11.5, color=BLACK, ha="left", va="top")
    # the opening answer on the left
    lx, lw, lh = 0.35, 3.0, 1.2
    bx, bw, bh, gap = 4.3, 6.35, 1.0, 0.18
    top = H - 1.25
    centers = []
    for i, (kind, gloss, q) in enumerate(FOLLOWUPS):
        y = top - i * (bh + gap) - bh
        text_box(ax, bx, y, bw, bh, "", fill=PALE_GRAY, radius=0.06)
        t = label(ax, bx + 0.2, y + bh - 0.2, kind, size=12.5, bold=True, color=BLACK, ha="left", va="top")
        label(ax, text_right_edge(fig, ax, t) + 0.12, y + bh - 0.2, f"({gloss})", size=11, color=BLACK, ha="left", va="top")
        label(ax, bx + 0.2, y + 0.2, f'"{q}"', size=11.5, color=BLACK, ha="left", va="bottom", wrap_in=bw - 0.4)
        centers.append(y + bh / 2)
    mid = sum(centers) / len(centers)
    text_box(ax, lx, mid - lh / 2, lw, lh, "Your opening answer: one story", fill=NAVY, text_color="white", size=12.5, bold=True)
    for cy in centers:
        arrow(ax, (lx + lw, mid), (bx - 0.02, cy), color=GRAY, lw=1.6, head=14, connection="arc3,rad=0")
    label(ax, 0.35, 0.68, "McKinsey asks 10 to 25 follow-ups per story; BCG asks two or three.", size=11.5, color=BLACK,
          ha="left", va="center")
    diagram_source(ax, SRC_FOLLOWUPS)
    assert_fits(fig, W, "02")
    finish(fig, OUT / "02-follow-up-question-types.png")
    add("02-follow-up-question-types.png",
        "Diagram of four follow-up question types, each with a sample question about a tutoring program story",
        "McKinsey interviewers ask 10 to 25 follow-ups per story, drawn from these four types.",
        SRC_FOLLOWUPS,
        "Diagram drawn in matplotlib from the four follow-up types in the scoring section and the sample follow-ups listed under the leadership story",
        anchor_for("Hacking the Case Interview sorts PEI follow-ups into four types"))


# ---------------------------------------------------------------- 03: time per part of a PEI answer (vertical range columns)
def timing_chart():
    fig, ax = new_figure(width=9.5, height=5.6)
    xs = list(range(len(TIMING)))
    for x, (part, lo, hi, lab) in zip(xs, TIMING):
        ax.bar(x, lo, width=0.5, color=NAVY, zorder=3)
        ax.bar(x, hi - lo, bottom=lo, width=0.5, color=LIGHT_BLUE, zorder=3)
        ax.text(x, hi + 4, lab, ha="center", va="bottom", fontsize=12.5, color=BLACK)
    ax.set_xticks(xs)
    ax.set_xticklabels([t[0] for t in TIMING], fontsize=13)
    ax.set_ylim(0, 205)
    ax.set_xlim(-0.6, len(TIMING) - 0.4)
    style_axes(ax, title="Time for each part of a McKinsey PEI answer", value_axis=False)
    range_legend(ax, "upper left")
    fig.subplots_adjust(left=0.04, right=0.98, top=0.86, bottom=0.1)
    add_source(fig, SRC_TIMING)
    assert_fits(fig, 9.5, "03")
    finish(fig, OUT / "03-pei-answer-timing.png")
    add("03-pei-answer-timing.png",
        "Bar chart of seconds spent on summary, problem, actions and result in a McKinsey PEI answer",
        "Actions get two to three minutes; summary, problem and result get 10 to 45 seconds each.",
        SRC_TIMING,
        "Bars from the Hacking the Case Interview timing sentence in the draft (10 to 15 seconds, 30 to 45 seconds, two to three minutes, 30 to 45 seconds); navy to the low end, light blue to the high end",
        anchor_for("Every one of the six stories uses the same five-part structure"))


# ---------------------------------------------------------------- 04: the five-part story, filled in (diagram)
def skeleton_diagram():
    W = 11
    lx, lw = 0.35, 2.2           # part labels
    cx, cw = 2.75, 6.0           # content boxes
    nx, nw = 8.95, 1.75          # note beside the actions block
    size, pad = 11.5, 0.17
    heights = []
    for _, _, content in SKELETON:
        n_lines = wrap(content, cw - 2 * pad, size).count("\n") + 1
        heights.append(max(0.62, n_lines * size * 1.3 / 72 + 2 * pad))
    gap = 0.16
    H = 0.95 + sum(heights) + gap * (len(SKELETON) - 1) + 0.6
    fig, ax = canvas(W, H, title="A five-part story, using the club recruiting example")
    y = H - 0.95
    for (part, hint, content), h in zip(SKELETON, heights):
        hot = part.startswith("3.")
        text_box(ax, cx, y - h, cw, h, content, fill=PALE_BLUE if hot else PALE_GRAY, edge=NAVY if hot else None,
                 lw=1.6 if hot else 1.0, size=size, ha="left", pad_in=pad, text_color=BLACK, radius=0.06)
        label(ax, lx, y - h / 2, part, size=12.5, bold=True, color=BLACK, ha="left", va="center", wrap_in=lw)
        if hint:
            n_part = wrap(part, lw, 12.5, bold=True).count("\n") + 1
            label(ax, lx, y - h / 2 - n_part * 0.13 - 0.1, hint, size=11, color=BLACK, ha="left", va="center")
        if hot:
            label(ax, nx, y - h / 2, "Two to three minutes of the telling; the part the interviewer scores",
                  size=10.5, color=BLACK, ha="left", va="center", wrap_in=nw)
        y -= h + gap
    diagram_source(ax, SRC_WSG)
    assert_fits(fig, W, "04")
    finish(fig, OUT / "04-five-part-story-example.png")
    add("04-five-part-story-example.png",
        "Five stacked boxes showing setup, role, actions, result and lesson for the club recruiting story, actions shaded",
        "The shaded actions block is the part the interviewer scores and gets two to three minutes of the telling.",
        SRC_WSG,
        "Diagram drawn in matplotlib from the five-part structure sentence and the club recruiting (failure) story in the draft, in note form",
        anchor_for("Then build the one-page grid."))


# ---------------------------------------------------------------- 05: the story-to-firm grid (table graphic with wrapped cells)
def grid_table():
    W = 11
    widths = [1.55, 2.45, 1.95, 2.3, 2.35]
    x0, size, hsize = 0.35, 10.5, 11
    xs, acc = [], x0
    for w in widths:
        xs.append(acc)
        acc += w
    pad = 0.1
    wrapped = [[wrap(c, w - 2 * pad, size) for c, w in zip(row, widths)] for row in GRID]
    row_h = [max(t.count("\n") + 1 for t in r) * size * 1.3 / 72 + 0.22 for r in wrapped]
    head_w = [wrap(h, w - 2 * pad, hsize, bold=True) for h, w in zip(GRID_HEADER, widths)]
    head_h = max(t.count("\n") + 1 for t in head_w) * hsize * 1.3 / 72 + 0.2
    H = 0.95 + head_h + sum(row_h) + 0.6
    fig, ax = canvas(W, H, title="Which story answers which firm's fit question")
    y = H - 0.95
    for t, x in zip(head_w, xs):
        label(ax, x + pad, y - head_h / 2, t, size=hsize, bold=True, color=BLACK, ha="left", va="center", linespacing=1.3)
    y -= head_h
    line(ax, (x0, y), (sum(widths) + x0, y), color=BLACK, lw=0.9, zorder=2)
    for r, h in zip(wrapped, row_h):
        for i, (t, x) in enumerate(zip(r, xs)):
            label(ax, x + pad, y - h / 2, t, size=size, bold=(i == 0), color=BLACK, ha="left", va="center", linespacing=1.3)
        y -= h
    diagram_source(ax, SRC_WSG)
    assert_fits(fig, W, "05")
    finish(fig, OUT / "05-story-to-firm-grid.png")
    add("05-story-to-firm-grid.png",
        "Table mapping six fit stories to McKinsey dimensions, BCG qualities, Bain prompts and tier 2 firm questions",
        "Each story carries a first and second McKinsey tag, so six stories give two examples per dimension.",
        SRC_WSG,
        "Table drawn in matplotlib from the story grid in the draft, cells condensed to note form (every word checked against the draft's row)",
        anchor_for("| 6. Analytical problem |"), dated=True)


# ---------------------------------------------------------------- manifest
def check_manifest():
    from PIL import Image
    for e in entries:
        for k in ("alt", "caption", "source", "method", "anchor"):
            for ch in (chr(0x2014), chr(0x2013), chr(0x2212)):   # em dash, en dash, Unicode minus
                assert ch not in e[k], f"dash in manifest {e['file']} {k}"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
        assert len(e["caption"].split()) <= 20, f"caption of {e['file']} is over 20 words"
        assert e["source"].startswith("Source:"), f"source of {e['file']} must start with 'Source:'"
        hits = [l for l in LINES if l.strip().startswith(e["anchor"])]
        assert len(hits) == 1, f"anchor for {e['file']} matches {len(hits)} draft lines: {e['anchor']!r}"
        im = Image.open(OUT / e["file"])
        assert im.width <= 2200, f"{e['file']} is {im.width} px wide"
        assert im.info.get("Author") in (None, "Wall Street Guide"), f"{e['file']} carries an author tag"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    fit_minutes_chart()
    followup_diagram()
    timing_chart()
    skeleton_diagram()
    grid_table()
    entries.sort(key=lambda e: e["file"])
    check_manifest()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT.relative_to(ROOT)}")
    for e in entries:
        print(f"  {e['file']}  anchor={e['anchor']!r}  dated={e['regenerate_at_publish']}")


if __name__ == "__main__":
    main()
