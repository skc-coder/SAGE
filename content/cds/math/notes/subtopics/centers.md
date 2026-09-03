---
title: "Centers of Triangles"
exam: "CDS"
subject: "Math"
topic: "Triangles"
subtopic: "Centers"
tags: [cds, math, triangles, centroid, incenter, circumcenter, orthocenter, subtopic]
---

# Centers of Triangles

## 1. Summary of 4 Core Triangle Centers

| Center Name | Intersection of | Position (Acute/Right/Obtuse) | Key Properties & Ratios |
| :--- | :--- | :--- | :--- |
| **Centroid ($G$)** | Medians | Always inside | Divides medians in ratio $2:1$. Divides triangle into 6 equal areas. |
| **Incenter ($I$)** | Internal Angle Bisectors | Always inside | Equidistant from all 3 sides ($r$). $\angle BIC = 90^\circ + \frac{\angle A}{2}$. |
| **Circumcenter ($O$)** | Perpendicular Side Bisectors | Inside / Midpoint of Hypotenuse / Outside | Equidistant from all 3 vertices ($R$). $\angle BOC = 2\angle A$. |
| **Orthocenter ($H$)** | Altitudes | Inside / Vertex of Right Angle / Outside | $\angle BHC = 180^\circ - \angle A$. |

---

## 2. Detailed Center Theorems

### 1. Centroid ($G$)
- **Median Ratio**: $AG : GD = 2 : 1$ for median $AD$.
- **Area Partition**: The 3 medians divide $\Delta ABC$ into 6 sub-triangles of equal area:
  $$\text{Area}(\Delta GAB) = \text{Area}(\Delta GBC) = \text{Area}(\Delta GCA) = \frac{1}{3} \text{Area}(\Delta ABC)$$
- **Centroid Coordinate / Vector Sum**:
  $$\vec{GA} + \vec{GB} + \vec{GC} = \vec{0}$$

### 2. Incenter ($I$)
- **Incenter Angle Formulas**:
  $$\angle BIC = 90^\circ + \frac{1}{2}\angle A, \quad \angle CIA = 90^\circ + \frac{1}{2}\angle B, \quad \angle AIB = 90^\circ + \frac{1}{2}\angle C$$
- **Inradius**:
  $$r = \frac{\Delta}{s} \quad (\text{Right Triangle: } r = \frac{a + b - c}{2})$$

### 3. Circumcenter ($O$)
- **Angle Subtended at Circumcenter**:
  $$\angle BOC = 2\angle A$$
- **Circumradius**:
  $$R = \frac{abc}{4\Delta} \quad (\text{Right Triangle: } R = \frac{\text{Hypotenuse}}{2})$$

### 4. Orthocenter ($H$)
- **Orthocenter Angle Formula**:
  $$\angle BHC = 180^\circ - \angle A$$
- **Right Triangle Special Case**:
  - Orthocenter $H$ lies directly on the right-angled vertex.
  - Circumcenter $O$ lies on the midpoint of hypotenuse.

---

## 3. Euler Line Theorem & Distance Formulas

1. **Euler Line**:
   In any triangle, the Orthocenter ($H$), Centroid ($G$), and Circumcenter ($O$) are collinear, and $G$ divides $HO$ in the ratio $2:1$:
   $$HG : GO = 2 : 1$$
   *(Note: In equilateral triangles, $H, G, O, I$ all coincide).*
2. **Euler's Distance Formula (Incenter-Circumcenter)**:
   $$d^2 = R^2 - 2Rr \implies d = \sqrt{R(R - 2r)}$$
   *(Implication: $R \ge 2r$ for all triangles, equality holds for equilateral).*

---

## 4. Linked Practice Questions

- [[cds/math/notes/questions/q4_tri|Q4: Incenter Angle Formula & Bisector Concurrency]]

---

## 5. Variations

- [[cds/math/notes/variations/var17|Variation 17: Median Partition & Sub-triangle Area Ratios]]
