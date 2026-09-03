---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "HCF and LCM"
difficulty: "Medium"
tags: [cds, elementary-mathematics, hcf-lcm, topic]
---

# HCF and LCM

## Theory, Intuition & Formulas

### 1. Fundamental Definitions & Canonical Prime Factorization
- **Highest Common Factor (HCF / GCD)**: The greatest positive integer that divides each of the given numbers without leaving a remainder.
  - For canonical factorizations $A = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$ and $B = p_1^{b_1} p_2^{b_2} \cdots p_k^{b_k}$:
    $$\operatorname{HCF}(A, B) = p_1^{\min(a_1, b_1)} \cdot p_2^{\min(a_2, b_2)} \cdots p_k^{\min(a_k, b_k)}$$
- **Least Common Multiple (LCM)**: The smallest positive integer that is divisible by each of the given numbers.
  - For canonical factorizations:
    $$\operatorname{LCM}(A, B) = p_1^{\max(a_1, b_1)} \cdot p_2^{\max(a_2, b_2)} \cdots p_k^{\max(a_k, b_k)}$$

### 2. Fundamental Product Identity
For any two positive integers $A$ and $B$:
$$\operatorname{HCF}(A, B) \times \operatorname{LCM}(A, B) = A \times B$$
> [!WARNING]
> This product identity holds **strictly for two numbers only**! For three or more numbers, $\operatorname{HCF}(A, B, C) \times \operatorname{LCM}(A, B, C) \neq A \cdot B \cdot C$.

### 3. Co-prime Representation Model
If $\operatorname{HCF}(A, B) = H$, then the numbers can always be written as:
$$A = H \cdot x, \quad B = H \cdot y \quad \text{where } \operatorname{GCD}(x, y) = 1 \text{ (co-prime)}$$
- Product relation: $A \cdot B = H^2 x y = H \cdot L \implies \operatorname{LCM}(A, B) = L = H \cdot x \cdot y$.
- Ratio of numbers: $\frac{A}{B} = \frac{x}{y}$ (in lowest reduced form).

### 4. Fractions & Polynomials HCF & LCM
- **Fractions**:
  $$\operatorname{HCF}\left(\frac{a}{b}, \frac{c}{d}, \frac{e}{f}\right) = \frac{\operatorname{HCF}(a, c, e)}{\operatorname{LCM}(b, d, f)}$$
  $$\operatorname{LCM}\left(\frac{a}{b}, \frac{c}{d}, \frac{e}{f}\right) = \frac{\operatorname{LCM}(a, c, e)}{\operatorname{HCF}(b, d, f)}$$
  *(Note: Fractions MUST be in lowest reduced form before applying formulas!)*

- **Polynomials**:
  - Express polynomials in fully factored product form over $\mathbb{R}$ or $\mathbb{Z}$.
  - Take lowest powers of common irreducible linear/quadratic factors for HCF, and highest powers of all factors for LCM.

---

## Subtopics & Core Models

- [[cds/math/notes/subtopics/hcf_methods|HCF Methods & Co-Prime Copair Counting]]
- [[cds/math/notes/subtopics/lcm_models|LCM Models & Remainder Theorems]]

---

## Variations

- [[cds/math/notes/variations/var8|HCF via Successive Quotients]]
- [[cds/math/notes/variations/var9|Co-prime Pairs Given Product & HCF]]
- [[cds/math/notes/variations/var10|Largest 4-Digit Number with Constant Remainder]]
- [[cds/math/notes/variations/var11|Smallest 4-Digit Number with Constant Difference]]

---

## Performance Overview

```mermaid
xychart-beta
    title "Topic Accuracy"
    x-axis ["HCF and LCM"]
    y-axis "Accuracy %" 0 --> 100
    bar [100]
```

```mermaid
pie title HCF LCM Difficulty
    "HCF Methods (Easy)" : 1
    "LCM Models (Medium)" : 1
```

```mermaid
pie title Mistake Breakdown
    "None" : 1
```

---

## Navigation

- [[cds/math/math_overview|Elementary Mathematics Overview]]
- [[cds/math/question_db|Question Database]]
