---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Number System"
subtopic: "Decimal Fractions & Recurring Decimals"
difficulty: "Easy"
tags: [cds, math, decimals, subtopic]
---

# Decimal Fractions & Recurring Decimals

## Theory, Intuition & Formulas

### 1. Classification of Decimals

1. **Terminating Decimals**:
   - Fractions whose denominator in prime-factored form contains ONLY powers of $2$ and $5$ (i.e., $q = 2^a \cdot 5^b$).
   - Example:
     $$\frac{13}{80} = \frac{13}{2^4 \cdot 5^1} = 0.1625$$

2. **Pure Recurring Decimals**:
   - Every digit after the decimal point repeats infinitely.
   - Denominator contains prime factors other than $2$ and $5$.
   - Example:
     $$0.\overline{27} = 0.272727\dots$$

3. **Mixed Recurring Decimals**:
   - Some digits after the decimal point do not repeat, followed by infinitely repeating digits.
   - Example:
     $$0.17\overline{9} = 0.179999\dots$$

---

### 2. General Proof & Conversion Formulas

#### Theorem 1: Pure Recurring Decimal to Vulgar Fraction
For a pure recurring decimal $0.\overline{a_1 a_2 \dots a_n}$ with $n$ repeating digits:
$$0.\overline{a_1 a_2 \dots a_n} = \frac{a_1 a_2 \dots a_n}{10^n - 1} = \frac{a_1 a_2 \dots a_n}{\underbrace{99\dots9}_{n \text{ times}}}$$

**Proof**:
Let $x = 0.\overline{a_1 a_2 \dots a_n}$.
Multiply by $10^n$:
$$10^n x = (a_1 a_2 \dots a_n).\overline{a_1 a_2 \dots a_n}$$
Subtract original $x$:
$$10^n x - x = a_1 a_2 \dots a_n$$
$$(10^n - 1) x = a_1 a_2 \dots a_n \implies x = \frac{a_1 a_2 \dots a_n}{10^n - 1}$$

---

#### Theorem 2: Mixed Recurring Decimal to Vulgar Fraction
For a mixed recurring decimal $0.b_1 b_2 \dots b_m \overline{a_1 a_2 \dots a_n}$ with $m$ non-repeating digits and $n$ repeating digits:
$$0.b_1 b_2 \dots b_m \overline{a_1 a_2 \dots a_n} = \frac{(\text{Full Number}) - (\text{Non-repeating Part})}{\underbrace{99\dots9}_{n \text{ times}}\underbrace{00\dots0}_{m \text{ times}}}$$

**Proof**:
Let $x = 0.b_1 b_2 \dots b_m \overline{a_1 a_2 \dots a_n}$.
Shift non-repeating part by multiplying by $10^m$:
$$10^m x = (b_1 b_2 \dots b_m).\overline{a_1 a_2 \dots a_n}$$
Shift repeating block by multiplying by $10^{m+n}$:
$$10^{m+n} x = (b_1 b_2 \dots b_m a_1 a_2 \dots a_n).\overline{a_1 a_2 \dots a_n}$$
Subtract:
$$(10^{m+n} - 10^m) x = (b_1 \dots b_m a_1 \dots a_n) - (b_1 \dots b_m)$$
$$10^m (10^n - 1) x = (\text{Full Number}) - (\text{Non-repeating Part})$$
$$x = \frac{(\text{Full Number}) - (\text{Non-repeating Part})}{99\dots900\dots0}$$

---

## Linked Practice Questions

- [[cds/math/notes/questions/q_dec1|Q1: Converting Pure Recurring Decimal 0.232323...]]
- [[cds/math/notes/questions/q_dec2|Q2: Sum of Recurring Decimals 0.6 + 0.8 + 0.7]]
- [[cds/math/notes/questions/q_dec3|Q3: Mixed Recurring Decimal 0.1236]]

---

## Navigation
- [[cds/math/notes/decimals|Chapter 4: Decimal Fractions]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
