**Set (Unary):** `EXISTS SQ`, `NOT EXISTS SQ`

**Set (Binary):** `UNION`, `INTERSECT`, `EXCEPT` (= set difference SQ1 − SQ2)

Tuple operators:

**`op IN SQ`**

True if `op` matches any value in the subquery result.

```sql
-- find employees in HR or IT
SELECT name FROM employees
WHERE dept IN ('HR', 'IT');

-- same with subquery
SELECT name FROM employees
WHERE dept IN (SELECT dept FROM allowed_depts);
```

---

**`op ANY SQ`**

True if the condition holds for **at least one** value in SQ. `SOME` is identical.

```sql
-- salary greater than at least one salary in HR dept
SELECT name FROM employees
WHERE salary > ANY (SELECT salary FROM employees WHERE dept = 'HR');
```

If HR has salaries `{30000, 50000, 70000}`, this returns employees with salary > 30000 (just needs to beat one).

---

**`op ALL SQ`**

True if the condition holds for **every** value in SQ.

```sql
-- salary greater than every salary in HR dept
SELECT name FROM employees
WHERE salary > ALL (SELECT salary FROM employees WHERE dept = 'HR');
```

Same HR `{30000, 50000, 70000}` — now employee must have salary > 70000.

---

**The equivalences:**

`IN` ↔ `= ANY` — both mean "equals at least one"

```sql
WHERE dept IN (SQ)
-- same as
WHERE dept = ANY (SQ)
```

`NOT IN` ↔ `<> ALL` — both mean "not equal to any single one"

```sql
WHERE dept NOT IN (SQ)
-- same as
WHERE dept <> ALL (SQ)
```

---

**NULL trap with NOT IN**  ^4ed70d

```sql
SELECT name FROM employees
WHERE dept NOT IN (SELECT dept FROM other_table);
```

If subquery result contains even one NULL → entire `NOT IN` returns UNKNOWN → **no rows returned at all.**

Because `'HR' <> NULL` = UNKNOWN, and UNKNOWN propagates.

`NOT EXISTS` is safer in this case:

```sql
SELECT name FROM employees E
WHERE NOT EXISTS (
    SELECT 1 FROM other_table O
    WHERE O.dept = E.dept
);
```

This is a classic GATE trap — `NOT IN` vs `NOT EXISTS` give different results when NULLs are present.