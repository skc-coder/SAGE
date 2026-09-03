---
exam: "GATE CS"
subject: "Algorithms"
topic: "Multi-Topic Graph Algorithms"
tags: [gate-cs, algorithms, mst, dsu, variation-note]
date: 2026-09-03
---

# Kruskal DSU Complexity

> **Problem**: If edge weights in graph $G$ are already sorted in $O(|E|)$ time using Counting Sort, what is the exact tight time complexity of Kruskal's algorithm to compute the MST using DSU with path compression and rank union?

> [!faq]- View Solution
> $O(|E| \cdot \alpha(|V|))$, where $\alpha$ is the slow-growing Inverse Ackermann function. Sorting is no longer the bottleneck ($O(|E|)$), so the DSU operations dominate.
