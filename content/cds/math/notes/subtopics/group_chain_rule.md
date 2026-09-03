---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Time and Work"
subtopic: "Group Work & Chain Rule"
difficulty: "Medium"
tags: [cds, elementary-mathematics, time-and-work, subtopic]
---

# Group Work & Chain Rule Fundamental Formula

## General Equation & Proof

### Derivation of the Master Chain Rule Equation
Consider two groups performing work under varying parameters:
- Group 1: $M_1$ people, $D_1$ days, $T_1$ hours/day, efficiency $E_1$, producing work $W_1$ and earning wages $R_1$.
- Group 2: $M_2$ people, $D_2$ days, $T_2$ hours/day, efficiency $E_2$, producing work $W_2$ and earning wages $R_2$.

Since work done $W$ is directly proportional to manpower ($M$), time in days ($D$), daily hours ($T$), and individual worker efficiency ($E$):
$$W \propto M \cdot D \cdot T \cdot E$$

This implies:
$$\frac{M \cdot D \cdot T \cdot E}{W} = \text{Constant}$$

Equating the proportionality constant for both groups gives:
$$\frac{M_1 \cdot D_1 \cdot T_1 \cdot E_1}{W_1} = \frac{M_2 \cdot D_2 \cdot T_2 \cdot E_2}{W_2}$$

### Wage Distribution Principle
Wages ($R$) paid to workers are directly proportional to the total quantum of work performed ($W$):
$$R \propto W \implies \frac{W_1}{W_2} = \frac{R_1}{R_2}$$

Thus, combining work output and wage earnings:
$$\frac{M_1 \cdot D_1 \cdot T_1 \cdot E_1}{W_1 \cdot R_1} = \frac{M_2 \cdot D_2 \cdot T_2 \cdot E_2}{W_2 \cdot R_2}$$

---

## Practical Special Cases

1. **Constant Work ($W_1 = W_2$) and Same Hours ($T_1 = T_2$)**:
   $$M_1 \cdot D_1 = M_2 \cdot D_2$$

2. **Garrison Food Provision Dynamics**:
   - If a garrison of $n$ men has provision for $D$ days, total food units are $F = n \cdot D$.
   - If after $d$ days, $m$ additional men join:
     $$n(D - d) = (n + m) \cdot D_{\text{rem}}$$
     $$D_{\text{rem}} = \frac{n(D - d)}{n + m}$$

---

## Linked Practice Questions
- [[content/cds/math/notes/questions/q17|Q17: Men & Boys Equivalence System]]
- [[content/cds/math/notes/questions/q39|Q39: Multi-Worker Wages Ratio Distribution]]

---

## Variations
- [[content/cds/math/notes/variations/var25|Variation 25: Staggered Group Arrival with Wage Penalty Function]]

---

## Navigation
- [[content/cds/math/notes/work|Time and Work Topic]]
- [[content/cds/math/math_overview|Subject Dashboard]]
