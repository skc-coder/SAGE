---
exam: "CDS"
subject: "Math"
topic: "Numbers"
subtopic: "Divisibility"
difficulty: "Hard"
status: "Correct"
importance: "Important"
tags: [cds, math, variation]
---

# Variation 5: Divisibility of 562k984 by 13

If $562k984$ is divisible by 13, find digit $k$.

- **Correct Answer**: (c) 7

> [!faq]- View Solution
> 3-digit grouping from right: $G_0 = 984$, $G_1 = 62k = 620 + k$, $G_2 = 5$.
> Alternating sum:
> $$\text{Diff} = 984 - (620 + k) + 5 = 369 - k$$
> Test $369 - k \pmod{13}$:
> $369 = 13 \times 28 + 5 \implies 369 \equiv 5 \pmod{13}$.
> Thus $5 - k \equiv 0 \pmod{13} \implies k = 5$.

## Navigation
- [[cds/math/notes/subtopics/divisibility|Subtopic: Divisibility Rules]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
