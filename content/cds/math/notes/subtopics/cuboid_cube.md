---
exam: "CDS"
subject: "Math"
topic: "Surface Area and Volume of Solids"
subtopic: "Cuboid & Cube"
difficulty: "Medium"
tags: [cds, math, solids, cuboid, cube, subtopic]
---

# Cuboid & Cube

## 1. Core Definition & Geometry

A **cuboid** (rectangular parallelopiped) is a 3D solid bounded by six rectangular faces. It possesses 8 corners (vertices), 12 edges, 6 faces, and 4 spatial diagonals.
A **cube** is a special cuboid where length = breadth = height ($l = b = h = a$).

---

## 2. Fundamental Formulas

### Cuboid (Dimensions $l, b, h$)
- **Volume ($V$)**:
  $$V = l \cdot b \cdot h = \text{Base Area} \times \text{Height}$$
- **Total Surface Area ($\text{TSA}$)**:
  $$\text{TSA} = 2(lb + bh + lh)$$
- **Lateral Surface Area ($\text{LSA}$ / Area of 4 Walls)**:
  $$\text{LSA} = 2(l + b)h$$
- **Length of Space Diagonal ($d$)**:
  $$d = \sqrt{l^2 + b^2 + h^2}$$
  *(This represents the length of the longest rod that can be placed inside the room).*

### Cube (Edge Length $a$)
- **Volume ($V$)**:
  $$V = a^3$$
- **Total Surface Area ($\text{TSA}$)**:
  $$\text{TSA} = 6a^2$$
- **Lateral Surface Area ($\text{LSA}$)**:
  $$\text{LSA} = 4a^2$$
- **Space Diagonal ($d$)**:
  $$d = a\sqrt{3}$$

---

## 3. Advanced Relations & High-Yield Theorems

### Adjacent Face Areas Identity
If $x, y, z$ represent the surface areas of three adjacent faces meeting at a vertex:
$$x = lb, \quad y = bh, \quad z = lh$$
Multiplying the three equations gives:
$$xyz = (lb)(bh)(lh) = l^2 b^2 h^2 = (lbh)^2 = V^2$$
$$\therefore V = \sqrt{xyz}$$

### Sum of All Edges vs Surface Area & Diagonal
The sum of all 12 edges is $S = 4(l + b + h)$, so $l + b + h = \frac{S}{4}$.
Squaring $(l + b + h)$:
$$(l + b + h)^2 = (l^2 + b^2 + h^2) + 2(lb + bh + lh)$$
$$\left(\frac{S}{4}\right)^2 = d^2 + \text{TSA}$$
$$\text{TSA} = (l+b+h)^2 - d^2$$

### Open Box Cut-out from Metallic Sheet
When square corners of side $x$ are cut out from a rectangular sheet of length $L$ and breadth $B$ to fold an open top box:
- New length $l = L - 2x$
- New breadth $b = B - 2x$
- Height $h = x$
- **Volume of Box**:
  $$V(x) = (L - 2x)(B - 2x)x$$

---

## 4. Summary Table

| Property | Cuboid | Cube |
| :--- | :--- | :--- |
| **Volume ($V$)** | $l b h$ | $a^3$ |
| **TSA** | $2(lb + bh + lh)$ | $6a^2$ |
| **LSA / 4 Walls** | $2(l+b)h$ | $4a^2$ |
| **Space Diagonal** | $\sqrt{l^2+b^2+h^2}$ | $a\sqrt{3}$ |
| **Face Area Product** | $V = \sqrt{xyz}$ | $V = x^{3/2}$ |
