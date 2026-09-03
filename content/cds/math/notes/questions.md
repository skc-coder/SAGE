---
exam: "CDS"
subject: "Math"
topic: "Numbers and HCF/LCM"
difficulty: "Medium"
tags: [cds, math, questions]
---

# Practice Questions

## Questions & Solutions

### Question 1 (Q12: Continuous Equal Ratios)

If $\frac{a}{4} = \frac{b}{5} = \frac{c}{6}$, then the value of $\frac{a + b + c}{b}$ is:

(a) 3  
(b) 2  
(c) 6  
(d) 4  

> [!faq]- View Solution
> **Method 1: Direct Value Substitution (Exam Shortcut ⚡)**  
> Substitute $a=4, b=5, c=6$ directly:
> $$\frac{4 + 5 + 6}{5} = \frac{15}{5} = 3$$
> 
> **Method 2: Theorem of Equal Ratios (Addendo Property)**  
> $$\frac{a+b+c}{4+5+6} = \frac{b}{5} \implies \frac{a+b+c}{15} = \frac{b}{5} \implies \frac{a+b+c}{b} = 3$$
> 
> **Correct Answer:** **(a) 3**

---

### Question 2 (Q26: Dual Remainder AP Sum)

What is the sum of positive integers less than 100 which leave a remainder 1 when divided by 3 and leave a remainder 2 when divided by 4?

(a) 416  
(b) 620  
(c) 1250  
(d) 1314  

> [!faq]- View Solution
> 1. **First term $a$**: Smallest number $N \equiv 2 \pmod 4$ and $N \equiv 1 \pmod 3$ is $a = 10$.
> 2. **Common difference $d$**: $d = \operatorname{LCM}(3, 4) = 12$.
> 3. **AP Sequence**: $10, 22, 34, 46, 58, 70, 82, 94$ ($n = 8$, last term $l = 94$).
> 4. **Sum**:
>    $$S_8 = \frac{8}{2}(10 + 94) = 4 \times 104 = 416$$
> 
> **Correct Answer:** **(a) 416**

---

### Question 3 (Q30: Even Integer Divisibility)

If $k$ is any even positive integer, then $(k^2 + 2k)$ is:

(a) divisible by 24  
(b) divisible by 8 but may not be divisible by 24  
(c) divisible by 4 but may not be divisible by 8  
(d) divisible by 2 but may not be divisible by 4  

> [!faq]- View Solution
> Let $k = 2m$:
> $$k^2 + 2k = (2m)^2 + 2(2m) = 4m(m + 1)$$
> Since $m(m+1)$ is the product of two consecutive integers, it is always even ($m(m+1) = 2p$).
> Thus $k^2 + 2k = 4(2p) = 8p$ $\implies$ **Always divisible by 8**.
> For $k = 2$, $k^2 + 2k = 8$ (not divisible by 24).
> 
> **Correct Answer:** **(b) divisible by 8 but may not be divisible by 24**

---

### Question 4 (Q37: 3-Digit Numbers Ending in 7 Divisible by 11)

What is the total number of three digit numbers with unit digit 7 and divisible by 11?

(a) 6  
(b) 7  
(c) 8  
(d) 9  

> [!faq]- View Solution
> 1. Numbers divisible by 11 are $11 \times k$. For unit digit to be 7, $k$ must end in 7 ($k = 17, 27, 37, \dots, 87$).
> 2. First 3-digit term: $a = 11 \times 17 = 187$.
> 3. Common difference: $d = 11 \times 10 = 110$.
> 4. Last term < 1000: $l = 11 \times 87 = 957$.
> 5. Number of terms:
>    $$957 = 187 + (n - 1)110 \implies 770 = (n - 1)110 \implies n = 8$$
> 
> **Correct Answer:** **(c) 8**

---

### Question 5 (HCF of Large Differences)

Find the largest number which divides 62, 132, and 237 leaving the same remainder in each case.

(a) 15  
(b) 25  
(c) 35  
(d) 45  

> [!faq]- View Solution
> Apply HCF Same Remainder Theorem:
> $$N = \operatorname{HCF}(|132 - 62|, |237 - 132|, |237 - 62|)$$
> $$N = \operatorname{HCF}(70, 105, 175)$$
> - $70 = 35 \times 2$
> - $105 = 35 \times 3$
> - $175 = 35 \times 5$
> 
> Thus, $\operatorname{HCF}(70, 105, 175) = 35$.
> 
> **Correct Answer:** **(c) 35**

---

### Question 6 (Co-prime Pair Counting Given Sum & HCF)

The sum of two numbers is 216 and their HCF is 27. How many such pairs of numbers are possible?

(a) 1  
(b) 2  
(c) 3  
(d) 4  

> [!faq]- View Solution
> Let numbers be $A = 27x$ and $B = 27y$, where $\operatorname{GCD}(x, y) = 1$.
> $$27x + 27y = 216 \implies 27(x + y) = 216 \implies x + y = 8$$
> Find co-prime positive integer pairs $(x, y)$ such that $x + y = 8$ and $x < y$:
> 1. $(1, 7)$ — $\operatorname{GCD}(1, 7) = 1$ ✅
> 2. $(2, 6)$ — $\operatorname{GCD}(2, 6) = 2 \neq 1$ ❌
> 3. $(3, 5)$ — $\operatorname{GCD}(3, 5) = 1$ ✅
> 4. $(4, 4)$ — $\operatorname{GCD}(4, 4) = 4 \neq 1$ ❌
> 
> Thus, there are exactly **2 valid pairs**: $(27 \times 1, 27 \times 7) = (27, 189)$ and $(27 \times 3, 27 \times 5) = (81, 135)$.
> 
> **Correct Answer:** **(b) 2**

---

### Question 7 (LCM Constant Difference)

Find the least number which when divided by 24, 32, and 36 leaves remainders 19, 27, and 31 respectively.

(a) 283  
(b) 288  
(c) 293  
(d) 300  

> [!faq]- View Solution
> Calculate differences $p = (x - a) = (y - b) = (z - c)$:
> - $24 - 19 = 5$
> - $32 - 27 = 5$
> - $36 - 31 = 5$
> 
> Constant difference $p = 5$.
> 
> Calculate $\operatorname{LCM}(24, 32, 36)$:
> - $24 = 2^3 \times 3$
> - $32 = 2^5$
> - $36 = 2^2 \times 3^2$
> - $\operatorname{LCM} = 2^5 \times 3^2 = 32 \times 9 = 288$
> 
> Applying Constant Difference Theorem:
> $$\text{Least } N = \operatorname{LCM}(24, 32, 36) - p = 288 - 5 = 283$$
> 
> **Correct Answer:** **(a) 283**

---

### Question 8 (Bell Ringing Concurrency Interval)

Six bells commence tolling together and toll at intervals of 2, 4, 6, 8, 10, and 12 seconds respectively. In 30 minutes, how many times do they toll together?

(a) 15  
(b) 16  
(c) 30  
(d) 31  

> [!faq]- View Solution
> 1. Find the interval of simultaneous tolling:
>    $$\operatorname{LCM}(2, 4, 6, 8, 10, 12) = 120 \text{ seconds} = 2 \text{ minutes}$$
> 2. Total time $T = 30 \text{ minutes}$.
> 3. Count of simultaneous tolls (including initial toll at $t=0$):
>    $$\text{Tolls} = \left\lfloor \frac{30}{2} \right\rfloor + 1 = 15 + 1 = 16$$
> 
> **Correct Answer:** **(b) 16**

---

### Question 9 (Example 3: Constant Difference 42, 72, 84)

What is the least number which when divided by 42, 72 and 84 leaves the remainders 25, 55 and 67, respectively?

(a) 521  
(b) 512  
(c) 504  
(d) 487  

> [!faq]- View Solution
> 1. **Check constant difference $p$**:
>    $$p = (42 - 25) = (72 - 55) = (84 - 67) = 17$$
> 2. **Calculate $\operatorname{LCM}(42, 72, 84)$**:
>    - $42 = 2 \times 3 \times 7$
>    - $72 = 2^3 \times 3^2$
>    - $84 = 2^2 \times 3 \times 7$
>    - $\operatorname{LCM} = 2^3 \times 3^2 \times 7 = 8 \times 9 \times 7 = 504$
> 3. **Apply Constant Difference Formula**:
>    $$\text{Required Number} = \operatorname{LCM}(42, 72, 84) - p = 504 - 17 = 487$$
> 
> **Correct Answer:** **(d) 487**

---

### Question 10 (Example 4: LCM with Perfect Divisibility Condition)

Find the least number which when divided by 5, 6, 7 and 8 leaves a remainder 3 but when divided by 9, leaves no remainder.

(a) 1620  
(b) 1683  
(c) 1635  
(d) 1672  

> [!faq]- View Solution
> 1. **Find $\operatorname{LCM}(5, 6, 7, 8)$**:
>    - $5 = 5$
>    - $6 = 2 \times 3$
>    - $7 = 7$
>    - $8 = 2^3$
>    - $\operatorname{LCM} = 2^3 \times 3 \times 5 \times 7 = 8 \times 105 = 840$
> 2. **Formulate General Number $N$**:
>    $$N = 840k + 3 \quad (k \in \mathbb{Z}^+)$$
> 3. **Apply Modulo 9 Condition ($N \equiv 0 \pmod 9$)**:
>    - Reduce $840 \pmod 9$: $840 = 9 \times 93 + 3 \implies 840 \equiv 3 \pmod 9$.
>    - Thus, $N = (93 \times 9 + 3)k + 3 \equiv 3k + 3 \pmod 9$.
> 4. **Find minimal integer $k$**:
>    $$3k + 3 \equiv 0 \pmod 9 \implies 3(k + 1) \equiv 0 \pmod 9$$
>    Smallest positive integer value is $k = 2$ ($3(2+1) = 9 \equiv 0 \pmod 9$).
> 5. **Calculate $N$ for $k = 2$**:
>    $$N = 840(2) + 3 = 1680 + 3 = 1683$$
> 
> **Correct Answer:** **(b) 1683**

---

### Question 11 (Modular Fast Power Reduction)

What is the remainder when $2^{100}$ is divided by 101?

(a) 1  
(b) 2  
(c) 100  
(d) 0  

> [!faq]- View Solution
> 1. **Check conditions for Fermat's Little Theorem**:
>    - Modulus $p = 101$ (101 is a prime number).
>    - Base $a = 2$, $\operatorname{GCD}(2, 101) = 1$.
> 2. **Apply Fermat's Little Theorem ($a^{p-1} \equiv 1 \pmod p$)**:
>    $$2^{101 - 1} \equiv 2^{100} \equiv 1 \pmod{101}$$
> 
> **Correct Answer:** **(a) 1**

---

### Question 12 (Negative Remainder Power Trick)

What is the remainder when $24^{101}$ is divided by 25?

(a) 1  
(b) 24  
(c) 23  
(d) 0  

> [!faq]- View Solution
> 1. **Convert to Negative Remainder**:
>    $$24 \equiv 24 - 25 \equiv -1 \pmod{25}$$
> 2. **Raise both sides to exponent 101**:
>    $$24^{101} \equiv (-1)^{101} \pmod{25} \equiv -1 \pmod{25}$$
> 3. **Convert Negative Remainder back to Positive**:
>    $$-1 \pmod{25} \equiv 25 - 1 = 24$$
> 
> **Correct Answer:** **(b) 24**

---

## Navigation

- [[cds/math/math_overview|Elementary Mathematics Overview]]


