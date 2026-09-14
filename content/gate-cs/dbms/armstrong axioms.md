### Primary Rules (RAT)

**Reflexivity** — If β ⊆ α then α → β (trivial FD)

**Augmentation** — If α → β then αγ → βγ (adding attributes doesn't break FD)

**Transitivity** — If α → β and β → γ then α → γ

These three are **sound and complete** — enough to derive all FDs.

### Secondary Rules (derived from RAT)

**Union** — If α → β and α → γ then α → βγ

**Decomposition** — If α → βγ then α → β and α → γ

**Pseudo Transitivity** — If α → β and γβ → δ then αγ → δ

**Composition** — If α → β and x → y then αx → βy