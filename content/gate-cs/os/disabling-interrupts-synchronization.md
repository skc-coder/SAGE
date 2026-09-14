A straightforward approach to prevent instruction interleaving inside a critical section on single-processor systems is to disable interrupts upon entry and re-enable them upon exit.

> [!definition] Mechanics
> When interrupts are disabled, the CPU cannot be preempted by the timer interrupt or external hardware devices. Context switching is temporarily halted, guaranteeing that no instruction interleaving occurs while a process executes its critical section ($\text{CS}$).

```c
// Process Entry
disable_interrupts();

// Critical Section (CS)
// ...

// Process Exit
enable_interrupts();
```

## Limitations & Risks

> [!trap] Limitations of Disabling Interrupts
> 1. **Multiprocessor Inefficiency:** Disabling interrupts on one core does not prevent concurrent execution on another core. Disabling interrupts across all cores requires high-overhead inter-processor signals (IPIs), which degrades system performance.
> 2. **Security & System Trust:** Giving user-level processes the privilege to disable interrupts is fundamentally unsafe. A buggy or malicious process could freeze the entire operating system by entering an infinite loop while interrupts are disabled.
> 3. **Applicability:** Disabling interrupts is feasible and practical only as an internal OS kernel synchronization primitive on uniprocessor architectures.
