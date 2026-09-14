Three systems exist for signed binary numbers (n bits total, 1 sign bit + n-1 magnitude bits):

| System | $+0$ | $-0$ | Min | Max |
|---|---|---|---|---|
| Sign-Magnitude | $0\underbrace{00\ldots0}_{n-1}$ | $1\underbrace{00\ldots0}_{n-1}$ | $-(2^{n-1}-1)$ | $2^{n-1}-1$ |
| 1's Complement | $0\underbrace{00\ldots0}_{n-1}$ | $1\underbrace{11\ldots1}_{n-1}$ | $-(2^{n-1}-1)$ | $2^{n-1}-1$ |
| 2's Complement | $0\underbrace{00\ldots0}_{n-1}$ | *(none)* | $-2^{n-1}$ | $2^{n-1}-1$ |

![](attachments/Pasted%20image%2020260428072208.png)


**2's complement is preferred** because:
- Only one representation of zero
- Full $2^n$ codes utilized
- Arithmetic is simpler
