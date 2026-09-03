---
exam: "GATE CS"
subject: "Algorithms"
topic: "Multi-Topic Graph Algorithms"
tags: [gate-cs, algorithms, mst, shortest-path, chapter-variations]
date: 2026-09-03
---

# Multi-Topic Chapter Variations — Graph Algorithms

This note aggregates **Tier 3 Variations** that cross-cut multiple topics within **Algorithms** (e.g., combining Minimum Spanning Trees, Shortest Paths, and Disjoint Set Union data structures).

---

## 1. MST + Shortest Paths (Dijkstra vs Prim)

### Tier 3 Variation 3.1: Shortest Path Tree vs MST Equivalence
> **Problem**: Let $G = (V, E, w)$ be a connected, weighted graph with positive distinct edge weights. Under what necessary and sufficient condition on $G$ will the Shortest Path Tree (SPT) rooted at vertex $s \in V$ be identical to the unique Minimum Spanning Tree (MST) of $G$?

<details>
<summary>Click to view Solution & Analysis</summary>

**Solution**: The SPT rooted at $s$ is identical to the MST if and only if for every vertex $v \in V \setminus \{s\}$, the unique path from $s$ to $v$ in the MST is the shortest path in $G$. 

*Key Intuition*: Prim's algorithm picks edges based on minimum local edge weight $w(u, v)$, while Dijkstra's picks based on total path distance $d(s, u) + w(u, v)$. When bottleneck path costs coincide with cumulative path costs across all vertices, the two trees are identical.
</details>

---

## 2. MST + Disjoint Set Union (Kruskal Time Complexity)

### Tier 3 Variation 3.2: Inverse Ackermann Bottleneck
> **Problem**: If edge weights in graph $G$ are already sorted in $O(|E|)$ time using Counting Sort, what is the exact tight time complexity of Kruskal's algorithm to compute the MST using DSU with path compression and rank union?

<details>
<summary>Click to view Solution & Analysis</summary>

**Solution**: $O(|E| \cdot \alpha(|V|))$, where $\alpha$ is the slow-growing Inverse Ackermann function. Sorting is no longer the bottleneck ($O(|E|)$), so the DSU operations dominate.
</details>
