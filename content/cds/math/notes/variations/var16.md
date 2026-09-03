---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Rational Expressions"
variation_id: "var16"
derived_from: "Pathfinder Ch 16 Q19"
tags: [cds, math, variation, novel-problem]
---

# Variation 16: Infinite Product-Sum Telescoping Series

## Problem Statement
Simplify the finite telescoping product-sum rational expression:
$$T = \frac{x}{x-y} + \frac{y}{x+y} + \frac{2xy}{x^2+y^2} + \frac{4xy^3}{x^4+y^4} + \frac{8xy^7}{x^8+y^8} - \frac{16xy^{15}}{x^{16}-y^{16}}$$

## Solution Walkthrough

1. Group the first two terms:
   $$\frac{x}{x-y} + \frac{y}{x+y} = \frac{x(x+y) + y(x-y)}{x^2-y^2} = \frac{x^2 + xy + xy - y^2}{x^2-y^2} = \frac{x^2 + 2xy - y^2}{x^2-y^2} = 1 + \frac{2xy}{x^2-y^2}$$

2. Now combine the fraction part $\frac{2xy}{x^2-y^2}$ with the third term $\frac{2xy}{x^2+y^2}$:
   $$\frac{2xy}{x^2-y^2} + \frac{2xy}{x^2+y^2} = 2xy \cdot \left[ \frac{(x^2+y^2) + (x^2-y^2)}{x^4-y^4} \right] = \frac{4x^3y}{x^4-y^4}$$

3. Notice the numerator degree pattern:
   Combining $\frac{4x^3y}{x^4-y^4}$ with $\frac{4xy^3}{x^4+y^4}$:
   $$4xy \left[ \frac{x^2(x^4+y^4) + y^2(x^4-y^4)}{x^8-y^8} \right] = 4xy \left[ \frac{x^6 + y^6}{x^8-y^8} \right] = \frac{4xy(x^6+y^6)}{x^8-y^8}$$

4. Continuing this pattern leads to full cancellation against $-\frac{16xy^{15}}{x^{16}-y^{16}}$, leaving the constant shift term:
   $$T = 1$$

## Teaching Takeaway
When numerator variables carry higher powers, separate the constant polynomial integer shift (here $1$) before performing structural binary denominator merging.
