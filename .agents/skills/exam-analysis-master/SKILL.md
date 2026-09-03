---
name: exam-analysis-master
description: Modular AI skill for exam practice, question taxonomy tracking, intuitive concept notes generation, novel variations testing, zero-rewrite session wrap, and user analytics (GATE, CDS, general exams) targeting Obsidian & Quarto.
---

# Exam Analysis & Practice Master Skill (`exam-analysis-master`)

This skill empowers the AI to act as an exam coach and knowledge curator for competitive exams (e.g., **GATE**, **CDS**, or general learning), generating Obsidian-native notes exportable via **Quarto** or **Quartz**.

---

## 1. Vault Structure & Layout

```text
content/
├── exams_config.md                 # Master Exams Registry
└── [exam]/                         # e.g., gate-cs/ or cds/
    ├── gate_cs_overview.md         # Exam Overview Dashboard (Subject Bar Charts & Mistake Pie Charts)
    └── [subject]/                  # e.g., algorithms/ or elementary-mathematics/
        ├── algorithms_overview.md  # Subject Overview Dashboard (Chapter & Topic Bar Charts)
        ├── question_db.md          # Central Question Taxonomy Database (Dynamic Dataview Queries)
        ├── test_sessions/          # Full Test Scorecards (Obsidian Properties / YAML Frontmatter)
        ├── practice_sessions/      # Book/Screenshot Practice Session Logs
        └── notes/                  # Core Topic Notes (Theory + Direct Links to Variations)
            ├── questions/          # Modular Question Notes (Question + Derivation + Tier 1 Variations)
            └── variations/         # Modular Variation Notes (Tier 2 Topic & Tier 3 Chapter Variations)
```

---

### Formatting & Metadata Standards

1. **Crisp, Minimalist Titles (STRICTLY NO Em-Dashes, Hyphens, or AI Fluff)**:
   - STRICTLY FORBID em-dashes (`—`), hyphens (`-`), buzzwords (`Master Dashboard`, `Executive Hub`, `Overview`, `Theory & Concept Notes`), and bloated header titles.
   - Headers MUST BE concise, raw names without extra text:
     - Exam Index: `# CDS` (NOT `# CDS Overview` or `# CDS — Overview`)
     - Subject Index: `# Elementary Mathematics` (NOT `# Elementary Mathematics Overview`)
     - Question Database: `# Question Database` (NOT `# Question Database - Elementary Mathematics` or `# Question DB — Algorithms`)
     - Topic Note: `# Heights and Distances` (NOT `# Heights and Distances - Theory & Concept Notes`)
     - Question Note: `# GATE 2021 Q34` or `# CDS 2024 Q13`
     - Test Session: `# 2026-09-03 CDS Mock 01` (NOT `# Test Session: 2026-09-03 CDS Mock 01`)

2. **Obsidian Frontmatter & Properties (MANDATORY)**:
   - ALL test session scorecards and question notes MUST store metadata strictly in frontmatter YAML properties, NEVER as bullet points in the markdown body.
   - **Difficulty Property (`difficulty`)**: Manually specified by the user (`Easy`, `Medium`, `Hard`) per question/subtopic note:
   ```yaml
   ---
   exam: "CDS"
   subject: "Elementary Mathematics"
   topic: "Trigonometry"
   subtopic: "Heights and Distances"
   difficulty: "Medium" # Manually specified by user per question
   date: 2026-09-03
   source_file: "cds_2024_math_mock1.pdf"
   source_file_link: "[[content/cds/elementary-mathematics/test_sessions/2026-09-03_cds_mock_01|Mock Test 01]]"
   question_number: "Q13"
   status: "Wrong"
   mistake_category: "Formula Misapplication"
   tags: [cds, elementary-mathematics, trigonometry]
   ---
   ```

3. **Dynamic Obsidian Dataview Queries for Tables (MANDATORY)**:
   - Question Databases (`question_db.md`) MUST use Obsidian `dataview` codeblocks to render dynamic question logs automatically instead of hardcoded markdown tables:
   ```markdown
   ## Dynamic Question Log

   ```dataview
   TABLE 
       rows.question_type AS "Question Types / Specializations",
       rows.file.link AS "Logged Question Notes",
       rows.difficulty AS "Difficulty",
       rows.status AS "Status",
       rows.mistake_category AS "Mistake Category"
   FROM "content/cds/elementary-mathematics/notes/questions"
   GROUP BY topic + " > " + subtopic AS "Topic & Subtopic"
   ```
   ```

4. **Direct Variation Links (STRICTLY NO Intermediate Variation Indexes)**:
   - In topic notes and overview pages (`## Chapter Variations`), link DIRECTLY to specific variation files (e.g. `[[content/cds/elementary-mathematics/notes/variations/trigonometry_chapter_variations|Trigonometry Chapter Variations]]` or direct variation notes). Never link to non-existent or intermediate variation indexes.

5. **Collapsible Solutions (`> [!faq]- View Solution`)**:
   - ALWAYS use native Obsidian Callout foldables for collapsible solutions/hints.

6. **Centered Display Math**: Use `$$ ... $$` separated by blank lines for math formulas.

---

## 3. Visual Performance Analytics (Subject Bar Charts & Pie Charts)

The system automatically embeds clean `xychart-beta` bar charts and `pie` charts across all three levels:

### Tier 1: Exam-Level Dashboard (`content/[exam]/[exam]_overview.md`)
```mermaid
xychart-beta
    title "Subject-Wise Accuracy % (CDS)"
    x-axis ["Elementary Mathematics", "General Knowledge", "English"]
    y-axis "Accuracy %" 0 --> 100
    bar [66, 0, 0]
```
```mermaid
pie title Exam Mistake Categories across Subjects
    "Formula Misapplication" : 1
```

### Tier 2: Subject-Level Dashboard (`content/[exam]/[subject]/[subject]_overview.md`)
1. **Chapter-Wise Accuracy Bar Chart**:
```mermaid
xychart-beta
    title "Chapter-Wise Accuracy % (Elementary Mathematics)"
    x-axis ["Trigonometry", "Geometry", "Algebra", "Mensuration"]
    y-axis "Accuracy %" 0 --> 100
    bar [66, 0, 0, 0]
```
2. **Topic-Wise Accuracy Bar Chart**:
```mermaid
xychart-beta
    title "Topic-Wise Accuracy %"
    x-axis ["Heights & Distances", "Trigonometric Identities"]
    y-axis "Accuracy %" 0 --> 100
    bar [66, 0]
```
3. **Subtopic & Question Type Breakdown (Frequency & Difficulty/Question Level)**:
   - **Question-Level Status vs Subtopic Taxonomy**: Subtopics themselves are NOT marked as entirely wrong or correct. Outcome status (`Correct` vs `Wrong`) is tracked at the **individual question level** in note frontmatter.
   - Subtopic charts break down **question frequency by specialization and difficulty rating** (`Easy`, `Medium`, `Hard`) or show question accuracy percentages across subtopics.
   - Render per-topic pie/bar charts initialized with `%%{init: {'themeVariables': ...}}%%` so subtopics under the same parent topic share dedicated color shades.

```mermaid
%%{init: {'themeVariables': { 'pie1': '#1e3a8a', 'pie2': '#2563eb', 'pie3': '#3b82f6', 'pie4': '#60a5fa'}}}%%
pie title Triangles Subtopics Question Frequency & Difficulty
    "Incenter (Easy)" : 2
    "Orthocenter (Hard)" : 3
    "Circumcenter (Medium)" : 1
    "Centroid (Easy)" : 2
```

```mermaid
%%{init: {'themeVariables': { 'pie1': '#064e3b', 'pie2': '#047857', 'pie3': '#10b981', 'pie4': '#34d399'}}}%%
pie title Circles Subtopics Question Frequency & Difficulty
    "Tangents (Medium)" : 4
    "Secants (Easy)" : 2
    "Cyclic Quadrilaterals (Hard)" : 3
    "Chords (Medium)" : 1
```

---

## 4. Section Order Standard

Overview pages MUST follow this exact vertical order:
1. `# [Title]`
2. `## Topics & Notes` / `## Subjects`
3. `## Chapter Variations`
4. `## Performance Overview` *(Subject/Chapter/Topic Bar Charts & Mistake Pie Charts)*
5. `## Navigation`

---

## 5. Analytics Commands

- `/wrap` $\rightarrow$ Relocates questions, updates dataview queries, embeds visual charts, and updates frontmatter properties.
- `/report [subject/topic]` $\rightarrow$ Renders accuracy ratio, Mistake Category Pie Chart, Topic Accuracy Heatmap, and actionable weak area advice.
- `/analyze [subject/topic/exam]` $\rightarrow$ Renders exam weightage distribution, trap patterns, and high-yield focus topics with visual charts.
