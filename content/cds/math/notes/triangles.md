---
title: "Triangles"
exam: "CDS"
subject: "Math"
topic: "Triangles"
tags: [cds, math, triangles, geometry, topic]
---

# Triangles

## 1. Overview & Fundamental Properties

A triangle $\Delta ABC$ is a closed 3-sided polygon formed by joining three non-collinear points.

### Fundamental Inequalities & Angle Relations
1. **Angle Sum Property**:
   $$\angle A + \angle B + \angle C = 180^\circ$$
2. **Exterior Angle Theorem**:
   $$\text{Exterior Angle} = \text{Sum of two opposite interior angles}$$
   $$\angle ACD = \angle A + \angle B$$
3. **Triangle Side Inequality**:
   - The sum of any two sides is strictly greater than the third side:
     $$a + b > c, \quad b + c > a, \quad c + a > b$$
   - The absolute difference of any two sides is strictly less than the third side:
     $$|a - b| < c < a + b$$
4. **Side-Angle Order**:
   - The side opposite to the largest angle is the longest side.
   - The side opposite to the smallest angle is the shortest side.

---

## 2. Classification of Triangles

### By Side Lengths
- **Scalene**: All 3 sides are unequal ($a \neq b \neq c$).
- **Isosceles**: Two sides are equal ($a = b$). Angles opposite equal sides are equal ($\angle A = \angle B$).
- **Equilateral**: All 3 sides are equal ($a = b = c$). All interior angles are $60^\circ$.

### By Angle Measures (Given sides $a \le b \le c$)
- **Acute-angled**: $c^2 < a^2 + b^2$ (All angles $< 90^\circ$).
- **Right-angled**: $c^2 = a^2 + b^2$ (One angle $= 90^\circ$).
- **Obtuse-angled**: $c^2 > a^2 + b^2$ (One angle $> 90^\circ$).

---

## 3. Subtopics

- [[cds/math/notes/subtopics/congruence|Congruence of Triangles]]
- [[cds/math/notes/subtopics/similarity|Similarity of Triangles]]
- [[cds/math/notes/subtopics/centers|Centers of Triangles]]
- [[cds/math/notes/subtopics/pythagoras|Pythagoras & Apollonius Theorems]]

---

## 4. Key Formulas & Area Rules

| Formula Type | Expression / Relation | Context |
| :--- | :--- | :--- |
| **Heron's Formula** | $\text{Area} = \sqrt{s(s-a)(s-b)(s-c)}$ | $s = \frac{a+b+c}{2}$ |
| **Base-Height** | $\text{Area} = \frac{1}{2} \cdot b \cdot h$ | Base $b$, Altitude $h$ |
| **Trigonometric Area** | $\text{Area} = \frac{1}{2} ab \sin C = \frac{1}{2} bc \sin A = \frac{1}{2} ca \sin B$ | Two sides and included angle |
| **Equilateral Area** | $\text{Area} = \frac{\sqrt{3}}{4} a^2, \quad h = \frac{\sqrt{3}}{2} a$ | Side length $a$ |
| **Inradius ($r$)** | $r = \frac{\text{Area}}{s}$ | Semi-perimeter $s$ |
| **Circumradius ($R$)** | $R = \frac{abc}{4 \times \text{Area}}$ | Sides $a, b, c$ |

---

## 5. Linked Practice & PYQ Questions

- [[cds/math/notes/questions/q1_tri|Q1: Angle Bisector Ratio & Area Distribution]]
- [[cds/math/notes/questions/q2_tri|Q2: Apollonius Theorem & Median Side Calculation]]
- [[cds/math/notes/questions/q3_tri|Q3: Similar Triangle Area Ratio & Altitude Theorem]]
- [[cds/math/notes/questions/q4_tri|Q4: Incenter Angle Formula & Bisector Concurrency]]

---

## 6. Variations

- [[cds/math/notes/variations/var17|Variation 17: Median Partition & Sub-triangle Area Ratios]]
- [[cds/math/notes/variations/var18|Variation 18: Thales Parallel Segment & Trapezium Area Split]]
- [[cds/math/notes/variations/var20|Variation 20: Apollonius Bounds in Obtuse Triangles]]
