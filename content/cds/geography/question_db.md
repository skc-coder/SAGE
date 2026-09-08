---
exam: "CDS"
subject: "Physical Geography"
---

# Question Database

```dataview
TABLE 
    rows.file.link AS "Logged Question Notes",
    rows.difficulty AS "Difficulty",
    rows.status AS "Status",
    rows.mistake_category AS "Mistake Category"
FROM "content/cds/geography/notes/questions"
GROUP BY topic AS "Topic"
```
