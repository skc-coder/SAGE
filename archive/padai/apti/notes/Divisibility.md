## divisibility rules
### Powers of 2
Check last **n digits** for divisibility by $2^n$:
- Last 1 digit ÷ 2
- Last 2 digits ÷ 4
- Last 3 digits ÷ 8
- Last 4 digits ÷ 16
- Last 5 digits ÷ 32

### Powers of 5
Check last **n digits** for divisibility by $5^n$:
- Last 1 digit = 0 or 5
- Last 2 digits ÷ 25
- Last 3 digits ÷ 125

### Digit Sum Rules
- **Rule of 3:** Sum of all digits ÷ 3 (successive sum results in 3, 6, 9 or 0)
- **Rule of 9:** Sum of all digits ÷ 9 (successive sum results in 9 or 0)


---

### Composite Numbers (Coprime Factorization)

Break into coprime factors, check both:

| Number | Factors | Check                 |
| ------ | ------- | --------------------- |
| 6      | 2 × 3   | Divisible by 2 AND 3  |
| 15     | 3 × 5   | Divisible by 3 AND 5  |
| 24     | 3 × 8   | Divisible by 3 AND 8  |
| 75     | 3 × 25  | Divisible by 3 AND 25 |

---
### common method for 7, 11 and 13
**Method 2 (Large numbers):** Form 3-digit pairs from right, alternating sum:
$$\text{Pair}_1 - \text{Pair}_2 + \text{Pair}_3 - ... \equiv 0 \pmod{7/11/13}$$
### special Pattern: Repeating 3-Digit Numbers

$$abcabc = abc \times 1001 = abc \times (7 \times 11 \times 13)$$

**Always divisible by 7, 11, and 13**

Example: 123123 divisible by all three

### Rule of 7

Remove last digit, double it, subtract from remainder. Repeat.


---

### Rule of 11

**Method 1 (Alternating sum):**
(Sum of odd position digits) - (Sum of even position digits) ≡ 0 (mod 11)

**Method 2 (2-digit pairs):** Form pairs from right, then take remainder from 11, then do sum:
$$\text{Pair}_1 - \text{Pair}_2 + \text{Pair}_3 - ... \equiv 0 \pmod{11}$$

---


---
## smallest/Largest Number Problems

### For Smallest n-digit number divisible by d:
1. Write smallest n-digit number: $10^{n-1}$
2. Divide by $d$: Get quotient $q$ and remainder $r$
3. if r == 0, then answer = q
4. else answer = d(q+1) = dq + d = dq +r + d-r = 10^n-1 + d-r
5. **Answer** = $10^{n-1} + (d - r)$
	1. In short you add enough stuff to remainder (d-r) to get to the next multiple of d

### For Largest n-digit number divisible by d:
1. Write largest n-digit number: $10^n - 1$ (all 9's)
2. Divide by $d$: Get remainder $r$
3. **Answer** = $(10^n - 1) - r$
	1. 	1. In short you subtract r to get to the previous multiple of d


## counting Numbers in Range divible by a given number

- First term: smallest multiple of $d$ > $a$
- Last term: largest multiple of $d$ < $b$
- Number of terms = $\frac{\text{Last} - \text{First}}{d} + 1$

When checking divisibility by group of numbers:

1. Find **LCM** of all divisors
2. Work with the LCM instead
3. Apply divisibility rules to LCM

**Example:** For divisibility by 3, 7, 11:
$$\text{LCM}(3, 7, 11) = 231$$
https://math.stackexchange.com/questions/8289/how-many-numbers-between-1-and-1000-can-be-divided-by-both-a-and-b
---

## NOT Divisible 

1. Find LCM of the divisors
2. Take the **largest multiple of LCM ≤ total count**
3. Apply the fraction formula to that count
4. Manually check the **remaining few numbers**

**Example: 1 to 100, neither divisible by 3 nor 5** 
(we dont include 1 but do include 100)

LCM(3, 5) = 15. Nearest multiple of 15 ≤ 100 = **90**

$$90 \times \frac{2}{3} \times \frac{4}{5} = \frac{90 \times 8}{15} = 48$$

Remaining: 91, 92, 93, 94, 95, 96, 97, 98, 99, 100

- 95, 100 → divisible by 5 ✗
- 93, 96, 99 → divisible by 3 ✗
- Remaining valid: 91, 92, 94, 97, 98 → **5 numbers**

$$\text{Answer} = 48 + 5 = 53$$

---

**Example: 700 to 950, neither divisible by 3 nor 7**

Total = 950 − 700 + 1 = 251... but here 700 is excluded, so total = **250**

LCM(3, 7) = 21. Nearest multiple of 21 ≤ 250 = **245**

$$245 \times \frac{2}{3} \times \frac{6}{7} = \frac{245 \times 12}{21} = \frac{2940}{21} = 140$$

Remaining 5 numbers: 946, 947, 948, 949, 950

- 948 → div by 3 ✗
- Check rest for div by 7: 7×135=945, remainders: 946→1, 947→2, 949→4, 950→5 → none divisible
- Valid: 946, 947, 949, 950 → **4 numbers**

$$\text{Answer} = 140 + 4 = 144$$

---

### Including Both Endpoints

When question says "from A to B **including both**":

$$\text{Total count} = B - A + 1$$

**Example: 500 to 650 including both, neither divisible by 3 nor 7**

$$\text{Total} = 650 - 500 + 1 = 151$$

LCM(3, 7) = 21. Nearest multiple of 21 ≤ 151 = **147**

$$147 \times \frac{2}{3} \times \frac{6}{7} = \frac{147 \times 12}{21} = \frac{1764}{21} = 84$$

Remaining 4: 647, 648, 649, 650

- 648 → div by 3 ✗
- Check rest for div by 7: 7×92=644, remainders: 647→3, 649→5, 650→6 → none
- Valid: 647, 649, 650 → **3 numbers**

$$\text{Answer} = 84 + 3 = 87$$
