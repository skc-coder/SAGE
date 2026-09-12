https://mathispower4u.com/linear-alg.php
https://www.youtube.com/watch?v=DOXbE4hMF4Y
## Definition
For an $n \times n$ matrix $A$, a **nonzero** vector $x \in \mathbb{R}^n$ is an **eigenvector** of $A$ if:
$$Ax = \lambda x$$
where $\lambda$ is a scalar called the **eigenvalue**.

- $x \neq 0$ is required; otherwise, any $\lambda$ would satisfy $A0 = \lambda 0$.

The word eigen is German meaning proper.
Eigenvalues can also be called proper values,
characteristic values, or latent roots.

## Finding (general) Eigenvalues
For any non zero vector $x$, $\lambda$ is an eigenvalue iff the system $(\lambda I - A)x = 0$ has a **nontrivial solution**. 
This occurs when:
$$\det(A - \lambda I) = 0$$
This is the **[[characteristic equation]]**. Expanding the determinant yields the **characteristic polynomial**, a degree-$n$ polynomial in $\lambda$. Its roots are the eigenvalues.

An matrix may will have $n$ number of eigenvalues.

## Finding Eigenvectors
For a specific eigenvalue $\lambda$, solve $(A - \lambda I)x = 0$ for nonzero $x$.

### Example: $\lambda = 2$ for the $3 \times 3$ matrix above
$$2I - A = \begin{bmatrix} 1 & -2 & 1 \\ 0 & 1 & -4 \\ 0 & 0 & 0 \end{bmatrix}$$
Row reduction gives:
- $x_2 = 4x_3$
- $x_1 = -2x_2 + x_3 = -7x_3$

Let $x_3 = t$ (free variable). Eigenvectors:
$$x = t \begin{bmatrix} -7 \\ 4 \\ 1 \end{bmatrix}, \quad t \neq 0$$


## Equivalent Conditions for $\lambda$ being an eigenvalue
- $\lambda$ satisfies the characteristic equation $\det(A -\lambda I) = 0$.
- $(\lambda I - A)x = 0$ has nontrivial solutions.
- There exists nonzero $x$ such that $Ax = \lambda x$.

## [[eigenvalues shortcuts]]
[[eignevalues transformations]]
[[Cayley Hamilton Theorem]]