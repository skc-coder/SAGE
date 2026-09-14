Replacing R with two or more relations such that:
- Each new relation has a subset of R's attributes
- Every attribute of R appears in at least one new relation

---

## 1. Lossless vs Lossy

**Lossless** — natural join of decomposed relations gives back exactly R. No spurious tuples.
**Lossy** — natural join produces extra spurious tuples (not losing original tuples, gaining wrong ones).

### Condition (binary decomposition only)

Lossless iff: R₁ ∩ R₂ → R₁ ∈ F⁺ OR  R₁ ∩ R₂ → R₂ ∈ F⁺

i.e. common attributes form a superkey of at least one of R₁, R₂.

Lossy iff: R₁ ∩ R₂ ↛ R₁ AND R₁ ∩ R₂ ↛ R₂

**How to check:** take closure of common attributes, see if it contains all columns of R₁ or R₂.

---

## 2. Dependency Preservation

Decompose R into R₁, R₂, ... with FDs F₁, F₂, ... projected onto each.
Decomposition is FD-preserving iff: (F₁ ∪ F₂ ∪ ...)⁺ = F⁺

Note:  (F₁ ∪ F₂ ...)⁺ ⊆ F⁺ always — you can never get *new* FDs by combining. The question is only whether all original FDs survive.

**Example:** R = {a,b,c,d,e}, F = {a→bc, cd→e, b→d, e→a}, R₁={a,b,c}, R₂={a,d,e}
- b→d cannot be verified in R₁ or R₂ alone → not FD-preserving.

---

## 3. Non-binary Decomposition — Chase Algorithm
https://www.youtube.com/watch?v=5zH1hvRiX7w
Successive combining method is unreliable — if it says lossless it's correct, if lossy it may be wrong. Use Chase instead.

**Algorithm:**
1. Make a table with subrelations as rows, attributes as columns
2. Put `a` where a relation contains that attribute
3. Apply each FD repeatedly. 
4. If any row becomes all `*` → lossless. 
5. Else → lossy.

**Example:** R(A,B,C,D,E), decomposition R₁(A,B), R₂(B,C,D), R₃(A,C), R₄(A,D,E) 

Initial table:

|     | A   | B   | C   | D   | E   |
| --- | --- | --- | --- | --- | --- |
| R₁  | *   | *   | #   | #   | #   |
| R₂  | #   | *   | *   | *   | #   |
| R₃  | *   | #   | *   | #   | #   |
| R₄  | *   | #   | #   | *   | *   |

Apply FDs repeatedly. If any row becomes all `*` → lossless.

**Example (lossy):** R(A,B,C,D), FD: B→AD, decomposition {A,B}, {B,C}, {C,D}

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| R₁  | *   | *   | #   | #   |
| R₂  | #   | *   | *   | #   |
| R₃  | #   | #   | *   | *   |

Apply B→AD: R₁ and R₂ both have * in B → make A and D * in both.

|   | A | B | C | D |
|---|---|---|---|---|
| R₁ | * | * | # | * |
| R₂ | * | * | * | * |

R₂ is all `*` → **lossless** ✅

> Note: The original notes concluded lossy here but applying B→AD correctly makes R₂ all * — so it's actually lossless.