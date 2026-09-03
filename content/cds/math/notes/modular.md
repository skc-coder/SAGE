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


### 3. Negative Remainder Conversion Rule
$-k \pmod m \equiv (-k + m) \pmod m$.

### 4. Modular Inverse & Cancellation
$a \cdot a^{-1} \equiv 1 \pmod m$. Exists if and only if $\operatorname{GCD}(a, m) = 1$.
### 5. Essential Theorems & Proofs

#### [[cds/math/notes/subtopics/flt|Theorem 1: Fermat's Little Theorem (FLT)]]
If $p$ is a prime number and $a$ is any integer such that $\operatorname{GCD}(a, p) = 1$, then:
$$\mathbf{a^{p-1} \equiv 1 \pmod p} \quad \text{and} \quad \mathbf{a^p \equiv a \pmod p}$$

#### [[cds/math/notes/subtopics/euler|Theorem 2: Euler's Totient Theorem (Composite Modulus $m$)]]
For ANY modulus $m$ (prime or composite) where $\operatorname{GCD}(a, m) = 1$:
$$\mathbf{a^{\phi(m)} \equiv 1 \pmod m}$$
where $\phi(m) = m \left(1 - \frac{1}{p_1}\right) \left(1 - \frac{1}{p_2}\right) \cdots \left(1 - \frac{1}{p_k}\right)$.

---

#### [[cds/math/notes/subtopics/crt|Theorem 2: Chinese Remainder Theorem (CRT)]]
Used to solve systems of simultaneous linear congruences with pairwise co-prime moduli $m_1, m_2, \dots, m_k$.

---

#### [[cds/math/notes/subtopics/wilson|Theorem 3: Wilson's Theorem]]
For any prime $p$: $(p-1)! \equiv -1 \pmod p$.


---

## Linked Practice Questions

- [[cds/math/notes/questions/q11|Question 11: Modular Fast Power Reduction]]
- [[cds/math/notes/questions/q12|Question 12: Negative Remainder Power Trick]]
- [[cds/math/notes/questions/q13|Question 13: Large Exponent Modulo Prime (2^1000 mod 17)]]
- [[cds/math/notes/questions/q14|Question 14: Sum of Powers Modulo Prime (1^12 + 2^12 + ... + 12^12 mod 13)]]
- [[cds/math/notes/questions/q15|Question 15: Wilson's Theorem Companion (12! + 2 mod 13)]]

---

## Navigation

- [[cds/math/math_overview|Elementary Mathematics Overview]]
- [[cds/math/question_db|Question Database]]
