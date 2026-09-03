---
exam: "CDS"
subject: "Math"
topic: "Trigonometry"
subtopic: "Extrema & Triangle Properties"
difficulty: "Hard"
tags: [cds, math, trigonometry, subtopic, extrema, triangle-properties]
---

# Extrema & Triangle Properties

## Theory & Intuition

### 1. Maximum & Minimum Values of Linear Expressions
For expressions of the form:
$$f(\theta) = a \cos \theta + b \sin \theta + c$$
- **Transformation**:
  Set $a = R \cos \phi$ and $b = R \sin \phi$, where $R = \sqrt{a^2 + b^2}$.
  $$f(\theta) = R \cos(\theta - \phi) + c$$
- **Bounds**:
  $$-\sqrt{a^2 + b^2} + c \le a \cos \theta + b \sin \theta + c \le \sqrt{a^2 + b^2} + c$$
- **Maximum Value**:
  $$\text{Max} = c + \sqrt{a^2 + b^2}$$
- **Minimum Value**:
  $$\text{Min} = c - \sqrt{a^2 + b^2}$$

### 2. Extrema of Quadratic & AM-GM Forms
- For $a \tan^2\theta + b \cot^2\theta$ (where $a, b > 0$):
  By AM-GM Inequality:
  $$\frac{a \tan^2\theta + b \cot^2\theta}{2} \ge \sqrt{a \tan^2\theta \cdot b \cot^2\theta} = \sqrt{ab}$$
  $$\implies a \tan^2\theta + b \cot^2\theta \ge 2\sqrt{ab}$$
  Minimum value is $2\sqrt{ab}$.

- For $\sin^2\theta + \cos^4\theta$:
  $$\sin^2\theta + \cos^4\theta = 1 - \cos^2\theta + \cos^4\theta = \left(\cos^2\theta - \frac{1}{2}\right)^2 + \frac{3}{4}$$
  $$\text{Minimum} = \frac{3}{4} \quad (\text{at } \cos^2\theta = 1/2), \quad \text{Maximum} = 1 \quad (\text{at } \cos^2\theta = 0 \text{ or } 1)$$

### 3. Properties of Triangles (Sine & Cosine Rules)
In any triangle $\Delta ABC$ with sides $a, b, c$ opposite to angles $A, B, C$:
- **Sine Rule**:
  $$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$$
  where $R$ is the circumradius of $\Delta ABC$.
- **Cosine Rule**:
  $$\cos A = \frac{b^2 + c^2 - a^2}{2bc}, \quad \cos B = \frac{c^2 + a^2 - b^2}{2ca}, \quad \cos C = \frac{a^2 + b^2 - c^2}{2ab}$$

---

## Linked Practice Questions
- [[content/cds/math/notes/questions/q26|Question 26: AM-GM Bound on Tan Square and Cot Square]]
- [[content/cds/math/notes/questions/q29|Question 29: Quadratic Equation in Cosine for Tan Value]]
- [[content/cds/math/notes/questions/q138|Question 138: Linear Combination Extrema Bounds]]

---

## Variations
- [[content/cds/math/notes/variations/var7|Variation 7: Cauchy-Schwarz and AM-GM Bound Optimization]]
- [[content/cds/math/notes/variations/var8|Variation 8: Circumradius Substitution in Side Sum Expressions]]
