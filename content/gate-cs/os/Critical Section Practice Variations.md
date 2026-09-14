---
tags:
  - operating-systems
  - concurrency
  - synchronization
  - gate-cs
---
# Critical Section Practice Variations & Invariant Analysis

Apply the contradiction and invariant rules directly to these three classic variations. For each problem, evaluate **Mutual Exclusion**, **Progress**, and **Bounded Waiting** without forward-tracing all interleavings.

---

## Variation 1: The Swapped Peterson Entry

Here, the order of writing to `flag` and `turn` is flipped relative to Peterson's standard solution.

```c
// Shared variables
bool flag[2] = {false, false};
int turn = 0;

// Code for Process P_i (i = 0 or 1, j = 1 - i)
do {
    turn = j;
    flag[i] = true;
    while (flag[j] && turn == j);

    // Critical Section

    flag[i] = false;

    // Remainder Section
} while (true);
```

### Questions & Tasks:
- **Mutual Exclusion:** Assume both $P_0$ and $P_1$ are inside the CS. Does that require a contradiction in `turn` or `flag`, or can both slip past the `while` gate if preempted right after updating `turn`?
- **Progress:** Check if a deadlock trap exists where both flags are `true` and the while conditions evaluate to `true` at the same time.
- **Bounded Waiting:** Does the algorithm guarantee a finite bound on bypasses?

---

### Invariant Deductions & Solutions:

1. **Mutual Exclusion: VIOLATED ($\boldsymbol{\times}$)**
   - **Hypothesis:** Assume $P_0 \in \text{CS}$ and $P_1 \in \text{CS}$ simultaneously at physical time $t$.
   - **Entry Pre-conditions:**
     - For $P_0 \in \text{CS}$, $P_0$ exited its `while(flag[1] && turn == 1)` loop. This requires $(\text{flag}[1] == \text{false}) \lor (\text{turn} == 0)$.
     - For $P_1 \in \text{CS}$, $P_1$ exited its `while(flag[0] && turn == 0)` loop. This requires $(\text{flag}[0] == \text{false}) \lor (\text{turn} == 1)$.
   - **Interleaving / Reachability Test:**
     - $P_0$ executes `turn = 1` and is preempted before setting `flag[0] = true`.
     - $P_1$ runs: executes `turn = 0`, sets `flag[1] = true`, evaluates `while (flag[0] && turn == 0)`. Since $P_0$ hasn't set `flag[0]` yet, $\text{flag}[0] == \text{false}$. $P_1$ enters CS!
     - $P_0$ resumes: sets `flag[0] = true`, evaluates `while (flag[1] && turn == 1)`. Since $P_1$ overwrote `turn = 0`, $\text{turn} == 1$ evaluates to `false`!
     - $P_0$ enters CS while $P_1$ is still inside CS $\implies$ $(P_0 \in \text{CS} \land P_1 \in \text{CS}) \not\implies \bot$. **Mutual Exclusion fails**.

2. **Progress: SATISFIED ($\boldsymbol{\checkmark}$)**
   - **Deadlock Trap Test:** $\Phi_{\text{Deadlock}} = W_0 \land W_1 = (\text{flag}[1] \land \text{turn} == 1) \land (\text{flag}[0] \land \text{turn} == 0) \implies (\text{turn} == 1 \land \text{turn} == 0) \equiv \bot$.
   - Deadlock is physically impossible because `turn` cannot hold both values simultaneously.
   - **Remainder Test:** If $P_1 \in \text{RS} \implies \text{flag}[1] = \text{false}$, then $W_0 = (\text{false} \land \text{turn} == 1) \equiv \text{false}$. $P_0$ enters without interference.

3. **Bounded Waiting: VIOLATED ($\boldsymbol{\times}$)**
   - Because Mutual Exclusion is broken, Bounded Waiting is invalid/violated under racing interleavings.

---

## Variation 2: Pure Turn-Taking (Strict Alternation)

A single variable coordinates entry without any flag arrays.

```c
// Shared variable
int turn = 0; // Initially 0

// Code for Process P_0                  // Code for Process P_1
do {                                    do {
    while (turn != 0);                      while (turn != 1);
    // Critical Section                      // Critical Section
    turn = 1;                               turn = 0;
    // Remainder Section                     // Remainder Section
} while (true);                         } while (true);
```

### Questions & Tasks:
- **Mutual Exclusion:** Can `turn == 0` and `turn == 1` hold simultaneously?
- **Progress:** Test the specific check where CS is empty, $P_1$ wants to enter, but $P_0$ is completely idle in its Remainder Section. Who controls the gate?
- **Bounded Waiting:** Check if either process can starve while waiting on the other.

---

### Invariant Deductions & Solutions:

1. **Mutual Exclusion: SATISFIED ($\boldsymbol{\checkmark}$)**
   - **Assertion:** $P_0 \in \text{CS} \implies \text{turn} = 0$, and $P_1 \in \text{CS} \implies \text{turn} = 1$.
   - **Joint Predicate:** $(P_0 \in \text{CS} \land P_1 \in \text{CS}) \implies (\text{turn} = 0 \land \text{turn} = 1) \equiv \bot$.
   - Atomic memory cell `turn` cannot hold two scalar values simultaneously. Mutual Exclusion holds unconditionally.

2. **Progress: VIOLATED ($\boldsymbol{\times}$)**
   - **Remainder Section Test:** Suppose $P_0$ executes CS, sets `turn = 1`, and enters an infinite Remainder Section (or terminates).
   - $P_1$ executes CS, sets `turn = 0`, and wants to re-enter. $P_1$ checks $W_1 = (\text{turn} \ne 1) \equiv (0 \ne 1) \equiv \text{true}$.
   - $P_1$ is blocked indefinitely by $P_0$ which is idle in its Remainder Section. Progress fails.

3. **Bounded Waiting: SATISFIED ($\boldsymbol{\checkmark}$)**
   - Neither process can enter twice in a row. Once $P_0$ exits, it sets `turn = 1`, guaranteeing $P_1$ enters next before $P_0$ can enter again. $\text{Bypasses}(P_i) \le 1$.

---

## Variation 3: Two-Flag "Polite" Protocol

Only an intention array is used, with no tie-breaking `turn` variable.

```c
// Shared variables
bool flag[2] = {false, false};

// Code for Process P_i (i = 0 or 1, j = 1 - i)
do {
    flag[i] = true;
    while (flag[j]);

    // Critical Section

    flag[i] = false;

    // Remainder Section
} while (true);
```

### Questions & Tasks:
- **Mutual Exclusion:** Assume both $P_0$ and $P_1$ are inside the CS. For both to be inside, both passed `while (flag[j])`. Can both read `flag[j] == false` before either sets `flag[i] = true`?
- **Progress:** Set `flag[0] = true` and `flag[1] = true` simultaneously. Can both while-loops evaluate to `true` forever?
- **Bounded Waiting:** Evaluate if starvation or deadlock occurs.

---

### Invariant Deductions & Solutions:

1. **Mutual Exclusion: SATISFIED ($\boldsymbol{\checkmark}$)**
   - **Assertion:** $P_0 \in \text{CS} \implies \text{flag}[0] = \text{true} \land \text{flag}[1] = \text{false}$ (at the moment $P_0$ passed the loop).
   - For both to be inside, both must have observed the other's flag as `false`. But each asserts its own flag to `true` *before* checking the other's flag.
   - Therefore, at least one process will see `flag[j] == true` and spin. Concurrent entry is impossible $\implies (P_0 \in \text{CS} \land P_1 \in \text{CS}) \implies \bot$.

2. **Progress: VIOLATED ($\boldsymbol{\times}$)**
   - **Deadlock Trap Test:** $P_0$ sets `flag[0] = true` and $P_1$ sets `flag[1] = true` concurrently.
   - Global Trapping Predicate: $\Phi_{\text{Deadlock}} = W_0 \land W_1 = (\text{flag}[1] == \text{true}) \land (\text{flag}[0] == \text{true})$.
   - This predicate holds without any contradiction! Both processes spin forever at their `while` loops while CS is empty $\implies$ Deadlock reachable $\implies$ Progress fails.

3. **Bounded Waiting: VIOLATED ($\boldsymbol{\times}$)**
   - Deadlock represents infinite waiting; no finite upper bound on entry exists when deadlocked.
