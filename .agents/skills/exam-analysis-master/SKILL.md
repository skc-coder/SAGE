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

1. **Question Notes (`notes/questions/[question_slug].md`)**:
   - Contains: Exact question statement + Step-by-step mathematical explanation & derivation + Root cause analysis + Tier 1 question variations.
   - Frontmatter metadata: `exam`, `subject`, `topic`, `subtopic`, `difficulty` (`Easy` | `Medium` | `Hard` - specified manually by user), `status`, `mistake_category`.

2. **Topic Notes (`notes/[topic_slug].md`)**:
   - Contains: Topic-level core theory, fundamental theorems, and intuition.
   - `## Subtopics`: Contains **ONLY wikilinks to dedicated Subtopic Pages** (e.g. `[[content/cds/elementary-mathematics/notes/subtopics/two_point_angle_elevation|Two-Point Angle of Elevation]]`).
   - **STRICT MANDATE: NO subtopic content or question links live directly inside topic notes!**

3. **Subtopic Notes (`notes/subtopics/[subtopic_slug].md`)**:
   - Contains: Specialized subtopic theory, formulaic properties, and proofs.
   - `## Linked Practice Questions`: The **ONLY place** where direct links to individual regular practice question notes (e.g., `[[content/cds/elementary-mathematics/notes/questions/cds_2024_math_q13|CDS 2024 Q13]]`) are stored!

4. **Variation Notes (`notes/variations/`)**:
   - Contains novel Tier 2 (Topic Level) and Tier 3 (Chapter Level) variations with collapsible solutions (`> [!faq]- View Solution`).

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

3. **Subtopic Pages (`notes/subtopics/[subtopic_slug].md`)**:
   - Contains subtopic notes & theory.
   - This is the **ONLY place** where direct links to individual practice question notes live!

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
