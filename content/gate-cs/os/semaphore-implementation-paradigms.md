## 3. Implementation Paradigms of Semaphores

### Paradigm A: Spinlock-Based (Busy Waiting) Implementation
The classic high-level conceptual model implements atomic checking via busy waiting:

```c
// Process P_i:
P(S);
/* Critical Section */
V(S);
```

```c
/* Busy-wait implementation of P and V for Binary Semaphore */
void P(int *S) {
    while (*S == 0); // Busy wait (spins wasting CPU clock cycles)
    *S = 0;
}

void V(int *S) {
    *S = 1;
}
```

> [!trap] CPU Cycle Wastage
> The basic spinlock design suffers heavily from **busy waiting**. When a process is waiting to enter its critical section, it continuously spins inside the `while` loop, hogging CPU cycles that other ready processes could utilize.

---

### Paradigm B: Block-Wakeup Implementation (Without Busy Waiting)
To eliminate CPU cycle wastage, modern operating systems maintain a waiting queue inside the semaphore data structure:

```c
typedef struct {
    int value;
    struct process *queue;
} Semaphore;
```

#### 1. Binary Semaphore (Mutex) with Sleep/Wakeup
```c
void P(Semaphore *S) {
    if (S->value == 0) {
        put_in_queue(current_process);
        sleep(); // Transition to BLOCKED state
    }
    S->value = 0;
}

void V(Semaphore *S) {
    if (!is_empty(S->queue)) {
        Process *P = remove_from_queue();
        wakeup(P); // Transition to READY state
    }
    S->value = 1;
}
```

#### 2. Counting Semaphore with Sleep/Wakeup
```c
void P(Semaphore *S) {
    S->value--;
    if (S->value < 0) {
        put_in_queue(current_process);
        sleep(); // Process blocks itself
    }
}

void V(Semaphore *S) {
    S->value++;
    if (S->value <= 0) {
        Process *P = remove_from_queue();
        wakeup(P); // Wake up one suspended process
    }
}
```

> [!property] Physical Meaning of Semaphore Value ($S.\text{value}$)
> In the block-wakeup counting semaphore implementation:
> - **$S.\text{value} > 0$:** Represents the exact number of resource instances currently free and immediately available.
> - **$S.\text{value} = 0$:** All resource instances are currently in use; no processes are waiting in the queue.
> - **$S.\text{value} < 0$:** All resource instances are allocated, and the magnitude $|S.\text{value}|$ represents the exact number of processes currently blocked and waiting in the queue.

> [!property] Non-Blocking Property of $V(S)$
> The $P(S)$ operation can **block** a calling process if $S.\text{value} \le 0$ before allocation. In contrast, the $V(S)$ operation **never blocks** the executing process; it simply increments the value and optionally unblocks a sleeping process.
