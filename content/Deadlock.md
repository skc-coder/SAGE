## 1. What is Deadlock?

A set of processes is **deadlocked** if every process in the set is waiting for an event that can only be caused by another process in the same set — and no process can proceed.

Classic example: Process A holds resource R1 and waits for R2. Process B holds R2 and waits for R1. Neither can proceed. Ever.

---

## 2. Four Necessary Conditions (Coffman Conditions)

All four must hold **simultaneously** for deadlock to occur. Remove any one → deadlock cannot happen.

| Condition            | Meaning                                                                                                         |
| -------------------- | --------------------------------------------------------------------------------------------------------------- |
| **Mutual Exclusion** | At least one resource must be held in a non-shareable mode — only one process at a time can use it.             |
| **Hold and Wait**    | A process is holding at least one resource and waiting to acquire additional resources held by other processes. |
| **No Preemption**    | Resources cannot be forcibly taken from a process — they must be released voluntarily.                          |
| **Circular Wait**    | A set of processes {P0, P1, ..., Pn} exists such that P0 waits for P1, P1 waits for P2, ..., Pn waits for P0.   |

> [!important]
> These are **necessary** conditions, not sufficient. All four together make deadlock **possible** — whether it actually occurs depends on the execution order.

---

## 3. Resource Allocation Graph (RAG)

A directed graph used to describe resource allocation state.

### Nodes

- **Process node:** Circle — $P_i$
- **Resource node:** Rectangle — $R_j$ (dots inside = number of instances)

### Edges

- **Request edge:** $P_i \rightarrow R_j$ — process $P_i$ is requesting resource $R_j$
- **Assignment edge:** $R_j \rightarrow P_i$ — an instance of $R_j$ is assigned to $P_i$

### Deadlock Detection from RAG

**Single instance resources:**
- Deadlock exists **if and only if** the RAG contains a **cycle**.

**Multiple instance resources:**
- A cycle is **necessary but not sufficient** for deadlock.
- Must use the Banker's Algorithm or detection algorithm to confirm.

### Example RAG with deadlock

```

P1 ──request──► R1 ──assigned──► P2 ▲ │ │ │ assigned request │ │ R2 ◄──────────────────────────────┘

```

P1 holds R2, wants R1. P2 holds R1, wants R2. Cycle → deadlock.

### Example RAG without deadlock (cycle but no deadlock)

```

R1 has 2 instances. P1 holds one instance of R1, wants another. P2 holds one instance of R1. P3 is not involved.

```

Cycle exists (P1 → R1 → P2 → R1 → P1) but P2 can finish and release its instance of R1, allowing P1 to proceed. No deadlock.

---

## 4. Deadlock Prevention

**Idea:** Ensure at least one of the four Coffman conditions can never hold. Done statically at system design time.

### 4.1 Eliminate Mutual Exclusion

Make resources shareable. Only works for inherently shareable resources (read-only files). Cannot eliminate for resources like printers, mutexes. **Not generally practical.**

### 4.2 Eliminate Hold and Wait

Require a process to request **all resources at once** before starting. If it can't get all of them, it gets none.

**Protocol 1:** Request all resources before execution begins.

**Protocol 2:** Request resources only when holding none — release all current resources before requesting new ones.

**Problems:**
- Low resource utilization — resources held for entire duration even if not needed yet.
- Starvation possible — a process needing many popular resources may wait forever.

### 4.3 Allow Preemption (Eliminate No Preemption)

If a process holding resources requests one it cannot immediately get, all its currently held resources are preempted (taken away). Process restarts only when it can get all needed resources.

**Works well for:** Resources whose state can be saved and restored (CPU registers, memory pages).

**Does not work for:** Printers, tape drives — you can't "undo" a half-printed page.

### 4.4 Eliminate Circular Wait

Impose a **total ordering** on all resource types. Assign each resource a unique integer. Processes must request resources in **strictly increasing order** of their numbers.

If $R_i$ and $R_j$ are needed and $i < j$, process must request $R_i$ before $R_j$. It can never request a resource with a lower number than one it already holds.

**Why this works:** If every process follows the ordering, a circular wait is impossible — you can't have P1 waiting for P2's resource while P2 waits for P1's resource if both must acquire in the same order.

**Problem:** Hard to impose a useful ordering that fits all processes. May force unnecessary waiting.

### Prevention Summary

| Condition eliminated | Method | Problem |
|---|---|---|
| Mutual exclusion | Make resources shareable | Not always possible |
| Hold and wait | Request all at once or release before requesting | Low utilization, starvation |
| No preemption | Forcibly take resources | Only for preemptable resources |
| Circular wait | Total ordering on resources | Ordering may be inconvenient |

---

## 5. Deadlock Avoidance

**Idea:** Don't restrict how resources are requested. Instead, dynamically examine each request and grant it only if the resulting state is **safe**. Requires advance knowledge of maximum resource needs.

### Safe State

A state is **safe** if the OS can find a **safe sequence** — an ordering of all processes such that each process can eventually get all the resources it needs using currently available resources plus resources held by processes earlier in the sequence.

```
Safe state → no deadlock will occur (with careful scheduling) 
Unsafe state → deadlock may occur (not guaranteed, but possible) 
Deadlock → circular wait, no process can proceed

Safe ──────────────────────────────────► Unsafe ──────────► Deadlock (avoidance keeps us here) (might drift here) (stuck here)

```

> [!important]
> Safe state ≠ no deadlock right now. It means deadlock can be **avoided** going forward.
> Unsafe state ≠ deadlock right now. It means deadlock **cannot be guaranteed to be avoided**.

### 5.1 Resource Allocation Graph Algorithm (Single Instance)

Used when each resource type has exactly **one instance**.

Add a new type of edge: **claim edge** $P_i \dashrightarrow R_j$ (dashed) meaning $P_i$ may request $R_j$ in the future.

**Rule:** Grant a request only if converting the request edge to an assignment edge does not create a **cycle** in the RAG (including claim edges).

**Algorithm:**
1. When $P_i$ requests $R_j$, check if adding assignment edge $R_j \rightarrow P_i$ creates a cycle.
2. If no cycle → grant request.
3. If cycle → $P_i$ must wait.

Cycle detection on $n$ nodes = $O(n^2)$.

### 5.2 Banker's Algorithm (Multiple Instances)

The main avoidance algorithm. Works for multiple instances of each resource type.

**Data structures** (for $n$ processes, $m$ resource types):

| Structure          | Size         | Meaning                                             |
| ------------------ | ------------ | --------------------------------------------------- |
| `Available[m]`     | $m$          | Number of available instances of each resource type |
| `Max[n][m]`        | $n \times m$ | Maximum demand of each process for each resource    |
| `Allocation[n][m]` | $n \times m$ | Currently allocated resources to each process       |
| `Need[n][m]`       | $n \times m$ | Remaining resource need of each process             |

$$\text{Need}[i][j] = \text{Max}[i][j] - \text{Allocation}[i][j]$$

#### Safety Algorithm

Determines if the current state is safe. $O(n^2 \times m)$.

```

Work = Available (copy of available) Finish[i] = false for all i

Repeat: Find i such that: Finish[i] == false AND Need[i] <= Work (all resource types)

```
If found:
    Work = Work + Allocation[i]   (Pi finishes, releases resources)
    Finish[i] = true

If no such i found: STOP
```

If Finish[i] == true for all i → SAFE STATE Else → UNSAFE STATE

```

#### Resource Request Algorithm

When process $P_i$ makes request $\text{Request}_i$:

```

1. If Request_i > Need[i]: ERROR — exceeded maximum claim
    
2. If Request_i > Available: P_i must wait (resources not available)
    
3. Pretend to allocate (tentatively): Available = Available - Request_i Allocation[i] = Allocation[i] + Request_i Need[i] = Need[i] - Request_i
    
4. Run Safety Algorithm on this new state: If SAFE → grant the request (keep the allocation) If UNSAFE → rollback, P_i must wait
    

```

#### Banker's Algorithm Example

3 processes (P0, P1, P2), 3 resource types A, B, C.

```

```
      Allocation    Max        Need       Available
      A  B  C    A  B  C    A  B  C      A  B  C
```

P0 0 1 0 7 5 3 7 4 3 3 3 2 P1 2 0 0 3 2 2 1 2 2 P2 3 0 2 9 0 2 6 0 0

```

Check if current state is safe:

- Work = [3, 3, 2], all Finish = false
- Find $i$ where Need[i] ≤ Work:
  - P0: Need = [7,4,3] ≤ [3,3,2]? No
  - P1: Need = [1,2,2] ≤ [3,3,2]? Yes → allocate
    - Work = [3,3,2] + [2,0,0] = [5,3,2], Finish[1] = true
- Find next:
  - P0: [7,4,3] ≤ [5,3,2]? No
  - P2: [6,0,0] ≤ [5,3,2]? No
  - No process found → **UNSAFE** (deadlock possible)

Wait — recheck P2: Need = [6,0,0] ≤ [5,3,2]? 6 > 5. Correct, unsafe.

Safe sequence does not exist in this example. Let's use a corrected example:

```

```
      Allocation    Max        Need       Available
      A  B  C    A  B  C    A  B  C      A  B  C
```

P0 0 1 0 7 5 3 7 4 3 3 3 2 P1 2 0 0 3 2 2 1 2 2 P2 3 0 2 9 0 2 6 0 0 P3 2 1 1 2 2 2 0 1 1 P4 0 0 2 4 3 3 4 3 1

```

Safe sequence: P1 → P3 → P4 → P0 → P2 (verify each step yourself as practice).

> [!tip] GATE exam strategy for Banker's
> Write out the Need matrix first — that's where errors happen.
> Then simulate: find any process whose Need ≤ Work, execute it, update Work, repeat.
> If you can finish all processes → safe.

---

## 6. Deadlock Detection

Used when neither prevention nor avoidance is applied. Let deadlock happen, then detect and recover.

### 6.1 Single Instance — Wait-for Graph

Simplification of RAG — remove resource nodes, keep only process nodes. Draw edge $P_i \rightarrow P_j$ if $P_i$ is waiting for a resource held by $P_j$.

**Deadlock exists iff wait-for graph contains a cycle.**

Maintain the graph and run cycle detection periodically. $O(n^2)$.

### 6.2 Multiple Instances — Detection Algorithm

Similar to Banker's safety algorithm but without the Max matrix (we don't need future demand for detection).

**Data structures:**

- `Available[m]`
- `Allocation[n][m]`
- `Request[n][m]` — current outstanding requests (not maximum need)

```

Work = Available Finish[i] = false if Allocation[i] ≠ 0, else true

Repeat: Find i such that: Finish[i] == false AND Request[i] <= Work

```
If found:
    Work = Work + Allocation[i]
    Finish[i] = true
```

If Finish[i] == false for some i → those processes are DEADLOCKED

```

**When to run detection:**
- Every time a request cannot be granted immediately.
- Periodically (every hour, every time CPU utilization drops below threshold).
- More frequent detection → faster recovery, higher overhead.

---

## 7. Deadlock Recovery

Once deadlock is detected, the OS must break it.

### 7.1 Process Termination

**Option 1 — Abort all deadlocked processes:**
- Definitely breaks deadlock.
- Very expensive — all work done by those processes is lost.

**Option 2 — Abort one process at a time:**
- Abort one, run detection again, repeat until deadlock broken.
- Expensive in detection overhead but less wasteful.

**Which process to abort?** Based on:
- Process priority (abort lowest priority first)
- How long process has run and how much longer it needs
- Resources it holds (prefer one that holds many)
- How many processes need to be aborted
- Whether process is interactive or batch

### 7.2 Resource Preemption

Forcibly take resources from some processes and give to others.

Three issues to address:

**Selecting a victim:** Minimize cost — prefer process that has run shortest, holds fewest resources.

**Rollback:** After preemption, the victim process cannot continue normally. Options:
- Total rollback: abort and restart.
- Partial rollback: roll back only far enough to break deadlock (requires checkpointing).

**Starvation:** Same process may always be chosen as victim. Fix: include number of times preempted in cost calculation — after $k$ preemptions, no longer a candidate.

---

## 8. Comparison: Prevention vs Avoidance vs Detection

| | Prevention | Avoidance | Detection & Recovery |
|---|---|---|---|
| **When** | Design time | Runtime (each request) | After deadlock occurs |
| **Knowledge needed** | None | Max resource demand | None |
| **Overhead** | Low (static rules) | Per-request safety check | Periodic detection |
| **Utilization** | Low (over-restricts) | Medium | High |
| **Allows unsafe states?** | No | No | Yes |
| **Method** | Eliminate one Coffman condition | Banker's / RAG algorithm | Wait-for graph / Detection algo |
| **Used in practice** | Partially (resource ordering) | Rarely (too restrictive) | Most real OSes |

> [!note] Real OS behavior
> Most real operating systems (Linux, Windows) do **not** implement deadlock avoidance or prevention for user processes. They simply ignore deadlock and let users or applications handle it. Prevention via resource ordering is used inside the kernel itself (lock ordering).

---

## 9. Key Formulas and Results

$$\text{Need}[i][j] = \text{Max}[i][j] - \text{Allocation}[i][j]$$

**Minimum resources to guarantee no deadlock** (single resource type, $n$ processes, each needs at most $m$ instances):

$$\text{Min resources needed} = n \times (m - 1) + 1$$

This guarantees at least one process can always complete. With fewer resources, deadlock is possible.

**Example:** 5 processes, each needs at most 3 instances of a resource.
$$\text{Min} = 5 \times (3-1) + 1 = 11$$
With 11 instances, deadlock cannot occur.

**Deadlock possible with:** $n \times (m-1)$ instances — every process holds $m-1$, none can finish.

---

## 10. GATE Angle

> [!tip] Most tested concepts

**Conditions:**
- Which condition is easiest to eliminate in practice? → **Circular wait** (resource ordering).
- Which condition cannot be eliminated for a mutex? → **Mutual exclusion**.
- All four conditions necessary for deadlock? → Yes, all four must hold simultaneously.

**RAG:**
- Single instance + cycle → deadlock? → **Yes, always.**
- Multiple instance + cycle → deadlock? → **Not necessarily.**
- Single instance + no cycle → deadlock? → **No.**

**Banker's Algorithm:**
- Need matrix = Max - Allocation.
- Safe sequence exists → system is in safe state.
- After granting a request, if state is unsafe → **deny the request and rollback**.
- Banker's requires processes to declare **maximum** resource needs in advance.

**Detection:**
- Wait-for graph used for? → Single instance deadlock detection.
- Detection algorithm (multiple instance) — `Request` matrix, not `Need` matrix.

**Formula:**
- $n$ processes, each needs at most $m$ of one resource → minimum to prevent deadlock = $n(m-1)+1$.
- Example: 3 processes each needing at most 2 → min = $3(1)+1 = 4$.

**Tricky:**
- Deadlock avoidance keeps system in safe state — this does NOT mean no process is waiting.
- A system can be in an unsafe state without being deadlocked (yet).
- Prevention eliminates possibility; avoidance eliminates occurrence given correct decisions.

---
