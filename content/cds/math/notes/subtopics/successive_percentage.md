---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Percentage"
subtopic: "Successive Percentage & Net Change"
difficulty: "Medium"
tags: [cds, math, percentage, subtopic, successive]
---

# Successive Percentage & Net Change

## Theory & Proofs

### 1. Algebraic Derivation of Net Change Formula
Let initial value be $V_0$.
- First change by $a\%$:
  $$V_1 = V_0 \left(1 + \frac{a}{100}\right)$$
- Second change by $b\%$:
  $$V_2 = V_1 \left(1 + \frac{b}{100}\right) = V_0 \left(1 + \frac{a}{100}\right)\left(1 + \frac{b}{100}\right)$$
- Expanding the product:
  $$V_2 = V_0 \left(1 + \frac{a}{100} + \frac{b}{100} + \frac{a \cdot b}{10000}\right) = V_0 \left[1 + \frac{1}{100}\left(a + b + \frac{ab}{100}\right)\right]$$
- Therefore, overall fractional change is $\frac{V_2 - V_0}{V_0} = \frac{1}{100}\left(a + b + \frac{ab}{100}\right)$.
- Multiplying by $100\%$, net percentage change is:
  $$\text{Net Change \%} = a + b + \frac{a \cdot b}{100}$$

### 2. Equal Percentage Increase and Decrease ($+x\%$ and $-x\%$)
When an item increases by $x\%$ and then decreases by $x\%$:
$$\text{Net Change \%} = x - x + \frac{x(-x)}{100} = -\frac{x^2}{100}\%$$
- There is **always a net loss/decrease** equal to $\frac{x^2}{100}\%$.

---

## Linked Practice Questions

- [[cds/math/notes/questions/q151|Q151: Sequential Increase and Decrease Net Percentage Change]]

---

## Variations

- [[cds/math/notes/variations/var28|Successive Price Increase and Decrease Net Effect]]
