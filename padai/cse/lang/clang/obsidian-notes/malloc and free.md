## Memory Layout
- **Stack**: Automatic variables (local vars).
- **Static/Global**: Global variables, static variables.
- **Heap**: Dynamic allocation (`malloc`, `calloc`, `realloc`).

## `malloc()`
- **Syntax**: `void *malloc(size_t size);`
- Allocates **contiguous memory** in the **Heap**.
- Returns **void pointer** (no typecast needed in C).
- Returns **NULL** on failure.
- **Uninitialized** memory (garbage values).

```c
int *p = malloc(4);  // Allocates 4 bytes
if (p == NULL) {
    // Handle error
}
*p = 3;  // Store value
```

## `free()`
- **Syntax**: `void free(void *ptr);`
- **Reclaims** heap memory for reuse.
- **Does NOT** change the pointer value (pointer becomes **dangling**).
- **Does NOT** zero out memory (OS may reuse it later).

```c
free(p);  // Memory reclaimed
// p still holds old address (1000), but memory is invalid
// Accessing *p now is undefined behavior
```


