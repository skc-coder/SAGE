### Number of Zeroes in an Expression

---

#### Basic Concept

Zeroes come from factors of 10 = 2 × 5. Each zero requires one pair of (2, 5).

**Number of zeroes = min(count of 2's, count of 5's)**

Since 2's are always more abundant than 5's, **count the 5's only**.

---

#### In a Product

**Example:** 8 × 15 × 23 × 17 × 25 × 22

Standard form: 2³ × 3¹ × 5¹ × 2³ × 17 × 5² × 2¹ × 11¹

- Count of 2's: 3 + 3 + 1 = **7**
- Count of 5's: 1 + 2 = **3**
- Number of zeroes = min(7, 3) = **3**

---

#### In n! (Factorial)

Use Legendre's formula to count 5's:

$$\text{Number of 5's in } n! = \left\lfloor \frac{n}{5} \right\rfloor + \left\lfloor \frac{n}{5^2} \right\rfloor + \left\lfloor \frac{n}{5^3} \right\rfloor + \cdots$$

**Example:** Number of zeroes in 100!

- ⌊100/5⌋ = 20
- ⌊100/25⌋ = 4
- ⌊100/125⌋ = 0 → stop

**Number of zeroes = 20 + 4 = 24**