https://www.w3schools.com/dsa/dsa_theory_hashtables.php

https://old.reddit.com/r/learnprogramming/comments/pthgms/differences_between_hashtable_hashmap_and_hashset/

## Abstract Data Types (ADTs)
**Set** and **Map** are *Abstract Data Types*—conceptual ideas defining functionality rather than concrete implementations.

- **Map**: Stores **key-value** pairs. Allows retrieval of a value using its associated key.
- **Set**: A collection of **unique** elements. Duplicate insertions are automatically ignored.

> [!NOTE]
> ADTs cannot be used directly in code; they require a concrete implementation.

## Hashing
**Hashing** is a method to concretely implement ADTs by organizing data into **buckets** (e.g., linked lists or balanced trees) for efficient retrieval.

- Converts data into an index (hash) to speed up access.
- Reduces search time complexity significantly.

