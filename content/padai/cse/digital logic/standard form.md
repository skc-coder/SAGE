## Standard Forms
- **Sum of Products (SOP)**: Sum of product terms (AND terms ORed together)
- **Product of Sums (POS)**: Product of sum terms (OR terms ANDed together)

> SOP is also called *disjunctive normal form*; POS is called *conjunctive normal form*

## Minterms
- Product term containing **each variable exactly once** (complemented or uncomplemented)
- Denoted by $m_i$
- For $n$ variables: $2^n$ possible minterms
- **True minterms**: Value 1 for exactly one input combination
- **False minterms**: Value 0 for that combination

## Maxterms
- Sum term containing **each variable exactly once** (complemented or uncomplemented)
- Denoted by $M_i$
- For $n$ variables: $2^n$ possible maxterms
- **True maxterms**: Value 0 for exactly one input combination
- **False maxterms**: Value 1 for that combination

## Relationship
- $M_i = \overline{m_i}$ and $m_i = \overline{M_i}$
- Function $F$ = sum of true minterms = product of false maxterms
- Complement $\overline{F}$ = sum of false minterms = product of true maxterms


## Naming Convention
- "Minterm" refers to minimum-satisfiability (only one combination satisfies it) [1]
- "Maxterm" refers to maximum-satisfiability (all terms must be 0 for output to be 0) [1]

## Canonical Forms
- **Canonical SOP**: Sum of all true minterms (output = 1)
- **Canonical POS**: Product of all false maxterms (output = 0)

## Example: $F = A + B'C$
**Sum of Minterms**:
$$
F = A(B+B')(C+C') + (A+A')B'C = ABC + ABC' + AB'C + AB'C' + A'B'C
$$

**Sum of Maxterms**:
$$
F = (A+B'+C)(A+B'+C')(A'+B'+C)
$$
(make use of reverse distributive law)