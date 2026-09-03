---
exam: "CDS"
subject: "Math"
topic: "Time and Distance"
subtopic: "Races & Transitive Deficits"
difficulty: "Hard"
tags: [cds, math, time-distance, variation]
---

# Variation 32: Transitive Distance Deficit in Three-Runner Races

## 1. Mathematical Statement

In a race of distance $L$, if contestant $A$ beats contestant $B$ by $x$ meters, and contestant $B$ beats contestant $C$ by $y$ meters, then the distance $z$ by which contestant $A$ beats contestant $C$ in the exact same race distance $L$ is given by:

$$z = x + y - \frac{xy}{L}$$

---

## 2. Theoretical Derivation

### Step 1: Speed Ratios & Distance Relations
Let the uniform speeds of runners $A, B, C$ be $S_A, S_B, S_C$ respectively.

1. When $A$ completes distance $L$, $B$ covers $(L - x)$ meters:
   $$\frac{S_B}{S_A} = \frac{L - x}{L} = 1 - \frac{x}{L}$$

2. When $B$ completes distance $L$, $C$ covers $(L - y)$ meters:
   $$\frac{S_C}{S_B} = \frac{L - y}{L} = 1 - \frac{y}{L}$$

### Step 2: Product Ratio $\frac{S_C}{S_A}$
The ratio of distance covered by $C$ to distance covered by $A$ in equal time:
$$\frac{S_C}{S_A} = \frac{S_B}{S_A} \times \frac{S_C}{S_B} = \left(1 - \frac{x}{L}\right)\left(1 - \frac{y}{L}\right)$$

$$\frac{S_C}{S_A} = 1 - \frac{x}{L} - \frac{y}{L} + \frac{xy}{L^2}$$

### Step 3: Distance Covered by $C$ when $A$ Finishes $L$
$$D_C = L \cdot \frac{S_C}{S_A} = L \left(1 - \frac{x + y}{L} + \frac{xy}{L^2}\right) = L - (x + y) + \frac{xy}{L}$$

### Step 4: Deficit Distance $z = L - D_C$
$$z = L - \left(L - (x + y) + \frac{xy}{L}\right)$$
$$z = x + y - \frac{xy}{L}$$

---

## 3. Key Takeaway & Application Rule

When $A$ beats $B$ by $x$ and $B$ beats $C$ by $y$, $A$ does **NOT** beat $C$ by simply $(x + y)$ meters. The correct deficit is reduced by the interactive correction term $\frac{xy}{L}$ because $C$ runs for a shorter distance when competing against $B$ than when competing against $A$.
