#!/usr/bin/env python3
"""Images for drafts/draft-deloitte-strategy-and-operations-career-guide-v1.md (October 5, 2026).

Run from the repo root:  python3 scripts/images/build_deloitte-strategy-and-operations-career-guide.py
Idempotent. Steps:
  1. rebuild scripts/images/models/northline-case.xlsx (scripts/images/models/build_northline_case.py)
  2. recalculate it with LibreOffice and check every printed value against the draft's two case tables
     and the payback paragraph; the script stops on any mismatch
  3. render the three Northline screenshots, the three-stage org diagram, the pay chart and the
     recruiting calendar into published/assets/images/deloitte-strategy-and-operations-career-guide/
  4. write that folder's manifest.json (the draft is never edited; insert_images.py uses the anchors)

Every name, date and figure comes from the draft. The calendar's 2027 windows are tagged [VERIFY]
in the draft and drawn as expected, so image 06 is dated and must be regenerated at publish.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
sys.path.insert(0, str(ROOT / "scripts" / "images" / "models"))
from wsg_viz import *          # noqa: E402,F401,F403
from wsg_diagrams import *     # noqa: E402,F401,F403
import build_northline_case as model  # noqa: E402

SLUG = "deloitte-strategy-and-operations-career-guide"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v1.md"
XLSX = model.OUT_XLSX
entries = []


def assert_fits(fig, width_in, name):
    """The tight bounding box must stay inside the canvas, or finish() shrinks the whole picture to fit."""
    fig.canvas.draw()
    bb = fig.get_tightbbox(fig.canvas.get_renderer())
    assert bb.x0 >= -0.05 and bb.x1 <= width_in + 0.05, f"{name}: content spans {bb.x0:.2f} to {bb.x1:.2f} in on a {width_in} in canvas"


def add(file, alt, caption, method, anchor):
    entries.append({"file": file, "alt": alt, "caption": caption, "method": method, "anchor": anchor})


# ---------------------------------------------------------------- 1 and 2: workbook, checked against the draft
ARTICLE = {
    # the draft's first table (Step two) and the sentence under it
    "D7": 1750, "E7": 2000, "D8": 0.96, "E8": 0.88, "D9": 70, "E9": 240, "D10": 150, "E10": 150,
    "D11": 10500, "E11": 36000, "D13": 546000, "E13": 1872000, "E14": 1326000,
    # Step three paragraph: 40 trucks at 50 a week is 2,000; last year about 88 percent utilization;
    # 15 extra minutes, five days, 40 trucks is 50 truck-hours; about 100 deliveries; effective capacity about 1,900
    "D20": 2000, "E20": 2000, "D21": 0.875, "E21": 1.0, "E23": 15, "E25": 50, "E27": 100, "E28": 1900,
    # the draft's second table (Step four) and the utilization sentence (about 93 percent)
    "D33": 100, "E33": 120000, "D34": 150, "F34": 450000, "D37": 250, "E37": 120000, "F37": 450000, "D38": 2150,
    # the payback paragraph
    "D43": 80, "D44": 624000, "D45": 1248000, "D47": 798000, "D49": 678000,
}


def build_and_check():
    path, R = model.build()
    print(f"built {path.relative_to(ROOT)}")
    vals = recalc_values(XLSX)["Northline case"]
    problems = []
    for ref, want in ARTICLE.items():
        got = vals.get(ref)
        if got is None or abs(float(got) - want) > 1e-6:
            problems.append(f"{ref}: workbook {got!r} vs article {want!r}")
    if abs(vals["D39"] - 2000 / 2150) > 1e-9 or round(vals["D39"] * 100) != 93:
        problems.append(f"D39 utilization after levers {vals['D39']!r} should round to 93 percent")
    for ref, v in vals.items():
        if isinstance(v, str) and (v.startswith("#") or v.startswith("Err")):
            problems.append(f"{ref} shows {v}")
    if problems:
        print("WORKBOOK DOES NOT MATCH THE ARTICLE:")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print("workbook checks: Step two table, Step three capacity figures, Step four levers table and the payback paragraph all match the draft")
    return R


# ---------------------------------------------------------------- 3a: screenshots
def screenshots(R):
    wb = "scripts/images/models/northline-case.xlsx"
    shots = [
        ("03-northline-cost-of-lateness.png", f"B{R['s2_header']}:E{R['s2_end']}",
         "Excel screenshot of the Northline Foods late delivery cost table for last year and this year",
         "Late deliveries went from 70 a week to 240, and at $150 each the annual cost went from $546,000 to $1,872,000, about $1.3 million more.",
         "| Annual cost of late deliveries (52 weeks) | $546,000 | $1,"),
        ("04-northline-capacity-and-loading.png", f"B{R['s3_header']}:E{R['s3_end']}",
         "Excel screenshot of the Northline fleet capacity block showing utilization and deliveries lost to loading time",
         "Forty trucks at 50 deliveries a week is 2,000 of capacity, and 15 extra loading minutes a day costs about 100 deliveries a week, so effective capacity is 1,900 against demand of 2,000.",
         "**Step three, find the cause.** Structure the possible cause"),
        ("05-northline-levers-and-payback.png", f"B{R['s4_header']}:F{R['pb_end']}",
         "Excel screenshot of the two Northline levers, their costs, and the annual and year one savings",
         "The loading fix recovers 100 deliveries a week for $120,000 once, three leased trucks add 150 for $450,000 a year, and the company keeps about $798,000 a year.",
         "If on-time delivery returns to 96 percent, late deliveries f"),
    ]
    for fname, rng, alt, caption, anchor in shots:
        render_range(XLSX, "Northline case", rng, OUT / fname)
        print(f"rendered {fname}  (Northline case!{rng})")
        add(fname, alt, caption, f"Workbook {wb}, sheet Northline case, range {rng}", anchor)


# ---------------------------------------------------------------- 3b: the three-stage org diagram
def org_diagram():
    W, H = 11, 9.6
    fig, ax = canvas(W, H, title="Three reorganizations: where Deloitte's Strategy & Operations work went")
    c1, w1 = 0.3, 2.55
    c2, w2 = 3.55, 3.0
    c3, w3 = 7.4, 3.3
    head_y = H - 1.0
    heads = [(c1, w1, "Stage one, through about 2019", "Three service areas; the S&O hire was a Business Analyst"),
             (c2, w2, "Stage two, about 2019 to 2024", "Six offering portfolios; the old groups became talent groups, the skill family you belonged to"),
             (c3, w3, "Stage three, 2024 onward", "Two businesses, and the Consultative Offerings tracks on apply.deloitte.com in October 2026")]
    for x, w, h1, h2 in heads:
        label(ax, x, head_y, h1, size=13, bold=True, ha="left", va="top")
        label(ax, x, head_y - 0.32, h2, size=10.5, color=TEXT_SECONDARY, ha="left", va="top", wrap_in=w, linespacing=1.2)
    gap, size, sub_size = 0.1, 11, 9.5
    s1 = [("Strategy & Operations", "the Business Analyst hire", True), ("Technology", "the Business Technology Analyst hire; today's Technology Transformation, Enterprise Tech Strategy, AI Innovation and Infrastructure Engineering tracks", False),
          ("Human Capital", "the title carried the practice's name", False)]
    s2 = [("Strategy & Analytics", "held Monitor Deloitte; S&O growth strategy work sat here", True),
          ("Customer & Marketing", "", False),
          ("Core Business Operations", "S&O supply chain work sat here", True),
          ("Enterprise Technology & Performance", "", False),
          ("Human Capital", "", False),
          ("Mergers & Acquisitions", "later took on restructuring", False)]
    s3_biz = [("Strategy, Risk & Transactions", "the strategy and operations side; Monitor Deloitte sits here under Strategy & Transactions", True),
              ("Technology & Transformation", "", False)]
    s3_tracks = [("Enterprise Strategy", "Monitor-flavored strategy, tied to a Strategy & Transactions path", True),
                 ("Functional & Operations Strategy", "the old operations side of S&O", True),
                 ("Enterprise Tech Strategy", "", False),
                 ("Technology Transformation (Packages, Platforms & AI)", "the implementation track", False),
                 ("AI Innovation", "", False),
                 ("Infrastructure Engineering", "", False),
                 ("Cyber", "posted by Deloitte & Touche LLP", False)]

    def box_h(w, name, sub):
        n1 = wrap(name, w - 0.24, size, bold=True).count("\n") + 1
        n2 = wrap(sub, w - 0.24, sub_size).count("\n") + 1 if sub else 0
        return 0.26 + n1 * size * 1.2 / 72 + n2 * sub_size * 1.15 / 72 + (0.06 if sub else 0)

    def column(x, w, items, y_top):
        pos = {}
        y = y_top
        for name, sub, hot in items:
            h = box_h(w, name, sub)
            text_box(ax, x, y - h, w, h, "", fill=PALE_ORANGE if hot else PALE_BLUE, edge=ORANGE if hot else PALE_BLUE,
                     lw=1.4 if hot else 1.0, radius=0.06)
            name_t = wrap(name, w - 0.24, size, bold=True)
            if sub:
                sub_t = wrap(sub, w - 0.24, sub_size)
                n2 = sub_t.count("\n") + 1
                sub_h = n2 * sub_size * 1.15 / 72
                label(ax, x + w / 2, y - 0.13, name_t, size=size, bold=True, ha="center", va="top", linespacing=1.15)
                label(ax, x + w / 2, y - h + 0.1 + sub_h / 2, sub_t, size=sub_size, color=TEXT_SECONDARY, ha="center", va="center", linespacing=1.15)
            else:
                label(ax, x + w / 2, y - h / 2, name_t, size=size, bold=True, ha="center", va="center", linespacing=1.15)
            pos[name] = (x, x + w, y - h / 2)
            y -= h + gap
        return pos, y

    body_top = head_y - 0.95
    p2, y2_end = column(c2, w2, s2, body_top)
    s1_height = sum(box_h(w1, n, s) + gap for n, s, _ in s1) - gap
    s1_top = body_top - ((body_top - (y2_end + gap)) - s1_height) / 2
    p1, _ = column(c1, w1, s1, s1_top)
    p3b, y3 = column(c3, w3, s3_biz, body_top)
    label(ax, c3, y3 - 0.06, "Campus postings: \"Consultative Offerings\" plus one of these tracks", size=10, bold=True, ha="left", va="top",
          color=TEXT_SECONDARY, wrap_in=w3)
    p3t, y3_end = column(c3, w3, s3_tracks, y3 - 0.42)
    assert y3_end > 0.55, f"stage three column runs off the canvas ({y3_end:.2f})"

    def link(a, b, pa, pb, color=ORANGE, lw=2.0):
        _, x_right, y1 = pa[a]
        x_left, _, yb = pb[b]
        arrow(ax, (x_right + 0.02, y1), (x_left - 0.02, yb), color=color, lw=lw, head=16)
    link("Strategy & Operations", "Strategy & Analytics", p1, p2)
    link("Strategy & Operations", "Core Business Operations", p1, p2)
    link("Strategy & Analytics", "Strategy, Risk & Transactions", p2, p3b)
    link("Strategy & Analytics", "Enterprise Strategy", p2, p3t)
    link("Core Business Operations", "Functional & Operations Strategy", p2, p3t)
    link("Core Business Operations", "Technology Transformation (Packages, Platforms & AI)", p2, p3t, color=LINE, lw=1.4)
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(facecolor=PALE_ORANGE, edgecolor=ORANGE, label="Where the S&O work went (the draft's translation table)"),
                       Line2D([0], [0], color=ORANGE, lw=2, label="The S&O thread"),
                       Line2D([0], [0], color=LINE, lw=1.4, label="The implementation side of the old operations work")],
              loc="lower left", bbox_to_anchor=(0.01, 0.0), ncol=3, frameon=False, fontsize=10.5)
    assert_fits(fig, W, "01-three-reorganizations.png")
    finish(fig, OUT / "01-three-reorganizations.png")
    add("01-three-reorganizations.png",
        "Diagram of Deloitte Consulting's three structures since 2019 with the Strategy and Operations lineage highlighted in orange",
        "Follow the orange thread: S&O split into two portfolios in 2019, and today its work sits in the Enterprise Strategy and Functional & Operations Strategy tracks.",
        "Diagram drawn in matplotlib from the three stages, the track list and the translation table in the draft; only names the draft states appear",
        "- AI Innovation, Infrastructure Engineering, and Cyber, the ")


# ---------------------------------------------------------------- 3c: pay by track
def pay_chart():
    import numpy as np
    fig, axes = new_figure(width=11, height=5.9, ncols=2, gridspec_kw={"width_ratios": [1, 1.9]})
    fig.suptitle("Deloitte pays its strategy tracks $15,000 more, and its intern rates rank the same way",
                 x=0.01, ha="left", fontsize=15.5, fontweight="bold", color=TEXT_PRIMARY)
    muted = TEXT_MUTED
    ax = axes[0]
    labels = ["Strategy tracks\n(Enterprise Strategy,\nFunctional & Operations\nStrategy, Enterprise\nTech Strategy)", "Technology\nTransformation\n(Packages,\nPlatforms & AI)"]
    vals = [105000, 90000]
    bars = ax.bar(range(2), vals, width=0.55, color=[BLUE, muted], zorder=3)
    for b in bars:
        ax.annotate("${:,.0f}\nbase estimate".format(b.get_height()), (b.get_x() + b.get_width() / 2, b.get_height()), ha="center",
                    va="bottom", xytext=(0, 4), textcoords="offset points", fontsize=11.5, color=TEXT_PRIMARY, linespacing=1.15)
    style_axes(ax, title="Full-time Analyst base, as posted")
    ax.title.set_fontsize(13)
    ax.set_xticks(range(2))
    ax.set_xticklabels(labels, fontsize=10.5)
    ax.set_ylim(0, 130000)
    ax.set_yticks([0, 30000, 60000, 90000, 120000])
    ax.set_yticklabels(["$0", "$30K", "$60K", "$90K", "$120K"])
    ax.set_xlim(-0.55, 1.55)
    ax2 = axes[1]
    labels2 = ["Summer Scholar,\nEnterprise\nStrategy", "Summer Scholar,\nFunctional &\nOperations Strategy", "Summer Scholar,\nTechnology\nTransformation",
               "Discovery Intern\n(last full posting,\nSummer 2025)"]
    vals2 = [53, 50, 40, 32]
    bars2 = ax2.bar(range(4), vals2, width=0.55, color=[BLUE, BLUE, muted, muted], zorder=3)
    for b in bars2:
        ax2.annotate("${:,.0f} an hour".format(b.get_height()), (b.get_x() + b.get_width() / 2, b.get_height()), ha="center",
                     va="bottom", xytext=(0, 4), textcoords="offset points", fontsize=11.5, color=TEXT_PRIMARY)
    style_axes(ax2, title="Internship hourly rate, as posted")
    ax2.title.set_fontsize(13)
    ax2.set_xticks(range(4))
    ax2.set_xticklabels(labels2, fontsize=10.5)
    ax2.set_ylim(0, 66)
    ax2.set_yticks([0, 20, 40, 60])
    ax2.set_yticklabels(["$0", "$20", "$40", "$60"])
    ax2.set_xlim(-0.55, 3.55)
    from matplotlib.patches import Patch
    axes[0].legend(handles=[Patch(color=BLUE, label="Strategy tracks (the seats that took over the old S&O work)"),
                            Patch(color=muted, label="Technology Transformation and the Discovery Internship")],
                   loc="upper left", bbox_to_anchor=(0.0, -0.42), ncol=2, frameon=False, fontsize=11)
    fig.text(0.01, 0.01, "Deloitte's own \"reasonable estimate\" lines on October 2026 postings, tagged for verification at publish.\n"
             "Signing bonus about $12,500 (third party); performance bonus not published.", ha="left", va="bottom", fontsize=10.5, color=TEXT_SECONDARY, style="italic")
    fig.subplots_adjust(top=0.8, bottom=0.38, wspace=0.28, left=0.07, right=0.99)
    assert_fits(fig, 11, "02-pay-by-track.png")
    finish(fig, OUT / "02-pay-by-track.png")
    add("02-pay-by-track.png",
        "Two bar charts of Deloitte analyst base pay and intern hourly rates by track from the firm's postings",
        "The $105,000 strategy tracks are the ones with the 3.3 GPA floor and the case interview, and the intern rates rank the tracks the same way.",
        "Chart from the pay table in the draft (Deloitte posting estimates, each tagged [VERIFY] in the text)",
        "| Discovery Intern (last full posting, Summer 2025) | $32 an")


# ---------------------------------------------------------------- 3d: recruiting calendar against MBB
def calendar():
    W, H = 11, 7.4
    fig, ax = canvas(W, H, title="Deloitte recruits in the fall, months after MBB closes for the same summer")
    x0, x1, ya = 0.5, W - 0.4, 1.35
    months = ["Aug\n2026", "Sep", "Oct", "Nov", "Dec", "Jan\n2027", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan\n2028", "Feb"]
    n = len(months)
    step = (x1 - x0) / n
    ax.plot([x0, x1], [ya, ya], color=TEXT_SECONDARY, lw=1.4, zorder=2)
    for i, m in enumerate(months):
        xa = x0 + i * step
        ax.plot([xa, xa], [ya - 0.06, ya + 0.06], color=TEXT_SECONDARY, lw=1.0, zorder=2)
        ax.text(xa + step / 2, ya - 0.16, m, ha="center", va="top", fontsize=10, color=TEXT_SECONDARY)
    ax.plot([x1, x1], [ya - 0.06, ya + 0.06], color=TEXT_SECONDARY, lw=1.0, zorder=2)

    def mx(mi, frac=0.5):
        return month_x(x0, step, mi, frac)

    tx = mx(2, 5 / 31)
    ax.plot([tx, tx], [ya, H - 0.9], color=LINE, lw=1.2, zorder=1)
    label(ax, tx + 0.1, H - 0.95, "Today, October 5, 2026", size=10.5, color=TEXT_MUTED, ha="left", va="center", italic=True)

    def bar(s, e, y, color, text, where="right", wrap_w=5.0):
        ax.plot([s, e], [y, y], color=color, lw=9, solid_capstyle="round", alpha=0.85, zorder=3)
        if where == "right":
            label(ax, e + 0.18, y, text, size=10.5, ha="left", va="center", wrap_in=wrap_w)
        else:
            label(ax, s - 0.18, y, text, size=10.5, ha="right", va="center", wrap_in=wrap_w)

    y = H - 1.4
    bar(mx(0, 0.6), mx(3, 1 / 30), y, BLUE, "Summer Scholar, Summer 2027, strategy tracks: posted late summer 2026, recruiting ends November 1, 2026 (open now)", wrap_w=6.2)
    y -= 0.62
    bar(mx(0, 0.6), mx(3, 1 / 30), y, BLUE, "Analyst, full time, Summer 2027 start: recruiting ends November 1, 2026 (open now)", wrap_w=6.2)
    y -= 0.62
    bar(mx(0, 0.6), mx(4, 31 / 31), y, BLUE, "Summer Scholar, Summer 2027, Technology Transformation: recruiting ends December 31, 2026 (open now)", wrap_w=5.6)
    y -= 0.62
    bar(mx(2, 0.3), mx(4, 31 / 31), y, ORANGE, "Discovery Internship, Summer 2027 (freshmen and sophomores): expected to post in fall and winter 2026; prior cycle closed in December", wrap_w=5.6)
    y -= 0.85
    bar(mx(5, 0.0), mx(12, 31 / 31), y, ORANGE, "McKinsey, BCG and Bain applications for Summer 2028: expected January through August 2027", where="right", wrap_w=3.0)
    y -= 0.85
    bar(mx(12, 0.0), mx(15, 1.0), y, ORANGE, "Summer Scholar, Summer 2028 (Class of 2029): postings expected August to September 2027, close expected late October or November 2027", where="left", wrap_w=6.4)
    y -= 0.85
    bar(mx(15, 0.0), mx(18, 1.0), y, ORANGE, "Discovery Internship, Summer 2028: expected late 2027 into early 2028", where="left", wrap_w=5.0)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], color=BLUE, lw=8, label="Posted window (verify the close date on apply.deloitte.com)"),
                       Line2D([0], [0], color=ORANGE, lw=8, label="Expected, projected from this year's pattern (not yet posted)")],
              loc="lower left", bbox_to_anchor=(0.02, 0.0), ncol=2, frameon=False, fontsize=10.5)
    assert_fits(fig, W, "06-recruiting-calendar-vs-mbb.png")
    finish(fig, OUT / "06-recruiting-calendar-vs-mbb.png")
    add("06-recruiting-calendar-vs-mbb.png",
        "Timeline from August 2026 to February 2028 of Deloitte's posted and expected recruiting windows against the expected MBB window",
        "A sophomore who misses the MBB spring 2027 windows still has Deloitte's Summer 2028 window ahead of them that fall, so plan the case prep once and use it twice.",
        "Timeline drawn in matplotlib from the recruiting table and the planning paragraph in the draft; 2027 windows carry [VERIFY] tags and are shown as expected",
        "Here's the comparison that matters for planning. For Summer ")


# ---------------------------------------------------------------- 4: manifest
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


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    R = build_and_check()
    org_diagram()
    pay_chart()
    screenshots(R)
    calendar()
    entries.sort(key=lambda e: e["file"])
    check_manifest()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
