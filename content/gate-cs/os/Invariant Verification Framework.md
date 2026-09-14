---
tags:
  - operating-systems
  - concurrency
  - synchronization
  - gate-cs
---
# Invariant Verification Framework

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

---

## 1. Mutual Exclusion Verification (Contradiction Method)

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
$$(P_0 \in \text{CS} \land P_1 \in \text{CS}) \implies (\text{turn} = 0 \land \text{turn} = 1) \equiv \bot$$

---

## 2. Progress Verification (Invariant Method)

Progress is a **liveness property** requiring deadlock-freedom and absence of external interference.

> [!definition] Progress (Formal Invariant)
> If no process is executing in its critical section ($\text{CS}$) and at least one process requests entry, the decision of who enters next cannot be postponed indefinitely:
> $$\left( \forall i, \; P_i \notin \text{CS} \land \exists j, \; P_j \in \text{Entry} \right) \implies \lozenge \left( \exists k, \; P_k \in \text{CS} \right)$$

To prove Progress using state invariants, test two complementary conditions:

### Condition A: Deadlock Trap Invariant (All Waiting Processes Trapped)

Hypothesize that all contending processes are stalled simultaneously at their entry wait barriers while no process holds the $\text{CS}$.

1. Define the busy-wait condition $W_i(S)$ for each process $P_i$ across shared state vector $S$:
   $$P_i \text{ is spinning} \iff W_i(S) = \text{true}$$
	Note that there are two kinds of busy-wait. One in which write also happens and one in which only reading events. The latter kinds is what we are talking about.
2. Construct the global deadlock assertion $\Phi_{\text{Deadlock}}$:
   $$\Phi_{\text{Deadlock}} = \left( \bigwedge_{i \in \text{Contenders}} W_i(S) \right) \land \left( \forall i, \; P_i \notin \text{CS} \right)$$
3. **Contradiction Test:**
   - If $\Phi_{\text{Deadlock}} \implies \bot$, deadlock is physically impossible.
   - If $\Phi_{\text{Deadlock}}$ yields a valid, reachable assignment of state variables $S$, **Progress is VIOLATED**.

### Condition B: Remainder Section Non-Interference Invariant

Hypothesize that only process $P_i$ wants to enter, while peer $P_j$ remains inactive in its Remainder Section ($\text{RS}$).

1. Set $P_j \in \text{RS} \implies \text{Interest}_j = \text{false}$ (or $P_j$ has halted).
2. Evaluate $P_i$'s wait condition $W_i(S)$:
   $$W_i(S \mid P_j \in \text{RS}) \stackrel{?}{=} \text{true}$$
3. **Interference Test:**
   - If $W_i(S)$ can evaluate to `true` while $P_j \in \text{RS}$, an uninterested or stalled peer is actively preventing an interested process from entering $\implies$ **Progress is VIOLATED**.

> [!property] Unified Progress Check Rules
> Progress is unconditionally guaranteed if and only if both conditions hold:
> 1. $\Phi_{\text{Deadlock}} = \bigwedge_i W_i(S) \implies \bot$ (No mutual entrapment)
> 2. $\forall i \ne j, \; \left( P_j \in \text{RS} \implies W_i(S) = \text{false} \right)$ (No remainder section blocking)

---

## 3. Bounded Waiting Verification (Bypass Bound)

Bounded Waiting represents system fairness and guarantees the absence of starvation.

### The Re-entry Verification Test

```
Step 1: P0 is executing inside CS. P1 is waiting inside the entry section.
                                │
Step 2: P0 completes CS, executes its exit section, and re-enters its remainder section.
                                │
Step 3: P0 immediately loops around and attempts to re-enter CS.
                                │
Step 4: Verify whether P1 is guaranteed entry, or if P0 can bypass P1 unboundedly.
```

- **Pass Condition:** The protocol invariants force $P_0$'s second entry attempt to block, compelling entry for $P_1$.
- **Fail Condition:** $P_0$ successfully skips or clears its own wait barrier while $P_1$ remains blocked, establishing a cyclic bypass ($P_0 \to P_0 \to P_0 \dots$) $\implies$ **Bounded Waiting is VIOLATED**.
