---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Heights and Distances"
subtopic: "Broken Pole & Tree Folding Property"
difficulty: "Easy"
tags: [cds, math, heights-and-distances, subtopic]
---

# Broken Pole & Tree Folding Property

## Concept & Mathematical Derivation

When a vertical telegraph pole or tree of initial total height $H$ breaks at a height $h$ from the ground due to a storm, the upper broken portion of length $(H - h)$ folds over and touches the ground at a distance $d$ from the base, forming an angle $\theta$ with the horizontal ground.

### Geometric Configuration
- Base to break point height: $BC = h$
- Upper broken section length: $AC = H - h$
- Distance of tip from base: $AB = d$
- Inclination angle with ground: $\angle CAB = \theta$

### Algebraic Equations

1. **Perpendicular to Base Relationship**:
   $$\tan \theta = \frac{h}{d} \implies h = d \cdot \tan \theta$$

2. **Hypotenuse to Base Relationship**:
   $$\cos \theta = \frac{d}{H - h} \implies H - h = d \cdot \sec \theta$$

3. **Total Initial Height Formula**:
   - Adding $h$ and $(H - h)$:
     $$H = h + (H - h) = d \cdot \tan \theta + d \cdot \sec \theta$$
   - Factoring $d$:
     $$H = d (\sec \theta + \tan \theta) = d \cdot \tan\left(\frac{\pi}{4} + \frac{\theta}{2}\right)$$

---

## Linked Practice Questions
- [[cds/math/notes/questions/q16_broken_pole|Q16: Pathfinder Broken Telegraph Pole (d=20m, theta=30deg)]]
