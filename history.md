# History Log

## Log Entries

### [2026-09-03T08:45:00+05:30] - Dataview Query & Frontmatter Standardization
- **User Feedback**: Standardize Dataview plugin queries for question log tables, strip all remaining bloated header titles, store test metadata in YAML frontmatter properties, and link directly to variation files without intermediate index links.
- **Implementation**:
  - Updated [`SKILL.md`](file:///home/skc/dev/SAGE/.agents/skills/exam-analysis-master/SKILL.md) to explicitly require Dataview queries (`dataview` codeblocks) for `question_db.md`.
  - Enforced metadata (Exam, Subject, Topic, Date, Source File) inside YAML frontmatter properties for test session scorecards.
  - Simplified topic note header title from `# Heights and Distances - Theory & Concept Notes` to `# Heights and Distances`.
  - Replaced hardcoded markdown table in [`question_db.md`](file:///home/skc/dev/SAGE/content/cds/elementary-mathematics/question_db.md) with dynamic Obsidian Dataview block.
  - Linked chapter variations directly to specific variation files.
  - Committed and pushed to remote branch `v5`.



### [2026-09-03T09:41:00+05:30] - Quartz 5 Vercel Deployment Configuration
- **User Request**: Setup Vercel deployment for Quartz 5.
- **Implementation**:
  - Created `vercel.json` with `"cleanUrls": true` to fix trailing `.html` extension URL routing.
  - Verified `quartz.config.yaml` configuration and completed local build check (`npx quartz build`).
  - Committed `vercel.json` and pushed changes to `origin/v5`.

---

## Overall Plan & Roadmap
- [x] Initial GitHub Issue #3 creation (`gh issue create`).
- [x] Skill architecture design and implementation plan.
- [ ] Create `~/.gemini/config/skills/exam-analysis-master/SKILL.md`.
- [ ] Create template Obsidian folder structure in `content/` (`exams_config.md`, subject indexes, question database template, `_quarto.yml`).
- [ ] Verify formatting guidelines and commands (`/wrap`, `/report`, `/analyze`).
- [ ] Commit changes with git standard.

---

## DOs and DON'Ts
### DOs
- DO enforce strict Obsidian frontmatter + LaTeX math formatting (`$...$`, `$$...$$`).
- DO use zero-token rewrite file relocation during `/wrap` (move `tmp/session_id/*.md` directly into `notes/`).
- DO generate novel variations testing fundamental theorems/concepts rather than naive number swaps.

### DON'Ts
- DON'T rewrite whole session contents during `/wrap` (wastes tokens and risks losing points).
- DON'T pollute global python environments or use generic purple gradients/AI slop.
- DON'T close GitHub issues or local tickets without explicit user approval.
