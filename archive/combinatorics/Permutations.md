# Permutations

**Topic:** Discrete Mathematics > Combinatorics > Foundations
**Source:** Personal notes — Combinatorics
**Tags:** #combinatorics #permutations #gate-cse
**Links:** [[moc combinatorics]] | [[Counting Rules]] | [[Combinations]]

---

> [!info] Overview
> A permutation is an **ordered** arrangement of objects. This note covers permutations without repetition, permutations where repetition is allowed in the output, permutations of a multiset (repeated elements in the input), and a set of specialized arrangement techniques for adjacency and gap constraints.

---

## 1. r-Permutations (No Repetition)

The number of ordered arrangements of $r$ objects chosen from $n$ distinct objects, with no repetition:

$$
P(n,r) = \frac{n!}{(n-r)!} = n(n-1)(n-2)\cdots(n-r+1)
$$

> [!example] Selecting 3 students from 5 to stand in line
> $$
> P(5,3) = 5 \times 4 \times 3 = 60
> $$

---

## 2. Permutations with Repetition Allowed (in Output)

When each of the $r$ positions can independently take any of the $n$ values (repetition allowed):

$$
n^r
$$

> [!example] Strings of length 10 over lowercase English letters
> $$
> 26^{10}
> $$

---

## 3. Permutations with Repeated Elements (in Input)

When arranging $n$ objects where the objects themselves are not all distinct — there are $k$ types, with $n_1$ of type 1, $n_2$ of type 2, ..., $n_k$ of type $k$, and $n_1 + n_2 + \dots + n_k = n$:

$$
\frac{n!}{n_1!\, n_2!\, \dots\, n_k!}
$$

> [!example] Rearranging the letters of SUCCESS
> S appears 3 times, C appears 2 times, U and E each appear once (7 letters total).
> $$
> \frac{7!}{3!\,2!\,1!\,1!} = 420
> $$

### 3.1 Two Derivation Methods

**Method 1 — Division rule:** Treat all repeated elements as temporarily distinct (e.g., label the two O's in COOK as $O_1, O_2$), permute normally, then divide by the number of ways each repeated group can be internally rearranged (since those rearrangements produce the same final word).

> [!example] COOK
> Treat both O's as distinct → $4!$ total arrangements → divide by $2!$ for the two O's → $\dfrac{4!}{2!} = 12$.

**Method 2 — Position assignment:** Assign positions to each letter type one at a time, choosing which of the remaining open positions that type occupies.

> [!example] COOK via position assignment
> C: choose 1 position out of 4 → $\binom{4}{1}$
> O: choose 2 positions out of the remaining 3 → $\binom{3}{2}$
> K: only 1 position left, fixed
>
> $$
> \binom{4}{1}\binom{3}{2} = 4 \times 3 = 12
> $$

> [!note] Key Idea
> Method 2 (position assignment) is more powerful in practice — it generalizes cleanly to problems with additional constraints (adjacency, ordering, gaps) that the simple division-rule method cannot handle directly.

### 3.2 Harder Examples — Position Assignment Method

> [!example] Arranging letters of PERMUTATIONS
> **Question:** In how many ways can the letters of PERMUTATIONS be arranged?
>
> **Approach:** 12 letters total, with T repeated twice (all others distinct). Choose 2 positions out of 12 for the T's, then arrange the remaining 10 distinct letters in the remaining positions:
>
> $$
> \binom{12}{2} \times 10!
> $$

> [!example] PERMUTATIONS with a gap constraint
> **Question:** In how many ways can the letters of PERMUTATIONS be arranged if there are always exactly 4 letters between P and S?
>
> **Approach:**
> - P and S, with exactly 4 letters between them, can start at 7 different positions along the 12-letter string (positions $1$–$6$ paired with positions $6$–$11$, i.e. 7 valid starting offsets), and the pair can appear as either "P...S" or "S...P" — 2 internal orders.
>
> $$
> 7 \times 2
> $$
>
> - The remaining 10 letters (T still repeated twice) fill the remaining 10 positions:
>
> $$
> \frac{10!}{2!}
> $$
>
> **Total:**
>
> $$
> 7 \times 2 \times \frac{10!}{2!}
> $$

### 3.3 Multinomial Notation

$$
\binom{n}{n_1,\, n_2,\, \dots,\, n_k} = \frac{n!}{n_1!\, n_2!\, \dots\, n_k!}
$$

> [!example]
> $$
> \binom{20}{5,\,9,\,6} = \frac{20!}{5!\,9!\,6!}
> $$

---

## 4. Special Arrangement Cases

| Situation                          | Method                                                                                |
| :--------------------------------- | :------------------------------------------------------------------------------------ |
| Substring (order fixed)            | Treat as a single unit, permute with the rest                                         |
| Subsequence (order doesn't matter) | Treat as a single unit; divide by 2 for the unordered pair                            |
| Elements next to each other        | Bundle as one unit → permute the units → permute internally                           |
| Elements never next to each other  | Fix the other elements first → permute the target elements into the gaps between them |

> [!example] WONDERING — exactly two consecutive vowels
> **Question:** In how many ways can the letters of WONDERING be arranged such that exactly two vowels are consecutive (and the third vowel is not adjacent to that pair)?
>
> **Setup:** Vowels: O, U, I. Consonants: W, N, N, D, R, G (N repeated).
>
> **Approach:**
> - Choose which 2 of the 3 vowels form the adjacent pair: $\binom{3}{2}$
> - Internal order of the chosen pair (e.g., OU vs UO): $2!$
> - Arrange the 6 consonants together with the vowel-pair treated as a single unit — that's 7 units total, but with N repeated: $\dfrac{6!}{2!}$ arrangements of the consonants alone; the vowel-pair unit and the third (lone) vowel are then placed into the gaps created by these 7 units.
> - Place the vowel-pair unit and the remaining lone vowel into 2 of the available gap positions, ensuring the lone vowel does not land adjacent to the pair unit: $_7P_2$
>
> $$
> \binom{3}{2} \times 2! \times \frac{6!}{2!} \times {}_7P_2
> $$
>
> > [!warning] Constraint to double-check
> > The critical constraint is that the **third** vowel must never end up adjacent to the chosen pair (otherwise all three vowels would effectively be consecutive, violating "exactly two"). This constraint is why the pair and the lone vowel are placed into gaps via a permutation ($_7P_2$) rather than simply multiplied as independent choices — verify this step carefully against a small worked case before relying on it for an exam answer.

---

## Related Notes

- [[Counting Rules]]
- [[Combinations]]
- [[moc combinatorics]]

## Open Questions

- [ ] Verify the WONDERING example's gap-placement step ($_7P_2$) against a manual small-case check — the source material itself flagged uncertainty here ("wait — actually...").
- [ ] Compute final numeric answers for the PERMUTATIONS examples in Section 3.2.
