## Row Sum Trick
If all **row sums** of $A$ are equal to $k$, then **$\lambda = k$** is an eigenvalue.
- More generally: $\sum R_{\min} \le \lambda \le \sum R_{\max}$ (bounds for eigenvalues).

### Example
$$A = \begin{bmatrix} -1 & 4 \\ 4 & -1 \end{bmatrix}$$
- Row sums: $R_1 = -1 + 4 = 3$, $R_2 = 4 - 1 = 3$.
- Since both are 3, $\lambda = 3$ is an eigenvalue.
- Using trace: $\lambda_1 + \lambda_2 = -1 + (-1) = -2$.
- If $\lambda_2 = 3$, then $\lambda_1 + 3 = -2 \implies \lambda_1 = -5$.


## Triangular/Diagonal Matrices
For **lower triangular**, **upper triangular**, or **diagonal** matrices, the **eigenvalues are the diagonal elements** themselves.

$$
A = \begin{bmatrix} a_{11} & * & * \\ 0 & a_{22} & * \\ 0 & 0 & a_{33} \end{bmatrix} \implies \lambda = a_{11}, a_{22}, a_{33}
$$

*   **Why?** The characteristic equation $\det(\lambda I - A) = 0$ becomes $(\lambda - a_{11})(\lambda - a_{22})(\lambda - a_{33}) = 0$.

## Complex Conjugate Pairs
For real matrices, complex eigenvalues always occur in **conjugate pairs**.

