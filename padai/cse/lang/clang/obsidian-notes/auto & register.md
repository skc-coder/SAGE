## 1. Auto (Default for Local Variables)
- **Storage**: Stack (runtime)
- **Initial Value**: Garbage
- **Scope**: Within block
- **Lifetime**: End of block
- **Note**: Cannot be used for global variables. Not accessible outside the file.

## 2. Register
- **Storage**: CPU Register
- **Initial Value**: Garbage
- **Scope**: Within block
- **Lifetime**: End of block
- **Note**: Hint to compiler for frequent variables. Modern compilers optimize this automatically.