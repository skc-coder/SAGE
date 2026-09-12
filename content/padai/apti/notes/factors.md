### finding factors:

**Key insight:** Find factors **below √n**, rest appear automatically.

**Example: 80 (√80 ≈ 8.9)**

Below √80: 1, 2, 4, 5, 8
Above √80: 10, 16, 20, 40, 80 (automatic)

### sum and count of factors
#### Standard Form Recap
p,q,r are prime factors.
If n = p^a × q^b × r^c, then:

- **Number of factors** = (a+1)(b+1)(c+1)
- **Sum of factors** = (p⁰+p¹+...+pᵃ)(q⁰+q¹+...+qᵇ)(r⁰+r¹+...+rᶜ)

**Example:** 240 = 2⁴ × 3¹ × 5¹

- Number of factors = (4+1)(1+1)(1+1) = **20**
- Sum = (1+2+4+8+16)(1+3)(1+5) = 31 × 4 × 6 = **744**

---

#### Even and Odd Factors

For n = 2³ × 3⁴ × 5² × 7³:

| Type             | Sum expression                           | Count                |
| ---------------- | ---------------------------------------- | -------------------- |
| All factors      | (2⁰+2¹+2²+2³)(3⁰...3⁴)(5⁰...5²)(7⁰...7³) | (3+1)(4+1)(2+1)(3+1) |
| **Even** factors | (2¹+2²+2³)(3⁰...3⁴)(5⁰...5²)(7⁰...7³)    | **(3)(5)(3)(4)**     |
| **Odd** factors  | (2⁰)(3⁰...3⁴)(5⁰...5²)(7⁰...7³)          | **(1)(5)(3)(4)**     |

**Rule:**
- Even → remove 2⁰ from the 2-bracket (start from 2¹)
- Odd → keep only 2⁰ (i.e., ignore all powers of 2)
- NOTE: no other even prime factor other than 2!

---

#### Factors Divisible by Some Number

Fix the minimum required powers of each prime, then let the rest vary freely.

**Example:** Factors of 1200 = 2⁴ × 3¹ × 5² that are divisible by 15 (= 3¹ × 5¹)

- 3 must be at least 3¹, 5 must be at least 5¹, 2 is free
- Sum = (2⁰+2¹+2²+2³+2⁴)(3¹)(5¹+5²)
- Count = **5 × 1 × 2 = 10**

**General rule:** For factors divisible by k, remove all powers *below* the minimum required power of each prime from the brackets.
#### Finding the Number of Prime Factors
different from finding the number of factors, which we did above.

**Of a number n:**

Repeatedly divide n by a prime number until it no longer divides evenly. The number of times it divides is the exponent (power) of that prime in the factorization.

**Example:** 72 = 2³ × 3², so 2 divides 3 times, 3 divides 2 times.

---

**Of n! (n factorial):**

The highest power of a prime p that exactly divides n! is:

$$\left\lfloor \frac{n}{p} \right\rfloor + \left\lfloor \frac{n}{p^2} \right\rfloor + \left\lfloor \frac{n}{p^3} \right\rfloor + \cdots$$

Keep adding terms until the floor value becomes 0.

**Example:** Highest power of 2 in 10!

- ⌊10/2⌋ = 5
- ⌊10/4⌋ = 2
- ⌊10/8⌋ = 1
- ⌊10/16⌋ = 0 → stop

**Total = 5 + 2 + 1 = 8**, so 2⁸ divides 10! exactly.

**Special case:**
To find number of zeros in $n!,$ do the above process with $p=5$

-