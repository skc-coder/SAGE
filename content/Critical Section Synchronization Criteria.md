---
tags:
  - operating-systems
  - concurrency
  - synchronization
  - gate-cs
---
# Critical Section Synchronization Criteria

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

---

## 1. Primary (Mandatory) Criteria

> [!definition] Mutual Exclusion (Safety Property)
> If process $P_i$ is executing in its critical section, no other process $P_j$ may execute in its critical section simultaneously. For all time instants $t$:
> $$\sum_{i=0}^{n-1} \mathbb{I}(P_i \in \text{CS}(t)) \le 1$$
> where $\mathbb{I}$ is the indicator function.

> [!definition] Progress (Liveness Property / Deadlock Freedom)
> If no process is executing in its critical section and one or more processes wish to enter, only those processes that are not executing in their remainder section can participate in deciding which process enters next, and this selection cannot be postponed indefinitely ($\ge 1$ process enters if there is demand).

> [!property] Completeness of Primary Criteria
> Mutual Exclusion ensures that at most one process enters ($\le 1$). Progress ensures that at least one process enters when needed ($\ge 1$). Together, they guarantee that exactly one process enters:
> $$\text{Mutual Exclusion } (\le 1) \;+\; \text{Progress } (\ge 1) \implies \text{Exactly One Process } (= 1)$$

---

## 2. Secondary Criteria

> [!definition] Bounded Waiting (Fairness Property / Starvation Freedom)
> There exists a finite upper bound $k \in \mathbb{N}$ on the number of times other processes are allowed to enter their critical sections after a given process $P_i$ has made a formal request to enter and before that request is granted:
> $$\text{Bypasses}(P_i) \le k$$

> [!property] Architectural Neutrality (Speed Rule)
> No assumptions may be made regarding the relative hardware execution speeds, clock frequencies, or the total number of CPUs/cores running the concurrent processes.
