---
exam: "CDS"
subject: "Math"
topic: "Circle"
subtopic: "Cyclic Quadrilaterals & Ptolemy's Theorem"
difficulty: "Hard"
tags: [cds, math, circle, cyclic-quadrilateral, subtopic]
---

# Cyclic Quadrilaterals & Ptolemy's Theorem

## 1. Core Properties & Theorems

### Definition
A quadrilateral $ABCD$ is cyclic if all four of its vertices $A, B, C, D$ lie on a single circle.

### Theorem 1: Opposite Angles Supplementary
The sum of either pair of opposite angles of a cyclic quadrilateral is $180^\circ$.
$$\angle A + \angle C = 180^\circ, \quad \angle B + \angle D = 180^\circ$$

- **Converse**: If the sum of a pair of opposite angles of a quadrilateral is $180^\circ$, then the quadrilateral is cyclic.

### Theorem 2: Exterior Angle Property
If one side of a cyclic quadrilateral is produced, the exterior angle so formed is equal to the interior opposite angle.
$$\angle \text{ext} = \angle \text{interior opposite}$$

### Ptolemy's Theorem
For any cyclic quadrilateral $ABCD$ with sides $a, b, c, d$ ($AB=a, BC=b, CD=c, DA=d$) and diagonals $p = AC$ and $q = BD$:
$$p \cdot q = a \cdot c + b \cdot d$$
$$AC \cdot BD = AB \cdot CD + BC \cdot AD$$

- **Diagonal Length Formulas**:
  $$AC = \sqrt{\frac{(ac + bd)(ad + bc)}{ab + cd}}$$
  $$BD = \sqrt{\frac{(ab + cd)(ac + bd)}{ad + bc}}$$

### Area of Cyclic Quadrilateral (Brahmagupta's Formula)
For a cyclic quadrilateral with side lengths $a, b, c, d$ and semi-perimeter $s = \frac{a+b+c+d}{2}$:
$$\text{Area} = \sqrt{(s-a)(s-b)(s-c)(s-d)}$$

---

## 2. Linked Practice Questions

- [[cds/math/notes/questions/q4_circle|Q4: Cyclic Quadrilateral Exterior & Opposite Angles]]

---

## 3. Variations

- [[cds/math/notes/variations/var26|Variation 26: Ptolemy's Theorem in Cyclic Quadrilaterals]]
