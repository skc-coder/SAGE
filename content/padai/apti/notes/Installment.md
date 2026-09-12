### The Foundation

Money has a **time value**. ₹100 today is not the same as ₹100 one year from now, because money kept today earns interest over time.

For example, at 10% interest:

- ₹100 today becomes ₹110 after 1 year
- ₹110 after 1 year becomes ₹121 after 2 years

This means ₹100 today and ₹110 after 1 year are **equivalent amounts** — just observed at different points in time.

---

### The Timeline

Every installment problem lives on a timeline:

```
TODAY -------(Year 1)-------(Year 2)-------(Year 3)
  P            X               X               X
```

- **P** = Principal (borrowed today)
- **X** = Each installment (paid at end of each year)

---

### Two Directions of Calculation

**Moving Forward (Future Value)** Multiply by the interest factor. This represents money growing over time.

At 10% rate, the factor per year is **1.1**

```
₹100  ──×1.1──►  ₹110  ──×1.1──►  ₹121
```

**Moving Backward (Present Value)** Divide by the interest factor. This represents bringing future money back to today.

```
₹100  ◄──÷1.1──  ₹110  ◄──÷1.1──  ₹121
```

---

### The Two Core Rules

These two rules solve every installment problem:

**Rule 1** $$\text{Sum of Present Values of all installments} = \text{Principal}$$

**Rule 2** $$\text{Sum of Future Values of all installments} = \text{Amount}$$

The logic behind Rule 1 is straightforward — whatever installments you pay in the future, their equivalent worth today must equal what you originally borrowed.

The logic behind Rule 2 — whatever installments you pay, their equivalent worth at the end of the loan period must equal the total amount owed (Principal + Interest).

---

### When to Use Which Rule

|What is given in the question|What is asked|Rule to apply|
|---|---|---|
|Principal (sum borrowed)|Installment value|Rule 1 — Present Value|
|Amount (sum due after N years)|Installment value|Rule 2 — Future Value|
|Installment value|Principal|Rule 1 — Present Value|

**Critical distinction:** If the question says "sum borrowed" → it is Principal. If it says "sum due in N years" → it is Amount. Reading this carefully eliminates most errors.

---

### Interest Factor Reference

|Rate|Simple Interest Factor (per year)|Compound Interest Factor (per year)|
|---|---|---|
|5%|+0.05 each year → 1.05, 1.10, 1.15...|×1.05 each year → 1.05, 1.05², 1.05³...|
|10%|1.10, 1.20, 1.30...|1.10, 1.10², 1.10³...|
|20%|1.20, 1.40, 1.60...|1.20, 1.20², 1.20³...|

The key difference: Simple Interest adds linearly. Compound Interest multiplies successively.

---

### Solved Example

**Question:** ₹6620 borrowed at 10% compound interest. Repaid in 3 equal annual installments. Find each installment.

**Step 1:** "Borrowed" means Principal is given → use Rule 1 (Present Value method)

**Step 2:** Write the equation

$$6620 = \frac{X}{1.1} + \frac{X}{1.1^2} + \frac{X}{1.1^3}$$

**Step 3:** Alternatively, use Rule 2 (Future Value — same answer)

$$6620 \times 1.1^3 = X \times 1.1^2 + X \times 1.1 + X$$

$$6620 \times 1.331 = X(1.21 + 1.10 + 1)$$

$$8811.32 = 3.31X$$

$$X = \frac{8811.32}{3.31} = \textbf{₹2662}$$

---

This is the complete concept. Every installment question, regardless of complexity, reduces to one of these two rules applied correctly.