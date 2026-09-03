---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Time and Distance"
subtopic: "Train Problems & Crossing Point/Platform Invariants"
difficulty: "Medium"
tags: [cds, math, time-distance, train, subtopic]
---

# Train Problems & Crossing Point/Platform Invariants

## 1. Core Principles of Train Motion

In train problems, the length of the moving train ($L_{\text{train}}$) must be added to the distance covered whenever crossing an extended stationary object or another moving train.

---

## 2. Crossing Invariants & Time Equations

### 1. Crossing a Point Object (Pole, Standing Man, Signal Post)
- **Object Dimensions**: Negligible length ($L_{\text{object}} = 0$).
- **Distance Covered**: $D = L_{\text{train}}$.
- **Time Taken**:
  $$T = \frac{L_{\text{train}}}{S_{\text{train}}}$$

### 2. Crossing an Extended Stationary Object (Platform, Bridge, Tunnel)
- **Distance Covered**: $D = L_{\text{train}} + L_{\text{object}}$.
- **Time Taken**:
  $$T = \frac{L_{\text{train}} + L_{\text{object}}}{S_{\text{train}}}$$

### 3. Two Moving Trains Crossing Each Other
- **Total Distance**: $D = L_1 + L_2$.
- **Relative Speed**:
  - Opposite Directions: $S_{\text{rel}} = S_1 + S_2$
  - Same Direction: $S_{\text{rel}} = |S_1 - S_2|$
- **Time Taken**:
  $$T = \frac{L_1 + L_2}{S_1 \pm S_2}$$

---

## 3. Post-Crossing Time Ratio Theorem

If two trains start simultaneously from stations $A$ and $B$ towards each other, and after meeting/crossing on the way, take $t_1$ and $t_2$ time respectively to reach their final destinations $B$ and $A$:

$$\frac{\text{Speed of Train 1}}{\text{Speed of Train 2}} = \frac{S_1}{S_2} = \sqrt{\frac{t_2}{t_1}}$$
