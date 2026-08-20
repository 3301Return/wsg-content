# Deep Dive Template (internal source-of-truth, not a published article)

**Use when:** Building the comprehensive internal guide for a topic that will spawn multiple published articles.
**Examples:** `deep-dives/restructuring.md` · `deep-dives/ib-recruiting-timeline.md` · `deep-dives/consulting-case-types.md`
**Word count:** No limit. Be thorough.
**Required:** Clear H2/H3 structure so the skill can reference sections by anchor

---

# {Topic} — Deep Dive

> **Internal use only.** Not a published article. This file is the source of truth for everything the article generator needs to know about {topic}, written in plain language with no SEO constraints.

## Why this exists

Briefly: what kind of articles will this deep dive feed? List the headlines you can imagine spawning from this guide.

Example for `restructuring.md`:
- "How Hard Is It to Break Into Restructuring?"
- "Evercore vs Houlihan vs PJT: Which RX Group Is Best for You?"
- "What Does a Day in the Life Look Like in Restructuring?"
- "Restructuring vs M&A: Which Should You Recruit For?"

## What it is

Plain explanation. Skip the SEO voice. Pretend you're explaining to a friend who is smart but new to the topic.

## How it actually works

Process, sequence, mechanics. Use named examples (real deals, real firms, real people where appropriate).

## Who the players are

Firms, roles, key people. Hierarchies. Differences between top-tier, middle, boutique, etc.

## Recruiting (if applicable)

- Timeline (specific dates and windows)
- Process (rounds, who interviews, what they look for)
- What's different vs adjacent paths (e.g., RX vs M&A recruiting)
- Common mistakes specific to this path

## Day-to-day reality

What the work actually looks like. Hours. Comp ranges. What surprises people.

## Exits

Where people go from here. Realistic timelines.

## Common myths

Things students wrongly believe about this topic, with the corrections. (These often become great article hooks.)

## Specific stories / scenarios

The most valuable part of a deep dive. Named (or de-identified) examples of real students and outcomes:
- "Student X at non-target landed RX role at Y by doing Z"
- "Common failure mode: student spent 6 months on technicals before networking"

These specifics power the credibility moments in spawned articles.

## Open questions / things to research

Anything you're not sure about yet. The skill will flag if it tries to write an article that depends on something in this section.

---

## How to use this with the article generator

When you ask for an article tied to this topic, tell Claude:

> "Write a WSG niche article on {headline}, anchored in `deep-dives/{topic}.md`."

The skill will:
1. Read this deep dive in full before drafting
2. Pull specifics from the relevant sections
3. Anchor the article in the named scenarios from the "Specific stories" section
4. Flag if it needs information from "Open questions" before proceeding
