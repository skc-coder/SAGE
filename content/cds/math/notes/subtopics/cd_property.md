---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Ratio and Proportion"
subtopic: "Componendo and Dividendo Theorem"
difficulty: "Hard"
tags: [cds, elementary-mathematics, ratio, subtopic, proof, cd-theorem]
---

# Componendo and Dividendo Theorem & Algebraic Invariants

## Theory & Proofs

### Statement of the Theorem
If four non-zero quantities $a, b, c, d$ satisfy the proportion:
$$\frac{a}{b} = \frac{c}{d}$$
then by applying **Componendo and Dividendo (C&D)** simultaneously, the transformation holds:
$$\frac{a + b}{a - b} = \frac{c + d}{c - d}$$

---

### Step-by-Step Rigorous Proof

1. **Derivation of Componendo**:
   - Add $1$ to both sides of the ratio equation $\frac{a}{b} = \frac{c}{d}$:
     $$\frac{a}{b} + 1 = \frac{c}{d} + 1$$
   - Taking a common denominator on each side:
     $$\frac{a + b}{b} = \frac{c + d}{d} \quad \text{--- (Equation 1)}$$

2. **Derivation of Dividendo**:
   - Subtract $1$ from both sides of the ratio equation $\frac{a}{b} = \frac{c}{d}$:
     $$\frac{a}{b} - 1 = \frac{c}{d} - 1$$
   - Taking a common denominator on each side:
     $$\frac{a - b}{b} = \frac{c - d}{d} \quad \text{--- (Equation 2)}$$

3. **Combining via Division**:
   - Divide Equation 1 by Equation 2:
     $$\frac{\frac{a + b}{b}}{\frac{a - b}{b}} = \frac{\frac{c + d}{d}}{\frac{c - d}{d}}$$
   - Cancelling common denominators $b$ and $d$ yields the final result:
     $$\frac{a + b}{a - b} = \frac{c + d}{c - d}$$

---

### Key Intuition & Pattern Recognition
- **Symmetry Restoration**: C&D simplifies fractions of the form $\frac{f(x) + g(x)}{f(x) - g(x)} = k$ directly into $\frac{f(x)}{g(x)} = \frac{k+1}{k-1}$.
- **Radical Elimination**: Essential for radical equations involving $\frac{\sqrt{A} + \sqrt{B}}{\sqrt{A} - \sqrt{B}}$.

---

## Linked Practice Questions

- [[cds/math/notes/questions/q1|CDS 2024 Q1: Componendo Dividendo Radical Simplification]]

---

## Variations

- [[cds/math/notes/variations/var_ratio1|Nested Componendo-Dividendo Higher Algebraic Invariant]]

---

## Navigation

- Back to Topic: [[cds/math/notes/ratio_proportion|Ratio and Proportion]]
- Central [[cds/math/question_db|Question Database]]
