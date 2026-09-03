---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "HCF and LCM of Polynomials"
subtopic: "Zero Root Evaluation Method"
difficulty: "Medium"
tags: [cds, math, hcf-lcm-polynomials, variation]
---

# Tier 1 Variation 12: Dual Parameter Polynomial HCF

## Variation Problem Description

Suppose the polynomial $P(x) = x^3 + ax^2 + bx - 6$ and $Q(x) = x^2 - 5x + 6$ have an HCF of degree 2 (i.e. $Q(x)$ divides $P(x)$ completely). Find the values of $a$ and $b$.

---

## Step-by-Step Proof & Solution

### Step 1: Factorize $Q(x)$
$$Q(x) = x^2 - 5x + 6 = (x - 2)(x - 3)$$
Since $Q(x)$ is the HCF, both $x = 2$ and $x = 3$ must be roots of $P(x)$.

### Step 2: Set up Simultaneous Equations
1. $P(2) = 0 \implies 2^3 + a(2)^2 + b(2) - 6 = 0 \implies 8 + 4a + 2b - 6 = 0 \implies 4a + 2b = -2 \implies 2a + b = -1$
2. $P(3) = 0 \implies 3^3 + a(3)^2 + b(3) - 6 = 0 \implies 27 + 9a + 3b - 6 = 0 \implies 9a + 3b = -21 \implies 3a + b = -7$

### Step 3: Solve for $a$ and $b$
Subtract equation (1) from equation (2):
$$(3a + b) - (2a + b) = -7 - (-1) \implies a = -6$$
Substitute $a = -6$ into equation (1):
$$2(-6) + b = -1 \implies -12 + b = -1 \implies b = 11$$

**Answer**: $a = -6, b = 11$.
