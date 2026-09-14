## Definition
Function $F$ **covers** function $G$ iff:
- Whenever $G = 1$, then $F = 1$  
**OR**
- Whenever $F = 0$, then $G = 0$

> Equivalent to: $G \Rightarrow F$ (logical implication)

## Examples
- $F = a + ab$, $G = a$ → $F$ covers $G$
- $F = a + b$, $G = a$ → $F$ covers $G$
- $F = x + \overline{z}$, $G = x + y + \overline{z}$ → $G$ covers $F$

## Covering in Canonical Forms
- If $F = \sum(1,2,3,4,6)$, then any $G$ with minterms  ⊇ {1,2,3,4,6} is covered by $F$
- If $F = \prod(0,5,7)$, then any $G$ with maxterms ⊇ {0,5,7} covers $F$

## Don’t Care Context
In minimization, “covers” is used to include don’t care terms — they can be treated as 1s if helpful, since covering only requires $F=1$ when $G=1$.

Think of taking dont care terms as making the function more strict (by covering) for minimization benefits.