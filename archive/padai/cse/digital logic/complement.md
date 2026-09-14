Every base $r$ has two complements:
- **Diminished Radix Complement** (r-1's complement)
- **Radix Complement** (r's complement)

**Formulas** (for $n$-digit number $N$):
$$\text{(r-1)'s complement} = r^n - 1 - N$$
$$\text{r's complement} = r^n - N$$

For decimal: 9's complement and 10's complement. For binary: 1's and 2's complement.

**Shortcut:** r-1's complement $+ 1$ = r's complement.

**Faster r's complement by inspection:** Starting from the rightmost digit, keep digits up to and including the first non-zero digit as-is; take the r-1's complement of all digits to the left.
