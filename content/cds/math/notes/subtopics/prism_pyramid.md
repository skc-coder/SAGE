---
exam: "CDS"
subject: "Math"
topic: "Surface Area and Volume of Solids"
subtopic: "Prism, Pyramid & Tetrahedron"
difficulty: "Hard"
tags: [cds, math, solids, prism, pyramid, tetrahedron, subtopic]
---

# Prism, Pyramid & Regular Tetrahedron

## 1. Right Prism

A solid whose top and bottom bases are congruent parallel polygons, and whose lateral sides are rectangular faces perpendicular to the base.

- **Volume ($V$)**:
  $$V = \text{Area of Base} \times \text{Height}$$
- **Lateral Surface Area ($\text{LSA}$)**:
  $$\text{LSA} = \text{Perimeter of Base} \times \text{Height}$$
- **Total Surface Area ($\text{TSA}$)**:
  $$\text{TSA} = \text{LSA} + 2 \times \text{Area of Base}$$

---

## 2. Right Pyramid

A solid whose base is any polygon and whose lateral faces are isosceles triangles meeting at a single point called the apex.

- **Slant Height ($l$)**:
  In a regular pyramid with base inradius $r_{\text{in}}$ and vertical height $h$:
  $$l = \sqrt{h^2 + r_{\text{in}}^2}$$
- **Slant Edge ($e$)**:
  With base circumradius $R_{\text{circ}}$ and height $h$:
  $$e = \sqrt{h^2 + R_{\text{circ}}^2}$$
- **Volume ($V$)**:
  $$V = \frac{1}{3} \times \text{Area of Base} \times \text{Height}$$
- **Lateral Surface Area ($\text{LSA}$)**:
  $$\text{LSA} = \frac{1}{2} \times \text{Perimeter of Base} \times \text{Slant Height } l$$
- **Total Surface Area ($\text{TSA}$)**:
  $$\text{TSA} = \text{LSA} + \text{Area of Base}$$

---

## 3. Regular Tetrahedron

A regular pyramid whose base and three lateral faces are all four congruent **equilateral triangles** of side length $a$.

### Derivations & Direct Formulas
- **Height ($h$)**:
  Distance from apex to centroid of base. Circumradius of base equilateral triangle $R = \frac{a}{\sqrt{3}}$.
  $$h = \sqrt{a^2 - R^2} = \sqrt{a^2 - \frac{a^2}{3}} = \sqrt{\frac{2}{3}a^2} = a\sqrt{\frac{2}{3}}$$
- **Volume ($V$)**:
  $$V = \frac{1}{3} \times \text{Area of Base} \times h = \frac{1}{3} \times \left(\frac{\sqrt{3}}{4}a^2\right) \times \left(a\sqrt{\frac{2}{3}}\right) = \frac{a^3}{6\sqrt{2}}$$
- **Slant Height ($l$)**:
  Height of face equilateral triangle:
  $$l = \frac{\sqrt{3}}{2}a$$
- **Total Surface Area ($\text{TSA}$)**:
  4 equilateral triangles:
  $$\text{TSA} = 4 \times \left(\frac{\sqrt{3}}{4}a^2\right) = \sqrt{3}a^2$$

---

## 4. Master Comparison Table

| Solid | Volume ($V$) | LSA | TSA |
| :--- | :--- | :--- | :--- |
| **Right Prism** | $\text{Base Area} \times h$ | $\text{Base Perimeter} \times h$ | $\text{LSA} + 2 \times \text{Base Area}$ |
| **Right Pyramid** | $\frac{1}{3} \times \text{Base Area} \times h$ | $\frac{1}{2} \times \text{Base Perimeter} \times l$ | $\text{LSA} + \text{Base Area}$ |
| **Regular Tetrahedron** | $\frac{a^3}{6\sqrt{2}}$ | $\frac{3\sqrt{3}}{4}a^2$ | $\sqrt{3}a^2$ |
