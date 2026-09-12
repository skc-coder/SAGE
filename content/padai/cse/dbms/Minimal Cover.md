A minimal cover of F is a simplified equivalent set of FDs with no redundancy. RHS must be single attribute always.

Two things to eliminate:
1. **Extraneous (redundant) attributes** on LHS
2. **Redundant FDs**

### Finding Extraneous Attributes

To test if A ∈ α is extraneous in α → β:
Compute (α − A)+ using F. If it contains β, then A is extraneous. 
We still keep α → β in F, because we start from the full FD set to arrive have (α − A)→ β. 

**Example:** F = {AB→C, C→A, BC→D, ACD→B, D→E, D→G, BE→C, CG→B, CG→D, CE→A, CE→G}

Is A extraneous in ACD→B?
- Compute CD+ = ACDEGB ✅ contains B, so A is extraneous → replace ACD→B with CD→B
- Proof: C→A, augment: CD→ACD, then ACD→B, by transitivity: CD→B ✅

### Finding Redundant FDs

To check if an FD α→β is redundant in F:

**Remove it from F, then compute α+ using remaining FDs. If α+ still contains β, the FD is redundant.**

---

**Example from above:**

F = {AB→C, C→A, BC→D, ACD→B, D→E, D→G, BE→C, CG→B, CG→D, CE→A, CE→G}

**Is CE→A redundant?** Remove CE→A from F. Compute CE+ using remaining FDs.

- C→A fires → CE+ = ACE... contains A ✅
- So CE→A is redundant.

**Is CG→B redundant?** Remove CG→B from F. Compute CG+ using remaining FDs.

- CG→D fires → add D → CGD
- D→E fires → add E → CGDE
- D→G fires (already have G)
- C→A fires → add A → ACGDE
- ACD→B fires (have A,C,D) → add B ✅
- CG+ contains B → CG→B is redundant.

**Is CG→D redundant?** Remove CG→D from F. Compute CG+ using remaining FDs.

- CG→B fires → add B → BCG
- BC→D fires → add D ✅
- CG+ contains D → CG→D is redundant.

---

**Key point:** CG→B and CG→D are each individually redundant given the other exists. But you can't remove both — removing one makes the other necessary. That's why two minimal covers exist.

### Two Valid Minimal Covers

**Cover 1** (keep CG→D, derive CG→B as redundant):
```
{AB→C, C→A, BC→D, CD→B, D→E, D→G, BE→C, CG→D, CE→G}
```

**Cover 2** (keep CG→B, derive CG→D and ACD→B as redundant):
```
{AB→C, C→A, BC→D, D→E, D→G, BE→C, CG→B, CE→G}
```

Both are valid. Minimal cover is not unique. Key insight: can't eliminate both CG→D and CG→B.

---

## Equivalence of FD Sets

F and G are equivalent if F+ = G+. Instead of computing full closure (expensive), check if every FD in F is derivable from G and vice versa using attribute closures.

**Example:**
F = {A→B, B→C, AC→D} and G = {A→B, B→C, A→D}

Using G to derive F:
- A+ = ABCD → covers A→B, A→C, A→D ✅
- B+ = BC → covers B→C ✅
- AC+ = ABCD → covers AC→D ✅

Using F to derive G:
- A+ = ABCD → covers A→B, A→D ✅
- B+ = BC → covers B→C ✅

Both directions hold → **F and G are equivalent.**

**Counter Example:**
F = {A→B, A→C} and G = {A→B, B→C}

- A+ using F = ABC, but B+ using F = B only
- B→C from G is **not** derivable from F → **not equivalent**