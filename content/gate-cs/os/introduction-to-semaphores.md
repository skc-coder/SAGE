## 1. Introduction to Semaphores
Semaphores were introduced by **Edsger W. Dijkstra** in 1965 as a robust synchronization tool to solve critical section problems without relying on complex, error-prone software flags or pure spinlocks.

> [!definition] Semaphore
> A **Semaphore** is an integer variable that, apart from initialization, is accessed strictly through two standard, indivisible (atomic) operations:
> - **$P(S)$** / **Down$(S)$** / **Wait$(S)$**: Decrements the semaphore value.
> - **$V(S)$** / **Up$(S)$** / **Signal$(S)$**: Increments the semaphore value.
> 
> *Etymology:* $P$ originates from the Dutch word *proberen* ("to test"), and $V$ comes from *verhogen* ("to increment").
> 
> A fundamental architectural constraint: **There is no direct way to inspect or read the internal numerical value of a semaphore variable directly in user space.**
