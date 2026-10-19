#!/usr/bin/env python3
"""Images for drafts/draft-accenture-strategy-analyst-career-guide-v3.md (October 11, 2026; v2 October 12; v3 October 14, 2026).

Run from the repo root:  python3 scripts/images/build_accenture-strategy-analyst-career-guide.py
Idempotent: rewrites every PNG in published/assets/images/accenture-strategy-analyst-career-guide/
and the folder's manifest.json. The draft is never edited; the coordinator inserts the image lines
from the manifest anchors with scripts/images/insert_images.py.

Every name, date and figure is hard-coded here and asserted against the draft text with a regex
before anything is drawn, so a QA edit that moves a number stops the build. The case arithmetic
is also recomputed (21% of $3.6B, 5% of $800M, the $796M check, 20% and about 18% share).
The v3 draft keeps a one-page version of the case with every figure the tree shows.

Banking format throughout (images.md, October 7 and 8, 2026): black Arial text, no gridlines, no
boxes or frames on charts, direct data labels, navy for Accenture Strategy and gray for the
comparison group, a source line in the bottom-left of every image.

Images:
  01  (removed October 12, 2026: the org diagram illustrated the Reinvention Services history cut in v2)
  02  (removed October 14, 2026: the pay-by-level section was cut to keep the guide at the Analyst level)
  03  recruiting calendar for a junior, October 2026 to fall 2028                        (dated)
  04  issue tree of the kitchen cabinet case with the segment numbers
  05  (removed October 14, 2026: the table image repeated the markdown comparison table)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import *          # noqa: E402,F401,F403
from wsg_diagrams import *     # noqa: E402,F401,F403

import matplotlib  # noqa: E402
matplotlib.rcParams["text.parse_math"] = False      # "$100,000" is never mathtext
matplotlib.rcParams["axes.unicode_minus"] = False   # no Unicode minus signs anywhere

SLUG = "accenture-strategy-analyst-career-guide"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v3.md"
TEXT = DRAFT.read_text(encoding="utf-8")
LINES = TEXT.split("\n")
entries = []


# ---------------------------------------------------------------- helpers
def in_draft(pattern, what):
    """Stop the build if the draft no longer says what the image says."""
    if re.search(pattern, TEXT) is None:
        print(f"DRAFT MISMATCH: {what}\n  pattern: {pattern}")
        sys.exit(1)


def add(file, alt, caption, source, method, anchor, dated):
    entries.append({"file": file, "alt": alt, "caption": caption, "source": source, "method": method,
                    "anchor": anchor, "regenerate_at_publish": dated})


def assert_fits(fig, width_in, name):
    """The tight bounding box must stay inside the canvas, or finish() shrinks the whole picture to fit."""
    fig.canvas.draw()
    bb = fig.get_tightbbox(fig.canvas.get_renderer())
    assert bb.x0 >= -0.05 and bb.x1 <= width_in + 0.05, f"{name}: content spans {bb.x0:.2f} to {bb.x1:.2f} in on a {width_in} in canvas"


def n_lines(text, width_in, size, bold=False):
    return wrap(text, width_in, size, bold).count("\n") + 1


def canvas_source(fig, text, W, x_in=0.35):
    """add_source() for a diagram canvas, shifted so it lines up with the title's left edge."""
    add_source(fig, text)
    fig.texts[-1].set_x(x_in / W)


# ---------------------------------------------------------------- the draft's facts, checked
def check_draft():
    # 03 calendar
    for pat, what in [
        (r"stay up through October 16, 2026", "posting closes October 16, 2026"),
        (r"campus deadlines in October through December, interviews December through February and decisions in March and April",
         "campus deadlines, interviews and decisions"),
        (r"10-week internship that starts in June", "10-week internship from June"),
        (r"Intern in Summer 2027, June through August", "internship June through August 2027"),
        (r"return offer in August 2027", "return offer August 2027"),
        (r"should open in spring or summer 2027 with a deadline before fall", "direct full-time posting spring or summer 2027"),
        (r"Start full time in fall 2028 as an Analyst\.", "full-time start fall 2028"),
    ]:
        in_draft(pat, what)
    # 04 issue tree
    for pat, what in [
        (r"flat at about \$800 million for two years while the US market grew from \$4\.0 billion to \$4\.4 billion", "market and client revenue"),
        (r"share fell from 20 percent to about 18 percent", "share 20 to about 18 percent"),
        (r"where the \$400 million of growth went", "$400 million of growth"),
        (r"\(a product type, a channel, a customer group\)", "branch one leaves"),
        (r"on price, product or distribution", "branch two leaves"),
        (r"first branch is a structural problem and the second an execution problem", "structural and execution"),
        (r"grew from \$400 million to \$800 million, while assembled cabinets stayed flat at \$3\.6 billion", "segment sizes"),
        (r"21 percent of the assembled segment and 5 percent of ready-to-assemble", "client shares by segment"),
        (r"21 percent of \$3\.6 billion is about \$756 million, 5 percent of \$800 million is \$40 million, and the sum is \$796 million", "the check"),
    ]:
        in_draft(pat, what)
    assert round(0.21 * 3600) == 756 and round(0.05 * 800) == 40 and 756 + 40 == 796
    assert 800 / 4000 == 0.20 and round(800 / 4400 * 100) == 18 and 4400 - 4000 == 400
    print("draft checks: calendar dates and case arithmetic all match")


# ---------------------------------------------------------------- 03 recruiting calendar
def calendar():
    W, H = 11.0, 6.9
    fig, ax = canvas(W, H, title="Accenture Strategy recruiting calendar for a junior, 2026 to 2028")
    x0, x1 = 3.75, W - 0.35
    n_months = 26                      # October 2026 through November 2028
    step = (x1 - x0) / n_months
    ya = 0.95
    ax.plot([x0, x1], [ya, ya], color=BLACK, lw=1.0, zorder=2)
    quarter_labels = {0: "Oct\n2026", 3: "Jan\n2027", 6: "Apr", 9: "Jul", 12: "Oct", 15: "Jan\n2028", 18: "Apr", 21: "Jul", 24: "Oct"}
    for i in range(n_months + 1):
        tall = i in quarter_labels
        ax.plot([x0 + i * step, x0 + i * step], [ya - (0.08 if tall else 0.04), ya], color=BLACK, lw=0.8, zorder=2)
        if tall:
            for j, part in enumerate(quarter_labels[i].split("\n")):
                ax.text(x0 + i * step, ya - 0.3 - j * 0.2, part, ha="left", va="baseline", fontsize=10, color=BLACK)

    def mx(month_index, day_frac=0.0):
        return x0 + (month_index + day_frac) * step

    # (label, kind, start, end) with months counted from October 2026 = 0; a point event has end None
    rows = [
        ("Summer 2027 internship posting closes October 16, 2026", "posted", mx(0, 16 / 31), None),
        ("Campus deadlines, October to December 2026 (expected)", "expected", mx(0), mx(3)),
        ("Interviews, December 2026 to February 2027 (expected)", "expected", mx(2), mx(5)),
        ("Offers, March to April 2027 (expected)", "expected", mx(5), mx(7)),
        ("Direct full-time posting for the Class of 2028, spring to summer 2027 (expected)", "expected", mx(5), mx(11)),
        ("Internship, 10 weeks, June to August 2027", "posted", mx(8), mx(11)),
        ("Return offer, August 2027", "posted", mx(10, 0.5), None),
        ("Full-time start as an Analyst, fall 2028", "posted", mx(23), mx(26)),
    ]
    y = H - 1.1
    row_gap = 0.6
    for text, kind, s, e in rows:
        col = NAVY if kind == "posted" else GRAY
        label(ax, 0.35, y, text, size=10.5, ha="left", va="center", wrap_in=3.2, color=BLACK)
        if e is None:
            ax.plot([s], [y], marker="D", ms=9, color=col, zorder=4)
        else:
            ax.plot([s, e], [y, y], color=col, lw=9, solid_capstyle="butt", zorder=3)
        y -= row_gap
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], color=NAVY, lw=8, label="Dates on Accenture's postings"),
                       Line2D([0], [0], color=GRAY, lw=8, label="Expected, from past cycles")],
              loc="lower left", bbox_to_anchor=(0.33, 0.0), ncol=2, frameon=False, fontsize=10.5, labelcolor=BLACK)
    canvas_source(fig, "Source: Accenture careers postings, October 2026, and WSG analysis", W)
    assert_fits(fig, W, "03-recruiting-calendar.png")
    finish(fig, OUT / "03-recruiting-calendar.png")
    add("03-recruiting-calendar.png",
        "Timeline from October 2026 to fall 2028 of Accenture Strategy application, interviews, offers, internship and full-time start",
        "Applications for the Summer 2027 internship close October 16, 2026.",
        "Source: Accenture careers postings, October 2026, and WSG analysis",
        "Timeline drawn in matplotlib from the four-step calendar and the interview-stage paragraph in the draft; windows tagged [VERIFY] there are shown as expected",
        "4. Start full time in fall 2028 as an Analyst.", True)


# ---------------------------------------------------------------- 04 issue tree
def issue_tree_image():
    root = N("Share fell from 20% to about 18%: market $4.0B to $4.4B, client flat at $800M", [
        N("Did the $400M of growth land where the client doesn't sell? (structural)", [
            N("Product type", [
                N("Ready-to-assemble: grew from $400M to $800M; client share 5%, or $40M"),
                N("Assembled: flat at $3.6B; client share 21%, or $756M"),
            ]),
            N("Channel"),
            N("Customer group"),
        ]),
        N("Is the client losing in the segments it serves? (execution)", [
            N("Price"),
            N("Product"),
            N("Distribution"),
        ]),
    ])
    col_w = [2.15, 2.35, 2.0, 2.9]
    opts = dict(col_w=col_w, sizes=(12.5, 11.5, 11, 10.5), gaps=(0.0, 0.5, 0.16, 0.12), min_h=(0.9, 0.62, 0.5, 0.46),
                col_gap=0.4, x0=0.35)
    tw, th = tree_extent(root, **opts)
    W = max(11.0, tw)
    H = th + 2.0
    fig, ax = canvas(W, H, title="Issue tree for the kitchen cabinet case")
    fills = [(NAVY, "white", None), (PALE_BLUE, BLACK, None), (PALE_GRAY, BLACK, None), ("white", BLACK, LINE)]
    y_end = nested_tree(ax, root, y_top=H - 1.05, fills=fills, center_depth=1,
                        col_labels=["The question", "Two branches", "Where to look", "The numbers"], **opts)
    label(ax, 0.35, y_end - 0.35, "Check: 21% of $3.6B is $756M, 5% of $800M is $40M, and $756M + $40M = $796M, about the client's $800M.",
          size=10.5, ha="left", va="top", color=BLACK)
    label(ax, 0.35, y_end - 0.62, "Finding: all $400M of the market's growth came from ready-to-assemble.", size=10.5, ha="left", va="top",
          color=BLACK, bold=True)
    canvas_source(fig, "Source: WSG analysis of the worked case in this article", W)
    assert_fits(fig, W, "04-case-issue-tree.png")
    finish(fig, OUT / "04-case-issue-tree.png")
    add("04-case-issue-tree.png",
        "Issue tree with a structural branch and an execution branch for the cabinet maker's lost market share",
        "All $400 million of the market's growth came from ready-to-assemble cabinets, where the client has 5 percent share.",
        "Source: WSG analysis of the worked case in this article",
        "Tree drawn with wsg_diagrams.nested_tree from the issue-tree and segment paragraphs of the worked case in the draft; the segment arithmetic is recomputed and asserted in this script",
        "The interviewer tells you ready-to-assemble cabinets, the fl", False)


# ---------------------------------------------------------------- manifest checks
def strip_metadata():
    """Resave every PNG through Pillow with no text chunks: white RGB, 200 dpi, nothing else."""
    from PIL import Image
    for e in entries:
        p = OUT / e["file"]
        im = Image.open(p).convert("RGB")
        im.save(p, "PNG", optimize=True, dpi=(PNG_DPI, PNG_DPI))


def check_manifest():
    from PIL import Image
    for e in entries:
        for k in ("alt", "caption", "source", "method", "anchor"):
            for ch in (chr(0x2014), chr(0x2013), chr(0x2212)):   # em dash, en dash, Unicode minus
                assert ch not in e[k], f"dash in manifest {e['file']} {k}"
        assert e["source"].startswith("Source:"), f"source line of {e['file']} must start with 'Source:'"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
        assert len(e["caption"].split()) <= 20, f"caption of {e['file']} is over 20 words"
        assert len(e["anchor"]) <= 60
        hits = [l for l in LINES if l.strip().startswith(e["anchor"])]
        assert len(hits) == 1, f"anchor for {e['file']} matches {len(hits)} draft lines: {e['anchor']!r}"
        im = Image.open(OUT / e["file"])
        assert im.width <= 2200, f"{e['file']} is {im.width} px wide"
        leftover = set(im.info) - {"dpi"}
        assert not leftover, f"{e['file']} still carries metadata: {leftover}"
    for png in OUT.glob("*.png"):
        assert any(png.name == e["file"] for e in entries), f"stray file {png.name} in the output folder"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    check_draft()
    calendar()
    issue_tree_image()
    entries.sort(key=lambda e: e["file"])
    strip_metadata()
    check_manifest()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
