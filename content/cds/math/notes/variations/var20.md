---
exam: "CDS"
subject: "Math"
topic: "Triangles"
subtopic: "Pythagoras & Apollonius"
difficulty: "Hard"
importance: "Important"
tags: [cds, math, triangles, apollonius, obtuse, inequalities, variation]
---

# Variation 20: Apollonius Bounds & Median Bounds in Obtuse Triangles

## Problem Pattern
Questions testing upper/lower bounds of median lengths in obtuse triangles and sum of median squares vs sum of side squares.

## Core Formula Framework

1. **Apollonius Identity**:
   $$m_a^2 = \frac{2b^2 + 2c^2 - a^2}{4}$$
2. **Median Square Sum**:
   $$m_a^2 + m_b^2 + m_c^2 = \frac{3}{4} (a^2 + b^2 + c^2)$$
3. **Median Inequality Bounds**:
   $$\frac{3}{4} (a + b + c) < m_a + m_b + m_c < a + b + c$$

---

## Novel Conceptual Variation

### Question
In $\Delta ABC$, side lengths are $a = 7$, $b = 8$, and $c = 13$.
1. Is $\Delta ABC$ acute, right, or obtuse?
2. Calculate the exact length of median $m_c$ drawn to side $c = 13$.

### Solution

1. **Test Triangle Angle Classification**:
   $$a^2 + b^2 = 7^2 + 8^2 = 49 + 64 = 113$$
   $$c^2 = 13^2 = 169$$
   Since $c^2 > a^2 + b^2$ ($169 > 113$), $\Delta ABC$ is an **obtuse-angled triangle** at vertex $C$ ($\angle C > 90^\circ$).

2. **Calculate Median $m_c$ via Apollonius**:
   $$m_c = \frac{1}{2} \sqrt{2a^2 + 2b^2 - c^2}$$
   $$m_c = \frac{1}{2} \sqrt{2(49) + 2(64) - 169}$$
   $$m_c = \frac{1}{2} \sqrt{98 + 128 - 169} = \frac{1}{2} \sqrt{57} \approx 3.77$$

---

## Linked Notes
- [[cds/math/notes/subtopics/pythagoras|Pythagoras & Apollonius Theorems]]
- [[cds/math/notes/questions/q2_tri|Q2: Apollonius Theorem & Median Side Calculation]]
