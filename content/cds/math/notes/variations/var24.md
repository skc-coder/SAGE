---
exam: "CDS"
subject: "Math"
topic: "Circle"
subtopic: "Tangents, Secants & Power of a Point"
difficulty: "Hard"
tags: [cds, math, circle, variation]
---

# Variation 24: Direct and Transverse Common Tangent Length Ratios

## 1. Problem Formulation & Theoretical Setup

Given two non-intersecting, non-concentric circles $S_1$ and $S_2$ with radii $R$ and $r$ ($R > r$) separated by distance $d$ between their centres ($d > R + r$).

- Length of Direct Common Tangent ($L_{\text{DCT}}$):
  $$L_{\text{DCT}} = \sqrt{d^2 - (R - r)^2}$$
- Length of Transverse Common Tangent ($L_{\text{TCT}}$):
  $$L_{\text{TCT}} = \sqrt{d^2 - (R + r)^2}$$

---

## 2. Key Identity & Structural Bounds

### Ratio of Common Tangents
$$\frac{L_{\text{DCT}}}{L_{\text{TCT}}} = \sqrt{\frac{d^2 - (R - r)^2}{d^2 - (R + r)^2}}$$

Since $(R + r)^2 > (R - r)^2$ for non-zero radii, $d^2 - (R - r)^2 > d^2 - (R + r)^2$, implying:
$$L_{\text{DCT}} > L_{\text{TCT}} \quad \forall d > R + r$$

### Special Case: External Touch Condition ($d = R + r$)
When the two circles touch externally:
- $L_{\text{TCT}} = 0$ (Transverse tangent degrades to point contact).
- $L_{\text{DCT}} = \sqrt{(R + r)^2 - (R - r)^2} = \sqrt{4Rr} = 2\sqrt{Rr}$.

---

## 3. Advanced Numerical Example

### Scenario
Two circles of radii $R = 9\text{ cm}$ and $r = 4\text{ cm}$ have centres separated by $d = 15\text{ cm}$. Find the ratio $L_{\text{DCT}} : L_{\text{TCT}}$.

### Solution
1. Calculate $L_{\text{DCT}}$:
   $$L_{\text{DCT}} = \sqrt{15^2 - (9 - 4)^2} = \sqrt{225 - 25} = \sqrt{200} = 10\sqrt{2}\text{ cm}$$
2. Calculate $L_{\text{TCT}}$:
   $$L_{\text{TCT}} = \sqrt{15^2 - (9 + 4)^2} = \sqrt{225 - 169} = \sqrt{56} = 2\sqrt{14}\text{ cm}$$
3. Ratio:
   $$\frac{L_{\text{DCT}}}{L_{\text{TCT}}} = \frac{10\sqrt{2}}{2\sqrt{14}} = \frac{5}{\sqrt{7}} = \frac{5\sqrt{7}}{7}$$
