---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "HCF and LCM of Polynomials"
subtopic: "Zero Root Evaluation Method"
difficulty: "Medium"
tags: [cds, math, hcf-lcm-polynomials, subtopic]
---

# Zero Root Evaluation Method

## Core Concept & Theorem

### The Factor Theorem
For any polynomial $P(x)$, a linear binomial $(x - \alpha)$ is a factor of $P(x)$ if and only if $P(\alpha) = 0$.

### Common Root Principle for Polynomial HCF
If $H(x)$ is the HCF of $P(x)$ and $Q(x)$, then every root $\alpha$ of $H(x)$ must simultaneously be a root of both $P(x)$ and $Q(x)$:
$$H(\alpha) = 0 \implies P(\alpha) = 0 \quad \text{and} \quad Q(\alpha) = 0$$

---

## Exam Shortcut Workflow for Unknown Parameter Questions

When asked to find an unknown constant (such as $k$, $p$, $q$, $a$, or $b$) given that $(x - k)$ or $(x + c)$ is the HCF of two polynomials $P(x)$ and $Q(x)$:

1. **Root Substitution**:
   Set the HCF linear factor equal to zero: $x - k = 0 \implies x = k$.
2. **Equate Both Polynomials to Zero**:
   $$P(k) = 0 \quad \text{and} \quad Q(k) = 0$$
3. **Solve for Unknowns**:
   - If one equation contains $k$, solve $P(k) = 0 \implies k$.
   - If both polynomials contain $k$ and other parameters $p, q$, solve the simultaneous system $P(k) = Q(k) = 0$.

---

## Key Theorem & Property Highlights

### 1. Polynomial Product Identity
$$\operatorname{HCF}(P(x), Q(x)) \times \operatorname{LCM}(P(x), Q(x)) = P(x) \times Q(x)$$
*(Note: Always hold up to non-zero scalar multipliers).*

### 2. Linear Combination / Bezout's Lemma for Polynomials
If $H(x) = \operatorname{HCF}(P(x), Q(x))$, then $H(x)$ divides any linear combination $A(x)P(x) + B(x)Q(x)$ for arbitrary polynomials $A(x), B(x)$.
In particular, $H(x)$ divides $P(x) - Q(x)$ and $P(x) + Q(x)$.

---

## Linked Practice Questions

- [[cds/math/notes/questions/q32|Q32: Linear HCF Parameter Evaluation]]
- [[cds/math/notes/questions/q33|Q33: Dual Quadratic Common HCF System]]
- [[cds/math/notes/questions/q34|Q34: Dual Expression Sum & Difference LCM / HCF Reconstruction]]
