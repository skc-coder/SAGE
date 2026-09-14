## 6. GATE Exam Corner Cases & Invariants

### Example 1: Net Semaphore Arithmetic
> [!formula] Net Semaphore State Equation
> $$\text{Final Value} = S_{\text{init}} + \#V - \#P$$

- **Problem (GATE 1992):** A counting semaphore $S$ is initialized to $7$. Then $20\ P$ operations and $15\ V$ operations are performed on $S$. What is the final value?
  $$\text{Final Value} = 7 - 20 + 15 = 2$$

---

### Example 2: Non-Terminating Loop with Asymmetric Releases
Consider 3 processes with binary semaphores $S_0 = 1, S_1 = 0, S_2 = 0$:

```c
// Process P0:
while (true) {
    wait(S0);
    print("0");
    release(S1);
    release(S2);
}

// Process P1:
wait(S1);
release(S0);

// Process P2:
wait(S2);
release(S0);
```

- **Analysis:**
  1. $P_0$ enters first ($S_0 = 1 \to 0$), prints `"0"`.
  2. $P_0$ executes `release(S1)` $\implies S_1 = 1$, and `release(S2)` $\implies S_2 = 1$.
  3. $P_1$ and $P_2$ can both become unblocked.
  4. Whichever runs ($P_1$ or $P_2$) performs `release(S0)`. Since $S_0$ is a **binary semaphore**, releasing it twice without an intervening `wait(S0)` clamps its maximum value to $1$.
  5. Thus, $P_0$ can re-enter at least once more.
  - **Result:** $P_0$ prints `"0"` **at least 2 times** (and up to 3 times depending on the precise scheduling sequence of $P_1$ and $P_2$). If $S_0$ had been a counting semaphore, $P_0$ would run exactly 3 times.

---

### Example 3: Mutual Exclusion Violation due to Asymmetric Signaling (GATE 1997)
Consider $9$ processes $P_1, \dots, P_9$ structured as:
```c
// P1 to P9:
while (1) {
    P(mutex);
    /* Critical Section */
    V(mutex);
}
```
And a process $P_{10}$ structured as:
```c
// P10:
while (1) {
    V(mutex);
    /* Critical Section */
    V(mutex);
}
```
If `mutex` is a binary semaphore initialized to $1$:

> [!trap] Critical Section Invariant Violation
> Because process $P_{10}$ contains a `while (1)` loop executing `V(mutex)` arbitrarily without any preceding `P(mutex)`, it continuously forces `mutex = 1`. 
> Consequently, **all 10 processes** ($P_1$ through $P_{9}$, plus $P_{10}$) can simultaneously enter the critical section.

---

### Example 4: Deadlock Detection from Acquisition Ordering
Given two binary semaphores $a = 1$ and $b = 1$:

| Option | Process $P_0$ | Process $P_1$ | Potential for Deadlock? |
| :--- | :--- | :--- | :--- |
| **(a)** | `P(a); P(b); CS; V(a); V(b);` | `P(a); P(b); CS; V(a); V(b);` | **No** (Identical lock acquisition order) |
| **(b)** | `P(a); P(b); CS; V(a); V(b);` | `P(b); P(a); CS; V(a); V(b);` | **Yes** (Circular wait: $P_0$ holds $a$, waits for $b$; $P_1$ holds $b$, waits for $a$) |
| **(c)** | `P(a); P(b); CS; V(a); V(b);` | `P(b); P(a); CS; V(b); V(a);` | **Yes** (Circular wait: inverted acquisition order) |
| **(d)** | `P(a); P(b); CS; V(a); V(b);` | `P(a); P(b); CS; V(b); V(a);` | **No** (Same lock acquisition order; release order does not affect deadlock) |

> [!property] Invariant: Deadlock Immunity via Resource Hierarchy
> The release order (`V(x)`) has **zero impact** on deadlock formation. Deadlock can only arise if there exists a circular wait in the **lock acquisition sequence** (`P(x)`). Enforcing a universal, global order on all `wait` operations guarantees freedom from circular wait.
