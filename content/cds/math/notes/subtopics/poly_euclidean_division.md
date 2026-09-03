---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "HCF and LCM of Polynomials"
subtopic: "Euclidean Division Algorithm for Polynomials"
difficulty: "Hard"
tags: [cds, math, hcf-lcm-polynomials, subtopic]
---

# Euclidean Division Algorithm for Polynomials

## Core Concept & Theory

When polynomials cannot be easily factorized using standard quadratic/cubic grouping techniques, the **Euclidean Long Division Algorithm** is used to find their HCF.

Given two polynomials $P(x)$ and $Q(x)$ with $\operatorname{deg}(P) \ge \operatorname{deg}(Q)$:
1. **Division Step**: Divide $P(x)$ by $Q(x)$ to get quotient $q_1(x)$ and remainder $R_1(x)$:
   $$P(x) = Q(x) \cdot q_1(x) + R_1(x), \quad \operatorname{deg}(R_1) < \operatorname{deg}(Q)$$
2. **Successive Division**: If $R_1(x) \neq 0$, make $Q(x)$ the new dividend and $R_1(x)$ the new divisor:
   $$Q(x) = R_1(x) \cdot q_2(x) + R_2(x)$$
3. **Termination**: Repeat until the remainder becomes zero: $R_{k-1}(x) = R_k(x) \cdot q_{k+1}(x) + 0$.
4. **Result**: The non-zero remainder $R_k(x)$ prior to zero remainder (monic or multiplied by scalar common factor) is the $\operatorname{HCF}(P(x), Q(x))$.

---

## Critical Rules for Polynomial Division:
- **Numerical Scalar Extraction**: If a scalar common factor exists in all terms of a polynomial or remainder (e.g. factor of 3 or $-39$), **extract it out**! Scalars do not affect the degree or root structure of polynomial HCF.
- **Negative Leading Coefficient**: If the leading term of a remainder becomes negative, multiply the remainder by $-1$ before making it the next divisor to simplify division.

---

## Direct Proof / Intuition

Why does $\operatorname{gcd}(P, Q) = \operatorname{gcd}(Q, R)$?
If $D(x)$ divides both $P(x)$ and $Q(x)$, then $D(x)$ divides $P(x) - Q(x)q(x) = R(x)$.
Conversely, if $D(x)$ divides $Q(x)$ and $R(x)$, it must divide $Q(x)q(x) + R(x) = P(x)$.
Thus, the set of common divisors of $(P, Q)$ is identical to $(Q, R)$, proving $\operatorname{HCF}(P, Q) = \operatorname{HCF}(Q, R)$.

---

## Linked Practice Questions

- [[cds/math/notes/questions/q31|Q31: Euclidean Division for 5th Degree Polynomials]]
