---

## subject: "Data Structures" topics: [Binary Tree, BST, Recursion, Linked List] last_reviewed: "" total_mistakes: 0

# Data Structures — Mistake Log

---
3z# 📦 SOURCES

## 🗂️ Sources Index

> Add every source once. Reference by ID everywhere else.

| ID      | Type                  | Source     | Link                                                                                     | Topics Covered |
| ------- | --------------------- | ---------- | ---------------------------------------------------------------------------------------- | -------------- |
| DSA-S01 | University Midterm    |            | [link](https://www.cs.umd.edu/class/summer2021/cmsc132/tests/midterm2/m2-summer2018.pdf) |                |
| DSA-S02 | University HW         |            | [link](https://claude.ai/chat/url)                                                       |                |
| DSA-S03 | University Assignment |            | [link](https://claude.ai/chat/url)                                                       |                |
| DSA-S04 | Quiz/Final            | MIT        | [link](https://courses.csail.mit.edu/6.006/oldquizzes/)                                  |                |
| DSA-S05 | Textbook              |            | —                                                                                        |                |
| DSA-S06 | PYQ                   | GATE PYQ   | [link](https://claude.ai/chat/url)                                                       |                |
| DSA-S07 | Test Series           | GO Classes | [link](https://claude.ai/chat/url)                                                       |                |
| DSA-S08 | Lab                   |            | —                                                                                        |                |
> Types: `University Midterm` / `University HW` / `University Assignment` / `University Quiz` / `Textbook` / `PYQ` / `Test Series` / `Lab`

---

## 🏛️ University Sources Log

> Track which universities you've hit per topic.

|Topic|MIT|Stanford|CMU|Berkeley|Princeton|UMD|UIUC|Others|
|---|---|---|---|---|---|---|---|---|
|Binary Tree|—|—|—|—|—|🔄|—|—|
|BST|—|—|—|—|—|🔄|—|—|
|Recursion|—|—|—|—|—|🔄|—|—|
|Linked List|—|—|—|—|—|🔄|—|—|

> ✅ done / 🔄 in progress / — not started

---

## 📊 PYQ + Test Series Log

|Date|Source ID|Source Name|Year / Mock #|Score|Weak topics|Notes|
|---|---|---|---|---|---|---|
|2026-06-19|DSA-S06|GATE PYQ|2022|—|BST pruning, recursion modeling|initial entry|
|2026-06-19|DSA-S07|GO Classes|Mock 1|—|two-pointer logic, BT vs BST|initial entry|

---

## 📅 Review

|Week|Sources used|Problems solved|Weak areas noticed|
|---|---|---|---|
|Week 1|DSA-S02, DSA-S06|6|BST pruning, recursion decomposition, edge-case handling|

---

# 🐛 MISTAKES

## 📌 Topic Index

- [[#Binary Tree]]
- [[#BST]]
- [[#Recursion]]
- [[#Linked List]]

---

## 📌 Weak Topics

- BST pruning logic
    
- Recursion base-case modeling
    
- Two-pointer / dummy node handling
    
- BT vs BST distinction
    

---

## Binary Tree

### M001

> **Source:** DSA-S01 — **Date:** 2026-06-19

**Problem:**  
Write `int countNodes(Node r, int min, int max)` — count nodes in a BT within range `[min, max]` inclusive.

**My approach:**  
Assumed BST-like pruning was possible and tried skipping subtrees based on value comparisons.

**Correct approach:**  
For a plain BT you **cannot prune** — you must visit every node since there is no ordering guarantee. Check if current node is in range, then recurse both subtrees regardless.

```java
int countNodes(Node r, int min, int max) {
    if (r == null) return 0;

    int count = (r.key >= min && r.key <= max) ? 1 : 0;

    return count +
           countNodes(r.left, min, max) +
           countNodes(r.right, min, max);
}
```

**Root cause:**

- ☑ Concept gap — BT vs BST distinction (no ordering in BT = no pruning)
    

**Key takeaway:**  
BT = visit all nodes always. BST = prune using ordering property.

**Revised?** ☑

---

## BST

### M002

> **Source:** DSA-S01 — **Date:** 2026-06-19

**Problem:**  
Same `countNodes` but on a BST — exploit ordering to prune subtrees.

**My approach:**  
Forgot pruning conditions and still traversed both sides unnecessarily.

**Correct approach:**  
BST ordering lets you skip entire subtrees.

```java
int countNodes(Node r, int min, int max) {
    if (r == null) return 0;
    if (r.key < min) return countNodes(r.right, min, max);
    if (r.key > max) return countNodes(r.left, min, max);

    return 1 +
           countNodes(r.left, min, max) +
           countNodes(r.right, min, max);
}
```

**Root cause:**

- ☑ Concept gap — forgot BST pruning logic
    

**Key takeaway:**  
If `< min` go right only. If `> max` go left only. Otherwise explore both.

**Revised?** ☑

---

### M003

> **Source:** DSA-S01 — **Date:** 2026-06-19

**Problem:**  
`Node deleteAll(Node r, int threshold)` — delete all nodes with keys lower than threshold from a BST.

**My approach:**  
Tried deleting node-by-node instead of using structural BST property to discard subtrees.

**Correct approach:**  
If `r.key < threshold` → discard node + entire left subtree.

```java
Node deleteAll(Node r, int threshold) {
    if (r == null) return null;

    if (r.key < threshold)
        return deleteAll(r.right, threshold);

    r.left = deleteAll(r.left, threshold);
    return r;
}
```

**Root cause:**

- ☑ Concept gap — BST structural property allows discarding entire subtree
    

**Key takeaway:**  
BST lets you delete in bulk using ordering.

**Revised?** ☑

---

## Recursion

### M004

> **Source:** DSA-S01 — **Date:** 2026-06-19

**Problem:**  
Grid paths from bottom-left to top-right using only up/right moves.

**My approach:**  
Initially tried iterative counting instead of recursion breakdown.

**Correct approach:**

```java
public int paths(int h, int w) {
    if (h < 0 || w < 0) return 0;
    if (h == 0 && w == 0) return 1;
    return paths(h - 1, w) + paths(h, w - 1);
}
```

**Root cause:**

- ☑ Concept gap — recursive decomposition of grid paths
    

**Key takeaway:**  
paths(h,w) = paths(h-1,w) + paths(h,w-1)

**Revised?** ☑

---

### M005

> **Source:** DSA-S02 — **Date:** 2026-06-19

**Problem:**  
Recursion vs iteration MCQ.

**My approach:**  
Confused memory usage direction and assumed recursion is “stronger.”

**Correct approach:**  
Recursion uses more memory due to call stack frames.

**Root cause:**

- ☑ Concept gap — call stack memory overhead
    

**Key takeaway:**  
Iteration = constant stack. Recursion = growing stack.

**Revised?** ☑

---

## Linked List

### M006

> **Source:** DSA-S02 — **Date:** 2026-06-19

**Problem:**  
Remove nth node from end of linked list.

**My approach:**  
Struggled with off-by-one indexing and didn’t account for head deletion cleanly.

**Correct approach:**  
Use dummy + two pointers.

```java
Node removeNthFromEnd(Node head, int n) {
    Node dummy = new Node(0);
    dummy.next = head;
    Node fast = dummy, slow = dummy;

    for (int i = 0; i <= n; i++) fast = fast.next;
    while (fast != null) {
        fast = fast.next;
        slow = slow.next;
    }

    slow.next = slow.next.next;
    return dummy.next;
}
```

**Root cause:**

- ☑ Edge case missed — head deletion needs dummy node
    
- ☑ Misread indexing (off-by-one risk)
    

**Key takeaway:**  
Dummy node + n+1 gap simplifies all edge cases.

**Revised?** ☑

---

## ⚠️ Repeat Mistakes

> Fill this on Sunday review only — mistakes you've made more than once.

| #   | Topic       | Core mistake                    | Times repeated |
| --- | ----------- | ------------------------------- | -------------- |
| 1   | BST         | Forgetting pruning conditions   | 1              |
| 2   | Recursion   | Weak base-case decomposition    | 1              |
| 3   | Linked List | Off-by-one + missing dummy node | 1              |

---

## 📅 Review Log

|Date|Topics reviewed|Pattern noticed|
|---|---|---|
|2026-06-19|BT, BST, Recursion, Linked List|Over-reliance on brute traversal; weak pruning intuition|
