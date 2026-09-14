# Binomial Theorem and Combinatorial Identities

**Topic:** Discrete Mathematics > Combinatorics > Identities
**Source:** Personal notes — Combinatorics (GO Classes)
**Tags:** #combinatorics #binomial-theorem #identities #gate-cse
**Links:** [[moc combinatorics]] | [[Combinations]] | [[Distribution Techniques]]

---

> [!info] Overview
> This note covers the binomial theorem and the standard family of combinatorial identities built on top of it — Pascal's identity, the Hockey Stick identity, Vandermonde's identity, and the Committee-Chairman identity — along with the general combinatorial proof strategy used to derive and verify them.

---

## 1. Binomial Theorem

$$
(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}
$$

### 1.1 Patterns to Remember

1. The expansion has $n+1$ terms, ranging from $a^n$ (i.e. $a^n b^0$) to $b^n$ (i.e. $a^0 b^n$).
2. Every term has the form: coefficient $\times$ power of $a$ $\times$ power of $b$.
3. The exponents on $a$ and $b$ in every term always sum to $n$.
4. Powers of $a$ decrease from $n$ down to $0$; powers of $b$ increase from $0$ up to $n$.
5. Setting $a=b=1$ gives:
   $$
   \sum_{r=0}^{n}\binom{n}{r} = 2^n
   $$

---

## 2. Symmetry

$$
\binom{n}{r} = \binom{n}{n-r}
$$

Choosing $r$ elements to include is equivalent to choosing $n-r$ elements to exclude.

---

## 3. Pascal's Identity

$$
\binom{n+1}{k} = \binom{n}{k-1} + \binom{n}{k}
$$

**Combinatorial story:** Fix one particular element out of the $n+1$. Every $k$-subset either **includes** that element (contributing $\binom{n}{k-1}$, since $k-1$ more elements are chosen from the remaining $n$) or **excludes** it (contributing $\binom{n}{k}$, choosing all $k$ from the remaining $n$).

### 3.1 Variation — Two Particular Elements

$$
\binom{n}{k} = \binom{n-2}{k-2} + 2\binom{n-2}{k-1} + \binom{n-2}{k}
$$

Fixing two particular elements, a $k$-subset either includes both, includes exactly one (2 ways to choose which), or includes neither.

### 3.2 Recursive Definition

$$
\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}
$$

This is the same identity as above, re-indexed, and is the standard recursive definition used to build Pascal's Triangle.

---

## 4. Hockey Stick Identity

$$
\sum_{k=r}^{n}\binom{k}{r} = \binom{n+1}{r+1}
$$

Equivalently:

$$
\binom{r}{r} + \binom{r+1}{r} + \dots + \binom{n}{r} = \binom{n+1}{r+1}
$$

### 4.1 Combinatorial Story

Count the ways to select $r+1$ numbers from $\{1, 2, \dots, n+1\}$ two different ways.

- **Side 1 (direct):** $\binom{n+1}{r+1}$
- **Side 2 (fix the maximum selected element):**
  - Max $= n+1$: remaining $r$ elements chosen from the first $n$ → $\binom{n}{r}$
  - Max $= n$: remaining $r$ chosen from the first $n-1$ → $\binom{n-1}{r}$
  - $\vdots$
  - Max $= r+1$: remaining $r$ chosen from the first $r$ → $\binom{r}{r}$

Summing side 2 over all possible values of the maximum reproduces the left-hand side of the identity.

### 4.2 Variations

$$
\binom{n}{r} = \binom{n+1}{r+1} - \binom{n}{r+1}
$$

$$
\binom{n-1}{r-1} = \binom{n}{r} - \binom{n-1}{r}
$$

> [!example]
> Evaluate: $\binom{5}{5} + \binom{6}{5} + \binom{7}{5} + \binom{8}{5} + \binom{9}{5}$.
>
> **Approach:** Direct application of the Hockey Stick identity with $r=5$, summing from $k=5$ to $9$:
> $$
> \sum_{k=5}^{9}\binom{k}{5} = \binom{10}{6}
> $$

---

## 5. Vandermonde's Identity

$$
\binom{m+n}{r} = \sum_{k=0}^{r}\binom{m}{k}\binom{n}{r-k}
$$

### 5.1 Combinatorial Story

Choose a committee of $r$ people from $m$ men and $n$ women combined. Split the count by **how many men** are on the committee: if $k$ men are chosen ($\binom{m}{k}$ ways), the remaining $r-k$ committee members must be women ($\binom{n}{r-k}$ ways).

> [!note] Recognition tip
> Whenever the top of a binomial coefficient is a **sum** like $m+n$ (including the special case $2n = n+n$), try recasting the problem as a committee selected from $m$ men and $n$ women.

### 5.2 Corollaries

$$
\binom{2n}{n} = \sum_{k=0}^{n}\binom{n}{k}^2
$$

$$
\binom{2n}{2} = 2\binom{n}{2} + n^2
$$

The second corollary follows by splitting a 2-person committee from $2n = n+n$ people into: both from the first group of $n$ ($\binom{n}{2}$), both from the second group of $n$ ($\binom{n}{2}$), or one from each ($n \times n$).

---

## 6. Committee-Chairman Identity

$$
k\binom{n}{k} = n\binom{n-1}{k-1}
$$

### 6.1 Combinatorial Story

Count "committee of size $k$ with one designated chairman from among them" two ways:

1. **Committee first:** pick the $k$-member committee ($\binom{n}{k}$ ways), then pick the chairman from within it ($k$ ways).
2. **Chairman first:** pick the chairman from all $n$ people ($n$ ways), then pick the remaining $k-1$ ordinary members from the other $n-1$ people ($\binom{n-1}{k-1}$ ways).

### 6.2 Variation — Ordinary Members First

Pick the $k-1$ ordinary (non-chairman) members first from $n$ people ($\binom{n}{k-1}$ ways), then pick the chairman from the remaining $n-k+1$ people:

$$
(n-k+1)\binom{n}{k-1}
$$

This produces the same value as the two forms above.

### 6.3 Sum Over All Committee Sizes

$$
\sum_{k=0}^{n} k\binom{n}{k} = n \cdot 2^{n-1}
$$

**Story:** LHS counts all ways to pick a subcommittee of any size and designate one member as chairman. RHS picks the chairman first ($n$ ways), then independently decides, for each of the remaining $n-1$ people, whether they're on the subcommittee or not ($2^{n-1}$ ways).

### 6.4 Recursive Ratio Form

$$
\binom{n}{r} = \frac{n}{r}\binom{n-1}{r-1}
$$

This is an important alternate recursive definition, directly equivalent to the Committee-Chairman identity rearranged.

---

## 7. Combinatorial Proof Strategy

General approach for proving identities by "counting the same thing two ways":

- Argue that the LHS and RHS both count the **same** combinatorial object, just via two different counting arguments.
- A **summation** on one side usually signals a case split via the sum rule — look for a special object whose value/position determines the case.
- **Products** on one side usually signal a staged counting argument via the product rule.
- If the top of a binomial coefficient is a sum like $m+n$, try the "committee from $m$ men, $n$ women" framing.
- There is no single "right" object to count — pick whatever framing makes the identity's structure feel natural, then verify against a small case.

### 7.1 Bijective Proofs

Simplify a hard counting problem by mapping it to an equivalent, easier one via a bijection.

> [!example] Subsets ↔ bit strings
> Counting subsets of size $k$ from an $n$-element set is equivalent to counting bit strings of length $n$ with exactly $k$ ones — each subset corresponds to exactly one such string (1 = "included," 0 = "excluded"), and vice versa.

> [!note] Key Idea
> Assigning numbers or positions to abstract elements is a common trick that turns an otherwise abstract combinatorial problem into a concrete counting problem with a known formula.

---

## Related Notes

- [[Combinations]]
- [[Distribution Techniques]]
- [[moc combinatorics]]

## Open Questions

- [ ] Finish the Hockey Stick example numerically and confirm $\binom{10}{6}$ matches a direct sum of the five terms.
- [ ] Add a worked example applying Vandermonde's identity to a concrete GATE-style committee problem for practice.
