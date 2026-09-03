# Tickets Log — SAGE

## Active Tickets

### [OPEN] Issue #3: Design & Implement Exam Practice & Smart Analysis Skill (`exam-analysis-master`)
- **GitHub Issue**: [#3](https://github.com/skc-coder/SAGE/issues/3)
- **Description**: Create a modular, extensible, clean, small, to-the-point AI skill for Obsidian & Quarto export to track exam questions, perform topic/subtopic taxonomy breakdown, generate concept notes, ask novel variations, track user performance, and support `/wrap`, `/report`, and `/analyze` workflows.
- **Acceptance Criteria**:
  - [ ] `SKILL.md` placed in `~/.gemini/config/skills/exam-analysis-master/SKILL.md`.
  - [ ] Support modes for PDF test walk-throughs and haphazard text/screenshot questions.
  - [ ] Fine-grained Question Taxonomy & Type tracking (e.g. Graph MST -> Adjacency Matrix vs Formulaic edge conditions).
  - [ ] Intuitive theorem/concept explanation on wrong answers.
  - [ ] Novel variation generator (testing underlying concepts).
  - [ ] Zero-rewrite `/wrap` session consolidation into `notes/` and `question_db.md`.
  - [ ] Analytics commands `/report [subject/topic]` and `/analyze [subject/topic/exam]`.
  - [ ] Quarto rendering compatibility (`_quarto.yml` / Obsidian markdown syntax).
