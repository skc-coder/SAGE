---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Heights and Distances"
subtopic: "Subtended Angles & Spherical Geometry"
difficulty: "Hard"
tags: [cds, math, heights-and-distances, subtopic, spherical]
---

# Subtended Angles & Spherical Geometry

## Spherical Subtended Angle Theorem

When a spherical object (e.g. balloon or sphere) of radius $r$ subtends an angle $\alpha$ at the eye of an observer at point $O$, and the angle of elevation of the center of the sphere $C$ is $\beta$, the height of the center of the sphere above the horizontal plane is given by:

$$h = r \cdot \sin \beta \cdot \text{cosec}\left(\frac{\alpha}{2}\right)$$

---

## Rigorous Proof

Let $O$ be the observer's eye on the horizontal ground plane.
Let $C$ be the center of the spherical balloon of radius $r$.

1. **Tangent Angle Subtended by Sphere**:
   - Draw two tangent lines from observer $O$ to the sphere touching at $T_1$ and $T_2$.
   - The total subtended angle is $\angle T_1 O T_2 = \alpha$.
   - The line joining $O$ to center $C$ bisects this subtended angle:

$$\angle T_1 O C = \angle T_2 O C = \frac{\alpha}{2}$$

2. **Distance from Observer to Sphere Center ($OC$)**:
   - In the right-angled triangle $\Delta O T_1 C$ ($\angle O T_1 C = 90^\circ$ since radius is perpendicular to tangent line):

$$\sin\left(\frac{\alpha}{2}\right) = \frac{T_1 C}{OC} = \frac{r}{OC}$$

   - Solving for distance $OC$:

$$OC = \frac{r}{\sin(\alpha/2)} = r \cdot \text{cosec}\left(\frac{\alpha}{2}\right)$$

3. **Vertical Height of Sphere Center ($h$)**:
   - Let $\beta$ be the angle of elevation of center $C$ from $O$ ($\angle COH = \beta$).
   - In right-angled triangle $\Delta O H C$:

$$\sin \beta = \frac{CH}{OC} = \frac{h}{OC}$$

   - Substituting $OC = r \cdot \text{cosec}(\alpha/2)$:

$$h = OC \cdot \sin \beta = r \cdot \sin \beta \cdot \text{cosec}\left(\frac{\alpha}{2}\right)$$

$$\blacksquare$$

---

## Linked Practice Questions
- [[content/cds/math/notes/questions/q45|Q45: Pathfinder Q35 Spherical Balloon Radius r with alpha=60deg, beta=60deg]]
