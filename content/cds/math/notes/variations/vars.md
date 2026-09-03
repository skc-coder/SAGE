# Set Theory Variations & Trap Patterns

## Variation 1: Power Set Element vs Subset Trap
- **Trap**: Distinguishing between $x \in \mathcal{P}(A)$ and $x \subseteq \mathcal{P}(A)$.
- **Example**: Let $A = \{a, \{b\}\}$.
  - Subsets of $A$: $\emptyset, \{a\}, \{\{b\}\}, \{a, \{b\}\}$.
  - Power set $\mathcal{P}(A) = \{\emptyset, \{a\}, \{\{b\}\}, \{a, \{b\}\}\}$.
  - $\{a\} \in \mathcal{P}(A)$ is TRUE, but $\{a\} \subseteq \mathcal{P}(A)$ is FALSE (since $a \notin \mathcal{P}(A)$).
  - $\{\{a\}\} \subseteq \mathcal{P}(A)$ is TRUE.

## Variation 2: Algebraic Simplification of Complex Set Expressions
- **Pattern**: Expression involving multiple complements, unions, and set differences (like $Q34$ or $Q59$).
- **Rule of Thumb**: Convert all set differences $P - Q$ into $P \cap Q'$, then apply De-Morgan's laws and Distributive laws.

## Variation 3: Bounded Optimisation in 3-Variable Venn Diagrams
- **Pattern**: Problems asking for range $a \le x \le b$ of intersection of 2 sets in a 3-set system.
- **Recipe**:
  1. Express triple intersection $g = n(A \cap B \cap C)$ using 3-set inclusion-exclusion formula.
  2. Set $g \ge 0$ for lower bound on pairwise intersection.
  3. Set pairwise intersection $\le \min(n(A), n(B))$ for upper bound.
