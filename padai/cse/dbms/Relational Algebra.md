### Divide
The Relational Division operator is used for queries involving **universal quantification**, typically identified by the keyword **"ALL"**.
Example: "Find sailors who have reserved *all* boats."

### Conditions
1. $Attr(s) \subset Attr(r)$ (Attributes of $s$ must be a proper subset of $r$).
2. Let $L = Attr(r) - Attr(s)$. The result relation will contain only attributes in $L$.

### Relational Algebra Formula
Division is a derived operator and is expressed using fundamental operators as:

$$r \div s = \pi_L(r) - \pi_L((\pi_L(r) \times s) - r)$$

### Logical Breakdown
1. $\pi_L(r) \times s$: Calculate all theoretically possible combinations of $L$ and $s$.
2. $(\dots) - r$: Find "missing" tuples (combinations that should exist but aren't in $r$).
3. $\pi_L(\dots)$: Extract the values from $L$ that are "incomplete."
4. $\pi_L(r) - \dots$: Subtract "incomplete" values from the set of all $L$ values to get those that matched *every* $s$.

### SQL Implementation

#### 1. Solution with EXCEPT (2-Level Nesting)
Based on the logic: "There exists no boat that has not been reserved by the sailor."

```sql
SELECT S.sname
FROM Sailors S
WHERE NOT EXISTS (
    (SELECT B.bid FROM Boats B) -- Set of all possible boats
    EXCEPT
    (SELECT R.bid FROM Reserves R WHERE R.sid = S.sid) -- Boats reserved by S
);
```

#### 2. Solution without EXCEPT (3-Level Nesting)
Uses correlated subqueries to check for the absence of a missing reservation.

```sql
SELECT S.sname
FROM Sailors S
WHERE NOT EXISTS (
    SELECT B.bid
    FROM Boats B
    WHERE NOT EXISTS (
        SELECT *
        FROM Reserves R
        WHERE R.bid = B.bid
        AND R.sid = S.sid
    )
);
