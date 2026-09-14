# Workspace Rules for SAGE

- **No GitHub Issues**: Do NOT use `gh issue create`, `gh issue comment`, or GitHub issue management in this project repository.
- **No History File**: Do NOT create, update, or maintain `history.md` in this project repository.
- **No Tickets File**: Do NOT create, update, or maintain `tickets.md` in this project repository.
- **No Quartz Site Build**: Do NOT run `npx quartz build` or build the Quartz site in this project repository.
- **Direct Focus**: Focus strictly on content creation, note generation, markdown editing, and clean git commits.
- **Obsidian Wikilinks Standard**: Never prefix wikilinks with `content/` (e.g. use `[[moc os]]` or `[[Critical Section Synchronization Criteria]]`, NOT `[[content/mocs/moc os]]`). Quartz strips the `content/` prefix, so including it breaks live web links on Vercel.

