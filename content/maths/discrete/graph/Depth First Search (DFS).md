## 1. Top-Down: Parent to Child (`Parameters`)

To pass information down the tree, use **function parameters**. Each recursive call receives an updated state from its parent.

- **Common Use Case:** Tracking current depth, path sums, or upper/lower bounds (BST validation).
    
- **Example:** Tree Level Order Traversal using depth.
    

Python

```
def dfs(node, depth):
    if not node:
        return
    if len(res) == depth:
        res.append([])
        
    res[depth].append(node.val)
    dfs(node.left, depth + 1)  # Passing incremented depth down
    dfs(node.right, depth + 1)
```

## 2. Bottom-Up: Child to Parent (`Return Values` / `nonlocal`) or use a local variable and return that, at root that contains the answer 

To pass information back up the tree, use **return statements** or update a **global/nonlocal variable**.

- **Common Use Case:** Calculating subtree heights, checking if a subtree contains a target, or finding the Lowest Common Ancestor (LCA).
    

Python

```
def maxDepth(root):
    def dfs(node):
        if not node: 
            return 0
        left = dfs(node.left)    # Information bubbling up from left child
        right = dfs(node.right)  # Information bubbling up from right child
        return max(left, right) + 1
    return dfs(root)
```

## 3. Early Stopping & Conditional Execution

To halt traversal early or execute code conditionally, evaluate the result of a child's recursive call **before** proceeding to the next line or the next sibling.

- **At Parent Level:** Check the child's status to short-circuit further exploration.
    
- **Common Use Case:** Searching for a specific node, path existence, or matching a complex pattern where searching the right subtree is redundant if the left subtree already found the solution.
    

Python

```
# Only explore the right subtree if the left subtree satisfies a condition
if dfs(node.left, target):
    if dfs(node.right, target):
        return True
return False
```