#!/usr/bin/env python3
"""Images for drafts/draft-bcg-case-interview-guide-v2.md (October 1, 2026).

Run from the repo root:  python3 scripts/images/build_bcg-case-interview-guide.py
Idempotent: rewrites every PNG in published/assets/images/bcg-case-interview-guide/ and the manifest.

Every number comes from the article's own tables and worked math (the section 1 process table,
the section 5 pizza chain exhibit and its step by step math, and the section 9 calendar table).
"""
import sys
from pathlib import Path

sys.path.insert(0, "scripts/images")
from wsg_viz import *          # noqa: E402,F401
from wsg_diagrams import *     # noqa: E402,F401

OUT = Path("published/assets/images/bcg-case-interview-guide")
OUT.mkdir(parents=True, exist_ok=True)
entries = []


def add(file, alt, caption, method, anchor):
    entries.append({"file": file, "alt": alt, "caption": caption, "method": method, "anchor": anchor})


# ---------------------------------------------------------------- 01 funnel
def funnel():
    W, H = 11, 7.4
    fig, ax = canvas(W, H, title="Two online screens sit between a BCG application and a human interviewer")
    stages = [
        ("Application", "Resume, top two office preferences, optional cover letter. By the deadline.", BLUE),
        ("Consulting Career Assessment (CCA)", "Timed reasoning and work style test, all US applicants. Invitation 30 to 90 minutes after you submit; 48 hours to complete; about 30 to 35 minutes.", BLUE),
        ("Online case (Casey)", "Chatbot case with written answers and a short recorded recommendation. About two weeks after the deadline, select candidates only, about 35 minutes.", BLUE),
        ("First round", "Two interviews, each a short behavioral plus a case, about 45 minutes each. Weeks after the online case.", SEQ_BLUE[9]),
        ("Final round", "Two or three interviews with principals and partners, about 45 minutes each, usually within a couple of weeks of round one.", SEQ_BLUE[11]),
    ]
    from matplotlib.patches import Polygon
    cx, top, band_h, gap = 3.4, H - 1.15, 0.95, 0.14
    widths = [5.6, 4.7, 3.8, 2.9, 2.0]
    y = top
    for (head, body, col), w in zip(stages, widths):
        w_next = w - 0.9
        poly = Polygon([(cx - w / 2, y), (cx + w / 2, y), (cx + w_next / 2, y - band_h), (cx - w_next / 2, y - band_h)],
                       closed=True, facecolor=col, edgecolor=SURFACE, linewidth=2, zorder=3)
        ax.add_patch(poly)
        ax.text(cx, y - band_h / 2, head, ha="center", va="center", fontsize=13.5 if len(head) < 24 else 12, color="white",
                fontweight="bold", zorder=4)
        label(ax, cx + widths[0] / 2 + 0.35, y - band_h / 2, body, size=11.5, ha="left", va="center", wrap_in=W - (cx + widths[0] / 2 + 0.35) - 0.4)
        y -= band_h + gap
    label(ax, 0.35, 0.45, "Online screens: the firm reads your file closely only after you clear them. Live rounds: where this guide spends its time.",
          size=11.5, color=TEXT_SECONDARY, italic=True, wrap_in=W - 0.8, va="center")
    finish(fig, OUT / "01-bcg-interview-funnel.png")
    add("01-bcg-interview-funnel.png",
        "Funnel diagram of BCG's process: application, CCA, online case, first round, final round, with timing notes",
        "Two automated screens run before anyone at BCG reads your file closely, and the online case score you post is the one the firm keeps.",
        "Funnel drawn in matplotlib from the five-row process table in section 1",
        "| Final round | Two or three interviews with principals and ")


# ---------------------------------------------------------------- 02 contribution per order
def contribution_chart():
    import numpy as np
    channels = ["In-store and carryout", "Own-app delivery", "Third-party app delivery"]
    two_years_ago = [8.00, 9.00, 5.50]
    last_year = [8.00, 9.00, 5.20]
    fig, ax = new_figure(width=10, height=5.6)
    x = np.arange(3)
    w = 0.34
    b1 = ax.bar(x - w / 2 - 0.01, two_years_ago, w, color=BLUE, label="Two years ago", zorder=3)
    b2 = ax.bar(x + w / 2 + 0.01, last_year, w, color=ORANGE, label="Last year", zorder=3)
    bar_labels(ax, b1, fmt="${:,.2f}", fontsize=12.5)
    bar_labels(ax, b2, fmt="${:,.2f}", fontsize=12.5)
    style_axes(ax, title="Third-party app orders keep $5.20 against $8 to $9 in the channels the chain controls",
               ylabel="Contribution per order, $")
    ax.set_xticks(x)
    ax.set_xticklabels(channels, fontsize=12.5)
    ax.set_ylim(0, 10.5)
    ax.set_yticks([0, 2, 4, 6, 8, 10])
    ax.legend(loc="upper right", ncol=2)
    ax.text(0, -0.16, "Contribution per order: the ticket minus food, packaging and store labor, minus the driver cost (own app) or the 30 percent commission (third-party apps).",
            transform=ax.transAxes, ha="left", va="top", fontsize=11, color=TEXT_SECONDARY, style="italic")
    fig.subplots_adjust(bottom=0.2)
    finish(fig, OUT / "02-contribution-per-order-by-channel.png")
    add("02-contribution-per-order-by-channel.png",
        "Grouped bar chart of contribution per pizza order by channel for two years ago and last year",
        "Contribution per order held at $8 in store and $9 on the chain's own app while the third-party channel that grew earns $5.20.",
        "Chart from the section 5 exhibit and the Step two contribution per order calculations",
        "- Third-party apps, two years ago: 30 percent of $25 is $7.5")


# ---------------------------------------------------------------- 03 contribution bridge
def bridge():
    fig, ax = new_figure(width=11, height=5.8)
    steps = [("In-store volume loss (6M orders at $8)", -48.0),
             ("Own-app volume loss (1M orders at $9)", -9.0),
             ("Third-party gain at the old $5.50 (9M orders)", 49.5),
             ("Third-party margin slip (13M orders at 30 cents)", -3.9)]
    end = waterfall(ax, steps, 236.0, "Contribution two years ago", "Contribution last year",
                    fmt="${:,.1f}M", ylabel="Total contribution, $ millions",
                    title="The chain sold 2 million more pizzas and made $11.4 million less contribution",
                    ymin=0, legend_loc="upper right")
    assert abs(end - 224.6) < 1e-9, end
    ax.set_ylim(0, 275)
    ax.set_yticks([0, 50, 100, 150, 200, 250])
    finish(fig, OUT / "03-contribution-bridge.png")
    add("03-contribution-bridge.png",
        "Waterfall chart bridging contribution from $236 million two years ago to $224.6 million last year",
        "Orders moved from the counter to third-party apps, and the bridge from $236 million to $224.6 million shows the margin leaving with them.",
        "Waterfall from the Step three totals and the Step five bridge figures in section 5",
        "**Step five: a bridge, if the interviewer wants precision.**")


# ---------------------------------------------------------------- 04 so what loop
def so_what_loop():
    W, H = 11, 6.9
    fig, ax = canvas(W, H, title="The hypothesis loop: after every number, say what it is, what it means, and where you go next")
    nodes = [
        ("1. State the hypothesis", "A specific guess about the cause, said out loud before you see any data."),
        ("2. Ask for the data", "The one or two numbers that would confirm or kill it."),
        ("3. Do the math", "Out loud, cleanly, with the unit."),
        ("4. Say the so what", "What it is. What it means for the client. Where you'd go next."),
    ]
    bw, bh, gap, x0, y1 = 2.3, 1.4, 0.42, 0.35, H - 2.95
    centers = []
    for i, (head, body) in enumerate(nodes):
        x = x0 + i * (bw + gap)
        centers.append(x + bw / 2)
        strong = i == 3
        text_box(ax, x, y1, bw, bh, "", fill=PALE_ORANGE if strong else PALE_BLUE, radius=0.08)
        text_box(ax, x, y1 + bh - 0.42, bw, 0.42, head, fill=ORANGE if strong else BLUE, text_color="white", size=12.5, bold=True, radius=0.08)
        label(ax, x + bw / 2, y1 + (bh - 0.42) / 2, body, size=11, ha="center", va="center", wrap_in=bw - 0.25)
        if i < 3:
            arrow(ax, (x + bw + 0.04, y1 + bh / 2), (x + bw + gap - 0.04, y1 + bh / 2), color=TEXT_SECONDARY, lw=2.0, head=20)
    # 5. Update sits under box 4
    x4 = x0 + 3 * (bw + gap)
    y5 = y1 - 0.75 - bh
    text_box(ax, x4, y5, bw, bh, "", fill=PALE_BLUE, radius=0.08)
    text_box(ax, x4, y5 + bh - 0.42, bw, 0.42, "5. Update", fill=BLUE, text_color="white", size=12.5, bold=True, radius=0.08)
    label(ax, x4 + bw / 2, y5 + (bh - 0.42) / 2, "Confirmed: what to do about it. Killed: the next hypothesis, and the data to test it.",
          size=11, ha="center", va="center", wrap_in=bw - 0.25)
    arrow(ax, (centers[3], y1 - 0.04), (centers[3], y5 + bh + 0.04), color=TEXT_SECONDARY, lw=2.0, head=20)
    # killed: back to 1 along a channel below the top row
    ych = y5 + bh / 2
    line(ax, (x4 - 0.04, ych), (centers[0], ych), color=TEXT_SECONDARY, lw=2.0)
    arrow(ax, (centers[0], ych), (centers[0], y1 - 0.04), color=TEXT_SECONDARY, lw=2.0, head=20)
    label(ax, (x4 + centers[0]) / 2, ych + 0.12, "Killed: back to step 1 with a new hypothesis and the data to test it", size=11.5,
          color=TEXT_SECONDARY, ha="center", va="bottom", italic=True)
    # confirmed: down to the recommendation
    yr = y5 - 0.75 - 0.9
    text_box(ax, x4 - 2.9, yr, bw + 2.9, 0.9, "Recommendation: answer first, then the numbers you've already proven, then risks and next steps",
             fill=SEQ_BLUE[11], text_color="white", size=12, bold=True, radius=0.08)
    arrow(ax, (centers[3], y5 - 0.04), (centers[3], yr + 0.9 + 0.04), color=TEXT_SECONDARY, lw=2.0, head=20)
    label(ax, centers[3] + 0.12, y5 - 0.4, "Confirmed", size=11.5, color=TEXT_SECONDARY, ha="left", va="center", italic=True)
    label(ax, x0, yr + 0.45, "Step 4 is the scored moment. A number with no so what is a number; a number with its meaning and the next question is a consultant talking.",
          size=11.5, color=TEXT_SECONDARY, italic=True, va="center", wrap_in=4.9)
    finish(fig, OUT / "04-hypothesis-so-what-loop.png")
    add("04-hypothesis-so-what-loop.png",
        "Flow diagram of the hypothesis loop: state, ask for data, do the math, say the so what, update, recommend",
        "Every number you compute goes through step four before you move, and a killed hypothesis sends you back to the top with a new one.",
        "Diagram drawn in matplotlib from the five-step cycle in section 4",
        "5. **Update.** Either \"that confirms it, so the next questio")


# ---------------------------------------------------------------- 05 calendar
def calendar():
    months = ["Oct\n2026", "Nov", "Dec", "Jan\n2027", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep\n2027"]
    W, H = 11, 6.3
    fig, ax = canvas(W, H, title="BCG's Summer 2028 calendar: the Summer Associate deadline is the date to build the year around")
    x0, x1, ya = 0.5, W - 0.4, 1.75
    step = month_axis(ax, months, ya, x0, x1)
    def mx(mi, frac=0.5):
        return month_x(x0, step, mi, frac)
    lanes = [
        # (y, start, end, where, wrap width, text)
        (H - 1.5, mx(3, 0.0), mx(8, 1.0), "above", 7.2, "Summer Associate internship, Summer 2028 (sophomores now): applications expected in the first half of 2027, single deadline likely late spring. Not yet posted."),
        (H - 2.35, mx(6, 0.3), mx(7, 0.95), "right", 5.2, "BCG Launch (virtual info series, not a job): 2027 registration not posted; the 2026 portal closed May 29"),
        (H - 3.1, mx(6, 0.5), mx(7, 0.45), "right", 5.2, "BCG Embark (virtual conference inside Launch): 2026 edition registered by April 15, event May 14; 2027 dates not posted"),
        (H - 3.95, mx(11, 0.3), mx(11, 0.7), "left", 5.2, "Growing Future Leaders (sophomore summer internship): past cycles closed mid September; no live posting"),
    ]
    for y, s, e, where, wrap_w, text in lanes:
        ax.plot([s, e], [y, y], color=ORANGE, lw=9, solid_capstyle="round", alpha=0.85, zorder=3)
        if where == "right":
            label(ax, e + 0.18, y, text, size=11.5, ha="left", va="center", wrap_in=wrap_w)
        elif where == "left":
            label(ax, s - 0.18, y, text, size=11.5, ha="right", va="center", wrap_in=wrap_w)
        else:
            label(ax, s, y + 0.14, text, size=11.5, ha="left", va="bottom", wrap_in=wrap_w)
    # today: the article's "what to do this week" for sophomores
    tx, ty = mx(0, 1 / 31), H - 3.1
    ax.plot([tx], [ty], marker="D", ms=11, color=BLUE, zorder=4)
    ax.plot([tx, tx], [ya, ty], color=GRID, lw=1.0, zorder=1)
    label(ax, tx + 0.18, ty, "October 1, 2026: create your BCG candidate profile, pick your two offices, do OneDay@BCG and one interactive case, start the math drill.",
          size=11.5, ha="left", va="center", wrap_in=3.9)
    # reference: last cycle's dated deadlines, shown as text under the axis
    label(ax, 0.5, 0.95, "Last cycle, for the pattern: Summer 2027 Summer Associate deadline June 2, 2026; full-time Associate deadline July 7, 2026. "
          "Every 2027 window above is projected from those dates and not yet posted by BCG.",
          size=11, color=TEXT_SECONDARY, italic=True, va="top", wrap_in=W - 1.0)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([0], [0], marker="D", color=BLUE, lw=0, ms=10, label="Today"),
                       Line2D([0], [0], color=ORANGE, lw=8, label="Expected window, projected from last cycle (verify on careers.bcg.com once posted)")],
              loc="lower left", bbox_to_anchor=(0.03, 0.0), ncol=2, frameon=False, fontsize=11.5)
    finish(fig, OUT / "05-summer-2028-calendar.png")
    add("05-summer-2028-calendar.png",
        "Timeline from October 2026 to September 2027 with BCG's expected Summer Associate, Launch, Embark and GFL windows",
        "Nothing on BCG's 2027 calendar is posted yet, so plan around a late spring Summer Associate deadline and treat Launch and Embark as useful extras.",
        "Timeline drawn in matplotlib from the section 9 calendar table; every window carries a [VERIFY] tag in the draft and is shown as expected",
        "| Full-time Associate, start 2029 | Students graduating 2029")


if __name__ == "__main__":
    funnel()
    contribution_chart()
    bridge()
    so_what_loop()
    calendar()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT}")
