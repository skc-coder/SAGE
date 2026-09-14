---
tags:
  - operating-systems
  - concurrency
  - synchronization
  - gate-cs
---
# Shared Counter & Race Condition Mechanics

When multiple threads access shared mutable state without proper synchronization, non-atomic machine instructions allow interleavings that cause race conditions.

Consider two concurrent threads executing an increment loop on a shared integer:

```c
// Shared variable residing in process heap/data segment
int count = 0;

// Thread 1                             // Thread 2
for (int i = 0; i < 10; i++) {          for (int i = 0; i < 10; i++) {
    count++;                                count++;
}                                       }
```

At the assembly level, a high-level language statement like `count++` is not atomic. On standard register-memory architectures, it compiles into three distinct machine instructions:

```c
LOAD  R, count    // Instruction 1: Read memory cell into internal CPU register
INCR  R          // Instruction 2: Arithmetic unit modifies register
STORE count, R    // Instruction 3: Write register back into memory cell
```

> [!definition] Race Condition
> A concurrent system state where the final outcome of an operation depends directly on the specific execution order, preemption timing, or relative scheduling of multiple threads or processes accessing shared memory.

---

## Extreme Value Derivations

The maximum and minimum possible final values of `count` after both threads finish their $10$ iterations each are bounded as follows:

### 1. Maximum Value: $20$
Occurs when threads execute completely serially or context switches occur strictly outside of the critical three-instruction window.
- $T_1$ runs all $10$ iterations to completion: $\text{count} = 10$.
- $T_2$ runs all $10$ iterations to completion: $\text{count} = 20$.

### 2. Minimum Value: $2$
Achieved via strategic interleaving across iterations where one thread overwrites and erases the valid historical increments performed by the other:

- **Step 1 ($T_1$, Iteration 1):** $T_1$ executes `LOAD R_1, count`. Since $\text{count} = 0$, $R_1 = 0$. Preempt $T_1$ immediately before `INCR`.
- **Step 2 ($T_2$, Iterations 1 to 9):** $T_2$ executes $9$ full read-modify-write iterations without preemption. The shared variable $\text{count}$ becomes $9$.
- **Step 3 ($T_1$, Resumes Iteration 1):** $T_1$ wakes up with stale local context ($R_1 = 0$). It executes `INCR R_1` ($R_1 = 1$) and `STORE count, R_1` ($\text{count} = 1$). This single write obliterates all $9$ increments achieved by $T_2$.
- **Step 4 ($T_2$, Iteration 10):** $T_2$ initiates its final iteration and executes `LOAD R_2, count`. It reads the current value $\text{count} = 1$, loading $R_2 = 1$. Preempt $T_2$ immediately before `INCR`.
- **Step 5 ($T_1$, Iterations 2 to 10):** $T_1$ runs its remaining $9$ iterations entirely to completion. It reads $\text{count} = 1$, increments it $9$ times, and writes $\text{count} = 1 + 9 = 10$.
- **Step 6 ($T_2$, Resumes Iteration 10):** $T_2$ resumes with its saved register value $R_2 = 1$. It performs `INCR R_2` ($R_2 = 2$) and finally executes `STORE count, R_2`. The shared variable $\text{count}$ is set to $2$.

> [!formula] Shared Counter Extreme Value Bounds
> For $k$ concurrent threads each incrementing a shared counter $N$ times (where $N \ge 2$):
> $$\text{Max Value} = k \cdot N$$
> $$\text{Min Value} = 2$$
> The minimum bound is independent of the number of iterations $N$, provided $N \ge 2$, because an unsynchronized store can overwrite an arbitrary number of prior committed updates.
