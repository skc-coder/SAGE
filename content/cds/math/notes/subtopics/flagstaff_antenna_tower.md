---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Heights and Distances"
subtopic: "Flagstaff & Antenna Subtended Angles"
difficulty: "Hard"
tags: [cds, elementary-mathematics, subtopic, heights]
---

# Flagstaff & Antenna Subtended Angles

## Theory & Derivation

When a vertical object of height $p$ (flagstaff/antenna) is mounted on top of a tower of height $h$, observing both bottom and top from a ground point $O$ yields two right-angled triangles sharing the same ground base $d$.

### General Height Equation Derivation

- Let base distance be $d$.
- Angle to bottom of antenna = $\alpha \implies \tan \alpha = \frac{h}{d} \implies d = \frac{h}{\tan \alpha}$
- Angle to top of antenna = $\beta \implies \tan \beta = \frac{h + p}{d} \implies d = \frac{h + p}{\tan \beta}$
- Equating distance expressions:
  $$\frac{h}{\tan \alpha} = \frac{h + p}{\tan \beta}$$
  $$h \tan \beta = h \tan \alpha + p \tan \alpha$$
  $$h(\tan \beta - \tan \alpha) = p \tan \alpha \implies h = \frac{p \tan \alpha}{\tan \beta - \tan \alpha}$$

---

## Linked Practice Questions

- [[cds/math/notes/questions/q4_heights|Q4: Radio Transmitter Antenna on Tall Building]]
- [[cds/math/notes/questions/q9_heights|Q9: Vertical Flagstaff General Formula Expression]]

---

## Variations

- [[content/cds/math/notes/variations/heights_variations#variation-4-mounted-flagstaffantenna-formula|Variation 4: Mounted Flagstaff/Antenna General Ratio]]
