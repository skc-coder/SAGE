---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Modular Arithmetic"
subtopic: "Modular Fast Power Reduction"
difficulty: "Hard"
tags: [cds, elementary-mathematics, modular, remainders, subtopic]
---

# Modular Fast Power Reduction & Negative Remainders

## Core Practical Manipulation Techniques

### 1. The Negative Remainder Trick (The Single Most Powerful Calculation Shortcut ⚡)

In modular arithmetic, a remainder can be expressed as a negative number:
$$a \equiv (a - m) \pmod m$$
- *Example*: $25 \pmod 7 \equiv 4 \pmod 7$, but also $4 - 7 = \mathbf{-3 \pmod 7}$.
- *Why is this useful?* Because $(-1)^{\text{even}} = +1$ and $(-1)^{\text{odd}} = -1$!

#### 💡 Practical Application Example:
Find $24^{100} \pmod{25}$.
- $24 \equiv -1 \pmod{25}$.
- $24^{100} \equiv (-1)^{100} \pmod{25} \equiv \mathbf{1 \pmod{25}}$.
*(Instead of multiplying 24 a hundred times, we solved it in 1 line!)*

---

### 2. Cyclicity / Pattern Method for Powers

Every base $a$ modulo $m$ repeats its remainders in a periodic cycle.

#### Step-by-Step Procedure:
1. Compute powers $a^1, a^2, a^3, \dots \pmod m$ until you hit $1$ or a repeating sequence.
2. The number of steps to reach 1 is the **cycle length $C$**.
3. Reduce the large exponent $E \pmod C$.
4. $a^E \pmod m \equiv a^{E \pmod C} \pmod m$.

---

### 3. Modular Inverse & Cancellation

To "divide" by $a$ modulo $m$, we multiply by the **Modular Multiplicative Inverse $a^{-1}$**:
$$a \cdot a^{-1} \equiv 1 \pmod m$$
- **Condition for Existence**: $a^{-1}$ exists if and only if $\operatorname{GCD}(a, m) = 1$.
- **Finding $a^{-1}$ using Fermat's Little Theorem**: If $m = p$ is prime, then:
  $$a^{p-2} \equiv a^{-1} \pmod p$$

---

## Linked Practice Questions

- [[cds/math/notes/questions#question-11-modular-negative-remainder-power|Question 11: Modular Power Reduction using Negative Remainder]]
- [[cds/math/notes/questions#question-12-fermats-little-theorem-remainder|Question 12: Finding Remainder using Fermat's Little Theorem]]

---

## Navigation

- [[cds/math/notes/modular|Modular Arithmetic Topic Page]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
