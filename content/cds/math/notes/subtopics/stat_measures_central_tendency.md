---
exam: "CDS"
subject: "Math"
topic: "Statistics"
subtopic: "Measures of Central Tendency"
difficulty: "Easy"
tags: [cds, math, statistics, subtopic, mean]
---

# Measures of Central Tendency

## Theory & Conceptual Foundations

A measure of central tendency is a single summary value that represents the central point or typical value of a probability distribution or dataset.

### 1. Arithmetic Mean ($\bar{x}$)
For raw data $x_1, x_2, \dots, x_n$:
$$\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i$$

For grouped data with frequencies $f_i$ and class marks $x_i$:
$$\bar{x} = \frac{\sum f_i x_i}{\sum f_i}$$

#### Linear Shift Transformation
If each observation $x_i$ is transformed to $y_i = a x_i + b$:
$$\bar{y} = a \bar{x} + b$$

- Adding/subtracting $c$ shifts mean by $\pm c$.
- Multiplying/dividing by $k$ scales mean by $\times/\div k$.

#### Sum of Deviations
The algebraic sum of deviations of observations from their arithmetic mean is always zero:
$$\sum_{i=1}^n (x_i - \bar{x}) = 0$$

---

### 2. Weighted & Combined Arithmetic Mean

#### Weighted Arithmetic Mean ($\bar{x}_w$)
When observations $x_i$ carry unequal importance represented by weights $w_i$:
$$\bar{x}_w = \frac{\sum_{i=1}^n w_i x_i}{\sum_{i=1}^n w_i}$$

#### Combined Mean of Two Groups ($\bar{x}_{12}$)
If group 1 has $n_1$ observations with mean $\bar{x}_1$ and group 2 has $n_2$ observations with mean $\bar{x}_2$:
$$\bar{x}_{12} = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2}{n_1 + n_2}$$

---

## Linked Practice Questions
- [[content/cds/math/notes/questions/q28_1|Question 28.1: Combined Mean of Pass and Fail Students]]
- [[content/cds/math/notes/questions/q28_2|Question 28.2: Weighted Arithmetic Mean of First n Natural Numbers]]

---

## Navigation
- [[content/cds/math/notes/statistics|Statistics Topic Page]]
- [[content/cds/math/math_overview|Elementary Mathematics]]
