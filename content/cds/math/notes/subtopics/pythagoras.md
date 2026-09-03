---
title: "Pythagoras & Apollonius Theorems"
exam: "CDS"
subject: "Math"
topic: "Triangles"
subtopic: "Pythagoras & Apollonius"
tags: [cds, math, triangles, pythagoras, apollonius, median, subtopic]
---

# Pythagoras & Apollonius Theorems

## 1. Pythagoras Theorem & Converse

### Pythagoras Theorem
In a right-angled triangle $\Delta ABC$ ($\angle C = 90^\circ$):
$$a^2 + b^2 = c^2$$

### Pythagorean Triplets
Common integer side lengths satisfying $a^2 + b^2 = c^2$:
- $(3, 4, 5)$
- $(5, 12, 13)$
- $(7, 24, 25)$
- $(8, 15, 17)$
- $(9, 40, 41)$
- $(11, 60, 61)$
- $(12, 35, 37)$
- $(20, 21, 29)$

### Acute & Obtuse Angle Generalization (Law of Cosines Connection)
- **Acute $\angle C < 90^\circ$**: $c^2 = a^2 + b^2 - 2a p \implies c^2 < a^2 + b^2$ ($p$ is projection of $b$ on $a$).
- **Obtuse $\angle C > 90^\circ$**: $c^2 = a^2 + b^2 + 2a p \implies c^2 > a^2 + b^2$.

---

## 2. Apollonius Theorem (Median Length Identity)

In any $\Delta ABC$, if $AD$ is the median drawn to side $BC$:

$$AB^2 + AC^2 = 2 \left( AD^2 + BD^2 \right) = 2 \left( AD^2 + \left(\frac{BC}{2}\right)^2 \right)$$

### Exact Median Length Formula
$$m_a = AD = \frac{1}{2} \sqrt{2b^2 + 2c^2 - a^2}$$
$$m_b = BE = \frac{1}{2} \sqrt{2a^2 + 2c^2 - b^2}$$
$$m_c = CF = \frac{1}{2} \sqrt{2a^2 + 2b^2 - c^2}$$

### Side-Median Sum Relations
1. **Sum of Squares of Medians**:
   $$m_a^2 + m_b^2 + m_c^2 = \frac{3}{4} \left( a^2 + b^2 + c^2 \right)$$
2. **Perimeter vs Median Sum Inequality**:
   $$\frac{3}{4} (a + b + c) < m_a + m_b + m_c < a + b + c$$

---

## 3. Right Triangle Median Properties

In right-angled triangle $\Delta ABC$ ($\angle A = 90^\circ$):
1. Median to hypotenuse $BC$ equals half the hypotenuse:
   $$AD = \frac{1}{2} BC = R$$
2. **Sum of Squares of Leg Medians**:
   If $BE$ and $CF$ are medians to legs $AC$ and $AB$:
   $$4 \left( BE^2 + CF^2 \right) = 5 BC^2$$

---

## 4. Linked Practice Questions

- [[cds/math/notes/questions/q2_tri|Q2: Apollonius Theorem & Median Side Calculation]]

---

## 5. Variations

- [[cds/math/notes/variations/var20|Variation 20: Apollonius Bounds in Obtuse Triangles]]
