# Changelog: skill update from Stephen's reference list (October 8, 2026)

Source: Stephen's notes and reference articles relayed by Sanskar on Slack (October 8), plus Sanskar's length note. Decisions confirmed in review: light first person, length as a medium target, focus on Stephen's quoted lines over copying the samples, humanizer built into the images skill. Previous articles were not revised.

## Writing rules

- **Openings answer the question first.** Sentence one says what the topic is or answers the headline; a bolded full-sentence fact follows; the last sentence says what the article covers. Two to five sentences. No narrative openings, no opinions about what readers get wrong. Models: the McKinsey Solve and Sophomore Insights openers. Anti-models: the BCG Casey and Consulting Exit Opportunities openers, with Stephen's rewrites. (`intros.md`, rewritten.)
- **Light first person is back.** "I get asked about X a lot," "In this article, I lay out..." No bio, credentials, memories, composite stories or byline. Amends October 7 rule 1.
- **Simple, direct titles.** Count, topic in search words, year if it applies.
- **Signposted numbered headings** ("1. Your school matters but probably not in the way you think") and **question headers in the reader's exact words** ("What is a sophomore insights program?"). `prose-editing.md` rules 12 and 13.
- **Bolds are full sentences with a fact.** Rule 14.
- **No unsupported opinions about what people get wrong.** Rule 15.
- **Length target: about 20 to 25 pages before images** (roughly 4,500 to 6,000 words at WSG spacing; measured at about 250 words a page on a test build). Over is allowed when the topic needs it, with the reason in the Thoroughness Report. Cut order in rule 16. Thoroughness now expands-then-pays: every added step is paid for by cutting repetition elsewhere.
- **Calibration samples are human-written only.** New `samples/reference-articles.md` (packaged as `.claude-skill/reference-articles.md`) holds Stephen's six good and two bad articles, quoted, with his notes. `drafts/` and `published/ai-written/` are never used as voice samples.

## Answer to Sanskar's question about sample docs

The skill pointed at `samples/` and `published/` for voice. The local repo's `samples/` has nine curated articles, but its own README says they may be AI-written; the Claude Content project mirror had none, and `published/human-written/` is empty. So the voice reference has been a mix of real WSG articles, possibly-AI samples and, in project-only sessions, earlier AI drafts. Stephen's reference list now sets the voice, `samples/README.md` marks the three samples he endorsed, and the skill forbids calibrating on AI drafts.

## Images

- **Image-text humanizer pass built into `images.md`.** Every title, label, callout, caption, alt text and source line is collected, run through the `humanizer` skill in embedded mode when available (otherwise the built-in rules and cut table), checked against the article's numbers, written back to the build script and manifest, and re-rendered.
- **Titles are short and literal by default**; an occasional plain takeaway title is fine (about one in three images at most). Captions are one plain sentence under about 20 words that states a fact from the chart. Labels are nouns and numbers.
- New "Fixing images already built" procedure for existing articles.

## Files changed

`.claude-skill/` SKILL.md, intros.md, prose-editing.md (rules 7, 9, 10 updated; 12 to 16 added; spot checks updated), thorough-explanations.md, images.md, consulting.md, reference-articles.md (new); `samples/reference-articles.md` (new), `samples/README.md` (Stephen's picks marked); `templates/` listicle.md, ultimate-guide.md, niche.md; `CLAUDE.md`.

Unchanged: plain-language.md, formatting.md, source-verification.md, recruiting-relevance.md, humanizer.

## Still to sync

- `style-guide/editorial-rules.md` Part 2 is named as the canonical copy of the prose rules. Rules 12 to 16 live in `.claude-skill/prose-editing.md` for now; mirror them into Part 2 when the repo is next edited.
- `style-guide/style-guide.md` and `templates/_brief-template.md` may still describe the October 7 intro rule or old word counts. SKILL.md's October 8 section overrides them.
- `scripts/check_article.py` still treats word count as info only. Optional: warn above about 6,500 words.
- Re-save the rebuilt `.skill` packages to the Claude account (wsg-article, wsg-intros, wsg-prose-editing, wsg-article-images, thorough-explanations).
