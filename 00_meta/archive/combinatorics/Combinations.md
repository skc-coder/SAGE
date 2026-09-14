# Combinations

**Topic:** Discrete Mathematics > Combinatorics > Foundations
**Source:** Personal notes — Combinatorics
**Tags:** #combinatorics #combinations #gate-cse
**Links:** [[moc combinatorics]] | [[Counting Rules]] | [[Permutations]]

---

> [!info] Overview
> A combination is an **unordered** selection of objects. This note covers combinations without repetition, combinations with repetition (CWR), and a summary table comparing all four combinations of ordered/unordered and with/without repetition.

---

## 1. r-Combinations (No Repetition)

$$
C(n,r) = \binom{n}{r} = \frac{n!}{r!(n-r)!} = C(n, n-r)
$$

> [!note] Key Idea
> A combination is a division-rule application on top of the product rule: select $r$ objects in order ($P(n,r)$ ways), then divide by $r!$ because the internal order of the selected objects doesn't matter.
>
> $$
> \binom{n}{r} = \frac{P(n,r)}{r!}
> $$

> [!example] Committee of 3 from 5 students
> $$
> C(5,3) = 10
> $$

> [!example] Two independent committees
> **Question:** 3 professors from a 9-person math department AND 4 professors from an 11-person CS department. How many ways?
>
> **Approach:** Product rule across two independent unordered selections.
>
> $$
> C(9,3) \times C(11,4) = 84 \times 330 = 27{,}720
> $$

---

## 2. Combinations with Repetition (CWR)

Selecting $r$ items from $n$ types, where repetition of a type is allowed and order does not matter:

$$
\binom{n+r-1}{r} = \binom{n+r-1}{n-1}
$$

> [!example] Selecting 5 fruits from apple, mango, orange (repetition allowed)
> This is a star-and-bars problem — see [[Distribution Techniques]] for the full derivation and template.

**Notation:** $\left(\!\binom{n}{r}\!\right)$ denotes $n$ boxes (types) and $r$ stars (selections) in the star-and-bars framework.

---

## 3. Summary Table

|                            | Repetition allowed  | No repetition                 |
| :------------------------- | :------------------ | :---------------------------- |
| Ordered (lists)            | $n^k$               | $P(n,k) = \dfrac{n!}{(n-k)!}$ |
| Unordered (sets/multisets) | $\dbinom{n+k-1}{k}$ | $C(n,k) = \dbinom{n}{k}$      |

> [!note] How to use this table
> Identify two properties of the problem first: (1) does order matter — is this a sequence/arrangement or a selection? (2) is repetition of an item allowed? Once both are answered, the correct formula is read directly off the table.

---

## Related Notes

- [[Counting Rules]]
- [[Permutations]]
- [[Distribution Techniques]]
- [[moc combinatorics]]

## Open Questions

- [ ] Add a worked derivation of the CWR fruit-selection example directly in this note, or confirm it is sufficiently covered by the star-and-bars template in [[Distribution Techniques]].
