# Batch brief: 5 consulting articles (October 11, 2026)

Repo root: `/home/claude/repo` (a copy of `Downloads/wsg-content-main v2/wsg-content-main`). Today is Sunday, October 11, 2026. Run every command from the repo root.

## Founder decisions taken before drafting (October 11)

- **Headlines are used exactly as given.** the founder chose to keep all five, including "McKinsey Hours: The Honest Read" and "Consulting Fit Interview: The Stories You Need Ready". Don't rename them. (The May 2026 rule about dropping "The honest read:" as a *sub-header* still applies inside the body: don't use "The honest read" as an H2 or H3, and don't close with a recap section.)
- **Two are v2 rewrites** of September 8 drafts that predate the October 7/8 rules: `drafts/draft-mckinsey-hours-honest-read-v1.md` and `drafts/draft-consulting-day-in-the-life-mbb-analysts-v1.md`. The v1 files are **fact sources only, never voice samples.** They open with a Stephen Turban bio and first-person McKinsey memories, both now banned. The v2 keeps and re-verifies the facts, drops every "I was at McKinsey" line, every "my alarm," every composite student, and rewrites the whole article under the October 8 rules at the new length target. Write the v2 to `drafts/draft-{slug}-v2.md`. Leave v1 untouched.
- **Three are fresh writes** (fit interview, MBB salary, Accenture). An August 27 session drafted short versions of the MBB salary and Accenture pieces, but those files were never saved anywhere; only their verified facts survive in `claude/batch-log-aug-27-2026.md`. Reuse those facts after re-checking them.
- **MBB Salary** is a three-firm side-by-side and links the live WSG McKinsey salary post for McKinsey depth.
- Outline approval skipped; draft straight through.
- Live-post list for internal links: `claude/wsg-live-urls-oct-11-2026.txt` (102 posts, sitemap fetched October 11, 2026). Link only to posts in that list. Drafts in `drafts/` and files in `published/ai-written/` are not live and can't be linked; mention them under "Cross-links to add once live" in your report instead.

## Rules every draft follows (read the files; this is only the index)

Read, in this order, before writing a word: `.claude-skill/SKILL.md` (October 8 and October 7 rules at the top, hard rules, VERIFY protocol), `.claude-skill/source-verification.md`, `.claude-skill/reference-articles.md`, `.claude-skill/intros.md`, `.claude-skill/plain-language.md`, `.claude-skill/thorough-explanations.md`, `.claude-skill/prose-editing.md`, `.claude-skill/consulting.md`, `consulting/voice-cues.md`, `consulting/recruiting-timeline.md`, `style-guide/style-guide.md`, the template for your format in `templates/`, and the firm-profile file named in your brief below.

The short version of what shipped wrong before and must not ship again:

1. **Opening** (intros.md): sentence one says what the topic is or answers the headline, with the target keyword. A bolded full sentence with a concrete fact follows. Last sentence says what the article covers. Two to five sentences. No scene, no story, no "most candidates...," no bio, no credentials, no `byline:` in the frontmatter.
2. **Voice:** "you" for the reader, "we" for WSG, light "I" only as framing ("In this article, I lay out..."). No first-person memories, no "when I was at McKinsey," no composite students with names or letters, no "a student I mentored."
3. **Headers:** plain and literal. Question headers are the reader's exact search question and the first sentence under them answers it. Numbered insight headings are short plain claims under 12 words. No clever second halves, no metaphors.
4. **Bolds:** full sentences with a fact or a clear rule, at least one per H2 section, and reading only the bolds tells the argument.
5. **No unsupported opinions** about what readers get wrong. No negatives about the writer, WSG, the article or the reader.
6. **No em dashes, en dashes or spaced hyphens anywhere.** Commas, periods, colons.
7. **Length:** niche about 4,500 to 5,500 words, ultimate guide about 5,000 to 6,000 (about 20 to 25 pages before images). Write to the range from the first draft. Explain every mechanism once, fully, then move on. Never close with a recap section.
8. **Every section carries a specific** (a named firm, a real number, a named program). Tag every moving number with `[VERIFY: ...]`. Never tag an entity's existence; verify it or remove it.
9. **Contractions. Say-it-out-loud test on every sentence and header.** Four or five say/don't callouts at the end of any article that teaches an answer.
10. **Links:** inline anchor-word links only, evergreen pages only (firm careers landing pages, the live WSG posts, named sources). No rotating job-posting URLs. Run `python3 scripts/check_links.py drafts/{file}.md` before you report.
11. **Gates:** `python3 scripts/check_article.py drafts/{file}.md` and `python3 scripts/check_style.py drafts/{file}.md` must pass. Also run the mechanical spot checks at the end of `prose-editing.md`.

## Frontmatter for every draft

```
---
headline: {exact headline}
target_keyword: {keyword}
secondary_keywords: [{kw1}, {kw2}, ...]
format: {ultimate-guide | niche}
sub_type: {firm-or-role for niche}
word_count_target: {range}
status: draft-v1 (or draft-v2)
---

# {Headline}

**Meta description:** {topic first, what the article covers, 150 to 160 characters, no person named}.
```

## Research standards for this batch

- Primary sources first: mckinsey.com, careers.bcg.com, bain.com, accenture.com careers pages. Then Management Consulted, Hacking the Case Interview, StrategyCase, PrepLounge, IGotAnOffer, CaseCoach, Leland. Then press (Fortune, Bloomberg, WSJ, Business Insider, Boston Globe). Reddit and Glassdoor only as a cross-check, never as the cited source for a number.
- Every tracker number gets the tracker's name and the month in the VERIFY tag. Trackers disagree on pay; say so in the article and give the range.
- Record every source you used (URL, what it supported, date retrieved) in your report so the QA agent can re-check it.

## Report format (return this as your final message, under 700 words)

1. Outline as built (headline, meta, intro's first sentence and bolded fact, the H2s in order).
2. Word count, VERIFY count, link count, check_article / check_style / check_links results.
3. Thoroughness Report (format in `thorough-explanations.md`).
4. Delivery summary (format in `source-verification.md`).
5. Facts verified, with sources (URL + what it supports), including anything that contradicted the brief or the v1 draft.
6. Cross-links to add once live (drafts in the repo that this article should link to or from).
7. Image ideas: 4 to 6 candidates, each with the exact draft line it should follow (first 60 characters), what it shows, and where the numbers come from.
8. Anything still thin or needing the founder's call.

---

## Article 1: Consulting Fit Interview: The Stories You Need Ready

- **Slug:** `consulting-fit-interview-stories-you-need-ready` → `drafts/draft-consulting-fit-interview-stories-you-need-ready-v1.md`
- **Format:** ultimate-guide (insight-led, numbered story headings as short plain claims). Target about 5,000 to 6,000 words.
- **Target keyword:** `consulting fit interview`. Secondary: consulting fit interview questions, consulting behavioral interview, McKinsey PEI stories, Bain experience interview, BCG behavioral interview, fit interview stories.
- **Target reader:** a junior with a first-round MBB or tier 2 interview in the next four to eight weeks who has done case prep and realizes the fit half is unprepared.
- **Firm-profile file:** `consulting/firm-profiles/mbb.md`. Also skim `consulting/firm-profiles/tier-2-strategy.md` for how fit runs at Oliver Wyman, Kearney and L.E.K.
- **Related live WSG posts to link:** `how-to-ace-the-mckinsey-personal-experience-interview` (the McKinsey PEI deep dive; this article covers all firms and the story bank, and points there for PEI detail), `why-consulting-how-to-answer-it-in-under-90-seconds`, `how-to-prepare-for-a-consulting-interview`, `what-is-a-case-interview-the-complete-undergrad-guide`.
- **Related drafts, not live (mention, don't link):** `drafts/draft-20-consulting-behavioral-interview-questions-v1.md` (October 1; a question list with sample answers; this article is the story bank, so it must not duplicate that list). Read its H2s so you don't repeat it.
- **Angle:** the fit interview tests a handful of things, and every firm's version draws on the same five or six stories. The article names the stories, says what each firm is testing with it, shows how to build each one so it survives ten minutes of follow-up questions, and maps the stories to the firms' dimensions.
- **Must verify from firm pages:** McKinsey's current PEI dimensions (the firm's careers interview page lists them; the historical three were personal impact, entrepreneurial drive and inclusive leadership, and the firm added or renamed dimensions in 2023 to 2025, so check the live page and tag it), how long the PEI runs and that it's one story per interview, how BCG runs behavioral questions (10 to 15 minutes inside the case round, the "BCG behavioral interview" framing on careers.bcg.com), and Bain's experience interview. Give the format of each in one table.
- **Suggested shape** (adjust to the facts):
  - Intro per intros.md: what a consulting fit interview is and where it sits; bolded fact (for example how much of a McKinsey round the PEI takes, verified); one line of facts; what the article covers.
  - H2 sub-questions: "What is a consulting fit interview?" "How many stories do I need for consulting interviews?" (answer with a number: five or six, and why).
  - How each firm runs the fit interview (McKinsey PEI, BCG, Bain, tier 2), with a table.
  - What interviewers are scoring (the dimensions, in plain words, with the firm's own language quoted where you can).
  - The stories, one numbered H2 each with a short plain claim heading, around 500 to 650 words each: leadership, influence or changing someone's mind, failure or setback, conflict inside a team, initiative or building something from nothing, a hard analytical problem you solved. For each: what it's testing, what a strong one has, a worked skeleton (third person, no composite names; "say your story is about a club budget" framing is fine), the follow-up questions a PEI interviewer asks ("what were you thinking at that moment," "what did they say back"), and what disqualifies it.
  - How to build a story so it survives drill-down: the structure (short setup, your role, actions in detail, result, what you'd do differently), the 70/30 split toward actions, "I" not "we," numbers in the result, a one-page story grid.
  - The story grid: one table mapping the six stories to the firm dimensions, so the reader sees which story covers which firm.
  - Say this / don't say that: four or five.
  - Conclusion: the next step (write the grid this week, run each story against a drill-down partner).

## Article 2: MBB Salary Breakdown 2026

- **Slug:** `mbb-salary-breakdown-2026` → `drafts/draft-mbb-salary-breakdown-2026-v1.md`
- **Format:** niche (role / comp). Target about 4,500 to 5,500 words.
- **Target keyword:** `mbb salary`. Secondary: McKinsey salary, BCG salary, Bain salary, MBB compensation, consulting salary undergrad, McKinsey Business Analyst salary, BCG Associate salary, Bain Associate Consultant salary.
- **Target reader:** a sophomore or junior deciding between consulting and banking, or holding an MBB offer and trying to read the offer letter.
- **Firm-profile file:** `consulting/firm-profiles/mbb.md`.
- **Related live WSG posts to link:** `mckinsey-salary-2026-business-analyst-associate-partner-pay-explained` (link it in the McKinsey section as the deeper dive), `mckinsey-business-analyst-role-salary-how-to-get-in`, `private-credit-salary-2026-full-breakdown` (only if a comparison section needs it), `top-10-consulting-exit-opportunities`, `the-ultimate-guide-on-how-to-break-into-mbb`.
- **Related drafts, not live:** `drafts/draft-investment-banking-analyst-salary-2027-v1.md` (October 5; use its take-home method as a model for the worked example, and mention it as a cross-link), `drafts/draft-mckinsey-associate-role-salary-career-path-v1.md`.
- **Facts from August 27 (re-check every one):** Hacking the Case Interview: base McKinsey $112K / BCG $110K / Bain $112K, performance bonus up to $18K / $22K / $23K, signing $5K, total about $137K to $140K; retirement McKinsey about 7.5% of salary, BCG about $11,875 lump, Bain about 4.5%. StrategyCase: all bases $110K, target bonus $30K, signing $10K to $15K, year one $155K to $165K. Post-MBA: about $190K to $192K base, $30K signing, totals about $267K to $285K. managementconsulted.com/consulting-salaries/ returned 403 to fetch in August; try again and cite only if it loads.
- **Must verify now:** the 2026 undergrad numbers at each firm from at least two trackers (Management Consulted 2026 report, Hacking the Case Interview, StrategyCase, PrepLounge), the post-MBA numbers, the ladder (McKinsey BA → Associate → Engagement Manager → Associate Partner → Partner; BCG Associate → Consultant → Project Leader → Principal → Partner; Bain AC → Senior AC → Consultant → Manager → Principal → Partner) with pay bands where a tracker publishes them, performance bonus mechanics (percent of base, tiers), retirement contribution, relocation, MBA sponsorship terms where public, and whether any firm published a 2026 raise.
- **Suggested shape:**
  - Intro: what MBB salary is and the undergrad base; bolded year-one total cash; what the article covers.
  - H2 sub-questions: "How much do MBB consultants make out of undergrad?" "Which of McKinsey, BCG and Bain pays the most?" (answer: within a few thousand of each other; the differences are in bonus and retirement).
  - How MBB pay is structured: base, performance bonus (how it's set and paid), signing bonus, relocation, retirement contribution, benefits. Explain each piece in plain words.
  - Undergrad pay at the three firms, side by side (table), with the trackers' disagreements stated.
  - The ladder: pay by level at each firm, with the years it takes and where the big jumps are (post-MBA, Engagement Manager / Project Leader / Manager, Partner).
  - Post-MBA and how MBA sponsorship works.
  - MBB vs investment banking in year one and year three (one table; say the per-hour version in a sentence).
  - MBB vs tier 2 and Big 4 strategy (short).
  - What you take home: one worked example for a New York first year (base plus bonus, federal, state and city tax, 401(k), monthly figure). Show the arithmetic step by step. Keep brackets tagged.
  - What the offer letter leaves out (bonus timing, clawbacks on signing bonuses, when the first raise lands, hours).
  - Conclusion: next step.

## Article 3: Consulting Day in the Life: What MBB Analysts Actually Do (v2 rewrite)

- **Slug:** `consulting-day-in-the-life-mbb-analysts` → `drafts/draft-consulting-day-in-the-life-mbb-analysts-v2.md`
- **Format:** niche (role). Target about 4,500 to 5,500 words.
- **Target keyword:** `consulting day in the life`. Secondary: McKinsey Business Analyst day in the life, what do consultants do all day, MBB analyst daily schedule, day in the life of a management consultant.
- **Target reader:** a sophomore deciding whether to recruit for consulting who wants to know what the job is hour by hour.
- **Firm-profile file:** `consulting/firm-profiles/mbb.md`.
- **Fact source:** `drafts/draft-consulting-day-in-the-life-mbb-analysts-v1.md` (September 8). Keep the facts, re-verify the ones that can move, and rewrite everything in WSG voice. The study structure, the Monday-to-Friday shape, the problem-solving session, the ghost deck, the pyramid principle, the so-what title, the time split, the Lilli changes and the intern version all stay as content. The hotel-lobby scene, "my alarm," "on my studies," the composite student H and every "I" memory go.
- **Related live WSG posts to link:** `mckinsey-business-analyst-role-salary-how-to-get-in`, `the-ultimate-guide-on-how-to-break-into-mbb`, `how-to-get-into-consulting-as-an-undergrad-the-full-roadmap`, `top-10-consulting-exit-opportunities`, `consulting-recruiting-timeline-for-undergrads-in-2026`.
- **Related drafts, not live:** `drafts/draft-mckinsey-hours-honest-read-v2.md` (being written in this batch; cross-link once live).
- **Must verify now:** the McKinsey Business Analyst posting language (team size, "present results to client management," travel), the Leland day-in-the-life piece (2026), the Hacking the Case Interview time-split estimate, the mckinsey.com careers blog summer BA post, BCG and Bain role titles, Lilli adoption and the January 2026 interview exercise (Fortune), headcount (Fortune May 2025, Bloomberg December 2025), internship lengths. Add anything new from 2026 (hybrid travel norms, AI in the day).
- **Suggested shape:** intro per intros.md (what a day in the life of an MBB analyst is, in one sentence; bolded time-split fact; what the article covers); H2 sub-questions ("What does a McKinsey Business Analyst do all day?" "Is a BCG Associate's day different from a McKinsey Business Analyst's?"); then numbered plain-claim sections: what a study is and your slice of it; Monday; Tuesday and Wednesday; Thursday; Friday; how the week splits; what changed in 2026; the intern version; four or five say/don't callouts; conclusion with a next step. Third person throughout: "a Business Analyst," "the team," "you."

## Article 4: Accenture Strategy Analyst Career Guide

- **Slug:** `accenture-strategy-analyst-career-guide` → `drafts/draft-accenture-strategy-analyst-career-guide-v1.md`
- **Format:** niche (firm-or-role). Target about 4,500 to 5,500 words.
- **Target keyword:** `accenture strategy analyst`. Secondary: Accenture Strategy salary, Accenture Strategy Analyst Development Program, Accenture Strategy vs MBB, Accenture Strategy interview, Accenture Strategy careers.
- **Target reader:** a junior at a target or semi-target school who has Accenture Strategy on the list beside MBB and tier 2 and wants to know what the job is, what it pays, how to get in and how it compares.
- **Firm-profile file:** `consulting/firm-profiles/tier-2-strategy.md` (Accenture Strategy is listed as tier 2 strategy). Also `consulting/firm-profiles/big-4-strategy.md` for the comparison section.
- **Related live WSG posts to link:** `monitor-deloitte-careers-salaries-interviews-how-to-get-hired` (the closest sibling article; model the structure on it, link it in the comparison), `top-10-consulting-jobs-for-undergrads-in-2026`, `how-to-get-into-consulting-as-an-undergrad-the-full-roadmap`, `consulting-recruiting-timeline-for-undergrads-in-2026`, `what-is-a-case-interview-the-complete-undergrad-guide`.
- **Related drafts, not live:** `drafts/draft-deloitte-strategy-and-operations-career-guide-v1.md` (October 5; the sibling firm guide, read its H2s for shape), `drafts/draft-top-10-management-consulting-firms-2026-v1.md`.
- **Facts from August 27 (re-check):** "Strategy Analyst Development Program" (requisition NAELFY26) and "Technology Strategy & Advisory Analyst" were current North America entry postings. StrategyCase bands: Strategy Analyst about $90K base plus $8K target bonus, all-in about $105K to $115K; strategy premium 15 to 25 percent over the core consulting analyst track (about $77K base / $85K total); analyst to consultant in two to three years.
- **Must verify now:** how Accenture Strategy sits inside Accenture today (Strategy & Consulting as a service; the 2014 launch of Accenture Strategy and the 2020 reorganization into Strategy & Consulting; whether "Accenture Strategy" is still the practice name on accenture.com), the Strategy Analyst Development Program page on accenture.com (what it is, locations, start timing, whether it's the undergrad entry route into strategy), what analysts work on (capability areas: growth strategy, M&A, cost, technology strategy, sustainability, industry groups), pay from at least two trackers (Management Consulted, StrategyCase, Glassdoor or Levels.fyi as cross-checks), the ladder (Analyst → Consultant → Manager → Senior Manager → Managing Director) with bands, the recruiting process (application window for Summer 2027 interns and fall 2027 full-time, online assessment if any, the interview rounds, the case format), target schools, GPA signals, and the honest comparison with MBB (pay, hours, travel, project type, exits, MBA sponsorship).
- **Suggested shape:** intro per intros.md (what an Accenture Strategy Analyst is; bolded pay or premium fact; what the article covers); H2 sub-questions ("Is Accenture Strategy the same as MBB?" "How much does an Accenture Strategy Analyst make?"); where Strategy sits inside Accenture (one short section, no founding history); what the analyst actually does, with two or three named project types; the Strategy Analyst Development Program; pay by level with a table; the recruiting process step by step, with the case interview walked once; what Accenture looks for; Accenture Strategy vs MBB vs Big 4 strategy (one table plus a paragraph on each axis); exits; how to prepare, with a short timeline; four say/don't callouts; conclusion with a next step.

## Article 5: McKinsey Hours: The Honest Read (v2 rewrite)

- **Slug:** `mckinsey-hours-honest-read` → `drafts/draft-mckinsey-hours-honest-read-v2.md`
- **Format:** niche (role / lifestyle). Target about 4,500 to 5,500 words.
- **Target keyword:** `mckinsey hours`. Secondary: McKinsey work-life balance, consulting hours, MBB hours, McKinsey Business Analyst hours, consulting vs banking hours, McKinsey weekends.
- **Target reader:** a student with an MBB offer or interview deciding whether the hours are livable, and comparing against a banking offer.
- **Firm-profile file:** `consulting/firm-profiles/mbb.md`.
- **Fact source:** `drafts/draft-mckinsey-hours-honest-read-v1.md` (September 8). Keep the facts and the section logic (weekly shape, the three things that set hours, the beach, travel, weekends, pay per hour, 2026 changes, team norms). Drop the bio, every "my two years," "when I was at the firm," "I'd fly out," and the closing "The honest read, in one paragraph" recap section (closing recaps are banned). Don't use "The honest read" as a header anywhere in the body.
- **Related live WSG posts to link:** `mckinsey-business-analyst-role-salary-how-to-get-in`, `mckinsey-salary-2026-business-analyst-associate-partner-pay-explained`, `the-ultimate-guide-on-how-to-break-into-mbb`, `top-10-consulting-exit-opportunities`, `how-to-beat-mckinsey-solve-a-step-by-step-guide`.
- **Related drafts, not live:** the day-in-the-life v2 and the MBB salary v1 from this batch.
- **Must verify now:** Hacking the Case Interview hours page (May 2026 numbers), StrategyCase hours page (July 2026), PrepLounge coach ranges, McKinsey BA posting language on hours, Take Time (does the program still exist on the careers site and on what terms), the Kutcher memo (Boston Globe / Bloomberg October 2024), weekend frequency data, JPMorgan 80-hour cap (Fortune / WSJ September 2024), BA comp 2026, Goldman first-year IB pay, Fortune May 2025 headcount, Bloomberg December 2025 cuts, Business Insider January 2026 (25,000 agents), Fortune June 2025 (Lilli 75 percent), Fortune January 2026 (Lilli interview exercise), the McKinsey careers blog "team norms" post, Perlow's BCG study (HBR 2009, 64.5 to 57.7 hours), CaseCoach on hours monitoring. Add anything new from 2026 on McKinsey hours.
- **Suggested shape:** intro per intros.md (how many hours, in one sentence; bolded tracker fact; what the article covers); H2 sub-questions ("How many hours do McKinsey consultants work?" "Are McKinsey hours better than investment banking hours?"); numbered plain-claim sections on the weekly shape (with a day-by-day table), what sets your hours, the beach, travel, weekends, the pay-per-hour math walked step by step, what changed in 2026, team norms and how to raise them; four or five say/don't callouts; conclusion with a next step and no recap.

---

## Images (separate agents, after drafting)

Three to six per article in the banking format via `scripts/images/wsg_viz.py` and `scripts/images/wsg_diagrams.py`, every image with a `source`, every string through the plain-language and humanizer passes in `.claude-skill/images.md`. Build scripts at `scripts/images/build_{slug}.py`, PNGs and `manifest.json` at `published/assets/images/{slug}/`, inserted with `scripts/images/insert_images.py`. Mark dated images "regenerate at publish."
