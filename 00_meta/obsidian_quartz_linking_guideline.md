# 🔗 Obsidian & Quartz Wikilink Guidelines

## Core Linking Rule
Always write standard Obsidian wikilinks **without** the `content/` root prefix.

### Correct Syntax
- `[[moc os]]`
- `[[moc os|Operating Systems]]`
- `[[Critical Section Synchronization Criteria|Sync Criteria]]`

### Incorrect Syntax (Breaks Live Site)
- ❌ `[[content/mocs/moc os]]`
- ❌ `[[content/gate-cs/os/Critical Section Synchronization Criteria]]`

---

## Why?
Quartz serves files from the `content/` directory as the root (`/`). 

When Quartz builds the site with `markdownLinkResolution: shortest`:
- `content/mocs/moc os.md` maps directly to URL route `/mocs/moc-os`
- Including `content/` in the link causes Quartz to look for `/content/mocs/moc-os` on the web server, resulting in a **404 Page Not Found** error.

---

## Global Customization Saved
This rule has also been added to `.agents/AGENTS.md` so that AI subagents automatically follow this pattern for all future note generation and refactorings.
