Recall the naive lock variable software attempt:

```c
// Naive Software Lock Attempt
while (busy == 1);   // Line 1: Wait until lock is free
busy = 1;            // Line 2: Acquire lock
count++;             // Line 3: Critical Section
busy = 0;            // Line 4: Release lock
```

> [!trap] Flaw in Software Lock
> If process $P_0$ reads `busy == 0` at Line 1 and gets preempted right before setting `busy = 1`, process $P_1$ can also evaluate `busy == 0`, enter the critical section, and set `busy = 1`. When $P_0$ resumes, it proceeds to Line 2 and also enters the critical section. **Mutual Exclusion is violated.**

## TSL Assembly Level Fix

The root cause of this failure is that **testing** the lock (`busy == 0`) and **setting** the lock (`busy = 1`) are two separate non-atomic operations. By replacing Lines 1 and 2 with an atomic hardware instruction, this race condition is eliminated.

At the assembly/architecture level, this is implemented as:

```assembly
TSL Rx, LOCK
```

This machine instruction atomically reads the value of memory location `LOCK` into register `Rx` and sets the value at memory location `LOCK` to a non-zero value ($1$).
