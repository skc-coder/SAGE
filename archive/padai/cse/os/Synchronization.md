## 1. Why Synchronization?

Multiple processes/threads share resources — memory, files, devices. Without coordination, concurrent access leads to **race conditions**: the outcome depends on the exact order of execution, which is non-deterministic.

### Race Condition Example

```c
// Both threads run: counter++
// Actual machine instructions:
//   LOAD R, counter
//   ADD  R, 1
//   STORE counter, R

// Thread 1: LOAD R = 5
// Thread 2: LOAD R = 5
// Thread 1: STORE counter = 6
// Thread 2: STORE counter = 6   <-- should be 7, got 6
```

The solution is to ensure that shared data is accessed by **only one process at a time** in certain sections of code — this is the **critical section problem**.

---

## 2. The Critical Section Problem

A **critical section** is a segment of code where a process accesses shared resources (shared variables, files, etc.).

### Structure of a Process

```
do {
    // --- entry section ---
    // (request permission to enter CS)

        // CRITICAL SECTION
        // (access shared resource here)

    // --- exit section ---
    // (signal that CS is done)

        // REMAINDER SECTION
        // (rest of the code)

} while (true);
```

### Three Requirements (must memorize)

Any correct solution to the critical section problem must satisfy all three:

| Requirement          | Meaning                                                                                                                                                                                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mutual Exclusion** | If process P is in its CS, no other process can be in its CS at the same time.                                                                                                                                                                              |
| **Progress**         | If no process is in the CS and some processes want to enter, only those not in their remainder section can decide who enters next — and this decision cannot be postponed indefinitely. (in the cs the program will do its task, not other managment tasks) |
| **Bounded Waiting**  | There must be a bound on the number of times other processes can enter the CS after a process has requested entry and before that request is granted. (No starvation.)                                                                                      |

> [!important] GATE loves asking which property a broken solution violates.
> 
> - No mutual exclusion → **race condition**
> - No progress → **deadlock** (no one can enter)
> - No bounded waiting → **starvation** (someone waits forever)

---

## 3. Peterson's Solution

A **software-only** solution for two processes (P0 and P1). Uses two shared variables:

```c
int turn;          // whose turn it is to enter CS
bool flag[2];      // flag[i] = true means Pi WANTS to enter CS
```

### Code for Process Pi (the other is Pj, where j = 1 - i)

```c
// Entry section
flag[i] = true;       // "I want to enter"
turn = j;             // "but you go first if you want"
while (flag[j] && turn == j)
    ;                 // busy-wait

    // CRITICAL SECTION

// Exit section
flag[i] = false;      // "I'm done"
```

### Why it works

- **Mutual exclusion:** Both can only be in CS if `turn == i` AND `turn == j` simultaneously — impossible.
- **Progress:** If Pj doesn't want to enter (`flag[j] == false`), Pi enters immediately.
- **Bounded waiting:** Pi waits at most one entry by Pj before getting its turn.

### Limitation

- Only works for **two processes**.
- Relies on **sequential consistency** of memory — modern CPUs reorder instructions, so Peterson's may fail on real hardware without memory barriers.
- **Busy-waits** (wastes CPU).

---

## 4. Hardware Solutions

### 4.1 Disabling Interrupts

```c
// Entry
disable_interrupts();

    // CRITICAL SECTION

// Exit
enable_interrupts();
```

- Works on **uniprocessor** systems — no context switch can occur without an interrupt.
- Fails on **multiprocessors** — disabling interrupts on one CPU doesn't affect others.
- Dangerous — user process can hold CPU forever. Only used inside the kernel itself.

### 4.2 Atomic Instructions (Hardware Locks)

Modern CPUs provide special instructions that execute as a single, uninterruptible unit.

#### `test_and_set()`

```c
// Hardware definition (atomic):
bool test_and_set(bool *target) {
    bool old = *target;
    *target = true;
    return old;
}

// Usage:
bool lock = false;

// Entry
while (test_and_set(&lock))   // spin until lock was false
    ;

    // CRITICAL SECTION

// Exit
lock = false;
```

- Returns old value, sets to `true`, all atomically.
- If lock was `false`: we get `false` returned, enter CS, lock is now `true`.
- If lock was `true`: we get `true` returned, keep spinning.

**Problem:** Does NOT guarantee bounded waiting — a process can starve.

#### `compare_and_swap()` (CAS)

```c
// Hardware definition (atomic):
int compare_and_swap(int *value, int expected, int new_value) {
    int old = *value;
    if (old == expected)
        *value = new_value;
    return old;
}

// Usage:
int lock = 0;

// Entry
while (compare_and_swap(&lock, 0, 1) != 0)
    ;

    // CRITICAL SECTION

// Exit
lock = 0;
```

- Checks if `*value == expected`; if yes, sets to `new_value`. All atomic.
- CAS is the foundation of lock-free data structures in the real world.

#### Bounded Waiting with test_and_set

To fix starvation, use a `waiting[]` array:

```c
bool waiting[n];   // waiting[i] = Pi is waiting to enter
bool lock = false;

// Entry for Pi:
waiting[i] = true;
bool key = true;
while (waiting[i] && key)
    key = test_and_set(&lock);
waiting[i] = false;

    // CRITICAL SECTION

// Exit for Pi:
// Find next waiting process j (in cyclic order)
j = (i + 1) % n;
while (j != i && !waiting[j])
    j = (j + 1) % n;

if (j == i)
    lock = false;      // no one waiting, release lock
else
    waiting[j] = false; // hand off directly to Pj
```

This satisfies all three requirements including bounded waiting.

---

## 5. Semaphores

A **semaphore** is an integer variable accessed only through two atomic operations:

```c
wait(S):             signal(S):
  while (S <= 0)       S++;
      ;  // busy wait
  S--;
```

Also written as `P(S)` / `V(S)` (from Dutch: Proberen/Verhogen — test/increment).

### Types

| Type                         | Initial value        | Use                                    |
| ---------------------------- | -------------------- | -------------------------------------- |
| **Binary semaphore** (mutex) | 1                    | Mutual exclusion. Behaves like a lock. |
| **Counting semaphore**       | N (any positive int) | Managing a resource pool of size N.    |

### Mutual Exclusion with Semaphore

```c
Semaphore mutex = 1;

// Process Pi:
wait(mutex);
    // CRITICAL SECTION
signal(mutex);
```

### Blocking Semaphore (No Busy Wait)

Instead of spinning, block the process:

```c
typedef struct {
    int value;
    struct process *list;  // waiting queue
} Semaphore;

wait(S):
    S.value--;
    if (S.value < 0) {
        add this process to S.list;
        block();      // put process to sleep
    }

signal(S):
    S.value++;
    if (S.value <= 0) {
        remove process P from S.list;
        wakeup(P);    // wake it up
    }
```

> [!note] With blocking semaphores, `S.value` can go negative. `|S.value|` = number of processes waiting on S.

### Semaphore Problems

**Deadlock:** Two processes each waiting for a signal the other will never send.

```c
// P0:          P1:
wait(S);        wait(Q);
wait(Q);        wait(S);   // deadlock
```

**Priority Inversion:** High-priority process waiting for a resource held by a low-priority process, which is preempted by a medium-priority process. Solution: **priority inheritance protocol**.

---

## 6. Classic Problem: Producer-Consumer (Bounded Buffer)

**Problem:** Producer generates items into a shared buffer of size N. Consumer takes items out. Neither should overflow or underflow the buffer.

```c
Semaphore mutex = 1;    // mutual exclusion on buffer
Semaphore empty = N;    // counts empty slots (initially all N are empty)
Semaphore full  = 0;    // counts full slots (initially 0)

// Producer:
do {
    // produce item
    wait(empty);         // wait for an empty slot
    wait(mutex);         // lock buffer
        add item to buffer
    signal(mutex);       // unlock
    signal(full);        // one more full slot
} while (true);

// Consumer:
do {
    wait(full);          // wait for a full slot
    wait(mutex);         // lock buffer
        remove item from buffer
    signal(mutex);       // unlock
    signal(empty);       // one more empty slot
    // consume item
} while (true);
```

> [!warning] Order matters! `wait(mutex)` must come AFTER `wait(empty)` / `wait(full)`. If you do `wait(mutex)` first, a producer holding the mutex while buffer is full will deadlock with a consumer waiting for mutex.

---

## 7. Classic Problem: Reader-Writer

**Problem:** Multiple readers can read simultaneously. A writer needs exclusive access — no readers or other writers while writing.

### First Readers-Writers Problem (Readers priority)

Readers are never kept waiting unless a writer has already been granted access.

```c
Semaphore rw_mutex = 1;   // exclusive access for writers
Semaphore mutex   = 1;    // protect read_count
int read_count = 0;       // number of active readers

// Writer:
wait(rw_mutex);
    // WRITE
signal(rw_mutex);

// Reader:
wait(mutex);
    read_count++;
    if (read_count == 1)
        wait(rw_mutex);    // first reader locks out writers
signal(mutex);

    // READ

wait(mutex);
    read_count--;
    if (read_count == 0)
        signal(rw_mutex);  // last reader lets writers in
signal(mutex);
```

**Problem with this solution:** Writers can **starve** — if readers keep arriving, `read_count` never drops to 0, and no writer ever gets `rw_mutex`.

### Second Readers-Writers Problem (Writers priority)

Once a writer is waiting, no new readers are allowed. Writers get priority. Readers may starve instead.

Implementation uses an additional semaphore to queue new readers when a writer is waiting. (Covered in advanced OS; less common in GATE.)

### Reader-Writer with Monitors / rwlock

Modern systems use `pthread_rwlock_t` which handles this internally. Understand the semaphore version for GATE.

---

## 8. Classic Problem: Dining Philosophers

**Problem:** 5 philosophers sit around a table. Between each pair is one chopstick (5 total). A philosopher needs both adjacent chopsticks to eat. They alternate between thinking and eating.

```
        [Phil 0]
   [c4]          [c0]
[Phil 4]          [Phil 1]
   [c3]          [c1]
      [Phil 3][Phil 2]
           [c2]
```

### Naive (Broken) Solution

```c
Semaphore chopstick[5] = {1, 1, 1, 1, 1};

// Philosopher i:
do {
    wait(chopstick[i]);            // pick up left
    wait(chopstick[(i+1) % 5]);   // pick up right
        // EAT
    signal(chopstick[i]);
    signal(chopstick[(i+1) % 5]);
    // THINK
} while (true);
```

**Deadlock:** All 5 philosophers pick up their left chopstick simultaneously. All wait for the right. No one eats. System is deadlocked.

### Solutions

#### Solution 1: Allow at most 4 philosophers at the table

```c
Semaphore table = 4;   // at most 4 can try to eat simultaneously

// Philosopher i:
wait(table);
wait(chopstick[i]);
wait(chopstick[(i+1) % 5]);
    // EAT
signal(chopstick[(i+1) % 5]);
signal(chopstick[i]);
signal(table);
```

At most 4 try to grab chopsticks, so at least one can always get both. Deadlock-free.

#### Solution 2: Asymmetric solution

- Even-numbered philosophers pick **left then right**.
- Odd-numbered philosophers pick **right then left**.

This breaks the circular wait condition. Deadlock-free.

#### Solution 3: Pick up both or neither (Monitor-based)

```c
// Philosopher only picks up chopsticks if BOTH are available.
// Uses a monitor with state tracking.

enum {THINKING, HUNGRY, EATING} state[5];
Semaphore self[5] = {0};   // for blocking individual philosophers
Semaphore mutex = 1;

void pickup(int i) {
    wait(mutex);
    state[i] = HUNGRY;
    test(i);               // try to enter EATING
    signal(mutex);
    wait(self[i]);         // block if couldn't eat
}

void putdown(int i) {
    wait(mutex);
    state[i] = THINKING;
    test((i+4)%5);         // check if left neighbor can now eat
    test((i+1)%5);         // check if right neighbor can now eat
    signal(mutex);
}

void test(int i) {
    if (state[(i+4)%5] != EATING &&
        state[i] == HUNGRY &&
        state[(i+1)%5] != EATING) {
        state[i] = EATING;
        signal(self[i]);
    }
}
```

This guarantees no deadlock and no starvation (with fair scheduling).

---

## 9. Monitors

A **monitor** is a high-level synchronization construct. Only one process can be active inside the monitor at a time — mutual exclusion is built in, you don't manage it manually.

```
monitor MonitorName {
    // shared variables

    condition x, y;   // condition variables

    procedure P1() { ... }
    procedure P2() { ... }

    // initialization code
}
```

### Condition Variables

Inside a monitor, you use **condition variables** (not semaphores):

```c
x.wait()    // suspends the calling process; releases monitor lock
x.signal()  // resumes one process waiting on x; if none, does nothing
```

> [!note] Key difference from semaphore signal: `signal()` on a semaphore always increments — it has memory. `x.signal()` on a condition variable does nothing if no one is waiting — no memory.

### Producer-Consumer with Monitor

```c
monitor BoundedBuffer {
    int buffer[N];
    int count = 0, in = 0, out = 0;
    condition not_full, not_empty;

    void insert(int item) {
        if (count == N) not_full.wait();
        buffer[in] = item;
        in = (in + 1) % N;
        count++;
        not_empty.signal();
    }

    int remove() {
        if (count == 0) not_empty.wait();
        int item = buffer[out];
        out = (out + 1) % N;
        count--;
        not_full.signal();
        return item;
    }
}
```

Much cleaner than raw semaphores — the mutual exclusion is implicit.

---

## 10. Other Synchronization Mechanisms

### Spinlocks

A lock where the waiting thread **busy-waits** (spins in a loop checking the lock). No OS involvement, no context switch.

- Good when: wait time is very short (less than a context switch cost), multiprocessor systems.
- Bad when: wait time is long — wastes entire CPU cycles.

Used heavily inside OS kernels and interrupt handlers.

### Mutex (Mutual Exclusion Lock)

Binary semaphore with ownership — only the thread that locked it can unlock it. If you try to lock an already-locked mutex, you **block** (sleep), not spin.

```c
pthread_mutex_t m = PTHREAD_MUTEX_INITIALIZER;
pthread_mutex_lock(&m);
    // critical section
pthread_mutex_unlock(&m);
```

### Read-Write Locks (rwlock)

Allows multiple concurrent readers OR one exclusive writer. Already covered conceptually in the Reader-Writer problem. `pthread_rwlock_t` in POSIX.

### Barriers

All threads must reach the barrier before any can proceed past it. Used in parallel computation to synchronize phases.

```c
pthread_barrier_wait(&barrier);
// all threads reach here before any continues
```

### Condition Variables (pthread)

```c
pthread_cond_wait(&cond, &mutex);    // release mutex, sleep, re-acquire on wake
pthread_cond_signal(&cond);          // wake one waiter
pthread_cond_broadcast(&cond);       // wake all waiters
```

Always used with a mutex. The standard pattern:

```c
pthread_mutex_lock(&mutex);
while (!condition)                   // always while, not if
    pthread_cond_wait(&cond, &mutex);
// do work
pthread_mutex_unlock(&mutex);
```

Use `while` not `if` — spurious wakeups can occur.

### Futex (Linux)

"Fast userspace mutex." Tries to acquire in userspace first (like a spinlock); only makes a syscall if it actually needs to wait. Used internally by pthreads. Not directly used in application code.

---

## 11. Deadlock vs Starvation vs Race Condition

| Definition         | Example                                                                                                |                                                                |
| ------------------ | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| **Race condition** | Outcome depends on execution order of concurrent processes                                             | Two threads incrementing a counter simultaneously              |
| **Deadlock**       | Set of processes each waiting for an event that only another blocked process can cause — circular wait | Dining philosophers all grab left chopstick                    |
| **Starvation**     | A process is perpetually denied a resource even though no deadlock — others keep getting it first      | Readers-priority RW lock starving writers                      |
| **Livelock**       | Processes keep changing state in response to each other but make no progress                           | Two people stepping aside for each other in a hallway, forever |

---

## 12. GATE Angle

> [!tip] High-frequency GATE questions

**Critical Section:**

- Which requirement does Peterson's solution satisfy? → All three.
- A solution where P0 always enters before P1 violates? → Bounded waiting (P1 starves).
- A solution where both can enter CS simultaneously violates? → Mutual exclusion.

**Semaphores:**

- Binary semaphore initial value? → 1.
- Counting semaphore for N-item buffer → `empty = N`, `full = 0`.
- If semaphore value is -3, how many processes are waiting? → 3.
- `wait()` is also called? → `P()`, `down()`.
- `signal()` is also called? → `V()`, `up()`.

**Producer-Consumer:**

- Correct order in producer: `wait(empty)` then `wait(mutex)` — never reverse.
- Reversing order → deadlock.

**Dining Philosophers:**

- Naive solution problem? → Deadlock (all grab left chopstick).
- Minimum number of philosophers that must be allowed at the table to avoid deadlock? → 4 (for 5 philosophers with 5 chopsticks).
- Which deadlock condition does the asymmetric solution break? → Circular wait.

**Monitors:**

- `x.signal()` when no one is waiting → does nothing (unlike semaphore V).
- How many processes inside a monitor at once? → At most 1.

**General:**

- `test_and_set` guarantees mutual exclusion? → Yes.
- `test_and_set` guarantees bounded waiting? → No (need additional mechanism).
- Which is faster: mutex or spinlock for short CS on multiprocessor? → Spinlock.

---

## 13. Summary Mind Map

```
SYNCHRONIZATION
│
├── Problem: Race Condition
│     └── Solution: Critical Section
│           ├── Requirements: Mutual Exclusion, Progress, Bounded Waiting
│
├── Software Solutions
│     └── Peterson's (2 processes only)
│
├── Hardware Solutions
│     ├── Disable interrupts (uniprocessor only)
│     ├── test_and_set (mutual exclusion, no bounded waiting)
│     └── compare_and_swap (CAS — foundation of lock-free programming)
│
├── Semaphores
│     ├── Binary (mutex) — init 1
│     ├── Counting — init N
│     ├── Busy-wait vs Blocking
│     └── Problems: Deadlock, Starvation, Priority Inversion
│
├── Classic Problems
│     ├── Producer-Consumer → 3 semaphores: mutex, empty, full
│     ├── Reader-Writer → rw_mutex + read_count + mutex
│     └── Dining Philosophers → deadlock by default; fix: max 4, asymmetric, or monitor
│
├── Monitors
│     ├── Built-in mutual exclusion
│     └── Condition variables: wait() / signal()
│
└── Other Mechanisms
      ├── Spinlock — busy-wait, short CS, multiprocessor
      ├── Mutex — blocking, owns lock
      ├── rwlock — multiple readers or one writer
      ├── Barriers — sync phases in parallel programs
      └── Futex — fast userspace mutex (Linux internals)
```

---

## Related Notes

- [[fork() and exec()]]
- [[User-Level vs Kernel-Level Threads]]
- [[Deadlock — Detection, Prevention, Avoidance]]
- [[CPU Scheduling]]