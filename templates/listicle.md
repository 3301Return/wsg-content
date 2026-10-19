# Listicle Template

**Use when:** Curated resource roundups, ranked lists, "top N" posts.
**Examples:** "Top 10 Sophomore Insights Programs for IB" · "10 Investment Banking Internships to Apply To in 2027" · "Top 10 Free Resources for Investment Banking Interview Questions in 2026"
**Length (October 14, 2026):** length follows the question. Focused pieces about 2,500 to 3,500 words; in-depth guides up to about 5,000 to 6,000 (20 to 25 pages). Write the editorial plan in SKILL.md first; its budget is the target.
**Required:** Exact count from headline · 1-2 H2 sub-questions phrased as the reader's exact question · Inline anchor-word hyperlinks · **Bolded lead-claim sentence + bolded concrete-takeaway sentence per item** (the skim narrative)

---

## TITLE
{Exact headline. Simple and direct: the count, the topic in search words, the year if it applies. "Top 10 Sophomore Insights Programs for IB."}

## META DESCRIPTION
{1-2 sentences, 150-160 chars, includes target keyword and the count}

## INTRODUCTION (one to three sentences)

Fast and to the point, then the list. Sentence one tells the reader what the list is or the one fact that frames it ("If you're applying to Investment Banking Summer Analyst programs in 2027, you're competing for Summer 2028 seats."). A bolded full sentence with a real number can follow ("Students who get into one of these programs are roughly 5 to 10 times more likely to convert into a Summer Analyst offer..."). Optionally one line on how the list is ordered. No story, no scene, no "most students."

## H2 SUB-QUESTIONS (1-2)

**{The reader's exact search question? e.g., "What is a sophomore insights program?"}**
{First sentence answers it directly. 2-4 sentences total.}

## BODY: NUMBERED LIST (SKIM-OPTIMIZED FORMAT)

Group items under plain H2s when the list has natural groups (Bulge Bracket / Elite Boutique / Boutique). Every item uses this pattern. Reading only the bolded sentences in order must tell the article's argument.

### Required structure per item

```
### N. [{Resource name}]({url})

**{Lead-claim sentence: what makes this distinct, who it's for, what trade-off it carries.}**

{One short paragraph, 2-3 sentences.}

- Website: {url or domain}
- Format: {short}
- Pricing / Cost: {short}
- Eligibility: {short}
- Best for: {short}
- Cons: {short, sourced from real reviews if available}

**Concrete takeaway: {one-sentence action: when to pick it, when to skip, what to pair with.}**
```

Notes:
- Field labels are not bolded. The lead claim and concrete takeaway carry the skim narrative.
- The lead claim is a complete sentence with a verb and, where possible, a fact.
- The concrete takeaway is actionable. "Buy WSP if your gap is modeling."
- For question-listicles, the answer walk-through under each item gets the room it needs, in plain words, step by step. Keep each answer to what the interviewer is testing; skip second worked examples.

## CONCLUSION (one short paragraph)

Tell the reader where to start. No recap of the list.

## ADDRESS WHAT'S NOT ON THE LIST

For "Top N" lists where well-known resources or firms don't appear, a short section on how to think about them. A paragraph, not a second list.

---

## Generation rules (for the skill)

- HARD RULE: count must match the headline exactly.
- HARD RULE: each item has a bolded lead-claim sentence and a bolded concrete-takeaway sentence. Run `python3 scripts/check_style.py drafts/{file}.md`.
- Every link is an inline anchor on the resource name.
- Calibrate on `samples/reference-articles.md` (Sophomore Insights, 2027 internships, free resources). Never on AI drafts.
- No em dashes or hyphens as structural punctuation in body copy.
- Run `.claude-skill/plain-language.md`, `.claude-skill/thorough-explanations.md` and `.claude-skill/prose-editing.md` before delivery, and check the length target.
