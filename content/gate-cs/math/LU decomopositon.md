https://www.youtube.com/watch?v=yVnSzpW0Stk
https://www.youtube.com/watch?v=ZUYNSAsY6bE
## Definition
An **LU decomposition** (or factorization) of a square matrix $A$ is a factorization $A = LU$, where:
- $L$ is a **lower triangular** matrix
- $U$ is an **upper triangular** matrix

## Need
LU decompositions can be used in [solving linear equations](solving%20linear%20equations.md) $Ax = b.$
1. Rewrite as $L(Ux) = b$.
2. Let $y = Ux$, solve $Ly = b$ using **forward substitution** (easy since $L$ is lower triangular).
3. Solve $Ux = y$ using **back substitution** (easy since $U$ is upper triangular).

**Benefit?**
- Once computed, $L$ and $U$ can solve multiple systems with the same $A$ but different $b$ vectors efficiently.
- The decomposition depends only on $A$, not $b$.

## Existence Theorem
A square matrix $A$ has an LU decomposition if it can be reduced to row echelon form $U$ via Gaussian elimination **without row swaps**.

## Construction Steps
1. Perform Gaussian elimination on $A$ to get $U$ (row echelon form), tracking multipliers.
2. Construct $L$:
   - **Diagonal entries**: Reciprocal of the multiplier used to create the leading 1 in that row.
   - **Below-diagonal entries**: Negative of the multiplier used to create the zero in that position.
3. Verify $A = LU$.

## Example
Given $A = \begin{bmatrix} 2 & 4 & 1 \\ 8 & 10 & 2 \\ 2 & 5 & 4 \end{bmatrix}$:

**Step 1: Gaussian Elimination to get $U$**
- $R_1 \leftarrow \frac{1}{2}R_1$ (multiplier $\frac{1}{2}$)
- $R_2 \leftarrow R_2 - 4R_1$ (multiplier $4$)
- $R_3 \leftarrow R_3 - 1R_1$ (multiplier $1$)
- $R_2 \leftarrow \frac{1}{9}R_2$ (multiplier $\frac{1}{9}$)
- $R_3 \leftarrow R_3 - 3R_2$ (multiplier $3$)
- $R_3 \leftarrow \frac{1}{2}R_3$ (multiplier $\frac{1}{2}$)

**Step 2: Construct $L$**
- Diagonal: Reciprocals of row-scaling multipliers ($2, 9, 2$).
- Below-diagonal: Negatives of row-addition multipliers ($4, 1, 3$).

$$
L = \begin{bmatrix} 2 & 0 & 0 \\ 4 & 9 & 0 \\ 1 & 3 & 2 \end{bmatrix}, \quad
U = \begin{bmatrix} 1 & 2 & 0.5 \\ 0 & 1 & -0.22 \\ 0 & 0 & 1 \end{bmatrix}
$$
*(Note: Exact values depend on specific row operations performed.)*

**Result:** $A = LU$.

## Key Properties
- LU decomposition is **not unique** unless additional constraints (like unit diagonal in $L$) are imposed.
- Efficient for solving $Ax = b$ repeatedly with varying $b$.