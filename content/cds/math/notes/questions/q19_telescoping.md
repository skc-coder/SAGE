---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Rational Expressions"
archetype: "Telescoping Power Series"
source: "Pathfinder Chapter 16 Q19 (CDS 2014 II)"
tags: [cds, math, rational-expressions, question, pyq]
---

# Question 19 (CDS 2014 II - Pathfinder Ch 16)

## Problem Statement
Simplify the expression:
$$S = \frac{1}{a-b} - \frac{1}{a+b} - \frac{2b}{a^2+b^2} - \frac{4b^3}{a^4+b^4} - \frac{8b^7}{a^8-b^8}$$

## Method & Solution
Combine terms sequentially from left to right using difference of squares $(a^k - b^k)(a^k + b^k) = a^{2k} - b^{2k}$:

1. First pair:
   $$\frac{1}{a-b} - \frac{1}{a+b} = \frac{(a+b) - (a-b)}{a^2 - b^2} = \frac{2b}{a^2-b^2}$$

2. Combine with 3rd term:
   $$\frac{2b}{a^2-b^2} - \frac{2b}{a^2+b^2} = 2b \cdot \left[ \frac{(a^2+b^2) - (a^2-b^2)}{a^4-b^4} \right] = \frac{4b^3}{a^4-b^4}$$

3. Combine with 4th term:
   $$\frac{4b^3}{a^4-b^4} - \frac{4b^3}{a^4+b^4} = 4b^3 \cdot \left[ \frac{(a^4+b^4) - (a^4-b^4)}{a^8-b^8} \right] = \frac{8b^7}{a^8-b^8}$$

4. Final subtraction with 5th term:
   $$\frac{8b^7}{a^8-b^8} - \frac{8b^7}{a^8-b^8} = 0$$

## Teaching Takeaway
When terms have powers of $2$ in exponents ($1, 2, 4, 8$) and alternating $+/-$ denominators, merge sequentially from the lowest power. The denominator automatically doubles its degree at each step.
