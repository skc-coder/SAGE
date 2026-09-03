# Question Database

## Performance Overview

### Mistake Distribution
```mermaid
pie title Mistake Categories
    "Calculation Error" : 1
```

### Topic Accuracy %
```mermaid
xychart-beta
    title "Topic Accuracy %"
    x-axis ["Number of MSTs", "MST Uniqueness"]
    y-axis "Accuracy %" 0 --> 100
    bar [0, 100]
```

---


## Dynamic Obsidian Dataview Query

```dataview
TABLE 
    rows.question_type AS "Question Types / Specializations",
    rows.file.link AS "Logged Question Notes"
FROM "content/gate-cs/algorithms/notes"
GROUP BY topic + " > " + subtopic AS "Topic & Subtopic"
```

