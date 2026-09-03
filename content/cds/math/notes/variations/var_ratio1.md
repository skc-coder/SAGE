---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Ratio and Proportion"
subtopic: "Componendo and Dividendo"
difficulty: "Hard"
importance: "Important"
tags: [cds, elementary-mathematics, ratio, variation, cd-theorem]
---

# Variation 1: Nested Componendo-Dividendo Higher Algebraic Invariant

## Novel Problem Statement
If $\frac{x^3 + 3x}{3x^2 + 1} = \frac{189}{61}$, find the real value of $x$.

---

## Step-by-Step Mathematical Solution

### Step 1: Recognize Algebraic Expansion Symmetry
Notice that $(x + 1)^3 = x^3 + 3x^2 + 3x + 1$ and $(x - 1)^3 = x^3 - 3x^2 + 3x - 1$.
The given expression is:
$$\frac{x^3 + 3x}{3x^2 + 1} = \frac{189}{61}$$

---

### Step 2: Apply Componendo and Dividendo
Applying C&D to both sides:
$$\frac{(x^3 + 3x) + (3x^2 + 1)}{(x^3 + 3x) - (3x^2 + 1)} = \frac{189 + 61}{189 - 61}$$

Rearranging the left-hand side numerator and denominator:
$$\frac{x^3 + 3x^2 + 3x + 1}{x^3 - 3x^2 + 3x - 1} = \frac{250}{128}$$

Using polynomial identities:
$$\frac{(x + 1)^3}{(x - 1)^3} = \frac{125}{64}$$

---

### Step 3: Extract Cube Roots & Solve
Taking the cube root on both sides:
$$\frac{x + 1}{x - 1} = \frac{\sqrt[3]{125}}{\sqrt[3]{64}} = \frac{5}{4}$$

Applying C&D once more:
$$\frac{(x + 1) + (x - 1)}{(x + 1) - (x - 1)} = \frac{5 + 4}{5 - 4}$$
$$\frac{2x}{2} = \frac{9}{1} \implies x = 9$$

---

## Takeaway & Examination Insight
C&D can be used in reverse to synthesize perfect binomial expansions $(a+b)^n / (a-b)^n$, reducing cubic/quartic polynomials into single linear root equations.

---

## Navigation

- Subtopic: [[cds/math/notes/subtopics/cd_property|Componendo and Dividendo Theorem]]
- Topic: [[cds/math/notes/ratio_proportion|Ratio and Proportion]]
