# Consulting Deep-Dive Index

This folder holds long-form internal guides for consulting topics. Deep dives are the well WSG articles draw from — they have no SEO constraints, no length limits, and are not published. When a writer needs to spawn an article on a consulting topic, they pull the relevant deep dive into context and shape the article from the slice they need.

The parallel structure to IB: `deep-dives/{topic}.md` for IB; `deep-dives/consulting/{topic}.md` for consulting.

## Gap analysis: deep dives to write

These are the high-priority deep dives. None exist yet. Each one would spawn multiple articles in the content calendar.

| Deep-dive | Status | Articles it spawns | Priority |
| --- | --- | --- | --- |
| `mbb-recruiting.md` | not started | "Top 10 Consulting Firms for Undergrads to Apply To in 2026", "How to Get Into McKinsey as an Undergrad", "MBB Application Deadlines 2026", "McKinsey vs BCG vs Bain — Which Should You Target?" | High |
| `case-interview.md` | not started | "10 Free Case Interview Resources", "How to Prepare for a McKinsey Case Interview", "The 5 Case Types Every Consulting Candidate Needs to Know" | High |
| `consulting-vs-banking.md` | not started | "Should You Pick Consulting or Investment Banking?", "Consulting Salary vs Investment Banking Salary 2026", "Hours Comparison: MBB vs Bulge Bracket IB" | Medium |
| `mbb-affinity-programs.md` | not started | "Top 10 MBB Sophomore Programs for Diverse Candidates", "How to Get Into McKinsey Insight", "Bain Build vs McKinsey Insight vs BCG Bridge to BCG" | Medium |
| `tier-2-consulting.md` | not started | "Top 10 Non-MBB Strategy Firms for Undergrads", "Oliver Wyman vs Strategy& vs Kearney", "How to Break Into a Tier-2 Strategy Firm" | Medium |
| `economic-consulting.md` | not started | "Top 10 Economic Consulting Firms for Econ Majors", "Analysis Group vs Cornerstone Research — Which to Target", "Why Economic Consulting Beats MBB for PhD-Bound Candidates" | High (econ-major-friendly angle) |
| `life-sciences-consulting.md` | not started | "Top 10 Life Sciences Consulting Firms for Pre-Med and Bio Majors", "ZS vs Putnam vs Clearview", "How to Break Into Pharma Strategy Without an MBA" | Medium |
| `consulting-exits.md` | not started | "Top Exit Options from MBB Consulting", "MBB to PE — The Realistic Path", "MBB to Tech PM — How Stripe and Meta Hire Consultants" | High |
| `case-interview-2026-updates.md` | not started | "How McKinsey Solve Has Changed in 2026", "What's New in BCG Casey", "Behavioral Interview Trends MBB Is Watching For" | Low (refresh-style article) |
| `consulting-with-no-summer-experience.md` | not started | "How to Get Into Consulting Without a Summer Internship", "Lateral Path From Industry to Consulting" | Low |

## How to use this folder

If a WSG article topic appears in the "Articles it spawns" column, check if the parent deep-dive exists. If yes, read it in full and pull the slice. If no, you have two options:

1. **Pull from the canonical context bundle** at `consulting/` and write the article fresh. Faster, but the article won't have the depth that comes from a real deep dive.
2. **Tell the user the deep dive is missing and offer to draft it first.** The deep dive is a one-time investment that pays back across 3-5 articles.

## Naming convention

`deep-dives/consulting/{topic-slug}.md`. No date in the filename — deep dives live forever and get updated in place. Use git history for version tracking.

## Content rules for consulting deep dives

Read `style-guide/style-guide.md` and `consulting/voice-cues.md` before drafting. The deep dive isn't an article so it doesn't follow the listicle/ultimate-guide structure — but it should still:

- Be specific (named firms, real numbers, real scenarios).
- Avoid filler.
- Disclose what we don't know (an "open questions" section is encouraged).
- Capture named-student or named-engagement scenarios that can later become credibility moments in articles.

If you find yourself writing a deep dive that doesn't include any specific firm names, real comp numbers, or real candidate scenarios, stop and re-anchor. The deep dive is the well — if the well is generic, every article drawn from it will be generic.
