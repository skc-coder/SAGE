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
├── exams_config.md                 # Registry of target exams & active subjects
└── [exam]/                         # e.g., gate-cs/ or cds/
    └── [subject]/                  # e.g., algorithms/
        ├── index.md                # Subject master index (Topics -> Questions & Direct Variations)
        ├── question_db.md          # Central Question & Taxonomy Database (Dataview compatible)
        ├── test_sessions/          # Log of test sessions
        ├── notes/                  # Core Topic Notes (Theory + Links)
        │   ├── questions/          # Modular Question Notes (Question + Derivation + Tier 1 Variations)
        │   └── variations/         # Modular Variation Notes (Tier 2 Topic & Tier 3 Chapter Variations)
        └── tmp/                    # Active session workspace
            └── [session_id]/       # Temporary session files
```

---

## 2. Formatting Standards

1. **Short & Crisp Titles**: Always use short 2-4 word titles:
   - Topic Note: `# Counting MSTs`
   - Question Note: `# GATE 2021 Q34`
   - Variations Note: `# Counting MSTs Variations`
2. **Clean Bullet Links (No Icons / No Code Ticks)**:
   - Do NOT place `❌` or `✅` icons next to topics on index pages.
   - Do NOT wrap status inside inline code ticks (`` `[Status: ❌]` ``).
   - Use clean, direct wikilinks: `[[content/gate-cs/algorithms/notes/counting_msts_formulaic|Counting MSTs]]`.
3. **Collapsible Solutions (`> [!faq]- View Solution`)**:
   - ALWAYS use native Obsidian Callout foldables for collapsible solutions/hints:
     ```markdown
     > [!faq]- View Solution
     > Edge $e_5$ (weight $2$) and $e_1$ (weight $3$) are strictly chosen first.
     >
     > $$ w(e_1)=3, \quad w(e_2)=5 $$
     ```
4. **Centered Display Math**: Use `$$ ... $$` separated by blank lines for math formulas.
5. **Obsidian Frontmatter**: Every note tracks metadata in frontmatter (never repeat redundant context bullet lists in the body):
   ```yaml
   ---
   exam: "GATE CS"
   subject: "Algorithms"
   topic: "Minimum Spanning Trees"
   subtopic: "Number of MSTs"
   question_type: "Formulaic Edge Conditions"
   source: "GATE CS 2021 Set 1 Q34"
   status: "Wrong"
   mistake_category: "Calculation Error"
   tags: [gate-cs, algorithms, mst]
   date: 2026-09-03
   ---
   ```

---

## 3. Interactive Practice Workflow

When user provides a question (via PDF walkthrough, text, or screenshot):

1. **Ingest & Taxonomy Breakdown**: Extract Exam, Year, Question Number, Subject, Topic, Subtopic, and Specialization.
2. **Evaluation & Explanation (If Wrong / Unsure)**:
   - Provide root cause, intuition, mathematical theorems, and step-by-step derivation.
   - Categorize mistake type (`Calculation Error`, `Conceptual Gap`, `Overlooked Edge Case`, `Misread Question`).
3. **Generate Novel Variations (3 Tiers)**:
   - **Tier 1 (Direct Question Variation)**: Placed inside `notes/questions/[question_slug].md`.
   - **Tier 2 (Topic Variation)**: Placed inside `notes/variations/[topic_slug]_variations.md`.
   - **Tier 3 (Chapter / Multi-Topic Variation)**: Placed inside `notes/variations/[variation_slug].md` and linked directly under `Chapter Variations` in `index.md`.

---

## 4. Modular Note Architecture & `/wrap` Pipeline

When user types `/wrap`:

1. **Question Notes (`notes/questions/[question_slug].md`)**:
   - Holds original question statement in blockquote + collapsible derivation (`> [!faq]- View Solution & Derivation`) + Tier 1 variations.
2. **Variation Notes (`notes/variations/[variation_slug].md`)**:
   - Holds dedicated variation problems with collapsible solutions (`> [!faq]- View Solution`).
3. **Topic Notes (`notes/[topic_slug].md`)**:
   - Holds core theory + index of links to Question Notes and Topic Variation Notes.
4. **Master Index (`[exam]/[subject]/index.md`)**:
   - Links directly to Topic Notes and **Directly to Chapter Variation Notes** (no intermediate indexer page).
5. **Database (`[exam]/[subject]/question_db.md`)**:
   - Topic-centric rows tracking subtopics, specializations, linked question notes, performance, and logged mistake categories.

---

## 5. Analytics Commands

- `/report [subject/topic]` $\rightarrow$ Renders accuracy ratio, mistake category breakdown, and weak areas.
- `/analyze [subject/topic/exam]` $\rightarrow$ Renders exam weightage, trap patterns, and high-yield focus topics.
