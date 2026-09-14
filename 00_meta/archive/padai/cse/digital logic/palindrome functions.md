### Palindrome Functions

Functions where $f' = f^d$ (complement equals dual).

**Property:** $f(a, b, c) = f(\bar{a}, \bar{b}, \bar{c})$

**Procedure to verify:**
- Compute $f'$ by inverting output of $f$
- Reverse the output of $f'$ to get $f^d$
- If $f' = f^d$, then $f$ is palindromic

### Counting Palindrome Functions

**Observation:** In the truth table, the lower half is fixed; upper half is independent.

**Total palindrome functions for $n$ variables:** $2^{2^{n-1}}$

**Intuition:** Only $2^{n-1}$ rows are free to choose (upper half), each can be 0 or 1.

---
**Source:** [YouTube](https://www.youtube.com/watch?v=fV6YWEJhP-M)