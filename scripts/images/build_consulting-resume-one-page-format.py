#!/usr/bin/env python3
"""Images for drafts/draft-consulting-resume-one-page-format-v1.md (October 1, 2026).

Run from the repo root:  python3 scripts/images/build_consulting-resume-one-page-format.py

1. 01-mbb-screen-four-scores.png     the four things the MBB screen scores, in order
2. 02-alex-doe-page-callouts.png     Sample A (junior) page with five numbered callouts
3. 03-sam-doe-page-callouts.png      Sample B (sophomore) page with five numbered callouts

Idempotent: every run rewrites the three PNGs and the manifest.
"""
import sys
import textwrap
from pathlib import Path

sys.path.insert(0, "scripts/images")
from wsg_viz import *                      # noqa: F401,F403
from resume_callouts import *              # noqa: F401,F403
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

SLUG = "consulting-resume-one-page-format"
OUT = Path("published/assets/images") / SLUG
PDF_A = "published/assets/Sample Consulting Resume - Junior (Alex Doe).pdf"
PDF_B = "published/assets/Sample Consulting Resume - Sophomore (Sam Doe).pdf"
OUT.mkdir(parents=True, exist_ok=True)
entries = []


# ---------------------------------------------------------------- 01 the four scores, in order
fig, ax = new_figure(width=11.0, height=6.0)
ax.axis("off")
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.text(0.04, 0.93, "The MBB screen scores four things, in this order", fontsize=17,
         fontweight="bold", color=TEXT_PRIMARY, va="center")

# the fast pass strip
strip = FancyBboxPatch((0.04, 0.745), 0.92, 0.10, boxstyle="round,pad=0,rounding_size=0.012",
                       transform=fig.transFigure, facecolor="#f2f2f2",
                       edgecolor="none")
fig.patches.append(strip)
fig.text(0.06, 0.815, "First pass, a few seconds", fontsize=13, fontweight="bold", color=TEXT_PRIMARY, va="center")
fig.text(0.06, 0.773, "The top third of the page: school, GPA, major and your first job title. "
         "It sorts you into “read properly” or “no.”",
         fontsize=12, color=TEXT_SECONDARY, va="center")

arrow = FancyArrowPatch((0.5, 0.74), (0.5, 0.665), transform=fig.transFigure, arrowstyle="-|>",
                        mutation_scale=22, color=TEXT_MUTED, linewidth=2)
fig.patches.append(arrow)
fig.text(0.515, 0.705, "if you pass, the slower read scores:", fontsize=12, color=TEXT_SECONDARY, va="center")

scores = [
    ("Academics", "GPA, school, major rigor, sometimes test scores. The cheapest signal that you'll survive the case and the analytical work."),
    ("Leadership", "You ran something with people in it. Titles, team sizes, and whether you chose the role or were handed it."),
    ("Impact", "The number moved because you were there. \u201cFrom 40 to 110 in one semester\u201d beats \u201cmanaged the committee.\u201d"),
    ("Distinctive", "One line they remember after the sixtieth resume: a business you started, a ranking, a language you actually speak."),
]
from matplotlib.patches import Ellipse
FW, FH = 11.0, 6.0                     # figure inches, to keep badges circular
box_w, gap, x = 0.205, 0.0333, 0.04
box_y, box_h = 0.20, 0.44
d_in = 0.40                            # badge diameter in inches
for n, (title, body) in enumerate(scores, start=1):
    b = FancyBboxPatch((x, box_y), box_w, box_h, boxstyle="round,pad=0,rounding_size=0.012",
                       transform=fig.transFigure, facecolor="white", edgecolor=BLUE, linewidth=2.2)
    fig.patches.append(b)
    cx, cy = x + 0.018 + d_in / FW / 2, box_y + box_h - 0.07
    fig.patches.append(Ellipse((cx, cy), d_in / FW, d_in / FH, transform=fig.transFigure,
                               facecolor=BLUE, edgecolor="none"))
    fig.text(cx, cy, str(n), fontsize=15, fontweight="bold", color="white", ha="center", va="center")
    fig.text(cx + d_in / FW / 2 + 0.012, cy, title, fontsize=15, fontweight="bold", color=TEXT_PRIMARY, va="center")
    yy = box_y + box_h - 0.16
    for line in textwrap.wrap(body, 24):
        fig.text(x + 0.018, yy, line, fontsize=11.5, color=TEXT_SECONDARY, va="center")
        yy -= 0.044
    if n < 4:
        a = FancyArrowPatch((x + box_w + 0.004, box_y + box_h / 2), (x + box_w + gap - 0.004, box_y + box_h / 2),
                            transform=fig.transFigure, arrowstyle="-|>", mutation_scale=18, color=TEXT_MUTED, linewidth=2)
        fig.patches.append(a)
    x += box_w + gap
foot = ("The firms don't publish a scoring sheet. This is the order the read tends to happen in, across the "
        "students I've worked with and what the firms say about who they hire.")
for k, line in enumerate(textwrap.wrap(foot, 120)):
    fig.text(0.04, 0.115 - k * 0.045, line, fontsize=11.5, color=TEXT_SECONDARY, va="center")
save_figure(fig, OUT / "01-mbb-screen-four-scores.png", tight=False)
entries.append({
    "file": "01-mbb-screen-four-scores.png",
    "alt": "Diagram of the consulting resume screen: a fast first pass, then four ordered scores for academics, leadership, impact and distinctiveness.",
    "caption": "Academics get read first and the distinctive line last, so the top third of your page has to carry the first two scores on its own.",
    "method": "Matplotlib text diagram from the article's section on how the MBB screen scores a page (scripts/images/build_consulting-resume-one-page-format.py).",
    "anchor": "**4. Something distinctive comes last, and it's what gets yo",
})


# ---------------------------------------------------------------- 02 Sample A, Alex Doe
page, lines = load_page(PDF_A)
callouts = [
    (region(lines, "State University", last="Honors Program in Economics"),
     "Academics score first",
     "A 3.82, a 35 and a quantitative major clear the first filter in two seconds. This top third is all the fast pass sees."),
    (region(lines, "Summer Consultant (Received Return Offer)"),
     "A title the fast pass can read",
     "Recruiters spend more time on job titles than on anything else. The return offer goes in parentheses after the title."),
    (region(lines, "Sized the US market", last="final steering committee presentation"),
     "Every bullet ends in a result with a number",
     "$1.4Bn is checkable (14 million patients, tested twice a year, about $50 a test), and “became the base case” means the client's leadership used it.", "bl"),
    (region(lines, "LEADERSHIP & ACTIVITIES", until="ADDITIONAL INFORMATION"),
     "Leadership runs as long as Experience",
     "Three entries. The presidency gets three bullets because it has three kinds of evidence: growth (90 to 210), a program built (12 offers, up from 4) and a client result (70% to 92%)."),
    (region(lines, "ADDITIONAL INFORMATION", last="woodworking"),
     "Three lines, nothing generic",
     "Tools used in a role on the page, a language with honest proficiency, and interests specific enough to start a conversation."),
]
draw_callouts(page, callouts, OUT / "02-alex-doe-page-callouts.png")
entries.append({
    "file": "02-alex-doe-page-callouts.png",
    "alt": "Alex Doe sample resume with five numbered callouts on academics, the job title, first bullet, Leadership section and Additional Information.",
    "caption": "Run the screen on Alex's page: the fast pass sees a 3.82 and a strategy firm title, and the slower read finds a number at the end of every bullet.",
    "method": "Page 1 of published/assets/Sample Consulting Resume - Junior (Alex Doe).pdf rendered with pdftoppm at 150 dpi; callouts drawn with Pillow from pdfplumber line positions (scripts/images/resume_callouts.py).",
    "anchor": "That's the whole page. Eleven bullets across Experience and ",
})


# ---------------------------------------------------------------- 03 Sample B, Sam Doe
page, lines = load_page(PDF_B)
callouts = [
    (region(lines, "Bachelor of Science in Applied Mathematics", last="SAT: 1540"),
     "Academics clear the first filter",
     "A 3.91, a 1540 and a math major pass the fast pass in two seconds, with no internship anywhere on the page."),
    (region(lines, "State University Department of Economics", last="extra year of data"),
     "A research job shows you can work and finish",
     "2.1 million records and “two weeks ahead of schedule” are the lines that show a large, messy dataset handled under someone else's deadline."),
    (region(lines, "Family-Owned Landscaping Business", last="second truck the following spring"),
     "A family business, written as a consultant would",
     "Problem (overtime), tool (a schedule), result (30% fewer overtime hours, same jobs). Then cash: days to payment from 34 to 12, spent on a second truck. This is the line a screener remembers."),
    (region(lines, "Residence Hall Association", last="over the same period"),
     "Leadership and impact from an elected role",
     "A $48,000 budget across 14 halls is a real organization. Approval time from 3 weeks to 5 days and attendance from 900 to 1,500 are the before and after."),
    (region(lines, "First-Year Case Competition", last="judges"),
     "A placement is a real number",
     "1st of 18 teams, what Sam personally built (the breakeven analysis), and who judged it."),
]
draw_callouts(page, callouts, OUT / "03-sam-doe-page-callouts.png")
entries.append({
    "file": "03-sam-doe-page-callouts.png",
    "alt": "Sam Doe sample sophomore resume with five numbered callouts on academics, research job, family business, elected role and case competition.",
    "caption": "Not one bullet on Sam's page says consulting, and it still passes, because every box holds a number that moved.",
    "method": "Page 1 of published/assets/Sample Consulting Resume - Sophomore (Sam Doe).pdf rendered with pdftoppm at 150 dpi; callouts drawn with Pillow from pdfplumber line positions (scripts/images/resume_callouts.py).",
    "anchor": "Nine bullets, one page, and not one of them says \"consulting",
})

write_manifest(OUT, entries)
print(f"wrote {len(entries)} images to {OUT}")
