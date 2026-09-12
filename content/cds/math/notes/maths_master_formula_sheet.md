---
exam: CDS / GATE / PGEE
subject: Mathematics
topic: Master Formula Sheet
difficulty: Medium
tags:
  - math
  - formulas
  - cds
  - gate
  - aptitude
  - algebra
  - geometry
  - trigonometry
  - statistics
---

# 🧮 Comprehensive Mathematics Master Formula Sheet

Complete reference of fundamental definitions, algebraic identities, number theory rules, sequence & series, geometry, mensuration, trigonometry, and statistics formulas across all competitive examinations.

---

## 1. Number Systems & Arithmetic Properties

### 1.1 Number Classification & Divisibility Rules
- **Divisibility Tests**:
  - $2^k$: Last $k$ digits divisible by $2^k$.
  - $3$ or $9$: Sum of all digits divisible by $3$ or $9$.
  - $11$: Difference between sum of odd-position digits and even-position digits is $0$ or divisible by $11$.
- **Number of Factors**: If $N = p_1^{a} p_2^{b} p_3^{c}$, then:
  $$\text{Total Factors } d(N) = (a + 1)(b + 1)(c + 1)$$
  $$\text{Sum of Factors } \sigma(N) = \left(\frac{p_1^{a+1}-1}{p_1-1}\right)\left(\frac{p_2^{b+1}-1}{p_2-1}\right)\left(\frac{p_3^{c+1}-1}{p_3-1}\right)$$
  $$\text{Product of Factors} = N^{\frac{d(N)}{2}}$$
- **Euler's Totient Function $\phi(N)$**: Count of coprime integers less than $N$:
  $$\phi(N) = N \left(1 - \frac{1}{p_1}\right)\left(1 - \frac{1}{p_2}\right)\dots\left(1 - \frac{1}{p_k}\right)$$
- **HCF & LCM Relation**: For two numbers $a$ and $b$:
  $$a \times b = \text{HCF}(a, b) \times \text{LCM}(a, b)$$
  $$\text{HCF of Fractions} = \frac{\text{HCF of Numerators}}{\text{LCM of Denominators}}, \quad \text{LCM of Fractions} = \frac{\text{LCM of Numerators}}{\text{HCF of Denominators}}$$

### 1.2 Remainder & Recurring Decimals
- **Euler's Theorem**: If $\gcd(a, m) = 1$, then $a^{\phi(m)} \equiv 1 \pmod m$.
- **Fermat's Little Theorem**: If $p$ is prime and $\gcd(a, p) = 1$, then $a^{p-1} \equiv 1 \pmod p$.
- **Wilson's Theorem**: For prime $p$, $(p-1)! \equiv -1 \pmod p$.
- **Recurring Decimals**:
  - Pure: $0.\overline{a_1 a_2 \dots a_n} = \frac{a_1 a_2 \dots a_n}{99\dots 9}$
  - Mixed: $0.b_1 \dots b_m \overline{a_1 \dots a_n} = \frac{(\text{Full number}) - (\text{Non-repeating part})}{99\dots 9 \, 00\dots 0}$

---

## 2. Algebra, Polynomials & Equations

### 2.1 Standard Algebraic Identities
1. $(a + b)^2 = a^2 + 2ab + b^2$
2. $(a - b)^2 = a^2 - 2ab + b^2$
3. $(a + b)^2 + (a - b)^2 = 2(a^2 + b^2)$
4. $(a + b)^2 - (a - b)^2 = 4ab$
5. $a^2 - b^2 = (a - b)(a + b)$
6. $(a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)$
7. $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$
8. $a^3 - b^3 = (a - b)(a^2 + ab + b^2)$
9. $(a + b)^3 = a^3 + b^3 + 3ab(a + b)$
10. $(a - b)^3 = a^3 - b^3 - 3ab(a - b)$
11. $a^3 + b^3 + c^3 - 3abc = (a + b + c)(a^2 + b^2 + c^2 - ab - bc - ca) = \frac{1}{2}(a+b+c)[(a-b)^2 + (b-c)^2 + (c-a)^2]$
    - *Special Case*: If $a + b + c = 0$, then $\mathbf{a^3 + b^3 + c^3 = 3abc}$.

### 2.2 Quadratic Equations & Polynomials
For quadratic equation $a x^2 + b x + c = 0$ ($a \neq 0$):
- **Roots**: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
- **Discriminant $D$**: $D = b^2 - 4ac$
  - $D > 0$: Real & Distinct roots.
  - $D = 0$: Real & Equal roots ($x = -b / 2a$).
  - $D < 0$: Complex conjugate roots.
- **Sum & Product of Roots**:
  $$\alpha + \beta = -\frac{b}{a}, \quad \alpha \beta = \frac{c}{a}$$
- **Forming Equation**: $x^2 - (\alpha + \beta) x + \alpha \beta = 0$.

---

## 3. Sequences, Series & Progressions

### 3.1 Arithmetic Progression (AP)
For AP with first term $a$ and common difference $d$:
- $n$-th term: $T_n = a + (n - 1)d$
- Sum of $n$ terms: $S_n = \frac{n}{2} [2a + (n - 1)d] = \frac{n}{2} (a + l)$
- Arithmetic Mean (AM) of $a$ and $b$: $\text{AM} = \frac{a + b}{2}$

### 3.2 Geometric Progression (GP)
For GP with first term $a$ and common ratio $r$:
- $n$-th term: $T_n = a r^{n-1}$
- Sum of $n$ terms: $S_n = \frac{a(r^n - 1)}{r - 1} \quad (r \neq 1)$
- Sum to infinity ($|r| < 1$): $S_\infty = \frac{a}{1 - r}$
- Geometric Mean (GM) of $a$ and $b$: $\text{GM} = \sqrt{a b}$

### 3.3 Harmonic Progression (HP) & Means Invariant
- Sequence $a_1, a_2, \dots$ is in HP if $\frac{1}{a_1}, \frac{1}{a_2}, \dots$ is in AP.
- Harmonic Mean (HM) of $a$ and $b$: $\text{HM} = \frac{2 a b}{a + b}$
- **Inequality of Means**: $\text{AM} \ge \text{GM} \ge \text{HM}$ (Equality holds when $a = b$).
- **Relation**: $\text{GM}^2 = \text{AM} \times \text{HM}$.

### 3.4 Standard Summation Formulas
| Series | Formula |
| :--- | :--- |
| $\sum_{k=1}^n k = 1 + 2 + \dots + n$ | $\mathbf{\frac{n(n+1)}{2}}$ |
| $\sum_{k=1}^n k^2 = 1^2 + 2^2 + \dots + n^2$ | $\mathbf{\frac{n(n+1)(2n+1)}{6}}$ |
| $\sum_{k=1}^n k^3 = 1^3 + 2^3 + \dots + n^3$ | $\mathbf{\left[\frac{n(n+1)}{2}\right]^2}$ |
| Sum of first $n$ odd numbers: $1 + 3 + \dots + (2n-1)$ | $\mathbf{n^2}$ |
| Sum of first $n$ even numbers: $2 + 4 + \dots + 2n$ | $\mathbf{n(n+1)}$ |

---

## 4. Commercial Arithmetic & Quant

### 4.1 Percentage, Profit & Loss
- **Percentage Change**: $\% \Delta = \frac{\text{New} - \text{Old}}{\text{Old}} \times 100$
- **Profit & Loss**:
  $$\text{Profit } P = \text{SP} - \text{CP}, \quad \text{Loss } L = \text{CP} - \text{SP}$$
  $$\text{Profit } \% = \frac{P}{\text{CP}} \times 100, \quad \text{Loss } \% = \frac{L}{\text{CP}} \times 100$$
- **Discount & Marked Price**:
  $$\text{Discount } D = \text{MP} - \text{SP}, \quad \text{Discount } \% = \frac{D}{\text{MP}} \times 100$$
- **Single Equivalent Discount for $d_1\%$ and $d_2\%$**:
  $$d_{\text{eq}} = d_1 + d_2 - \frac{d_1 d_2}{100}$$

### 4.2 Interest & Installments
- **Simple Interest (SI)**:
  $$\text{SI} = \frac{P \times R \times T}{100}, \quad A = P + \text{SI} = P\left(1 + \frac{RT}{100}\right)$$
- **Compound Interest (CI)**:
  $$A = P\left(1 + \frac{R}{100}\right)^T, \quad \text{CI} = A - P$$
  - Compounded half-yearly: $R \to R/2, T \to 2T$.
  - Compounded quarterly: $R \to R/4, T \to 4T$.
- **CI & SI Difference for 2 Years**:
  $$D_2 = \text{CI}_2 - \text{SI}_2 = P \left(\frac{R}{100}\right)^2$$
- **CI & SI Difference for 3 Years**:
  $$D_3 = P \left(\frac{R}{100}\right)^2 \left(\frac{300 + R}{100}\right)$$

### 4.3 Ratio, Proportion & Mixtures
- **Duplicate Ratio**: $a^2 : b^2$; **Sub-duplicate Ratio**: $\sqrt{a} : \sqrt{b}$.
- **Componendo & Dividendo**: If $\frac{a}{b} = \frac{c}{d}$, then:
  $$\frac{a + b}{a - b} = \frac{c + d}{c - d}$$
- **Alligation Rule**: If two ingredients of prices $C$ (cheaper) and $D$ (dearer) are mixed to get mean price $M$:
  $$\frac{\text{Quantity of Cheaper}}{\text{Quantity of Dearer}} = \frac{D - M}{M - C}$$

### 4.4 Time, Work, Speed & Distance
- **Work & Efficiency**: $\text{Work} = \text{Rate} \times \text{Time}$. If A completes work in $X$ days, 1 day work $= 1/X$.
- **Speed, Distance & Time**: $\text{Distance} = \text{Speed} \times \text{Time}$.
  - $1\text{ km/h} = \frac{5}{18}\text{ m/s}$, $1\text{ m/s} = \frac{18}{5}\text{ km/h}$.
- **Average Speed**:
  $$v_{\text{avg}} = \frac{\text{Total Distance}}{\text{Total Time}}$$
  - For equal distance at speeds $v_1$ and $v_2$: $v_{\text{avg}} = \frac{2 v_1 v_2}{v_1 + v_2}$.
- **Relative Speed**:
  - Same direction: $v_{\text{rel}} = |v_1 - v_2|$.
  - Opposite direction: $v_{\text{rel}} = v_1 + v_2$.
- **Boats & Streams**:
  - Downstream speed $u = v_b + v_s$.
  - Upstream speed $v = v_b - v_s$.
  - Boat speed $v_b = \frac{u + v}{2}$, Stream speed $v_s = \frac{u - v}{2}$.

---

## 5. Geometry & 2D Mensuration

### 5.1 Triangles
- **Area Formulas**:
  $$\text{Area} = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} a b \sin C$$
  $$\text{Heron's Formula: Area} = \sqrt{s(s - a)(s - b)(s - c)} \quad \text{where } s = \frac{a + b + c}{2}$$
- **Equilateral Triangle ($a$)**:
  $$\text{Height } h = \frac{\sqrt{3}}{2} a, \quad \text{Area} = \frac{\sqrt{3}}{4} a^2, \quad r_{\text{in}} = \frac{a}{2\sqrt{3}}, \quad R_{\text{circum}} = \frac{a}{\sqrt{3}}$$
- **Centres of Triangle**:
  - **Centroid ($G$)**: Intersection of medians. Divides median in $2:1$.
  - **Incenter ($I$)**: Intersection of angle bisectors. Inradius $r = \frac{\text{Area}}{s}$.
  - **Circumcenter ($O$)**: Intersection of perpendicular bisectors. Circumradius $R = \frac{abc}{4 \times \text{Area}}$.
  - **Orthocenter ($H$)**: Intersection of altitudes.
  - **Euler Line**: $H$, $G$, $O$ are collinear with $HG : GO = 2 : 1$.

### 5.2 Quadrilaterals & Circles
- **Parallelogram**: $\text{Area} = \text{base} \times \text{height}$. Diagonals bisect each other.
- **Rhombus**: $\text{Area} = \frac{1}{2} d_1 d_2$. Side $a = \frac{1}{2}\sqrt{d_1^2 + d_2^2}$. Diagonals bisect at $90^\circ$.
- **Trapezium**: $\text{Area} = \frac{1}{2} (a + b) \times h$.
- **Circle**:
  $$\text{Perimeter } C = 2\pi r, \quad \text{Area} = \pi r^2$$
  $$\text{Arc Length } L = \frac{\theta}{360^\circ} \times 2\pi r, \quad \text{Sector Area} = \frac{\theta}{360^\circ} \times \pi r^2 = \frac{1}{2} L r$$
- **Circle Theorems**:
  - Angle subtended at center is twice the angle subtended at circumference.
  - Angles in the same segment are equal. Angle in a semi-circle is $90^\circ$.
  - **Intersecting Chords Theorem**: $PA \times PB = PC \times PD$.
  - **Tangent-Secant Theorem**: $PT^2 = PA \times PB$.

---

## 6. 3D Mensuration & Solids

| Solid | Volume ($V$) | Curved / Lateral Surface Area ($\text{CSA}$) | Total Surface Area ($\text{TSA}$) |
| :--- | :--- | :--- | :--- |
| **Cube** ($a$) | $a^3$ | $4 a^2$ | $6 a^2$ |
| **Cuboid** ($l, b, h$) | $l b h$ | $2 h (l + b)$ | $2 (l b + b h + h l)$ |
| **Right Cylinder** ($r, h$) | $\pi r^2 h$ | $2 \pi r h$ | $2 \pi r (r + h)$ |
| **Right Cone** ($r, h, l$) | $\frac{1}{3} \pi r^2 h$ | $\pi r l \quad (l = \sqrt{r^2 + h^2})$ | $\pi r (r + l)$ |
| **Sphere** ($r$) | $\frac{4}{3} \pi r^3$ | $4 \pi r^2$ | $4 \pi r^2$ |
| **Hemisphere** ($r$) | $\frac{2}{3} \pi r^3$ | $2 \pi r^2$ | $3 \pi r^2$ |
| **Frustum of Cone** ($R, r, h$) | $\frac{1}{3} \pi h (R^2 + r^2 + R r)$ | $\pi l (R + r) \quad (l = \sqrt{h^2 + (R-r)^2})$ | $\text{CSA} + \pi R^2 + \pi r^2$ |

---

## 7. Trigonometry & Heights and Distances

### 7.1 Trigonometric Identities
- $\sin^2\theta + \cos^2\theta = 1$
- $1 + \tan^2\theta = \sec^2\theta \implies \sec^2\theta - \tan^2\theta = 1$
- $1 + \cot^2\theta = \csc^2\theta \implies \csc^2\theta - \cot^2\theta = 1$

### 7.2 Compound & Double Angle Formulas
- $\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B$
- $\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$
- $\tan(A \pm B) = \frac{\tan A \pm \tan B}{1 \mp \tan A \tan B}$
- $\sin 2\theta = 2 \sin\theta \cos\theta = \frac{2\tan\theta}{1 + \tan^2\theta}$
- $\cos 2\theta = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta = \frac{1 - \tan^2\theta}{1 + \tan^2\theta}$
- $\tan 2\theta = \frac{2\tan\theta}{1 - \tan^2\theta}$

### 7.3 Maxima & Minima of Trigonometric Expressions
- For $a \sin\theta + b \cos\theta$:
  $$\text{Minimum} = -\sqrt{a^2 + b^2}, \quad \text{Maximum} = +\sqrt{a^2 + b^2}$$
- For $a \sin^2\theta + b \cos^2\theta$:
  $$\text{Min} = \min(a, b), \quad \text{Max} = \max(a, b)$$

---

## 8. Statistics & Data Analysis

### 8.1 Measures of Central Tendency
- **Mean ($\bar{x}$)**:
  $$\text{Direct Method: } \bar{x} = \frac{\sum f_i x_i}{\sum f_i}$$
- **Median**:
  - Ungrouped ($n$ odd): Term at position $\frac{n+1}{2}$.
  - Ungrouped ($n$ even): Average of terms at $\frac{n}{2}$ and $\frac{n}{2} + 1$.
  - Grouped Continuous: $\text{Median} = L + \left(\frac{\frac{N}{2} - CF}{f}\right) \times h$
- **Mode**:
  - Grouped Continuous: $\text{Mode} = L + \left(\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\right) \times h$
- **Empirical Relationship**:
  $$\mathbf{\text{Mode} = 3 \times \text{Median} - 2 \times \text{Mean}}$$

### 8.2 Dispersion & Variance
- **Variance ($\sigma^2$)**:
  $$\sigma^2 = \frac{\sum (x_i - \bar{x})^2}{N} = \frac{\sum x_i^2}{N} - (\bar{x})^2$$
- **Standard Deviation ($\sigma$)**: $\sigma = \sqrt{\text{Variance}}$.
- **Coefficient of Variation (CV)**:
  $$\text{CV} = \frac{\sigma}{\bar{x}} \times 100\%$$

---

## Navigation
- [[cds/math/math_overview|Mathematics Master Dashboard]]
- [[content/index.md|Central Vault Index]]
