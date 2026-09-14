# Cheat Sheet - Discrete Mathematics

**Topic:** GATE CSE > Discrete Mathematics
**Source:** Compressed from Combinatorics notes
**Tags:** #cheat-sheet #discrete-mathematics #gate-cse
**Links:** [[Cheat Sheet MOC (GATE CSE)]] | [[moc combinatorics]] | [[Revision Tracker]]

---

> [!info] Overview
> Formulas and key trigger points only — no explanations, no examples. For learning/derivations, refer to the full topic notes linked in each section.

---

## Counting Rules

| Rule | Formula | Trigger |
| :--- | :--- | :--- |
| Sum | $\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert$ | disjoint OR / choose one |
| Product | $n_1 \times n_2 \times \dots \times n_k$ | sequential AND stages, fixed count per stage |
| Subtraction (2-set) | $\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert$ | overlapping OR |
| Division | $n/d$ | each outcome counted $d$ times |
| Complement | $\text{total} - \text{undesired}$ | undesired easier to count |

Full note: [[Counting Rules]]

---

## Permutations

| Case | Formula |
| :--- | :--- |
| $r$-permutation, no repetition | $P(n,r) = \dfrac{n!}{(n-r)!}$ |
| Permutation, repetition allowed | $n^r$ |
| Multiset permutation | $\dfrac{n!}{n_1!\,n_2!\,\dots\,n_k!}$ |

**Special arrangement cases:**

| Situation | Method |
| :--- | :--- |
| Substring | bundle, permute with rest |
| Subsequence | bundle, divide by $2$ |
| Adjacent | bundle → permute units → permute internally |
| Never adjacent | fix others → place into gaps |

Full note: [[Permutations]]

---

## Combinations

| Case | Formula |
| :--- | :--- |
| $r$-combination, no repetition | $C(n,r) = \dbinom{n}{r} = \dfrac{n!}{r!(n-r)!}$ |
| CWR | $\dbinom{n+r-1}{r}$ |

**Summary table:**

| | Rep. allowed | No repetition |
| :--- | :--- | :--- |
| Ordered | $n^k$ | $P(n,k)$ |
| Unordered | $\dbinom{n+k-1}{k}$ | $C(n,k)$ |

Full note: [[Combinations]]

---

## Distribution Techniques

| Type | Objects | Boxes | Formula |
| :--- | :--- | :--- | :--- |
| DODB | distinguishable | distinguishable | $\dfrac{n!}{n_1!\,n_2!\,\dots\,n_k!}$ (or $m^n$, no size constraint) |
| IODB (star-bars) | identical | distinguishable | $\dbinom{n+r-1}{r}$ |
| DOIB | distinguishable | identical | Stirling 2nd kind $S(n,k)$; sum → Bell number $B_n$ |
| IOIB | identical | identical | integer partition $P(n)$ |

**Variable restriction substitutions (IODB):**

| Restriction | Substitution |
| :--- | :--- |
| $x_i > c$ | reduce target by $c+1$ |
| $x_i \ge c$ | reduce target by $c$ |
| $\sum x_i \le n$ | add slack variable |

**Integer composition count:** $2^{n-1}$

Full note: [[Distribution Techniques]]

---

## Binomial Theorem and Identities

$$
(a+b)^n = \sum_{k=0}^{n}\binom{n}{k}a^k b^{n-k}, \qquad \sum_{r=0}^n \binom{n}{r} = 2^n
$$

| Identity | Formula |
| :--- | :--- |
| Symmetry | $\dbinom{n}{r} = \dbinom{n}{n-r}$ |
| Pascal's | $\dbinom{n+1}{k} = \dbinom{n}{k-1}+\dbinom{n}{k}$ |
| Hockey Stick | $\displaystyle\sum_{k=r}^{n}\binom{k}{r} = \binom{n+1}{r+1}$ |
| Vandermonde | $\dbinom{m+n}{r} = \displaystyle\sum_{k=0}^{r}\binom{m}{k}\binom{n}{r-k}$ |
| Committee-Chairman | $k\dbinom{n}{k} = n\dbinom{n-1}{k-1}$ |
| Chairman sum | $\displaystyle\sum_{k=0}^{n} k\binom{n}{k} = n\cdot 2^{n-1}$ |

Full note: [[Binomial Theorem and Combinatorial Identities]]

---

## Inclusion-Exclusion Principle (IEP)

$$
\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert - \lvert A \cap B \rvert
$$

$$
\lvert A \cup B \cup C \rvert = \lvert A \rvert+\lvert B \rvert+\lvert C \rvert - \lvert A\cap B\rvert - \lvert B\cap C\rvert - \lvert A\cap C\rvert + \lvert A\cap B\cap C\rvert
$$

**Bounds:** $\max(\lvert A\rvert,\lvert B\rvert) \le \lvert A\cup B\rvert \le \lvert A\rvert+\lvert B\rvert$

**Multiples in range:** $\left\lfloor \dfrac{b}{n}\right\rfloor - \left\lfloor \dfrac{a-1}{n}\right\rfloor$

**Symmetric difference:** $A \oplus B = \lvert A\rvert+\lvert B\rvert-2\lvert A\cap B\rvert$

Full notes: [[Inclusion-Exclusion Principle]] · [[Finding Union of Sets]]

---

## Derangements

$$
D_n = n!\left[1 - \frac{1}{1!}+\frac{1}{2!}-\dots+\frac{(-1)^n}{n!}\right]
$$

$$
D_n = (n-1)[D_{n-1}+D_{n-2}], \qquad D_n = nD_{n-1}+(-1)^n
$$

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $D_n$ | 1 | 0 | 1 | 2 | 9 | 44 | 265 |

**Parity:** $D_{\text{even}}$ = odd, $D_{\text{odd}}$ = even

**Identity:** $n! = \displaystyle\sum_{r=0}^n \binom{n}{r}D_{n-r}$

Full note: [[Derangements]]

---

## Onto Functions (Surjections)

$$
\#\text{onto} = n^m - \binom{n}{1}(n-1)^m + \binom{n}{2}(n-2)^m - \dots
$$

Full note: [[Onto Functions (Surjections) via IEP]]

---

## Related Notes

- [[Cheat Sheet MOC (GATE CSE)]]
- [[moc combinatorics]]
- [[Revision Tracker]]

## Open Questions

- [ ] Add Pigeonhole Principle, Generating Functions, and Recurrence Relations sections once those topic notes are finalized.
