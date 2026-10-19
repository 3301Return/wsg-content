# Batch log: 5 IB articles (October 11 to 12, 2026)

Repo: `Downloads/wsg-content-main v2/wsg-content-main` (worked on a copy at `/home/claude/repo`, then synced back). Brief: `claude/batch-brief-oct-11-2026-ib.md`. Instructions used by the agents: `claude/drafting-instructions-oct-11-ib.md`, `claude/qa-instructions-oct-11-ib.md`, `claude/images-instructions-oct-11-ib.md`. Research fact sheets: `claude/research/{slug}.md`. Live-post list: `claude/wsg-live-urls-oct-11-2026.txt` (102 posts). A separate consulting batch ran the same day; its files are `batch-brief-oct-11-2026.md` and `batch-log-oct-11-2026.md`, so this batch's files carry the `-ib` suffix.

## Repeat check (sitemap fetched October 11, 2026; local drafts and published folders)

| Headline | Live? | Drafted before? | Decision |
| --- | --- | --- | --- |
| How to Get Into Investment Banking: The 8-Step Undergrad Roadmap | No. Overlaps three live posts (9 Steps With No Experience; Freshman to Junior Roadmap; How Hard Is It) | No | Keep, written as the eight things to do in date order for the Summer 2028 cycle; links all three |
| Investment Banking Recruiting Timeline 2027: When Everything Actually Happens | No (consulting timeline only) | No | Write |
| Credit Analyst Interview Questions: 20 to Prepare For | No. Two private credit question posts live | No | Written across four credit seats (bank, rating agency, leveraged finance, private credit) |
| The STAR Method for Finance Interviews: Examples That Actually Land | No | No | Write |
| HireVue for Finance: How to Prepare for a Recorded Interview | No. Goldman HireVue questions post live | No | Covers the format across firms; links the Goldman post |

## Founder decisions

- Headlines word for word, all five.
- Cycle: apply in 2027, intern Summer 2028, Class of 2029. Research found the Summer 2028 cycle already open at elite boutiques (Evercore second week of September to November 15, 2026; Harris Williams October 2026 to January 2027), so both recruiting articles say the boutique wave opened in fall 2026.
- Program names as on firm pages today: Goldman Sachs Emerging Leaders Series and Possibilities Series, JPMorganChase Fellowship Program, Citi Early Identification, Morgan Stanley Early Insights, Moelis Leadership Development Program, Barclays Discovery Programme. Legacy names (Launching Leaders, Sophomore Edge, Advancing Black Pathways, Rising Junior Scholarship, Young Leaders, Wells Fargo Sophomore Discovery Fellowship) have no current firm page and aren't used. The live Sophomore Insights post still uses several of them. Jopwell now redirects to another company.
- Credit article: mixed across all four seats, grouped by seat.
- Sanskar's October 12 review of the earlier consulting batch applied to all five in QA: stay on the article's own subject (no explaining the topic by way of an adjacent one), cut the "why" the student doesn't need (history, firm-side rationale, origin stories), use judgment over the checklist. Cuts: HireVue company history and interview counts, DDI and the STAR method's origin, the industrial-psychology background beyond two sentences, rating-agency market share and the US sovereign example, the 2023 to 2024 PE on-cycle backstory, London's firm-by-firm dates, "why banks run early programs," "why a GPA is the first sort," the resume-scan study history, "why private credit grew" beyond two sentences, litigation detail.

## What shipped

All five pass `check_article.py` and `check_style.py`; zero em, en or minus dashes; zero invisible Unicode codepoints in drafts, manifests and .docx XML; .docx author and last-modified-by "Wall Street Guide"; PNG metadata stripped; no personal identifiers in any file. .docx in `published/ai-written/` via `markdown_to_docx_v2.py`, images embedded.

| # | Headline | Format | Words (wc, with tags and image lines) | Pages with images | Images | VERIFY | Links |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | How to Get Into Investment Banking: The 8-Step Undergrad Roadmap | ultimate-guide | 5,896 | 24 | 6 | 36 | 36 |
| 2 | Investment Banking Recruiting Timeline 2027: When Everything Actually Happens | ultimate-guide | 6,118 | 24 | 6 | 70 | 23 |
| 3 | Credit Analyst Interview Questions: 20 to Prepare For | listicle | 6,609 | 28 | 5 | 6 | 23 |
| 4 | The STAR Method for Finance Interviews: Examples That Actually Land | ultimate-guide | 5,790 | 23 | 5 | 5 | 18 |
| 5 | HireVue for Finance: How to Prepare for a Recorded Interview | ultimate-guide | 5,963 | 25 | 6 | 9 | 14 |

Pages are LibreOffice renders of the built .docx (Letter, Arial 11, double spaced), images included; prose alone lands at about 20 to 24 pages each. Article 3 runs longest because each of the 20 answers carries a worked number or table.

## Openings

1. "Getting into investment banking as an undergrad means landing an Investment Banking Summer Analyst seat for the summer before senior year, then converting it into a full-time offer." Bold: Goldman accepted fewer than 1 in 100 intern applicants in 2026, third year under 1 percent.
2. "If you're applying to Investment Banking Summer Analyst programs in 2027, you're competing for Summer 2028 seats, and the first applications opened in September 2026." Bold: Evercore's Summer 2028 window, about four months earlier than its last two cycles.
3. "Credit analyst interview questions test one thing: whether you can tell if a borrower will pay the money back, and what the lender gets if it doesn't." Bold: $1.55 trillion of US leveraged loans outstanding at end-2025.
4. "The STAR method is a four-part structure for answering behavioral interview questions: Situation, Task, Action, Result." Bold: Deloitte, PwC and Bank of America name it; JPMorgan's handbook teaches the same shape.
5. "HireVue is the recorded, one-way video interview most large banks use as the first round for Summer Analyst and full-time campus hiring." Bold: Goldman has used it since 2016; about one in three summer analyst applicants got one in 2019.

## Thoroughness Reports (drafting agents, then QA)

**1. Roadmap.** Expanded 6 (pitch parts in step 2; program list and Wall Street Bound in step 3; the five-sentence email and follow-up sequence in step 4; HireVue and EV vs equity value explained in step 6; superday and rolling screens in step 7; sub-question 1 bold carries the BofA number). Cut 3 echo lines plus the QA section 6 cuts (firm-side program rationale, GPA-sort rationale, resume-scan history). Still thin 2: return-offer timing has no primary source ("at the end of the program"); HL Insight Day session dates unconfirmed. Plain-language rewrites 6 (informational interview, rolling portal, HireVue, superday, staffer, EV vs equity value). About 5,600 prose words; in range.

**2. Timeline.** Expanded 4 (rolling explained with Goldman's worked chain; HireVue and superday defined; London as one short contrast; the on-cycle projection stated as a projection). Cut 3 unsupported claims, then QA cut the Vault/eFC trend paragraph, London's firm dates, the 2023 to 2024 PE backstory, Dimon and Rowan quotes, "Apollo less than half." Still thin 3: share of seats filled through sophomore programs (no public figure); return offer rate (unsourced 70 to 90 percent, tagged); Houlihan Lokey's 2027 open month (widest conflict). Plain-language rewrites 6. About 5,800 words; in range.

**3. Credit.** Expanded 7 (springing covenant; why 1.25x; overadvance; RR4/RR5 bands; floor and OID with the actual SOFR print; the full downside assumption list; revolver, amortization and sponsor at first use). Cut 16 passages from an 8,100-word first draft, then QA cut SEC market share, the US sovereign example, the SBA SOP paragraph, the closing default paragraph, Q18's growth story. Still thin 3: credit memo sections (from practice); lender-form FCCR (stated as the case's definition); Fitch 2026 default rates from secondary summaries (tagged). Plain-language rewrites 14. About 6,330 words; over the 6,000 line because of 20 worked items.

**4. STAR.** Expanded 3 (validity and rubric defined; timed snippets per part; the attempts screen and practice step). Cut 5, then QA cut the DDI origin, the Bain paragraph, Schmidt and Hunter and the extra validity figures, McKinsey PEI to one sentence. Still thin 1: HireVue help-center wording rests on the writer's fetch (Zendesk blocks the workspace). Plain-language rewrites 3. Eight worked answers at 176 to 185 words each. About 5,570 words; in range.

**5. HireVue.** Expanded 4 (Goldman's school and applicant figures; the 13-step on-screen order; the rights sentences; the 150-word budget). Cut 3, then QA cut company history and interview counts, lawsuit detail, the facial-analysis statement quote, firm-side rationales. Still thin 2: BofA's "two or three bankers" (prep guide only); no dated DCF report at a named bank. Plain-language rewrites 5. About 5,700 words; in range.

## Independent QA: corrections made

- **#1:** SEO "86 percent" → "more than 80 percent" (SEO FAQ); HL session dates removed (not on the HL page); M&I figures re-attributed to the right guide; two ibinterviewquestions "quotes" removed (not on the page); full-time timing corrected to late August through November with most BB/EB offers by early October (ibinterviewquestions, February 2026); Goldman return-offer range corrected; Citi Early ID wording matched to Citi's page; a false GPA-arithmetic claim rewritten (3.2 for two semesters plus 4.0 averages 3.47); Evercore live first round added, tagged.
- **#2:** Evercore open "September 9" → "second week of September (Extern September 9, Superday AI September 8)"; Goldman Emerging Leaders deadline no longer public (page says closed); an Extern "110 of 180 banks" figure not on the page replaced with its verified "106 firms, 729 positions by May 2026"; Adventis wording fixed (new postings, "a little under 200 firms"); Centerview window stated as a range with both sources; Moelis Suited assessment moved to the application stage per the firm page; Baird close inferred, not stated; Dimon "Georgetown" quote cut (not in Fortune); Protected Saturdays' 2023 kickoff was August, not June.
- **#3:** cov-lite claim limited to 2021 (the S&P article's year); two non-verbatim quotes de-quoted; doubtful-grade wording corrected to the FDIC manual's; JPMorgan MMBSI drift reworded to the posting; loan call protection corrected (callable any time, at best a 101 soft call for six months or a year); 214/84/42 attributed to Kirkland; "record" → "new high"; two arithmetic wordings fixed (2.9x, 1.7x).
- **#4:** "campus candidates" → "candidates" (Deloitte's page is general); Morgan Stanley quote matched to source; table count 18 → 19; 90-second split corrected to 18/9/54/9; "Done Answering" de-quoted (HireVue's blog says "I'm Done"); RoadToOffer (unverified) not named.
- **#5:** "since July 2016" → "since 2016" (HR Dive's wording); four help-center quotes made verbatim; Morgan Stanley Technology review dated July 2025, not September 2026; Deutsche Bank row limited to "some roles"; retake-erasure claim limited to the guides that say it; DCF attribution generalized; 150 words at 100 to 125 wpm is 72 to 90 seconds, not 80 to 90; NYC "alternative process" right dropped (not on nyc.gov).

## Images (28)

Rebuild from the repo root with `python3 scripts/images/build_{slug}.py`, then `python3 scripts/images/insert_images.py {slug} drafts/draft-{slug}-v1.md` (idempotent). Banking format throughout; every build script asserts its numbers against the draft text and fails on a mismatch; every string went through the plain-language and humanizer passes (examples: "Who gets paid first in a bankruptcy, and how much comes back" → "Order of payment in a bankruptcy, with Moody's recovery rates"; "The ceiling isn't the target" → "Words per part of a 150-word HireVue answer"; a narrative JPMorgan caption → "A JPMorgan link can arrive within hours of applying; Goldman's takes about a week").

| # | Images | What |
| --- | --- | --- |
| 1 | 6 | Goldman and BofA intern applications and acceptance; top feeder schools; fall 2026 program deadlines (dated); networking funnel; firms posting by month; application-to-offer sequence |
| 2 | 6 | Full cycle timeline (dated); fall 2026 program table (dated); Summer 2027 bulge-bracket windows with 2028 expectations (dated); Adventis postings by month (dated); Goldman January 1 chain; PE on-cycle timeline |
| 3 | 5 | Capital structure with recovery rates; rating scales with the investment-grade line; covenant cushion; loan vs bond; downside case |
| 4 | 5 | 90-second time split; structured vs unstructured validity; story bank matrix; worked answer 1 marked up by part; HireVue clock |
| 5 | 6 | Banks' recorded-interview table; boutiques and others; 13-step on-screen sequence; 150-word budget; recording setup; invitation-to-next-step timeline |

**Regenerate at publish (dated):** Roadmap 03; Timeline 01, 02, 03, 04, 05; HireVue 01, 02, 06.

## Links unlinked to pass `check_links.py` from the workspace (live via WebFetch; click-test and restore at publish)

Goldman Sachs: Emerging Leaders Series, Possibilities Series, students/prepare, purpose-and-values, the video-interviewing blog post. Morgan Stanley: students page (`morganstanley.com/people/students-graduates`), core values, interview-preparation. Baird GIB intern page. Bright Network Bank of America page. IGotAnOffer (Goldman HireVue, JPMorgan HireVue, IB behavioral). HireVue Help Center articles (Getting Started 360028433751, Preparing 360028139732, Practice FAQ 360044807611, Due date 360028139832, Devices 360028139752, ADA 360028139512, Restart 360028139712, Tips 360028433631) and the HV-4 tech specs. McKinsey careers/interviewing. University of Cincinnati STAR page. Wall Street Oasis. OCC Rating Credit Risk booklet. PitchBook LCD primer and October 2025 Private Credit Monitor. S&P Understanding Credit Ratings and the 2021 cov-lite article. Moody's Rating Symbols and Definitions PDF. Bloomberg (WBD to junk, May 20, 2025; OneStream, February 12, 2026). Staffing Industry Analysts (Adecco). ABF Journal OCC ABL summary. M&I direct lending. HR Dive (Goldman 2016), eFinancialCareers (July 2018), Courthouse News, Glassdoor JPM and MS pages, Citadel quant interview page, Aced guides, Lawrence and Bentley career pages. Evercore's job board is bot-walled.

## Cross-links to add once live

- Roadmap → Timeline (step 7), STAR (step 6), HireVue (step 7). Timeline → Roadmap, HireVue (January to April section). STAR → HireVue (section 5). HireVue → STAR (sections 4 and 5). Credit → none required.

## Still thin / for the founder

- Return-offer rates and timing: no bank publishes either; both recruiting articles say so and tag the community figures.
- Evercore's 2028 open date: September 8 (Superday AI) or 9 (Extern); the job board is bot-walled.
- Citi Early Identification: Extern's October 23 close conflicts with Citi's "December cohort opens in November"; the timeline table says so.
- Goldman HireVue attempts: one (2018 recruiters) vs one to three (2026 prep sites); both articles tell the reader to check the attempts screen.
- Credit article at about 6,330 prose words; drop Q16's TLA and second-lien follow-ups to land under 6,000 if wanted.
- Fitch 2026 default rates come from secondary summaries (Fitch's site blocks the workspace).
- 126 VERIFY tags remain across the five, all on moving numbers and dates; strip at Wix publish.

## Skills applied

wsg-article (SKILL.md, source-verification, reference-articles, intros, plain-language, thorough-explanations, prose-editing, formatting, images), wsg-intros, wsg-prose-editing and humanizer (drafting and QA passes, and on every image string), wsg-article-images, wsg-article-formatting (built through `markdown_to_docx_v2.py`), clean-user-facing-text and remove-ai-marks (invisible-codepoint and dash scan on drafts, manifests and .docx XML; PNG metadata stripped; .docx author "Wall Street Guide"; no personal identifiers).
