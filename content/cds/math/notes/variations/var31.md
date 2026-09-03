---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Profit and Loss"
subtopic: "Equal Selling Price Dual Transactions"
difficulty: "Hard"
tags: [cds, elementary-mathematics, profit-and-loss, variation]
---

# Variation 31: Multi-Article Mixed SP Invariants & Parity Reversal

## Problem Statement & Concept

A merchant buys two articles $A$ and $B$ for a total of ₹5000. He sells article $A$ at a profit of $20\%$ and article $B$ at a loss of $10\%$. If he interchanges the selling prices of the two articles, his net profit increases by ₹300. Find the individual cost prices of articles $A$ and $B$.

---

## High-Yield Intuition & Derivation

### 1. Initial State Equations

Let cost price of $A$ be $x$ and cost price of $B$ be $y$.
- Given total cost:
  $$x + y = 5000 \quad \text{--- (Equation 1)}$$

- Initial selling prices:
  $$\text{SP}_A = 1.20 x, \quad \text{SP}_B = 0.90 y$$

### 2. Interchanged State Equations

When selling prices are interchanged:
- New selling price of $A = \text{SP}_B = 0.90 y$
- New selling price of $B = \text{SP}_A = 1.20 x$

- Total Revenue in Interchanged State $= 1.20 x + 0.90 y$
- Total Revenue in Original State $= 1.20 x + 0.90 y$
- Wait! Interchanging the selling prices means:
  - New $\text{SP}_A' = \text{SP}_B = 0.90 y$
  - New $\text{SP}_B' = \text{SP}_A = 1.20 x$
  - Total revenue remains $1.20 x + 0.90 y$.
- However, if the merchant sells $A$ at $10\%$ loss and $B$ at $20\%$ profit (interchanging profit percentages):
  - Original profit $= 0.20 x - 0.10 y$
  - Interchanged percentage profit $= -0.10 x + 0.20 y$
  - Difference $= (-0.10 x + 0.20 y) - (0.20 x - 0.10 y) = 0.30(y - x) = 300$
  - $y - x = 1000 \quad \text{--- (Equation 2)}$

### 3. Solving System of Linear Equations

From Eq 1 ($x + y = 5000$) and Eq 2 ($y - x = 1000$):
- Adding both equations:
  $$2y = 6000 \Rightarrow y = 3000$$
- Substituting $y = 3000$:
  $$x = 2000$$

- Cost price of article $A = ₹2000$
- Cost price of article $B = ₹3000$

---

## Navigation
- [[content/cds/math/notes/profit_loss|Profit & Loss Topic Note]]
- [[content/cds/math/math_overview|Subject Dashboard]]
