---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Modular Arithmetic"
subtopic: "Fermat's Little Theorem"
difficulty: "Medium"
tags: [cds, elementary-mathematics, modular, theorem, flt]
---

# Fermat's Little Theorem (FLT)

## Statement & Formulation

If $p$ is a prime number and $a$ is any integer such that $\operatorname{GCD}(a, p) = 1$, then:

$$\mathbf{a^{p-1} \equiv 1 \pmod p}$$

### Alternative General Form (Holds for all integers $a$):
$$\mathbf{a^p \equiv a \pmod p}$$

---

## Mathematical Proof

Consider the set of non-zero residues modulo $p$:
$$S = \{1, 2, 3, \dots, p-1\}$$

Multiply every element in $S$ by $a$:
$$S' = \{1a, 2a, 3a, \dots, (p-1)a\}$$

1. **Distinctness**: No two elements in $S'$ are congruent modulo $p$.  
   If $i \cdot a \equiv j \cdot a \pmod p$, since $\operatorname{GCD}(a, p) = 1$, we can cancel $a$ to get $i \equiv j \pmod p$.
2. **Remainder Set Equivalence**:  
   Therefore, $S'$ modulo $p$ is a permutation of $S$.
3. **Multiply all elements together**:
   $$(1a)(2a)(3a)\cdots((p-1)a) \equiv 1 \cdot 2 \cdot 3 \cdots (p-1) \pmod p$$
   $$a^{p-1} \cdot (p-1)! \equiv (p-1)! \pmod p$$
4. **Cancel $(p-1)!$**:  
   Since all factors in $(p-1)!$ are co-prime to $p$, $\operatorname{GCD}((p-1)!, p) = 1$. Dividing both sides yields:
   $$\mathbf{a^{p-1} \equiv 1 \pmod p} \quad \blacksquare$$

---

## Group Theory & Lagrange's Theorem Connection

Fermat's Little Theorem is a direct special case of **Lagrange's Theorem** in Group Theory:

> **Lagrange's Theorem Corollary:** For any finite group $G$ of order $|G| = n$ and element $g \in G$:
> $$\mathbf{g^n = e} \quad (\text{where } e \text{ is the identity element of } G)$$

### Derivation of FLT from Group Theory:
1. Consider the **Multiplicative Group of Integers Modulo $p$**:
   $$\mathbb{Z}_p^\times = \{1, 2, 3, \dots, p - 1\}$$
2. **Group Order**: Since $p$ is prime, there are $p - 1$ elements $\implies |G| = p - 1$.
3. **Identity Element**: $e = 1$.
4. Apply Lagrange's Corollary $g^{|G|} = e$ to element $a \in \mathbb{Z}_p^\times$:
   $$\mathbf{a^{p-1} \equiv 1 \pmod p} \quad \blacksquare$$

#### Example ($p = 7$, $a = 3$):
Group $\mathbb{Z}_7^\times = \{1, 2, 3, 4, 5, 6\}$ (Order $|G| = 6$).  
Cyclic subgroup $\langle 3 \rangle = \{3, 2, 6, 4, 5, 1\}$ (Order $|H| = 6$).  
By Lagrange's Theorem: $3^6 \equiv \mathbf{1 \pmod 7}$.

---

## High-Yield CDS Exam Variations

1. **Power Reduction ($E > p-1$)**: Reduce $E \pmod{p-1}$. E.g., $2^{1000} \pmod{17} \implies 1000 = 16(62) + 8 \implies 2^8 \equiv 1 \pmod{17}$.
2. **Sum of Powers Modulo Prime**: $\sum_{x=1}^{p-1} x^{p-1} \equiv \sum 1 = (p-1) \equiv -1 \pmod p$.
3. **Modular Inverse Calculation**: $a^{-1} \equiv a^{p-2} \pmod p$.

---

## Linked Practice Questions

- [[cds/math/notes/questions/q11|Question 11: Modular Fast Power Reduction]]
- [[cds/math/notes/questions/q13|Question 13: Large Exponent Modulo Prime (2^1000 mod 17)]]
- [[cds/math/notes/questions/q14|Question 14: Sum of Powers Modulo Prime]]

## Related Theorems & Topics

- [[cds/math/notes/subtopics/crt|Chinese Remainder Theorem]]
- [[cds/math/notes/subtopics/wilson|Wilson's Theorem]]
- [[cds/math/notes/modular|Modular Arithmetic Topic]]
