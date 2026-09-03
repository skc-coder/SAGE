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

## Fast Option Root-Testing Heuristic (5-Second Exam Shortcut)

When given multiple-choice options for polynomial **HCF** or **LCM**, you can avoid full long division or factoring by testing root values directly!

### 1. The HCF Option Testing Rule
If an option $(x - \alpha)$ is the true HCF:
- Setting $x = \alpha$ **MUST make BOTH polynomials evaluate to ZERO simultaneously**:
  $$P(\alpha) = 0 \quad \text{AND} \quad Q(\alpha) = 0$$
- If any option yields $P(\alpha) \neq 0$ or $Q(\alpha) \neq 0$, **ELIMINATE IT IMMEDIATELY**!

#### Worked Example (PYQ 2014 II Q38):
Find the HCF of $P(x) = 2x^3 + x^2 - x - 2$ and $Q(x) = 3x^3 - 2x^2 + x - 2$.
Options: (a) $x - 1$, (b) $x + 1$, (c) $2x + 1$, (d) $2x - 1$.

- **Test Option (a) $x - 1 \implies x = 1$**:
  $$P(1) = 2(1)^3 + 1^2 - 1 - 2 = 2 + 1 - 1 - 2 = 0 \quad \checkmark$$
  $$Q(1) = 3(1)^3 - 2(1)^2 + 1 - 2 = 3 - 2 + 1 - 2 = 0 \quad \checkmark$$
  Since $x = 1$ makes **both $P(1)=0$ and $Q(1)=0$**, Option (a) $x - 1$ is the correct HCF instantly!

---

### 2. The LCM Option Testing Rule
If an option $L(x)$ is the true LCM:
- Every root $\alpha$ of the given input polynomials $P(x)$ and $Q(x)$ **MUST also make the LCM option evaluate to ZERO**:
  $$P(\alpha) = 0 \implies L(\alpha) = 0$$
  $$Q(\beta) = 0 \implies L(\beta) = 0$$
- **Shortcut Trick**: Pick an easy small integer (e.g. $x = 2$ or $x = 3$) where $P(x) \neq 0$ and $Q(x) \neq 0$. Compute numeric values $P(2)$ and $Q(2)$. The correct LCM option $L(2)$ **MUST be a numeric multiple of both $P(2)$ and $Q(2)$**!

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
