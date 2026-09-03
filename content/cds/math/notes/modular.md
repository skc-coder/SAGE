---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Modular Arithmetic"
difficulty: "Hard"
tags: [cds, elementary-mathematics, modular-arithmetic, topic]
---

# Modular Arithmetic

## Theory, Intuition & Key Properties

Modular arithmetic (often called "clock arithmetic") is the study of remainders. Instead of focusing on the quotient when $a$ is divided by $m$, we focus purely on the remainder.

---

### 1. Definition of Congruence

We say that two integers $a$ and $b$ are **congruent modulo $m$** (written as $a \equiv b \pmod m$) if and only if their difference $(a - b)$ is a multiple of $m$.

$$\mathbf{a \equiv b \pmod m \iff m \mid (a - b) \iff a = k \cdot m + b}$$

#### 💡 Practical Intuition:
- $a \equiv b \pmod m$ simply means **"$a$ and $b$ leave the exact same remainder when divided by $m$."**
- Example: $17 \equiv 5 \pmod{12}$ because $17 - 5 = 12$ (or both leave remainder 5 when divided by 12).
- Example: $23 \equiv -1 \pmod{6}$ because $23 - (-1) = 24$, which is a multiple of 6 (or 23 is 1 short of 24).

---

### 2. Fundamental Algebraic Rules (Manipulating Congruences)

If $a \equiv b \pmod m$ and $c \equiv d \pmod m$, then:

1. **Addition Rule**:
   $$a + c \equiv b + d \pmod m$$
2. **Subtraction Rule**:
   $$a - c \equiv b - d \pmod m$$
3. **Multiplication Rule**:
   $$a \cdot c \equiv b \cdot d \pmod m$$
4. **Exponentiation Rule**:
   $$a^k \equiv b^k \pmod m \quad (\text{for any positive integer } k)$$

> [!CAUTION]
> **Division Rule (The Common Trap!)**: You CANNOT simply divide both sides of a congruence by an integer $c$!
> - If $a \cdot c \equiv b \cdot c \pmod m$, then $a \equiv b \pmod{\frac{m}{\operatorname{GCD}(c, m)}}$.
> - **Special Case**: If $\operatorname{GCD}(c, m) = 1$ (co-prime), ONLY THEN can you cancel $c$:
>   $$a \cdot c \equiv b \cdot c \pmod m \implies a \equiv b \pmod m \quad (\text{if } \operatorname{GCD}(c, m) = 1)$$

---

### 3. Essential Theorems & Proofs

#### Theorem 1: Fermat's Little Theorem (FLT)
If $p$ is a prime number and $a$ is any integer such that $\operatorname{GCD}(a, p) = 1$, then:
$$\mathbf{a^{p-1} \equiv 1 \pmod p}$$

- **Practical Use**: Reduces massive powers modulo a prime!
- *Example*: What is $2^{100} \pmod{101}$? Since 101 is prime and $\operatorname{GCD}(2, 101) = 1$, $2^{100} \equiv 1 \pmod{101}$.

---

#### Theorem 2: Euler's Totient Theorem (Generalization of FLT)
For ANY modulus $m$ (prime or composite) and integer $a$ co-prime to $m$ ($\operatorname{GCD}(a, m) = 1$):
$$\mathbf{a^{\phi(m)} \equiv 1 \pmod m}$$
where $\phi(m)$ is **Euler's Totient Function** (the count of integers up to $m$ that are co-prime to $m$).

- **Formula for $\phi(m)$**: If $m = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$, then:
  $$\phi(m) = m \left(1 - \frac{1}{p_1}\right) \left(1 - \frac{1}{p_2}\right) \cdots \left(1 - \frac{1}{p_k}\right)$$

---

#### Theorem 3: Chinese Remainder Theorem (CRT)
Used to solve systems of simultaneous linear congruences with pairwise co-prime moduli:
$$\begin{cases} x \equiv a_1 \pmod{m_1} \\ x \equiv a_2 \pmod{m_2} \\ \vdots \\ x \equiv a_k \pmod{m_k} \end{cases}$$
If $\operatorname{GCD}(m_i, m_j) = 1$ for all $i \neq j$, there exists a **unique solution modulo $M = m_1 \cdot m_2 \cdots m_k$**.

---

## Subtopics & Core Techniques

- [[cds/math/notes/subtopics/modular_manipulation|Modular Fast Power Reduction & Negative Remainders]]

---

## Navigation

- [[cds/math/math_overview|Elementary Mathematics Overview]]
- [[cds/math/question_db|Question Database]]
