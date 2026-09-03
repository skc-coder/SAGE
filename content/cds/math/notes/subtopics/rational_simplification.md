---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Rational Expressions"
subtopic: "Simplification & Telescoping"
tags: [cds, math, simplification, telescoping]
---

# Rational Simplification & Telescoping

## 1. Structural Telescoping in Rational Series

When adding long sequences of rational fractions, look for telescoping cancellation.

### Model 1: Binary Differences ($2^k$ Power Fractions)
Consider the sum:
$$S = \frac{1}{a-b} + \frac{1}{a+b} + \frac{2b}{a^2+b^2} + \frac{4b^3}{a^4+b^4} + \frac{8b^7}{a^8+b^8}$$

* **Step 1**: Combine the first two terms:
  $$\frac{1}{a-b} + \frac{1}{a+b} = \frac{(a+b)+(a-b)}{a^2-b^2} = \frac{2a}{a^2-b^2}$$
* **Step 2**: If the next term is $-\frac{2b}{a^2-b^2}$ or similar, combine sequentially using $a^{2k}-b^{2k}$ identity.
* **Step 3**: The series collapses term-by-term into a single irreducible fraction.

---

## 2. Rational Shift Transformation

When given a rational relation like:
$$\frac{x}{x+1} + \frac{y}{y+2} + \frac{z}{z+1009} = K$$

To evaluate the shifted form $\frac{1}{x+1} + \frac{2}{y+2} + \frac{1009}{z+1009}$:

> [!TIP] Key Identity
> Use the complement identity:
> $$\frac{x}{x+a} = 1 - \frac{a}{x+a} \implies \frac{a}{x+a} = 1 - \frac{x}{x+a}$$

Summing across all terms transforms the original sum directly into the target expression without solving for individual variables $x, y, z$.
