---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Modular Arithmetic"
subtopic: "Cheatsheet & Key Theorems"
difficulty: "Hard"
tags: [cds, elementary-mathematics, modular, cheatsheet, theorems]
---

# Modular Arithmetic — Core Theorems, Properties & Models

## 1. Definition of Congruence
$$a \equiv b \pmod m \iff m \mid (a - b) \iff a = k \cdot m + b$$
*Intuition: $a$ and $b$ leave the exact same remainder when divided by $m$.*

---

## 2. Fundamental Algebraic Rules
If $a \equiv b \pmod m$ and $c \equiv d \pmod m$:
1. **Addition**: $a + c \equiv b + d \pmod m$
2. **Subtraction**: $a - c \equiv b - d \pmod m$
3. **Multiplication**: $a \cdot c \equiv b \cdot d \pmod m$
4. **Exponentiation**: $a^k \equiv b^k \pmod m \quad (\text{for } k \in \mathbb{Z}^+)$
5. **Division / Cancellation Rule**:
   $$a \cdot c \equiv b \cdot c \pmod m \implies a \equiv b \pmod{\frac{m}{\operatorname{GCD}(c, m)}}$$
   *(If $\operatorname{GCD}(c, m) = 1$, you can directly cancel $c$: $a \equiv b \pmod m$).*
6. **Negative Remainder Conversion Rule**:
   $$-k \pmod m \equiv (-k + m) \pmod m$$

---

## 3. Key Modular Theorems

### Theorem 1: Fermat's Little Theorem (FLT) — Prime Modulus $p$
If $p$ is prime and $\operatorname{GCD}(a, p) = 1$:
$$\mathbf{a^{p-1} \equiv 1 \pmod p} \quad \text{and} \quad \mathbf{a^p \equiv a \pmod p}$$
- **Modular Inverse**: $a^{-1} \equiv a^{p-2} \pmod p$.

---

### Theorem 2: Euler's Totient Theorem — Any Modulus $m$ (Composite or Prime)
If $\operatorname{GCD}(a, m) = 1$:
$$\mathbf{a^{\phi(m)} \equiv 1 \pmod m}$$
where $\phi(m) = m \left(1 - \frac{1}{p_1}\right)\left(1 - \frac{1}{p_2}\right)\cdots\left(1 - \frac{1}{p_k}\right)$.
- **Modular Inverse**: $a^{-1} \equiv a^{\phi(m) - 1} \pmod m$.

---

### Theorem 3: Chinese Remainder Theorem (CRT) — Simultaneous Congruences
System of congruences $x \equiv a_i \pmod{m_i}$ with pairwise co-prime moduli $\operatorname{GCD}(m_i, m_j) = 1$:
- Total modulus $M = m_1 \cdot m_2 \cdots m_k$.
- Partial products $M_i = \frac{M}{m_i}$, and inverse $y_i = M_i^{-1} \pmod{m_i}$.
- Unique solution modulo $M$:
  $$\mathbf{x \equiv \sum_{i=1}^k a_i M_i y_i \pmod M}$$

---

### Theorem 4: Wilson's Theorem — Factorial Remainder Test for Primes
An integer $p > 1$ is prime if and only if:
$$\mathbf{(p - 1)! \equiv -1 \pmod p} \quad \iff \quad \mathbf{(p - 1)! + 1 \equiv 0 \pmod p}$$

---

## 4. Grand Algebraic Hierarchy

$$\begin{array}{ccc}
 & \mathbf{\text{Lagrange's Theorem in Group Theory}} & \\
 & (g^{|G|} = e \text{ for any finite group } G) & \\
 & \swarrow \qquad \qquad \searrow & \\
\mathbf{\text{Euler's Totient Theorem}} & & \mathbf{\text{Fermat's Little Theorem (FLT)}} \\
G = \mathbb{Z}_m^\times \text{ (Composite } m \text{)} & & G = \mathbb{Z}_p^\times \text{ (Prime } p \text{)} \\
|G| = \phi(m) & & |G| = p - 1 \\
a^{\phi(m)} \equiv 1 \pmod m & & a^{p-1} \equiv 1 \pmod p
\end{array}$$

---

## Navigation
- [[cds/math/notes/modular|Modular Arithmetic Main Topic Note]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
