# Changelog: October 12, 2026 (founder and Sanskar feedback on the consulting drafts)

## The feedback

- Founder: "the process just seems like it's following instructions too much without using its own intelligence, like it's starting off the consulting skeleton by spending a lot of time talking about similarities/difference between banking resumes."
- On a Leonardo da Vinci "earliest known resume" paragraph: "🤢."
- Sanskar: "let's also do one thing where we stop asking it to explain these redundant parts. I think the student doesn't need the 'why' behind resume screenings" (on "Start on the firm's side of the table. McKinsey receives roughly 1 million resumes...").
- Sanskar: "a bug in the system where a lot of consulting banking becomes interlinked... deflecting the point into banking resume opposed to explaining what is actually the issue."

## Rule changes

- `.claude-skill/prose-editing.md` (and `style-guide/editorial-feedback-july-2026.md`): new rules 17 to 20 (stay in the article's own field; no history or trivia the reader can't act on; say what to do, not why the firm does it; judge every section against the headline), a new item 7 in the rule 16 cut order, and four new mechanical spot checks.
- `.claude-skill/SKILL.md`: new "October 12, 2026 review" section at the top; editorial rule 4 ("lead with the company's perspective") narrowed, since it was producing the firm-side "why" sections; a section-verdict step added to the workflow (step 5); a sixth gut-check question; a hard rule.
- `.claude-skill/consulting.md`: "Explain consulting directly" note under openings.
- `skills/wsg-article.skill` and `skills/wsg-prose-editing.skill` repackaged. Account-skill updates proposed for wsg-article and wsg-prose-editing.

## The five October 11 articles, revised

Founder decisions: banking kept as one short comparison only in MBB Salary and McKinsey Hours (where the reader is choosing); skills updated. Brief: `claude/revision-brief-oct-12-2026.md`.

| Article | New version | Body words (no tags) | Pages with images | Images | Main cuts |
| --- | --- | --- | --- | --- | --- |
| Consulting Fit Interview | v2 | 6,113 → 5,351 | 24 | 5 | Firm-side "what the interviewer is trying to answer" block, Bain/BCG process quotes, "the interviewer is checking whether" lines in the stories, McKinsey's 2025 dimension rename history, the recap closer |
| MBB Salary Breakdown 2026 | v2 | 5,265 → 4,737 | 23 | 6 | Banking cut to one table and four sentences; banking removed from intro, offer-letter section and say/don't; tier 2 prose that repeated its table; trivia (tracker history, Bain title rename); recap closer |
| Consulting Day in the Life | v3 | 4,745 → 4,541 | 21 | 5 (headcount chart removed) | Minto biography, "historically," McKinsey headcount and layoffs, AI-agent counts, five "why the firm" lines |
| Accenture Strategy Analyst | v2 | 5,555 → 4,925 | 22 | 4 (org chart removed) | "Where Strategy sits" section (revenue, headcount, 2014 and 2020 reorganizations), firm-perspective framing of the job, MBB asides outside the comparison, recap closer |
| McKinsey Hours | v3 | 4,417 → 3,454 | 15 | 3 (pay, headcount, Perlow charts removed) | Pay-per-hour section, JPMorgan cap story, Kutcher memo, headcount and layoffs, Perlow 2009 study, 2027 raise; banking kept as a four-sentence sub-question |

All five pass check_article, check_style and check_links; zero hits on the new rule 17 to 19 greps outside the two allowed comparisons. McKinsey Hours now runs about 3,450 words (15 pages with images), under the niche range; Stephen's reference articles run 1,700 to 3,000, and nothing was padded back.
