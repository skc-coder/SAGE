---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Percentage"
subtopic: "Asymmetric Comparison & Price-Consumption Balance"
difficulty: "Medium"
tags: [cds, math, percentage, subtopic, price-consumption]
---

# Asymmetric Comparison & Price-Consumption Balance

## Theory & Proofs

### 1. Proof of Asymmetric Comparison Formula
Suppose quantity $A$ is $x\%$ more than quantity $B$.
- Let $B = 100$.
- Then $A = 100 + x$.
- The absolute difference between $A$ and $B$ is $x$.
- To express how much less $B$ is than $A$, we use $A$ as the reference denominator:
  $$\text{Percentage Less} = \frac{A - B}{A} \times 100 = \left(\frac{x}{100 + x} \times 100\right)\%$$

Similarly, if $A$ is $x\%$ less than $B$:
- $B = 100 \implies A = 100 - x$.
- Reference base $A = 100 - x$.
- Percentage more of $B$ over $A$:
  $$\text{Percentage More} = \left(\frac{x}{100 - x} \times 100\right)\%$$

### 2. Proof of Price-Consumption Expenditure Neutrality
Expenditure is given by:
$$\text{Expenditure } E = \text{Price } P \times \text{Consumption } C$$
If price increases by $x\%$, new price $P' = P \left(1 + \frac{x}{100}\right) = P \cdot \frac{100+x}{100}$.
To keep expenditure $E$ constant:
$$P' \times C' = E = P \times C$$
$$P \left(\frac{100+x}{100}\right) C' = P \cdot C \implies C' = C \left(\frac{100}{100+x}\right)$$
The reduction in consumption is:
$$\Delta C = C - C' = C \left(1 - \frac{100}{100+x}\right) = C \left(\frac{x}{100+x}\right)$$
Expressing this reduction as a percentage of original consumption $C$:
$$\text{Percentage Reduction} = \left(\frac{x}{100+x} \times 100\right)\%$$

---

## Linked Practice Questions

- [[cds/math/notes/questions/q149|Q149: Asymmetric Salary Comparison]]
- [[cds/math/notes/questions/q150|Q150: Cooking Gas Price Increase and Consumption Reduction]]

---

## Variations

- [[cds/math/notes/variations/var29|Price Increase with Expenditure-Consumption Compensation]]
