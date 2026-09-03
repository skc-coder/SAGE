---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Heights and Distances"
subtopic: "3D Orthogonal Road Distance & Bearings"
difficulty: "Hard"
tags: [cds, math, heights-and-distances, subtopic, 3d]
---

# 3D Orthogonal Road Distance & Bearings

## Problem Archetype & Theorem

When a vertical tower $BD = h$ is observed from two points $A$ and $C$ on a straight horizontal road, where $A$ lies due South/North and $C$ lies due West/East of the tower, the triangle formed on the horizontal plane $\Delta ABC$ is right-angled at $B$ ($\angle ABC = 90^\circ$).

### Geometric Setup
- Tower height: $BD = h$
- Observer distance at point $A$: $AB = d_1$
- Observer distance at point $C$: $BC = d_2$
- Angle of elevation from $A$: $\alpha \implies d_1 = h \cot \alpha$
- Angle of elevation from $C$: $\beta \implies d_2 = h \cot \beta$

### Shortest Perpendicular Distance to the Road
Let $p = BE$ be the shortest perpendicular distance from the foot of the tower $B$ to the line of road $AC$.

In right-angled triangle $\Delta ABC$ ($\angle B = 90^\circ$):

$$\frac{1}{p^2} = \frac{1}{d_1^2} + \frac{1}{d_2^2}$$

Substituting $d_1 = h \cot \alpha$ and $d_2 = h \cot \beta$:

$$\frac{1}{p^2} = \frac{1}{h^2 \cot^2 \alpha} + \frac{1}{h^2 \cot^2 \beta} = \frac{\tan^2 \alpha + \tan^2 \beta}{h^2}$$

- Solving for shortest distance $p$:

$$p = \frac{h}{\sqrt{\tan^2 \alpha + \tan^2 \beta}} = \frac{d_1 d_2}{\sqrt{d_1^2 + d_2^2}}$$

---

## Linked Practice Questions
- [[content/cds/math/notes/questions/q46|Q46: Pathfinder Q38 Tower Distance from Road (200m West, 300m South)]]
