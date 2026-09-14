# Synchronization: Invariant Analysis of the Critical Section Problem

## Conceptual Breakdown & Mechanics

### The Core Problem and Failure Modes of Forward Tracing
Analyzing concurrent protocols by forward execution tracing—generating interleavings step-by-step across all possible preemption points—leads to an exponential state space explosion ($O(k^n)$ states for $n$ instructions across $k$ threads). To reliably evaluate synchronization primitives under competitive exam conditions, we utilize **Invariant-Driven Analysis** and the **Contradiction Method**, working backward from violation states rather than forward from initial states.

### 1. Systematic Mutual Exclusion Verification (Contradiction Method)
Mutual Exclusion mandates that at most one process executes within its Critical Section ($\text{CS}$) at any single point in physical time $t$.

To verify Mutual Exclusion:
1. **Hypothesize the Violation:** Assume there exists an instant $t$ such that both $P_0$ and $P_1$ are concurrently inside the $\text{CS}$.
2. **Establish the Program Counter Postcondition:**
   - $P_0$ is inside $\text{CS} \implies P_0$ has executed its entry boundary test, but has **not** executed its exit statement.
   - $P_1$ is inside $\text{CS} \implies P_1$ has executed its entry boundary test, but has **not** executed its exit statement.
3. **Derive Invariants of Shared Variables:** Identify the conditions necessary for each process to cross the entry barrier into the $\text{CS}$.
   - If entry to $\text{CS}$ requires process $P_i$ to evaluate a condition $C_i(V) = \text{true}$ over shared state $V$, both $P_0$ and $P_1$ being in $\text{CS}$ requires $C_0(V) \land C_1(V)$ to hold simultaneously at their **respective points of passage**.
1. **Identify Invariant Contradictions:**
   - For a single scalar variable such as `turn`, $P_0 \in \text{CS} \implies \text{turn} = 0$, while $P_1 \in \text{CS} \implies \text{turn} = 1$. Since $\text{turn} \in \{0, 1\}$ is an atomic memory cell, $\text{turn} = 0 \land \text{turn} = 1$ is physically impossible, provided that the write statements to turn are in the RS.
   - Trace whether an intervening process can alter this state: if the modification instruction is guarded by a flag (e.g., `while (flag[j]);`), and the occupant holds its flag `flag[i] = true` until exit, the update instruction cannot physically execute before exit. Hence, a contradiction is reached, and Mutual Exclusion holds unconditionally.

### 2. Systematic Progress Verification (Deadlock-Freedom Equation)
Progress mandates that if no process is in its $\text{CS}$ and some processes wish to enter, only those processes not executing in their remainder sections can participate in deciding which will enter next, and this selection cannot be postponed indefinitely.

To verify Progress:
1. **Deadlock Trap State:** Set all interested processes' intention variables to active (e.g., $\text{flag}[0] = \text{true} \land \text{flag}[1] = \text{true}$) while no process is inside the $\text{CS}$ ($\text{CS}$ is empty).
2. **Evaluate Simultaneous Trapping:** Determine if all competing processes can be simultaneously trapped in busy-wait loops:
   $$\bigwedge_{i=0}^{n-1} \text{WaitCondition}_i = \text{true}$$
3. **Evaluate Remainder Isolation:** Consider the case where only a single process $P_i$ wishes to enter, while process $P_j$ remains inactive in its remainder section ($\text{flag}[j] = \text{false}$).
   - If $P_i$'s progress is blocked by a variable requiring $P_j$ to execute its entry or exit code (such as strict turn-taking where $\text{turn} = j$), the algorithm violates Progress.

### 3. Systematic Bounded Waiting Verification (Bypass Bound)
Bounded Waiting requires that there exists a limit on the number of times other processes are allowed to enter their critical sections after a process has made a request to enter and before that request is granted.

To verify Bounded Waiting:
1. **Inspect the Exit Section:** Check whether the exiting process explicitly transfers permission or updates arbitration state (e.g., toggling `turn` or waking a specific queue).
2. **Examine Re-entry Advantage:** If process $P_i$ exits the $\text{CS}$, sets $\text{flag}[i] = \text{false}$, but leaves the arbitration variable $\text{turn} = i$:
   - If $P_j$ is pre-empted while waiting inside the entry section, $P_i$ can loop back into its remainder code, re-issue an entry request, observe $\text{turn} = i$, and re-enter $\text{CS}$.
   - If $P_i$ can repeat this cycle unboundedly without yielding to $P_j$, Starvation occurs, and Bounded Waiting is violated.

---

## Revision Elements

> [!definition] Mutual Exclusion
> A system property ensuring that if process $P_i$ is executing in its critical section, no other processes are allowed to execute in their critical sections concurrently:
> $$\forall t, \quad \sum_{i=0}^{n-1} \mathbb{I}(P_i \in \text{CS}(t)) \le 1$$

> [!definition] Progress (Liveness)
> A property ensuring that if the critical section is empty and some processes want to enter, only processes currently requesting entry can participate in deciding who enters next, and this decision cannot be deferred indefinitely (deadlock freedom).

> [!definition] Bounded Waiting
> A fairness bound ensuring that for any process $P_i$ requesting entry to its critical section, the number of entries granted to any other process $P_j$ before $P_i$ enters is bounded by a finite constant $k \in \mathbb{N}$:
> $$\text{Bypasses}(P_i) \le k$$

> [!theorem] Contradiction Invariant for Mutual Exclusion
> Mutual Exclusion holds if and only if the joint assertion of processes residing inside the critical section implies a contradiction in the underlying system state space:
> $$(P_0 \in \text{CS} \land P_1 \in \text{CS}) \implies \bot$$

> [!theorem] Peterson's Order Invariant
> In two-process solutions using intention flags and a tie-breaking scalar, the intention must precede the tie-breaker:
> $$\text{flag}[i] \leftarrow \text{true} \prec \text{turn} \leftarrow j$$
> Inverting this sequence allows a thread to read an unasserted flag before its peer registers intent, breaking the invariant and violating Mutual Exclusion.

> [!formula] Strict Alternation Turn Invariant
> In pure turn-taking protocols where entry requires $\text{turn} = i$:
> $$\text{turn} \in \{0, 1\} \implies (\text{turn} = 0) \land (\text{turn} = 1) \equiv \text{False}$$
> Mutual exclusion is guaranteed unconditionally, but progress is strictly violated when $P_{1-i}$ halts in its remainder section.

---

## Traps & Edge Cases

* **Swapping the Peterson Statements:** Executing `turn = j` *before* `flag[i] = true` creates a window where $P_0$ sets `turn = 1` and is pre-empted. $P_1$ can then set `turn = 0`, set `flag[1] = true`, observe `flag[0] == false`, and enter $\text{CS}$. When $P_0$ resumes, it sets `flag[0] = true`, evaluates `turn == 0` (satisfied by $P_1$'s prior write), and also enters $\text{CS}$, violating Mutual Exclusion.
* **Exit Section Omission of Arbitration:** If the exit section only resets `flag[i] = false` and does not update `turn`, a fast process $P_i$ can loop through its remainder section and bypass a slow/pre-empted waiting process $P_j$ infinitely, violating Bounded Waiting.
* **Strict Alternation remainder fault:** In algorithms relying solely on a scalar variable `turn`, if $P_0$ leaves $\text{CS}$, sets `turn = 1`, and terminates, $P_1$ can enter once, set `turn = 0`, and subsequently be permanently blocked because $P_0$ never runs again to set `turn = 1`. This violates Progress.
* **Two-Flag Lockstep:** When only intention flags are used (`flag[i] = true; while (flag[j]);`), preemption after both write `flag[0] = flag[1] = true` leads to mutual blocking: both while-loops evaluate to $\text{true}$ forever. Mutual Exclusion is preserved, but Progress fails (deadlock).

---

## Practice Questions: Invariant-Based Deduction of Classic Variations

Apply the contradiction and invariant rules directly to these three classic variations to evaluate **Mutual Exclusion**, **Progress**, and **Bounded Waiting** without forward-tracing all interleavings.

---

### Variation 1: The Swapped Peterson Entry

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

#### Invariant Deductions:

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

### Variation 2: Pure Turn-Taking (Strict Alternation)

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

#### Invariant Deductions:

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

### Variation 3: Two-Flag "Polite" Protocol

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

#### Invariant Deductions:

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