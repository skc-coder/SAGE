Type conversion in C occurs in three contexts:
1. Arithmetic operations
2. Assignment operations
3. Printing (format specifiers)

* Arithmetic Conversions

** Basic Principle
Operands are promoted to a common type before arithmetic operations. The general rule: narrower types convert to wider types, signed converts to unsigned when widths match.

** Integer Promotions (Applied First)
- `char` and `short` (both signed and unsigned) → always promoted to `int` first
- If `int` can represent all values of the original type, convert to `int`
- Otherwise, convert to `unsigned int`
- Then further conversions applied as needed per usual arithmetic conversion rules

** Usual Arithmetic Conversions

After integer promotions, if operands still differ:

1. If either operand is `long double` → both become `long double`
2. Else if either is `double` → both become `double`
3. Else if either is `float` → both become `float`
4. Otherwise (both are integers after promotion):
   - If both signed or both unsigned → narrower converts to wider
   - If unsigned operand's rank ≥ signed operand's rank → signed converts to unsigned
   - If signed type can represent all values of unsigned type → unsigned converts to signed
   - Otherwise → both convert to unsigned version of signed type

** Common Examples

| Type 1           | Type 2           | Result Type           |
|------------------|------------------|-----------------------|
| `int`            | `float`          | both → `float`        |
| `short`          | `unsigned int`   | both → `unsigned int` |
| `int`            | `unsigned int`   | both → `unsigned int` |
| `unsigned int`   | `long`           | depends on sizes*     |
| `long`           | `unsigned long`  | both → `unsigned long`|

*On typical 32-bit systems where `int` and `long` are same size, `unsigned int` → `long` doesn't happen; both become `unsigned long`.

** Signed ↔ Unsigned Conversion Mathematics

*** Signed → Unsigned (modular arithmetic)
Let $n$ = number of bits in target type, $N = 2^n$

**** For non-negative values:
- Value remains unchanged: $result = value$
- Memory: sign bit becomes regular bit, rest unchanged

**** For negative values (two's complement):
- Mathematical formula: $result \equiv value \pmod N$
- Equivalently: $result = value + N$
- Since $-k + 2^n = 2^n - k$, this gives the expected result

**** Example (16-bit)
```c
// n = 16, N = 2^16 = 65536
short x = -1;
unsigned short y = x;
// y = -1 + 65536 = 65535 = 0xFFFF
```

*** Unsigned → Signed (reduction modulo 2^n to signed range)
Let $n$ = number of bits, $N = 2^n$, range = $[-2^{n-1}, 2^{n-1} - 1]$

**** For values in $[0, 2^{n-1} - 1]$:
- Value remains unchanged

**** For values in $[2^{n-1}, 2^n - 1]$:
- Mathematically: $result = value - 2^n$
- Memory: bits unchanged, reinterpreted with two's complement

**** Example (16-bit)
```c
// n = 16, N = 2^16 = 65536
unsigned short x = 65535;  // 0xFFFF
short y = x;
// y = 65535 - 65536 = -1
```

* Assignment Conversions

** General Rule
Right-hand side converts to left-hand side type.

** Wide → Narrow (left side has fewer bits)

*** Target is Unsigned
- Apply modular arithmetic: $result \equiv value \pmod{2^n}$
- High-order bits discarded, low-order bits retained
- Result always non-negative
- Mathematically: $result = value \ \& \ (2^n - 1)$

**** Example
```c
// 32-bit to 8-bit
unsigned int x = 0x12345678;
unsigned char y = x;  
// y = 0x78 = 120
// Mathematically: 0x12345678 mod 256 = 120
```

*** Target is Signed
- *Implementation-defined behavior* (not portable!)
- Typically: same bit-level operation as unsigned case
- Low n bits retained, interpreted as two's complement
- If bit (n-1) is 0: result is positive
- If bit (n-1) is 1: result is negative

**** Example
```c
// 32-bit to 8-bit
int x = 0x000000FF;  // 255
char y = x;
// y = -1 (if 0xFF interpreted as signed byte)
// Because: 0xFF as signed 8-bit = -1 in two's complement
```

** Narrow → Wide (left side has more bits)
- Simple extension, no data loss

*** Unsigned types
- Zero extension: high-order bits filled with 0
- $result = value$ (mathematically unchanged)

*** Signed types
- Sign extension: high-order bits filled with sign bit
- Preserves numerical value

**** Example
```c
// Sign extension
char x = -1;        // 0xFF (8 bits)
int y = x;          // 0xFFFFFFFF (32 bits)
// Numerical value -1 preserved

// Zero extension
unsigned char x = 255;  // 0xFF (8 bits)
unsigned int y = x;     // 0x000000FF (32 bits)
// Numerical value 255 preserved
```

* Printing Conversions

Format specifiers in `printf()` family determine type interpretation and conversion.

** Common Format Specifiers

| Specifier | Expects Type    | Conversion Applied              |
|-----------|-----------------|---------------------------------|
| `%d`      | `int`           | signed decimal                  |
| `%u`      | `unsigned int`  | unsigned decimal                |
| `%f`      | `double`        | `float` promoted to `double`    |
| `%lf`     | `double`        | double precision                |
| `%c`      | `int`           | converted to `unsigned char`    |
| `%x`      | `unsigned int`  | unsigned hexadecimal            |
| `%ld`     | `long`          | signed long decimal             |
| `%zu`     | `size_t`        | size_t (unsigned)               |

** Type Mismatch = Undefined Behavior

The format specifier *must* match the actual type (after default promotions). Mismatches cause undefined behavior.

```c
int x = -1;
printf("%u", x);  // UB! Prints 4294967295 on 32-bit systems
                  // (treats -1's bit pattern as unsigned)

unsigned int y = 4294967295u;
printf("%d", y);  // UB! Prints -1 on 32-bit systems
                  // (treats unsigned bit pattern as signed)
```

* Mathematical Details: Two's Complement

** Representation
For an $n$-bit signed integer $x$ with bits $b_{n-1}...b_1 b_0$:

$$
x = -b_{n-1} \cdot 2^{n-1} + \sum_{i=0}^{n-2} b_i \cdot 2^i
$$

** Range
- Signed $n$-bit: $[-2^{n-1}, 2^{n-1} - 1]$
- Unsigned $n$-bit: $[0, 2^n - 1]$

** Conversion Formulas

*** Signed → Unsigned (value $v$, $n$ bits)
$$
u = \begin{cases}
v & \text{if } v \geq 0 \\
v + 2^n & \text{if } v < 0
\end{cases}
$$

Or simply: $u \equiv v \pmod{2^n}$

*** Unsigned → Signed (value $u$, $n$ bits)
$$
s = \begin{cases}
u & \text{if } u < 2^{n-1} \\
u - 2^n & \text{if } u \geq 2^{n-1}
\end{cases}
$$

** Truncation ($n$ bits → $m$ bits, $m < n$)
Result = value mod $2^m$, keeping only lower $m$ bits:

$$
\text{result} = v \bmod 2^m = v \land (2^m - 1)
$$

* Key Takeaways

- Arithmetic: `char`/`short` promote to `int` first, then smaller types → larger, signed → unsigned when same size
- Assignment: RHS → LHS type; narrow targets truncate via mod $2^n$
- Signed ↔ Unsigned: modular arithmetic applies ($N = 2^n$)
- Printing: format specifier controls interpretation; mismatches = UB
- Implementation: assumes two's complement (C99+ standard in C23)