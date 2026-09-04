---
exam: "CDS"
subject: "Math"
topic: "Set Theory"
subtopic: "Venn Diagrams & Cardinality"
difficulty: "Hard"
tags: [cds, math, set-theory, subtopic]
---

# Systematic 8-Region Method for 3-Set Word Problems

## 1. The Atomic 8-Region Variable Assignment Strategy
Every 3-set problem ($A, B, C$) within a Universal set $U$ breaks down into **8 disjoint elementary regions**:

```
      +-----------------------------------------+
      | Universal Set U                         |
      |   +-------------+     +-------------+   |
      |  /     A         \   /      B        \  |
      | /                 \ /                 \ |
      | |   a (Only A)    | |   b (Only B)    | |
      | |       \    d   /   \   e    /       | |
      | |        \ (A∩B) /   \ (B∩C) /        | |
      | |         +-----+-----+-----+         | |
      | \        /       |     |     \        / |
      |  \      /    f   |  g  |      \      /  |
      |   +----+  (A∩C)  |(A∩B∩C)      +----+   |
      |         \        |     |      /         |
      |          +-------+-----+-----+          |
      |                 /   c (Only C)\         |
      |                /               \        |
      |               +-----------------+       |
      |                                         |
      |       h = Neither A, B, nor C           |
      +-----------------------------------------+
```

### The 8 Variables Defined:
- $a$: Elements in **Only A**
- $b$: Elements in **Only B**
- $c$: Elements in **Only C**
- $d$: Elements in **Only A and B** ($A \cap B \cap C'$)
- $e$: Elements in **Only B and C** ($B \cap C \cap A'$)
- $f$: Elements in **Only A and C** ($A \cap C \cap B'$)
- $g$: Elements in **All Three** ($A \cap B \cap C$)
- $h$: Elements in **None** ($(A \cup B \cup C)'$)

---

## 2. The 5 Universal Linear Equations
Instead of memorizing complex set formulas, translate every question into these 5 fundamental equations:

$$\begin{aligned}
\text{Total Universal Set } N(U) &= a + b + c + d + e + f + g + h \\
\text{Total Set } A &= a + d + f + g \\
\text{Total Set } B &= b + d + e + g \\
\text{Total Set } C &= c + e + f + g \\
\text{Intersection } (A \cap B) &= d + g \\
\text{Intersection } (B \cap C) &= e + g \\
\text{Intersection } (A \cap C) &= f + g
\end{aligned}$$

---

## 3. High-Yield Grouping Shortcuts

1. **Exactly One Category**:
   $$E_1 = a + b + c$$

2. **Exactly Two Categories**:
   $$E_2 = d + e + f$$

3. **At Least Two Categories**:
   $$E_{\ge 2} = d + e + f + g = E_2 + g$$

4. **Sum of Sets Equation**:
   $$N(A) + N(B) + N(C) = (a+b+c) + 2(d+e+f) + 3g = E_1 + 2E_2 + 3g$$

5. **Sum of Pairwise Intersections Equation**:
   $$N(A \cap B) + N(B \cap C) + N(A \cap C) = (d+e+f) + 3g = E_2 + 3g$$

---

## 4. The 4-Step Systematic Algorithm

1. **Step 1 — Draw & Label**: Draw the 3-circle Venn diagram and assign variables $a, b, c, d, e, f, g, h$.
2. **Step 2 — Bottom-Up Filling**: If $g$ (all 3) and pairwise intersections are given, start filling from the innermost center $g$ outwards!
3. **Step 3 — System of Linear Equations**: If central regions are unknown, write down the 5 linear equations using $a, b, c, d, e, f, g, h$.
4. **Step 4 — Non-Negativity Bounds (for Ranges)**:
   Since all regions represent physical counts of items:
   $$a \ge 0, \quad b \ge 0, \quad c \ge 0, \quad d \ge 0, \quad e \ge 0, \quad f \ge 0, \quad g \ge 0, \quad h \ge 0$$
   Use $g \ge 0$ and region non-negativity to instantly find minimum and maximum possible values of any unknown!
