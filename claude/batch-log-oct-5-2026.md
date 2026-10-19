# Batch log: 8 articles (October 5, 2026)

Repo: `Downloads/wsg-content-main v2/wsg-content-main`. Brief: `claude/batch-brief-oct-5-2026.md`. Images brief: `claude/images-brief-oct-5-2026.md`. Live-post list for internal links: `claude/wsg-live-urls-oct-5-2026.txt` (102 posts, sitemap fetched October 5, 2026).

## Founder decisions taken before drafting

- Repeat check: "Top 30 Consulting Interview Questions and How to Answer Them" and "How to Pass the Bain SOVA Test" already existed as drafts (Sep 25), so both were replaced with "Ultimate Guide to the MECE Framework" and "Centerview Partners: The Complete Career Guide". The old drafts are untouched.
- "Deloitte Strategy & Operations Career Guide" kept, written as the Deloitte Consulting analyst-track guide (what S&O became) and differentiated from the live Monitor Deloitte post, which it links.
- Headline 1 uses US "Practice", not "Practise".
- Model articles: our own Excel workbooks with the articles' numbers, screenshotted. The founder supplied a reference DCF workbook for structure; its layout is summarized without attribution in `reference/dcf-workbook-structure-oct-2026.md`. Our workbook (`torvik-dcf.xlsx`) uses a fictional company, our numbers and the house palette, and nothing in any file names or hints at the source.
- Outline approval skipped; drafted straight through.

## What shipped

All eight pass `check_article.py` and `check_style.py`; zero em, en or minus dashes; register grep clean. .docx in `published/ai-written/` via `markdown_to_docx_v2.py`, images embedded, author and last-modified-by set to "Wall Street Guide".

| # | Headline | Format | Hook | Words | Images | VERIFY |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Financial Modeling Test: What to Expect and How to Practice | ultimate-guide | real public story (Herndon and the Reinhart-Rogoff spreadsheet) | ~14,750 | 17 | 11 |
| 2 | Investment Banking Analyst Salary 2027: What You Actually Take Home | ultimate-guide | stat ($200,000 keeps $130,282) | ~9,450 | 8 | 73 |
| 3 | Growth Equity Interview Guide for Undergrads | ultimate-guide | direct claim (sourcing before modeling) | ~12,550 | 8 | 62 |
| 4 | The Three Financial Statements: How They Link and How to Explain It | ultimate-guide | reader question ($10 of depreciation) | ~11,250 | 14 | 1 |
| 5 | How to Get Into Bain's Sophomore Programs | niche | decision moment (Maya, two deadlines) | ~6,700 | 3 | 41 |
| 6 | Deloitte Strategy & Operations Career Guide | niche | first-call quote (Caleb, "does S&O still exist?") | ~7,250 | 6 | 69 |
| 7 | Ultimate Guide to the MECE Framework | ultimate-guide | scene (Stephen's McKinsey whiteboard) | ~10,650 | 17 | 2 |
| 8 | Centerview Partners: The Complete Career Guide | ultimate-guide | friend story (Harvard classmate Nate) | ~8,600 | 6 | 35 |

Word counts include tables and image lines.

## Independent QA (same day)

Two QA agents recomputed every worked number independently and verified six-plus facts per article against primary sources. All arithmetic tied except three derived figures, fixed:

- #6: capacity after both levers is 2,150 (not 2,250), about 93 percent utilization (not 89). Prose fixed; the Northline workbook formula and image rebuilt to match.
- #7: synthesis said revenue drop was "all volume"; volume fell $11.25M against an $8.55M price gain. Fixed. Tree 1's "Other" bucket (17 percent of cost) broke the article's own 10 percent rule; one line added explaining why it stays one branch.
- #5: program-to-ACI gap is five to eight weeks (First Forward is about eight). Fixed in text and in the timeline image caption.

Other QA edits: #1 hook date softened (semester unverified) and the 2.2 percent figure attributed to all three data corrections; duplicate composite "Rohan" in #1 renamed so #3 keeps it; #2 relocation tax exception corrected (Pub 15-B), Goldman fees $9.34B; #3 Spectrum deadline tense; #4 pre-1988 funds statement reworded; #6 Discovery is a sophomore program (not freshman), offering-portfolio date tagged; #7 keyword moved into the first 100 words, "stayed inside the firm until 1999" corrected; #8 WBD settlement dates corrected (announced Sept 21, approved Sept 30), lawsuit year fixed, Kenvue closing cited to Kimberly-Clark's Oct 1 statement. Contraction and say-it-out-loud fixes throughout.

## Images (79)

Rebuild from the repo root with `python3 scripts/images/build_{slug}.py`, then `python3 scripts/images/insert_images.py {slug} drafts/draft-{slug}-v1.md` (new this batch: inserts image lines from each manifest's anchors, idempotent, so image agents no longer edit drafts).

| # | Images | Workbook | Checks |
| --- | --- | --- | --- |
| 1 | 17: every DCF block (historicals, segments, scenario switch, assumptions, operating build, working capital, PP&E, cost of debt, beta, WACC, UFCF and PV, formula close-up, TV and bridge, sensitivity), value bridge, formats chart, time budget | `torvik-dcf.xlsx` (8 tabs, CHOOSE-based scenario switch) | 726 cells match; Bear and Bull flips match |
| 2 | 8: base by tier, federal and NY bracket screenshots, gross-to-net waterfall, four cities, bonus withholding, three years, budget | `analyst-takehome.xlsx` | section 4 cell for cell |
| 3 | 8: venture vs growth vs buyout, ARR bridge, unit economics, cap table, preference formulas, returns, MOIC by scenario, Bear waterfall | `harborline-screen.xlsx` | sections 7, 8, 9, 11 |
| 4 | 14: six-links diagram, walk order, $10 depreciation, five scenarios, three Lantern statements, cash bridge, balance check, formula close-up | `lantern-bikes.xlsx` | 194 of 194 cells; balance check 0 |
| 5 | 3: Class of 2029 timeline, four-program grid, weeks-between plan | none | dates from article |
| 6 | 6: org diagram, pay by track, Northline case (3 screenshots), calendar vs MBB | `northline-case.xlsx` | both case tables and payback |
| 7 | 17: festival sorts, four mini-trees, four worked trees (dishwasher split in two), restaurant bridge, dental levers, OR idle hours, four drill trees | none (`wsg_diagrams.nested_tree` added) | all figures recomputed |
| 8 | 6: deal sizes, pay ranges, accretion scenarios, paper LBO paydown, value bridge, Paramount timeline | none | drill math recomputed |

**Regenerate at publish (dated):** Bain 01 and 03, Deloitte 06, Centerview 06 (Paramount's expected Oct 6 close); all 8 salary images when the 2027 brackets publish.

## Cross-links to add once live

- #1 Modeling test → Oct 1 three statement and LBO drafts; #4 (10-K table); #3 (section 1).
- #2 Salary → #8 (section 2); #3 (section 9).
- #3 Growth equity → #1 (section 4), #4 (section 7), #2 (section 2); Oct 1 LBO, finance resume, 20 behavioral.
- #4 Three statements → #1 (sections 2, 6); #3 (deferred revenue); #8 (technical bar); Oct 1 three statement, NWC, LBO.
- #5 Bain → Oct 1 Bain v2, BCG v2, consulting resume, 20 behavioral, 10 case examples; #7; #6 (fallbacks).
- #6 Deloitte → #5, #7, Oct 1 consulting resume, 20 behavioral, 10 case examples.
- #7 MECE → Oct 1 10 case examples, Bain v2, BCG v2, consulting resume.
- #8 Centerview → #2 (pay table), #1 and #4 (first round); Oct 1 LBO (Q2), three statement (Q1), NWC (Q4).

## Still thin / founder decisions

- Composites (Rohan #3, Sam #1, Maya #5, Caleb #6, Nate #8, R #7, R #2) and Stephen's whiteboard memory (#7): swap in real stories where they exist.
- #5 quotes two real Bain employees (Cristina Gutierrez Ramos, Sofia Cordovez Capriles) from Bain's own pages. Confirm comfort naming them.
- #2: Evercore's 2021 $15,000 signing bonus unconfirmed by a primary source (tagged); keep or cut.
- #3 and #4: second sub-question answers run 6 sentences against the 2 to 4 guideline.
- #8: "$3.5 million revenue per employee" (reported) doesn't match $1.9B / ~500 ($3.8M); Paramount closes Oct 6, update tense at publish; Vault respondent count and the $130K January 2022 base unconfirmed from a primary source.
- #6: Discovery posting says 32 US cities, one third-party copy says 30.
- #5: Bain's 2027 pages don't say whether program participants get an ACI fast track.

## Tooling added

- `scripts/images/insert_images.py` (manifest-driven image insertion).
- `scripts/images/models/numbers_{slug}.py` for articles 1 to 4 (plain Python, prints every table).
- `scripts/images/models/build_torvik_dcf.py`, `build_lantern_bikes.py`, `build_analyst_takehome.py`, `build_harborline_screen.py`, `build_northline_case.py`; eight `scripts/images/build_{slug}.py` scripts.
- `wsg_diagrams.py`: `N()`, `tree_extent()`, `nested_tree()` for arbitrary-depth trees.
- `reference/dcf-workbook-structure-oct-2026.md`.

## Skills applied

wsg-article (SKILL.md, source-verification, intros, plain-language, thorough-explanations, prose-editing, formatting, consulting addendum, images), humanizer / wsg-prose-editing (register and say-it-out-loud passes), clean-user-facing-text and remove-ai-marks checks (no em, en or minus dashes; docx and workbook author metadata "Wall Street Guide"; no personal identifiers in any output; the remove-ai-marks HTTP service isn't running in this environment, so the metadata strip was done directly).
