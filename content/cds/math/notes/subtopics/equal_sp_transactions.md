---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Profit and Loss"
subtopic: "Equal Selling Price Dual Transactions"
difficulty: "Hard"
tags: [cds, elementary-mathematics, profit-and-loss, subtopic]
---

# Equal Selling Price Dual Transactions

## Theory & Mathematical Formulation

Dual-article transactions where the selling prices of two distinct articles are identical ($\text{SP}_1 = \text{SP}_2 = \text{SP}$) present classic exam traps.

### Case 1: Identical Gain and Loss Percentages ($x\%$ profit and $x\%$ loss)

When two articles are sold at the same selling price, one at a gain of $x\%$ and the other at a loss of $x\%$:

1. **Overall Net Invariant**:
   - There is **ALWAYS an overall loss** in the combined transaction.
   - The overall loss percentage is given by:
     $$\text{Overall Loss } \% = \left( \frac{x}{10} \right)^2 \% = \frac{x^2}{100} \% $$

2. **Mathematical Proof**:
   - Let individual cost prices be $\text{CP}_1$ and $\text{CP}_2$.
   - Since $\text{SP}_1 = \text{SP}_2 = \text{SP}$:
     $$\text{CP}_1 = \frac{100 \cdot \text{SP}}{100 + x}, \quad \text{CP}_2 = \frac{100 \cdot \text{SP}}{100 - x}$$
   - Total Cost Price:
     $$\text{CP}_{\text{total}} = 100 \cdot \text{SP} \left( \frac{1}{100 + x} + \frac{1}{100 - x} \right) = \frac{20000 \cdot \text{SP}}{10000 - x^2}$$
   - Total Selling Price:
     $$\text{SP}_{\text{total}} = 2 \cdot \text{SP}$$
   - Net Loss Ratio:
     $$\frac{\text{CP}_{\text{total}} - \text{SP}_{\text{total}}}{\text{CP}_{\text{total}}} = \frac{\frac{20000}{10000 - x^2} - 2}{\frac{20000}{10000 - x^2}} = \frac{x^2}{10000} = \frac{x^2}{100}\%$$

### Case 2: Asymmetric Gain $x\%$ and Loss $y\%$ (Equal Selling Price)

1. **Overall Net Percentage Formula**:
   $$\text{Net } \% = \frac{100(x - y) - 2xy}{200 + x - y}$$
   - Positive result $\Rightarrow$ Gain $\%$.
   - Negative result $\Rightarrow$ Loss $\%$.

2. **Cost Price Splitting Theorem**:
   - Total Cost of two items = $S$. One sold at loss $r\%$, other at gain $R\%$ with equal selling prices:
     $$\text{CP}_{\text{loss}} = S \times \frac{100 + R}{(100 - r) + (100 + R)}$$
     $$\text{CP}_{\text{gain}} = S \times \frac{100 - r}{(100 - r) + (100 + R)}$$

---

## Linked Practice Questions
- [[cds/math/notes/questions/q11_4|Q11.4: Dual Vehicle Sale with Symmetric Profit/Loss]]
- [[cds/math/notes/questions/q11_5|Q11.5: Asymmetric Dual Sale with Constant Selling Price]]

---

## Navigation
- [[cds/math/notes/profit_loss|Profit & Loss Topic Note]]
- [[cds/math/math_overview|Subject Dashboard]]
