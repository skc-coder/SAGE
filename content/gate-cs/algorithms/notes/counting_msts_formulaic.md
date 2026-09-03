---
exam: "GATE CS"
subject: "Algorithms"
topic: "Minimum Spanning Trees"
subtopic: "Number of MSTs"
question_type: "Formulaic Edge Conditions"
tags: [gate-cs, algorithms, mst, topic-hub]
date: 2026-09-03
---

# Counting Minimum Spanning Trees — Topic Executive Hub

## 1. Executive Theory & Intuition

### Kruskal's & Cycle Property for MST Counting
When edge weights are determined by a formula $w(u, v) = f(u, v)$, determining the number of distinct MSTs relies on inspecting **equal weight edge choices** during Kruskal's algorithm execution.

> [!NOTE]
> **Cycle Property**: In any cycle $C$, if the maximum weight edge $e \in C$ is unique, then $e$ cannot belong to any MST. Conversely, if multiple edges in $C$ share the maximum weight, choices arise leading to multiple MSTs.

---

## 2. Index of Logged Questions & Variations

- [[content/gate-cs/algorithms/notes/questions/gate_2021_q34_counting_msts|GATE 2021 Set 1 Q34 — Formulaic Edge Conditions ($w(i, j) = i+j$)]] `[Status: ❌ Wrong | Mistake: Calculation Error]`

---

## 3. Tier 2: Topic Synthesis Variations

> **Topic Variation 2.1 (General Equal-Weight Cycle Theorem)**: Let $G$ be a connected graph where $k$ edges share the same maximum weight $W$ on a cycle of length $k$, while all other $m-k$ edges have distinct weights strictly less than $W$. How many MSTs does $G$ possess?

> [!faq]- Click to view Solution
> Since all $m-k$ smaller distinct edges are chosen unconditionally and form trees/forests, exactly $k-1$ edges of weight $W$ must be chosen from the cycle of $k$ edges to connect the components.
>
> $$ \text{Number of MSTs} = \binom{k}{k-1} = k $$
