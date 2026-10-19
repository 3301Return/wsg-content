#!/usr/bin/env python3
"""Images for drafts/draft-credit-analyst-interview-questions-20-v1.md (October 11, 2026).

Run from the repo root:  python3 scripts/images/build_credit-analyst-interview-questions-20.py
Idempotent: rewrites every PNG in published/assets/images/credit-analyst-interview-questions-20/
and the folder's manifest.json. The draft is never edited; the coordinator inserts the image
lines from the manifest anchors with scripts/images/insert_images.py.

Every number comes from the draft: the question 6 cushion table, the question 7 recovery
figures, the question 12 rating table, the question 15 loan-versus-bond table and the
question 20 downside table. Each one is read back out of the draft and compared with the
figures drawn here, so an edit to the draft fails this build instead of leaving a stale image.
Banking format throughout (images.md, October 7, 2026): black Arial text, no gridlines,
no boxes or frames around charts, direct labels, source line bottom-left.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts" / "images"))
from wsg_viz import *          # noqa: E402,F401,F403
from wsg_diagrams import canvas, finish, wrap, label  # noqa: E402

import matplotlib  # noqa: E402
matplotlib.rcParams["text.parse_math"] = False      # "$83.3" must never be read as mathtext
matplotlib.rcParams["axes.unicode_minus"] = False   # hyphen-minus only

SLUG = "credit-analyst-interview-questions-20"
OUT = ROOT / "published" / "assets" / "images" / SLUG
DRAFT = ROOT / "drafts" / f"draft-{SLUG}-v1.md"
TEXT = DRAFT.read_text(encoding="utf-8")
LINES = TEXT.split("\n")
PALE = ["#dbe7f3", "#e4edf6", "#edf2f8", "#f3f3f3", "#f7f7f7", "#fbfbfb"]   # pale fills behind black text
WSG_SOURCE = "Source: WSG analysis of the worked example in this article"
entries = []


# ---------------------------------------------------------------- the draft's numbers, transcribed
Q6_ROWS = [
    ["Leverage (debt / EBITDA)", "6.0x maximum", "5.0x", "$83.3", "$16.7, or 16.7 percent"],
    ["Interest coverage (EBITDA / interest)", "2.0x minimum", "3.3x", "$60.0", "$40.0, or 40 percent"],
]
Q7 = {"trading_loan": 65, "trading_bond": 38, "ultimate_loan": 71, "ultimate_bond": 47}
Q12_ROWS = [
    ["Aaa", "AAA", "Investment grade"],
    ["Aa1, Aa2, Aa3", "AA+, AA, AA-", "Investment grade"],
    ["A1, A2, A3", "A+, A, A-", "Investment grade"],
    ["Baa1, Baa2, Baa3", "BBB+, BBB, BBB-", "Investment grade (lowest)"],
    ["Ba1, Ba2, Ba3", "BB+, BB, BB-", "Speculative grade"],
    ["B1, B2, B3", "B+, B, B-", "Speculative grade"],
    ["Caa, Ca, C", "CCC, CC, C, D", "Speculative grade (near or in default)"],
]
Q15_ROWS = [
    ["Interest", "Floating: SOFR plus a spread", "Fixed coupon"],
    ["Security", "Usually secured, first lien", "Usually unsecured"],
    ["Repayment", "Amortizes, plus mandatory prepayments", "Bullet at maturity"],
    ["Call protection", "Callable any time; at best a 101 soft call for six months or a year", "Non-call for 2 to 5 years, then declining premiums"],
    ["Covenants", "Springing maintenance test on the revolver, otherwise incurrence", "Incurrence only"],
    ["Buyers", "Institutional loan accounts", "Bond investors"],
]
Q20_ROWS = [
    ["EBITDA", "50.0", "35.0"],
    ["Less: cash interest (9 percent on $250 million)", "(22.5)", "(22.5)"],
    ["Less: capex", "(5.0)", "(5.0)"],
    ["Less: cash taxes", "(5.0)", "(2.0)"],
    ["Free cash flow before principal", "17.5", "5.5"],
    ["Less: amortization (1 percent)", "(2.5)", "(2.5)"],
    ["Cash left after debt service", "15.0", "3.0"],
    ["FCCR", "1.60x", "1.12x"],
    ["Leverage (debt / EBITDA)", "5.0x", "7.1x"],
]


# ---------------------------------------------------------------- checks against the draft
def draft_table(first_cell):
    """Rows of the markdown table whose first data row starts with first_cell, as lists of cell strings."""
    rows, inside = [], False
    for ln in LINES:
        if ln.startswith("| " + first_cell):
            inside = True
        if inside:
            if not ln.startswith("|"):
                break
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue
            rows.append(cells)
    return rows


def check_draft():
    assert draft_table("Leverage (debt / EBITDA) | 6.0x") == Q6_ROWS, "question 6 table changed in the draft"
    assert draft_table("Aaa |") == Q12_ROWS, "question 12 table changed in the draft"
    assert draft_table("Interest | Floating") == Q15_ROWS, "question 15 table changed in the draft"
    assert draft_table("EBITDA | 50.0") == Q20_ROWS, "question 20 table changed in the draft"
    q7 = re.search(r"first-lien loans recovering about (\d+) cents on the dollar against (\d+) cents for senior unsecured bonds", TEXT)
    assert q7 and (int(q7.group(1)), int(q7.group(2))) == (Q7["trading_loan"], Q7["trading_bond"]), "question 7 trading-price recoveries changed"
    q7b = re.search(r"1987 to 2023, term loans recovered (\d+) percent and senior unsecured bonds (\d+) percent", TEXT)
    assert q7b and (int(q7b.group(1)), int(q7b.group(2))) == (Q7["ultimate_loan"], Q7["ultimate_bond"]), "question 7 ultimate recoveries changed"
    assert "trading-price recoveries from 1983 to 2023" in TEXT, "question 7 trading-price period changed"
    # the question 6 arithmetic the bars are drawn from
    assert "$500 divided by 6.0, which is $83.3" in TEXT and "2.0 times $30, which is $60" in TEXT
    assert "EBITDA can fall by $16.7" in TEXT and "EBITDA can fall by $40" in TEXT
    assert "$100 of EBITDA and $500 of debt at 6 percent" in TEXT
    # the question 20 bridge adds up
    assert 50.0 - 22.5 - 5.0 - 5.0 == 17.5 and 35.0 - 22.5 - 5.0 - 2.0 == 5.5
    assert 17.5 - 2.5 == 15.0 and 5.5 - 2.5 == 3.0
    assert round((50 - 5 - 5) / (22.5 + 2.5), 2) == 1.60 and round((35 - 5 - 2) / (22.5 + 2.5), 2) == 1.12
    assert round(250 / 50, 1) == 5.0 and round(250 / 35, 1) == 7.1
    print("draft checks: questions 6, 7, 12, 15 and 20 all match the figures drawn")


def anchor_for(prefix):
    hits = [ln for ln in LINES if ln.startswith(prefix)]
    assert len(hits) == 1, f"anchor prefix matches {len(hits)} lines: {prefix!r}"
    ln = hits[0]
    assert not ln.lstrip().startswith(("|", "-", "*", ">", "#")) and not re.match(r"^\s*\d+\.\s", ln), f"anchor is a list, table, quote or heading: {prefix!r}"
    return ln[:60]


def add(file, alt, caption, source, method, anchor):
    entries.append({"file": file, "alt": alt, "caption": caption, "source": source, "method": method, "anchor": anchor})


# ---------------------------------------------------------------- a wrapped table in the banking format
def wrapped_table(header, rows, out_path, title=None, source=None, col_w=None, col_align=None, size=12.5,
                  bold_rows=(), rule_after=None, rule_label=None, width=11.0, x0=0.35):
    """bank_table() with wrapped cells: black text, a rule under the header, a rule above any bold row,
    an optional labeled divider after row rule_after. col_w in inches."""
    n = len(header)
    col_w = col_w or [(width - 2 * x0) / n] * n
    col_align = col_align or ["left"] * n
    pad = 0.1
    def cell_text(text, i, bold=False):
        return wrap(str(text), col_w[i] - 2 * pad, size, bold)
    row_h = []
    for r, row in enumerate(rows):
        bold = r in bold_rows
        lines_n = max(cell_text(c, i, bold).count("\n") + 1 for i, c in enumerate(row))
        row_h.append(lines_n * size * 1.25 / 72 + 2 * pad + 0.06)
    head_h = max(cell_text(h, i, True).count("\n") + 1 for i, h in enumerate(header)) * size * 1.25 / 72 + 2 * pad + 0.06
    extra = 0.42 if rule_after is not None else 0
    H = 0.35 + (0.55 if title else 0) + head_h + sum(row_h) + extra + 0.5
    fig, ax = canvas(width, H)
    y = H - 0.3
    if title:
        ax.text(x0, y, title, ha="left", va="top", fontsize=16, fontweight="bold", color=BLACK)
        y -= 0.55
    xs = []
    x = x0
    for w in col_w:
        xs.append(x)
        x += w
    def put_row(cells, top, h, bold):
        for i, c in enumerate(cells):
            t = cell_text(c, i, bold)
            if col_align[i] == "right":
                ax.text(xs[i] + col_w[i] - pad, top - h / 2, t, ha="right", va="center", fontsize=size, color=BLACK,
                        fontweight="bold" if bold else "normal", linespacing=1.25)
            else:
                ax.text(xs[i] + pad, top - h / 2, t, ha="left", va="center", fontsize=size, color=BLACK,
                        fontweight="bold" if bold else "normal", linespacing=1.25)
    put_row(header, y, head_h, True)
    y -= head_h
    ax.plot([x0, width - x0], [y, y], color=BLACK, lw=0.9)
    for r, (row, h) in enumerate(zip(rows, row_h)):
        bold = r in bold_rows
        if bold:
            ax.plot([x0, width - x0], [y, y], color=BLACK, lw=0.7)
        put_row(row, y, h, bold)
        y -= h
        if rule_after is not None and r == rule_after:
            ax.plot([x0, width - x0], [y - 0.06, y - 0.06], color=BLACK, lw=1.2, ls=(0, (4, 2)))
            if rule_label:
                ax.text(width - x0, y - 0.1, rule_label, ha="right", va="top", fontsize=11, color=BLACK, fontstyle="italic")
            y -= extra
    if source:
        add_source(fig, source)
    return finish(fig, out_path)


# ---------------------------------------------------------------- 01 capital structure and recovery
def capital_structure():
    W, H = 11.0, 5.7
    fig, ax = canvas(W, H, title="Order of payment in a bankruptcy, with Moody's recovery rates", title_size=16)
    stack = ["Revolver and first-lien term loans (paid first)",
             "Second-lien loans (junior claim on the same collateral)",
             "Senior unsecured bonds",
             "Subordinated debt: mezzanine, PIK notes, vendor notes",
             "Preferred stock",
             "Common equity (paid last)"]
    x, w, bh, gap = 0.35, 4.4, 0.66, 0.1
    y = H - 1.0
    from matplotlib.patches import FancyBboxPatch
    for i, text in enumerate(stack):
        ax.add_patch(FancyBboxPatch((x, y - bh), w, bh, boxstyle="round,pad=0,rounding_size=0.06",
                                    facecolor=PALE[i], edgecolor=PALE[i], zorder=2))
        ax.text(x + 0.15, y - bh / 2, wrap(text, w - 0.3, 12), ha="left", va="center", fontsize=12, color=BLACK, zorder=3)
        y -= bh + gap
    top_y, bot_y = H - 1.0, y + gap
    ax.annotate("", xy=(x + w + 0.25, bot_y), xytext=(x + w + 0.25, top_y),
                arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.2, mutation_scale=16))
    ax.text(x + w + 0.33, (top_y + bot_y) / 2, "Paid first\nto last", ha="left", va="center", fontsize=11, color=BLACK, linespacing=1.3)

    # recovery bars, right side
    rx, max_w = 6.55, 2.9
    ax.text(rx, H - 1.0, "Recovery, cents on the dollar", ha="left", va="top", fontsize=12.5, fontweight="bold", color=BLACK)
    groups = [("First-lien term loans", Q7["trading_loan"], Q7["ultimate_loan"]),
              ("Senior unsecured bonds", Q7["trading_bond"], Q7["ultimate_bond"])]
    yb = H - 1.55
    for name, trading, ultimate in groups:
        ax.text(rx, yb, name, ha="left", va="center", fontsize=12, fontweight="bold", color=BLACK)
        yb -= 0.42
        for lab, val, col in [("Price after default, 1983 to 2023", trading, NAVY),
                              ("What lenders finally got back, 1987 to 2023", ultimate, LIGHT_BLUE)]:
            ax.text(rx, yb, lab, ha="left", va="center", fontsize=10.5, color=BLACK)
            yb -= 0.3
            bw = max_w * val / 100
            ax.add_patch(FancyBboxPatch((rx, yb - 0.11), bw, 0.22, boxstyle="square,pad=0", facecolor=col, edgecolor=col, zorder=2))
            ax.text(rx + bw + 0.08, yb, f"{val}%", ha="left", va="center", fontsize=12, color=BLACK, fontweight="bold")
            yb -= 0.4
        yb -= 0.2
    add_source(fig, "Source: Bermuda Monetary Authority, Moody's recovery rates for loans and bonds, September 2024")
    finish(fig, OUT / "01-capital-structure-recovery.png")
    add("01-capital-structure-recovery.png",
        "Diagram of the capital structure from revolver to common equity with Moody's recovery rates for loans and bonds",
        "First-lien loans recovered 65 cents on the dollar against 38 for senior unsecured bonds, on Moody's trading prices.",
        "Bermuda Monetary Authority, Moody's recovery rates for loans and bonds, September 2024",
        "Diagram drawn in matplotlib from the question 7 stack and the four Moody's recovery figures in the draft (65, 38, 71, 47 percent)",
        anchor_for("The revolver and first-lien term loans have the first claim"))


# ---------------------------------------------------------------- 02 rating scales
def rating_scales():
    wrapped_table(["Moody's", "S&P", "Grade"], Q12_ROWS, OUT / "02-rating-scales.png",
                  title="Moody's and S&P rating scales", col_w=[3.0, 3.0, 4.3],
                  rule_after=3, rule_label="Investment grade ends at Baa3 and BBB-",
                  source="Source: Moody's and S&P Global Ratings, rating symbols and definitions, October 2026")
    add("02-rating-scales.png",
        "Table of Moody's and S&P rating symbols side by side with the investment grade line after Baa3 and BBB-",
        "Investment grade ends at Baa3 on Moody's scale and BBB- on S&P's.",
        "Moody's and S&P Global Ratings, rating symbols and definitions, October 2026",
        "Table graphic drawn in matplotlib from the question 12 rating table in the draft",
        anchor_for("Moody's rating symbols document says"))


# ---------------------------------------------------------------- 03 covenant cushion bars
def covenant_cushion():
    today, lev_limit, cov_limit = 100.0, 83.3, 60.0
    assert Q6_ROWS[0][3] == f"${lev_limit}" and Q6_ROWS[1][3] == f"${cov_limit}"
    fig, ax = new_figure(width=11.0, height=5.6)
    cats = ["EBITDA today", "Lowest EBITDA that\npasses the 6.0x\nleverage covenant", "Lowest EBITDA that\npasses the 2.0x\ninterest coverage covenant"]
    vals = [today, lev_limit, cov_limit]
    bars = ax.bar(range(3), vals, width=0.55, color=[GRAY, NAVY, MID_BLUE], zorder=3)
    bar_labels(ax, bars, fmt="${:,.1f}", fontsize=13)
    # cushion brackets
    for i, (lim, txt) in enumerate([(lev_limit, "Cushion: $16.7,\nor 16.7 percent"), (cov_limit, "Cushion: $40.0,\nor 40 percent")], start=1):
        xb = i + 0.42
        ax.plot([xb, xb], [lim, today], color=BLACK, lw=1.0, zorder=4)
        ax.plot([xb - 0.06, xb + 0.06], [lim, lim], color=BLACK, lw=1.0, zorder=4)
        ax.plot([xb - 0.06, xb + 0.06], [today, today], color=BLACK, lw=1.0, zorder=4)
        ax.text(xb + 0.1, (lim + today) / 2, txt, ha="left", va="center", fontsize=11.5, color=BLACK, linespacing=1.25)
    ax.plot([-0.5, 2.9], [today, today], color=BLACK, lw=0.8, ls=(0, (3, 3)), zorder=2)
    ax.set_xlim(-0.55, 3.4)
    ax.set_ylim(0, 118)
    ax.set_xticks(range(3))
    ax.set_xticklabels(cats, fontsize=12)
    style_axes(ax)
    ax.set_title("Leverage covenant breaks first: EBITDA can fall 16.7 percent", loc="left", pad=30, color=BLACK)
    ax.text(0, 1.01, "$ (borrower with $100 of EBITDA and $500 of debt at 6 percent)", transform=ax.transAxes, ha="left", va="bottom", fontsize=11.5, color=BLACK)
    add_source(fig, WSG_SOURCE)
    finish(fig, OUT / "03-covenant-cushion.png")
    add("03-covenant-cushion.png",
        "Bar chart of EBITDA today against the lowest EBITDA that passes the leverage and interest coverage covenants",
        "EBITDA can fall $16.7 before the 6.0x leverage test breaks and $40.0 before the 2.0x coverage test breaks.",
        "WSG analysis of the worked example in this article",
        "Bar chart drawn in matplotlib from the question 6 cushion table in the draft ($100 today, $83.3 and $60.0 at the limits)",
        anchor_for("The leverage covenant binds first."))


# ---------------------------------------------------------------- 04 loan versus bond
def loan_vs_bond():
    wrapped_table(["Feature", "Leveraged loan (term loan B)", "High-yield bond"], Q15_ROWS, OUT / "04-loan-vs-bond.png",
                  title="Leveraged loan vs high-yield bond", col_w=[2.0, 4.6, 3.7],
                  source="Source: WSG summary of PitchBook LCD's leveraged loan primer and Ashurst's loan and bond comparison, October 2026")
    add("04-loan-vs-bond.png",
        "Table comparing a leveraged loan and a high-yield bond on interest, security, repayment, call protection, covenants and buyers",
        "A leveraged loan floats, is secured and amortizes; a high-yield bond is fixed-rate, usually unsecured and repaid at maturity.",
        "WSG summary of PitchBook LCD's leveraged loan primer and Ashurst's loan and bond comparison, October 2026",
        "Table graphic drawn in matplotlib from the question 15 comparison table in the draft",
        anchor_for("A floating rate means the lender earns more"))


# ---------------------------------------------------------------- 05 downside case
def downside_case():
    rows = [r[:] for r in Q20_ROWS]
    rows[7][0] = "Fixed charge coverage (FCCR)"
    wrapped_table(["$ millions", "Base case", "EBITDA down 30 percent"], rows, OUT / "05-downside-case.png",
                  title="Downside case: EBITDA falls 30 percent", col_w=[5.3, 2.5, 2.5], col_align=["left", "right", "right"],
                  bold_rows=(4, 6), source=WSG_SOURCE)
    add("05-downside-case.png",
        "Table of the base case and the 30 percent EBITDA downside with cash flow, FCCR and leverage",
        "FCCR falls from 1.60x to 1.12x and leverage rises from 5.0x to 7.1x when EBITDA drops 30 percent.",
        "WSG analysis of the worked example in this article",
        "Table graphic drawn in matplotlib from the question 20 downside table in the draft",
        anchor_for("In the base case the borrower covers"))


# ---------------------------------------------------------------- manifest checks
def check_manifest():
    from PIL import Image
    for e in entries:
        for k in ("alt", "caption", "source", "method", "anchor"):
            for ch in (chr(0x2014), chr(0x2013), chr(0x2212)):
                assert ch not in e[k], f"dash in manifest {e['file']} {k}"
        n = len(e["alt"].split())
        assert 10 <= n <= 20, f"alt text of {e['file']} has {n} words"
        assert len(e["caption"].split()) <= 20, f"caption of {e['file']} is over 20 words"
        hits = [ln for ln in LINES if ln.strip().startswith(e["anchor"])]
        assert len(hits) == 1, f"anchor for {e['file']} matches {len(hits)} draft lines: {e['anchor']!r}"
        im = Image.open(OUT / e["file"])
        assert im.width <= 2200, f"{e['file']} is {im.width} px wide"
    src = Path(__file__).read_text(encoding="utf-8")
    assert not any(ord(c) in (0x2014, 0x2013, 0x2212) for c in src), "dash character in the build script"


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    check_draft()
    capital_structure()
    rating_scales()
    covenant_cushion()
    loan_vs_bond()
    downside_case()
    check_manifest()
    write_manifest(OUT, entries)
    print(f"wrote {len(entries)} images and manifest to {OUT.relative_to(ROOT)}")
