#!/usr/bin/env python3
"""
combine_context.py — Bundle your Obsidian vault notes into a single
markdown file, ready to paste into any AI chat (no API/CLI needed).

USAGE
    python3 combine_context.py                      interactive: pick files, combine
    python3 combine_context.py --preset weekly       use a saved preset
    python3 combine_context.py --save-preset weekly  pick files, save them as a preset
    python3 combine_context.py --list-presets        show saved presets
    python3 combine_context.py --vault /path/to/vault  (re)point at a vault

FIRST RUN: it asks for your vault path once and remembers it
(~/.config/personal_os/config.json).

ALWAYS INCLUDED, regardless of preset:
    05-System/Master-Prompt.md
    05-System/Preferences.md
    05-System/Modes.md
    03-Goals/  (whole folder)

OUTPUT: writes <vault>/combined_context.md and copies it to the
clipboard (wl-copy on Wayland/Hyprland, xclip as fallback).
"""

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "personal_os"
CONFIG_FILE = CONFIG_DIR / "config.json"

DEFAULT_EXCLUDE_DIRS = {".obsidian", "Templates", ".trash"}

ALWAYS_FIRST = [
    "05-System/Master-Prompt.md",
    "05-System/Preferences.md",
    "05-System/Modes.md",
    "03-Goals",
]


def load_config():
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text())
    return {}


def save_config(cfg):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2))


def get_vault_path(args) -> Path:
    cfg = load_config()
    if args.vault:
        cfg["vault_path"] = args.vault
        save_config(cfg)
    if "vault_path" not in cfg:
        path = input("Enter the full path to your Obsidian vault: ").strip()
        cfg["vault_path"] = path
        save_config(cfg)
    vault = Path(cfg["vault_path"]).expanduser()
    if not vault.exists():
        sys.exit(f"Vault path does not exist: {vault}")
    return vault


def presets_file(vault: Path) -> Path:
    return vault / "05-System" / "presets.json"


def load_presets(vault: Path) -> dict:
    pf = presets_file(vault)
    if pf.exists():
        return json.loads(pf.read_text())
    return {}


def save_presets(vault: Path, presets: dict):
    pf = presets_file(vault)
    pf.parent.mkdir(parents=True, exist_ok=True)
    pf.write_text(json.dumps(presets, indent=2))


def all_md_files(vault: Path, exclude_dirs=DEFAULT_EXCLUDE_DIRS):
    files = []
    for p in vault.rglob("*.md"):
        rel = p.relative_to(vault)
        if any(part in exclude_dirs for part in rel.parts):
            continue
        files.append(rel)
    return sorted(files)


def expand_selection(vault: Path, entries: list, daily_days: int) -> list:
    seen, seen_set = [], set()

    def add(p: Path):
        if p not in seen_set and p.exists() and p.suffix == ".md":
            seen.append(p)
            seen_set.add(p)

    for entry in entries:
        full = vault / entry
        if full.is_dir():
            for f in sorted(full.rglob("*.md")):
                rel_parts = f.relative_to(vault).parts
                if any(part in DEFAULT_EXCLUDE_DIRS for part in rel_parts):
                    continue
                if "01-Daily" in rel_parts:
                    try:
                        file_date = datetime.strptime(f.stem, "%Y-%m-%d")
                        if file_date < datetime.now() - timedelta(days=daily_days):
                            continue
                    except ValueError:
                        pass
                add(f)
        elif full.exists():
            add(full)
        else:
            print(f"  (skipping, not found: {entry})")

    return seen


def interactive_pick(vault: Path) -> list:
    files = all_md_files(vault)
    print(f"\nFound {len(files)} markdown files in vault.\n")
    for i, f in enumerate(files, 1):
        print(f"  [{i:>3}] {f}")
    print("\nSelect numbers ('1 4 7'), ranges ('1-5'), 'all', or 'q' to cancel.")
    raw = input("> ").strip()
    if raw.lower() == "q":
        sys.exit("Cancelled.")
    if raw.lower() == "all":
        return [str(f) for f in files]
    chosen = set()
    for tok in raw.split():
        if "-" in tok:
            a, b = tok.split("-")
            chosen.update(range(int(a), int(b) + 1))
        else:
            chosen.add(int(tok))
    return [str(files[i - 1]) for i in sorted(chosen) if 1 <= i <= len(files)]


def combine(vault: Path, entries: list, daily_days: int, out_path: Path) -> str:
    ordered = list(ALWAYS_FIRST) + [e for e in entries if e not in ALWAYS_FIRST]
    file_list = expand_selection(vault, ordered, daily_days)

    chunks = [f"<!-- Combined context generated {datetime.now():%Y-%m-%d %H:%M} -->\n"]
    for f in file_list:
        rel = f.relative_to(vault)
        chunks.append(f"\n\n---\n## FILE: {rel}\n---\n")
        try:
            chunks.append(f.read_text(encoding="utf-8"))
        except Exception as e:
            chunks.append(f"(could not read file: {e})")

    combined = "".join(chunks)
    out_path.write_text(combined, encoding="utf-8")
    print(f"\nCombined {len(file_list)} files -> {out_path}")
    return combined


def copy_to_clipboard(text: str) -> bool:
    for tool, cmd in [("wl-copy", ["wl-copy"]), ("xclip", ["xclip", "-selection", "clipboard"])]:
        if shutil.which(tool):
            subprocess.run(cmd, input=text.encode("utf-8"))
            print(f"Copied to clipboard via {tool}")
            return True
    print("No clipboard tool found. Install one:")
    print("    sudo dnf install wl-clipboard   # Wayland / Hyprland")
    print("    sudo dnf install xclip          # X11")
    return False


def main():
    parser = argparse.ArgumentParser(description="Combine vault notes into one file for pasting to AI.")
    parser.add_argument("--vault", help="Path to your Obsidian vault (saved after first use)")
    parser.add_argument("--preset", help="Use a saved preset by name")
    parser.add_argument("--list-presets", action="store_true")
    parser.add_argument("--save-preset", metavar="NAME", help="Interactively pick files, save as this preset")
    parser.add_argument("--out", default="combined_context.md", help="Output filename (written to vault root)")
    parser.add_argument("--days", type=int, default=7, help="Days of Daily notes to include (default 7)")
    parser.add_argument("--no-clipboard", action="store_true", help="Don't auto-copy to clipboard")
    args = parser.parse_args()

    vault = get_vault_path(args)
    presets = load_presets(vault)

    if args.list_presets:
        if not presets:
            print("No presets saved yet.")
        for name, entries in presets.items():
            print(f"\n{name}:")
            for e in entries:
                print(f"  - {e}")
        return

    if args.save_preset:
        entries = interactive_pick(vault)
        presets[args.save_preset] = entries
        save_presets(vault, presets)
        print(f"Saved preset '{args.save_preset}' with {len(entries)} entries.")
        if input("Combine using this preset now? [Y/n] ").strip().lower() == "n":
            return
        entries_to_use = entries
    elif args.preset:
        if args.preset not in presets:
            sys.exit(f"No such preset: {args.preset}. Run --list-presets to see options.")
        entries_to_use = presets[args.preset]
    else:
        print("No preset given — defaulting to ALL files.")
        print("Use --preset NAME for a saved set, or --save-preset NAME to define one.\n")
        entries_to_use = [str(f) for f in all_md_files(vault)]

    out_path = vault / args.out
    combined = combine(vault, entries_to_use, args.days, out_path)

    if not args.no_clipboard:
        copy_to_clipboard(combined)


if __name__ == "__main__":
    main()
