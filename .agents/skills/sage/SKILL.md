---
name: sage
description: Smart Analysis & Generation for Exams (SAGE) - Modular AI skill for exam practice, question taxonomy tracking, intuitive concept notes generation, novel variations testing, zero-rewrite session wrap, and user analytics (GATE, CDS, Physical Geography, general exams) targeting Obsidian & Quarto.
---

# SAGE — Smart Analysis & Generation for Exams (`sage`)

This skill empowers the AI to act as an exam coach and knowledge curator for competitive exams (e.g., **CDS**, **GATE**, **NDA**, **CAPF**, **Physical Geography**), generating exhaustive Obsidian-native notes, PYQ breakdown notes, and hard/tricky practice variations.

---

## 1. Automated PDF Notes & PYQ Extraction Workflow

When processing study material PDFs (handwritten notes + PYQ slides):

1. **PDF Pipeline Execution**:
   - Use `scripts/pdf_study_pipeline.py --pdf <file.pdf> --out <output.json>` to scan and extract page text and OCR content.
2. **Exhaustive Note & Point Inclusion Mandate**:
   - **Zero Omission**: Every single concept, bullet, definition, scientist name, date, formula, and diagram note from the PDF notes MUST be captured in the subject/topic notes.
   - **Rich Pedagogical Framing**: For every concept, provide:
     - Clear, intuitive explanations
     - First-principles derivations / logic
     - Real-world / daily life examples
     - Mind-expanding fun facts
     - Concrete memory mnemonics
3. **Tricky & Hard PYQs Filtering + Variation Engine**:
   - Filter PYQs that test edge cases, traps, multi-statement logic, or subtle distractor choices.
   - For every selected tricky PYQ:
     - Create an individual note in `content/[exam]/[subject]/notes/questions/`
     - Provide exhaustive step-by-step solution + intuition & distraction analysis.
     - Generate **Tier 1 / Tier 2 Novel Variations** testing the exact same underlying trap with modified numbers, reversed conditions, or multi-statement combinations in `content/[exam]/[subject]/notes/variations/`.

---

## 2. Vault Structure & Note Taxonomy Hierarchy

```text
content/
├── exams_config.md                 # Master Exams Registry
└── [exam]/                         # e.g., cds/ or gate-cs/
    ├── [exam]_overview.md          # Exam Overview Dashboard
    └── [subject]/                  # e.g., physical-geography/ or math/
        ├── [subject]_overview.md   # Subject Overview Dashboard (ALL Visual Analytics Graphs)
        ├── question_db.md          # Central Question Taxonomy Database (PURE Dataview Tables ONLY)
        └── notes/                  # Core Topic & Subtopic Notes
            ├── subtopics/          # Atomic Theorem / Specific Subtopic Notes
            ├── questions/          # Dedicated Individual Question Notes (q1.md, q2.md, etc.)
            └── variations/         # Dedicated Variation Notes (var1.md, var2.md, etc.)
```

---

### Dedicated Individual Question & Variation Files Mandate (STRICT)

- **INDIVIDUAL QUESTION & VARIATION FILES**: Do NOT pool questions or variations into single monolithic files (`questions.md` or `vars.md`).
- **FOLDER STRUCTURE**:
  - Questions live in dedicated directory: `content/[exam]/[subject]/notes/questions/q1.md`, `q2.md`, `q3.md`, etc.
  - Variations live in dedicated directory: `content/[exam]/[subject]/notes/variations/var1.md`, `var2.md`, `var3.md`, etc.
- **MANDATORY YAML FRONTMATTER PROPERTIES**: Every individual question and variation file MUST include:
  ```yaml
  ---
  exam: "CDS"
  subject: "Physical Geography"
  topic: "Universe and Solar System"
  subtopic: "Big Bang Theory"
  difficulty: "Hard"     # "Easy" | "Medium" | "Hard"
  status: "Correct"        # "Correct" | "Wrong"
  importance: "Important"  # "Normal" | "Important"
  tags: [cds, physical-geography, question]
  ---
  ```
- **DIRECT BACKLINKING**: Subtopic notes must link directly to the individual file (e.g. `[[cds/physical-geography/notes/questions/q1|Question 1: Lagrange Points Distance]]`).

### Short Filename Mandate across ALL Taxonomy Levels

- **STRICT MANDATE FOR ALL FILENAMES**: All files and directories across ALL levels (subjects, topics, subtopics, questions, variations) MUST use ultra-short, single-word or 1-2 word lowercase kebab-case names!
  - Subject directory: `cds/geography/` instead of `cds/physical-geography/`
  - Subject overview: `geography_overview.md`
  - Topic notes: `universe.md`
  - Subtopic notes: `big-bang.md`
  - Question notes: `q1.md`
  - Variation notes: `var1.md`

---

### Formatting & Title Standards (KISS Principle)

1. **Crisp Minimalist Titles**: Header titles MUST be clean names without em-dashes or AI fluff.
2. **Obsidian Frontmatter**: Store metadata strictly in YAML frontmatter properties.
3. **Dynamic Obsidian Dataview Queries**: `question_db.md` MUST use Obsidian `dataview` blocks.

