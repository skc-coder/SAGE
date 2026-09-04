---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Sequence and Series"
subtopic: "AP Properties"
difficulty: "Easy"
tags: [cds, elementary-mathematics, sequence-series, subtopic]
---

# Arithmetic Progression (AP) Properties & Summations

## Theory, Intuition & Derivations

### 1. Structure of an Arithmetic Progression
An Arithmetic Progression is a sequence where consecutive terms maintain a constant difference:
$$d = a_k - a_{k-1}$$

If $a$ is the first term and $d$ is the common difference, the sequence unfolds as:
$$a, a+d, a+2d, a+3d, \dots$$

### 2. General Term Derivation
The $n$-th term $T_n$ accumulates $(n-1)$ steps of common difference $d$ added to the starting term $a$:
$$T_n = a + (n-1)d$$

### 3. Summation Formula Derivation (Gauss Trick)
Write the sum $S_n$ forward and backward:
$$S_n = a + (a+d) + (a+2d) + \dots + (l-d) + l$$
$$S_n = l + (l-d) + (l-2d) + \dots + (a+d) + a$$

Adding term-by-term vertically:
$$2 S_n = (a+l) + (a+l) + \dots + (a+l) \quad \text{($n$ terms)}$$
$$2 S_n = n(a+l) \implies S_n = \frac{n}{2}(a+l)$$

Substituting $l = a + (n-1)d$:
$$S_n = \frac{n}{2} [2a + (n-1)d]$$

---

## Linked Practice Questions

- [[cds/math/notes/questions/q110|Q110: Sum of 11 terms of AP]]
- [[cds/math/notes/questions/q113|Q113: Ratio of m-th terms from ratio of sums of two APs]]
- [[cds/math/notes/questions/q114|Q114: Sum of inserted Arithmetic Means]]

---

## Navigation

- [[cds/math/notes/sequence_series|Topic: Sequence and Series]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
