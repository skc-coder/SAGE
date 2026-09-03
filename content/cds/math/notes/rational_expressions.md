---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Rational Expressions"
difficulty: "Medium"
tags: [cds, math, rational-expressions, algebra]
---

# Rational Expressions

## 1. Foundational Definition & Properties

A **Rational Expression** is an algebraic expression of the form:
$$\frac{P(x)}{Q(x)}$$
where $P(x)$ and $Q(x)$ are polynomials, and $Q(x) \neq 0$.

> [!NOTE] Key Rules
> 1. **Polynomial Subsumption**: Every polynomial is a rational expression (with denominator $Q(x) = 1$, a degree $0$ constant polynomial).
> 2. **Non-Polynomial Rational Expressions**: If $Q(x)$ has degree $\ge 1$ and does not divide $P(x)$ completely, the expression is a rational expression but **not** a polynomial.
> 3. **Valid Denominators**: Expressions like $\frac{x^3 + 2x^2 + 1}{x^{1/2} + 1}$ or $\frac{x+1}{\sqrt{x}-1}$ are **not** rational expressions because their denominators/numerators are not polynomials (fractional powers of variables are invalid in polynomials).

---

## 2. Lowest Form Reduction (Canonical Simplification)

A rational expression $\frac{P(x)}{Q(x)}$ is in its **lowest (irreducible) terms** if:
$$\gcd(P(x), Q(x)) = 1$$

### Reduction Algorithm:
1. Factorize both $P(x)$ and $Q(x)$ into irreducible linear and quadratic factors over $\mathbb{R}$.
2. Determine $g(x) = \gcd(P(x), Q(x))$.
3. Divide numerator and denominator by $g(x)$:
   $$\frac{P(x)}{Q(x)} = \frac{\frac{P(x)}{g(x)}}{\frac{Q(x)}{g(x)}}$$

---

## 3. Operations on Rational Expressions

### A. Addition & Subtraction (Telescoping & Common Denominators)
* **Like Denominators**:
  $$\frac{P(x)}{Q(x)} \pm \frac{H(x)}{Q(x)} = \frac{P(x) \pm H(x)}{Q(x)}$$
* **Unlike Denominators**:
  $$\frac{A(x)}{B(x)} + \frac{C(x)}{D(x)} = \frac{A(x) \cdot \frac{L(x)}{B(x)} + C(x) \cdot \frac{L(x)}{D(x)}}{L(x)}, \quad \text{where } L(x) = \text{lcm}(B(x), D(x))$$

### B. Multiplication & Division
* **Product**: $\frac{P(x)}{Q(x)} \times \frac{G(x)}{H(x)} = \frac{P(x) \cdot G(x)}{Q(x) \cdot H(x)}$
* **Quotient**: $\frac{P(x)}{Q(x)} \div \frac{G(x)}{H(x)} = \frac{P(x)}{Q(x)} \times \frac{H(x)}{G(x)} = \frac{P(x) \cdot H(x)}{Q(x) \cdot G(x)}$

---

## 4. Cyclic Symmetric Rational Identities & Theorems

In CDS examination questions, rational expression problems frequently test cyclic identities in variables $x, y, z$ or $a, b, c$.

### Theorem 1: Zero-Sum Cyclic Identity
If $x + y + z = 0$, then:
1. $\frac{x}{x+y} + \frac{y}{y+z} + \frac{z}{z+x}$ simplifies via linear substitution $x+y = -z$, $y+z = -x$, $z+x = -y$.
2. $\frac{xyz}{(x+y)(y+z)(z+x)} = \frac{xyz}{(-z)(-x)(-y)} = \frac{xyz}{-xyz} = -1$.

### Theorem 2: Symmetric Quadratic Cyclic Sum
If $x + y + z = 0$, then:
$$x^2 + y^2 - z^2 = (x+y)^2 - 2xy - z^2 = (-z)^2 - 2xy - z^2 = -2xy$$
Hence:
$$\frac{1}{x^2 + y^2 - z^2} + \frac{1}{y^2 + z^2 - x^2} + \frac{1}{z^2 + x^2 - y^2} = -\frac{1}{2xy} - \frac{1}{2yz} - \frac{1}{2zx} = -\frac{x+y+z}{2xyz} = 0$$

### Theorem 3: Cyclic Fraction Splitting
For pairwise distinct parameters $a, b, c$:
$$\frac{a}{(a-b)(a-c)} + \frac{b}{(b-c)(b-a)} + \frac{c}{(c-a)(c-b)} = 0$$

---

## 5. Subtopic & Cheatsheet Links

* [[cds/math/notes/subtopics/rational_simplification|Rational Simplification & Partial Fractions]]
* [[cds/math/notes/subtopics/cyclic_rational_identities|Cyclic Rational Identities & Constant Shifts]]
