```cpp
// Shared variable: initialized to false (unlocked)
bool lock = false;

do {
    // Entry Section: Atomically test and acquire the lock
    while (test_and_set(&lock))
        ; // Busy waiting (spin-lock)

    // Critical Section
    // ...

    // Exit Section: Release the lock
    lock = false;

    // Remainder Section
    // ...
} while (true);
```

## Evaluation of Synchronization Criteria

> [!property] Formal Analysis of `test_and_set` Solution
> - **Mutual Exclusion ($\text{ME}$):** **Satisfied.** If process $P_i$ executes `test_and_set(&lock)` when `lock == false`, it receives `false`, exits the `while` loop, and sets `lock = true`. Any other process attempting to enter executes `test_and_set(&lock)`, receiving `true` and looping continuously until $P_i$ sets `lock = false`.
> - **Progress:** **Satisfied.** When no process is in the critical section (`lock == false`), any process wishing to enter can immediately execute `test_and_set(&lock)`, obtain `false`, and proceed into the $\text{CS}$.
> - **Bounded Waiting ($\text{BW}$):** **NOT Satisfied.** When multiple processes are spinning on the `while (test_and_set(&lock))` loop, hardware bus/cache arbitration does not guarantee first-come, first-served selection. A process may theoretically wait indefinitely if other contending processes repeatedly acquire the lock first. This causes **starvation**.

> [!formula] Advantages & Disadvantages Summary
> **Advantages:**
> 1. Applicable to any number of processes ($N \ge 2$).
> 2. Works seamlessly across uniprocessor and multiprocessor shared-memory environments.
> 3. Simple to implement and verify.
> 4. Multiple distinct critical sections can be supported simultaneously using distinct lock variables.
>
> **Disadvantages:**
> 1. **Busy Waiting (Spinlock):** While waiting, processes consume CPU cycles running the loop.
> 2. **Lack of Bounded Waiting:** Starvation can occur.
