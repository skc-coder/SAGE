## The Core Idea: Two Modes of CPU Operation

Modern CPUs run in one of two modes at any given time:

| Mode            | Also called             | Who runs here               | What's allowed                                |
| --------------- | ----------------------- | --------------------------- | --------------------------------------------- |
| **User mode**   | Ring 3 (x86)            | User programs, applications | Limited instruction set only                  |
| **Kernel mode** | Ring 0, Supervisor mode | OS kernel                   | Everything, including privileged instructions |

The CPU has a **mode bit** (1 bit in a status register, e.g., PSW on x86). `1 = user`, `0 = kernel`. Hardware checks this bit before executing sensitive instructions.

---

## Privileged (Reserved) Instructions

Instructions that can **only execute in kernel mode**. If a user-mode program tries to run one, the CPU raises a trap (protection fault) and hands control to the OS.

**Examples:**
- `HLT` — halt the CPU
- `IN` / `OUT` — direct I/O port access
- `LIDT` / `LGDT` — load interrupt/descriptor tables
- Modifying the mode bit itself
- Disabling interrupts (`CLI` on x86)
- Direct memory-mapped I/O access

> [!important]
> Privileged instructions are a **hardware mechanism**. The CPU enforces them — not the OS. The OS just decides what to do after the CPU traps.

---

## System Call

A **system call** is how a user-mode program voluntarily requests a service from the kernel.

It is the **only legal way** for user code to enter kernel mode intentionally.

### How it works (step by step)

1. User program sets up arguments (in registers or stack).
2. User program executes a special instruction:
   - `INT 0x80` (older Linux x86)
   - `SYSCALL` (x86-64)
   - `SWI` / `SVC` (ARM)
3. This instruction causes a **trap** → CPU switches to kernel mode.
4. CPU jumps to the **system call handler** (address stored in a kernel table).
5. Kernel identifies which syscall was requested (via syscall number in a register).
6. Kernel executes the requested service (e.g., `read`, `write`, `fork`).
7. Kernel sets return value, restores user context, switches back to user mode.
8. Execution resumes at the next instruction after the syscall.

### Examples of system calls

| Category        | Examples                                 |
| --------------- | ---------------------------------------- |
| Process control | `fork()`, `exec()`, `exit()`, `wait()`   |
| File I/O        | `open()`, `read()`, `write()`, `close()` |
| Memory          | `mmap()`, `brk()`                        |
| Communication   | `pipe()`, `socket()`, `send()`           |
| Device          | `ioctl()`                                |

> [!note]
> `printf()` is **not** a system call — it is a C library function. Internally it calls `write()`, which IS a system call.

---

## Trap

A **trap** is a **synchronous, software-generated interrupt** caused by the currently executing instruction.

"Synchronous" means it happens as a direct result of the instruction that just ran — not from some external event.

### Two kinds of traps

**Intentional trap (software trap):**
- Generated deliberately by executing `INT n`, `SYSCALL`, `SWI`, etc.
- Used to implement system calls.
- Control transfers to a predefined kernel handler.

**Unintentional trap (exception / fault):**
- Generated because the instruction did something invalid.
- Examples: divide by zero, illegal memory access, privileged instruction in user mode.
- See "Exceptions" below.

> [!tip] GATE phrasing
> Many textbooks (including Silberschatz) use "trap" to mean specifically the **intentional** software-generated kind used for system calls. Others use it as a general term for any synchronous control transfer to the kernel. Know both usages.

---

## Exception

An **exception** is an **unintentional, synchronous event** caused by an error or unusual condition during instruction execution.

The CPU detects the problem, interrupts the current flow, and transfers control to an OS exception handler.

### Types of exceptions

| Type      | What it means                                       | Example                                | Resumable?       |
| --------- | --------------------------------------------------- | -------------------------------------- | ---------------- |
| **Fault** | Error that might be fixable; instruction is retried | Page fault, divide by zero (sometimes) | Yes (if handled) |
| **Trap**  | Intentional exception after instruction completes   | Breakpoint (`INT 3`), syscall          | Yes              |
| **Abort** | Severe, unrecoverable error                         | Hardware failure, double fault         | No               |

### Common exceptions

- **Divide by zero** — arithmetic error
- **Page fault** — memory access to a page not currently in RAM (most page faults are handled transparently — OS loads the page and retries)
- **Segmentation fault** — access to an invalid/protected memory region; OS usually kills the process
- **Invalid opcode** — CPU encounters an unrecognized instruction
- **Protection fault** — user mode program tries to execute a privileged instruction
- **Stack overflow** — stack grows beyond its allocated region (a kind of page fault or segfault)

---

## Interrupt

An **interrupt** is an **asynchronous event** — it comes from **outside** the currently executing instruction, typically from hardware.

The CPU finishes the current instruction (usually), then checks for pending interrupts, then transfers to an interrupt handler.

### Hardware interrupt sources

- Timer (clock chip) — used for preemptive scheduling
- Keyboard / mouse input
- Disk I/O completion
- Network packet arrival
- USB events

### How it works

1. Device signals the CPU via an **interrupt request line (IRQ)**.
2. CPU completes current instruction.
3. CPU saves current state (PC, registers, PSW).
4. CPU looks up the handler address in the **Interrupt Descriptor Table (IDT)**.
5. CPU switches to kernel mode and jumps to the handler.
6. Handler services the interrupt (e.g., reads data from disk buffer).
7. CPU restores saved state and resumes user program.

---

## Full Comparison Table

|                  | System Call             | Trap (intentional)                     | Exception                         | Interrupt                 |
| ---------------- | ----------------------- | -------------------------------------- | --------------------------------- | ------------------------- |
| **Triggered by** | User program explicitly | Special instruction (`SYSCALL`, `INT`) | CPU detecting an error            | External hardware         |
| **Synchronous?** | Yes                     | Yes                                    | Yes                               | No (asynchronous)         |
| **Intentional?** | Yes                     | Yes                                    | No                                | No                        |
| **Mode switch?** | User → Kernel           | User → Kernel                          | User → Kernel (usually)           | Any → Kernel              |
| **Example**      | `read()` syscall        | `INT 0x80`                             | Page fault, divide by zero        | Timer tick, disk I/O done |
| **Resumable?**   | Yes                     | Yes                                    | Depends (fault = yes, abort = no) | Yes                       |
|                  |                         |                                        |                                   |                           |

---

## Mode Switch vs Context Switch

These are different — often confused.

**Mode switch:** CPU changes from user mode to kernel mode (or back). The same process keeps running, just in a different privilege level. Fast.

**Context switch:** The OS switches from one process to another — saves the full state of process A, loads state of process B. Slower. A context switch always involves a mode switch, but a mode switch does not always cause a context switch.

---

## The Dual-Mode Protection Chain (Summary)

```

User Program | | wants OS service v System Call instruction (SYSCALL / INT 0x80) | | causes a trap → CPU sets mode bit to kernel v Kernel System Call Handler | | performs the service v Returns to user mode (mode bit reset to user) | v User Program resumes

```

Privileged instructions sit outside this chain — they don't ask permission, they just get blocked by hardware if attempted in user mode, which itself raises an exception (protection fault).

---

## GATE Angle

> [!tip] Common GATE questions
> - Which of these is NOT a system call? → Library functions like `printf`, `malloc` are not.
> - A page fault is a ___ → Exception (specifically a fault, which is retried after handling).
> - Timer interrupt is ___ → Asynchronous hardware interrupt.
> - `fork()` uses which mechanism to enter kernel mode? → Trap (system call).
> - Privileged instruction executed in user mode causes? → Protection fault / trap.
> - Mode switch is faster/slower than context switch? → Faster.
> - Which events are synchronous? → System calls, traps, exceptions. Interrupts are async.

---

## Related Notes

- [[User-Level vs Kernel-Level Threads]]
- [[Process Scheduling]]
- [[Memory Management - Paging]]
- [[Deadlock]]
```

The one distinction that trips people up the most: a **trap** is the mechanism (the hardware event that causes mode switch), while a **system call** is the higher-level concept (the user program requesting OS service). A system call is implemented _using_ a trap, but not every trap is a system call. Page faults are also traps, and they have nothing to do with the user requesting anything.