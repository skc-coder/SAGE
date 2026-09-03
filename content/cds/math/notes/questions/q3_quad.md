---
exam: "CDS"
subject: "Math"
topic: "Quadrilateral and Polygon"
subtopic: "Regular Hexagon Geometry"
difficulty: "Hard"
status: "Correct"
importance: "Important"
tags: [cds, math, question, hexagon, polygon]
---

# Q3: Regular Hexagon Area and Sub-Triangle Ratio

## Question
Let $ABCDEF$ be a regular hexagon with side length $a$.
1. Find the total area of the regular hexagon.
2. Find the area of $\Delta ACE$ formed by joining alternate vertices.
3. Determine the ratio of the area of $\Delta ACE$ to the total area of hexagon $ABCDEF$.

## Step-by-Step Solution

### 1. Total Area of Regular Hexagon
A regular hexagon can be partitioned into 6 equilateral triangles of side length $a$ with a common vertex at the center $O$.
- Area of one equilateral triangle of side $a$:
  $$\text{Area}(\Delta OAB) = \frac{\sqrt{3}}{4} a^2$$
- Total area of Hexagon $ABCDEF$:
  $$\text{Area}_{\text{hex}} = 6 \times \frac{\sqrt{3}}{4} a^2 = \frac{3\sqrt{3}}{2} a^2$$

### 2. Side Length of Equilateral Triangle $\Delta ACE$
In $\Delta ABC$:
- Sides $AB = a$ and $BC = a$.
- Included angle $\angle B = 120^\circ$.
- By Cosine Rule in $\Delta ABC$:
  $$AC^2 = a^2 + a^2 - 2(a)(a)\cos(120^\circ) = 2a^2 - 2a^2 \left(-\frac{1}{2}\right) = 3a^2$$
  $$AC = a\sqrt{3}$$

Since $AC = CE = EA = a\sqrt{3}$, $\Delta ACE$ is an equilateral triangle with side length $s = a\sqrt{3}$.

### 3. Area of $\Delta ACE$
$$\text{Area}(\Delta ACE) = \frac{\sqrt{3}}{4} s^2 = \frac{\sqrt{3}}{4} (a\sqrt{3})^2 = \frac{3\sqrt{3}}{4} a^2$$

### 4. Ratio of Areas
$$\frac{\text{Area}(\Delta ACE)}{\text{Area}_{\text{hex}}} = \frac{\frac{3\sqrt{3}}{4} a^2}{\frac{3\sqrt{3}}{2} a^2} = \frac{1}{2}$$

Thus, the triangle formed by joining alternate vertices of a regular hexagon covers exactly **50% (1 : 2 ratio)** of the hexagon's total area.
