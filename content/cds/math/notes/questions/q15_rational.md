---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Rational Expressions"
archetype: "Shifted Constant Sum"
source: "Pathfinder Chapter 16 Q15"
tags: [cds, math, rational-expressions, question]
---

# Question 15 (Pathfinder Ch 16)

## Problem Statement
If:
$$\frac{1}{x+1} + \frac{2}{y+2} + \frac{1009}{z+1009} = 1$$

What is the value of:
$$\frac{x}{x+1} + \frac{y}{y+2} + \frac{z}{z+1009}$$

## Method & Solution
Using the linear complement identity $\frac{v}{v+k} = 1 - \frac{k}{v+k}$:

1. Rewrite each term of the target expression:
   $$\frac{x}{x+1} = 1 - \frac{1}{x+1}$$
   $$\frac{y}{y+2} = 1 - \frac{2}{y+2}$$
   $$\frac{z}{z+1009} = 1 - \frac{1009}{z+1009}$$

2. Sum the three expressions:
   $$\frac{x}{x+1} + \frac{y}{y+2} + \frac{z}{z+1009} = (1 + 1 + 1) - \left( \frac{1}{x+1} + \frac{2}{y+2} + \frac{1009}{z+1009} \right)$$

3. Substitute the given condition:
   $$\text{Target} = 3 - 1 = 2$$

## Teaching Takeaway
Never attempt to solve for individual variables $(x, y, z)$ in an underdetermined system with fewer equations than variables. Look for complementary variable transformations $\frac{x}{x+k} + \frac{k}{x+k} = 1$.
