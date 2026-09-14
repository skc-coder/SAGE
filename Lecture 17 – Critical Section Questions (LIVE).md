
## 1. Software-Based Attempts

### Attempt 1: Single Lock / Interested Variable

C

```
// Shared variable
int interested = 0; // 0 = free, 1 = occupied

// Process P1                    // Process P2
while (interested);              while (interested);
interested = 1;                  interested = 1;
// Critical Section              // Critical Section
interested = 0;                  interested = 0;
```

- **ME (Failed)**: If $P_1$ executes `while (interested)` and is preempted before executing `interested = 1`, $P_2$ executes the check, sees `interested == 0`, and proceeds. Both processes enter the CS.
    
      
    
- **Progress (Satisfied)**: If the CS is idle, any incoming process can enter. No deadlock occurs.
    
      
    
- **BW (Failed)**: A fast process exiting the CS can immediately re-acquire the lock before a preempted waiting process proceeds.
    
      
    
- **Verdict**: **ME: ✗ | Progress: ✓ | BW: ✗**
    
      
    

### Attempt 2: Strict Alternation (Turn Variable)


```c
// Shared variable
int turn = 0; // 0 for P0, 1 for P1

// Process P0                    // Process P1
while (turn != 0);               while (turn != 1);
// Critical Section              // Critical Section
turn = 1;                        turn = 0;
```

- **ME (Satisfied)**: Since `turn` holds only one value at a time, concurrent entry is impossible.
    
      
    
- **Progress (Failed)**: Enforces strict order ($P_0 \to P_1 \to P_0 \dots$). If `turn == 0` and $P_0$ does not want to enter, $P_1$ is blocked indefinitely from entering the CS by an uninterested process.
    
      
    
- **BW (Satisfied)**: Neither process can enter twice consecutively; each process waits at most one turn.
    
      
    
- **Verdict**: **ME: ✓ | Progress: ✗ | BW: ✓**
    
      
    

### Attempt 3: Per-Process Intent Flags


```c
// Shared variable
int want[2] = {0, 0}; // false, false

// Process P0                    // Process P1
want[0] = 1;                     want[1] = 1;
while (want[1] == 1);            while (want[0] == 1);
// Critical Section              // Critical Section
want[0] = 0;                     want[1] = 0;
```

- **ME (Satisfied)**: A process cannot enter unless the other's flag is `0`.
- **Progress (Failed)**: If $P_0$ sets `want[0] = 1` and is preempted before the loop, and $P_1$ sets `want[1] = 1`, both enter `while` loops waiting for the other's flag to clear, causing **deadlock**.
    
      
    
- **BW (Satisfied)**: In non-deadlocking interleaved execution, alternating flag checks prevent starvation.
    
      
    
- **Verdict**: **ME: ✓ | Progress: ✗ | BW: ✓**
    
      
    

## 3. Comparative Summary

| **Solution Attempt**  | **Mutual Exclusion** | **Progress** | **Bounded Waiting** | **Failure Cause**                                   |
| --------------------- | -------------------- | ------------ | ------------------- | --------------------------------------------------- |
| **Attempt 1 (Lock)**  | ✗                    | ✓            | ✗                   | Preemption between test and set                     |
| **Attempt 2 (Turn)**  | ✓                    | ✗            | ✓                   | Strict alternation (uninterested process blocks CS) |
| **Attempt 3 (Flags)** | ✓                    | ✗            | ✓                   | Mutual deadlock when flags set concurrently         |

