Arrays decay to pointers in most expressions (e.g., function arguments).

**Difference**: `sizeof` behaves differently.
- `sizeof(arr)` → Size of the **entire array** (e.g., 20 bytes for `int arr`).
- `sizeof(ptr)` → Size of the **pointer** (e.g., 8 bytes on 64-bit).

**Example:**
```c
int arr = {1, 2, 3, 4, 5};
int *ptr = arr;

sizeof(arr);  // 20 (5 * 4 bytes)
sizeof(ptr);  // 8 (size of address)