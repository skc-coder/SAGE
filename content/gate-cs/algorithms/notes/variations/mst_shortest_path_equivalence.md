---
exam: "GATE CS"
subject: "Algorithms"
topic: "Multi-Topic Graph Algorithms"
tags: [gate-cs, algorithms, mst, shortest-path, variation-note]
date: 2026-09-03
---

# MST vs Shortest Path Tree Equivalence

> **Problem**: Let $G = (V, E, w)$ be a connected, weighted graph with positive distinct edge weights. Under what necessary and sufficient condition on $G$ will the Shortest Path Tree (SPT) rooted at vertex $s \in V$ be identical to the unique Minimum Spanning Tree (MST) of $G$?

> [!faq]- View Solution
> The SPT rooted at $s$ is identical to the MST if and only if for every vertex $v \in V \setminus \{s\}$, the unique path from $s$ to $v$ in the MST is the shortest path in $G$.
>
> *Key Intuition*: Prim's algorithm picks edges based on minimum local edge weight $w(u, v)$, while Dijkstra's picks based on total path distance $d(s, u) + w(u, v)$. When bottleneck path costs coincide with cumulative path costs across all vertices, the two trees are identical.
