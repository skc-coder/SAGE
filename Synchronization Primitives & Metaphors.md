---
tags:
  - operating-systems
  - concurrency
  - synchronization
  - gate-cs
---
# Synchronization Primitives & Metaphors

Software and hardware solutions utilize three core coordination abstractions:

| Mechanism | Metaphor | Write Authority | Core Vulnerability When Used Alone |
| :--- | :--- | :--- | :--- |
| `flag[i]` | Sticky note on a door | Local process only ($P_i$ writes `flag[i]`) | Deadlock under simultaneous declaration |
| `turn` | Shared physical token / baton | Shared ($P_i$ passes to $P_j$) | Progress violation (uninterested process blocks CS) |
| `lock` | Deadbolt on a door | Atomic Read-Modify-Write caller | Spinlock busy-waiting; starvation without queues |

---

## 1. The Intention Flag (`flag[i]`)
- **Semantic Role:** Denotes intention or interest without granting unilateral entry authority.
- **Entry Protocol:**
  ```c
  flag[i] = true;
  while (flag[j]);
  ```
- **Exit Protocol:**
  ```c
  flag[i] = false;
  ```
- **Operational Failure:** When used alone, simultaneous writes (`flag[0] = flag[1] = true`) lead to mutual entrapment where each process spins forever waiting for the other to clear its flag.

---

## 2. The Turn Variable (`turn`)
- **Semantic Role:** A singular scalar token that arbitrates authority. A single memory cell cannot hold two distinct values simultaneously.
- **Entry Protocol:**
  ```c
  while (turn != i);
  ```
- **Exit Protocol:**
  ```c
  turn = j;
  ```
- **Operational Failure:** Enforces strict alternation ($P_0 \to P_1 \to P_0 \dots$). If $P_0$ finishes and sets $\text{turn} = 1$, but $P_1$ remains idle in its remainder section without requesting the CS, $P_0$ is completely blocked from re-entering, violating Progress.

---

## 3. The Hardware Lock (`lock`)
- **Semantic Role:** A shared binary state ($0 = \text{free}, 1 = \text{held}$) manipulated via atomic Read-Modify-Write CPU instructions (`TestAndSet`, `Swap`, `XCHG`).
- **Entry Protocol:**
  ```c
  while (TestAndSet(&lock));
  ```
- **Exit Protocol:**
  ```c
  lock = 0;
  ```
- **Operational Failure:** Eliminates race conditions during entry checks via hardware bus locking, but burns CPU cycles spinning and lacks inherent ordering, which can cause starvation without auxiliary queueing.
