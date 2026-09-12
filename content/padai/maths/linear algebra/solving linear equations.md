Also called #gaussian_elimination.
https://en.wikipedia.org/wiki/Gaussian_elimination

The basic strategy is to replace one system with an equivalent system (i.e., one with the same solution set) that is easier to solve.

This is done through elementary [[row operations]] to obtain row reduced [echelon form](echelon%20form.md).

The variables corresponding to pivot columns in the matrix are called **basic variables**.  The other variable is called a **free variable**.

Whenever a system is *consistent* the solution set can be described explicitly by solving the reduced system of equations for the basic variables in terms of the free variables. 

This operation is possible because the reduced echelon form places each basic variable in one and only one equation. 

**Example:** Given augmented matrix in reduced echelon form:
$$
\begin{bmatrix}
1 & 0 & -5 & 1 \\
0 & 1 & 1 & 4 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

Associated equations:
$$
\begin{aligned}
x_1 - 5x_3 &= 1 \\
x_2 + x_3 &= 4 \\
0 &= 0
\end{aligned}
$$

Solve for basic variables in terms of free variable:
$$
\begin{cases}
x_1 = 1 + 5x_3 \\
x_2 = 4 - x_3 \\
x_3 \text{ is free}
\end{cases}
$$

