#!/usr/bin/env python3
"""Images for drafts/draft-bain-case-interview-guide-v2.md (October 1, 2026).

Run from the repo root:  python3 scripts/images/build_bain-case-interview-guide.py
Idempotent: rewrites every PNG in published/assets/images/bain-case-interview-guide/ and the manifest.

Every number comes from the article's own tables and worked math (section 6, the FreshBowl case,
and the section 11 calendar table). Nothing here is sourced from outside the draft.
"""
import sys
from pathlib import Path

sys.path.insert(0, "scripts/images")
from wsg_viz import *          # noqa: E402,F401
from wsg_diagrams import *     # noqa: E402,F401

OUT = Path("published/assets/images/bain-case-interview-guide")
OUT.mkdir(parents=True, exist_ok=True)
entries = []


def add(file, alt, caption, method, anchor):
    entries.append({"file": file, "alt": alt, "caption": caption, "method": method, "anchor": anchor})


# ---------------------------------------------------------------- 01 hiring process flow
def hiring_flow():
    fig, ax = canvas(11, 4.4, title="Bain's hiring process has four steps, and the firm tells you how each interview went")
    steps = [
        ("1. Application", "Resume (Word or PDF), education, work experience, test scores. Cover letters at many offices; check your school's Bain page."),
        ("2. Digital assessment", "Sova or TestGorilla, named in the invitation email. About 30 to 40 minutes. Problem solving, communication, analytical skills. Calculator allowed."),
        ("3. Round one", "Two interviews back to back, roughly 40 minutes each, with consultants, managers or senior managers. A case plus some experience questions."),
        ("4. Final round", "Two to three interviews of 40 to 60 minutes with senior managers and partners. Deeper experience questions. Some offices outside the US add a written case."),
    ]
    x, y, w, h, gap = 0.35, 1.25, 2.45, 2.05, 0.28
    for i, (head, body) in enumerate(steps):
        bx = x + i * (w + gap)
        text_box(ax, bx, y, w, h, "", fill=PALE_BLUE, radius=0.1)
        text_box(ax, bx, y + h - 0.62, w, 0.62, head, fill=BLUE, text_color="white", size=14, bold=True, radius=0.1)
        label(ax, bx + 0.15, y + h - 0.78, body, size=11.5, color=TEXT_PRIMARY, ha="left", va="top", wrap_in=w - 0.3)
        if i < len(steps) - 1:
            arrow(ax, (bx + w + 0.03, y + h / 2), (bx + w + gap - 0.03, y + h / 2), color=TEXT_SECONDARY, lw=2.2, head=20)
    # feedback note under the two live rounds
    bx3 = x + 2 * (w + gap)
    ax.plot([bx3, bx3 + 2 * w + gap], [y - 0.22, y - 0.22], color=ORANGE, lw=2.2, solid_capstyle="round", zorder=2)
    label(ax, bx3 + (2 * w + gap) / 2, y - 0.38, "After each interview, you'll learn exactly how it went (Bain's words). Use round-one feedback before the final.",
          size=11.5, color=TEXT_PRIMARY, ha="center", va="top", wrap_in=2 * w + gap)
    label(ax, x, y - 0.38, "The assessment is one part of the review, not a gate that erases your resume.", size=11.5,
          color=TEXT_SECONDARY, ha="left", va="top", wrap_in=2 * w + gap, italic=True)
    finish(fig, OUT / "01-hiring-process-four-steps.png")
    add("01-hiring-process-four-steps.png",
        "Four boxes in a row showing Bain's hiring steps: application, digital assessment, round one, final round",
        "Bain's four steps in order, and the firm tells you how each interview went before the next one.",
        "Diagram drawn in matplotlib from the four-step list in section 1 of the draft",
        "- **Final round.** Two to three interviews with senior manag")


# ---------------------------------------------------------------- 02 Exhibit 3 cohort chart
def cohort_chart():
    cohorts = ["Opened more\nthan 5 years\nago (50 stores)", "Opened 2 to 5\nyears ago\n(40 stores)", "Opened in the\nlast 2 years\n(30 stores)"]
    revenue = [1.8, 1.5, 1.0]          # $ millions per store
    margin = [18, 13, 10]              # percent
    ebitda_k = [324, 195, 100]         # $ thousands per store, as the article states them
    plan_k = 220                       # what the plan needs per new store
    fig, axes = new_figure(width=11, height=5.6, ncols=3)
    fig.suptitle("Each new FreshBowl store needs $220,000 of EBITDA a year; the newest cohort earns $100,000",
                 x=0.01, ha="left", fontsize=16, fontweight="bold", color=TEXT_PRIMARY)
    panels = [("Average revenue per store", revenue, "${:,.1f}M", 2.3),
              ("Store-level EBITDA margin", margin, "{:.0f}%", 23),
              ("Store-level EBITDA per store", ebitda_k, "${:,.0f}K", 400)]
    for ax, (ttl, vals, f, ymax) in zip(axes, panels):
        bars = ax.bar(range(3), vals, width=0.55, color=BLUE, zorder=3)
        for b in bars:   # value labels with a white backing so a reference line passes behind them
            ax.annotate(f.format(b.get_height()), (b.get_x() + b.get_width() / 2, b.get_height()), ha="center",
                        va="bottom", xytext=(0, 3), textcoords="offset points", fontsize=12.5, color=TEXT_PRIMARY,
                        bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.5), zorder=5)
        style_axes(ax, title=ttl)
        ax.title.set_fontsize(13.5)
        ax.set_xticks(range(3))
        ax.set_xticklabels(cohorts, fontsize=10)
        ax.set_xlim(-0.5, 2.5)
        ax.set_ylim(0, ymax)
        ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.grid(False)
    ax3 = axes[2]
    ax3.axhline(plan_k, color=ORANGE, lw=2.2, zorder=2)
    ax3.annotate("Plan: $220K", (2.47, plan_k), ha="right", va="bottom", xytext=(0, 4),
                 textcoords="offset points", fontsize=11.5, color=TEXT_PRIMARY, zorder=5)
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    axes[0].legend(handles=[Patch(color=BLUE, label="FreshBowl store cohort (Exhibit 3)"),
                            Line2D([0], [0], color=ORANGE, lw=2.2, label="What management's plan assumes per new store")],
                   loc="upper left", bbox_to_anchor=(0.0, -0.3), ncol=2, frameon=False, fontsize=11.5)
    fig.subplots_adjust(top=0.82, bottom=0.3, wspace=0.3, left=0.03, right=0.99)
    finish(fig, OUT / "02-freshbowl-store-cohorts.png")
    add("02-freshbowl-store-cohorts.png",
        "Three bar charts comparing FreshBowl store cohorts by revenue, margin and EBITDA per store against the plan",
        "The newest FreshBowl stores earn less revenue at a thinner margin, so each one makes $100,000 against the $220,000 the plan needs.",
        "Chart from Exhibit 3 (store performance by age) and the per-store EBITDA figures in the Math question 3 so what",
        "| Opened in the last 2 years | 30 | $1.0 million | 10 percen")


# ---------------------------------------------------------------- 03 EBITDA scenarios
def scenario_chart():
    labels = ["Today", "Plan as written\n(new stores earn\n$1.5M at 15%)", "New stores like the\n2 to 5 year cohort\n($1.5M at 13%)",
              "New stores like the\nnewest cohort\n($1.0M at 10%)"]
    vals = [18, 36.5, 33.5, 24]
    target = 36
    fig, ax = new_figure(width=10, height=5.8)
    bars = ax.bar(range(4), vals, width=0.55, color=[TEXT_MUTED, BLUE, BLUE, BLUE], zorder=3)
    for b in bars:
        ax.annotate("${:,.1f}M".format(b.get_height()), (b.get_x() + b.get_width() / 2, b.get_height()), ha="center",
                    va="bottom", xytext=(0, 3), textcoords="offset points", fontsize=13, color=TEXT_PRIMARY,
                    bbox=dict(facecolor=SURFACE, edgecolor="none", pad=1.5), zorder=5)
    ax.axhline(target, color=ORANGE, lw=2.2, zorder=2)
    ax.annotate("Target: $36M", (-0.45, target), ha="left", va="bottom", xytext=(0, 4),
                textcoords="offset points", fontsize=12, color=TEXT_PRIMARY, zorder=5)
    style_axes(ax, title="Using FreshBowl's own store data, 100 new stores land $2.5 to $12 million short of the $36 million target",
               ylabel="Company EBITDA in year five, $ millions")
    ax.set_xticks(range(4))
    ax.set_xticklabels(labels, fontsize=11.5)
    ax.set_xlim(-0.5, 3.5)
    ax.set_ylim(0, 44)
    ax.set_yticks([0, 10, 20, 30, 40])
    for i, g in [(2, "$2.5M short"), (3, "$12M short")]:
        ax.annotate(g, (i, vals[i] - 1.2), ha="center", va="top", fontsize=12, color="white", zorder=5)
    from matplotlib.lines import Line2D
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=TEXT_MUTED, label="Today"), Patch(color=BLUE, label="Year five scenarios (Math questions 2 and 3)"),
                       Line2D([0], [0], color=ORANGE, lw=2.2, label="EBITDA the price needs")],
              loc="upper left", bbox_to_anchor=(0, -0.2), ncol=3, frameon=False)
    fig.subplots_adjust(bottom=0.3)
    finish(fig, OUT / "03-freshbowl-ebitda-scenarios.png")
    add("03-freshbowl-ebitda-scenarios.png",
        "Bar chart of FreshBowl year five EBITDA under three scenarios against the $36 million target line",
        "Run the plan on FreshBowl's own cohort numbers and year five EBITDA lands between $24 million and $33.5 million, not $36 million.",
        "Chart from the Math question 2 and Math question 3 results in section 6 (both passes)",
        "- Gap to target: $36 million minus $33.5 million = **$2.5 mi")


# ---------------------------------------------------------------- 04 weak vs strong close
WEAK = [
    ("Walks back through Exhibit 1",
     "So, to sum up what we looked at. We started by looking at FreshBowl's current position, where they have 120 stores at $1.5 million each, which gets you to $180 million in revenue, and then with a 15 percent margin and $9 million of overhead that's $18 million of EBITDA."),
    ("Walks through the plan",
     "Then we looked at the management plan, which assumes 20 stores a year, and when you run that through you get $36.5 million, so on paper it works."),
    ("Cohort data, then a hedge",
     "But then the cohort data showed that newer stores are doing $1 million and 10 percent, which is a lot worse, and when you use those numbers you only get to $24 million, although if you use the middle cohort you get $33.5 million, so it kind of depends."),
    ("Loose ends",
     "There's also the $90 million of capex to think about, and a price increase could help, maybe 1 to 4 percent."),
    ("The answer, last, hedged twice",
     "So overall I think it's a riskier deal than management is presenting and the fund should probably be cautious, maybe try to get a lower price, and do some more work on the new stores before deciding."),
]
STRONG = [
    ("The answer, first", "Don't buy at this price."),
    ("The gap, with numbers",
     "The price needs $36 million of EBITDA and FreshBowl's own store data gets you to $24 to $33.5 million, so the plan is $2.5 to $12 million short."),
    ("Two reasons",
     "Two reasons: new stores open at $1 million of revenue and a 10 percent margin against the $1.5 million and 15 percent the plan assumes, and overhead grows by $4 million."),
    ("One risk",
     "The risk to my view is that the newest stores are just ramping, which would put us at the top of that range."),
    ("Next step, then stop",
     "So either renegotiate to a price that works on $30 million, or spend the next two weeks on revenue by month since opening, which tells us whether this is a ramp or a quality problem. If it's a ramp, the deal works close to the current price."),
]


def close_graphic():
    W, H = 11, 9.6
    fig, ax = canvas(W, H, title="The same FreshBowl analysis, closed two ways")
    col_w, tag_w, size = 3.75, 1.3, 12.5
    cols = [(0.35, "The weak close", WEAK, PALE_ORANGE, ORANGE, "About 185 words. The recommendation arrives in the last clause, hedged twice."),
            (5.6, "The strong close", STRONG, PALE_BLUE, BLUE, "About 135 words. Answer in the first four words, every number from the case, one risk, one next step.")]
    for x, head, parts, fill, accent, foot in cols:
        text_box(ax, x, H - 1.35, tag_w + col_w + 0.15, 0.55, head, fill=accent, text_color="white", size=15, bold=True, radius=0.08)
        y = H - 1.6
        for tag, body in parts:
            t = wrap(body, col_w - 0.2, size)
            n = t.count("\n") + 1
            bh = n * size * 1.3 / 72 + 0.22
            text_box(ax, x + tag_w + 0.15, y - bh, col_w, bh, "", fill=fill, radius=0.06)
            ax.text(x + tag_w + 0.25, y - bh / 2, t, ha="left", va="center", fontsize=size, color=TEXT_PRIMARY, linespacing=1.3, zorder=5)
            label(ax, x + tag_w, y - bh / 2, tag, size=11, color=TEXT_SECONDARY, ha="right", va="center", bold=True, wrap_in=tag_w - 0.05)
            y -= bh + 0.12
        label(ax, x + tag_w + 0.15, y - 0.08, foot, size=11.5, color=TEXT_SECONDARY, ha="left", va="top", italic=True, wrap_in=col_w)
    finish(fig, OUT / "04-weak-close-vs-strong-close.png")
    add("04-weak-close-vs-strong-close.png",
        "Side by side text of a weak case close that recaps the analysis and a strong close that answers first",
        "Same candidate, same numbers: the weak close recaps the case and hedges the verdict, the strong close gives it in four words and stops.",
        "Text graphic drawn in matplotlib from the two closes quoted in section 7",
        "About 135 words, answer in the first four words, every numbe")


# ---------------------------------------------------------------- 05 Summer 2028 calendar
def calendar():
    months = ["Oct\n2026", "Nov", "Dec", "Jan\n2027", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep\n2027"]
    W, H = 11, 7.2
    fig, ax = canvas(W, H, title="Bain's calendar for a sophomore in October 2026: Kickstart now, BEL or CREW in winter, ACI in spring")
    x0, x1, ya = 0.5, W - 0.4, 1.3
    step = month_axis(ax, months, ya, x0, x1)
    def mx(mi, frac=0.5):
        return month_x(x0, step, mi, frac)
    lanes = [
        # (y, kind, start, end, where, wrap width, text)
        (H - 1.2, "date", mx(0, 5 / 31), None, "right", 9.5, "Consulting Kickstart application deadline, Monday October 5 (open now)"),
        (H - 1.75, "date", mx(0, 11 / 31), None, "right", 9.5, "Associate Consultant full time deadline, October 11 on Bain's Harvard page (open now; check your school's page)"),
        (H - 2.75, "range", mx(0, 0.5), mx(4, 0.6), "above", 7.5, "CREW (sophomore women): 2027 cycle not yet posted; last cycle's applications ran in the fall and winter"),
        (H - 3.5, "range", mx(2, 0.8), mx(3, 0.95), "right", 6.4, "BEL (sophomores): expect applications around January 2027"),
        (H - 4.5, "range", mx(5, 0.0), mx(7, 1.0), "above", 6.0, "First Forward (first generation or lower income sophomores) and BASE (pre MBA): next cycles expected spring 2027"),
        (H - 5.5, "range", mx(5, 0.0), mx(7, 1.0), "above", 3.5, "Associate Consultant Intern, Summer 2028: first deadline expected around spring 2027"),
        (H - 5.5, "range", mx(9, 0.5), mx(11, 1.0), "above", 2.3, "ACI, Summer 2028: second deadline expected around late summer 2027"),
    ]
    for y, kind, s, e, where, wrap_w, text in lanes:
        if kind == "date":
            ax.plot([s], [y], marker="D", ms=11, color=BLUE, zorder=4)
            ax.plot([s, s], [ya, y], color=GRID, lw=1.0, zorder=1)
            label(ax, s + 0.18, y, text, size=11.5, ha="left", va="center", wrap_in=wrap_w)
        else:
            ax.plot([s, e], [y, y], color=ORANGE, lw=9, solid_capstyle="round", alpha=0.85, zorder=3)
            if where == "right":
                label(ax, e + 0.18, y, text, size=11.5, ha="left", va="center", wrap_in=wrap_w)
            else:
                label(ax, s, y + 0.14, text, size=11.5, ha="left", va="bottom", wrap_in=wrap_w)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], marker="D", color=BLUE, lw=0, ms=10, label="Posted deadline (verify on bain.com)"),
                       Line2D([0], [0], color=ORANGE, lw=8, label="Expected window, projected from last cycle (not yet posted)")],
              loc="lower left", bbox_to_anchor=(0.03, 0.0), ncol=2, frameon=False, fontsize=11.5)
    finish(fig, OUT / "05-summer-2028-calendar.png")
    add("05-summer-2028-calendar.png",
        "Timeline from October 2026 to September 2027 with Bain's posted deadlines and expected program windows",
        "Consulting Kickstart closes this week, BEL and CREW come in the winter, and the first Associate Consultant Intern window is expected in spring 2027.",
        "Timeline drawn in matplotlib from the section 11 calendar table; windows tagged [VERIFY] in the draft are shown as expected",
        "| Associate Consultant, full time | Seniors graduating Decem")


if __name__ == "__main__":
    hiring_flow()
    cohort_chart()
    scenario_chart()
    close_graphic()
    calendar()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT}")
