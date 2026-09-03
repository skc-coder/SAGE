---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Heights and Distances"
subtopic: "Two-Point Observer Shift & Shadow Length Problems"
difficulty: "Medium"
tags: [cds, elementary-mathematics, subtopic, heights]
---

# Two-Point Observer Shift & Shadow Length Problems

## Theory & Intuitive Foundations

When an observer moves a distance $d$ along a horizontal line directly towards or away from a vertical tower of height $h$:
- As the observer moves **towards** the tower, the angle of elevation **increases** ($\alpha \to \beta$ where $\beta > \alpha$).
- As the observer moves **away** from the tower (or shadow lengthens), the angle of elevation **decreases**.

### Derivation of Shift Equation

Let the initial distance from the tower base be $x_1$ and final distance be $x_2$:
- $x_1 = h \cot \alpha$
- $x_2 = h \cot \beta$
- The distance moved $d = x_1 - x_2$:
  $$d = h(\cot \alpha - \cot \beta)$$
- Solving for $h$:
  $$h = \frac{d}{\cot \alpha - \cot \beta} = \frac{d \sin \alpha \sin \beta}{\sin(\beta - \alpha)}$$

---

## Linked Practice Questions

- [[cds/math/notes/questions/q2_heights|Q2: Light House Depression Angles on Opposite Sides]]
- [[cds/math/notes/questions/q5_heights|Q5: Shadow Length Variation with Sun Altitude Change]]
- [[cds/math/notes/questions/q7_heights|Q7: Speed of Aeroplane Changing Elevation in Time Interval]]

---

## Variations

- [[cds/math/notes/variations/heights_variations#variation-2-two-point-shift-along-straight-line|Variation 2: Two-Point Observer Shift Along Line]]
