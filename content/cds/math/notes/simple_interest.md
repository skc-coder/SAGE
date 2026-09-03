---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Simple Interest"
difficulty: "Medium"
tags: [cds, elementary-mathematics, simple-interest, topic]
---

# Simple Interest

## Theory, Intuition & Formulas

Simple Interest ($SI$) represents linear compensation charged on the principal amount ($P$) borrowed over a period ($T$) at a specified rate ($R\%$) per annum.

### Core Axioms & Invariants

1. **Linear Interest Dynamics**:
   Simple Interest is accrued purely on the initial principal sum $P$ without compounding:
   $$SI = \frac{P \cdot R \cdot T}{100}$$

2. **Maturity Accumulation**:
   Total amount $A$ returned after $T$ years:
   $$A = P + SI = P \left(1 + \frac{R \cdot T}{100}\right)$$

3. **Rate Differential Invariant**:
   If interest rate increases by $\Delta R\%$ over time $T$, the incremental interest gained is linearly proportional:
   $$\Delta SI = \frac{P \cdot \Delta R \cdot T}{100}$$

---

## Subtopics & Specialized Questions

- [[cds/math/notes/subtopics/si_formula_rate|Fundamental SI & Rate Laws]]
- [[cds/math/notes/subtopics/si_dual_amounts|Multiple Amounts System]]
- [[cds/math/notes/subtopics/si_equated_partition|Equated Simple Interest Partitioning]]

### Linked Practice Questions
- [[cds/math/notes/questions/q44|Q44: Monthly Interest Principal Calculation]]
- [[cds/math/notes/questions/q45|Q45: Doubling Period Rate Percentage]]
- [[cds/math/notes/questions/q46|Q46: Dual Maturity Amount Rate & Principal Extraction]]
- [[cds/math/notes/questions/q47|Q47: Equated Interest Multi-Part Allocation]]

---

## Variations

- [[cds/math/notes/variations/var30|Variation 30: Variable Step-Rate Capital Allocation & Floating Rate Invariant]]

---

## Performance Overview

```mermaid
xychart-beta
    title "Topic Accuracy"
    x-axis ["SI Formula", "Dual Amounts", "Partitioning"]
    y-axis "Accuracy %" 0 --> 100
    bar [100, 100, 100]
```

```mermaid
pie title Simple Interest Difficulty
    "Standard Formula (Easy)" : 50
    "Dual Amounts (Medium)" : 30
    "Partitioning & Rate Change (Hard)" : 20
```

---

## Navigation
- [[cds/math/math_overview|Subject Dashboard]]
- [[cds/cds_overview|CDS Master Dashboard]]
