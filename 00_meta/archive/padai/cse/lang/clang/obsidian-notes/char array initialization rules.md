## Character Arrays & Null Terminator
- Default value for uninitialized elements is `\0=NULL` (ASCII 0).
- String literals automatically include `\0`.

**Examples:**
```c
char t[5] = {'a', 'b', 'c', 'd'};   // {'a', 'b', 'c', 'd', '0=NULL=\0'}
char t[4] = {'a', 'b', 'c', 'd'};   // {'a', 'b', 'c', 'd'} (No \0)

char s[5] = "abcd";                  // {'a', 'b', 'c', 'd', '\0'}
char s[4] = "abcd";                  // {'a', 'b', 'c', 'd'} (No \0)
```

## Dimension Deduction
If dimension is omitted, compiler counts elements.

**Examples:**
```c
int myArray[] = {1, 2, 3, 4, 5, 6, 7, 8, 9}; // Size deduced as 9

char s[] = "abcd";                           // Size deduced as 5 (includes \0)
```
