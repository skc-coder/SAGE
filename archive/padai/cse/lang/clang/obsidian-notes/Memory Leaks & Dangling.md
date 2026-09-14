## Memory Leak
- **Cause**: Losing the pointer to allocated memory.
- **Result**: Memory wasted until program terminates.

## Dangling Pointer
- **Definition**: Pointer pointing to **freed memory**.
- **Cause**: Accessing memory after `free()`.
- **Risk**: Undefined behavior (crash, garbage values).

```c
int *p = malloc(8);
free(p);  // Memory reclaimed
*p = 5;   // DANGEROUS: Accessing freed memory
```

