
**Pig** is a scripting platform for Hadoop that processes and analyzes large datasets without requiring complex Java code. Developed by Yahoo to simplify big data analysis.

---

## Why Pig?

- **Problem**: MapReduce required lengthy Java code (70-80 lines for simple queries)
- **Solution**: Pig Latin — procedural scripting language for non-programmers
- Reduces development time, easier to maintain and optimize

---

## MapReduce vs Hive vs Pig

| Aspect           | MapReduce                                 | Hive              | Pig                                       |
| ---------------- | ----------------------------------------- | ----------------- | ----------------------------------------- |
| **Language**     | Java/Python (compiled)                    | HiveQL (SQL-like) | Pig Latin (scripting)                     |
| **Data Types**   | Structured, semi-structured, unstructured | Structured only   | Structured, semi-structured, unstructured |
| **Code Length**  | 70-80 lines                               | Short SQL queries | Few lines of script                       |
| **Partitioning** | Yes                                       | Yes               | No                                        |
| **Users**        | Programmers                               | Data analysts     | Researchers, programmers                  |
| **Performance**  | Fastest                                   | Medium            | Medium (better than Hive)                 |
| **Abstraction**  | Low                                       | High              | High                                      |


| Feature               | Apache Pig                                                                | MapReduce                                   |
| --------------------- | ------------------------------------------------------------------------- | ------------------------------------------- |
| **Language Type**     | High-level data flow language (Pig Latin)                                 | Low-level programming paradigm              |
| **Ease of Use**       | Easier; SQL-like syntax, ideal for non-Java developers                    | Complex; requires Java programming skills   |
| **Lines of Code**     | Fewer lines (10 lines of Pig ≈ 200 lines of MapReduce)                    | Verbose, requires more code                 |
| **Abstraction Level** | High-level abstraction                                                    | Low-level, rigid framework                  |
| **Join Operations**   | Simple and built-in                                                       | Difficult and manual                        |
| **Compilation**       | No explicit compilation; Pig scripts convert to MapReduce jobs at runtime | Requires explicit compilation               |
| **Data Structures**   | Supports complex types (tuples, bags, maps)                               | Limited to key-value pairs                  |
| **Programming Model** | Declarative (focus on what to do)                                         | Imperative (explicit map and reduce steps)  |
| **Development Speed** | Faster development and prototyping                                        | Slower due to detailed coding               |
| **Execution Flow**    | Multi-query approach optimizes pipelines                                  | Each step often requires separate job setup |

Apache Pig internally compiles to MapReduce jobs, offering a simpler interface while leveraging Hadoop's scalability.

---

## Architecture

![](attachments/Pasted%20image%2020260421060451.png)

- **Pig Latin Scripts** — user writes procedural data flow code
- **Grunt Shell** — interactive command-line interface
- **Parser** — checks syntax, outputs DAG (Directed Acyclic Graph)
- **Optimizer** — optimizes logical plan
- **Compiler** — converts DAG to MapReduce jobs
- **Execution Engine** — runs on MapReduce/HDFS
- **DUMP** — displays results; **STORE** — saves to HDFS

---

## Pig Latin Data Model

Fully nestable hierarchy:

| Level     | Description                         | Example                 |
| --------- | ----------------------------------- | ----------------------- |
| **Atom**  | Single primitive value              | `50`, `"Rob"`           |
| **Tuple** | Sequence of fields (like a row)     | `(Rob, 5)`              |
| **Bag**   | Collection of tuples (like a table) | `{(Rob,5), (Mike,10)}`  |
| **Map**   | Key-value pairs                     | `[name#'Mike', age#10]` |

---

## Execution Modes

**Data Location:**
- **Local Mode** — reads/writes to Linux filesystem (small datasets)
- **MapReduce Mode** — reads/writes to HDFS (default, large datasets)

**Code Writing:**
- **Interactive** — line-by-line in Grunt shell
- **Batch** — entire script in `.pig` file
- **Embedded** — user-defined functions (UDFs) in Java

---

## Common Pig Latin Commands

```pig
-- Load data
office = LOAD 'pig_input' USING PigStorage(',') AS (id:int, name:chararray, profession:chararray, age:int);

-- Project columns
office_each = FOREACH office GENERATE name, age;

-- Filter rows
office_filter = FILTER office BY profession == 'doctor';

-- Sort
office_desc = ORDER office BY id DESC;

-- Limit results
office_limit = LIMIT office 2;

-- Group by
grouped = GROUP office BY profession;

-- Display results
DUMP office;

-- Store to HDFS
STORE office INTO 'output_path';
```

---
## Key Features

- **Ease of programming** — SQL-like syntax, fewer lines
- **Handles all data types** — structured, semi-structured, unstructured
- **User-defined functions (UDFs)** — extend functionality
- **Rich operators** — JOIN, FILTER, GROUP, COUNT, etc.
- **Parallel processing** — multiple queries simultaneously
- **Auto optimization & compilation** — internal optimization

---

## Pig vs Hive

- **Pig** = procedural, flexible, handles unstructured data, for ETL/transformations
- **Hive** = declarative SQL, structured data only, for querying/reporting


# Questions

**PART-A**

- Q.1 What are the different ways of executing a Pig script?
	Apache Pig scripts can be executed in three primary ways:
	
	### 1. Interactive Mode (Grunt Shell)
	Run Pig commands directly in the Grunt shell for immediate feedback. This mode is ideal for testing and development.
	*   Start the shell with: `pig -x local` (for local mode) or `pig -x mapreduce` (for HDFS mode).
	*   Enter Pig Latin statements like `A = LOAD 'data.txt'; DUMP A;` at the `grunt>` prompt.
	
	### 2. Batch Mode (Script)
	Execute a complete script file containing a series of Pig Latin statements.
	*   Write your script in a file (e.g., `script.pig`).
	*   Run it from the command line: `pig -x local script.pig` or `pig -x mapreduce script.pig`.
	*   From within the Grunt shell, use the `exec script.pig` or `run script.pig` commands.
	
	### 3. Embedded Mode (UDF)
	Integrate Pig scripts within applications written in languages like Java, Python, or Ruby by defining and using User-Defined Functions (UDFs).
- Q.2 What is Pig scripts?
    A **Pig script** is a program written in **Pig Latin**, a high-level, declarative scripting language used to analyze and process large datasets in the Hadoop ecosystem.  It defines a sequence of data flow operations (like LOAD, FILTER, JOIN, GROUP, STORE) that are internally compiled into MapReduce, Tez, or Spark jobs for execution. 
- Q.3 Explain parser.
    The **parser** is the first component in the Pig execution stack.  It receives the Pig script and performs **syntax checking, type checking, and other validation**.  Its output is a **Directed Acyclic Graph (DAG)**, which represents the Pig Latin statements and logical operators, with operators as nodes and data flows as edges. 
- Q.4 What is the aim of optimizer.
    The **optimizer** receives the DAG from the parser and performs **logical optimizations** to improve the efficiency of the execution plan.  Key optimizations include **projection pushdown** (removing unnecessary columns early) and **filter pushdown** (applying filters as early as possible), which reduce the amount of data processed in subsequent steps. 
- Q.5 Write the function of compiler and execution engine.
    The **compiler** takes the optimized logical plan (DAG) and **compiles it into a series of physical MapReduce (or Tez/Spark) jobs**.  The **execution engine** is responsible for **submitting these compiled jobs to the Hadoop cluster in the correct order** and managing their execution to produce the final output.
- Q.6 Explain tuple operator.
		In Apache Pig, a **tuple** is an **ordered set of fields**, similar to a row in a database table.  The **tuple constructor operator** is the pair of parentheses `( )`. 
	*   **Syntax & Use**: `(field1, field2, ..., fieldN)` is used to create a tuple from specified elements. For example, `(Raju, 30)` creates a tuple with two fields.
	*   **Dereferencing**: You can access a field within a tuple using the dot operator `.` by its name (e.g., `tuple.name`) or its positional notation (e.g., `tuple.$0` for the first field).
- Q.7 What do you mean by bag and map operator?
	*   **Bag**: A **bag** is a **collection of tuples**, similar to a table in a database.  It is unordered and can contain duplicates. The **bag constructor operator** is the pair of curly braces `{ }`.  For example, `{(Raju, 30), (Mohammad, 45)}` creates a bag with two tuples. Bags are often the result of operations like `GROUP` or `JOIN`. 
	
	*   **Map**: A **map** is a **set of key-value pairs**, where the key must be a `chararray` (string) and the value can be any data type.  The **map constructor operator** is the pair of square brackets `[ ]`.  For example, `['name'#'Raju', 'age'#30]` creates a map. You access a value using the pound operator `#` (e.g., `map#'name'`).
- Q.8 What is the use of having filters in Apache Pig?
	The **FILTER operator** in Apache Pig is used to **select specific tuples (rows) from a relation based on a defined condition**, effectively removing unwanted data. 
	
	*   **Purpose**: It works similarly to the `WHERE` clause in SQL, allowing you to include only the data that meets your criteria (e.g., `FILTER A BY age > 30;`) or to remove data you don't want. 
	*   **Syntax**: `new_relation = FILTER old_relation BY condition;`
	*   **Usage**: The condition is a boolean expression using comparison operators (`==`, `!=`, `>`, `<`, etc.) and logical operators (`AND`, `OR`, `NOT`). For example, `FILTER data BY state == 'CA' AND salary > 50000;` creates a new relation with only the records from California earning over 50,000.
- Q.9 Suppose there's a file called “test.txt” having 150 records in HDFS. Write the PIG command to retrieve the first 10 records of the file.
	To retrieve the first 10 records from the file `test.txt` in HDFS using Apache Pig, use the **`LIMIT`** operator. 
	
	1.  **Load** the data from HDFS into a relation. 
	2.  **Apply** the `LIMIT` operator to that relation.
	
	```pig
	data = LOAD 'test.txt' USING PigStorage() AS (/* define your schema here */);
	first_10 = LIMIT data 10;
	DUMP first_10;
	```
	
	The `LIMIT data 10;` command will return up to 10 tuples from the `data` relation. Note that without an `ORDER BY` clause, the specific 10 records returned are not guaranteed to be the first 10 in the file, as Pig processes data in a distributed manner. However, for the purpose of simply getting *any* 10 records from the file, this is the correct command.
- Q.10 What are the features of bag?
	A **bag** in Apache Pig is an **unordered collection of tuples**, which may contain duplicates.  Its key features are:
	*   **Unordered**: There is no guaranteed order for tuples within a bag. 
	*   **Duplicates Allowed**: A bag can contain multiple identical tuples. 
	*   **Flexible Schema**: Tuples within a bag can have a different number of fields or different data types. However, for effective processing, Pig expects a consistent schema. 
	*   **Null Substitution**: If Pig tries to access a field that doesn't exist in a tuple, it substitutes a `null` value.

- Q.11 What is an outer bag?

	An **outer bag** is **synonymous with a relation** in Pig.  It is the top-level container for a dataset, equivalent to a table in a relational database. For example, the result of a `LOAD` statement is an outer bag.

- Q.12 What is an inner bag?
	An **inner bag** in Apache Pig is a **bag that exists as a field within a tuple of another bag** (typically the outer bag or relation).  It arises commonly when using operations like `GROUP` or `COGROUP`, where grouped data is stored inside a bag nested within each output tuple. 
	
	Inner bags are essential for handling grouped or structured data, allowing Pig to represent hierarchical datasets — for example, all records associated with a specific key. 
	
	### Example
	
	Consider a relation `A` loaded from data:
	
	```pig
	A = LOAD 'data' AS (f1:int, f2:int, f3:int);
	DUMP A;
	```
	
	Output:
	```
	(1,2,3)
	(4,2,1)
	(8,3,4)
	(4,3,3)
	```
	
	Now, group `A` by the first field:
	
	```pig
	X = GROUP A BY f1;
	DUMP X;
	```
	
	Output:
	```
	(1,{(1,2,3)})
	(4,{(4,2,1),(4,3,3)})
	(8,{(8,3,4)})
	```
	
	Here:
	- `X` is a relation (outer bag).
	- Each tuple in `X` has two fields: `f1` (int) and `A` (bag of tuples).
	- The second field `{(4,2,1),(4,3,3)}` is an **inner bag** — it's a bag nested inside the tuple.

**PART-B**

- Q.13 What are the various diagnostic operators available in Apache Pig?
	Apache Pig provides **four main diagnostic operators** used for debugging, inspecting execution plans, and verifying data flow in Pig Latin scripts. 
	
	### 1. **DUMP Operator**
	- **Purpose**: Executes the Pig Latin script up to that point and **displays the results on the terminal**. 
	- **Use Case**: Debugging data at intermediate steps. 
	- **Syntax**:  
	  ```pig
	  DUMP alias;
	  ```
	
	### 2. **DESCRIBE Operator**
	- **Purpose**: **Displays the schema** (data structure) of a relation. 
	- **Use Case**: Verifying field names and data types after transformations. 
	- **Syntax**:  
	  ```pig
	  DESCRIBE alias;
	  ```
	
	### 3. **EXPLAIN Operator**
	- **Purpose**: **Shows the logical, physical, and MapReduce execution plans** used to compute a relation. 
	- **Use Case**: Understanding how Pig translates scripts into execution jobs, useful for optimization.
	- **Syntax**:  
	  ```pig
	  EXPLAIN alias;
	  ```
	
	### 4. **ILLUSTRATE Operator**
	- **Purpose**: **Demonstrates the step-by-step execution** of a sequence of Pig Latin statements using small subsets of data. 
	- **Use Case**: Debugging complex transformations by visualizing data flow. 
	- **Syntax**:  
	  ```pig
	  ILLUSTRATE alias;
	  ```
- Q.22 Explain the various [[pig latin operations]].
- Q.14 State the usage of the group, order by, and distinct keywords in Pig scripts.
	### GROUP
	
	- **Purpose**: Groups tuples by one or more key fields. 
	- **Usage**: Creates a new relation where each tuple contains a **group key** and a **bag of all tuples** that share that key. 
	- **Example**:
	    
	    ```
	    grouped = GROUP data BY age;
	    ```
	    
	
	### ORDER BY
	
	- **Purpose**: Sorts a relation by one or more fields in ascending (`ASC`) or descending (`DESC`) order. 
	    
	- **Usage**: Useful for ordered output or ensuring consistent results. 
	    
	- **Example**:
	    
	    ```
	    sorted = ORDER data BY salary DESC;
	    ```
	    
	
	### DISTINCT
	
	- **Purpose**: Removes duplicate tuples from a relation. 
	    
	- **Usage**: Applied to entire tuples; for partial field deduplication, use `GROUP BY` on those fields followed by `FLATTEN`. 
	    
	- **Example**:
	    
	    ```
	    unique = DISTINCT data;
	    ```
- Q.17 Explain grunt.
	**Grunt** is the **interactive command-line shell** provided by Apache Pig for writing and executing Pig Latin scripts.  It allows users to interactively enter Pig Latin statements, run HDFS and shell commands, and debug scripts in real time. 
	
	### Key Features:
	- **Interactive Execution**: Enter Pig Latin statements line by line and see results using `DUMP` or `DESCRIBE`. 
	- **Shell Integration**: Run HDFS commands using `fs -ls`, `fs -cat`, etc., and local shell commands using `sh ls`, `sh cat`. 
	- **Script Execution**: Use `run` or `exec` to execute Pig scripts from within the shell. 
	- **Utility Commands**: Supports `help`, `clear`, `history`, `set`, and `quit` for environment control and debugging. 
	
	### Starting Grunt:
	```bash
	$ pig -x local    # Local mode
	$ pig             # MapReduce mode (default)
	```
	
	Once started, the prompt changes to `grunt>`, indicating readiness for input.
- Q.19 Write the features of Pig.
	Apache Pig is a high-level data processing platform designed for Hadoop, offering several key features:
	
	### Rich Set of Operators
	Provides built-in operators for **join, filter, group, order by, distinct**, and more, simplifying complex data transformations. 
	
	### Ease of Programming
	Uses **Pig Latin**, a SQL-like scripting language that is easy to learn, especially for those familiar with SQL, reducing the need for complex Java MapReduce code. 
	
	### Optimization Opportunities
	Automatically optimizes execution plans (e.g., projection and pushdown), allowing developers to focus on data semantics rather than performance tuning. 
	
	### Extensibility
	Supports **User-Defined Functions (UDFs)** in Java, Python, or other languages to extend functionality for custom data processing tasks. 
	
	### Handles All Data Types
	Processes **structured, semi-structured, and unstructured** data, storing results in HDFS. 
	
	### Multi-Query Approach
	Reduces code length significantly by enabling pipeline-style data flow, minimizing the need for intermediate storage and improving development efficiency. 
	
	### Nested Data Types
	Supports complex data types like **tuples, bags, and maps**, enabling representation of hierarchical and nested data structures.
- Q.21 Explain Pig Latin application flow.
	The Pig Latin application flow consists of three main phases:
	
	1. **Parsing**:  
	   The script is parsed by the **Parser**, which checks syntax, performs type checking, and produces a **Directed Acyclic Graph (DAG)** representing the logical plan. 
	
	2. **Optimization**:  
	   The logical plan is passed to the **Optimizer**, which applies transformations like projection pushdown and redundant operation removal to improve efficiency. 
	
	3. **Compilation & Execution**:  
	   The optimized plan is **compiled into MapReduce jobs** (or Tez/Spark tasks), which are then submitted to Hadoop for execution.  Results are stored or displayed using `STORE` or `DUMP`.
	
	Pig operates as a **dataflow language**, where data moves through a sequence of transformations defined by operators like `LOAD`, `FILTER`, `GROUP`, and `JOIN`.
	
- Q.25 Explain nested model and also explain interactive modes of Pig.
	## Nested Model in Apache Pig
	
	Apache Pig's data model is **fully nested**, supporting complex, hierarchical structures through:
	
	- **Atom**: A single atomic value (e.g., string, number). 
	- **Tuple**: An ordered set of fields (e.g., `(name, age)`). 
	- **Bag**: An unordered collection of tuples, which can contain inner bags. 
	- **Map**: A collection of key-value pairs (e.g., `['name'#'John']`).
	
	A **relation** is a bag of tuples and may contain nested elements like inner bags, enabling rich data representations.
