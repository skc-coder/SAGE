---
source: https://youtu.be/z1c0YlmFyFI?t=6515
tags:
---

📝 [[Problems - Averages]]

---
## Averages

### Fundamental Principle
**Net deficit below avg = Net surplus above avg**

Visualization:
$$12 \to +3 \to 15$$
$$13 \to +2 \to 15$$
$$17 \to -2 \to 15$$
$$18 \to -3 \to 15$$
$$\text{Sum deviations} = 0$$

### Inclusion Changes Average
When a new number is added and avg increases by $\Delta$:
- The increase $\Delta$ is "distributed" across all old numbers
- New number = old avg + $\Delta \times (\text{old count} + 1)$

**Example:** Avg of 4 numbers is 15. Add 5th number → avg becomes 16.
- Increase = 1 per number × 4 old numbers = 4
- 5th number = $15 + 1 \times 5 = 20$ ✓

This formula also works for decrease in average as well. Use $-Delta$
### Exclusion changes Average
If average **increases** by $\Delta$:
$$ x = \text{Old Avg} - \Delta(n-1) $$
If average **decreases** by $\Delta$ (use $\Delta$ as positive value):
$$ x = \text{Old Avg} + \Delta(n-1) $$
---
### Core Method — Deviation

**Don't sum. Assume, deviate, correct.**

**Steps:**
1. Assume any value $A$ as average
2. Find deviation of each from $A$: $d_i = \text{number} - A$
3. Total deviation: $\sum d_i$
4. Actual avg: $A + \frac{\sum d_i}{n}$

**If $\sum d_i = 0$, then $A$ is the answer.**

**Example:** Avg of 4552, 4548, 4550
- Assume $A = 4550$
- Deviations: $+2, -2, 0$ → sum = 0
- Average = **4550** ✓
---

## Grouped Data

When data comes as groups (each with its own average):

- Use **ratio of group sizes** instead of raw counts
- Apply deviation method on group averages

**Example:** 5 students avg 40 kg, 3 students avg 52 kg, 2 students avg 48 kg

Ratio = 5 : 3 : 2. Assume $A = 40$:

$$\text{Total deviation} = (0)(5) + (12)(3) + (8)(2) = 0 + 36 + 16 = 52$$

$$\text{Correction} = \frac{52}{10} = 5.2 \implies \text{Avg} = 45.2$$

---

## Key Property

> If you add/subtract/multiply a constant $k$ to **all** values, the average shifts by the same $k$.

$$\text{new avg} = \text{old avg} \pm k \quad \text{(add/subtract)}$$ $$\text{new avg} = \text{old avg} \times k \quad \text{(multiply)}$$
---
### Time & Averages
If avg age today = $x$ years, then:
- After $n$ years: avg age = $x + n$
- $n$ years ago: avg age = $x - n$

(Each person ages by $n$ years, so avg ages by $n$)

## Finding a Missing Value (Reverse)

Given overall average and all values except one:

**Trazū (Balance) Rule:** Total deviation from the given average = 0

$$\sum \text{deviations} = 0 \implies x = \text{avg} + (\text{net deficit})$$

**Example:** 4 scores: 78, 85, 69, 90, avg of all 5 = 80. Find 5th.

- Deviations from 80: $-2,\ +5,\ -11,\ +10$ → net = $+2$
- 5th score must give $-2$ → $x = 80 - 2 = \mathbf{78}$

---

## Consecutive Number Averages
## Average & Sum Formulas
[[common series]]

---

## Inclusion / Exclusion / Replacement

#### Universal Formula
$$\Delta \text{ avg} = \frac{\text{Sum of changes}}{\text{Total count}}$$

#### Rules by Case

**Inclusion (add numbers):**
- $\Delta = +\frac{\text{new number} - \text{old avg}}{\text{count}}$

**Exclusion (remove numbers):**
- $\Delta = -\frac{\text{removed number} - \text{old avg}}{\text{count}}$

**Replacement (remove old, add new):**
- $\Delta = \frac{\text{new} - \text{old}}{\text{count}}$

**Multiple changes (mix of add/remove/replace):**
- $\Delta = \frac{\sum(\text{inclusion delta}) - \sum(\text{exclusion delta}) + \sum(\text{all replacemnts})}{\text{total count}}$

---

## Middle Value 
Find deviations. Their net sum shall equal 0.
Nullify multiple removal of data by adding them again.

**Example:** 15 results, avg = 21. First 7 avg = 21, last 7 avg = 20. Find 8th.

- Last 7 deficit from 21: $-1 \times 7 = -7$
- 8th must compensate: $+7$
- 8th result $= 21 + 7 = \mathbf{28}$

---

📝 [[Problems - Averages]]