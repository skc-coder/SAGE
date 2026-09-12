
- **Generic pointer**: Can hold address of any data type.
- **Cannot dereference directly**: Must cast to specific type first.
- **Cannot perform arithmetic**: Size of `void` is unknown.

```c
void *p;
*p;          // ERROR: cannot dereference
p + 1;       // ERROR in standard C (GCC extension allows it, treating as char)
```
- `sizeof(void)` → **Undefined** (compilation error in standard C)
- `sizeof(void *)` → **8 bytes** (on 64-bit systems)
- GCC extension: `p + 1` on `void *` increments by **1 byte** (treats as `char *`)

https://stackoverflow.com/questions/1666224/what-is-the-size-of-void