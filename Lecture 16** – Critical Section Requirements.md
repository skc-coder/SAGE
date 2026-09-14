---
tags:
  - operating-systems
  - concurrency
  - synchronization
  - gate-cs
---

# Min and Max Values of Shared Counter

## Problem Statement

A shared variable `count` is initialized to `0`. Two concurrent threads execute the following code:

```c
// Shared variable
int count = 0;

// Thread 1
for (int i = 0; i < 10; i++) {
    count++;
}

// Thread 2
for (int i = 0; i < 10; i++) {
    count++;
}
```

What are the **minimum** and **maximum** possible final values of `count`?

---

## Machine-Level Decomposition of `count++`

At the assembly level, `count++` is non-atomic and consists of three distinct instructions:
1. **LOAD**: `R = count`
2. **INCR**: `R = R + 1`
3. **STORE**: `count = R`

---

## Results

* **Maximum Value:** `20`
* **Minimum Value:** `2`

---

## Detailed Analysis

### Maximum Value: `20`
Occurs when execution is completely serial (no overlapping race conditions) or when context switches occur strictly after a full read-modify-write cycle completes:
* $T_1$ runs completely to completion $\rightarrow \text{count} = 10$
* $T_2$ runs completely to completion $\rightarrow \text{count} = 20$

---

### Minimum Value: `2`
Achieved through interleaved execution and strategic preemption across iterations:

1. **$T_1$ (1st iteration):** 
   * Executes **LOAD** instruction only.
   * Internal register $R_1 = 0$.
   * $T_1$ is preempted.

2. **$T_2$ (Iterations 1 to 9):** 
   * Runs $9$ full iterations (LOAD, INCR, STORE) without preemption.
   * `count` becomes $9$.

3. **$T_1$ resumes (1st iteration):** 
   * Executes **INCR** ($R_1 = 1$) and **STORE** (`count = 1`).
   * `count` is overwritten to $1$ (erasing the $9$ increments made by $T_2$).

4. **$T_2$ (10th iteration):** 
   * Executes **LOAD** instruction only.
   * Internal register $R_2 = 1$.
   * $T_2$ is preempted.

5. **$T_1$ (Iterations 2 to 10):** 
   * Runs all remaining $9$ iterations to completion.
   * `count` becomes $1 + 9 = 10$.

6. **$T_2$ resumes (10th iteration):** 
   * Executes **INCR** ($R_2 = 2$) and **STORE** (`count = 2`).
   * Finishes execution.
   * Final value of `count` is overwritten to **$2$**.

---

## Key Takeaway & Formula

For $k$ concurrent threads each incrementing a shared counter $N$ times (where $N \ge 2$):
* **$\text{Max Value} = k \times N$**
* **$\text{Min Value} = 2$** (independent of $N$, provided $N \ge 2$)


---
tags:
  - operating-systems
  - concurrency
  - synchronization
  - critical-section
  - gate-cs
---

# Critical Section Problem & Synchronization Criteria

## Core Requirements of a Critical Section (CS) Solution

A valid software or hardware solution to the Critical Section problem must satisfy the primary criteria:

```
        ┌─────────────────────────────────────────────────────────┐
        │        Critical Section Synchronization Criteria        │
        └────────────────────────────┬────────────────────────────┘
                                     │
           ┌─────────────────────────┴─────────────────────────┐
           ▼                                                   ▼
┌──────────────────────┐                           ┌──────────────────────┐
│  Primary (Mandatory) │                           │ Secondary (Optional) │
├──────────────────────┤                           ├──────────────────────┤
│ 1. Mutual Exclusion  │                           │ 3. Bounded Waiting   │
│ 2. Progress          │                           │ 4. Architectural     │
└──────────────────────┘                           │    Neutrality (Speed)│
                                                   └──────────────────────┘
```

---

## 1. Mutual Exclusion (ME)

* **Definition:** At most **one process** is permitted inside the critical section at any given time ($\le 1$).
* If process $P_i$ is executing in its critical section, no other process $P_j$ is allowed to execute in its critical section.

### Trivial Example (Non-Functional)
```c
// Process 1                // Process 2
while(1);                   while(1);
/* Critical Section */      /* Critical Section */
```
* **Analysis:** Mutual exclusion is strictly satisfied because **zero** processes ever enter the CS ($\le 1$). 
* **Conclusion:** Mutual exclusion alone is **insufficient** to form a working synchronization solution.

---

## 2. Progress (Absence of Deadlock)

* **Definition:** If no process is executing in its CS and one or more processes wish to enter, only those processes that are **not executing in their remainder section** can participate in deciding which process enters next.
* This selection **cannot be postponed indefinitely**.
* **Intuition:** 
  * At least one process must enter if processes are waiting ($\ge 1$).
  * A process outside the critical section (in remainder code) must not block an interested process from entering.
  * Ensures the system does not deadlock or freeze.

$$\text{Mutual Exclusion } (\le 1) \;+\; \text{Progress } (\ge 1) \implies \text{Exactly One Process } (= 1)$$

---

## 3. Bounded Waiting (Absence of Starvation / Fairness)

* **Definition:** There exists a bound or limit on the number of times other processes are allowed to enter their critical sections after a process has made a request to enter and before that request is granted.
* **Intuition:** 
  * Prevents indefinite postponement or **starvation**.
  * If process $P_1$ requests to enter, process $P_2$ must not repeatedly bypass $P_1$ infinitely ($P_2 \to P_2 \to P_2 \dots$).
  * A process cannot be repeatedly overtaken without bound.

---

## Implementation Approaches

```
                     ┌───────────────────────────────────┐
                     │ Implementation of CS Solutions    │
                     └─────────────────┬─────────────────┘
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
┌────────────────┐             ┌────────────────┐             ┌────────────────┐
│ 1. Software    │             │ 2. OS Support  │             │ 3. Hardware    │
├────────────────┤             ├────────────────┤             ├────────────────┤
│ • Pure user-   │             │ • System calls │             │ • Special CPU  │
│   space code   │             │ • Semaphores   │             │   instructions │
│ • Peterson's   │             │ • Mutex locks  │             │ • TestAndSet() │
│ • Dekker's     │             │ • Monitors     │             │ • Swap() / XCHG│
└────────────────┘             └────────────────┘             └────────────────┘
```

---

## Practical Checklist for Evaluating CS Code

Use these operational tests and counter-example scenarios to evaluate any concurrency snippet:

### 1. Testing for Mutual Exclusion
* **Check 1:** Assume process $P_1$ is already inside the CS. Process $P_2$ attempts to enter.
  * $\to$ Show that $P_2$ is blocked in its entry code.
* **Check 2:** Two (or more) processes arrive simultaneously at the entry code.
  * $\to$ Show that at most one process successfully passes the entry gate and enters the CS.

### 2. Testing for Progress (Deadlock Freedom)
* **Check 1:** CS is empty, only one process ($P_1$) wants to enter.
  * $\to$ Verify whether $P_1$ can enter without waiting for any other process.
* **Check 2:** Two processes arrive at the entry code at the exact same instant.
  * $\to$ Verify whether at least one process can resolve entry and move inside, or if both get stuck (deadlock).

### 3. Testing for Bounded Waiting (Starvation Freedom)
* **Check 1:** Process $P_1$ is inside the CS, and process $P_2$ is waiting in the entry code.
* **Check 2:** $P_1$ exits the CS and immediately loops around to request entry again.
  * $\to$ Check whether $P_1$ can repeatedly re-enter while $P_2$ remains starved indefinitely.
  * $\to$ If $P_1$ can bypass $P_2$ without any upper bound, **Bounded Waiting is violated**.