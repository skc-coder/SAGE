# Unit Digit Concepts

## Basics
- Unit digit = last digit of a number
- For multiplication: multiply only unit digits
  - e.g., 12 × 13 → 2 × 3 = 6
- For addition: add only unit digits
  - e.g., 1234 + 2345 + 1090 → 4 + 5 + 0 = 9
- **For subtraction:** 
  - **If result is negative, add 10**
  - **e.g., 2 - 7 = -5 → -5 + 10 = 5**

## Special Cases
- **5 × any odd number** → unit digit = 5
- **5 × any even number** → unit digit = 0
- **0, 1, 5, 6** → unit digit same for any power
  - e.g., 5ⁿ → 5, 6ⁿ → 6

## Cyclic Patterns
- **Cycle length 4** (for 2, 3, 7, 8):
  - Divide power by 4, use remainder
  - If remainder 0 → use 4
  - e.g., 2⁴⁷ → 47 ÷ 4 = rem 3 → 2³ = 8
- **Cycle length 2** (for 4, 9):
  - 4: odd power → 4, even power → 6
  - 9: odd power → 9, even power → 1

## Power Calculations
- For large powers: use cyclic patterns
- For expressions like aᵇᶜ: evaluate from top down
  - e.g., 32³²³² → 2³²³² → 2⁴ = 16 → unit digit 6
(when power is divided by 4 and remainder is zero than we take 4 as power, like we did here, otherwise take the power as remainder as it is)
## Examples
- 232 × 235 → 2 × 5 = 0
- 43⁴⁶ → 3⁴⁶ → 3² = 9 (since 46 ÷ 4 = rem 2)
- 4⁶³ → 4 (since 63 is odd)