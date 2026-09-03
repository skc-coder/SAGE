# Question Database

```dataview
TABLE 
    rows.question_number AS "Q#",
    rows.file.link AS "Question Note",
    rows.difficulty AS "Difficulty",
    rows.status AS "Status",
    rows.mistake_category AS "Mistake Category"
FROM "content/cds/elementary-mathematics/notes/questions"
GROUP BY topic + " > " + subtopic AS "Topic & Subtopic"
```
