# SAGE — Smart Analysis & Generation for Exams

SAGE is an AI-powered system designed to analyze practice sessions, track question databases with fine-grained taxonomy, generate concept notes, ask novel variations, and render clean notes using **Obsidian** and **Quarto** / **Quartz**.

## Setup & Installation

```bash
git clone https://github.com/skc-coder/SAGE.git
cd SAGE
npm install
```

## Running & Publishing the Site

```bash
# Start local Quartz / web development server
npx quartz build --serve

# Or render with Quarto (if installed)
quarto render content/
```

## Update & Run

```bash
git pull origin v5
npx quartz build --serve
```

---

## AI Skill Usage Guidelines

The system uses the global AI skill `exam-analysis-master` (`~/.gemini/config/skills/exam-analysis-master/SKILL.md`).

### Key Commands:
- `/wrap`: Consolidates temporary session notes from `tmp/session_id/` into `notes/`, updating indices and `question_db.md` without rewriting text.
- `/report [subject/topic]`: Displays user accuracy, mistake patterns, and weak areas.
- `/analyze [subject/topic/exam]`: Displays exam focus areas, high-frequency question types, and preparation recommendations.
