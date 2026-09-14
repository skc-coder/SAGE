```markdown
# getchar() and Input

## getchar()
- Reads **single character** from stdin.
- Returns the character as an `int` (to handle `EOF`).
- Simpler than `scanf("%c", &c)`.

```c
char c;
c = getchar();          // Read one char
// Equivalent to:
scanf("%c", &c);
```

