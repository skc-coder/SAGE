---
exam: "CDS"
subject: "Math"
topic: "Statistics"
subtopic: "Graphical Representation & Ogive Median"
difficulty: "Medium"
tags: [cds, math, statistics, subtopic, ogive, pie-chart, histogram]
---

# Graphical Representation & Ogive Median

## Theory & Visual Techniques

Visual representation facilitates quick comparison and structural insight into large datasets.

---

### 1. Histogram & Area Equivalence
- **Histogram**: Continuous adjacent rectangles where:
  $$\text{Base} = \text{Class Interval Size } (h), \quad \text{Height} = \text{Frequency } (f_i)$$
- **Total Area of Histogram**:
  $$\text{Total Area} = \sum (\text{Base} \times \text{Height}) = h \sum f_i = N \cdot h$$
- For uneven class intervals, height is adjusted as **Frequency Density**:
  $$\text{Frequency Density} = \frac{\text{Frequency}}{\text{Class Width}}$$

---

### 2. Ogives (Cumulative Frequency Curves)

#### A. Less-Than Ogive (Rising Curve)
- Plot points $(\text{Upper Class Limit}, cf)$ and join with a smooth curve.
- Starts near 0 on the left and rises to $N = \sum f_i$.

#### B. More-Than Ogive (Falling Curve)
- Plot points $(\text{Lower Class Limit}, cf_{\text{more}})$ and join with a smooth curve.
- Starts at total frequency $N$ on the left and falls towards 0.

#### C. Graphical Median Determination Theorem
- **Theorem**: The $x$-coordinate of the point of intersection of the "Less-than Ogive" and "More-than Ogive" is strictly equal to the **Median** ($M_e$) of the distribution.
- Alternatively, locating $N/2$ on the $Y$-axis of a Less-than Ogive and projecting down to the $X$-axis gives the **Median**.

---

### 3. Pie Chart (Sector Angle Formula)
A circular graph where total area ($360^\circ$) is partitioned proportionally:

$$\text{Central Angle } \theta_i = \left( \frac{f_i}{\sum f_i} \right) \times 360^\circ = \left( \text{Percentage } p_i \right) \times 3.6^\circ$$

---

## Linked Practice Questions
- [[cds/math/notes/questions/q28_7|Question 28.7: Sector Central Angle and Expense Calculation]]

---

## Navigation
- [[cds/math/notes/statistics|Statistics Topic Page]]
- [[cds/math/math_overview|Elementary Mathematics]]
