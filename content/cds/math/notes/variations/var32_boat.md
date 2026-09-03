---
exam: "CDS"
subject: "Math"
topic: "Time and Distance"
subtopic: "Boats and Streams"
difficulty: "Hard"
tags: [cds, math, time-distance, variation]
---

# Variation 33: Round-Trip River Navigation & Still Water Speed Invariant

## 1. Mathematical Statement

If a boat travels downstream for distance $D$ and returns upstream across the same distance $D$, taking total round-trip time $T$, and the speed of the stream is $v$, then the boat's speed in still water $u$ satisfies the quadratic relation:

$$T u^2 - 2 D u - T v^2 = 0$$

$$\implies u = \frac{D + \sqrt{D^2 + T^2 v^2}}{T}$$

---

## 2. Theoretical Derivation

### Step 1: Upstream and Downstream Times
- Downstream Speed: $S_d = u + v \implies T_1 = \frac{D}{u + v}$
- Upstream Speed: $S_u = u - v \implies T_2 = \frac{D}{u - v}$

### Step 2: Total Round-Trip Time Equation
$$T = T_1 + T_2 = \frac{D}{u + v} + \frac{D}{u - v}$$

Combine fractions over a common denominator:
$$T = D \left[\frac{(u - v) + (u + v)}{(u + v)(u - v)}\right] = D \left[\frac{2u}{u^2 - v^2}\right]$$

$$T(u^2 - v^2) = 2Du$$
$$T u^2 - 2Du - T v^2 = 0$$

### Step 3: Solving Quadratic for $u$
Applying the quadratic formula $a = T, b = -2D, c = -T v^2$:

$$u = \frac{-(-2D) \pm \sqrt{(-2D)^2 - 4(T)(-Tv^2)}}{2T}$$
$$u = \frac{2D \pm \sqrt{4D^2 + 4T^2 v^2}}{2T} = \frac{D \pm \sqrt{D^2 + T^2 v^2}}{T}$$

Since speed in still water $u > 0$, taking the positive root yields:
$$u = \frac{D + \sqrt{D^2 + T^2 v^2}}{T}$$
