---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Rational Expressions"
archetype: "System Symmetric Elimination"
source: "Pathfinder Chapter 16 Q20 (CDS 2016 I)"
tags: [cds, math, rational-expressions, question, pyq]
---

# Question 20 (CDS 2016 I - Pathfinder Ch 16)

## Problem Statement
If $a - by^2 - cz^2 = 0$, $ax^2 - b + cz^2 = 0$, and $ax^2 + by^2 - c = 0$, find the value of:
$$\frac{x^2}{a+x^2} + \frac{y^2}{b+y^2} + \frac{z^2}{c+z^2}$$

## Method & Solution

1. Rewrite the system of equations:
   $$\begin{cases}
   by^2 + cz^2 = a \quad \implies \text{Add } ax^2 \text{ to both sides:} \quad ax^2 + by^2 + cz^2 = a + ax^2 = a(1+x^2) \\
   ax^2 + cz^2 = b \quad \implies \text{Add } by^2 \text{ to both sides:} \quad ax^2 + by^2 + cz^2 = b(1+y^2) \\
   ax^2 + by^2 = c \quad \implies \text{Add } cz^2 \text{ to both sides:} \quad ax^2 + by^2 + cz^2 = c(1+z^2)
   \end{cases}$$

2. Let $S = ax^2 + by^2 + cz^2$. Then:
   $$1+x^2 = \frac{S}{a} \implies \frac{x^2}{1+x^2} = 1 - \frac{1}{1+x^2} = 1 - \frac{a}{S} = \frac{S-a}{S}$$
   Similarly:
   $$\frac{y^2}{1+y^2} = \frac{S-b}{S}, \quad \frac{z^2}{1+z^2} = \frac{S-c}{S}$$

3. Sum the three terms:
   $$\text{Target} = \frac{(S-a) + (S-b) + (S-c)}{S} = \frac{3S - (a+b+c)}{S}$$

4. From adding all three original equations:
   $$(by^2+cz^2) + (ax^2+cz^2) + (ax^2+by^2) = a+b+c \implies 2(ax^2+by^2+cz^2) = a+b+c \implies 2S = a+b+c$$

5. Substitute $a+b+c = 2S$:
   $$\text{Target} = \frac{3S - 2S}{S} = \frac{S}{S} = 1$$

## Teaching Takeaway
System symmetry allows summing all equations to find the global invariant $S = ax^2 + by^2 + cz^2 = \frac{a+b+c}{2}$. Expressing each variable ratio in terms of $S$ yields an instant reduction to $1$.
