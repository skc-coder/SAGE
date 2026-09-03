# Question Database

```dataview

TABLE WITHOUT ID
    "Topic & Subtopic" AS "Topic & Subtopic",
    rows.file.link AS "Questions / Variations",
    rows.status AS "Status",
    rows.importance AS "Importance",
    rows.difficulty AS "Difficulty"
FROM "content/cds/math/notes/questions" OR "content/cds/math/notes/variations"
FLATTEN topic + " > " + subtopic AS "Topic & Subtopic"
GROUP BY "Topic & Subtopic"
```
