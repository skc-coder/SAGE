![](attachments/statedig.png)
### States

| State                 | Description                                                                                                       |
| --------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **New**               | Process is being created. PCB allocated, not yet admitted to ready queue.                                         |
| **Ready**             | Process is in memory, waiting for CPU. Everything is ready — just needs the processor.                            |
| **Running**           | Process is currently executing on a CPU. Only one process per CPU core at a time.                                 |
| **Waiting** (Blocked) | Process is waiting for some event — I/O completion, semaphore, child exit, etc. Cannot use CPU even if it's free. |
| **Terminated**        | Process has finished execution. PCB still exists until parent calls `wait()`.                                     |

### Transitions

| Transition           | Trigger                                                                          |
| -------------------- | -------------------------------------------------------------------------------- |
| New → Ready          | OS admits the process (long-term scheduler)                                      |
| Ready → Running      | Short-term scheduler dispatches it                                               |
| Running → Ready      | Preempted by timer interrupt (time quantum expired)                              |
| Running → Waiting    | Process requests I/O or waits on event (`wait()`, `sleep()`, semaphore `wait()`) |
| Waiting → Ready      | I/O completes, event occurs, semaphore signalled                                 |
| Running → Terminated | Process calls `exit()` or is killed                                              |

> [!important]
> A process **never** goes directly from Waiting → Running. It always goes Waiting → Ready → Running. The CPU scheduler picks from the ready queue only.

---

## 3. Seven-State Model (With Suspend)

Real systems add **suspended** states to handle memory pressure. When RAM is full, the OS **swaps out** a process to disk.


### Additional States

| State                 | Description                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ready-Suspended**   | Process is ready to run but has been swapped out to disk. Will move to Ready when swapped back in.                                          |
| **Waiting-Suspended** | Process is waiting for I/O AND has been swapped to disk. When I/O completes, moves to Ready-Suspended (not directly Ready — still on disk). |

### Why suspend?

- Memory is full, a new high-priority process needs memory.
- Process has been idle (blocked) for a long time.
- User explicitly pauses a process (`Ctrl+Z` in shell → `SIGSTOP`).

---


## 6. Types of Schedulers

The OS has multiple schedulers operating at different timescales.

### 6.1 Long-Term Scheduler (Job Scheduler)

- **What:** Decides which processes are admitted from the job pool into memory (New → Ready).
- **How often:** Infrequently — seconds to minutes.
- **Controls:** Degree of multiprogramming (how many processes are in memory at once).
- **Goal:** Maintain a good mix of CPU-bound and I/O-bound processes to keep both CPU and I/O devices busy.
- **Present in:** Batch systems. Many modern interactive OSes (Linux, Windows) have no long-term scheduler — processes are admitted immediately.

### 6.2 Short-Term Scheduler (CPU Scheduler)

- **What:** Decides which ready process gets the CPU next (Ready → Running).
- **How often:** Very frequently — milliseconds. Must be fast.
- **Controls:** CPU utilization and responsiveness.
- **Goal:** Maximize CPU utilization, minimize response time, meet scheduling criteria.
- **Present in:** Every OS, always.

### 6.3 Medium-Term Scheduler (Swapper)

- **What:** Decides which processes to swap out to disk and swap back in (handles suspended states).
- **How often:** Occasionally, based on memory pressure.
- **Controls:** Degree of multiprogramming dynamically.
- **Goal:** Free up memory when needed; bring back processes when memory is available.
- **Present in:** Systems with virtual memory and swapping.

### Comparison Table

| | Long-Term | Short-Term | Medium-Term |
|---|---|---|---|
| Also called | Job scheduler | CPU scheduler | Swapper |
| Frequency | Low (minutes) | High (ms) | Medium |
| Queue managed | Job pool → Ready | Ready → Running | Memory ↔ Disk |
| Controls | Degree of multiprogramming | CPU allocation | Memory pressure |
| Speed required | Slow OK | Must be very fast | Moderate |

---



## 9. Dispatcher

The **dispatcher** is the module that actually gives control of the CPU to the process selected by the short-term scheduler.

Dispatcher tasks:
- Context switching.
- Switching to user mode.
- Jumping to the correct location in the user program (restoring PC).

**Dispatch latency** = time it takes to stop one process and start another. Should be minimal.

> [!note] Scheduler vs Dispatcher
> The **scheduler** decides *which* process runs next (policy).
> The **dispatcher** actually *does* the switch (mechanism).
> They are separate components.

---

