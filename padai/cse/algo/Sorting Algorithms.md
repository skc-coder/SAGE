## 📌 Quick Reference

|Algorithm|Best|Average|Worst|Space|Stable|In-place|
|---|---|---|---|---|---|---|
|Bubble Sort|`Ω(n)`|`Θ(n²)`|`O(n²)`|`O(1)`|✅|✅|
|Insertion Sort|`Ω(n)`|`Θ(n²)`|`O(n²)`|`O(1)`|✅|✅|
|Selection Sort|`Ω(n²)`|`Θ(n²)`|`O(n²)`|`O(1)`|❌|✅|
|Merge Sort|`Ω(n log n)`|`Θ(n log n)`|`O(n log n)`|`O(n)`|✅|❌|
|Quick Sort|`Ω(n log n)`|`Θ(n log n)`|`O(n²)`|`O(log n)`|❌|✅|
|Heap Sort|`Ω(n log n)`|`Θ(n log n)`|`O(n log n)`|`O(1)`|❌|✅|
|Counting Sort|`Ω(n+k)`|`Θ(n+k)`|`O(n+k)`|`O(k)`|✅|❌|
|Radix Sort|`Ω(nk)`|`Θ(nk)`|`O(nk)`|`O(n+k)`|✅|❌|

> [!note] Definitions
> 
> - **Stable:** Equal elements maintain their original relative order
> - **In-place:** Uses only `O(1)` extra memory (ignoring recursion stack)
> - `k` = range of values (Counting), number of digits (Radix)

---

## 1 — Bubble Sort

### Idea

Repeatedly **bubble the largest unsorted element to its correct position** by swapping adjacent elements that are out of order. After each pass, one more element is settled at the end.

### Dry Run — `[5, 3, 8, 1]`

```
Pass 1:  [5,3,8,1] → [3,5,8,1] → [3,5,8,1] → [3,5,1,8]   ← 8 is placed ✓
Pass 2:  [3,5,1,8] → [3,5,1,8] → [3,1,5,8]               ← 5 is placed ✓
Pass 3:  [3,1,5,8] → [1,3,5,8]                            ← 3 is placed ✓
Result:  [1, 3, 5, 8]
```

### Algorithm

```
for i = 0 to n-2:
    swapped = false
    for j = 0 to n-2-i:
        if A[j] > A[j+1]:
            swap(A[j], A[j+1])
            swapped = true
    if not swapped: break        ← early exit if already sorted
```

### Analysis

|Case|Condition|Comparisons|
|---|---|---|
|Best|Already sorted (with early exit)|`n − 1` → `Ω(n)`|
|Worst|Reverse sorted|`n(n−1)/2` → `O(n²)`|
|Average|Random input|`Θ(n²)`|

> [!tip] Key Points
> 
> - Without the `swapped` flag, best case is also `O(n²)`
> - Stable because we only swap when strictly greater (not equal)
> - Rarely used in practice — Insertion Sort is better in all cases

---

## 2 — Insertion Sort

### Idea

Build the sorted array **one element at a time**. Pick the next unsorted element and **insert it into its correct position** among the already-sorted elements by shifting larger elements right.

Think of sorting a hand of playing cards — you pick up one card at a time and slot it in.

### Dry Run — `[5, 3, 8, 1]`

```
Start:    [5 | 3, 8, 1]     sorted part = [5]
i=1: key=3  → shift 5 right → [3, 5 | 8, 1]
i=2: key=8  → 8 > 5, no shift → [3, 5, 8 | 1]
i=3: key=1  → shift 8,5,3   → [1, 3, 5, 8]
```

### Algorithm

```
for i = 1 to n-1:
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]          ← shift right
        j = j - 1
    A[j+1] = key               ← insert
```

### Analysis

|Case|Condition|Comparisons|Shifts|
|---|---|---|---|
|Best|Already sorted|`n − 1`|`0`|
|Worst|Reverse sorted|`n(n−1)/2`|`n(n−1)/2`|
|Average|Random|`Θ(n²)`|`Θ(n²)`|

> [!success] When to use Insertion Sort
> 
> - Nearly sorted data — approaches `O(n)`
> - Small arrays (n ≤ 20) — low constant factor
> - **Adaptive:** Performance improves with pre-sortedness
> - Used as a base case inside Merge Sort / Tim Sort in practice

> [!tip] Insertion Sort vs Bubble Sort Both are `O(n²)` but Insertion Sort does **fewer writes** (shifts, not swaps). One shift = 1 assignment vs one swap = 3 assignments. Insertion Sort is faster in practice.

---

## 3 — Selection Sort

### Idea

Divide the array into a sorted left part and unsorted right part. In each pass, **select the minimum element** from the unsorted part and place it at the boundary.

### Dry Run — `[5, 3, 8, 1]`

```
Pass 1: min of [5,3,8,1] = 1  → swap with index 0 → [1 | 3, 8, 5]
Pass 2: min of [3,8,5]   = 3  → already at index 1 → [1, 3 | 8, 5]
Pass 3: min of [8,5]     = 5  → swap with index 2 → [1, 3, 5 | 8]
Result: [1, 3, 5, 8]
```

### Algorithm

```
for i = 0 to n-2:
    min_idx = i
    for j = i+1 to n-1:
        if A[j] < A[min_idx]:
            min_idx = j
    swap(A[i], A[min_idx])
```

### Analysis

|Case|Comparisons|Swaps|
|---|---|---|
|All cases|`n(n−1)/2`|`O(n)`|

> [!warning] Why always `Θ(n²)`? The inner loop always scans the entire unsorted part — there's no early exit. Even if the array is sorted, Selection Sort still does all comparisons. That's why best = worst = `Θ(n²)`.

> [!tip] Selection Sort's one advantage It makes at most **`n − 1` swaps** — useful when writes are expensive (e.g., flash memory). Insertion/Bubble Sort can make `O(n²)` writes.

> [!warning] Not Stable Swapping non-adjacent elements can disturb the relative order of equal elements. Example: `[3a, 3b, 1]` → after pass 1: `[1, 3b, 3a]` — order of the two 3s is reversed.

---

## 4 — Merge Sort

### Idea

Classic **Divide and Conquer**. Split the array in half recursively until you reach single elements (trivially sorted), then **merge** sorted halves back together.

```
Divide:  [38, 27, 43, 3]
         /              \
    [38, 27]          [43, 3]
    /      \          /     \
  [38]    [27]     [43]    [3]

Conquer (merge):
  [27, 38]          [3, 43]
         \          /
          [3, 27, 38, 43]
```

### Merge Procedure

The key operation — merges two sorted halves `A[l..m]` and `A[m+1..r]` into a sorted array.

```
merge(A, l, m, r):
    create temp arrays L = A[l..m],  R = A[m+1..r]
    i = 0, j = 0, k = l
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:          ← ≤ ensures stability
            A[k++] = L[i++]
        else:
            A[k++] = R[j++]
    copy remaining elements of L or R
```

### Algorithm

```
mergeSort(A, l, r):
    if l < r:
        m = (l + r) / 2
        mergeSort(A, l, m)
        mergeSort(A, m+1, r)
        merge(A, l, m, r)
```

### Recurrence

$$T(n) = 2T\left(\frac{n}{2}\right) + \Theta(n)$$

By Master Theorem (Case 2): $T(n) = \Theta(n \log n)$

### Analysis

|Case|Time|Why|
|---|---|---|
|Best|`Ω(n log n)`|Always divides equally, always merges|
|Average|`Θ(n log n)`|Same structure regardless of input|
|Worst|`O(n log n)`|No bad pivot, always balanced|

> [!success] Merge Sort Strengths
> 
> - Guaranteed `O(n log n)` — no worst-case blow-up like Quick Sort
> - **Stable** — preserves relative order of equal elements
> - Best for **linked lists** (no random access needed for merge)
> - Best for **external sorting** (data too large for RAM)

> [!warning] Merge Sort Weakness Requires `O(n)` extra space for the temporary arrays during merge. Not in-place.

### Counting Inversions

> [!abstract] Application Merge Sort can count **inversions** (pairs where `i < j` but `A[i] > A[j]`) in `O(n log n)` time. When merging, every time we pick from the right half over the left half, we count `mid − left_pointer` inversions.

---

## 5 — Quick Sort

### Idea

**Divide and Conquer** using a pivot. Partition the array so all elements smaller than the pivot are to its left and all larger are to its right. The pivot is now in its **final sorted position**. Recursively sort the two halves.

### Partition (Lomuto scheme)

```
partition(A, l, r):
    pivot = A[r]          ← choose last element as pivot
    i = l - 1
    for j = l to r-1:
        if A[j] <= pivot:
            i++
            swap(A[i], A[j])
    swap(A[i+1], A[r])    ← place pivot in final position
    return i + 1
```

### Dry Run — `[3, 6, 8, 10, 1, 2, 1]`, pivot = `1` (last)

```
After partition: [1, 1 | pivot_pos | 3, 6, 8, 10, 2]
                  ↑ all ≤ pivot       ↑ all > pivot
Recurse on each side
```

### Algorithm

```
quickSort(A, l, r):
    if l < r:
        p = partition(A, l, r)
        quickSort(A, l, p-1)
        quickSort(A, p+1, r)
```

### Recurrence & Analysis

|Case|Condition|Recurrence|Time|
|---|---|---|---|
|Best|Pivot always splits evenly|`T(n) = 2T(n/2) + Θ(n)`|`Θ(n log n)`|
|Average|Random input|`T(n) = T(n/9) + T(9n/10) + Θ(n)` style|`Θ(n log n)`|
|Worst|Pivot always min or max|`T(n) = T(0) + T(n-1) + Θ(n)`|`O(n²)`|

> [!warning] When does worst case happen?
> 
> - Array already sorted (ascending or descending) with first/last element as pivot
> - All elements are equal
> - Fix: **randomized pivot** — pick pivot randomly → worst case becomes astronomically unlikely

> [!tip] Why Quick Sort is preferred in practice
> 
> - In-place — no extra memory beyond `O(log n)` stack
> - Excellent cache performance (accesses contiguous memory)
> - Average case constant factor is small
> - `O(n log n)` average despite `O(n²)` worst case with randomized pivot

> [!abstract] Average Case Analysis With randomized pivot, expected number of comparisons = `2n ln n ≈ 1.39 n log₂ n`. This is only ~39% more than the theoretical minimum — remarkably efficient.

---

## 6 — Heap Sort

### Prerequisite — Max Heap

A **Max Heap** is a complete binary tree where every parent is ≥ its children. The root always holds the maximum element.

```
        9
       / \
      5   8
     / \ / \
    2  4 6  7
```

Stored as array: `[9, 5, 8, 2, 4, 6, 7]`

- Parent of index `i`: `⌊(i−1)/2⌋`
- Left child of `i`: `2i + 1`
- Right child of `i`: `2i + 2`

### Heapify (sift-down)

Fix a single violation at index `i` by sifting it down.

```
heapify(A, n, i):
    largest = i
    left  = 2i + 1
    right = 2i + 2
    if left < n and A[left] > A[largest]:   largest = left
    if right < n and A[right] > A[largest]: largest = right
    if largest ≠ i:
        swap(A[i], A[largest])
        heapify(A, n, largest)       ← recurse down
```

Cost of one `heapify` call: `O(log n)` (height of tree)

### Build Max Heap

```
buildHeap(A, n):
    for i = n/2 - 1 downto 0:   ← start from last non-leaf
        heapify(A, n, i)
```

> [!success] Build Heap is `O(n)`, not `O(n log n)`! Intuition: most nodes are near the bottom and need very little sifting. The exact sum telescopes to `O(n)`. This is a commonly tested GATE fact.

### Heap Sort Algorithm

```
heapSort(A, n):
    buildHeap(A, n)                       ← O(n)
    for i = n-1 downto 1:
        swap(A[0], A[i])                  ← move max to end
        heapify(A, i, 0)                  ← restore heap on reduced size
```

### Dry Run — `[4, 10, 3, 5, 1]`

```
After buildHeap:  [10, 5, 3, 4, 1]

i=4: swap A[0]↔A[4] → [1,5,3,4,|10]  heapify → [5,4,3,1,|10]
i=3: swap A[0]↔A[3] → [1,4,3,|5,10]  heapify → [4,1,3,|5,10]
i=2: swap A[0]↔A[2] → [3,1,|4,5,10]  heapify → [3,1,|4,5,10]
i=1: swap A[0]↔A[1] → [1,|3,4,5,10]  heapify → [1,|3,4,5,10]

Result: [1, 3, 4, 5, 10] ✓
```

### Analysis

|Phase|Cost|
|---|---|
|Build heap|`O(n)`|
|n extractions × heapify|`n × O(log n)` = `O(n log n)`|
|**Total**|**`O(n log n)`**|

> [!success] Heap Sort Strengths
> 
> - Guaranteed `O(n log n)` in all cases — no worst-case blow-up
> - In-place — `O(1)` extra space
> - Combines the space efficiency of Quick Sort with the guaranteed performance of Merge Sort

> [!warning] Heap Sort Weakness **Not stable** — swapping the root with the last element can disrupt relative order. Poor cache performance — heap operations jump around memory (not cache-friendly like Quick Sort).

---

## 7 — Decision Tree Lower Bound

> [!abstract] Theorem Any comparison-based sorting algorithm requires at least `Ω(n log n)` comparisons in the worst case.

### Proof Idea

- A decision tree models every possible sequence of comparisons an algorithm can make
- Each **leaf** represents one possible sorted output (a permutation)
- There are `n!` possible permutations → tree must have ≥ `n!` leaves
- A binary tree of height `h` has at most `2^h` leaves
- So: `2^h ≥ n!` → `h ≥ log₂(n!)`
- By Stirling's approximation: `log₂(n!) = Θ(n log n)`

$$\therefore \text{ any comparison sort needs } \Omega(n \log n) \text{ comparisons}$$

> [!success] Consequence Merge Sort, Heap Sort, and Quick Sort (average) are all **asymptotically optimal** among comparison-based sorting algorithms.

> [!warning] Why Counting and Radix Sort beat this bound They are **not comparison-based** — they use the actual values of elements (arithmetic, not just comparisons), so the decision tree argument doesn't apply.

---

## 8 — Counting Sort

### Idea

For integers in range `[0, k]`. Count how many times each value appears, then use those counts to place each element directly into its correct output position. **No comparisons needed.**

### Algorithm

```
countingSort(A, n, k):
    C[0..k] = 0                          ← count array

    for i = 0 to n-1:  C[A[i]]++        ← count occurrences

    for i = 1 to k:    C[i] += C[i-1]   ← cumulative (prefix sum)
                                          ← C[v] = last position of value v

    for i = n-1 downto 0:               ← iterate BACKWARDS for stability
        B[C[A[i]] - 1] = A[i]
        C[A[i]]--

    return B
```

### Dry Run — `A = [1, 3, 2, 3, 1]`, k = 3

```
Count:       C = [0, 2, 1, 2]       (index 0: zero 0s, index 1: two 1s, ...)
Cumulative:  C = [0, 2, 3, 5]
Place (backwards):
  A[4]=1 → B[C[1]-1] = B[1] = 1, C[1]=1
  A[3]=3 → B[C[3]-1] = B[4] = 3, C[3]=4
  A[2]=2 → B[C[2]-1] = B[2] = 2, C[2]=2
  A[1]=3 → B[C[3]-1] = B[3] = 3, C[3]=3
  A[0]=1 → B[C[1]-1] = B[0] = 1, C[1]=0
Result B = [1, 1, 2, 3, 3] ✓
```

### Analysis

- **Time:** `O(n + k)` — two passes over `A` (size `n`) + one pass over `C` (size `k`)
- **Space:** `O(n + k)` — output array `B` (size `n`) + count array `C` (size `k`)
- **Stable:** Yes — the backwards iteration preserves relative order of equal elements

> [!warning] When NOT to use Counting Sort When `k >> n` (range much larger than count). E.g., sorting 10 numbers in range `[0, 10⁶]` → wastes memory. Use only when `k = O(n)`.

---

## 9 — Radix Sort

### Idea

Sort integers **digit by digit**, from the **Least Significant Digit (LSD) to the Most Significant Digit (MSD)**. Use a stable sort (Counting Sort) at each digit level.

> [!idea] Why LSD first? If we sort MSD first, subsequent digit sorts would corrupt earlier results. LSD first: each pass refines the previous ordering. Stability ensures that a later pass never disturbs the correct relative order already established.

### Algorithm

```
radixSort(A, n):
    d = number of digits in max element
    for i = 1 to d:
        stableSort(A) by digit i        ← use Counting Sort on digit i
```

### Dry Run — `[170, 45, 75, 90, 802, 24, 2, 66]`

```
Sort by units digit (d=1):
  [170, 90, 802, 2, 24, 45, 75, 66]

Sort by tens digit (d=2):
  [802, 2, 24, 45, 66, 170, 75, 90]

Sort by hundreds digit (d=3):
  [2, 24, 45, 66, 75, 90, 170, 802]  ✓
```

### Analysis

- **Time:** `O(d × (n + k))` where `d` = digits, `k` = base (usually 10)
- If `d` is constant and `k = O(n)` → `O(n)`
- **Space:** `O(n + k)`
- **Stable:** Yes (because each digit-pass uses a stable sort)

> [!tip] Radix Sort vs Counting Sort Radix Sort extends Counting Sort to handle large numbers by sorting digit by digit. Counting Sort sorts in one pass but needs range `k` to be small. Radix Sort can handle 32-bit integers in 4 passes with base 256 → still `O(n)`.

---

## 10 — Choosing the Right Sorting Algorithm

```
Is data nearly sorted?
  └─ YES → Insertion Sort (approaches O(n))
  └─ NO ↓

Are values integers in a small range [0, k]?
  └─ YES → Counting Sort or Radix Sort (sub-linear possible)
  └─ NO ↓

Is extra memory O(n) acceptable?
  └─ YES → Merge Sort (guaranteed O(n log n), stable)
  └─ NO ↓

Is guaranteed O(n log n) needed?
  └─ YES → Heap Sort (in-place, O(n log n) worst case)
  └─ NO  → Quick Sort (fastest in practice, randomized pivot)
```

---

## 11 — Common GATE Questions

> [!warning] Frequently Tested
> 
> 1. Which sorting algorithms are stable? → **Bubble, Insertion, Merge, Counting, Radix**
> 2. Which sorting algorithms are in-place? → **Bubble, Insertion, Selection, Quick, Heap**
> 3. Best sorting algorithm for linked lists → **Merge Sort** (no random access needed)
> 4. Best case of Bubble Sort **with** early exit flag → `O(n)`
> 5. Build Heap complexity → `O(n)` (not `O(n log n)`)
> 6. Lower bound for comparison sorting → `Ω(n log n)` (decision tree proof)
> 7. Which algorithm has best case ≠ worst case but both are `O(n²)`? → **Insertion Sort** (best `Ω(n)`)
> 8. Selection sort is NOT stable — provide a counterexample → `[3a, 3b, 1]`

---

## 🔗 Related Notes

- [[Max Min Tournament Method]]
- [[Divide and Conquer - Part 1]]
- [[Quick Sort - Detailed Analysis]]
- [[Heap and Heap Sort]]
- [[Decision Tree and Lower Bounds]]
- [[GATE PYQs - Algorithms]]

---

_Lectures: 20a · 20b · 20c · 20d · 20e · 20f_