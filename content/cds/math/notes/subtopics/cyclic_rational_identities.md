---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Rational Expressions"
subtopic: "Cyclic Rational Identities"
tags: [cds, math, cyclic-identities, algebra]
---

# Cyclic Rational Identities & Symmetric Systems

## 1. System of 3 Linear Symmetric Rational Equations

Given a system of symmetric linear equations:

$$ax - by - cz = 0$$
$$-ax + by - cz = 0$$

### Example Architecture (Pathfinder Q20 Model):

$$a - by^2 - cz^2 = 0$$
$$ax^2 - b + cz^2 = 0$$
$$ax^2 + by^2 - c = 0$$

Summing all three equations:

$$(2ax^2 - a) + (2by^2 - b) + (2cz^2 - c) = 0 \implies 2(ax^2 + by^2 + cz^2) = a + b + c$$

Solving for single variables yields:

$$\frac{x^2}{a + x^2} = \frac{a}{a+b+c} \quad \text{or} \quad \frac{x}{a+x} + \frac{y}{b+y} + \frac{z}{c+z} = 1$$

> **Related Questions & Variations**:
> * [[cds/math/notes/questions/q20_system|Question 20 (CDS 2016 I - Pathfinder Ch 16)]]

---

## 2. Cyclic Sum of Products (Condition $pq + qr + rp = 0$)

When $pq + qr + rp = 0$, substitute $qr = -pq - rp = -p(q+r)$:

$$\frac{p}{p^2 - qr} = \frac{p}{p^2 - (-pq - rp)} = \frac{p}{p(p + q + r)} = \frac{1}{p+q+r}$$

Thus the sum across all three variables:

$$\frac{p}{p^2 - qr} + \frac{q}{q^2 - rp} + \frac{r}{r^2 - pq} = \frac{1}{p+q+r} + \frac{1}{p+q+r} + \frac{1}{p+q+r} = \frac{p+q+r}{p+q+r} = 1$$
