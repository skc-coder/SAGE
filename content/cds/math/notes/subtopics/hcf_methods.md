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

---

## Linked Practice Questions

- [[cds/math/notes/questions/q5|Question 5: HCF of Large Differences]]
- [[cds/math/notes/questions/q6|Question 6: Co-Prime Pair Counting Given Sum & HCF]]

---

## Variations

- [[cds/math/notes/variations/var8|Variation 8: HCF via Successive Quotients]]
- [[cds/math/notes/variations/var9|Variation 9: Co-prime Pairs Given Product & HCF]]

---

## Navigation

- [[cds/math/notes/hcf_lcm|HCF and LCM Topic Page]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
