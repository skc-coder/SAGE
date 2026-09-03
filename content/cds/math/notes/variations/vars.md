---
exam: "CDS"
subject: "Math"
topic: "Numbers"
difficulty: "Medium"
tags: [cds, math, variations]
---

# Number System Variations

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
> Thus $5 - k \equiv 0 \pmod{13} \implies k = 5$ or $369 - 7 = 362 = 13 \times 27 + 11$.
> Checking $369 - 5 = 364 = 13 \times 28$ $\implies k=5$.

---

### Variation 6: Repunit Remainder Modulo 13
What is the remainder when $N = \underbrace{777\dots777}_{30 \text{ times}}$ is divided by 13?

- **Correct Answer**: (a) 0

> [!faq]- View Solution
> Any 6-digit repeated block $777777 = 777 \times 1001$, which is divisible by 13.
> Since 30 digits = 5 complete blocks of 6 digits ($30 = 6 \times 5$), the entire 30-digit number is perfectly divisible by 13. Remainder = 0.

## Navigation

- [[cds/math/math_overview|Elementary Mathematics Overview]]
