## 5. Common Synchronization Patterns & Classical Problems

### Pattern 1: Basic Mutual Exclusion (Mutex)
To protect a critical section among $N$ processes:
- Initialize binary semaphore: $S = 1$.
- Enclose the critical section:

```c
P(S);
/* Critical Section */
V(S);
```

---

### Pattern 2: Statement Ordering / Precedence Enforcement
Suppose Process $A$ has statement $A_2$ and Process $B$ has statement $B_4$. We require that $A_2$ completes execution **strictly before** $B_4$ begins ($A_2 \to B_4$).

- Initialize synchronization semaphore: $S = 0$.
- Structure processes:

```c
// Process A:
A1;
A2;
V(S); // Signal that A2 is complete
A3;
A4;
A5;

// Process B:
B1;
B2;
P(S); // Wait until A signals completion
B4;
B5;
```

---

### Pattern 3: Strict Alternation of Outputs (`ABABAB...`)
Generate an infinite alternating sequence of characters `A` and `B` from two concurrent processes $P$ and $Q$.

```c
Semaphore S = 0; // Signals permission to print B
Semaphore T = 1; // Signals permission to print A

// Process P:
while (1) {
    P(T);
    print("A");
    V(S);
}

// Process Q:
while (1) {
    P(S);
    print("B");
    V(T);
}
```

---

### Pattern 4: Concurrency Limit and Overwriting Analysis
Consider a shared variable `k = 0` updated by 4 concurrent processes $W, X, Y, Z$:
```c
Read(k);
k = k + 1; // or k = k - 1, k = k - 2, k = k + 2
Write(k);
```
If access is governed by a counting semaphore initialized to $S = 2$, at most **two processes can execute concurrently** in the critical section at any moment.

> [!property] Bounded Interleaving Analysis
> - If $S = 1$, mutual exclusion is strictly preserved; interleaving is prevented, ensuring maximum consistency ($k_{\max} = k_{\min}$).
> - If $S = 2$, two processes can read an outdated value of $k$ concurrently, leading to lost updates. The final value depends on which process writes last, allowing values to be completely overwritten.

---

### Pattern 5: Preventing Interleaved Substrings
Given processes printing `00` and `11`:
```c
// Process P:
while (1) {
    // Blank W
    print("0");
    print("0");
    // Blank X
}

// Process Q:
while (1) {
    // Blank Y
    print("1");
    print("1");
    // Blank Z
}
```
To ensure the output string **never contains an odd run** of zeros or ones (i.e., no substrings like $01^n0$ or $10^n1$ where $n$ is odd):
- Mutual exclusion must be maintained around the pair of print operations to eliminate interleaving.
- Set:
  - $\text{Blank } W = P(S)$
  - $\text{Blank } X = V(S)$
  - $\text{Blank } Y = P(S)$
  - $\text{Blank } Z = V(S)$
  - Semaphore initialization: $S = 1$.
