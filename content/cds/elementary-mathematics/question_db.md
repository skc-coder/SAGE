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
    title "Score Trend"
    x-axis ["Mock 01", "Mock 02"]
    y-axis "Accuracy %" 0 --> 100
    bar [66.67, 66.67]
```

### 2. Mistake Breakdown by Category
```mermaid
pie title Mistake Breakdown
    "Conceptual Gap" : 3
    "Calculation Error" : 2
    "Formula Misapplication" : 1
```

---

## Navigation
- [[content/cds/elementary-mathematics/elementary_mathematics_overview|Elementary Mathematics]]
- [[content/cds/cds_overview|CDS]]
