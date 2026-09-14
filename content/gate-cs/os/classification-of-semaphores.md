## 2. Classification of Semaphores

1. **Binary Semaphore (Mutex):**
   - Can take only binary values: $S \in \{0, 1\}$.
   - Primarily used to enforce **Mutual Exclusion** across concurrent processes accessing a single critical section.
2. **Counting Semaphore:**
   - Can take unrestricted non-negative/arbitrary integer values ($-\infty$ to $+\infty$ in record structures).
   - Used to manage resource allocation for resources with multiple identical instances (e.g., bounded buffers, reader-writer configurations).
