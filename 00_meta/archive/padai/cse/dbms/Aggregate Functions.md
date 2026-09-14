Always return a set of cardinality at min 1 — never empty. 
May return `{NULL}` or `{0}` but not empty set. 
So `EXISTS COUNT(*)` is always true.

All aggregate functions ignore NULL except `COUNT(*)`.

| Function             | Behaviour                           |
| -------------------- | ----------------------------------- |
| `COUNT(*)`           | counts all rows including NULL rows |
| `COUNT(col)`         | counts only non-NULL values         |
| `SUM, AVG, MAX, MIN` | ignore NULL values entirely         |

If all values are NULL → `SUM/AVG/MAX/MIN` return NULL, `COUNT(*)` returns row count, `COUNT(col)` returns 0.

```sql
CREATE TABLE t (val INT);
INSERT INTO t VALUES (NULL);
INSERT INTO t VALUES (NULL);
```

**Results:**

|Function|Output|
|---|---|
|`COUNT(*)`|2|
|`COUNT(val)`|0|
|`MAX(val)`|NULL|
|`MIN(val)`|NULL|
|`SUM(val)`|NULL|
|`AVG(val)`|NULL|

**Why:**

- `COUNT(*)` counts rows, doesn't care about values → 2
- `COUNT(val)` counts non-NULL values → 0
- All others ignore NULL, so they're operating on an empty set → return NULL

---

**Edge case — empty table (no rows at all):**

|Function|Output|
|---|---|
|`COUNT(*)`|0|
|`COUNT(val)`|0|
|`MAX(val)`|NULL|
|`MIN(val)`|NULL|
|`SUM(val)`|NULL|
|`AVG(val)`|NULL|

So `MAX/MIN/SUM/AVG` on empty set = NULL, not 0. Only `COUNT` returns 0.

This is why the statement _"aggregate functions always return non-empty set"_ holds — they always return exactly one row, but that row's value may be NULL.