- The (link able) global variable is not of `static` storage class, tough it is stored in static area.
	- It is available for linking, but `static` storage class variables are not.
- This global type has these properties:
- **Storage**: Static Memory
- **Initial Value**: Zero
- **Scope**: Global
- **Lifetime**: End of program
- **Linker**: Available to the linker (can span multiple files).

```c
int a != extern int a != static int a
```