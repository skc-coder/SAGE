https://www.youtube.com/watch?v=rr17cbPGWGA&t=926s
# Apache Hive – Overview

**Hive** is a ![data warehouse](data%20systems) system built on top of Hadoop (HDFS) that lets you query large datasets using **HiveQL (HQL)** — a SQL-like language. Developed at Facebook to avoid writing complex MapReduce Java code.

---

## Architecture
![](attachments/Pasted%20image%2020260420083316.png)
![[Pasted image 20260420073531.png]]

- **Hive Clients** — connect via Thrift, JDBC, or ODBC drivers
- **Hive Services** — Web UI (HUE) or CLI for submitting queries
- **[[Hive Driver]]** — processes all queries through 3 steps:
  1. *Compiler* — parses and analyzes the query
  2. *Optimizer* — creates an optimized MapReduce execution plan
  3. *Executor* — runs the tasks
- **[[Metastore]]** — stores schema/metadata (table names, columns, location); stored on Apache Derby DB
- **Execution Engine** — bridge between Hive and Hadoop (MapReduce/YARN/Tez)
- **HDFS** — distributed storage layer

---

## Data Modeling

| Concept            | Description                                        |
| ------------------ | -------------------------------------------------- |
| **Tables**         | Same as RDBMS tables                               |
| **[[Partitions]]** | Group data by a key (e.g. date) for faster queries |
| **Buckets**        | Further divide partitions for efficient querying   |

---

## Data Types
#### Primitive

**Numeric**

| Type      | Description                                 | Example             |
| --------- | ------------------------------------------- | ------------------- |
| `INT`     | 32-bit integer                              | `42`                |
| `FLOAT`   | 32-bit decimal (less precise)               | `3.14`              |
| `DOUBLE`  | 64-bit decimal (more precise)               | `3.14159265`        |
| `DECIMAL` | Exact fixed-point number, no rounding error | `99.99` (for money) |

Use `DECIMAL` when precision matters (prices, tax). Use `DOUBLE` for scientific values.

---

**String**

| Type         | Description                                      | Example                     |
| ------------ | ------------------------------------------------ | --------------------------- |
| `STRING`     | Variable length, no limit                        | `"John Doe"`                |
| `VARCHAR(n)` | Variable length, max `n` chars                   | `VARCHAR(50)`               |
| `CHAR(n)`    | Fixed length, always `n` chars, pads with spaces | `CHAR(10)` → `"John      "` |

`STRING` is most common in Hive. `CHAR`/`VARCHAR` are for when you need length constraints.

---

**DateTime**

| Type        | Description                             | Example                   |
| ----------- | --------------------------------------- | ------------------------- |
| `DATE`      | Calendar date only                      | `2024-01-15`              |
| `TIMESTAMP` | Date + time (up to nanoseconds)         | `2024-01-15 10:30:00.000` |
| `INTERVAL`  | A duration/difference between two times | `INTERVAL '5' DAY`        |

Format for import: `YYYY-MM-DD` for date, `YYYY-MM-DD HH:MM:SS` for timestamp.

---

**Misc**

| Type      | Description                   | Example               |
| --------- | ----------------------------- | --------------------- |
| `BOOLEAN` | True/false flag               | `TRUE`, `FALSE`       |
| `BINARY`  | Raw bytes, stores binary data | images, encoded blobs |

---

#### Complex:
- `ARRAY<type>` — collection of same-type elements
- `MAP<key, value>` — key-value pairs
- `STRUCT<col:type>` — structured record with named fields
- `UNIONTYPE<type1, type2>` — heterogeneous types

---


## Tables
- **Managed Table**:
    
    - Hive owns the data
    - Data lives in Hive’s managed directory
    - `DROP TABLE` → deletes data and metadata
    - Best for data that is only used within Hive
    - `create table`
    
- **External Table**:
    - Hive does not own the data
    - Data lives outside Hive’s control
    - `DROP TABLE` → only removes metadata; data stays
    - Best for data shared across tools or when you want to keep data separate
    - `create external table`
## Hive vs RDBMS

| Feature            | Hive                             | RDBMS                       |
| ------------------ | -------------------------------- | --------------------------- |
| Schema enforcement | On **read**                      | On **write**                |
| Data size          | Petabytes                        | Terabytes                   |
| Write pattern      | **WORM** (write once, read many) | Read & write many times     |
| Scalability        | Cheap, linear (add nodes)        | Expensive hardware upgrades |
| Type               | Data **warehouse**               | Database                    |
|                    |                                  |                             |

---

## HIVE vs PIG

| Feature               | Hive                                                 | Pig                                   |
| --------------------- | ---------------------------------------------------- | ------------------------------------- |
| **Language**          | HiveQL — SQL-like, declarative                       | Pig Latin — procedural, scripting     |
| **Use Case**          | Ad-hoc querying, reporting, analysts                 | ETL, data transformation, developers  |
| **Abstraction Level** | High — closer to SQL                                 | Medium — more control over data flow  |
| **Data Model**        | Tables with schema (RDBMS-like)                      | Bags, tuples, fields (schema-on-read) |
| **Execution**         | MapReduce/Tez/Spark (via Hive)                       | MapReduce/Tez/Spark (via Pig)         |
| **Schema**            | Schema-on-read (enforced at query time)              | Schema-on-read (optional, flexible)   |
| **Performance**       | Optimized for queries, slower for complex transforms | Better for multi-step transformations |
| **Ease of Use**       | Easy for SQL users                                   | Steeper learning curve                |
| **Debugging**         | Easier — SQL syntax, familiar                        | Harder — need to trace data flow      |

---

### When to Use Which?

- **Use Hive** if:
  - You’re writing **SQL-like queries**
  - You need **reports, dashboards, or ad-hoc analysis**
  - You’re comfortable with **tables, columns, joins**
  - You want **schema enforcement**

- **Use Pig** if:
  - You’re doing **complex ETL pipelines**
  - You need **multi-step data transformations**
  - You want **fine control over data flow**
  - You’re comfortable with **procedural scripting**

---

### Example

**Hive (SQL-like):**
```sql
SELECT dept, AVG(salary)
FROM employees
GROUP BY dept;
```

**Pig (Procedural):**
```pig
emp = LOAD 'employees.txt' USING PigStorage(',') AS (id:int, name:chararray, dept:chararray, salary:int);
grp = GROUP emp BY dept;
avg_sal = FOREACH grp GENERATE group, AVG(emp.salary);
DUMP avg_sal;
```

---

## Key HQL Commands
https://www.scribd.com/document/229443179/Hortonworks-CheatSheet-SQLtoHive
```sql
-- Show/create/drop database
SHOW DATABASES;
CREATE DATABASE office;
DROP DATABASE office CASCADE;
USE office;

-- Create table
CREATE TABLE employee (
  id INT, name STRING, dept STRING,
  year_of_joining INT, salary INT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
TBLPROPERTIES ("skip.header.line.count"="1");

-- Load data
LOAD DATA LOCAL INPATH '/home/cloudera/documents/employee.csv'
INTO TABLE employee;

-- Basic queries
SELECT * FROM employee;
SELECT COUNT(*) FROM employee;
SELECT * FROM employee WHERE salary > 25000;

-- Join
SELECT c.id, c.name, c.age, o.amount
FROM customer c
JOIN order o ON c.id = o.customer_id;

-- Alter / Drop
ALTER TABLE employee RENAME TO employees;
DROP TABLE employees;
```

---


## Questions

# 🐝 Apache Hive — Complete Notes

> [!info] About These Notes These notes cover Hive concepts from beginner to advanced level, organized for easy review and revision.

---

## PART-A — Short Answer Questions

---

### Q.1 What is Hive?

> [!abstract] Definition **Apache Hive** is a **data warehouse infrastructure** built on top of Apache Hadoop for providing data summarization, query, and analysis.

- Developed by **Facebook**, later open-sourced and donated to Apache.
- Provides an **SQL-like interface** called **HiveQL (HQL)** to interact with data stored in HDFS.
- Translates SQL queries into **MapReduce jobs**, Tez, or Spark jobs for execution on the Hadoop cluster.
- Designed for **batch processing** of very large datasets.
- Not suited for **OLTP (Online Transaction Processing)** — better for **OLAP (Online Analytical Processing)**.

```
User → HiveQL Query → Hive → MapReduce/Tez/Spark → HDFS
```

---

### Q.2 Difference Between External Table and Managed Table in Hive

> [!tip] Key Distinction The key difference lies in **who controls the data lifecycle**.

| Feature             | Managed Table                                     | External Table                            |
| ------------------- | ------------------------------------------------- | ----------------------------------------- |
| **Also Called**     | Internal Table                                    | External Table                            |
| **Data Location**   | Hive warehouse directory (`/user/hive/warehouse`) | User-specified directory                  |
| **Data Ownership**  | Hive owns the data                                | User/External system owns the data        |
| **On DROP TABLE**   | Data + metadata both deleted                      | Only metadata deleted; data remains       |
| **Use Case**        | Hive-exclusive data processing                    | Shared data with other tools (Pig, Spark) |
| **Schema on Write** | Yes                                               | Yes                                       |
| **Created With**    | `CREATE TABLE`                                    | `CREATE EXTERNAL TABLE`                   |

> [!warning] Important Use **External Tables** when you do NOT want Hive to delete your data when the table is dropped.

---

### Q.3 Features of Hive

> [!note] Core Features

1. **SQL-like Query Language (HiveQL)** — Familiar interface for SQL users.
2. **Scalability** — Works on petabytes of data stored in HDFS.
3. **Schema on Read** — Schema is applied when data is read, not when stored.
4. **Extensibility** — Supports custom UDFs (User Defined Functions), UDAFs, UDTFs.
5. **Multiple File Formats** — Supports TextFile, SequenceFile, RCFile, ORC, Parquet, Avro.
6. **Partitioning & Bucketing** — Optimizes query performance.
7. **Metastore** — Stores metadata in an RDBMS (MySQL, Derby, PostgreSQL).
8. **Integration** — Works with HBase, Pig, Spark, Kafka.
9. **JDBC/ODBC Support** — Allows BI tools to connect via HiveServer2.
10. **Built-in Functions** — Provides string, date, math, and aggregate functions.

---

### Q.4 What is a Partition in Hive?

> [!abstract] Definition A **partition** in Hive is a way of **dividing a table into parts** based on the values of one or more columns, where each unique value of the partition column corresponds to a **sub-directory** in HDFS.

**Example:**

```sql
CREATE TABLE sales (
    product STRING,
    amount DOUBLE
)
PARTITIONED BY (year INT, month INT);
```

**HDFS Structure:**

```
/user/hive/warehouse/sales/
    year=2023/month=1/
    year=2023/month=2/
    year=2024/month=1/
```

- Each partition = a **separate folder** in HDFS.
- Queries on a specific partition **scan only that folder**, not the entire table.
- Two types:
    - **Static Partitioning** — Partition values specified manually.
    - **Dynamic Partitioning** — Partition values determined automatically from data.

---

### Q.5 Why is Partitioning Required in Hive?

> [!success] Reasons for Partitioning

1. **Performance Optimization** — Queries scan only relevant partitions instead of the full dataset (**partition pruning**).
2. **Reduced I/O** — Less data read from HDFS = faster queries.
3. **Parallel Processing** — Different partitions can be processed in parallel.
4. **Data Organization** — Logical grouping of data (e.g., by date, region, category).
5. **Cost Efficiency** — Reduces resource consumption on large clusters.

**Without Partitioning:**

```
SELECT * FROM logs WHERE year = 2024;
→ Full table scan (TBs of data)
```

**With Partitioning:**

```
SELECT * FROM logs WHERE year = 2024;
→ Scans only /logs/year=2024/ folder
```

---

### Q.6 Why Does Hive Not Store Metadata Information in HDFS?

> [!question] Reasoning

Hive stores metadata in the **Metastore** (an RDBMS like MySQL or Derby) rather than in HDFS because:

|Reason|Explanation|
|---|---|
|**Low Latency Access**|RDBMS provides fast random access; HDFS is optimized for sequential reads|
|**ACID Transactions**|Metastore needs transactional consistency for schema operations|
|**Small Data Size**|Metadata is small and structured — RDBMS handles it efficiently|
|**Query Optimization**|Metadata is frequently accessed during query compilation — RDBMS is faster|
|**Concurrency**|Multiple users querying metadata simultaneously — RDBMS handles concurrency well|
|**HDFS Limitations**|HDFS does not support in-place updates or low-latency reads|

> [!tip] HDFS is designed for **write-once, read-many** large files. Metadata is small, frequently updated, and needs random access — exactly what RDBMS is built for.

---

### Q.7 Components Used in Hive Query Processors

> [!abstract] Query Processing Pipeline

The Hive query processor consists of the following components:

```
HiveQL Query
     ↓
1. Parser
     ↓
2. Semantic Analyzer
     ↓
3. Logical Plan Generator
     ↓
4. Logical Optimizer
     ↓
5. Physical Plan Generator
     ↓
6. Physical Optimizer
     ↓
7. Execution Engine
```

|Component|Function|
|---|---|
|**Parser**|Parses HiveQL into an Abstract Syntax Tree (AST)|
|**Semantic Analyzer**|Validates query against Metastore (checks table/column existence)|
|**Logical Plan Generator**|Creates a logical query plan (operator tree)|
|**Logical Optimizer**|Applies rule-based optimizations (predicate pushdown, column pruning)|
|**Physical Plan Generator**|Converts logical plan to MapReduce/Tez/Spark tasks|
|**Physical Optimizer**|Optimizes physical plan (join reordering, map joins)|
|**Execution Engine**|Submits and executes tasks on the cluster|
|**Metastore**|Provides schema/metadata for validation and planning|

---

## PART-B — Medium Answer Questions

---

### Q.8 Introduction to Hive (Hello to Hive)

> [!abstract] Overview

Apache Hive is a **data warehousing solution** built on top of **Apache Hadoop** that enables users to query and manage large datasets using a familiar SQL-like language.

#### Background & History

- Originated at **Facebook** in 2007 to manage petabytes of data.
- Open-sourced in **2008** and donated to Apache Software Foundation in **2008**.
- Became a top-level Apache project in **2010**.

#### Why Hive?

Before Hive, querying HDFS data required writing complex **Java MapReduce programs**. Hive democratized big data by:

- Allowing **SQL-literate analysts** to work with big data.
- Abstracting MapReduce complexity.
- Enabling **batch analytics** at massive scale.

#### Hello, Hive! — First Steps

```sql
-- Launch Hive CLI
$ hive

-- Create a database
CREATE DATABASE my_first_db;
USE my_first_db;

-- Create a table
CREATE TABLE hello_world (
    id INT,
    message STRING
);

-- Load data
INSERT INTO hello_world VALUES (1, 'Hello, Hive!');

-- Query data
SELECT * FROM hello_world;
```

#### Where Hive Fits

```
Raw Data → HDFS → Hive (HiveQL) → Analysis/Reports → BI Tools
```

#### Key Facts

- **Not** a database — it's a query layer over HDFS.
- Queries are slow (minutes to hours) — designed for batch, not real-time.
- Best for **ETL pipelines**, **data warehousing**, and **ad-hoc analytics**.

---

### Q.9 Key Differences Between Hive and Pig

> [!note] Hive vs Pig

|Feature|Apache Hive|Apache Pig|
|---|---|---|
|**Type**|Data Warehouse / Query Engine|Data Flow / Scripting Platform|
|**Language**|HiveQL (SQL-like)|Pig Latin (procedural, data flow)|
|**Primary Users**|SQL Analysts, Data Analysts|Programmers, Data Engineers|
|**Processing Model**|Declarative (WHAT to do)|Procedural (HOW to do it)|
|**Schema**|Required (schema-on-read)|Optional (schema-on-demand)|
|**Best For**|Structured data, reporting|Semi-structured data, ETL|
|**Metastore**|Yes (stores table metadata)|No built-in metastore|
|**Joins**|SQL-style joins|JOIN operators in Pig Latin|
|**UDF Support**|Yes (Java, Python)|Yes (Java, Python)|
|**Query Optimization**|Automatic (CBO, rule-based)|Manual control|
|**Data Source**|HDFS, HBase|HDFS, HBase, Local FS|
|**Output**|Tables, files|Files|
|**Latency**|High (batch)|High (batch)|

**Hive Example:**

```sql
SELECT department, COUNT(*) FROM employees GROUP BY department;
```

**Pig Equivalent:**

```pig
emp = LOAD 'employees' USING PigStorage(',');
grp = GROUP emp BY department;
result = FOREACH grp GENERATE group, COUNT(emp);
DUMP result;
```

> [!tip] When to Use Which?
> 
> - Use **Hive** for structured data with known schema and SQL-style analytics.
> - Use **Pig** for complex data transformations, ETL workflows, and semi-structured data.

---

### Q.10 Architecture of Hive

> [!abstract] Hive Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                        HIVE CLIENTS                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────┐  │
│  │ Hive CLI │  │ Web UI   │  │JDBC/ODBC │  │Thrift/REST │  │
│  └──────────┘  └──────────┘  └──────────┘  └────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────────┐
│                    HIVE SERVICES                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              HiveServer2 / Driver                    │    │
│  │  ┌──────────┐ ┌──────────┐ ┌────────┐ ┌─────────┐  │    │
│  │  │  Parser  │ │Semantic  │ │ Query  │ │Execution│  │    │
│  │  │          │ │Analyzer  │ │Planner │ │ Engine  │  │    │
│  │  └──────────┘ └──────────┘ └────────┘ └─────────┘  │    │
│  └─────────────────────────────────────────────────────┘    │
└──────────┬─────────────────────────┬───────────────────────-┘
           │                         │
┌──────────▼──────────┐   ┌─────────▼────────────────────────┐
│     METASTORE        │   │        HADOOP ECOSYSTEM           │
│  ┌───────────────┐  │   │  ┌──────────┐  ┌──────────────┐  │
│  │   Database    │  │   │  │   HDFS   │  │  MapReduce   │  │
│  │ (MySQL/Derby) │  │   │  │          │  │  / Tez       │  │
│  │  - Tables     │  │   │  │  Data    │  │  / Spark     │  │
│  │  - Columns    │  │   │  │  Storage │  │  Execution   │  │
│  │  - Partitions │  │   │  └──────────┘  └──────────────┘  │
│  │  - Locations  │  │   │  ┌──────────┐                     │
│  └───────────────┘  │   │  │  YARN    │                     │
└─────────────────────┘   │  │ Resource │                     │
                           │  │ Manager  │                     │
                           │  └──────────┘                     │
                           └──────────────────────────────────┘
```

#### Component Descriptions

**1. Hive Clients**

- **CLI (Command Line Interface)** — Terminal-based interface.
- **Web UI** — Browser-based interface (HWI / Hue).
- **JDBC/ODBC** — For connecting BI tools (Tableau, Power BI).
- **Thrift Server** — Language-agnostic API.

**2. HiveServer2 / Driver**

- Entry point for all queries.
- Manages sessions, authentication, and query execution.

**3. Compiler/Query Processor**

- Parses, validates, optimizes, and plans query execution.

**4. Metastore**

- Stores all metadata: database names, table schemas, partition info, storage locations.
- Backed by RDBMS (Derby by default, MySQL for production).

**5. Execution Engine**

- Submits the query plan to MapReduce, Tez, or Spark.
- Default engine: **Tez** (faster than MapReduce).

**6. HDFS**

- Actual data storage.
- Hive tables map to directories in HDFS.

---

### Q.11 Hive CLI Client

> [!abstract] Command Line Interface

The **Hive CLI** is the original command-line interface for interacting with Hive. It provides a shell where users can run HiveQL commands.

#### Starting the CLI

```bash
$ hive
# or
$ hive --service cli
```

#### CLI Prompt

```
hive>
```

#### Common CLI Commands

```sql
-- Show databases
SHOW DATABASES;

-- Use a database
USE database_name;

-- Show tables
SHOW TABLES;

-- Describe a table
DESCRIBE table_name;
DESCRIBE EXTENDED table_name;   -- detailed info
DESCRIBE FORMATTED table_name;  -- formatted output

-- Run a query
SELECT * FROM table_name LIMIT 10;

-- Quit
quit;
exit;
```

#### Running Script Files

```bash
# Run a HiveQL script
$ hive -f script.hql

# Run inline command
$ hive -e "SELECT COUNT(*) FROM my_table;"
```

#### Useful CLI Options

```bash
hive --hiveconf hive.execution.engine=tez  # Set config at startup
hive --define KEY=VALUE                     # Pass variables
hive -v                                     # Verbose mode
```

#### Setting Properties in CLI

```sql
-- Inside hive shell
SET hive.execution.engine=tez;
SET mapreduce.job.reduces=10;
SET hive.auto.convert.join=true;
```

> [!warning] Deprecated The original Hive CLI is deprecated in favor of **Beeline** (JDBC-based CLI connecting to HiveServer2).

#### Beeline (Modern CLI)

```bash
$ beeline
beeline> !connect jdbc:hive2://localhost:10000
```

---

### Q.12 Web Browser as Hive Client

> [!abstract] Web-Based Hive Interfaces

Several web-based interfaces allow users to interact with Hive through a browser, eliminating the need for command-line access.

#### 1. Hive Web Interface (HWI)

- Built into older Hive distributions.
- Accessible at `http://<hive-host>:9999/hwi`.
- Allows browsing databases, tables, and running queries.
- **Largely deprecated** in modern Hive versions.

#### 2. Apache Hue (Hadoop User Experience)

- Most popular web UI for Hive.
- URL: `http://<hue-host>:8888`

**Features of Hue:**

- SQL Editor with **autocomplete** and **syntax highlighting**.
- Query history and saved queries.
- Visual result display (tables, charts).
- File browser for HDFS.
- Job browser for monitoring MapReduce/Tez jobs.
- Supports Hive, Impala, Spark SQL, Pig.

```
Browser → Hue Web Server → HiveServer2 → Execution Engine → HDFS
```

#### 3. Apache Zeppelin

- Web-based notebook for interactive analytics.
- Supports Hive interpreter.
- Allows mixing code, queries, and visualizations in one notebook.

#### 4. Cloudera Data Warehouse / Ambari Views

- Enterprise web UIs that include Hive query editors.
- Provided by Cloudera and Hortonworks (now merged) distributions.

#### Advantages of Web Browser Clients

|Advantage|Description|
|---|---|
|**Accessibility**|No installation needed on client machine|
|**Collaboration**|Shared query history and notebooks|
|**Visualization**|Built-in charts and result formatting|
|**User-Friendly**|GUI for non-technical users|
|**Multi-user**|Role-based access control|

---

### Q.14 Features of HiveQL (Query Language)

> [!note] HiveQL Feature Set

HiveQL is Hive's query language, modeled after SQL with extensions for big data.

#### 1. DDL (Data Definition Language)

```sql
CREATE DATABASE, DROP DATABASE
CREATE TABLE, DROP TABLE, ALTER TABLE
CREATE VIEW, DROP VIEW
MSCK REPAIR TABLE  -- Recover partitions
```

#### 2. DML (Data Manipulation Language)

```sql
LOAD DATA [LOCAL] INPATH '...' INTO TABLE ...
INSERT INTO TABLE ... SELECT ...
INSERT OVERWRITE TABLE ...
EXPORT TABLE ... TO '...'
IMPORT TABLE ... FROM '...'
```

#### 3. Query Features

```sql
SELECT ... FROM ... WHERE ...
GROUP BY, HAVING
ORDER BY, SORT BY, DISTRIBUTE BY, CLUSTER BY
LIMIT, OFFSET
DISTINCT
```

#### 4. Join Support

- INNER JOIN, LEFT OUTER JOIN, RIGHT OUTER JOIN, FULL OUTER JOIN
- CROSS JOIN, LEFT SEMI JOIN, MAP JOIN

#### 5. Subqueries & CTEs

```sql
-- Subquery
SELECT * FROM (SELECT id, name FROM emp WHERE dept='IT') t;

-- CTE (WITH clause)
WITH it_emp AS (SELECT * FROM emp WHERE dept='IT')
SELECT * FROM it_emp WHERE salary > 50000;
```

#### 6. Built-in Functions

|Category|Examples|
|---|---|
|**String**|`CONCAT`, `SUBSTR`, `UPPER`, `LOWER`, `TRIM`, `LENGTH`|
|**Math**|`ABS`, `CEIL`, `FLOOR`, `ROUND`, `SQRT`, `POWER`|
|**Date**|`CURRENT_DATE`, `DATE_ADD`, `DATEDIFF`, `YEAR`, `MONTH`|
|**Aggregate**|`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `COLLECT_SET`|
|**Conditional**|`IF`, `CASE WHEN`, `COALESCE`, `NVL`, `NULLIF`|

#### 7. User Defined Functions (UDFs)

```sql
-- Register UDF
ADD JAR /path/to/myudf.jar;
CREATE TEMPORARY FUNCTION my_func AS 'com.example.MyUDF';

-- Use it
SELECT my_func(column) FROM table;
```

#### 8. Window Functions

```sql
SELECT name, salary,
    RANK() OVER (PARTITION BY dept ORDER BY salary DESC) as rank,
    SUM(salary) OVER (PARTITION BY dept) as dept_total
FROM employees;
```

#### 9. Partitioning & Bucketing in Queries

```sql
-- Query specific partition
SELECT * FROM logs WHERE year=2024 AND month=1;

-- Enable dynamic partitioning
SET hive.exec.dynamic.partition=true;
```

#### 10. ACID Transactions (Hive 3+)

```sql
-- Requires ORC format + bucketing
UPDATE employees SET salary = salary * 1.1 WHERE dept='IT';
DELETE FROM employees WHERE id = 1001;
```

---

### Q.15 Types of Joins in HiveQL

> [!abstract] Join Types

Hive supports multiple join types for combining data from two or more tables.

#### 1. INNER JOIN (Default JOIN)

Returns only rows that have **matching values in both tables**.

```sql
SELECT e.name, d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;
```

```
employees:  1,Alice,10    departments: 10,Engineering
            2,Bob,20                   20,Marketing
            3,Carol,99   
Result: Alice-Engineering, Bob-Marketing  (Carol excluded - no match)
```

#### 2. LEFT OUTER JOIN

Returns **all rows from left table** + matching rows from right. Non-matching right rows → NULL.

```sql
SELECT e.name, d.dept_name
FROM employees e
LEFT OUTER JOIN departments d
ON e.dept_id = d.dept_id;
```

```
Result: Alice-Engineering, Bob-Marketing, Carol-NULL
```

#### 3. RIGHT OUTER JOIN

Returns **all rows from right table** + matching rows from left.

```sql
SELECT e.name, d.dept_name
FROM employees e
RIGHT OUTER JOIN departments d
ON e.dept_id = d.dept_id;
```

#### 4. FULL OUTER JOIN

Returns **all rows from both tables**, NULLs where no match.

```sql
SELECT e.name, d.dept_name
FROM employees e
FULL OUTER JOIN departments d
ON e.dept_id = d.dept_id;
```

#### 5. CROSS JOIN (Cartesian Product)

Returns **every combination** of rows from both tables. Use with caution — can produce huge results.

```sql
SELECT e.name, d.dept_name
FROM employees e
CROSS JOIN departments d;
-- m × n rows produced
```

#### 6. LEFT SEMI JOIN

Returns rows from the **left table that have a match** in the right table. Similar to `WHERE EXISTS`.

```sql
SELECT e.name
FROM employees e
LEFT SEMI JOIN dept_managers dm
ON e.id = dm.emp_id;
-- Returns employees who are also managers
```

#### 7. MAP JOIN (Broadcast Join)

Optimization for joining a **large table with a small table**. The small table is loaded into memory (broadcasted).

```sql
SELECT /*+ MAPJOIN(d) */ e.name, d.dept_name
FROM employees e
JOIN departments d
ON e.dept_id = d.dept_id;
```

```sql
-- Auto map join
SET hive.auto.convert.join=true;
SET hive.mapjoin.smalltable.filesize=25000000; -- 25MB threshold
```

#### Join Summary Table

|Join Type|Left Table|Right Table|Notes|
|---|---|---|---|
|INNER JOIN|Matched only|Matched only|Default|
|LEFT OUTER|All rows|Matched / NULL|—|
|RIGHT OUTER|Matched / NULL|All rows|—|
|FULL OUTER|All rows|All rows|NULLs for non-matches|
|CROSS JOIN|All rows|All rows|Cartesian product|
|LEFT SEMI|Matched rows|Not in output|Like EXISTS|
|MAP JOIN|Large table|Small table (in-mem)|Performance optimization|

> [!tip] Best Practice Always put the **largest table last** in Hive joins for better optimization (reducer memory management).

---

## PART-C — Long Answer Questions

---

### Q.16 Working of Hive

> [!abstract] End-to-End Hive Query Execution

#### Complete Working Diagram

```
User/Application
     │
     ▼ HiveQL Query
┌─────────────────────────────────────┐
│           HIVE DRIVER               │
│                                     │
│  Step 1: PARSER                     │
│  • Tokenizes the HiveQL query       │
│  • Builds Abstract Syntax Tree(AST) │
│  • Checks basic syntax              │
│                                     │
│  Step 2: SEMANTIC ANALYZER          │
│  • Validates table/column names     │
│  • Checks data types                │
│  • Consults METASTORE               │
│                                     │
│  Step 3: LOGICAL PLAN GENERATOR     │
│  • Creates operator tree            │
│  • Operations: TableScan, Filter,   │
│    GroupBy, Join, Select            │
│                                     │
│  Step 4: LOGICAL OPTIMIZER          │
│  • Predicate Pushdown               │
│  • Column Pruning                   │
│  • Partition Pruning                │
│                                     │
│  Step 5: PHYSICAL PLAN GENERATOR    │
│  • Converts to MapReduce/Tez tasks  │
│  • Determines number of reducers    │
│                                     │
│  Step 6: PHYSICAL OPTIMIZER         │
│  • Map Join optimization            │
│  • Join reordering                  │
└──────────────────┬──────────────────┘
                   │
         ┌─────────▼──────────┐
         │   EXECUTION ENGINE  │
         │  (MapReduce/Tez/    │
         │   Spark)            │
         └─────────┬──────────┘
                   │
         ┌─────────▼──────────┐
         │     YARN            │
         │  (Resource Manager) │
         └─────────┬──────────┘
                   │
         ┌─────────▼──────────┐
         │       HDFS          │
         │  (Data Storage)     │
         └─────────┬──────────┘
                   │
         ┌─────────▼──────────┐
         │   RESULTS           │
         │ → CLI / Application │
         └─────────────────────┘
```

#### Step-by-Step Explanation

**Step 1 — Query Submission** User submits a HiveQL query through CLI, Beeline, JDBC, or REST API.

**Step 2 — Parsing** The **Parser** converts HiveQL to an **Abstract Syntax Tree (AST)**.

```
SELECT name FROM employees WHERE dept='IT'
→ AST: [SELECT] → [name] FROM [employees] WHERE [dept='IT']
```

**Step 3 — Semantic Analysis**

- Validates tables and columns against **Metastore**.
- Resolves column references, checks data types.
- Identifies partitions involved.

**Step 4 — Logical Planning** Creates a tree of logical operators:

```
→ TableScan(employees)
  → Filter(dept='IT')
    → Select(name)
```

**Step 5 — Optimization**

- **Predicate Pushdown**: Move filters closer to data source.
- **Partition Pruning**: Skip irrelevant partitions.
- **Column Pruning**: Read only needed columns.

**Step 6 — Physical Planning** Converts logical plan to **MapReduce / Tez / Spark DAG**.

**Step 7 — Execution**

- YARN allocates resources.
- Tasks run on DataNodes where data resides (data locality).
- Results written back to HDFS or returned to user.

#### Hive with Different Execution Engines

|Engine|Speed|Default Since|
|---|---|---|
|MapReduce|Slowest|Hive 0.x|
|Apache Tez|~2-10x faster|Hive 0.13|
|Apache Spark|Fastest|Hive 1.1 (via Spark)|

```sql
-- Set execution engine
SET hive.execution.engine=tez;    -- or mr, spark
```

---

### Q.17 Installation of Hive / Getting Started with Hive

> [!info] Prerequisites
> 
> - Java 8+ installed
> - Hadoop installed and running (HDFS + YARN)
> - `JAVA_HOME` and `HADOOP_HOME` set

#### Step 1: Download Hive

```bash
# Download Apache Hive
wget https://downloads.apache.org/hive/hive-3.1.3/apache-hive-3.1.3-bin.tar.gz

# Extract
tar -xzf apache-hive-3.1.3-bin.tar.gz

# Move to /opt
sudo mv apache-hive-3.1.3-bin /opt/hive
```

#### Step 2: Set Environment Variables

```bash
# Add to ~/.bashrc or ~/.profile
export HIVE_HOME=/opt/hive
export PATH=$PATH:$HIVE_HOME/bin
export HADOOP_HOME=/opt/hadoop

# Apply
source ~/.bashrc
```

#### Step 3: Configure Hive

```bash
cd $HIVE_HOME/conf
cp hive-env.sh.template hive-env.sh
cp hive-site.xml.template hive-site.xml
```

**Edit `hive-env.sh`:**

```bash
export HADOOP_HOME=/opt/hadoop
export HIVE_CONF_DIR=$HIVE_HOME/conf
```

**Edit `hive-site.xml`:**

```xml
<configuration>
  <!-- Metastore Database (MySQL example) -->
  <property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:mysql://localhost/metastore?createDatabaseIfNotExist=true</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionDriverName</name>
    <value>com.mysql.jdbc.Driver</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionUserName</name>
    <value>hiveuser</value>
  </property>
  <property>
    <name>javax.jdo.option.ConnectionPassword</name>
    <value>hivepassword</value>
  </property>
  <!-- Hive Warehouse Location -->
  <property>
    <name>hive.metastore.warehouse.dir</name>
    <value>/user/hive/warehouse</value>
  </property>
  <!-- HiveServer2 settings -->
  <property>
    <name>hive.server2.thrift.port</name>
    <value>10000</value>
  </property>
</configuration>
```

#### Step 4: Set Up Metastore Database

```bash
# Install MySQL connector
cp mysql-connector-java-*.jar $HIVE_HOME/lib/

# Create MySQL database and user
mysql -u root -p
CREATE DATABASE metastore;
CREATE USER 'hiveuser'@'localhost' IDENTIFIED BY 'hivepassword';
GRANT ALL ON metastore.* TO 'hiveuser'@'localhost';
FLUSH PRIVILEGES;
exit;

# Initialize schema
schematool -initSchema -dbType mysql
```

#### Step 5: Create HDFS Directories

```bash
# Start Hadoop first
start-dfs.sh
start-yarn.sh

# Create Hive directories in HDFS
hdfs dfs -mkdir -p /user/hive/warehouse
hdfs dfs -chmod g+w /user/hive/warehouse
hdfs dfs -mkdir -p /tmp/hive
hdfs dfs -chmod 777 /tmp/hive
```

#### Step 6: Start HiveServer2

```bash
# Start HiveServer2
hiveserver2 &

# Or as a service
$HIVE_HOME/bin/hiveserver2 --hiveconf hive.root.logger=INFO,console
```

#### Step 7: Connect via Beeline

```bash
# Connect to HiveServer2
beeline -u jdbc:hive2://localhost:10000

# Or interactive
$ beeline
beeline> !connect jdbc:hive2://localhost:10000 hiveuser hivepassword
```

#### Step 8: Verify Installation

```sql
-- Test Hive
SHOW DATABASES;
CREATE DATABASE test_db;
USE test_db;
CREATE TABLE test (id INT, name STRING);
INSERT INTO test VALUES (1, 'Hive Works!');
SELECT * FROM test;
-- Output: 1  Hive Works!
```

#### Hive Directory Structure

```
$HIVE_HOME/
├── bin/          ← hive, beeline, schematool scripts
├── conf/         ← hive-site.xml, hive-env.sh
├── lib/          ← JAR files
├── logs/         ← Log files
└── examples/     ← Sample data and queries
```

---

### Q.19 Creating and Managing Databases and Tables in Hive

> [!abstract] Database & Table Management

#### Database Operations

```sql
-- Create database
CREATE DATABASE company_db;

-- Create with properties
CREATE DATABASE IF NOT EXISTS company_db
COMMENT 'Company analytics database'
LOCATION '/user/hive/company_warehouse'
WITH DBPROPERTIES ('created_by'='admin', 'year'='2024');

-- Show databases
SHOW DATABASES;
SHOW DATABASES LIKE 'comp*';

-- Use database
USE company_db;

-- Describe database
DESCRIBE DATABASE company_db;
DESCRIBE DATABASE EXTENDED company_db;

-- Alter database
ALTER DATABASE company_db SET DBPROPERTIES ('version'='2.0');

-- Drop database
DROP DATABASE company_db;                   -- fails if non-empty
DROP DATABASE company_db CASCADE;           -- drops all tables too
DROP DATABASE IF EXISTS company_db CASCADE;
```

#### Table Operations

**1. Managed Table (Internal)**

```sql
CREATE TABLE employees (
    emp_id      INT,
    name        STRING,
    salary      DOUBLE,
    department  STRING,
    hire_date   DATE
)
COMMENT 'Employee master table'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE;
```

**2. External Table**

```sql
CREATE EXTERNAL TABLE ext_sales (
    sale_id   INT,
    product   STRING,
    amount    DOUBLE,
    sale_date STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE
LOCATION '/data/sales/raw/';
```

**3. Partitioned Table**

```sql
CREATE TABLE logs (
    log_id    INT,
    message   STRING,
    severity  STRING
)
PARTITIONED BY (year INT, month INT, day INT)
STORED AS ORC;
```

**4. Bucketed Table**

```sql
CREATE TABLE user_events (
    user_id   INT,
    event     STRING,
    ts        TIMESTAMP
)
CLUSTERED BY (user_id) INTO 32 BUCKETS
STORED AS ORC
TBLPROPERTIES ('transactional'='true');
```

**5. Table with ORC and Compression**

```sql
CREATE TABLE optimized_table (
    id   INT,
    data STRING
)
STORED AS ORC
TBLPROPERTIES (
    'orc.compress'='SNAPPY',
    'orc.stripe.size'='67108864'
);
```

**6. CTAS (Create Table As Select)**

```sql
CREATE TABLE it_employees AS
SELECT * FROM employees WHERE department='IT';
```

#### Table Management Commands

```sql
-- Show tables
SHOW TABLES;
SHOW TABLES IN company_db;
SHOW TABLES LIKE 'emp*';

-- Describe table
DESCRIBE employees;
DESCRIBE EXTENDED employees;
DESCRIBE FORMATTED employees;

-- Alter table
ALTER TABLE employees RENAME TO staff;

-- Add column
ALTER TABLE employees ADD COLUMNS (email STRING);

-- Change column
ALTER TABLE employees CHANGE salary salary FLOAT COMMENT 'Monthly salary';

-- Replace columns (redefine all columns)
ALTER TABLE employees REPLACE COLUMNS (id INT, name STRING);

-- Add partition
ALTER TABLE logs ADD PARTITION (year=2024, month=1, day=15)
LOCATION '/data/logs/2024/01/15';

-- Drop partition
ALTER TABLE logs DROP PARTITION (year=2022);

-- Show partitions
SHOW PARTITIONS logs;

-- Repair table (recover partitions from HDFS)
MSCK REPAIR TABLE logs;

-- Drop table
DROP TABLE employees;           -- deletes data (managed) or just metadata (external)
DROP TABLE IF EXISTS employees;

-- Truncate table (removes data, keeps schema)
TRUNCATE TABLE employees;
```

#### Storage Formats

|Format|Description|Best For|
|---|---|---|
|**TEXTFILE**|Plain text, default|Simple data, interoperability|
|**SEQUENCEFILE**|Binary key-value pairs|Intermediate results|
|**RCFILE**|Row-Columnar|Legacy columnar|
|**ORC**|Optimized Row Columnar|Best compression + performance|
|**PARQUET**|Columnar, Apache standard|Spark + Hive integration|
|**AVRO**|Schema-based, row-oriented|Kafka + schema evolution|

---

### Q.20 Hive Data Manipulation Language (DML)

> [!abstract] DML Operations in Hive

#### 1. Loading Data

**Load from Local File System:**

```sql
LOAD DATA LOCAL INPATH '/home/user/data/employees.csv'
INTO TABLE employees;

-- With overwrite
LOAD DATA LOCAL INPATH '/home/user/data/employees.csv'
OVERWRITE INTO TABLE employees;
```

**Load from HDFS:**

```sql
LOAD DATA INPATH '/hdfs/data/employees.csv'
INTO TABLE employees;
-- Note: This MOVES the file (not copies) from HDFS
```

**Load into Partition:**

```sql
LOAD DATA LOCAL INPATH '/data/jan_sales.csv'
INTO TABLE sales
PARTITION (year=2024, month=1);
```

#### 2. INSERT Operations

**Insert from SELECT:**

```sql
-- Append
INSERT INTO TABLE it_employees
SELECT * FROM employees WHERE department='IT';

-- Overwrite
INSERT OVERWRITE TABLE it_employees
SELECT * FROM employees WHERE department='IT';
```

**Insert into Partition:**

```sql
-- Static partition
INSERT INTO TABLE logs PARTITION (year=2024, month=1)
SELECT log_id, message, severity FROM raw_logs
WHERE year=2024 AND month=1;

-- Dynamic partition
SET hive.exec.dynamic.partition=true;
SET hive.exec.dynamic.partition.mode=nonstrict;

INSERT INTO TABLE logs PARTITION (year, month)
SELECT log_id, message, severity, year, month FROM raw_logs;
```

**Multi-Table Insert:**

```sql
FROM employees
INSERT INTO TABLE it_staff SELECT * WHERE department='IT'
INSERT INTO TABLE hr_staff SELECT * WHERE department='HR'
INSERT INTO TABLE finance_staff SELECT * WHERE department='Finance';
```

**Insert Values (Hive 0.14+):**

```sql
INSERT INTO TABLE employees VALUES
(1, 'Alice', 75000, 'IT'),
(2, 'Bob', 65000, 'HR');
```

#### 3. UPDATE and DELETE (ACID Tables)

> [!warning] Requirements UPDATE/DELETE require:
> 
> - ORC storage format
> - Bucketing enabled
> - `transactional=true` table property
> - `hive.support.concurrency=true`

```sql
-- Enable ACID
SET hive.support.concurrency=true;
SET hive.enforce.bucketing=true;
SET hive.exec.dynamic.partition.mode=nonstrict;
SET hive.txn.manager=org.apache.hadoop.hive.ql.lockmgr.DbTxnManager;

-- UPDATE
UPDATE employees SET salary = salary * 1.1 WHERE department='IT';

-- DELETE
DELETE FROM employees WHERE emp_id = 1001;
```

#### 4. EXPORT and IMPORT

```sql
-- Export table to HDFS
EXPORT TABLE employees TO '/backup/employees_export';

-- Import table from HDFS
IMPORT TABLE employees_restored FROM '/backup/employees_export';
```

#### 5. Writing Query Results to Files

```sql
-- Write to local file system
INSERT OVERWRITE LOCAL DIRECTORY '/tmp/output'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT * FROM employees;

-- Write to HDFS
INSERT OVERWRITE DIRECTORY '/hdfs/output/employees'
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
SELECT * FROM employees WHERE salary > 50000;
```

---

### Q.21 Querying and Analyzing Data in Hive

> [!abstract] Data Querying and Analytics

#### 1. Basic SELECT

```sql
SELECT * FROM employees;
SELECT name, salary FROM employees;
SELECT DISTINCT department FROM employees;
SELECT name, salary * 12 AS annual_salary FROM employees;
```

#### 2. WHERE Clause & Filtering

```sql
SELECT * FROM employees WHERE salary > 60000;
SELECT * FROM employees WHERE department = 'IT' AND salary > 70000;
SELECT * FROM employees WHERE department IN ('IT', 'Finance', 'HR');
SELECT * FROM employees WHERE name LIKE 'A%';
SELECT * FROM employees WHERE salary BETWEEN 50000 AND 80000;
SELECT * FROM employees WHERE email IS NULL;
```

#### 3. Aggregation

```sql
-- COUNT, SUM, AVG, MIN, MAX
SELECT
    department,
    COUNT(*) AS emp_count,
    AVG(salary) AS avg_salary,
    MAX(salary) AS max_salary,
    MIN(salary) AS min_salary,
    SUM(salary) AS total_salary
FROM employees
GROUP BY department;

-- HAVING (filter after aggregation)
SELECT department, AVG(salary) AS avg_sal
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
```

#### 4. Sorting

```sql
-- ORDER BY: Global sort (single reducer)
SELECT * FROM employees ORDER BY salary DESC;

-- SORT BY: Sort per reducer (faster, not globally sorted)
SELECT * FROM employees SORT BY salary DESC;

-- DISTRIBUTE BY: Control which reducer gets which data
SELECT * FROM employees DISTRIBUTE BY department SORT BY salary;

-- CLUSTER BY: DISTRIBUTE BY + SORT BY same column
SELECT * FROM employees CLUSTER BY department;
```

#### 5. Joins for Analysis

```sql
-- Department-wise employee and manager data
SELECT e.name, e.salary, d.dept_name, m.manager_name
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
LEFT JOIN managers m ON d.dept_id = m.dept_id
ORDER BY e.salary DESC;
```

#### 6. Subqueries

```sql
-- Find employees earning above company average
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Find departments with more than 5 employees
SELECT department
FROM (
    SELECT department, COUNT(*) as cnt
    FROM employees
    GROUP BY department
) dept_counts
WHERE cnt > 5;
```

#### 7. Common Table Expressions (CTE)

```sql
WITH
dept_avg AS (
    SELECT department, AVG(salary) AS avg_sal
    FROM employees
    GROUP BY department
),
high_earners AS (
    SELECT e.name, e.salary, e.department
    FROM employees e
    JOIN dept_avg d ON e.department = d.department
    WHERE e.salary > d.avg_sal
)
SELECT * FROM high_earners ORDER BY salary DESC;
```

#### 8. Window Functions (Analytics)

```sql
SELECT
    name,
    department,
    salary,
    -- Rank within department
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dept_rank,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rank,
    -- Row number
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num,
    -- Running total
    SUM(salary) OVER (PARTITION BY department ORDER BY salary) AS running_total,
    -- Lead and Lag
    LAG(salary, 1) OVER (PARTITION BY department ORDER BY hire_date) AS prev_salary,
    LEAD(salary, 1) OVER (PARTITION BY department ORDER BY hire_date) AS next_salary,
    -- Percentile
    PERCENT_RANK() OVER (PARTITION BY department ORDER BY salary) AS pct_rank
FROM employees;
```

#### 9. CASE Statements

```sql
SELECT
    name,
    salary,
    CASE
        WHEN salary >= 80000 THEN 'High'
        WHEN salary >= 60000 THEN 'Medium'
        WHEN salary >= 40000 THEN 'Low'
        ELSE 'Entry Level'
    END AS salary_band
FROM employees;
```

#### 10. String and Date Functions

```sql
-- String functions
SELECT
    UPPER(name),
    LOWER(department),
    LENGTH(name),
    SUBSTR(name, 1, 5),
    CONCAT(name, ' - ', department),
    REGEXP_REPLACE(phone, '[^0-9]', '') AS cleaned_phone
FROM employees;

-- Date functions
SELECT
    hire_date,
    YEAR(hire_date) AS hire_year,
    MONTH(hire_date) AS hire_month,
    DATEDIFF(CURRENT_DATE, hire_date) AS days_employed,
    DATE_ADD(hire_date, 365) AS first_anniversary
FROM employees;
```

#### 11. Analytical Query Examples

**Top-N per Group:**

```sql
-- Top 3 highest paid employees per department
SELECT name, department, salary
FROM (
    SELECT name, department, salary,
        ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn
    FROM employees
) ranked
WHERE rn <= 3;
```

**Pivot-style Analysis:**

```sql
SELECT
    year,
    SUM(CASE WHEN quarter=1 THEN revenue ELSE 0 END) AS Q1,
    SUM(CASE WHEN quarter=2 THEN revenue ELSE 0 END) AS Q2,
    SUM(CASE WHEN quarter=3 THEN revenue ELSE 0 END) AS Q3,
    SUM(CASE WHEN quarter=4 THEN revenue ELSE 0 END) AS Q4
FROM quarterly_sales
GROUP BY year;
```

**Year-over-Year Growth:**

```sql
WITH yearly AS (
    SELECT YEAR(sale_date) AS yr, SUM(amount) AS total
    FROM sales
    GROUP BY YEAR(sale_date)
)
SELECT
    yr,
    total,
    LAG(total) OVER (ORDER BY yr) AS prev_year,
    ROUND((total - LAG(total) OVER (ORDER BY yr)) / LAG(total) OVER (ORDER BY yr) * 100, 2) AS growth_pct
FROM yearly;
```

#### 12. Query Optimization Tips

> [!tip] Performance Best Practices

```sql
-- 1. Use partition filters
SELECT * FROM logs WHERE year=2024 AND month=1;  ✅

-- 2. Enable map join for small tables
SET hive.auto.convert.join=true;

-- 3. Use ORC format with predicate pushdown
SET hive.optimize.ppd=true;

-- 4. Enable Cost Based Optimizer
SET hive.cbo.enable=true;
SET hive.stats.autogather=true;

-- 5. Use LIMIT for exploratory queries
SELECT * FROM large_table LIMIT 100;

-- 6. Analyze tables for statistics
ANALYZE TABLE employees COMPUTE STATISTICS;
ANALYZE TABLE employees COMPUTE STATISTICS FOR COLUMNS;

-- 7. Use EXPLAIN to view query plan
EXPLAIN SELECT * FROM employees WHERE department='IT';
EXPLAIN EXTENDED SELECT * FROM employees WHERE department='IT';
```

---

## 📚 Quick Reference Card

> [!summary] Hive Cheat Sheet

### Essential Commands

```sql
SHOW DATABASES;                              -- List databases
USE db_name;                                 -- Switch database
SHOW TABLES;                                 -- List tables
DESCRIBE table_name;                         -- Show schema
SHOW PARTITIONS table_name;                  -- List partitions
MSCK REPAIR TABLE table_name;               -- Sync partitions

-- Execution engine
SET hive.execution.engine=tez;

-- Dynamic partitioning
SET hive.exec.dynamic.partition=true;
SET hive.exec.dynamic.partition.mode=nonstrict;
```

### File Formats

```
TextFile → Simple CSV/TSV
ORC      → Best for Hive (compression + columnar)
Parquet  → Best for Spark interop
Avro     → Best for schema evolution
```

### Key Properties

```
hive.execution.engine          = tez/mr/spark
hive.auto.convert.join         = true (map join)
hive.cbo.enable                = true (optimizer)
hive.exec.dynamic.partition    = true
hive.support.concurrency       = true (ACID)
```

---

_Notes compiled for Apache Hive 3.x | Last Updated: 2024_