---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "HCF and LCM of Polynomials"
subtopic: "Polynomial Factorization HCF & LCM"
difficulty: "Medium"
tags: [cds, math, hcf-lcm-polynomials, subtopic]
---

# Polynomial Factorization HCF & LCM

## Core Concept & Theory

When polynomials $P(x)$ and $Q(x)$ are completely factorized over the field of real or rational numbers into irreducible linear or quadratic factors:
$$P(x) = c_1 \cdot f_1(x)^{a_1} \cdot f_2(x)^{a_2} \cdots f_k(x)^{a_k}$$
$$Q(x) = c_2 \cdot f_1(x)^{b_1} \cdot f_2(x)^{b_2} \cdots f_k(x)^{b_k}$$

### Rules for Computation:
1. **Numerical Coefficient HCF & LCM**: Compute the scalar HCF $\operatorname{gcd}(c_1, c_2)$ and LCM $\operatorname{lcm}(c_1, c_2)$ of the leading numeric multipliers independently.
2. **Polynomial HCF (Greatest Common Divisor)**: Take the product of all **common irreducible factors**, each raised to the **minimum exponent**:
   $$\operatorname{HCF}(P(x), Q(x)) = \operatorname{gcd}(c_1, c_2) \cdot \prod_{i=1}^k f_i(x)^{\min(a_i, b_i)}$$
3. **Polynomial LCM (Least Common Multiple)**: Take the product of **all present irreducible factors**, each raised to the **maximum exponent**:
   $$\operatorname{LCM}(P(x), Q(x)) = \operatorname{lcm}(c_1, c_2) \cdot \prod_{i=1}^k f_i(x)^{\max(a_i, b_i)}$$

---

## Standard Algebraic Identities for Factorization

To factorize higher-degree polynomials quickly in exam conditions, memorize these core algebraic identities:
- $a^2 - b^2 = (a-b)(a+b)$
- $a^3 - b^3 = (a-b)(a^2 + ab + b^2)$
- $a^3 + b^3 = (a+b)(a^2 - ab + b^2)$
- $a^4 - b^4 = (a^2 - b^2)(a^2 + b^2) = (a-b)(a+b)(a^2 + b^2)$
- $a^6 - b^6 = (a^3 - b^3)(a^3 + b^3) = (a-b)(a+b)(a^2 + ab + b^2)(a^2 - ab + b^2)$
- $a^4 + a^2 b^2 + b^4 = (a^2 + ab + b^2)(a^2 - ab + b^2)$ *(Sophie Germain / Quartic Identity)*

---

## Key Worked Pattern

**Example**: Find the HCF of $P(x) = x^4 - y^4$ and $Q(x) = x^6 - y^6$.
1. Factorize $P(x)$: $x^4 - y^4 = (x^2 - y^2)(x^2 + y^2) = (x-y)(x+y)(x^2 + y^2)$.
2. Factorize $Q(x)$: $x^6 - y^6 = (x^3 - y^3)(x^3 + y^3) = (x-y)(x^2 + xy + y^2)(x+y)(x^2 - xy + y^2) = (x^2 - y^2)(x^4 + x^2 y^2 + y^4)$.
3. Common terms: $(x-y)$ and $(x+y)$, so $\operatorname{HCF} = (x-y)(x+y) = x^2 - y^2$.

---

## Linked Practice Questions

- [[cds/math/notes/questions/q29|Q29: LCM of Cubic & Quadratic Factorable Polynomials]]
- [[cds/math/notes/questions/q30|Q30: Numerical Coefficient HCF with Multi-Variable Polynomials]]
