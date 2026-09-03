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

### Dedicated Individual Question & Variation Files Mandate (STRICT)

- **INDIVIDUAL QUESTION & VARIATION FILES**: Do NOT pool questions or variations into single monolithic files (`questions.md` or `vars.md`).
- **FOLDER STRUCTURE**:
  - Questions live in dedicated directory: `content/[exam]/[subject]/notes/questions/q1.md`, `q2.md`, `q3.md`, etc.
  - Variations live in dedicated directory: `content/[exam]/[subject]/notes/variations/var1.md`, `var2.md`, `var3.md`, etc.
- **MANDATORY YAML FRONTMATTER PROPERTIES**: Every individual question and variation file MUST include:
  ```yaml
  ---
  exam: "CDS"
  subject: "Math"
  topic: "HCF and LCM"
  subtopic: "LCM Models"
  difficulty: "Medium"     # "Easy" | "Medium" | "Hard"
  status: "Correct"        # "Correct" | "Wrong"
  importance: "Important"  # "Normal" | "Important"
  tags: [cds, math, question]
  ---
  ```
- **DIRECT BACKLINKING**: Subtopic notes must link directly to the individual file (e.g. `[[cds/math/notes/questions/q11|Question 11: Modular Fast Power Reduction]]`).

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
   - Links ONLY to **Topic Pages** (`[[cds/math/notes/trigonometry|Ch 20. Trigonometry]]`).
   - **MANDATORY**: Always prefix the link display text with the explicit Chapter Number (e.g. `[[cds/math/notes/hcf_lcm|Ch 3. HCF and LCM of Numbers]]`).
   - STRICTLY NO direct links to regular practice questions or subtopics on subject overview pages!


2. **Topic Pages (`notes/[topic_slug].md`)**:
   - Links ONLY down to **Subtopic Pages** under `## Subtopics` (e.g. `[[cds/elementary-mathematics/notes/subtopics/two_point_angle_elevation|Two-Point Angle of Elevation]]`).
   - Links to **Topic Variations** under `## Variations`.
   - **NO question links or inline subtopic content inside topic pages!**

3. **Subtopic Notes (`notes/subtopics/[subtopic_slug].md`)**:
   - Contains: Specialized subtopic theory, formulaic properties, and proofs (e.g., proofs of theorems like Addendo property live HERE, NOT in question notes!).
   - `## Linked Practice Questions`: Direct links to individual regular practice question notes (e.g., `[[cds/math/notes/questions/q12|Q12]]`).
   - `## Variations`: **MANDATORY**: Direct links to all topic & subtopic variations inside `vars.md` (e.g., `[[cds/math/notes/variations/vars#variation-4-1001-principle|Variation 4: 1001 Principle]]`).


---

### Atomic Theorem Notes & Hyperlink Graph Mandate (STRICT)

- **ATOMIC THEOREM PAGES**: Major independent mathematical theorems, principles, and core techniques (e.g. Fermat's Little Theorem, Chinese Remainder Theorem, Euler's Totient Theorem, Euclidean Division Algorithm) MUST be extracted into their own dedicated subtopic/theorem notes in `notes/subtopics/[theorem_slug].md`.
- **OBSIDIAN WIKI-LINK GRAPH MESH**: Main topic notes, subtopic notes, question notes, and variation notes MUST hyper-link to these atomic theorem pages using Obsidian wiki-links (e.g. `[[cds/math/notes/subtopics/flt|Fermat's Little Theorem]]` or `[[cds/math/notes/subtopics/crt|Chinese Remainder Theorem]]`).
- **NO MONOLITHIC COPIED TEXT**: Instead of repeating 3-page theorem proofs inside multiple question files or main topic files, link directly to the atomic theorem note!

### Zero-Omission Instant Note Persistence Rule (STRICT)

- **ALWAYS WRITE/UPDATE VAULT NOTES INSTANTLY**: Every piece of theory, intuition, mathematical proof, theorem derivation, worked example, or concept explanation provided in chat MUST be immediately saved/appended into the corresponding vault note file (`content/[exam]/[subject]/notes/...`) BEFORE responding!
- **NO CHAT-ONLY EXPLANATIONS**: Never provide an explanation in chat without persisting it in the Obsidian vault.
- **NO WAITING FOR EXPLICIT USER PROMPTS**: Do not wait for the user to ask "did you save this?". Save every explanation automatically into the vault.

### Intuition & Mathematical Rigor Mandate (STRICT)

- **JARGON WITH IMMEDIATE READABILITY**: You ARE encouraged to use formal mathematical terms and notations (e.g. congruences $a \equiv b \pmod m$, prime factorizations, quotients, linear combinations, modular inverses), BUT you MUST immediately translate every step into clear, intuitive, plain-English explanations.
- **NO UNEXPLAINED SYMBOL DUMPING**: Never dump raw equations or modular arithmetic lines without explaining *why* the algebraic step was taken.
- **NO LONG HORIZONTAL INLINE EQUATION RUN-ONS (STRICT READABILITY RULE)**:
  - NEVER dump long multi-step equations, stream-of-consciousness algebra, or inline derivations wrapped in inline math `$ ... $` across multiple lines. Long inline math equations cause hideous horizontal overflow, word wrapping glitches, and unreadable text blobs in Obsidian and Quartz!
  - **STRICT NEWLINES & PUNCTUATION FOR EQUATIONS & EXPLANATIONS**:
    - Every explanatory step MUST end with proper punctuation (period `.`, colon `:`, or semicolon `;`).
    - NEVER append an equation or a second sentence directly after inline math on the same line without a newline or bullet point.
    - Every standalone mathematical step or equation MUST be placed on its own separate line using display math `$$ ... $$` or as an indented bullet point `- ...`.
    - Example of **FORBIDDEN BAD FORMAT**: `Factor out $x^2$: $P(x) = 36x^2(3x^2+5x-2)$ Split middle term $5x = 6x-x$: $P(x) = 36x^2(3x-1)(x+2)`
    - Example of **REQUIRED GOOD FORMAT**:
      - Factor out $x^2$:
        $$P(x) = 36x^2(3x^2 + 5x - 2)$$
      - Split middle term $5x = 6x - x$:
        $$P(x) = 36x^2(3x - 1)(x + 2)$$
- **NO CHILDISH ANALOGIES**: Strictly avoid kindergarten analogies ("sweets in boxes", "pizza slices", "friends sharing toys"). Keep explanations sharp, mature, and exam-focused.

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

## 4. Analytics & Study Commands

- `/study chapter [x]` $\rightarrow$ Automated bookmark lookup & text extraction using `scripts/chapter_study_helper.py`, topic & subtopic note creation, key theorem/pattern categorization, and unique practice question session setup.
- `/wrap` $\rightarrow$ Relocates questions, updates dataview queries, embeds visual charts, and updates frontmatter properties.
- `/report [subject/topic]` $\rightarrow$ Renders accuracy ratio, Mistake Category Pie Chart, Topic Accuracy Heatmap, and actionable weak area advice.
- `/analyze [subject/topic/exam]` $\rightarrow$ Renders exam weightage distribution, trap patterns, and high-yield focus topics with visual charts.

