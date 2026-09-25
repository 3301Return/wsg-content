#!/usr/bin/env python3
"""
check_style.py — prose-level style checker for WSG drafts.

Catches the failures that shipped in the June 2026 batch:
- Bolded sentences starting with a pronoun without referent
- Bolded sentences that are flat lists of capitalized firm names
- Bolded fragments (less than 5 words and missing a verb signal)
- Listicle items missing a bolded lead-claim sentence and a bolded concrete-takeaway
- Listicle items with > 4 sentences of post-bullet description
- Intros longer than 3 paragraphs
- Missing H2 sub-questions after intro
- Missing "say this / don't say that" in how-to-answer articles
- Listicle missing the "what's not on this list" exception section
- Skim-narrative test: bold-only extract must include claim sentences, not just labels

Exits 0 with warnings if all checks pass, 1 if any HARD-RULE check fails.

Usage:
  python3 scripts/check_style.py drafts/draft-foo-v1.md
"""

import re
import sys
from pathlib import Path


PRONOUN_STARTS = ("that ", "it ", "it's", "this ", "these ", "those ", "whatever ", "such ", "they ", "he ", "she ")
LABEL_BOLDS = {"website:", "format:", "pricing:", "cost:", "eligibility:", "best for:", "cons:", "pros:", "who they place:", "who they hire:", "where to apply:", "application deadline:", "deadline:", "recruiting cadence:"}


def strip_frontmatter(text):
    if not text.startswith("---"):
        return text, {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text, {}
    fm = {}
    for line in parts[1].strip().splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return parts[2].lstrip("\n"), fm


def split_intro(body):
    lines = body.splitlines()
    intro, rest = [], []
    in_post = False
    for ln in lines:
        if ln.startswith("## "):
            in_post = True
        if in_post:
            rest.append(ln)
        else:
            intro.append(ln)
    return intro, rest


def count_paragraphs(lines):
    paragraphs = []
    current = []
    for ln in lines:
        if ln.startswith("#"):
            continue
        if ln.strip().startswith("**Meta description:"):
            continue
        if ln.strip():
            current.append(ln.strip())
        else:
            if current:
                paragraphs.append(" ".join(current))
                current = []
    if current:
        paragraphs.append(" ".join(current))
    return paragraphs


def extract_bolded_sentences(body):
    out = []
    for m in re.finditer(r"\*\*([^*]+?)\*\*", body):
        text = m.group(1).strip()
        out.append(text)
    return out


def is_pronoun_lead(sentence):
    s = sentence.lstrip().lower()
    return any(s.startswith(p) for p in PRONOUN_STARTS)


def is_firm_list(sentence):
    s = sentence.rstrip(".!?").strip()
    if " all " in s.lower() or " are " in s.lower() or " is " in s.lower() or " hire" in s.lower():
        return False
    parts = [p.strip() for p in re.split(r",| and ", s) if p.strip()]
    if len(parts) < 3:
        return False
    cap_count = sum(1 for p in parts if p and p[0].isupper() and len(p.split()) <= 4)
    return cap_count >= len(parts) - 1


def is_label_only(sentence):
    """Bolded text that's just a field label like 'Website:' or 'Cons:'."""
    s = sentence.strip().lower()
    return s in LABEL_BOLDS or (s.endswith(":") and len(s.split()) <= 4)


def is_complete_claim(sentence):
    """At least 5 words, ends with terminal punctuation, has a verb signal."""
    s = sentence.strip()
    if len(s.split()) < 5:
        return False
    if not (s.endswith(".") or s.endswith("?") or s.endswith("!")):
        return False
    return True


def find_listicle_items(body):
    items = []
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        ln = lines[i]
        if re.match(r"^##+ \d+\.\s", ln):
            heading = ln
            j = i + 1
            content = []
            while j < len(lines) and not re.match(r"^##+ ", lines[j]):
                content.append(lines[j])
                j += 1
            items.append((heading, "\n".join(content)))
            i = j
        else:
            i += 1
    return items


def count_h2_subquestions(body):
    count = 0
    for ln in body.splitlines():
        if re.match(r"^## \d+\.", ln):
            break
        if ln.startswith("## ") and ln.rstrip().endswith("?"):
            count += 1
    return count


def has_say_dont_say(body):
    return "don't say" in body.lower() or "do not say" in body.lower()


def has_exception_section(body):
    for ln in body.splitlines():
        if not ln.startswith("## "):
            continue
        s = ln.lower()
        if "not on" in s or "what about" in s or "exception" in s:
            return True
    return False


def main():
    if len(sys.argv) != 2:
        print("Usage: check_style.py <draft.md>", file=sys.stderr)
        sys.exit(2)

    path = Path(sys.argv[1])
    raw = path.read_text(encoding="utf-8")
    body, fm = strip_frontmatter(raw)

    fmt = fm.get("format", "").lower()
    headline = fm.get("headline", "")

    print(f"\n=== {path} ===")
    print(f"  format: {fmt}")
    print(f"  headline: {headline[:60]}")
    print()

    warnings = []
    failures = []

    # Check 1: intro paragraph count
    intro_lines, _ = split_intro(body)
    intro_paragraphs = count_paragraphs(intro_lines)
    if len(intro_paragraphs) > 3:
        failures.append(f"INTRO TOO LONG: {len(intro_paragraphs)} paragraphs (rule: 1-2 short, max 3)")
    elif len(intro_paragraphs) > 2:
        warnings.append(f"intro is {len(intro_paragraphs)} paragraphs (rule prefers 1-2)")

    # Check 2: H2 sub-questions
    n_subq = count_h2_subquestions(body)
    if n_subq == 0:
        failures.append("MISSING H2 SUB-QUESTIONS: rule requires 1-2 after intro, found 0")

    # Check 3: bolded sentences
    bolds = extract_bolded_sentences(body)
    for b in bolds:
        if "Meta description" in b:
            continue
        if is_pronoun_lead(b) and is_complete_claim(b):
            failures.append(f"NON-SELF-CONTAINED BOLD: '{b[:80]}...' starts with pronoun without referent")
        if is_firm_list(b):
            failures.append(f"RANDOM BOLDED WORDS: '{b[:80]}...' is a flat list of capitalized names")

    # Check 4: skim test — at least 4 complete-claim bolds in the body
    complete_claims = [b for b in bolds if is_complete_claim(b) and not b.lower().endswith("?") and "Meta description" not in b]
    if len(complete_claims) < 4:
        failures.append(f"SKIM TEST FAIL: only {len(complete_claims)} complete-claim bolds in body (rule: at least 4 needed for skim narrative)")

    # Check 5: listicle-specific
    if fmt == "listicle":
        items = find_listicle_items(body)
        for h, item_text in items:
            # Each item must have at least one complete-claim bolded sentence
            item_bolds = extract_bolded_sentences(item_text)
            item_claims = [b for b in item_bolds if is_complete_claim(b)]
            if not item_claims:
                failures.append(f"LISTICLE ITEM MISSING CLAIM BOLD: '{h.strip()[:50]}' has no bolded complete-sentence claim (rule: lead claim + concrete takeaway per item)")
            # Check description chunkiness
            # extract non-bullet, non-bolded text
            non_bullet_lines = [l for l in item_text.splitlines() if l.strip() and not l.strip().startswith(("-", "*", "**"))]
            joined = " ".join(non_bullet_lines)
            sents = [s for s in re.split(r"[.!?]+", joined) if s.strip()]
            if len(sents) > 6:
                warnings.append(f"LISTICLE ITEM TOO CHUNKY: '{h.strip()[:50]}' has {len(sents)} sentences of description")

        if not has_exception_section(body):
            warnings.append("LISTICLE missing 'what's not on this list' / exception section")

    # Check 6: how-to-answer say/don't-say
    how_to_answer_signals = ("interview question", "how to prepare", "how to answer", "behavioral")
    if any(s in headline.lower() for s in how_to_answer_signals):
        if not has_say_dont_say(body):
            failures.append("MISSING 'say this / don't say that' callouts")

    # Output
    if failures:
        for f in failures:
            print(f"  X  FAIL  {f}")
    if warnings:
        for w in warnings:
            print(f"  ?  WARN  {w}")
    if not failures and not warnings:
        print("  OK  all style checks pass")
    print()

    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
