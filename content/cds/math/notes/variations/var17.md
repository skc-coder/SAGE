---
exam: "CDS"
subject: "Math"
topic: "Triangles"
subtopic: "Centers"
difficulty: "Hard"
importance: "Important"
tags: [cds, math, triangles, centroid, medians, area-partition, variation]
---

# Variation 17: Median Partition & Sub-triangle Area Ratios

## Problem Pattern
Questions testing area ratios formed by centroid $G$, midpoints of sides $D, E, F$, and medial triangle $\Delta DEF$.

## Core Theorem Framework

1. **6 Equal Areas by Centroid**:
   The three medians divide $\Delta ABC$ into 6 smaller triangles of equal area:
   $$\text{Area}(\Delta GBD) = \text{Area}(\Delta GCD) = \text{Area}(\Delta GCE) = \text{Area}(\Delta GAE) = \text{Area}(\Delta GAF) = \text{Area}(\Delta GBF) = \frac{1}{6} \text{Area}(\Delta ABC)$$

2. **Medial Triangle Area**:
   The triangle $\Delta DEF$ formed by joining the midpoints of the three sides has:
   $$\text{Area}(\Delta DEF) = \frac{1}{4} \text{Area}(\Delta ABC)$$

3. **Midpoint of Median Intersection**:
   If $E$ is the midpoint of median $AD$, then:
   $$\text{Area}(\Delta BED) = \frac{1}{4} \text{Area}(\Delta ABC)$$

---

## Novel Conceptual Variation

### Question
In $\Delta ABC$, $AD$ is a median and $E$ is the midpoint of $AD$. Line $BE$ extended meets $AC$ at $F$. Find the ratio $AF : FC$ and the ratio $\text{Area}(\Delta AEF) : \text{Area}(\Delta ABC)$.

### Solution
1. **Construction**: Draw line $DG \parallel BF$ meeting $AC$ at $G$.
2. **Apply Thales in $\Delta CDG$**: Since $D$ is midpoint of $BC$ and $DG \parallel BF \implies G$ is midpoint of $FC \implies FG = GC$.
3. **Apply Thales in $\Delta AEF$**: Since $E$ is midpoint of $AD$ and $EF \parallel DG \implies F$ is midpoint of $AG \implies AF = FG$.
4. **Conclusion on Side Ratio**:
   $$AF = FG = GC \implies AF : FC = 1 : 2$$
5. **Conclusion on Area Ratio**:
   - $\text{Area}(\Delta ABD) = \frac{1}{2} \text{Area}(\Delta ABC)$
   - $\text{Area}(\Delta ABE) = \frac{1}{2} \text{Area}(\Delta ABD) = \frac{1}{4} \text{Area}(\Delta ABC)$
   - In $\Delta ABF$, $E$ divides $BF$ in ratio $3:1 \implies \text{Area}(\Delta AEF) = \frac{1}{12} \text{Area}(\Delta ABC)$.

---

## Linked Notes
- [[cds/math/notes/subtopics/centers|Centers of Triangles]]
- [[cds/math/notes/questions/q1_tri|Q1: Angle Bisector Ratio & Area Distribution]]
