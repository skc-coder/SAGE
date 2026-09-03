---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Percentage"
subtopic: "Asymmetric Comparison & Price-Consumption Balance"
difficulty: "Medium"
tags: [cds, math, percentage, subtopic, price-consumption]
---

# Asymmetric Comparison & Price-Consumption Balance

## Theory & Intuitive Proofs

### 1. Intuitive Proof of Asymmetric Comparison (The "Ruler/Base" Model)
A percentage is not an absolute quantity; it is always a **fraction of a specific base denominator**.

When we say **"$A$ is $x\%$ more than $B$"**, we are taking **$B$ as our reference ruler ($100$)**:
- $B = 100$
- $A = 100 + x$
- Absolute difference (gap): $\Delta = A - B = x$

When we flip the question to ask **"How much less is $B$ than $A$?"**, the absolute gap $\Delta = x$ remains identical, but our **reference ruler (denominator) switches from $B$ to $A$ ($100 + x$)**:
$$\text{Percentage Less} = \frac{\text{Absolute Gap }\Delta}{\text{New Base } A} \times 100 = \left(\frac{x}{100 + x} \times 100\right)\%$$

> [!TIP]
> **Denominator Scaling Principle**: Since $A$ ($100+x$) is larger than $B$ ($100$), dividing the same gap $x$ by a **larger denominator** yields a **smaller percentage**!
> 
> *Example*: If $A$ is $25\%$ more than $B$:
> - $B = 100$, $A = 125$. Gap $= 25$.
> - $B$ is less than $A$ by $\frac{25}{125} \times 100 = 20\%$.

---

### 2. Dual Case: "$A$ is $x\%$ LESS than $B$"
When **"$A$ is $x\%$ less than $B$"**:
- $B = 100$
- $A = 100 - x$
- Absolute difference (gap): $\Delta = B - A = x$

To find how much **more** $B$ is than $A$, the reference base switches to $A = 100 - x$:
$$\text{Percentage More} = \frac{\text{Absolute Gap }\Delta}{\text{New Base } A} \times 100 = \left(\frac{x}{100 - x} \times 100\right)\%$$

> [!TIP]
> **Denominator Scaling Principle**: Since $A$ ($100-x$) is smaller than $B$ ($100$), dividing the same gap $x$ by a **smaller denominator** yields a **larger percentage**!
> 
> *Example*: If $A$ is $20\%$ less than $B$:
> - $B = 100$, $A = 80$. Gap $= 20$.
> - $B$ is more than $A$ by $\frac{20}{80} \times 100 = 25\%$.

---

### 3. Proof & Intuition of Price-Consumption Expenditure Neutrality

#### 🛑 Physical Dimension Check: Never Swap Units Again!
If you ever get confused on whether Expenditure $= \text{Price} \times \text{Consumption}$ or something else, **just check the real-world units**:
- **Price ($P$)**: $\frac{\text{₹}}{\text{kg}}$ (Rupees *per* kilogram)
- **Consumption ($C$)**: $\text{kg}$ (Kilograms consumed)
- **Expenditure ($E$)**: $\text{₹}$ (Total Rupees spent out of wallet)

Multiply the units together:
$$\text{Price} \times \text{Consumption} = \left(\frac{\text{₹}}{\text{kg}}\right) \times (\text{kg}) = \text{₹} = \text{Expenditure}$$

> [!WARNING]
> **Why your inverted memory fails physically**:
> If you write $\text{Consumption} = \text{Price} \times \text{Expenditure}$:
> $$\left(\frac{\text{₹}}{\text{kg}}\right) \times (\text{₹}) = \frac{\text{₹}^2}{\text{kg}} \neq \text{kg} \quad \text{(Rupees-squared per kg makes no sense!)}$$

#### 🧠 The 5-Second Mental Model: "The See-Saw / Seesaw Scale"
Since $\text{Expenditure } (E) = \text{Price } (P) \times \text{Consumption } (C)$:

If **Price increases by factor $F$**, then to keep the area $E$ identical, **Consumption must be multiplied by $\frac{1}{F}$** (its reciprocal)!

1. **Price Multiplier $F$**:
   - Price increases by $x\% \implies F = \frac{100 + x}{100}$.
2. **Consumption Reciprocal Multiplier $\frac{1}{F}$**:
   - New Consumption $C' = C \times \frac{100}{100 + x}$.
3. **Consumption Reduction**:
   - Fraction of consumption reduced:
     $$1 - \frac{100}{100 + x} = \frac{(100 + x) - 100}{100 + x} = \frac{x}{100 + x}$$
   - Expressed as percentage reduction:
     $$\text{Percentage Reduction} = \left(\frac{x}{100 + x} \times 100\right)\%$$

> [!KEYWORD]
> **Why is Price-Consumption EXACTLY identical to Asymmetric Comparison?**
> Because **New Price $P'$** acts as the **New Base ($100+x$)**! The amount of money you need to cut out of your consumption is proportional to the **NEW higher price**, not the old price!

#### Step-by-Step Algebraic Derivation
$$\text{Expenditure } E = P \times C$$

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
