---
exam: "CDS"
subject: "Math"
topic: "Quadrilateral and Polygon"
subtopic: "Variations"
difficulty: "Hard"
tags: [cds, math, variation, quadrilateral, polygon]
---

# Quadrilateral & Polygon Novel Variations

## Variation 21: Trapezium Diagonal Intersection & Area Split Formula
In trapezium $ABCD$ with $AB \parallel CD$, diagonals $AC$ and $BD$ intersect at $O$.
- If $\text{Area}(\Delta AOB) = A_1$ and $\text{Area}(\Delta COD) = A_2$, then:
  $$\text{Area}(\Delta AOC) = \text{Area}(\Delta BOD) = \sqrt{A_1 A_2}$$
  $$\text{Total Area of Trapezium } ABCD = (\sqrt{A_1} + \sqrt{A_2})^2$$

## Variation 22: Midpoint Quadrilateral Area & Perimeter Bounds
For any arbitrary convex quadrilateral $ABCD$ of area $\mathcal{A}$ and perimeter $P$:
- The quadrilateral $PQRS$ formed by joining the midpoints of consecutive sides is always a **parallelogram**.
- $\text{Area}(PQRS) = \frac{1}{2} \mathcal{A}$
- $\text{Perimeter}(PQRS) = AC + BD$ (sum of the diagonals of $ABCD$).

## Variation 23: Regular $n$-gon Diagonal Intersection Count
In a regular polygon of $n$ sides, the number of diagonals is:
$$D = \frac{n(n - 3)}{2}$$
- Number of triangles formed by joining vertices of regular $n$-gon $= \binom{n}{3}$.
- Number of internal diagonal intersection points (assuming no 3 diagonals concur) $= \binom{n}{4}$.
