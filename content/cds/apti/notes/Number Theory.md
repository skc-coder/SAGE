---
source: https://www.youtube.com/watch?v=szz5JEY_vgI&list=PLoh0AzN1l5EPdIOdxLCeaVPw2tW-Z0k2U&index=9
tags:
---
📝 [[cds/apti/notes/Problems - Number Theory]]

---

- [[cds/apti/notes/Divisibility]]
- [[cds/apti/notes/Remainder Theory]]
- [[cds/apti/notes/unit digit]]
- [[cds/apti/notes/number of zeros]]
- [[cds/apti/notes/hcf lcm]]
## [[cds/apti/notes/factors]]

## recurring decimals

### Type 1: Pure Recurring
Recurrence starts immediately after decimal point.

$$0.\overline{5} = \frac{5}{9}$$
$$3.\overline{24} = 3 + \frac{24}{99}$$
$$5.\overline{362} = 5 + \frac{362}{999}$$

**Rule:** Recurring digits ÷ (9's equal to digit count)

### Type 2: Impure Recurring
Non-recurring part, then recurring.

$$0.4\overline{35} = \frac{435 - 4}{990}$$
$$0.43\overline{542} = \frac{43542 - 435}{99000}$$

**Rule:**
- Numerator: (full number up to first repeat) - (non-recurring part)
- Denominator: (9's = recurring digits) + (0's = non-recurring digits)

## odd & even operations

| Operation    | Odd ○ Odd | Even ○ Even | Odd ○ Even    | Even ○ Odd |
| ------------ | --------- | ----------- | ------------- | ---------- |
| Multiply (×) | Odd       | Even        | Even          | Even       |
| Add (+)      | Even      | Even        | Odd           | Odd        |
| Subtract (−) | Even      | Even        | Odd           | Odd        |
| Divide (÷)   | Odd       | Even or Odd | Not divisible | Even       |

In divide case, if odd in denominator, then result is parity of numerator.