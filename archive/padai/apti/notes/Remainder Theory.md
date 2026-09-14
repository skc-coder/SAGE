## Basics

**Divisor Reduction Rule:** If $N \div d_1$ gives remainder $r$, and $d_2$ is a factor of $d_1$:
- Remainder when $N \div d_2$ = $r \bmod d_2$
- If $d_2$ is NOT a factor of $d_1$ → Cannot be determined

**Properties:** Additive, subtraction, multiplicative

**Negative Remainder:** Add divisor to get positive equivalent.

---

## Finding Divisor from Remainders

**Problem:** $N \div d$ gives remainder 15. $10N \div d$ gives remainder 6. Find least $d$.

**Solution:**
1. $10N$ has remainder $10 \times 15 = 150$
2. $150 \div d$ gives remainder 6
3. So $d | (150 - 6) = 144$
4. $d > 15$ (divisor > remainder always)
5. Least $d = 16$

---

## Type 2 — $a^n + b^n$ divided by $(a+b)$

$$a^n + b^n \equiv 0 \pmod{a+b} \iff n \text{ is odd}$$

$$a^n + b^n \not\equiv 0 \pmod{a+b} \iff n \text{ is even}$$

**Example:** $71^{83} + 73^{83} \div 36$

$71 \equiv -1 \pmod{36}$, $73 \equiv +1 \pmod{36}$

$$(-1)^{83} + (1)^{83} = -1 + 1 = 0$$

Remainder = **0**

---

## Type 3 — Polynomial Remainder (Factor Theorem)

Remainder of $f(m) \div (m + k)$ = $f(-k)$

**Example:** $m^{12} - 1 \div (m + 1)$

Set $m = -1$: $(-1)^{12} - 1 = 0$

Remainder = **0**

---

## HCF Type — Same Remainder for All Numbers

**Rule:** HCF$(n_1 - r, n_2 - r, n_3 - r)$ or HCF of pairwise differences

**Example:** Greatest number dividing 156, 181, 331 each leaving remainder 6.

$$156 - 6 = 150, \quad 181 - 6 = 175, \quad 331 - 6 = 325$$

$$\text{HCF}(150, 175, 325) = 25$$

Answer = **25**

---

## LCM Type — Same Remainder for All Numbers

**Steps:**
1. Find LCM of divisors
2. Find multiple of LCM in range
3. Add remainder

**Example:** Greatest 6-digit number divisible by 16, 24, 72, 84 leaving remainder 15.

$$\text{LCM}(16, 24, 72, 84) = 1008$$

$$\text{Greatest 6-digit multiple} = 1008 \times 99 = 99792$$

$$99792 + 15 = 99807$$

---

## Successive Division

**Finding Least Number:** Work backwards from last quotient (usually 0).

$$N = (Q_{prev} \times d) + r$$

**Example:** Divisors: 3, 4, 7 | Remainders: 2, 3, 5

- $(0 \times 7) + 5 = 5$
- $(5 \times 4) + 3 = 23$
- $(23 \times 3) + 2 = 71$

Smallest $N = 71$

**General Form:** $$N = \text{LCM}(d_1, d_2, \dots) \cdot k + N_{min}$$

---

## Constant Difference Concept

If $d_1 - r_1 = d_2 - r_2 = d_3 - r_3 = K$ (constant):

$$N = \text{LCM}(d_1, d_2, d_3, \dots) \cdot k - K$$

**Example:** Divisors: 36, 72, 80, 88 | Remainders: 16, 52, 60, 68

$36 - 16 = 20$, $72 - 52 = 20$ ... ($K = 20$)

$$N = \text{LCM}(36, 72, 80, 88) - 20$$

---

## Digital Sum & Divisibility by 9

$$N \bmod 9 = (\text{Sum of Digits}) \bmod 9$$

**Use:** If divisor is multiple of 9, find remainder to quickly get digital sum.

---

## Factorials and Remainders

Find point where $m!$ becomes divisible by $X$. All terms after $m!$ have remainder 0.

**Example:** $(1! + 2! + 3! + \dots + n!) \bmod 15$

- $1! = 1$
- $2! = 2$
- $3! = 6$
- $4! = 24$
- $5! = 120$ (divisible by 15)

Sum = $1 + 2 + 6 + 24 = 33$

$$33 \bmod 15 = 3$$

---

## Key Formulas

- **Successive Divisor:** If $N \bmod A = R$ and $B | A$, then $N \bmod B = R \bmod B$

- **Odd Power:** $a^n + b^n \equiv 0 \pmod{a+b}$ if $n$ is odd