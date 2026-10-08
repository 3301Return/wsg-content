#!/usr/bin/env python3
"""Images for drafts/draft-20-consulting-behavioral-interview-questions-v1.md (October 1, 2026).

Run from the repo root:  python3 scripts/images/build_20-consulting-behavioral-interview-questions.py

1. 01-pei-vs-standard-behavioral.png   one story in ten minutes against five questions in twenty
2. 02-structured-vs-unstructured-validity.png  validity bars, 0.51 against 0.38 (Schmidt and Hunter 1998)
3. 03-five-part-story-shape.png        the five-part story shape with the actions in the middle

Idempotent: every run rewrites the three PNGs and the manifest.
"""
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, "scripts/images")
from wsg_viz import *                      # noqa: F401,F403
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Patch

SLUG = "20-consulting-behavioral-interview-questions"
OUT = Path("published/assets/images") / SLUG
OUT.mkdir(parents=True, exist_ok=True)
entries = []


# ---------------------------------------------------------------- 01 PEI vs a standard behavioral round
fig, ax = new_figure(width=11.0, height=5.4)
fig.subplots_adjust(left=0.235, right=0.965, top=0.84, bottom=0.25)
fig.text(0.04, 0.93, "The PEI spends ten minutes on one story; a standard round spends four on each of five",
         fontsize=16, fontweight="bold", color=TEXT_PRIMARY, va="center")
style_axes(ax, xlabel="Minutes into the behavioral portion", ygrid_only=False)
ax.grid(False)
ax.set_xlim(0, 20)
ax.set_xticks([0, 5, 10, 15, 20])
ax.set_ylim(-0.75, 1.5)
ax.set_yticks([1, 0])
ax.set_yticklabels(["McKinsey PEI", "Standard behavioral round\n(Big 4 first round)"], fontsize=13, color=TEXT_PRIMARY)
ax.spines["left"].set_visible(False)
bar_h = 0.44
# PEI: one story, ten minutes
ax.barh(1, 10, height=bar_h, color=BLUE, left=0)
ax.text(5, 1, "One story, about ten minutes", ha="center", va="center", color="white", fontsize=13, fontweight="bold")
ax.text(0, 1 - bar_h / 2 - 0.1, "Follow-ups the whole way: what did you say, what did they say back, what did you do next?",
        ha="left", va="top", color=TEXT_SECONDARY, fontsize=11.5)
# standard: five questions in twenty minutes (a small surface gap between bars)
gap_min = 0.08
for k in range(5):
    ax.barh(0, 4 - gap_min, height=bar_h, color=ORANGE, left=k * 4 + gap_min / 2)
    ax.text(k * 4 + 2, 0, f"Q{k + 1}", ha="center", va="center", color="white", fontsize=13, fontweight="bold")
ax.text(0, 0 - bar_h / 2 - 0.1, "Five questions in about twenty minutes, so each answer has to land in roughly four",
        ha="left", va="top", color=TEXT_SECONDARY, fontsize=11.5)
fig.legend(handles=[Patch(color=BLUE, label="McKinsey PEI"), Patch(color=ORANGE, label="Standard behavioral round")],
           loc="lower left", bbox_to_anchor=(0.235, 0.03), ncol=2, frameon=False)
save_figure(fig, OUT / "01-pei-vs-standard-behavioral.png", tight=False)
entries.append({
    "file": "01-pei-vs-standard-behavioral.png",
    "alt": "Timeline comparing the McKinsey PEI, one story over ten minutes, with a standard behavioral round of five questions in twenty.",
    "caption": "Same half hour of fit questions, two very different shapes: the PEI goes deep on one story and a standard round skims five.",
    "method": "Matplotlib timeline from the article's own description of the two formats (one story in about ten minutes; five questions in twenty), scripts/images/build_20-consulting-behavioral-interview-questions.py.",
    "anchor": "**The McKinsey PEI goes deep on one story for about ten minu",
})


# ---------------------------------------------------------------- 02 structured vs unstructured validity
fig, ax = new_figure(width=11.0, height=6.2)
fig.subplots_adjust(left=0.09, right=0.97, top=0.80, bottom=0.19)
fig.text(0.04, 0.935, "Structured interviews predict job performance better than unstructured ones",
         fontsize=16, fontweight="bold", color=TEXT_PRIMARY, va="center")
fig.text(0.04, 0.875, "0 means the interview tells you nothing about how the person will perform; 1.0 would mean it predicts performance perfectly.",
         fontsize=11.5, color=TEXT_SECONDARY, va="center")
style_axes(ax, ylabel="Validity (correlation with later job performance)")
labels = ["Structured interview\n(fixed questions, scored the same way for everyone)",
          "Unstructured interview\n(a free-form conversation)"]
vals = [0.51, 0.38]
x = [0, 1]
w = 0.26
for xi, v in zip(x, vals):
    # a thin bar with a rounded data end and a square baseline, per the mark spec
    body = FancyBboxPatch((xi - w / 2, 0), w, v, boxstyle="round,pad=0,rounding_size=0.008",
                          facecolor=BLUE, edgecolor="none", mutation_aspect=1)
    ax.add_patch(body)
    ax.add_patch(FancyBboxPatch((xi - w / 2, 0), w, 0.02, boxstyle="square,pad=0", facecolor=BLUE, edgecolor="none"))
    ax.annotate(f"{v:.2f}", (xi, v), ha="center", va="bottom", xytext=(0, 5), textcoords="offset points",
                fontsize=15, fontweight="bold", color=TEXT_PRIMARY)
ax.set_xlim(-0.55, 1.55)
ax.set_ylim(0, 0.6)
ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=12.5, color=TEXT_PRIMARY)
fig.text(0.04, 0.04, "Source: Schmidt and Hunter (1998), a review of 85 years of research on hiring methods.",
         fontsize=11, color=TEXT_MUTED, va="center")
save_figure(fig, OUT / "02-structured-vs-unstructured-validity.png", tight=False)
entries.append({
    "file": "02-structured-vs-unstructured-validity.png",
    "alt": "Bar chart showing interview validity of 0.51 for structured interviews against 0.38 for unstructured interviews.",
    "caption": "The jump from 0.38 to 0.51 is why the firms grade your stories against a sheet, per Schmidt and Hunter's 1998 review of 85 years of hiring research.",
    "method": "Chart drawn from the two figures the article cites (Schmidt and Hunter 1998, structured 0.51, unstructured 0.38), scripts/images/build_20-consulting-behavioral-interview-questions.py.",
    "anchor": "Behavioral interviewing is younger than most students assume",
})


# ---------------------------------------------------------------- 03 the five-part story shape
fig, ax = new_figure(width=11.0, height=5.6)
ax.axis("off")
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.text(0.04, 0.92, "Interviewers score the middle of the story", fontsize=17, fontweight="bold",
         color=TEXT_PRIMARY, va="center")
fig.text(0.04, 0.845, "The five parts every story follows, and the one part the follow-ups all land on.",
         fontsize=12.5, color=TEXT_SECONDARY, va="center")

parts = [
    ("1", "Setup", "Two sentences: where you were and what your role was.", 0.148),
    ("2", "Problem", "Stated plainly, with what was at stake.", 0.148),
    ("3", "Your actions", "In the first person, with at least one line of what you actually said.", 0.26),
    ("4", "Result", "With a number.", 0.13),
    ("5", "What changed", "One sentence on what you'd do differently or how you work now.", 0.17),
]
FW, FH = 11.0, 5.6
x, gap = 0.04, 0.0175
box_y, box_h = 0.30, 0.40
for n, title, body, bw in parts:
    hot = n == "3"
    face, edge, ink, ink2 = ("white", GRID, TEXT_PRIMARY, TEXT_SECONDARY)
    if hot:
        face, edge, ink, ink2 = (BLUE, BLUE, "white", "white")
    fig.patches.append(FancyBboxPatch((x, box_y), bw, box_h, boxstyle="round,pad=0,rounding_size=0.012",
                                      transform=fig.transFigure, facecolor=face, edgecolor=edge, linewidth=2))
    fig.text(x + 0.016, box_y + box_h - 0.075, f"{n}  {title}", fontsize=14, fontweight="bold", color=ink, va="center")
    yy = box_y + box_h - 0.15
    width_chars = int(bw * 112)
    for line in textwrap.wrap(body, width_chars):
        fig.text(x + 0.016, yy, line, fontsize=11.5, color=ink2, va="center")
        yy -= 0.046
    if n != "5":
        a = FancyArrowPatch((x + bw + 0.002, box_y + box_h / 2), (x + bw + gap - 0.002, box_y + box_h / 2),
                            transform=fig.transFigure, arrowstyle="-|>", mutation_scale=14, color=TEXT_MUTED, linewidth=1.8)
        fig.patches.append(a)
    if hot:
        hot_x, hot_w = x, bw
    x += bw + gap

# the bracket under the actions box
bx0, bx1 = hot_x + 0.01, hot_x + hot_w - 0.01
fig.patches.append(FancyArrowPatch((bx0, box_y - 0.03), (bx1, box_y - 0.03), transform=fig.transFigure,
                                   arrowstyle="-", color=BLUE, linewidth=2.5))
for bx in (bx0, bx1):
    fig.patches.append(FancyArrowPatch((bx, box_y - 0.03), (bx, box_y - 0.005), transform=fig.transFigure,
                                       arrowstyle="-", color=BLUE, linewidth=2.5))
fig.text((bx0 + bx1) / 2, box_y - 0.085, "Scored here. Every follow-up is “what did you say next?”",
         fontsize=12.5, fontweight="bold", color=TEXT_PRIMARY, ha="center", va="center")
fig.text(0.04, 0.09, "Most students spend their prep time on the setup and the ending. The interviewer is waiting for the middle.",
         fontsize=11.5, color=TEXT_SECONDARY, va="center")
save_figure(fig, OUT / "03-five-part-story-shape.png", tight=False)
entries.append({
    "file": "03-five-part-story-shape.png",
    "alt": "Five boxes for setup, problem, your actions, result and what changed, with the actions box highlighted as the scored part.",
    "caption": "Every story has the same five parts, and the follow-ups all land in the third one, so write the actions out before you practice the rest.",
    "method": "Matplotlib text diagram from the article's five-part story list, scripts/images/build_20-consulting-behavioral-interview-questions.py.",
    "anchor": "- One sentence on what you'd do differently or what changed ",
})

write_manifest(OUT, entries)
print(f"wrote {len(entries)} images to {OUT}")
