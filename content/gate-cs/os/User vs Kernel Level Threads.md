## What is a Thread?

A thread is the smallest unit of CPU execution. A single process can have multiple threads, all sharing the same address space (code, data, heap) but each having its own stack, registers, and program counter.

---

## User-Level Threads (ULT)

Threads that are **managed entirely in user space** by a thread library. The kernel has no knowledge of their existence — it sees only one process.

**Examples:** POSIX Pthreads (in user mode), Java Green Threads (old JVM), GNU Pth

### How it works

The thread library handles:
- Thread creation and destruction
- Scheduling (which thread runs next)
- Context switching between threads
- Storing/restoring registers and stack

The kernel only schedules the **process** as a whole. From the kernel's perspective, the process is single-threaded.

### Advantages

- **Fast context switch** — no kernel mode transition needed, no system call overhead.
- **Portable** — runs on any OS, even ones with no thread support.
- **Flexible scheduling** — the application can implement its own scheduling policy.
- **No kernel resources consumed** — creating thousands of ULTs is cheap.

### Disadvantages

- **Blocking system calls block the entire process.** If one thread calls `read()` and it blocks, the kernel blocks the whole process — all other threads in that process stop too.
- **Cannot exploit multiple CPUs.** The kernel sees one process, maps it to one CPU. True parallelism is impossible.
- **Page faults stop all threads.** If one thread triggers a page fault, the whole process halts.

### Mapping model

`Many-to-One` — many user threads map to a single kernel thread (one process).

---

## Kernel-Level Threads (KLT)

Threads that are **managed directly by the OS kernel**. The kernel knows about each thread individually and schedules them independently.

**Examples:** Windows threads, Linux `pthreads` (in kernel mode, via `clone()`), Solaris LWP

### How it works

- Each thread has its own kernel-side data structures (Thread Control Block in kernel space).
- The kernel schedules each thread independently on available CPUs.
- Thread creation, destruction, and context switching all go through system calls.

### Advantages

- **True parallelism** — multiple KLTs of the same process can run simultaneously on multiple cores.
- **Blocking is isolated** — if one thread blocks on I/O, other threads in the same process continue executing.
- **Kernel can schedule efficiently** — time-slicing works at thread granularity.

### Disadvantages

- **Slower context switch** — every thread operation (create, switch, terminate) requires a system call → user-to-kernel mode transition.
- **Higher overhead** — each thread consumes kernel resources (memory for kernel-side TCB, etc.).
- **Limited scalability** — creating tens of thousands of kernel threads is expensive; the kernel has a cap.

### Mapping model

`One-to-One` — each user thread maps to one kernel thread.

---

## Quick Comparison Table

| Feature | User-Level Threads | Kernel-Level Threads |
|---|---|---|
| Managed by | Thread library (user space) | OS Kernel |
| Kernel awareness | No | Yes |
| Context switch cost | Low (no syscall) | High (syscall needed) |
| Blocking syscall effect | Blocks entire process | Blocks only that thread |
| Multi-core parallelism | No | Yes |
| Creation overhead | Very low | Higher |
| Mapping | Many-to-One | One-to-One |
| Example | GNU Pth, Green Threads | Linux pthreads, Windows threads |

---

## The Blocking Problem (ULT)

> [!warning] Key Exam Point
> In ULT, a **blocking system call** (like `read`, `write`, `sleep`) causes the **entire process to block**, not just the calling thread.
> This is because the kernel only sees the process — it has no idea threads exist inside it.

**Workaround:** Use **jacketing** — wrap blocking system calls with non-blocking versions. Before a potentially blocking call, check if it would block; if yes, switch to another thread first.

---

## Many-to-Many Model (Hybrid)

Some systems (e.g., older Solaris, Windows fibers) use a **Many-to-Many** model:
- Multiple user threads map to multiple (but possibly fewer) kernel threads.
- Gets the best of both: parallelism from KLTs, low-overhead scheduling from ULTs.
- Complex to implement; rarely used today since modern hardware makes 1:1 cheap enough.

---

## GATE Angle

> [!tip] What GATE asks
> - Which model supports true parallelism on multiprocessors? → **KLT**
> - In which model does a blocking call block the whole process? → **ULT**
> - Context switch is faster in? → **ULT**
> - Which uses Many-to-One mapping? → **ULT**
> - `pthread_create()` on Linux creates? → **KLT** (via `clone()` syscall)

---
