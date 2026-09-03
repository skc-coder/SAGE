---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Modular Arithmetic"
subtopic: "Chinese Remainder Theorem"
difficulty: "Hard"
tags: [cds, elementary-mathematics, modular, theorem, crt]
---

# Chinese Remainder Theorem (CRT)

## Statement & Construction

Used to solve systems of simultaneous linear congruences with pairwise co-prime moduli:

$$\begin{cases} x \equiv a_1 \pmod{m_1} \\ x \equiv a_2 \pmod{m_2} \\ \vdots \\ x \equiv a_k \pmod{m_k} \end{cases}$$

If $\operatorname{GCD}(m_i, m_j) = 1$ for all $i \neq j$, there exists a **unique solution modulo $M = m_1 \cdot m_2 \cdots m_k$**.

---

## Construction Algorithm

1. Compute total product $M = m_1 \cdot m_2 \cdots m_k$.
2. For each $i$, compute partial product $M_i = \frac{M}{m_i}$.
3. Find modular inverse $y_i = M_i^{-1} \pmod{m_i}$ such that $M_i y_i \equiv 1 \pmod{m_i}$.
4. The unique solution is:
   $$\mathbf{x \equiv \sum_{i=1}^k a_i M_i y_i \pmod M}$$

---

## Linked Practice Questions

- [[cds/math/notes/questions/q2|Question 2: Dual Remainder AP Sum]]

## Related Theorems & Topics

- [[cds/math/notes/subtopics/flt|Fermat's Little Theorem]]
- [[cds/math/notes/modular|Modular Arithmetic Topic]]
