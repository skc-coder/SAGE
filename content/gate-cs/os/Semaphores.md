# Semaphores & Synchronization

Counting semaphores maintain an integer value and a process list.
Here is 3 pages of derivation and explanation that you will NEVER need in revision...
...lots of rough work...

> [!formula]
> Current blocked processes: $m = |S|$ when $S < 0$. Initial value $k$, successful wait operations $n_W$, signal operations $n_S \implies S = k + n_S - n_W$. ^formula-state

Here is another page of code examples...
...more explanation...

> [!trap]
> Swapping `wait(mutex)` and `wait(empty)` in Producer-Consumer leads directly to deadlock, not just starvation. ^trap-pc-deadlock