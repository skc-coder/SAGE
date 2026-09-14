# 2.3.4 — The Select Algorithm

> **Goal:** Given an unsorted array `A` of `n` elements and an integer `k`, find the **kth smallest element** of `A`.

---

## 📌 Problem Definition

| Term       | Meaning                                             |
| ---------- | --------------------------------------------------- |
| **Input**  | Unsorted array `A` of `n` elements, and integer `k` |
| **Output** | `select(A, k)` → the kth smallest element of `A`    |

### Special Cases

$$\text{select}(A,\ 1) = \min \qquad \text{select}!\left(A,\ \left\lfloor\tfrac{n}{2}\right\rfloor\right) = \text{median} \qquad \text{select}(A,\ n) = \max$$

### Example

```
A = [7, 2, 6, 9, 1, 6, 4, 11]

select(A, 1) = 1    ← minimum
select(A, 8) = 11   ← maximum
```

---

## 💡 Naive Approach

> Simply **sort** the array and return `A[k-1]`.

- Time complexity: $O(n \log n)$
- ❓ Can we do **better**?

---

## ⚡ Quickselect — Using Partition

We borrow the **partition step from Quicksort**.

### How Partition Works

Partition picks a **pivot** and rearranges the array so that:

- All elements **left** of pivot are smaller
- All elements **right** of pivot are larger
- The pivot is at its **correct sorted position** `m`

```
Original:  [ 3 | 2 | 9 | 8 | 1 | 6 | 4 | 11 ]   ← pivot chosen randomly

After partition:
  Left part      Pivot   Right part
[ 3  2  1  4 ] | [6] | [ 7  8  11 ]
  indices 1–4     5     indices 6–8
```

> _After partitioning, if pivot lands at index 5, we know for sure the **5th smallest element is 6**._

### Key Insight

|Condition|Action|
|---|---|
|`k == m`|Pivot **is** the answer!|
|`k < m`|Answer is in the **left half**|
|`k > m`|Answer is in the **right half**|

---

## 🧾 Pseudocode

```python
select(A, p, q, k):
    if (p == q):
        return A[0]

    m = partition(A, p, q)       # m = final index of pivot

    if (m == k):
        return A[m]              # pivot is the kth smallest

    if (k < m):
        return select(A, p, m-1, k)          # search left half

    if (k > m):
        return select(A, m+1, q, k-m)
        # k-m because indexing restarts from 0 at m+1
```

> [!note] Why `k - m` in the right recursive call? When we recurse on the right subarray `A[m+1..q]`, the indices reset. So if we wanted the overall `k`th element and the pivot was at `m`, we now want the `(k - m)`th element in the right subarray.

---

## ⏱️ Time Complexity

### Worst Case

$$T(n) = T(n-1) + \Theta(n) = \Theta(n^2)$$

- Occurs when partition is **maximally unequal** every time (e.g., always picks min or max as pivot)
- This is _worse_ than just sorting!

### Average Case

$$T(n) = O(n)$$

- With random pivot selection, expected linear time

---

## 🧠 Median of Medians (MOM Algorithm)

> [!tip] **The clever fix for worst-case linear time** The **Median of Medians** algorithm finds an _approximate_ median deterministically, guaranteeing a balanced-enough split every time.

### Why it matters:

- Guarantees **worst-case $O(n)$** time for `select`
- Extremely clever — finds the median of any array in **linear time**
- Used as the pivot selection strategy in a guaranteed-linear `select`

### High-level idea:

1. Divide `A` into groups of 5
2. Find the median of each group (trivial for size 5)
3. Recursively find the median of those medians → use as pivot
4. Recurse on the appropriate partition

$$\Rightarrow T(n) = O(n) \text{ even in the worst case}$$

---

## 🔁 Summary

```
┌────────────────────────────────────────────────────────┐
│              SELECT ALGORITHM OVERVIEW                 │
├──────────────────┬─────────────────────────────────────┤
│ Naive (sort)     │ O(n log n)                          │
│ Quickselect      │ O(n) avg,  O(n²) worst              │
│ MOM Algorithm    │ O(n) guaranteed (worst case)        │
└──────────────────┴─────────────────────────────────────┘
```

---

## 🔗 Related Topics

- [[Quicksort & Partition]]
- [[Median of Medians (MOM)]]
- [[Divide and Conquer]]
- [[Sorting Algorithms]]

---

_Source: Go Classes — goclasses.in | Lecture 19b_