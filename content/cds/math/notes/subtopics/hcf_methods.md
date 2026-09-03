---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "HCF and LCM"
subtopic: "HCF Methods & Co-prime Pairs"
difficulty: "Easy"
tags: [cds, elementary-mathematics, hcf, subtopic]
---

# HCF Methods & Co-Prime Pair Counting

## Theory & Calculation Methods

### 1. Long Division Method (Euclidean Algorithm)
To find $\operatorname{HCF}(a, b)$ where $a > b$:
- Divide $a$ by $b$ to get quotient $q_1$ and remainder $r_1$.
- If $r_1 = 0$, then $\operatorname{HCF}(a, b) = b$.
- Otherwise, divide $b$ by $r_1$ to get remainder $r_2$.
- Continue successive division until remainder becomes $0$. The **last non-zero divisor** is the HCF.

#### Proof of Euclidean Algorithm:
If $a = b \cdot q + r$, then any common divisor of $a$ and $b$ must also divide $r = a - b \cdot q$.
Conversely, any common divisor of $b$ and $r$ must divide $a = b \cdot q + r$.
Hence, $\operatorname{GCD}(a, b) = \operatorname{GCD}(b, r)$.

### 2. Difference Property of HCF
For any set of positive integers, their HCF must divide the difference between any pair of them.
$$\operatorname{HCF}(a, b, c) \le \operatorname{HCF}(|a-b|, |b-c|, |c-a|)$$
> [!TIP]
> **Shortcut for Large Numbers**: Find the difference between closest numbers. The HCF is either that difference or a factor of that difference!

---

## Standard Problem Types & Solution Models

### Case 1: HCF of Numbers Leaving Same Remainder $R$ (Unspecified $R$)
- **Problem**: Find the largest number $N$ which divides $x, y, z$ leaving the *same remainder* $R$ in each case.
- **Formula**:
  $$N = \operatorname{HCF}(|x - y|, |y - z|, |z - x|)$$
- **Intuition**: Since $x = N q_1 + R$, $y = N q_2 + R$, and $z = N q_3 + R$, subtracting eliminates $R$:
  $$x - y = N(q_1 - q_2), \quad y - z = N(q_2 - q_3)$$
  Thus $N$ is the HCF of the pairwise differences!

### Case 2: HCF of Numbers Leaving Specified Remainders $a, b, c$
- **Problem**: Find the largest number $N$ which divides $x, y, z$ leaving remainders $a, b, c$ respectively.
- **Formula**:
  $$N = \operatorname{HCF}(x - a, \, y - b, \, z - c)$$

---

## Linked Practice Questions

- [[cds/math/notes/questions#question-5-hcf-of-large-differences|Question 5: HCF of Numbers Leaving Same Remainder]]
- [[cds/math/notes/questions#question-6-co-prime-pair-counting-given-sum-hcf|Question 6: Co-Prime Pair Counting Given Sum & HCF]]

---

## Variations

- [[cds/math/notes/variations/vars#variation-8-hcf-via-successive-quotients|Variation 8: Long Division Successive Quotients]]
- [[cds/math/notes/variations/vars#variation-9-coprime-pairs-given-product-and-hcf|Variation 9: Co-prime Pairs Given Product & HCF]]

---

## Navigation

- [[cds/math/notes/hcf_lcm|HCF and LCM Topic Page]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
