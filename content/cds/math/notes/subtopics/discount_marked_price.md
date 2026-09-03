---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Profit and Loss"
subtopic: "Marked Price, Discount and Markup"
difficulty: "Medium"
tags: [cds, elementary-mathematics, profit-and-loss, subtopic]
---

# Marked Price, Discount and Markup

## Theory & Mathematical Formulation

### 1. Key Invariants

1. **Marked Price ($\text{MP}$)**:
   - The list price printed on the label/catalog.
   - **Discount is ALWAYS calculated on Marked Price ($\text{MP}$)**:
     $$\text{Discount} = \text{MP} - \text{SP}$$
     $$\text{Discount } \% = \left( \frac{\text{MP} - \text{SP}}{\text{MP}} \right) \times 100\%$$

2. **Selling Price Formula**:
   $$\text{SP} = \text{MP} \times \left( 1 - \frac{d}{100} \right)$$

3. **Markup Percentage ($m\%$)**:
   - The percentage by which the trader raises the price above cost price:
     $$\text{MP} = \text{CP} \times \left( 1 + \frac{m}{100} \right)$$

4. **Net Profit with Markup $m\%$ and Discount $d\%$**:
   - $\text{SP} = \text{CP} \left(1 + \frac{m}{100}\right)\left(1 - \frac{d}{100}\right)$
   - Net Profit $\%$:
     $$\text{Net Profit } \% = m - d - \frac{m \cdot d}{100}$$

5. **Direct Relation between $\text{MP}$ and $\text{CP}$ for Target Profit $p\%$ after Discount $d\%$**:
   $$\frac{\text{MP}}{\text{CP}} = \frac{100 + p}{100 - d}$$

### 2. Successive Discount Series

- For successive discounts $d_1\%, d_2\%, d_3\%$:
  $$\text{SP} = \text{MP} \times \left(1 - \frac{d_1}{100}\right) \times \left(1 - \frac{d_2}{100}\right) \times \left(1 - \frac{d_3}{100}\right)$$
- **Equivalent Single Discount ($D_{\text{eq}}\%$)**:
  $$D_{\text{eq}}\% = \left[ 1 - \left(1 - \frac{d_1}{100}\right)\left(1 - \frac{d_2}{100}\right)\left(1 - \frac{d_3}{100}\right) \right] \times 100\%$$

---

## Linked Practice Questions
- [[cds/math/notes/questions/q11_8|Q11.8: Target Profit Markup and Discount Relation]]
- [[cds/math/notes/questions/q11_9|Q11.9: Equivalent Single Discount Series Calculation]]

---

## Navigation
- [[cds/math/notes/profit_loss|Profit & Loss Topic Note]]
- [[cds/math/math_overview|Subject Dashboard]]
