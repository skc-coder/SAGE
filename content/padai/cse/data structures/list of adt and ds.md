## Abstract Data Types (ADTs) vs. Data Structures

An **Abstract Data Type (ADT)** defines *what* operations can be performed on data, without specifying *how* they are implemented—focusing on behavior and interface. A **data structure** is the concrete implementation of an ADT, detailing how data is organized and manipulated in memory.

For example, a **Stack ADT** defines operations like `push` and `pop`, but it can be implemented using an array (Array-based Stack) or a linked list (Linked Stack).



---

### 1. Common ADTs and Their Implementations

#### List ADT
Represents an ordered sequence of elements with operations like `get(pos)`, `add(pos, item)`, and `remove(pos)`.

- **Array-based implementation**: Fast access (`O(1)`), but insertion/deletion costly (`O(n)`).
- **Linked List implementation**: Dynamic size, efficient insertions/deletions at ends (`O(1)`), but slow access (`O(n)`).

#### Stack ADT
Follows Last-In-First-Out (LIFO) principle with `push`, `pop`, and `peek` operations.

- **Array-based Stack**: Fixed or dynamic size; efficient time complexity.
- **Linked List-based Stack**: Grows dynamically; no risk of overflow.

#### Queue ADT
Follows First-In-First-Out (FIFO) principle with `enqueue` and `dequeue` operations.

- **Array-based Queue**: Can use circular buffer for efficiency.
- **Linked List-based Queue**: Efficient insertion and deletion from front and rear.

#### Deque (Double-ended Queue) ADT
Allows insertion and removal from both ends.

- **Array-based Deque**: Efficient if using dynamic array with amortized resizing.
- **Doubly Linked List**: Natural fit due to bidirectional links.

#### Set ADT
Stores unique elements with operations like `insert`, `delete`, and `contains`.

- **Hash Table**: Average `O(1)` for operations.
- **Balanced BST (e.g., Red-Black Tree)**: Guaranteed `O(log n)` performance.

#### Map (Associative Array) ADT
Stores key-value pairs with operations like `put(key, value)` and `get(key)`.

- **Hash Table**: Fast average-case lookup.
- **Binary Search Tree (BST)**: Ordered keys, `O(log n)` with balanced trees.

#### Priority Queue ADT
Retrieves elements based on priority (highest/lowest first).

- **Heap (Binary/Multiway)**: Most common; supports `insert` and `extract-max/min` in `O(log n)`.
- **Sorted Array/List**: Simple but inefficient for dynamic data.

---

### 2. Comparison Table

| ADT               | Common Operations                     | Typical Data Structures Used       |
|-------------------|----------------------------------------|-------------------------------------|
| **List**          | `get`, `add`, `remove`, `size`         | Array, Linked List                  |
| **Stack**         | `push`, `pop`, `peek`, `isEmpty`       | Array, Linked List                  |
| **Queue**         | `enqueue`, `dequeue`, `front`          | Array (circular), Linked List       |
| **Deque**         | `insertFront`, `insertRear`, `delete`  | Doubly Linked List, Dynamic Array   |
| **Set**           | `add`, `remove`, `contains`            | Hash Table, Red-Black Tree          |
| **Map**           | `put`, `get`, `remove`, `containsKey`  | Hash Table, BST                     |
| **Priority Queue**| `insert`, `extractMax/Min`             | Binary Heap, Fibonacci Heap         |
| **Tree**          | `insert`, `search`, `traverse`         | Binary Tree, AVL Tree, B-Tree       |
| **Graph**         | `addEdge`, `traverse`, `shortestPath`  | Adjacency List, Adjacency Matrix    |

---

### 3. Further Exploration

Understanding the distinction between ADTs and data structures enables better design choices based on performance needs, memory constraints, and use cases.

