## Pointer Subtraction
- **Requirement**: Both pointers must point to elements of the **same array**.
- **Result**: Difference in **number of elements** between the two positions.
- **Violation**: Undefined behavior (garbage value or error).

```
char s[] = "abcdef";
char *p = s;
char *q = s + 5;

printf("%d\n", q - p);  // Output: 5
printf("%d\n", p - q);  // Output: -5
```

## Type Casting and Pointer Arithmetic

- Arithmetic depends on **pointer type**, not the underlying data.
- `sizeof(type=*ptr)` determines increment/decrement size.


```C
char str[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
char a = str;             
char c = *((char*)((int *)str + 2));  // 'I' 
char d = (str + 2)[3];        // 'F' (str + 2)[3] = *(str+2+3).
```

## Pointer Type Casting Example

```c
char *str = (char*)1000;
long *u_ptr = (long*)str;      // 1000
int *i_ptr = (int*)(u_ptr + 1); // 1000 + sizeof(long) = 1008 (assuming 64-bit)
char *c_ptr = (char*)(i_ptr + 2); // 1008 + 2*sizeof(int) = 1016
```

- `u_ptr + 1` → adds `sizeof(long)` (8 bytes on 64-bit)
- `i_ptr + 2` → adds `2 * sizeof(int)` (8 bytes)
- `c_ptr` → adds `1 * sizeof(char)` (1 byte) per increment
