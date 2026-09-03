# Question Database — Algorithms (GATE CS)

This database tracks every question asked, its fine-grained taxonomy specialization, source, user performance, and linked concept note.

## Questions Log

| Source | Topic | Subtopic | Question Type / Specialization | Status | Note Link |
| :--- | :--- | :--- | :--- | :---: | :--- |
| GATE CS 2021 Set 1 Q34 | Minimum Spanning Trees | Number of MSTs | Formulaic Edge Conditions ($w(e) = i+j$) | ❌ Wrong | [[content/gate-cs/algorithms/notes/gate_2021_q34_mst\|Note]] |
| GATE CS 2018 Q12 | Minimum Spanning Trees | Uniqueness | Distinct Edge Weights Theorem | ✅ Correct | [[content/gate-cs/algorithms/notes/gate_2018_q12_mst\|Note]] |

---

## Dataview Query (Obsidian Dynamic View)
```dataview
TABLE topic AS Topic, subtopic AS Subtopic, question_type AS "Specialization", status AS Status
FROM "content/gate-cs/algorithms/notes"
SORT date DESC
```
