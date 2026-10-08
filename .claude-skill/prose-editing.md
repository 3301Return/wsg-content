---
name: wsg-prose-editing
description: Prose-level editing rules for WallStreetGuide (WSG) articles from the July 2026 editorial review, the September "say it out loud" test, and the October 2026 founder and Stephen reviews (plain and signposted headers, question headers, full-sentence bolds, no unsupported opinions, length target). Use when writing, editing, or reviewing WSG articles or any draft that should not read as AI-written. Trigger on requests to cut AI tells, remove echo sentences or em-dashes, humanize a draft, shorten a draft, improve sentence variety, fix odd or off-register wording, or apply burstiness and perplexity principles.
---

# WSG Prose Editing

Pruning and variance rules from the July 2026 editorial review, extended in September and October 2026. They layer on top of the WSG style guide when working in the WSG repo, and stand alone for any other prose. They tell you what to cut and how to vary. The WSG format itself (bolded skim narrative, H2 sub-questions, say/don't blocks) stays as specified in the main skill.

Canonical repo copy: `style-guide/editorial-rules.md` Part 2. This module is the packaged mirror so the rules travel with the skill; edit the repo copy first, then re-mirror here and repackage.

Source: the July 12, 2026 edit pass on the consulting cover letter draft, the August 27 founder review, the October 7 founder review, and Stephen's October 8 reference list. Every existing rule in `style-guide/style-guide.md` and `style-guide/editorial-rules.md` Part 1 still applies.

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

Stephen flagged the Sophomore Insights opener as the model: the bolded line is a complete sentence with a concrete number in it ("roughly 5 to 10 times more likely to convert into a Summer Analyst offer"). Bold a sentence that would still make sense pasted alone, carries a fact or a clear rule, and is the one thing a skimmer should take from that section. Never bold a fragment, a label, or a sentence that only sets up the next one.

## 15. No unsupported opinions about what people get wrong (October 8, 2026)

Stephen's criticism of the Casey opener: "weirdly opinionated about what people get wrong without showing evidence." Cut sentences that claim what "most candidates" think, expect, miss or get wrong unless the next sentence gives the evidence (a survey, a firm's own statement, a number). If there's no evidence, state the fact the reader needs instead: what the test is, how long it takes, how it's scored.

## 16. Length: cut to the target (October 8, 2026)

Sanskar's note: recent drafts run about 35 pages without images. The target is about 20 to 25 pages (roughly 4,500 to 6,000 words at WSG .docx spacing; SKILL.md has the details). Over is fine when the topic truly needs it, but the default is to land in range. Cut in this order, before touching any explanation step:

1. Echo enders and recaps (rule 1). A closing section never re-summarizes the article.
2. Second and third worked examples of the same mechanism. Keep the best one and give the follow-ups as one or two sentences.
3. Tables that repeat what the prose already said, and prose that repeats a table.
4. "Honest read," "what this means for you" and "the trade-off" sections that restate earlier sections.
5. Background the reader didn't come for (founding history, long firm lists, every deal in a year).
6. Say/don't blocks beyond four or five.

Never cut a step from an explanation to hit the number (`thorough-explanations.md`). Cut repetition and side material instead.

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
- Length: `wc -w drafts/{file}.md` against the SKILL.md target.
- `python3 scripts/check_style.py drafts/{file}.md` still gates the build.

## Where these rules live

1. `style-guide/editorial-rules.md` Part 2 is the canonical copy.
2. The packaged wsg-article skill carries the same rules as its `prose-editing.md` module. Edit the repo copy first, then mirror into `.claude-skill/prose-editing.md` and repackage `skills/wsg-article.skill` and `skills/wsg-prose-editing.skill`.
