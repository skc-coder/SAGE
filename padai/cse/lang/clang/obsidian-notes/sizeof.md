it is an operator.
output in bytes.
calculated at compile time, based on the fixed type to size mappings.

```c
char c = 'a, *p = &c;

sizeof(c);   // 1 (size of char)
sizeof(c+1); // 4 (size of int)
sizeof(p) // 8
```

