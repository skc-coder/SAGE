# Question Database

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

---

## Performance Overview

### 1. Test Series Marks Trendline
```mermaid
xychart-beta
    title "Test Series Score Progression (Elementary Mathematics)"
    x-axis ["Mock 01 (Trig)", "Mock 02 (Extensive Math)"]
    y-axis "Accuracy %" 0 --> 100
    bar [66.67, 66.67]
```

### 2. Chapter-Wise & Topic-Wise Accuracy
```mermaid
xychart-beta
    title "Chapter-Wise Accuracy %"
    x-axis ["Trigonometry", "Geometry", "Circles & Polygons", "Algebra", "Mensuration"]
    y-axis "Accuracy %" 0 --> 100
    bar [100, 50, 66, 50, 100]
```

```mermaid
xychart-beta
    title "Topic-Wise Accuracy %"
    x-axis ["Heights & Distances", "Triangles", "Circles", "Polygons", "Algebra"]
    y-axis "Accuracy %" 0 --> 100
    bar [100, 75, 75, 50, 50]
```

### 3. Subtopic Question Frequency & Difficulty Distribution
```mermaid
%%{init: {'themeVariables': { 'pie1': '#1e3a8a', 'pie2': '#2563eb', 'pie3': '#3b82f6', 'pie4': '#60a5fa'}}}%%
pie title Triangles Subtopics Question Frequency & Difficulty
    "Incenter (Easy)" : 1
    "Orthocenter (Hard)" : 1
    "Circumcenter (Medium)" : 1
    "Centroid (Easy)" : 1
```

```mermaid
%%{init: {'themeVariables': { 'pie1': '#064e3b', 'pie2': '#047857', 'pie3': '#10b981', 'pie4': '#34d399'}}}%%
pie title Circles Subtopics Question Frequency & Difficulty
    "Tangents (Medium)" : 1
    "Secants (Easy)" : 1
    "Cyclic Quadrilaterals (Hard)" : 1
    "Chords (Medium)" : 1
```

### 4. Mistake Breakdown by Category
```mermaid
pie title Subject Mistake Category Breakdown
    "Conceptual Gap" : 3
    "Calculation Error" : 2
    "Formula Misapplication" : 1
```

---

## Navigation
- [[content/cds/elementary-mathematics/elementary_mathematics_overview|Elementary Mathematics]]
- [[content/cds/cds_overview|CDS]]
