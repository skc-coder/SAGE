---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Time and Work"
subtopic: "Men-Women Equivalence"
difficulty: "Medium"
tags: [cds, elementary-mathematics, time-and-work, subtopic]
---

# Men-Women Equivalence & Or-And Conversion Rule

## Mathematical Formulation

### 1. "OR" Condition Equivalence Rule
If $m$ men or $n$ women can complete a piece of work in $a$ days:
- 1 man's 1-day work:
  $$E_m = \frac{1}{m \cdot a}$$
- 1 woman's 1-day work:
  $$E_w = \frac{1}{n \cdot a}$$

Equating total work done in $a$ days:
$$m \text{ Men} = n \text{ Women} \implies 1 \text{ Man} = \frac{n}{m} \text{ Women}$$

#### Combined Time Formula for $x$ Men and $y$ Women
The total daily work rate of $x$ men and $y$ women is:
$$E_{x+y} = x \cdot E_m + y \cdot E_w = \frac{x}{m \cdot a} + \frac{y}{n \cdot a} = \frac{1}{a} \left( \frac{x}{m} + \frac{y}{n} \right)$$

Therefore, the time $D$ taken by $x$ men and $y$ women working together is:
$$D = \frac{1}{E_{x+y}} = \frac{a}{\frac{x}{m} + \frac{y}{n}} = \frac{m \cdot n \cdot a}{n \cdot x + m \cdot y}$$

---

### 2. "AND" System of Simultaneous Equations
If:
- Case 1: $a_1$ men and $b_1$ boys finish work in $d_1$ days
- Case 2: $a_2$ men and $b_2$ boys finish work in $d_2$ days

Let 1 man's 1-day work be $m$ and 1 boy's 1-day work be $b$.
$$d_1 (a_1 m + b_1 b) = d_2 (a_2 m + b_2 b) = 1 \text{ (Total Work)}$$

Rearranging to find the efficiency ratio $\frac{m}{b}$:
$$d_1 a_1 m + d_1 b_1 b = d_2 a_2 m + d_2 b_2 b$$
$$m (d_1 a_1 - d_2 a_2) = b (d_2 b_2 - d_1 b_1)$$
$$\frac{m}{b} = \frac{d_2 b_2 - d_1 b_1}{d_1 a_1 - d_2 a_2}$$

---

## Linked Practice Questions
- [[content/cds/math/notes/questions/q17|Q17: Men & Boys Equivalence System]]

---

## Navigation
- [[content/cds/math/notes/work|Time and Work Topic]]
- [[content/cds/math/math_overview|Subject Dashboard]]
