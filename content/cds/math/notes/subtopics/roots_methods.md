---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Square Roots and Cube Roots"
subtopic: "Prime Factorization & Division Method"
difficulty: "Medium"
tags: [cds, elementary-mathematics, roots, subtopic]
---

# Prime Factorization & Division Method

## Theory, Intuition & Properties

The square root of a non-negative real number $x$, denoted $\sqrt{x}$, is the unique non-negative real number $y$ such that $y^2 = x$.

### Properties of Perfect Squares

- **Ending Digits**: A natural number ending in $2, 3, 7$, or $8$ is **never** a perfect square.
- **Parity**: The square of an even integer is even ($ (2k)^2 = 4k^2 $), and the square of an odd integer is odd ($ (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2+2k)+1 $).
- **Consecutive Differences**: The difference of squares of two consecutive natural numbers equals their sum:
  $$(n+1)^2 - n^2 = (n+1+n)(n+1-n) = 2n + 1$$
- **Four Consecutive Product Theorem**: The product of four consecutive integers plus $1$ is always a perfect square:
  $$n(n+1)(n+2)(n+3) + 1 = (n^2 + 3n + 1)^2$$
- **Trailing Zeroes**: A number ending in an odd number of trailing zeroes is never a perfect square.

---

### Methods of Finding Square Roots

1. **Prime Factorization Method**: Express the number as a product of prime powers:
   $$n = p_1^{2a_1} p_2^{2a_2} \dots p_k^{2a_k} \implies \sqrt{n} = p_1^{a_1} p_2^{a_2} \dots p_k^{a_k}$$
2. **Long Division Method**: Group digits into periods of two from right to left (for integer part) and left to right (for decimal part), finding maximal quotient digits iteratively.

---

### Properties of Cubes & Cube Roots

- **Digit Patterns**: Cubes of numbers ending in $0, 1, 4, 5, 6, 9$ end in the same digit. Cubes ending in $3$ end in $7$ (and vice versa); cubes ending in $2$ end in $8$ (and vice versa).
- **Negative Cubes**: $\sqrt[3]{-x} = -\sqrt[3]{x}$ for all $x \in \mathbb{R}$.

---

## Linked Practice Questions

- [[cds/math/notes/questions/q5_1|Q1: Decimal Root Simplification Ratio]]
- [[cds/math/notes/questions/q5_2|Q2: Smallest 4-Digit Perfect Square]]

## Variations

- [[cds/math/notes/variations/var5|Ch 5 Variations (Nested Infinite Radicals & Consecutive Product Squares)]]
