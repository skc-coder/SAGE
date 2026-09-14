https://mathcircle.berkeley.edu/sites/default/files/BMC6/pdf0607/catalan.pdf

| n   | $C_n$ |
| --- | ----- |
| 0   | 1     |
| 1   | 1     |
| 2   | 2     |
| 3   | 5     |
| 4   | 14    |
| 5   | 42    |
| 6   | 132   |
| 7   | 429   |
| 8   | 1430  |
| 9   | 4862  |
| 10  | 16796 |

Formula: $C_n = \frac{1}{n+1}\binom{2n}{n}$

Recurrence: $C_0 = 1, \quad C_{n+1} = \sum_{i=0}^{n} C_i \cdot C_{n-i}$