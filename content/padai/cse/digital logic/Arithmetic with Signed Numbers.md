### Sign-Magnitude
- **Same signs:** Add magnitudes, keep the sign.
- **Different signs:** Subtract smaller magnitude from larger, take sign of the larger.

### 1's and 2's Complement
All operations ($+M+N$, $+M-N$, $-M+N$, $-M-N$) reduce to **just adding** the representations.

| System | End carry handling |
|---|---|
| 2's complement | **Discard** end carry |
| 1's complement | **Add the carry back** (end-around carry) |

Example: $3 - 2$ in 2's complement = (repr. of $+3$) + (repr. of $-2$), then discard carry if any.
$3 - (-2) = 3 + 2$ = (repr. of $+3$) + (repr. of $+2$).

## Links
[[Binary Codes]] | [[Binary Code Patterns]]