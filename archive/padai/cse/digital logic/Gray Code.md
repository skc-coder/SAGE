## Gray Code
- Binary code where consecutive values differ by only one bit.
- Used in digital systems for error detection and minimizing switching errors.

### Construction
- **Recursive method**:
  - Start with 1-bit: 0, 1
  - For n-bit: 
    - First half: (n-1) bit Gray code with leading 0
    - Second half: (n-1) bit Gray code in reverse with leading 1
- **Formula**: $G(n) = n \oplus \left\lfloor \frac{n}{2} \right\rfloor$
### Binary to Gray Code
For a 4-bit number with binary bits $b_3b_2b_1b_0$:
- $g_3 = b_3$
- $g_2 = b_3 \oplus b_2$
- $g_1 = b_2 \oplus b_1$
- $g_0 = b_1 \oplus b_0$

### Gray to Binary Conversion
For a 4-bit Gray code $g_3g_2g_1g_0$:
- $b_3 = g_3$
- $b_2 = g_3 \oplus g_2$
- $b_1 = g_3 \oplus g_2 \oplus g_1$
- $b_0 = g_3 \oplus g_2 \oplus g_1 \oplus g_0$

### General Formula
- $G(n) = n \oplus \left\lfloor \frac{n}{2} \right\rfloor$
- Where $\oplus$ is bitwise XOR
### Applications
- Digital encoders
- Karnaugh maps
- Minimizing switching errors in circuits
