Pig Latin operations can be categorized into four main types: **Relational**, **Arithmetic**, **Diagnostic**, and **Query & Analysis**. Each category serves a distinct purpose in data processing.

---

## 1. Relational Operations
 https://www.edureka.co/blog/operators-in-apache-pig/
These operations manipulate data structure, similar to SQL operations.

| Operation    | Purpose                              | Example                                                                      |
| ------------ | ------------------------------------ | ---------------------------------------------------------------------------- |
| **LOAD**     | Read data from HDFS/local            | `data = LOAD 'input.txt' USING PigStorage(',') AS (id:int, name:chararray);` |
| **STORE**    | Write data to HDFS                   | `STORE data INTO 'output_path';`                                             |
| **FILTER**   | Select rows based on condition       | `filtered = FILTER data BY age > 20;`                                        |
| **FOREACH**  | Apply transformation to each row     | `transformed = FOREACH data GENERATE id, UPPER(name);`                       |
| **GROUP**    | Group data by key(s)                 | `grouped = GROUP data BY dept;`                                              |
| **JOIN**     | Combine data from multiple relations | `joined = JOIN data1 BY id, data2 BY id;`                                    |
| **CROSS**    | Cartesian product of two relations   | `crossed = CROSS data1, data2;`                                              |
| **UNION**    | Combine relations                    | `combined = UNION data1, data2;`                                             |
| **DISTINCT** | Remove duplicates                    | `unique = DISTINCT data;`                                                    |
| **SPLIT**    | Divide relation into multiple parts  | `SPLIT data INTO data_young IF age < 30, data_old IF age >= 30;`             |

---

## 2. Arithmetic Operations

These operations perform mathematical calculations on numeric data.

| Operation | Purpose | Example |
|---|---|---|
| **+** | Addition | `result = FOREACH data GENERATE id, salary + 1000;` |
| **-** | Subtraction | `result = FOREACH data GENERATE id, salary - 500;` |
| **\*** | Multiplication | `result = FOREACH data GENERATE id, salary * 1.1;` |
| **/** | Division | `result = FOREACH data GENERATE id, salary / 1000;` |
| **%** | Modulo | `result = FOREACH data GENERATE id, salary % 100;` |
| **ABS()** | Absolute value | `result = FOREACH data GENERATE id, ABS(salary);` |
| **ROUND()** | Round to nearest integer | `result = FOREACH data GENERATE id, ROUND(salary);` |
| **FLOOR()** | Round down to nearest integer | `result = FOREACH data GENERATE id, FLOOR(salary);` |
| **CEIL()** | Round up to nearest integer | `result = FOREACH data GENERATE id, CEIL(salary);` |
| **SQRT()** | Square root | `result = FOREACH data GENERATE id, SQRT(salary);` |
| **POW()** | Power | `result = FOREACH data GENERATE id, POW(salary, 2);` |

---

## 3. Diagnostic Operations

These operations analyze data structure and content.

| Operation      | Purpose                     | Example                                              |
| -------------- | --------------------------- | ---------------------------------------------------- |
| **DESCRIBE**   | Show schema of relation     | `DESCRIBE data;`                                     |
| **DUMP**       | Display results on screen   | `DUMP data;`                                         |
| **ILLUSTRATE** | Show step-by-step execution | `ILLUSTRATE data;`                                   |
| **EXPLAIN**    | Show execution plan         | `EXPLAIN data;`                                      |
| **CAT**        | Display content of a file   | `CAT 'input.txt';`                                   |
| **TOKENIZE()** | Split string into words     | `words = FOREACH data GENERATE TOKENIZE(name);`      |
| **FLATTEN()**  | Expand nested structures    | `flattened = FOREACH data GENERATE FLATTEN(grades);` |

---

## 4. Query & Analysis Operations

These operations perform aggregations and statistical analysis.

| Operation    | Purpose                | Example                                                   |
| ------------ | ---------------------- | --------------------------------------------------------- |
| **COUNT()**  | Count rows             | `count = FOREACH grouped GENERATE group, COUNT(data);`    |
| **SUM()**    | Sum values             | `sum = FOREACH grouped GENERATE group, SUM(data.salary);` |
| **AVG()**    | Calculate average      | `avg = FOREACH grouped GENERATE group, AVG(data.salary);` |
| **MIN()**    | Find minimum value     | `min = FOREACH grouped GENERATE group, MIN(data.salary);` |
| **MAX()**    | Find maximum value     | `max = FOREACH grouped GENERATE group, MAX(data.salary);` |
| **COGROUP**  | Group by multiple keys | `cogrouped = COGROUP data1 BY id, data2 BY id;`           |
| **ORDER**    | Sort data              | `sorted = ORDER data BY salary DESC;`                     |
| **LIMIT**    | Return top N rows      | `top = LIMIT data 10;`                                    |
| **RANK**     | Assign rank to rows    | `ranked = RANK data BY salary DESC;`                      |
| **DISTINCT** | Remove duplicates      | `unique = DISTINCT data;`                                 |

---

## Summary

| Category | Purpose | Key Operations |
|---|---|---|
| **Relational** | Data structure manipulation | LOAD, STORE, FILTER, FOREACH, GROUP, JOIN, UNION, SPLIT |
| **Arithmetic** | Mathematical calculations | +, -, *, /, %, ABS, ROUND, FLOOR, CEIL, SQRT, POW |
| **Diagnostic** | Data inspection and debugging | DESCRIBE, DUMP, ILLUSTRATE, EXPLAIN, CAT, TOKENIZE, FLATTEN |
| **Query & Analysis** | Aggregation and statistics | COUNT, SUM, AVG, MIN, MAX, COGROUP, ORDER, LIMIT, RANK |

Use **DUMP** to see results, **STORE** to save output, and **EXPLAIN** to understand execution plans.