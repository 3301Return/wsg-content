# WSG SEO Checklist

Run before delivering any draft. The skill walks through this automatically — but you can run it manually on any post.

## On-page SEO

- [ ] H1 contains the exact target keyword
- [ ] Meta description is 150-160 characters and includes the target keyword naturally
- [ ] Target keyword appears in the first 100 words
- [ ] Target keyword appears in at least 2 H2 headings
- [ ] At least 1-2 H2 sub-questions reflect real search queries (for AI summaries / featured snippets)
- [ ] Secondary keywords are woven in naturally — never stuffed
- [ ] Word count is in the 1,800-2,500 range (no padding to hit a target)

## Structure

- [ ] H2/H3 hierarchy is clean — no skipped levels
- [ ] Intro is 2-4 short paragraphs (not one wall of text)
- [ ] List items in listicles match the count in the headline exactly
- [ ] Conclusion does not summarize — it pushes to the next step

## Links

- [ ] All external links are inline anchor-word hyperlinks (not URL footers)
- [ ] Internal links to related WSG posts where natural (1-3 is plenty)
- [ ] No broken or placeholder links
- [ ] Ran `python3 scripts/check_links.py drafts/{file}.md` and it returned PASS
- [ ] No rotating job-posting URLs (Greenhouse `gh_jid=`, BofA `/job-detail/{N}/`, iCIMS `/jobs/{N}/`, Citi numeric postings, LinkedIn job postings, Workday specific posting URLs)
- [ ] For forward-looking articles, all links go to evergreen firm careers landing pages, not cycle-specific posting URLs
- [ ] When a specific page doesn't exist yet (e.g., "2028 SA Program" before applications open), text describes when the page will appear and links to the firm's general careers root instead

## Voice & quality (the WSG-specific bar)

- [ ] No filler phrases ("highly competitive," "in today's landscape," "many students find")
- [ ] No em-dashes or hyphens used as structural punctuation in body copy
- [ ] At least one specific number, named firm, or real scenario per major section
- [ ] At least one moment of "only someone who has done this would know" insight
- [ ] No definitions of basic terms (this isn't Wikipedia)
- [ ] Bolded sentences are full claims, not random words
- [ ] CTA only if it lands naturally — otherwise leave it out

## The 4-question gut check

Before delivering the draft:

1. Does this sound like real experience?
2. Would a smart junior find this useful?
3. Could another blog have written this?
4. If I cut a paragraph, would it matter?

Target answers: yes / yes / no / yes. If anything is off, revise before delivery.
