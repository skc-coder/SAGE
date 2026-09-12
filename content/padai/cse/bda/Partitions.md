### Partition in Hive

A **partition** is a way to organize data in Hive by splitting it into subdirectories based on one or more columns (e.g., date, region, category).

---

### Why Use Partitioning?

- **Faster queries** — Hive scans only relevant partitions
- **Better performance** — avoids full table scans
- **Efficient data management** — easy to delete or update specific data

---

### How It Works

- Data is stored in directories like:  
    `/user/hive/warehouse/employees/year=2023/month=01/`
- Each partition is a subdirectory
- Hive uses the partition column(s) to locate data quickly

---

### Example

```
CREATE TABLE employees (
  id INT, name STRING, dept STRING
)
PARTITIONED BY (year INT, month INT);
```

Data stored as:

`/year=2023/month=01/ /year=2023/month=02/ /year=2024/month=01/`

Query:

```
SELECT * FROM employees WHERE year = 2024 AND month = 1;
```

→ Hive only scans `/year=2024/month=01/` — much faster.