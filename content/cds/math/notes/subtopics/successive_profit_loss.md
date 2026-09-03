---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Profit and Loss"
subtopic: "Successive Profit and Loss"
difficulty: "Medium"
tags: [cds, elementary-mathematics, profit-and-loss, subtopic]
---

# Successive Profit and Loss

## Theory & Mathematical Formulation

When an article undergoes sequential percentage transactions (or multiple traders resell an item sequentially with profits $x\%$ and $y\%$), the net effective change is governed by compounding multipliers rather than simple addition.

### 1. Two-Stage Net Percentage Formula
- For two successive profit/loss changes $x\%$ and $y\%$ (where profit is positive and loss is negative):
  $$\text{Net } \% \text{ Change} = x + y + \frac{xy}{100}$$
- **Interpretation**:
  - Positive net result $\Rightarrow$ overall profit.
  - Negative net result $\Rightarrow$ overall loss.

### 2. Multi-Trader Sequential Resale Chain
- If Trader 1 buys at $\text{CP}_1$ and sells to Trader 2 at profit $p_1\%$, and Trader 2 sells to Trader 3 at profit $p_2\%$:
  $$\text{Final Price } (\text{CP}_3) = \text{CP}_1 \times \left(1 + \frac{p_1}{100}\right) \times \left(1 + \frac{p_2}{100}\right)$$

---

## Linked Practice Questions
- [[cds/math/notes/questions/q11_3|Q11.3: Resale Chain between Sequential Traders]]

---

## Navigation
- [[cds/math/notes/profit_loss|Profit & Loss Topic Note]]
- [[cds/math/math_overview|Subject Dashboard]]
