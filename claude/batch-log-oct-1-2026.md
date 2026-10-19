# Batch log: 10 articles (October 1, 2026)

Repo: `Downloads/wsg-content-main v2/wsg-content-main` (the founder's live copy). Brief: `claude/batch-brief-oct-1-2026.md`. Live-post list used for internal links: `claude/wsg-live-urls-oct-1-2026.txt` (94 posts, fetched from the blog sitemap on October 1, 2026).

## Founder decisions taken before drafting

- Checked wallstreetguide.net first: neither "Bain Case Interview Guide" nor "BCG Case Interview Guide" is live, so both were regenerated as improved v2 drafts (v1 files left untouched) rather than swapped for other titles.
- Resume articles: samples inline only, no downloadable files.
- Model articles: no Excel files from us. Agents searched for free, high-quality templates and linked only those they could open without a paywall or signup (one each; see below).
- Headlines word for word. Outline-approval step skipped; drafted straight through.
- Intros: strong, varied hooks with first names and real public stories; 2 to 4 verified fun facts woven into each body.

## What shipped

Drafts in `drafts/`, all passing `check_article.py`, `check_style.py` and `check_links.py` with no hard failures; zero em dashes, en dashes or Unicode minus signs; register grep clean.

| # | Vertical | Headline | Format | Hook | Words | VERIFY |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | IB | LBO Model Explained: What an Undergrad Actually Needs to Know | ultimate-guide | real deal story (Blackstone's 2007 Hilton buyout) | ~10,700 | 13 |
| 2 | IB | Finance Resume Template: A Format Built for Banking and Consulting | ultimate-guide | first-call quote (Priya, two resumes, zero first rounds) | ~6,600 | 2 |
| 3 | IB | Asset Management Interview Prep: What They Actually Ask Undergrads | ultimate-guide | real public story (Peter Lynch, "I never said that") | ~10,100 | 32 |
| 4 | IB | Net Working Capital: How to Explain It in an Interview | ultimate-guide | reader question plus scene (Dev and the $50 million follow-up) | ~8,000 | 2 |
| 5 | IB | Three Statement Model: How to Build One for a Modeling Test | ultimate-guide | real public story (JPMorgan's 2012 VaR spreadsheet cell) | ~9,000 | 3 |
| 6 | CON | Consulting Resume: The One-Page Format That Passes the Screen | ultimate-guide | decision moment (Ana, "Which?", night before Bain's deadline) | ~7,000 | 10 |
| 7 | CON | 20 Consulting Behavioral Interview Questions and Sample Answers | listicle (20) | Stephen's own McKinsey PEI follow-up memory | ~9,100 | 3 |
| 8 | CON | Bain Case Interview Guide (v2) | ultimate-guide | friend story (Theo lost the final on the close; Nadia drilled it and won) | ~9,300 | 22 |
| 9 | CON | BCG Case Interview Guide (v2) | ultimate-guide | scene (the first sixty seconds of a candidate-led case, by the clock) | ~7,400 | 15 |
| 10 | CON | 10 Case Interview Examples With Full Worked Solutions | listicle (10) | real public story (Fermi's piano tuners and the Trinity estimate) | ~10,900 | 6 |

.docx builds in `published/ai-written/` via `scripts/markdown_to_docx_v2.py` (Arial, Title 24 / Heading 2 18 / body 11, double spacing, pipe tables as Word tables). Author and Last Modified By set to "Wall Street Guide" on all ten. Filenames use " - " in place of colons.

## Depth notes (the founder asked for in-depth model articles)

- **#1 LBO:** where each input lives (10-K, 10-Q, proxy, 8-K, credit agreement, CapIQ / FactSet / PitchBook, PitchBook LCD for leverage levels, CIM and QoE for private targets), tab layout and color conventions, the six blocks built in order, a full TargetCo model ($100M EBITDA, 10x entry, 6x leverage, five years: 2.59x MOIC, 20.9% IRR, sources = uses at $1,050M), both sensitivity grids, the paper LBO (3.30x / 27.0%), a what-to-skip list for a two-hour test, mistakes, say/don't-say. Template linked: A Simple Model's free LBO download (opened and inspected). Macabacus (trial-gated), WSP (email-gated) and CFI (account) named, not linked.
- **#5 Three statement:** the six links, where each input sits in a 10-K, historicals input rules, the assumptions block (days-based working capital), build order, the balance-check error patterns (constant gap = missing link, growing gap = sign or linking error), the interest circularity and toggle, a full worked model (2025A plus three projected years, revolver draws in 2027 and repays in 2028, check row 0.0 every year under both toggle settings), a two-hour time budget, what graders open first. Template linked: Mergers & Inquisitions' free Otis 90-minute three statement file (opened). Macabacus, WSP, CFI and A Simple Model gated, not linked.
- **#4 NWC:** banker vs textbook definition, every operating line in plain words, sign logic through the three statements, DCF and LBO flow-through, the M&A peg with the CB&I v. Westinghouse fight (Delaware Supreme Court, 2017), the cash conversion cycle worked on Amazon's FY2020 10-K (negative 53 days), Dell's 1990s model, the days-based projection, red flags, every classic question answered.
- **#10 Cases:** ten original cases (airline profitability, gym growth, EV charging entry, snack M&A, SaaS pricing, two market sizings, warehouse operations with Little's Law, pet insurance launch, car wash PE diligence), every number computed before it went into a table.

## Independent QA (same day)

Two QA agents that had not seen the drafting recomputed every worked number from the articles' own inputs (all tied, in all ten), verified about six facts per article against primary sources, and checked the house rules and the .docx builds. Fixes made from their reports before the final build:

- **#7:** McKinsey's interviewing page names three PEI themes (personal impact, entrepreneurial drive, inclusive leadership; problem solving is the case). The draft had asserted "courageous change" as a fourth named theme; corrected throughout, with a VERIFY note that some prep sites add it. Janz "1977 conference" softened to "late 1970s." BCG five-qualities VERIFY tag removed (verified).
- **#1:** EA take-private close corrected to August 4, 2026 (tagged); Stern Metals attributed to Kohlberg alone (Kravis and Roberts joined Bear Stearns later); the leverage sensitivity grid now states its split assumption (75 percent term loan / 25 percent notes at every leverage level); "20 to 40 minutes" effort count softened; composite renamed from Theo to Marcus so the batch has one Theo (Bain).
- **#2:** ACT rule made consistent between sections 4 and 7; "no blank line" claim scoped to the real page (the web layout adds spacing); bullets-per-role rule reworded to match the sample; research assistant dates aligned with the ordering rule; certification and interests lines varied away from the live John Doe sample.
- **#3:** Fidelity fixed income internship timing corrected to spring 2027 recruiting for 2028 (per jobs.fidelity.com); bond example timing fixed (rates move right after purchase, so the 5-year price applies); echo line cut; composite renamed Jonah.
- **#4:** projection table text now states Year 2 revenue and COGS and that days are rounded to whole numbers (exact days give a figure about $1.5 million higher); Amazon quote located in the MD&A overview; CB&I v. Westinghouse phrasing matched to the opinion.
- **#6:** "sophomore summer at a startup" corrected to freshman summer (dates); BCG FAQ quote restored to "ethical, results-driven, curious, and excellent problem solvers"; two leadership bullets varied away from the John Doe shapes.
- **#8:** Stephen's name added to the body (it appeared only in the meta); process quote attributed to Bain's interviewing pages; intern pay now cited to bain.com's ACI page ($9,000 a month) rather than a prep site.
- **#10:** pet insurance steady-state figure corrected from "roughly $20 million" to about $22 million a year (the article's own inputs); gym case Lever D labeled as valued at today's pricing; opening paragraph trimmed.
- All ten: 30-plus "say it out loud" lines rewritten in plain form (copywriter fragments, stacked metaphors); U+2212 minus signs in math bullets replaced with the word "minus."

## Internal links used, per article

- **#1 LBO:** walk-me-through-an-lbo; walk-me-through-a-dcf; ebitda-explained; 25-private-equity-interview-questions; 50-accounting-interview-questions; PE internship ultimate guide.
- **#2 Finance resume:** investment-banking-resume (live Sept 2026 post); how-to-build-a-consulting-resume; investment-banking-internship-cv; consulting-cover-letter; 10-investment-banking-internships-2027; 15-best-consulting-internships.
- **#3 AM prep:** goldman-sachs-asset-management-interview; hedge fund ultimate guide; bridgewater-associates-internship; what-does-an-equity-research-analyst-do; equity-research-vs-investment-banking; walk-me-through-a-dcf.
- **#4 NWC:** 50-accounting-interview-questions; walk-me-through-a-dcf; ebitda-explained; walk-me-through-an-lbo; 10-deal-discussion-questions; 2026-investment-banking-interview-guide-for-sophomores.
- **#5 Three statement:** 50-accounting-interview-questions; walk-me-through-a-dcf; walk-me-through-an-lbo; ebitda-explained; is-wall-street-prep-worth-it; 20-fp-a-interview-questions.
- **#6 Consulting resume:** how-to-build-a-consulting-resume; investment-banking-resume; consulting-recruiting-timeline-2026; how-to-get-into-consulting-as-an-undergrad; 15-best-consulting-internships; consulting-cover-letter.
- **#7 Behavioral:** how-to-ace-the-mckinsey-personal-experience-interview; why-consulting-how-to-answer; how-to-prepare-for-a-consulting-interview; ultimate guide to MBB; 30-examples-ib-behavioral-questions; how-to-build-a-consulting-resume.
- **#8 Bain v2:** what-is-a-case-interview; 7-case-interview-frameworks; 10-tips-to-beat-the-case-interview; 10-free-resources-for-case-consulting-prep; ultimate guide to MBB; consulting-recruiting-timeline-2026.
- **#9 BCG v2:** bcg-online-assessment-guide; bcg-casey-chatbot-interview; bcg-internship-how-to-win-the-offer; what-is-a-case-interview; 7-case-interview-frameworks; ultimate guide to MBB.
- **#10 Cases:** what-is-a-case-interview; 7-case-interview-frameworks; 10-tips-to-beat-the-case-interview; how-to-prepare-for-a-consulting-interview; ultimate-guide-to-the-mckinsey-case-interview; 10-free-resources-for-case-consulting-prep.

## Cross-links to add between the ten once they're live

| From | To |
| --- | --- |
| #1 LBO | #4 NWC (working capital line in Step 3, the sign-flip mistake); #5 Three statement (PE internship model, conventions) |
| #2 Finance resume | #6 Consulting resume (the two full consulting samples); #7 Behavioral ("walk me through this bullet") |
| #3 AM prep | #1 LBO (debt and EV mechanics); #4 NWC (the free cash flow working capital line); #2 Finance resume |
| #4 NWC | #5 Three statement (sections 3, 4, 10); #1 LBO (section 6); #3 AM (earnings-quality red flags) |
| #5 Three statement | #1 LBO (sections 11 and sub-question 2); #4 NWC (days bullets) |
| #6 Consulting resume | #2 Finance resume (blank template, banking vs consulting table); #7 Behavioral; #8 and #9 (timing paragraph) |
| #7 Behavioral | #6 Consulting resume (story bank); #8 Bain and #9 BCG (firm paragraphs); #10 Cases ("the case half is a separate skill"); #2 Finance resume (item 20) |
| #8 Bain v2 | #9 BCG (candidate-led comparison); #7 Behavioral (section 10); #10 Cases (section 6); #6 Consulting resume (application step) |
| #9 BCG v2 | #8 Bain (sub-question 1 and close); #10 Cases (section 5, prep plan); #7 Behavioral (section 8); #6 Consulting resume |
| #10 Cases | #8 Bain and #9 BCG (candidate-led note); #7 Behavioral (PEI mention); the Sept 25 "25 Case Interview Questions" draft once live |

Also worth adding to older live posts: link #2 from the live IB resume post and the consulting resume checklist; link #4 and #5 from the walk-me-through-a-DCF and walk-me-through-an-LBO posts; link #7 from the McKinsey PEI post; link #8 and #9 from the "what is a case interview" and MBB ultimate guide posts; link #3 from the Goldman Sachs Asset Management interview post.

## Research findings that affect the context bundle

- **McKinsey PEI (article #7).** mckinsey.com/careers/interviewing names three PEI themes (Personal Impact, Entrepreneurial Drive, Inclusive Leadership) with a sample question each; the "four areas" on the page include Problem Solving, which is the case. "Courageous change" does not appear on McKinsey's page. `consulting/` canon of three dimensions stands.
- **Bain (article #8).** Bain's practice cases moved: Coffee Shop Co. and FashionCo now live under bain.com/careers/hiring-process/interviewing/ (the old /case-interview/ sub-URLs 404). New sophomore webinar series "Consulting Kickstart" (three-part October series, deadline October 5, 2026). BEL (14 offices, founded 2009), CREW (15 offices), First Forward (1.5 days, 6 offices), BASE (pre-MBA) confirmed by name; all 2026 cycles closed, 2027 unposted. Bain's own ACI page lists intern pay at $9,000 a month. Digital assessment: Sova or TestGorilla, 30 to 40 minutes, calculator allowed, feedback within 60 days. Harvard AC full-time deadline October 11, 2026. `consulting/firm-profiles/mbb.md` should pick up Consulting Kickstart and the new practice-case URLs.
- **BCG (article #9).** US Associate page: CCA invitation 30 to 90 minutes after submission, 48 hours to complete, about 35 minutes, no retake; online case to select candidates about two weeks after the deadline; cover letters not required; up to two offices. BCG's five published attributes: integrity, intellectual curiosity, creative thinking, collaborative mindset, drive. Embark (sophomores, April 15 to May 14 applications for the December 2027 to July 2028 program) is the visible sophomore track; the GFL link still serves the generic campus page; Launch closed May 29, 2026. 2025 revenue $14.4 billion, 40 percent-plus from AI and tech (April 23, 2026 release). Summer 2027 US Associate applications closed; Summer 2028 dates not posted.
- **Asset management programs (article #3).** Firm pages confirmed for BlackRock, Fidelity (equity: Boston window for 2028 opens winter 2027; fixed income: spring 2027 recruiting for 2028), T. Rowe Price, Capital Group (Capital Associates Program), Wellington Early Career Investor, PIMCO, Vanguard, Invesco, Franklin Templeton, GSAM, J.P. Morgan AM Summer Analyst, MSIM, Neuberger Berman, Dodge & Cox, AllianceBernstein, MFS, Loomis Sayles. None publish class sizes. Every 2028 date is pattern-based and tagged. BlackRock AUM $15.3 trillion (Q2 2026). Morningstar: passive passed active at end-2023 ($13.29T vs $13.23T).
- **LBO market context (article #1).** PitchBook LCD 2025: sponsor equity about 46 percent of deal value, leverage under 5x. EA take-private: $55 billion, $210 a share, PIF / Silver Lake / Affinity Partners, about $20 billion of JPMorgan debt, closed August 4, 2026 (tagged). Hilton: $47.50 a share, about $26 billion, 40 percent premium (Blackstone July 3, 2007 release); $819 million 2010 restructuring; $2.34 billion IPO December 2013; about $14 billion total profit (Bloomberg, May 2018).
- **Templates.** Free and openable without signup as of October 1, 2026: A Simple Model's LBO download (email required for the file, page lists it free) and Mergers & Inquisitions' Otis 90-minute three statement file. Gated: Macabacus (14-day trial), Wall Street Prep (email, no full template), CFI (free account), A Simple Model's other files (email).

## Link verification notes

`check_links.py` reports the following as unreachable from the drafting sandbox only; each was confirmed live with a browser-style fetch: mckinsey.com (timeout), quiz.bcg.com (proxy block), jobs.fidelity.com (403), nb.com (429), and wallstreetguide.net itself (429 rate limit when many links are checked at once). Click-test all of these before publish.

## VERIFY tags to clear before publish (highest value first)

- #3: every 2028 open date, eligibility and pay line for the 17 firms (all pattern-based); BlackRock AUM; FRED 10-year yield and the FactSet forward P/E used in the market-view answers.
- #8: Summer 2028 ACI postings; 2027 dates for Consulting Kickstart, CREW, BEL, First Forward and BASE; whether US offices use a written case; comp.
- #9: Summer 2028 Summer Associate window; 2027 Launch and Embark dates; GFL status; comp and intern pay; US round structure.
- #1: Hilton equity split (sources range $5.6B to $6.5B); EA close and terms; LCD 2025 leverage figures; RJR and TXU figures; the A Simple Model download terms.
- #6: Summer 2028 MBB windows; BCG SAT/ACT field; cover letter requirements by office; the founder's 3.7 effective GPA read.
- #7: PEI theme labels (confirmed today; re-check at publish); McKinsey 800,000 / 8,000 (2018).
- #10: Summer 2028 MBB cycle; NEVI / Midwest EV incentive status; USTMA 2025 forecast; 2024 box office and screen count; NAPHIA 2025 figures; Mister Car Wash take-private status.
- #2: Goldman 2025 intern figures; McKinsey application volume.
- #4: Amazon FY2025 CCC; Dell 1998 component figures.
- #5: 21 percent statutory rate; M&I file still ungated.

Grep each draft for `[VERIFY` for the full list.

## Still thin (needs the founder)

- #1 section 6 ("Marcus"), #3 section 2 ("Jonah"), #4 intro ("Dev"), #5 section 6 ("T"), #2 intro ("Priya"), #6 intro ("Ana") and #8 intro ("Theo" and "Nadia") are composites. Swap in real WSG student stories where they exist.
- #7 intro: Stephen's PEI memory is plausible and general; a real detail would strengthen it.
- #3: a founder read on which long-only firms WSG students have actually placed at would let the firm list be ordered by relevance instead of alphabetically within tiers.
- #8: whether US Bain offices use a written case (sources conflict; the article says so).
- #6: the effective MBB GPA bar (3.7) is the founder's pattern, not a published figure; tagged.

## Resume sample assets (added same day, founder request)

Built by the new `scripts/build_resume_assets.py` from the plain-text resume blocks saved as `drafts/sample-resume-*.md` (extracted from the two resume articles), into `published/assets/`:

- `WSG One-Page Resume Template.docx`: the blank bracketed skeleton, editable, Arial 10.5, 0.5 inch margins.
- `Sample Finance Resume (Jane Doe).pdf` and `.docx`: the filled sample from the Finance Resume Template article.
- `Sample Consulting Resume - Junior (Alex Doe).pdf` and `.docx`: Sample A from the Consulting Resume article.
- `Sample Consulting Resume - Sophomore (Sam Doe).pdf` and `.docx`: Sample B.

All three PDFs are one page and fill it: the builder auto-fits each sample, choosing the largest body size from 11 down to 10 that stays on one page and then stretching the section and entry spacing until about 96 to 98 percent of the page is used (Jane 10pt, Alex and Sam 11pt). PDF metadata (Title, Author, Creator, Producer) and docx core properties (Author, Last Modified By) are set to "Wall Street Guide"; LibreOffice's XMP block is stripped. The PDFs are rendered with Liberation Sans, which has Arial's metrics, so the page breaks match what Word shows. Both resume articles now carry a `[VERIFY: add the download links ... once uploaded to Wix]` placeholder where the files belong, and their .docx builds were refreshed.

## Images (added same day, founder request)

Founder's ask: relevant pictures and graphs in the documents, Excel screenshots for the model articles. Sourcing decision: rebuild each model in our own workbook with the article's numbers and screenshot that, never a third party's model; charts drawn from the articles' own tables; one public domain photo. Brief: `claude/images-brief-oct-1-2026.md`. Five agents, 63 images, every one placed in its draft with alt text and a caption, every .docx rebuilt with the images embedded at the printable width.

| # | Article | Images | What they are |
| --- | --- | --- | --- |
| 1 | LBO | 12 | Hilton timeline; sources and uses, operating model, cash flow to debt paydown, debt schedule, returns, both sensitivity grids and the paper LBO as live-formula screenshots of `scripts/images/models/targetco-lbo.xlsx`; a formula close-up; debt balance by year; the value creation bridge |
| 2 | Finance resume | 3 | Jane Doe page with five callouts; the verb-what-how-number bullet anatomy; banking read vs consulting read side by side with the six tilts boxed |
| 3 | Asset management | 4 | passive vs active assets (Morningstar via CNBC); the seven-part pitch diagram; DCF sensitivity heatmap; bond price vs yield curve with the $958 and $1,045 points |
| 4 | NWC | 6 | change-in-NWC table, peg table, days and Year 3 projection, inventory three-statement walk as screenshots of `ridgeline-nwc.xlsx`; EBIT to unlevered FCF bridge; cash conversion cycle timelines (Ridgeline and Amazon FY2020) |
| 5 | Three statement | 13 | drivers, IS, BS, CFS, schedules, revolver block, check row, toggle close-up, formula close-up as screenshots of `three-statement-test.xlsx`; the two deliberately broken error-pattern sheets; check pattern lines; the 2026 cash waterfall |
| 6 | Consulting resume | 3 | the MBB screen's four ordered scores; Alex and Sam pages with callouts |
| 7 | Behavioral | 3 | PEI vs standard behavioral timelines; structured vs unstructured validity bars (Schmidt and Hunter 1998); the five-part story shape |
| 8 | Bain v2 | 5 | four-step hiring flow; FreshBowl cohort chart and EBITDA scenarios from the article's exhibit; weak close vs strong close; Summer 2028 calendar |
| 9 | BCG v2 | 5 | the funnel; contribution per order by channel; the contribution bridge; the hypothesis and so-what loop; Summer 2028 calendar |
| 10 | Cases | 9 | Fermi's Los Alamos badge (Wikimedia Commons, PD-USGov-DOE, credited); issue trees for the airline, EV charging and snack M&A cases; airline cost bridge; EV unit economics; pricing options; tire sizing funnel; car wash returns by scenario |

Workbook checks: `recalc_values()` compared the LBO (every table, both grids, paper LBO: zero mismatches), three statement (163 cells, check row 0.0 in all four years) and NWC (62 cells) workbooks against the article tables; each build script exits non-zero on a mismatch. Two NWC notes for the editor: Year 2 DPO is 43.45 exactly, the article's table rounds the one-decimal 43.5 up to 44 (the workbook shows both); the rounded CCC components 29 + 73 minus 43 come to 59 against the exact 59.6 the chart uses.

Regenerate at publish (dated): `bain-case-interview-guide/05-summer-2028-calendar.png` (shows the October 5 Kickstart deadline and "today"), `bcg-case-interview-guide/05-summer-2028-calendar.png`, and the Hilton timeline and passive vs active chart if their VERIFY figures change. Rebuild commands, from the repo root: `python3 scripts/images/build_{slug}.py` for each article slug (each rebuilds its workbook, asserts the numbers, renders and writes the manifest).

Tooling added: `scripts/images/wsg_viz.py` (palette, chart style, Excel formatting helpers, `render_range` xlsx to PNG via LibreOffice, `recalc_values`), `scripts/images/wsg_diagrams.py`, `scripts/images/resume_callouts.py`, `scripts/images/models/build_*.py`; `markdown_to_docx_v2.py` now embeds `![alt](path "Caption")` lines as centered pictures with italic captions (a missing file becomes a bracketed placeholder plus a warning); `markdown_to_wix_html.py` turns the same line into a figure with a figcaption. The Fermi photo is the 330 px Commons rendition resampled to 660 px (the full-size download was rate limited); swap in the full-size file before publish if a sharper copy is wanted.

Wix: upload each PNG from `published/assets/images/{slug}/`, paste the manifest's `alt` into the alt field and the `caption` under the image.

Skill: `.claude-skill/images.md` (new module, also proposed to the account as `wsg-article-images`) records the sourcing rule, the rebuild-the-model workflow, the toolkit, naming, manifests, insertion syntax and the QA checklist.

## Tooling and files

- `claude/wsg-live-urls-oct-1-2026.txt`: live post list used for internal linking. Refresh from `https://www.wallstreetguide.net/blog-posts-sitemap.xml` before the next batch.
- `claude/batch-brief-oct-1-2026.md`: the brief the drafting agents worked from.
- `reference/ib-resume-article-live-sep-2026.md`: skeleton copy of the live IB resume article, used by the two resume articles.
- `scripts/verified-brands.txt`: 83 entities verified this batch appended under an October 1, 2026 header.
- `scripts/build_resume_assets.py`: new, builds the resume sample .docx and .pdf assets with Wall Street Guide metadata. Rerun after any edit to `drafts/sample-resume-*.md`.
- `_claude-staging/wsg-src2.zip` (one level above the repo) is the staging archive used to copy the repo into the drafting sandbox; safe to delete.

## Skills applied

wsg-article (SKILL.md, source-verification, intros, plain-language, thorough-explanations, prose-editing, formatting, consulting addendum), humanizer / wsg-prose-editing passes (register grep across all ten clean), clean-user-facing-text and remove-ai-marks checks (no em, en or minus dashes; docx author metadata set to Wall Street Guide; no personal identifiers in any output), plus two independent QA agents per the source-verification subagent pattern.
