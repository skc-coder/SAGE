## 1 — Finding Maximum

### Naive / Linear Scan

```
max = A[0]
for i = 1 to n-1:
    if A[i] > max:
        max = A[i]
```

- **Comparisons:** `n − 1`
- **Time complexity:** `Θ(n)`
- This is **optimal** — you must look at every element at least once.

---

## 2 — Finding 2nd Maximum

### Naïve approach (two separate passes)

- Pass 1: Find max → `n − 1` comparisons
- Pass 2: Find max of remaining → `n − 2` comparisons
- **Total:** `2n − 3` comparisons

### Smarter single-pass approach

Track both `max` and `second_max` simultaneously.

```
max = -∞,  second = -∞
for each element x in A:
    if x > max:
        second = max
        max = x
    else if x > second:
        second = x
```

- **Comparisons:** `2(n − 1)` in the worst case
- Still `Θ(n)`, but more comparisons than necessary

### 🏆 Optimal: Tournament Method for 2nd Max

> [!idea] Key Insight The 2nd maximum **must have lost directly to the maximum** at some round of the tournament. So we only need to re-examine the elements that lost to the overall winner.

**Algorithm:**

1. Run a full tournament (like a knock-out bracket) to find `max` → `n − 1` comparisons
2. The winner (`max`) defeated exactly `⌈log₂ n⌉` opponents
3. Find the max among those `⌈log₂ n⌉` losers → `⌈log₂ n⌉ − 1` comparisons

**Total comparisons:**

$$ (n - 1) + (\lceil \log_2 n \rceil - 1) = n + \lceil \log_2 n \rceil - 2 $$

> [!success] This is the **proven lower bound** for finding both max and 2nd max simultaneously.

---

## 3 — Tournament Method: Finding Max & Min

### Problem

Find both maximum and minimum of an array of `n` elements with the **fewest comparisons possible**.

---

### Approach 1 — Independent Linear Scans

- Find max: `n − 1` comparisons
- Find min: `n − 1` comparisons
- **Total: `2n − 2` comparisons**

---

### Approach 2 — Single Pass (Track Both)

```
if A[0] > A[1]:
    max = A[0],  min = A[1]
else:
    max = A[1],  min = A[0]

for i = 2 to n-1 (step 1):
    if A[i] > max: max = A[i]       // 1 comparison
    else if A[i] < min: min = A[i]  // 1 comparison (only if first fails)
```

- **Worst case:** `2(n − 2)` comparisons for the loop + 1 initial = `2n − 3`
- Not optimal

---

### Approach 3 — 🏆 Tournament / Pairwise Comparison (Optimal)

> [!idea] Core Idea Compare elements **in pairs first**. The larger of each pair is a candidate for max; the smaller is a candidate for min. This saves comparisons by doing two jobs with one comparison.

**Algorithm (for even `n`):**

```
Step 1: Compare pairs (A[0],A[1]), (A[2],A[3]), ...
        → Put larger in set MAX_CANDIDATES
        → Put smaller in set MIN_CANDIDATES
        Comparisons: n/2

Step 2: Find max of MAX_CANDIDATES  → n/2 − 1 comparisons
Step 3: Find min of MIN_CANDIDATES  → n/2 − 1 comparisons

Total: n/2 + (n/2 − 1) + (n/2 − 1) = 3n/2 − 2
```

**For odd `n`:**  
Set both `max = min = A[0]`, then process remaining `n−1` elements in pairs. → Total: `⌈3n/2⌉ − 2` comparisons

> [!success] Comparison Count (Pairwise Tournament) $$\left\lfloor \frac{3n}{2} \right\rfloor - 2$$ This is the **proven lower bound** — no algorithm can do better.

---

### Comparison Summary Table

|Method|Comparisons|Optimal?|
|---|---|---|
|Two independent scans|`2n − 2`|✗|
|Single-pass (track both)|`2n − 3`|✗|
|Pairwise tournament|`⌊3n/2⌋ − 2`|✓|

---

## 4 — Tournament Method: Full Binary Tree View

> [!abstract] Intuition Think of the array elements as leaves of a **complete binary tree**. Each internal node stores the winner (max) of its two children. The root is the overall maximum.

```
         [max]
        /     \
    [5]         [9←max]
   /   \        /     \
 [5]  [3]    [9]     [7]
  ↑    ↑      ↑       ↑
  A[0] A[1]  A[2]    A[3]
```

- Total nodes at leaf level: `n`
- Total internal comparisons (edges): `n − 1`
- Height of tree: `⌈log₂ n⌉`
- Elements the winner beat: exactly `⌈log₂ n⌉` (one per level)

---

## 5 — Lower Bound Arguments

### For finding Maximum

- Every element except the max must **lose at least once**
- So at least `n − 1` comparisons are needed
- Linear scan achieves this → **optimal**

### For finding Max & Min simultaneously

Using an adversary argument / information-theoretic argument:

- We need `n − 1` "losses" to identify min
- We need `n − 1` "wins" to identify max
- But each comparison generates **one win and one loss**
- Naively: `2(n−1)` comparisons needed
- With pairwise trick: we generate a win AND a loss from one comparison → `⌊3n/2⌋ − 2` is achievable and optimal

### For finding 2nd Maximum

Lower bound: `n + ⌈log₂ n⌉ − 2`

> [!note] Why log n term? The 2nd max must have lost to max. Max could have beaten any of the `n−1` other elements, so without additional structure we don't know which one is 2nd. The tournament ensures max beats only `⌈log₂ n⌉` elements, making the follow-up search efficient.

---

## 6 — GATE PYQ Notes (13b, 13c)

> [!warning] Frequently Tested Patterns
> 
> - "What is the minimum number of comparisons to find max and min of n elements?" → `⌊3n/2⌋ − 2`
> - "Find 2nd maximum with minimum comparisons" → `n + ⌈log₂ n⌉ − 2`
> - Questions may give a specific `n` (e.g., n=8, n=16) and ask for the count — just substitute

### Example — n = 8

|Problem|Formula|Answer|
|---|---|---|
|Find max|`n − 1`|7|
|Find max & min (pairwise)|`⌊3×8/2⌋ − 2`|10|
|Find 2nd max (tournament)|`8 + ⌈log₂ 8⌉ − 2 = 8 + 3 − 2`|9|

### Example — n = 16 (common GATE value)

|Problem|Answer|
|---|---|
|Find max|15|
|Find max & min|22|
|Find 2nd max|19|

---

## 7 — TIFR Question Note

> [!tip] TIFR Angle TIFR problems often ask to **prove** the lower bound, not just state it. Be prepared to:
> 
> 1. Define the adversary strategy
> 2. Show that any algorithm can be forced to use ≥ `⌊3n/2⌋ − 2` comparisons
> 3. Construct the pairwise algorithm to show the bound is tight

---

## 8 — Quick Recall

```
Max only           →  n − 1              comparisons  (optimal)
Max + Min naive    →  2n − 3             comparisons
Max + Min optimal  →  ⌊3n/2⌋ − 2        comparisons  (pairwise tournament) ✓
2nd Max optimal    →  n + ⌈log₂n⌉ − 2   comparisons  (full tournament) ✓
```

---

## 🔗 Related Notes

- [[Divide and Conquer - Part 1]]
- [[Merge Sort]]
- [[Asymptotic Analysis]]
- [[GATE PYQs - Algorithms]]

---

_Lectures: 12a · 12b · 12c · 12d · 13a · 13b · 13c_