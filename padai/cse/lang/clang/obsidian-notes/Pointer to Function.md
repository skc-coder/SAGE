- **Syntax**: `return_type (*ptr_name)(arg_types);`

```c
int my_fun(int x) { return x + 1; }

int main() {
    int (*p)(int);  // p is a pointer to a function taking int, returning int
    p = my_fun;

    printf("%d", p(2));  // Output: 3
    // No need to dereference: p(2) works same as (*p)(2)
}
```
