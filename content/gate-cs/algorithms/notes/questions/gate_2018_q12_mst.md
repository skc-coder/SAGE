---
exam: "GATE CS"
subject: "Algorithms"
topic: "Minimum Spanning Trees"
subtopic: "Uniqueness"
question_type: "Distinct Edge Weights Theorem"
source: "GATE CS 2018 Q12"
status: "Correct"
tags: [gate-cs, algorithms, mst, question-note]
date: 2026-09-03
---

# GATE 2018 Q12

> **Original Question**: Let $G = (V, E)$ be a connected graph with distinct edge weights. Is the Minimum Spanning Tree of $G$ guaranteed to be unique?

> [!faq]- View Solution & Derivation
> Using the Cut Property, distinct edge weights guarantee that at every step of Prim's or Kruskal's algorithm, the minimum weight edge crossing a cut is unique, preventing any branching choices. Thus, the MST is strictly unique.

---

## Direct Question Variations

> **Variation 1.1 (Cut Choice Test)**: If all edge weights in $G$ are distinct, is the maximum weight edge of $G$ guaranteed to be excluded from every MST of $G$?

> [!faq]- View Solution
> **No**. The maximum weight edge of the entire graph is only excluded if it lies on a cycle (by the Cycle Property). If the maximum edge is a bridge (cut-edge), it MUST be included in the MST to keep the graph connected.
