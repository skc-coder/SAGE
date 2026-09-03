---
exam: "CDS"
subject: "Math"
topic: "Formulas"
difficulty: "Easy"
tags: [cds, math, formulas]
---

# Formulas

## Arithmetic Progression (AP)

### 1. General Term ($n$-th term)
$$a_n = a + (n - 1)d$$
- $a$: First term
- $d$: Common difference ($a_k - a_{k-1}$)
- $n$: Number of terms

### 2. Sum of First $n$ Terms ($S_n$)
$$S_n = \frac{n}{2} [2a + (n - 1)d] = \frac{n}{2} (a + l)$$
- $l$: Last term ($a_n$)

### 3. Arithmetic Mean (AM)
For two numbers $A$ and $B$:
$$\text{AM} = \frac{A + B}{2}$$

---

## Geometric Progression (GP)

### 1. General Term ($n$-th term)
$$t_n = a \cdot r^{n - 1}$$
- $a$: First term
- $r$: Common ratio ($\frac{t_k}{t_{k-1}}$)

### 2. Sum of First $n$ Terms ($S_n$)
- When $r \neq 1$:
  $$S_n = \frac{a(r^n - 1)}{r - 1} \quad \text{if } r > 1$$
  $$S_n = \frac{a(1 - r^n)}{1 - r} \quad \text{if } r < 1$$

### 3. Sum of Infinite GP ($S_\infty$)
- Valid when $|r| < 1$:
  $$S_\infty = \frac{a}{1 - r}$$

### 4. Geometric Mean (GM)
For two positive numbers $A$ and $B$:
$$\text{GM} = \sqrt{A \cdot B}$$

---

## Harmonic Progression (HP)

### 1. Definition
A sequence $a_1, a_2, a_3, \dots$ is in HP if its reciprocals $\frac{1}{a_1}, \frac{1}{a_2}, \frac{1}{a_3}, \dots$ are in AP.

### 2. Harmonic Mean (HM)
For two positive numbers $A$ and $B$:
$$\text{HM} = \frac{2AB}{A + B}$$

---

## AM-GM-HM Inequality
For any positive real numbers:
$$\text{AM} \ge \text{GM} \ge \text{HM}$$
$$\frac{A + B}{2} \ge \sqrt{AB} \ge \frac{2AB}{A + B}$$
*(Equality holds when $A = B$)*

---

## Important Summations

1. Sum of first $n$ natural numbers:
   $$\sum_{k=1}^n k = \frac{n(n+1)}{2}$$

2. Sum of squares of first $n$ natural numbers:
   $$\sum_{k=1}^n k^2 = \frac{n(n+1)(2n+1)}{6}$$

3. Sum of cubes of first $n$ natural numbers:
   $$\sum_{k=1}^n k^3 = \left[ \frac{n(n+1)}{2} \right]^2$$

## Navigation

- [[cds/math/math_overview|Elementary Mathematics Overview]]
