# Linear Equations — Chapter 17 Topic & Subtopic Notes

## 1. Chapter Overview & Taxonomy

| Subtopic | Focus Areas & Theoretical Foundations | Key Theorems & Properties |
| :--- | :--- | :--- |
| **1. System Consistency & Solvability** | $a_1 x + b_1 y = c_1$, $a_2 x + b_2 y = c_2$ | Ratios $\frac{a_1}{a_2}, \frac{b_1}{b_2}, \frac{c_1}{c_2}$, Unique/Infinite/No solution |
| **2. Algebraic Transformations & Substitution** | Non-linear systems reducible to linear | Substitution $u=\frac{1}{x}, v=\frac{1}{y}$ or $2^a, 3^b$, Symmetric Elimination |
| **3. Digit Reversal & Number Theory** | $N = 10x + y$, Reversed $N' = 10y + x$ | $N - N' = 9(x-y)$, $N + N' = 11(x+y)$, Digit Sum Multiplier $k+m=11$ |
| **4. 3-Variable Linear Systems & Cyclic Sums** | $x+y+z=d$, Pairwise sums $x+y=a, y+z=b, z+x=c$ | Cyclic Addition $\sum (x+y) = 2(x+y+z)$, Determinants / Elimination |
| **5. Applied Word Problems & Rates** | Upstream/Downstream speed, Coin counting, Mixture, Allocation | Relative speed $v_d = u+v, v_u = u-v$, Unit cost equations, Fixed + variable rates |

---

## 2. Core Theorems, Theorems & Mathematical Properties

### Theorem 1: Determinant & Ratio Condition for 2-Variable Linear Systems
Given a system of two linear equations:
$$a_1 x + b_1 y = c_1$$
$$a_2 x + b_2 y = c_2$$

1. **Unique Solution (Consistent & Independent)**:
   $$\frac{a_1}{a_2} \neq \frac{b_1}{b_2} \quad \iff \quad a_1 b_2 - a_2 b_1 \neq 0$$
   *Geometric Meaning*: The lines intersect at exactly one point.

2. **Infinitely Many Solutions (Consistent & Dependent)**:
   $$\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$$
   *Geometric Meaning*: The two equations represent the exact same line (coincident lines).

3. **No Solution (Inconsistent)**:
   $$\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$$
   *Geometric Meaning*: The lines are strictly parallel and non-intersecting.

---

### Theorem 2: The Two-Digit Reversal Invariant Theorem
Let $N$ be a two-digit number with tens digit $x$ and unit digit $y$, so $N = 10x + y$.
Let $N'$ be the number formed by interchanging the digits, so $N' = 10y + x$.

1. **Difference Property**:
   $$N - N' = (10x + y) - (10y + x) = 9(x - y)$$
   *Consequence*: The difference between any 2-digit number and its reverse is **always a multiple of 9**, and dividing this difference by 9 gives the difference between the digits $|x - y|$.

2. **Sum Property**:
   $$N + N' = (10x + y) + (10y + x) = 11(x + y)$$
   *Consequence*: The sum of any 2-digit number and its reverse is **always a multiple of 11**.

3. **Digit Sum Multiplier Complementarity**:
   If $N = k(x+y)$ and $N' = m(x+y)$, then:
   $$N + N' = (k + m)(x + y)$$
   Since $N + N' = 11(x + y)$, it strictly holds that:
   $$k + m = 11 \implies m = 11 - k$$

---

### Theorem 3: Pairwise Sum Symmetries (Cyclic Systems)
When given pairwise sums of three variables $x, y, z$:
$$x + y = S_1$$
$$y + z = S_2$$
$$z + x = S_3$$

Adding all three equations yields:
$$2(x + y + z) = S_1 + S_2 + S_3 \implies x + y + z = \frac{S_1 + S_2 + S_3}{2}$$

Individual variables are recovered instantly by subtraction:
$$x = (x+y+z) - (y+z) = \frac{S_1 + S_2 + S_3}{2} - S_2$$
$$y = (x+y+z) - (z+x) = \frac{S_1 + S_2 + S_3}{2} - S_3$$
$$z = (x+y+z) - (x+y) = \frac{S_1 + S_2 + S_3}{2} - S_1$$

*Eldest-Youngest Age Difference*:
$$x - z = (x+y) - (y+z) = S_1 - S_2$$

---

## 3. High-Yield Question Categorization Matrix

| Category | Typical Question Types | Unique Archetypes Selected for Practice |
| :--- | :--- | :--- |
| **Cat 1: Solvability & Consistency** | Value of $k$ for unique/infinite/no solutions, linear independence | **Q18, Q38, Q48, Q69** |
| **Cat 2: Algebraic Substitutions** | Reciprocal variables $\frac{1}{x}, \frac{1}{y}$, exponential variables $2^a, 3^b$ | **Q35, Q37, Q50, Q68** |
| **Cat 3: Digit & Number Properties** | Reversal differences, digit-sum ratios, prime/composite factors | **Q33, Q54, Q67, Q72** |
| **Cat 4: Cyclic & Multi-Variable** | 3-variable systems, pairwise sums, ratio share allocations | **Q39, Q46, Q70** |
| **Cat 5: Motion, Work & Rates** | Upstream/downstream speed, train passenger transfers, income/expenditure ratios | **Q19, Q31, Q71** |

---

## 4. Curated Unique Practice Questions (With Detailed Solvers)

### Question 1 (Algebraic Exponents): Q50 [CDS 2012 I]
**Problem**: If $3^{x+y} = 81$ and $81^{x-y} = 3$, then what is the value of $x$?

- **Step 1**: Express both equations with prime base 3.
  $$3^{x+y} = 81 = 3^4 \implies x + y = 4 \quad \text{--- (i)}$$
- **Step 2**: Convert second equation:
  $$(3^4)^{x-y} = 3^1 \implies 3^{4(x-y)} = 3^1 \implies 4(x-y) = 1 \implies x - y = \frac{1}{4} \quad \text{--- (ii)}$$
- **Step 3**: Add equations (i) and (ii) to eliminate $y$:
  $$2x = 4 + \frac{1}{4} = \frac{17}{4} \implies x = \frac{17}{8}$$
- **Answer**: **(b) $\frac{17}{8}$**

---

### Question 2 (Digit Reversal Invariant): Q72 [CDS 2016 I]
**Problem**: Let a two-digit number be $k$ times the sum of its digits. If the number formed by interchanging the digits is $m$ times the sum of the digits, then what is the value of $m$?

- **Step 1**: Let the 2-digit number be $N = 10x + y$ and sum of digits be $S = x + y$.
  Given $N = k(x+y)$.
- **Step 2**: Let reversed number be $N' = 10y + x = m(x+y)$.
- **Step 3**: Add $N$ and $N'$:
  $$N + N' = (10x + y) + (10y + x) = 11(x + y)$$
- **Step 4**: Equate to factored form:
  $$(k + m)(x + y) = 11(x + y) \implies k + m = 11 \implies m = 11 - k$$
- **Answer**: **(c) $11 - k$**

---

### Question 3 (Reciprocal Parameterization): Q68 [CDS 2016 I]
**Problem**: If $\frac{p}{x} + \frac{q}{y} = m$ and $\frac{q}{x} + \frac{p}{y} = n$, then what is $\frac{x}{y}$ equal to?

- **Step 1**: Substitute $u = \frac{1}{x}$ and $v = \frac{1}{y}$:
  $$p u + q v = m \quad \text{--- (i)}$$
  $$q u + p v = n \quad \text{--- (ii)}$$
- **Step 2**: Solve for $u$ and $v$ using Cramer's rule / elimination:
  Multiply (i) by $p$ and (ii) by $q$:
  $$p^2 u + p q v = p m$$
  $$q^2 u + p q v = q n$$
  Subtracting gives:
  $$(p^2 - q^2) u = p m - q n \implies u = \frac{p m - q n}{p^2 - q^2}$$
- **Step 3**: Similarly multiply (i) by $q$ and (ii) by $p$:
  $$p q u + q^2 v = q m$$
  $$p q u + p^2 v = p n$$
  Subtracting gives:
  $$(p^2 - q^2) v = p n - q m \implies v = \frac{p n - q m}{p^2 - q^2}$$
- **Step 4**: Compute ratio $\frac{x}{y}$:
  $$\frac{x}{y} = \frac{1/u}{1/v} = \frac{v}{u} = \frac{\frac{p n - q m}{p^2 - q^2}}{\frac{p m - q n}{p^2 - q^2}} = \frac{p n - q m}{p m - q n} = \frac{n p - m q}{m p - n q}$$
- **Answer**: **(d) $\frac{n p - m q}{m p - n q}$** (or equivalent option matching signs)

---

### Question 4 (Pairwise Cyclic Sums): Q70 [CDS 2016 I]
**Problem**: There are three brothers. The sums of ages of two of them at a time are 4 yr, 6 yr and 8 yr. The age difference between the eldest and the youngest is:

- **Step 1**: Let the ages of the brothers in increasing order be $a \le b \le c$.
- **Step 2**: Pairwise sums give:
  $$a + b = 4$$
  $$a + c = 6$$
  $$b + c = 8$$
- **Step 3**: Find difference between eldest ($c$) and youngest ($a$):
  $$(b + c) - (a + b) = c - a = 8 - 4 = 4 \text{ years}$$
- **Answer**: **(b) 4 yr**

---

### Question 5 (System Consistency & Infinite Solutions): Q69 [CDS 2016 I]
**Problem**: The value of $k$, for which the system of equations $3x - k y - 20 = 0$ and $6x - 10y + 40 = 0$ has no solution, is:

- **Step 1**: Write equations in standard form $a x + b y = c$:
  $$3x - k y = 20 \implies a_1 = 3, b_1 = -k, c_1 = 20$$
  $$6x - 10y = -40 \implies a_2 = 6, b_2 = -10, c_2 = -40$$
- **Step 2**: Apply condition for NO solution ($\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$):
  $$\frac{3}{6} = \frac{-k}{-10} \implies \frac{1}{2} = \frac{k}{10} \implies k = 5$$
- **Check constant ratio**:
  $$\frac{c_1}{c_2} = \frac{20}{-40} = -\frac{1}{2} \neq \frac{1}{2}$$
  Thus, $k = 5$ guarantees parallel lines and no solution.
- **Answer**: **(c) 5**

---

## 5. Next Steps & Interactive Practice Plan

1. **Review Notes**: Check the theoretical foundations and key theorems above.
2. **Practice Session**: Try solving remaining curated questions from Pathfinder Chapter 17 (e.g. Q19 downstream/upstream rate, Q31 train transfers, Q71 ratio income-savings).
3. **Vault Sync**: These notes are formatted for immediate Obsidian & SAGE vault integration.
