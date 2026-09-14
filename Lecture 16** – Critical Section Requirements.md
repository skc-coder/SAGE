---
tags:
  - operating-systems
  - concurrency
  - synchronization
  - gate-cs
---
# Concurrency, Race Conditions, and Critical Section Requirements

## 1. Shared Counter & Race Condition Mechanics

When multiple threads access shared mutable state without proper synchronization, non-atomic machine instructions allow interleavings that cause race conditions.

Consider two concurrent threads executing an increment loop on a shared integer:

```c
// Shared variable residing in process heap/data segment
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

At the assembly level, a high-level language statement like `count++` is not atomic. On standard register-memory architectures, it compiles into three distinct machine instructions:

```c
LOAD  R, count    // Instruction 1: Read memory cell into internal CPU register
INCR  R          // Instruction 2: Arithmetic unit modifies register
STORE count, R    // Instruction 3: Write register back into memory cell
```

> [!definition] Race Condition
> A concurrent system state where the final outcome of an operation depends directly on the specific execution order, preemption timing, or relative scheduling of multiple threads or processes accessing shared memory.

### Extreme Value Derivations

The maximum and minimum possible final values of `count` after both threads finish their $10$ iterations each are bounded as follows:

1. **Maximum Value: $20$**
   Occurs when threads execute completely serially or context switches occur strictly outside of the critical three-instruction window.
   - $T_1$ runs all $10$ iterations to completion: $\text{count} = 10$.
   - $T_2$ runs all $10$ iterations to completion: $\text{count} = 20$.

2. **Minimum Value: $2$**
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

---

## 2. The Critical Section Problem & Synchronization Criteria

A section of code that accesses shared resources (such as memory, files, or hardware registers) is called a **Critical Section (CS)**.

```
        ┌─────────────────────────────────────────────────────────┐
        │        Critical Section Synchronization Criteria        │
        └────────────────────────────┬────────────────────────────┘
                                     │
                    ┌────────────────┴────────────────┐
                    ▼                                 ▼
        ┌──────────────────────┐          ┌──────────────────────┐
        │  Primary (Mandatory) │          │ Secondary (Optional) │
        ├──────────────────────┤          ├──────────────────────┤
        │ 1. Mutual Exclusion  │          │ 3. Bounded Waiting   │
        │ 2. Progress          │          │ 4. Architectural     │
        │                      │          │    Neutrality (Speed)│
        └──────────────────────┘          └──────────────────────┘
```

### Primary (Mandatory) Criteria

> [!definition] Mutual Exclusion (Safety Property)
> If process $P_i$ is executing in its critical section, no other process $P_j$ may execute in its critical section simultaneously. For all time instants $t$:
> $$\sum_{i=0}^{n-1} \mathbb{I}(P_i \in \text{CS}(t)) \le 1$$
> where $\mathbb{I}$ is the indicator function.

> [!definition] Progress (Liveness Property / Deadlock Freedom)
> If no process is executing in its critical section and one or more processes wish to enter, only those processes that are not executing in their remainder section can participate in deciding which process enters next, and this selection cannot be postponed indefinitely ($\ge 1$ process enters if there is demand).

> [!property] Completeness of Primary Criteria
> Mutual Exclusion ensures that at most one process enters ($\le 1$). Progress ensures that at least one process enters when needed ($\ge 1$). Together, they guarantee that exactly one process enters:
> $$\text{Mutual Exclusion } (\le 1) \;+\; \text{Progress } (\ge 1) \implies \text{Exactly One Process } (= 1)$$

### Secondary Criteria

> [!definition] Bounded Waiting (Fairness Property / Starvation Freedom)
> There exists a finite upper bound $k \in \mathbb{N}$ on the number of times other processes are allowed to enter their critical sections after a given process $P_i$ has made a formal request to enter and before that request is granted:
> $$\text{Bypasses}(P_i) \le k$$

> [!property] Architectural Neutrality (Speed Rule)
> No assumptions may be made regarding the relative hardware execution speeds, clock frequencies, or the total number of CPUs/cores running the concurrent processes.

---

## 3. Canonical Coordination Primitives: Metaphors & Mechanics

Software and hardware solutions utilize three core coordination abstractions:

| Mechanism | Metaphor | Write Authority | Core Vulnerability When Used Alone |
| :--- | :--- | :--- | :--- |
| `flag[i]` | Sticky note on a door | Local process only ($P_i$ writes `flag[i]`) | Deadlock under simultaneous declaration |
| `turn` | Shared physical token / baton | Shared ($P_i$ passes to $P_j$) | Progress violation (uninterested process blocks CS) |
| `lock` | Deadbolt on a door | Atomic Read-Modify-Write caller | Spinlock busy-waiting; starvation without queues |

### A. The Intention Flag (`flag[i]`)
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

### B. The Turn Variable (`turn`)
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

### C. The Hardware Lock (`lock`)
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

---

## 4. Software Synchronization Attempts: Step-by-Step Deconstructions

### Attempt 1: Single Shared Lock Variable

```c
// Shared variable: 0 = free, 1 = occupied
int interested = 0;

// Process P0                     // Process P1
while (interested);               while (interested);
interested = 1;                   interested = 1;
/* Critical Section */            /* Critical Section */
interested = 0;                   interested = 0;
```

- **Mutual Exclusion Check:** Assume $P_0$ executes `while (interested);` and reads $0$. Before it can execute `interested = 1`, it is preempted. $P_1$ runs, tests `interested`, reads $0$, sets `interested = 1`, and enters the CS. $P_0$ resumes, sets `interested = 1`, and enters the CS concurrently. **Violated ($\boldsymbol{\times}$)**.
- **Progress Check:** If the CS is idle ($\text{interested} = 0$), any requesting process immediately proceeds past the loop. No process outside the CS blocks entry. **Satisfied ($\boldsymbol{\checkmark}$)**.
- **Bounded Waiting Check:** A fast process exiting the CS can immediately loop around and re-acquire the lock before a preempted waiting peer executes its store. **Violated ($\boldsymbol{\times}$)**.

> [!trap] The Test-and-Set Separation Trap
> Separating the check of a condition (`while (interested)`) from its update (`interested = 1`) into distinct, non-atomic instructions will invariably violate Mutual Exclusion whenever preemption occurs between them.

### Attempt 2: Strict Alternation (Turn Variable)

```c
// Shared variable: 0 for P0, 1 for P1
int turn = 0;

// Process P0                     // Process P1
while (turn != 0);                while (turn != 1);
/* Critical Section */            /* Critical Section */
turn = 1;                         turn = 0;
```

- **Mutual Exclusion Check:** Since $\text{turn} \in \{0, 1\}$, the predicates $(\text{turn} == 0)$ and $(\text{turn} == 1)$ cannot evaluate to true simultaneously. At most one process enters. **Satisfied ($\boldsymbol{\checkmark}$)**.
- **Progress Check:** Suppose $P_0$ executes its CS, sets $\text{turn} = 1$, and enters a long remainder section. $P_1$ executes its CS, sets $\text{turn} = 0$, and finishes. If $P_1$ wants to re-enter the CS immediately, it is blocked at `while (turn != 1)` because $\text{turn} = 0$. $P_0$ is in its remainder section and has no desire to enter the CS, yet it prevents $P_1$ from entering. **Violated ($\boldsymbol{\times}$)**.
- **Bounded Waiting Check:** Neither process can enter twice consecutively. Once a process requests entry, it waits for at most one entry of the other process. **Satisfied ($\boldsymbol{\checkmark}$)**.

> [!trap] Strict Alternation Remainder Fault
> Never use pure turn-taking when processes run at differing frequencies. If process $P_i$ terminates in its remainder section while $\text{turn} = i$, all other processes are permanently blocked from the CS, resulting in a fatal progress failure.

### Attempt 3: Per-Process Intent Flags

```c
// Shared variable
int want[2] = {0, 0};

// Process P0                     // Process P1
want[0] = 1;                      want[1] = 1;
while (want[1] == 1);             while (want[0] == 1);
/* Critical Section */            /* Critical Section */
want[0] = 0;                      want[1] = 0;
```

- **Mutual Exclusion Check:** For $P_0$ to enter the CS, it must observe $\text{want}[1] == 0$. For $P_1$ to enter, it must observe $\text{want}[0] == 0$. Since each process asserts its own flag before testing the other's, both cannot simultaneously observe the other's flag as $0$. **Satisfied ($\boldsymbol{\checkmark}$)**.
- **Progress Check:** If $P_0$ executes `want[0] = 1` and is immediately preempted, and $P_1$ executes `want[1] = 1`, both reach their respective `while` loops. $P_0$ tests $\text{want}[1] == 1$ (true) and spins; $P_1$ tests $\text{want}[0] == 1$ (true) and spins. Both processes are deadlocked, and neither enters the empty CS. **Violated ($\boldsymbol{\times}$)**.
- **Bounded Waiting Check:** Deadlock is an infinite wait state; neither process can proceed. Under deadlock, bounded waiting is vacuous and broken. **Violated ($\boldsymbol{\times}$)**.

---

## 5. Comparative Evaluation of Software Attempts

| Attempt | Mutual Exclusion | Progress | Bounded Waiting | Root Mechanism Failure |
| :--- | :---: | :---: | :---: | :--- |
| **Attempt 1 (Lock)** | $\boldsymbol{\times}$ | $\boldsymbol{\checkmark}$ | $\boldsymbol{\times}$ | Non-atomic check and set instructions |
| **Attempt 2 (Turn)** | $\boldsymbol{\checkmark}$ | $\boldsymbol{\times}$ | $\boldsymbol{\checkmark}$ | Rigid alternation; inactive peer blocks entry |
| **Attempt 3 (Flags)** | $\boldsymbol{\checkmark}$ | $\boldsymbol{\times}$ | $\boldsymbol{\times}$ | Symmetric intent declaration creates deadlock |

---

## 6. Peterson's Algorithm & The Order Invariant

Peterson's Algorithm merges the intention flag array with an arbitration turn variable:

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

## 7. Formal Invariant-Driven Verification Framework

Forward tracing across thread interleavings leads to a combinatorial state-space explosion ($O(k^n)$ states for $n$ instructions across $k$ threads). For competitive examination verification, apply backward invariant analysis across the three requirements.

```
       System Synchronization Invariant Checks
                          │
       ┌──────────────────┼──────────────────┐
       ▼                  ▼                  ▼
Mutual Exclusion       Progress        Bounded Waiting
  (Safety ⊥)          (Deadlock &     (Re-entry Loop &
                      Livelock ⊥)     Strict Alternation)
```

### A. Mutual Exclusion Verification (Contradiction Method)

To verify whether a protocol guarantees Mutual Exclusion:

```
Step 1: Hypothesize Violation ──> Assume P0 ∈ CS and P1 ∈ CS concurrently at physical time t.
                                           │
Step 2: PC Postcondition    ──> Identify entry boundary conditions that must evaluate to TRUE.
                                           │
Step 3: State Invariant      ──> Derive the memory state required: C0(V) ∧ C1(V) = TRUE.
                                           │
Step 4: Contradiction Check  ──> Prove that C0(V) ∧ C1(V) requires conflicting memory values.
```

> [!theorem] Contradiction Invariant for Mutual Exclusion
> Mutual Exclusion holds unconditionally if and only if the joint assertion of multiple processes concurrently residing inside the critical section implies a logical contradiction in the system state space:
> $$(P_0 \in \text{CS} \land P_1 \in \text{CS}) \implies \bot$$

For example, in a pure turn-based protocol:
$$P_0 \in \text{CS} \implies \text{turn} = 0$$
$$P_1 \in \text{CS} \implies \text{turn} = 1$$
$$(P_0 \in \text{CS} \land P_1 \in \text{CS}) \implies (\text{turn} = 0 \land \text{turn} = 1)$$
Because a single physical memory word cannot hold two distinct scalar values simultaneously, $(\text{turn} = 0 \land \text{turn} = 1) \equiv \text{False} \equiv \bot$. Hence, Mutual Exclusion is guaranteed.

---

### B. Progress Verification (Invariant Method)

Progress is a **liveness property** requiring deadlock-freedom and absence of external interference.

> [!definition] Progress (Formal Invariant)
> If no process is executing in its critical section ($\text{CS}$) and at least one process requests entry, the decision of who enters next cannot be postponed indefinitely:
> $$\left( \forall i, \; P_i \notin \text{CS} \land \exists j, \; P_j \in \text{Entry} \right) \implies \lozenge \left( \exists k, \; P_k \in \text{CS} \right)$$
> where $\lozenge$ denotes temporal eventual occurrence.

To prove Progress using state invariants without manual thread interleaving, test two complementary conditions:

#### Condition 1: Deadlock Trap Invariant (All Waiting Processes Trapped)

Hypothesize that all contending processes are stalled simultaneously at their entry wait barriers while no process holds the $\text{CS}$.

1. Define the busy-wait condition $W_i(S)$ for each process $P_i$ across shared state vector $S$:
   $$P_i \text{ is spinning} \iff W_i(S) = \text{true}$$
2. Construct the global deadlock assertion $\Phi_{\text{Deadlock}}$:
   $$\Phi_{\text{Deadlock}} = \left( \bigwedge_{i \in \text{Contenders}} W_i(S) \right) \land \left( \forall i, \; P_i \notin \text{CS} \right)$$
3. **Contradiction Test:**
   - If $\Phi_{\text{Deadlock}} \implies \bot$ (system state contradiction), deadlock is physically impossible.
   - If $\Phi_{\text{Deadlock}}$ yields a valid, reachable assignment of state variables $S$, **Progress is VIOLATED**.

##### Example 1: Intent Flags Deadlock Proof (Attempt 3)
- Wait condition for $P_0$: $W_0 = (\text{want}[1] == 1)$
- Wait condition for $P_1$: $W_1 = (\text{want}[0] == 1)$
- Trapping assertion:
  $$\Phi_{\text{Deadlock}} = (\text{want}[1] == 1) \land (\text{want}[0] == 1)$$
Since both processes can reach their wait barriers having set their respective flags to $1$, the condition holds without contradiction. Hence, deadlock is reachable $\implies$ **Progress fails**.

##### Example 2: Peterson's Algorithm Livelock/Deadlock Proof
- Wait conditions:
  $$W_0 = (\text{flag}[1] == \text{true} \land \text{turn} == 1)$$
  $$W_1 = (\text{flag}[0] == \text{true} \land \text{turn} == 0)$$
- Global trapping predicate:
  $$\Phi_{\text{Deadlock}} = W_0 \land W_1 \implies (\text{turn} == 1) \land (\text{turn} == 0)$$
Because scalar cell `turn` cannot simultaneously evaluate to both $0$ and $1$:
$$(\text{turn} == 1 \land \text{turn} == 0) \equiv \bot$$
Deadlock is mathematically impossible.

#### Condition 2: Remainder Section Non-Interference Invariant

Hypothesize that only process $P_i$ wants to enter, while peer $P_j$ remains inactive in its Remainder Section ($\text{RS}$).

1. Set $P_j \in \text{RS} \implies \text{Interest}_j = \text{false}$ (or $P_j$ has halted).
2. Evaluate $P_i$'s wait condition $W_i(S)$:
   $$W_i(S \mid P_j \in \text{RS}) \stackrel{?}{=} \text{true}$$
3. **Interference Test:**
   - If $W_i(S)$ can evaluate to `true` while $P_j \in \text{RS}$, an uninterested or stalled peer is actively preventing an interested process from entering.
   - When an inactive peer can induce $W_i = \text{true}$, **Progress is VIOLATED**.

##### Example: Strict Alternation Remainder Fault (Attempt 2)
In Attempt 2: `while (turn != 1);` for $P_1$.
If $P_0$ is in its remainder section or terminates with $\text{turn} = 0$:
$$W_1 = (\text{turn} \ne 1) \equiv (0 \ne 1) \equiv \text{true}$$
$P_1$ spins indefinitely waiting for a write operation that $P_0$ will never execute $\implies$ **Progress fails**.

> [!property] Unified Progress Check Rules
> Progress is unconditionally guaranteed if and only if both conditions hold:
> 1. $\Phi_{\text{Deadlock}} = \bigwedge_i W_i(S) \implies \bot$ (No mutual entrapment)
> 2. $\forall i \ne j, \; \left( P_j \in \text{RS} \implies W_i(S) = \text{false} \right)$ (No remainder section blocking)

---

### C. Bounded Waiting Verification (Bypass Bound)

Bounded Waiting represents system fairness and guarantees the absence of starvation.

> [!definition] Bounded Waiting (Fairness)
> After a process initiates its entry request, there exists an upper bound on the number of entries granted to other processes before this request is satisfied.

#### The Re-entry Verification Test

To verify Bounded Waiting for any synchronization protocol:

```
Step 1: P0 is executing inside CS. P1 is waiting inside the entry section.
                                │
Step 2: P0 completes CS, executes its exit section, and re-enters its remainder section.
                                │
Step 3: P0 immediately loops around and attempts to re-enter CS.
                                │
Step 4: Verify whether P1 is guaranteed entry, or if P0 can bypass P1 unboundedly.
```

- **Pass Condition:** The protocol invariants force $P_0$'s second entry attempt to block, compelling the scheduler or memory state to grant entry to $P_1$.
- **Fail Condition:** $P_0$ successfully skips or clears its own wait barrier while $P_1$ remains blocked, establishing a cyclic bypass:
  $$P_0 \to P_0 \to P_0 \dots$$
  If bypass cycles can repeat infinitely without yielding to $P_1$, **Bounded Waiting is VIOLATED**.

> [!trap] Unbounded Re-entry Trap
> If a process $P_0$ can reset its own intent in the exit section without updating or passing the arbitration token (`turn`), it can loop through remainder code, reset its flag, observe the stale token still granting it priority, and bypass waiting peer $P_1$ indefinitely.

---

## 8. Hard Questions & Tricky Scenarios
<!-- Reserved for personal manual additions -->