---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Number System"
subtopic: "Ratios and Proportions"
difficulty: "Easy"
tags: [cds, elementary-mathematics, subtopic]
---

# Ratios and Proportions

## Theory & Properties

### 1. Continuous Ratio Properties
Given $\frac{a}{x} = \frac{b}{y} = \frac{c}{z} = k$:
- Homogeneous algebraic fractions can be solved instantly via direct coefficient replacement ($a=x, b=y, c=z$).

---

### 2. Deep Proof: Why the Addendo Property Works

#### Mathematical Statement
$$\text{If } \frac{a}{x} = \frac{b}{y} = \frac{c}{z}, \text{ then } \frac{a + b + c}{x + y + z} = \frac{a}{x} = \frac{b}{y} = \frac{c}{z}$$

#### Proof:
1. **Set the common ratio equal to a constant $k$:**
   $$\frac{a}{x} = k \implies a = xk$$
   $$\frac{b}{y} = k \implies b = yk$$
   $$\frac{c}{z} = k \implies c = zk$$

2. **Add all the numerators together:**
   $$a + b + c = xk + yk + zk$$

3. **Factor out the common multiplier $k$:**
   $$a + b + c = k(x + y + z)$$

4. **Divide both sides by $(x + y + z)$:**
   $$\frac{a + b + c}{x + y + z} = k$$

5. **Conclusion:**
   Since $k$ was originally equal to $\frac{a}{x}$, $\frac{b}{y}$, and $\frac{c}{z}$, it proves that:
   $$\frac{a + b + c}{x + y + z} = \frac{a}{x} = \frac{b}{y} = \frac{c}{z}$$

---

### 3. General Multiplier Form (Weighted Addendo)
The Addendo property also works with any arbitrary weights $l, m, n \neq 0$:
$$\frac{la + mb + nc}{lx + my + nz} = \frac{a}{x} = \frac{b}{y} = \frac{c}{z}$$

## Linked Practice Questions

- [[content/cds/elementary-mathematics/notes/questions/pathfinder_number_system_q12|Pathfinder Number System Q12]]

## Navigation

- [[content/cds/elementary-mathematics/notes/number_system|Number System Topic]]
