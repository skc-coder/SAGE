## Overflow Detection

**Sign-magnitude:** Overflow if there's a carry out from the magnitude's MSB (**dont consider sign bit)** (only possible when signs are the same).

**1's and 2's complement:**
- Overflow occurs only when adding two numbers of the **same sign**.
- Rule: If both inputs have MSB = 1 and result MSB = 0, or both inputs MSB = 0 and result MSB = 1 → **overflow**.
- Different sign inputs → overflow **impossible**.

---
