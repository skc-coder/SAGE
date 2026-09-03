---
exam: "GATE CS"
subject: "Algorithms"
topic: "Minimum Spanning Trees"
subtopic: "Number of MSTs"
question_type: "Formulaic Edge Conditions"
source: "GATE CS 2021 Set 1 Q34"
status: "Wrong"
mistake_category: "Calculation Error"
tags: [gate-cs, algorithms, mst, question-note]
date: 2026-09-03
---

# GATE 2021 Set 1 Q34 — Counting MSTs (Formulaic Edge Conditions)

## 1. Question Context
- **Source**: GATE CS 2021 Set 1 Q34
- **Specialization**: Formulaic Edge Conditions ($w(i, j) = i + j$)
- **Status**: ❌ Wrong *(Calculation Error: Miscalculated equal-weight edge sum on cycle)*

---

## 2. Derivation & Solution
For a connected graph $G = (V, E)$ where vertices are indexed $1 \dots n$ and edge weight $w(i, j) = i + j$:
1. Edge weights grow monotonically with vertex indices.
2. Contracting lower-weight edges first reveals that cycle edges with identical sum $i+j$ allow mutually exclusive selections.

---

## 3. Tier 1: Direct Question Variations

> **Variation 1.1 (Edge Choice on Cycle)**: Suppose graph $G$ has vertices $\{1, 2, 3, 4\}$ with edges $e_1=(1,2)$, $e_2=(2,3)$, $e_3=(3,4)$, $e_4=(4,1)$, $e_5=(1,3)$ with the following edge weights:
>
> $$ w(e_1)=3, \quad w(e_2)=5, \quad w(e_3)=5, \quad w(e_4)=5, \quad w(e_5)=2 $$
>
> How many distinct MSTs can be formed?

> [!faq]- Click to view Solution
> Edge $e_5$ (weight $2$) and $e_1$ (weight $3$) are strictly chosen first. The remaining vertices require connecting via edges of weight $5$, yielding $3$ valid MST combinations.
