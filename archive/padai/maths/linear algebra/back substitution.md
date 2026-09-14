a equation in echelon form may be used to get solution system using back substitution.
it is similar to backward phase of [echelon form](echelon%20form.md).

just express basic variable starting from bottom in terms of free variables and do substitution in above equations.

Example:
$$
\begin{aligned}
x_1 - 7x_2 + 2x_3 - 5x_4 + 8x_5 &= 10 \\
x_2 - 3x_3 + 3x_4 + x_5 &= -5 \\
x_4 - x_5 &= 4
\end{aligned}
$$
1. From eq 3: $x_4 = 4 + x_5$
2. Substitute into eq 2, solve for $x_2$
3. Substitute $x_2, x_4$ into eq 1, solve for $x_1$
