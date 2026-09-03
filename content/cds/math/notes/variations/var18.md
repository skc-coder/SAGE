---
exam: "CDS"
subject: "Math"
topic: "Triangles"
subtopic: "Similarity"
difficulty: "Medium"
importance: "Important"
tags: [cds, math, triangles, similarity, thales, area-split, variation]
---

# Variation 18: Thales Parallel Segment & Trapezium Area Split

## Problem Pattern
Questions where a line parallel to one side divides a triangle into a smaller similar triangle and a quadrilateral (trapezium) of equal or proportional areas.

## Core Formula Framework

If $DE \parallel BC$ in $\Delta ABC$ with $D \in AB, E \in AC$:
$$\Delta ADE \sim \Delta ABC \implies \frac{\text{Area}(\Delta ADE)}{\text{Area}(\Delta ABC)} = \left(\frac{AD}{AB}\right)^2$$

If $DE$ divides $\text{Area}(\Delta ABC)$ into two equal parts:
$$\text{Area}(\Delta ADE) = \frac{1}{2} \text{Area}(\Delta ABC) \implies \left(\frac{AD}{AB}\right)^2 = \frac{1}{2}$$
$$\frac{AD}{AB} = \frac{1}{\sqrt{2}} \implies AD = \frac{AB}{\sqrt{2}}$$

---

## Novel Conceptual Variation

### Question
A line segment $DE \parallel BC$ cuts sides $AB$ and $AC$ of $\Delta ABC$ such that $\text{Area}(\Delta ADE) : \text{Area}(\text{Trapezium } BCED) = 4 : 5$. If $AB = 18\text{ cm}$, find the length of segment $BD$.

### Solution

1. **Relate Top Triangle Area to Total Triangle Area**:
   $$\text{Area}(\Delta ABC) = \text{Area}(\Delta ADE) + \text{Area}(\text{Trapezium } BCED) = 4 + 5 = 9 \text{ units}$$
   $$\frac{\text{Area}(\Delta ADE)}{\text{Area}(\Delta ABC)} = \frac{4}{9}$$

2. **Apply Similarity Area Theorem**:
   $$\left(\frac{AD}{AB}\right)^2 = \frac{4}{9} \implies \frac{AD}{AB} = \sqrt{\frac{4}{9}} = \frac{2}{3}$$

3. **Compute $AD$ and $BD$**:
   $$AD = \frac{2}{3} \times 18 = 12\text{ cm}$$
   $$BD = AB - AD = 18 - 12 = 6\text{ cm}$$

---

## Linked Notes
- [[cds/math/notes/subtopics/similarity|Similarity of Triangles]]
- [[cds/math/notes/questions/q3_tri|Q3: Similar Triangle Area Ratio & Altitude Theorem]]
