---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Heights and Distances"
subtopic: "Cloud Reflection in Water"
difficulty: "Hard"
tags: [cds, math, heights-and-distances, variation]
---

# Variation 21: Elliptic Cloud Reflection in Spherical Lake

## Generalised Formula

For an observer at height $h$ observing a cloud elevation $\alpha$ and image depression $\beta$ in a reflective body of water, the actual height $H$ of the cloud above the water surface is given by:

$$H = h \cdot \frac{\tan \beta + \tan \alpha}{\tan \beta - \tan \alpha} = h \cdot \frac{\sin(\beta + \alpha)}{\sin(\beta - \alpha)}$$

---

## Proof & Symmetry Analysis

1. Elevation equation: $\tan \alpha = \frac{H - h}{x} \implies x = \frac{H - h}{\tan \alpha}$
2. Depression equation: $\tan \beta = \frac{H + h}{x} \implies x = \frac{H + h}{\tan \beta}$
3. Equating $x$:

$$\frac{H - h}{\tan \alpha} = \frac{H + h}{\tan \beta}$$

$$(H - h)\tan \beta = (H + h)\tan \alpha$$

$$H(\tan \beta - \tan \alpha) = h(\tan \beta + \tan \alpha)$$

$$H = h \cdot \frac{\tan \beta + \tan \alpha}{\tan \beta - \tan \alpha}$$

---

## Special Cases

- **Case 1 ($\alpha = 30^\circ, \beta = 60^\circ$)**:
  $$H = h \cdot \frac{\sqrt{3} + 1/\sqrt{3}}{\sqrt{3} - 1/\sqrt{3}} = h \cdot \frac{4/\sqrt{3}}{2/\sqrt{3}} = 2h$$
  *(Matches Q47 where $h = 200\text{ m} \implies H = 400\text{ m}$)*

- **Case 2 ($\alpha = 45^\circ, \beta = 60^\circ$)**:
  $$H = h \cdot \frac{\sqrt{3} + 1}{\sqrt{3} - 1} = h(2 + \sqrt{3})$$
