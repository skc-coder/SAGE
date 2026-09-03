---
exam: "CDS"
subject: "Math"
topic: "Surface Area and Volume of Solids"
variation_set: "Chapter 27 Advanced 3D Mensuration Variations"
difficulty: "Hard"
tags: [cds, math, solids, variations, var27]
---

# Advanced 3D Mensuration & Solid Geometry Variations

## Variation 1: Rate of Liquid Flow Through Pipe into Cylindrical/Rectangular Tank

### Problem Model
Water flows through a cylindrical pipe of internal diameter $d = 2r$ at a rate of $v$ km/h into a rectangular tank of dimensions $L \times B$. How long will it take to raise the water level in the tank by height $H$?

### Step-by-Step Derivation
- Cross-sectional area of pipe: $A_{\text{pipe}} = \pi r^2$.
- Velocity of water flow: $v = \text{length of water column flowing per unit time}$.
- Volume flowing out of pipe in time $t$:
  $$V_{\text{out}}(t) = A_{\text{pipe}} \cdot v \cdot t = \pi r^2 \cdot v \cdot t$$
- Volume required in tank to reach height $H$:
  $$V_{\text{tank}} = L \cdot B \cdot H$$
- Equating volumes:
  $$\pi r^2 \cdot v \cdot t = L \cdot B \cdot H \implies t = \frac{L \cdot B \cdot H}{\pi r^2 v}$$

---

## Variation 2: Submersion of Solid Spheres into Cylindrical Vessel

### Problem Model
A cylindrical container of radius $R$ contains water up to height $h_0$. $n$ identical solid metal spheres of radius $r$ are completely dropped into the cylinder. Find the rise in water level $\Delta h$.

### Step-by-Step Derivation
- Total volume of $n$ submerged spheres:
  $$V_{\text{spheres}} = n \times \frac{4}{3}\pi r^3$$
- Volume of water displaced in cylinder:
  $$V_{\text{displaced}} = \pi R^2 \cdot \Delta h$$
- Equating displaced volume to sphere volume:
  $$\pi R^2 \cdot \Delta h = n \times \frac{4}{3}\pi r^3 \implies \Delta h = \frac{4 n r^3}{3 R^2}$$

---

## Variation 3: Solid Cone Cut into Three Equal Volume Slices

### Problem Model
A solid right circular cone of height $H$ is cut into three parts by two planes parallel to its base, such that the volumes of the three resulting solids (top cone, middle frustum, bottom frustum) are in the ratio $1 : 1 : 1$. Find the heights from the apex at which the cuts are made.

### Step-by-Step Derivation
- Let top small cone volume be $V_1 = V$.
- Second cone volume from top: $V_2 = 2V$.
- Total original cone volume: $V_3 = 3V$.
- Since volume of similar cones is proportional to the cube of their vertical heights ($V \propto h^3$):
  $$\frac{h_1^3}{H^3} = \frac{V_1}{V_3} = \frac{1}{3} \implies h_1 = \frac{H}{\sqrt[3]{3}}$$
  $$\frac{h_2^3}{H^3} = \frac{V_2}{V_3} = \frac{2}{3} \implies h_2 = H \sqrt[3]{\frac{2}{3}}$$
- The two parallel cuts must be made at distances $h_1 = \frac{H}{\sqrt[3]{3}}$ and $h_2 = H\left(\frac{2}{3}\right)^{1/3}$ from the vertex.

---

## Variation 4: Inscribed Sphere inside a Right Circular Cone

### Problem Model
A sphere of radius $r$ is inscribed inside a right circular cone of base radius $R$ and height $H$. Find $r$ in terms of $R$ and $H$.

### Step-by-Step Derivation
- Draw axial cross-section of cone (an isosceles triangle with base $2R$ and altitude $H$).
- Slant height $l = \sqrt{R^2 + H^2}$.
- Semi-vertical angle $\theta$: $\tan \theta = \frac{R}{H}, \sin \theta = \frac{R}{l} = \frac{R}{\sqrt{R^2 + H^2}}$.
- Centre of sphere lies on cone axis at height $r$ from base, so distance from apex to sphere centre is $H - r$.
- From right triangle formed by apex, sphere centre, and point of tangency on slant height:
  $$\sin \theta = \frac{r}{H - r}$$
  $$\frac{R}{\sqrt{R^2 + H^2}} = \frac{r}{H - r} \implies r( \sqrt{R^2 + H^2} + R ) = R H \implies r = \frac{R H}{R + \sqrt{R^2 + H^2}} = \frac{R H}{R + l}$$
