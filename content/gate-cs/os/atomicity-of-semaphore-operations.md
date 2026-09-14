## 4. Atomicity of $P(S)$ and $V(S)$ Operations
Because $P(S)$ and $V(S)$ modify shared state variables (`S->value`, queue pointers), their execution must be **strictly atomic**.

- Operating systems ensure atomicity of the semaphore operations themselves using hardware instructions like **Test-and-Set (TSL)** or by disabling interrupts on single-core architectures.
- While this technically introduces a tiny amount of busy waiting inside $P()$ and $V()$, the critical region of $P()$ and $V()$ is minuscule (a few instructions).
- **Core architectural trade-off:** Semaphores move the long, unbounded busy waiting out of the application's critical section into a brief, fixed, minimal hardware-supported spinlock inside the OS kernel primitives.
