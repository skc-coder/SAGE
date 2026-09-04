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

---

## Variation 3: Symmetrical Radical Componendo & Dividendo Transformation

### Mathematical Formulation

Given $x = \frac{\sqrt{u} + \sqrt{v}}{\sqrt{u} - \sqrt{v}}$, express the relationship between $x^2$, $x$, and $\frac{u}{v}$.

### Generalized Derivation

- Step 1: Apply C&D to $x = \frac{x}{1}$:
  $$\frac{x+1}{x-1} = \frac{\sqrt{u}}{\sqrt{v}}$$

- Step 2: Square both sides:
  $$\frac{(x+1)^2}{(x-1)^2} = \frac{u}{v} \implies \frac{x^2+2x+1}{x^2-2x+1} = \frac{u}{v}$$

- Step 3: Apply C&D a second time:
  $$\frac{(x^2+2x+1)+(x^2-2x+1)}{(x^2+2x+1)-(x^2-2x+1)} = \frac{u+v}{u-v} \implies \frac{2(x^2+1)}{4x} = \frac{u+v}{u-v} \implies \frac{x^2+1}{2x} = \frac{u+v}{u-v}$$

- Step 4: For special case $u = a+2b$ and $v = a-2b$:
  $$\frac{u+v}{u-v} = \frac{2a}{4b} = \frac{a}{2b} \implies \frac{x^2+1}{2x} = \frac{a}{2b} \implies b(x^2+1) = ax \implies bx^2 - ax + b = 0$$

