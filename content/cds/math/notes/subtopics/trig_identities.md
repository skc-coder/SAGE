---
exam: "CDS"
subject: "Math"
topic: "Trigonometry"
subtopic: "Fundamental Identities & Ratios"
difficulty: "Medium"
tags: [cds, math, trigonometry, subtopic, identities]
---

# Fundamental Identities & Ratios

## Theory & Intuition

Trigonometric ratios express the proportional relationships between the sides of a right-angled triangle relative to an acute angle $\theta$.

### Standard Ratios & Reciprocals
- $\sin\theta = \frac{\text{Perpendicular}}{\text{Hypotenuse}}$, $\csc\theta = \frac{1}{\sin\theta}$
- $\cos\theta = \frac{\text{Base}}{\text{Hypotenuse}}$, $\sec\theta = \frac{1}{\cos\theta}$
- $\tan\theta = \frac{\sin\theta}{\cos\theta} = \frac{\text{Perpendicular}}{\text{Base}}$, $\cot\theta = \frac{\cos\theta}{\sin\theta} = \frac{1}{\tan\theta}$

### Pythogorean Identities
$$\sin^2\theta + \cos^2\theta = 1$$
$$1 + \tan^2\theta = \sec^2\theta \implies \sec^2\theta - \tan^2\theta = 1$$
$$1 + \cot^2\theta = \csc^2\theta \implies \csc^2\theta - \cot^2\theta = 1$$

### Difference of Squares Decomposition (High Yield CDS Pattern)
From $\sec^2\theta - \tan^2\theta = 1$:
$$(\sec\theta - \tan\theta)(\sec\theta + \tan\theta) = 1 \implies \sec\theta - \tan\theta = \frac{1}{\sec\theta + \tan\theta}$$
Similarly:
$$(\csc\theta - \cot\theta)(\csc\theta + \cot\theta) = 1 \implies \csc\theta - \cot\theta = \frac{1}{\csc\theta + \cot\theta}$$

### Algebraic Reciprocal Identity Trap
If $x = \tan\theta + \cot\theta$:
$$x = \frac{\sin\theta}{\cos\theta} + \frac{\cos\theta}{\sin\theta} = \frac{\sin^2\theta + \cos^2\theta}{\sin\theta \cos\theta} = \frac{1}{\sin\theta \cos\theta} = \frac{2}{\sin 2\theta}$$
Since $|\sin 2\theta| \le 1$:
$$|\tan\theta + \cot\theta| \ge 2$$

---

## Linked Practice Questions
- [[content/cds/math/notes/questions/q14|Question 14: Logarithmic Complementary Product]]
- [[content/cds/math/notes/questions/q20_trig|Question 20: Allied Angle Quotient to Tan Formula]]
- [[content/cds/math/notes/questions/q26|Question 26: AM-GM Bound on Tan Square and Cot Square]]

---

## Variations
- [[content/cds/math/notes/variations/var3|Variation 3: Secant-Tangent Conjugate Reciprocal System]]
- [[content/cds/math/notes/variations/var4|Variation 4: Logarithmic Product Telescoping]]
