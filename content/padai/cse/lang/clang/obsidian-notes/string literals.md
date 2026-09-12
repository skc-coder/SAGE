- `char c[] = "Hello";` → array of strings (with `0` at end)
- `char *t = "Hello";` → **Pointer** to string in **static/RO** memory.

```c
#include <stdio.h>

int main() {
    char c[] = "yo!";
    char *t = "hello!";

    c[1] = 'f';   // ✅ OK. 'c' is a modifiable array.
    t[2] = 'd';   // ❌ Segmentation Fault. 't' points to read-only memory.
}
```


