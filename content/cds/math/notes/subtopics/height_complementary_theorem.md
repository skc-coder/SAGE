---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Heights and Distances"
subtopic: "Complementary Angles Height Theorem"
difficulty: "Medium"
tags: [cds, math, heights-and-distances, subtopic, proof]
---

# Complementary Angles Height Theorem

## Theorem Statement

If the angles of elevation of the top of a vertical tower of height $h$ from two collinear points on the ground at distances $a$ and $b$ ($a > b$) from the base of the tower are complementary, then the height of the tower is given by:

$$h = \sqrt{ab}$$

---

## Rigorous Mathematical Proof

Let $AD = h$ be the vertical tower standing on a horizontal plane.
Let $C$ and $B$ be two points on the ground collinear with foot $D$ such that:

- $CD = b$
- $BD = a$

Let the angle of elevation of the top $A$ at point $C$ be $\theta$.
Since the angles of elevation at $B$ and $C$ are complementary, the angle of elevation at point $B$ is $(90^\circ - \theta)$.

### Step 1: Evaluate Tangent at Point C
In right-angled triangle $\Delta ADC$:

$$\tan \theta = \frac{AD}{CD} = \frac{h}{b}$$

- Expressing height $h$ in terms of $\tan \theta$:

$$h = b \cdot \tan \theta \quad \text{--- (Equation 1)}$$

### Step 2: Evaluate Tangent at Point B
In right-angled triangle $\Delta ADB$:

$$\tan(90^\circ - \theta) = \frac{AD}{BD} = \frac{h}{a}$$

- Using the complementary angle identity $\tan(90^\circ - \theta) = \cot \theta$:

$$\cot \theta = \frac{h}{a}$$

- Expressing $\tan \theta$ by taking the reciprocal:

$$\tan \theta = \frac{a}{h} \quad \text{--- (Equation 2)}$$

### Step 3: Equate Expressions for $\tan \theta$
Equating Equation 1 and Equation 2:

$$\frac{h}{b} = \frac{a}{h}$$

- Cross-multiplying terms:

$$h^2 = a \cdot b$$

- Taking the principal positive square root:

$$h = \sqrt{ab}$$

$$\blacksquare$$

---

## Linked Practice Questions
- [[content/cds/math/notes/questions/q43|Q43: Pathfinder Example 3 Complementary Heights]]
