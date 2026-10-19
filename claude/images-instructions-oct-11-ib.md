# Image instructions: October 11, 2026 IB batch

You are building the images for one WSG draft. Work from `/home/claude/repo`. Today is Sunday, October 11, 2026. You never edit the draft; a QA agent is editing it at the same time. You build images from the draft's own numbers, write a manifest, and report.

## 1. Read first

1. `.claude-skill/images.md` in full (the banking format, the image-text plain-language and humanizer passes, the manifest fields, the rules that never bend).
2. Load the `dataviz` skill with the Skill tool and follow its form rules where they don't conflict with the banking format in `images.md` (the banking format wins: black Arial text, no gridlines, no boxes or frames, direct labels, source bottom-left, `BANK_SERIES` colors).
3. `scripts/images/wsg_viz.py` and `scripts/images/wsg_diagrams.py` (read the function signatures and docstrings).
4. Two model build scripts: `scripts/images/build_bain-sophomore-programs-how-to-get-in.py` (timeline, table graphic, plan) and `scripts/images/build_investment-banking-analyst-salary-2027.py` (bars, waterfall) or `build_20-consulting-behavioral-interview-questions.py` (diagrams). Match their structure: one idempotent script that rebuilds every image and writes the manifest in one run, with assertions that the numbers in the images match the draft text.
5. One existing manifest, for example `published/assets/images/bain-sophomore-programs-how-to-get-in/manifest.json`.
6. The humanizer skill: `/root/.claude/skills/synced/37fa8fbb-96dc-473e-ae57-5dce92d68ec3_c2846f6b-18df-4d08-a8e7-8471d3775030/humanizer/SKILL.md`.
7. The draft itself, in full. The image plan in your prompt came from the writer; check each anchor still exists in the draft (QA may be editing; match on the first 40 characters if 60 don't match, and record the final anchor you used).

## 2. Build

- Five or six images, a mix of types (bars, a table graphic, a timeline, a sequence or diagram). Every number comes from the draft text or a table in it; assert it in the script (read the draft file, regex the figure, compare) so a later edit to the draft fails the build loudly.
- File names: `published/assets/images/{slug}/NN-short-name.png`, in reading order, at most 2,200 px wide. Script: `scripts/images/build_{slug}.py`. Manifest: `published/assets/images/{slug}/manifest.json` with `file`, `alt`, `caption`, `source`, `method`, `anchor` per image (anchor = the first 60 characters, verbatim, of the draft line the image follows; never a line in the intro, inside a list, a table row or a quote; if the natural spot is a table, anchor on the paragraph after the table).
- Every string on or under an image (title, subtitle, axis titles, labels, callouts, legend, caption, alt, source line) goes through the plain-language pass and then the humanizer pass in `images.md` before rendering: short literal titles by default (at most one takeaway title per three images), captions one plain sentence under 20 words stating a fact from the chart, labels as nouns and numbers, alt text 10 to 20 plain words, source lines in the set format. No em dashes, en dashes or Unicode minus signs anywhere, including the manifest; use "to" for ranges and a hyphen-minus for negatives.
- Dated images (calendars, deadlines, "expected" windows): mark projected items "expected" and list them in your report under "regenerate at publish."
- Timelines: use `wsg_diagrams.month_axis` and `month_x`, or the approach in the Bain build script.
- After rendering, open every PNG with the Read tool and check: black text, no gridlines or boxes, no clipped or colliding labels, source line present, every word plain and literal. Fix and re-render.
- Run `python3 scripts/images/insert_images.py {slug} drafts/draft-{slug}-v1.md --dry-run` to confirm every anchor resolves. Do not run it without `--dry-run`; the coordinator inserts after QA.

## 3. Report back (under 400 words)

1. The images: file, type, what it shows, the numbers it carries, the source line, the anchor used.
2. Every string that the plain-language or humanizer pass changed (old → new), briefly.
3. Assertions in the build script (what they check).
4. Dry-run result for the anchors.
5. Dated images to regenerate at publish.
