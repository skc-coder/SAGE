---
exam: "CDS"
subject: "Math"
topic: "Numbers"
difficulty: "Medium"
tags: [cds, math, questions]
---

# Numbers Practice Questions

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

## Navigation

- [[cds/math/math_overview|Elementary Mathematics Overview]]
