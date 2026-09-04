---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Number System"
subtopic: "Base-b Positional Representation & Radix Expansion"
difficulty: "Medium"
tags: [cds, math, base-representation, floating-point, computer-science, subtopic]
---

# Base-b Positional Representation & Radix Expansion

## Theory, Intuition & Fundamental Proofs

### 1. The Fundamental Theorem of Base-$b$ Fractional Termination

**Theorem**: A reduced rational fraction $\frac{p}{q}$ (where $\gcd(p, q) = 1$) has a **terminating expansion** in base $b$ if and only if every prime factor of $q$ is also a prime factor of $b$. That is:
$$\operatorname{prime\_factors}(q) \subseteq \operatorname{prime\_factors}(b)$$

---

### Formal Mathematical Proof

#### ($\implies$) Proof of Direct Condition:
Assume $\frac{p}{q}$ terminates in base $b$ after $k$ fractional digits.
Then $\frac{p}{q}$ can be written as a finite radix expansion:
$$\frac{p}{q} = \frac{d_1}{b^1} + \frac{d_2}{b^2} + \dots + \frac{d_k}{b^k} = \frac{N}{b^k}$$
where $N = d_1 b^{k-1} + d_2 b^{k-2} + \dots + d_k$ is an integer.

Cross-multiplying yields:
$$p \cdot b^k = N \cdot q$$

Since $q$ divides $N \cdot q$, $q$ must divide $p \cdot b^k$.
Because $\gcd(p, q) = 1$, by Euclid's Lemma, $q$ must divide $b^k$:
$$q \mid b^k$$

By the Fundamental Theorem of Arithmetic, if $q \mid b^k$:
1. Every prime factor $r$ that divides $q$ must also divide $b^k$ (transitivity of divisibility).
2. The prime factors of $b^k = (b \cdot b \cdot \dots \cdot b)$ are **identical** to the prime factors of $b$ (raising a number to power $k$ repeats existing prime factors; it never introduces new prime factors).
3. Therefore, if $r \mid b^k$, then $r$ MUST be one of the prime factors of $b$ ($r \mid b$).

Hence, $\operatorname{prime\_factors}(q) \subseteq \operatorname{prime\_factors}(b)$.

---

### 2. Base Comparison Table

| Base $b$ | Base Name | Prime Factors of Base $b$ | Terminating Denominators $q = p_1^{e_1} p_2^{e_2} \dots$ | Example Terminating | Example Non-Terminating (Infinite Repeating) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Base 10** | Decimal | $\{2, 5\}$ | $q = 2^a \cdot 5^b$ | $\frac{1}{2} = 0.5$, $\frac{1}{5} = 0.2$, $\frac{1}{8} = 0.125$ | $\frac{1}{3} = 0.\overline{3}$, $\frac{1}{7} = 0.\overline{142857}$ |
| **Base 2** | Binary | $\{2\}$ | $q = 2^a$ | $\frac{1}{2} = 0.1_2$, $\frac{1}{4} = 0.01_2$, $\frac{1}{8} = 0.001_2$ | **$\frac{1}{10} = 0.000110011\dots_2$**, **$\frac{1}{5} = 0.00110011\dots_2$** |
| **Base 16** | Hexadecimal | $\{2\}$ | $q = 2^a$ (since $16 = 2^4$) | $\frac{1}{2} = 0.8_{16}$, $\frac{1}{4} = 0.4_{16}$, $\frac{1}{16} = 0.1_{16}$ | **$\frac{1}{10} = 0.199999\dots_{16}$**, $\frac{1}{5} = 0.3333\dots_{16}$ |
| **Base 12** | Duodecimal | $\{2, 3\}$ | $q = 2^a \cdot 3^b$ | $\frac{1}{2} = 0.6_{12}$, $\frac{1}{3} = 0.4_{12}$, $\frac{1}{4} = 0.3_{12}$, $\frac{1}{6} = 0.2_{12}$ | $\frac{1}{5} = 0.\overline{2497}_{12}$ |

---

### 3. Binary & Floating-Point Computer Arithmetic Implication

#### The IEEE 754 Floating-Point Paradox
Computers use binary (Base 2) representation (IEEE 754 Standard).
Since $\operatorname{prime\_factors}(2) = \{2\}$:
- Only fractions with denominators $q = 2^a$ can be stored with exact precision in binary.
- The simple decimal number **$0.1 = \frac{1}{10}$** has denominator $10 = 2 \times 5$.
- Because $5 \nmid 2$, **$0.1$ CANNOT be represented exactly in binary or IEEE 754 floating-point numbers!**

#### Derivation of $0.1_{10}$ in Binary:
$$\frac{1}{10} = 0.0001100110011\dots_2 = 0.00\overline{0110}_2$$

When IEEE 754 double precision rounds this infinite binary fraction to 53 bits of mantissa, it produces:
$$0.1000000000000000055511151231257827021181583404541015625$$

This explains the famous software behavior:
$$0.1 + 0.2 \neq 0.3 \quad (\text{in Python/JS: } 0.1 + 0.2 = 0.30000000000000004)$$

---

## Linked Practice Questions

- [[cds/math/notes/questions/q_dec1|Q1: Converting Pure Recurring Decimal 0.232323...]]

---

## Navigation
- [[cds/math/notes/subtopics/recurring_decimals|Subtopic: Decimal Fractions & Recurring Decimals]]
- [[cds/math/notes/decimals|Chapter 4: Decimal Fractions]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
