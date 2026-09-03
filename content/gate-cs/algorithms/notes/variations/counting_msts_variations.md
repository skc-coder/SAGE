---
exam: "GATE CS"
subject: "Algorithms"
topic: "Minimum Spanning Trees"
subtopic: "Number of MSTs"
question_type: "Formulaic Edge Conditions"
tags: [gate-cs, algorithms, mst, variations-note]
date: 2026-09-03
---

# Topic Synthesis Variations — Minimum Spanning Trees (Counting MSTs)

## 1. General Equal-Weight Cycle Theorem

> **Variation 2.1**: Let $G$ be a connected graph where $k$ edges share the same maximum weight $W$ on a cycle of length $k$, while all other $m-k$ edges have distinct weights strictly less than $W$. How many MSTs does $G$ possess?

> [!faq]- View Solution
> Since all $m-k$ smaller distinct edges are chosen unconditionally and form trees/forests, exactly $k-1$ edges of weight $W$ must be chosen from the cycle of $k$ edges to connect the components.
>
> $$ \text{Number of MSTs} = \binom{k}{k-1} = k $$
