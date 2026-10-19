# Batch brief: 8 WSG articles (October 5, 2026)

Repo root: `/home/claude/repo` (a working copy of the founder's `Downloads/wsg-content-main v2/wsg-content-main`). Today is **Monday, October 5, 2026**. US spelling throughout.

## Founder instructions for this batch (override defaults where they conflict)

1. **Headlines word for word.** Listed below. Do not shorten or retitle, even where a headline runs past the 8-10 word guideline. One founder-approved change: article 1 uses US "Practice", not "Practise".
2. **Repeat check done.** Two of the founder's original eight ("Top 30 Consulting Interview Questions and How to Answer Them" and "How to Pass the Bain SOVA Test") already exist as drafts in `drafts/` and were swapped for "Ultimate Guide to the MECE Framework" and "Centerview Partners: The Complete Career Guide". "Deloitte Strategy & Operations Career Guide" stays but must be clearly differentiated from the live Monitor Deloitte post (see article 6).
3. **Intros must not be cookie cutter.** Each article gets a different hook type AND a different shape from every other article in this batch and from the recent batches (list below). Allowed: first names for composite students ("a sophomore I worked with last spring, call her Priya"), real and verifiable public stories, scenes, first-call quotes, stats with a bite, decision moments, direct claims. Never a full fake name for a composite. WSG never looks bad in its own stories (setbacks happen before someone finds WSG, or to a roommate or friend). Stephen intro present in the first three paragraphs, credentials only from `writers/stephen-turban.md` (Harvard College '17, McKinsey 2017 to 2019, Lumiere co-founder, WSG founder). Keyword in the first 100 words. Two to three short paragraphs, then the H2 sub-questions.
4. **Make the body interesting.** Every article carries 2 to 4 real, verified, interesting facts woven into the body where they teach something (the origin of a term, a famous deal, a founder story, a number that surprises). Verify each on the web before using it. Anything that moves gets a `[VERIFY: ...]` tag. No "Fun fact:" labels. Do not invent a fact to fill the quota.
5. **Technical articles go deep.** Articles 1, 3, 4 and 7 are technical. Walk every mechanism step by step in plain words a sharp high schooler could follow on one read. Use the technical term, then explain it at first use. Work every number. 5,000 to 9,000 words is normal for them. Articles 2, 5, 6 and 8 run 4,000 to 7,000.
6. **All arithmetic in a worked example must tie.** For articles 1, 2, 3 and 4: build the numbers in a Python script first and save that script as `scripts/images/models/numbers_{slug}.py` (plain Python, prints every table the article shows). Paste the printed results into the article tables. State in your final report that the numbers were script-checked. The image agents will rebuild your model in Excel from that script, so keep it clean and commented.
7. **Internal links (backlinks).** Use ONLY URLs listed in `claude/wsg-live-urls-oct-5-2026.txt` (the live sitemap fetched today, 102 posts). Add 3 to 6 internal links per article where they help the reader, as inline anchor text. Never a "related posts" footer. Do not link to the other seven articles in this batch, and do not link to the October 1 drafts (LBO model, three statement model, NWC, asset management, finance resume, consulting resume, 20 behavioral questions, Bain v2, BCG v2, 10 case examples): none of those are live. List suggested cross-links to them in your final report instead.
8. **No em dashes, no en dashes, no hyphens as pause punctuation, no Unicode minus signs.** Grep before you finish: `grep -nE "—|–|−" drafts/{file}.md` must return nothing.
9. **Every named entity verified** per `.claude-skill/source-verification.md` using WebSearch / WebFetch. Tier 1 household names skip verification. Every time-sensitive claim (deadlines, pay, dates, program names, eligibility, test providers, AUM, headcounts, tax brackets) tagged `[VERIFY: ...]` inline AND researched so the stated value is the best current one. If you can't verify a fact, leave it out.
10. **Skip the outline-approval step.** The founder approved the headlines and asked to draft straight through.
11. **Images come later, from a separate agent.** Do not insert image lines. Do write your worked examples as clean pipe tables with a one-line lead-in, because the image agent screenshots a rebuilt workbook of exactly those tables. For article 1, read `reference/dcf-workbook-structure-oct-2026.md` and build the worked DCF test on that layout. Never name, describe or hint at any outside template, workbook, school workshop or person as the source of that layout; it is ours.
12. **No downloadable files from us.** Article-only. Where a free, high-quality outside template exists and clears the bar (free without a paywall surprise, from a source bankers recognize, matches what the article teaches), you may link it once after opening it. Macabacus (trial-gated), Wall Street Prep (email-gated) and CFI (account-gated) may be named, not linked. A Simple Model's LBO download and Mergers & Inquisitions' free Otis three statement file cleared on October 1.

## Required reading (in this order) before drafting

- `CLAUDE.md`
- `.claude-skill/SKILL.md`, `.claude-skill/source-verification.md`, `.claude-skill/intros.md`, `.claude-skill/plain-language.md`, `.claude-skill/thorough-explanations.md`, `.claude-skill/prose-editing.md`
- `style-guide/style-guide.md`, `style-guide/editorial-feedback-may-2026.md`, `style-guide/editorial-feedback-july-2026.md`, `style-guide/seo-checklist.md`, `style-guide/link-verification.md`, `style-guide/recruiting-timeline-glossary.md`
- `writers/stephen-turban.md`
- The matching template in `templates/` and 1-2 samples in `samples/`
- `claude/batch-log-oct-1-2026.md` and `claude/batch-log-sep-25-2026.md` (what shipped, the hooks already used, the founder's review notes) and `claude/corrections-aug-21-2026.md`
- **Consulting articles (5, 6, 7):** also `.claude-skill/consulting.md` and every file in `consulting/` (firm-profiles, recruiting-timeline, case-interview-frameworks, voice-cues, sources/INDEX). Known corrections: MBB undergrad intern recruiting runs IB-style (apply sophomore spring year A for Summer A+1 internships, graduate A+2). The cycle that matters for a reader in October 2026 is **applications in 2027 for Summer 2028 internships (Class of 2029)**. Last cycle's confirmed dates: McKinsey BA intern window Jan 1 to Mar 29, 2026; BCG Summer Associate deadline June 2, 2026; Bain ACI March 29 and August 31, 2026. McKinsey's PEI has three named themes (personal impact, entrepreneurial drive, inclusive leadership). Bain's practice cases live under bain.com/careers/hiring-process/interviewing/. Bain's digital assessment is Sova or TestGorilla.
- **IB articles (1, 2, 3, 4, 8):** `deep-dives/INDEX.md`. For technical sourcing, `400-ib-questions.txt` and `wsp-redbook.txt` in the repo root are text extracts of two interview guides. Grep them for your topic (e.g., `grep -n -i "depreciation" 400-ib-questions.txt | head -40`). Paraphrase and re-derive; never copy their wording or their example numbers.

## Hooks already used recently (do not repeat the shape)

Oct 1 batch: Blackstone's 2007 Hilton buyout (real deal story); first-call quote (Priya, two resumes); Peter Lynch "I never said that" (real public story); reader question plus scene (Dev and the $50 million follow-up); JPMorgan's 2012 VaR spreadsheet cell (real spreadsheet-error story); decision moment (Ana, night before Bain's deadline); Stephen's own McKinsey PEI follow-up memory; friend story (Theo lost the final on the close, Nadia won); the first sixty seconds of a candidate-led case by the clock (scene); Fermi's piano tuners (real public story). Sep 25 batch: friend's younger brother (Owen); Blackstone 57,000 / 138 stat; Einhorn's 2008 Ira Sohn speech; first-call quote; reader question; the silent interviewer scene; decision moment (Leo); US Airways 1549 and checklists. Sep 19 batch: 11:40 pm Sunday resume scene (D); direct claims in the old Bain and BCG v1s.

## The 8 articles

| # | Vertical | Exact headline | Slug | Format | Hook assignment |
|---|---|---|---|---|---|
| 1 | IB | Financial Modeling Test: What to Expect and How to Practice | financial-modeling-test-what-to-expect | ultimate-guide | Real public story: the 2013 Reinhart-Rogoff spreadsheet error. Thomas Herndon, a UMass Amherst graduate student, tried to replicate "Growth in a Time of Debt" (Carmen Reinhart and Kenneth Rogoff, 2010) for a class assignment and found an Excel range that left out five countries. Verify from the Herndon, Ash and Pollin 2013 paper and press coverage (Bloomberg, FT, The Economist), tag what moves. The point for the reader: someone is going to open your spreadsheet and check the cells. |
| 2 | IB | Investment Banking Analyst Salary 2027: What You Actually Take Home | investment-banking-analyst-salary-2027 | ultimate-guide | Stat with a bite: the gross-to-net gap. Lead with the script-checked number from your own worked example (e.g., "A first-year analyst in New York earning about $200,000 all-in keeps about $X after taxes"), then why. |
| 3 | IB | Growth Equity Interview Guide for Undergrads | growth-equity-interview-guide-undergrads | ultimate-guide | Direct claim the reader will want to argue with, about sourcing being the job (growth equity interviews test whether you can find and judge companies before they test whether you can model them). Short, opinionated, then the reason. |
| 4 | IB | The Three Financial Statements: How They Link and How to Explain It | three-financial-statements-how-they-link | ultimate-guide | Question the reader is already asking, phrased the way they'd type it ("how do the three financial statements link together"), framed around the one interview question every bank asks: walk me through $10 of depreciation. Different shape from the Dev scene on October 1 (no scene, no follow-up twist; the question, why it's asked, and the promise). |
| 5 | CON | How to Get Into Bain's Sophomore Programs | bain-sophomore-programs-how-to-get-in | niche (firm-or-role) | Decision moment with a first name: a sophomore with a bank insight program and a Bain early program on the same weekend, or the same application week, calling to ask which one matters more. Different firm and tension from Ana (resume drafts) and Leo (BCG). |
| 6 | CON | Deloitte Strategy & Operations Career Guide | deloitte-strategy-and-operations-career-guide | niche (firm-or-role) | First-call quote: a student asking whether "Deloitte S&O" still exists because an older cousin or club alum did it years ago. Use the quote to open the rename story (the S&O service line became part of Deloitte Consulting's offering portfolios; Monitor Deloitte is the strategy practice inside it). |
| 7 | CON | Ultimate Guide to the MECE Framework | ultimate-guide-mece-framework | ultimate-guide | Scene, first person: Stephen's own McKinsey memory of a manager redrawing an issue tree at a whiteboard and crossing out a branch that overlapped another. Plausible and general; never invent a client, an industry detail Stephen couldn't have said, or a quote. |
| 8 | IB | Centerview Partners: The Complete Career Guide | centerview-partners-career-guide | ultimate-guide | Friend or classmate story with a first name: a Harvard classmate (composite, first name only) who went to Centerview and what the first year looked like from the outside (hours, deal names in the news, the decision not to recruit for PE). Keep every detail plausible and generic; no real person. |

## Per-article guidance

### 1. Financial Modeling Test: What to Expect and How to Practice (ultimate-guide)

Target keyword: `financial modeling test`. Secondary: modeling test, excel modeling test, private equity modeling test, investment banking modeling test, financial modeling test practice.

H2 sub-questions: "What is a financial modeling test?" and "How long is a financial modeling test?"

The article answers, in this order and in depth:

1. **Who gives modeling tests and when.** Private equity (on-cycle and off-cycle associate recruiting, and increasingly the undergrad PE internship process), growth equity, some elite boutiques and middle-market banks (laterals, off-cycle analysts, occasionally Summer Analyst finals), restructuring groups, corporate development, some hedge funds. Say which is common and which is rare; tag anything firm-specific.
2. **The five formats**, each with its time, what you receive, what you hand in, and what it tests: (a) the paper LBO (whiteboard or pen, 20 to 30 minutes, link the live "walk me through an LBO" post rather than re-teaching it); (b) the timed Excel LBO (60 to 120 minutes, a one-page prompt, build from blank); (c) the timed three statement plus DCF or LBO (2 to 4 hours, a case pack with historicals); (d) the take-home case (1 to 5 days, a model plus a 5 to 10 slide memo); (e) the live build on a shared screen. A table comparing them.
3. **What's in the case pack and where each input lives.** CIM excerpt, historical financials, an assumptions page, the prompt, sometimes a blank template with locked formatting. For a public company test: the 10-K lines you need (and only those). Say what you pull from each page.
4. **How graders grade.** What they open first (does it work: the balance check, the sources and uses, the returns or the implied price), what they check second (is it right: the sign on working capital, the tax on EBIT not EBT, the terminal value math, the share count), then speed and cleanliness (one formula per row, blue / black / green, no hardcodes inside formulas, labeled units), then the debrief (can you defend every assumption in two sentences). A simple five-part rubric table.
5. **A full worked example: a two-hour DCF-based modeling test.** Build it on the layout in `reference/dcf-workbook-structure-oct-2026.md` for a fictional company you invent (an industrial or consumer company with two or three segments; not an electronics retailer). Three years of historicals, five projected years, a scenario switch (Bear / Base / Bull), segment revenue build, margins, working capital by days, PP&E roll-forward, tax on EBIT, unlevered free cash flow, WACC by CAPM with an unlevered-and-relevered beta from a small peer set (fictional peers labeled as such, or real large-cap peers with every figure tagged VERIFY), discounting from a valuation date (explain the year-fraction and mid-year choices in plain words), terminal value by exit multiple with a Gordon growth cross-check, enterprise value to equity value to implied share price, and a WACC-versus-exit-multiple sensitivity grid. Script-check every table (instruction 6). Show the tables in build order with the formulas described in words beside them ("NOPAT is EBIT times one minus the tax rate"). Say what a take-home version adds (comps tab, football field, the memo).
6. **A time budget for the two-hour test**, minute by minute, and the order to build in so a half-finished model still scores (inputs, then the operating build, then the DCF, then checks, then sensitivities, then formatting).
7. **What to add and what not to add** under time pressure (add: a check row, a scenario switch if it's quick, a one-line sensitivity; skip: segment detail beyond what's given, tax schedules, stock comp detail, a full comps tab, chart formatting).
8. **The mistakes that fail tests.** Working capital sign flipped, terminal value not discounted, mixing fiscal and calendar years, hardcoding a plug, circular references without a toggle, an unlabeled unit, a model that only works for the base case.
9. **How to practice, four weeks out and one week out.** Free resources (Mergers & Inquisitions' free three statement file, A Simple Model, Macabacus / WSP / CFI named not linked, the SEC's EDGAR for real 10-Ks), the rebuild-from-memory drill (build the same model three times, blank sheet each time, timed), the 20 Excel shortcuts that matter (list them, with what each does), the no-mouse rule, auditing with F2 and Ctrl+[ and trace precedents.
10. **The debrief:** say this / don't say that for the questions graders ask afterward ("Why 2.5 percent terminal growth?", "What would change your number the most?", "Walk me through the working capital line").

Fun facts to consider (verify): the Reinhart-Rogoff error from the hook; the Excel row limit (1,048,576); that the first spreadsheet, VisiCalc, was written in 1979 by a Harvard Business School student (Dan Bricklin) with Bob Frankston; Lotus 1-2-3's role on 1980s Wall Street.

Internal links to consider: walk-me-through-a-dcf, walk-me-through-an-lbo, private-equity-interview-questions-25-for-undergrad-candidates, the PE internship ultimate guide, 50-accounting-interview-questions, is-wall-street-prep-worth-it, 25-private-equity-interview-questions-that-actually-get-asked.

### 2. Investment Banking Analyst Salary 2027: What You Actually Take Home (ultimate-guide)

Target keyword: `investment banking analyst salary`. Secondary: investment banking analyst salary 2027, first year analyst salary, investment banking bonus, investment banking analyst take home pay, investment banking salary new york.

H2 sub-questions: "How much does a first-year investment banking analyst make?" and "How much of an investment banking salary goes to taxes?"

"2027" means the analyst class that starts in summer 2027. State early that the figures are the latest confirmed numbers (the 2026 class and the Summer 2026 bonus season) and that 2027 is a projection, tagged.

Content, in depth:

1. **The pay stack.** Base, signing bonus, relocation, the stub bonus (first partial year, paid at year-end for a July start, prorated), the full-year bonus, the second and third-year base steps. Explain each in plain words.
2. **Base salary by firm tier** for first, second and third-year analysts: bulge bracket, elite boutique, middle market, regional. Research the current numbers (the 2021 raise wave, the 2024 and 2025 moves; which banks are at $110,000, which at $120,000 or above; Centerview and Evercore at the top). Every figure tagged VERIFY with the source named in the tag. A table.
3. **Bonus ranges by bucket** (top, middle, bottom) and how banks decide them (the ranking, the bonus pool, deal flow, group). The Summer 2026 bonus season numbers if reported (Wall Street Oasis, Litquidity, press) with tags. Why the same base can produce very different all-in.
4. **The take-home math, fully worked.** One first-year analyst in New York City, single, no dependents, $120,000 base plus an $80,000 bonus (or your researched figures), for the 2026 tax year: federal income tax by bracket (the 2026 brackets and the standard deduction from IRS Rev. Proc. 2025-32, tagged), Social Security (6.2 percent up to the 2026 wage base, tagged), Medicare (1.45 percent, plus the 0.9 percent additional above $200,000), New York State tax by bracket, New York City resident tax by bracket, then the net. Show the arithmetic line by line in a table, script-checked (instruction 6). Then the same analyst with a 6 percent 401(k) contribution and a typical health premium, to show what pre-tax deductions do. Explain why the bonus check looks small (federal supplemental withholding at 22 percent, New York's supplemental rate, FICA all at once) and why that is withholding, not the final tax.
5. **The same gross in four cities**: New York, Charlotte, Houston, San Francisco (or Chicago), with state and city tax differences worked, so the reader sees the spread. Tag each state's 2026 rates.
6. **A monthly budget for the New York first-year**: rent ranges by neighborhood (tagged), the 40x rent rule landlords use, transit, food, the first-year savings rate that's realistic.
7. **Pay over the three analyst years and the jump to associate**, and how IB pay compares with McKinsey (link the live McKinsey salary post), private credit (link the live private credit salary post) and equity research (link the ER post).
8. **What moves 2027 pay**: deal activity, the bonus pool, the bank's year, and the history of base raises. The 2021 Goldman analyst survey that triggered the raise wave (verify from press).
9. Say this / don't say that for the comp questions students ask on networking calls and in interviews ("What's the bonus like?" is the wrong question; what to ask instead).

Fun facts to consider (verify): the 2021 Goldman first-year analyst "working conditions" survey and the $110,000 base raises that followed; the Social Security wage base history; that New York City is one of the few US cities with its own income tax.

Internal links: private-credit-salary-2026, mckinsey-salary-2026, what-does-an-equity-research-analyst-do, how-hard-is-it-to-get-into-investment-banking, top-10-investment-banks, investment-banking-summer-internship-what-is-it-and-how-to-convert-to-full-time, top-middle-market-investment-banks.

### 3. Growth Equity Interview Guide for Undergrads (ultimate-guide)

Target keyword: `growth equity interview`. Secondary: growth equity interview questions, growth equity internship, growth equity analyst, growth equity vs private equity, growth equity sourcing.

H2 sub-questions: "What do growth equity interviews ask?" and "Do growth equity firms hire undergrads?"

Content, in depth:

1. **What growth equity is**, in plain words, against venture and buyout: minority stakes in companies that already work (real revenue, 25 percent plus growth, profitable or close), little or no debt, preferred stock with downside protection. One paragraph per difference, with a number.
2. **The firms and their undergrad programs**: General Atlantic, Insight Partners, TA Associates, Summit Partners, Spectrum Equity, JMI Equity, Stripes, Level Equity, PSG, Great Hill Partners, Silversmith, Volition, Sageview, TCV, Vista's growth arm, and others you verify. For each: whether it hires analysts out of undergrad, whether it runs a summer internship, when the next cycle opens (tagged), what the analyst does. Verify every program on the firm's own site; drop any you can't.
3. **What the analyst actually does**: sourcing (cold emails and calls, CRM, the weekly company count), market maps, first screens, the deal team work once a company is live. Explain why sourcing is the job at the analyst level and why interviews test it.
4. **The interview process** step by step: resume screen, phone screen, the sourcing or "pitch me a company" conversation, the case (evaluate a company from a short deck), the modeling test (a growth model and a cap table), the behavioral round, the final with partners.
5. **The question bank, grouped, every question with a full sample answer**: why growth equity (versus PE, VC, banking); sourcing questions ("how would you find companies in vertical X", "what's a company you'd want us to look at and why", "what do you do when the founder won't take the call"); SaaS and growth metrics, each explained from zero with a worked number: ARR, net revenue retention, gross retention, gross margin, CAC and CAC payback, LTV to CAC, the Rule of 40, burn multiple, magic number; valuation (EV to revenue multiples, growth-adjusted multiples, why growth companies aren't valued on EBITDA); deal terms, each walked with numbers: liquidation preference (1x non-participating versus participating), the difference between pre-money and post-money, dilution, a simple cap table; judgment questions ("what would make you pass on a company growing 80 percent"); behavioral.
6. **A full worked investment screen** for a fictional software company (name it; invent the numbers): ARR, growth, retention, margins, CAC payback, burn; a proposed $100 million investment at a stated post-money; three exit scenarios five years out with the return to the preferred shown both with and without a 1x preference (so the reader sees what the preference does); MOIC and IRR arithmetic shown. Script-check (instruction 6).
7. **A sourcing drill** the reader can run this week (pick a vertical, build a 30-company list, write the first email), with a sample email.
8. **The four-week prep plan** and say this / don't say that.

Fun facts to consider (verify): TA Associates was founded in 1968; General Atlantic was founded in 1980 by Chuck Feeney, the Duty Free Shoppers co-founder who gave away his fortune; Summit Partners in 1984; Insight Partners in 1995 by Jeff Horing and Jerry Murdock; the "Rule of 40" popularized by Brad Feld in 2015.

Internal links: the-ultimate-guide-to-landing-a-private-equity-internship-as-an-undergrad, private-equity-interview-questions-25-for-undergrad-candidates, venture-capital-internships-for-undergrads, private-credit-vs-private-equity, walk-me-through-an-lbo, top-10-private-equity-recruiting-firms.

### 4. The Three Financial Statements: How They Link and How to Explain It (ultimate-guide)

Target keyword: `three financial statements`. Secondary: how the three financial statements link, how do the 3 statements connect, walk me through the three financial statements, income statement balance sheet cash flow statement, $10 depreciation question.

H2 sub-questions: "How do the three financial statements link together?" and "What is the $10 of depreciation question?"

Differentiate from the live "50 accounting interview questions" post (link it once) and from the October 1 three statement model article (which teaches building a model; this one teaches the links and the interview answers). Content, in depth:

1. **Each statement in plain words**: what it measures, over what period, the lines that matter, where it sits in a 10-K. One short section each.
2. **The six links**, each with a one-line example and a number: net income to the top of the cash flow statement and into retained earnings; depreciation and amortization added back on the cash flow statement and reducing PP&E; capex in investing activities and increasing PP&E; working capital changes on the cash flow statement and on the balance sheet; debt raised or repaid in financing activities and on the balance sheet; ending cash from the cash flow statement onto the balance sheet. Then why the balance sheet balances, in plain words (every transaction touches two things).
3. **The order to walk them in an interview** (income statement, cash flow statement, balance sheet) and why, with the 30-second version and the two-minute version written out.
4. **Walk me through $10 of depreciation**, line by line, using a 25 percent tax rate and saying why older guides use 40 percent. Show the income statement effect, the cash flow effect, the balance sheet effect, and the balance check, in a table.
5. **Ten more scenarios, each worked the same way**: inventory up $10 paid in cash; inventory up $10 on credit; $100 of capex paid in cash; raise $100 of debt; buy back $50 of stock; $20 of deferred revenue collected; a $50 write-down of PP&E; a $10 dividend; accrued expenses up $10; the sale of equipment for more than book value. Vary the lengths.
6. **A mini set of statements that tie**: a fictional company (name it), Year 1 to Year 2, all three statements in tables with the links labeled, balance check zero, script-checked (instruction 6). Then "what changed and why" in prose.
7. **The follow-ups**: which statement would you pick if you could only have one (and the real answer, with the argument for each); can a company have positive net income and negative cash flow; how the statements differ for a bank, a software company, a retailer; what goes above and below the line.
8. **Where to find each line in a 10-K** (Item 8; the notes that matter).
9. **Mistakes in interview answers** (saying "depreciation is cash", forgetting the tax shield, starting on the balance sheet, forgetting that cash is on the balance sheet too) and say this / don't say that.

Fun facts to consider (verify): Luca Pacioli's 1494 Summa de arithmetica codified double-entry bookkeeping, and he was a friend of Leonardo da Vinci; the cash flow statement only became required in the US in 1987 (FASB Statement No. 95); the first SEC-mandated annual reports (10-K) date to the 1930s securities laws.

Internal links: 50-accounting-interview-questions, ebitda-explained, walk-me-through-a-dcf, the-2026-investment-banking-interview-guide-for-sophomores, 10-deal-discussion-questions, 20-fp-a-interview-questions, top-10-free-resources-for-investment-banking-interview-questions-in-2026.

### 5. How to Get Into Bain's Sophomore Programs (niche, firm-or-role, consulting)

Target keyword: `bain sophomore programs`. Secondary: bain sophomore internship, bain BEL program, bain CREW program, bain first forward, bain consulting kickstart.

H2 sub-questions: "What sophomore programs does Bain offer?" and "Does Bain have a sophomore internship?"

Lead with Bain's perspective (what the firm wants from early programs: an early pipeline into the Associate Consultant Intern process, a wider range of backgrounds, a first look at strong sophomores before the ACI cycle), then back-derive what makes a competitive applicant. Content:

1. **The programs, one section each, verified on bain.com and university career pages today**: Building Entrepreneurial Leaders (BEL), CREW, First Forward, Consulting Kickstart (the fall 2026 webinar series the October 1 research found, deadline October 5, 2026), and any sophomore summer track Bain runs in the US (research whether Bain posts a sophomore internship or a "Summer Associate Consultant" program for sophomores; if none exists, say so plainly and point to the ACI track). BASE is pre-MBA: mention once to exclude it. For each program: what it is, who it's for (class year, background), where (offices), format and length, what you do during it, what it leads to (fast-track to ACI interviews, mentorship), the next cycle's expected window with a VERIFY tag, and the application pieces.
2. **The timeline for a Class of 2029 sophomore**: early programs in spring and summer 2027, ACI applications in 2027 for Summer 2028, full-time 2029. Don't recite timeline math at the reader; one clean table.
3. **What Bain screens for** (academics, leadership with numbers, a reason for Bain that isn't "culture", the short-answer questions), and how to write the application pieces, with a sample short answer.
4. **The interview or selection step**, if a program has one (a conversation, a short case, a video), verified; and how it differs from the ACI case interview (link the live case-prep posts).
5. **How a program converts into an ACI offer**, and what to do in the months between.
6. **If you don't get in**: the ACI main track, BCG Embark (link the live BCG sophomore post), McKinsey SSBA, bank insight programs (link the live sophomore insight programs post), and how to use the fall of sophomore year.
7. Say this / don't say that for the "why Bain" and "why consulting" answers at the sophomore stage.

Fun facts to consider (verify): Bill Bain left BCG to found Bain & Company in 1973; "A Bainie never lets another Bainie fail"; Bain's long run near the top of Glassdoor's Best Places to Work; the BEL program's founding year.

Internal links: how-to-get-the-bcg-sophomore-internship, consulting-recruiting-timeline-for-undergrads-in-2026, 15-best-consulting-internships, the-ultimate-guide-on-how-to-break-into-mbb, how-to-get-into-consulting-as-an-undergrad, how-to-build-a-consulting-resume, top-10-sophomore-insights-programs-for-ib, consulting-online-assessments.

### 6. Deloitte Strategy & Operations Career Guide (niche, firm-or-role, consulting)

Target keyword: `deloitte strategy and operations`. Secondary: deloitte s&o, deloitte consulting analyst, deloitte consulting business analyst, deloitte strategy and analytics, deloitte consulting interview.

H2 sub-questions: "Does Deloitte still have a Strategy & Operations practice?" and "How is Deloitte S&O different from Monitor Deloitte?"

The live post "Monitor Deloitte Careers: Salaries, Interviews, How to Get Hired" covers the strategy practice; link it in the first sub-question answer and do not repeat it. This article is the guide to the wider Deloitte Consulting analyst track that S&O became. Content:

1. **The rename, in plain words.** Research the current structure on deloitte.com: the old Strategy & Operations service line, the move to offering portfolios (verify today's names: Strategy & Analytics, Customer & Marketing, Core Business Operations, Enterprise Technology & Performance, Human Capital, or whatever Deloitte lists now), where Monitor Deloitte sits, and what "S&O" means when a student says it today. Tag every structural claim.
2. **What the work is**: operations transformation, supply chain, M&A integration, finance transformation, growth and corporate strategy on the Monitor side, with a one-paragraph example project for each (fictional client, plausible scope).
3. **The analyst track**: role titles (Analyst, Consultant, Senior Consultant, Manager, Senior Manager, Principal / Managing Director; verify), the Summer Scholar internship, the Discovery internship for freshmen and sophomores (verify), class sizes relative to MBB, target schools and how non-targets get in, the staffing model, travel, hours.
4. **Pay**, with every figure tagged: analyst base, signing, bonus, the Summer Scholar weekly rate, and how it compares to MBB and tier 2 (link the live Monitor post for the strategy-side comp).
5. **The interview process**, step by step: application, the online assessment if any, first round (behavioral plus case), the group case at some campuses (verify), the final round; what Deloitte's case style looks like (shorter, more conversational, often operations flavored) with a short worked example.
6. **The recruiting timeline** for Summer 2027 internships (many Deloitte applications open in late summer and fall 2026, verify what's open today) and Summer 2028, with a table.
7. **Exits and MBA sponsorship** (the Graduate School Assistance Program, verify), corporate strategy, PE operations roles, tech.
8. **Who should pick Deloitte over MBB or tier 2**, framed positively, and say this / don't say that for "why Deloitte".

Fun facts to consider (verify): William Welch Deloitte, London, 1845; Deloitte's acquisition of Monitor Group in 2013; Deloitte University in Westlake, Texas; Deloitte Consulting's revenue scale against MBB.

Internal links: monitor-deloitte-careers-salaries-interviews-how-to-get-hired (required), top-10-consulting-jobs-for-undergrads-in-2026, consulting-recruiting-timeline-for-undergrads-in-2026, how-to-prepare-for-a-consulting-interview, consulting-case-study-how-to-structure-your-answer-under-pressure, top-10-consulting-exit-opportunities, how-to-build-a-consulting-resume.

### 7. Ultimate Guide to the MECE Framework (ultimate-guide, consulting)

Target keyword: `mece framework`. Secondary: mece principle, mece meaning, mece case interview, issue tree, mutually exclusive collectively exhaustive.

H2 sub-questions: "What does MECE mean?" and "Why do consulting interviewers care about MECE?"

First-person McKinsey framing is right for this one. Content, in depth:

1. **MECE in plain words**, with a non-business example first (sorting people by age bands, then the overlap and gap failures), then the business one.
2. **Where it came from** (Barbara Minto at McKinsey in the 1960s and the Pyramid Principle; verify dates and her role) and why it stuck.
3. **The four ways to cut a problem**, each with a worked tree: by formula (profit equals revenue minus cost; revenue equals price times volume), by process or sequence (the customer journey, the supply chain), by segment (customer, product, geography, channel), by opposites (internal versus external, new versus existing, fixed versus variable). When each works and when it doesn't.
4. **The two tests** (overlap, gap) and how to run them on a tree in 30 seconds, with examples that pass and fail.
5. **Four worked issue trees in prose and bullets**: a profitability case (an airline or a restaurant chain), a market entry case, a revenue growth case, an operations case. Each with the top-line question, the branches, the sub-branches, and which branch you'd prioritize and why. Draw each with indented bullets so the image agent can render it.
6. **The common failures**: overlap, gaps, the "other" bucket, a list instead of a tree, mixing two cutting logics at one level, seven branches when three would do, structures with no hypothesis.
7. **MECE at every level of the case**: the opening structure, the hypotheses, the synthesis ("three reasons, no overlap"), the final recommendation, the slide.
8. **MECE outside the case**: a resume, an email to a manager, a consulting slide, a cover letter.
9. **The limits**: "MECE enough" versus perfect; why interviewers prefer a clear three-branch tree to a perfect seven-branch one; when to abandon the tree.
10. **Ten drills with answers** (segment the revenue of a coffee chain; why are ER wait times up; the costs of a gym; how a bank could grow deposits; and so on), each with a MECE tree and one common non-MECE attempt.
11. Say this / don't say that when presenting a structure in a case.

Fun facts to consider (verify): Barbara Minto was McKinsey's first female MBA consultant (1963, from Harvard Business School); The Pyramid Principle's publication history; the acronym's pronunciation ("me-see").

Internal links: 7-case-interview-frameworks, what-is-a-case-interview, consulting-case-study-how-to-structure-your-answer-under-pressure, 10-tips-to-beat-the-case-interview, ultimate-guide-to-the-mckinsey-case-interview, 25-case-interview-questions-to-practice-before-your-first-round, how-to-prepare-for-a-consulting-interview.

### 8. Centerview Partners: The Complete Career Guide (ultimate-guide, IB)

Target keyword: `centerview partners`. Secondary: centerview partners careers, centerview partners salary, centerview analyst salary, centerview partners internship, centerview interview.

H2 sub-questions: "What is Centerview Partners known for?" and "How much do Centerview Partners analysts make?"

This is the definitive career page for a navigational keyword. Operator framing (Stephen is not a banker). Content:

1. **What Centerview is**: founded in 2006 by Blair Effron and Robert Pruzan (verify), independent advisory only (no lending, no trading, no capital markets), offices (verify), size (partners and headcount, tagged), and the deals it's known for (verify at least four large recent mandates via press releases or Bloomberg / WSJ / Reuters, with the role Centerview played, tagged). Why clients hire a firm with no balance sheet, in plain words.
2. **How it differs from a bulge bracket and from the other elite boutiques** (Evercore, PJT, Moelis, Lazard, Qatalyst, Perella Weinberg): generalist analysts, lean deal teams, the partner-to-analyst ratio, the M&A-only focus, no coverage group silos.
3. **The analyst program**: three years, generalist staffing, the famously top-of-street pay (research and tag: base, bonus, all-in), the direct-promote path, Centerview's stance on PE recruiting (research the firm's historical policy of asking analysts not to recruit on-cycle and whether that holds today; tag), what analysts actually do day to day, hours.
4. **The Summer Analyst program**: when the Summer 2028 cycle is expected to open (applications in 2027, tagged), the application components, target schools and how non-targets get in, the cover letter question.
5. **The interview process**, step by step: first round, superday, the technical bar (higher than most BBs: accounting, valuation, merger math, a full paper LBO), the "why Centerview" and "why advisory" answers, the behavioral style.
6. **A technical mini-drill** of six questions Centerview-style interviewers favor, each answered in full (accretion / dilution math, a paper LBO, a DCF question, an M&A process question).
7. **Culture, hours, and the honest read** (the trade-offs: intensity, small class, less structure, fewer exit-timing options if you don't recruit on-cycle).
8. **Exits**: where Centerview analysts go, direct promotion, and the reputation effect on PE and hedge fund recruiting.
9. **How to network into Centerview** (coffee chats, alumni, the right ask), and say this / don't say that for the interview.

Fun facts to consider (verify): the founding story (Effron from UBS, Pruzan from Wasserstein Perella); Centerview's revenue per partner or per banker if a credible source reports it; a famous mandate (verify every detail).

Internal links: top-10-investment-banks, top-m-a-investment-banks, how-hard-is-it-to-get-into-investment-banking, 10-investment-banking-internships-to-apply-to-in-2027, the-2026-investment-banking-interview-guide-for-sophomores, how-to-prepare-for-evercore-investment-banking-interview-questions, 30-examples-investment-banking-behavioral-interview-questions, investment-banking-resume-the-one-page-template.

## Output and checks

- Write to `drafts/draft-{slug}-v1.md` with the frontmatter from SKILL.md "Output format": `byline: stephen-turban`, `hook_type`, `format` (and `sub_type` for niche), meta description starting "WSG founder Stephen Turban" at 150 to 160 characters.
- Every H2 carries 2 to 3 self-contained bolded claims. The bold-only read-through must tell the argument.
- Include the two H2 sub-questions right after the intro, each answered in 2 to 4 sentences.
- Blank line before every list and every table (the docx builder needs it). Pipe tables are supported.
- Run the passes in order on your own draft: plain-language, thoroughness (expand every jump), prose editing (echo enders, register words, say-it-out-loud test, burstiness), intros checklist.
- Run: `python3 scripts/check_article.py drafts/{file}.md`, `python3 scripts/check_style.py drafts/{file}.md`, `python3 scripts/check_links.py drafts/{file}.md`. Fix every hard failure. (`check_links` may report wallstreetguide.net or some firm sites as unreachable or 403 from this sandbox; confirm those with WebFetch and note them.)
- Register grep: `grep -inE "delve|landscape|crucial|navigate|ultimately|it's worth noting|in this guide|not just|at the end of the day|game.chang|more than people realize|testament|underscores|pivotal" drafts/{file}.md` and fix every hit.
- Dash grep: `grep -nE "—|–|−" drafts/{file}.md` must be empty.
- Do NOT build the .docx; the coordinator does that. Do not edit any file other than your own draft, your own `scripts/images/models/numbers_{slug}.py`, and scratch files under `/tmp`.
- Final reply to the coordinator (under 450 words): file path, word count, hook used, fun facts used (with the source each was checked against), internal links used, suggested cross-links to other batch articles and to the October 1 drafts, newly verified entities (name and URL, so the coordinator can add them to `scripts/verified-brands.txt`), the list of VERIFY tags, anything you couldn't verify and left out, the worked-example tables the image agent should screenshot (by section), and the Thoroughness Report in the format from `.claude-skill/thorough-explanations.md`.
