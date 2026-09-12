# 2.4.5 — Counting Sort & Radix Sort

---

## Assumptions

- Keys are **integers**
- Maximum value of any key is $\leq k$

---

## 1️⃣ Counting Sort

> **Idea:** Take each value, push it into a **bucket** at that index, then pop elements from each bucket **left to right (FIFO)** and insert into a new output array.

### Walkthrough Example

```
Input:  [ 3a  5a  2a  3b  1   6   5b  2b ]

                        ↓ pop in FIFO order

Bucket:  [  ]  [1]  [2a,2b]  [3a,3b]  [  ]  [5a,5b]  [6]
index:    0     1      2        3       4       5       6

        ← Total bucket size = max(array) = k

Output: [ 1   2a  2b   3a  3b   5a  5b   6 ]
                                        ↑ stable sort!
```

> [!tip] **Stable Sort** Elements with the same key maintain their **original relative order** in the output. This is crucial for Radix Sort to work correctly.

### Complexity

|Complexity|
|---|---|
|**Time**|$O(n + k)$|
|**Space**|$O(n)$|

> When $k = O(n)$, counting sort runs in $O(n)$ — faster than any comparison-based sort!

---

## 2️⃣ Radix Sort

> **Idea:** Perform counting sort on the **least-significant digit** first, then the next least-significant, and so on.

### Example — Sorting 3-digit numbers

```
Original →  Sort by 1s  →  Sort by 10s  →  Sort by 100s

  329           720            329              329
  457           355            436              355
  657           436            839              436
  839     →     457      →     355       →      457
  436           657            457              657
  720           329            657              720
  355           839            720              839
```

Each column is one pass of counting sort. After 3 passes → fully sorted ✅

### How Many Iterations?

- If numbers have $t$ digits (in base 10): **$d = t$ iterations**
- For $n$ integers each in range ${1, 2, \ldots, n^t}$: $d = \log_{10}(n^t) = t \cdot \log_{10} n$

### Per-Iteration Cost

- Each pass = counting sort = $O(n + k)$
- For integers only: $k = 9$ (digits 0–9), so each pass is $O(n)$

### Total Running Time

$$T = O(n \cdot d) = O!\left(n^t \cdot \log_{10}(n^t)\right) = O(n^t \cdot t \cdot \log_{10} n)$$

$$\boxed{\text{Running time of Radix Sort} = O(n^t \times \log_k n)}$$

### Is $O(nd)$ Good?

> [!question] How good is $O(nd)$? Sorting $n$ integers in **base 10**, each in range ${1, 2, \ldots, n^t}$:
> 
> - Iterations needed: $d = \log_{10} n^t$
> - Each iteration: $O(n)$
> - Total: $O(n \cdot \log_{10} n^t) = O(n^t \cdot \log_{10} n)$

> [!warning] **Critical Requirement — Stability** The inner sort used in each pass of Radix Sort **must be stable**. If it's not stable, numbers may shift to incorrect positions across passes. Counting sort is the standard choice precisely because it's stable.

---

## 📊 Comparison: Counting vs Radix

```
┌────────────────┬──────────────────┬───────────────────────┐
│ Algorithm      │ Time             │ Notes                 │
├────────────────┼──────────────────┼───────────────────────┤
│ Counting Sort  │ O(n + k)         │ Stable. Key = index.  │
│ Radix Sort     │ O(n^t × log_k n) │ Needs stable subroutine│
│ Merge Sort     │ O(n log n)       │ Comparison-based      │
│ Quick Sort     │ O(n log n) avg   │ Not stable            │
└────────────────┴──────────────────┴───────────────────────┘
```

---

## 🧩 Practice Problems

### Problem 1 — Insertion Sort Bug

```c
void InsertionSort(int A[], int n) {
    int i, j, v;
    for (i = 2; i <= n - 1; i++)   // ← BUG: loop ignores last element!
    {
        v = A[i];
        j = i;
        while (A[j - 1] > v && j >= 1)
        {
            A[j] = A[j - 1];
            j--;
        }
        A[j] = v;
    }
}
// Assumes index of array starts from 1
// This means indices go: 1, 2, ..., n-1, n
```

> [!bug] The loop `i <= n-1` **ignores the last element**. It should be `i <= n`.

**Question:** What is the exact number of **key comparisons** performed by insertion sort on input: `12, 13, 15, 18, 17, 16, 14, 10?`

> [!note] Approach Count comparisons element by element. For each `i`, count how many times `A[j-1] > v` is evaluated (including the final false comparison that exits the while loop).

---

### Problem 2 — Quicksort Partition Debug

**Scenario:** After the **first partition step**, the array is:

```
[ 5,  8,  10,  7,  12,  15,  24,  22,  20 ]
```

Which of the following is correct about the pivot?

- (a) The pivot could have been either 12 or 15
- (b) The pivot could have been 15, but could not have been 12
- (c) The pivot could have been 12, but could not have been 15 ✅
- (d) Neither 15 nor 12 could have been the pivot

> [!info] **Answer: (a) — but the note says "there is no way to know"** After partition, the pivot is at its **final sorted position**. Elements to its left are ≤ pivot and to its right are ≥ pivot.
> 
> - 12 is at index 5 (1-indexed): left = `[5,8,10,7]` ✓, right = `[15,24,22,20]` ✓ → **12 could be pivot**
> - 15 is at index 6: left = `[5,8,10,7,12]` ✓, right = `[24,22,20]` ✓ → **15 could also be pivot**
> 
> **Handwritten note:** _"There is no way to know"_ — both 12 and 15 are valid candidates!

---

### Problem 3 — Quicksort on Sorted Array

**Scenario:** Sorted array of $n$ distinct elements. Quicksort always picks the **middle element** as pivot.

What is the tightest upper bound for worst-case performance?

- (a) $O(n)$
- (b) $O(n \log n)$ ✅
- (c) $O(n^2)$
- (d) $O(n^3)$

> [!tip] **Strategy: Always make a recurrence equation for this type of question** Choosing the middle element of a sorted array as pivot always splits perfectly in half: $$T(n) = 2T(n/2) + O(n) \implies T(n) = O(n \log n)$$ This is actually the **best case** for quicksort — perfectly balanced partitions every time.

---

### Problem 4 — Comparison-Based Sorting Correctness

**Question:** Which recurrences are sufficient to prove a comparison-based sorting algorithm works correctly?

|Professor|Recurrence|$T(n)$ Complexity|Valid?|
|---|---|---|---|
|A|$T(n) = 2T(n-1) + 1$|$O(2^n)$|✅ Possible|
|B|$T(n) = 4T(n/5) + 5n \log\log n$|$< O(n \log n)$|❌ Too fast|
|C|$T(n) = 7T(n/6) + n/42$|$O(n^{\log_6 7})$|✅ Possible|
|D|$T(n) = T(n-1) + 1$|$O(n)$|❌ Too fast|

> [!important] **Key Insight** Any comparison-based sorting algorithm **must** take $\Omega(n \log n)$ time in the worst case (information-theoretic lower bound).
> 
> - **B and D** have recurrences that solve to **less than $O(n \log n)$** — this means they _cannot_ be correct comparison-based sorting algorithms!
> - If the time complexity is below $O(n \log n)$, the algorithm hasn't made enough comparisons to determine the correct order.
> 
> _"Here only sorting algo is given — we don't know if it's correct, but based on TC we can conclude which algo is NOT comparison-based."_

---

## 🔗 Related Topics

- [[Counting Sort]]
- [[Quicksort & Partition]]
- [[Insertion Sort]]
- [[Comparison-Based Sorting Lower Bound]]
- [[Divide and Conquer]]
- [[2.3.4 - Select Algorithm]]

---

_Source: Go Classes — goclasses.in | Lecture 19b_