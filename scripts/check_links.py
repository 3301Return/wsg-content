#!/usr/bin/env python3
"""
WSG Link Verification
=====================

Extracts every Markdown link from an article and verifies each one:
- Reachable (HEAD or GET returns 2xx / 3xx)
- Not suspicious (cycle-specific year doesn't conflict with article time horizon,
  no rotating job-posting ID patterns)

Usage:
    python3 scripts/check_links.py drafts/{file}.md
    python3 scripts/check_links.py published/{file}.md
    python3 scripts/check_links.py drafts/*.md

Exit code 0 = all links pass. Exit code 1 = at least one link failed.

Dependencies:
    pip install requests --break-system-packages

If requests isn't available, the script falls back to urllib.
"""

import re
import sys
from pathlib import Path

try:
    import requests
    HAVE_REQUESTS = True
except ImportError:
    HAVE_REQUESTS = False
    import urllib.request
    import urllib.error

# Pattern matches: [text](url) and **[text](url)**
LINK_RX = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

# Patterns for suspicious / rotating job-posting URLs and unsafe ATS root URLs
SUSPICIOUS_PATTERNS = [
    (re.compile(r"gh_jid=\d+", re.IGNORECASE),
     "Greenhouse posting ID — rotates each cycle"),
    (re.compile(r"/job-detail/\d+/", re.IGNORECASE),
     "BofA-style numeric Job ID — rotates each cycle"),
    (re.compile(r"icims\.com/jobs/\d+/", re.IGNORECASE),
     "iCIMS specific posting — rotates each cycle"),
    (re.compile(r"/jobs/\d{9,}", re.IGNORECASE),
     "Numeric posting ID — likely rotates"),
    (re.compile(r"linkedin\.com/jobs/view/", re.IGNORECASE),
     "LinkedIn job posting — almost always rotates"),
    (re.compile(r"glassdoor\.com/job-listing/", re.IGNORECASE),
     "Glassdoor specific listing — rotates"),
    (re.compile(r"myworkdayjobs\.com/[^/]+/job/", re.IGNORECASE),
     "Workday specific posting — rotates"),
    (re.compile(r"jobs\.citi\.com/job/[^/]+/[^/]+/\d+/\d+", re.IGNORECASE),
     "Citi specific posting — rotates"),
    # ATS root URLs that 404 without a specific path
    (re.compile(r"^https?://[^/]*icims\.com/?$", re.IGNORECASE),
     "iCIMS portal root URL — usually 404s without a job path. Link to the firm's public careers page instead."),
    (re.compile(r"^https?://[^/]*myworkdayjobs\.com/[^/]+/?$", re.IGNORECASE),
     "Workday ATS root URL — usually 404s without a specific posting. Link to the firm's public careers page instead."),
]

USER_AGENT = "Mozilla/5.0 (compatible; WSGLinkCheck/1.0; +https://wallstreetguide.net)"


def parse_frontmatter_status(text):
    """Try to detect the article's time horizon from the headline."""
    m = re.search(r"^headline:\s*[\"']?(.+?)[\"']?\s*$", text, flags=re.MULTILINE)
    if not m:
        return None
    headline = m.group(1)
    years = re.findall(r"\b(20\d\d)\b", headline)
    return years[0] if years else None


def check_url(url, timeout=10):
    """Return (status_code_or_label, error_string)."""
    if HAVE_REQUESTS:
        try:
            r = requests.head(url, allow_redirects=True, timeout=timeout,
                              headers={"User-Agent": USER_AGENT})
            if r.status_code == 405 or r.status_code >= 500:
                # Some servers don't support HEAD; retry with GET
                r = requests.get(url, allow_redirects=True, timeout=timeout,
                                 headers={"User-Agent": USER_AGENT}, stream=True)
                r.close()
            return r.status_code, None
        except requests.exceptions.RequestException as e:
            return "UNREACHABLE", str(e).split("\n")[0][:120]
    else:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.getcode(), None
        except urllib.error.HTTPError as e:
            return e.code, None
        except Exception as e:
            return "UNREACHABLE", str(e).split("\n")[0][:120]


def is_suspicious(url, article_year):
    """Return list of (pattern_name, reason) tuples for any suspicious patterns."""
    flags = []
    for pat, reason in SUSPICIOUS_PATTERNS:
        if pat.search(url):
            flags.append(reason)
    # Year check: if URL contains a year and it's significantly different from the article year
    if article_year:
        url_years = re.findall(r"\b(20\d\d)\b", url)
        for uy in url_years:
            if int(uy) < int(article_year):
                flags.append(
                    f"URL contains year {uy} but article horizon is {article_year} — "
                    f"this URL may be for a past cycle and could rotate")
                break
    return flags


def extract_links(body):
    """Return list of (text, url) tuples. Skips local file links."""
    out = []
    for m in LINK_RX.finditer(body):
        text, url = m.group(1), m.group(2)
        if url.startswith("http://") or url.startswith("https://"):
            out.append((text, url))
    return out


def check_article(path):
    """Run link checks against one article. Return (pass_bool, lines)."""
    text = Path(path).read_text(encoding="utf-8")
    article_year = parse_frontmatter_status(text)

    # Strip frontmatter for link extraction
    body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)
    links = extract_links(body)

    if not links:
        return True, [f"=== {path} ===", "  (no http(s) links found)\n"]

    lines = [f"=== {path} ==="]
    if article_year:
        lines.append(f"  Article time horizon: {article_year}")
    lines.append(f"  Links found: {len(links)}\n")

    broken = []
    suspicious = []
    seen = set()

    for text_anchor, url in links:
        if url in seen:
            continue
        seen.add(url)

        # Suspicious check (synchronous, no network)
        flags = is_suspicious(url, article_year)

        # Reachability check (network — may take a moment)
        status, err = check_url(url)
        status_str = f"HTTP {status}" if isinstance(status, int) else status

        ok_status = isinstance(status, int) and 200 <= status < 400
        ok_suspicious = len(flags) == 0
        ok = ok_status and ok_suspicious

        marker = "OK " if ok else ("X  " if not ok_status else "?  ")
        line = f"  {marker}{status_str:>15}  {url}"
        if not ok_status:
            broken.append((url, status_str, err))
            line += f"\n        ERROR: {err}" if err else ""
        if flags:
            suspicious.append((url, flags))
            for f in flags:
                line += f"\n        SUSPICIOUS: {f}"
        lines.append(line)

    lines.append("")
    if not broken and not suspicious:
        lines.append(f"  PASS: {len(seen)} unique links, all reachable, none suspicious")
    else:
        if broken:
            lines.append(f"  X  {len(broken)} broken or unreachable link(s)")
        if suspicious:
            lines.append(f"  ?  {len(suspicious)} suspicious link(s) — review and consider replacing")
    return (not broken and not suspicious), lines


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/check_links.py <article-file.md> [more files...]")
        sys.exit(1)

    if not HAVE_REQUESTS:
        print("Note: requests not installed; falling back to urllib. "
              "For better results: pip install requests --break-system-packages\n")

    all_pass = True
    for path in sys.argv[1:]:
        if not Path(path).exists():
            print(f"File not found: {path}")
            all_pass = False
            continue
        ok, lines = check_article(path)
        for line in lines:
            print(line)
        print()
        if not ok:
            all_pass = False

    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
