---
exam: "CDS"
subject: "Math"
topic: "Quadrilateral and Polygon"
subtopic: "Trapezium Diagonals & Euler Identity"
difficulty: "Hard"
status: "Correct"
importance: "Important"
tags: [cds, math, question, trapezium, geometry]
---

# Q1: Trapezium Diagonal Length Identity

## Question
In a trapezium $ABCD$ with $AB \parallel CD$, prove that the sum of the squares of the diagonals is given by:
$$AC^2 + BD^2 = AD^2 + BC^2 + 2(AB \cdot CD)$$

## Step-by-Step Solution

### 1. Vector / Coordinate Approach
Let the vertices of trapezium $ABCD$ be defined in the Cartesian coordinate system:
- Place vertex $A$ at the origin $(0, 0)$.
- Vector $\vec{AB} = a \hat{i}$, where $a = AB$.
- Vector $\vec{DC} = b \hat{i}$, where $b = CD$, and vertex $D$ is at $(x_D, y_D)$.
- Vertex $C$ is located at $(x_D + b, y_D)$.

### 2. Distance Calculations for Sides & Diagonals
- Non-parallel side $AD^2$:
  $$AD^2 = x_D^2 + y_D^2$$
- Non-parallel side $BC^2$:
  $$\vec{BC} = \vec{C} - \vec{B} = (x_D + b - a) \hat{i} + y_D \hat{j}$$
  $$BC^2 = (x_D + b - a)^2 + y_D^2 = x_D^2 + y_D^2 + (b - a)^2 + 2 x_D (b - a)$$

- Sum of non-parallel sides $AD^2 + BC^2$:
  $$AD^2 + BC^2 = 2 x_D^2 + 2 y_D^2 + a^2 + b^2 - 2ab + 2 x_D (b - a)$$

- Diagonal $AC^2$:
  $$AC^2 = (x_D + b)^2 + y_D^2 = x_D^2 + y_D^2 + b^2 + 2b x_D$$

- Diagonal $BD^2$:
  $$BD^2 = (x_D - a)^2 + y_D^2 = x_D^2 + y_D^2 + a^2 - 2a x_D$$

### 3. Summing Diagonal Squares
Summing $AC^2$ and $BD^2$:
$$AC^2 + BD^2 = (x_D^2 + y_D^2 + b^2 + 2b x_D) + (x_D^2 + y_D^2 + a^2 - 2a x_D)$$
$$AC^2 + BD^2 = 2 x_D^2 + 2 y_D^2 + a^2 + b^2 + 2 x_D (b - a)$$

### 4. Comparing Both Expressions
Subtracting $(AD^2 + BC^2)$ from $(AC^2 + BD^2)$:
$$(AC^2 + BD^2) - (AD^2 + BC^2) = 2ab = 2(AB \cdot CD)$$
$$AC^2 + BD^2 = AD^2 + BC^2 + 2(AB \cdot CD)$$

Hence, proved!
