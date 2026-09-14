## Type 1: Simple Traversal
कोई level tracking नहीं — बस visit करना है।

```python
queue = deque([root])
while queue:
    node = queue.popleft()
    visit(node)
    for child in node.children:
        queue.append(child)
```

Use when: nodes को traverse करना है, level की ज़रूरत नहीं।

---

## Type 2: Level-Order
हर level के elements अलग collect करने हैं।

```python
queue = deque([root])
res = []
while queue:
    level = []
    for _ in range(len(queue)):   # ← यही level boundary देता है
        node = queue.popleft()
        level.append(node.val)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    res.append(level)
```

**Key insight:** outer loop का `len(queue)` = उस level के nodes की count।  
Inner loop ख़त्म → एक पूरा level done।

---

## Variant: Rightmost Element Per Level
(e.g. right side view of binary tree)

```python
while queue:
    for i in range(len(queue)):
        node = queue.popleft()
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
        if i == len(queue):           # last in this level
            res.append(node.val)
```

> No `level[]` list needed — level track करने की ज़रूरत नहीं,  
> बस inner loop का last element पकड़ना है।

---

## 1. Top-Down: Parent to Child (`Parameters`)
add the extra info to be appsed form parent to child in the tuple that is added to queue