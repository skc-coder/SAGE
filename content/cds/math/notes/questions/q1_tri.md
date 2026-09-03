---
exam: "CDS"
subject: "Math"
topic: "Triangles"
subtopic: "Similarity"
difficulty: "Medium"
importance: "Important"
date: 2026-09-03
source_file: "cds pathfinder.pdf"
question_number: "Ch23 Practice Q13"
status: "Correct"
tags: [cds, math, triangles, similarity, bisector, question]
---

# Practice Q13: Internal Angle Bisector & Sub-triangle Area Ratio

## Question Text

In $\Delta ABC$, $AE$ is the internal bisector of $\angle A$ meeting $BC$ at $E$. If $AB = 6\text{ cm}$, $AC = 9\text{ cm}$, and $\text{Area}(\Delta ABC) = 35\text{ cm}^2$, find $\text{Area}(\Delta ABE)$.

---

## Key Theorem & Method

### Internal Angle Bisector Theorem
The internal angle bisector of a triangle divides the opposite side internally in the ratio of the adjacent sides:
$$\frac{BE}{EC} = \frac{AB}{AC} = \frac{6}{9} = \frac{2}{3}$$

### Common Altitude Area Rule
Triangles $\Delta ABE$ and $\Delta AEC$ share the exact same vertex $A$ and altitude $h$ dropped to line $BC$.
Therefore, their areas are directly proportional to their base lengths:
$$\frac{\text{Area}(\Delta ABE)}{\text{Area}(\Delta AEC)} = \frac{BE}{EC} = \frac{2}{3}$$

---

## Step-by-Step Solution

1. **Calculate Base Ratio**:
   $$BE : EC = 2 : 3 \implies BE = \frac{2}{5} BC$$
2. **Compute Sub-triangle Area**:
   $$\text{Area}(\Delta ABE) = \frac{2}{2 + 3} \times \text{Area}(\Delta ABC)$$
   $$\text{Area}(\Delta ABE) = \frac{2}{5} \times 35 = 14\text{ cm}^2$$

---

## Related Notes
- Subtopic Note: [[cds/math/notes/subtopics/similarity|Similarity of Triangles]]
- Variation Note: [[cds/math/notes/variations/var17|Variation 17: Median Partition & Sub-triangle Area Ratios]]
