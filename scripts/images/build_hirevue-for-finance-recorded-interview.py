#!/usr/bin/env python3
"""Images for drafts/draft-hirevue-for-finance-recorded-interview-v1.md (October 11, 2026).

Run from the repo root:  python3 scripts/images/build_hirevue-for-finance-recorded-interview.py
Idempotent: rewrites every PNG in published/assets/images/hirevue-for-finance-recorded-interview/
and the folder's manifest.json (file, alt, caption, source, method, anchor). The draft is never
edited; the coordinator inserts the image lines with scripts/images/insert_images.py.

Every number and every firm detail comes from the draft: the section 1 firm table, the 13 steps
in section 2, the word budget in section 5, the setup rules in section 6 and the timing list in
section 7. The script reads the draft and asserts each figure before it draws, so a later edit
to the draft fails the build loudly. Banking format throughout: black Arial text, no gridlines,
no boxes or frames around charts, direct labels, source line bottom-left.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import (BANK_SERIES, BLACK, GRAY, LIGHT_BLUE, MID_BLUE, NAVY, add_source, new_figure,  # noqa: E402
                     save_figure, style_axes, write_manifest)
from wsg_diagrams import canvas, finish, label, month_x, text_box, wrap  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.rcParams["text.parse_math"] = False
matplotlib.rcParams["axes.unicode_minus"] = False
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon  # noqa: E402

SLUG = "hirevue-for-finance-recorded-interview"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v1.md"
TEXT = DRAFT.read_text(encoding="utf-8")
LINES = TEXT.split("\n")
PALE = "#eef3f9"      # box fill behind black text in the diagrams
entries = []


def add(file, alt, caption, source, method, anchor):
    entries.append({"file": file, "alt": alt, "caption": caption, "source": source, "method": method, "anchor": anchor})


def anchor_for(start):
    """The first 60 characters, verbatim, of the one draft line that starts with `start`."""
    hits = [l for l in LINES if l.startswith(start)]
    assert len(hits) == 1, f"{len(hits)} draft lines start with {start!r}"
    return hits[0][:60]


def must(pattern, where=TEXT, what=None):
    assert re.search(pattern, where), f"draft no longer says {what or pattern!r}"


def section(n):
    """Text of the draft's numbered H2 section n."""
    m = re.search(rf"^## {n}\. .*?(?=^## )", TEXT, re.S | re.M)
    assert m, f"section {n} missing"
    return m.group(0)


# ---------------------------------------------------------------- the section 1 table, read from the draft
def draft_table_rows():
    rows = {}
    for l in LINES:
        if l.startswith("| ") and not l.startswith("| Firm") and not l.startswith("| ---"):
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(cells) == 4:
                rows[cells[0]] = cells
    assert len(rows) == 20, f"section 1 table has {len(rows)} firm rows, expected 20"
    return rows


# firm, recorded interview?, what candidates report (trimmed), source type
BANKS = [
    ("Goldman Sachs", "Yes, HireVue, since 2016", "3 to 6 questions, 1:30 to 2:00 answers, usually one take, about a week", "Goldman's own post; HR Dive"),
    ("JPMorgan", "Yes, HireVue", "3 to 5 questions, one optional retake, 7 days", "Federal court record; Glassdoor"),
    ("Morgan Stanley", "Yes, HireVue (prep guides)", "3 to 5 questions, 90 seconds to 2 minutes, one retry, 48 to 72 hours", "Prep guides; Glassdoor"),
    ("Bank of America", "Yes, HireVue (prep guides)", "5 to 7 questions, 2 to 3 minutes, about two days", "Prep guide"),
    ("Citi", "Yes, HireVue (prep guides)", "3 to 6 questions, 1 to 3 minutes, about 48 hours", "Prep guide"),
    ("Barclays", "No video step on its official page", "Application, two assessments, assessment centre", "Barclays' own page"),
    ("UBS", "Yes, HireVue (prep guides)", "6 to 8 questions, about 2 minutes, no re-record", "Prep guide"),
    ("Deutsche Bank", "Yes for some roles; platform not named", "UK, Germany and APAC roles; invite about six weeks after applying", "Deutsche Bank's own page"),
    ("Wells Fargo", "Yes, HireVue (prep guides)", "4 to 6 prompts; next day to about a week", "Prep guide"),
    ("RBC", "Yes, HireVue (prep guides)", "4 to 5 questions, 90 to 120 seconds", "Prep guide"),
    ("Jefferies", "Online test, then phone or HireVue (prep guides)", "SHL test, then a 20 to 30 minute first round", "Prep guide"),
]
OTHERS = [
    ("Evercore", "No, live only in the US (prep guides)", "No recorded screen in the US; UK and EMEA have one", "Prep guide"),
    ("Lazard", "Recorded, mainly UK and Europe (prep guides)", "3 to 5 questions, about 2 minutes, no retakes", "Prep guide"),
    ("PJT Partners", "No; written Suited assessment, then live (prep guides)", "Every interview is live", "Prep guide"),
    ("Moelis", "No; written Suited assessment, then live (prep guides)", "No recorded video at any point", "Prep guide"),
    ("BlackRock", "Yes, a recorded pre-interview assessment", "3 minutes prep, 90-second answers, no retakes", "BlackRock's early careers page"),
    ("Vanguard", "Yes, HireVue after online games (prep guides)", "Background and interest questions", "Prep guide"),
    ("Fidelity", "HireVue for some roles (prep guides)", "Replaces a live behavioral round for some roles", "Prep guide"),
    ("Citadel", "No, live", "45 to 60 minute remote first round; CoderPad link sent ahead", "Citadel's own page"),
    ("McKinsey", "No; the Solve game, then live", "Problem-solving game, no recorded video", "McKinsey's own page"),
]


def check_table(rows, draft):
    """Every firm is a row of the draft table, and every number in a trimmed cell appears in that row."""
    for firm, uses, report, src in rows:
        assert firm in draft, f"{firm} is not in the section 1 table"
        row_text = " ".join(draft[firm])
        for cell in (uses, report):
            for num in re.findall(r"\d[\d:]*", cell):
                assert num in row_text, f"{firm}: {num!r} from {cell!r} is not in the draft row"
        key = {"Yes": "Yes", "No": "No", "Online": "Online", "Recorded": "Recorded", "HireVue": "HireVue"}
        assert draft[firm][1].split(",")[0].split(";")[0].split(" ")[0] == uses.split(",")[0].split(";")[0].split(" ")[0], \
            f"{firm}: recorded-interview answer changed ({draft[firm][1]!r})"


def table_graphic(fname, title, rows, source):
    header = ["Firm", "Recorded interview?", "What candidates report", "Source"]
    W = 11.0
    col_w = [1.55, 2.55, 4.0, 2.35]
    size, pad, x_left = 11.0, 0.07, 0.3
    heights = []
    for row in rows:
        n = max(wrap(c, w - 2 * pad, size).count("\n") + 1 for c, w in zip(row, col_w))
        heights.append(n * size * 1.25 / 72 + 2 * pad + 0.06)
    head_h = 0.36
    H = 0.75 + head_h + sum(heights) + 0.55
    fig, ax = canvas(W, H, title=title, title_size=16)
    xs = []
    acc = x_left
    for w in col_w:
        xs.append(acc)
        acc += w
    y = H - 0.8
    for x, h in zip(xs, header):
        label(ax, x + pad, y - head_h / 2, h, size=size, bold=True, color=BLACK, ha="left", va="center")
    y -= head_h
    ax.plot([x_left, acc], [y, y], color=BLACK, lw=0.9)
    for row, h in zip(rows, heights):
        for x, w, cell in zip(xs, col_w, row):
            label(ax, x + pad, y - h / 2, cell, size=size, color=BLACK, ha="left", va="center", wrap_in=w - 2 * pad, linespacing=1.2)
        y -= h
    ax.plot([x_left, acc], [y, y], color=BLACK, lw=0.5)
    ax.text(x_left, y - 0.22, source, ha="left", va="top", fontsize=10, color=BLACK)
    finish(fig, OUT / fname)


def image_01_02():
    draft = draft_table_rows()
    check_table(BANKS, draft)
    check_table(OTHERS, draft)
    assert len(BANKS) + len(OTHERS) == 20
    src = "Source: Firm careers pages, court records, Glassdoor and prep guides, October 2026"
    table_graphic("01-banks-recorded-interview.png", "Which banks use a recorded first-round interview", BANKS, src)
    add("01-banks-recorded-interview.png",
        "Table of 11 banks showing whether each uses a recorded interview, what candidates report and the source",
        "Goldman, JPMorgan, Morgan Stanley, Bank of America and Citi all run a recorded round.",
        "Firm careers pages, court records, Glassdoor and prep guides, October 2026",
        "Table graphic drawn in matplotlib from the first 11 rows of the section 1 firm table, candidate reports trimmed to a few words",
        anchor_for("Two patterns in the table are worth knowing"))
    table_graphic("02-boutiques-and-others-recorded-interview.png", "Boutiques, asset managers and others: recorded or live", OTHERS,
                  "Source: Firm careers pages, Glassdoor and prep guides, October 2026")
    add("02-boutiques-and-others-recorded-interview.png",
        "Table of nine boutiques, asset managers and other firms showing recorded or live first rounds and the source",
        "Evercore, PJT and Moelis interview live from the first round; Lazard records mainly outside the US.",
        "Firm careers pages, Glassdoor and prep guides, October 2026",
        "Table graphic drawn in matplotlib from the last nine rows of the section 1 firm table, candidate reports trimmed to a few words",
        anchor_for("The elite boutiques run smaller processes"))


# ---------------------------------------------------------------- 03 on-screen sequence
STEPS = [
    "Invitation email arrives with the due date or window",
    "Requirements page, with the accommodations link",
    "Bank, role, question count and total length shown",
    "Accept the terms",
    "Optional intro video from the bank",
    "Camera and microphone check",
    "Choose: practice question or skip",
    "Attempts screen: takes per question",
    "Practice questions: unlimited, never submitted",
    "Press Start Now: the clocks run",
    "Each question: prep clock, 3-second countdown, answer clock, auto-submit",
    "Connection drops: reopen the link, back to the last unanswered question",
    "Answers upload; the bank decides next steps",
]


def image_03():
    s2 = section(2)
    numbered = re.findall(r"^(\d+)\. ", s2, re.M)
    assert numbered == [str(i) for i in range(1, 14)], f"section 2 has steps {numbered}"
    for phrase in ("Practice or Interview", "Start Now", "Not Recording", "Start Recording", "three-second countdown",
                   "Done Answering", "last unanswered question", "three generic practice questions", "the number of attempts"):
        must(re.escape(phrase), s2, phrase)
    W = 11.0
    bw, bh, gap, per_row = 1.9, 1.05, 0.22, 5
    x_left = 0.35
    rows = [STEPS[0:5], STEPS[5:10], STEPS[10:13]]
    row_h = bh + 0.55
    H = 0.85 + len(rows) * row_h + 0.65
    fig, ax = canvas(W, H, title="HireVue on screen: 13 steps from invitation to upload", title_size=16)
    y = H - 0.95 - bh
    n = 0
    centers = []
    for r, row in enumerate(rows):
        for i, text in enumerate(row):
            n += 1
            x = x_left + i * (bw + gap)
            fill = NAVY if n in (8, 10, 11) else PALE
            tc = "white" if n in (8, 10, 11) else BLACK
            text_box(ax, x, y, bw, bh, f"{n}. {text}", fill=fill, text_color=tc, size=10.5, pad_in=0.1, radius=0.05)
            centers.append((x, y, n))
            if i > 0:
                ax.annotate("", xy=(x, y + bh / 2), xytext=(x - gap, y + bh / 2),
                            arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.2, mutation_scale=12, shrinkA=0, shrinkB=0))
        if r < len(rows) - 1:
            # return connector from the row's last box down to the next row's first box
            x_end = x_left + (len(row) - 1) * (bw + gap) + bw / 2
            y_next = y - row_h + bh
            ax.plot([x_end, x_end], [y, y - 0.22], color=BLACK, lw=1.2)
            ax.plot([x_end, x_left + bw / 2], [y - 0.22, y - 0.22], color=BLACK, lw=1.2)
            ax.annotate("", xy=(x_left + bw / 2, y_next), xytext=(x_left + bw / 2, y - 0.22),
                        arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.2, mutation_scale=12, shrinkA=0, shrinkB=0))
        y -= row_h
    # legend for the three dark boxes
    yl = y + row_h - 0.42
    ax.add_patch(Rectangle((x_left, yl - 0.09), 0.26, 0.18, facecolor=NAVY, edgecolor=NAVY))
    label(ax, x_left + 0.36, yl, "Steps that set the rules: the attempts screen, Start Now, and the question clocks",
          size=10.5, color=BLACK, va="center")
    ax.text(x_left, yl - 0.4, "Source: HireVue Candidate Help Center, on-demand interview articles, October 2026",
            ha="left", va="top", fontsize=10, color=BLACK)
    finish(fig, OUT / "03-on-screen-sequence.png")
    add("03-on-screen-sequence.png",
        "Flow diagram of the 13 HireVue screens from the invitation email to the upload of your answers",
        "Steps 1 to 9 are setup you can do days early; the clocks start at step 10, Start Now.",
        "HireVue Candidate Help Center, on-demand interview articles, October 2026",
        "Sequence diagram drawn in matplotlib from the 13 numbered steps in section 2 of the draft",
        anchor_for("Step 3 tells you the total length"))


# ---------------------------------------------------------------- 04 word budget
BUDGET = [("Situation\n2 sentences", 25), ("Task\n1 sentence", 15), ("Action\n5 or 6 sentences", 85), ("Result\n1 or 2 sentences", 25)]


def image_04():
    s5 = section(5)
    must(r"The situation gets two sentences, around 25 words", s5)
    must(r"The task gets one, around 15", s5)
    must(r"five or six sentences and around 85 words", s5)
    must(r"The result gets one or two sentences, around 25 words", s5)
    must(r"about 70 to 90 seconds", s5)
    assert sum(v for _, v in BUDGET) == 150
    must(r"Here's what 150 words looks like", s5)
    fig, ax = new_figure(width=11.0, height=5.0)
    names = [n for n, _ in BUDGET][::-1]
    vals = [v for _, v in BUDGET][::-1]
    colors = [GRAY, NAVY, GRAY, GRAY]   # action in navy, the rest gray
    bars = ax.barh(range(4), vals, color=colors, height=0.6)
    for b, v in zip(bars, vals):
        ax.text(b.get_width() + 1.5, b.get_y() + b.get_height() / 2, f"{v} words", va="center", ha="left", fontsize=13, color=BLACK)
    ax.set_yticks(range(4))
    ax.set_yticklabels(names, fontsize=12.5)
    ax.set_xlim(0, 105)
    ax.set_xticks([])
    style_axes(ax, value_axis=True)
    ax.set_title("Words per part of a 150-word HireVue answer", loc="left", pad=36, color=BLACK)
    ax.spines["bottom"].set_visible(False)
    ax.text(0, 1.03, "150 words in all, about 70 to 90 seconds at a normal speaking pace", transform=ax.transAxes,
            ha="left", va="bottom", fontsize=11.5, color=BLACK)
    add_source(fig, "WSG analysis of the answer plan in this article")
    save_figure(fig, OUT / "04-answer-word-budget.png")
    add("04-answer-word-budget.png",
        "Horizontal bar chart of a 150-word answer split into situation 25, task 15, action 85 and result 25 words",
        "The action gets around 85 of the 150 words; situation, task and result share the other 65.",
        "WSG analysis of the answer plan in this article",
        "Bar chart drawn in matplotlib from the section 5 word budget (25, 15, 85, 25 words; 150 total; about 70 to 90 seconds)",
        anchor_for("Here's what 150 words looks like"))


# ---------------------------------------------------------------- 05 setup diagram
def image_05():
    s6 = section(6)
    must(r"The recording is 480p", s6)
    must(r"light source in front of you", s6)
    must(r"near the top center of your screen", s6)
    must(r"level with your eyes", s6)
    must(r"a stack of books under it", s6)
    must(r"quiet, distraction free area", s6)
    must(r"looking at your webcam while speaking", s6)
    W, H = 11.0, 6.3
    fig, ax = canvas(W, H, title="Recording setup: light in front, camera window top center, lens at eye level", title_size=16)
    # ---- left panel: side view
    label(ax, 0.35, H - 0.85, "Side view", size=12.5, bold=True, color=BLACK)
    base_y = 1.45
    ax.plot([0.4, 5.2], [base_y, base_y], color=BLACK, lw=1.2)                      # desk
    label(ax, 5.25, base_y - 0.06, "Desk", size=10.5, color=BLACK, ha="left", va="top")
    # books and laptop
    for i in range(3):
        ax.add_patch(Rectangle((2.55, base_y + i * 0.17), 1.1, 0.15, facecolor=LIGHT_BLUE, edgecolor="white", lw=0.8))
    lap_y = base_y + 0.51
    ax.add_patch(Rectangle((2.45, lap_y), 1.3, 0.08, facecolor=GRAY, edgecolor=GRAY))                  # keyboard base
    ax.add_patch(Polygon([(3.65, lap_y + 0.08), (3.75, lap_y + 0.08), (3.45, lap_y + 1.55), (3.35, lap_y + 1.55)],
                         closed=True, facecolor=NAVY, edgecolor=NAVY))                                   # screen, slight tilt
    lens = (3.4, lap_y + 1.5)
    ax.add_patch(Circle(lens, 0.06, facecolor="white", edgecolor=BLACK, lw=1.0, zorder=5))
    # person
    head = (4.75, lap_y + 1.5)
    ax.add_patch(Circle(head, 0.32, facecolor=PALE, edgecolor=BLACK, lw=1.0))
    ax.plot([head[0], head[0]], [head[1] - 0.32, base_y], color=BLACK, lw=1.0)
    # eye line
    ax.plot([lens[0] + 0.08, head[0] - 0.34], [lens[1], lens[1]], color=BLACK, lw=0.9, ls=(0, (3, 3)))
    label(ax, head[0] + 0.42, lens[1], "Lens level\nwith your eyes", size=10.5, color=BLACK, ha="left", va="center", linespacing=1.15)
    label(ax, 2.4, base_y + 0.26, "Books under\nthe laptop", size=10.5, color=BLACK, ha="right", va="center", linespacing=1.15)
    # lamp in front, slightly above the lens
    lamp = (1.3, lap_y + 2.0)
    ax.plot([lamp[0], lamp[0]], [base_y, lamp[1] - 0.05], color=BLACK, lw=1.2)
    ax.add_patch(Polygon([(lamp[0] - 0.3, lamp[1]), (lamp[0] + 0.3, lamp[1]), (lamp[0] + 0.15, lamp[1] + 0.3), (lamp[0] - 0.15, lamp[1] + 0.3)],
                         closed=True, facecolor=MID_BLUE, edgecolor=MID_BLUE))
    for dy in (-0.15, 0.0, 0.15):
        ax.annotate("", xy=(head[0] - 0.45, head[1] + 0.25 + dy * 1.5), xytext=(lamp[0] + 0.32, lamp[1] + 0.05 + dy),
                    arrowprops=dict(arrowstyle="-", color=MID_BLUE, lw=0.9, ls=(0, (2, 3)), shrinkA=0, shrinkB=0))
    label(ax, lamp[0], lamp[1] + 0.42, "Lamp or window in front of you,\na little above the lens", size=10.5, color=BLACK,
          ha="center", va="bottom", linespacing=1.15)
    # the wrong place for a window
    label(ax, 5.15, lap_y + 0.5, "No window\nbehind you", size=10.5, color=BLACK, ha="left", va="center", linespacing=1.15)
    ax.plot([5.3, 5.3], [base_y + 0.1, base_y + 0.85], color=GRAY, lw=1.2, ls=(0, (3, 3)))
    # ---- right panel: the screen
    label(ax, 6.6, H - 0.85, "Your screen", size=12.5, bold=True, color=BLACK)
    sx, sy, sw, sh = 6.6, 1.45, 4.0, 3.1
    ax.add_patch(Rectangle((sx, sy), sw, sh, facecolor=PALE, edgecolor=GRAY, lw=0.8))
    ax.add_patch(Circle((sx + sw / 2, sy + sh + 0.12), 0.06, facecolor="white", edgecolor=BLACK, lw=1.0, zorder=5))
    label(ax, sx + sw / 2 + 0.14, sy + sh + 0.12, "Lens", size=10, color=BLACK, va="center")
    cw, ch = 1.5, 1.0
    ax.add_patch(Rectangle((sx + sw / 2 - cw / 2, sy + sh - 0.18 - ch), cw, ch, facecolor=NAVY, edgecolor=NAVY))
    label(ax, sx + sw / 2, sy + sh - 0.18 - ch / 2, "Camera window\nnear the top center", size=10, color="white", ha="center", va="center", linespacing=1.15)
    label(ax, sx + sw / 2, sy + sh - 0.18 - ch - 0.22, "Question text sits close to the lens, so your eyes travel less",
          size=10, color=BLACK, ha="center", va="top", wrap_in=sw - 0.4, linespacing=1.15)
    label(ax, sx + 0.15, sy + 0.5, "Look at the lens while you talk, not at your own face",
          size=10, color=BLACK, ha="left", va="center", wrap_in=sw - 0.3, linespacing=1.15)
    # the three room notes along the bottom
    notes = ["Quiet room, door closed", "Recording is 480p: light and framing do the work", "Everything else closed, charger in, wired or next to the router"]
    for xn, note in zip((0.35, 2.9, 6.6), notes):
        label(ax, xn, 0.98, note, size=10, color=BLACK, va="center")
    ax.text(0.35, 0.55, "Source: HireVue interview tips page and candidate FAQ, October 2026", ha="left", va="top", fontsize=10, color=BLACK)
    finish(fig, OUT / "05-recording-setup.png")
    add("05-recording-setup.png",
        "Diagram of a HireVue recording setup: lamp in front, laptop on books, lens at eye level, camera window top center",
        "Light in front, camera window at the top center of the screen, lens level with your eyes, quiet room.",
        "HireVue interview tips page and candidate FAQ, October 2026",
        "Setup diagram drawn in matplotlib from the section 6 rules (light in front, camera window near the top center, lens at eye level, quiet room, 480p)",
        anchor_for("**Put your light in front of you"))


# ---------------------------------------------------------------- 06 invitation to next step
def image_06():
    s7 = section(7)
    must(r"invitation arrives about a week after you apply, you get about a week to complete it", s7)
    must(r"a response comes in about two weeks", s7)
    must(r"can arrive within hours of applying \(one September 2026 Glassdoor report said two to three hours\), you get seven days", s7)
    must(r"superday invitations have followed about two weeks after recording", s7)
    W, H = 11.0, 5.0
    fig, ax = canvas(W, H, title="Goldman and JPMorgan: from application to the next step, as reported", title_size=16)
    x0, x1, ya = 2.3, W - 0.4, 1.45
    weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]
    step = (x1 - x0) / len(weeks)     # same geometry as wsg_diagrams.month_axis, drawn in black
    ax.plot([x0, x1], [ya, ya], color=BLACK, lw=1.2, zorder=2)
    for i, m in enumerate(weeks + [""]):
        xa = x0 + i * step
        ax.plot([xa, xa], [ya - 0.06, ya + 0.06], color=BLACK, lw=1.0, zorder=2)
        if m:
            ax.text(xa + step / 2, ya - 0.14, m, ha="center", va="top", fontsize=11, color=BLACK)
    label(ax, 0.35, ya - 0.14, "Weeks after\nyou apply", size=10.5, color=BLACK, va="top", linespacing=1.15)

    def wx(w, frac=0.0):
        return month_x(x0, step, w, frac)

    lanes = {"Goldman Sachs": H - 1.5, "JPMorgan": H - 2.6}
    for name, y in lanes.items():
        label(ax, 0.35, y, name, size=12.5, bold=True, color=BLACK, va="center")
    # Goldman: invite about a week after applying, about a week to complete, response about two weeks later
    yg = lanes["Goldman Sachs"]
    ax.plot([wx(0), wx(1)], [yg, yg], color=LIGHT_BLUE, lw=10, solid_capstyle="butt")
    ax.plot([wx(1), wx(2)], [yg, yg], color=NAVY, lw=10, solid_capstyle="butt")
    ax.plot([wx(2), wx(4)], [yg, yg], color=GRAY, lw=10, solid_capstyle="butt")
    ax.plot([wx(1)], [yg], marker="D", ms=9, color=BLACK, zorder=4)
    label(ax, wx(0, 0.5), yg + 0.2, "Invitation about a\nweek after applying", size=10.5, color=BLACK, ha="center", va="bottom", linespacing=1.15)
    label(ax, wx(1, 0.5), yg - 0.2, "About a week\nto complete", size=10.5, color=BLACK, ha="center", va="top", linespacing=1.15)
    label(ax, wx(3, 0.0), yg + 0.2, "Response in about two weeks\n(recruiters, 2018)", size=10.5, color=BLACK, ha="center", va="bottom", linespacing=1.15)
    # JPMorgan: invite within hours, seven days, superday invite about two weeks after recording
    yj = lanes["JPMorgan"]
    ax.plot([wx(0), wx(1)], [yj, yj], color=NAVY, lw=10, solid_capstyle="butt")
    ax.plot([wx(1), wx(3)], [yj, yj], color=GRAY, lw=10, solid_capstyle="butt")
    ax.plot([wx(0, 0.02)], [yj], marker="D", ms=9, color=BLACK, zorder=4)
    label(ax, wx(0, 0.02) - 0.08, yj + 0.2, "Invitation within hours\n(one report: 2 to 3 hours)", size=10.5, color=BLACK, ha="left", va="bottom", linespacing=1.15)
    label(ax, wx(0, 0.5), yj - 0.2, "7 days to complete", size=10.5, color=BLACK, ha="center", va="top", linespacing=1.15)
    label(ax, wx(2, 0.0), yj + 0.2, "Superday invitation about\ntwo weeks after recording", size=10.5, color=BLACK, ha="center", va="bottom", linespacing=1.15)
    # legend
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], marker="D", color=BLACK, lw=0, ms=8, label="Invitation arrives"),
                       Line2D([0], [0], color=LIGHT_BLUE, lw=8, label="Waiting for the invitation"),
                       Line2D([0], [0], color=NAVY, lw=8, label="Window to record"),
                       Line2D([0], [0], color=GRAY, lw=8, label="Waiting for the bank's answer")],
              loc="lower left", bbox_to_anchor=(0.02, 0.1), ncol=4, frameon=False, fontsize=10.5)
    ax.text(0.35, 0.38, "Source: eFinancialCareers and Glassdoor, candidate-reported HireVue timing, October 2026",
            ha="left", va="top", fontsize=10, color=BLACK)
    finish(fig, OUT / "06-invitation-to-next-step.png")
    add("06-invitation-to-next-step.png",
        "Timeline of Goldman and JPMorgan HireVue timing from application through the recording window to the next step",
        "A JPMorgan link can arrive within hours of applying; Goldman's takes about a week.",
        "eFinancialCareers and Glassdoor, candidate-reported HireVue timing, October 2026",
        "Timeline drawn in matplotlib from the section 7 timing list (Goldman: invite about a week, about a week to complete, response about two weeks; JPMorgan: invite within hours, 7 days, superday invite about two weeks after recording); reported timing, not firm-published",
        anchor_for("**Goldman's invitation usually arrives"))


# ---------------------------------------------------------------- manifest checks
def check_manifest():
    from PIL import Image
    bad = tuple(chr(c) for c in (0x2014, 0x2013, 0x2212))   # em dash, en dash, Unicode minus
    for e in entries:
        for k, v in e.items():
            assert not any(ch in v for ch in bad), f"dash in manifest {e['file']} {k}"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
        assert len(e["caption"].split()) < 20, f"caption of {e['file']} is {len(e['caption'].split())} words"
        assert e["source"], f"{e['file']} has no source"
        hits = [l for l in LINES if l.strip().startswith(e["anchor"])]
        assert len(hits) == 1, f"anchor for {e['file']} matches {len(hits)} draft lines: {e['anchor']!r}"
        im = Image.open(OUT / e["file"])
        assert im.width <= 2200, f"{e['file']} is {im.width} px wide"
    # no dashes in any string drawn on the images either
    src = Path(__file__).read_text(encoding="utf-8")
    assert not any(ch in src for ch in bad), "dash character in the build script"


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    image_01_02()
    image_03()
    image_04()
    image_05()
    image_06()
    check_manifest()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT.relative_to(ROOT)}")
