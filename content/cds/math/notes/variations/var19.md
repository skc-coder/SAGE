---
exam: "CDS"
subject: "Math"
topic: "Trigonometry"
subtopic: "Fundamental Identities & Ratios"
difficulty: "Medium"
tags: [cds, math, trigonometry, variation]
---

# Trigonometry Variation Notes

## Chapter 20 Exam Variations & Trap Patterns

### Variation 1: Clock Hand Overlap & Perpendicularity Times
- **Pattern**: Finding the exact time between hour $H$ and $H+1$ when hands are opposite ($180^\circ$) or perpendicular ($90^\circ$).
- **Formula**:
  $$t = \frac{2}{11} \left( 30H \pm \theta \right) \text{ minutes}$$

---

### Variation 2: Arc Length Ratio across Concentric Circles
- **Pattern**: Two arcs of equal length subtend angles $\theta_1$ and $\theta_2$ at centers of different radii $r_1$ and $r_2$.
- **Formula**:
  $$l = r_1 \theta_1 = r_2 \theta_2 \implies \frac{r_1}{r_2} = \frac{\theta_2}{\theta_1}$$

---

### Variation 3: Secant-Tangent Conjugate Reciprocal System
- **Pattern**: If $\sec\theta + \tan\theta = x$, then $\sec\theta - \tan\theta = \frac{1}{x}$.
- **Key Deductions**:
  $$\sec\theta = \frac{1}{2}\left(x + \frac{1}{x}\right) = \frac{x^2 + 1}{2x}$$
  $$\tan\theta = \frac{1}{2}\left(x - \frac{1}{x}\right) = \frac{x^2 - 1}{2x}$$

---

### Variation 4: Logarithmic Product Telescoping
- **Pattern**: Evaluating $\sum_{k=1}^{n-1} \log\left(\tan\frac{k\pi}{2n}\right)$.
- **Key Deduction**: Terms pair as $\tan(k\theta) \cdot \tan\left(\frac{\pi}{2} - k\theta\right) = 1$, yielding overall sum $= 0$.

---

### Variation 5: Triple Angle Expansion Factorization
- **Pattern**: Recognizing $3\sin\theta - 4\sin^3\theta$ or $4\cos^3\theta - 3\cos\theta$ in nested algebraic expressions.
- **Key Deduction**: Condenses directly to $\sin 3\theta$ or $\cos 3\theta$.

---

### Variation 6: Geometric Progression Angle Products
- **Pattern**: Evaluating $\cos\theta \cos(2\theta) \cos(4\theta) \dots \cos(2^{n-1}\theta)$.
- **Formula**:
  $$P = \frac{\sin(2^n \theta)}{2^n \sin\theta}$$

---

### Variation 7: Cauchy-Schwarz and AM-GM Bound Optimization
- **Pattern**: Finding minimum of $a^2\tan^2\theta + b^2\cot^2\theta$ or $a^2\sec^2\theta + b^2\csc^2\theta$.
- **Formulas**:
  - $\text{Min}(a^2\tan^2\theta + b^2\cot^2\theta) = 2ab$
  - $\text{Min}(a^2\sec^2\theta + b^2\csc^2\theta) = (a + b)^2$

---

### Variation 8: Circumradius Substitution in Side Sum Expressions
- **Pattern**: Simplifying $a^2 + b^2 + c^2$ or $\sin^2 A + \sin^2 B + \sin^2 C$ using $a = 2R\sin A$.
- **Key Deduction**: Directly connects geometric side lengths with trigonometric square sums.
