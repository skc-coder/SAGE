## Definitions

- **Depth of root** = 0, its child = 1 (same as level)
- **Height h tree** → last level = h, root = 0
- **Leaves in a perfect tree of n nodes** = (n+1)/2 ⚠️ not (n-1)/2

---

## Types of Binary Trees

|Type|Property|
|---|---|
|**Full**|Every node has 0 or 2 children|
|**Complete**|All levels filled except possibly last (filled left to right)|
|**Perfect**|All internal nodes have 2 children, all leaves at same level|

---

## Key Formulas

### General

- $N = L + I$ → total nodes = leaves + internal nodes
- $1 + 2 + 2^2 + \dots + 2^k = 2^{k+1} - 1$ ← remember this!

### Perfect Tree of height h

| Property              | Formula       |
| --------------------- | ------------- |
| No. of levels         | h             |
| No. of leaves         | $2^h$         |
| No. of internal nodes | $2^h - 1$     |
| Total nodes           | $2^{h+1} - 1$ |

### Any Binary Tree of height h

| Property   | Formula       |
| ---------- | ------------- |
| Min nodes  | $h + 1$       |
| Max nodes  | $2^{h+1} - 1$ |
| Min leaves | $1$           |
| Max leaves | $2^h$         |

### Complete Binary Tree of height h

| Property  | Formula       |
| --------- | ------------- |
| Min nodes | $2^h$         |
| Max nodes | $2^{h+1} - 1$ |

---

## GATE PYQs

> **GATE CSE 2007** — Height = max edges in root-to-leaf path. Max nodes in BT of height h? **Answer: C → $2^{h+1} - 1$**

> **GATE CSE 2015 Set 1** — Height = longest root-to-leaf path length. Max and min nodes in BT of height 5? **Answer: A → 63 and 6** (Max = $2^6 - 1 = 63$, Min = $5 + 1 = 6$)

---

## Representation

- **Array** → suitable for complete binary trees (use parent/child index formulas)
- **Linked List** → general purpose

---

## Traversals

### Types (DFS)

- **Pre-order** → Root → Left → Right
- **In-order** → Left → Root → Right
- **Post-order** → Left → Right → Root

### Trick

> 1st visit = Pre | 2nd visit = In | 3rd visit = Post

### Inorder shortcut

> Project all nodes onto a horizontal plane → gives inorder directly


---

## Tree Construction

### What uniquely constructs a Binary Tree?

| Given                                      | Unique Tree?                                  |
| ------------------------------------------ | --------------------------------------------- |
| Inorder + Preorder                         | ✅ Yes (General BT)                            |
| Inorder + Postorder                        | ✅ Yes (General BT)                            |
| Preorder + Postorder                       | ❌ No (General BT)                             |
| Preorder + Postorder + **Full BT**         | ✅ Yes                                         |
| One traversal + fixed structure (e.g. CBT) | ✅ Yes                                         |
| Only Preorder or only Postorder            | ❌ No (root fixed, left/right split ambiguous) |
| Only Inorder                               | ❌ No (root not even clear)                    |

### Why Pre+Post alone fails

Root is fixed, but the remaining nodes can be placed entirely as left or right subtree → multiple trees possible.

### Why Pre+Post+Full BT works

Full BT forces 0 or 2 children → there must be a split, and it must be consistent in both traversals. 
The last consecutive node in postorder acts as the subtree root (like a "full stop").


---

## [[Catalan Number]]

$$C_n = \frac{1}{n+1}\binom{2n}{n}$$

**Used for:**

- Stack permutations
- No. of distinct binary trees with n nodes (given inorder / preorder / postorder alone)

| Formula                                 |                 |
| --------------------------------------- | --------------- |
| No. of **unlabelled** trees for n nodes | $C_n$           |
| No. of **labelled** trees for n nodes   | $C_n \times n!$ |

---

