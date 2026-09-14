The **rank** of a matrix $A$ is the dimension of the **column space** of $A$, denoted as $\text{rank}(A)$.

It equals the number of **pivot columns** in the (row) reduced echelon form (RREF) of $A$.

## Key Properties
- $\text{rank}(A) \le \min(m, n)$ for an $m \times n$ matrix.
- $\text{rank}(A) = \text{rank}(A^T)$.
- $\text{rank}(A) + \text{nullity}(A) = n$ (Rank-Nullity Theorem).

## Interpretation
- **Full Rank**: If $\text{rank}(A) = \min(m, n)$, the matrix has full rank.
- **Linear Independence**: The rank equals the maximum number of linearly independent columns (or rows).
- **Span**: The columns of $A$ span a subspace of dimension $\text{rank}(A)$.
# Rank and [Solutions to Linear Systems](Solutions%20to%20Linear%20Systems)

For a system $A\mathbf{x} = \mathbf{b}$ where $A$ is $m \times n$:

## Existence of Solutions
- **Consistent** if $\text{rank}(A) = \text{rank}([A | \mathbf{b}])$.
- **Inconsistent** if $\text{rank}(A) < \text{rank}([A | \mathbf{b}])$.

## Uniqueness of Solutions
*If consistent*:
- **Unique solution** if $\text{rank}(A) = n$ (no free variables).
- **Infinitely many solutions** if $\text{rank}(A) < n$ (at least one free variable).

## [Homogeneous Linear Systems](Homogeneous%20Linear%20Systems.md) ($A\mathbf{x} = \mathbf{0}$)
- Always consistent (trivial solution $\mathbf{x} = \mathbf{0}$).
	- ie. rank (A) = rank(A|b), always
- **Nontrivial (infinite) solutions exist** iff $\text{rank}(A) < n$.

