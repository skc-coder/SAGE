---
exam: "GATE CS"
subject: "Algorithms"
topic: "Minimum Spanning Trees"
subtopic: "Number of MSTs"
question_type: "Formulaic Edge Conditions"
tags: [gate-cs, algorithms, mst, graph-theory]
date: 2026-09-03
---

# Counting Minimum Spanning Trees — Formulaic Edge Conditions

## 1. Theory & Intuition

### Kruskal's & Cycle Property for MST Counting
When edge weights are determined by a formula $w(u, v) = f(u, v)$, determining the number of distinct MSTs relies on inspecting **equal weight edge choices** during Kruskal's algorithm execution.

> [!NOTE]
> **Cycle Property**: In any cycle $C$, if the maximum weight edge $e \in C$ is unique, then $e$ cannot belong to any MST. Conversely, if multiple edges in $C$ share the maximum weight, choices arise leading to multiple MSTs.

---

## 2. Logged Questions & Derivations

### Question 1: GATE CS 2021 Set 1 Q34
- **Source**: GATE CS 2021 Set 1 Q34
- **Status**: ❌ Wrong (Miscalculated edge weight equal-weight cycle)

#### Derivation & Fix
For a connected graph $G = (V, E)$ where vertices are indexed $1 \dots n$ and edge weight $w(i, j) = i + j$:
1. Edge weights grow monotonically with vertex indices.
2. Contracting lower-weight edges first reveals that cycle edges with identical sum $i+j$ allow mutually exclusive selections.

---

## 3. Novel Concept Variations

### Variation 1.1 (Underlying Cycle-Weight Choice)
> **Problem**: Let $G$ be a connected graph with $n$ vertices. Suppose all edges have distinct weights except for a single cycle $C = (v_1, v_2, v_3)$ where $w(v_1, v_2) = w(v_2, v_3) = w(v_3, v_1) = W$, and $W$ is strictly greater than all other edge weights in $G$. How many MSTs does $G$ have?

<details>
<summary>Click to view Solution & Intuition</summary>

Any MST must span all $n$ vertices. The distinct lower-weight edges form a set of components. To connect the cycle vertices without forming a cycle of weight $W$, we must pick exactly **2 out of the 3** edges of weight $W$.
Thus, there are $\binom{3}{2} = 3$ distinct MSTs.
</details>
