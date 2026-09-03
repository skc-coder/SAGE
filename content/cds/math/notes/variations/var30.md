---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Profit and Loss"
subtopic: "Dishonest Dealer and False Weights"
difficulty: "Hard"
tags: [cds, elementary-mathematics, profit-and-loss, variation]
---

# Variation 30: Dual-Stage False Weight & Markup Compounding

## Problem Statement & Concept

A trader buys sugar from a wholesaler using a false weight of $1200\text{ g}$ for every $1000\text{ g}$ (cheating by $20\%$ while buying). He then marks up the cost price by $10\%$, allows a discount of $5\%$ to retail customers, and uses a false weight of $900\text{ g}$ for every $1000\text{ g}$ while selling. What is his net overall profit percentage?

---

## High-Yield Intuition & Derivation

### 1. Stage-Wise Multipliers

Let the cost price of $1\text{ g}$ true weight of sugar for the wholesaler be $₹1$.

1. **Buying Stage (Cheating on Purchase)**:
   - Trader pays for $1000\text{ g}$ ($₹1000$), but gets $1200\text{ g}$.
   - Effective Cost Price per gram for trader:
     $$\text{CP}_{\text{effective}} = \frac{1000}{1200} = ₹\frac{5}{6} \text{ per gram}$$

2. **Pricing & Discount Stage (Markup + Discount)**:
   - Price marked per nominal gram $= 1 \times \left(1 + \frac{10}{100}\right) = ₹1.10$.
   - Price charged per nominal gram after $5\%$ discount $= 1.10 \times \left(1 - \frac{5}{100}\right) = 1.10 \times 0.95 = ₹1.045$.

3. **Selling Stage (Cheating on Sale)**:
   - When a customer asks for $1000\text{ g}$, trader charges for $1000\text{ g}$ (i.e. $1000 \times 1.045 = ₹1045$), but delivers only $900\text{ g}$.
   - Actual cost incurred by trader to provide $900\text{ g}$:
     $$\text{Actual Cost} = 900 \times \text{CP}_{\text{effective}} = 900 \times \frac{5}{6} = ₹750$$

### 2. Overall Profit Evaluation

- Revenue received $= ₹1045$
- Total Cost incurred $= ₹750$
- Overall Profit $= 1045 - 750 = ₹295$
- Overall Profit $\% = \frac{295}{750} \times 100\% = \frac{2950}{75} = 39.33\%$

---

## General Invariant Formula

$$\text{Net Multiplier} = \left(\frac{W_{\text{bought\_true}}}{W_{\text{paid\_for}}}\right) \times \left(1 + \frac{m}{100}\right) \times \left(1 - \frac{d}{100}\right) \times \left(\frac{W_{\text{charged\_for}}}{W_{\text{delivered\_false}}}\right)$$

---

## Navigation
- [[content/cds/math/notes/profit_loss|Profit & Loss Topic Note]]
- [[content/cds/math/math_overview|Subject Dashboard]]
