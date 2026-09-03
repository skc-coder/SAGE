---
exam: "GATE CS"
subject: "Algorithms"
topic: "Minimum Spanning Trees"
subtopic: "Uniqueness"
question_type: "Distinct Edge Weights Theorem"
tags: [gate-cs, algorithms, mst, uniqueness]
date: 2026-09-03
---

# Minimum Spanning Trees — Uniqueness & Distinct Weights Theorem

## 1. Theory & Intuition

### Cut & Cycle Theorems for Unique MSTs
- **Distinct Weights Theorem**: If all edge weights in a connected weighted graph $G$ are distinct, then $G$ has a **unique** minimum spanning tree.
- **Cut Property**: For any cut $C$ of graph $G$, if the weight of an edge $e$ in $C$ is strictly smaller than the weights of all other edges in $C$, then $e$ belongs to every MST of $G$.

---

## 2. Logged Questions & Derivations

### Question 1: GATE CS 2018 Q12
- **Source**: GATE CS 2018 Q12
- **Status**: ✅ Correct

#### Derivation
Using the Cut Property, distinct edge weights guarantee that at every step of Prim's or Kruskal's algorithm, the minimum weight edge crossing a cut is unique, preventing any branching choices.

---

## 3. Novel Concept Variations

### Variation 1.1 (Converse Property Test)
> **Problem**: Is it possible for a connected graph $G$ with *some duplicate edge weights* to still possess a unique MST? Provide a condition or counterexample.

<details>
<summary>Click to view Solution & Intuition</summary>

**Yes**. Distinct edge weights are a *sufficient* condition, but not a *necessary* condition for MST uniqueness. For example, if duplicate weight edges belong to disjoint cuts and never form cycles of equal-weight max edges, the MST remains unique.
</details>
