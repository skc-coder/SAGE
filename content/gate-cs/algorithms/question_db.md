# Question Database — Algorithms (GATE CS)

This database tracks every question asked, its fine-grained taxonomy specialization, source, user performance, and linked concept note.

# Question Database — Algorithms (GATE CS)

This database tracks topics, subtopics, and specialized question patterns. Questions are grouped compactly within their corresponding concept rows.

## Topic & Question Taxonomy Database

| Topic | Subtopic | Question Type / Specialization | Logged Questions & Notes | Performance (Correct / Total) |
| :--- | :--- | :--- | :--- | :---: |
| **Minimum Spanning Trees** | Number of MSTs | Formulaic Edge Conditions ($w(e) = i+j$) | • [[content/gate-cs/algorithms/notes/gate_2021_q34_mst\|GATE '21 Q34 (❌)]] | 0 / 1 (0%) |
| | | Adjacency Matrix Representation | • [[content/gate-cs/algorithms/notes/gate_2015_q42_mst\|GATE '15 Q42 (✅)]]<br>• [[content/gate-cs/algorithms/notes/gate_2019_q18_mst\|GATE '19 Q18 (❌)]] | 1 / 2 (50%) |
| | Uniqueness | Distinct Edge Weights Theorem | • [[content/gate-cs/algorithms/notes/gate_2018_q12_mst\|GATE '18 Q12 (✅)]] | 1 / 1 (100%) |

---

## Dataview Dynamic Grouping (Obsidian Query)

```dataview
TABLE 
    rows.question_type AS "Question Types / Specializations",
    rows.file.link AS "Logged Question Notes"
FROM "content/gate-cs/algorithms/notes"
GROUP BY topic + " > " + subtopic AS "Topic & Subtopic"
```

