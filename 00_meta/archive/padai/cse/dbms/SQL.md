[SQL Basics Cheat Sheet](https://www.datacamp.com/cheat-sheet/sql-basics-cheat-sheet) | [Join Cheat Sheet](https://www.datacamp.com/cheat-sheet/sql-joins-cheat-sheet) 

![](attachments/Pasted%20image%2020260430084314.png)


![](attachments/Pasted%20image%2020260430085650.png)

## [Types of Queries](https://medium.com/@sohamshinde156/basics-types-of-queries-in-sql-5f163ee44adf) 
DDL, DML, DQL, DCL, TCL — Data Definition, Manipulation, Query, Control, Transaction Control.

## Evaluation Order
`FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY`

## GROUP BY, HAVING, WHERE
- Non-aggregate fields in `SELECT` and `HAVING` must come from `GROUP BY`. No restriction on fields inside aggregate functions. [medium](https://medium.com/@riccardoodone/the-love-hate-relationship-between-select-and-group-by-in-sql-4957b2a70229)
- `WHERE` and `GROUP BY` can't use aggregate functions. Any field from `FROM` is allowed.
- `WHERE` filters rows before `GROUP BY` runs — reduces rows to be grouped. `HAVING` applies conditions group-wise after grouping.
- [HAVING Clause](https://www.w3schools.com/sql/sql_having.asp) 

## [Join](Join.md)

## DISTINCT
```sql
SELECT DISTINCT COL1, COL2 ...
```
`COL1, COL2` together form a distinct tuple. `COL2` alone may still have duplicates in output.

## Nested Queries
- **Independent**: inner query has no relation from outer query. Computed once, reused for each tuple.
- **[Correlated Queries](https://en.wikipedia.org/wiki/Correlated_subquery)**: inner query references outer query's relation. Recomputed for each tuple of the outer query. 

`WHERE` works with single values at a time. Operators to work with subquery results:
`op IN SQ`, `op ANY SQ`, `op ALL SQ`, `[NOT] EXISTS SQ`

## ORDER BY
Default is ascending. Priority is left to right — if `[1]` results in equality, check `[2]`, and so on.

## Alias (AS)
Temporary name for column, table, or subquery — lasts for duration of query.
- `SELECT` alias can't be used in `WHERE` or `GROUP BY` (SELECT runs after both).
- Table alias created in `FROM` can be used in `WHERE`.

## [[Aggregate Functions]]

## [[sql operators]]

## [[NULL]]
## WITH ... AS
Creates a named temporary relation usable in the following main query.
```sql
WITH cte_name AS (
    SELECT ...
)
SELECT * FROM cte_name;
```