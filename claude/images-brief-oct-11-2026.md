# Images brief: October 11, 2026 batch

You are building the pictures for ONE WallStreetGuide (WSG) draft. Repo root `/home/claude/repo`; run everything from there. Today is Sunday, October 11, 2026.

## Read first

1. `.claude-skill/images.md` in full. It is the spec: the three kinds of image, the banking format, the plain-language and humanizer passes on every string, the source-line rule, the manifest fields, the workflow, the rules that never bend.
2. `scripts/images/wsg_viz.py` and `scripts/images/wsg_diagrams.py` (read the function signatures and docstrings; use the toolkit, don't reinvent it).
3. One existing build script as the pattern: `scripts/images/build_deloitte-strategy-and-operations-career-guide.py` and `scripts/images/build_investment-banking-analyst-salary-2027.py`.
4. `scripts/images/insert_images.py` (docstring) so your manifest anchors work with it.
5. Load the `dataviz` skill with the Skill tool before drawing any chart (form rules: one axis, no dual axes, a legend when two or more series, selective direct labels, nothing decorative). If the Skill tool can't load it, follow the banking format in images.md.
6. Your draft, in full. Note: a QA agent is editing the same draft at the same time. You do NOT edit the draft. You choose anchors (the first 60 characters of the line each image follows) from lines least likely to change: table rows, lines that start with a number or a firm name. Record the anchor text exactly as it appears right now.

## What to build

Four to six images per article in the banking format: black Arial text, no gridlines, no boxes, no frames, no cell borders, direct data labels instead of a value axis on bars, `BANK_SERIES` colors (navy for the subject, gray for the comparison group), `add_source()` in the bottom-left of every chart, `bank_table()` for tables as graphics, `wsg_diagrams` for diagrams and timelines. Mix the types: at least one chart, one table or diagram, and one timeline or process graphic where the article has one. No model screenshots unless the article has a worked model. Outside images (news charts, firm pages) only if the article names the real thing and you can credit it per images.md; otherwise build.

**Every number in an image matches the draft.** Read the numbers from the draft file in your script (or hard-code them and assert them against the draft text with a regex) so a mismatch stops the build. Dated images (calendars, "2026" pay tables, headcount lines) get `"regenerate_at_publish": true` in the manifest and a note in your report.

## Image text (the October 8 rule)

Every string a reader sees (title, subtitle, axis titles, labels, legend entries, callouts, diagram boxes, caption, alt text, source line) gets the plain-language pass and then the humanizer pass from images.md before you render:

- Titles short and literal, under about 10 words: "First-year pay at McKinsey, BCG and Bain, 2026". A plain takeaway title on at most one image in three.
- Captions one plain sentence under 20 words that says what to look at; a fact, not a comment. No "notice how," no story, no twist.
- Labels are nouns and numbers. Alt text 10 to 20 plain words describing the picture.
- Source lines: "Source: {outlet or page}, {topic}, {month year}." For a chart drawn from the article's own numbers: "Source: WSG analysis of the figures in this article." For tracker data: "Source: Management Consulted, 2026 consulting salary report, 2026."
- No jargon the article hasn't explained, no noun piles, no em or en dashes or Unicode minus anywhere (write "2022 to 2026," "-5%").
- Cut significance words (key, crucial, striking), antithesis ("X, not Y"), narration ("this chart shows"), drama (massive, skyrockets), cute compression.
- Read every string out loud: would a banker say it that way in a meeting?

## Files

- Build script: `scripts/images/build_{slug}.py`, idempotent, runnable from the repo root, rebuilds every PNG and writes the manifest in one run.
- PNGs: `published/assets/images/{slug}/NN-short-name.png`, two-digit NN in reading order, at most 2,200 px wide, 200 dpi, white background. Strip metadata; no personal identifiers anywhere; workbook author (if any) "Wall Street Guide".
- Manifest: `published/assets/images/{slug}/manifest.json`, a JSON list, one entry per image with `file`, `alt`, `caption`, `source` (required, starts with "Source:"), `method` (what it was drawn from), `anchor` (first 60 characters of the draft line it follows, exactly), and `regenerate_at_publish` (true/false).
- Then run `python3 scripts/images/insert_images.py {slug} drafts/{draft-file} --dry-run` and confirm every anchor resolves and nothing lands in the intro, a list, a table or a quote. Do NOT run it without `--dry-run`; the coordinator inserts after QA finishes.
- Look at every PNG you made (Read the file) and fix clipped or colliding labels, gridlines, boxes, or any string that still reads AI-written.

## Report (under 400 words)

Each image: file, anchor, what it shows, where the numbers come from, dated or not. The checks you ran (numbers asserted against the draft, dry-run anchors resolved). The strings you changed in the humanizer pass (old → new, up to ten examples). Anything you decided not to illustrate and why. The exact rebuild command.
