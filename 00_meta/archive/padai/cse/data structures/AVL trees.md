---

## subject: "DS" topic: "AVL Trees" source: "https://www.youtube.com/watch?v=9QSN62vo-l0&list=PLIPZ2_p3RNHgsP1q_r_7af_Sii_aZZ8aa"

# AVL Trees

---
[https://www.youtube.com/watch?v=9QSN62vo-l0&list=PLIPZ2_p3RNHgsP1q_r_7af_Sii_aZZ8aa](https://www.youtube.com/watch?v=9QSN62vo-l0&list=PLIPZ2_p3RNHgsP1q_r_7af_Sii_aZZ8aa)"
## 1. Core Concept & Properties

- **Definition:** Self-balancing BSTs
- **Height:** Number of **edges** on the longest path from root to leaf
- **Density vs Height:** More nodes per level = less height. Sparse levels = more height
- **Tree Counting:** To count unique AVL trees for a given key set — analyze possibilities for each root key separately

---

## 2. Balance Operations (Rotations)

> Rotations are just **pointer reassignments** — $O(1)$ time. Not actually "shifting shapes."

### Stick → Mountain (Single Rotation)

- Triggered by **straight line** imbalance: LL or RR insertion
- Middle node shifts up to become new subtree root

### Elbow → Mountain (Double Rotation)

- Triggered by **zigzag** imbalance: LR or RL insertion
- Last node shifts to middle
- Step 1: Rotate bottom edge → turn elbow into stick
- Step 2: Rotate again → form balanced mountain

---

## 3. Mathematical Bounds

**Minimum nodes for height $h$:** $$n(h) = n(h-1) + n(h-2) + 1$$

> $n(0) = 1$, $n(1) = 2$ — mirrors Fibonacci growth

**Maximum nodes for height $h$:** $$n_{max} = 2^{h+1} - 1$$

> Perfectly complete binary tree

---

## 4. Operations

### Left Rotation (Right-Heavy Imbalance)

```java
function leftRotate(X):
    Y = X.right
    T2 = Y.left

    Y.left = X
    X.right = T2

    X.height = max(height(X.left), height(X.right)) + 1
    Y.height = max(height(Y.left), height(Y.right)) + 1

    return Y  // new subtree root
```

---

### Insertion

> Standard BST insert → backtrack → check balance → **first imbalanced node** → rotate Shape is determined by that node + path to insertion point

```c
function insert(node, key):
    // 1. Standard BST Insert
    if node is null: return newNode(key)
    if key < node.key:     node.left  = insert(node.left, key)
    else if key > node.key: node.right = insert(node.right, key)
    else: return node  // no duplicates

    // 2. Update Height
    node.height = 1 + max(height(node.left), height(node.right))

    // 3. Balance Factor
    balance = height(node.left) - height(node.right)

    // 4. Rebalance
    if balance > 1  and key < node.left.key:   return rightRotate(node)          // LL
    if balance < -1 and key > node.right.key:  return leftRotate(node)           // RR
    if balance > 1  and key > node.left.key:                                     // LR
        node.left = leftRotate(node.left)
        return rightRotate(node)
    if balance < -1 and key < node.right.key:                                    // RL
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node
```

> ⚠️ Even after rotating, backtracking continues to root to update heights

> ⚠️ Rebalancing may decrease height or keep it same — but **insertion never decreases height**. It can't — that would break the minimum node-height relation.
---

### Deletion

> Delete as usual → backtrack → first imbalanced node → rotate **towards longer height side** (use balance factor to find it).
> Unlike insertion, we do NOT move towards point of deletion.
>  
>  Keep backtracking — imbalance can cascade. May rotate multiple times. 
>   
>  **Same height case → make a stick** (not for convenience —it's required for correctness)

```c
function delete(node, key):
    // 1. Standard BST Delete
    if node is null: 
	    return node
    if key < node.key:      
	    node.left  = delete(node.left, key)
    else if key > node.key: 
	    node.right = delete(node.right, key)
    else:
        if node.left is null or node.right is null:
            temp = node.left if node.left else node.right
            if temp is null: node = null
            else: node = temp
        else:
            temp = minValueNode(node.right)
            node.key = temp.key
            node.right = delete(node.right, temp.key)

    // 2. Update Height
    node.height = 1 + max(height(node.left), height(node.right))

    // 3. Balance Factor
    balance = height(node.left) - height(node.right)

    // 4. Rebalance (can cascade up to root)
    // LL
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)
    // LR
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    // RR
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)
    // RL
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node
```


---

## 5. Complexity

| Operation | Rotations needed                                      |
| --------- | ----------------------------------------------------- |
| Insertion | At most **1** (single or double)                      |
| Deletion  | Up to **$O(\log n)$** — imbalance can cascade to root |