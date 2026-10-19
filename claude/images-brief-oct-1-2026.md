# Images brief: illustrations for the 10 October 1, 2026 articles

Repo root: `/home/claude/repo`. Today is October 1, 2026. Run everything from the repo root.

## What the founder asked for

"Relevant and important pictures and graphs" in the documents. For the model articles, "screenshots of sample Excel sheets, especially for topics like cash flow." Sourcing decision: screenshots of other people's models are copyrighted, but the models themselves aren't, so **rebuild the model in Excel with the numbers from our article, then screenshot our workbook.** Use the structure of the two free templates the articles link (A Simple Model's LBO: one sheet, sources and uses on top, then income statement, balance sheet, cash flow and debt schedule; Mergers & Inquisitions' Otis three statement file: a drivers block on top, then IS, BS, CFS with years across). Images go in the .docx files and as PNGs for Wix. Volume: 2 to 4 per article where they teach something, more where they help, no hard cap; the model articles get the most.

## Shared toolkit (use it, don't reinvent it)

`scripts/images/wsg_viz.py`. Read it first. It gives you:

- `new_figure()`, `style_axes()`, `bar_labels()`, `save_figure()`: the house chart style (Arial, the validated palette: `BLUE`, `ORANGE`, `AQUA`, `YELLOW`, a `SEQ_BLUE` ramp, `DIVERGING`, recessive grid, 2200 px wide at 200 dpi).
- `new_workbook()`, `put()`, `header_bar()`, `set_widths()`, `year_header()`, the `FMT_*` number formats: banker formatting for workbooks (blue hardcodes on pale yellow, black formulas, green links, navy section bars, totals with a top rule).
- `render_range(xlsx, sheet, "B2:H30", out_png)`: an Excel-looking screenshot of a range (row and column headings, gridlines, formulas recalculated by LibreOffice).
- `recalc_values(xlsx)`: the recalculated cell values, to check the workbook against the article's tables.
- `write_manifest(folder, entries)`.

Also load the `dataviz` skill with the Skill tool before drawing any chart and follow its form rules (one axis, no dual axes, categorical hues in the fixed order BLUE, ORANGE, AQUA, YELLOW, never cycled; sequential = one hue; a legend whenever there are two or more series; selective direct labels; nothing decorative). The palette in `wsg_viz.py` is the dataviz reference palette, already validated.

## Rules for every image

1. **Every number in an image matches the article.** Screenshots come from a workbook that reproduces the article's worked example cell for cell; charts are drawn from the article's own tables. Run `recalc_values()` on each workbook and compare against the article's tables before rendering. A screenshot with a number that disagrees with the text is worse than no screenshot.
2. **Original only, with two exceptions.** Build everything yourself. The exceptions: (a) a public domain or Creative Commons photo from Wikimedia Commons where a person is the hook (check the file page's license, record the URL and license in the manifest, put the credit in the caption); (b) a chart drawn from public data the article already cites (then the caption names the source). Never screenshot a third party's model, chart, slide or site.
3. **Captions and alt text.** Caption: one plain sentence in Stephen's voice, no "Figure N", no em or en dashes, says what the reader should notice. Alt text: 10 to 20 words describing the picture for a screen reader. Chart titles are short claims, not labels ("Paying one turn less adds six points of IRR").
4. **Files.** PNG, 2200 px wide at most, 200 dpi, white background. Path: `published/assets/images/{article-slug}/NN-short-name.png` (NN two digits in reading order). Workbooks: `scripts/images/models/{name}.xlsx` built by `scripts/images/models/build_{name}.py`. Your render script: `scripts/images/build_{article-slug}.py`, runnable from the repo root, idempotent. Write `published/assets/images/{article-slug}/manifest.json` with one entry per image: `file`, `alt`, `caption`, `method` (workbook range, chart from table X, Wikimedia URL and license), `anchor` (the first 60 characters of the draft line the image follows).
5. **Insert into the draft.** Add a line `![alt text](published/assets/images/{slug}/NN-name.png "Caption")` on its own, with a blank line before and after, directly after the paragraph, table or list it illustrates. Never inside a list, table or quote block. Keep the article text itself unchanged except for a short lead-in sentence where the image needs one ("Here's what that block looks like in the sheet.").
6. **No dashes.** No em or en dashes anywhere: not in captions, alt text, chart labels, cell labels or manifest text. Use "to" for ranges ("Year 1 to Year 5") and commas or periods elsewhere.
7. **No identifiers.** Nothing in a workbook, chart or PNG names a real student or carries personal metadata. Workbook author stays blank or "Wall Street Guide".
8. **Check the build.** After inserting the image lines, run `python3 scripts/markdown_to_docx_v2.py drafts/{file}.md /tmp/{slug}-check.docx` and confirm no "image not found" warning, then `python3 scripts/check_article.py` and `python3 scripts/check_style.py` on the draft. Do NOT write to `published/ai-written/`; the coordinator rebuilds those. Edit only your own draft(s), your own scripts and image folders.
9. **Report back** (under 400 words): each image with its anchor and what it shows, the workbook checks you ran (which article tables you matched, any mismatch), anything you decided not to illustrate and why, and the exact commands to rebuild your images.

## Excel screenshot style (model articles)

- One worksheet per model, laid out the way the article describes the test layout: assumptions on top, then the blocks in build order, years across, labels in column B, numbers from column D on, column A narrow. Section headers as navy bars (`header_bar`). Inputs blue on pale yellow, formulas black, totals bold with a top rule. Units stated once ("$ millions").
- Show formulas as live Excel formulas, not pasted values, so a reader who downloads nothing still sees how the cells connect. The screenshot shows values; add one extra screenshot per model with a formula visible (render a small range after writing the formula text into an adjacent cell as a label, e.g. `=D20-D21` shown in column J next to the row, with a "Formula" header).
- Keep each screenshot to one readable block (12 to 40 rows). A full-model screenshot is unreadable at article width.
- The circularity toggle, the balance check row and the revolver plug each get their own close-up where the article explains them.

## Assignments

| Agent | Articles (drafts in `drafts/`) | Slugs for image folders |
| --- | --- | --- |
| A | #1 `draft-lbo-model-explained-undergrad-v1.md` | `lbo-model-explained-undergrad` |
| B | #5 `draft-three-statement-model-modeling-test-v1.md` | `three-statement-model-modeling-test` |
| C | #4 `draft-net-working-capital-interview-v1.md`, #3 `draft-asset-management-interview-prep-undergrads-v1.md` | `net-working-capital-interview`, `asset-management-interview-prep-undergrads` |
| D | #2 `draft-finance-resume-template-banking-consulting-v1.md`, #6 `draft-consulting-resume-one-page-format-v1.md`, #7 `draft-20-consulting-behavioral-interview-questions-v1.md` | `finance-resume-template-banking-consulting`, `consulting-resume-one-page-format`, `20-consulting-behavioral-interview-questions` |
| E | #8 `draft-bain-case-interview-guide-v2.md`, #9 `draft-bcg-case-interview-guide-v2.md`, #10 `draft-10-case-interview-examples-worked-solutions-v1.md` | `bain-case-interview-guide`, `bcg-case-interview-guide`, `10-case-interview-examples-worked-solutions` |

### Agent A, LBO (aim for 7 to 10 images)

Build `scripts/images/models/build_targetco_lbo.py` -> `targetco-lbo.xlsx` reproducing the article's TargetCo model with formulas: transaction assumptions, sources and uses, the operating model (revenue to cash available for debt repayment), the debt schedule by tranche with beginning-balance interest (and a cell showing the average-balance alternative for Year 1 as the article does), the returns block (exit EV, net debt, equity, MOIC, IRR), the two sensitivity grids (compute the grid values in Python the way the article's writer did and write them as values, labeled as a data table), and a second sheet for the paper LBO. Screenshots: sources and uses; operating model; debt schedule; returns; each sensitivity grid; paper LBO; one formula close-up. Charts: debt balance by year (bar, from the schedule); the value creation bridge (waterfall from the article's section 5 numbers); the Hilton timeline (a simple horizontal timeline with the verified dated figures from the intro, as a chart, no photos).

### Agent B, three statement (aim for 7 to 10 images)

Build `scripts/images/models/build_three_statement.py` -> `three-statement-test.xlsx` on one sheet laid out like a modeling test: drivers block, income statement, balance sheet, cash flow statement, debt and revolver block, the balance check row, the interest toggle cell. Years: the article's 2025A and three projected years. Screenshots: drivers, IS, BS, CFS, revolver and check row, the toggle close-up, one formula close-up, and the "error pattern" example (build a second small sheet with a deliberately broken link so the check row shows the constant gap, and one with a sign error showing the growing gap, as the article describes). Charts: cash flow waterfall for 2026 (net income to ending cash); the balance check patterns (two lines).

### Agent C, NWC and asset management (4 to 6 each)

NWC: `build_ridgeline_nwc.py` -> `ridgeline-nwc.xlsx`: the NWC schedule with the DSO, DIO, DPO calculation and the Year 3 projection table; the three-statement walk for the inventory example; the peg table. Charts: the cash conversion cycle as a timeline bar (DIO plus DSO minus DPO, with the article's numbers and the Amazon FY2020 figures as a second example); the NWC to unlevered free cash flow bridge.
Asset management: charts only: bond price against market yield for the article's 5-year 5 percent bond (a curve with the $958 and $1,045 points marked); the DCF sensitivity grid as a heatmap (sequential blue) from the article's table; the stock pitch structure as a simple seven-box diagram; passive versus active fund assets at end-2023 (two bars, Morningstar via CNBC, tagged in the caption).

### Agent D, resumes and behavioral (2 to 4 each)

Resumes: render page 1 of `published/assets/Sample Finance Resume (Jane Doe).pdf`, `Sample Consulting Resume - Junior (Alex Doe).pdf` and `Sample Consulting Resume - Sophomore (Sam Doe).pdf` with `pdftoppm -r 150`, then add numbered callouts with Pillow or matplotlib (a thin colored box around the region plus a short label in the margin) for the rules each article teaches (GPA on its own line, the verb-what-how-number bullet, the leadership section's weight, the three-line Additional Information). For #2 also a side-by-side "banking read vs consulting read" graphic: the same page twice with the six tilts highlighted. For #6, the MBB screen's four scores as an ordered diagram. Behavioral (#7): the five-part story shape as a diagram; the structured versus unstructured interview validity bars (0.51 vs 0.38, Schmidt and Hunter 1998, cited in the caption); a PEI versus standard behavioral comparison graphic (one story ten minutes versus five questions twenty minutes).

### Agent E, Bain, BCG, case examples (3 to 5 each, more for #10)

Bain (#8): the hiring process as a four-step flow; the FreshBowl worked case exhibit as a chart drawn from the article's table; the weak close versus strong close as a side-by-side text graphic; the Summer 2028 calendar timeline (tagged dates shown as "expected"). BCG (#9): the funnel (application, CCA, online case, round 1, final); the pizza chain case exhibit chart (contribution per order by channel) from the article's table; the "so what" loop diagram; the calendar timeline. Cases (#10): an issue tree diagram for two or three cases (profitability, market entry, M&A); a chart for each exhibit table where a chart reads faster than the table (airline cost bridge, EV charging unit economics, pricing tiers, car wash returns); the market sizing funnel for one sizing case; Enrico Fermi's Los Alamos badge photo from Wikimedia Commons if it is public domain (US government work; verify on the file page, record the URL and license, credit in the caption).
