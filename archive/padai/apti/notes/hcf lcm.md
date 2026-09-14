## Definitions

- **LCM (Least Common Multiple)**: `लघुत्तम समापवर्तक` - Smallest number divisible by all given numbers.
- **HCF (Highest Common Factor)**: `महत्तम समापवर्तक` - Largest number that divides all given numbers.

### Key Difference
- **LCM** works with **Multiples** (smallest common multiple).
- **HCF** works with **Factors** (largest common factor).

---

## Methods to Calculate

### 1. Prime Factorization Method
Write each number as a product of prime factors.

- **For LCM**: Take the **highest power** of each prime factor.
- **For HCF**: Take the **lowest power** of each common prime factor.

### 2. Division Method

**For LCM (Common Division)**:
- Divide by numbers that divide at least two given numbers.
- Stop when no common divisor exists.
- Multiply all divisors and the remaining numbers.

**For HCF (Common Division)**:
- Divide by numbers that divide *all* given numbers.
- Stop when no common divisor exists.
- Multiply only the common divisors.

A shortcut:

1. Find smallest difference between any two numbers
2. Find all factors of that difference
3. Check which factor divides **all** original numbers (start from highest)
4. First match = HCF

#### Optimization Tips

- Skip even factors if any original number is odd
- Use prime number differences when available (either prime is HCF or HCF = 1)
- No need to check the divisbility with numbers used to generate the differences 

### Example: Find LCM & HCF of 12 and 15

**LCM**:
$$ 12 = 2^2 \times 3 $$
$$ 15 = 3 \times 5 $$
$$ LCM = 2^2 \times 3 \times 5 = 60 $$

**HCF**:
$$ HCF = 3 $$

---

## Relationship between Numbers, HCF & LCM

For two numbers:
$$ \text{Number}_1 \times \text{Number}_2 = HCF \times LCM $$

### Important Points

1.  Any number = HCF × (some integer)
    $$ \text{Let } N_1 = H \times x, \quad N_2 = H \times y $$
    **Here, `x` and `y` are co-prime (no common factors).**

2.  $$ LCM = H \times (x \times y) $$

---

## HCF & LCM of Fractions

For fractions:

$$ \text{HCF} = \frac{HCF(\text{Numerators})}{LCM(\text{Denominators})} $$

$$ \text{LCM} = \frac{LCM(\text{Numerators})}{HCF(\text{Denominators})} $$

---

## Key Concepts for Problem Solving

### 1. Using the Product Formula
If `N1` and `N2` are two numbers, `H` = HCF, `L` = LCM:
$$ N_1 \times N_2 = H \times L $$

### 2. Co-prime Relationship
If `H` is the HCF, let:
$$ N_1 = H \times a, \quad N_2 = H \times b $$
Where `a` and `b` are **co-prime**.
Then:
$$ L = H \times a \times b $$

### 3. Using Sum and Difference
Given `N1 + N2` or `N1 - N2`, and `H`, you can find `a+b` or `a-b`.

### Example
- **Given**: `H = 5`, `L = 495`, `N1 + N2 = 100`.
- **Let**: `N1 = 5a`, `N2 = 5b`.
- `5(a + b) = 100 => a + b = 20`
- `L = H * a * b => 495 = 5 * a * b => a * b = 99`
- **Solve**: Two numbers with sum 20 and product 99 are 11 and 9.
- **Difference**: `N1 - N2 = 5(11 - 9) = 10`

### 4. Number of Possible Pairs
Given `H` and `N1 * N2` or `N1 + N2`:
1.  Express `N1 = H * a`, `N2 = H * b`
2.  Find the value of `a * b` or `a + b`.
3.  List all co-prime pairs `(a, b)` that satisfy the condition.
4.  The number of such `(a, b)` pairs is the number of possible number pairs.