### 1. **Parser**

- Validates the **syntax** of the HiveQL query
- Checks if the query follows HiveQL grammar rules
- Converts query into an **Abstract Syntax Tree (AST)**
- If syntax is wrong → throws error

Example:
```sql
SELECT * FROM employees WHERE salary > 50000;
-- Parser checks: valid SELECT, valid table name, valid WHERE clause
```

---

### 2. **Semantic Analyzer**

- Validates the **semantic meaning** of the query
- Checks if:
  - Tables exist in metastore
  - Columns exist in those tables
  - Data types are compatible
  - Functions used are valid

Example:
```sql
SELECT * FROM nonexistent_table;  -- Semantic error: table doesn't exist
SELECT salary_invalid FROM employees;  -- Semantic error: column doesn't exist
```

---

### 3. **Optimizer**

- Creates an **optimized execution plan**
- Reduces unnecessary operations
- Reorders operations for efficiency
- Generates a **Directed Acyclic Graph (DAG)** of MapReduce/Spark tasks

Optimizations:
- Predicate pushdown (filter early)
- Join reordering
- Column pruning (select only needed columns)

---

### 4. **Compiler**

- Converts the optimized plan into **executable code**
- Generates MapReduce/Spark/Tez tasks
- Creates job configuration

---

### 5. **Execution Engine**

- Executes the compiled tasks
- Acts as a **bridge** between Hive and Hadoop
- Submits jobs to MapReduce, Spark, or Tez
- Monitors job progress

---

### 6. **Metastore**

- Stores and retrieves **metadata** (table schemas, column info, locations)
- Accessed during parsing and semantic analysis
- Provides table/partition information

---

### 7. **Driver**

- **Orchestrates** all components
- Receives query from client
- Passes query through: Parser → Semantic Analyzer → Optimizer → Compiler → Execution Engine
- Returns results to client

---

### Query Flow Diagram

```
User Query
    ↓
[Driver]
    ↓
[Parser] → checks syntax → AST
    ↓
[Semantic Analyzer] → checks table/column validity → consults [Metastore]
    ↓
[Optimizer] → creates optimized plan → DAG
    ↓
[Compiler] → generates MapReduce/Spark tasks
    ↓
[Execution Engine] → submits to Hadoop/Spark
    ↓
Results back to client
```

---
