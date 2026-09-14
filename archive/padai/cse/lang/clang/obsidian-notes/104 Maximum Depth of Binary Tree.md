```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS / Level Order Traversal
        # Each iteration of the outer loop processes exactly one level.
        depth = 0

        queue = [root]

        while queue:
            # Number of nodes currently in this level
            nodes_in_level = len(queue)

            for _ in range(nodes_in_level):
                node = queue.pop(0)

                # Handles the empty-tree case when root is None
                # I intially used break, but it only breaks out of inner loop, so return

                if not node:
                    return 0

                # Add children to be processed in the next level
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # Finished processing one complete level
            depth += 1

        return depth
```

## Possible Improvements

### 1. Handle `root is None` Before Starting BFS

Instead of checking:

```python
if not node:
    return 0
```

inside the loop, handle the empty-tree case once at the beginning:

```python
if not root:
    return 0
```

This removes a conditional check from every BFS iteration and makes it clear that all nodes in the queue are valid tree nodes.

---

### 2. Use `collections.deque` Instead of a List

Current code:

```python
node = queue.pop(0)
```

Removing the first element from a Python list is `O(n)` because all remaining elements must be shifted.

Using a deque:

```python
from collections import deque

queue = deque([root])
node = queue.popleft()
```

makes queue operations `O(1)` and is the standard choice for BFS.

---

### Final Optimized Version

```python
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth
```