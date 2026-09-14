### Definition

An **implicant** is a product term or group of $2^n$ ones in a K-map that implies the function.

Number of implicants = all possible groups of size 1, 2, 4, 8, ...

### Prime Implicants (PI)

Implicants that cannot be expanded further (maximum-sized groups). They may or may not be covered by other PIs.

### Essential Prime Implicants (EPI)

A PI that covers at least one minterm not covered by any other PI.

**Finding EPIs:** Identify all PIs first, then those covering at least one essential 1 are EPIs.

### K-Map Strategy

- Group from corners first, then fold
- Expand groups in all directions
- Mark covered terms

### Minimum SOP Expression

$$\text{Min SOP} = \text{All EPIs} + \text{minimum PIs covering remaining minterms}$$

**Uniqueness:** If EPIs alone cover all minterms → unique minimized expression. Converse is not always true.

### Don't Care Conditions (X)

- **Forming implicants & PIs:** Treat X as 1
- **Selecting EPIs:** Treat X as 1 only if it helps cover real 1s; otherwise treat as 0
- X cannot make a PI essential (only real 1s do)

### Cyclic K-Map

- No EPIs
- Each minterm covered by exactly 2 PIs
- Multiple (typically 2) minimum SOP solutions
- All PIs are same size

### Key Properties

- Removing a literal from an implicant may keep it an implicant
- Removing a literal from a PI makes it non-implicant
- **PIs have no redundant literals**

---
**Source:** [YouTube](https://www.youtube.com/watch?v=fV6YWEJhP-M)