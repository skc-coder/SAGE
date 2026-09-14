# 2s complement binary to decimal
## Using weights
For bit patterns with many zeros.

**2's complement** is a weighted system. The MSB has weight $-2^{n-1}$

Example: $10_2$ in 2's complement:
$$= - 2^1 = -2$$

Why? $10110$ in 2's complement = $-(100000 - 10110)$ (minus because MSB is 1) $= -2^5 + (2^4 + 2^2 + 2^1) = -2^4 + (2^2 + 2^1)$. 

**1's complement**: MSB has weight $-(2^{n-1} - 1)$.

## Using complement

For numbers with many 1s (e.g., $01111111$), find the 2's complement first and compute from there. 

# 1s complement binary to decimal

Weight of MSB: = $-2^{n-1} + 1.$
Overall = 2s complement decimal (a negative number) + 1.
Adding 1, because sign of the result of the number will be negative, hence effectively subtracting.