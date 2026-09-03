---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Modular Arithmetic"
subtopic: "Modular Fast Power Reduction & Negative Remainders"
difficulty: "Hard"
tags: [cds, elementary-mathematics, modular, remainders, subtopic]
---

# Modular Fast Power Reduction & Negative Remainders

## Core Practical Manipulation Techniques

### 1. Formal Euclidean Definition of Negative Dividends & Remainders

By the Euclidean Division Theorem, dividing any integer $A$ by positive integer $B$ yields quotient $Q$ and remainder $R$:
$$A = B \cdot Q + R \quad \text{where } \mathbf{0 \le R < B}$$

> [!IMPORTANT]
> The formal mathematical remainder $R$ MUST ALWAYS be non-negative ($0 \le R < B$).

#### 🔍 Example: What is the remainder when $-1$ is divided by $6$? ($ -1 \pmod 6 $)
Express $-1 = 6 \cdot Q + R$:
- If quotient $Q = 0 \implies -1 = 6(0) + (-1) \implies R = -1$ ❌ *(Invalid because $R < 0$)*
- If quotient $Q = -1 \implies -1 = 6(-1) + R \implies -1 = -6 + R \implies \mathbf{R = 5}$ ✅ *(Valid because $0 \le 5 < 6$)*

Thus, $-1 \pmod 6 \equiv \mathbf{5 \pmod 6}$.  
In general:
$$\mathbf{-1 \pmod m \equiv (m - 1) \pmod m}$$

---

### 2. The Number Line Intuition (Visualizing Negative Modulo)

Think of modular arithmetic on a number line with steps of size **6**:

$$\dots, -12, -6, \mathbf{0}, 6, 12, 18, \dots \quad (\text{Multiples of 6, Remainder } 0)$$

Every integer lies relative to the **previous multiple of 6 going left to right**:

| Dividend $A$ | Division Form ($B \cdot Q + R$) | Quotient $Q$ | Remainder $R \pmod 6$ |
| :--- | :--- | :--- | :--- |
| $+13$ | $6 \times 2 + 1$ | $2$ | $1$ |
| $+7$ | $6 \times 1 + 1$ | $1$ | $1$ |
| $+1$ | $6 \times 0 + 1$ | $0$ | $1$ |
| **$-1$** | $6 \times (-1) + \mathbf{5}$ | $-1$ | **$5$** |
| **$-2$** | $6 \times (-1) + \mathbf{4}$ | $-1$ | **$4$** |
| **$-3$** | $6 \times (-1) + \mathbf{3}$ | $-1$ | **$3$** |
| **$-5$** | $6 \times (-1) + \mathbf{1}$ | $-1$ | **$1$** |

---

### 3. The Negative Remainder Conversion Rule

Whenever an intermediate calculation yields a negative remainder $-k \pmod m$, **add the modulus $m$** to convert it into a standard positive remainder:

$$\mathbf{-k \pmod m \equiv (-k + m) \pmod m}$$

- $-1 \pmod 6 \implies -1 + 6 = \mathbf{5}$
- $-2 \pmod 6 \implies -2 + 6 = \mathbf{4}$
- $-5 \pmod 6 \implies -5 + 6 = \mathbf{1}$
- $-13 \pmod 7 \implies -13 + 7 = -6 \implies -6 + 7 = \mathbf{1}$

---

### 4. The Negative Remainder Exponent Shortcut ⚡

We temporarily use negative remainders in exponent problems because $(-1)^{\text{even}} = +1$ and $(-1)^{\text{odd}} = -1$.

#### Practical Application Example 1:
Find $24^{100} \pmod{25}$.
- $24 \equiv 24 - 25 = -1 \pmod{25}$.
- $24^{100} \equiv (-1)^{100} \pmod{25} \equiv \mathbf{1 \pmod{25}}$.

#### Practical Application Example 2:
Find $25^{99} \pmod{26}$.
- $25 \equiv -1 \pmod{26}$.
- $25^{99} \equiv (-1)^{99} \pmod{26} \equiv -1 \pmod{26}$.
- Convert to positive remainder: $-1 + 26 = \mathbf{25 \pmod{26}}$.

---

### 5. Cyclicity / Pattern Method for Powers

Every base $a$ modulo $m$ repeats its remainders in a periodic cycle.

#### Step-by-Step Procedure:
1. Compute powers $a^1, a^2, a^3, \dots \pmod m$ until you hit $1$ or a repeating sequence.
2. The number of steps to reach 1 is the **cycle length $C$**.
3. Reduce the large exponent $E \pmod C$.
4. $a^E \pmod m \equiv a^{E \pmod C} \pmod m$.

---

### 6. Modular Inverse & Cancellation

To "divide" by $a$ modulo $m$, we multiply by the **Modular Multiplicative Inverse $a^{-1}$**:
$$a \cdot a^{-1} \equiv 1 \pmod m$$
- **Condition for Existence**: $a^{-1}$ exists if and only if $\operatorname{GCD}(a, m) = 1$.
- **Finding $a^{-1}$ using Fermat's Little Theorem**: If $m = p$ is prime, then:
  $$a^{p-2} \equiv a^{-1} \pmod p$$

---

## Linked Practice Questions

- [[cds/math/notes/questions#question-11-modular-negative-remainder-power|Question 11: Modular Power Reduction using Negative Remainder]]
- [[cds/math/notes/questions#question-12-negative-remainder-power-trick|Question 12: Negative Remainder Power Trick]]

---

## Navigation

- [[cds/math/notes/modular|Modular Arithmetic Topic Page]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
