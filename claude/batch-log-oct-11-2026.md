# Batch log: 5 consulting articles (October 11, 2026)

Repo: `Downloads/wsg-content-main v2/wsg-content-main` (worked on a copy at `/home/claude/repo` in the cloud workspace, then synced back). Brief: `claude/batch-brief-oct-11-2026.md`. QA brief: `claude/qa-brief-oct-11-2026.md`. Images brief: `claude/images-brief-oct-11-2026.md`. Live-post list for internal links: `claude/wsg-live-urls-oct-11-2026.txt` (102 posts, sitemap fetched October 11, 2026).

## Repeat check before drafting

Checked the live sitemap (102 posts), the local repo (`drafts/`, `published/ai-written/`) and the Claude Content project mirror for all five headlines.

| Headline | Live on WSG? | Already drafted? |
| --- | --- | --- |
| Consulting Fit Interview: The Stories You Need Ready | No. Adjacent live posts: McKinsey PEI guide, "Why Consulting?" | No |
| MBB Salary Breakdown 2026 | No, but "McKinsey Salary 2026: Business Analyst, Associate, Partner Pay Explained" is live | August 27 session drafted a 1,666-word version; the file was never saved anywhere |
| Consulting Day in the Life: What MBB Analysts Actually Do | No | September 8 v1 in the project mirror only (3,244 words, scene opening, Stephen bio) |
| Accenture Strategy Analyst Career Guide | No | August 27 session drafted a 1,735-word version; file never saved |
| McKinsey Hours: The Honest Read | No | September 8 v1 in the project mirror only (2,936 words, stat hook, Stephen bio, closing recap) |

## Founder decisions taken before drafting

- All five headlines kept exactly as given, including "McKinsey Hours: The Honest Read" and "Consulting Fit Interview: The Stories You Need Ready" (the October 8 simple-title rule would have trimmed both; the founder chose to keep them). Inside the body, "The honest read" is never a header and no article closes with a recap.
- The two September 8 drafts were rewritten in full as v2 under the October 7/8 rules (no bio, no narrative opening, no composite students, length target), keeping and re-verifying their facts. v1 files copied into `drafts/` for the record and left untouched.
- MBB Salary written as a three-firm side-by-side, linking the live McKinsey salary post.
- Outline approval skipped; outlines posted in chat as drafting started.
- Workflow: five drafting agents in parallel (research, verify, draft, passes, gates), then five independent QA agents (fresh eyes, primary sources reopened, arithmetic recomputed, surgical edits) in parallel with five image agents (built from the drafts, never editing them), then images inserted, .docx built, page counts checked.

## What shipped

All five pass `check_article.py` and `check_style.py`; zero em, en or minus dashes; zero invisible Unicode codepoints in drafts, manifests and .docx XML; no personal identifiers; `check_links.py` passes on every draft. .docx in `published/ai-written/` via `markdown_to_docx_v2.py`, images embedded, author and last-modified-by set to "Wall Street Guide".

| # | Headline | Format | Body words (no tags) | Pages before images | Pages with images | Images | VERIFY | Links |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Consulting Fit Interview: The Stories You Need Ready | ultimate-guide | 6,113 (5,637 without tables) | 22 | 26 | 5 | 34 | 7 |
| 2 | MBB Salary Breakdown 2026 | niche | 5,265 (4,572 without tables) | 21 | 24 | 6 | 85 | 11 |
| 3 | Consulting Day in the Life: What MBB Analysts Actually Do (v2) | niche | 4,745 | 18 | 23 | 6 | 39 | 15 |
| 4 | Accenture Strategy Analyst Career Guide | niche | 5,555 (5,181 without tables) | 22 | 25 | 5 | 56 | 19 |
| 5 | McKinsey Hours: The Honest Read (v2) | niche | 4,417 | 17 | 21 | 6 | 54 | 20 |

Page counts are LibreOffice renders of the built .docx (Letter, Arial 11, double spaced). Articles 3 and 5 land a little under the 20-page floor; SKILL.md allows shorter when the topic is covered, and neither QA agent padded.

## Openings (intros.md, October 8)

1. "A consulting fit interview is the part of a McKinsey, BCG or Bain interview where the interviewer asks about things you've done, and it sits in the same meeting as the case rather than in a separate round." Bold: PEI takes 10 to 20 minutes of a 45 to 60 minute interview, all on one story.
2. "MBB salary is what McKinsey, BCG and Bain pay their consultants, and for an undergraduate hire in the United States the 2026 base is $110,000 to $112,000..." Bold: year-one total cash about $130,000 to $140,000.
3. "A consulting day in the life at McKinsey, BCG or Bain is one slice of one client project: interviews and Excel during the day, slides at night, and a client meeting at the end of the week." Bold: HTCI June 2026 split, 28 / 22 / 15 percent.
4. "An Accenture Strategy Analyst is the entry-level consultant in Accenture's Strategy practice, hired out of undergrad through the Strategy Analyst Development Program." Bold: about $90,000 base, roughly $100,000 total cash, about a quarter below MBB.
5. "McKinsey hours come to about 55 to 65 a week for a consultant on a client project, and a first-year Business Analyst should plan on 60." Bold: HTCI May 2026, MBB average 55 to 65, peaks 70 to 80 or more.

## Thoroughness Reports (as delivered by the drafting agents, then QA)

**1. Fit interview.** Expanded 3 (the "two angles" mechanism in sub-question 2; the dimension-by-story arithmetic in the grid section; commercial due diligence glossed). Cut 4 echo sentences. Still thin 1: McKinsey's own theme labels load dynamically on mckinsey.com/careers/interviewing, so the four names (Leadership, Connection, Drive, Growth) rest on four trackers plus the live WSG PEI post. Plain-language rewrites 5 (PEI, Skills Interview, STAR, commercial due diligence, "rubric"). Over target? Marginally with tables; prose is about 5,600.

**2. MBB salary.** Expanded 4 (performance bonus tiers and attainment; 401(k) deposit vs match with dollar examples; the New York phase-in walked step by step; MBA sponsorship clawback and the two doors to post-MBA pay). Cut 2 (401(k) deferral variant held to one paragraph; tier 2 held to one table). Still thin 3 (see founder decisions). Plain-language rewrites 9. Over target? No.

**3. Day in the life (v2).** Expanded 6 (hypothesis-first walked with the plant-overtime example; data-request wording good vs bad; so-what title, ghost deck, pyramid, MECE each explained once; steering committee, backup page, pre-wire defined; staffing explained; which two tasks AI compresses). Cut 4 (hotel-lobby scene, every "I" memory, composite student H, the closing recap bold; the unsupported first-year-banker comparison). Still thin 2 (sophomore-to-junior conversion rate removed as unsourced; staffing manager title varies by office). Plain-language rewrites 11. Over target? No.

**4. Accenture.** Expanded 3 (the full case walk with arithmetic shown; requisition codes and level numbers explained; bonus, 401(k) and ESPP mechanics). Cut 6 (McKinsey headcount aside; prose repeating the comparison table; ESPP detail; project-paragraph repetition; prep bullets; label bolds). Still thin 2 (target schools rest on one tracker's three examples; Potentia's use for undergrads unconfirmed, cut to a tagged aside). Plain-language rewrites 5. Over target? Marginally by `wc -w` only because of 56 VERIFY tags; publishable body about 5,200 to 5,500.

**5. McKinsey hours (v2).** Expanded 5 (why the client week peaks midweek; study and "staffed" defined; the beach arithmetic; the 720-hour gap spelled out; "AI agents" explained). Cut 3 (v1 bio and first-person memories; v1 closing recap; a "more client-dependent than ever" quote that isn't on either HTCI page). Still thin 2 (2027 base raise is one tracker; Goldman bonus range is self-reported data). Plain-language rewrites 9. Over target? No (under).

## Independent QA (same day): what the second pair of eyes changed

Every QA agent reopened the primary sources (14 to 20 facts each) and recomputed every calculation in Python.

- **#1 Fit:** PEI minutes were a blend of two trackers (15 to 20) that contradicted WSG's own PEI post; now 10 to 20, all three trackers cited. Four Bain "quotes" were paraphrases inside quote marks; replaced with verbatim text from bain.com. A Bain "convince someone of your idea" prompt attributed to Leland doesn't exist; replaced with Leland's "overcome resistance to implement a solution" (prose and grid). The BCG "against both our values and the core competencies" line is a recruiter quote on the page, now attributed that way. HTCI's own timing works out to about 63 percent on actions, not 70; the bold keeps 70 as the midpoint of HTCI and StrategyCase (80) and the tag says so. Echo line cut, one header made plainer, a bold added to the closing section.
- **#2 Salary:** "Most first-years land at 50 to 80 percent of max" was only on HTCI's Bain page (50 to 70); rewritten. Bain Senior AC promotion claim corrected. M&I's IB base is $100K to $125K, not $110K to $125K; its bonus figure is implied (total minus base), now said so. The post-MBA tier 2 gap was overstated (Oliver Wyman and Strategy& are at $190K); rewritten. Management Consulted's sponsorship figure isn't per year; fixed. The live WSG McKinsey post reports a $30K target bonus and $140K to $160K all-in against this article's $18K cap; the article now states the difference. Three $1 rounding alignments in the take-home; BCG post-MBA high end $242K to $240K; "passes $400,000 by junior partner" to "$350,000 to $600,000"; raise arithmetic tightened. Two bolds added (say/don't and next-step sections).
- **#3 Day in the life:** No v1 bio survived. One contradiction fixed (steering committee cadence: "every three or four weeks" vs StrategyCase's weekly; now "depends on the client," both kept). Workstream defined at first use; duplicate definition cut; "running hot" to plain words; associate partner glossed; a 70-word five-link closing sentence split; six one-sentence paragraphs split off for variety. The undergraduate-page quote couldn't be re-fetched (mckinsey.com students pages time out from the workspace); tag says so.
- **#4 Accenture:** An HTCI/Levels.fyi column ($92,000 median, 11 to 19 percent premium) wasn't on any HTCI page; re-sourced to HTCI's June 2026 consulting salary page. Transaction Advisory isn't on the services page; now attributed to job postings. Two posting "quotes" weren't in any posting; replaced with verified lines. Potentia (Accenture's online assessment) has no source tying it to the undergraduate Analyst process; cut from the table and the say/don't block to two tagged sentences. Bonus range made consistent ($9K to $11K both places); "Analyst to MD 12 to 14 years" to "12 to 18"; computer science to marketing in the preferred-majors list (per the posting); meta trimmed to 155 characters.
- **#5 Hours:** No v1 bio or recap survived. StrategyCase's 80 to 95 percent is utilization, not "weeks staffed"; reworded and explained. "A study usually runs two to six months" contradicted the 2 to 4 week PE line that followed; now "a few weeks to six months." Two 12-word headers shortened. Bloomberg's December 2025 figure is "up to 10 percent of some non-client-facing teams," not "about 10 percent." The Lilli interview exercise is a pilot as of January 2026, not "since January 2026." Sternfels gave 25,000 agents at CES and about 20,000 on HBR's IdeaCast the same month; prose now gives the range, the bold keeps 25,000. Team size re-sourced to StrategyCase's three to six (the live BA posting gives none). Three say-it-out-loud fixes; say/don't answers made self-contained.

## Facts verified this batch (reusable; several supersede August 27 and September 8)

- **MBB undergrad pay 2026 (Management Consulted 2026 report, `managementconsulted.com/consultant-salary/`, loads; `/consulting-salaries/` still 403):** McKinsey $112K base, bonus up to $18K, $5K signing, $10K relocation, 7.5 percent retirement, 19 PTO days; BCG $110K, up to $22K, $5K, $6K relocation, profit sharing up to $4,400, 15 PTO; Bain $112K, up to $22,500 (target $15K), $5K, $5K relocation ($10K NYC), 4.5 percent up to $6,050, 20 PTO. Post-MBA $192K / $190K / $192K, bonus up to $40K / $47.5K / $63K, $30K signing. 2026 salaries flat. Hacking the Case Interview firm pages (June 2026) agree on McKinsey and Bain; HTCI's BCG page says $115K base. **StrategyCase (`strategycase.com/mbb-salaries/`, August 31, 2026) alone reports a McKinsey base raise to $120K effective January 2027 with Bain matching; no primary source and no second tracker as of October 11.** The live WSG McKinsey salary post (updated September 28, 2026) has the same $110K to $112K base but a $30K target bonus and $140K to $160K all-in.
- **IB comparison:** Mergers & Inquisitions 2026 report: analyst all-in $165K to $225K (all analyst years), base $100K to $125K, year three $200K to $270K. Goldman $110K base, $60K to $90K bonus (Superday AI, July 2026; WSP confirms base). IB hours 70 to 80 normal, 100+ on live deals (M&I); JPMorgan 80-hour cap "in most cases," live deals exempt (Fortune, September 12, 2024).
- **2026 tax inputs:** IRS Rev. Proc. 2025-32 / IR-2025-103 brackets and $16,100 standard deduction; New York IT-2105-I (2026) $8,000 deduction, state and city schedules, $107,650 / $157,650 / $50,000 phase-in; Social Security wage base $184,500. Worked example: $124,000 gross (base $112,000 plus $12,000 bonus), federal $18,494, Social Security $7,688, Medicare $1,798, state $6,462, city $4,371, take-home $85,187 (68.7 percent), $7,099 a month.
- **Fit formats:** McKinsey PEI 10 to 20 minutes of a 45 to 60 minute interview, one story per interviewer, two first-round and two to three final-round interviews, 10 to 25 follow-ups; dimensions renamed in summer 2025 to Leadership, Connection, Drive, Growth (HTCI June 11, 2026; StrategyCase June 16, 2026; CaseCoach; the live WSG PEI post); mckinsey.com/careers/interviewing static text confirms "four areas" and "two personal examples" and the "your specific role" / "key actions that were critical to success" wording, but the theme labels load dynamically. BCG: "Skills Interview," five qualities (Integrity, Intellectual Curiosity, Creative Thinking, Collaborative Mindset, Drive), 10 to 15 fit minutes inside a 45 minute slot (careers.bcg.com; HTCI June 14, 2026). Bain: same scripted questions for every candidate, "objective scoring system," format varies by office, about 15 minutes where run (bain.com; HTCI June 12, 2026; PrepLounge March 25, 2026). Oliver Wyman about 15 minutes, two first-round interviews (PrepLounge April 28, 2026); L.E.K. 5 to 10 minutes (StrategyCase May 12, 2026); Kearney 55-minute interviews with a behavioral part (PrepLounge August 14, 2025).
- **Day in the life:** HTCI (updated June 5, 2026) week split 28 / 22 / 15 / 12 / 11 / 12 percent on a 65-hour week, teams of 3 to 6, studies 2 to 6 months (supersedes the April 2026 split in the September 8 draft). Leland (February 5, 2026, ex-McKinsey) timestamps: Monday 5:00 / 5:45 / 6:45 / on site about 1 p.m. / 6 to 8 / 8 to 11:30; Tuesday 7 a.m. breakfast, 8:30 check-in, 1 to 2 p.m. problem-solving session, 5:30 to 9 dinner, 9 to 11:30 work; Friday 8 to 9 / noon / 1 to 4 / 5:30 / 5:45. StrategyCase (July 20, 2026): two to three days a week on site, "decided by your client." Current McKinsey BA posting: "take ownership of a workstream," "research, analyzing data, interviews, and brainstorming," "factories, hospitals, mines"; **"teams of three to five" and "present results to client management" are no longer in the live posting** (confirmed on a mirror of a posting closed August 16, 2024). BA Intern 8 to 10 weeks (mckinsey.com/careers/BusinessAnalystIntern); BCG Summer Associates about 8 to 12 weeks; Bain ACI page: one week of training, "own a distinct piece," regular travel, in person most days, generative AI tools.
- **McKinsey 2026 AI and headcount:** Lilli used by 75 percent of the workforce monthly and the Smaje "armies of business analysts" quote are a **Bloomberg** report, June 2, 2025 (Fortune syndicated it; the September 8 log credited Fortune). Business Insider April 2025: Lilli 70 percent, 17 times a week, Deckster. Fortune January 14, 2026: Lilli exercise piloted in some final rounds, Sternfels "about 20,000 agents"; Business Insider January 2026 (CES): 40,000 people, 25,000 agents, 1.5 million hours. Fortune May 29, 2025: 45,100 at end-2023 to about 40,000. Bloomberg December 16, 2025: a few thousand cuts, "up to 10 percent of some non-client-facing teams," over 18 to 24 months, consultant hiring continues. Bain careers blog August 21, 2025: ChatGPT Enterprise, Sage, 19,000+ GPTs.
- **McKinsey hours:** HTCI hours page (May 7, 2026): 55 to 65 average, 70 to 80+ peaks, 12 to 14 hour client days, Friday 6 to 8, "closer to 40" between projects, 6 to 10 travel hours, 2 to 3 days on site, New York and Dallas 60 to 65, Amsterdam and Zurich 50 to 55; work-life page (May 8, 2026): Vault 2026 majority work weekends fewer than once a month, bench 30 to 40, Take Time up to 10 weeks, managers penalized for overworking teams. StrategyCase (July 14, 2026): 50 to 80 staffed, low 60s, 30 to 60 on the beach, 10 to 16 hours Monday to Wednesday, Thursday 10 to 12, Friday 6 to 12, utilization 80 to 95 percent. PrepLounge (June 23, 2025): 12-hour day, "never worked one single weekend." Take Time: mckinsey.com careers blog July 30, 2018 (10 weeks), June 5, 2019 (5 to 10 weeks), July 31, 2020; team norms quote September 6, 2019; **no 2026 program page found.** Kutcher memo: Boston Globe October 2, 2024 (Bloomberg byline), "renewed set of expectations, not a policy." Perlow: HBR October 2009; 64.5 to 57.7 hours over 29 weeks (Knowledge at Wharton, July 3, 2012). CaseCoach April 3, 2023. "More client-dependent than ever" (September 8 draft) is on neither HTCI page.
- **Accenture:** accenture.com careers pages list three Analyst Development Programs (Strategy, Consulting, Technology) and a 10-week Summer Analyst Program; "Accenture Strategy" is no longer the practice name on careers pages (just "Strategy"). Posting R00354373 (Entry Level Advisory Summer Analyst, NAELFY27): five tracks including Strategy, graduation December 2027 to August 2028, June start, 10 weeks, $27 to $35 an hour for the whole posting, 14 cities, posted until October 16, 2026, prior internship required (rotating URL, not linked). Reinvention Services effective September 1, 2025, Strategy led by Muqsit Ashraf (newsroom June 20, 2025); four services effective March 1, 2020 (8-K January 13, 2020); FY2014 four growth platforms. Q4 FY26 (October 1, 2026): $74.18B revenue, about 814,000 people. Accenture FY19 Case Interview Workbook PDF live: 45 to 60 minutes, three case types. StrategyCase (July 13, 2026): Strategy Analyst $90K base, about $100K total, 15 to 25 percent premium over core consulting, 10 to 12 percent bonus, 6 percent 401(k) match, 30 to 50 percent gap to MBB (supersedes the August 27 note of $105K to $115K all-in). HTCI consulting salary page (June 2, 2026): $85K to $95K analyst, about $135K consultant, $187,660 manager, $263,888 senior manager, $400K to $630K MD. Glassdoor Strategy Analyst median $107K (September 2026, cross-check only). Management Consulted: Accenture Strategy MBA sponsorship up to $100K for the top 10 analysts. "Technology Strategy & Advisory Analyst" (August 27 note): only acquisition-specific postings found in 2025 to 2026; not in the article. **Potentia:** no source ties it to the undergraduate Analyst process.

## Images (28)

Rebuild from the repo root with `python3 scripts/images/build_{slug}.py`, then `python3 scripts/images/insert_images.py {slug} drafts/draft-{slug}-v{n}.md` (idempotent). All built in the banking format (`BANK_SERIES`, no gridlines or boxes, direct labels, `add_source()` bottom-left); every build script asserts its numbers against the draft text and exits non-zero on a mismatch (three scripts caught QA edits mid-run and were updated). Every title, label, caption, alt text and source line went through the plain-language and humanizer passes (examples of old → new in the agent reports: "Notice how the week stacks three 13-hour days at the front" → "Monday through Wednesday run 12 to 14 hours each, Thursday 10 to 12 and Friday 6 to 8"; "Centerview-style" takeaway titles replaced with literal ones).

| # | Images | What |
| --- | --- | --- |
| 1 | 5 | Fit minutes per first-round interview by firm; four follow-up question types; PEI answer timing; five-part story skeleton on the recruiting example; story-to-firm grid |
| 2 | 6 | First-year cash by firm (stacked); pay ladder by level; MBB vs IB year one and three with per-hour callout; undergrad base and bonus cap by firm (MBB vs tier 2 and Big 4); federal bracket math table; New York gross-to-net waterfall |
| 3 | 6 | Case team diagram; Monday-to-Friday client-site week grid (Leland times); pyramid principle on the plant-cost example; twelve-week study timeline; week split by activity; headcount and AI agents |
| 4 | 5 | Where Strategy sits inside Accenture (Reinvention Services); total cash by level vs MBB; recruiting calendar October 2026 to fall 2028; case issue tree; Accenture vs MBB vs Monitor Deloitte comparison table |
| 5 | 6 | Hours by weekday; staffed vs between-studies vs average; four-day vs two-or-three-day on-site week; pay per hour McKinsey vs banking at three hours assumptions; headcount and AI agents; Perlow BCG study before and after |

**Regenerate at publish (dated):** Fit 01 and 05; all six Salary images (2026 pay and tax rules); Day in the Life 06; Accenture 02, 03 and 05; Hours 04 and 05.

Toolkit note from the day-in-the-life image agent: on `wsg_diagrams.canvas()` figures, `add_source()` lands at the paper's edge because the axes box spans the whole figure; that script uses local `canvas_source()` and `left_title()` helpers worth folding into `wsg_viz.py`.

## Links removed to pass `check_links.py` from the workspace (restore at publish after a click test)

The workspace proxy can't reach mckinsey.com, and hackingthecaseinterview.com returns 403 to python-requests (200 in a browser). These were live via WebFetch on October 11 and are cited by name in the text:

- `https://www.mckinsey.com/careers/interviewing` (fit interview, McKinsey section)
- McKinsey BA posting and `mckinsey.com/careers/students/undergraduate-degree-candidates` (day in the life, hours)
- The three McKinsey careers blog posts on Take Time and team norms (hours)
- `hackingthecaseinterview.com/pages/consulting-hours-per-week`, `/pages/day-in-the-life-of-a-mckinsey-consultant`, `/pages/mckinsey-pei-questions`, the HTCI salary pages

## Cross-links to add once live

- Fit → 20 Consulting Behavioral Interview Questions (Oct 1 draft), Day in the Life v2, MBB Salary v1. Inbound from the 20 questions draft, Bain and BCG case guides v2, Hours v2.
- Salary → IB Analyst Salary 2027 v1 (banking section), McKinsey Associate role v1 (post-MBA), Hours v2, Accenture v1 (tier 2 table). Inbound from Hours v2, Day in the Life v2, Top 10 Consulting Firms v1.
- Day in the Life → Hours v2 (section 6 hours sentence), MBB Salary v1, Fit v1.
- Accenture → Deloitte S&O guide v1, Top 10 Consulting Firms v1, MBB Salary v1, Fit v1.
- Hours → Day in the Life v2, MBB Salary v1, McKinsey Associate role v1, IB Analyst Salary 2027 v1.

## Still thin / founder decisions

- **McKinsey PEI theme labels:** click the four themes on mckinsey.com/careers/interviewing in a browser to confirm Leadership, Connection, Drive, Growth before publish (trackers and the live WSG PEI post agree; the page itself couldn't be read).
- **$120,000 McKinsey base from January 2027:** StrategyCase only, no primary source. Both salary and hours articles keep $110K to $112K and flag the raise. Decide whether to lead with it at the 2027 refresh.
- **WSG's own McKinsey salary post** reports a $30K target bonus and $140K to $160K all-in; this batch uses Management Consulted's $18K cap and $130K to $140K. The salary article says so; one of the two should be reconciled before publish.
- **Fit article's "about 70 percent on actions":** midpoint of HTCI (about 63 percent by its own timing) and StrategyCase (80 percent). Founder may prefer "about two thirds."
- **Potentia:** no source confirms it in Accenture's undergraduate process; now two tagged sentences. Keep or cut.
- **Accenture target schools** rest on one tracker's three examples. NAELFY28 full-time timing is inferred from last year's Canada posting.
- **Take Time** is described on mckinsey.com only in 2018 to 2020 posts; tag says to confirm with a recruiter.
- **Hours bolded say/don't question labels:** both v2 articles bold the interviewer's question as a callout label; confirm the house convention is acceptable under rule 14.
- **Length:** Day in the Life (18 pages) and Hours (17 pages) land under the 20-page floor before images. Shorter is allowed when the topic is covered; neither was padded.
- 268 VERIFY tags remain across the five, all on moving numbers (pay, tax brackets, tracker figures, dates, quotes), none on entity existence. Strip at Wix publish.

## Repo housekeeping in this batch

- `.claude-skill/SKILL.md` and `.claude-skill/source-verification.md` refreshed from the synced account skill (October 8 wording). The repo's `formatting.md` was kept (it carries the visual spec the synced copy lacks).
- `drafts/draft-mckinsey-hours-honest-read-v1.md` and `drafts/draft-consulting-day-in-the-life-mbb-analysts-v1.md` added from the project mirror (they were missing from the local repo).

## Skills applied

wsg-article (SKILL.md, source-verification, reference-articles, intros, plain-language, thorough-explanations, prose-editing, consulting addendum, formatting, images), wsg-prose-editing and humanizer (register, echo-ender, antithesis, burstiness and say-it-out-loud passes by the drafting and QA agents; the same method on every image string), wsg-article-images (banking format, source lines, image-text humanizer pass), wsg-article-formatting (built through `markdown_to_docx_v2.py`), clean-user-facing-text and remove-ai-marks checks (zero invisible codepoints in drafts, manifests and .docx XML; zero em, en or minus dashes; .docx author and last-modified-by "Wall Street Guide"; no personal identifiers in any output; the watermark HTTP service isn't available in the workspace, so the Unicode scan and metadata strip were done directly, as in the October 5 batch).

## October 12 revision

Revised after founder and Sanskar feedback; see `claude/changelog-oct-12-2026.md`. Current versions: fit v2, salary v2, day in the life v3, Accenture v2, hours v3. The .docx files in `published/ai-written/` are rebuilt from these.
