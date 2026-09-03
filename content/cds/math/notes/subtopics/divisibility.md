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

## Combined 7-11-13 Shortcut Trick (The 3-Digit Grouping Rule)

Since $7 \times 11 \times 13 = 1001$:
- Split any large number into 3-digit groups from right to left.
- Take the alternating sum of these 3-digit groups.
- Test the resulting number for divisibility by 7, 11, or 13!

## Linked Practice Questions

- [[cds/math/notes/questions/q12|Q12]]

## Navigation

- [[cds/math/notes/numbers|Number System]]
