---
exam: "CDS"
subject: "Math"
topic: "Numbers"
subtopic: "Remainders"
difficulty: "Hard"
status: "Correct"
importance: "Important"
tags: [cds, math, variation]
---

# Variation 7: AP Sum with Dual Remainders

Find the sum of all 2-digit numbers leaving remainder 3 when divided by 5 and remainder 1 when divided by 4.

> [!faq]- View Solution
> First term $a \equiv 3 \pmod 5$ and $a \equiv 1 \pmod 4$:
> - Check mod 4 on numbers $\equiv 3 \pmod 5$: $3, 8, 13, 18, \dots$
> - $13 \equiv 1 \pmod 4 \implies a = 13$.
> Common difference $d = \operatorname{LCM}(5, 4) = 20$.
> AP terms < 100: $13, 33, 53, 73, 93$ ($n = 5$).
> $$S_5 = \frac{5}{2}(13 + 93) = \frac{5}{2}(106) = 5 \times 53 = 265$$

## Navigation
- [[cds/math/notes/subtopics/remainders|Subtopic: Remainders]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
