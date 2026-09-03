---
exam: "CDS"
subject: "Math"
topic: "HCF and LCM"
subtopic: "HCF Methods"
difficulty: "Medium"
status: "Correct"
importance: "Important"
tags: [cds, math, variation]
---

# Variation 8: HCF via Successive Quotients

In finding the HCF of two numbers by division method, the successive quotients from top to bottom are 1, 8, and 2. If the last divisor is 105, find the two numbers.

> [!faq]- View Solution
> Work backwards using Euclidean algorithm steps:
> 1. Last divisor $d_3 = 105$, quotient $q_3 = 2 \implies \text{Dividend } r_1 = 105 \times 2 + 0 = 210$.
> 2. Second divisor $d_2 = 210$, quotient $q_2 = 8 \implies \text{Dividend } B = 210 \times 8 + 105 = 1680 + 105 = 1785$.
> 3. First divisor $d_1 = 1785$, quotient $q_1 = 1 \implies \text{Dividend } A = 1785 \times 1 + 210 = 1995$.
> 
> Thus, the two numbers are **1785 and 1995**.

## Navigation
- [[cds/math/notes/subtopics/hcf_methods|Subtopic: HCF Methods]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
