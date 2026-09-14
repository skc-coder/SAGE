# Update File Format — Reference

This is the syntax I'll use whenever you say "give me the update file." Save
this somewhere in `05-System/` for reference. You won't need to write this
syntax yourself — I generate it, you just run the script.

## Basic structure

```
UPDATE TO: <path/to/file.md, relative to vault root>
SECTION: <exact heading text, no # symbols> OR (none)
ADD:
- line one to add
- line two to add

DONE: <task text, with or without "- " or "- [ ] ">
CANCELLED: <task text>
REMOVE: <task text>
REPLACE: <old text>|||<new text>
```

- Multiple `UPDATE TO:` blocks can exist in one file — one per file/section combo.
- `SECTION: (none)` means "just append to the end of the file" — no header targeting.
- If a named section doesn't exist yet, it's created automatically (as a `##` heading) at the end of the file.
- If the target file doesn't exist yet, it's created automatically.
- `DONE` / `CANCELLED` / `REMOVE` / `REPLACE` match on line *content* — you don't need to include the `- ` or `- [ ] ` prefix, just the text itself.
- If a `DONE`/`CANCELLED`/`REMOVE`/`REPLACE` target isn't found (typo, already changed, etc.), the script prints a warning and skips it — it never crashes or guesses.

## Example

```
UPDATE TO: 05-System/Preferences.md
SECTION: Non-negotiables (locked in, starting June 22)
REPLACE: Sleep: 9 PM sharp, wake 5 AM|||Sleep: 9 PM sharp, wake 6 AM
ADD:
- Strength training: 6:00-7:00 PM (evening, cool temp)

UPDATE TO: 00-Inbox/inbox.md
SECTION: (none)
DONE: know about afcat, cds exam and physical requirements
CANCELLED: app (defer)
```

## Running it

```bash
python3 update_vault.py <updates_file.md> <path_to_your_vault_root>
```

Every run backs up every file it's about to touch into:
`<vault_root>/05-System/backups/<timestamp>/`

before making any changes — so you can always recover the previous version.

## How to use this going forward

Just tell me **"give me the update file"** at any point, and I'll generate one
using this exact syntax based on everything we've decided in the conversation.
Save it anywhere, then run the command above.
