# Listicle Template

**Use when:** Curated resource roundups, ranked lists, "top N" posts.
**Examples:** "Top 10 Free Resources for Investment Banking Interview Questions in 2026" · "10 Free Resources for Case Consulting Prep"
**Word count:** 1,800 to 2,200
**Required:** Exact count from headline · 1-2 H2 sub-questions · Inline anchor-word hyperlinks (not URL footers) · **Bolded lead-claim sentence + bolded concrete-takeaway sentence per item** (the skim narrative)

---

## TITLE
{Exact headline from content calendar}

## META DESCRIPTION
{1-2 sentences, 150-160 chars, includes target keyword and the count}

## INTRODUCTION (2-3 short paragraphs)

Open with the reader's pain or a contrarian observation about the category. Skip "in this article we will."

End with what the reader will leave with: "Here are the {N} resources I recommend, ranked by where they fit in your prep."

## H2 SUB-QUESTIONS (1-2)

**{Real search query the reader is also asking?}**
{2-4 sentence answer.}

## BODY: NUMBERED LIST (SKIM-OPTIMIZED FORMAT)

Per the June 2026 editorial review, every listicle item MUST use the three-element pattern below. The bolded lead-claim + bolded concrete-takeaway together form the skim narrative. Reading just the bolded sentences in order must tell the article's argument.

### Required structure per item

```
### N. [{Resource name}]({url})

**{Lead-claim sentence in one line: what makes this distinct, who it's for, what trade-off it carries.}**

- Website: {url or domain}
- Format: {short}
- Pricing / Cost: {short}
- Eligibility: {short}
- Best for: {short}
- Cons: {short — sourced from real reviews if available}

**Concrete takeaway: {one-sentence action — when to pick it, when to skip, what to pair with.}**
```

Notes on the structure:
- The bullet field labels (Website:, Format:, etc.) are NOT bolded in v3 onward. The lead claim and concrete takeaway carry the skim narrative.
- The lead claim must be a complete sentence with a verb. Not a label, not a fragment.
- The concrete takeaway must be actionable. Not "this is great." Yes "Buy WSP if your gap is modeling."

## CONCLUSION (1-2 paragraphs)

Tell the reader where to start. Share the principle behind the list.

## ADDRESS WHAT'S NOT ON THE LIST

For "Top N" lists where well-known resources or firms don't appear, include a short section explaining how to think about them. The reader will notice the gap and bounce if it isn't addressed.

---

## Generation rules (for the skill)

- HARD RULE: count must match the headline exactly.
- HARD RULE: each item has a bolded lead-claim sentence and a bolded concrete-takeaway sentence. Run `python3 scripts/check_style.py drafts/{file}.md` to verify before docx build.
- Every link must be an inline anchor on the resource name.
- Pull tone from at least one listicle sample in `samples/listicles/` (gold standard: PE Recruiters listicle).
- No em-dashes or hyphens as structural punctuation in body copy.
- Reading only the bolded sentences in order MUST tell the article's argument. Run the skim test.
