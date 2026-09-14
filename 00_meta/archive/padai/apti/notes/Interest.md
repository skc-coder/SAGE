---
source: https://www.youtube.com/watch?v=hOO4teNGkUA&list=PL3JmT-xgOMNxGdXaRXitX0kadTVEIFZ3n&index=8
tags:
problems: "[[Problems - Interest]]"
---
# Interest
Interest is the extra money you earn/give on top of principal amount.

The man who lends money is the Creditor and the man
who borrows money is the Debtor.
# Simple Interest (SI)
If we say “the rate of interest per annum is r%”, we mean that ` r is the interest on a principal of 100 for 1 year.

> Simple Interest = interest that **stays the same every year**

Total interest = SI = interest of 1st year $\times$ number of years $= P \times \text{rate (fraction)} \times \text{time} = P \times \frac{R}{100} \times T = \frac{PRT}{100}$.

> **Amount** $= P + SI$ (principal is always 100%)

### Trick 1 — Multi-year SI

Don't use the formula. Find the overall interset rate ($=rate*time$) and then use that on P.

$$\text{Total SI} = R \times T \text{ (as \%)} \quad \text{applied on } P$$

**Example:** $P = 4000$, $R = 15\%$, $T = 5$ yr

$$\text{SI} = 15 \times 5 = 75\% \text{ of } 4000 = 3000$$

---

### Trick 2 — Money doubles

If money doubles in $T$ years:

$$R = \frac{100}{T}$$

**Example:** doubles in 15 yr → $R = \frac{100}{15} = 6\frac{2}{3}\%$

---

### Trick 3 — Money becomes $\frac{m}{n}$ of itself
 $SI = PRT.$
**Example:** becomes $\frac{7}{6}$ in 3 yr → $P=6,\; A=7,\; SI=1$

$$R = \frac{1 \times 100}{6 \times 3} = \frac{100}{18} = 5\frac{5}{9}\%$$

---

### Trick 4 — Variable rates across years

Add up $R \times T$ for each period → total % → apply on $P$

**Example:** 6% for 4 yr, 8% for 6 yr, 10% for 5 yr

$$\text{Total \%} = (6 \times 4) + (8 \times 6) + (10 \times 5) = 24 + 48 + 50 = 122$$

> Just multiply each rate by its years and sum. Result is total SI%.

Hence SI = SI% & P

---

### Trick 5 — "Higher rate" difference problems

If rate were $\Delta R$ higher for $T$ years, extra interest $= \Delta R \times T$% of $P$

**Example:** 3% higher for 2 yr gives ₹300 extra

$$3 \times 2 = 6\% \text{ of } P = 300 \implies P = 5000$$

---

### Trick 6 — Two amounts at different times

Given $A_1$ at $T_1$ years and $A_2$ at $T_2$ years:

$$\text{SI per year} = \frac{A_2 - A_1 (\text{interest earned over the years})}{T_2 - T_1}$$

$$P = A_1 - (\text{SI per year} \times T_1)$$

**Example:** ₹720 in 2 yr, ₹1020 in 7 yr

$$\text{SI/yr} = \frac{1020 - 720}{7 - 2} = \frac{300}{5} = 60$$

$$P = 720 - (60 \times 2) = 600$$

---


---

# Compound interset
### 2. CI Calculation (Line Method, time < 3)

Avoid complex formulas like $A = P(1 + \frac{r}{100})^n$. Use the "Line Method" for quick calculation:

![[Pasted image 20260328080809.png]]

### 4. Succeseive percentage/PCG (when time > 3)

PCG = building amount year by year, reusing previous calculations.

**Year 1:** $$100 \xrightarrow{+12} 112$$

**Year 2:** 12% of 112 = 12% of 100 + 12% of 12 = 12 + 1.44 = 13.44
$$112 \xrightarrow{+13.44} 125.44$$

**Year 3:** 12% of 125.44 = 12% of 112 + 12% of 13.44
- 12% of 112 = 13.44 (known)
- 12% of 13.44 = 12% of 12 + 12% of 1.44 = 1.44 + 0.17 = 1.61
Total = 13.44 + 1.61 = 15.05
$$125.44 \xrightarrow{+15.05} 140.49$$


Each year's interest = $$r\% \text{ of previous amount} = r\% \text{ of prev-1 amount} + r\% \text{ of last interest}$$


### 3. Fractional Time (e.g., 1.5 years or 2 years 4 months)

1. Calculate for the **next full year** (e.g., for 1.5 years, calculate for 2 years).
2. Take the full interest for the completed years.
3. Take a **fractional part** of the interest for the final partial year.
	- _Example (1.5 years):_ Year 1 (Full) + Year 2 (Half).
	- _Example (2 years 4 months):_ Year 1 (Full) + Year 2 (Full) + Year 3 ($\frac{4}{12}$ or $\frac{1}{3}$).
        
Or

| Case | Compounding Type | Amount Formula | Rate per Period | Number of Periods |
|------|-----------------|----------------|-----------------|------------------|
| 2 | **Half-Yearly** | $A = P \left(1 + \frac{r/2}{100}\right)^{2n}$ | $\frac{r}{2}\%$ | $2n$ half-years |
| 3 | **Quarterly** | $A = P \left(1 + \frac{r/4}{100}\right)^{4n}$ | $\frac{r}{4}\%$ | $4n$ quarters |
| — | **CI – SI Difference (2 years)** | $\text{Difference} = P \left( \frac{r}{100} \right)^2$ | — | — |

### 4. Depreciation
The value of a machine or any article subject to wear and tear decreases with time.  
This decrease is called **depreciation**.

$V_f=V_o(1−r/100)^t$

---

# SI VS CI

- Compound: successive multiplications (1.1 × 1.1 = 1.21 for 2 years at 10%)
- Simple: linear addition (10% + 10% = 20% for 2 years at 10%)
- Amount for n years at r%: 
	- Amount = P(1 + (n × r/100))
	- Amount = P(1+r/100)^n
- Overall rate for n years at r%:
	- For SI: rate * time
	- For CI: rate ^ time
# [[Installment]]
https://www.youtube.com/watch?v=o1ZMeSKOuME
