---
exam: "CDS"
subject: "Math"
topic: "Numbers, HCF & LCM"
difficulty: "Medium"
tags: [cds, math, variations]
---

# Topic Variations

## Tier 1 & Tier 2 Variations

### Variation 1: Continuous Ratio Substitution
If $\frac{x}{3} = \frac{y}{7} = \frac{z}{11} = \frac{w}{15}$, find the value of $\frac{2x + 3y + z}{w - y}$.

- **User Answer**: (b) $4.75$ — **CORRECT!**

> [!faq]- View Solution
> Direct substitution: $x=3, y=7, z=11, w=15$.
> $$\frac{2(3) + 3(7) + 11}{15 - 7} = \frac{6 + 21 + 11}{8} = \frac{38}{8} = 4.75$$

---

### Variation 2: Weighted Addendo Property
If $\frac{a}{2} = \frac{b}{3} = \frac{c}{5}$, then the value of $\frac{3a - 2b + 4c}{3(2) - 2(3) + 4(5)}$ is equal to:

- **User Answer**: (a) $\frac{a}{2}$ — **CORRECT!**

> [!faq]- View Solution
> By Weighted Addendo Property:
> $$\frac{3a - 2b + 4c}{3(2) - 2(3) + 4(5)} = \frac{a}{2} = \frac{b}{3} = \frac{c}{5} = k$$

---

### Variation 3: Homogeneous Quadratic Ratio
If $\frac{p}{3} = \frac{q}{4} = \frac{r}{5}$, calculate the value of $\frac{p^2 + q^2 + r^2}{pq + qr}$.

- **User Answer**: (c) $\frac{50}{32} = \frac{25}{16}$ — **CORRECT!**

> [!faq]- View Solution
> Direct substitution: $p=3, q=4, r=5$.
> $$\frac{3^2 + 4^2 + 5^2}{(3)(4) + (4)(5)} = \frac{9 + 16 + 25}{12 + 20} = \frac{50}{32} = \frac{25}{16}$$

---

### Variation 4: Divisibility of 3-Digit Repeated Number (1001 Principle)
A 6-digit number formed by repeating a 3-digit number (e.g. $abcabc$) is always divisible by:

- **User Answer**: (d) All of 7, 11, and 13 — **CORRECT!**

> [!faq]- View Solution
> $abcabc = abc \times 1000 + abc = abc(1000 + 1) = abc \times 1001$.
> Since $1001 = 7 \times 11 \times 13$, $abcabc$ is always divisible by 7, 11, and 13.

---

### Variation 5: Divisibility of $562k984$ by 13
If $562k984$ is divisible by 13, find digit $k$.

- **Correct Answer**: (c) 7

> [!faq]- View Solution
> 3-digit grouping from right: $G_0 = 984$, $G_1 = 62k = 620 + k$, $G_2 = 5$.
> Alternating sum:
> $$\text{Diff} = 984 - (620 + k) + 5 = 369 - k$$
> Test $369 - k \pmod{13}$:
> $369 = 13 \times 28 + 5 \implies 369 \equiv 5 \pmod{13}$.
> Thus $5 - k \equiv 0 \pmod{13} \implies k = 5$.

---

### Variation 6: Repunit Remainder Modulo 13
What is the remainder when $N = \underbrace{777\dots777}_{30 \text{ times}}$ is divided by 13?

- **Correct Answer**: (a) 0

> [!faq]- View Solution
> Any 6-digit repeated block $777777 = 777 \times 1001$, which is divisible by 13.
> Since 30 digits = 5 complete blocks of 6 digits ($30 = 6 \times 5$), the entire 30-digit number is perfectly divisible by 13. Remainder = 0.

---

### Variation 7: AP Sum with Dual Remainders
Find the sum of all 2-digit numbers leaving remainder 3 when divided by 5 and remainder 1 when divided by 4.

> [!faq]- View Solution
> First term $a \equiv 3 \pmod 5$ and $a \equiv 1 \pmod 4$:
> - Check mod 4 on numbers $\equiv 3 \pmod 5$: $3, 8, 13, 18, \dots$
> - $13 \equiv 1 \pmod 4 \implies a = 13$.
> Common difference $d = \operatorname{LCM}(5, 4) = 20$.
> AP terms < 100: $13, 33, 53, 73, 93$ ($n = 5$).
> $$S_5 = \frac{5}{2}(13 + 93) = \frac{5}{2}(106) = 5 \times 53 = 265$$

---

### Variation 8: HCF via Successive Quotients
In finding the HCF of two numbers by division method, the successive quotients from top to bottom are 1, 8, and 2. If the last divisor is 105, find the two numbers.

> [!faq]- View Solution
> Work backwards using Euclidean algorithm steps:
> 1. Last divisor $d_3 = 105$, quotient $q_3 = 2 \implies \text{Dividend } r_1 = 105 \times 2 + 0 = 210$.
> 2. Second divisor $d_2 = 210$, quotient $q_2 = 8 \implies \text{Dividend } B = 210 \times 8 + 105 = 1680 + 105 = 1785$.
> 3. First divisor $d_1 = 1785$, quotient $q_1 = 1 \implies \text{Dividend } A = 1785 \times 1 + 210 = 1995$.
> 
> Thus, the two numbers are **1785 and 1995**.

---

### Variation 9: Co-prime Pairs Given Product and HCF
The product of two numbers is 4107. If the HCF of these numbers is 37, find the greater number.

> [!faq]- View Solution
> Let numbers be $A = 37x$ and $B = 37y$ with $\operatorname{GCD}(x, y) = 1$.
> $$37x \times 37y = 4107 \implies 1369 (x \cdot y) = 4107 \implies x \cdot y = 3$$
> Co-prime pairs for $x \cdot y = 3$ are $(1, 3)$.
> Greater number $B = 37 \times 3 = 111$.

---

### Variation 10: Largest 4-Digit Number with Constant Remainder
Find the greatest 4-digit number which when divided by 12, 18, 21, and 28 leaves a remainder of 3 in each case.

> [!faq]- View Solution
> 1. $\operatorname{LCM}(12, 18, 21, 28) = 252$.
> 2. Greatest 4-digit number = 9999.
> 3. Divide 9999 by 252: $9999 = 252 \times 39 + 171 \implies \text{Remainder } 171$.
> 4. Largest multiple of 252 under 10000 = $9999 - 171 = 9828$.
> 5. Add constant remainder 3: $N = 9828 + 3 = 9831$.

---

### Variation 11: Smallest 4-Digit Number with Constant Difference
Find the smallest 4-digit number which when divided by 6, 7, 8, and 9 leaves remainders 4, 5, 6, and 7 respectively.

> [!faq]- View Solution
> 1. Constant difference $p = (6-4) = (7-5) = (8-6) = (9-7) = 2$.
> 2. $\operatorname{LCM}(6, 7, 8, 9) = 504$.
> 3. Smallest 4-digit multiple of 504: $504 \times 2 = 1008$.
> 4. Subtract constant difference 2: $N = 1008 - 2 = 1006$.

---

## Navigation

- [[cds/math/math_overview|Elementary Mathematics Overview]]
