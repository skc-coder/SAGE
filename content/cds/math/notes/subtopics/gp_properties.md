---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Sequence and Series"
subtopic: "GP Properties"
difficulty: "Medium"
tags: [cds, elementary-mathematics, sequence-series, subtopic]
---

# Geometric Progression (GP) Properties & Infinite Series

## Theory, Intuition & Derivations

### 1. Structure of a Geometric Progression
A sequence with constant common ratio $r = \frac{a_k}{a_{k-1}}$:
$$a, ar, ar^2, ar^3, \dots$$

### 2. Finite Geometric Sum Derivation
Let $S_n = a + ar + ar^2 + \dots + ar^{n-1}$.
Multiply the entire sum by $r$:
$$r S_n = ar + ar^2 + ar^3 + \dots + ar^n$$

Subtract $r S_n$ from $S_n$:
$$S_n - r S_n = a - ar^n$$
$$S_n (1 - r) = a (1 - r^n) \implies S_n = \frac{a(1 - r^n)}{1 - r} \quad (r \ne 1)$$

### 3. Infinite Geometric Series ($|r| < 1$)
When $|r| < 1$, as $n \to \infty$, $r^n \to 0$.
The sum simplifies to:
$$S_\infty = \frac{a}{1 - r}$$

---

## Linked Practice Questions

- [[cds/math/notes/questions/q111|CDS Sequence & Series Q2: 4th, 10th, 16th terms of GP]]

---

## Navigation

- [[cds/math/notes/sequence_series|Topic: Sequence and Series]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
