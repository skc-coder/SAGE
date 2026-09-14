Sources: 
https://www.cs.cmu.edu/afs/cs/academic/class/15210-s14/www/lectures/hash.pdf
https://www.w3schools.com/dsa/dsa_theory_hashtables.php
## Abstract Data Types (ADTs)
https://old.reddit.com/r/learnprogramming/comments/pthgms/differences_between_hashtable_hashmap_and_hashset/

**Set** and **Map** are *Abstract Data Types*—conceptual ideas defining functionality rather than concrete implementations.

- **Map**: Stores **key-value** pairs. Allows retrieval of a value using its associated key.
- **Set**: A collection of **unique** elements. Duplicate insertions are automatically ignored.

> [!NOTE]
> ADTs cannot be used directly in code; they require a concrete implementation.

## Hashing
**Hashing** is a method to concretely implement ADTs by organizing data into **buckets** (e.g., linked lists or balanced trees) for efficient retrieval.

- Converts data into an index (hash) to speed up access.
- Reduces search time complexity significantly.

---

# Hashing — Short Notes

## Collision Resolution Types

- **Separate Chaining** — linked list per slot
- **Open Addressing** — store in alternate slot (linear/quadratic/double hashing)

## Probing Techniques

- **Linear**: `h(k,i) = (h(k) + i) mod m` → primary clustering
- **Quadratic**: `h(k,i) = (h(k) + i²) mod m` → secondary clustering
- **Double Hashing**: `h(k,i) = (h1(k) + i·h2(k)) mod m` → minimal clustering, needs `gcd(h2(k), m) = 1`

## Theorems

1. Chaining: successful & unsuccessful search = `Θ(1 + λ)`
2. Linear probing: unsuccessful ≈ `½(1 + 1/(1-λ)²)`
3. Quadratic probing: `m` prime + table ≤ half full → guaranteed empty slot found, no repeat probes
4. Double/Uniform hashing: unsuccessful ≤ `1/(1-λ)`
5. Double/Uniform hashing: succesful = O(1/lambda)