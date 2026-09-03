---
name: sage
description: Smart Analysis & Generation for Exams (SAGE) - Modular AI skill for exam practice, question taxonomy tracking, intuitive concept notes generation, novel variations testing, zero-rewrite session wrap, and user analytics (GATE, CDS, general exams) targeting Obsidian & Quarto.
---

# SAGE — Smart Analysis & Generation for Exams (`sage`)

This skill empowers the AI to act as an exam coach and knowledge curator for competitive exams (e.g., **GATE**, **CDS**, or general learning), generating Obsidian-native notes exportable via **Quarto** or **Quartz**.

---

## 1. Vault Structure & Note Taxonomy Hierarchy

```text
content/
├── exams_config.md                 # Master Exams Registry
└── [exam]/                         # e.g., gate-cs/ or cds/
    ├── gate_cs_overview.md         # Exam Overview Dashboard (Subject-Level Accuracy & Exam Mistake Pie)
    └── [subject]/                  # e.g., algorithms/ or elementary-mathematics/
        ├── algorithms_overview.md  # Subject Overview Dashboard (ALL Visual Analytics Graphs)
        ├── question_db.md          # Central Question Taxonomy Database (PURE Dataview Tables ONLY - NO CHARTS)
        ├── test_sessions/          # Full Test Scorecards (YAML Frontmatter Properties)
        ├── practice_sessions/      # Book/Screenshot Practice Session Logs
        └── notes/                  # Core Topic & Subtopic Notes (Theorems, Intuition, Theory)
            ├── questions/          # Modular Question Notes (Question + Step-by-Step Explanation + Tier 1 Variations)
            └── variations/         # Modular Variation Notes (Tier 2 Topic & Tier 3 Chapter Variations)
```

---

### Note Content Guidelines by Taxonomy Level

### Consolidated Questions Page Mandate per Chapter (STRICT)

- **ONE CONSOLIDATED QUESTIONS PAGE PER CHAPTER**: Do NOT create separate `.md` files for individual practice questions (e.g. no individual `q12.md`, `q26.md`, etc.). All solved practice questions for a chapter/topic belong in **ONE single consolidated page** at `notes/questions.md`!
- **CONSOLIDATED QUESTIONS FORMAT**:
  - Main Heading: `# [TOPIC] Practice Questions` (e.g. `# Numbers Practice Questions`).
  - Section per question: `### Question 1 (Q12: [SHORT TITLE])`, `### Question 2 (Q26: [SHORT TITLE])`, etc.
  - Question statement & options directly under the heading.
  - Solution inside collapsible block: `> [!faq]- View Solution`.
- **SUBTOPIC LINKING**: Subtopic notes must link directly to the specific question heading anchor inside `notes/questions.md` (e.g. `[[cds/math/notes/questions#question-1-q12-continuous-equal-ratios|Question 1 (Q12)]]`).

### Short Filename Mandate across ALL Taxonomy Levels

- **STRICT MANDATE FOR ALL FILENAMES**: All files and directories across ALL levels (subjects, topics, subtopics, questions, variations) MUST use ultra-short, single-word or 1-2 word lowercase kebab-case names!
  - Subject directory: `cds/math/` instead of `cds/elementary-mathematics/`
  - Subject overview: `math_overview.md` instead of `elementary_mathematics_overview.md`
  - Topic notes: `numbers.md` instead of `number_system.md`
  - Subtopic notes: `ratios.md` instead of `ratios_and_proportions.md`
  - Question notes: `q12.md` instead of `pathfinder_number_system_q12.md`
  - Variation notes: `vars.md` instead of `number_system_variations.md`
- **RATIONALE**: Long folder and file names break breadcrumbs, overflow sidebars, and look ugly on Quartz/Quarto web publishing!


5. **Question Database (`[subject]/question_db.md`)**:
   - Resides strictly at the subject root (`content/[exam]/[subject]/question_db.md`).
   - Contains **PURE dynamic Dataview query tables ONLY**.
   - **STRICT MANDATE: ZERO CHARTS in `question_db.md`**.

---

### Strict Hierarchical Linking Rules

1. **Subject Overview Dashboards (`[subject]_overview.md`)**:
   - Links ONLY to **Topic Pages** (`[[content/cds/elementary-mathematics/notes/trigonometry_identities|Heights and Distances]]`).
   - STRICTLY NO direct links to regular practice questions or subtopics on subject overview pages!

2. **Topic Pages (`notes/[topic_slug].md`)**:
   - Links ONLY down to **Subtopic Pages** under `## Subtopics` (e.g. `[[content/cds/elementary-mathematics/notes/subtopics/two_point_angle_elevation|Two-Point Angle of Elevation]]`).
   - Links to **Topic Variations** under `## Variations`.
   - **NO question links or inline subtopic content inside topic pages!**

3. **Subtopic Notes (`notes/subtopics/[subtopic_slug].md`)**:
   - Contains: Specialized subtopic theory, formulaic properties, and proofs (e.g., proofs of theorems like Addendo property live HERE, NOT in question notes!).
   - `## Linked Practice Questions`: Direct links to individual regular practice question notes (e.g., `[[cds/math/notes/questions/q12|Q12]]`).
   - `## Variations`: **MANDATORY**: Direct links to all topic & subtopic variations inside `vars.md` (e.g., `[[cds/math/notes/variations/vars#variation-4-1001-principle|Variation 4: 1001 Principle]]`).


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

2. **Obsidian Frontmatter & Difficulty Properties (MANDATORY across ALL taxonomy levels)**:
   - Topic, Subtopic, and Question notes MUST store metadata strictly in YAML frontmatter properties.
   - **User-Defined Difficulty Property (`difficulty`)**: Every note level includes a `difficulty: "Easy" | "Medium" | "Hard"` property manually entered/edited by the user to rate difficulty!

   - **Topic Note Frontmatter Example**:
     ```yaml
     ---
     exam: "CDS"
     subject: "Elementary Mathematics"
     topic: "Trigonometry"
     difficulty: "Hard" # User manual rating for entire topic
     tags: [cds, elementary-mathematics, trigonometry, topic]
     ---
     ```

   - **Subtopic Note Frontmatter Example**:
     ```yaml
     ---
     exam: "CDS"
     subject: "Elementary Mathematics"
     topic: "Trigonometry"
     subtopic: "Heights and Distances"
     difficulty: "Medium" # User manual rating for subtopic
     tags: [cds, elementary-mathematics, subtopic]
     ---
     ```

   - **Question Note Frontmatter Example**:
     ```yaml
     ---
     exam: "CDS"
     subject: "Elementary Mathematics"
     topic: "Trigonometry"
     subtopic: "Heights and Distances"
     difficulty: "Medium" # User manual rating for question
     date: 2026-09-03
     source_file: "cds_2024_math_mock1.pdf"
     question_number: "Q13"
     status: "Wrong"
     mistake_category: "Formula Misapplication"
     tags: [cds, elementary-mathematics, trigonometry, question]
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

## 2. Visual Analytics Graph Distribution Standard

All visual analytics graphs MUST be placed **at the bottom of overview files** under `## Performance Overview` (below tables, theory, variation links, and topic links).

### 1. Exam Overview (`[exam]_overview.md`)
- **Subject-Wise Accuracy Bar Chart**: `xychart-beta` comparing overall subject accuracy.
- **Exam-Wide Mistake Breakdown Pie Chart**: `pie` title `Exam Mistakes`.

### 2. Subject Overview (`[subject]_overview.md`) — THE CENTRAL GRAPH HUB
- **Test Series Score Trendline**: `xychart-beta` title `"Score Trend"` showing mock test score progression.
- **Chapter-Wise Accuracy Bar Chart**: `xychart-beta` title `"Chapter Accuracy"`.
- **Topic-Wise Accuracy Bar Chart**: `xychart-beta` title `"Topic Accuracy"`.
- **Per-Topic Subtopic Difficulty Pie Charts**: `pie` charts with explicit `%%{init: {'themeVariables': ...}}%%` color shade palettes per parent topic.
  - **MANDATORY RULE**: All difficulty suffix tags in pie charts (e.g., `"Two-Point Angle (Medium)"`, `"Heights & Distances (Hard)"`) MUST strictly read directly from the user's manual `difficulty` YAML frontmatter properties set in the respective Topic/Subtopic note files!
- **Subject Mistake Breakdown Pie Chart**: `pie` title `Mistake Breakdown`.

### 3. Subject-Level Question Database (`[subject]/question_db.md`)
- **ZERO CHARTS**: Contains PURE Dataview tables ONLY!

---

### Mermaid Title Length & Overflow Rules (STRICT MANDATE)

- **Concise Titles Only (Max 2-3 Words)**: NEVER write long pie/bar chart titles like `pie title Triangles Subtopics Question Frequency & Difficulty` because Obsidian/Mermaid clips and overflows long SVG title text on the left margin!
- **Mandatory Short Titles**:
  - `pie title Triangles Difficulty`
  - `pie title Circles Difficulty`
  - `pie title Trig & Algebra Difficulty`
  - `pie title Mistake Breakdown`
  - `xychart-beta title "Chapter Accuracy"`
  - `xychart-beta title "Topic Accuracy"`
  - `xychart-beta title "Score Trend"`

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
