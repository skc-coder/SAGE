---
exam: "CDS"
subject: "Math"
topic: "Triangles"
subtopic: "Centers"
difficulty: "Medium"
importance: "Important"
date: 2026-09-03
source_file: "cds pathfinder.pdf"
question_number: "PYQ 2018 II Q65"
status: "Correct"
tags: [cds, math, triangles, incenter, angle, pyq, question]
---

# CDS PYQ 2018 II Q65: Incenter Angle Formula

## Question Text

In $\Delta ABC$, the internal bisectors of $\angle B$ and $\angle C$ intersect at point $I$. If $\angle A = 70^\circ$, find the measure of $\angle BIC$.

---

## Key Theorem & Method

### Incenter Subtended Angle Theorem
The angle subtended by any side at the incenter $I$ is related to the opposite vertex angle by:
$$\angle BIC = 90^\circ + \frac{1}{2} \angle A$$

---

## Step-by-Step Solution

1. **Apply Incenter Angle Formula**:
   $$\angle BIC = 90^\circ + \frac{70^\circ}{2}$$
   $$\angle BIC = 90^\circ + 35^\circ = 125^\circ$$

2. **Proof Sketch**:
   In $\Delta BIC$: $\angle BIC = 180^\circ - \left(\frac{\angle B}{2} + \frac{\angle C}{2}\right)$.
   Since $\angle B + \angle C = 180^\circ - \angle A$, we get:
   $$\frac{\angle B + \angle C}{2} = 90^\circ - \frac{\angle A}{2}$$
   Substituting gives $\angle BIC = 180^\circ - \left(90^\circ - \frac{\angle A}{2}\right) = 90^\circ + \frac{\angle A}{2}$.

---

## Related Notes
- Subtopic Note: [[cds/math/notes/subtopics/centers|Centers of Triangles]]
