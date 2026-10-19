# Batch brief: 5 WSG articles (October 11, 2026)

Repo root: `/home/claude/repo` (a working copy of the founder's `Downloads/wsg-content-main v2/wsg-content-main`). Today is **Sunday, October 11, 2026**. US spelling throughout. Rules in force: `.claude-skill/SKILL.md` (October 8 review on top), `intros.md`, `plain-language.md`, `thorough-explanations.md`, `prose-editing.md`, `images.md`, `formatting.md`, `source-verification.md`, `style-guide/recruiting-timeline-glossary.md`. Calibrate on `samples/reference-articles.md` and the three Stephen-endorsed samples only.

Research fact sheets (every fact below is sourced there): `claude/research/{slug}.md`. Live-post list for internal links: `claude/wsg-live-urls-oct-11-2026.txt` (102 posts, sitemap fetched October 11, 2026; same set as October 5).

## Founder decisions taken before drafting

1. **Headlines word for word.** All five as sent, including the subtitles.
2. **Repeat check done.** None of the five is live or drafted. Three live posts overlap article 1 ("How to Get Into Investment Banking With No Experience: 9 Steps That Work," "Investment Banking Preparation: The Freshman to Junior Roadmap," "How Hard Is It to Get Into Investment Banking? 6 Things That Actually Matter"). Founder: keep article 1, differentiate it (semester-by-semester checklist for the Summer 2028 cycle) and link all three. Two live private credit question posts overlap article 3; founder: write it across all four credit seats (bank, rating agency, leveraged finance, private credit), grouped by seat. A live Goldman HireVue questions post overlaps article 5; article 5 covers the format across firms and links it.
3. **Cycle.** Article 2 and every recruiting reference: apply in 2027, intern Summer 2028, Class of 2029 (sophomores in 2026-2027). Research finding the articles must handle: the Summer 2028 cycle is already open at elite boutiques (Evercore September 9 to November 15, 2026; Harris Williams October 2026 to January 2027; Moelis Houston to December 14; PWP TPH to November 10). Bulge brackets are expected December 2026 to January 2027. "Apply in 2027" is right for bulge brackets and the middle market; the articles say the boutique wave opened in fall 2026.
4. **Program names.** Use the names on firm pages today: Goldman Sachs Emerging Leaders Series (sophomores) and Possibilities Series (first-years); JPMorganChase Fellowship Program; Citi Early Identification; Morgan Stanley Early Insights; Moelis Leadership Development Program; Barclays Discovery Programme. Legacy names (Launching Leaders, Sophomore Edge, Winning Women as a program, Advancing Black Pathways, Undergraduate Camp, Rising Junior Scholarship, Young Leaders, Early ID Leadership Program, Wells Fargo Sophomore Discovery Fellowship) have no current firm page and are not used. Jopwell redirects to another company and is not cited.
5. **Length.** 5,000 to 6,000 words each before images (20 to 25 pages). Article 3 (20 worked answers) may run to about 6,500; the Thoroughness Report says why.
6. **Intros** per `intros.md`: sentence one answers the headline, a bolded full-sentence fact, one line of facts, one line on what the article covers. Light first person for framing only. No bio, no stories, no "most candidates."
7. **Outline approval:** condensed outlines posted to the founder October 11; drafting starts on approval.
8. **Images:** 4 to 6 per article, banking format, built from the article's numbers (`scripts/images/wsg_viz.py`, `wsg_diagrams.py`), manifests with source lines, humanizer pass on every string, inserted with `insert_images.py`. Dated calendar images go in the batch log under "regenerate at publish."
9. **Delivery:** `drafts/draft-{slug}-v1.md`, `published/ai-written/{Title}.docx` via `markdown_to_docx_v2.py`, images in `published/assets/images/{slug}/`, this brief, the batch log, and the live-URL list, committed back to the founder's folder. Thoroughness Reports in chat.

---

## Article 1: How to Get Into Investment Banking: The 8-Step Undergrad Roadmap

- **Slug:** `how-to-get-into-investment-banking-8-step-roadmap`
- **Format:** ultimate-guide (numbered claim headings)
- **Target keyword:** how to get into investment banking
- **Secondary:** investment banking roadmap, Investment Banking Summer Analyst, IB recruiting for undergrads, how to break into investment banking
- **Reader:** a freshman or sophomore at any school, Class of 2029 or 2030, who wants the whole path in order
- **Differentiation:** the three live posts argue what matters (How Hard), give nine fixes for a student with no experience, and give a year-by-year prep plan. This one is the eight things to do, in the order they come due, pinned to the Summer 2028 cycle's real dates, with the interview process and the return offer included.

Intro: "Getting into investment banking as an undergrad means landing an Investment Banking Summer Analyst seat for the summer before senior year, then converting it into a full-time offer." Bold: "**Goldman Sachs accepted fewer than 1 in 100 of its intern applicants in 2026, the third year in a row below 1 percent.**" Line: the seat is decided in sophomore year; Summer 2028 applications opened in September 2026 at elite boutiques and open in December 2026 and January 2027 at bulge brackets. Last: "In this article, I lay out the eight steps in order, from freshman fall to the full-time offer, with the dates that matter for the Class of 2029."

Sub-questions (H2, exact search phrasing):
- How hard is it to get into investment banking? (Under 1 percent at Goldman; Bank of America about 0.8 percent on 240,000 applications; but a process, not a lottery. Link How Hard post.)
- Do you need to go to a target school to get into investment banking? (No. College Transitions sample of about 10,500 analysts: NYU 386, Michigan 296, Cornell 279, Baruch 168 in 11th. Goldman's 2024 class came from more than 475 schools; Bank of America's 2026 campus class from more than 500.)

Body (numbered claim headings, under 12 words):
1. A GPA above 3.5 is the first filter, so protect it from day one. (BofA 3.5 preferred; Goldman no published minimum; M&I: non-targets need 3.8 or higher.)
2. Join one finance club and produce one number from it. (Student funds: Nittany Lion Fund $10M+ run by 40 students a semester; Maize & Blue Fund $700,000+ with 3 to 4 person pitch teams; CFA Research Challenge teams of 3 to 5.)
3. Apply to the freshman and sophomore programs, because they are the earliest door. (Possibilities Series March 1; Emerging Leaders Series October 4; JPMorganChase Fellowship November to mid-January; Citi Early Identification November and February; Morgan Stanley Early Insights October 30; Moelis LDP October 22; Houlihan Lokey Insight Day October 19; Girls Who Invest October 15; MLT January 15; SEO Career mid-April. Link Sophomore Insights post and diversity fellowships post.)
4. Start cold emailing the summer before sophomore year, and expect 1 reply in 5 to 10. (M&I mechanics: 10 to 25 percent response, half take a call, 2 to 3 calls a week, 300 to 500 emails over six months; junior bankers answer more than MDs; Centerview asks you not to email multiple people.)
5. Build a one-page resume that reads in six seconds. (Link the two live resume posts; what goes in each line; the number from step 2.)
6. Learn the technicals and five STAR stories before portals open, not after. (Categories in order: accounting links, EV vs equity value, multiples and the three methods, DCF, then M&A and LBO; free resources BIWS, WSP, M&I, WSO, Peak Frameworks. Link 2026 interview guide for sophomores and 30 behavioral examples.)
7. Apply the day a portal opens, because the effective deadline is day one. (Evercore September 9 to November 15, 2026; Harris Williams October to January; bulge brackets December 2026 to January 2027, Morgan Stanley ran January 1 to February 15 last cycle; Adventis: 28 firms posted in December 2025, 47 in January 2026; HireVue within hours to a week; superday of 2 to 5 interviews at Goldman, 4 to 6 elsewhere; offers March to June; classes essentially full by May. Link 10 IB internships 2027 and the new timeline article once live.)
8. Treat the summer as a 10-week interview, because the return offer is the job. (9 to 10 weeks, June to August; return offers in the final week; no bank publishes a rate; full-time postings for non-returners September to October of senior year; link summer internship conversion post.)

Then: "The Class of 2029 calendar" (one table: month, what's due, step number). Conclusion: the next thing to do this month, by class year.

Images (4 to 5): Goldman applicants 2024 to 2025 and acceptance rate bars; Class of 2029 calendar (dated); top feeder schools by analyst count (College Transitions); the networking funnel (300 emails to calls to referrals); the interview sequence (application, HireVue, first round, superday) with typical gaps.

Word target: 5,000 to 5,500. VERIFY tags on every program deadline and pay figure.

---

## Article 2: Investment Banking Recruiting Timeline 2027: When Everything Actually Happens

- **Slug:** `investment-banking-recruiting-timeline-2027`
- **Format:** ultimate-guide (plain descriptive headers by period)
- **Target keyword:** investment banking recruiting timeline
- **Secondary:** investment banking recruiting timeline 2027, Summer 2028 investment banking internship, Investment Banking Summer Analyst 2028, IB recruiting 2027
- **Reader:** a sophomore in October 2026 (Class of 2029) who needs every date for the next 22 months
- **Glossary check:** application year 2027 (first wave fall 2026), internship Summer 2028, graduation 2029. Eligibility language: "graduating December 2028 to June 2029."

Intro: "If you're applying to Investment Banking Summer Analyst programs in 2027, you're competing for Summer 2028 seats, and the first applications opened in September 2026." Bold: "**Evercore opened its Summer 2028 application on September 9, 2026 and closes it on November 15, about four months earlier than its last two cycles.**" Line: bulge brackets expected December 2026 to January 2027; interviews and offers January to May 2027; middle market rolling through fall 2027. Last: "In this article, I lay out the whole cycle month by month, from sophomore programs this fall to the full-time offer in August 2028."

Sub-questions:
- When do investment banking summer analyst applications open for 2027? (Elite boutiques September to November 2026; bulge brackets December 2026 to January 2027; middle market January through fall 2027. Most are rolling.)
- Is it too late to apply for a Summer 2028 investment banking internship? (No for bulge brackets and the middle market; Evercore closes November 15; sophomore programs mostly close in October and November.)

Body (period headers):
1. The whole cycle on one page (table: period, what happens, who; from fall 2026 through fall 2028).
2. Fall 2026: sophomore and insight programs are the first deadlines (dated list; what they feed into; Prospect Rock: participants routinely get accelerated interviews, no published share).
3. September to November 2026: elite boutiques open first (Evercore, Harris Williams, PWP, Moelis Houston open now; PJT, Centerview, Lazard, Houlihan Lokey expected November to January per trackers, with the conflicts flagged; Evercore's process: two 30-minute live interviews, no HireVue, offers within days of superdays).
4. December 2026 to January 2027: bulge brackets open and the clock starts the day they post (Summer 2027 evidence table: Morgan Stanley January 1 to February 15, 2026; RBC deadline January 30; BofA rolling and "close as positions are filled"; Citi, Barclays, UBS, DB, Wells December to January; Goldman IB posting by January 1; JPMorgan conflict December to March; Adventis: 28 firms December, 47 January, 350 postings in January; 2028 forecast peaks at 349 applications in January 2027).
5. January to April 2027: HireVue in days, first rounds in weeks, superdays by spring (Goldman invite about a week after applying, a week to complete; JPMorgan within hours, 7 days; Morgan Stanley due two days after the deadline; superdays of 2 to 5 interviews at Goldman, 4 to 6 typical; offers March to June; bulge-bracket classes essentially full by May 2026).
6. Spring to fall 2027: the middle market and the second waves (Baird opens late December for two weeks with superdays in late February; Piper Sandler January to February; William Blair, Raymond James, Lincoln rolling; Deutsche Bank's fall wave August to September 2026 for 2027 seats; Goldman's firm-wide application August 15 for remaining seats; London's August to November windows as the contrast).
7. Summer 2028: the internship and the return offer (9 to 10 weeks, June to August; return offers in the final week or early fall; no published rates).
8. August 2028 to January 2029: full-time recruiting and the private equity on-cycle (full-time postings September to October, interviews October to December; PE on-cycle restarted January 5, 2026 after the 2025 pause: JPMorgan's June 4, 2025 memo, Apollo and General Atlantic pausing Class of 2027 interviews, Goldman's quarterly attestation; what that means for a 2028 intern).

Conclusion: what to do this week, dated October 2026 (Evercore by November 15, Morgan Stanley Early Insights by October 30, Moelis LDP October 22, Houlihan Lokey October 19, Citi Early Identification October 23, JPMorganChase Fellowship when it opens in November, then bulge brackets on day one in December and January).

Images (5): the full cycle on one timeline (dated, regenerate at publish); Summer 2027 opening and closing months by firm (table); firms posting by month, Summer 2027 actual and Summer 2028 forecast (bars, Adventis); from application to offer at a bulge bracket (sequence with typical gaps); fall 2026 program deadlines (table, dated).

Word target: 5,000 to 6,000. Every date VERIFY-tagged; conflicts stated as ranges, never resolved by guessing.

---

## Article 3: Credit Analyst Interview Questions: 20 to Prepare For

- **Slug:** `credit-analyst-interview-questions-20`
- **Format:** listicle (question-listicle; exact count 20)
- **Target keyword:** credit analyst interview questions
- **Secondary:** credit interview questions, private credit interview questions, leveraged finance interview questions, rating agency interview questions, commercial banking credit analyst interview
- **Reader:** a junior or senior interviewing for a credit seat at a bank, a rating agency, a leveraged finance group, or a private credit fund
- **Differentiation:** the two live private credit posts are private-credit-only and fit-heavy. This one groups by seat and walks the machinery with one worked number per mechanism.

Intro: "Credit analyst interview questions test one thing: whether you can tell if a borrower will pay the money back, and what the lender gets if it doesn't." Bold: "**US leveraged loans outstanding hit a record $1.55 trillion at the end of 2025, and the banks, rating agencies and private credit funds that hold them all hire credit analysts.**" Line: the four seats and how the questions shift. Last: "Here are the 20 questions that come up across all four, with the answer the interviewer wants."

Sub-questions:
- What does a credit analyst actually do? (Underwrites: decides whether a company can repay, structures the loan, monitors it; by seat.)
- How technical is a credit analyst interview? (Bank: fit plus ratios; rating agency: scale and methodology; LevFin: IB-level accounting and valuation; private credit: a 3-statement or LBO-style case, 90 minutes to 3 to 4 hours.)

The 20 (grouped under plain H2s; each item: question as the H3, bolded lead claim on what it tests, plain walk-through with one worked example, bolded takeaway):

Questions every credit seat asks
1. Walk me through how you'd decide whether to lend $10 million to a company. (Five Cs, SFNet definition.)
2. Which metrics tell you a company can carry its debt? (Leverage, interest coverage, DSCR, FCCR, liquidity, with typical bank minimums.)
3. How do you get from EBITDA to the cash that actually pays the loan? (EBITDA, less cash interest, cash taxes, capex, change in working capital; one worked table.)
4. What is EBITDA, and what's wrong with using it for debt capacity? (Add-backs, capex-heavy businesses; link EBITDA post.)
5. What's the difference between a maintenance covenant and an incurrence covenant? (LCD definitions; cov-lite meaning.)
6. A borrower has $100 of EBITDA and $500 of debt at 6 percent; covenants are 6.0x maximum leverage and 2.0x minimum coverage. How much cushion is there? (Worked: leverage 5.0x, EBITDA can fall to $83.3 before a breach, a 16.7 percent cushion; interest $30, coverage 3.3x, EBITDA can fall to $60; leverage binds first.)
7. Who gets paid first if the company goes bankrupt? (Revolver and term loans, second lien, senior unsecured, subordinated, preferred, common; Moody's recoveries: first-lien loans 65 percent, senior unsecured 38 percent.)

Bank credit analyst questions
8. What is DSCR and what minimum do banks want? (1.25x; SBA's floor to 1.25x effective October 1, 2026.)
9. What's a borrowing base, and how do advance rates work? (OCC: 70 to 85 percent of eligible receivables, up to 65 percent of inventory; worked example.)
10. What's in a credit memo, and what do the risk ratings mean? (Pass, special mention, substandard, doubtful, loss, FDIC wording; expected loss = PD x LGD x EAD.)
11. Why commercial banking rather than investment banking? (Say/don't inside the answer.)

Rating agency questions
12. Walk me through the rating scale and where investment grade ends. (Moody's and S&P scales, Baa3/BBB-, the agencies' own definitions; S&P 50 percent, Moody's 32 percent, Fitch 12 percent of ratings.)
13. What's the difference between an outlook and a watch? (S&P: six months to two years vs one-in-two within 90 days; Moody's wording.)
14. Why would an agency downgrade a company that still makes money? (Warner Bros. Discovery 2025: Fitch BBB- to BB+, Moody's Baa3 to Ba1, with their stated reasons and the RR4/RR5 notching; Adecco at 2.0x leverage.)

Leveraged finance questions
15. What's the difference between a leveraged loan and a high-yield bond? (Floating vs fixed, secured vs unsecured, amortization, six-month soft call vs non-call periods, maintenance vs incurrence.)
16. How is a term loan B priced, and what do a floor and an OID do to the yield? (SOFR+250, a 3 percent floor, 99 OID = 100 bps; TLA vs TLB; second lien about 200 bps more.)
17. A sponsor wants 7x debt to EBITDA instead of 5x. How do you evaluate it? (KBRA: 5.5x large-cap, 4.75x core middle market; coverage at each level; the 2013 guidance's 6.0x reference and its December 2025 rescission.)

Private credit questions
18. What's the difference between private credit and broadly syndicated loans, and why did it grow? (Private credit financed 84 percent of 2025 LBOs by count; Moody's expects AUM above $2 trillion in 2026; unitranche at SOFR+450 to 500; 77 percent of core middle market loans keep maintenance covenants vs 38 percent of jumbo loans.)
19. What's a unitranche, and how does PIK interest work? (First-out and last-out; PIK adds to principal; worked line.)
20. Build a downside case: if EBITDA falls 30 percent, does this loan still get repaid? (Worked table; FCCR; Fitch private credit default rate 6.3 percent through August 2026; first-lien ultimate recovery 71 percent.)

Then: "Questions not on this list" (brain teasers, current SOFR and Treasury levels, yield to worst, workout vs restructuring; link restructuring questions post). Say this, don't say that (five). Conclusion: where to start by seat.

Images (5 to 6): capital structure and recovery rates (diagram); the rating scales side by side with the investment-grade line (table); the covenant cushion worked example (table); loan vs bond (table); the downside case (table); default rates by market, July 2026 (bars).

Word target: 5,500 to 6,500; say why in the report if over 6,000.

---

## Article 4: The STAR Method for Finance Interviews: Examples That Actually Land

- **Slug:** `star-method-finance-interviews`
- **Format:** ultimate-guide (how-to-answer; say/don't block required)
- **Target keyword:** STAR method
- **Secondary:** STAR method interview examples, STAR method finance interview, behavioral interview questions finance, STAR method investment banking
- **Reader:** a student with a HireVue or first round in the next two weeks who has heard "use STAR" and needs to see it done

Intro: "The STAR method is a four-part structure for answering behavioral interview questions: Situation, Task, Action, Result." Bold: "**Deloitte, PwC and Bank of America tell campus candidates to use it by name, and JPMorgan's own interview handbook teaches the same shape under different letters.**" Line: in a HireVue you get about 30 seconds to think and two minutes to talk, so the structure has to be automatic. Last: "In this article, I lay out what each part does, how to split the time, eight worked answers to the questions banks ask most, and the fixes for the mistakes career offices see every cycle."

Sub-questions:
- What does STAR stand for in an interview? (Letters, DDI's claim to have introduced it in the 1970s, the common variants.)
- How long should a STAR answer be? (60 to 120 seconds; about 150 to 190 words at 90 seconds; MIT's split: Situation 20 percent, Task 10, Action 60, Result 10.)

Body:
1. Why banks score behavioral answers against a rubric (Sackett 2022: structured interviews 0.42 vs unstructured 0.19; Schmidt and Hunter 1998: 0.51 vs 0.38; Bain gives every candidate the same questions and scores objectively; the published values and competencies: Goldman's four, JPMorgan's five, Morgan Stanley's five, BofA's seven.)
2. The four parts, with the time split and the "I" rule.
3. Five stories cover almost every question (story bank: team, failure, conflict, leadership, analysis; the 18 real questions mapped to them.)
4. Eight worked answers (each: the question, the full 90-second answer as sample text, two sentences on why it works): failed; teammate not pulling weight; led; tight deadline; data to a recommendation; influenced without authority; difficult feedback; learned quickly. Settings: a student fund pitch team, a CFA Research Challenge team, a part-time job, a club event, a class project, a campus job. Sample text follows body-copy rules.
5. STAR in a recorded HireVue (30-second prep bullets; Goldman's two-minute cutoff; one attempt at Goldman, one retake at JPMorgan; link GS HireVue post and the new HireVue article once live.)
6. The mistakes career offices see most (Situation too long; no number in the Result; "we"; memorized script; negative about a teammate; Deloitte: "not to make stories up.")
7. Say this, don't say that (five).
Conclusion: write five stories this week, time each at 90 seconds, record on a phone.

Images (4 to 5): the time split (bars, 20/10/60/10); interview validity, structured vs unstructured (bars, Sackett 2022 and Schmidt and Hunter 1998); the story bank matrix (table: five stories by question type); one worked answer marked up by part with word counts (annotated text graphic); the HireVue clock (30 seconds prep, 120 seconds answer).

Word target: 5,000 to 5,500.

---

## Article 5: HireVue for Finance: How to Prepare for a Recorded Interview

- **Slug:** `hirevue-for-finance-recorded-interview`
- **Format:** ultimate-guide (how-to-prepare; say/don't block required)
- **Target keyword:** HireVue
- **Secondary:** HireVue interview, HireVue questions finance, recorded video interview banking, one-way video interview, HireVue investment banking
- **Reader:** a student holding a HireVue invitation from any bank, with two to seven days to complete it
- **Differentiation:** the live Goldman post lists Goldman's questions. This one covers the format across firms: who uses it, what happens on screen, who watches, what they ask, and the prep plan.

Intro: "HireVue is the recorded, one-way video interview most large banks use as the first round for Summer Analyst and full-time campus hiring." Bold: "**Goldman Sachs has used it for every first-round campus interview since July 2016, and about one in three of its summer analyst applicants got one in 2019.**" Line: a typical bank HireVue is three to six questions, 30 seconds to prepare, about two minutes to answer, and a deadline of two to seven days. Last: "In this article, I lay out which firms use it, what happens on screen, who watches the video, what they ask, and how to prepare in the week you have."

Sub-questions:
- Is HireVue scored by AI? (At the banks, people watch; Goldman says trained human recruiters and colleagues review; HireVue dropped facial analysis in 2020; its AI scoring, where an employer buys it, works on the transcript.)
- Can you redo a HireVue question? (The employer sets attempts and the screen shows them before you start; Goldman has usually been one take, JPMorgan one retake; once submitted you can't go back; HireVue can't reset or extend.)

Body:
1. Which banks use HireVue and which interview live (table: Goldman, JPMorgan on primary sources; Morgan Stanley, BofA, Citi, UBS, Wells Fargo, RBC per prep guides; Barclays' official page lists no video step; Deutsche Bank unnamed video; Evercore, Moelis, PJT live only; Lazard recorded mainly in the UK; BlackRock recorded pre-interview assessment; Citadel live; McKinsey Solve.)
2. What happens on screen, step by step (HireVue help center: requirements page, question count and length shown, equipment check, three practice questions never submitted, the attempts screen, prep countdown, three-second countdown, answer countdown, "Done Answering," no pause, dropped-connection resume, employer deadline.)
3. Who watches the video and what they score (Goldman's statement; Bank of America's two or three bankers per candidate as reported; HireVue's reviewer tools; the 2020 end of facial analysis; Illinois and New York City notice rights in two sentences.)
4. The questions banks ask (why this firm and division; behavioral; a recent news item that affects the division, reported at JPMorgan, Citi, Bank of America and Morgan Stanley; situational; occasional three-statement or DCF; link Goldman HireVue post, STAR article, 30 behavioral examples, DCF post.)
5. The 30 seconds and the two minutes (bullets in the prep window; 150 words; Goldman's hard cutoff; "Done Answering" early; one attempt.)
6. Setup that reads well on a recruiter's screen (light in front, camera top-center at eye level, look at the lens, quiet room, Chrome, no Chromebook, phone app, dress, notes nearby but not read.)
7. A one-week plan from the invitation (timing by firm: Goldman about a week after applying and about a week to complete; JPMorgan within hours and 7 days; Morgan Stanley 48 to 72 hours; Citi and BofA about 48 hours; day-by-day plan.)
8. Say this, don't say that (five, for the common prompts.)
FAQ (three short questions: more time, phone, internet drop). Conclusion.

Images (4 to 5): which firms use HireVue (table); the on-screen sequence (diagram: prep, countdown, answer, submit); from application to superday with typical gaps at Goldman and JPMorgan (timeline); HireVue interviews conducted, 2021 to 2026 (bars: 24 million by October 2021, 70 million-plus by 2026); the setup (diagram: light, camera, eye line).

Word target: 5,000 to 5,500.

---

## Internal links available (live, October 11, 2026)

All under `https://www.wallstreetguide.net/post/`:

how-hard-is-it-to-get-into-investment-banking-6-things-that-actually-matter; how-to-get-into-investment-banking-with-no-experience-9-steps-that-work; investment-banking-preparation-the-freshman-to-junior-roadmap; top-10-sophomore-insights-programs-for-ib; 10-investment-banking-internships-to-apply-to-in-2027; investment-banking-resume-the-one-page-template-that-gets-interviews; investment-banking-internship-cv-8-things-every-strong-application-includes; the-2026-investment-banking-interview-guide-for-sophomores; 30-examples-investment-banking-behavioral-interview-questions; top-15-goldman-sachs-hirevue-questions-and-how-to-answer-them; goldman-sachs-summer-analyst-interview-a-round-by-round-breakdown; goldman-sachs-superday-what-to-expect-and-12-questions-you-will-be-asked; jp-morgan-superday-tips-for-2026; investment-banking-summer-internship-what-is-it-and-how-to-convert-to-full-time; top-10-free-resources-for-investment-banking-interview-questions-in-2026; walk-me-through-a-dcf-the-7-step-answer-that-works; walk-me-through-an-lbo-the-6-step-answer-interviewers-want-to-hear; 20-private-credit-interview-questions; 20-examples-of-private-credit-interview-questions; private-credit-how-to-break-into-it-as-an-undergrad; direct-lending-careers-what-undergraduates-need-to-know; top-10-private-credit-firms-for-undergraduates; restructuring-interview-questions-20-you-must-know; 50-accounting-interview-questions-that-you-should-practice-before-your-interview; ebitda-explained-for-finance-interviews-what-they-actually-want-to-hear; 10-deal-discussion-questions-you-will-face-in-ib-interviews-and-how-to-answer-them; how-to-ace-the-mckinsey-personal-experience-interview; consulting-recruiting-timeline-for-undergrads-in-2026; 2026-guide-to-diversity-finance-fellowships-and-deadlines; private-equity-interview-questions-25-for-undergrad-candidates; the-ultimate-guide-to-landing-a-private-equity-internship-as-an-undergrad; top-10-investment-banks-what-makes-each-one-different-and-who-should-actually-target-them; top-middle-market-investment-banks-10-firms-for-2027.

Cross-links between the five (add once live): 1 to 2, 4, 5; 2 to 1, 5; 4 to 5; 5 to 4; 3 to none required.
