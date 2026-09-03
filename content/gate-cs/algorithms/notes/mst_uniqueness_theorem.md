---
exam: "GATE CS"
subject: "Algorithms"
topic: "Minimum Spanning Trees"
subtopic: "Uniqueness"
question_type: "Distinct Edge Weights Theorem"
tags: [gate-cs, algorithms, mst, uniqueness]
date: 2026-09-03
---

# MST Uniqueness

## 1. Core Theory & Intuition
- **Distinct Weights Theorem**: If all edge weights in a connected weighted graph $G$ are distinct, then $G$ has a **unique** minimum spanning tree.
- **Cut Property**: For any cut $C$ of graph $G$, if the weight of an edge $e$ in $C$ is strictly smaller than the weights of all other edges in $C$, then $e$ belongs to every MST of $G$.

---

## 2. Logged Questions
- ✅ **[[content/gate-cs/algorithms/notes/questions/gate_2018_q12_mst|GATE 2018 Q12: Distinct Edge Weights Theorem]]**

---

## 3. Topic Variations & Synthesis
> **Variation 1 (Converse Property Test)**: Is it possible for a connected graph $G$ with *some duplicate edge weights* to still possess a unique MST? Provide a condition or counterexample.

> [!faq]- View Solution
> **Yes**. Distinct edge weights are a *sufficient* condition, but not a *necessary* condition for MST uniqueness. For example, if duplicate weight edges belong to disjoint cuts and never form cycles of equal-weight max edges, the MST remains unique.
