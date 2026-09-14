#!/usr/bin/env python3
"""
Vault Updater
-------------
Reads a single "changes" file (see UPDATE_FILE_FORMAT.md for syntax) and
applies all described changes to your Obsidian vault markdown files:
  - Adds new lines under a specific section (creates the section if missing)
  - Marks existing lines DONE or CANCELLED (strikethrough + label)
  - Removes lines entirely
  - Replaces an exact existing line with new text

Always backs up every file it touches before writing, into:
  <vault_root>/05-System/backups/<timestamp>/

Usage:
    python3 update_vault.py <updates_file.md> <vault_root_dir>

Example:
    python3 update_vault.py updates_2026_06_23.md ~/Documents/PersonalOS
"""

import sys
import shutil
from pathlib import Path
from datetime import datetime


def parse_updates_file(text: str):
    """Parse the custom update-file syntax into a list of file-change blocks.

    Returns a list of dicts:
        {
            "file": "05-System/Preferences.md",
            "section": "Non-negotiables" or None,
            "adds": [list of lines to add],
            "dones": [exact line text to mark DONE],
            "cancelleds": [exact line text to mark CANCELLED],
            "removes": [exact line text to delete],
            "replaces": [(old_line, new_line), ...],
        }
    """
    blocks = []
    current = None
    mode = None  # which list we're currently appending raw lines to ("adds" or None)

    lines = text.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()

        if stripped.startswith("UPDATE TO:"):
            if current:
                blocks.append(current)
            current = {
                "file": stripped[len("UPDATE TO:"):].strip(),
                "section": None,
                "adds": [],
                "dones": [],
                "cancelleds": [],
                "removes": [],
                "replaces": [],
            }
            mode = None

        elif stripped.startswith("SECTION:"):
            if current is None:
                i += 1
                continue
            sec = stripped[len("SECTION:"):].strip()
            if sec.lower() in ("(none)", "none", ""):
                current["section"] = None
            else:
                current["section"] = sec
            mode = None

        elif stripped.startswith("ADD:"):
            mode = "adds"
            # allow inline content right after ADD: on same line (rare, but tolerate)
            rest = stripped[len("ADD:"):].strip()
            if rest and current is not None:
                current["adds"].append(rest)

        elif stripped.startswith("DONE:"):
            if current is not None:
                current["dones"].append(stripped[len("DONE:"):].strip())
            mode = None

        elif stripped.startswith("CANCELLED:"):
            if current is not None:
                current["cancelleds"].append(stripped[len("CANCELLED:"):].strip())
            mode = None

        elif stripped.startswith("REMOVE:"):
            if current is not None:
                current["removes"].append(stripped[len("REMOVE:"):].strip())
            mode = None

        elif stripped.startswith("REPLACE:"):
            if current is not None:
                payload = stripped[len("REPLACE:"):].strip()
                if "|||" in payload:
                    old, new = payload.split("|||", 1)
                    current["replaces"].append((old.strip(), new.strip()))
            mode = None

        else:
            # Continuation line: only meaningful while in "adds" mode.
            # Blank lines are kept as-is if we're mid-ADD (rare); otherwise ignored.
            if mode == "adds" and current is not None:
                if stripped == "":
                    # blank line ends the ADD block
                    mode = None
                else:
                    current["adds"].append(raw.rstrip())
            # else: ignore stray blank lines / comments between blocks

        i += 1

    if current:
        blocks.append(current)

    return blocks


def find_section_bounds(file_lines, section_name):
    """Find the (start, end) line indices of a markdown section by header text.

    Matches any header level (#, ##, ###...) whose text (after stripping the
    leading #'s and whitespace) equals section_name exactly.
    Returns (start_index, end_index) where:
        start_index = index of the header line itself
        end_index   = index of the line BEFORE the next header of equal-or-higher
                      level (i.e. the exclusive end of this section's body)
    Returns None if not found.
    """
    target = section_name.strip().lower()
    header_idx = None
    header_level = None

    for idx, line in enumerate(file_lines):
        stripped = line.strip()
        if stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            text = stripped[level:].strip().lower()
            # strip emoji/markdown noise loosely isn't attempted; exact text match
            if text == target:
                header_idx = idx
                header_level = level
                break

    if header_idx is None:
        return None

    end_idx = len(file_lines)
    for idx in range(header_idx + 1, len(file_lines)):
        stripped = file_lines[idx].strip()
        if stripped.startswith("#"):
            level = len(stripped) - len(stripped.lstrip("#"))
            if level <= header_level:
                end_idx = idx
                break

    return (header_idx, end_idx)


def apply_adds(file_lines, section_name, new_lines):
    """Insert new_lines at the end of the named section's body.
    If section_name is None, append at end of file.
    If section doesn't exist, create it (## level) at end of file, then add.

    Idempotent: any line whose stripped content already exists anywhere
    in the file (matched after strip_markup, so "- foo" == "foo") is
    skipped, so re-running the same updates file twice does not duplicate
    content. Returns (updated_lines, skipped_duplicates).
    """
    if not new_lines:
        return file_lines, []

    existing_content = {strip_markup(l) for l in file_lines if l.strip() != ""}

    lines_to_add = []
    skipped = []
    for nl in new_lines:
        # Header lines (e.g. "## Some Section") are content-matched on the
        # full header text, same rule, so re-adding an identical block header
        # won't duplicate it either.
        key = strip_markup(nl) if not nl.strip().startswith("#") else nl.strip()
        if key in existing_content or nl.strip() in existing_content:
            skipped.append(nl)
            continue
        lines_to_add.append(nl)
        existing_content.add(key)

    if not lines_to_add:
        return file_lines, skipped

    if section_name is None:
        if file_lines and file_lines[-1].strip() != "":
            file_lines.append("")
        return file_lines + lines_to_add, skipped

    bounds = find_section_bounds(file_lines, section_name)

    if bounds is None:
        if file_lines and file_lines[-1].strip() != "":
            file_lines.append("")
        file_lines.append(f"## {section_name}")
        file_lines.extend(lines_to_add)
        return file_lines, skipped

    start, end = bounds
    insert_at = end
    while insert_at > start + 1 and file_lines[insert_at - 1].strip() == "":
        insert_at -= 1

    result = file_lines[:insert_at] + lines_to_add + file_lines[insert_at:]
    return result, skipped


def strip_markup(text: str) -> str:
    """Strip common leading markdown markup (bullets, checkboxes) and
    surrounding whitespace, so matches can be specified as plain content
    text without needing to reproduce '- ' or '- [ ] ' exactly.
    """
    t = text.strip()
    if t.startswith("-"):
        rest = t[1:].lstrip()
        if rest.startswith("[") and "]" in rest:
            close = rest.index("]")
            rest = rest[close + 1:].lstrip()
        t = rest
    return t.strip()


def apply_line_ops(file_lines, dones, cancelleds, removes, replaces):
    """Apply DONE / CANCELLED / REMOVE / REPLACE operations.

    Matching is on the *content* of the line -- i.e. after stripping a
    leading bullet/checkbox marker ("- ", "- [ ] ", "- [x] ") and outer
    whitespace -- so the updates file can specify either the raw line or
    just its content without reproducing bullet syntax exactly.

    Returns (new_lines, list_of_not_found) for reporting.
    """
    not_found = []
    result = []

    replace_map = {strip_markup(old): new for old, new in replaces}
    done_set = {strip_markup(d) for d in dones}
    cancelled_set = {strip_markup(c) for c in cancelleds}
    remove_set = {strip_markup(r) for r in removes}

    matched = {
        "done": set(),
        "cancelled": set(),
        "removed": set(),
        "replaced": set(),
    }

    for line in file_lines:
        stripped_line = line.strip()
        content = strip_markup(stripped_line)
        indent = line[: len(line) - len(line.lstrip())] if line.strip() else ""

        if content in remove_set:
            matched["removed"].add(content)
            continue  # drop the line

        if content in replace_map:
            new_text = replace_map[content]
            if new_text.lstrip().startswith("-"):
                result.append(f"{indent}{new_text.lstrip()}")
            else:
                prefix = stripped_line[: len(stripped_line) - len(content)] if content else ""
                result.append(f"{indent}{prefix}{new_text}")
            matched["replaced"].add(content)
            continue

        if content in done_set:
            prefix = stripped_line[: len(stripped_line) - len(content)] if content else ""
            result.append(f"{indent}{prefix}~~{content}~~ → DONE")
            matched["done"].add(content)
            continue

        if content in cancelled_set:
            prefix = stripped_line[: len(stripped_line) - len(content)] if content else ""
            result.append(f"{indent}{prefix}~~{content}~~ → CANCELLED")
            matched["cancelled"].add(content)
            continue

        result.append(line)

    for target_set, key in (
        (done_set, "done"),
        (cancelled_set, "cancelled"),
        (remove_set, "removed"),
        (set(replace_map.keys()), "replaced"),
    ):
        for item in target_set:
            if item not in matched[key]:
                not_found.append(item)

    return result, not_found


def backup_file(filepath: Path, backup_root: Path, vault_root: Path):
    if not filepath.exists():
        return None
    rel = filepath.relative_to(vault_root)
    dest = backup_root / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(filepath, dest)
    return dest


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 update_vault.py <updates_file.md> <vault_root_dir>")
        sys.exit(1)

    updates_path = Path(sys.argv[1]).expanduser()
    vault_root = Path(sys.argv[2]).expanduser()

    if not updates_path.exists():
        print(f"ERROR: updates file not found: {updates_path}")
        sys.exit(1)
    if not vault_root.is_dir():
        print(f"ERROR: vault root not found or not a directory: {vault_root}")
        sys.exit(1)

    updates_text = updates_path.read_text(encoding="utf-8")
    blocks = parse_updates_file(updates_text)

    if not blocks:
        print("No UPDATE TO: blocks found in the updates file. Nothing to do.")
        sys.exit(0)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_root = vault_root / "05-System" / "backups" / timestamp

    print(f"Found {len(blocks)} file-update block(s).")
    print(f"Backups will be saved to: {backup_root}\n")

    report_lines = []

    for block in blocks:
        target_file = vault_root / block["file"]
        report_lines.append(f"--- {block['file']} ---")

        if not target_file.exists():
            # Create the file (and parent dirs) if it doesn't exist yet
            target_file.parent.mkdir(parents=True, exist_ok=True)
            target_file.write_text("", encoding="utf-8")
            report_lines.append("  (file did not exist -- created new)")

        backup_path = backup_file(target_file, backup_root, vault_root)
        if backup_path:
            report_lines.append(f"  Backed up to: {backup_path}")

        file_lines = target_file.read_text(encoding="utf-8").splitlines()

        # 1. Line-level ops first (done/cancelled/remove/replace)
        file_lines, not_found = apply_line_ops(
            file_lines,
            block["dones"],
            block["cancelleds"],
            block["removes"],
            block["replaces"],
        )
        for nf in not_found:
            report_lines.append(f"  WARNING: exact text not found, skipped: {nf!r}")

        # 2. Additions (idempotent -- duplicates are skipped, not re-added)
        if block["adds"]:
            file_lines, skipped_dupes = apply_adds(file_lines, block["section"], block["adds"])
            sec_label = block["section"] if block["section"] else "(end of file)"
            added_count = len(block["adds"]) - len(skipped_dupes)
            report_lines.append(f"  Added {added_count} line(s) to section: {sec_label}")
            for sd in skipped_dupes:
                report_lines.append(f"  SKIPPED (already present): {sd!r}")

        new_content = "\n".join(file_lines)
        if not new_content.endswith("\n"):
            new_content += "\n"
        target_file.write_text(new_content, encoding="utf-8")
        report_lines.append("  Saved.\n")

    print("\n".join(report_lines))
    print(f"\nDone. {len(blocks)} file(s) updated. Backups at: {backup_root}")


if __name__ == "__main__":
    main()
