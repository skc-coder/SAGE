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

#### Derivation & Solution
For a connected graph $G = (V, E)$ where vertices are indexed $1 \dots n$ and edge weight $w(i, j) = i + j$:
1. Edge weights grow monotonically with vertex indices.
2. Contracting lower-weight edges first reveals that cycle edges with identical sum $i+j$ allow mutually exclusive selections.

#### Tier 1: Direct Question Variations (GATE '21 Q34)
> **Variation 1.1 (Edge Choice on Cycle)**: Suppose graph $G$ has vertices $\{1, 2, 3, 4\}$ with edges $e_1=(1,2), e_2=(2,3), e_3=(3,4), e_4=(4,1), e_5=(1,3)$ with weights $w(e_1)=3, w(e_2)=5, w(e_3)=5, w(e_4)=5, w(e_5)=2$. How many distinct MSTs can be formed?

<details>
<summary>Click to view Solution</summary>

Edge $e_5$ (weight 2) and $e_1$ (weight 3) are strictly chosen first. The remaining vertices require connecting via edges of weight 5, yielding 3 valid MST combinations.
</details>

---

## 3. Tier 2: Topic Synthesis Variations (Counting MSTs Note Level)

> **Topic Variation 2.1 (General Equal-Weight Cycle Theorem)**: Let $G$ be a connected graph where $k$ edges share the same maximum weight $W$ on a cycle of length $k$, while all other $m-k$ edges have distinct weights strictly less than $W$. How many MSTs does $G$ possess?

<details>
<summary>Click to view Solution</summary>

Since all $m-k$ smaller distinct edges are chosen unconditionally and form trees/forests, exactly $k-1$ edges of weight $W$ must be chosen from the cycle of $k$ edges to connect the components.
Number of MSTs = $\binom{k}{k-1} = k$.
</details>
