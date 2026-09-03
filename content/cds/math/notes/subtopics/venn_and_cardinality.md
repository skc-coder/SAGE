---
exam: "CDS"
subject: "Math"
topic: "Set Theory"
subtopic: "Venn Diagrams & Cardinality"
difficulty: "Hard"
tags: [cds, math, set-theory, subtopic]
---

# Venn Diagrams & Inclusion-Exclusion Principle

## 1. Cardinality Rules for Two Sets
Let $A$ and $B$ be finite sets in a universal set $U$:

1. **Union Formula**:
   $$n(A \cup B) = n(A) + n(B) - n(A \cap B)$$
2. **Disjoint Sets**:
   $$n(A \cap B) = 0 \implies n(A \cup B) = n(A) + n(B)$$
3. **Only $A$ (Elements in $A$ but not $B$)**:
   $$n(A - B) = n(A) - n(A \cap B)$$
4. **Exactly One of $A$ or $B$**:
   $$n(A \Delta B) = n(A) + n(B) - 2n(A \cap B)$$
5. **Neither $A$ nor $B$**:
   $$n(A' \cap B') = n(U) - n(A \cup B)$$

## 2. Inclusion-Exclusion Principle for Three Sets
For finite sets $A$, $B$, and $C$:

$$n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(B \cap C) - n(C \cap A) + n(A \cap B \cap C)$$

### Region-Based Analysis (Venn Diagram Regions)
Let region variables be:
- $a, b, c$: Only $A$, Only $B$, Only $C$
- $d, e, f$: Exactly two of $A, B, C$
- $g$: All three $A \cap B \cap C$

Key Relations:
- Total union $n(A \cup B \cup C) = a + b + c + d + e + f + g$
- $n(A) = a + d + f + g$
- Sum of pairwise intersections $= d + e + f + 3g$

## 3. Boundary & Optimization Theorem
If $A$ and $B$ have $m$ and $n$ elements respectively ($m \le n$):
- **Minimum value of $n(A \cup B)$**: $\max(m, n) = n$ (when $A \subseteq B$)
- **Maximum value of $n(A \cup B)$**: $m + n$ (when $A \cap B = \emptyset$)
- **Minimum value of $n(A \cap B)$**: $\max(0, m + n - n(U))$
- **Maximum value of $n(A \cap B)$**: $\min(m, n) = m$
