---
exam: "CDS"
subject: "Math"
topic: "Set Theory"
subtopic: "Types of Sets"
difficulty: "Easy"
tags: [cds, math, set-theory, subtopic]
---

# Types of Sets

## 1. Core Definitions & Notation
A **set** is a well-defined collection of distinct objects.
- **Roster / Tabular Form**: $A = \{2, 3, 5, 7\}$
- **Set-Builder Form**: $A = \{x : x \text{ is a prime number, } x < 10\}$

## 2. Classification of Sets
1. **Empty Set (Null / Void Set)** $\emptyset$ or $\{\}$:
   - Contains zero elements. $| \emptyset | = 0$.
   - Example: $C = \{x : x^2 = 16 \text{ and } x \text{ is an odd integer}\} = \emptyset$.
2. **Singleton Set**:
   - Contains exactly 1 element. e.g., $B = \{x : x + 3 = 3\} = \{0\}$.
3. **Finite vs Infinite Sets**:
   - **Finite**: Countable number of elements (e.g., set of birds in a zoo).
   - **Infinite**: Uncountable/endless elements (e.g., integers $< 1000$, points on a line segment).
4. **Equal Sets ($A = B$)**:
   - Every element of $A$ is in $B$ and every element of $B$ is in $A$. ($A \subseteq B \land B \subseteq A$).
5. **Equivalent Sets ($A \sim B$)**:
   - Same cardinal number $|A| = |B|$, elements need not be identical.

## 3. Power Set & Subsets
- **Subset ($A \subseteq B$)**: Every element of $A$ belongs to $B$.
- **Proper Subset ($A \subset B$)**: $A \subseteq B$ and $A \neq B$.
- **Power Set $\mathcal{P}(A)$**: Set of all subsets of $A$.
  - Number of subsets of set with $n$ elements $= 2^n$.
  - Number of non-empty proper subsets $= 2^n - 2$.
  - Key Identity: $\emptyset \in \mathcal{P}(A)$ and $\emptyset \subseteq A$.

## 4. Key Properties & Exam Patterns
- $\emptyset \subseteq A$ for every set $A$.
- $\emptyset \in \{\emptyset\}$, but $\emptyset \neq \{\emptyset\}$.
- If $|A| = 4$, non-empty proper subsets $= 2^4 - 2 = 14$.
