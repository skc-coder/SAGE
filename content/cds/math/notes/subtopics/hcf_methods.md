---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "HCF and LCM"
subtopic: "HCF Methods & Co-prime Pairs"
difficulty: "Easy"
tags: [cds, elementary-mathematics, hcf, subtopic]
---

# HCF Models & Co-Prime Pair Counting

## Theory & Calculation Methods

### 1. Long Division Method (Euclidean Algorithm)
To find $\operatorname{HCF}(a, b)$ where $a > b$:
1. Divide the larger number ($a$) by the smaller number ($b$) to get remainder $r_1$.
2. Divide the previous divisor ($b$) by the remainder ($r_1$) to get remainder $r_2$.
3. Repeat this process: **Divide the previous divisor by the new remainder**.
4. Stop when the remainder becomes $0$. The **last divisor used** is the HCF of the two numbers.

#### Extension to 3 Numbers:
To find $\operatorname{HCF}(A, B, C)$:
$$\operatorname{HCF}(A, B, C) = \operatorname{HCF}\Big(\operatorname{HCF}(A, B), C\Big)$$
- **Step 1**: Find $H_1 = \operatorname{HCF}(A, B)$ using division method.
- **Step 2**: Find $\operatorname{HCF}(H_1, C)$ using division method. The resulting final divisor is the HCF of all 3 numbers.

#### Proof of Euclidean Algorithm:
If $a = b \cdot q + r$, then any common divisor of $a$ and $b$ must also divide $r = a - b \cdot q$.
Conversely, any common divisor of $b$ and $r$ must divide $a = b \cdot q + r$.
Hence, $\operatorname{GCD}(a, b) = \operatorname{GCD}(b, r)$.

### 3. Core HCF Remainder Rules & Theorems


#### Rule 2: Greatest Divisor Leaving Specified Remainders $(a, b, c)$
The greatest number that divides $x, y, z$ leaving remainders $a, b, c$ respectively is:
$$\mathbf{\operatorname{HCF}(x - a, \, y - b, \, z - c)}$$

#### Rule 3: Greatest Divisor Leaving Same Remainder $R$ (Unknown)
The greatest number that divides $x, y, z$ leaving the *same* remainder in each case is:
$$\mathbf{\operatorname{HCF}(|x - y|, \, |y - z|, \, |z - x|)}$$
Another way of saying that find the GCD of ^^^^^
Because if two numbers have same remainders when divided by a number then their difference is evenly divided by that number.

## Linked Practice Questions

- [[cds/math/notes/questions/q5|Question 5: HCF of Large Differences]]
- [[cds/math/notes/questions/q6|Question 6: Co-Prime Pair Counting Given Sum & HCF]]
- [[cds/math/notes/questions/q16|Question 16: HCF of 3 Numbers via Long Division (204, 1190, 1445)]]
- [[cds/math/notes/questions/q17|Question 17: Greatest Number Leaving Different Remainders (CDS 2014 I)]]
- [[cds/math/notes/questions/q18|Question 18: HCF of (a + b) and (a - b) for Co-prime (a, b) (CDS 2014 I)]]
- [[cds/math/notes/questions/q20|Question 20: Greatest Common Divisor with Same Remainder 17 (CDS 2012 II)]]
- [[cds/math/notes/questions/q21|Question 21: Measuring Vessel Maximum Capacity (Drums Problem)]]
- [[cds/math/notes/questions/q23|Question 23: Algebraic Factor HCF (a^2 b^4 + 2a^2 b^2 and (ab)^7 - 4a^2 b^9)]]
- [[cds/math/notes/questions/q24|Question 24: HCF of Linear Expressions m = 2n + 1 and k = 9n + 4]]
- [[cds/math/notes/questions/q25|Question 25: Number of Possible Pair Sets Given Product & HCF (CDS 2014 II)]]
- [[cds/math/notes/questions/q27|Question 27: Homogeneity Property HCF(a/c, b/c) for HCF(a,b) = c]]
- [[cds/math/notes/questions/q28|Question 28: Algebraic Identities of HCF & LCM (CDS 2016 I)]]

---

## Variations

- [[cds/math/notes/variations/var8|Variation 8: HCF via Successive Quotients]]
- [[cds/math/notes/variations/var9|Variation 9: Co-prime Pairs Given Product & HCF]]

---

## Navigation

- [[cds/math/notes/hcf_lcm|HCF and LCM Topic Page]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
