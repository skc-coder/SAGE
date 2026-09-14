### 1. Triangular/Diagonal Matrices
If $A$ is upper triangular, lower triangular, or diagonal:
$$ \det(A) = \text{product of diagonal elements} $$
$$ \det \begin{bmatrix} a & b & c \\ 0 & d & e \\ 0 & 0 & f \end{bmatrix} = a \cdot d \cdot f $$

### 2. Row/Column Operations
Use these to create zeros (make it triangular):
*   **Swap rows/cols:** $\det(A_{new}) = -\det(A_{old})$
*   **Multiply row/col by $k$:** $\det(A_{new}) = k \cdot \det(A_{old})$
*   **Add multiple of one row/col to another:** $\det(A_{new}) = \det(A_{old})$ (No change - **Best for simplification**)

### 3. Special Matrices
*   **Zero Row/Col:** $\det(A) = 0$
*   **Identical Rows/Cols:** $\det(A) = 0$
*   **Proportional Rows/Cols:** $\det(A) = 0$

### 4. Properties
*   $\det(A^T) = \det(A)$
*   $\det(AB) = \det(A)\det(B)$
*   $\det(A^{-1}) = \frac{1}{\det(A)}$ (if invertible)
*   $\det(kA) = k^n \det(A)$ for $n \times n$ matrix (Common mistake: don't forget $k^n$)


### 8. $3 \times 3$ Sarrus Rule (Visual)
$$
A = \begin{bmatrix} 
a_{11} & a_{12} & a_{13} \\ 
a_{21} & a_{22} & a_{23} \\ 
a_{31} & a_{32} & a_{33} 
\end{bmatrix}
$$

$$
\begin{array}{ccc|cc}
a_{11} & a_{12} & a_{13} & a_{11} & a_{12} \\
a_{21} & a_{22} & a_{23} & a_{21} & a_{22} \\
a_{31} & a_{32} & a_{33} & a_{31} & a_{32}
\end{array}
$$

### The Formula
$$
\det(A) = (\text{Sum of Down-Right}) - (\text{Sum of Up-Right})
$$

**Down-Right ($\searrow$) — Positive:**
1.  $a_{11} \cdot a_{22} \cdot a_{33}$
2.  $a_{12} \cdot a_{23} \cdot a_{31}$
3.  $a_{13} \cdot a_{21} \cdot a_{32}$

**Up-Right ($\nearrow$) — Negative:**
1.  $a_{31} \cdot a_{22} \cdot a_{13}$
2.  $a_{32} \cdot a_{23} \cdot a_{11}$
3.  $a_{33} \cdot a_{21} \cdot a_{12}$

**Final Equation:**
$$
\det(A) = (a_{11}a_{22}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32}) - (a_{13}a_{22}a_{31} + a_{11}a_{23}a_{32} + a_{12}a_{21}a_{33})
$$

