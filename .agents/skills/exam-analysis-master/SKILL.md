---
name: exam-analysis-master
description: Modular AI skill for exam practice, question taxonomy tracking, intuitive concept notes generation, novel variations testing, zero-rewrite session wrap, and user analytics (GATE, CDS, general exams) targeting Obsidian & Quarto.
---

# Exam Analysis & Practice Master Skill (`exam-analysis-master`)

This skill empowers the AI to act as an exam coach and knowledge curator for competitive exams (e.g., **GATE**, **CDS**, or general learning), generating Obsidian-native notes exportable via **Quarto** or **Quartz**.

---

## 1. Vault Structure & Note Taxonomy Hierarchy

```text
content/
├── exams_config.md                 # Master Exams Registry
└── [exam]/                         # e.g., gate-cs/ or cds/
    ├── gate_cs_overview.md         # Exam Overview Dashboard
    └── [subject]/                  # e.g., algorithms/ or elementary-mathematics/
        ├── algorithms_overview.md  # Subject / Chapter Overview Dashboard
        ├── question_db.md          # Central Question Taxonomy Database (Dynamic Dataview Queries)
        ├── test_sessions/          # Full Test Scorecards (YAML Frontmatter Properties)
        ├── practice_sessions/      # Book/Screenshot Practice Session Logs
        └── notes/                  # Core Topic & Subtopic Notes (Theorems, Intuition, Theory)
            ├── questions/          # Modular Question Notes (Question + Step-by-Step Explanation + Tier 1 Variations)
            └── variations/         # Modular Variation Notes (Tier 2 Topic & Tier 3 Chapter Variations)
```

---

### Note Content Guidelines by Taxonomy Level

1. **Question Notes (`notes/questions/[question_slug].md`)**:
   - Contains: Exact question statement + Step-by-step mathematical explanation & derivation + Root cause analysis + Tier 1 question variations.
   - Frontmatter metadata: `exam`, `subject`, `topic`, `subtopic`, `difficulty`, `status`, `mistake_category`.

2. **Topic Notes (`notes/[topic_slug].md`)**:
   - Contains: Core theory, fundamental theorems, intuition, geometric/algebraic proofs, and formulaic properties.
   - Subtopic sections (`### [Subtopic Name]`): Contains theory for that subtopic + specialized question headers linking directly to individual question notes.

3. **Variation Notes (`notes/variations/`)**:
   - Contains novel Tier 2 (Topic Level) and Tier 3 (Chapter Level) variations with collapsible solutions (`> [!faq]- View Solution`).

---

### Strict Hierarchical Linking Rules

1. **Subject & Chapter Overview Dashboards**:
   - Links ONLY to **Topic Pages** (`[[content/cds/elementary-mathematics/notes/trigonometry_identities|Heights and Distances]]`).
   - STRICTLY NO direct links to regular practice questions on subject/chapter overview pages!
   - MAY link directly to **Subject-wide & Chapter-wide Variations** under `## Chapter Variations`.

2. **Topic Pages**:
   - Links down to **Subtopic Section Headers** (`### Specialized Questions: Two-Point Angle`).
   - Links directly to **Topic-level Variations** (`## Topic Variations`).

3. **Subtopic Section Headers (Inside Topic Pages)**:
   - This is the **ONLY place** where direct links to individual regular practice question notes (e.g., `[[content/cds/elementary-mathematics/notes/questions/cds_2024_math_q13|CDS 2024 Q13]]`) are stored!

---

### Formatting & Title Standards (KISS Principle)

1. **Crisp Minimalist Titles (STRICTLY NO Em-Dashes, Hyphens, or AI Fluff)**:
   - Header titles MUST be raw names without extra fluff:
     - Exam Index: `# CDS` (NOT `# CDS Overview`)
     - Subject Index: `# Elementary Mathematics`
     - Question Database: `# Question Database`
     - Topic Note: `# Heights and Distances` (NOT `# Heights and Distances - Theory & Concept Notes`)
     - Question Note: `# CDS 2024 Q13`
     - Test Session: `# 2026-09-03 CDS Mock 01`

2. **Obsidian Frontmatter Properties (MANDATORY)**:
   - All test scorecards and question notes MUST store metadata in frontmatter YAML properties:
   ```yaml
   ---
   exam: "CDS"
   subject: "Elementary Mathematics"
   topic: "Trigonometry"
   subtopic: "Heights and Distances"
   difficulty: "Medium" # Manually entered by user (Easy / Medium / Hard)
   date: 2026-09-03
   source_file: "cds_2024_math_mock1.pdf"
   question_number: "Q13"
   status: "Wrong"
   mistake_category: "Formula Misapplication"
   tags: [cds, elementary-mathematics, trigonometry]
   ---
   ```

3. **Dynamic Obsidian Dataview Queries for Tables (MANDATORY)**:
   - `question_db.md` MUST use Obsidian `dataview` blocks:
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

---

### Graph Placement Rules Across Files

1. **Exam Overview (`[exam]_overview.md`)**:
   - Subject-wise accuracy bar chart (`xychart-beta`)
   - Chapter-wise & Topic-wise accuracy bar charts (`xychart-beta`)
   - Exam-wide mistake category pie chart (`pie`)

2. **Subject Overview (`[subject]_overview.md`)**:
   - Chapter-wise & Topic-wise accuracy bar charts (`xychart-beta`)
   - Per-topic Subtopic Question Frequency & Difficulty pie charts (`pie`)

3. **Subject-Level Question Database (`[subject]/question_db.md`)**:
   - Dynamic Question Log Dataview table
   - Test Series Marks Trendline (`xychart-beta`)
   - Subject Mistake Category Breakdown (`pie`)

---

### Mermaid Title Length & Overflow Rules (STRICT MANDATE)

- **Concise Titles Only (Max 3-4 Words)**: NEVER write long pie chart titles like `pie title Triangles Subtopics Question Frequency & Difficulty` because Obsidian/Mermaid clips and overflows long SVG title text on the left margin!
- **Allowed Concise Titles**:
  - `pie title Triangles Difficulty`
  - `pie title Circles Difficulty`
  - `pie title Mistake Breakdown`
  - `xychart-beta title "Topic Accuracy"`

---

## 3. Section Order Standard

All overview and topic files MUST strictly follow this vertical order:
1. `# [Title]`
2. `## Theory, Intuition & Formulas` (or `## Topics & Notes` on Subject pages)
3. `## Subtopics & Specialized Questions` (Topic pages)
4. `## Variations` (Subject/Chapter/Topic level direct variation links)
5. `## Performance Overview` *(Bar charts & themeVariables color-shaded Pie charts placed HERE at the bottom)*
6. `## Navigation`

---

## 4. Analytics Commands

- `/wrap` $\rightarrow$ Relocates questions, updates dataview queries, embeds visual charts, and updates frontmatter properties.
- `/report [subject/topic]` $\rightarrow$ Renders accuracy ratio, Mistake Category Pie Chart, Topic Accuracy Heatmap, and actionable weak area advice.
- `/analyze [subject/topic/exam]` $\rightarrow$ Renders exam weightage distribution, trap patterns, and high-yield focus topics with visual charts.
