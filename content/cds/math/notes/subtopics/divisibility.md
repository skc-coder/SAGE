---
exam: "CDS"
subject: "Math"
topic: "Numbers"
subtopic: "Divisibility"
difficulty: "Medium"
tags: [cds, math, subtopic]
---

# Divisibility Rules & Mathematical Proofs

## 1. Divisibility Rule of 7

### Rule:
Take the last digit, double it, and subtract it from the remaining truncated number. If the result is divisible by 7 (or 0), the original number is divisible by 7.

### Proof (Modular Arithmetic & Osculation):
Let a number $N$ be represented as $N = 10A + B$, where $B$ is the last digit and $A$ is the remaining truncated number.

1. We want to check if $10A + B \equiv 0 \pmod 7$.
2. Multiply the entire congruence by 5 (since $\gcd(5, 7) = 1$):
   $$5(10A + B) = 50A + 5B$$
3. Since $50 \equiv 1 \pmod 7$ and $5 \equiv -2 \pmod 7$:
   $$50A + 5B \equiv 1A + (-2)B \pmod 7$$
   $$\implies A - 2B \pmod 7$$
4. Hence, $N = 10A + B$ is divisible by 7 if and only if **$A - 2B$** is divisible by 7. $\blacksquare$

---

## 2. Divisibility Rule of 11

### Rule:
Take the alternating sum of the digits (sum of digits at odd places minus sum of digits at even places). If the difference is divisible by 11 (or 0), the original number is divisible by 11.

### Proof (Expansion in Base 10):
Let $N = a_n \cdot 10^n + a_{n-1} \cdot 10^{n-1} + \dots + a_1 \cdot 10^1 + a_0$.

1. Observe powers of 10 modulo 11:
   - $10 \equiv -1 \pmod{11}$
   - $10^2 = 100 \equiv +1 \pmod{11}$
   - $10^3 = 1000 \equiv -1 \pmod{11}$
   - In general, $10^k \equiv (-1)^k \pmod{11}$.

2. Substitute $10^k \equiv (-1)^k \pmod{11}$ into the polynomial representation of $N$:
   $$N \equiv a_n(-1)^n + a_{n-1}(-1)^{n-1} + \dots + a_1(-1)^1 + a_0 \pmod{11}$$
   $$N \equiv a_0 - a_1 + a_2 - a_3 + \dots \pmod{11}$$

3. Hence, $N$ is divisible by 11 if and only if the alternating sum of digits **$(a_0 - a_1 + a_2 - a_3 + \dots)$** is divisible by 11. $\blacksquare$

---

## 3. Divisibility Rule of 13

### Rule:
Take the last digit, multiply it by 4, and add it to the remaining truncated number. If the result is divisible by 13 (or 0), the original number is divisible by 13.

### Proof (Osculation Method):
Let $N = 10A + B$, where $B$ is the last digit and $A$ is the remaining number.

1. We want to check if $10A + B \equiv 0 \pmod{13}$.
2. Multiply by 4 (since $\gcd(4, 13) = 1$):
   $$4(10A + B) = 40A + 4B$$
3. Since $40 \equiv 1 \pmod{13}$:
   $$40A + 4B \equiv 1A + 4B \pmod{13}$$
   $$\implies A + 4B \pmod{13}$$
4. Hence, $10A + B$ is divisible by 13 if and only if **$A + 4B$** is divisible by 13. $\blacksquare$

---

## 4. Divisibility Rule of 17

### Rule:
Take the last digit, multiply it by 5, and subtract it from the remaining truncated number. If the result is divisible by 17 (or 0), the original number is divisible by 17.

### Proof (Osculation Method):
Let $N = 10A + B$, where $B$ is the last digit and $A$ is the remaining number.

1. We want to check if $10A + B \equiv 0 \pmod{17}$.
2. Multiply by 5 (since $\gcd(5, 17) = 1$):
   $$5(10A + B) = 50A + 5B$$
3. Since $50 \equiv -1 \pmod{17}$ (since $50 = 3 \times 17 - 1$):
   $$50A + 5B \equiv -1A + 5B \pmod{17}$$
4. Multiply by $-1$:
   $$-(-A + 5B) \equiv A - 5B \pmod{17}$$
5. Hence, $10A + B$ is divisible by 17 if and only if **$A - 5B$** is divisible by 17. $\blacksquare$

---

## 5. Combined 7-11-13 Shortcut Trick (The 3-Digit Grouping Rule)

### Rule:
Since $7 \times 11 \times 13 = 1001$:
1. Split any large number into **3-digit groups** starting from right to left (units place).
2. Take the **alternating sum** of these 3-digit groups (Group 1 - Group 2 + Group 3 - ...).
3. If the resulting difference is divisible by 7, 11, or 13, then the original number is also divisible by 7, 11, or 13 respectively!

---

### Mathematical Proof (Base $1000$ Expansion):

Let any large number $N$ be represented in base $1000$ using 3-digit blocks $G_0, G_1, G_2, \dots, G_k$:
$$N = G_k \cdot (1000)^k + G_{k-1} \cdot (1000)^{k-1} + \dots + G_1 \cdot (1000)^1 + G_0$$

Notice the key algebraic identity:
$$1000 = 1001 - 1$$

Since $1001 = 7 \times 11 \times 13$, modulo $1001$ we have:
$$1000 \equiv -1 \pmod{1001}$$

Taking powers of $1000$ modulo $1001$:
- $(1000)^1 \equiv -1 \pmod{1001}$
- $(1000)^2 = (-1)^2 \equiv +1 \pmod{1001}$
- $(1000)^3 = (-1)^3 \equiv -1 \pmod{1001}$
- In general: $(1000)^m \equiv (-1)^m \pmod{1001}$

Substitute this into the base $1000$ expansion of $N$:
$$N \equiv G_0 - G_1 + G_2 - G_3 + \dots \pmod{1001}$$

Since any divisor of $1001$ (which are 7, 11, and 13) also divides any multiple of $1001$:
$$\text{If } 1001 \mid (N - (G_0 - G_1 + G_2 - \dots)), \text{ then } 7, 11, 13 \text{ also divide } N \iff 7, 11, 13 \text{ divide } (G_0 - G_1 + G_2 - \dots) . \blacksquare$$

---

### Worked Example:

Test if $N = 45,983,724$ is divisible by 7, 11, or 13.

1. **Split into 3-digit groups from right to left**:
   - $G_0 = 724$
   - $G_1 = 983$
   - $G_2 = 045$

2. **Calculate Alternating Sum**:
   $$\text{Diff} = G_0 - G_1 + G_2 = 724 - 983 + 45 = -214$$

3. **Test $-214$**:
   - **For 7**: $-214 = 7 \times (-30) - 4$ $\implies$ **Not divisible by 7**
   - **For 11**: $-214 = 11 \times (-19) - 5$ $\implies$ **Not divisible by 11**
   - **For 13**: $-214 = 13 \times (-16) - 6$ $\implies$ **Not divisible by 13**

## Linked Practice Questions

- [[cds/math/notes/questions#question-3-q30-even-integer-divisibility|Question 3 (Q30)]]
- [[cds/math/notes/questions#question-4-q37-3-digit-numbers-ending-in-7-divisible-by-11|Question 4 (Q37)]]

## Variations

- [[cds/math/notes/variations/vars#variation-4-divisibility-of-3-digit-repeated-number-1001-principle|Variation 4: 1001 Principle]]
- [[cds/math/notes/variations/vars#variation-5-divisibility-of-562k984-by-13|Variation 5: Finding Unknown Digit $k$]]
- [[cds/math/notes/variations/vars#variation-6-repunit-remainder-modulo-13|Variation 6: Repunit Modulo 13]]

## Navigation

- [[cds/math/notes/numbers|Number System]]
