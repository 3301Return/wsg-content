# Batch brief: 10 WSG articles (October 1, 2026)

Repo root: `/home/claude/repo` (a working copy of the founder's `Downloads/wsg-content-main v2/wsg-content-main`). Today is **Thursday, October 1, 2026**. US spelling throughout.

## Founder instructions for this batch (override defaults where they conflict)

1. **Headlines word for word.** Listed below. Do not shorten or retitle, even where a headline runs past the 8-10 word guideline.
2. **Intros must not be cookie cutter.** The founder's words: "make sure the intros are not all super cookie cutter and unique, interesting, use names, stories, etc. need to be a strong hook." Each article gets a different hook type AND a different shape from every other article in this batch (the assignment per article is below; it is a starting point, and you may pick a stronger hook of a different type if you say so in your report). Allowed: first names for composite students ("a student I worked with last spring, call her Priya"), real and verifiable public stories (a famous deal, a famous investor, a famous spreadsheet error), scenes, first-call quotes, stats with a bite, decision moments. Never a full fake name for a composite. WSG never looks bad in its own stories (setbacks happen before someone finds WSG, or to a roommate or friend). Stephen intro present in the first three paragraphs, credentials only from `writers/stephen-turban.md`. Keyword in the first 100 words. Two to three short paragraphs, then the H2 sub-questions.
3. **Make the body interesting.** The founder asked for "interesting fun facts." Every article carries 2 to 4 real, verified, interesting facts woven into the body where they teach something (the origin of a term, a famous deal, a founder story, a number that surprises). Verify each one on the web before using it. Anything that moves (AUM, application counts, rankings) gets a `[VERIFY: ...]` tag. No "Fun fact:" labels needed; a one or two sentence aside inside the relevant section reads better. Do not invent a fact to fill the quota.
4. **Technical articles go deep.** The founder's words on the model articles: "really go in depth with the models one (where to find info, how to input info, how to structure it, what to add and not to add, etc)." Apply the same standard to Net Working Capital and the case solutions. Walk every mechanism step by step in plain words a sharp high schooler could follow on one read. Use the technical term, then explain it at first use. Work every number. Longer is expected: 4,000 to 8,000 words is normal for articles 1, 3, 4, 5, 7 and 10.
5. **All arithmetic in a worked example must tie.** For articles 1, 4, 5 and 10: build the numbers in a short Python script first (`python3 -c` or a scratch file under `/tmp`), then paste the results into the article tables. A balance sheet that doesn't balance or an IRR that's off by a point is a failure. State in your final report that the numbers were script-checked.
6. **Internal links (backlinks).** Use ONLY URLs listed in `claude/wsg-live-urls-oct-1-2026.txt` (the live sitemap fetched today, 94 posts). Add 3 to 6 internal links per article where they help the reader, as inline anchor text. Never a "related posts" footer. Do not link to the other nine articles in this batch (not live yet); instead list suggested cross-links in your final report.
7. **No em dashes, no en dashes, no hyphens as pause punctuation.** Grep before you finish: `grep -nE "—|–" drafts/{file}.md` must return nothing.
8. **Every named entity verified** per `.claude-skill/source-verification.md` using WebSearch / WebFetch. Tier 1 household names skip verification. Every time-sensitive claim (deadlines, pay, dates, program names, eligibility, test providers, AUM, headcounts) tagged `[VERIFY: ...]` inline AND researched so the stated value is the best current one. If you can't verify a fact, leave it out.
9. **Skip the outline-approval step.** The founder approved the headlines and asked to draft straight through.
10. **Resume articles (2 and 6): inline samples only.** No downloadable files. Reuse the skeleton (section order, header line, entry format, bullet formula, one-page rules) from `reference/ib-resume-article-live-sep-2026.md`, not its text. Where the IB article says "download the template," these articles don't; the sample on the page is the template.
11. **Model articles (1 and 5): no Excel files from us.** The founder: "article only, no Excel files UNLESS you can find sample Excel sheets that are really really good, then use those." Search for free, downloadable, high-quality LBO and three statement templates (Macabacus, Wall Street Prep free resources, Corporate Finance Institute free templates, A Simple Model, and anything better you find). Open each one. Link only to a template that (a) is actually free to download without a paywall surprise, (b) is from a source bankers recognize, and (c) matches the structure the article teaches. If none clears that bar, say so in the article in one sentence and move on. Never link a template you haven't opened.

## Required reading (in this order) before drafting

- `CLAUDE.md`
- `.claude-skill/SKILL.md`, `.claude-skill/source-verification.md`, `.claude-skill/intros.md`, `.claude-skill/plain-language.md`, `.claude-skill/thorough-explanations.md`, `.claude-skill/prose-editing.md`
- `style-guide/style-guide.md`, `style-guide/editorial-feedback-may-2026.md`, `style-guide/editorial-feedback-july-2026.md`, `style-guide/seo-checklist.md`, `style-guide/link-verification.md`, `style-guide/recruiting-timeline-glossary.md`
- `writers/stephen-turban.md`
- The matching template in `templates/` (ultimate-guide.md or listicle.md) and 1-2 samples in `samples/`
- `claude/batch-log-sep-25-2026.md` (what shipped last week, the hooks already used, the founder's review notes) and `claude/corrections-aug-21-2026.md`
- **Consulting articles (6 to 10):** also `.claude-skill/consulting.md` and every file in `consulting/` (firm-profiles, recruiting-timeline, case-interview-frameworks, voice-cues, sources/INDEX). Known correction: MBB undergrad intern recruiting runs IB-style: apply sophomore spring (year A) for Summer A+1 internships, graduate A+2. The cycle that matters for a reader in October 2026 is **applications in 2027 for Summer 2028 internships (Class of 2029)**. Last cycle's confirmed dates for reference: McKinsey BA intern window Jan 1 to Mar 29, 2026; BCG Summer Associate deadline June 2, 2026; Bain ACI March 29 and August 31, 2026. Verify the next cycle on the firms' own pages and tag.
- **IB articles (1 to 5):** `deep-dives/INDEX.md`. For technical sourcing, `400-ib-questions.txt` and `wsp-redbook.txt` in the repo root are text extracts of the two interview guides in `deep-dives/`. Grep them for your topic (e.g., `grep -n -i "working capital" wsp-redbook.txt | head -50`). Paraphrase and re-derive; never copy their wording or their exact example numbers.

## Hooks already used recently (do not repeat the shape)

Sep 25 batch: friend's younger brother with a first name (Owen); Blackstone 57,000 applicants / 138 stat; Einhorn's 2008 Ira Sohn speech (real public story); first-call quote; reader question; the silent interviewer scene; decision moment with a first name (Leo); US Airways 1549 and checklists (real outside story). Sep 19 batch: 11:40 pm Sunday resume scene (D); and the existing Bain v1 (direct claim about synthesis) and BCG v1 (direct claim, "hands you the wheel").

## The 10 articles

| # | Vertical | Exact headline | Slug | Format | Hook assignment |
|---|---|---|---|---|---|
| 1 | IB | LBO Model Explained: What an Undergrad Actually Needs to Know | lbo-model-explained-undergrad | ultimate-guide | Real public deal story: Blackstone's 2007 Hilton buyout (about $26 billion at the top of the market, nearly lost in the crisis, ended as one of the most profitable PE deals ever at roughly $14 billion of profit). Verify every figure (Bloomberg, WSJ, Reuters) and tag. |
| 2 | IB | Finance Resume Template: A Format Built for Banking and Consulting | finance-resume-template-banking-consulting | ultimate-guide | First-call quote from a student who recruited for both IB and consulting with two different resumes and got nowhere with either. |
| 3 | IB | Asset Management Interview Prep: What They Actually Ask Undergrads | asset-management-interview-prep-undergrads | ultimate-guide | Real public story: Peter Lynch's Magellan Fund (about 29 percent a year, 1977 to 1990) and his "buy what you know" idea, used to show that AM interviews test a different muscle from banking interviews. Verify and tag. |
| 4 | IB | Net Working Capital: How to Explain It in an Interview | net-working-capital-interview | ultimate-guide | Question the reader is already asking, phrased the way they'd type it, with a short scene of a student giving the textbook answer and getting the follow-up they didn't expect. |
| 5 | IB | Three Statement Model: How to Build One for a Modeling Test | three-statement-model-modeling-test | ultimate-guide | Real public spreadsheet-error story: JPMorgan's 2012 CIO "London Whale" VaR spreadsheet (the January 2013 task force report found manual copy-paste steps and a formula that divided by a sum instead of an average, understating risk). Verify from the report and press coverage. Alternative if it doesn't hold up: the Reinhart-Rogoff 2013 Excel error. |
| 6 | CON | Consulting Resume: The One-Page Format That Passes the Screen | consulting-resume-one-page-format | ultimate-guide | Decision moment with a first name: a sophomore choosing between two resume drafts the night before a deadline, one built for banking and one for consulting. |
| 7 | CON | 20 Consulting Behavioral Interview Questions and Sample Answers | 20-consulting-behavioral-interview-questions | listicle (20) | Stephen's own McKinsey interview memory, first person, general and honest (he went through McKinsey on-cycle recruiting; keep details plausible and never invent specifics he couldn't have said). |
| 8 | CON | Bain Case Interview Guide | bain-case-interview-guide | ultimate-guide, **write as v2** | Friend or roommate story with a first name, about someone who cased well and lost a Bain final on the close, then what the next person did differently. Different from v1's direct-claim opener. |
| 9 | CON | BCG Case Interview Guide | bcg-case-interview-guide | ultimate-guide, **write as v2** | Scene: the first sixty seconds of a candidate-led case, told from the chair, with the silence after "so how would you approach this?" Different from v1's direct-claim opener. |
| 10 | CON | 10 Case Interview Examples With Full Worked Solutions | 10-case-interview-examples-worked-solutions | listicle (10) | Real public story: Enrico Fermi's "how many piano tuners are in Chicago" estimation (Fermi problems), the ancestor of every market sizing case. Verify the attribution. |

Articles 8 and 9 have v1 drafts in `drafts/` (about 2,000 words each, written before the September thoroughness standard). Read the v1 in full first. Keep what's right, fix anything stale, and write a new v2 that is deeper on every section, with a new intro and a full worked case. Save as `drafts/draft-{slug}-v2.md`. Do not edit v1.

## Per-article guidance

### 1. LBO Model Explained (ultimate-guide)

Target keyword: `lbo model`. Secondary: lbo model explained, how to build an lbo model, lbo model for interviews, paper lbo.

H2 sub-questions: "What is an LBO model?" and "Do undergrads need to build a full LBO model for interviews?"

The article answers, in this order and in depth:

1. **What the model is doing.** Buy a company mostly with borrowed money, run it for about five years, pay down debt with its cash flow, sell it. The three ways the equity makes money (EBITDA grows, debt gets paid down, the exit multiple is higher than the entry multiple) with a small numeric example for each.
2. **Where the information comes from.** Public target: the 10-K (income statement, balance sheet, cash flow statement, the debt footnote, the lease footnote), the 10-Q for the latest quarter, the proxy statement (DEF 14A) for share counts, options and RSUs, the 8-K and press release for deal terms, the credit agreement (an exhibit to the 8-K or 10-K) for interest rates, amortization and covenants, S&P Capital IQ / FactSet / Bloomberg / PitchBook for trading comps, precedent LBO multiples and sponsor data, and leveraged finance market data (PitchBook LCD, for example) for how many turns of leverage the market gives a company like this. Private target in a modeling test or a PE internship: the CIM, the management model, the quality of earnings report. For each source say what you pull and where it sits in the document.
3. **How to input it.** Tab layout (Transaction Assumptions, Sources and Uses, Operating Model, Debt Schedule, Returns, Sensitivities, or one tab with those blocks for a test), color convention (blue hardcodes, black formulas, green links to other tabs), units in one place, three years of history and five to seven years of projection, one assumption column driving the rows, no hardcodes inside formulas.
4. **How to structure it, step by step.** Purchase price (LTM EBITDA times multiple), equity purchase price and net debt, fees. Sources and uses as a table. Operating model from revenue to EBITDA to EBIT to interest to taxes to net income to cash available for debt repayment. Debt schedule by tranche (revolver, term loan B, senior notes, maybe a second lien), interest on average versus beginning balance and the circularity that creates (and the two ways to handle it), mandatory amortization, the cash sweep. Returns: exit EBITDA times exit multiple, minus net debt at exit, equals equity value; MOIC and IRR with the arithmetic shown (and the rule of thumb for IRR from MOIC and years). Sensitivity tables (entry multiple vs exit multiple, leverage vs exit year). Checks: sources equal uses, debt never negative, cash never below the minimum.
5. **A full worked example with numbers that tie**, in tables. Fictional company, round numbers (e.g., $100 million EBITDA, 10x entry, 6x leverage, five years). Script-check it. Show the debt paydown year by year and the IRR.
6. **What to add and what not to add** in a two to three hour modeling test, a paper LBO on a whiteboard, and a PE internship model. What interviewers look at first (the returns and whether the sources and uses balance), what wastes time (PIK toggles, detailed tax schedules, management rollover mechanics, dividend recaps, unless the prompt asks).
7. **The paper LBO** as the interview version: the five-minute walkthrough with a worked example.
8. **Mistakes that get otherwise good models thrown out.**
9. **Templates worth downloading** (only if they clear instruction 11).
10. Say this / don't say that callouts for the common LBO interview questions.

Fun facts to consider (verify each): KKR's founders did "bootstrap" deals at Bear Stearns in the 1960s before founding KKR in 1976; RJR Nabisco in 1988 at about $25 billion and the book Barbarians at the Gate; TXU in 2007 as the largest LBO at the time and its 2014 bankruptcy; the EA take-private announced in 2025 as the largest LBO ever by deal value (verify the terms and status before using).

Internal links to consider: walk-me-through-an-lbo, walk-me-through-a-dcf, 25-private-equity-interview-questions, the PE internship ultimate guide, ebitda-explained, 50-accounting-interview-questions, top-10-private-equity-recruiting-firms.

### 2. Finance Resume Template (ultimate-guide)

Target keyword: `finance resume template`. Secondary: finance resume, resume for investment banking and consulting, finance internship resume, finance resume format.

H2 sub-questions: "What format should a finance resume use?" and "Can the same resume work for banking and consulting?"

Content: the one-page format and why it works for both verticals; the blank template with bracketed placeholders (header line, Education, Experience, Leadership & Activities, Additional Information) and a short note under each section on what goes there; one filled sample for a new fictional person (not John Doe; use a different placeholder name in the same style, e.g., JANE DOE, a junior at a large public university who recruited for both banking and consulting: a boutique IB summer, a consulting club or pro bono consulting role, a case competition, a research assistant job, a campus leadership role); section-by-section rules (consistent with the IB article: GPA rules, bullet formula verb-what-how-number, two to three bullets per role, no objective, no photo, no skills fluff); how a banking screener reads it versus how a consulting screener reads it, and the small changes that tilt the same page one way or the other (which experience goes first, which bullets lead with deal exposure versus leadership and impact, whether test scores appear); file naming and PDF; the mistakes that get a strong resume cut; say this / don't say that bullet rewrites (Don't write / Write).

Differentiate from the live IB resume post (link to it) and the live consulting resume checklist post (link to it): this article is the format itself and the dual-track sample. Don't repeat the IB article's text.

Fun facts to consider (verify): Goldman Sachs's reported applicant count for a recent Summer Analyst class versus seats; McKinsey's reported annual application volume; the origin of the one-page rule.

Internal links: investment-banking-resume live post, how-to-build-a-consulting-resume live post, investment-banking-internship-cv, consulting-cover-letter, 10-investment-banking-internships-to-apply-to-in-2027, 15-best-consulting-internships.

### 3. Asset Management Interview Prep (ultimate-guide)

Target keyword: `asset management interview`. Secondary: asset management interview questions, asset management internship interview, buy side interview undergrad, stock pitch interview.

H2 sub-questions: "What do asset management interviews ask undergrads?" and "Is asset management easier to get into than investment banking?"

Content: how AM differs from IB and from hedge funds (long-only, fundamental versus quant, equity versus fixed income, multi-manager systems like Capital Group's versus star-manager shops); the firms and their undergrad programs (BlackRock, Fidelity, T. Rowe Price, Capital Group, Wellington Management, PIMCO, Vanguard, Invesco, Franklin Templeton, Goldman Sachs Asset Management, J.P. Morgan Asset Management, Morgan Stanley Investment Management, Neuberger Berman, Dodge & Cox, and others you verify) with program names, timing for the next open cycle, and VERIFY tags; the question bank in groups, each question walked with a full sample answer: the stock pitch (full structure: one-line thesis, what the business does, why the market is wrong, valuation, catalysts, risks, what would make you change your mind), market view questions, technicals (P/E, EV/EBITDA, free cash flow yield, DCF basics, and for fixed income roles: price versus yield, duration, credit spreads, each explained from zero with numbers), fit questions (why asset management and not banking, why long-only, what do you read, a holding you'd never own), behavioral questions; a worked sample pitch (fictional company or a real large company with every figure tagged VERIFY or framed as illustrative); the two-week prep plan; say this / don't say that.

Fun facts to consider (verify): Peter Lynch's record; John Bogle launching the first index fund at Vanguard in 1976; BlackRock's AUM today; Capital Group's multiple portfolio manager system dating to 1958.

Internal links: goldman-sachs-asset-management-interview, the-ultimate-guide-to-breaking-into-a-hedge-fund, what-does-an-equity-research-analyst-do, the-ultimate-comparison-equity-research-vs-investment-banking, walk-me-through-a-dcf, bridgewater-associates-internship.

### 4. Net Working Capital (ultimate-guide)

Target keyword: `net working capital`. Secondary: net working capital interview question, change in net working capital, working capital formula, nwc in dcf.

H2 sub-questions: "What is net working capital in an interview answer?" and "Why do banks exclude cash and debt from net working capital?"

Content: the textbook definition versus the banker definition and why they differ; the operating items (receivables, inventory, prepaid expenses versus payables, accrued expenses, deferred revenue) and what each one means in plain words; the sign logic (an increase in NWC uses cash, a decrease frees cash) walked with numbers through the three statements; where it sits in the cash flow statement; how it feeds unlevered free cash flow in a DCF; how it feeds cash available for debt paydown in an LBO; the working capital peg in M&A deals (what the peg is, why buyers and sellers argue about it, how the purchase price adjusts); the cash conversion cycle (DSO, DIO, DPO formulas, each worked with numbers); negative working capital businesses (subscription software, restaurants, Amazon) and why that can be a strength or a warning; how to project NWC in a model (days-based versus percentage of revenue); red flags (receivables growing faster than revenue); the classic interview questions with full answers (inventory up $10 through the three statements; a company pays suppliers faster; why deferred revenue is a liability the company wants; how NWC changes in a recession; what a big NWC build means); say this / don't say that.

Fun facts to consider (verify): Amazon's long run of negative working capital and its cash conversion cycle; Dell's negative cash conversion cycle in the 1990s build-to-order model.

Internal links: 50-accounting-interview-questions, ebitda-explained, walk-me-through-a-dcf, walk-me-through-an-lbo, the-2026-investment-banking-interview-guide-for-sophomores, 10-deal-discussion-questions.

### 5. Three Statement Model (ultimate-guide)

Target keyword: `three statement model`. Secondary: 3 statement model, three statement financial model, modeling test, how to build a three statement model.

H2 sub-questions: "What is a three statement model?" and "How long does a three statement modeling test take?"

Content, in depth: how the three statements connect (net income to the cash flow statement and to retained earnings; D&A; capex to PP&E; working capital changes; debt issuance and repayment to the balance sheet; ending cash from the cash flow statement to the balance sheet), each link explained with a one-line example; where to find the information in a 10-K (Item 8, the three statements, the notes that matter: D&A in the cash flow statement, capex in investing activities, the debt footnote, share count on the cover page and in the EPS note, the effective tax rate in the tax footnote; MD&A for guidance) and in a modeling test case pack; how to input historicals (three years, collapse the company's line items to the ones you need, sign convention, units, keep the company's labels in a column so you can trace them); the assumptions block (revenue growth, gross margin, SG&A as a percent of revenue, D&A as a percent of revenue or of beginning PP&E, capex as a percent of revenue, working capital through days: DSO, DIO, DPO, tax rate, interest rate on debt and on cash, dividends or buybacks, minimum cash); how to structure it, step by step: income statement first, then balance sheet except cash and debt, then cash flow statement, then cash flows back to the balance sheet, then the revolver plug; the balance check row and what it means when the difference is a constant (one missing link) versus growing (a sign or linking error); the interest circularity (interest on average debt) and the toggle to switch it off; formatting conventions (blue hardcodes, black formulas, green links, one formula across each row, years across the top, no hardcodes in formulas, totals as sums); a full worked example with numbers that tie, in tables, with three years of projections and the balance check at zero (script-check it); what to add and what not to add in a two to three hour test (add a revolver plug, a check row, a simple debt schedule, a basic sensitivity if time allows; skip segment builds, detailed tax schedules, stock based compensation detail, multiple tranches, unless asked); a time budget for a two hour test; the errors that fail tests; what the grader opens first; templates worth downloading (only if they clear instruction 11).

Fun facts to consider (verify): VisiCalc, the first spreadsheet, written by Dan Bricklin while at Harvard Business School in 1979; Excel's row limit of 1,048,576; the JPMorgan or Reinhart-Rogoff error from the hook.

Internal links: 50-accounting-interview-questions, walk-me-through-a-dcf, walk-me-through-an-lbo, ebitda-explained, is-wall-street-prep-worth-it, 20-fp-a-interview-questions.

### 6. Consulting Resume (ultimate-guide)

Target keyword: `consulting resume`. Secondary: consulting resume template, consulting resume format, mckinsey resume, consulting resume example.

H2 sub-questions: "What do consulting firms look for on a resume?" and "Should a consulting resume be one page?"

Content: how the MBB resume screen works (what screeners score and in what order: academics, leadership, impact, something distinctive), the same one-page skeleton as the IB template with the consulting tilt (leadership gets more room, every bullet needs a quantified result, breadth matters, test scores sometimes appear for underclassmen, languages and international experience earn a line), **two full inline samples**: Sample A is a junior with a consulting internship (placeholder firm names like "Tier 2 Strategy Consulting Firm" in the same style as the IB sample) plus leadership; Sample B is a sophomore with no consulting experience who still passes the screen (campus leadership with numbers, a research job, a nonprofit or small business, a case competition); bullet rewrites that turn tasks into impact; how to show impact without a consulting internship; where the cover letter fits; the mistakes that get consulting resumes cut; say this / don't say that (Don't write / Write).

Link to the live consulting resume checklist post and differentiate: that one is a checklist with examples, this one is the format plus two full samples.

Fun facts to consider (verify): McKinsey's reported annual application volume and hire rate; the number of resumes a typical MBB campus recruiter screens per school.

Internal links: how-to-build-a-consulting-resume, consulting-cover-letter, how-to-get-into-consulting-as-an-undergrad, 15-best-consulting-internships, consulting-recruiting-timeline-for-undergrads-in-2026, why-consulting-how-to-answer.

### 7. 20 Consulting Behavioral Interview Questions and Sample Answers (listicle, exactly 20)

Target keyword: `consulting behavioral interview questions`. Secondary: consulting fit interview, mckinsey pei questions, bain behavioral interview, bcg behavioral questions.

H2 sub-questions: "How many behavioral questions are in a consulting interview?" and "How is the McKinsey PEI different from a normal behavioral interview?"

Scope: pure behavioral and fit. The site already has a draft "Top 30 Consulting Interview Questions" that mixes fit, behavioral, case openers and market sizing; this article goes deeper on behavioral only, with a full sample answer for every one of the 20. Cover McKinsey's PEI dimensions (verify the current list on mckinsey.com: personal impact, entrepreneurial drive, inclusive leadership, and courageous change if still listed), Bain's and BCG's behavioral styles, and the tier 2 and Big 4 versions.

Per item: H3 "N. Question", then tight bullets (What they're testing / What a strong answer includes / Where it shows up), then a full sample answer of 150 to 250 words in a student's voice (composite, placeholder firm and club names, specific numbers), then one bolded takeaway sentence. Group the 20 under H2s (leadership, impact, drive, teamwork and conflict, failure and growth, motivation). End with say this / don't say that callouts.

Internal links: how-to-ace-the-mckinsey-personal-experience-interview, why-consulting-how-to-answer-it-in-under-90-seconds, how-to-prepare-for-a-consulting-interview, the-ultimate-guide-on-how-to-break-into-mbb, 30-examples-investment-banking-behavioral-interview-questions.

### 8. Bain Case Interview Guide (ultimate-guide, v2)

Target keyword: `bain case interview`. Secondary: bain interview process, bain written case, bain case interview prep, bain associate consultant intern interview.

Read `drafts/draft-bain-case-interview-guide-v1.md` first. Keep its correct structure facts (rounds, interviewer-led first round, candidate-led finals, the written case at some offices, the Sova / TestGorilla test, Bain's published practice cases), verify each against bain.com today, and go much deeper: a full worked Bain-style first-round case with an exhibit and the math, a walk-through of the written case format step by step, the "answer first" synthesis with a worked example of a weak close and a strong close, how Bain's assessment works, the Bain practice cases on bain.com and how to use them, the PE due diligence flavor, the Summer 2028 calendar (applications in 2027, VERIFY), sophomore programs (BEL, CREW, First Forward, BASE; verify names and status), a four-week prep plan, say this / don't say that.

Fun facts to consider (verify): Bill Bain left BCG to found Bain & Company in 1973; Bain Capital was formed in 1984 with Mitt Romney; "A Bainie never lets another Bainie fail"; Bain's "results, not reports" positioning.

Internal links: what-is-a-case-interview, 7-case-interview-frameworks, 10-tips-to-beat-the-case-interview, how-to-prepare-for-a-consulting-interview, the-ultimate-guide-on-how-to-break-into-mbb, 15-best-consulting-internships, consulting-recruiting-timeline-for-undergrads-in-2026.

### 9. BCG Case Interview Guide (ultimate-guide, v2)

Target keyword: `bcg case interview`. Secondary: bcg interview process, bcg casey, bcg online assessment, bcg case interview prep.

Read `drafts/draft-bcg-case-interview-guide-v1.md` first. Keep what's right, verify everything against bcg.com and careers.bcg.com today (the Sep 25 research found BCG Embark as the visible sophomore track and GFL links serving the generic campus page; see the batch log), and go much deeper: how the CCA and Casey screens work and how to prepare (link to the live Casey and online assessment posts rather than re-teaching them in full), a full worked candidate-led case with the structure, an exhibit, the math and the recommendation, the hypothesis-driven approach and how to say "so what" after every number, BCG's scoring dimensions (verify on BCG's own pages before naming them), the behavioral half, BCG's own practice cases, the Summer 2028 calendar (applications in 2027, VERIFY), a four-week prep plan, say this / don't say that.

Fun facts to consider (verify): Bruce Henderson founded BCG in 1963; the experience curve (1966) and the growth-share matrix (1970); BCG's early days inside Boston Safe Deposit and Trust Company.

Internal links: bcg-online-assessment-guide, the-ultimate-guide-to-the-bcg-casey-chatbot-interview, bcg-internship-how-to-win-the-offer, what-is-a-case-interview, 7-case-interview-frameworks, 10-tips-to-beat-the-case-interview, the-ultimate-guide-on-how-to-break-into-mbb.

### 10. 10 Case Interview Examples With Full Worked Solutions (listicle, exactly 10)

Target keyword: `case interview examples`. Secondary: case interview example with solution, practice case interview, market sizing example, profitability case example.

H2 sub-questions: "What does a full case interview answer look like?" and "How many practice cases should you do before an interview?"

Ten original cases, every one a different case type and a different industry: profitability (a regional airline or a restaurant chain), revenue growth (a gym chain), market entry (EV charging, a foreign retailer entering the US), M&A (a snack company buying a competitor), pricing (a software product), market sizing (two: one top-down, one bottom-up), operations and cost (hospital emergency room wait times or a warehouse), new product launch, and private equity due diligence (should a fund buy a car wash chain). Never reuse a firm's published practice case (McKinsey's Beautify and Diconsa, BCG's and Bain's published cases are copyrighted and already covered elsewhere on the site); write originals.

Per case: H3 "N. Case title (type, industry)", then the prompt as the interviewer would say it, the clarifying questions a strong candidate asks and the answers, the structure in prose with the two or three branches that matter, the data or exhibit as a table, the math worked line by line as bullets ending in a bolded result, the "so what," the recommendation in answer-first form as a short quoted paragraph (with risks and next steps), what separates a strong candidate from an average one on this case, and a bolded takeaway. Script-check every number. Vary the lengths; the two market sizing cases run shorter than the M&A case.

Internal links: what-is-a-case-interview, 7-case-interview-frameworks, 10-tips-to-beat-the-case-interview, how-to-prepare-for-a-consulting-interview, ultimate-guide-to-the-mckinsey-case-interview, 10-free-resources-for-case-consulting-prep.

## Output and checks

- Write to `drafts/draft-{slug}-v1.md` (v2 for articles 8 and 9) with the frontmatter from SKILL.md "Output format": `byline: stephen-turban`, `hook_type`, `format`, meta description starting "WSG founder Stephen Turban" at 150 to 160 characters.
- Every H2 carries 2 to 3 self-contained bolded claims. Listicle items: bold the lead and the takeaway. The bold-only read-through must tell the argument.
- Include the two H2 sub-questions right after the intro, each answered in 2 to 4 sentences.
- Blank line before every list and every table (the docx builder needs it). Pipe tables are supported.
- Run the passes in order on your own draft: plain-language, thoroughness (expand every jump), prose editing (echo enders, register words, say-it-out-loud test, burstiness), intros checklist.
- Run: `python3 scripts/check_article.py drafts/{file}.md`, `python3 scripts/check_style.py drafts/{file}.md`, `python3 scripts/check_links.py drafts/{file}.md`. Fix every hard failure. (`check_links` may report wallstreetguide.net or some firm sites as unreachable or 403 from this sandbox; confirm those with WebFetch and note them.)
- Register grep: `grep -inE "delve|landscape|crucial|navigate|ultimately|it's worth noting|in this guide|not just|at the end of the day|game.chang|more than people realize" drafts/{file}.md` and fix every hit.
- Dash grep: `grep -nE "—|–" drafts/{file}.md` must be empty.
- Do NOT build the .docx; the coordinator does that. Do not edit any file other than your own draft and your own scratch files under `/tmp`.
- Final reply to the coordinator (under 450 words): file path, word count, hook used, fun facts used (with the source each was checked against), internal links used, suggested cross-links to other batch articles, newly verified entities (name and URL, so the coordinator can add them to `scripts/verified-brands.txt`), the list of VERIFY tags, anything you couldn't verify and left out, and the Thoroughness Report in the format from `.claude-skill/thorough-explanations.md`.
