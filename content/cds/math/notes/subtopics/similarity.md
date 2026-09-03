---
title: "Similarity of Triangles"
exam: "CDS"
subject: "Math"
topic: "Triangles"
subtopic: "Similarity"
tags: [cds, math, triangles, similarity, thales, subtopic]
---

# Similarity of Triangles

## 1. Concept of Similarity

Two triangles $\Delta ABC$ and $\Delta PQR$ are **similar** ($\Delta ABC \sim \Delta PQR$) if:
1. Corresponding angles are equal: $\angle A = \angle P, \quad \angle B = \angle Q, \quad \angle C = \angle R$
2. Corresponding sides are proportional:
   $$\frac{AB}{PQ} = \frac{BC}{QR} = \frac{CA}{RP} = k$$

---

## 2. Criteria for Similarity

- **AAA / AA Similarity**: If two angles of one triangle are equal to two angles of another, the triangles are similar.
- **SSS Similarity**: If all three pairs of corresponding sides are proportional, the triangles are similar.
- **SAS Similarity**: If one angle of a triangle is equal to one angle of another and the sides including these angles are proportional.

---

## 3. Fundamental Theorems

### Thales / Basic Proportionality Theorem (BPT)
If a line is drawn parallel to one side of a triangle intersecting the other two sides:
$$\text{In } \Delta ABC, \text{ if } DE \parallel BC \implies \frac{AD}{DB} = \frac{AE}{EC} \quad \text{and} \quad \frac{AD}{AB} = \frac{AE}{AC} = \frac{DE}{BC}$$

### Internal & External Angle Bisector Theorems
1. **Internal Angle Bisector Theorem**:
   If $AD$ bisects $\angle A$ internally meeting $BC$ at $D$:
   $$\frac{BD}{DC} = \frac{AB}{AC}$$
2. **External Angle Bisector Theorem**:
   If $AE$ bisects exterior angle $\angle A$ meeting $BC$ extended at $E$:
   $$\frac{BE}{EC} = \frac{AB}{AC}$$

---

## 4. Linear & Area Ratios of Similar Triangles

If $\Delta ABC \sim \Delta PQR$ with scale factor $k = \frac{AB}{PQ}$:
1. **Linear Ratio**:
   $$\frac{\text{Altitude}_1}{\text{Altitude}_2} = \frac{\text{Median}_1}{\text{Median}_2} = \frac{\text{Bisector}_1}{\text{Bisector}_2} = \frac{\text{Perimeter}_1}{\text{Perimeter}_2} = k$$
2. **Area Ratio Theorem**:
   $$\frac{\text{Area}(\Delta ABC)}{\text{Area}(\Delta PQR)} = \left(\frac{AB}{PQ}\right)^2 = \left(\frac{h_1}{h_2}\right)^2 = \left(\frac{m_1}{m_2}\right)^2 = k^2$$

---

## 5. Right Triangle Altitude Proportions

In right-angled triangle $\Delta ABC$ ($\angle A = 90^\circ$) with altitude $AD \perp BC$:
1. $\Delta ABD \sim \Delta CBA \implies AB^2 = BD \cdot BC$
2. $\Delta ACD \sim \Delta BCA \implies AC^2 = CD \cdot BC$
3. $\Delta ABD \sim \Delta CAD \implies AD^2 = BD \cdot CD$
4. **Product Formula**: $AD = \frac{AB \cdot AC}{BC}$

---

## 6. Linked Practice Questions

- [[cds/math/notes/questions/q1_tri|Q1: Angle Bisector Ratio & Area Distribution]]
- [[cds/math/notes/questions/q3_tri|Q3: Similar Triangle Area Ratio & Altitude Theorem]]

---

## 7. Variations

- [[cds/math/notes/variations/var18|Variation 18: Thales Parallel Segment & Trapezium Area Split]]
