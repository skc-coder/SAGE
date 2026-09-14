A rectangular matrix is in echelon (steplike) form (or row echelon form) if it has the following three properties:
1. All nonzero rows are above any rows of all zeros.
2. Each leading entry of a row is in a column to the right of the leading entry of the row above it.
3. All entries in a column below a leading entry are zeros.
If a matrix in echelon form satisfies the following additional conditions, then it is
in reduced echelon form (or reduced row echelon form):
4. The leading entry in each nonzero row is 1.
5. Each leading 1 is the only nonzero entry in its column.

![](attachments/Pasted%20image%2020260428155815.png)

> [!info] Uniqueness of the Reduced Echelon Form
> Each matrix is row equivalent to one and only one reduced echelon matrix.
> 
> And it makes sense, because after making leading entry 1, there is no row operation that doesn't break the condition for rref, hence there is only 1 of this.

---
A **pivot position** in a matrix $A$ is a location in A that corresponds to a leading 1 in the reduced echelon form of $A$. 

A **pivot column** is a column of $A$ that contains
a pivot position

---

# Reducing to ref and rref

The combination of steps 1–4 is called the **forward phase** of the row reduction
algorithm.
Step 5, which produces the unique reduced echelon form, is called the **backward phase**. See [[back substitution]].

1. Begin with the leftmost nonzero column. This is a pivot column. The pivot position is at the top.
2. Select a nonzero entry in the pivot column as a pivot. If necessary, interchange rows to move this entry into the pivot position.
3. Use row replacement operations to create zeros in all positions below the pivot.
4. Cover (or ignore) the row containing the pivot position and cover all rows, if any, above it. Apply steps 1–3 to the submatrix that remains. Repeat the process until there are no more nonzero rows to modify.
5. Beginning with the rightmost pivot and working upward and to the left, create zeros above each pivot. If a pivot is not 1, make it 1 by a scaling operation.