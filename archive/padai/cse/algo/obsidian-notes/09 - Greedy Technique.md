> **Source:** GO Classes — Notes by Quantum City (AIR 107) **Lectures:** 26a, 27a, 27c, 28a, 28b, 28d, 29a, 29b, 29c, 30b, 31a, 31c, 32a, 33c, 34a, 34e, 35a

---

> [!warning] Greedy May Fail! **Shopkeeper Example:** You need to give change of ₹30. You have one ₹25 note and three ₹10 notes.
> 
> - Greedy says: pick best available → you choose ₹25
> - Now you can't make ₹5 change → **method fails!**
> 
> ∴ Greedy might **not** work sometimes.

---

## 4.1 Shortest Path Problem

> Single source shortest path — find shortest path (by weight) from one source to all destinations.

### Attempts to Solve

| Attempt       | Method                                                | Issue                                                             |
| ------------- | ----------------------------------------------------- | ----------------------------------------------------------------- |
| **Attempt 1** | Brute force — find shortest among all paths           | Total paths = $2^k$, Time = $O(2^k)$ → Exponential TC             |
| **Attempt 2** | BFS — convert edge weights to dummy nodes of weight 1 | Works but if weights are too high, number of dummy nodes explodes |
| **Final**     | **Dijkstra's Algorithm**                              | ✅ Efficient!                                                      |

> [!tip] Key Property **Subpaths of the shortest path are also shortest paths.**

---

### 4.1.1 Dijkstra's Algorithm

> _Lecture 26a_

### Core Idea

- Each node holds a value = **shortest possible distance at that moment**
- Initially all nodes have $\infty$
- **Pick min → go to that node → relax all outgoing edges → repeat until all nodes visited**
- **Relax** = assign minimum distance to neighbors of selected node

### RELAX Procedure

```
RELAX(u, v, w):
    if (d[v] > d[u] + w):
        d[v] = d[u] + w
        parent[v] = u
```

### Dijkstra Code

```python
Dijkstra(G, s):
1    key[v] = ∞  for all v in V
2    key[s] = 0
3    S = ∅
4    initialize priority queue Q to all vertices
5    while Q is not empty:
6        u = EXTRACT-MIN(Q)
7        S = S ∪ {u}
8        for each adjacent v of u:
9            RELAX(u, v, w)
```

---

### Time Complexity of Dijkstra

> _Lecture 27c_

> [!note] Key Observation Every edge is relaxed **exactly once**.

**Three priority queue operations used:**

- `INSERT` (implicit in line 4)
- `EXTRACT-MIN` (line 6)
- `DECREASE-KEY` (implicit in RELAX at line 9)

$$\text{Total TC} = \sum_{u \in V} T(\text{ExtractMin}) + \sum_{u \in V} \left(\sum_{v \in u.\text{neighbors}} T(\text{DecreaseKey})\right)$$

> [!info] Adjacency Matrix Note:
>  In adjacency matrix, for finding neighbors you traverse a whole row of 1s and 0s. 
>  For 1s: $\deg(v) \times T(\text{DecreaseKey})$ 
>  For 0s: $O(1) \times (V - \deg(v)) \rightarrow T(\text{ExtractKey})$ $$\therefore TC = V \log V + E \log V + V^2$$

**General Formulas:**

| Representation   | TC                                                                     |
| ---------------- | ---------------------------------------------------------------------- |
| Adjacency List   | $V \times T(\text{ExtractMin}) + E \times T(\text{DecreaseKey})$       |
| Adjacency Matrix | $V \times T(\text{ExtractMin}) + E \times T(\text{DecreaseKey}) + V^2$ |

### Full Complexity Table

| Graph Representation | Priority Queue | Time Complexity        |
| -------------------- | -------------- | ---------------------- |
| Adjacency List       | Heap           | $(E + V) \log V$       |
| Adjacency Matrix     | Heap           | $(E + V) \log V + V^2$ |
| Adjacency List       | Unsorted Array | $V^2 + E$              |
| Adjacency Matrix     | Unsorted Array | $V^2 + E$              |
| Adjacency List       | Sorted Array   | $V + EV$               |
| Adjacency Matrix     | Sorted Array   | $V + EV + V^2$         |
| Adjacency List       | Fibonacci Heap | $V \log V + E$         |
| Adjacency Matrix     | Fibonacci Heap | $V \log V + E + V^2$   |

> [!important] For **RELAX** procedure:
> 
> - Using **Heap** → $O(\log n)$ for decrease-min
> - Using **Array** → $O(1)$ for decrease-min

---

### Dijkstra on Negative Edges?

> _Lecture 27a_

> [!failure] Dijkstra FAILS on Negative Edges
> 
> - In first iteration, Dijkstra assumes the minimum distance node is finalized
> - With negative edges, a later path via another node could give a shorter distance
> - Node 3 gets dequeued with wrong distance → algorithm ignores it
> 
> **Example:** Node 5 min distance should be 1, but Dijkstra gives 2, because node 3 gets dequeued early.

**Idea: Add weight to make all edges non-negative?**

- Looks correct, works for some graphs
- **Fails as a general solution** — adding uniform weight changes relative shortest paths on longer routes
    - Original shortest = 10 weight path
    - After +2: shortest becomes 17 weight path ❌

> [!warning] Negative Cycles
> 
> - Undirected graph with even one negative edge → can create a negative cycle
> - Example: A—1—B—(-2)—C—3—D → shortest = 1-2+3 = 2, but Dijkstra loops: B→C→B→C→... infinitely
> - **We need an algorithm that at least detects negative weight cycles**

---

### 4.1.2 Shortest Path in Directed Acyclic Graph (DAG)

> _Lecture 28a_

> [!success] DAG handles Negative Weights! 

How?

- No cycles → no infinite loops → negative edges are safe!
- Relaxation from all possible paths to a node are considered before finally going on it.

This is not brute force because we use a possible topological order of the graph to guide our relaxation.

### DAG Shortest Path Algorithm

```
Shortest path of DAG:
1: Set d[s] = 0  and  d[v] = ∞  for all v ≠ s
2: Topologically sort the vertices of G          → O(V + E)
3: for each vertex u in topologically sorted order:
4:     for every edge (u, v):
5:         RELAX(u, v)
6:     end for
7: end for
```

> We do topological ordering first $O(V+E)$
> For every vertex we are doing $1 + \deg(v)$ work.
$$\therefore \text{TC} = O(V + E)$$


### Comparison of Approaches

| Algorithm        | Strategy                                         | Notes                                       |
| ---------------- | ------------------------------------------------ | ------------------------------------------- |
| **Dijkstra**     | Pick min → relax outgoing edges                  | No negative edges                           |
| **DAG SP**       | Pick in topological order → relax outgoing edges | Handles negatives, no cycles                |
| **Bellman-Ford** | Relax edges in any order, $(V-1)$ times          | Handles negatives + detects negative cycles |

---

### 4.1.3 Bellman-Ford Algorithm

> _Lecture 28b_

> [!quote] Core Principle
> If we relax in the order of shortest path (along with intermixed other relaxations), we will get the shortest path cost.

### Why This Works — Path Relaxation Property

- There always exists **one shortest relaxation sequence**
- Inserting extra relaxations in between doesn't change the final shortest path cost
- To find shortest path, the **shortest relaxation sequence must at least be covered**
- This is called the **path-relaxation property**

**Example:** Relaxation path = $e_5, e_4, e_3, e_2, e_8$ You can add any relaxations (edges) **between** this sequence → still gives shortest path cost ✅

### Algorithm

```
Bellman_Ford(G, s):
    d[v] = ∞  for all v in V
    d[s] = 0
    for i = 1 to V - 1:
        for each edge (u, v) in E:         → O(VE)
            RELAX(u, v, w)
    for each edge (u, v) in E:
        if (d[v] > d[u] + w):
            return false                   // Negative cycle detected!
    return true
```

> [!note] Worst Case When $E = O(V^2)$: $TC = O(V^3)$

> [!important] Key Property **If we run k iterations, we have the shortest path to all vertices reachable via at most k edges.**

---

### Why Bellman-Ford Works (Proof Sketch)

> _Lecture 28d_

Suppose shortest path is: $S \xrightarrow{2} V_1 \xrightarrow{1} V_2 \xrightarrow{2} V_3 \xrightarrow{3} V_4 \cdots \xrightarrow{1} V_k$

- **1st iteration:** Somewhere edge $S \to V_1$ will relax → never changes (it's shortest)
- **2nd iteration:** Somewhere $V_1 \to V_2$ will relax → min cost never changes (two shortest paths)
- **...kth iteration:** $V_{k-1} \to V_k$ definitely relaxes ✅
- Thus all shortest path edges are relaxed by the $k$th iteration

### Negative Cycle Detection

- After $V-1$ relaxations → shortest paths are finalized
- Do **one more** relaxation pass
    - If no change → **no negative cycle**
    - If some $d[v]$ changes → **negative cycle exists!**

> [!caution] If negative cycle exists → Bellman-Ford **fails** to find shortest path, but **will detect** it.

### Bellman-Ford with Early Termination

```
Bellman_Ford(G, s):                    RELAX(u, v, w):
    d[v] = ∞  for all v in V              if (d[v] > d[u] + w):
    d[s] = 0                                  d[v] = d[u] + w
    for i = 1 to V - 1:                       relaxed = true
        relaxed = false
        for each edge (u, v) in E:
            RELAX(u, v, w)
        if (relaxed == false): break   // Early exit if nothing relaxed

    for each edge (u, v) in E:
        if (d[v] > d[u] + w):
            return false
    return true
```

> [!summary] Dijkstra vs Bellman-Ford
> 
> - **Dijkstra:** Fast but ❌ doesn't work for negative weight edges
> - **Bellman-Ford:** Slower but ✅ works for negative edges, detects negative cycles

---

## 4.2 Minimum Spanning Trees (MST)

> _Lecture 29a_

> [!definition] Spanning Tree A **spanning tree** of an undirected graph is a connected subgraph that:
> 
> - Contains **all vertices**
> - Has **no cycles**

> [!definition] MST **Minimum Spanning Tree** = spanning tree with **minimum total edge weight**
> 
> A MST connects all vertices while minimizing the total weight of edges used.

### Brute Force for MST

- $n$ vertices → $2^n$ possible combinations (include/exclude each edge)
- **Spanning trees in complete graph** $K_n$ = $n^{n-2}$
- **Spanning trees in complete bipartite graph** $K_{m,n}$ = $m^{n-1} \cdot n^{m-1}$
- Listing all and taking minimum → **exponential time** ❌

---

### 4.2 Two Properties of MSTs

> _Lecture 29b_ — (Assuming all edge weights are **distinct**)

> [!tip] Cut Property **The smallest edge crossing any cut must be part of ALL MSTs.**

> [!tip] Cycle Property **The largest edge on any cycle is NEVER in any MST.**

### Number of Cuts

- Graph with $n$ vertices → $2^n$ possible cuts
- But ${a}{b,c,...}$ and ${b,c,...}{a}$ are counted twice → divide by 2
- Empty set partition is invalid $$\therefore \text{Total valid cuts} = 2^{n-1} - 1$$

### Propositions

> [!note] From Cut Property A graph has a **unique MST** if, for every cut, there is a **unique light edge** crossing it.
> 
> - Converse is **NOT** true in general
> - But if **every edge weight is distinct** → bijection (both directions hold)

> [!note] From Cycle Property An edge is **not in any MST** if and only if it is the **unique heaviest edge** in some cycle.

---

### 4.2.1 Kruskal's Algorithm

> _Lecture 29c_

### Generic MST Framework

```
MST(G, w):
    A = ∅
    while (A does not form a spanning tree):
        find an edge (u, v) that is safe     // safe = must be included in MST
        A = A ∪ {(u, v)}
    return A
```

Two algorithms guarantee a safe edge each iteration:

1. **Kruskal's Algorithm**
2. **Prim's Algorithm**

### Kruskal's Algorithm

```
Kruskal(G):
    sort edges in increasing order        → O(E log E)
    T = ∅
    for each edge e1 in sorted order:
        if e1 ∪ T does not make a cycle:
            T = T ∪ {e1}
    return T
```

**Cycle detection approaches:**

- Using **DFS**: $TC = E \log E + E \times O(V + E)$
- Using **Union-Find data structure**: cycle check in $O(1)$

$$\therefore \text{Kruskal's TC with Union-Find} = O(E \log E)$$

> [!question] Can Kruskal's handle negative weights? **Yes!** Negative weights have no impact — we are only **sorting edges**, not finding paths.

---

### 4.2.2 Prim's Algorithm

> _Lecture 30b, 31a_

### Core Idea

> Take any set of vertices → the **least weight edge in the cut** is always part of MST (by cut property)

> [!question] Do we need to detect cycles in Prim's? **No!** Selected vertices are dequeued and never revisited → no edges between selected and past dequeued vertices → no cycles possible.

### Prim's vs Dijkstra's — Side by Side

| **Dijkstra**   | **Prim's**                            |                            |
| -------------- | ------------------------------------- | -------------------------- |
| **Goal**       | Closest vertex to **source**          | Closest vertex to **tree** |
| **Key update** | `d[v] > d[u] + w` → `d[v] = d[u] + w` | `d[v] > w` → `d[v] = w`    |
| **TC**         | Same as Prim's                        | Same as Dijkstra's         |

```
Dijkstra(G, s):                         Prims(G, s):
1  key[v] = ∞ for all v in V           1  key[v] = ∞ for all v in V
2  key[s] = 0                          2  key[s] = 0
3  S = ∅                               3  S = ∅
4  init priority queue Q               4  init priority queue Q
5  while Q is not empty:               5  while Q is not empty:
6      u = EXTRACT-MIN(Q)              6      u = EXTRACT-MIN(Q)
7      S = S ∪ {u}                     7      S = S ∪ {u}
8      for each adjacent v of u:       8      for each adjacent v of u:
9          if v ∈ Q and d[v] > d[u]+w  9          if v ∈ Q and d[v] > w
10             d[v] = d[u] + w         10             d[v] = w
11             // decrease key         11             // decrease key
12             parent[v] = u           12             parent[v] = u
```

> [!important] Prim's Priority **Priority of a node = distance of that node from the MST** (the value written on top of the node). That determines its priority in the queue.

---

### 4.2.3 MST with Edge Modification

> _Lecture 31c_

> [!question] If G has a cycle and edge e has minimum weight on that cycle → must e be in every MST? **This looks true but is FALSE!** (counter-example exists)

### 4 Cases When an Edge Weight Changes

#### Case 1: Edge IS in MST, weight DECREASES

> [!success] Trivial Decreasing a MST edge weight → **same MST** as before. No change needed.

#### Case 2: Edge is NOT in MST, weight DECREASES

> [!warning] Action Required
> 
> 1. **Add** this edge to the MST → creates **exactly 1 cycle**
> 2. By **cycle property**: find and **remove** the highest weight edge on that cycle
> 3. Use DFS/BFS to find the cycle
> 
> **Complexity: $O(V + E)$**

#### Case 3: Edge IS in MST, weight INCREASES

> [!warning] Action Required
> 
> 1. **Remove** this edge from MST → creates **2 disconnected components**
> 2. Find both components: $O(V + E)$
> 3. Find crossing edges: $O(E)$
> 4. Find min among them: $O(E)$
> 5. Compare and add best crossing edge
> 
> **Total: $O(V+E) + O(E) + O(E) + O(1) = O(V+E)$**

#### Case 4: Edge is NOT in MST, weight INCREASES

> [!success] Trivial Edge not in MST → increasing it further → **still won't be in MST**. MST stays the same.

---

## 4.3 Some More Greedy Algorithms

### 4.3.1 Huffman Encoding

> _Lecture 32a_

### Optimal Codes Problem

- **Input:** Distribution/frequencies of characters
- **Output:** A way to encode characters as efficiently (compactly) as possible

**Example:** A: 45 | B: 13 | C: 12 | D: 16 | E: 9 | F: 5

- Using fixed 3 bits per character: A needs $45 \times 3 = 135$ bits
- Goal: **minimize total bits (ASAP)**

### Prefix-Free Code

> [!definition] A code is **prefix-free** if no codeword is a prefix of another codeword. This ensures **unambiguous decoding**.

|Code 1 ✅|Code 2 ❌|Code 3 ❌|
|---|---|---|
|00|011|**01**|
|11|110|**10**|
|100|0011|0001|
|011|**1100**|0010|
|010|**1010**|0100|

### Huffman Coding — The Solution!

> [!success] Huffman's Greedy Strategy **Greedily build subtrees by merging, starting with the 2 most infrequent letters.** → Produces **prefix-free code** that is **optimal**!

**Example — Build tree for A:45, B:13, C:12, D:16, E:9, F:5:**

```
Step 1: Merge F(5) + E(9) = 14
Step 2: Merge C(12) + B(13) = 25
Step 3: Merge 14 + D(16) = 30
Step 4: Merge 25 + 30 = 55
Step 5: Merge A(45) + 55 = 100 (root)
```

**Final Tree:**

```
           (100)
          0/    \1
        (A:45)  (55)
               0/   \1
            (25)    (30)
           0/  \1  0/  \1
         (C:12)(B:13)(14)(D:16)
                    0/ \1
                  (F:5)(E:9)
```

### Huffman Code

```
HUFFMAN(C):
    n = |C|
    Q = C                        // min-priority queue by frequency
    for i = 1 to n - 1:
        x = Extract-Min(Q)
        y = Extract-Min(Q)
        z.freq = x.freq + y.freq
        Insert(Q, z)
    return Extract-Min(Q)
```

> [!note]
> 
> - $2(n-1)$ extract-min operations
> - **Time Complexity: $O(n \log n)$**
> - Variations: can use **probability** of occurrence instead of count

---

### Optimal Merge Pattern

> _Lecture 33c_

- **Input:** Set of files of different lengths
- **Output:** Optimal sequence of two-way merges to obtain a single file
- Structure is **just like Huffman** — merge smallest files first

**Example: N = 3, files (q1, q2, q3) = (30, 20, 10)**

|Merge Order|Cost|
|---|---|
|1, 2, 3|50 + 60 = **110**|
|1, 3, 2|40 + 60 = **100**|
|2, 1, 3|50 + 60 = **110**|
|2, 3, 1|30 + 60 = **90** ✅|
|3, 1, 2|40 + 60 = **100**|
|3, 2, 1|30 + 60 = **90** ✅|

> Optimal = merge smallest two first (like Huffman) → min cost = 90

---

### 4.3.2 Interval Scheduling Problem

> _Lecture 34a_

- **Input:** Set of intervals (activities with start & finish times)
- **Output:** **Maximum subset of non-overlapping intervals**

### Problem Setup

- $n$ activities ${a_1, a_2, \ldots, a_n}$
- Each $a_i$ has start time $s_i$ and finish time $f_i$, where $0 \leq s_i < f_i < \infty$
- Activity $a_i$ occupies half-open interval $[s_i, f_i)$
- Activities $a_i$ and $a_j$ are **compatible** if: $s_i \geq f_j$ OR $s_j \geq f_i$

**Example Table:**

|$i$|1|2|3|4|5|6|7|8|9|10|11|
|---|---|---|---|---|---|---|---|---|---|---|---|
|$s_i$|1|3|0|5|3|5|6|8|8|2|12|
|$f_i$|4|5|6|7|9|9|10|11|12|14|16|

- ${a_3, a_9, a_{11}}$ — mutually compatible but NOT maximum
- ${a_1, a_4, a_8, a_{11}}$ — **largest subset** ✅
- ${a_2, a_4, a_9, a_{11}}$ — also a largest subset ✅

### Ideas Evaluated

|Idea|Strategy|Result|
|---|---|---|
|**Idea 1**|Pick interval of **minimum size**|❌ Fails — e.g., one big interval blocks many small ones|
|**Idea 2**|Pick interval overlapping **minimum others**|❌ Fails — counter-example exists|
|**Idea 3**|Pick interval with **earliest finish time**|✅ **Optimal!**|

> [!success] Greedy Choice: Earliest Finish Time Repeatedly pick the interval with the **earliest finish time**, discard all conflicting intervals, and repeat. This works for **every case** and is **provably optimal**.

> [!question] Does "choose interval that ends LAST" work? **No!** — Counter-example exists ❌

> [!tip] Another valid optimal strategy "Choose the interval that **starts last**, discard all conflicting intervals, and recurse." ✅

---

### 4.3.2 (cont.) — Job Scheduling with Deadlines

> _Lecture 34e_

|Job|J1|J2|J3|J4|J5|J6|J7|
|---|---|---|---|---|---|---|---|
|**Deadline**|9|1|5|7|4|10|5|
|**Profit**|15|2|18|1|25|20|8|

### Algorithm Steps

1. **Step 1:** Sort all jobs in **decreasing order of profit** → $O(n \log n)$
2. **Step 2:** Initialize array of size = **max deadline** → $O(n)$
3. **Step 3:** Take max profit job, search from the **right side** of array for slot $i$ where deadline $\leq i$ (linear search) → $O(n^2)$ overall
4. **Step 4:** Repeat Step 3 for all jobs

**Sorted order:** J5(25) → J6(20) → J3(18) → J1(15) → J7(8) → J2(2) → J4(1)

**Final Schedule:**

|Slot|0|1|2|3|4|5|6|7|8|9|10|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Job||J2||J7|J5|J3||J4||J1|J6|

---

### 4.3.3 Fractional Knapsack

> _Lecture 35a_

- **Goal:** Choose items (fractions allowed) such that **total profit is maximized**

### Ideas

|Idea|Strategy|Result|
|---|---|---|
|**Idea 1**|Pick items with **maximum profit**|❌ Not working (ignores weight)|
|**Idea 2**|Pick by **profit/weight ratio** (value per unit weight)|✅ **Optimal!**|

### Algorithm

1. Compute $\frac{\text{profit}}{\text{weight}}$ for all items
2. Sort in **decreasing order** of $p/w$ → largest ratio first
3. Greedily fill the knapsack

> [!success] Time Complexity **$O(n)$** — surprisingly efficient!

**Visual Example (Knapsack capacity = 50):**

|Item|Weight|Profit|P/W|
|---|---|---|---|
|Item 1|10|$60|6.0|
|Item 2|20|$100|5.0|
|Item 3|30|$120|4.0|

- Greedy picks item 1 (ratio 6) + item 2 (ratio 5) + 20/30 of item 3
- Total = $60 + $100 + $80 = **$240** ✅ (Optimal)

---

## 📊 Algorithm Comparison Summary

|Algorithm|Graph Type|Negative Edges|Negative Cycle Detection|Time Complexity|
|---|---|---|---|---|
|**Dijkstra**|Any directed|❌ No|❌ No|$(E+V)\log V$ (adj list + heap)|
|**DAG SP**|DAG only|✅ Yes|N/A (no cycles)|$O(V+E)$|
|**Bellman-Ford**|Any directed|✅ Yes|✅ Yes|$O(VE)$|
|**Kruskal's**|Undirected (MST)|✅ Yes|N/A|$O(E \log E)$|
|**Prim's**|Undirected (MST)|✅ Yes|N/A|Same as Dijkstra|

---

## 🔗 Topic Map

```
Greedy Algorithms
├── Shortest Path
│   ├── Dijkstra (non-negative weights)
│   ├── DAG Shortest Path (topological order)
│   └── Bellman-Ford (negative weights + cycle detection)
├── Minimum Spanning Tree
│   ├── Properties (Cut & Cycle)
│   ├── Kruskal's (sort edges + union-find)
│   ├── Prim's (grow tree greedily)
│   └── MST under edge modification (4 cases)
└── Other Greedy
    ├── Huffman Encoding (optimal prefix-free codes)
    ├── Optimal Merge Pattern
    ├── Interval Scheduling (earliest finish time)
    ├── Job Scheduling with Deadlines
    └── Fractional Knapsack (profit/weight ratio)
```

---

_Made by Quantum City — AIR 107 | GO Classes_