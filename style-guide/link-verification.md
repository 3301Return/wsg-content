# Link Verification Protocol (mandatory before any article ships)

**The rule:** every URL in a WSG article must point to a page that exists, works today, and is appropriate for the article's time horizon. If a link is broken, speculative, or points to content that doesn't exist yet, remove it. **Better to have no link than a wrong one.**

A wrong link looks worse than a missing link. It signals the writer didn't actually click through. It also frustrates the reader, who came for specifics and got a 404.

## What counts as a "wrong" link

Three categories to catch:

### 1. Dead links (broken at time of writing)

The URL 404s, redirects to an unrelated page, or has been renamed and not updated. The writer is responsible for actually clicking each link in the draft and confirming it loads what they expect.

### 2. Rotating job-posting URLs

Examples: specific Job IDs on BofA careers (`/job-detail/13953/`), specific Greenhouse posting IDs (`/jobs/4621009006`), specific iCIMS postings (`/jobs/9024/`), Citi `89623967312`-style numeric posting IDs. **These rotate every cycle.** A URL that works today for "Bank of America 2027 Global IB SA Job ID 13953" will 404 after the 2027 cycle closes.

**Rule:** never link to a cycle-specific job posting unless the article is going to be published and read within the same active cycle. For forward-looking articles (e.g., "10 IB Internships to Apply To in 2027" written in 2026), link to the firm's evergreen careers landing page, not the rotating job-posting URL.

### 3. Speculative URLs

URLs to pages that don't exist yet. Examples: "Goldman Sachs 2028 Summer Analyst Program" page when the 2028 cycle hasn't opened. "Citi Spring 2027 Early ID cohort posting" before that cohort is announced. **Never invent a URL or guess what the firm will use next cycle.**

**Rule:** if the specific page doesn't exist yet, link to the firm's evergreen careers landing page and describe in the article body when the specific page will appear.

## What counts as a "safe" link

- Firm root career page: `https://www.goldmansachs.com/careers/students`
- Firm program-tier landing page that exists across cycles: `https://www.bvp.com/analyst-program`
- Permanent reference docs: `https://docs.claude.com/...`
- Wikipedia, news articles, and other stable third-party sources

The test: would this link still work in 18 months if the firm changes its cycle naming or rotates job postings? If yes, it's safe. If no, replace.

## Verification before delivery (mandatory)

Before a draft moves from `drafts/` to `published/`, run the link checker:

```bash
python3 scripts/check_links.py drafts/{file}.md
```

The script extracts every Markdown link, attempts a HEAD request on each, and reports:
- Working (200 / 301 / 302 to expected destination)
- Broken (404 / 410 / 500)
- Unreachable (timeout, DNS error)
- Suspicious (URL contains a cycle-specific year that doesn't match the article's time horizon, or contains numeric posting IDs)

**Address every flagged link before publishing.** Either fix the URL, replace with an evergreen alternative, or remove the link entirely and keep the text un-hyperlinked.

## Specific patterns to flag manually

The script will catch most cases. These edge cases need a human eye:

- Links to Wall Street Oasis forum posts (often rotate or get deleted)
- Links to Medium / Substack articles (authors sometimes pull posts)
- Links to specific deal-news WSJ / Bloomberg articles (paywall changes)
- Links to LinkedIn job postings (almost always rotate)
- Links to specific Glassdoor pages (rotate)

For all of these, prefer linking to the firm/publication root over the specific page when the article will be read across multiple months.

## If a link cannot be verified at all

Default to no link. Drop the anchor and leave the text un-linked. A sentence like "submit to William Blair's careers page" without a hyperlink is a better outcome than a hyperlinked phrase that 404s when clicked.

## Common patterns we use safely

These domains and URL patterns are evergreen and safe to link without further verification (unless they 404):

- `goldmansachs.com/careers/students` — general students page
- `careers.jpmorgan.com` — careers root
- `jobs.citi.com` — early careers root
- `careers.bankofamerica.com/en-us/students` — students root
- `williamblair.com/Careers` — careers root
- `bvp.com/analyst-program` and `bvp.com/bessemer-fellows` — program landing pages
- `info.insightpartners.com/Summer-Analyst-Program.html` — program landing page
- `dormroomfund.com` — root
- `contrary.com` — root
- `evercore.com/careers/students-graduates/students-graduates-u-s/` — students page
- `moelis.com/careers/` — careers root
- `jefferies.com/careers/students-and-graduates/` — students root
- `hl.wd1.myworkdayjobs.com/Campus` — campus Workday root (evergreen URL even if specific postings rotate)
- `lazard.com/careers/students/` — students root
- `centerviewpartners.com/careers.aspx` — careers root
- `lincolninternational.com/campus-early-careers/` — campus root

These are unsafe and almost always need replacement:

- Any URL with `gh_jid=` (Greenhouse posting ID — rotates)
- Any URL with `Job-ID` or `/job-detail/{number}/` (rotates)
- Any URL ending in `/jobs/{number}` (rotates)
- Citi `jobs.citi.com/job/.../{numeric-id}` posting URLs
- Stifel `careers-stifel.icims.com/jobs/{number}/.../job` postings
- Specific Workday posting URLs ending in `R{number}` (rotate)
- Specific BofA Job IDs (e.g., `13953`)

## When the article is for the current cycle

If an article is genuinely about the cycle that's open right now (e.g., "10 IB Internships to Apply To in 2026" published May 2026, reading audience is sophomores applying *right now* in May 2026), specific cycle URLs are acceptable because the reader will click them within the same active window. Even so, prefer general landing pages where possible — they remain useful after the cycle closes and the article keeps ranking on SEO long-tail.

## Output of a clean link audit

A passing audit returns:

```
✓ 12 links checked
✓ 12 reachable
✓ 0 suspicious (cycle-specific patterns)
PASS
```

A failing audit lists each broken link, what's wrong with it, and a suggested replacement.
