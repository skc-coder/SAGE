---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Algebraic Operations"
subtopic: "Remainder and Factor Theorem"
difficulty: "Medium"
tags: [cds, elementary-mathematics, remainder-theorem, factor-theorem, subtopic]
---

# Remainder and Factor Theorem

## Theory & Proofs

### 1. Remainder Theorem Derivation
Given a dividend polynomial $P(x)$ divided by a linear monic polynomial $(x - a)$:
By the Division Algorithm:
$$P(x) = (x - a) \cdot q(x) + R$$
where $R$ is a constant remainder (since $\deg(R) < \deg(x-a) = 1$).

Substituting $x = a$:
$$P(a) = (a - a) \cdot q(a) + R = 0 + R = R$$
$$\implies R = P(a)$$

#### Linear Divisor $(bx + c)$:
When divided by $(bx + c)$, set $bx + c = 0 \implies x = -\frac{c}{b}$. The remainder is:
$$R = P\left(-\frac{c}{b}\right)$$

---

### 2. Factor Theorem Proof
Let $P(x)$ be a polynomial.
1. **Direct Condition**: If $(x - a)$ is a factor of $P(x)$, then $P(x) = (x - a) q(x)$ for some polynomial $q(x)$.
   Evaluating at $x = a$:
   $$P(a) = (a - a) q(a) = 0$$

2. **Converse Condition**: If $P(a) = 0$, by Remainder Theorem $P(x) = (x - a) q(x) + P(a) = (x - a) q(x) + 0$.
   Therefore, $(x - a)$ divides $P(x)$ exactly, making $(x - a)$ a factor of $P(x)$.

---

## Linked Practice Questions
- [[cds/math/notes/questions/q48|Q48: Remainder Evaluation via Linear Divisor]]
- [[cds/math/notes/questions/q49|Q49: Unknown Parameter $k$ via Factor Theorem]]

## Variations
- [[cds/math/notes/variations/var26|Variation 26: Generalized Dual Parameter Factor Theorem System]]
