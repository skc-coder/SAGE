---
exam: "CDS"
subject: "Math"
topic: "Circle"
subtopic: "Cyclic Quadrilaterals & Ptolemy's Theorem"
difficulty: "Hard"
tags: [cds, math, circle, variation]
---

# Variation 26: Ptolemy's Theorem in Cyclic Quadrilaterals

## 1. Mathematical Statement

For any cyclic quadrilateral $ABCD$:
$$AC \cdot BD = AB \cdot CD + BC \cdot AD$$

---

## 2. Derivation / Construction Proof

Construct point $E$ on diagonal $AC$ such that $\angle ABE = \angle DBC$.

### Step 1: Similar Triangles $\Delta ABE \sim \Delta DBC$
- $\angle ABE = \angle DBC$ (by construction)
- $\angle BAE = \angle BDC$ (angles in same segment subtended by arc $BC$)
Therefore, $\Delta ABE \sim \Delta DBC$ (AA similarity):
$$\frac{AE}{AB} = \frac{CD}{BD} \implies AE \cdot BD = AB \cdot CD \quad \text{--- (Eq 1)}$$

### Step 2: Similar Triangles $\Delta EBC \sim \Delta ABD$
- $\angle EBC = \angle EBD + \angle DBC = \angle EBD + \angle ABE = \angle ABD$
- $\angle BCE = \angle BDA$ (angles in same segment subtended by arc $AB$)
Therefore, $\Delta EBC \sim \Delta ABD$ (AA similarity):
$$\frac{EC}{BC} = \frac{AD}{BD} \implies EC \cdot BD = BC \cdot AD \quad \text{--- (Eq 2)}$$

### Step 3: Sum Equations
Adding Eq 1 and Eq 2:
$$(AE + EC) \cdot BD = AB \cdot CD + BC \cdot AD$$
Since $AE + EC = AC$:
$$AC \cdot BD = AB \cdot CD + BC \cdot AD$$
