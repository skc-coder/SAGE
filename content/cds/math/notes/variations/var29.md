---
exam: "CDS"
subject: "Math"
topic: "Sequence and Series"
variation_set: "Chapter 2 Sequence and Series Variations"
difficulty: "Hard"
tags: [cds, math, sequence-series, variations, var29]
---

# Sequence and Series Advanced Exam Variations

## Variation 1: AP Selection Strategy for Odd & Even Terms

### Problem Model
When solving problems involving sum or product of terms in AP:
- For 3 terms in AP: choose $a-d, a, a+d$ (Sum $= 3a$).
- For 4 terms in AP: choose $a-3d, a-d, a+d, a+3d$ (Common difference $= 2d$, Sum $= 4a$).
- For 5 terms in AP: choose $a-2d, a-d, a, a+d, a+2d$ (Sum $= 5a$).

---

## Variation 2: Sum of $n$ Terms as Quadratic in $n$

### Problem Model
If the sum of first $n$ terms of a sequence is $S_n = A n^2 + B n$, prove it is an AP and find $a$ and $d$.

### Step-by-Step Derivation
- $T_n = S_n - S_{n-1}$
  $$T_n = (A n^2 + B n) - [A(n-1)^2 + B(n-1)]$$
  $$T_n = A n^2 + B n - A(n^2 - 2n + 1) - B n + B$$
  $$T_n = 2 A n + (B - A)$$
- First term $a = T_1 = 2A(1) + B - A = A + B$.
- Common difference $d = T_n - T_{n-1} = 2A$.
- **Exam Rule**: If $S_n = A n^2 + B n$, then common difference is always $d = 2A$ (twice the coefficient of $n^2$).

---

## Variation 3: Infinite Geometric Series with Recurring Decimals

### Problem Model
Express recurring decimals as infinite GP sums (e.g., $0.\overline{42} = 0.424242\dots$).

### Step-by-Step Derivation
$$0.424242\dots = \frac{42}{100} + \frac{42}{10000} + \frac{42}{1000000} + \dots$$
This is an infinite GP with $a = \frac{42}{100}$ and $r = \frac{1}{100}$.
$$S_\infty = \frac{a}{1 - r} = \frac{\frac{42}{100}}{1 - \frac{1}{100}} = \frac{\frac{42}{100}}{\frac{99}{100}} = \frac{42}{99} = \frac{14}{33}$$

---

## Variation 4: Inserting $n$ Means Between Two Numbers

### Problem Model
Insert $n$ arithmetic means $M_1, M_2, \dots, M_n$ between $a$ and $b$.

### Step-by-Step Derivation
- Total terms in progression: $n + 2$.
- First term is $a$, last term $(n+2)$-th term is $b$.
  $$b = a + (n + 2 - 1)d = a + (n+1)d \implies d = \frac{b - a}{n + 1}$$
- Sum of $n$ arithmetic means inserted between $a$ and $b$:
  $$\sum_{i=1}^{n} M_i = n \times \left(\frac{a + b}{2}\right)$$
  *(The sum of $n$ AMs between two numbers equals $n$ times the single AM between them!)*
