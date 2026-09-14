**Using r's complement** to compute $M - N$:
$$M - N = M + (r^n - N) - r^n = M + \text{r's complement of } N - r^n$$

- If $M \geq N$: end carry occurs (the $-r^n$ cancels the overflow). **Discard it** → answer is positive.
- If $M < N$: no carry. **Take r's complement of result and add a minus sign** → answer is negative.

**Using r-1's complement** to compute $M - N$:
$$M - N = M + \text{(r-1)'s complement of } N - r^n + 1$$

- If $M \geq N$: end carry occurs. **First discard the carry (remove overflow), then add 1** (end-around carry). i.e. subtract $r^n$ first, then add the $+1$.
- If $M < N$: no carry. **Take r-1's complement of result and add minus sign** i.e. add $-r^n + 1$.