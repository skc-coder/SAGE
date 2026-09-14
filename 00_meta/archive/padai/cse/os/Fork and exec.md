## The Big Picture

Unix uses a two-step model for creating new processes:

1. **`fork()`** — duplicate the current process
2. **`exec()`** — replace the duplicate with a new program

These two together let the shell (and any program) spawn child processes running completely different programs. Neither alone is sufficient for the general case.

---

## `fork()`

### What it does

`fork()` creates an **exact copy** of the calling process. The new process is called the **child**; the original is the **parent**.

After `fork()` returns, two processes exist, both about to execute the instruction immediately after the `fork()` call.

### What gets copied

| Resource         | Copied?                    | Notes                                                 |
| ---------------- | -------------------------- | ----------------------------------------------------- |
| Code segment     | Shared (read-only)         | Both parent and child point to same physical pages    |
| Data segment     | Copy-on-Write              | Separate copies made only when one side writes        |
| Heap             | Copy-on-Write              | Same                                                  |
| Stack            | Copy-on-Write              | Same                                                  |
| File descriptors | Copied (shared underlying) | Both processes share the same open file table entries |
| PID              | Not copied                 | Child gets a new unique PID                           |
| PPID             | New                        | Child's PPID = parent's PID                           |
| Pending signals  | Not inherited              | Child starts with empty pending signal set            |

### Copy-on-Write (COW)

`fork()` does not immediately copy all memory pages. Instead:

- Parent and child initially share the same physical pages (mapped read-only for both).
- When either process tries to **write** to a shared page, the OS makes a private copy of that page for the writer.
- This makes `fork()` very fast — especially when followed immediately by `exec()` (which throws away the copied memory anyway).

### Return value

This is the key thing to remember:

```c
pid_t pid = fork();

if (pid < 0) {
    // fork failed — no child was created
} else if (pid == 0) {
    // we are in the CHILD process
    // pid == 0 is how the child knows it's the child
} else {
    // we are in the PARENT process
    // pid = the child's PID
}
````

`fork()` returns **twice** — once in the parent (returns child's PID) and once in the child (returns 0). Same call, two returns, two processes.

### What happens to the PC?

Both processes start executing from the instruction **right after** `fork()`. The only difference is the return value they see.

---

## `exec()`

### What it does

`exec()` **replaces** the current process's memory image with a new program. It does not create a new process — it transforms the calling process into a different program.

After a successful `exec()`:

- The process keeps its PID.
- The old code, data, heap, and stack are completely replaced.
- The new program starts executing from its own `main()`.
- Open file descriptors are usually preserved (unless marked `FD_CLOEXEC`).

### The exec family

`exec()` is actually a family of functions — all ultimately call the `execve()` system call:

|Function|How program is found|Args passed as|Environment|
|---|---|---|---|
|`execl()`|Full path|List|Inherited|
|`execv()`|Full path|Array|Inherited|
|`execlp()`|PATH search|List|Inherited|
|`execvp()`|PATH search|Array|Inherited|
|`execle()`|Full path|List|Explicit|
|`execve()`|Full path|Array|Explicit|

Only `execve()` is an actual system call. The others are C library wrappers around it.

### What exec does NOT do

- Does not create a new process.
- Does not return on success — if `exec()` returns, it failed.
- Does not change the PID.
- Does not close file descriptors (unless `FD_CLOEXEC` is set on them).

```c
execvp("ls", args);
// if we reach this line, exec failed
perror("exec failed");
exit(1);
```

---

## fork + exec Together: How the Shell Works

This pattern is how every shell spawns commands:

```c
pid_t pid = fork();

if (pid == 0) {
    // child process
    execvp("ls", args);   // replace child with "ls"
    exit(1);              // only reached if exec fails
} else {
    // parent (shell) waits for child to finish
    wait(NULL);
}
```

Step by step:

1. Shell calls `fork()` → child created (copy of shell).
2. Child calls `exec("ls")` → child's memory replaced with `ls` program.
3. `ls` runs, prints output, exits.
4. Parent (shell) was waiting via `wait()` → gets notified child exited.
5. Shell resumes, prints prompt.

The parent-child separation is what makes this safe — the child can do whatever it wants (redirect file descriptors, set environment variables, drop privileges) before calling exec, without affecting the parent shell at all.

---

## `wait()` and `waitpid()`

After `fork()`, the parent usually needs to know when the child finishes.

```c
pid_t wait(int *status);
pid_t waitpid(pid_t pid, int *status, int options);
```

- `wait()` blocks until **any** child terminates.
- `waitpid()` waits for a **specific** child (by PID), and can be made non-blocking with `WNOHANG`.

### Zombie process

When a child exits but the parent hasn't called `wait()` yet, the child becomes a **zombie**. It holds no resources, but its exit status is kept in the process table until the parent collects it. If the parent never calls `wait()`, zombies accumulate.

### Orphan process

If the parent exits before the child, the child becomes an **orphan**. The OS re-parents it to `init` (PID 1), which periodically calls `wait()` to clean up.

---

## What fork() Copies vs What exec() Replaces

```
Before fork():
  Parent Process
  [code | data | heap | stack]
  PID = 100

After fork():
  Parent Process          Child Process
  [code | data |          [code | data |
   heap | stack]           heap | stack]  <- copy (COW)
  PID = 100               PID = 101

After child calls exec("ls"):
  Parent Process          Child Process
  [code | data |          [ls code | ls data |
   heap | stack]           ls heap | ls stack]  <- totally replaced
  PID = 100               PID = 101  <- PID unchanged
```

---

## Important Edge Cases

### File descriptors after fork

Both parent and child share the **same underlying open file descriptions** (not just copies). If the child writes to a file, the file offset advances for both. This is intentional — it's how shell pipelines work.

### fork() in multithreaded programs

Only the thread that called `fork()` is copied into the child. Other threads do not exist in the child. This can cause deadlocks if another thread held a mutex at the time of fork — the mutex is locked in the child with no thread to unlock it. In practice: call `exec()` immediately after `fork()` in multithreaded programs.

### vfork()

An older, now mostly obsolete variant. `vfork()` does not copy the address space at all — the child runs in the parent's memory and the parent is suspended until the child calls `exec()` or `exit()`. Dangerous (child can corrupt parent's memory). Avoid it.

---

## GATE Angle

> [!tip] Common GATE questions
> 
> - `fork()` returns what value to the parent? → Child's PID (positive integer).
> - `fork()` returns what to the child? → 0.
> - `fork()` returns negative? → Fork failed, no child created.
> - How many times does `fork()` return? → Twice (once per process).
> - After `exec()`, does the PID change? → No.
> - After `exec()`, does execution return to the line after exec? → Only if exec fails.
> - What is a zombie process? → Child exited, parent hasn't called `wait()` yet.
> - What is an orphan process? → Parent exited before child; init adopts the child.
> - COW in fork means? → Memory pages are shared until one side writes, then copied.

### Classic trick question

```c
int main() {
    fork();
    fork();
    fork();
    printf("hello\n");
    return 0;
}
```

How many times is "hello" printed?

Each `fork()` doubles the number of processes. After 3 forks: $2^3 = 8$ processes. **Answer: 8.**

General rule: `n` fork() calls with no branching → $2^n$ processes.

---

## Related Notes

- [[System Calls, Traps, Exceptions]]
- [[Process vs Thread]]
- [[Process Scheduling]]
- [[Inter-Process Communication]]

```

The classic trick question at the end is basically guaranteed to show up somewhere — the $2^n$ rule works only when there's no `if (pid == 0)` branching. The moment you add branching, you have to trace it manually.
```