#!/usr/bin/env python3
"""Images for drafts/draft-star-method-finance-interviews-v2.md (October 11, 2026; v2 October 14, 2026).

Run from the repo root:  python3 scripts/images/build_star-method-finance-interviews.py
Idempotent: rewrites every PNG in published/assets/images/star-method-finance-interviews/
and the folder's manifest.json. The draft is never edited; the coordinator inserts the image
lines from the manifest anchors with scripts/images/insert_images.py.

Every number and every quoted word comes from the draft and is asserted against it before
rendering, so a later edit to the draft fails this build loudly:

  01-star-time-split.png          MIT's 20/10/60/10 split of a 90-second answer (18/9/54/9 seconds)
  (02 interview validity and 03 story matrix were cut in v2, October 14 fix plan)
  04-star-answer-marked-up.png    worked answer 1 with S, T, A, R marked and word counts
  05-hirevue-clock.png            one HireVue question: appears, 30 seconds prep, up to 2 minutes, submit
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
from matplotlib.patches import FancyBboxPatch  # noqa: E402

SLUG = "star-method-finance-interviews"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v2.md"
TEXT = DRAFT.read_text(encoding="utf-8")
LINES = TEXT.split("\n")
entries = []


def add(file, alt, caption, source, method, anchor):
    entries.append({"file": file, "alt": alt, "caption": caption, "source": source, "method": method, "anchor": anchor})


def must(pattern, what):
    """The draft must contain this exact phrase (regex); returns the match."""
    m = re.search(pattern, TEXT)
    assert m, f"draft no longer says {what!r} (pattern {pattern!r})"
    return m


def anchor_for(prefix):
    """The first 60 characters of the one draft line that starts with prefix."""
    hits = [l for l in LINES if l.strip().startswith(prefix)]
    assert len(hits) == 1, f"anchor {prefix!r} matches {len(hits)} draft lines"
    return hits[0].strip()[:60]


def assert_fits(fig, width_in, name):
    fig.canvas.draw()
    bb = fig.get_tightbbox(fig.canvas.get_renderer())
    assert bb.x0 >= -0.05 and bb.x1 <= width_in + 0.05, f"{name}: content spans {bb.x0:.2f} to {bb.x1:.2f} in on a {width_in} in canvas"


# ---------------------------------------------------------------- 01 the 90-second split
def time_split():
    must(r"Situation 20 percent, Task 10 percent, Action 60 percent and Result 10 percent", "MIT's 20/10/60/10 split")
    must(r"in a 90-second answer the Action gets 54 seconds", "Action gets 54 seconds")
    must(r"The Situation gets about 18 seconds", "Situation 18 seconds")
    must(r"The Task gets about 9 seconds", "Task 9 seconds")
    must(r"The Action gets about 54 seconds", "Action 54 seconds")
    must(r"The Result gets about 9 seconds", "Result 9 seconds")
    parts = [("Situation", 20), ("Task", 10), ("Action", 60), ("Result", 10)]
    secs = {p: round(90 * pct / 100) for p, pct in parts}
    assert secs == {"Situation": 18, "Task": 9, "Action": 54, "Result": 9}, secs
    assert sum(secs.values()) == 90

    fig, ax = new_figure(width=11.0, height=5.0)
    ys = list(range(len(parts)))[::-1]
    for y, (p, pct) in zip(ys, parts):
        color = NAVY if p == "Action" else GRAY
        ax.barh(y, pct, height=0.56, color=color, zorder=3)
        ax.text(pct + 1.2, y, f"{pct}%  ({secs[p]} seconds)", ha="left", va="center", fontsize=13, color=BLACK)
    ax.set_xlim(0, 80)
    ax.set_xticks([])
    style_axes(ax, title="Time split of a 90-second STAR answer")
    ax.set_yticks(ys)
    ax.set_yticklabels([p for p, _ in parts], fontsize=13)
    ax.spines["bottom"].set_visible(False)
    ax.axvline(0, color=BLACK, lw=0.8, zorder=2)
    add_source(fig, "Source: MIT Career Advising and Professional Development, The STAR Method for Behavioral Interviews.")
    save_figure(fig, OUT / "01-star-time-split.png")
    add("01-star-time-split.png",
        "Bar chart splitting a 90-second STAR answer: Situation 18 seconds, Task 9, Action 54, Result 9.",
        "The Action gets 60 percent of the answer, about 54 seconds of 90.",
        "MIT Career Advising and Professional Development, The STAR Method for Behavioral Interviews; seconds are WSG's arithmetic on a 90-second answer",
        "Horizontal bars drawn from the MIT 20/10/60/10 split quoted in the draft; seconds are the split applied to the draft's 90-second answer",
        anchor_for("Here's what each part is for, and about how long it gets"))


# ---------------------------------------------------------------- 04 worked answer 1, marked up
def marked_answer():
    i = next(k for k, l in enumerate(LINES) if l.startswith("### Tell me about a time you failed and how you overcame it"))
    ans = next(l for l in LINES[i + 1:] if l.strip()).strip()
    assert ans.startswith('"') and ans.endswith('"'), "worked answer 1 is not a quoted paragraph"
    ans = ans.strip('"')
    cuts = ["My job on the team was the model", "I went back to the last three 10-Ks", "The corrected model cut our price target"]
    idx = [ans.index(c) for c in cuts]
    parts = [("S", "Situation", ans[:idx[0]].strip()), ("T", "Task", ans[idx[0]:idx[1]].strip()),
             ("A", "Action", ans[idx[1]:idx[2]].strip()), ("R", "Result", ans[idx[2]:].strip())]
    counts = {name: len(t.split()) for _, name, t in parts}
    total = sum(counts.values())
    must(r"Each one runs 150 to 190 words", "150 to 190 words")
    assert 150 <= total <= 190 and abs(total - 180) <= 10, f"worked answer 1 runs {total} words"
    # the section 2 snippets must still be the opening of each part
    must(re.escape("Last spring I was one of four analysts on a pitch team"), "Situation snippet")
    must(re.escape("My job on the team was the model, so the error was mine to find."), "Task snippet")
    must(re.escape("I went back to the last three 10-Ks and rebuilt revenue by segment"), "Action snippet")
    must(re.escape("The corrected model cut our price target by 11 percent"), "Result snippet")

    W = 11.0
    size, text_x, text_w = 11.5, 2.2, W - 2.2 - 0.35
    blocks = []
    for letter, name, t in parts:
        wrapped = wrap(t, text_w, size)
        n = wrapped.count("\n") + 1
        blocks.append((letter, name, wrapped, max(n * size * 1.3 / 72 + 0.3, 0.78)))
    H = 1.05 + sum(b[3] for b in blocks) + 0.12 * (len(blocks) - 1) + 0.65
    fig, ax = canvas(W, H, title=f"Worked answer 1, marked up by part ({total} words)")
    y = H - 0.95
    for letter, name, wrapped, h in blocks:
        fill = NAVY if name == "Action" else MID_BLUE
        text_box(ax, 0.3, y - 0.62, 0.62, 0.62, letter, fill=fill, text_color="white", size=18, bold=True, radius=0.06)
        label(ax, 1.05, y - 0.2, name, size=12, bold=True, ha="left", va="center")
        label(ax, 1.05, y - 0.45, f"{counts[name]} words", size=10.5, ha="left", va="center")
        label(ax, text_x, y - 0.08, wrapped, size=size, ha="left", va="top", linespacing=1.3)
        y -= h + 0.12
    label(ax, 0.3, y - 0.1, "Source: WSG analysis of the worked example in this article.", size=10, ha="left", va="top")
    assert_fits(fig, W, "04-star-answer-marked-up.png")
    finish(fig, OUT / "04-star-answer-marked-up.png")
    add("04-star-answer-marked-up.png",
        "The first worked answer with its Situation, Task, Action and Result marked and word counts per part.",
        f"The Action runs {counts['Action']} of the answer's {total} words, the Situation {counts['Situation']}.",
        "WSG analysis of the worked example in this article",
        "Text graphic of worked answer 1 copied verbatim from the draft, split at the Task, Action and Result sentences; word counts computed in the script",
        anchor_for('"Last spring I was one of four analysts on a pitch team'))
    return counts, total


# ---------------------------------------------------------------- 05 one HireVue question
def hirevue_clock():
    must(r"about 30 seconds to prepare and up to about two minutes to answer", "30 seconds prep, two-minute answer")
    must(r"before a two-minute cutoff", "two-minute cutoff")
    must(r"At 150 words you'll finish around 90 seconds", "150 words is about 90 seconds")
    must(r"The answer submits when the clock runs out or when you click", "submit rule")
    must(r"click the done button", "done button")
    steps = [("Question appears on screen", "One question at a time"),
             ("30 seconds to prepare", "Write four words: setting, task, first action, number"),
             ("Record, up to 2 minutes", "150 words runs about 90 seconds"),
             ("Answer submits", "When you click done or the clock runs out")]
    W, H = 11.0, 4.9
    fig, ax = canvas(W, H, title="One HireVue question, step by step")
    bw, bh, gap, x = 2.35, 0.95, 0.35, 0.3
    y_box = H - 2.0
    for k, (head, sub) in enumerate(steps):
        fill = NAVY if k == 2 else MID_BLUE
        text_box(ax, x, y_box, bw, bh, head, fill=fill, text_color="white", size=12.5, bold=True, radius=0.06)
        label(ax, x + bw / 2, y_box - 0.18, sub, size=10.5, ha="center", va="top", wrap_in=bw - 0.05, linespacing=1.22)
        if k < len(steps) - 1:
            arrow(ax, (x + bw + 0.04, y_box + bh / 2), (x + bw + gap - 0.04, y_box + bh / 2), color=BLACK, lw=1.6)
        x += bw + gap
    # the recording clock under the boxes: 0 to 120 seconds, with 90 marked
    x0, x1, ya = 0.3, W - 0.3, 0.95
    ax.plot([x0, x1], [ya, ya], color=BLACK, lw=1.2)
    for s, text in [(0, "0:00 start"), (90, "1:30, about 150 words"), (120, "2:00 cutoff")]:
        xs = x0 + (x1 - x0) * s / 120
        ax.plot([xs, xs], [ya - 0.07, ya + 0.07], color=BLACK, lw=1.2)
        label(ax, xs, ya - 0.14, text, size=10.5, ha="center" if 0 < s < 120 else ("left" if s == 0 else "right"), va="top")
    ax.plot([x0, x0 + (x1 - x0) * 90 / 120], [ya + 0.22, ya + 0.22], color=NAVY, lw=7, solid_capstyle="butt")
    ax.plot([x0 + (x1 - x0) * 90 / 120, x1], [ya + 0.22, ya + 0.22], color=LIGHT_BLUE, lw=7, solid_capstyle="butt")
    label(ax, x0, ya + 0.72, "The recording clock on step 3", size=11, bold=True, ha="left", va="bottom")
    label(ax, x0 + (x1 - x0) * 45 / 120, ya + 0.42, "Talking, at the pace you practiced", size=10.5, ha="center", va="bottom")
    label(ax, x0 + (x1 - x0) * 105 / 120, ya + 0.42, "Cushion", size=10.5, ha="center", va="bottom")
    label(ax, 0.3, 0.42, "Source: IGotAnOffer and Mergers & Inquisitions HireVue interview guides, 2026.",
          size=10, ha="left", va="top")
    assert_fits(fig, W, "05-hirevue-clock.png")
    finish(fig, OUT / "05-hirevue-clock.png")
    add("05-hirevue-clock.png",
        "Four-step sequence of a HireVue question: question appears, 30 seconds to prepare, record up to two minutes, submit.",
        "Each question gives about 30 seconds to prepare and up to two minutes to record.",
        "IGotAnOffer and Mergers & Inquisitions HireVue interview guides, 2026",
        "Sequence diagram drawn from the HireVue settings in section 4 of the draft (30 seconds of prep, a two-minute cutoff, 150 words in about 90 seconds, submit on click or at the cutoff)",
        anchor_for("At Goldman Sachs and JPMorgan, the first round is a recorded"))


# ---------------------------------------------------------------- manifest checks
def check_manifest():
    from PIL import Image
    for e in entries:
        for k in ("alt", "caption", "source", "method", "anchor"):
            for ch in (chr(0x2014), chr(0x2013), chr(0x2212)):
                assert ch not in e[k], f"dash in manifest {e['file']} {k}"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
        assert len(e["caption"].split()) < 20, f"caption of {e['file']} is {len(e['caption'].split())} words"
        hits = [l for l in LINES if l.strip().startswith(e["anchor"])]
        assert len(hits) == 1, f"anchor for {e['file']} matches {len(hits)} draft lines: {e['anchor']!r}"
        assert not hits[0].lstrip().startswith(("|", "-", ">", "*", "1.", "2.", "3.")), f"anchor for {e['file']} is a table row, list item or quote"
        im = Image.open(OUT / e["file"])
        assert im.width <= 2200, f"{e['file']} is {im.width} px wide"
    src = (ROOT / "scripts" / "images" / "build_star-method-finance-interviews.py").read_text(encoding="utf-8")
    for ch in (chr(0x2014), chr(0x2013), chr(0x2212)):
        assert ch not in src, "dash character in the build script"


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    time_split()
    counts, total = marked_answer()
    hirevue_clock()
    check_manifest()
    write_manifest(OUT, entries)
    print(f"worked answer 1: {counts}, {total} words")
    print(f"wrote {len(entries)} images and manifest to {OUT.relative_to(ROOT)}")
