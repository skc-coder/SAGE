---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Time and Distance"
subtopic: "Linear & Circular Races, Head Starts & Distance Deficits"
difficulty: "Hard"
tags: [cds, math, time-distance, races, subtopic]
---

# Linear & Circular Races, Head Starts & Distance Deficits

## 1. Linear Races & Terminology

In a race of distance $d$ meters between contestants $A$ and $B$:

- **$A$ beats $B$ by $x$ meters**:
  When $A$ reaches the finish line ($d$ meters), $B$ has covered $(d - x)$ meters in the exact same time.
  $$\frac{\text{Speed of } A}{\text{Speed of } B} = \frac{S_A}{S_B} = \frac{d}{d - x}$$

- **$A$ beats $B$ by $t$ seconds**:
  $A$ completes the race of distance $d$ in time $T$, while $B$ takes time $(T + t)$ to complete distance $d$.
  $$\text{Speed of } B = \frac{\text{Distance Deficit } x}{\text{Time Deficit } t}$$

- **$A$ gives $B$ a start of $x$ meters**:
  $A$ starts from position $0$, while $B$ starts from position $x$ ahead of $A$. To finish the race, $A$ covers $d$ meters while $B$ needs to cover $(d - x)$ meters.

- **$A$ gives $B$ a start of $t$ seconds**:
  $A$ starts running $t$ seconds after $B$ leaves the starting point.

---

## 2. Transitive Race Competitions

If in a race of distance $d$:
1. $A$ beats $B$ by $x$ meters $\implies \frac{S_A}{S_B} = \frac{d}{d - x}$
2. $B$ beats $C$ by $y$ meters $\implies \frac{S_B}{S_C} = \frac{d}{d - y}$

Then ratio of speeds of $A$ and $C$:
$$\frac{S_A}{S_C} = \frac{S_A}{S_B} \times \frac{S_B}{S_C} = \left(\frac{d}{d - x}\right) \times \left(\frac{d}{d - y}\right)$$

Distance covered by $C$ when $A$ covers $d$ meters is $d_C = d \times \frac{S_C}{S_A}$.
$A$ beats $C$ by $(d - d_C)$ meters.

---

## 3. Circular Races & Concurrency

For two runners $A$ and $B$ running on a circular track of circumference $C$ with speeds $S_A$ and $S_B$:

- **Time to meet for the first time anywhere on track**:
  $$T_{\text{first}} = \frac{C}{S_{\text{rel}}} = \begin{cases} \frac{C}{S_A - S_B} & \text{(Same Direction)} \\[6pt] \frac{C}{S_A + S_B} & \text{(Opposite Direction)} \end{cases}$$

- **Time to meet for the first time at the STARTING point**:
  $$T_{\text{start}} = \text{LCM}\left(\frac{C}{S_A}, \frac{C}{S_B}\right)$$
