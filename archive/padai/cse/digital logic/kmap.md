## Adjacency Principle
Two minterms (or max terms) $m_i$ and $m_j$ are **adjacent** if their binary representations differ by **exactly one variable**.

> Example: $m_1 = \overline{a}\overline{b}c$ and $m_3 = \overline{a}bc$ → differ only in $b$ → can be combined → result: $\overline{a}c$

> $m_0 = \overline{a}\overline{b}\overline{c}$ and $m_3 = \overline{a}bc$ → differ in two variables → **not adjacent** → cannot be combined

## Key Insight
Combining adjacent minterms eliminates the variable that changes between them — this is the core of K-map minimization.

![[Pasted image 20260418094354.png]]