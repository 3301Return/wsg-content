# Batch log: 8 articles + sample IB cover letter PDF (September 25, 2026)

Repo: `Downloads/wsg-content-main v2/wsg-content-main` (the founder's live copy for this batch).

## What shipped

Drafts in `drafts/` (v1, all pass `check_article.py` and `check_style.py` with no hard-rule failures, zero em or en dashes):

| # | Vertical | Headline | Format | Hook | Words | VERIFY tags |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | IB | Finance Internship: How to Find One as a Freshman or Sophomore | ultimate-guide | friend story (a friend's brother, Owen) | ~4,000 | 16 |
| 2 | IB | Private Equity Interview Questions: 25 for Undergrad Candidates | listicle (25) | stat with a bite (Blackstone 57,000 / 138) | ~9,800 | 12 |
| 3 | IB | Hedge Fund Interview Prep for Undergrads: Questions and Pitch Structure | ultimate-guide | real scene (Einhorn, Ira Sohn 2008) | ~7,400 | 8 |
| 4 | IB | Investment Banking Cover Letter: Template and Example That Landed Offers | ultimate-guide | first-call quote | ~3,900 | 5 |
| 5 | CON | Consulting Online Assessments: What Each Firm Uses and How to Prepare | ultimate-guide | reader question | ~5,000 | 15 |
| 6 | CON | 25 Case Interview Questions to Practice Before Your First Round | listicle (25) | scene (the silent interviewer) | ~9,800 | 2 |
| 7 | CON | How to Get the BCG Sophomore Internship | niche (firm-or-role) | decision moment (Leo) | ~4,000 | 25 |
| 8 | CON | Consulting Case Study: How to Structure Your Answer Under Pressure | ultimate-guide | real outside story (US Airways 1549, NTSB report) | ~5,500 | 2 |

.docx builds in `published/ai-written/` via `scripts/markdown_to_docx_v2.py` (Arial, Title 24 / Heading 2 18 / body 11, double spacing). Author and Last Modified By set to "Wall Street Guide" on all eight. Filenames use " - " in place of colons.

Sample cover letter: `published/assets/Sample Investment Banking Cover Letter (John Doe).pdf`, one page, built by the new `scripts/build_cover_letter_pdf.py` from `drafts/sample-ib-cover-letter-john-doe.md`. PDF metadata (Author, Creator, Producer) set to "Wall Street Guide". The letter is fictional and the article says so: a composite built from the patterns in letters that got students interviews, with bank, banker and school names left in brackets so no real person or firm is invented. The article carries a `[VERIFY: add PDF download link once uploaded to Wix]` placeholder.

## Founder decisions taken during the batch

- Headline #6 switched from "Practise" to US "Practice". All other headlines used word for word, including the ones over the 8-10 word guideline.
- Intros allowed to break from the single-letter composite rule: first names (Owen, Leo) and real, sourced public stories (Einhorn on Lehman; Flight 1549) are in the rotation. WSG still never looks bad in its own stories.
- Interview-question and technical articles written thorough: every answer walked step by step, every number worked, technical terms used and then explained in plain words at first use. Word counts run well over the guidelines by design.
- Cover letter example is fictional, framed honestly. Headline kept.
- Article #2 is aimed at undergrad PE internship candidates to keep it separate from the live "25 Private Equity Interview Questions That Actually Get Asked" post; it links to that post once.

## Internal links (backlinks) used, per article

All links point only to URLs in `claude/wsg-live-urls-sep-25-2026.txt` (the blog sitemap fetched September 25, 2026).

- **#1 Finance internship:** 10 IB internships to apply to in 2027; freshman-to-junior roadmap; top 10 sophomore insight programs; 2026 diversity finance fellowships; IB internship CV; IB with no experience.
- **#2 PE questions:** 25 PE interview questions that actually get asked; walk me through an LBO; walk me through a DCF; PE internship ultimate guide; top 10 PE recruiting firms; private credit vs PE.
- **#3 Hedge fund prep:** ultimate guide to breaking into a hedge fund; Bridgewater internship; what an equity research analyst does; S&T ultimate guide; DCF walk-through; break into restructuring.
- **#4 IB cover letter:** consulting cover letter template; IB internship CV; 10 IB internships 2027; breaking into Wall Street 10 strategies; top 10 investment banks; top middle market banks 2027.
- **#5 Online assessments:** McKinsey Solve guide; BCG online assessment guide; BCG Casey chatbot guide; consulting recruiting timeline 2026; 10 free case prep resources; 10 consulting interview prep tools.
- **#6 25 case questions:** McKinsey case interview guide; how to prepare for a consulting interview; 10 tips to beat the case interview; McKinsey PEI; 10 free case prep resources; MBB ultimate guide.
- **#7 BCG sophomore:** BCG online assessment guide; BCG Casey chatbot guide; MBB ultimate guide; consulting recruiting timeline 2026; 15 best consulting internships; consulting resume checklist.
- **#8 Case structure:** 10 tips to beat the case interview; McKinsey case interview guide; how to prepare for a consulting interview; MBB ultimate guide; McKinsey PEI; 10 free case prep resources.

## Cross-links to add between the eight once they're live

| From | To |
| --- | --- |
| #1 Finance internship | #4 cover letter (steps 5 and 6, small firms sometimes ask for one); #3 hedge fund prep (student-fund stock pitch section); #2 PE questions (family office / PE targets) |
| #2 PE questions | #3 hedge fund prep (pitch question); #1 finance internship (fit section); #4 cover letter (light) |
| #3 Hedge fund prep | #2 PE questions (valuation and accounting overlap); #1 finance internship (recruiting timeline section); #4 cover letter (programs section) |
| #4 Cover letter | #1 finance internship; #2 PE questions (middle-market "selling to a PE firm" passage); #3 hedge fund prep (light) |
| #5 Online assessments | #6 25 case questions (Casey and mental math sections); #8 case structure (Casey written answer and video); #7 BCG sophomore (BCG section) |
| #6 25 case questions | #8 case structure (practice and say/don't-say sections); #5 online assessments (prep section); #7 BCG sophomore ("how many practice cases" answer) |
| #7 BCG sophomore | #5 online assessments (CCA/Casey step); #8 case structure and #6 25 case questions (case section and prep plan); #1 finance internship (fallback section) |
| #8 Case structure | #6 25 case questions (practice plan); #5 online assessments (practice plan); #7 BCG sophomore (firm-format paragraph) |

Also worth adding to older live posts: link the new #4 from the live consulting cover letter post and the IB internship CV post; link #2 from the live 25 PE questions post ("if you're an undergrad, start here"); link #5 from the McKinsey Solve, BCG online assessment and Casey posts; link #7 from the 15 best consulting internships post.

## Research findings that affect the context bundle

- **BCG sophomore programs (article #7).** As of September 25, 2026, the Growing Future Leaders and Bridge to Consulting links on careers.bcg.com serve the generic campus page, and BCG's job search returns no sophomore postings. BCG Advance has moved to juniors. BCG Embark (new in 2026, inside Launch, for sophomores of all backgrounds) is the visible early-engagement track. Bridge to BCG confirmed as advanced-degree only. The last confirmed GFL cycle closed September 24, 2025 (Villanova and Hacking the Case Interview; Duke's page shows September 11, 2024 for the prior cycle). BCG Summer 2027 Summer Associate deadline June 2, 2026 confirmed via Yale OCS and Tufts. `consulting/recruiting-timeline.md` and `consulting/firm-profiles/mbb.md` should pick up Embark and the GFL status.
- **McKinsey SSBA.** Last confirmed cycle ran May 1 to June 10, 2025; McKinsey has skipped a cycle before and its site blocks sandbox fetches, so Summer 2027 status is unconfirmed.
- **Consulting online assessments (article #5).** Firm-sourced: McKinsey Solve page, FAQ PDF and July 2025 lab blog (about 300,000 takers a year); Bain's digital assessment page names Sova and TestGorilla, 30 to 40 minutes, calculator allowed; PwC's FAQ (15 to 20 minutes, results valid 120 days). Tier 2 and Big 4 US formats come only from prep sites that disagree with each other; the article says so. Prep-site claims left out because no firm source backs them: Casey's "+3/-1" scoring, pass rates, "Sea Wolf replaced Ecosystem in 2025."
- **Hedge fund programs (article #3).** Citadel Summer 2027 posting took 2028 grads at $2,500 to $3,000 a week and closed February 4, 2026. Bridgewater $71,000 for Summer 2027. D. E. Shaw Fundamental Research Analyst Intern $25,000 a month. Millennium's first Investment Internship class was Summer 2027 (about 30 interns, full by June 2026). All tagged for the Summer 2028 cycle.

## Link verification notes

`check_links.py` reports the following as unreachable from the drafting sandbox only; each was confirmed live with a browser-style fetch: mckinsey.com (timeout), quiz.bcg.com (proxy block), goldmansachs.com program pages (403), careers.bankofamerica.com (403), morganstanley.com students page (timeout), citadel.com/careers/students (403), blackstone.com students page (403), pif.gov.sa (403), pwc.com (403), and wallstreetguide.net itself (429 rate limit when many links are checked at once). Wells Fargo's sophomore program page returned 404 and its careers site blocked the check, so Wells Fargo is named in #1 without a link. Click-test all of these before publish.

## VERIFY tags to clear before publish (highest value first)

- #7: whether GFL posts a fall 2026 cycle; Summer 2028 Summer Associate window and graduation range; Launch/Embark 2027 dates; SSBA, BEL and CREW 2027 dates.
- #1: every bank freshman and sophomore program window for the cycle open at publish (Goldman Possibilities Series and Emerging Leaders, Morgan Stanley Early Insights, Citi Early ID, BofA Sophomore Summer Analyst, JPMorganChase Fellowship, Wells Fargo Sophomore Discovery, MLT, Girls Who Invest, SEO).
- #5: each firm's 2026-27 test format, especially the BCG CCA-then-Casey sequence in the US and Bain's Sova norm-group scoring.
- #3: Summer 2028 pay and open dates at Citadel, Point72, Bridgewater, D. E. Shaw, Millennium, Balyasny; the S&P 500 forward P/E (FactSet, 20.0 in August 2026).
- #2: Blackstone 57,000 / 138; Bain PE market figures; EA take-private terms and the "largest LBO ever" description; "12 is the new 5."
- #4: which bulge bracket portals ask for a letter in the 2028 cycle; Evercore FAQ still says required; the PDF download link.
- #6 and #8: Summer 2028 MBB open dates; the CDC marriages figure; whether Beautify and Diconsa are still on McKinsey's interviewing page.

Grep each draft for `[VERIFY` for the full list.

## Tooling changes

- `scripts/markdown_to_docx_v2.py`: added pipe-table support (markdown tables render as Word tables, Arial 10pt black, bold header row, single-spaced cells). Everything else unchanged. Three drafts in this batch use tables (#5, #7, #8).
- `scripts/build_cover_letter_pdf.py`: new, builds the one-page sample cover letter PDF with Wall Street Guide metadata.
- `claude/wsg-live-urls-sep-25-2026.txt`: the live post list used for internal linking. Refresh it from `https://www.wallstreetguide.net/blog-posts-sitemap.xml` before the next batch.
- `claude/batch-brief-sep-25-2026.md`: the brief the drafting agents worked from.

## Still thin (needs the founder)

- #3 section 2 and #8 use a composite student "R" with no real detail. Swap in a real WSG student story if one exists.
- #6's only first-person McKinsey moment (interviewer-led cases) is general. A real memory would strengthen it.
- #2 Q3's sample answer uses placeholders for a firm deal and a person spoken to, and says so.
- #7: GFL pay and BCG conversion rates are unpublished; the article says so rather than guessing.

## Skills applied

wsg-article (SKILL.md, source-verification, intros, plain-language, thorough-explanations, prose-editing, formatting, consulting addendum), humanizer / wsg-prose-editing passes (register grep across all eight came back clean: no "delve", "landscape", "crucial", "navigate", "ultimately", "it's worth noting", "in this guide we", or any phrase on the intros cut list), clean-user-facing-text and remove-ai-marks checks (no em or en dashes, docx author metadata set, PDF metadata set to Wall Street Guide, no personal identifiers in any output).

## Independent QA pass (same day)

A separate checker that had not seen the drafting confirmed: formatting standard on all eight .docx (one Title, Heading 2 only, Arial, black, 11pt body, double spacing, author metadata); headline and H2 parity between .md and .docx; no leaked markdown; VERIFY counts matching; 25 items in each listicle; zero em or en dashes in every docx and the PDF; PDF metadata clean with no personal identifiers. Six fact spot-checks confirmed against primary sources (NTSB AAR-10/03; Einhorn's 2008 speech; Blackstone 57,000 / 138; Bain's Sova / TestGorilla page; Evercore's FAQ) and one via secondary sources (BCG's June 2, 2026 deadline).

Fixes made after QA: two untagged time-sensitive claims in #7 (BCG Advance eligibility) tagged; two precise figures in #7 (school-page count, BEL founding year) softened and tagged; one fragment triad in #7's intro rewritten as a sentence; the PDF placeholder line in #4 rewritten so the sentence stands on its own with the VERIFY tag after it. Both .docx rebuilt.

## Founder review round 1 (September 25, 2026, same day)

- **25 Case Interview Questions, v2.** Founder: bolding wrong and too little, slightly too long, needs a mix of list form and paragraphs. v2 restructures every case: a bolded lead sentence (type and skill tested), the prompt in plain type under a bold label, three clarifying questions, the structure as a short prose paragraph with one bolded insight, the math as bullets ending in a bolded result sentence, the recommendation as a short quoted paragraph, and a bolded takeaway. 258 bold spans (130 full-sentence claims) vs 70 in v1. Length 9,640 words vs 9,758; the 25 math walk-throughs alone are about 3,350 words and were kept step for step, so a bigger cut would mean dropping calculations or cases. .docx rebuilt from v2.
- **Finance Internship, v2.** Founder: add much more networking. Two new H2 sections: "How many people should you network with for a finance internship?" (5 chats a week, 50 emails a week with the reply-rate funnel worked, the 2-per-firm-per-day rule and why, a Sunday-to-Friday schedule) and "Keep networking after you land a finance internship" (the 12 to 18 month pipeline, thank-you within 24 hours, one more intro per call, update every 6 to 8 weeks with a sample email, a five-column tracker, re-engagement with a sample email). 6,650 words vs 4,000. .docx rebuilt from v2.
