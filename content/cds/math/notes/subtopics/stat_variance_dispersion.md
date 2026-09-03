---
exam: "CDS"
subject: "Math"
topic: "Statistics"
subtopic: "Dispersion & Variance"
difficulty: "Hard"
tags: [cds, math, statistics, subtopic, variance, standard-deviation]
---

# Dispersion & Variance

## Theory & Formulas

Dispersion measures the extent to which numerical data tends to spread about an average value.

---

### 1. Mean Deviation ($MD$)
Mean deviation is the arithmetic mean of absolute deviations from a central measure (Mean or Median).

- **From Mean**:
  $$MD(\bar{x}) = \frac{\sum f_i |x_i - \bar{x}|}{\sum f_i}$$

- **Coefficient of Mean Deviation**:
  $$\text{Coeff of } MD = \frac{MD}{\bar{x}} \times 100\%$$

---

### 2. Variance ($\sigma^2$) & Standard Deviation ($\sigma$)

#### Population Variance ($\sigma^2$)
Variance is the mean of squared deviations from the arithmetic mean:
$$\sigma^2 = \frac{\sum_{i=1}^n (x_i - \bar{x})^2}{n} = \frac{\sum x_i^2}{n} - (\bar{x})^2$$

For grouped data:
$$\sigma^2 = \frac{\sum f_i (x_i - \bar{x})^2}{N} = \frac{\sum f_i x_i^2}{N} - (\bar{x})^2 \quad \text{where } N = \sum f_i$$

#### Standard Deviation ($\sigma$)
Standard deviation is the positive square root of variance:
$$\sigma = +\sqrt{\text{Variance}} = \sqrt{\sigma^2}$$

#### Properties of Variance & SD
1. **Origin Change (Shift)**: Adding/subtracting a constant $k$ to each observation leaves Variance and SD **unchanged**.
   $$\text{Var}(X + k) = \text{Var}(X)$$
2. **Scale Change (Multiplication)**: Multiplying each observation by constant $a$ scales SD by $|a|$ and Variance by $a^2$.
   $$\text{SD}(aX) = |a| \cdot \text{SD}(X), \quad \text{Var}(aX) = a^2 \text{Var}(X)$$

---

### 3. Coefficient of Variation ($CV$)
$CV$ measures relative dispersion independent of measurement units:
$$CV = \frac{\sigma}{\bar{x}} \times 100\%$$

- Series with smaller $CV$ is more **consistent** / stable.
- Series with larger $CV$ is more **variable** / scattered.

---

## Linked Practice Questions
- [[content/cds/math/notes/questions/q28_6|Question 28.6: Mean Deviation of Ungrouped Observations]]

---

## Navigation
- [[content/cds/math/notes/statistics|Statistics Topic Page]]
- [[content/cds/math/math_overview|Elementary Mathematics]]
