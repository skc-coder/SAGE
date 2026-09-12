# Distribution Techniques

**Topic:** Discrete Mathematics > Combinatorics > Distributions
**Source:** Personal notes — Combinatorics
**Tags:** #combinatorics #distributions #star-and-bars #gate-cse
**Links:** [[moc combinatorics]] | [[Counting Rules]] | [[Combinations]]

---

> [!info] Overview
> Every "distribute objects into boxes" problem is classified along two independent axes: whether the **objects** are distinguishable or identical, and whether the **boxes** are distinguishable or identical. This gives four fundamental templates — DODB, IODB, DOIB, IOIB — each with a distinct counting method.

| | Distinguishable boxes | Identical boxes |
| :--- | :--- | :--- |
| **Distinguishable objects** | DODB | DOIB |
| **Identical objects** | IODB (star-and-bars) | IOIB (integer partitions) |

---

## 1. DODB — Distinguishable Objects, Distinguishable Boxes

$$
\frac{n!}{n_1!\, n_2!\, \dots\, n_k!}
$$

where $n_1 + n_2 + \dots + n_k = n$ are the fixed sizes of each (distinguishable) box.

> [!note] Handling edge cases
> - If the box sizes don't sum to $n$, add a "trash box" to absorb the leftover objects, sized so all boxes sum to $n$.
> - If there is **no** size constraint on the boxes at all, each object independently picks any of $m$ boxes: $m^n$.

> [!example] Distributing card hands
> **Question:** Distribute hands of 5 cards each to 4 players from a standard 52-card deck.
>
> **Method 1 — sequential selection:**
> $$
> \binom{52}{5}\binom{47}{5}\binom{42}{5}\binom{37}{5}
> $$
>
> **Method 2 — permute-then-divide:** Permute all 52 cards in a row; the first 5 go to player A, next 5 to B, and so on. Since the order **within** each player's hand doesn't matter, divide by $5!$ for each of the 4 hands, and the unused 32 cards' order doesn't matter either, so divide by $32!$:
>
> $$
> \frac{52!}{5!\,5!\,5!\,5!\,32!}
> $$

### 1.1 "At Least" Case (No Trash Box)

> [!example] 8 distinct objects, 3 boys, everyone gets at least 2
> **Approach:** Since exact box sizes aren't fixed, enumerate the valid size **patterns** that satisfy "at least 2 each" and sum over patterns:
>
> **Case $(2,2,4)$:** choose which boy gets 4 objects, then distribute.
> $$
> \binom{3}{1} \times \binom{8}{4} \times \binom{4}{2} \times \binom{2}{2}
> $$
>
> **Case $(2,3,3)$:** choose which boy gets 2 objects, then distribute.
> $$
> \binom{3}{1} \times \binom{8}{2} \times \binom{6}{3} \times \binom{3}{3}
> $$
>
> **Total:** sum of the two cases.

> [!warning] Common mistake
> Writing $\binom{8}{2}\binom{6}{2}\binom{4}{2} \times 3^2$ for the $(2,3,3)$-type distribution is **wrong** — it overcounts, because it fails to correctly account for which boxes receive the larger shares and double-counts arrangements that are structurally identical once box sizes are equal. Always identify the box-size pattern explicitly and choose which distinguishable box gets which size **before** distributing objects.

### 1.2 Box Sizes Permutable Among Boxes

> [!example] 15 distinguishable objects, 5 boxes, sizes $\{1,2,3,4,5\}$ (not pre-assigned to specific boxes)
> **Approach:** This looks like it should be IODB, but since the *objects* are distinguishable, it is still DODB — the size labels $1,2,3,4,5$ can be permuted among the 5 boxes in $5!$ ways, and for each fixed assignment of sizes to boxes, the standard DODB formula applies. First permute the size assignment across boxes, then apply the DODB selection.

---

## 2. IODB — Identical Objects, Distinguishable Boxes (Star-and-Bars)

$$
\binom{n+r-1}{r} = \binom{n+r-1}{n-1}
$$

where $r$ = number of identical objects (stars), $n$ = number of distinguishable boxes, and $n-1$ = number of dividers (bars) needed to separate the boxes.

### 2.1 Three Equivalent Derivations

1. **Assign positions to bars** (box boundaries) among the $r+n-1$ total slots: $\binom{r+n-1}{n-1}$
2. **Assign positions to stars** (objects) among the $r+n-1$ total slots: $\binom{r+n-1}{r}$
3. **Division rule:** permute all $(n-1+r)$ symbols (stars and bars) as if distinct — $(n-1+r)!$ — then divide by $r!$ (since the stars are identical to each other) and $(n-1)!$ (since the bars are identical to each other).

### 2.2 IODB Template — Six Equivalent Problem Forms

All of the following reduce to the same formula $\binom{n+r-1}{r}$:

| # | Problem form | Description |
| :--- | :--- | :--- |
| 1 | Star-and-bars | $r$ stars, $n$ boxes, $n-1$ bars |
| 2 | IODB | $r$ identical objects into $n$ distinct boxes |
| 3 | CWR | $r$-combinations from $n$ elements, with repetition |
| 4 | Multiset | Size-$r$ multisets from an $n$-element set |
| 5 | Integer solutions | Non-negative integer solutions to $x_1+x_2+\dots+x_n = r$ |
| 6 | Non-decreasing sequence | Sequences $1 \le a_1 \le a_2 \le \dots \le a_r \le n$ |

### 2.3 Variable Restrictions in Integer-Solution Problems

| Restriction | Substitution / Technique |
| :--- | :--- |
| $x_i > c$ | Substitute $x_i' = x_i - c - 1$; reduce the target sum by $c+1$ |
| $x_i \ge c$ | Reduce the target sum by $c$ (substitute $x_i' = x_i - c$) |
| $\sum x_i \le n$ | Introduce a slack variable $x_{r+1} \ge 0$ and solve $\sum x_i = n$ |
| Upper bound on $x_i$ | Use the complement rule, or handle case-by-case if the bound is small (large bounds may require inclusion-exclusion — see [[Inclusion-Exclusion Principle#12. Distribution with Upper-Bound Constraints (Stars and Bars + IEP)]]) |

> [!example] Strict inequality
> $x_1+x_2+x_3 < 11$, non-negative integers → introduce slack variable $x_4$ and solve $x_1+x_2+x_3+x_4=11$.

> [!example] Positivity with an upper bound
> $x_1+x_2+x_3+x_4+x_5=20$, all variables positive, with $x_3 \le 3$ → resolve via the complement rule or case-by-case enumeration on $x_3 \in \{1,2,3\}$.

### 2.4 Non-Decreasing Digit Sequences

| Digit pool | Length | Count |
| :--- | :--- | :--- |
| $\{1,\dots,9\}$ | $n$ | $\dbinom{n+8}{8}$ |
| $\{0,\dots,9\}$ | $n$ | $\dbinom{n+9}{9} - 1$ (subtract the all-zeros sequence) |

> [!warning] Not every ordering variant is IODB
> - **Strictly increasing / strictly decreasing** sequences are **not** IODB problems — they reduce to a plain combination count (each valid strictly-monotonic sequence corresponds to exactly one subset of the digit pool).
> - When counting **numbers** rather than raw sequences, the leading digit typically cannot be $0$ — this constraint matters for non-decreasing numbers (leftmost digit restricted) and for non-increasing numbers (only the leftmost position needs the nonzero constraint checked).

### 2.5 Integer Composition (Ordered Summation)

A **composition** of a positive integer $n$ is a way of writing $n$ as an ordered sum of positive integers.

**Approach — case by case on number of parts $k$:** For a composition into exactly $k$ parts, $T_1+T_2+\dots+T_k=n$ with each $T_i \ge 1$. Substituting $T_i' = T_i - 1$ reduces this to $\sum T_i' = n-k$ over non-negative integers, an IODB problem:

$$
\binom{(n-k)+k-1}{k-1} = \binom{n-1}{k-1}
$$

**Total compositions of $n$**, summing over all valid part-counts $k=1$ to $n$:

$$
\sum_{k=1}^{n} \binom{n-1}{k-1} = \sum_{j=0}^{n-1}\binom{n-1}{j} = 2^{n-1}
$$

$$
\boxed{\text{Number of compositions of } n = 2^{n-1}}
$$

> [!note] Proof sketch
> $n$ can be written as a composition into 1 part, 2 parts, ..., or $n$ parts. By the sum rule, summing the count for each part-count $k$ gives the total. The resulting sum $\sum_{k=1}^{n}\binom{n-1}{k-1}$ is exactly the binomial expansion of $(1+1)^{n-1} = 2^{n-1}$ (see [[Binomial Theorem and Combinatorial Identities]]).

---

## 3. DOIB — Distinguishable Objects, Identical Boxes (Set Partitions)

When boxes are identical, distributing distinguishable objects into them is equivalent to partitioning the object set into unlabeled non-empty groups (equivalence classes).

### 3.1 Equal Box Sizes — Division Rule Applies

When room/box sizes are **distinct** from each other, there is no overcounting — simply select objects into each box according to its size requirement (standard DODB-style product of combinations). But when **two or more boxes share the same size**, those boxes become interchangeable, and the division rule must be applied to correct for overcounting.

> [!example] 9 friends into 4 groups of sizes 2, 2, 2, 3
> **Approach:** Select the group members via combinations as usual, then divide by $3!$ to account for the fact that the three size-2 groups are indistinguishable from one another (permuting which size-2 group is "first," "second," "third" produces the same partition).
>
> $$
> \frac{\binom{9}{2}\binom{7}{2}\binom{5}{2}\binom{3}{3}}{3!}
> $$

> [!example] 12 friends into 5 groups of sizes 2, 2, 2, 3, 3
> **Approach:** Same idea — divide by $3!$ for the three interchangeable size-2 groups, and by $2!$ for the two interchangeable size-3 groups.
>
> $$
> \frac{\binom{12}{2}\binom{10}{2}\binom{8}{2}\binom{6}{3}\binom{3}{3}}{3! \times 2!}
> $$

### 3.2 No Size Requirement — Case by Case on Number of Groups Used

When the group-size requirement is removed entirely, split into cases based on **how many groups (rooms) are actually used**, since each case has a different overcounting structure.

> [!example] 3 friends, partition into any number of non-empty groups
> - **1 room used:** $\{abc\}$ together → $1$ way
> - **2 rooms used:** split sizes $(2,1)$; choose which 2 of the 3 are together: $\binom{3}{2} \times \binom{1}{1} = 3$ ways (the $(1,2)$ split is the same partition as $(2,1)$, so no double counting here since we're directly choosing the pair)
> - **3 rooms used:** each friend alone → $1$ way
>
> $$
> \text{Total} = 1 + 3 + 1 = 5
> $$

> [!example] 4 friends, partition into any number of non-empty groups
> This is the 4th **Bell number**, $B_4 = \sum_{k=1}^{4} S(4,k)$, where $S(n,k)$ denotes the **Stirling number of the second kind** (the number of ways to partition an $n$-element set into exactly $k$ non-empty unlabeled groups).
>
> **Case $k=1$ (1 part):** all together.
> $$
> S(4,1) = 1 \quad \{abcd\}
> $$
>
> **Case $k=2$ (2 parts):** splits as $(1,3)$ or $(2,2)$.
> $$
> S(4,2) = \binom{4}{1} + \frac{\binom{4}{2}}{2!} = 4 + 3 = 7
> $$
>
> **Case $k=3$ (3 parts):** split as $(1,1,2)$.
> $$
> S(4,3) = \binom{4}{2} = 6
> $$
>
> **Case $k=4$ (4 parts):** all separate.
> $$
> S(4,4) = 1 \quad \{a\},\{b\},\{c\},\{d\}
> $$
>
> $$
> B_4 = 1+7+6+1 = 15
> $$

> [!note] Key Idea
> DOIB (partitioning a set of distinguishable objects into unlabeled non-empty groups) is the same combinatorial object as counting the number of **equivalence relations** on that set — each partition into groups corresponds exactly to one equivalence relation.

---

## 4. IOIB — Identical Objects, Identical Boxes (Integer Partitions)

Here both the objects **and** the boxes are identical, so only the multiset of group **sizes** matters — not which specific elements are in which group, and not which group is "first."

> [!example] Integer partitions of 4
> An integer partition of 4 treats the units as identical; only the sizes of the parts matter.
>
> - **1 part:** $4$ — 1 way
> - **2 parts:** $3+1$, $2+2$ — 2 ways
> - **3 parts:** $2+1+1$ — 1 way
> - **4 parts:** $1+1+1+1$ — 1 way
>
> $$
> P(4) = 1+2+1+1 = 5
> $$

> [!warning] Distinguishing DOIB from IOIB
> Both DOIB (Section 3) and IOIB (this section) use case-by-case reasoning over the number of groups, but they answer **different** questions: DOIB counts partitions of a set of **distinguishable** elements (so $(1,3)$ split has multiple distinct realizations depending on *which* element is alone), while IOIB counts partitions of an **integer** (so $(1,3)$ has exactly one realization, since the units are interchangeable). Compare $B_4 = 15$ (DOIB) against $P(4) = 5$ (IOIB) for the same total of 4 — the gap illustrates how much the distinguishability of objects matters.

---

## Related Notes

- [[Counting Rules]]
- [[Combinations]]
- [[Inclusion-Exclusion Principle]]
- [[moc combinatorics]]

## Open Questions

- [ ] Verify the $(2,1)$ case count in the "3 friends, no size requirement" example against a full manual enumeration to confirm no overcounting was missed.
- [ ] Add a standalone reference table of Stirling numbers of the second kind $S(n,k)$ for small $n$, and connect explicitly to Bell numbers.
- [ ] Cross-check the integer composition proof (Section 2.5) against a direct small-case enumeration (e.g., $n=3$ should give $2^{2}=4$ compositions: $3$; $1+2$; $2+1$; $1+1+1$).
