---
exam: "CDS"
subject: "Math"
topic: "Quadrilateral and Polygon"
subtopic: "British Flag Theorem"
difficulty: "Medium"
status: "Correct"
importance: "Important"
tags: [cds, math, question, rectangle, geometry]
---

# Q2: British Flag Theorem in Rectangle

## Question
Let $O$ be an interior point of a rectangle $ABCD$. Prove that:
$$OB^2 + OD^2 = OA^2 + OC^2$$

## Step-by-Step Solution

### 1. Perpendicular Grid Setup
Draw lines through point $O$ parallel to the sides of rectangle $ABCD$:
- Line parallel to $AB$ and $CD$ meeting $AD$ at $P$ and $BC$ at $Q$.
- Line parallel to $AD$ and $BC$ meeting $AB$ at $R$ and $CD$ at $S$.

This divides rectangle $ABCD$ into four right-angled triangles with perpendicular offsets:
- Let $AP = AR = x$, $PD = AS = y$.
- Let $RB = PC = z$, $SC = BQ = w$.

### 2. Applying Pythagoras Theorem in 4 Corner Right Triangles
In the four small right-angled triangles centered around $O$:
- In $\Delta APO$:
  $$OA^2 = AP^2 + PO^2$$
- In $\Delta CSO$:
  $$OC^2 = CS^2 + SO^2$$
- In $\Delta BQO$:
  $$OB^2 = BQ^2 + QO^2$$
- In $\Delta DPO$:
  $$OD^2 = DP^2 + PO^2$$

Since $PO = AR$, $QO = RB$, $SO = DP$, etc.:
- $OA^2 + OC^2 = AP^2 + PO^2 + CS^2 + SO^2$
- $OB^2 + OD^2 = BQ^2 + QO^2 + DP^2 + PO^2$

### 3. Verification of Identity
Both sums simplify to the sum of squares of the four orthogonal segment lengths from $O$ to the rectangular grid lines:
$$OA^2 + OC^2 = OB^2 + OD^2$$

Hence, proved!
