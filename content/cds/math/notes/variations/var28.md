---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Percentage"
subtopic: "Successive Percentage & Net Change"
difficulty: "Medium"
tags: [cds, math, percentage, variation]
---

# Variation 28: Successive Price Increase and Decrease Net Effect

## Problem Statement
An item's price is increased by $x\%$ and subsequently decreased by $x\%$. Prove that the final price is strictly less than the original price by $\frac{x^2}{100}\%$.

---

## Proof & Theoretical Intuition

### 1. Algebraic Derivation
Let initial price be $P_0$.
- Price after $x\%$ increase:
  $$P_1 = P_0 \left(1 + \frac{x}{100}\right)$$
- Price after $x\%$ decrease:
  $$P_2 = P_1 \left(1 - \frac{x}{100}\right) = P_0 \left(1 + \frac{x}{100}\right)\left(1 - \frac{x}{100}\right)$$
- Using difference of squares $(1+a)(1-a) = 1 - a^2$:
  $$P_2 = P_0 \left(1 - \frac{x^2}{10000}\right) = P_0 - P_0 \left(\frac{x^2}{10000}\right)$$
- Net percentage loss:
  $$\text{Loss \%} = \frac{P_0 - P_2}{P_0} \times 100\% = \frac{x^2}{100}\%$$

---

## Linked Practice Questions
- [[cds/math/notes/questions/q151|Q151: Sequential Increase and Decrease Net Percentage Change]]
