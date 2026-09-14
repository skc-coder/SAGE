---
cssclasses:
  - dashboard
banner: "![[home.jpg]]"
banner_x: 0.5
banner_y: 0.78
source: https://tfthacker.com/article-obsidian-dashboardplusplus2022
---
# tasks

## today

```tasks
not done
due today
sort by priority
```
## upcoming

```tasks
not done
due after today
due before in 8 days
sort by due
```

## inbox

```dataview
TASK
FROM ""
WHERE !completed
AND !tags
```
---

# gate/pgee

## moc
- [[moc cs]]
- [[moc maths]]
- [[padai/pgee/pgee]]
- [[moc aptitude]]

## tasks 

```dataview
TASK
FROM #pgee
WHERE !completed
SORT due asc
```
## 📊 Revision Tracker

```dataview
table status, last_review
from #gate
sort last_review desc
```

---

# development

## current Projects

- [[Project 1]]
- [[Project 2]]

## recent Work

```dataview
list
from "Projects"
sort file.mtime desc
limit 5
```

---

# learning

## 📖 Topics

- [[Urdu]]
    
- [[System Design]]
    
- [[Web Dev]]
    
---

# vault insights

## 🗄️ Recent Files

```dataview
list
from ""
sort file.mtime desc
limit 6
```

## ⭐ Favorites

```dataview
list
from #fav
sort file.name asc
limit 5
```

