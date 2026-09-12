# Counting Rules

**Topic:** Discrete Mathematics > Combinatorics > Foundations
**Source:** Personal notes — Combinatorics
**Tags:** #combinatorics #counting #gate-cse
**Links:** [[moc combinatorics]] | [[Permutations]] | [[Combinations]] | [[Inclusion-Exclusion Principle]]

---

> [!info] Overview
> Combinatorics is the study of counting discrete objects — strings, hands of cards, events, categorizations. Every counting problem decomposes into stages or parts, and the atoms of the problem come from one set or multiple distinct sets. This note covers the five core counting rules and the general phenomenon of overcounting that most of combinatorics is built to manage.

---

## 1. Sum Rule

Used when choosing **one** thing from disjoint alternatives, or taking the union of disjoint sets.

$$
|A \cup B| = |A| + |B| \quad \text{when } A \cap B = \varnothing
$$

If the sets overlap, the sum rule does not apply directly — inclusion-exclusion is required instead (see [[Inclusion-Exclusion Principle]]).

> [!example] City selection with overlap
> Selecting which city to visit from $\{a,b\}$ or $\{b,c\}$: total is $3$, not $4$, because $b$ is counted once, not twice.

---

## 2. Product Rule

Used when a task consists of **sequential stages** (an AND situation).

$$
\text{total} = n_1 \times n_2 \times \dots \times n_k
$$

> [!warning] Key requirement
> For each outcome of stage 1, there must be **exactly** $n_2$ ways to complete stage 2 — not "roughly $n_2$" or a range depending on the choice at stage 1. If the number of stage-2 options varies depending on the stage-1 outcome, the product rule cannot be applied directly; the problem must be split into cases instead.

Formally, if $A$ and $B$ are finite sets, the cardinality of their Cartesian product is:

$$
|A \times B| = |A| \times |B|
$$

---

## 3. Subtraction Rule (2-Set Inclusion-Exclusion)

$$
|A \cup B| = |A| + |B| - |A \cap B|
$$

This is the two-set case of the general inclusion-exclusion principle. See [[Inclusion-Exclusion Principle]] for the full treatment (3-set, 4-set, and general $n$-set formulas, plus a large set of worked applications).

> [!example] Bit string practice questions
> - How many bit strings of length 8 either start with 1 or end with 00?
> - How many bit strings start with 00 or 101?
> - How many bit strings start with 10 or end with 00?
> - How many bit strings start with 00 or 000? (Note: these two conditions overlap — a string starting with 000 also starts with 00 — so care is needed in identifying $A \cap B$.)

---

## 4. Division Rule

Used when a counting procedure counts each outcome exactly $d$ times.

$$
\text{distinct ways} = \frac{n}{d}
$$

**Set form:** If a finite set $A$ is the union of $n$ pairwise disjoint subsets, each of size $d$, then:

$$
n = \frac{|A|}{d}
$$

**Function form:** If $f: A \to B$ is a $d$-to-one function, then:

$$
|B| = \frac{|A|}{d}
$$

> [!note] Key Idea
> The division rule is most useful when a naive count *appears* to give $n$ ways, but on closer inspection each true outcome has been counted $d$ equivalent times (e.g., counting ordered selections when the actual objects being counted are unordered).

---

## 5. Complement Rule

$$
\text{desired} = \text{total} - \text{undesired}
$$

Use when the undesired cases are easier to count than the desired ones directly.

> [!warning] Caution
> The "total" must correctly represent the full universe of discourse and must cover **all** desired cases — an incorrectly scoped total (e.g., off-by-one on an inclusive/exclusive boundary) silently produces a wrong final answer even if the "undesired" count is correct.

---

## 6. Overcounting

Overcounting happens when the same object is counted multiple times across different stages or parts of a counting argument.

### 6.1 Fix 1 — Division Rule

Applicable when **every** outcome has the same fixed number of equivalent forms. Divide the raw count by that fixed factor.

### 6.2 Fix 2 — Case by Case

Applicable when the overcounting factor **varies** across outcomes (i.e., not every outcome is overcounted by the same amount). In this situation, split the problem into cases where the overcounting factor is constant within each case, and sum the corrected counts.

> [!note] Requirements for valid case splitting
> Cases must be:
> - **Exhaustive** — every outcome falls into at least one case.
> - **Mutually disjoint** — no outcome falls into more than one case.
>
> If cases overlap, apply inclusion-exclusion (or a Venn diagram) across the cases rather than simply summing them.

---

## Related Notes

- [[moc combinatorics]]
- [[Permutations]]
- [[Combinations]]
- [[Inclusion-Exclusion Principle]]

## Open Questions

- [ ] Work through the four bit-string subtraction-rule practice questions listed in Section 3 and record final numeric answers.
- [ ] Reconcile this note with the pre-existing [[combinatorics/combinatorics]] and [[Combinatorics practice]] notes in the vault to check for duplicate or conflicting content.
