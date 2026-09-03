---
exam: "CDS"
subject: "Math"
topic: "Set Theory"
subtopic: "Set Operations & Laws"
difficulty: "Medium"
tags: [cds, math, set-theory, subtopic]
---

# Set Operations & Algebraic Laws

## 1. Core Operations
1. **Union ($A \cup B$)**:
   $$\{x : x \in A \text{ or } x \in B\}$$
2. **Intersection ($A \cap B$)**:
   $$\{x : x \in A \text{ and } x \in B\}$$
3. **Difference ($A - B$)**:
   $$\{x : x \in A \text{ and } x \notin B\} = A \cap B'$$
4. **Symmetric Difference ($A \Delta B$)**:
   $$A \Delta B = (A - B) \cup (B - A) = (A \cup B) - (A \cap B)$$
5. **Complement ($A'$)**:
   $$A' = U - A = \{x : x \in U \text{ and } x \notin A\}$$

## 2. Fundamental Algebraic Laws
- **Idempotent Laws**:
  $$A \cup A = A, \quad A \cap A = A$$
- **Identity Laws**:
  $$A \cup \emptyset = A, \quad A \cap U = A$$
- **Commutative Laws**:
  $$A \cup B = B \cup A, \quad A \cap B = B \cap A$$
- **Associative Laws**:
  $$(A \cup B) \cup C = A \cup (B \cup C), \quad (A \cap B) \cap C = A \cap (B \cap C)$$
- **Distributive Laws**:
  $$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$$
  $$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$$
- **De-Morgan's Laws**:
  $$(A \cup B)' = A' \cap B'$$
  $$(A \cap B)' = A' \cup B'$$

## 3. Important Set Identities
- $A - (B \cup C) = (A - B) \cap (A - C)$
- $A - (B \cap C) = (A - B) \cup (A - C)$
- $(A - B) \cap (B - A) = \emptyset$
- $A \cap (A \cup B) = A$ (Absorption Law)
- $A \cup (A \cap B) = A$
