CK of R is a minimal subset X such that X⁺ = R (covers all attributes, no proper subset does the same).

- **Sub-key**: proper subset of a CK
- **Super-key**: any set containing a CK

### Attribute Classification (for finding CKs efficiently)

| Type              | Definition                                                                    |
| ----------------- | ----------------------------------------------------------------------------- |
| **Necessary**     | Never appears on RHS of any FD (or absent from all FDs) — must be in every CK |
| **Useless**       | Appears ONLY on RHS — never part of any CK                                    |
| **Middle-ground** | Neither necessary nor useless                                                 |

**Example:** R(ABCDEG), F = {AB→C, C→D, AD→E}
- Necessary: A, B, G — Useless: E — Middle-ground: C, D

### Algorithm to find all CKs

1. Classify attributes into necessary (X), useless (Y), middle-ground (M)
2. Compute X⁺. If X⁺ = R → X is the only CK, done.
3. Else enumerate subsets of M (each expanded with X), test closure, keep minimal ones that give R.

**Example:** R(ABCDEG), F minimal = {A→B, A→D, B→C, C→E, BD→A}
- G never appears → necessary. E only on RHS → useless. X = {G}, M = {A,B,C,D}
- G⁺ = G ≠ R, so enumerate subsets of M with G added.
- AG⁺ = ABCDEG = R ✅ → AG is CK
- BDG⁺ = ABCDEG = R ✅ → BDG is CK
- Final: K = {AG, BDG}
