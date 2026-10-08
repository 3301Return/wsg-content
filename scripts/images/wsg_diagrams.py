#!/usr/bin/env python3
"""Diagram helpers on top of wsg_viz (October 2026, case-interview articles).

Boxes, arrows, issue trees, funnels, waterfalls and calendar timelines drawn with
matplotlib in the house style. Coordinates on a diagram canvas are inches, so a
10 x 6 canvas is a 10 by 6 inch figure (2000 x 1200 px at 200 dpi) and font sizes
in points relate to box sizes predictably (72 pt = 1 inch).

Usage:
    import sys; sys.path.insert(0, "scripts/images")
    from wsg_viz import *
    from wsg_diagrams import *
    fig, ax = canvas(10, 6)
    text_box(ax, 1, 4, 3, 1, "Application", fill=BLUE, text_color="white")
    arrow(ax, (4, 4.5), (5, 4.5))
    finish(fig, "published/assets/images/slug/01-name.png")
"""
import textwrap
from pathlib import Path

from wsg_viz import (AQUA, BLUE, GRID, ORANGE, PNG_DPI, SEQ_BLUE, SURFACE, TEXT_MUTED,
                     TEXT_PRIMARY, TEXT_SECONDARY, YELLOW, new_figure, save_figure)

import matplotlib
matplotlib.rcParams["text.parse_math"] = False   # "$36M" and "$18M" in one string must never become mathtext
matplotlib.rcParams["axes.unicode_minus"] = False

RED = "#e34948"           # the warm pole of the diverging pair, used for decreases
PALE_BLUE = "#e9f2fc"     # box fill behind primary text
PALE_ORANGE = "#fdeee6"
PALE_GRAY = "#f2f1ee"
LINE = "#b9b8b3"          # connector lines, one step darker than the grid
MAX_W_PX = 2200


# ---------------------------------------------------------------- canvas
def canvas(width, height, title=None, title_size=18):
    """A blank diagram canvas in inch coordinates: (0,0) bottom left, (width,height) top right."""
    fig, ax = new_figure(width=width, height=height)
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.grid(False)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    if title:
        ax.text(0.35, height - 0.35, title, ha="left", va="top", fontsize=title_size,
                fontweight="bold", color=TEXT_PRIMARY)
    return fig, ax


def finish(fig, out_path, tight=True):
    """Save, then enforce the 2200 px width cap (bbox_inches='tight' can add a few pixels)."""
    out = save_figure(fig, out_path, tight=tight)
    from PIL import Image
    im = Image.open(out)
    if im.width > MAX_W_PX:
        ratio = MAX_W_PX / im.width
        im = im.convert("RGB").resize((MAX_W_PX, int(round(im.height * ratio))), Image.LANCZOS)
        im.save(out, "PNG", optimize=True)
    return out


# ---------------------------------------------------------------- text helpers
def wrap(text, width_in, fontsize, bold=False):
    """Wrap text to fit width_in inches at fontsize pt (Arial averages about 0.5 em per character)."""
    em_per_char = 0.52 if bold else 0.49
    chars = max(8, int(width_in * 72 / (fontsize * em_per_char)))
    lines = []
    for para in text.split("\n"):
        lines.extend(textwrap.wrap(para, chars) or [""])
    return "\n".join(lines)


def label(ax, x, y, text, size=13, color=TEXT_PRIMARY, ha="left", va="center", bold=False,
          italic=False, wrap_in=None, linespacing=1.25):
    if wrap_in:
        text = wrap(text, wrap_in, size, bold)
    return ax.text(x, y, text, ha=ha, va=va, fontsize=size, color=color,
                   fontweight="bold" if bold else "normal", fontstyle="italic" if italic else "normal",
                   linespacing=linespacing)


def text_box(ax, x, y, w, h, text, fill=PALE_BLUE, edge=None, text_color=TEXT_PRIMARY, size=13,
             bold=False, radius=0.08, pad_in=0.12, ha="center", lw=1.0, linespacing=1.25, zorder=3):
    """A rounded box with wrapped, centered text. (x, y) is the bottom-left corner."""
    from matplotlib.patches import FancyBboxPatch
    box = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={radius}",
                         facecolor=fill, edgecolor=edge or fill, linewidth=lw, zorder=zorder)
    ax.add_patch(box)
    t = wrap(text, w - 2 * pad_in, size, bold)
    tx = x + w / 2 if ha == "center" else x + pad_in
    ax.text(tx, y + h / 2, t, ha=ha, va="center", fontsize=size, color=text_color,
            fontweight="bold" if bold else "normal", linespacing=linespacing, zorder=zorder + 1)
    return box


def arrow(ax, p1, p2, color=TEXT_SECONDARY, lw=1.8, head=18, style="-|>", connection="arc3,rad=0",
          zorder=2):
    ax.annotate("", xy=p2, xytext=p1,
                arrowprops=dict(arrowstyle=style, color=color, lw=lw, mutation_scale=head,
                                shrinkA=0, shrinkB=0, connectionstyle=connection),
                zorder=zorder)


def line(ax, p1, p2, color=LINE, lw=1.6, zorder=1):
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, lw=lw, solid_capstyle="round", zorder=zorder)


def elbow(ax, p1, p2, color=LINE, lw=1.6, zorder=1):
    """Horizontal-then-vertical-then-horizontal connector from a parent's right edge to a child's left edge."""
    xm = (p1[0] + p2[0]) / 2
    ax.plot([p1[0], xm, xm, p2[0]], [p1[1], p1[1], p2[1], p2[1]], color=color, lw=lw,
            solid_joinstyle="round", zorder=zorder)


# ---------------------------------------------------------------- issue tree
def tree_height(branches, box_h=0.62, gap=0.14):
    """Vertical inches an issue_tree with these branches needs (leaves stacked, branches separated by 2 gaps)."""
    total = 0
    for _, leaves in branches:
        total += len(leaves) * (box_h + gap) - gap
    total += (len(branches) - 1) * gap * 3
    return total


def issue_tree(ax, root, branches, x0=0.35, y_top=None, root_w=2.3, branch_w=2.4, leaf_w=3.0,
               box_h=0.62, gap=0.14, size=12.5, leaf_size=11.5, root_fill=BLUE, branch_fill=PALE_BLUE,
               leaf_fill=PALE_GRAY, canvas_h=None, col_gap=0.45):
    """Draw a left-to-right issue tree.

    root: text. branches: list of (branch_text, [leaf_text, ...]).
    Leaves are stacked top to bottom; each branch box centers on its leaves.
    Size the canvas with tree_height() first. Returns the y where the tree ends.
    """
    leaf_h = box_h
    y = y_top if y_top is not None else canvas_h - 0.9
    leaf_x = x0 + root_w + col_gap + branch_w + col_gap
    branch_x = x0 + root_w + col_gap
    branch_centers = []
    for b_text, leaves in branches:
        tops = []
        for leaf in leaves:
            text_box(ax, leaf_x, y - leaf_h, leaf_w, leaf_h, leaf, fill=leaf_fill, size=leaf_size,
                     ha="left", pad_in=0.12)
            tops.append(y - leaf_h / 2)
            y -= leaf_h + gap
        cy = sum(tops) / len(tops)
        branch_centers.append(cy)
        bh = max(box_h, min(len(leaves) * (leaf_h + gap) - gap, 1.6))
        text_box(ax, branch_x, cy - bh / 2, branch_w, bh, b_text, fill=branch_fill, size=size, bold=True)
        for t in tops:
            elbow(ax, (branch_x + branch_w, cy), (leaf_x, t))
        y -= gap * 2
    root_cy = sum(branch_centers) / len(branch_centers)
    rh = 1.1
    text_box(ax, x0, root_cy - rh / 2, root_w, rh, root, fill=root_fill, text_color="white", size=size + 1,
             bold=True)
    for cy in branch_centers:
        elbow(ax, (x0 + root_w, root_cy), (branch_x, cy))
    return y


# ---------------------------------------------------------------- nested tree (any depth)
# Added October 5, 2026 for the MECE guide, whose trees run three and four levels deep and
# whose nodes vary in length. issue_tree() above is unchanged; this is the general case.
#
#   root = N("Profit fell $13.9M", [
#              N("Revenue fell $2.7M", [N("Volume: ..."), N("Price: ...")]),
#              N("Costs rose $11.2M",  [N("Food ..."), N("Labor ...", [N("Hours ..."), N("Wage ...")])]),
#          ])
#   W, H = tree_extent(root, col_w=[2.2, 2.4, 3.2, 3.0])
#   fig, ax = canvas(W, H + 1.0, title="...")
#   nested_tree(ax, root, col_w=[2.2, 2.4, 3.2, 3.0], y_top=H + 1.0 - 0.9)
#
# Each depth is one column. A node's box is as tall as its wrapped text needs (never less than
# min_h); a parent centers on its children; siblings at depth d are separated by gap[d] so the
# top-level branches sit further apart than the leaves. Fills by depth: navy root with white
# text, pale blue, pale gray, then white with a gray edge.

def N(text, children=None, fill=None, text_color=None, size=None, bold=None, edge=None):
    """A tree node for nested_tree(): text plus optional children and per-node style overrides."""
    return {"text": text, "children": list(children or []), "fill": fill, "text_color": text_color,
            "size": size, "bold": bold, "edge": edge}


DEFAULT_TREE_FILLS = [(BLUE, "white", None), (PALE_BLUE, TEXT_PRIMARY, None), (PALE_GRAY, TEXT_PRIMARY, None),
                      ("white", TEXT_PRIMARY, LINE)]


def _node_box_h(node, depth, col_w, sizes, min_h, pad_v, pad_in, line_sp, bold_depth):
    at = lambda seq, i: seq[min(i, len(seq) - 1)]
    size = node["size"] or at(sizes, depth)
    bold = node["bold"] if node["bold"] is not None else depth <= bold_depth
    text = wrap(node["text"], at(col_w, depth) - 2 * pad_in, size, bold)
    n_lines = text.count("\n") + 1
    return max(at(min_h, depth), n_lines * size / 72 * line_sp + 2 * pad_v), text, size, bold


def _measure(node, depth, cfg):
    col_w, sizes, gaps, min_h, pad_v, pad_in, line_sp, bold_depth = cfg
    box_h, text, size, bold = _node_box_h(node, depth, col_w, sizes, min_h, pad_v, pad_in, line_sp, bold_depth)
    node["_box_h"], node["_wrapped"], node["_size"], node["_bold"] = box_h, text, size, bold
    if node["children"]:
        gap = gaps[min(depth + 1, len(gaps) - 1)]
        kids = sum(_measure(c, depth + 1, cfg) for c in node["children"]) + gap * (len(node["children"]) - 1)
        node["_sub_h"] = max(box_h, kids)
        node["_kids_h"] = kids
    else:
        node["_sub_h"] = box_h
        node["_kids_h"] = 0
    return node["_sub_h"]


def tree_extent(root, col_w=(2.2, 2.4, 3.0, 3.0), sizes=(13.5, 12.5, 11.5, 11.5), gaps=(0.0, 0.34, 0.14, 0.1),
                min_h=(0.9, 0.62, 0.5, 0.46), pad_v=0.11, pad_in=0.12, line_sp=1.22, bold_depth=1, col_gap=0.45,
                x0=0.35, **_ignored):
    """(width, height) in inches that nested_tree() with these settings needs, not counting a title or a note."""
    cfg = (list(col_w), list(sizes), list(gaps), list(min_h), pad_v, pad_in, line_sp, bold_depth)
    h = _measure(root, 0, cfg)
    depth = _depth(root)
    w = x0 * 2 + sum(col_w[min(d, len(col_w) - 1)] for d in range(depth + 1)) + col_gap * depth
    return w, h


def _depth(node):
    return 0 if not node["children"] else 1 + max(_depth(c) for c in node["children"])


def nested_tree(ax, root, y_top, col_w=(2.2, 2.4, 3.0, 3.0), sizes=(13.5, 12.5, 11.5, 11.5),
                gaps=(0.0, 0.34, 0.14, 0.1), min_h=(0.9, 0.62, 0.5, 0.46), pad_v=0.11, pad_in=0.12, line_sp=1.22,
                bold_depth=1, col_gap=0.45, x0=0.35, fills=None, col_labels=None, col_label_size=11,
                leaf_ha="left", radius=0.08, center_depth=1):
    """Draw a left-to-right tree of N() nodes, any depth. y_top is the top edge of the tree.

    col_w, sizes, gaps and min_h are per depth (the last value repeats). gaps[d] is the vertical
    space between siblings at depth d. fills: list of (fill, text_color, edge) per depth.
    Text is centered down to center_depth and aligned leaf_ha (a list) below it; bold down to bold_depth.
    col_labels: optional text written above each column (e.g. "Level 1: by channel").
    Returns the y where the tree ends (its bottom edge).
    """
    cfg = (list(col_w), list(sizes), list(gaps), list(min_h), pad_v, pad_in, line_sp, bold_depth)
    _measure(root, 0, cfg)
    fills = fills or DEFAULT_TREE_FILLS
    at = lambda seq, i: seq[min(i, len(seq) - 1)]
    xs = []
    x = x0
    for d in range(_depth(root) + 1):
        xs.append(x)
        x += at(col_w, d) + col_gap
    if col_labels:
        for d, lab in enumerate(col_labels):
            if lab:
                ax.text(xs[d], y_top + 0.12, lab, ha="left", va="bottom", fontsize=col_label_size,
                        color=TEXT_SECONDARY, fontstyle="italic")

    from matplotlib.patches import FancyBboxPatch

    def draw(node, depth, top):
        w = at(col_w, depth)
        fill, tcolor, edge = at(fills, depth)
        fill = node["fill"] or fill
        tcolor = node["text_color"] or tcolor
        edge = node["edge"] or edge
        sub_h, box_h = node["_sub_h"], node["_box_h"]
        cy = top - sub_h / 2
        bx = xs[depth]
        box = FancyBboxPatch((bx, cy - box_h / 2), w, box_h, boxstyle=f"round,pad=0,rounding_size={radius}",
                             facecolor=fill, edgecolor=edge or fill, linewidth=1.0, zorder=3)
        ax.add_patch(box)
        ha = "center" if depth <= center_depth else leaf_ha      # top levels centered, deeper nodes read as a list
        tx = bx + w / 2 if ha == "center" else bx + pad_in
        ax.text(tx, cy, node["_wrapped"], ha=ha, va="center", fontsize=node["_size"], color=tcolor,
                fontweight="bold" if node["_bold"] else "normal", linespacing=line_sp, zorder=4)
        if node["children"]:
            gap = at(gaps, depth + 1)
            y = top - (sub_h - node["_kids_h"]) / 2
            for c in node["children"]:
                c_top = y
                draw(c, depth + 1, c_top)
                elbow(ax, (bx + w, cy), (xs[depth + 1], c_top - c["_sub_h"] / 2))
                y -= c["_sub_h"] + gap
        return cy

    draw(root, 0, y_top)
    return y_top - root["_sub_h"]


# ---------------------------------------------------------------- waterfall
def waterfall(ax, steps, start, start_label, end_label, fmt="${:,.1f}M", ylabel=None, title=None,
              label_size=12, totals_color=TEXT_MUTED, up_color=BLUE, down_color=RED, neg_fmt="(${:,.1f}M)",
              bar_w=0.62, ymin=None, legend_loc="upper right"):
    """A bridge chart: a start total, signed steps, an end total. Labels on every bar
    (bridges are sparse enough that selective labeling is the whole set)."""
    import numpy as np
    labels = [start_label] + [s[0] for s in steps] + [end_label]
    n = len(labels)
    xs = np.arange(n)
    run = start
    bottoms, heights, colors = [0], [start], [totals_color]
    for _, d in steps:
        if d >= 0:
            bottoms.append(run); heights.append(d); colors.append(up_color)
        else:
            bottoms.append(run + d); heights.append(-d); colors.append(down_color)
        run += d
    bottoms.append(0); heights.append(run); colors.append(totals_color)
    ax.bar(xs, heights, bottom=bottoms, width=bar_w, color=colors, zorder=3)
    # connectors
    level = start
    for i, (_, d) in enumerate(steps):
        ax.plot([xs[i] + bar_w / 2, xs[i + 1] - bar_w / 2], [level, level], color=LINE, lw=1.0, zorder=2)
        level += d
    ax.plot([xs[-2] + bar_w / 2, xs[-1] - bar_w / 2], [level, level], color=LINE, lw=1.0, zorder=2)
    # labels
    ax.annotate(fmt.format(start), (xs[0], start), ha="center", va="bottom", xytext=(0, 4),
                textcoords="offset points", fontsize=label_size, color=TEXT_PRIMARY, fontweight="bold")
    for i, (_, d) in enumerate(steps):
        top = bottoms[i + 1] + heights[i + 1]
        txt = fmt.format(d) if d >= 0 else neg_fmt.format(-d)
        ax.annotate(txt, (xs[i + 1], top), ha="center", va="bottom", xytext=(0, 4),
                    textcoords="offset points", fontsize=label_size, color=TEXT_PRIMARY)
    ax.annotate(fmt.format(run), (xs[-1], run), ha="center", va="bottom", xytext=(0, 4),
                textcoords="offset points", fontsize=label_size, color=TEXT_PRIMARY, fontweight="bold")
    ax.set_xticks(xs)
    slot_in = 8.4 / n - 0.12          # the plot is about 8.4 in wide on an 11 in figure
    tick_size = 11.5 if n <= 6 else 11
    ax.set_xticklabels([wrap(l, min(1.25, slot_in), tick_size) for l in labels], fontsize=tick_size)
    if ylabel:
        ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title, loc="left", pad=14)
    if ymin is not None:
        ax.set_ylim(bottom=ymin)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=totals_color, label="Total"), Patch(color=up_color, label="Increase"),
                       Patch(color=down_color, label="Decrease")], loc=legend_loc, ncol=3, frameon=False)
    return run


# ---------------------------------------------------------------- calendar timeline
def month_axis(ax, months, y, x0, x1, size=11.5):
    """Draw a horizontal month axis for the list of (label) months between x0 and x1."""
    n = len(months)
    step = (x1 - x0) / n
    ax.plot([x0, x1], [y, y], color=TEXT_SECONDARY, lw=1.4, zorder=2)
    for i, m in enumerate(months):
        xa = x0 + i * step
        ax.plot([xa, xa], [y - 0.06, y + 0.06], color=TEXT_SECONDARY, lw=1.2, zorder=2)
        ax.text(xa + step / 2, y - 0.16, m, ha="center", va="top", fontsize=size, color=TEXT_SECONDARY)
    ax.plot([x1, x1], [y - 0.06, y + 0.06], color=TEXT_SECONDARY, lw=1.2, zorder=2)
    return step


def month_x(x0, step, month_index, day_frac=0.5):
    """x of a point month_index months after the axis start, day_frac through the month."""
    return x0 + (month_index + day_frac) * step


__all__ = [n for n in dir() if not n.startswith("_")]
