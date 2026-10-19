# Niche Template

**Use when:** Firm/role posts, edge-case student situations, or honest reviews. The niche template flexes across all three sub-types.
**Examples:** "How to Break Into Evercore Restructuring" · "Breaking Into IB From a Junior Transfer at a Non-Target" · "Is Wall Street Prep Worth It? 4 Pros and Cons You Need to Know"
**Length (October 14, 2026):** length follows the question. Focused pieces about 2,500 to 3,500 words; in-depth guides up to about 5,000 to 6,000 (20 to 25 pages). Write the editorial plan in SKILL.md first; its budget is the target.
**Required:** Direct-answer intro · 1-2 H2 sub-questions · Heavy use of specifics (firm names, real numbers, named scenarios) · Anchored to a deep dive when one exists

---

## SUB-TYPE: pick one

**A. Firm/role deep dive** (e.g., "How to Break Into Evercore Restructuring")
- Body structure: What the firm/role is and does · Recruiting timeline & process · What they look for · How to network here · Interview prep

**B. Edge-case student** (e.g., "Breaking Into IB From a Non-Target as a Junior Transfer")
- Body structure: The two or three real obstacles · How to handle each · Realistic timeline · Who has done this before

**C. Honest review** (e.g., "Is Wall Street Prep Worth It")
- Body structure: What it is · Pros (specific) · Cons (specific) · Who should use it · Who should skip it · Cheaper or better alternatives

---

## TITLE
{Exact headline. Simple and direct.}

## META DESCRIPTION
{1-2 sentences, 150-160 chars. Make it concrete to win the click.}

## INTRODUCTION (two to five sentences)

Follow `.claude-skill/intros.md`. Sentence one says what the firm, situation or product is, or answers the title. A bolded full sentence with the most useful fact. Last sentence says what the article covers.

Reviews can open with plain first-person framing, as in Stephen's reference: "I get asked about Wall Street Prep a lot. Students want to know if it's worth the money, whether it'll actually help them get an offer, and whether there's something better they should be using instead." No bio, no story.

## H2 SUB-QUESTIONS (1-2)

**{The reader's exact long-tail question?}**
{First sentence answers it. 2-4 sentences total.}

## BODY (use the structure from your sub-type above)

### Section 1: {Plain descriptive header}

Lead with what makes this situation, firm or product different. Then specifics. If a `deep-dives/{topic}.md` exists, pull the names, processes and numbers that answer the reader's question.

### Section 2: {Plain descriptive header}

{Same pattern.}

## CONCLUSION (one short paragraph)

Tell the reader exactly what to do next given their situation. No recap, no "good luck with your journey."

---

## Generation rules (for the skill)

- BEFORE writing: check `deep-dives/` for a relevant guide.
- At least one named firm, real timeline, or concrete scenario per section.
- Reviews must include real cons.
- Calibrate on `samples/reference-articles.md` (the Wall Street Prep review and McKinsey Solve guide are the closest). Never on AI drafts.
- No em dashes or hyphens as structural punctuation.
- Write for the one specific reader; long-tail keywords are high-intent.
- Firm/role posts carry the most technical mechanics. Explain them in plain words at first use, one worked example per mechanism. Run `.claude-skill/plain-language.md`, `.claude-skill/thorough-explanations.md` and `.claude-skill/prose-editing.md` before delivery, and check the length target.
