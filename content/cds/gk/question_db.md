# Question Database

```dataview
TABLE 
    rows.file.link AS "Logged Question Notes",
    rows.difficulty AS "Difficulty",
    rows.status AS "Status",
    rows.importance AS "Importance"
FROM "content/cds/gk/notes/questions"
GROUP BY topic + " > " + subtopic AS "Topic & Subtopic"
```
