A [[system of linear equations]] cam be viewed in three different but equivalent ways: as a matrix equation, as a vector equation, or as a system of linear equations (duh!).

---
If $A$ is an $m \times n$ matrix, with columns $\mathbf{a}_1, \dots, \mathbf{a}_n$, and if $\mathbf{b}$ is in $\mathbb{R}^m$, the *matrix equation*
$$
A\mathbf{x} = \mathbf{b} \tag{4}
$$
has the same solution set as the vector equation
$$
x_1\mathbf{a}_1 + x_2\mathbf{a}_2 + \cdots + x_n\mathbf{a}_n = \mathbf{b} \tag{5}
$$
which, in turn, has the same solution set as the system of linear equations whose augmented matrix is
$$
\begin{bmatrix}
\mathbf{a}_1 & \mathbf{a}_2 & \cdots & \mathbf{a}_n & \mathbf{b}
\end{bmatrix} \tag{6}
$$


The following statements are logically equivalent i.e. either they are all true statements or they are all false.

* For each $\mathbf{b}$ in $\mathbb{R}^m$, the equation $A\mathbf{x} = \mathbf{b}$ has a solution.
* Each $\mathbf{b}$ in $\mathbb{R}^m$ is a linear combination of the columns of $A$.
* The columns of $A$ span $\mathbb{R}^m$.
* $A$ has a pivot position in every row.
	* We are talking about coefficient matrix, not an augmented matrix. If an augmented matrix has a pivot position in every row, then the equation may or may not be consistent.


EXAMPLE:
Compute $A\mathbf{x}$, where $A = \begin{bmatrix} 2 & 3 & 4 \\ -1 & 5 & -3 \\ 6 & -2 & 8 \end{bmatrix}$ and $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$.

SOLUTION
From the definition,
$$
\begin{bmatrix} 2 & 3 & 4 \\ -1 & 5 & -3 \\ 6 & -2 & 8 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = x_1 \begin{bmatrix} 2 \\ -1 \\ 6 \end{bmatrix} + x_2 \begin{bmatrix} 3 \\ 5 \\ -2 \end{bmatrix} + x_3 \begin{bmatrix} 4 \\ -3 \\ 8 \end{bmatrix} \tag{7}
$$
$$
= \begin{bmatrix} 2x_1 \\ -x_1 \\ 6x_1 \end{bmatrix} + \begin{bmatrix} 3x_2 \\ 5x_2 \\ -2x_2 \end{bmatrix} + \begin{bmatrix} 4x_3 \\ -3x_3 \\ 8x_3 \end{bmatrix}
$$
$$
= \begin{bmatrix} 2x_1 + 3x_2 + 4x_3 \\ -x_1 + 5x_2 - 3x_3 \\ 6x_1 - 2x_2 + 8x_3 \end{bmatrix}
$$

The first entry in the product $A\mathbf{x}$ is a sum of products (sometimes called a **dot product**), using the first row of $A$ and the entries in $\mathbf{x}$. That is,
$$
\begin{bmatrix} 2 & 3 & 4 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} 2x_1 + 3x_2 + 4x_3 \end{bmatrix}
$$

This matrix shows how to compute the first entry in $A\mathbf{x}$ directly, without writing down all the calculations shown in (7). Similarly, the second entry in $A\mathbf{x}$ can be calculated at once by multiplying the entries in the second row of $A$ by the corresponding entries in $\mathbf{x}$ and then summing the resulting products:
$$
\begin{bmatrix} -1 & 5 & -3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} = \begin{bmatrix} -x_1 + 5x_2 - 3x_3 \end{bmatrix}
$$

Likewise, the third entry in $A\mathbf{x}$ can be calculated from the third row of $A$ and the entries in $\mathbf{x}$.