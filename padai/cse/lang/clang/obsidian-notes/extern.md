`extern int max;` tells the compiler:
- A global variable `max` exists **somewhere** (locally or externally).
- **No memory allocation** happens here.
- The **linker** resolves the actual address later.

## Usage

```c
#include <stdio.h>
int main() {
    extern int max;  // Declaration only
    printf("%d", max);
}
int max;  // Definition (allocates memory, initializes to 0)
```

---

Unused Extern Declarations:

If an `extern` variable or function is **declared but never used**, the compiler and linker **ignore it**.
- **No compile error**
- **No linker error**

Examples:

```c
#include <stdio.h>
extern int i;  // Declared, never used

int main() {
    int i = 5;  // Local 'i' shadows the extern 'i'
    printf("%d", i);
    return 0;
}
```

```c
#include <stdio.h>
void fun(void);  // Declared, never called

int main() {
    printf("Hello");
    return 0;
}
```

---
## Error
```c
#include <stdio.h>
int main() {
    extern int max = 5;
    printf("%d", max);
}
```

`extern int max = 5;` is made of two statements.
```c
extern int max;
int max = 5; 
```

So there is two variables of same name in same local scope. Hence compiler error.


But this is fine.
```c
#include <stdio.h>

extern int max = 5;

int main() {
    printf("%d", max);
}
```


This is analogous to the fact that we can declare an (extern) [functions](functions.md#^78147e) but cant define  it inside another.
But we can do declaration and definition both globally.
