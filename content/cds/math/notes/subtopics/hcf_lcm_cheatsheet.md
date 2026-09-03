---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "HCF and LCM"
subtopic: "Cheatsheet & Key Theorems"
difficulty: "Medium"
tags: [cds, elementary-mathematics, hcf-lcm, cheatsheet, theorems]
---

# HCF & LCM — Core Theorems, Properties & Models

## 1. Fundamental Definitions & Canonical Prime Factorization
For canonical prime factorizations $A = p_1^{a_1} p_2^{a_2} \cdots p_k^{a_k}$ and $B = p_1^{b_1} p_2^{b_2} \cdots p_k^{b_k}$:
- **Highest Common Factor (HCF / GCD)**:
  $$\operatorname{HCF}(A, B) = p_1^{\min(a_1, b_1)} \cdot p_2^{\min(a_2, b_2)} \cdots p_k^{\min(a_k, b_k)}$$
- **Least Common Multiple (LCM)**:
  $$\operatorname{LCM}(A, B) = p_1^{\max(a_1, b_1)} \cdot p_2^{\max(a_2, b_2)} \cdots p_k^{\max(a_k, b_k)}$$

---

## 2. Fundamental Theorems & Properties
1. **Two-Number Product Identity**:
   $$\operatorname{HCF}(A, B) \times \operatorname{LCM}(A, B) = A \times B$$
   *(Strictly for 2 numbers only! Does NOT hold for 3 or more numbers).*
2. **Co-prime Factor Representation Model**:
   If $\operatorname{HCF}(A, B) = H$, then $A = H \cdot x$ and $B = H \cdot y$, where $\operatorname{GCD}(x, y) = 1$ (co-prime).
   - $\operatorname{LCM}(A, B) = L = H \cdot x \cdot y$.
   - Product of ratios: $x \cdot y = \frac{L}{H}$.
3. **Difference Divisibility Property**:
   $$\operatorname{HCF}(A, B) = \operatorname{HCF}(A - B, B) \quad (\text{for } A > B)$$
   *The HCF of any two numbers must divide their absolute difference $|A - B|$.*
4. **Euclidean Algorithm (Long Division)**:
   If $a = b \cdot q + r$, then $\operatorname{GCD}(a, b) = \operatorname{GCD}(b, r)$.  
   For 3 numbers: $\operatorname{HCF}(A, B, C) = \operatorname{HCF}\big(\operatorname{HCF}(A, B), C\big)$.
5. **Fraction HCF & LCM Formulas** (Fractions must be in lowest reduced form):
   $$\operatorname{HCF}\left(\frac{a}{b}, \frac{c}{d}\right) = \frac{\operatorname{HCF}(a, c)}{\operatorname{LCM}(b, d)}, \qquad \operatorname{LCM}\left(\frac{a}{b}, \frac{c}{d}\right) = \frac{\operatorname{LCM}(a, c)}{\operatorname{HCF}(b, d)}$$

---

## 3. Core HCF & LCM Remainder Models

| Model Type | Problem Condition | Required Form / Formula |
| :--- | :--- | :--- |
| **HCF Model 1** | Greatest number dividing $x, y, z$ leaving remainders $a, b, c$ | $N = \operatorname{HCF}(x - a, \, y - b, \, z - c)$ |
| **HCF Model 2** | Greatest number dividing $x, y, z$ leaving the **same unknown remainder $R$** | $N = \operatorname{HCF}(\|x - y\|, \, \|y - z\|, \, \|z - x\|)$ |
| **LCM Model 1** | Smallest number divided by $x, y, z$ leaving **constant remainder $R$** | $\text{Least } N = \operatorname{LCM}(x, y, z) + R$ |
| **LCM Model 2** | Smallest number divided by $x, y, z$ leaving remainders $a, b, c$ with **constant difference $p = x-a = y-b = z-c$** | $\text{Least } N = \operatorname{LCM}(x, y, z) - p$ |
| **LCM Model 3** | Smallest multiple of $M$ divided by $x, y, z$ leaving remainder $R$ | $N = k \cdot \operatorname{LCM}(x, y, z) + R$, solve for smallest integer $k$ such that $N \equiv 0 \pmod M$ |
| **LCM Model 4** | Bell Ringing & Circular Track Meeting Time | $\text{Simultaneous Meeting Time} = \operatorname{LCM}(t_1, t_2, \dots, t_k)$ |

---

## Navigation
- [[cds/math/notes/hcf_lcm|HCF and LCM Main Topic Note]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
