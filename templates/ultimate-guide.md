# Ultimate Guide Template

**Use when:** Insight-led guides on a major topic. The reader leaves with a clear picture and a process to follow.
**Examples:** "How Hard Is It to Get Into Investment Banking? 6 Things That Actually Matter" · "How to Beat McKinsey Solve: A Step-by-Step Guide"
**Length target:** about 5,000 to 6,000 words (about 20 to 25 pages in the built .docx before images). Shorter is fine when the topic is covered. Longer only when the topic truly needs it; say why in the Thoroughness Report.
**Required:** Direct-answer intro · 1-2 H2 sub-questions after the intro · 6-8 sections · conclusion with a next step

---

## TITLE
{Exact headline. Simple and direct, in the words a student searches. "How to Beat McKinsey Solve: A Step-by-Step Guide."}

## META DESCRIPTION
{1-2 sentences, 150-160 chars, includes target keyword naturally}

## INTRODUCTION (two to five sentences, one or two short paragraphs)

Follow `.claude-skill/intros.md`:

1. Sentence one says what the topic is or answers the headline's question. "McKinsey Solve is the gamified pre-interview assessment every McKinsey candidate has to pass before getting a case interview."
2. A bolded full sentence with the most useful fact (a number, a length, a rate).
3. Optional: one line of quick facts (format, timing, the main options).
4. Last sentence: what the article covers. "In this article, I lay out..." is fine.

No story, no scene, no opinion about what readers get wrong.

## H2 SUB-QUESTIONS (1-2)

**{The reader's exact search question? e.g., "How long does McKinsey Solve take and is it timed?"}**
{First sentence answers it directly. 2-4 sentences total. Concrete numbers where possible.}

## BODY: SECTIONS

Two kinds of section header:

- **Numbered insights** ("N things that matter" articles): a short plain claim that gives the takeaway. "1. Your school matters but probably not in the way you think." Under 12 words, ordinary words.
- **Explainer sections:** a plain description or a question. "How McKinsey Solve is scored." "What changed about Solve in 2026."

### 1. {Short plain claim, e.g., "Your GPA is a filter, not a scorecard"}

Pattern:
- Sentence 1-2: the claim, said plainly
- Sentence 3-5: the proof (named scenario, real number, a firm's own statement)
- Sentence 6-8: what to do, with a timeline

**{One bolded full sentence that carries the section's point, with a fact in it.}**

### 2. {Next}
{Same pattern.}

{6-8 sections total. Cut any that repeat an earlier one or that the reader didn't come for.}

## CONCLUSION (one short paragraph)

Give the reader the next step. Don't summarize the article.

If a CTA fits naturally, include it. Default to none.

---

## Generation rules (for the skill)

- Calibrate on `samples/reference-articles.md` (How Hard Is It, McKinsey Solve). Never on AI drafts.
- If a relevant `deep-dives/{topic}.md` exists, read it first and pull only what answers the article's question.
- Every section includes at least one specific (named firm, real number, named scenario).
- Bold full sentences only.
- No em dashes or hyphens as structural punctuation.
- Use the target keyword in: H1, meta, first sentence, at least 2 H2s, naturally throughout.
- Technical mechanisms get walked step by step in plain words, with one worked example per mechanism. Run `.claude-skill/plain-language.md`, `.claude-skill/thorough-explanations.md` and `.claude-skill/prose-editing.md` before delivery, and check the length target.
