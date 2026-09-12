NULL means absence of value — not zero, not empty string, just unknown/missing.

### Three-Valued Logic
SQL has three truth values: TRUE, FALSE, UNKNOWN.
Any comparison with NULL yields UNKNOWN, not FALSE.

| Expression     | Result  |
| -------------- | ------- |
| `NULL = NULL`  | UNKNOWN |
| `NULL <> NULL` | UNKNOWN |
| `NULL = 5`     | UNKNOWN |
| `NULL > 5`     | UNKNOWN |

`WHERE` and `HAVING` only keep rows where condition is TRUE. UNKNOWN rows are discarded — same effect as FALSE but not the same thing.

### Checking for NULL
```sql
-- ❌ Wrong — yields UNKNOWN, never catches NULL
WHERE val = NULL

-- ✅ Correct
WHERE val IS NULL
WHERE val IS NOT NULL
````

### Arithmetic

Any arithmetic with NULL propagates NULL. `5 + NULL = NULL`, `NULL * 0 = NULL`, `NULL / NULL = NULL`

### [[Aggregate Functions]]

### NULL in AND / OR

|A|B|A AND B|A OR B|
|---|---|---|---|
|TRUE|UNKNOWN|UNKNOWN|TRUE|
|FALSE|UNKNOWN|FALSE|UNKNOWN|
|UNKNOWN|UNKNOWN|UNKNOWN|UNKNOWN|

FALSE AND UNKNOWN = FALSE because no matter what UNKNOWN is, FALSE AND anything = FALSE. TRUE OR UNKNOWN = TRUE for same reason.

### [NULL trap with NOT IN](sql%20operators.md#^4ed70d)

### NULL in GROUP BY

NULL values are treated as equal for grouping — all NULL rows go into one group together.