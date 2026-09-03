---
exam: "CDS"
subject: "Math"
topic: "Triangles"
subtopic: "Pythagoras & Apollonius"
difficulty: "Hard"
importance: "Important"
date: 2026-09-03
source_file: "cds pathfinder.pdf"
question_number: "Ch23 Practice Q39"
status: "Correct"
tags: [cds, math, triangles, apollonius, median, pythagoras, question]
---

# Practice Q39: Median Length Calculation via Apollonius Theorem

## Question Text

In $\Delta ABC$, side lengths are $AB = 6\text{ cm}$, $AC = 8\text{ cm}$, and $BC = 10\text{ cm}$. Find the length of median $AD$ drawn from vertex $A$ to side $BC$.

---

## Key Theorem & Method

### Apollonius Theorem
For any triangle $\Delta ABC$ with median $AD$ to side $BC$:
$$AB^2 + AC^2 = 2 \left( AD^2 + BD^2 \right)$$

Since $D$ is the midpoint of $BC$, $BD = \frac{BC}{2} = 5\text{ cm}$.

---

## Step-by-Step Solution

1. **Check Right Triangle Condition**:
   $$AB^2 + AC^2 = 6^2 + 8^2 = 36 + 64 = 100 = 10^2 = BC^2$$
   Thus $\Delta ABC$ is a right-angled triangle at $\angle A = 90^\circ$.

2. **Method 1 (Right Triangle Hypotenuse Median Identity)**:
   In a right-angled triangle, the median to the hypotenuse equals half the hypotenuse:
   $$AD = \frac{BC}{2} = \frac{10}{2} = 5\text{ cm}$$

3. **Method 2 (Apollonius Formula Verification)**:
   $$6^2 + 8^2 = 2 \left( AD^2 + 5^2 \right)$$
   $$100 = 2 \left( AD^2 + 25 \right) \implies 50 = AD^2 + 25 \implies AD^2 = 25 \implies AD = 5\text{ cm}$$

---

## Related Notes
- Subtopic Note: [[cds/math/notes/subtopics/pythagoras|Pythagoras & Apollonius Theorems]]
- Variation Note: [[cds/math/notes/variations/var20|Variation 20: Apollonius Bounds in Obtuse Triangles]]
