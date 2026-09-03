---
exam: "CDS"
subject: "Math"
topic: "Statistics"
subtopic: "Continuous Median & Mode"
difficulty: "Medium"
tags: [cds, math, statistics, subtopic, median, mode]
---

# Continuous Median & Mode Formulas

## Theory & Derivations

In grouped continuous frequency distributions, exact values of observations within class intervals are unknown. Median and Mode are evaluated via linear interpolation within their respective key intervals.

---

### 1. Continuous Median Formula

#### Identification of Median Class
1. Compute cumulative frequencies $cf$.
2. Find $N = \sum f_i$.
3. The **Median Class** is the first class interval whose cumulative frequency is greater than or equal to $N/2$.

#### Derivation / Interpolation Formula
$$M_e = l + \left( \frac{\frac{N}{2} - c}{f} \right) \cdot h$$
where:
- $l$: Lower limit of the median class.
- $N$: Total frequency ($\sum f_i$).
- $c$: Cumulative frequency of the class immediately preceding the median class.
- $f$: Frequency of the median class.
- $h$: Width of the median class interval.

---

### 2. Continuous Mode Formula

#### Identification of Modal Class
The **Modal Class** is the class interval having the maximum frequency ($f_1$).

#### Interpolation Formula
$$M_o = l + \left( \frac{f_1 - f_0}{2f_1 - f_0 - f_2} \right) \cdot h$$
where:
- $l$: Lower limit of the modal class.
- $f_1$: Frequency of the modal class.
- $f_0$: Frequency of the class immediately preceding the modal class.
- $f_2$: Frequency of the class immediately succeeding the modal class.
- $h$: Width of the modal class interval.

---

## Linked Practice Questions
- [[content/cds/math/notes/questions/q28_3|Question 28.3: Continuous Grouped Median Computation]]
- [[content/cds/math/notes/questions/q28_4|Question 28.4: Modal Class & Mode Evaluation]]

---

## Navigation
- [[content/cds/math/notes/statistics|Statistics Topic Page]]
- [[content/cds/math/math_overview|Elementary Mathematics]]
