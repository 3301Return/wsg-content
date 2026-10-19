---
name: wsg-prose-editing
description: Prose-level editing rules for WallStreetGuide (WSG) articles from the July 2026 editorial review, the September "say it out loud" test, and the October 2026 founder, Stephen and Sanskar reviews (plain and signposted headers, question headers, full-sentence bolds, no unsupported opinions, length, staying in the article's own field, no trivia, no firm-side why, judging every section, no absolutes, saying each point once, reader level, example proportion). Use when writing, editing, or reviewing WSG articles or any draft that should not read as AI-written. Trigger on requests to cut AI tells, remove echo sentences or em-dashes, humanize a draft, shorten a draft, improve sentence variety, fix odd or off-register wording, or apply burstiness and perplexity principles.
---

# WSG Prose Editing

Pruning and variance rules from the July 2026 editorial review, extended in September and October 2026. They layer on top of the WSG style guide when working in the WSG repo, and stand alone for any other prose. They tell you what to cut and how to vary. The WSG format itself (bolded skim narrative, H2 sub-questions, say/don't blocks) stays as specified in the main skill.

Canonical repo copy: `style-guide/editorial-rules.md` Part 2. This module is the packaged mirror so the rules travel with the skill; edit the repo copy first, then re-mirror here and repackage.

Source: the July 12, 2026 edit pass on the consulting cover letter draft, the August 27 founder review, the October 7 founder review, Stephen's October 8 reference list, the October 12 founder and Sanskar notes on the consulting resume draft, and the October 14 founder review of the STAR and Accenture drafts. Every existing rule in `style-guide/style-guide.md` and `style-guide/editorial-rules.md` Part 1 still applies.

## 1. Cut echo enders. Keep payoffs.

The July review found 8 to 9 sentences that closed a section by restating the paragraph's point in fancier words. Real examples that were cut:

> "Most weak cover letters fail on generic content and recycled templates, which means specificity is both the fix and the differentiator."

> "Naming a specific contact, practice, or piece of work is the single clearest way to prove your interest in a firm is real."

Both sentences follow paragraphs that already made the same point. A reader who got it the first time reads the restatement as filler. A reader trained on AI text reads it as a tell.

**The delete test:** remove the sentence. If the section lost no information, it was an echo. Cut it.

**The suspect openers:** "which means," "in other words," "put simply," "that's why," "ultimately." A closing sentence that starts with one of these is guilty until proven otherwise.

**The bound:** don't strip every section ender. Two protections apply.

First, the skim narrative is load-bearing. WSG articles bold self-contained claims so that reading only the bolds tells the argument, and `check_style.py` tests for this. After cutting, at least three sections should still end on a bolded claim, and the bold-only read-through must still carry the article. If it doesn't, you cut a payoff, not an echo. Restore it.

Second, calibration sentences are content, not echo. "The cover letter is a margin tool, not a decider, but margins are exactly where competitive applications are won or lost" was cut in the July pass and should not have been. It sizes the stakes. A sentence that tells the reader how much something matters, with a mechanism attached, earns its place even in closing position.

The distinction in one line: an echo repeats the paragraph at the same level of abstraction, a payoff compresses it into a rule the reader can carry out of the article.

## 2. Dangling verbs get objects, and the fix obeys the punctuation rules

Caught in review: "This is where most letters fall apart and where you can separate." Separate what? The verb needs an object.

Em dashes stay banned in body copy, including in edits, including when the dash would genuinely read fine. Fix with a period and a short second sentence:

> "This is where most letters fall apart. It's also where you can set yourself apart."

Same rule for en dashes and spaced hyphens used as pause punctuation. Commas, periods, and colons cover every case.

## 3. Sequences become lists. Arguments stay prose.

Three or more consecutive sentences sharing the same scaffold ("The first... The second... The third..."), describing steps, parts, or fields, are a list. Convert them to bullets.

Reasoning is not a list. If the sentences build on each other rather than sit beside each other, bullets would break the argument. Leave it as prose.

Formatting note: blank line before the list, or it renders wrong in Wix and the docx builder mangles it.

## 4. Repair voice with something concrete, not something safer

The review replaced "That last point is the quiet one:" with "That last part matters more than people realize:". The replacement is worse in a different direction: "more than people realize" is filler.

When a phrase reads as strained, the repair must add information, not subtract personality. The concrete fix: "That last paragraph is the one screeners actually remember." A specific claim beats both the clever version and the bland one.

## 5. Sample text inside articles follows body-copy rules

Example cover letters, example answers, and say/don't blocks are the most-copied text in any WSG article, so they get edited hardest. Cut stated-goal throat-clearing, split any sentence carrying three ideas, and swap abstract language for one concrete detail.

## 6. Burstiness: vary length on purpose

AI text runs uniform: sentences of 15 to 25 words, paragraphs of 60 to 90, every section the same shape. Human writing spikes.

- In any five-paragraph stretch, at least one paragraph under 15 words and at least one over 100.
- Sentence lengths in a section should span from under 6 words to over 30.
- At least one section should open with its shortest sentence.

Vary by cutting, never by padding.

## 7. Perplexity: predictable phrases teach nothing

If the reader can finish your sentence, the sentence carried no information. Raise perplexity the honest way: names, numbers, dates, mechanisms. Never with thesaurus swaps.

| Cut this | Why |
| --- | --- |
| "It's not just X, it's Y," "X is not Y dressed up as Z" | The most common AI antithesis scaffolds |
| Adjective triplets ("clear, concise, and compelling") | Rule-of-three filler; keep the strongest one |
| "at the end of the day," "the key takeaway" | Pure connective tissue |
| "navigate," "landscape," "leverage" (as a verb), "crucial" | AI register words; say the plain thing |
| "more than people realize," "best-kept secret" | Filler hedges and fake reveals |

## 8. Restraint is a rule, not a mood

Every edit should be traceable to a named rule in this file or the style guide. If you can't name the rule a sentence breaks, leave it alone. Rewriting for taste creates churn and new errors.

## 9. The "say it out loud" test

Every sentence, headers included, has to pass one test: **would a person say this sentence out loud to a student across a table?** If not, write the plain version.

Real lines flagged and removed:

| Cut this | Why |
| --- | --- |
| "That's the headline." | Nobody talks like this. |
| "the caveats the recruiting brochures leave out" | Odd object, odd rhythm. |
| "before counting retirement money" | Unclear. Say "before the 401(k) match" or cut it. |
| "life happens in deposits," "which kind of tired you want to be," "the smallest interesting number" | Copywriter lines. They sound written, not said. |
| "the interview's real center of gravity," "pressure-tested for your fingerprint" | Metaphor stacked on metaphor. |
| "case clock," "cheap homework," "mental math under a clock," "holdouts need dragging" | Off-register, compressed, or cute. |
| "Rent is not national." | A fragment pretending to be an insight. |
| "the job is a lobby, not a house" (October 8) | Stephen: "this is terrible." Say the fact: tenure is about two years. |
| "a clock that never stops," "That is the part that catches people," "walk out rattled" (October 8) | Narrative drama. Say how long it is and what it tests. |

The fix follows rule 4: replace it with something concrete (a number, a name, a mechanism), not with a safer cliché.

Two related checks:

- **No fake-precise effort counts.** "Ran 47 practice cases" reads as invented. Use roundable language. Real outcome numbers stay.
- **WSG never looks bad in its own stories.** Stories go in the body, never in the intro.

## 10. Plain headers (October 7, 2026)

A reader who sees only the header should know what's in the section. No metaphor, no clever second half after a colon.

| Cut this | Write this |
| --- | --- |
| "The MECE framework in plain words: start with a room, not a business" | "What MECE means" |
| "Centerview is a 2006 startup that now sits on the biggest deals in the world" | "Centerview's history and the deals it advises on" |
| "An investment banking analyst salary comes in five pieces, and only one of them arrives every two weeks" | "How analyst pay is structured" |

## 11. No negatives (October 7, 2026)

Leave out what the writer, WSG or the article is not, can't do or won't cover, and leave out negative framings of the reader. Delete them; say what the article does or what the reader should do. Factual downsides the reader needs (a review's cons, a mistakes section written as fixes) stay, said plainly.

## 12. Signposted numbered headings (October 8, 2026)

In an ultimate guide or any "N things" article, each numbered heading is a short, plain claim that tells the reader the takeaway before they read the section. Stephen's model (How Hard Is It to Get Into Investment Banking?):

> 1. Your school matters but probably not in the way you think

Others from the same article: "Your GPA is a filter, not a scorecard." "Timing is the silent killer."

What makes these work: under 12 words, ordinary words, a point of view, and a reader could repeat it. That's different from the rule 10 failures, which are long, decorative, or need the body to decode. Descriptive headers ("What MECE means") stay right for explainer sections; claim headers are for the numbered insights.

## 13. Question headers use the reader's exact question (October 8, 2026)

H2 sub-questions and FAQ entries are phrased the way a student types them into Google: "What is a sophomore insights program?" "Are sophomore insights programs only for diverse candidates?" "Can I retake McKinsey Solve if I fail?"

- Sentence case, ends with a question mark, one question per header.
- The first sentence under it answers the question directly. Yes, no, a number, or a definition. Then the detail.
- No clever questions ("So, what's the catch?"), no two-part questions.

## 14. Bolded sentences are full sentences with a fact (October 8, 2026)

*October 14: a bold can and should carry a qualifier where the fact varies (rule 21), and not every section needs one.* Stephen flagged the Sophomore Insights opener as the model: the bolded line is a complete sentence with a concrete number in it ("roughly 5 to 10 times more likely to convert into a Summer Analyst offer"). Bold a sentence that would still make sense pasted alone, carries a fact or a clear rule, and is the one thing a skimmer should take from that section. Never bold a fragment, a label, or a sentence that only sets up the next one.

## 15. No unsupported opinions about what people get wrong (October 8, 2026)

Stephen's criticism of the Casey opener: "weirdly opinionated about what people get wrong without showing evidence." Cut sentences that claim what "most candidates" think, expect, miss or get wrong unless the next sentence gives the evidence (a survey, a firm's own statement, a number). If there's no evidence, state the fact the reader needs instead: what the test is, how long it takes, how it's scored.

## 16. Length: cut to the plan's budget (October 8, updated October 14, 2026)

Length follows the question (October 14, 2026): focused pieces about 2,500 to 3,500 words, in-depth guides up to about 6,000 (SKILL.md has the details). The editorial plan sets the budget. When a draft runs over its budget, cut in this order, before touching any step of what the reader will do:

1. Echo enders and recaps (rule 1). A closing section never re-summarizes the article.
2. Second and third worked examples of the same mechanism. Keep the best one and give the follow-ups as one or two sentences.
3. Tables that repeat what the prose already said, and prose that repeats a table.
4. "Honest read," "what this means for you" and "the trade-off" sections that restate earlier sections.
5. Background the reader didn't come for (founding history, long firm lists, every deal in a year).
6. Say/don't blocks beyond two or three, or any that repeat what the examples already showed.
7. Explanations of how the system works (how firms score, the research behind a method, why a process exists) when the reader only needs what to do (rule 22). Levels and detail above the reader's stage (rule 23). Points already made in another format (rule 22).
8. Comparisons with another field outside the one allowed comparison section (rule 17), history and trivia (rule 18), and firm-side "why" setups (rule 19). Items 7 and 8 usually go before anything in items 1 to 6.

Never cut a step from what the reader will do (`thorough-explanations.md`). Cut repetition, background and side material instead.

## 17. Stay in the article's own field (October 12, 2026)

Sanskar's flag on the consulting resume draft: it opened its skeleton by comparing consulting resumes with banking resumes, and a later paragraph said "students treat a consulting resume as a banking resume with the order changed." His note: "a bug in the system where a lot of consulting banking becomes interlinked... deflecting the point into banking resume opposed to explaining what is actually the issue."

A consulting article explains consulting. A banking article explains banking. Don't explain one by contrasting it with the other ("unlike banking," "a banker would," "the banking version of this"). Explain the thing directly.

A comparison belongs in an article only when the reader is choosing between the two (salary, hours, "consulting vs banking"), and then once, in its own clearly labeled section or sub-question, kept short. Nowhere else.

## 18. No history or trivia the reader can't act on (October 12, 2026)

Flagged: a consulting resume paragraph built on Leonardo da Vinci's 1482 letter to Ludovico Sforza as "the earliest known resume." Reaction: "🤢."

Cut founding dates, reorganization timelines, who coined a term and when, "the earliest known," famous-person anecdotes, and firm-level revenue and headcount in articles about a junior role. **The test:** if a student deleted the sentence, would they do anything differently? If not, it goes. A one-clause attribution ("the pyramid principle, from Barbara Minto's book") is fine. A biography isn't.

## 19. Say what to do, not why the firm does it (October 12, 2026)

Flagged: a section that opened "Start on the firm's side of the table. McKinsey receives roughly 1 million resumes annually... The resume screen exists to get the stack down to the people worth 45 minutes of a consultant's time." Sanskar: "the student doesn't need the 'why' behind resume screenings."

Cut firm-side setups ("start on the firm's side," "the screen exists to," "the firm is trying to," "to understand X you have to understand why firms...") and application-volume statistics used to justify a process. Give the student the what and the how. Keep a "why" only when it changes what the student does, and then as one clause attached to the instruction ("Put GPA on its own line, because the screener checks it first").

This narrows the older "lead with the company's perspective" rule (SKILL.md editorial rule 4), which was being over-applied.

## 20. Judge every section against the headline (October 12, 2026)

The founder's note on the same batch: "the process just seems like it's following instructions too much without using its own intelligence." Templates, briefs and outlines list sections that might help. They're not a checklist.

Before delivering, give every H2 a verdict: keep, cut, shrink or rewrite. **The question:** does a student reading this headline need this section to do what the headline promises? Background sections, "how this differs from X" sections, tables that repeat the prose, and closers that recap all fail it. Cut them or fold their one useful fact into a section that passes. Shorter is fine when the topic is covered; never pad back to the length target.

## 21. Conversational, not absolute (October 14, 2026)

The founder: "The writing is still a little AI-y and absolute in places. Things like 'five stories cover every behavioural question' or making very definite statements about how recruiters score candidates aren't really the tone we're going for, and aren't necessarily true in every case... Whenever it sounds like a Nat Geo narrator, that's an issue."

Recruiting varies by firm, office, team, interviewer and year. Write like someone who knows the field talking to a student: "usually," "often," "most firms," "some banks," "in most first rounds," "a common approach is." Use a qualifier where it's true, not on every sentence; a plain fact ("Goldman's first round is a HireVue") stays plain.

| Cut this | Write this |
| --- | --- |
| "Five stories cover every behavioral question." | "Five stories usually cover most of what you'll be asked." |
| "The interviewer is scoring Partnership." | "A Goldman interviewer will often be listening for teamwork." |
| "Banks score your answers against a rubric." | "Many banks use a set list of qualities when they review answers." |
| "That's the format at the banks." | "That's how most large banks run it." |
| "Every one of the six fixes can be run in ten minutes." | "Most of these fixes take a few minutes on a written story." |

Narrator voice is a sentence that pronounces on how the world works from above: sweeping, certain, slightly dramatic. "The structure has to be automatic by the time the question appears." "A smaller true story beats a bigger invented one." "This is how influence works inside a bank." Say it as advice instead: "It helps to have the structure down before the first question." Bolded sentences follow the same rule.

## 22. Say each point once, and teach the doing, not the system (October 14, 2026)

The founder on the STAR draft: "we've spent so much time explaining how banks score interviews, the research behind structured interviews... does a student really need all of that to learn how to give a better STAR answer?" And: "eight full sample answers, explanations after each, a table mapping 19 questions, and then another 'say this, don't say that' section... the student should get the meat of it quicker."

Two failures, one fix each:

- **Explaining the system.** How firms score, what the research says, why a method exists, how a process works behind the scenes. If the reader's goal is to do something (give an answer, apply, pass a test), the system gets two lines at most. The words go to the doing.
- **Repeating a point in several formats.** An example, then an explanation of the example, then a table, then a say/don't block, all landing the same lesson. Pick the one format that teaches it fastest. Three or four sample answers that each show something different beat eight that show the same shape. A short note after an example is fine only when it adds what the example doesn't show.

Also: no two sections with the same purpose. If section 1 explains why the Action matters and section 6 has a mistake about the Action, merge them.

## 23. Match the reader's level (October 14, 2026)

The founder: "The Accenture article goes into Managing Director salaries; for someone looking at an entry-level Analyst role, I don't think all of that is necessary."

Cover the reader's seat in detail. Anything above or beside it gets a line: "Consultants (two to three years in) earn about $X; pay rises from there." A full pay ladder, a senior career path or partner economics belongs in an article about those roles.

## 24. Keep examples in proportion (October 14, 2026)

The founder: "multiple pages going across the kitchen cabinet case doesn't make sense as this isn't the interview or how-to-break-in guide; we can keep it sure, but like 1 page."

A worked example illustrates the section it sits in. In a career or role guide, a practice case or sample answer runs about a page. In an article whose whole question is that example (a case interview guide, a sample-answers article), it can run longer. Size the example to the article's question, not to how much there is to say about it.

## Mechanical spot checks (run before docx build)

- Dashes: `grep -nE "—|–| - " drafts/{file}.md` should return nothing in body copy.
- Echo suspects: `grep -inE "which means|in other words|put simply|ultimately," drafts/{file}.md` and apply the delete test.
- Register words: `grep -inE "not just|dressed up|best-kept|at the end of the day|game.chang|crucial|navigate|landscape" drafts/{file}.md`
- Negatives: `grep -inE "\bI'm not\b|\bI am not\b|\bwe (don't|won't|can't)\b|this (guide|article) (won't|doesn't|isn't)" drafts/{file}.md` and cut every hit about the writer, WSG or the article.
- Unsupported opinions: `grep -inE "most (students|candidates|people) (get|make|fail|expect|think|walk|miss|underestimate)|catches people|people get wrong" drafts/{file}.md` and apply rule 15.
- Bio and stories in first person: `grep -inE "I went to|I was at|when I was|as a (former|McKinsey|banker)|my (classmate|friend|roommate|student)|I'm the founder" drafts/{file}.md`. Light first-person framing ("In this article, I lay out") is fine; bio, credentials and memories go.
- Headers: `grep -nE "^#{2,3} " drafts/{file}.md` and read them alone. Question headers end in "?"; numbered insight headers are short plain claims; everything else is descriptive.
- Say-it-out-loud suspects: `grep -inE "the headline|brochure|center of gravity|lobby|catches people|rattled|case clock|under a clock" drafts/{file}.md` and apply rule 9.
- Effort counts: `grep -nE "\b[0-9]{2,3} (practice )?(cases|flashcards|mocks|hours)" drafts/{file}.md`.
- Skim test: `grep -oE "\*\*[^*]+\*\*" drafts/{file}.md` and read the bolds top to bottom. Each is a full sentence (rule 14), and together they tell the argument.
- Length: `wc -w drafts/{file}.md` against the editorial plan's budget.
- Other field (rule 17): in a consulting article `grep -inE "bank|banker|goldman|jpmorgan|wall street" drafts/{file}.md`; in a banking article `grep -inE "consult|mckinsey|bcg|bain" drafts/{file}.md`. Every hit sits in the one comparison section the topic needs, or goes.
- History and trivia (rule 18): `grep -inE "history|historically|founded|in 1[0-9]{3}|earliest|first (woman|female|known)|renamed|reorganiz" drafts/{file}.md` and apply the deletion test.
- Firm-side why (rule 19): `grep -inE "firm's side|side of the table|exists to|is trying to|the reason (firms|the firm)|receives (roughly |about )?[0-9]" drafts/{file}.md`.
- Absolutes and narrator voice (rule 21): `grep -inE "\b(every|always|never|all|only|the number is|exactly|cover(s)? every|is scoring|are scoring|the interviewer (is|wants|hears)|what (banks|firms|recruiters) want)\b" drafts/{file}.md` and read each hit. Keep it if it's literally true; otherwise add the qualifier or say it as advice.
- Repetition (rule 22): list the article's key points and where each appears. Any point taught in two places or two formats keeps one.
- Level and proportion (rules 23 and 24): any table or section about levels above the reader's, and any example over about a page in a non-interview article, gets cut down.
- Section verdicts (rule 20): list every H2 with keep / cut / shrink / rewrite and one reason before the docx build.
- `python3 scripts/check_style.py drafts/{file}.md` still gates the build.

## Where these rules live

1. `style-guide/editorial-rules.md` Part 2 is the canonical copy.
2. The packaged wsg-article skill carries the same rules as its `prose-editing.md` module. Edit the repo copy first, then mirror into `.claude-skill/prose-editing.md` and repackage `skills/wsg-article.skill` and `skills/wsg-prose-editing.skill`.
