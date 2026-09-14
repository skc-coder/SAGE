## 1. Definition

A **Binary Search Tree** is a binary tree where:

- All nodes in the **left subtree** of a node are **strictly less than** the node's value
- All nodes in the **right subtree** of a node are **strictly greater than** the node's value
- **No duplicate values** are stored in a BST
- This property holds **recursively** for every subtree

> [!important] Every value to the **left** is **smaller**, every value to the **right** is **greater**. No exceptions.

---

## 2. Traversal

- Inorder traversal always produces a **sorted ascending sequence**
- Multiple tree shapes (different roots) can produce the same inorder → inorder alone **cannot** reconstruct a unique BST
- Given a **fixed BST structure** only **one** valid key-to-node mapping exists

|Traversal|Uniquely determines BST?|
|---|---|
|Pre-order|✅ Yes|
|Post-order|✅ Yes|
|Inorder|❌ No|

---

## 3. BST Construction
### Zig-Zag Pattern (Chain of height h, nodes = h+1)

A zig-zag BST is one where at each level you choose to go left or right (no node has two children):

Number of possible structures for hieght h=$2^{h-1}$ 

- At each level: **2 choices** (insert as left child or right child)
- The **last node** is fixed (only one spot left) → `h - 1` free choices
- Each structure corresponds to a **unique insertion order**

> [!note] This is also used in the GATE CSE 2016 question.

## 4. Operations
### 3.1 Search

```
Step 1: Start at root
Step 2: If key < current node → go LEFT, repeat
Step 3: If key > current node → go RIGHT, repeat
Step 4: If key == current node → FOUND ✓
Step 5: If leaf node reached and key not found → NOT FOUND ✗
```

---

### 3.2 Insertion

- Same logic as search — traverse until you find the correct empty spot
- When you reach a leaf node:
    - If new value < leaf → insert as **left child**
    - If new value > leaf → insert as **right child**

---

### 3.3 Deletion

First, understand these two concepts:

| Term                    | Definition                                                                        |
| ----------------------- | --------------------------------------------------------------------------------- |
| **Inorder Predecessor** | Maximum value in the inorder traversal and if present in **left subtree** (floor) |
| **Inorder Successor**   | Minimum value in the inorder traversal and if present in **right subtree** (ceil) |

**Three cases:**

| Case   | Condition                 | Action                                                                                                       |
| ------ | ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Case 1 | Node is a **leaf**        | Simply delete it                                                                                             |
| Case 2 | Node has **one child**    | Delete node, connect child directly to parent                                                                |
| Case 3 | Node has **two children** | Replace with **inorder successor** OR **inorder predecessor**, then recursively delete that replacement node |

> [!tip] In Case 3, after the replacement, the node to be deleted recursively will have **at most one child** (never two). So **at most 2 deletions** are ever needed for a single delete operation.

---

### 3.4 Range Search

Print all values between `k1` and `k2`:

```c
void RangePrinter(node *root, int k1, int k2) {
    if (root == NULL) return;
    if (root->data >= k1 && root->data <= k2) {
        printf("%d", root->data);
        RangePrinter(root->left, k1, k2);
        RangePrinter(root->right, k1, k2);
    }
    else if (root->data < k1)
        RangePrinter(root->right, k1, k2);
    else
        RangePrinter(root->left, k1, k2);
}
```

**Complexity:** `O(h + m)` where:

- `h` = height of tree
- `m` = number of nodes in range
- For balanced BST: `h = log n`, so → `O(log n + m)`
- If `n >> m`, simplifies to `O(log n)`

---

## 4. Time Complexity

| Operation | Best Case          | Average Case | Worst Case               |
| --------- | ------------------ | ------------ | ------------------------ |
| Search    | O(1) — key is root | O(log n)     | O(n) — chain/skewed tree |
| Insertion | O(1) — empty tree  | O(log n)     | O(n) — chain/skewed tree |
| Deletion  | O(1) — first node  | O(log n)     | O(n) — chain/skewed tree |

> [!warning] Worst case occurs when BST degenerates into a **linked list (chain structure)** — e.g., inserting sorted values in order.

---

## 5. Probe Sequences (Search Path Validity)

 For a **successful** search of key `k`:

A legal probe sequence must satisfy:

- Values **less than k** appear in **increasing order**
- Values **greater than k** appear in **decreasing order**
- These two groups can be interleaved in any order, but each group must maintain its order
-  **Number of valid sequences** with `p` values less than k and `q` values greater than k: $$\binom{p+q}{p} = \frac{(p+q)!}{p! \cdot q!}$$
---

## 6. Number of Insertion Permutations

### Core Idea

> Given a **filled BST**, find the number of valid insertion orders that produce the exact same tree. 
> This is equivalent to: given the same **structure** (but empty), how many insertion orders produce it? Since a fixed structure corresponds to a **unique node-to-key mapping**, both questions reduce to the same problem.

### Rules

- The **root must always be inserted first** — no exceptions
- For each subtree, a parent must be inserted before its children
- Children of the same parent can be interleaved freely → count using **combinations**

[[Permutations]]

---
## 7. GATE Questions (Practice)

### GATE CSE 1996

> BST built by inserting: `50, 15, 62, 5, 20, 58, 91, 3, 8, 37, 60, 24` Nodes in left and right subtree of root respectively? **Answer: B → (7, 4)**

---

### GATE CSE 1996

> BST used to locate 43. Which probe sequences are valid?
> 
> - (a) `61 52 14 17 40 43`
> - (b) `2 3 50 40 60 43`
> - (c) `10 65 31 48 37 43`
> - (d) `81 61 52 14 41 43`
> - (e) `17 77 27 66 18 43`

---

### GATE CSE 1997

> BST with values 1–8, pre-order traversal. Which is valid output?
> 
> - A. `5 3 1 2 4 7 8 6`
> - B. `5 3 1 2 6 4 8 7`
> - C. `5 3 2 4 1 6 7 8`
> - D. `5 3 1 2 4 7 6 8` **Answer: D**

---

### GATE CSE 2003

> Numbers `7,5,1,8,3,6,0,9,4,2` inserted in order into empty BST. Inorder traversal? **Answer: C → `0 1 2 3 4 5 6 7 8 9`** _(BST inorder always gives sorted output)_

---

### GATE CSE 2001

> Insert `15, 32, 20, 9, 3, 25, 12, 1` into BST. Draw tree, then delete 15.

---

### GATE IT 2006

> Numbers 1–100 in BST, searching for 55. Which sequence CANNOT occur?
> 
> - A. `{10, 75, 64, 43, 60, 57, 55}`
> - B. `{90, 12, 68, 34, 62, 45, 55}`
> - C. `{9, 85, 47, 68, 43, 57, 55}`
> - D. `{79, 14, 72, 56, 16, 53, 55}` **Answer: C** _(47 → 68 is fine, but 68 → 43 violates: 43 < 47, already went left past 47)_

---

### GATE IT 2007

> Searching for 60, nodes `10, 20, 40, 50, 70, 80, 90` traversed (order unknown). How many valid orderings?
> 
> - Values < 60: `{10, 20, 40, 50}` — must be increasing
> - Values > 60: `{70, 80, 90}` — must be decreasing
> - Answer: `C(7,4) = 35` → **Answer: A → 35**

---

### GATE CSE 2016

> How many ways to insert `1,2,3,4,5,6,7` to get a BST of height 6?
> 
> - Height 6 with 7 nodes = chain (every node has exactly one child)
> - At each level, 2 choices (go left or right)
> - Total structures = 2^6
> - In this case for each structure there is only one possible order of insertions
> - Answer: **2⁶ = 64**

---

### GATE CSE 2020

> In balanced BST with n elements, worst case time to report all elements in range [a,b] where k elements are reported? **Answer: B → Θ(log n + k)**

---

### GATE CSE 2014

> Balanced BST with n numbers. Sum all numbers between L and H (m such numbers). Tightest upper bound: `O(n^a log^b n + m^c log^d n)`
> 
> - Time = `O(log n + m)` → a=0, b=1, c=1, d=0
> - `a + 10b + 100c + 1000d` = `0 + 10 + 100 + 0` = **110**

---

## 8. Quick Reference Cheatsheet

```
BST Property:    left < root < right  (no duplicates)
Inorder Output:  Always sorted (ascending)
Pre/Post order:  Uniquely determines the BST
Inorder alone:   Does NOT uniquely determine BST

Search/Insert/Delete:
  Best:    O(1)
  Average: O(log n)
  Worst:   O(n)  ← skewed/chain tree

Range Search:    O(h + m) = O(log n + k) for balanced tree

Valid probe seq (successful search for k):
  → values < k must be increasing
  → values > k must be decreasing
  → count = C(p+q, p)

Deletion cases:
  Leaf       → just remove
  One child  → bypass node
  Two child  → swap with inorder successor/predecessor, then delete that
             → at most 2 deletions needed total
```

---
[AVL trees](AVL%20trees.md)