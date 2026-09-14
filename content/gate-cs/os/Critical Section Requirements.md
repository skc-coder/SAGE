---
tags:
  - operating-systems
  - concurrency
  - synchronization
  - gate-cs
---
# Critical Section & Race Conditions (MOC)

## Index of Atomic Notes

- [[gate-cs/os/Shared Counter & Race Condition Mechanics]] — Assembly level execution (`LOAD`, `INCR`, `STORE`) and calculation of bounds ($2$ to $2N$).
- [[gate-cs/os/Critical Section Synchronization Criteria]] — Primary (Mutual Exclusion, Progress) and Secondary (Bounded Waiting, Architectural Neutrality) rules.
- [[gate-cs/os/Software Synchronization Primitives & Attempts]] — Primitives (`flag[i]`, `turn`, `lock`), code attempts (Attempts 1, 2, 3), hardware TestAndSet, and comparative matrix.
- [[gate-cs/os/Peterson's Algorithm & Order Invariant]] — Algorithm mechanics, mathematical correctness, and the critical write-order invariant.
- [[gate-cs/os/Invariant Verification Framework]] — Formal contradiction proofs for Mutual Exclusion, 2-condition Progress proofs, and Re-entry Bounded Waiting tests.
- [[gate-cs/os/Critical Section Practice Variations]] — Practice questions and step-by-step invariant deductions for classic protocol variations (Swapped Peterson, Pure Turn-Taking, Two-Flag Polite).

---

## 1. Quick Overview

```
                               ┌──────────────────────────────────────────────┐
                               │ Critical Section Synchronization Framework  │
                               └──────────────────────┬───────────────────────┘
                                                      │
                       ┌──────────────────────────────┴──────────────────────────────┐
                       ▼                                                            ▼
    ┌─────────────────────────────────────┐                      ┌─────────────────────────────────────┐
    │          Core Requirements          │                      │         Verification Method         │
    ├─────────────────────────────────────┤                      ├─────────────────────────────────────┤
    │ 1. Mutual Exclusion  (Safety ≤ 1)   │                      │ 1. Contradiction Proof (Safety)     │
    │ 2. Progress          (Liveness ≥ 1) │                      │ 2. Trapping & RS Invariants         │
    │ 3. Bounded Waiting   (Fairness)     │                      │ 3. Re-entry Bypass Loop Test        │
    └─────────────────────────────────────┘                      └─────────────────────────────────────┘
```

> [!property] Completeness of Primary Criteria
> Mutual Exclusion ensures at most one process enters ($\le 1$). Progress ensures at least one process enters when requested ($\ge 1$). Together:
> $$\text{Mutual Exclusion } (\le 1) \;+\; \text{Progress } (\ge 1) \implies \text{Exactly One Process } (= 1)$$