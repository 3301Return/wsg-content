# Batch brief: 8 WSG articles (September 25, 2026)

Repo root: /home/claude/repo (a working copy of the founder's `wsg-content-main v2`). Today is September 25, 2026.

## Founder instructions for this batch (override defaults where they conflict)

1. **Headlines word for word**, with one change: US spelling everywhere ("Practice", never "Practise"). Headlines are listed below. Do not shorten them even if they exceed the 8-10 word guideline.
2. **Intros do not have to be cookie cutter.** Rotate hooks. The founder explicitly allows a first name for a person in a story sometimes (e.g., "Priya", "Marcus") instead of a single letter, or a more creative opening: a scene, an outside-finance story, a well-known public story (only if real and verifiable). Composite students still must never be presented with full fake names, and WSG never looks bad in its own stories. Stephen intro still present in the first three paragraphs (credentials only from `writers/stephen-turban.md`).
3. **Interview-question and technical articles must be thorough**: explain every answer and every mechanism step by step, in plain words a sharp high schooler could follow on one read. Do not avoid technical terms; use them, then explain them in plain words at first use. Work every number. Longer is expected.
4. **Internal links (backlinks) to existing WSG articles.** Use ONLY URLs listed in `claude/wsg-live-urls-sep-25-2026.txt`. Add 3 to 6 internal links per article where they genuinely help the reader (inline anchor text, never a "related posts" footer). Also note in your final report which OTHER articles in this batch yours should cross-link to once they are live (the 8 slugs are below; do not link to them yet, since they are not published).
5. No em dashes or en dashes anywhere. No hyphens as structural punctuation.
6. Every named entity verified per `.claude-skill/source-verification.md` using WebSearch/WebFetch. Every time-sensitive claim (deadlines, comp, dates, program names, eligibility, test providers) tagged `[VERIFY: ...]` inline, AND researched on the web so the stated value is the best current one. If you can't verify, don't state it.
7. Skip the "outline first, wait for approval" step: the founder approved the headlines; draft straight to file.

## Required reading (in this order) before drafting

- `CLAUDE.md`
- `.claude-skill/SKILL.md`, `.claude-skill/source-verification.md`, `.claude-skill/intros.md`, `.claude-skill/plain-language.md`, `.claude-skill/thorough-explanations.md`, `.claude-skill/prose-editing.md`
- `style-guide/style-guide.md`, `style-guide/recruiting-timeline-glossary.md`, `style-guide/editorial-feedback-july-2026.md`, `style-guide/seo-checklist.md`, `style-guide/link-verification.md`
- `writers/stephen-turban.md`
- The matching template in `templates/` and 1-2 samples in `samples/`
- Consulting articles: also `.claude-skill/consulting.md` and every file in `consulting/` (firm-profiles, recruiting-timeline, case-interview-frameworks, voice-cues). NOTE the known correction: MBB undergrad intern recruiting now runs IB-style: apply sophomore spring (year A) → intern Summer A+1 → graduate A+2. E.g. McKinsey BA intern window Jan 1 to Mar 29, 2026 was for Class of 2028 (Summer 2027 interns). BCG intern deadline June 2, 2026 (Class of 2028). Verify the NEXT open cycle (apps in 2027 for Summer 2028, Class of 2029) on the firms' own pages.
- IB/PE/HF articles: `deep-dives/INDEX.md`; you may extract text from `deep-dives/400-IB-Questions-Interview-Guide.pdf` and `deep-dives/Wall+Street+Prep+_+The+RedBook.pdf` with `pdftotext` for technical question sourcing (paraphrase, never copy).

## The 8 articles

| # | Vertical | Exact headline | Slug | Format | Hook guidance |
|---|---|---|---|---|---|
| 1 | IB | Finance Internship: How to Find One as a Freshman or Sophomore | finance-internship-freshman-sophomore | ultimate-guide | Friend/family story with a first name (e.g., a friend's younger sibling) |
| 2 | IB | Private Equity Interview Questions: 25 for Undergrad Candidates | private-equity-interview-questions-25-undergrad | listicle (25) | Direct claim or stat with a bite |
| 3 | IB | Hedge Fund Interview Prep for Undergrads: Questions and Pitch Structure | hedge-fund-interview-prep-undergrads | ultimate-guide | Creative: a real, verifiable public stock-pitch story, or a vivid scene |
| 4 | IB | Investment Banking Cover Letter: Template and Example That Landed Offers | investment-banking-cover-letter-template-example | ultimate-guide | First-call quote |
| 5 | CON | Consulting Online Assessments: What Each Firm Uses and How to Prepare | consulting-online-assessments-by-firm | ultimate-guide | Question the reader is already asking |
| 6 | CON | 25 Case Interview Questions to Practice Before Your First Round | 25-case-interview-questions-to-practice | listicle (25) | Scene |
| 7 | CON | How to Get the BCG Sophomore Internship | how-to-get-the-bcg-sophomore-internship | niche (firm-or-role) | Decision moment with a first name |
| 8 | CON | Consulting Case Study: How to Structure Your Answer Under Pressure | consulting-case-study-structure-under-pressure | ultimate-guide | Creative outside-consulting story (e.g., how pilots or ER doctors use checklists under pressure; must be real/verifiable if factual) |

Existing live overlap to handle: the site already has "25 Private Equity Interview Questions That Actually Get Asked" (link to it and differentiate #2 as undergrad-candidate specific: sophomore/junior PE internship interviews, fewer on-cycle-associate questions, more "why PE as an undergrad", paper LBO basics explained from zero). The site already has a consulting cover letter article (link it from #4) and a BCG online assessment guide and Casey chatbot guide (link from #5 and #7).

## Output and checks

- Write to `drafts/draft-{slug}-v1.md` with the frontmatter from SKILL.md "Output format" (byline: stephen-turban; meta description starts "WSG founder Stephen Turban", 150-160 chars).
- Every H2 carries 2-3 self-contained bolded claims (founder asked for more bolding last batch). Listicle items: bold the question/item lead.
- Include 1-2 H2 sub-questions right after the intro.
- Run: `python3 scripts/check_article.py drafts/{file}.md`, `python3 scripts/check_style.py drafts/{file}.md`, `python3 scripts/check_links.py drafts/{file}.md`. Fix every hard failure. (check_links may show wallstreetguide.net or some firm sites as unreachable/403 from this sandbox; if so, confirm with WebFetch instead and note it.)
- Grep your file for "—" and "–" and remove them.
- Do NOT build the .docx; the coordinator does that.
- Final reply to coordinator: file path, word count, hook used, internal links used, suggested cross-links to other batch articles, list of VERIFY tags, and the Thoroughness Report. Keep it under 400 words.
