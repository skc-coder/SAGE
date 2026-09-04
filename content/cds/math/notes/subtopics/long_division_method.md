---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Square Roots and Cube Roots"
subtopic: "Long Division Method for Square Roots"
difficulty: "Medium"
tags: [cds, elementary-mathematics, roots, division-method, subtopic]
---

# Long Division Method for Square Roots

## 1. Core Intuition & Algebraic Foundation

The Long Division Method extracts digits of $\sqrt{N}$ one period at a time based on binomial expansion identity:
$$(10A + b)^2 = 100A^2 + 20Ab + b^2 = 100A^2 + b(20A + b)$$

### Mathematical Intuition Step-by-Step

- Let $A$ be the portion of the square root already calculated.
- Let $b$ be the next single digit of the square root we wish to determine.
- The value of $A$ shifted into the current place value has square contribution $100A^2$.
- Subtracting $100A^2$ from the current dividend leaves a remainder $R$:
  $$R = (20A + b)b$$
- Therefore, to find the largest valid digit $b$:
  - Double the current root quotient $A$ to form $2A$.
  - Place $2A$ in the tens position ($20A$).
  - Find the largest digit $b$ such that $(20A + b) \cdot b \le R$.

---

## 2. Formal Proof of the Period Grouping Rule

### Theorem (Base-10 Digit Pairing)
If a number $N$ is grouped into $k$ periods of 2 digits each starting from the units place (or decimal point), its square root $\sqrt{N}$ contains exactly $k$ digits before the decimal point.

### Rigorous Algebraic Proof

- Consider an integer $N$ having $2k-1$ or $2k$ decimal digits.
- Bound $N$ between two consecutive powers of 10:
  $$10^{2k-2} \le N < 10^{2k}$$
- Taking square roots across the inequality:
  $$\sqrt{10^{2k-2}} \le \sqrt{N} < \sqrt{10^{2k}}$$
  $$10^{k-1} \le \sqrt{N} < 10^k$$
- Any real number strictly bounded between $10^{k-1}$ and $10^k$ has exactly $k$ integer digits in base 10.
- Hence, each 2-digit period in $N$ corresponds strictly to 1 decimal digit in $\sqrt{N}$.

---

## 3. Directional Grouping Rule (Integer vs Decimal)

### Integer Part (Right to Left $\leftarrow$)
- Group digits in pairs starting from the units digit moving left:
  $$\dots, \overline{d_5 d_4}, \overline{d_3 d_2}, \overline{d_1}$$
- **Reason**: Place values increase by factors of $100 = 10^2$. Grouping right-to-left ensures that the leftmost single digit (if odd number of total digits) correctly represents the highest power of 100.

### Decimal Part (Left to Right $\rightarrow$)
- Group digits in pairs starting immediately after the decimal point moving right:
  $$0.\overline{f_1 f_2}\,\, \overline{f_3 f_4}\,\, \overline{f_5 f_6}\dots$$
- **Reason**: Decimal place values decrease by factors of $\frac{1}{100} = 10^{-2}$. Padded zeroes must always be added to the **right** ($0.5 = 0.50$, NOT $0.05$) to preserve value while maintaining 2-digit periods.

---

## 4. Worked Example with Detailed Derivation

### Problem: Find $\sqrt{53824}$ using Long Division

#### Step 1: Period Pairing
- Group from right to left: $\overline{5}\,\,\overline{38}\,\,\overline{24}$.
- Total periods = $3 \implies \sqrt{53824}$ is a 3-digit integer.

#### Step 2: First Digit ($A_1 = 2$)
- Largest digit $b_1$ such that $b_1^2 \le 5$ is $2$ ($2^2 = 4 \le 5$).
- Remainder $R_1 = 5 - 4 = 1$.
- Bring down next period $\overline{38} \implies$ New dividend = $138$.

#### Step 3: Second Digit ($A_2 = 23$)
- Double current quotient $A_1 = 2 \implies 2 \times 2 = 4$.
- Trial divisor: $4b_2 \cdot b_2$.
- Find max $b_2$:
  - $43 \times 3 = 129 \le 138$
  - $44 \times 4 = 176 > 138$
- Choose $b_2 = 3$. New quotient digit = $3$.
- Remainder $R_2 = 138 - 129 = 9$.
- Bring down next period $\overline{24} \implies$ New dividend = $924$.

#### Step 4: Third Digit ($A_3 = 232$)
- Double current quotient $A_2 = 23 \implies 23 \times 2 = 46$.
- Trial divisor: $46b_3 \cdot b_3$.
- Find max $b_3$:
  - $462 \times 2 = 924 \le 924$
- Choose $b_3 = 2$. New quotient digit = $2$.
- Remainder $R_3 = 924 - 924 = 0$.

$$\sqrt{53824} = 232$$

---

## 5. Key Properties & Algorithm Rules

1. **Exact Digit Count**:
   - For an $n$-digit integer:
     - If $n$ is even, $\text{digits in } \sqrt{N} = \frac{n}{2}$.
     - If $n$ is odd, $\text{digits in } \sqrt{N} = \frac{n+1}{2}$.
2. **Remainder Bound**:
   - The remainder $R_k$ at any step after subtracting $(20A+b)b$ must be strictly less than $2A + 1$, where $A$ is the updated quotient.
3. **Decimal Precision Extension**:
   - Append pairs of zeroes (`00`) to the right of the decimal point to compute square roots of non-perfect squares to any required decimal place.

---

## Linked Notes

- [[cds/math/notes/roots|Topic Note: Square Roots & Cube Roots]]
- [[cds/math/notes/subtopics/roots_methods|Subtopic: Prime Factorization & Division Method]]
- [[cds/math/notes/questions/q5_1|Q1: Decimal Root Simplification]]
- [[cds/math/notes/questions/q5_2|Q2: Smallest 4-Digit Perfect Square]]
