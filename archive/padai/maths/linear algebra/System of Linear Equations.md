A system of [[linear equations]] has 
1. no solution, or
2. exactly one solution, or
3. infinitely many solutions.

A system of linear equations is said to be **consistent** if it has either one solution or infinitely many solutions; a system is **inconsistent** if it has no solution.

---

 TWO FUNDAMENTAL QUESTIONS ABOUT A LINEAR SYSTEM
1. Is the system **consistent**; that is, does at least one solution exist? 
2. If a solution exists, is it the only one; that is, is the solution **unique**?

Both of these questions can be answered by reducing the system to row reduced [echelon form](echelon%20form.md). 
See [[solving linear equations]].

> [!info] Existence and Uniqueness Theorem
A linear system is consistent if and only if the rightmost column of the *augmented matrix* is not a pivot column—that is, if and only if an **echelon form** of the augmented matrix has *no row* of the form with b nonzero $[0.....0 b].$
>
If a linear system is consistent, then the solution set contains either 
(i) a unique solution, when there are no free variables, or 
(ii) infinitely many solutions, when there is at least one free variable.

[[Homogeneous Linear Systems]]
