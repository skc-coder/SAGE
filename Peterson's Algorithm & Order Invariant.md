---
tags:
  - operating-systems
  - concurrency
  - synchronization
  - gate-cs
---
# Peterson's Algorithm & Order Invariant

Peterson's Algorithm merges the intention flag array with an arbitration turn variable to satisfy all primary and secondary Critical Section requirements for two processes.

---

## 1. Algorithm Structure

```c
// Shared variables
bool flag[2] = {false, false};
int turn = 0;

// Process Pi (i ∈ {0, 1}, peer j = 1 - i)
flag[i] = true;
turn = j;
while (flag[j] && turn == j);

/* Critical Section */

flag[i] = false;

/* Remainder Section */
```

---

## 2. Key Invariants & Correctness

> [!theorem] Peterson's Order Invariant
> In two-process algorithms combining intention flags with a tie-breaker scalar, the write to the intention flag must strictly precede the write to the tie-breaker:
> $$\text{flag}[i] \leftarrow \text{true} \prec \text{turn} \leftarrow j$$
> Inverting this sequence allows a thread to read an unasserted flag before its peer registers intent, breaking the invariant and violating Mutual Exclusion.

> [!trap] Swapping Peterson's Entry Statements
> If process $P_i$ executes `turn = j` **before** `flag[i] = true`:
> 1. $P_0$ sets `turn = 1` and is preempted.
> 2. $P_1$ sets `turn = 0`, sets `flag[1] = true`, checks `flag[0]` (which is still `false`), skips the while loop, and enters the CS.
> 3. $P_0$ resumes, sets `flag[0] = true`, checks `while (flag[1] && turn == 1)`. Since `turn == 0` (overwritten by $P_1$), the while condition evaluates to `false`.
> 4. $P_0$ enters the CS while $P_1$ is still inside. **Mutual Exclusion is violated.**

---

## 3. Evaluation of Requirements

- **Mutual Exclusion:** Satisfied ($\boldsymbol{\checkmark}$). Both processes entering simultaneously would require `turn == 0` and `turn == 1` to hold concurrently, which is impossible ($\bot$).
- **Progress:** Satisfied ($\boldsymbol{\checkmark}$). `turn` can only hold one value at a time, ensuring at least one while-condition evaluates to `false`.
- **Bounded Waiting:** Satisfied ($\boldsymbol{\checkmark}$). Upon exiting, $P_0$ sets `flag[0] = false`, allowing $P_1$ to immediately enter. When $P_0$ re-requests entry, it sets `turn = 1`, yielding priority to $P_1$.
