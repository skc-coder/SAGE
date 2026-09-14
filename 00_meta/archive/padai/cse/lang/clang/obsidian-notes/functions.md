Default return type is int.
Need declaration (or definition) before use.

Acceptable forms of declarations:
```c
int mul(int a, int b);
int mul(int, int);
mul(int a, int b);
mul(int, int);
```

## Extern and static functions!

^78147e

## By default, functions are extern.

We can have fun with this.

```c
int main()
{
int fun();
fun(); // FINE
return 0;
}

int g()
{
fun(); // NOT FINE. NOT DECLARED.
}
  
int fun()
{
printf("Yo! inside fun!");
return 1;
}
```

## Static functions
```c
// Example 1: Static Function (File Scope)
static void fun(void) {
    printf("Hello");
}

int main() {
    fun();
    return 0;
}
// Result: Other files CANNOT use this function.
// The function is hidden from the linker.

// Example 2: External Function (Default)
void fun(void) {
    printf("Hello");
}

int main() {
    fun();
    return 0;
}
// Result: Other files CAN use this function.
// Default linkage is 'extern'.
```