#!/usr/bin/env python3
"""Images for drafts/draft-mckinsey-hours-honest-read-v3.md (October 11, 2026; v3 October 12, 2026).

Run from the repo root:  python3 scripts/images/build_mckinsey-hours-honest-read.py
Idempotent. Rebuilds three PNGs in the banking format (black Arial text, no gridlines, no
boxes, direct data labels, a source line bottom-left) and writes the manifest:

  01-hours-by-weekday.png          bar chart from the day-by-day table in section 1
  02-staffed-vs-between-studies.png  staffed week, week between studies, annual average (section 3)
  03-on-site-days.png              diagram: four-day on-site week vs two-or-three-day week (section 4)

v3 (October 12, 2026) removed 04-pay-per-hour (the banking pay section was cut), 05-headcount-
and-ai-agents (headcount history cut) and 06-bcg-night-off-study (the 2009 BCG study cut).
Numbering keeps its gaps.

Every number is asserted against the draft text with a regex before it is drawn; a mismatch
stops the build.

Nothing here edits the draft. The coordinator inserts the image lines with
scripts/images/insert_images.py from the manifest's anchors.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import (BANK_SERIES, BLACK, GRAY, LIGHT_BLUE, NAVY, add_source, new_figure,  # noqa: E402
                     save_figure, style_axes, write_manifest)
from wsg_diagrams import PALE_GRAY, canvas, finish, label, text_box  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.rcParams["text.parse_math"] = False      # dollar signs must never become mathtext
matplotlib.rcParams["axes.unicode_minus"] = False   # no Unicode minus anywhere

SLUG = "mckinsey-hours-honest-read"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v3.md"

SRC_TRACKERS = "Source: Hacking the Case Interview, consulting hours per week, May 2026, and StrategyCase, July 2026"

entries = []
STRINGS = []   # every string a reader sees, checked before rendering


# ---------------------------------------------------------------- helpers
def draft_text():
    return DRAFT.read_text(encoding="utf-8")


def must(text, pattern, what):
    """The draft must contain this pattern, or the image would show a number the article doesn't."""
    if not re.search(pattern, text):
        print(f"DRAFT MISMATCH ({what}): /{pattern}/ not found in {DRAFT.relative_to(ROOT)}")
        sys.exit(1)


def s(*strings):
    """Register reader-facing strings for the text checks and return them unchanged."""
    STRINGS.extend(strings)
    return strings if len(strings) > 1 else strings[0]


BANNED = ["—", "–", "−", "honest read", "notice how", "this chart", "as you can see",
          "crucial", "striking", "pivotal", "massive", "staggering", "skyrocket", "plummet", "the real story"]


def check_strings():
    for t in STRINGS:
        low = t.lower()
        for b in BANNED:
            assert b not in low, f"banned text {b!r} in image string {t!r}"


def titles(ax, title, subtitle=None):
    """Bold left-aligned title; a subtitle only when it carries the unit or the assumption."""
    ax.set_title(title, loc="left", pad=30 if subtitle else 14, color=BLACK)
    if subtitle:
        ax.text(0, 1.02, subtitle, transform=ax.transAxes, ha="left", va="bottom", fontsize=11.5, color=BLACK)


def value_labels(ax, bars, texts, fontsize=12.5, bold=False):
    for b, t in zip(bars, texts):
        ax.annotate(t, (b.get_x() + b.get_width() / 2, b.get_height()), ha="center", va="bottom",
                    xytext=(0, 4), textcoords="offset points", fontsize=fontsize, color=BLACK,
                    fontweight="bold" if bold else "normal")


def add(file, alt, caption, source, method, anchor, dated=False):
    s(alt, caption, source)
    entries.append({"file": file, "alt": alt, "caption": caption, "source": source, "method": method,
                    "anchor": anchor, "regenerate_at_publish": dated})


# ---------------------------------------------------------------- 01: hours by weekday
def chart_weekday(text):
    rows = [("Monday", "Client site or home office", 12, 14), ("Tuesday", "Client site", 12, 14),
            ("Wednesday", "Client site", 12, 14), ("Thursday", "Client site, then home", 10, 12),
            ("Friday", "Home office", 6, 8), ("Saturday and Sunday", "Off", 0, 2)]
    for day, where, lo, hi in rows:
        must(text, rf"\| {re.escape(day)} \| {re.escape(where)} \| {lo} to {hi} \|", f"table row {day}")
    must(text, r"three 13-hour days, an 11-hour day and a 7-hour day, which comes to 57", "weekday sum")
    mids = [(lo + hi) / 2 for _, _, lo, hi in rows]
    assert mids == [13, 13, 13, 11, 7, 1]
    assert sum(mids[:5]) == 57

    fig, ax = new_figure(width=11, height=5.8)
    x = list(range(len(rows)))
    bars = ax.bar(x, mids, width=0.58, color=NAVY, zorder=3)
    value_labels(ax, bars, s(*[f"{lo} to {hi}" for _, _, lo, hi in rows]))
    ax.set_xticks(x)
    ax.set_xticklabels(s("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday\nand Sunday"), fontsize=12.5)
    ax.set_ylim(0, 16.5)
    ax.set_xlim(-0.6, len(rows) - 0.4)
    style_axes(ax)
    titles(ax, s("Hours by weekday on a McKinsey client week"),
           s("Hours of work a day, evenings included; bar height is the midpoint of each range"))
    add_source(fig, SRC_TRACKERS)
    save_figure(fig, OUT / "01-hours-by-weekday.png")
    add("01-hours-by-weekday.png",
        "Bar chart of McKinsey work hours by weekday, from 12 to 14 on Monday to 0 to 2 on weekends",
        "Monday through Wednesday run 12 to 14 hours each, Thursday 10 to 12 and Friday 6 to 8.",
        SRC_TRACKERS,
        "Bar chart from the day-by-day table in section 1 (midpoint of each range plotted, range in the label)",
        "| Saturday and Sunday | Off | 0 to 2 | An hour or two of Sun")


# ---------------------------------------------------------------- 02: staffed weeks, the beach and the average
def chart_staffed_vs_beach(text):
    must(text, r"Say 44 weeks at 65 hours and 4 weeks at 42: that averages 63", "beach arithmetic")
    staffed_w, staffed_h, beach_w, beach_h = 44, 65, 4, 42
    avg = (staffed_w * staffed_h + beach_w * beach_h) / (staffed_w + beach_w)
    assert round(avg) == 63 and staffed_w + beach_w == 48

    fig, ax = new_figure(width=11, height=5.6)
    cats = s("Staffed week\n(44 weeks a year)", "Week between studies\n(4 weeks a year)", "Average over\nthe 48 weeks")
    vals = [staffed_h, beach_h, 63]
    bars = ax.bar(range(3), vals, width=0.5, color=[NAVY, NAVY, GRAY], zorder=3)
    value_labels(ax, bars, s("65 hours", "42 hours", "63 hours"))
    ax.set_xticks(range(3))
    ax.set_xticklabels(cats, fontsize=12.5)
    ax.set_ylim(0, 76)
    ax.set_xlim(-0.6, 2.6)
    style_axes(ax)
    titles(ax, s("Hours a week: staffed, between studies and the average"),
           s("Example from this article: 48 working weeks a year"))
    add_source(fig, SRC_TRACKERS)
    save_figure(fig, OUT / "02-staffed-vs-between-studies.png")
    add("02-staffed-vs-between-studies.png",
        "Bar chart of hours a week in a staffed week, a week between studies and the average over 48 weeks",
        "Forty-four weeks at 65 hours and four weeks at 42 average 63 hours a week.",
        SRC_TRACKERS,
        "Bar chart from the staffed and between-studies example in section 3 (44 weeks at 65, 4 weeks at 42, average 63)",
        "The 60-hour figure is an average across staffed and unstaff")


# ---------------------------------------------------------------- 03: four-day on-site week vs two-or-three-day week
def diagram_on_site(text):
    must(text, r"Monday through Thursday at the client and Friday at the home office", "four-day pattern")
    must(text, r"now spend 2 to 3 days on site with clients instead of the traditional 4 day travel week", "two to three days")
    must(text, r"6 to 10 hours of travel per week on top of your actual working hours", "travel hours")
    must(text, r"has given some of that back", "travel given back")
    must(text, r"the client decides\.", "client decides")

    W, H = 11, 5.45
    fig, ax = canvas(W, H, title=s("Days on site: the four-day week and the two-or-three-day week"), title_size=16)
    days = s("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    x0, bw, gap = 3.25, 1.42, 0.1
    xs = [x0 + i * (bw + gap) for i in range(5)]
    head_y = H - 0.95
    for x, d in zip(xs, days):
        label(ax, x + bw / 2, head_y, d, size=12, bold=True, ha="center", va="center")
    rows = [
        (H - 2.05, s("Four-day on-site week", "the pattern before 2020"),
         [("client", s("Client site\nTravel out")), ("client", s("Client site")), ("client", s("Client site")),
          ("client", s("Client site\nTravel home")), ("home", s("Home office"))],
         s("Travel: 6 to 10 hours a week on top of work hours")),
        (H - 3.95, s("Two-or-three-day on-site week", "most teams now"),
         [("home", s("Home office")), ("client", s("Client site")), ("client", s("Client site")),
          ("some", s("Client site\non some weeks")), ("home", s("Home office"))],
         s("Travel: some of the 6 to 10 hours come back")),
    ]
    fills = {"client": LIGHT_BLUE, "home": PALE_GRAY, "some": "#d9e5f2"}
    bh = 0.95
    for y, (name, sub), cells, note in rows:
        label(ax, 0.35, y + bh / 2 + 0.08, name, size=12.5, bold=True, ha="left", va="center", wrap_in=2.7)
        label(ax, 0.35, y + bh / 2 - 0.3, sub, size=11, ha="left", va="center", wrap_in=2.7)
        for x, (kind, t) in zip(xs, cells):
            text_box(ax, x, y, bw, bh, t, fill=fills[kind], text_color=BLACK, size=11.5, radius=0.05)
        label(ax, xs[0], y - 0.32, note, size=11.5, ha="left", va="center")
    label(ax, 0.35, 0.62, s("Which days are on site is decided by the client."), size=11, ha="left", va="center")
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=LIGHT_BLUE, label=s("Client site")), Patch(color=fills["some"], label=s("Client site on some weeks")),
                       Patch(color=PALE_GRAY, label=s("Home office"))],
              loc="lower right", bbox_to_anchor=(0.995, 0.075), ncol=3, frameon=False, fontsize=11)
    # on a diagram canvas the axes fill the figure, so the source is placed by hand, flush with the title
    label(ax, 0.35, 0.2, SRC_TRACKERS, size=10, ha="left", va="center")
    finish(fig, OUT / "03-on-site-days.png")
    add("03-on-site-days.png",
        "Diagram of two McKinsey weeks: four days at the client site against two or three, with travel hours",
        "A four-day on-site week adds 6 to 10 hours of travel on top of work hours.",
        SRC_TRACKERS,
        "Diagram drawn in matplotlib from the travel pattern and the 6 to 10 travel hours in section 4",
        "Hacking the Case Interview's May 2026 pages say teams \"now s")


# ---------------------------------------------------------------- manifest checks
def check_manifest():
    lines = [l.strip() for l in draft_text().split("\n")] if DRAFT.exists() else None
    from PIL import Image
    for e in entries:
        for k in ("alt", "caption", "source", "method", "anchor"):
            for ch in ("—", "–", "−"):
                assert ch not in e[k], f"dash in manifest {e['file']} {k}"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
        assert len(e["caption"].split()) <= 22, f"caption of {e['file']} runs long"
        assert e["source"].startswith("Source:"), f"source of {e['file']} must start with 'Source:'"
        assert len(e["anchor"]) <= 60
        im = Image.open(OUT / e["file"])
        assert im.width <= 2200, f"{e['file']} is {im.width} px wide"
        if lines is not None:
            hits = [l for l in lines if l.startswith(e["anchor"].strip())]
            if len(hits) != 1:
                print(f"  WARNING: anchor for {e['file']} matches {len(hits)} draft lines right now: {e['anchor']!r}")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    text = draft_text()
    chart_weekday(text)
    chart_staffed_vs_beach(text)
    diagram_on_site(text)
    check_strings()
    entries.sort(key=lambda e: e["file"])
    check_manifest()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
