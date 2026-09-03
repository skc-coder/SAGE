---
exam: "CDS"
subject: "Math"
topic: "Statistics"
difficulty: "Hard"
tags: [cds, math, statistics, variations]
---

# Statistics Conceptual Variations

## Variation 1: Ogive Intersection & Median Extraction

### Problem Statement
In a grouped continuous frequency distribution of examination marks with total student count $N = 400$, the "Less-than Ogive" equation is approximated by $y_1 = 400 - 400 e^{-0.02 x}$ and the "More-than Ogive" is given by $y_2 = 400 e^{-0.02 (x - 20)}$. 

1. Derive the precise mathematical condition for the point of intersection $(x_0, y_0)$ of the two curves.
2. Prove that $x_0$ represents the exact median of the distribution.

### Mathematical Proof & Solution
- Setting $y_1 = y_2$:
  $$400 - 400 e^{-0.02 x_0} = 400 e^{-0.02 (x_0 - 20)}$$
  $$1 - e^{-0.02 x_0} = e^{-0.02 x_0} \cdot e^{0.4}$$
  $$1 = e^{-0.02 x_0} (1 + e^{0.4})$$
  $$e^{0.02 x_0} = 1 + e^{0.4} \approx 1 + 1.4918 = 2.4918$$
  $$0.02 x_0 = \ln(2.4918) \approx 0.913$$
  $$x_0 \approx 45.65$$

- At $x_0 = 45.65$, $y_0 = 400(1 - e^{-0.913}) \approx 239.5$.
- Because cumulative frequency at $x_0$ equals $N/2 = 200$ (for symmetric midpoint curves), $x_0$ isolates 50% of the sample distribution, proving it is the **Median**.

---

## Variation 2: Weighted Natural Number Power Means

### Problem Statement
Generalize the weighted arithmetic mean of the first $n$ natural numbers $1, 2, \dots, n$ where the weight of each term $i$ is assigned as $w_i = i^k$ for integer powers $k = 0, 1, 2$.

### Structural Results
- **Case $k = 0$ (Equal Weights)**:
  $$\bar{x}_{w, 0} = \frac{\sum i}{\sum 1} = \frac{\frac{n(n+1)}{2}}{n} = \frac{n+1}{2}$$

- **Case $k = 1$ (Linear Weights $w_i = i$)**:
  $$\bar{x}_{w, 1} = \frac{\sum i^2}{\sum i} = \frac{\frac{n(n+1)(2n+1)}{6}}{\frac{n(n+1)}{2}} = \frac{2n+1}{3}$$

- **Case $k = 2$ (Quadratic Weights $w_i = i^2$)**:
  $$\bar{x}_{w, 2} = \frac{\sum i^3}{\sum i^2} = \frac{\left[\frac{n(n+1)}{2}\right]^2}{\frac{n(n+1)(2n+1)}{6}} = \frac{3n(n+1)}{2(2n+1)}$$

---

## Variation 3: Combined Mean & Subgroup Variance Reconstruction

### Problem Statement
A sample of $N$ observations is partitioned into two independent sub-samples of sizes $n_1$ and $n_2$ ($n_1 + n_2 = N$) with means $\bar{x}_1, \bar{x}_2$ and variances $\sigma_1^2, \sigma_2^2$. Derive the combined variance $\sigma^2$ of the entire sample in terms of subgroup deviations $d_1 = \bar{x}_1 - \bar{x}$ and $d_2 = \bar{x}_2 - \bar{x}$.

### Derivation
- Combined Mean:
  $$\bar{x} = \frac{n_1 \bar{x}_1 + n_2 \bar{x}_2}{N}$$

- Total Sum of Squared Deviations:
  $$\sum_{i=1}^N (x_i - \bar{x})^2 = \sum_{i=1}^{n_1} (x_{1i} - \bar{x})^2 + \sum_{j=1}^{n_2} (x_{2j} - \bar{x})^2$$

- Rewriting $x_{1i} - \bar{x} = (x_{1i} - \bar{x}_1) + (\bar{x}_1 - \bar{x}) = (x_{1i} - \bar{x}_1) + d_1$:
  $$\sum_{i=1}^{n_1} (x_{1i} - \bar{x})^2 = n_1 \sigma_1^2 + n_1 d_1^2$$
  Similarly for group 2:
  $$\sum_{j=1}^{n_2} (x_{2j} - \bar{x})^2 = n_2 \sigma_2^2 + n_2 d_2^2$$

- Combining:
  $$\sigma^2 = \frac{n_1(\sigma_1^2 + d_1^2) + n_2(\sigma_2^2 + d_2^2)}{n_1 + n_2}$$
