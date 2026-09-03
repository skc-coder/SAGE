# History Log

## Log Entries

### [2026-09-03T14:46:00+05:30] - Fix External Links to Internal Obsidian Wikilinks
- **User Feedback**: Correct external `file:///...` links to native Obsidian wikilinks `[[path|Title]]` in `math_overview.md`.
- **Implementation**:
  - Replaced `[Key Theorems & Models Cheatsheet](file:///...)` with `[[cds/math/notes/subtopics/hcf_lcm_cheatsheet|Key Theorems & Models Cheatsheet]]` and `[[cds/math/notes/subtopics/modular_cheatsheet|Key Theorems & Models Cheatsheet]]` in [`math_overview.md`](file:///home/skc/dev/SAGE/content/cds/math/math_overview.md).
  - Committed and pushed to `origin/v5`.

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

### [2026-09-03T11:21:00+05:30] - Pathfinder Chapter 3: HCF and LCM Notes Creation
- **User Request**: Create notes, subtopics, and practice variations for Pathfinder CDS Mathematics Chapter 3 (HCF and LCM).
- **Implementation**:
  - Created GitHub Issue [#4](https://github.com/skc-coder/SAGE/issues/4) and updated [`tickets.md`](file:///home/skc/dev/SAGE/tickets.md).
  - Created main topic note [`hcf_lcm.md`](file:///home/skc/dev/SAGE/content/cds/math/notes/hcf_lcm.md) with canonical prime factorization formulas, product identity, co-prime models, and fraction/polynomial rules.
  - Created subtopic note [`hcf_methods.md`](file:///home/skc/dev/SAGE/content/cds/math/notes/subtopics/hcf_methods.md) for Long Division/Euclidean algorithm, difference shortcut, and HCF remainder cases.
  - Created subtopic note [`lcm_models.md`](file:///home/skc/dev/SAGE/content/cds/math/notes/subtopics/lcm_models.md) covering Constant Remainder Theorem ($\text{LCM} + R$), Constant Difference Theorem ($\text{LCM} - p$), and Bell Ringing concurrency.
  - Updated [`questions.md`](file:///home/skc/dev/SAGE/content/cds/math/notes/questions.md) with Pathfinder practice questions (Q5-Q8) and solution blocks.
  - Added variations (Variations 8-11) to [`vars.md`](file:///home/skc/dev/SAGE/content/cds/math/notes/variations/vars.md).
  - Linked new topic and charts in [`math_overview.md`](file:///home/skc/dev/SAGE/content/cds/math/math_overview.md) and verified Quartz build (`npx quartz build`).
  - Committed and pushed changes to `origin/v5`.

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
