---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Square Roots and Cube Roots"
difficulty: "Hard"
tags: [cds, elementary-mathematics, roots, variation]
---

# Square Roots and Cube Roots Variations

## Variation 1: Infinite Nested Radical Convergence

### Mathematical Formulation

Find the value of $x = \sqrt{a + \sqrt{a + \sqrt{a + \dots}}}$ where $a > 0$.

### Closed-Form Solution & Derivation

- Step 1: Express self-similarity in the radical:
  $$x = \sqrt{a + x}$$

- Step 2: Square both sides and form quadratic:
  $$x^2 - x - a = 0$$

- Step 3: Apply standard quadratic formula for $x > 0$:
  $$x = \frac{1 + \sqrt{1 + 4a}}{2}$$

---

## Variation 2: Four Consecutive Product Plus One Theorem

### Mathematical Formulation

Prove that for any integer $n$, the product $P(n) = n(n+1)(n+2)(n+3) + 1$ is a perfect square.

### Algebraic Derivation

- Step 1: Group extreme and middle terms:
  $$P(n) = [n(n+3)][(n+1)(n+2)] + 1 = (n^2 + 3n)(n^2 + 3n + 2) + 1$$

- Step 2: Let $y = n^2 + 3n$:
  $$P(n) = y(y + 2) + 1 = y^2 + 2y + 1 = (y + 1)^2$$

- Step 3: Substitute back $y$:
  $$\sqrt{n(n+1)(n+2)(n+3) + 1} = n^2 + 3n + 1$$
