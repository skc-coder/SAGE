---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Heights and Distances"
subtopic: "Elevated Observer & Opposite Building Models"
difficulty: "Hard"
tags: [cds, elementary-mathematics, subtopic, heights]
---

# Elevated Observer & Opposite Building Models

## Theory & Derivation

When observing an opposite structure of height $H$ from a window/balcony at height $h_1$ across a street of width $w$:
- Angle of elevation of the top of the opposite structure = $\theta$
- Angle of depression of the foot of the opposite structure = $\phi$

### Mathematical Formula Derivation

1. From the observer window to the base of the opposite building:
   $$\tan \phi = \frac{h_1}{w} \implies w = \frac{h_1}{\tan \phi} = h_1 \cot \phi$$
2. From the observer window to the top of the opposite building (additional height $h_2 = H - h_1$):
   $$\tan \theta = \frac{h_2}{w} \implies h_2 = w \tan \theta = (h_1 \cot \phi) \tan \theta$$
3. Total Height $H$:
   $$H = h_1 + h_2 = h_1 + h_1 \tan \theta \cot \phi = h_1 (1 + \tan \theta \cot \phi)$$

---

## Linked Practice Questions

- [[cds/math/notes/questions/q8_heights|Q8: Person Trajectory Stone Throw to Hit Fruit]]
- [[cds/math/notes/questions/q10_heights|Q10: Window Height Opposite Building Elevation and Depression]]

---

## Variations

- [[content/cds/math/notes/variations/heights_variations#variation-5-window-level-opposite-building-height|Variation 5: Window-Level Opposite Building Elevation/Depression]]
