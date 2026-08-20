# Deep Dives

This folder holds your **internal source-of-truth guides** — the long, comprehensive explainers that aren't published as articles themselves but feed multiple articles.

## How this works (your restructuring example)

You said you'd write a complete guide explaining how restructuring works, and then create articles based on that guide. That's exactly what this folder is for.

1. You write (or paste) `restructuring.md` here — the full deep dive: what RX is, how the deals work, who the key players are, how recruiting differs, comp, exits, day-to-day work, etc.
2. When you ask for an article like "How to break into Evercore restructuring," the generator reads `deep-dives/restructuring.md` first to ground itself in the real details.
3. The output article only uses the slice relevant to that headline — but it's anchored in the deep dive's specifics, which is what makes the article feel like real experience instead of recycled advice.

## Suggested deep dives to seed

Common WSG topics that benefit from this treatment:
- `restructuring.md`
- `m-and-a-process.md`
- `ib-recruiting-timeline.md`
- `consulting-case-types.md`
- `target-vs-non-target-recruiting.md`

You don't need to write all of these upfront. Add a deep dive when you're about to spawn 3+ articles from one topic area.

## Format

Plain Markdown is best. Structure with H2/H3 sections so the generator can reference them by anchor (e.g., "see `deep-dives/restructuring.md#networking`").

There's no length limit. These are internal — they don't need to be polished.
