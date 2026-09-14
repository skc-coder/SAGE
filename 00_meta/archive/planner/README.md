# Personal OS — How This Works

1. Plan each day in `01-Daily/` using the Daily Template — it auto-pulls
   tasks due today from your project files (Tasks plugin).
2. Every task lives ONCE, in its project file under `02-Projects/`. Never
   re-typed anywhere else.
3. Big goals + SMART breakdown live in `03-Goals/Yearly-Goals-2026.md`.
4. Weekly (or whenever): run
   `python3 05-System/scripts/combine_context.py`
   and paste the result into any AI chat. It auto-includes
   Master-Prompt.md, Preferences.md, Modes.md, and your Goals.
5. The AI will ask you questions, flag stalled tasks, and check in on you.
   Paste any `UPDATE TO: ...` blocks it gives back into the matching file.
6. Weekly review goes in `04-Reviews/Weekly/` using the Weekly Review Template.

To change how the AI behaves: edit `05-System/Master-Prompt.md` and
`05-System/Modes.md` directly — plain markdown, no code involved.
