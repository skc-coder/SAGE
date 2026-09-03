---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "HCF and LCM"
subtopic: "LCM Models & Remainder Theorems"
difficulty: "Medium"
tags: [cds, elementary-mathematics, lcm, remainders, subtopic]
---

# LCM Models & Remainder Theorems

## Core Remainder Models for Divided Numbers

When a required number $N$ is divided by $x, y, z$:

---

### Model 1: Constant Remainder Case (Same Remainder $R$)
- **Problem Formulation**: Find the least number $N$ which when divided by $x, y,$ and $z$ leaves the **same remainder $R$** in each case.
- **Formula**:
  $$\text{Least } N = \operatorname{LCM}(x, y, z) + R$$
- **General Form** (for $k^{\text{th}}$ terms or range constraints):
  $$N = k \cdot \operatorname{LCM}(x, y, z) + R \quad (k \in \mathbb{Z}^+)$$
- **Intuition**: $N - R$ is a multiple of $x, y,$ and $z$, so $N - R$ must be a multiple of $\operatorname{LCM}(x, y, z)$.

---

### Model 2: Constant Difference Case (Variable Remainders $a, b, c$)
- **Problem Formulation**: Find the least number $N$ which when divided by $x, y,$ and $z$ leaves remainders $a, b,$ and $c$ respectively, where:
  $$(x - a) = (y - b) = (z - c) = p \quad (\text{Constant Difference } p)$$
- **Formula**:
  $$\text{Least } N = \operatorname{LCM}(x, y, z) - p$$
- **General Form**:
  $$N = k \cdot \operatorname{LCM}(x, y, z) - p \quad (k \in \mathbb{Z}^+)$$
- **Intuition**: $N + p$ is simultaneously divisible by $x, y,$ and $z$ because adding $p$ to remainder $a$ gives $a + (x - a) = x$, completing a full group. Therefore, $N + p$ is a multiple of $\operatorname{LCM}(x, y, z)$.

---

### Model 3: Divisibility Condition on Remainder Model ($N \pmod M \equiv 0$)
- **Problem Formulation**: Find the least number $N$ which when divided by $x, y, z$ leaves remainder $R$, but $N$ is **exactly divisible by $M$**.
- **Formula & Method**:
  1. Express $N$ in parameterized general form:
     $$N = k \cdot \operatorname{LCM}(x, y, z) + R$$
  2. Reduce the coefficient of $k$ modulo $M$:
     $$N = k \cdot [q \cdot M + r_{\text{LCM}}] + R \equiv k \cdot r_{\text{LCM}} + R \pmod M$$
  3. Find the smallest positive integer $k \in \{1, 2, 3, \dots\}$ such that:
     $$(k \cdot r_{\text{LCM}} + R) \equiv 0 \pmod M$$
  4. Substitute that minimal $k$ back into $N = k \cdot \operatorname{LCM}(x, y, z) + R$.

---

### Model 4: Bell Ringing / Circular Track Race Concurrency
- **Problem Formulation**: Bells ring at intervals $t_1, t_2, t_3$ seconds. If they toll together now, when will they toll together next?
- **Formula**:
  $$\text{Time Interval} = \operatorname{LCM}(t_1, t_2, t_3)$$
- **Number of simultaneous tolls in total time $T$**:
  $$\text{Count} = \left\lfloor \frac{T}{\operatorname{LCM}(t_1, t_2, t_3)} \right\rfloor + 1 \quad (\text{including initial simultaneous toll at } t=0)$$

---

## Linked Practice Questions

- [[cds/math/notes/questions#question-7-lcm-constant-difference|Question 7: Least Number Leaving Variable Remainders (Constant Diff)]]
- [[cds/math/notes/questions#question-8-bell-ringing-concurrency-interval|Question 8: Bell Ringing Concurrency Interval]]
- [[cds/math/notes/questions#question-9-example-3-constant-difference-42-72-84|Question 9 (Example 3): Pathfinder Constant Difference (42, 72, 84)]]
- [[cds/math/notes/questions#question-10-example-4-lcm-with-perfect-divisibility-condition|Question 10 (Example 4): Pathfinder LCM with Divisibility Condition]]

---

## Variations

- [[cds/math/notes/variations/vars#variation-10-lcm-range-bound-four-digit-number|Variation 10: Largest 4-Digit Number with Constant Remainder]]
- [[cds/math/notes/variations/vars#variation-11-lcm-constant-difference-four-digit-number|Variation 11: Smallest 4-Digit Number with Constant Difference]]

---

## Navigation

- [[cds/math/notes/hcf_lcm|HCF and LCM Topic Page]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
