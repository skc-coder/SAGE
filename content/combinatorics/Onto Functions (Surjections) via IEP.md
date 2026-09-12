# Onto Functions (Surjections) via IEP

**Topic:** Discrete Mathematics > Combinatorics > IEP Applications
**Source:** GO Classes — Discrete Mathematics, Combinatorics (IEP Application Lecture)
**Tags:** #combinatorics #functions #IEP #gate-cse
**Links:** [[Inclusion-Exclusion Principle]] | [[Derangements]] | [[moc combinatorics]]

---

> [!info] Overview
> An onto (surjective) function $f: A \to B$ hits every element of $B$ at least once. Counting onto functions directly is awkward, but counting the complement — functions that **miss** at least one element of $B$ — is a clean IEP application. This note covers the derivation, the "distinct objects into distinct boxes" (DODB) alternative method, and worked GATE-style examples.

---

## 1. Definition

$f: A \to B$ is **onto (surjective)** if:

$$
\forall y \in B, \; \exists x \in A \text{ such that } f(x) = y
$$

In words: every element of the codomain $B$ has at least one preimage in $A$.

---

## 2. Core Strategy

$$
\#\text{onto functions} = \text{Total functions} - \#\text{NOT onto}
$$

"NOT onto" means **at least one** element of $B$ has no preimage. If $B = \{b_1, \dots, b_n\}$, define events $\overline{b_i}$ = "$b_i$ has no preimage." Then:

$$
\#\text{onto} = |B|^{|A|} - \left|\overline{b_1} \cup \overline{b_2} \cup \dots \cup \overline{b_n}\right|
$$

The union on the right is computed via IEP, since these "missing element" events overlap.

---

## 3. Worked Example — 2-Element Codomain

> [!example] $X=\{1,2,3,4\} \to Y=\{a,b\}$
> **Question:** How many onto functions are there from a 4-element set to a 2-element set?
>
> **Approach:**
> $$
> \#\text{onto} = \text{Total} - (\overline{a} \cup \overline{b})
> $$
>
> $$
> \text{Total} = 2^4
> $$
>
> $\overline{a}$: functions where $a$ has no preimage $\implies$ every element of $X$ maps only to $b$ $\implies 1^4 = 1$ way (the constant function to $b$).
> $\overline{b}$: symmetric, $1^4 = 1$ way.
> $\overline{a} \cap \overline{b}$: **neither** $a$ nor $b$ has a preimage — impossible since $Y=\{a,b\}$ has no other elements to map to. Count $= 0$.
>
> $$
> \overline{a} \cup \overline{b} = \overline{a} + \overline{b} - \overline{a \cap b} = 1 + 1 - 0 = 2
> $$
>
> $$
> \#\text{onto} = 2^4 - 2 = 14
> $$
>
> **Answer:** $\boxed{14}$

---

## 4. GATE PYQ — 3-Element Codomain

> [!example] GATE CSE 2015 Set 2 — Q40
> **Question:** The number of onto functions from $X=\{1,2,3,4\}$ to $Y=\{a,b,c\}$ is ______.
>
> **Method 1 — DODB (Distinct Objects into Distinct Boxes) template:**
>
> Since $|X|=4 > |Y|=3$, an onto function must have exactly one $Y$-element receiving 2 preimages and the other two receiving 1 each (the only way to distribute 4 distinct objects onto 3 distinct nonempty boxes without any box empty). There are 3 ways to choose **which** box gets 2 elements:
>
> | $a$ | $b$ | $c$ |
> | :--- | :--- | :--- |
> | 2 | 1 | 1 |
> | 1 | 2 | 1 |
> | 1 | 1 | 2 |
>
> For a fixed distribution pattern (say $2,1,1$), the number of ways to assign the 4 distinct elements of $X$ into these differently-labeled group sizes is a multinomial coefficient:
>
> $$
> x = \frac{4!}{2!\,(1!)^2} = 12
> $$
>
> Since there are 3 such patterns (one for each choice of which letter gets the pair):
>
> $$
> \text{Final Answer} = 3 \times 12 = 36
> $$
>
> **Method 2 — IEP:**
>
> $$
> \#\text{onto} = \text{Total} - (\overline{a} \cup \overline{b} \cup \overline{c}) = 3^4 - (\overline{a}\cup\overline{b}\cup\overline{c})
> $$
>
> Single term: $\overline{a}$ = functions mapping $X$ into $\{b,c\}$ only $= 2^4$.
> Pair term: $\overline{a} \cap \overline{c}$ = functions mapping $X$ into $\{b\}$ only $= 1^4 = 1$.
> Triple term: $\overline{a}\cap\overline{b}\cap\overline{c}$ = impossible (no elements left to map to) $= 0$.
>
> $$
> \overline{a}\cup\overline{b}\cup\overline{c} = \underbrace{(3 \times 2^4)}_{\text{singles}} - \underbrace{(3 \times 1)}_{\text{pairs}} + \underbrace{0}_{\text{triple}} = 48 - 3 = 45
> $$
>
> $$
> \#\text{onto} = 3^4 - 45 = 81 - 45 = 36
> $$
>
> **Answer:** $\boxed{36}$

> [!note] Key Idea
> Both methods agree ($36$), which is a good sanity check. DODB is faster when the codomain is small (few distribution patterns to enumerate); IEP is more systematic and scales better when direct case enumeration would get complicated (see the 6→3 example below, where DODB has 3 messy cases vs. one clean IEP expression).

---

## 5. Jobs-to-Employees Assignment (5 → 4, at least one job each)

> [!example] 5 different jobs, 4 different employees, everyone gets ≥1 job
> **Question:** How many ways to assign 5 different jobs to 4 different employees if every employee is assigned at least one job?
>
> **Reframing:** This is exactly an onto function from the set of 5 jobs to the set of 4 employees (each job maps to exactly one employee; "every employee assigned ≥1 job" = onto).
>
> **Method 1 — DODB:**
>
> With 5 distinct jobs into 4 distinct employees, all onto, the distribution pattern must be one employee getting 2 jobs and the rest getting 1 each:
>
> | A | B | C | D |
> | :--- | :--- | :--- | :--- |
> | 2 | 1 | 1 | 1 |
> | 1 | 2 | 1 | 1 |
> | 1 | 1 | 2 | 1 |
> | 1 | 1 | 1 | 2 |
>
> 4 such patterns. For a fixed pattern:
>
> $$
> x = \frac{5!}{2!\,(1!)^3} = 60
> $$
>
> $$
> \text{Final Answer} = 4 \times 60 = 240
> $$
>
> **Method 2 — IEP:**
>
> $$
> \#\text{onto} = 4^5 - (\overline{a}\cup\overline{b}\cup\overline{c}\cup\overline{d})
> $$
>
> $$
> \overline{a}\cup\overline{b}\cup\overline{c}\cup\overline{d} = \binom{4}{1}3^5 - \binom{4}{2}2^5 + \binom{4}{3}1^5 - \binom{4}{4}0^5
> $$
>
> (The last term is $0$ because it's impossible for all 4 employees to simultaneously have no jobs when 5 jobs must go somewhere.)
>
> $$
> \#\text{onto} = 4^5 - \left[\binom{4}{1}3^5 - \binom{4}{2}2^5 + \binom{4}{3}1^5\right] = 1024 - [4(243) - 6(32) + 4(1)]
> $$
>
> $$
> = 1024 - [972 - 192 + 4] = 1024 - 784 = 240
> $$
>
> **Answer:** $\boxed{240}$

---

## 6. Onto Functions from a 6-Element Set to a 3-Element Set

> [!example] Rosen Example — 6 → 3 onto functions
> **Question:** How many onto functions are there from a set with six elements to a set with three elements?
>
> **Why DODB struggles here:** With $|A|=6, |B|=3$, the valid distribution patterns include $(4,1,1)$, $(2,2,2)$, and $(1,2,3)$ — multiple structurally different cases, each needing separate multinomial counts and separate handling of "how many distinct label-assignments of that pattern." This is **error-prone and inefficient** for larger gaps between domain and codomain size.
>
> **IEP method (preferred here):**
>
> Let $P_i$ = "element $b_i$ is not in the range" for $i=1,2,3$.
>
> $$
> N(P_1'P_2'P_3') = N - \big[N(P_1)+N(P_2)+N(P_3)\big] + \big[N(P_1P_2)+N(P_1P_3)+N(P_2P_3)\big] - N(P_1P_2P_3)
> $$
>
> - $N = 3^6$ (total functions)
> - $N(P_i) = 2^6$ (functions avoiding one specific element of $B$; there are $\binom{3}{1}$ such terms)
> - $N(P_iP_j) = 1^6 = 1$ (functions avoiding two specific elements, i.e., constant functions; $\binom{3}{2}$ such terms)
> - $N(P_1P_2P_3) = 0$ (impossible — no target left for any element)
>
> $$
> \#\text{onto} = 3^6 - \binom{3}{1}2^6 + \binom{3}{2}1^6 - 0 = 729 - 3(64) + 3(1) - 0
> $$
>
> $$
> = 729 - 192 + 3 = 540
> $$
>
> **Answer:** $\boxed{540}$

---

## 7. General Formula (Reference)

For onto functions from an $m$-element set to an $n$-element set:

$$
\#\text{onto} = \sum_{k=0}^{n} (-1)^k \binom{n}{k}(n-k)^m
$$

This is the **Stirling-numbers-of-the-second-kind**-adjacent formula; the lecture builds it up case by case (2→ and 3→ codomains) rather than stating this closed form directly, but every worked example above is an instance of it.

| $m \to n$ | Formula instance | Result |
| :--- | :--- | :--- |
| $4 \to 2$ | $2^4 - \binom{2}{1}1^4$ | $14$ |
| $4 \to 3$ | $3^4 - \binom{3}{1}2^4 + \binom{3}{2}1^4$ | $36$ |
| $5 \to 4$ | $4^5 - \binom{4}{1}3^5 + \binom{4}{2}2^5 - \binom{4}{3}1^5$ | $240$ |
| $6 \to 3$ | $3^6 - \binom{3}{1}2^6 + \binom{3}{2}1^6$ | $540$ |

---

## Related Notes

- [[Inclusion-Exclusion Principle]]
- [[Derangements]]
- [[moc combinatorics]]

## Open Questions

- [ ] Derive and store the general Stirling-number-based onto-function formula as its own reference note, since the lecture only builds specific instances.
- [ ] Practice the DODB method on a case where the domain-codomain gap is larger (e.g., $7 \to 3$) to compare effort against the IEP method directly.
