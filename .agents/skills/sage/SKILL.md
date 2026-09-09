---
name: sage
description: Smart Analysis & Generation for Exams (SAGE) - Modular AI skill for exam practice, question taxonomy tracking, intuitive concept notes generation, novel variations testing, zero-rewrite session wrap, and user analytics (GATE, CDS, Physical Geography, general exams) targeting Obsidian & Quarto.
---

# SAGE — Smart Analysis & Generation for Exams (`sage`)

This skill empowers the AI to act as an exam coach and knowledge curator for competitive exams (e.g., **CDS**, **GATE**, **NDA**, **CAPF**, **Physical Geography**), generating exhaustive Obsidian-native notes, PYQ breakdown notes, and hard/tricky practice variations.

---

## 0. Lessons Learned & Execution Guardrails (CRITICAL)

When processing any PDF study material:

1. **PDF Hygiene & Git Policy**:
   - **NEVER stage or commit PDFs or large binary image files** to Git (`.gitignore` must contain `pdfs/`, `*.pdf`, `*.png`).
   - Run `git rm --cached` if any media file was accidentally tracked.
2. **Background Task Lifecycle**:
   - **ZERO lingering tasks**: Always kill background tasks (`manage_task kill`) before finishing any turn.
   - Do NOT poll background tasks in a loop.
3. **LaTeX Math Formatting Rules**:
   - **Single backslashes in raw strings**: Never double-escape or tab-character corrupt LaTeX commands (`\text{}`, `\times`, `\rightarrow`, `\approx`).
   - **Dollar Sign Balance**: Ensure every `$` is strictly matched on the same line or explicitly escaped (`\$`).
4. **Exhaustive Note Extraction**:
   - **Line-by-Line & Fact-by-Fact**: Cover every handwritten point, definition, formula, diagram annotation, and option.
   - Provide intuitive explanations, derivations, real-world examples, and memory mnemonics.

---

## 1. Automated PDF Notes & PYQ Extraction Workflow

When processing study material PDFs (handwritten notes + PYQ slides):

1. **Fast Local OCR Pipeline Execution**:
   - Extract page text and OCR content using PyMuPDF (`fitz`) and Tesseract OCR into `/tmp/pdf_extraction.json`.
   - Avoid external API rate limits by relying on fast local extraction.
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
     - Create an individual note in `content/[exam]/[subject]/notes/questions/q1.md`, `q2.md`, etc.
     - Provide exhaustive step-by-step solution + intuition & distraction analysis.
     - Generate **Tier 1 / Tier 2 Novel Variations** testing the exact same underlying trap in `content/[exam]/[subject]/notes/variations/var1.md`, `var2.md`, etc.

---

## 2. Vault Structure & Note Taxonomy Hierarchy

```text
content/
├── exams_config.md                 # Master Exams Registry
└── [exam]/                         # e.g., cds/ or gate-cs/
    ├── [exam]_overview.md          # Exam Overview Dashboard
    └── [subject]/                  # e.g., geography/ or math/
        ├── [subject]_overview.md   # Subject Overview Dashboard (ALL Visual Analytics Graphs)
        ├── question_db.md          # Central Question Taxonomy Database (PURE Dataview Tables ONLY)
        └── notes/                  # Core Topic & Subtopic Notes
            ├── questions/          # Dedicated Individual Question Notes (q1.md, q2.md, etc.)
            └── variations/         # Dedicated Variation Notes (var1.md, var2.md, etc.)
```

---

## 3. Dedicated Individual Question & Variation Files Mandate (STRICT)

- **INDIVIDUAL QUESTION & VARIATION FILES**: Do NOT pool questions or variations into single monolithic files.
- **FOLDER STRUCTURE**:
  - Questions live in dedicated directory: `content/[exam]/[subject]/notes/questions/q1.md`, `q2.md`, etc.
  - Variations live in dedicated directory: `content/[exam]/[subject]/notes/variations/var1.md`, `var2.md`, etc.
- **MANDATORY YAML FRONTMATTER PROPERTIES**: Every individual question and variation file MUST include:
  ```yaml
  ---
  exam: "CDS"
  subject: "Geography"
  topic: "Universe and Solar System"
  subtopic: "Big Bang Theory"
  difficulty: "Hard"     # "Easy" | "Medium" | "Hard"
  status: "Correct"        # "Correct" | "Wrong"
  importance: "Important"  # "Normal" | "Important"
  tags: [cds, geography, question]
  ---
  ```
- **DIRECT BACKLINKING**: Subtopic notes must link directly to the individual file (e.g. `[[cds/geography/notes/questions/q1|Question 1: Lagrange Points Distance]]`).

### Short Filename Mandate across ALL Taxonomy Levels

- **STRICT MANDATE FOR ALL FILENAMES**: All files and directories across ALL levels (subjects, topics, subtopics, questions, variations) MUST use ultra-short, single-word or 1-2 word lowercase kebab-case names!
  - Subject directory: `cds/geography/` instead of `cds/physical-geography/`
  - Subject overview: `geography_overview.md`
  - Topic notes: `universe.md`
  - Subtopic notes: `big-bang.md`
  - Question notes: `q1.md`
  - Variation notes: `var1.md`

---

## 4. Slash Command `/process-pdf` Workflow

When the user triggers `/process-pdf <pdf_path> [exam] [subject]`, execute the following automated steps:

1. **Initialize Local Extraction**: Extract all embedded text and Tesseract OCR lines into `/tmp/pdf_extract.json`.
2. **Identify Chapter/Topic Boundaries**: Group pages into discrete chapters/topics.
3. **Generate Exhaustive Explanatory Notes**: Write/update topic Markdown files in `content/[exam]/[subject]/notes/` covering every line, definition, formula, diagram annotation, and option.
4. **Extract Questions & Variations**: Create `q1.md`..`qN.md` and `var1.md`..`varN.md`.
5. **Verify LaTeX & Frontmatter**: Run LaTeX checker to ensure 0 dollar-sign or math syntax errors.
6. **Git Commit & Auto-Push**: Stage changes (excluding PDFs/images), commit with descriptive message, and push to Git remote.
7. **Clean Up Tasks**: Verify zero background tasks running before completing turn.
