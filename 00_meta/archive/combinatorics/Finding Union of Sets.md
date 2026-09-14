# Finding Union of Sets

**Topic:** Discrete Mathematics > Combinatorics > Set Theory
**Source:** Personal notes — Combinatorics
**Tags:** #combinatorics #set-theory #IEP #gate-cse
**Links:** [[moc combinatorics]] | [[Inclusion-Exclusion Principle]] | [[Counting Rules]]

---

> [!info] Overview
> Quick-reference note on the general approach to finding the size of a set union. Full formulas, derivations, and worked applications live in [[Inclusion-Exclusion Principle]]; this note captures the general framing and quick bounds.

---

## 1. General Approach

Use a Venn diagram. Many identities can express $|A \cup B|$ depending on which quantities are known — for example:

$$
|A \cup B| = |A - B| \cup |B - A| \cup (A \cap B)
$$

$$
|A \cup B| = |A| + |B| - |A \cap B|
$$

Inclusion-exclusion is **one** technique among several for computing a union — it is the most general and systematic, but region-splitting via a Venn diagram can sometimes be faster for a specific problem structure.

---

## 2. General Inclusion-Exclusion Formula

$$
|A_1 \cup A_2 \cup \dots \cup A_n| = \sum|A_i| - \sum|A_i \cap A_j| + \sum|A_i \cap A_j \cap A_k| - \dots
$$

**Method:** assign a number to each region of the Venn diagram based on how many of the $n$ sets that region belongs to. Add all single-set regions, subtract all pairwise intersections, add all triple intersections, and so on, alternating sign.

See [[Inclusion-Exclusion Principle]] for the full 2-set, 3-set, 4-set derivations and a large set of worked applications (divisibility counting, string counting, card hands, adjacency-constrained arrangements, bounded distributions).

---

## 3. Bounds on $|A \cup B|$

$$
\max(|A|,|B|) \le |A \cup B| \le |A|+|B|
$$

- Lower bound (equality) holds when one set is a subset of the other.
- Upper bound (equality) holds when the two sets are disjoint.

---

## 4. Counting Multiples in a Range

For counting integers divisible by $r$ within a range:

$$
\text{multiples of } r \text{ in } (a, b] = \left\lfloor \frac{b}{r} \right\rfloor - \left\lfloor \frac{a}{r} \right\rfloor
$$

$$
\text{if } a \text{ is inclusive: } \left\lfloor \frac{b}{r} \right\rfloor - \left\lfloor \frac{a-1}{r} \right\rfloor
$$

> [!note] Inclusivity convention
> By default, ranges are treated as inclusive at both ends unless stated otherwise. If $b$ is **not** itself a multiple of $r$, whether the upper bound is inclusive or exclusive at $b$ makes no difference to the count. If $b$ **is** a multiple of $r$, inclusivity at $b$ does matter and must be checked carefully.

Full worked divisibility problems (7 or 11, up to 1000, etc.) are in [[Inclusion-Exclusion Principle#6. Divisibility / Counting Multiples]].

---

## Related Notes

- [[Inclusion-Exclusion Principle]]
- [[Counting Rules]]
- [[moc combinatorics]]

## Open Questions

- [ ] None currently — this note is intentionally a thin pointer to [[Inclusion-Exclusion Principle]] for full detail.
