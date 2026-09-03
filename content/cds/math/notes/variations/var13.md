---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "HCF and LCM of Polynomials"
subtopic: "Polynomial Factorization HCF & LCM"
difficulty: "Hard"
tags: [cds, math, hcf-lcm-polynomials, variation]
---

# Tier 2 Variation 13: Higher Power Sophie Germain Identity HCF

## Variation Problem Description

Find the HCF of $P(x) = x^4 + 4$ and $Q(x) = x^4 + 2x^3 + 2x^2$.

---

## Step-by-Step Proof & Solution

### What is the Sophie Germain Identity?

The classical **Sophie Germain Identity** states:
$$a^4 + 4b^4 = (a^2 + 2b^2 - 2ab)(a^2 + 2b^2 + 2ab)$$

For $a = x$ and $b = 1$, this simplifies to:
$$x^4 + 4 = (x^2 - 2x + 2)(x^2 + 2x + 2)$$

---

### Step 1: Factorize $P(x) = x^4 + 4$

Normally, $x^4 + 4$ looks like a sum of squares $A^2 + B^2$ which cannot be factored over real numbers. But by adding and subtracting the middle term $4x^2$, we convert it into a **difference of squares** $(A + B)^2 - C^2$:

1. Rewrite as squares plus/minus $4x^2$:
   $$P(x) = (x^2)^2 + 2^2 + 4x^2 - 4x^2$$

2. Complete the perfect square:
   $$P(x) = (x^2 + 2)^2 - (2x)^2$$

3. Apply difference of squares $A^2 - B^2 = (A - B)(A + B)$:
   $$P(x) = (x^2 + 2 - 2x)(x^2 + 2 + 2x)$$
   $$P(x) = (x^2 - 2x + 2)(x^2 + 2x + 2)$$

---

### Step 2: Factorize $Q(x) = x^4 + 2x^3 + 2x^2$

Factor out $x^2$:
$$Q(x) = x^2(x^2 + 2x + 2)$$

---

### Step 3: Compare Factors to Find HCF

- Factors of $P(x)$: $(x^2 - 2x + 2)$ and $(x^2 + 2x + 2)$
- Factors of $Q(x)$: $x^2$ and $(x^2 + 2x + 2)$

The shared quadratic factor is $(x^2 + 2x + 2)$.

$$\operatorname{HCF}(P(x), Q(x)) = x^2 + 2x + 2$$
