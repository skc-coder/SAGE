
![](attachments/Pasted%20image%2020260430085650.png)

## Join
- Cartesian product just matches all rows to all rows of the two relations
- Joins use *comparison* to math rows
- Joins output only one column for the "common" columns b/w the relations specified in `USING` or `ON`
- If only matching rows in output -> inner join
- If non matching rows in output -> outer join


### Inner Join / Theta Join ($\theta$)
- Uses $<, >, \le, \ge, =, \ne$
- Returns only matching tuples
#### EQUI Join
- Theta Join using only equality ($=$)

#### Natural Join ($\bowtie$)
- EQUI Join but on all common attributes
- Removes duplicates automatically
- If no common attributes $\rightarrow$ Cross Product
- Columns = $|R| + |S| - \text{common attributes}$

### Outer Join
- Preserves non-matching tuples using NULLs
- They also have their "natural" join version, where common attributes are removed.

#### Left Outer Join ($\ ⟕$)
- Keeps all tuples from left relation
- Unmatched right attributes $\rightarrow$ NULL

#### Right Outer Join ($\ ⟖$)
- Keeps all tuples from right relation
- Unmatched left attributes $\rightarrow$ NULL

#### Full Outer Join ($\ ⟗$)
- Keeps all tuples from both relations




## SQL Join
**Point 1 — Self join needs aliasing**

```sql
-- ❌ Wrong — ambiguous, DB doesn't know which Employee is which
SELECT *
FROM Employee, Employee;

-- ✅ Correct
SELECT *
FROM Employee AS E, Employee AS M;
```

**Point 2 — Three ways to write Cartesian product**

```sql
-- All three are equivalent
SELECT * FROM A, B;
SELECT * FROM A CROSS JOIN B;
SELECT * FROM A JOIN B;          -- no ON/USING = CROSS JOIN
```


---

**Differences:**

**Cartesian Product (`CROSS JOIN`)**

- Every row of A paired with every row of B
- If A has m rows, B has n rows → result has m×n rows
- No condition, no duplicate column removal

```sql
SELECT * FROM A, B;
SELECT * FROM A CROSS JOIN B;
```

---

**Natural Join (`NATURAL JOIN`)**

- Automatically joins on ALL columns with same name in both tables
- Duplicate columns are removed from result
- If no common column exists → behaves like Cartesian product
- And on the other hand if $R$ and $S$ have same schema $R \bowtie S = R \cap S$.

```sql
SELECT * FROM A NATURAL JOIN B;
```

```
A(id, name)   B(id, dept)
→ joins on id automatically
→ result has (id, name, dept) not (id, name, id, dept)
```

---

**Full Outer Join (`FULL JOIN`)**

- Returns all rows from both tables
- Where match exists → combined row
- Where no match → NULL filled on the missing side

```sql
SELECT * FROM A FULL OUTER JOIN B ON A.id = B.id;
```

**Summary table:**

| Condition       | Duplicates removed     | Unmatched rows |                      |
| --------------- | ---------------------- | -------------- | -------------------- |
| Cartesian       | None                   | No             | All combinations     |
| Natural Join    | Auto on same-name cols | Yes            | Only matches         |
| Inner Join      | Manual ON clause       | No             | Only matches         |
| Full Outer Join | Manual ON clause       | No             | Both sides with NULL |
