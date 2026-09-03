---
exam: "CDS"
subject: "Math"
topic: "Set Theory"
subtopic: "Cartesian Product & Ordered Pairs"
difficulty: "Medium"
tags: [cds, math, set-theory, subtopic]
---

# Cartesian Product & Ordered Pairs

## 1. Ordered Pairs
An ordered pair $(a, b)$ consists of two elements $a \in A$ and $b \in B$ in a fixed order.
- **Equality**: $(a, b) = (c, d) \iff a = c \text{ and } b = d$.
- **Non-commutativity**: $(a, b) \neq (b, a)$ unless $a = b$.
- Note difference between set $\{a, b\} = \{b, a\}$ and ordered pair $(a, b) \neq (b, a)$.

## 2. Cartesian Product ($A \times B$)
The Cartesian product of sets $A$ and $B$:
$$A \times B = \{(a, b) : a \in A \text{ and } b \in B\}$$

### Cardinality Properties:
- If $|A| = m$ and $|B| = n$, then $|A \times B| = m \cdot n$.
- If either $A$ or $B$ is empty, $A \times B = \emptyset$.
- If either $A$ or $B$ is infinite (and non-empty), $A \times B$ is infinite.

## 3. Key Properties & Set Identities
1. $A \times (B \cup C) = (A \times B) \cup (A \times C)$
2. $A \times (B \cap C) = (A \times B) \cap (A \times C)$
3. $A \times (B - C) = (A \times B) - (A \times C)$
4. $(A \times B) \cap (C \times D) = (A \cap C) \times (B \cap D)$
5. If $A \subseteq B$, then $A \times C \subseteq B \times C$.
