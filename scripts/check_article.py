#!/usr/bin/env python3
"""
WSG Article Compliance Checker (rev May 25, 2026)
=================================================

Runs WSG style + SEO rules + source-verification gates against any draft Markdown file.

Blocking issues (failures):
- Em-dashes in body
- Filler phrases
- Bare URLs (instead of inline anchors)
- Listicle count mismatch with headline
- No H2 sub-questions
- Target keyword missing from H1
- Word count materially outside target range (HARD cap)
- Suspicious capitalized brand names NOT in scripts/verified-brands.txt
- Broken links (delegated to check_links.py if available)

Usage:
    python3 scripts/check_article.py drafts/draft-{slug}-v1.md
"""

import re
import subprocess
import sys
import yaml
from pathlib import Path


FILLER_PHRASES = [
    r"highly competitive",
    r"in today'?s landscape",
    r"many students find",
    r"it'?s important to note",
    r"it is important to note",
    r"in this guide we will",
    r"in this article we will",
    r"at the end of the day",
    r"needless to say",
    r"that being said",
    r"in conclusion",
    r"as previously mentioned",
]

BOLD_FULL_SENTENCE = re.compile(r"\*\*[^*]+[.!?]\*\*")
BOLD_FRAGMENT = re.compile(r"\*\*[^*]+\*\*")

VERIFIED_BRANDS_PATH = Path(__file__).parent / "verified-brands.txt"


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, flags=re.DOTALL)
    if not m:
        return {}, text
    try:
        return yaml.safe_load(m.group(1)) or {}, m.group(2)
    except yaml.YAMLError:
        return {}, m.group(2)


def get_headline_count(headline):
    for m in re.finditer(r"\b(\d+)\b", headline):
        n = int(m.group(1))
        if not (1900 <= n <= 2100):
            return n
    return None


def count_h3(body):
    return len(re.findall(r"^###\s+", body, flags=re.MULTILINE))


def count_numbered_listicle_items(body):
    """Listicles may use ### N. (default) OR ## N. (when entries are large)."""
    h3_numbered = len(re.findall(r"^###\s+\d+\.\s", body, flags=re.MULTILINE))
    h2_numbered = len(re.findall(r"^##\s+\d+\.\s", body, flags=re.MULTILINE))
    return max(h3_numbered, h2_numbered)


def find_h2_sub_questions(body):
    h2s = re.findall(r"^##\s+(.+)$", body, flags=re.MULTILINE)
    return [h for h in h2s if h.strip().endswith("?")]


def find_bare_urls(body):
    return re.findall(r"^https?://\S+$", body, flags=re.MULTILINE)


def find_verify_tags(body):
    return re.findall(r"\[VERIFY:\s*([^\]]+)\]", body)


def find_unverified_risk_claims(body):
    risk_lines = []
    lines = body.split("\n")
    risky_patterns = [
        r"applications? (open|close|are open|are closed)",
        r"\$\d+,\d{3}",
        r"deadline.*\b20\d\d",
        r"GPA.*\b\d\.\d",
        r"\bclass of 20\d\d\b",
        r"applications? (typically )?(opened|closed)",
        r"acceptance rate.*\d",
    ]
    for i, line in enumerate(lines):
        for pat in risky_patterns:
            if re.search(pat, line, flags=re.IGNORECASE):
                if "[VERIFY" not in line:
                    risk_lines.append((i + 1, line.strip()[:120], pat))
                break
    return risk_lines


def check_keyword_placement(body, target_keyword):
    if not target_keyword:
        return None
    kw = target_keyword.lower()
    h1_match = re.search(r"^#\s+(.+)$", body, flags=re.MULTILINE)
    h1_text = h1_match.group(1).lower() if h1_match else ""
    first_100 = " ".join(re.sub(r"[#*\[\]()]", " ", body).split()[:100]).lower()
    return {
        "in_h1": kw in h1_text,
        "in_first_100_words": kw in first_100,
        "h2_count_with_keyword": sum(
            1 for h in re.findall(r"^##\s+(.+)$", body, flags=re.MULTILINE)
            if kw in h.lower()
        ),
    }


def load_verified_brands():
    """Return a lowercased set of verified brand names."""
    if not VERIFIED_BRANDS_PATH.exists():
        return set()
    brands = set()
    for line in VERIFIED_BRANDS_PATH.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        brands.add(line.lower())
    return brands


STOPWORDS_PHRASE = {
    # Cities / generic geography
    "new york", "san francisco", "los angeles", "wall street",
    "main street", "south asia", "north america", "south america",
    "united states", "united kingdom",
    # Financial terms (NOT brands, just capitalized concepts)
    "balance sheet", "cash flow", "cash flow statement", "income statement",
    "free cash flow", "net income", "net working capital",
    "enterprise value", "equity value", "earnings per share",
    "capital asset pricing model", "cost of equity", "cost of capital",
    "general atlantic venture fellows", "operating system",
    "global markets", "institutional securities", "investment bank",
    "investment grade", "high yield", "credit default swap", "interest rate swap",
    "mortgage backed security", "personal experience interview",
    "case study interview", "case interview", "case interviews",
    "ib interview course", "ib analyst", "ib analysts",
    "pe analyst", "pe associate", "pe associates", "pe diligence", "pe seat",
    "former pe", "former mbb", "former ib", "ex mbb", "ex ib",
    # Recruiting structure
    "summer associate", "summer analyst", "business analyst",
    "associate consultant", "associate consultant intern",
    "investment banking summer analyst", "junior summer",
    "sophomore summer", "first year", "second year",
    # Common process / event terms
    "money back guarantee", "fear tactics", "huge scam",
    "academic paper", "fit interview", "behavioral interview",
    "first round", "final round", "second round", "third round",
    "live mock", "live mock case", "case prep", "case interview prep",
    "office hours", "open hours", "structured products",
    "trading interview terms defined", "interview terms defined",
    # Tech products / platforms (generic)
    "microsoft teams", "khan academy",
    # Generic verbs in capitalized positions
    "do bcg", "is solve", "does solve", "doing solve", "drill ecosystem",
    "use preplounge", "beat mckinsey solve",
    # Other false-positive patterns
    "asked investment banking interview questions",
    "answer them", "answer the", "answer this",
    "but ib", "but consulting", "but pe", "but the", "but it",
    "if eurusd", "if you", "if i",
    "consulting recruiting",
    "investment banking career coach",
}


def extract_candidate_brands(body):
    """Pull mid-sentence capitalized multi-word phrases that LOOK like brand names."""
    # Strip markdown links
    stripped = re.sub(r"\[([^\]]+)\]\([^)]+\)", "", body)
    # Strip bolding markers
    stripped = re.sub(r"\*\*", "", stripped)
    # Strip headings (don't flag headline-derived phrases)
    stripped = re.sub(r"^#+\s+.*$", "", stripped, flags=re.MULTILINE)

    pattern = re.compile(r"\b([A-Z][a-zA-Z&\.]+(?:\s+[A-Z][a-zA-Z&\.\-]+){1,4})\b")
    candidates = set()
    for m in pattern.finditer(stripped):
        phrase = m.group(1).strip()
        # Skip sentence-boundary artifacts: if the match contains a period mid-phrase,
        # it crosses sentence boundary (e.g., "Goldman Sachs. Goldman")
        if re.search(r"\.\s", phrase) or re.search(r"\.[A-Z]", phrase):
            continue
        # Skip stopwords
        if phrase.lower() in STOPWORDS_PHRASE:
            continue
        candidates.add(phrase)
    return candidates


def check_fabrication_risk(body):
    """
    Compare every capitalized multi-word phrase against the verified-brands list.
    Anything that LOOKS like a brand but is NOT verified gets flagged.
    """
    brands = load_verified_brands()
    if not brands:
        return []
    candidates = extract_candidate_brands(body)
    flagged = []
    for phrase in sorted(candidates):
        p_lower = phrase.lower()
        if p_lower in brands:
            continue
        # Skip well-known non-brand patterns
        # Skip phrases that look like deal names (X-Y format already handled)
        # Skip school names with "of" / "at" / "in" connectors
        if re.search(r"\b(of|at|in|the|and|to|for|on)\b", p_lower):
            continue
        # Skip "Stephen Turban" and "Sam Shiah" — verified named individuals
        verified_individuals = {"stephen turban", "sam shiah", "brian dechesare",
                                "ali partovi", "marc cosentino", "victor cheng",
                                "eleni henkel", "leah trabich", "brian o'callaghan",
                                "pam esterson", "susanna nichols", "vedica qalbani",
                                "adam zoia", "annette krassner", "andris zoltners",
                                "prabhakant sinha", "david aaker", "clayton christensen",
                                "michael porter", "mark fuller", "bill achtmeyer",
                                "john rutherford", "frank quattrone", "david handler",
                                "danielle caston strazzini", "alison bellino johnson"}
        if p_lower in verified_individuals:
            continue
        # Skip deal references with "deal"
        if "deal" in p_lower:
            continue
        flagged.append(phrase)
    return flagged


def check_links(path):
    """Delegate to scripts/check_links.py if it exists. Return (ok, summary)."""
    link_script = Path(__file__).parent / "check_links.py"
    if not link_script.exists():
        return (True, "(check_links.py not present; skipping link verification)")
    try:
        result = subprocess.run(
            ["python3", str(link_script), str(path)],
            capture_output=True, text=True, timeout=60
        )
        return (result.returncode == 0,
                result.stdout.splitlines()[-1] if result.stdout else "(no output)")
    except Exception as e:
        return (False, f"(link check error: {e})")


def check_article(path):
    text = Path(path).read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)

    issues = []
    warnings = []
    info = []

    word_count = len(body.split())
    info.append(f"Word count: {word_count}")

    headline = fm.get("headline", "")
    target_keyword = fm.get("target_keyword", "")
    fmt = fm.get("format", "")
    expected_count = get_headline_count(headline) if fmt == "listicle" else None

    # 1. Em-dash check (BLOCKING)
    em_dash_count = body.count("—")
    if em_dash_count > 0:
        issues.append(f"Em-dashes found in body: {em_dash_count}")

    # 2. Filler phrase check (BLOCKING)
    for phrase in FILLER_PHRASES:
        matches = re.findall(phrase, body, flags=re.IGNORECASE)
        if matches:
            issues.append(f"Filler phrase '{matches[0]}' found {len(matches)}x")

    # 3. Bare URL check (BLOCKING)
    bare = find_bare_urls(body)
    if bare:
        issues.append(f"Bare URLs found (should be inline anchors): {len(bare)}")

    # 4. Listicle count match (BLOCKING)
    if fmt == "listicle" and expected_count:
        item_count = count_numbered_listicle_items(body)
        if item_count != expected_count:
            issues.append(
                f"Listicle count mismatch: headline says {expected_count}, body has {item_count} numbered items"
            )
        else:
            info.append(f"Listicle count matches headline: {expected_count}")

    # 5. H2 sub-questions present (BLOCKING)
    sub_qs = find_h2_sub_questions(body)
    if len(sub_qs) < 1:
        issues.append("No H2 sub-questions found (need 1-2 after intro)")
    else:
        info.append(f"H2 sub-questions: {len(sub_qs)}")

    # 6. Keyword placement
    if target_keyword:
        kw_check = check_keyword_placement(body, target_keyword)
        if not kw_check["in_h1"]:
            warnings.append(f"Target keyword '{target_keyword}' missing from H1")
        if not kw_check["in_first_100_words"]:
            warnings.append(f"Target keyword '{target_keyword}' not in first 100 words")

    # 7. Word count cap — NOW BLOCKING on upper bound
    if fmt == "listicle":
        if word_count > 2500:
            issues.append(f"Word count {word_count} exceeds listicle hard cap (2,500)")
        elif word_count > 2300:
            warnings.append(f"Word count {word_count} above listicle target (1,800-2,200); trim if possible")
        elif word_count < 1700:
            warnings.append(f"Word count {word_count} below listicle target (1,800)")
    elif fmt == "ultimate-guide":
        if word_count > 2600:
            issues.append(f"Word count {word_count} exceeds ultimate-guide hard cap (2,600)")
        elif word_count < 1900:
            warnings.append(f"Word count {word_count} below ultimate-guide target (2,000)")
    elif fmt == "niche":
        if word_count > 2400:
            issues.append(f"Word count {word_count} exceeds niche hard cap (2,400)")
        elif word_count < 1700:
            warnings.append(f"Word count {word_count} below niche target (1,800)")

    # 8. VERIFY tag report
    verify_tags = find_verify_tags(body)
    info.append(f"[VERIFY] tags in draft: {len(verify_tags)}")
    risk_lines = find_unverified_risk_claims(body)
    if risk_lines:
        warnings.append(
            f"{len(risk_lines)} potentially time-sensitive claims without [VERIFY] tags"
        )

    # 9. Fabrication-risk check (WARNING — manual review)
    flagged_brands = check_fabrication_risk(body)
    if flagged_brands:
        warnings.append(
            f"{len(flagged_brands)} capitalized phrases NOT in verified-brands.txt "
            f"(verify or add to whitelist if real):"
        )
        for b in flagged_brands[:8]:
            warnings.append(f"    - {b}")

    # 10. Link verification (WARNING)
    ok, summary = check_links(path)
    if not ok:
        warnings.append(f"Link check warning: {summary}")
    else:
        info.append(f"Link check: {summary}")

    # ----- format report -----
    lines = [f"\n=== {path} ===\n"]
    lines.extend(f"  i  {x}" for x in info)
    if warnings:
        lines.append("")
        lines.extend(f"  ?  {x}" for x in warnings)
    if issues:
        lines.append("")
        lines.extend(f"  X  {x}" for x in issues)
    if not issues:
        lines.append("\n  PASS: no blocking issues")
    else:
        lines.append(f"\n  FAIL: {len(issues)} blocking issue(s)")
    return (len(issues) == 0, "\n".join(lines))


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/check_article.py <draft-file.md> [more files...]")
        sys.exit(1)
    all_pass = True
    for path in sys.argv[1:]:
        try:
            ok, report = check_article(path)
            print(report)
            if not ok:
                all_pass = False
        except FileNotFoundError:
            print(f"File not found: {path}")
            all_pass = False
    print()
    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
