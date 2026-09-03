---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Time and Work"
subtopic: "Work Efficiency & Combined Rates"
difficulty: "Easy"
tags: [cds, elementary-mathematics, time-and-work, subtopic]
---

# Work Rate & Combined Efficiency Theorem

## Theorem Statement & Derivation

### Mathematical Definition of Efficiency
Work rate (or efficiency $E$) is defined as the scalar quantity of work completed per unit time. If $W$ units of work require $D$ days to complete:
$$E = \frac{W}{D}$$

When work is normalized as a unit whole ($W = 1$):
$$E = \frac{1}{D}$$

### Derivation of Combined Work Formula
Let Person $A$ take $x$ days and Person $B$ take $y$ days to complete a unit job individually.

1. **Individual Daily Rates**:
   - $A$'s 1-day work:
     $$E_A = \frac{1}{x}$$
   - $B$'s 1-day work:
     $$E_B = \frac{1}{y}$$

2. **Combined Daily Rate**:
   - When $A$ and $B$ work together, their daily contributions combine additively:
     $$E_{A+B} = E_A + E_B = \frac{1}{x} + \frac{1}{y} = \frac{x + y}{xy}$$

3. **Total Time Inversion**:
   - The total number of days $D_{A+B}$ required to complete the unit work together is the reciprocal of $E_{A+B}$:
     $$D_{A+B} = \frac{1}{E_{A+B}} = \frac{xy}{x + y}$$

---

## Extension to $n$ Workers and Partial Work

- For 3 workers $A, B, C$ taking $x, y, z$ days respectively:
  $$E_{A+B+C} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z} = \frac{xy + yz + zx}{xyz}$$
  $$D_{A+B+C} = \frac{xyz}{xy + yz + zx}$$

- **Partial Work Principle**:
  - If a worker works for $k$ days at efficiency $E = \frac{1}{D}$, the fraction of work completed is:
    $$W_{\text{done}} = k \cdot E = \frac{k}{D}$$
  - The remaining work is:
    $$W_{\text{rem}} = 1 - \frac{k}{D} = \frac{D - k}{D}$$

---

## Linked Practice Questions
- [[cds/math/notes/questions/q21|Q21: Alternating Work Cycle & Clock Completion]]
- [[cds/math/notes/questions/q38|Q38: Relative Efficiency & Difference in Days]]

---

## Variations
- [[cds/math/notes/variations/var24|Variation 24: Dynamic Non-Linear Fatigue & Variable Efficiency Cycle]]

---

## Navigation
- [[cds/math/notes/work|Time and Work Topic]]
- [[cds/math/math_overview|Subject Dashboard]]
