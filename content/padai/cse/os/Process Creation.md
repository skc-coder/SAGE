## 4. Process Control Block (PCB)

Every process has a PCB maintained by the OS. Contains everything needed to resume the process later.

| Field                  | Contents                                          |
| ---------------------- | ------------------------------------------------- |
| Process state          | Current state (ready, running, waiting, etc.)     |
| PID                    | Unique process identifier                         |
| Program counter        | Address of next instruction to execute            |
| CPU registers          | All register values (saved on context switch)     |
| CPU scheduling info    | Priority, scheduling queue pointers               |
| Memory management info | Page tables, segment tables, base/limit registers |
| I/O status             | List of open files, I/O devices allocated         |
| Accounting info        | CPU time used, time limits, job ID                |

---

## 5. Context Switch

When the CPU switches from one process to another, the OS must:

1. Save the state of the **current process** into its PCB (registers, PC, stack pointer).
2. Load the state of the **next process** from its PCB.
3. Transfer control to the new process.

**Context switch time is pure overhead** — the system does no useful work during it. Modern CPUs minimize this with hardware support (e.g., TSS on x86).

Context switch cost depends on: number of registers, memory that must be flushed (TLB, caches), OS complexity.

---
