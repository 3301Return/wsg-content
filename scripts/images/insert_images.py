#!/usr/bin/env python3
"""Insert image lines into a draft from an images manifest (October 2026).

Usage, from the repo root:

    python3 scripts/images/insert_images.py {slug} drafts/draft-{slug}-v1.md [--dry-run]

Reads published/assets/images/{slug}/manifest.json. For each entry it finds the first
line of the draft whose text starts with the entry's "anchor" (the first 60 characters of
the line the image should follow), skips to the end of that line's block if the anchor is
a table row or a list item, and inserts

    (blank line)
    ![alt](published/assets/images/{slug}/{file} "caption")
    (blank line)
    *Source: {source}*          <- from the entry's "source" field (October 7, 2026 rule)
    (blank line)

Every entry needs a "source": where the information in the image comes from ("Bain & Company
careers site, October 2026", "Company 10-K for fiscal 2025, SEC EDGAR", "WSG analysis of the
worked example in this article"). An entry without one is reported as a warning.

after it. Idempotent: an image line already in the draft is left alone. Anchors that are
not found, or that sit before the first H2 (the intro), are reported and skipped, so the
image agents never have to edit a draft while the QA agents are editing it.
"""
import json
import re
import sys
from pathlib import Path


def block_end(lines, i):
    """If lines[i] is a table row or list item, return the index of the last line of that block."""
    line = lines[i]
    is_table = line.lstrip().startswith("|")
    is_list = re.match(r"^\s*([-*+]|\d+\.)\s", line) is not None
    if not (is_table or is_list):
        return i
    j = i
    while j + 1 < len(lines):
        nxt = lines[j + 1]
        if is_table and nxt.lstrip().startswith("|"):
            j += 1
        elif is_list and (re.match(r"^\s*([-*+]|\d+\.)\s", nxt) or (nxt.startswith("  ") and nxt.strip())):
            j += 1
        else:
            break
    return j


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    slug, draft = sys.argv[1], Path(sys.argv[2])
    dry = "--dry-run" in sys.argv
    folder = Path("published/assets/images") / slug
    manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
    text = draft.read_text(encoding="utf-8")
    lines = text.split("\n")
    first_h2 = next((i for i, l in enumerate(lines) if l.startswith("## ")), len(lines))

    inserted, skipped, missing_source = 0, [], []
    for entry in manifest:
        img_path = f"published/assets/images/{slug}/{entry['file']}"
        if not (Path(img_path).exists()):
            skipped.append((entry["file"], "image file missing"))
            continue
        caption = entry["caption"].replace('"', "'")
        img_line = f"![{entry['alt']}]({img_path} \"{caption}\")"
        if any(img_path in l for l in lines):
            continue  # already placed
        anchor = entry.get("anchor", "").strip()
        if not anchor:
            skipped.append((entry["file"], "no anchor"))
            continue
        idx = next((i for i, l in enumerate(lines) if l.strip().startswith(anchor)), None)
        if idx is None:
            # second try: whitespace-insensitive match on the first 40 characters
            key = re.sub(r"\s+", " ", anchor[:40])
            idx = next((i for i, l in enumerate(lines) if re.sub(r"\s+", " ", l.strip()).startswith(key)), None)
        if idx is None:
            skipped.append((entry["file"], f"anchor not found: {anchor!r}"))
            continue
        if idx < first_h2:
            skipped.append((entry["file"], "anchor is in the intro; not inserting"))
            continue
        end = block_end(lines, idx)
        insert_at = end + 1
        # keep exactly one blank line on each side
        new = []
        if lines[end].strip() != "":
            new.append("")
        new.append(img_line)
        src = (entry.get("source") or "").strip()
        if src:
            if not src.lower().startswith(("source", "photo")):
                src = "Source: " + src
            new.append("")
            new.append(f"*{src.rstrip('.')}.*")
        else:
            missing_source.append(entry["file"])
        if insert_at >= len(lines) or lines[insert_at].strip() != "":
            new.append("")
        lines[insert_at:insert_at] = new
        first_h2 = next((i for i, l in enumerate(lines) if l.startswith("## ")), len(lines))
        inserted += 1

    if not dry:
        draft.write_text("\n".join(lines), encoding="utf-8")
    print(f"{slug}: inserted {inserted} image line(s){' (dry run)' if dry else ''}")
    for f, why in skipped:
        print(f"  SKIPPED {f}: {why}")
    for f in missing_source:
        print(f"  WARNING {f}: no 'source' in manifest; add one so the article credits the data")
    sys.exit(1 if skipped else 0)


if __name__ == "__main__":
    main()
