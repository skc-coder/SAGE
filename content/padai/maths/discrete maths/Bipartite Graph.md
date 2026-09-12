---
tags: [graph-theory, discrete-mathematics, bipartite-graphs]
source: https://en.wikipedia.org/wiki/Bipartite_graph
created: 2026-03-13
---
# Key Concepts

| Concept                  | Meaning                                                    |
| ------------------------ | ---------------------------------------------------------- |
| Bipartite Graph          | Graph whose vertices can be divided into two disjoint sets |
| Bipartition              | The division $(U,V)$                                       |
| Balanced Bipartite Graph | $U=V$                                                      |
| Biregular Graph          | Equal degree within each partition                         |
| Complete Bipartite Graph | Every vertex in $U$ connected to every vertex in $V$       |
| Odd Cycle Rule           | Bipartite graphs contain **no odd cycles**                 |
| 2-Colorability           | Bipartite graphs require **only two colors**               |

---
# Bipartite Graph

In the field of [[moc graphs]] (a branch of [[Mathematics]]), a **Bipartite Graph** (also called a **Bigraph**) is a special type of [[Graph (Discrete Mathematics)|graph]] in which the **vertices** can be divided into two separate groups.

---

## Definition

> [!INFO] **Bipartite Graph Definition**
> A **bipartite graph** is a graph whose vertex set can be partitioned into two **disjoint** and **independent** sets such that **every edge connects a vertex from one set to the other set**.

Let the vertex set be divided into two parts:

- **$U$**
- **$V$**

These sets satisfy the following properties:

- $U \cap V = \varnothing$ (they are **disjoint**)
- Every edge connects a vertex in $U$ to a vertex in $V$
- There are **no edges connecting vertices within the same set**

---

## Mathematical Representation

A bipartite graph is often written as:

$$
G = (U, V, E)
$$

Where:

- $G$ → the **graph**
- $U$ → first set of vertices
- $V$ → second set of vertices
- $E$ → set of **edges**

Each edge in $E$ connects:

$$
u \in U \quad \text{to} \quad v \in V
$$

---

## Equivalent Characterization

> [!IMPORTANT] **Odd Cycle Property**
> A graph is **bipartite if and only if it does not contain any odd-length cycles.**

This property is one of the most important theoretical tests for determining whether a graph is bipartite.

---

## Graph Coloring Interpretation

The two sets $U$ and $V$ can be interpreted as a **two-coloring** of the graph.

### Coloring Scheme

- All vertices in **$U$** → colored **blue**
- All vertices in **$V$** → colored **red**

Since edges only connect vertices from different sets:

- Every edge connects **different colors**
- No two adjacent vertices share the same color

Thus:

> [!INFO] **2-Colorable Graph**
> A graph is **bipartite if and only if it is 2-colorable** (its [[Chromatic Number]] is ≤ 2).

---

### Non-Bipartite Example

> [!CAUTION] **Triangle Graph**
> A triangle graph cannot be bipartite.

Reason:

1. Color first vertex **blue**
2. Color second vertex **red**
3. Third vertex connects to both colors

Therefore:

- It cannot be assigned either color
- The graph **cannot be 2-colored**

This occurs because a **triangle contains an odd cycle (length = 3)**.

---

## Bipartition

The vertex sets $U$ and $V$ are called the **parts** of the graph.

> [!NOTE]
> If a bipartite graph is **not connected**, it may have **more than one valid bipartition**.

In such cases, the notation

$$
(U, V, E)
$$

is useful for specifying the particular bipartition used in an application.

---

## Balanced Bipartite Graph

If both vertex sets have equal size:

$$
|U| = |V|
$$

then the graph is called a:

> [!INFO] **Balanced Bipartite Graph**

Where:

- $|U|$ = number of vertices in $U$
- $|V|$ = number of vertices in $V$

---

## Biregular Bipartite Graph

If all vertices on the **same side** of the bipartition have the **same degree**, the graph is called:

> [!INFO] **Biregular Graph**

Meaning:

- All vertices in $U$ have identical degree
- All vertices in $V$ have identical degree

---

# Examples of Bipartite Graphs

## 1. Affiliation Networks

Bipartite graphs frequently appear when modeling **relations between two different classes of objects**.

### Example

A graph of:

- **Football Players**
- **Football Clubs**

Edges represent:

- A **player playing for a club**

This forms an **Affiliation Network**, commonly used in [[Social Network Analysis]].

---

## 2. Trees

> [!INFO]
> **Every [[Tree (Graph Theory)|tree]] is bipartite.**

Reason:

- Trees contain **no cycles**
- Therefore they **cannot contain odd cycles**

---

## 3. Even Cycle Graphs

> [!INFO]
> Cycle graphs with an **even number of vertices** are bipartite.

Example:

- $C_4$
- $C_6$
- $C_8$

But **odd cycles (like $C_3$ or $C_5$) are not bipartite.**

---

## 4. Planar Graphs with Even Faces

A **planar graph** is bipartite if **all faces have even length**.

Special cases include:

- **Grid Graphs**
- **Square Graphs**

Characteristics:

- Each inner face has **4 edges**
- Inner vertices usually have **4 or more neighbors**

---

# Complete Bipartite Graph

A very important class of bipartite graphs is the **Complete Bipartite Graph**.

It is denoted by:

$$
K_{m,n}
$$

Where:

- $m$ = number of vertices in set $U$
- $n$ = number of vertices in set $V$

---

## Definition

> [!INFO] **Complete Bipartite Graph**
> A graph in which **every vertex in $U$ connects to every vertex in $V$.**

Formally:

$$
G = (U, V, E)
$$

Where:

- $|U| = m$
- $|V| = n$

And:

$$
E = \{ (u,v) \mid u \in U,\ v \in V \}
$$

---

## Number of Edges

The total number of edges is:

$$
|E| = m \times n
$$

Thus:

$$
K_{m,n} \text{ has } mn \text{ edges}
$$

---

# Characterizations of Bipartite Graphs

A graph is bipartite if it satisfies **any one** of the following equivalent conditions.

---

## 1. Odd Cycle Characterization

> [!IMPORTANT]
> An **undirected graph** is bipartite **if and only if it contains no odd cycles**.

---

## 2. Two-Colorability

> [!IMPORTANT]
> A graph is bipartite **if and only if it can be colored using two colors**.

Mathematically:

$$
\chi(G) \le 2
$$

Where:

- $\chi(G)$ = **Chromatic Number**

---