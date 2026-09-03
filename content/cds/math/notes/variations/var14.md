---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "HCF and LCM of Polynomials"
subtopic: "Zero Root Evaluation Method"
difficulty: "Hard"
tags: [cds, math, hcf-lcm-polynomials, variation]
---

# Tier 3 Variation 14: Difference of Powers Divisibility Identity

## Variation Problem Description

Prove that $(x^2 - y^2)$ is the HCF of $P(x,y) = x^n - y^n$ and $Q(x,y) = x^m - y^m$ if and only if $\operatorname{gcd}(n, m) = 2$ where both $n$ and $m$ are even integers.

---

## Step-by-Step Proof & Solution

### Step 1: General Power Difference Identity
For any positive integers $n, m$:
$$\operatorname{HCF}(x^n - y^n, x^m - y^m) = x^{\operatorname{gcd}(n, m)} - y^{\operatorname{gcd}(n, m)}$$

### Step 2: Proof via Euclidean Algorithm on Exponents
Let $d = \operatorname{gcd}(n, m)$.
By Bezout's identity for integers, there exist integers $a, b$ such that $an + bm = d$.
Applying the polynomial division algorithm on $x^n - y^n$ and $x^m - y^m$ mimics exponent Euclidean division step-by-step:
$$x^n - y^n = (x^m - y^m) q(x, y) + y^m(x^{n-m} - y^{n-m})$$
Thus, the degree/power reduces exactly as $\operatorname{gcd}(n, m)$.

### Step 3: Conclusion
Therefore, $\operatorname{HCF}(x^n - y^n, x^m - y^m) = x^{\operatorname{gcd}(n, m)} - y^{\operatorname{gcd}(n, m)}$.
If $\operatorname{gcd}(n, m) = 2$, then $\operatorname{HCF} = x^2 - y^2$.
