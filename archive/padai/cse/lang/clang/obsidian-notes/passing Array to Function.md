## Passing 2D Array to Function
- When `int a[5][6]` is passed to a function, it decays to a **pointer to an array of 6 ints**.
- Type: `int (*)[6]` (NOT `int **`).

```c
void fun(int a[][6]) { }        // Correct: decays to int (*)[6]
void fun(int (*a)[6]) { }       // Correct: explicit pointer to array
void fun(int **a) { }           // ERROR: incompatible types
```

## Key Rules
- **First dimension** can be omitted in function parameter: `int a[][6]`.
- **Second dimension** is **mandatory** for pointer arithmetic to work.
- `a[i][j]` ≡ `*(*(a + i) + j)`
```