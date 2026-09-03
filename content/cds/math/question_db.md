# Question Database

```dataview
TABLE 
    rows.file.link AS "Question / Variation",
    rows.status AS "Status",
    rows.importance AS "Importance",
    rows.difficulty AS "Difficulty"
FROM "content/cds/math/notes/questions" OR "content/cds/math/notes/variations"
GROUP BY topic + " > " + subtopic AS "Topic & Subtopic"
```
