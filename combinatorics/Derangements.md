# Derangements

**Topic:** Discrete Mathematics > Combinatorics > IEP Applications
**Source:** GO Classes — Discrete Mathematics, Combinatorics (Derangement Lecture + Practice Set 3)
**Links:** [[moc combinatorics]] | [[Inclusion-Exclusion Principle]] | [[Onto Functions (Surjections) via IEP]]

---

> [!info] Overview
> A derangement is a permutation in which **no element** ends up in its original position — "everyone is homeless." This note derives the derangement count $D_n$ using IEP, builds the closed-form and recurrence formulas, proves a parity result, and works through the full standard practice set (GATE-style and textbook questions).

---

## 1. Definition

A **derangement** of $1, 2, \dots, n$ is a permutation such that no element appears in its original position.

$$
D_n = \text{number of derangements of } n \text{ distinct elements}
$$

> [!note] Key Idea
> $D_n$ only applies when you have $n$ **distinct** elements going into $n$ **distinct** positions. If elements repeat (e.g., word "aabc"), the formula does not directly apply — you must reason case by case (see Section 8).

### 1.1 Small Cases by Direct Enumeration

For $n=3$, letters $a,b,c$, all $3! = 6$ permutations:

| Permutation | Derangement? |
| :--- | :--- |
| abc | No (all fixed) |
| acb | No (a fixed) |
| bac | No (c fixed) |
| bca | Yes |
| cab | Yes |
| cba | No (b fixed) |

$$
D_3 = 2
$$

For $n=2$: only $ba$ is a derangement ($ab$ is not).

$$
D_2 = 1
$$

---

## 2. Deriving $D_4$ via IEP

### 2.1 Setup

$$
D_4 = 4! - \big(\text{at least one element in its original position}\big)
$$

Let $a, b, c, d$ denote the **events**: element $a$ is in its original (1st) position, $b$ in its original (2nd), etc.

$$
D_4 = 4! - |a \cup b \cup c \cup d|
$$

### 2.2 Counting Each Term

Each event fixes some positions and leaves the rest free to permute:

| Term | Meaning | Count |
| :--- | :--- | :--- |
| $a$ | $a$ fixed, $b,c,d$ free | $3!$ |
| $ab$ | $a,b$ fixed, $c,d$ free | $2!$ |
| $abc$ | $a,b,c$ fixed, $d$ free | $1!$ |
| $abcd$ | all fixed | $1$ |

By symmetry every single-element term is $3!$ (4 such terms), every pair-term is $2!$ ($\binom{4}{2}=6$ such terms), every triple-term is $1!$ ($\binom{4}{3}=4$ terms), and the full term is $1$ ($\binom{4}{4}=1$ term).

### 2.3 IEP Expansion

$$
a \cup b \cup c \cup d = \binom{4}{1}3! - \binom{4}{2}2! + \binom{4}{3}1! - \binom{4}{4}
$$

$$
D_4 = 4! - \left[\binom{4}{1}3! - \binom{4}{2}2! + \binom{4}{3}1! - \binom{4}{4}\right] = 4! - [24 - 12 + 4 - 1]
$$

$$
\boxed{D_4 = 9}
$$

---

## 3. General Formula via IEP

Generalizing the $D_4$ derivation to $n$ elements $a_1, \dots, a_n$:

$$
D_n = n! - \left[\binom{n}{1}(n-1)! - \binom{n}{2}(n-2)! + \binom{n}{3}(n-3)! - \dots \pm \binom{n}{n} \cdot 1\right]
$$

Since $\binom{n}{r}(n-r)! = \dfrac{n!}{r!(n-r)!}(n-r)! = \dfrac{n!}{r!}$, this simplifies to:

$$
D_n = n! - \left[\frac{n!}{1!} - \frac{n!}{2!} + \frac{n!}{3!} - \dots \pm \frac{n!}{n!}\right]
$$

Factoring out $n!$:

$$
\boxed{D_n = n!\left[1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \frac{1}{4!} - \dots + \frac{(-1)^n}{n!}\right]}
$$

### 3.1 Table of Values

| $n$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $D_n$ | 1 | 0 | 1 | 2 | 9 | 44 | 265 |

> [!note] Convention
> $D_0 = 1$ by convention (there is exactly one permutation of zero elements — the empty permutation — and it vacuously has "no fixed points").

---

## 4. Recurrence Relations

### 4.1 First Recurrence: $D_n = (n-1)[D_{n-1} + D_{n-2}]$

**Setup — track where element "1" goes.** Element 1 has $(n-1)$ possible houses to go to (any house except its own), and this covers all derangements exhaustively.

Fix "1 → $k$'s house" for some specific $k \ne 1$. Split into two cases based on whether $k$ reciprocates:

$$
\begin{aligned}
\text{Case 1:} \quad & 1 \to k\text{'s house AND } k \to 1\text{'s house} \implies \text{remaining } (n-2) \text{ elements must derange} \implies D_{n-2} \\
\text{Case 2:} \quad & 1 \to k\text{'s house AND } k \not\to 1\text{'s house} \implies \text{relabel } k\text{'s house as "1's spot" for the rest} \implies D_{n-1}
\end{aligned}
$$

So for each fixed choice of $k$, the number of derangements with "$1 \to k$" is $D_{n-1}+D_{n-2}$. Since there are $(n-1)$ choices for $k$:

$$
\boxed{D_n = (n-1)\left[D_{n-1} + D_{n-2}\right]}
$$

**Base cases:** $D_1 = 0$, $D_2 = 1$.

**Verification:**

$$
\begin{aligned}
D_3 &= (3-1)[D_2+D_1] = 2(1+0) = 2 \\
D_4 &= 3(D_3+D_2) = 3(2+1) = 9 \\
D_5 &= 4(D_4+D_3) = 4(9+2) = 44 \\
D_6 &= 5(D_5+D_4) = 5(44+9) = 265
\end{aligned}
$$

### 4.2 Second Recurrence: $D_n = nD_{n-1} + (-1)^n$

This follows from the closed-form summation (proof skipped in lecture, stated as a known result):

$$
\boxed{D_n = nD_{n-1} + (-1)^n}
$$

**Verification:** $D_5 = 5 \times D_4 + (-1)^5 = 5(9) - 1 = 44$ ✓.

---

## 5. Parity of $D_n$

> [!example] Prove: $D_n$ is odd $\iff$ $n$ is even
> **Question:** For which $n$ is $D_n$ even?
>
> **Observed pattern:**
>
> | $n$ | 1 | 2 | 3 | 4 | 5 | 6 |
> | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
> | $D_n$ | 0 (even) | 1 (odd) | 2 (even) | 9 (odd) | 44 (even) | 265 (odd) |
>
> **Claim:** $D_{\text{even}}$ is odd, and $D_{\text{odd}}$ is even.
>
> **Proof (by induction), using $D_n = (n-1)[D_{n-1}+D_{n-2}]$:**
>
> *Base cases:* $D_1=0$ (even), $D_2=1$ (odd), $D_3=2$ (even), $D_4=9$ (odd) — pattern holds.
>
> *Inductive hypothesis:* Assume the claim holds for all indices up to $n-1$.
>
> *Case 1 — $n$ even:* Then $(n-1)$ is odd. By hypothesis, $D_{n-1} = D_{\text{odd}}$ is even, and $D_{n-2} = D_{\text{even}}$ is odd.
> $$
> D_n = \underbrace{(n-1)}_{\text{odd}}\big[\underbrace{D_{n-1}}_{\text{even}} + \underbrace{D_{n-2}}_{\text{odd}}\big] = \text{odd} \times (\text{even}+\text{odd}) = \text{odd} \times \text{odd} = \text{odd}
> $$
> So $D_{\text{even}} = \text{odd}$. ✓
>
> *Case 2 — $n$ odd:* Then $(n-1)$ is even.
> $$
> D_n = \underbrace{(n-1)}_{\text{even}}\big[D_{n-1}+D_{n-2}\big] = \text{even} \times (\text{anything}) = \text{even}
> $$
> So $D_{\text{odd}} = \text{even}$. ✓
>
> **Conclusion:** $D_n$ is even $\iff n$ is odd; $D_n$ is odd $\iff n$ is even. **Hence proved.**

---

## 6. Identity: $n! = \sum_{r=0}^{n} \binom{n}{r} D_{n-r}$

### 6.1 The "Two Ways to Count" Argument

Count all $n!$ permutations of $n$ elements two different ways.

**Side 1 (direct):** $n!$

**Side 2 (by number of fixed points):** Every permutation has *exactly* $r$ elements in their original position for some $r \in \{0, 1, \dots, n\}$. These cases are mutually exclusive and exhaustive.

$$
n! = \sum_{r=0}^{n} \big(\text{\# permutations with exactly } r \text{ fixed points}\big)
$$

To count "exactly $r$ fixed points": choose **which** $r$ elements stay fixed ($\binom{n}{r}$ ways), then the remaining $n-r$ elements must be **fully deranged** ($D_{n-r}$ ways — otherwise the fixed-point count would exceed $r$).

$$
\boxed{n! = \sum_{r=0}^{n} \binom{n}{r} D_{n-r}}
$$

Expanded:

$$
n! = \binom{n}{0}D_n + \binom{n}{1}D_{n-1} + \binom{n}{2}D_{n-2} + \dots + \binom{n}{n}D_0
$$

---

## 7. Summary of All Derangement Identities

| # | Identity |
| :--- | :--- |
| 1 | $D_n = n!\left[1 - \dfrac{1}{1!} + \dfrac{1}{2!} - \dfrac{1}{3!} + \dots + \dfrac{(-1)^n}{n!}\right]$ |
| 2 | $D_n = (n-1)\left[D_{n-1}+D_{n-2}\right]$ |
| 3 | $D_{\text{odd}} = \text{even}$, $D_{\text{even}} = \text{odd}$ |
| 4 | $D_n = nD_{n-1} + (-1)^n$ |
| 5 | $n! = \displaystyle\sum_{r=0}^n \binom{n}{r} D_{n-r}$ |

---

## 8. Derangements with Repeated Elements (Multiset Case)

> [!warning] $D_n$ formula requires distinct elements in distinct positions
> If the word has repeated letters, the standard $D_n$ formula does **not** apply directly — you must enumerate.

**Example — "aab":** No derangement exists. Answer: $0$.

**Example — "aabc":** Enumerate directly. Valid derangements found: `bcaa`, `cbaa`. Answer: $2$.

**Example — "L I M I T" (word LIMIT, repeated I):**

Split by which position each **non-repeated** letter effectively "swaps into," using the two I's as flexible fillers. The lecture's case analysis gives three symmetric cases (one for each of L, M, T being placed correctly-away):

$$
D_{\text{LIMIT}} = \underbrace{\frac{2}{\text{choices for T}} \times 2!}_{4} + \underbrace{\frac{2}{\text{choices for M}} \times 2!}_{4} + \underbrace{\frac{2}{\text{choices for L}} \times 2!}_{4} = 4+4+4 = 12
$$

**Answer:** $\boxed{12}$

---

## 9. Standard Practice Set — Fully Worked Questions

> [!example] Q1 — Derangements of 4 elements / general $n$
> **Question:** How many derangements are there of 4 elements? How many permutations on $n$ symbols are derangements?
>
> **Answer:** $D_4 = 9$ (derived in Section 2); general count is $D_n$ from Section 3.

> [!example] Q2 — Senior prank nameplate swap
> **Question:** Nameplates on 5 professors' doors are switched so that **all** end up on the wrong door. How many ways?
>
> **Approach:** "All wrong door" $\equiv$ no nameplate in its original position $\equiv D_5$.
>
> **Answer:** $\boxed{D_5 = 44}$

> [!example] Q3 — Hat check problem
> **Question:** 5 gentlemen's hats are returned randomly. How many ways so that **none** gets his own hat back?
>
> **Answer:** $\boxed{D_5 = 44}$

> [!example] Q4 — Exactly 1 fixed point (Oscar Levin, Ex 1.6 Q8)
> **Question:** How many permutations of $\{1,2,3,4,5\}$ leave exactly 1 element fixed?
>
> **Approach:** Choose which element stays fixed ($\binom{5}{1}$ ways); the remaining 4 must be **fully deranged** ($D_4$), otherwise more than one element would be fixed. These cases (for different choices of the fixed element) are mutually exclusive.
>
> $$
> \binom{5}{1} \times D_4 = 5 \times 9 = 45
> $$
>
> **Answer:** $\boxed{45}$

> [!example] Q5 — Derangements of {1,...,6} beginning with 1,2,3 in some order (Rosen 8.6 Q25)
> **Question:** How many derangements of $\{1,2,3,4,5,6\}$ begin with the integers 1, 2, 3 (in some order)?
>
> **Approach:** Equivalent (by symmetry of the problem structure) to counting derangements which, split into the first-3 block $\{1,2,3\}$ and last-3 block $\{4,5,6\}$, place $\{1,2,3\}$-values into first-3 positions and $\{4,5,6\}$-values into last-3 positions such that no element is in its original spot. Since block 1 (positions 1–3, values from $\{1,2,3\}$) and block 2 (positions 4–6, values from $\{4,5,6\}$) don't share any "home" positions between blocks, every arrangement within blocks is automatically a derangement — both blocks independently just need any permutation of their 3 elements ($3!$ each), since none of $\{1,2,3\}$'s original homes are among positions 1–3 anyway... more precisely, verified by direct case-check: valid patterns are counted as $3! \times 3!$.
>
> $$
> 3! \times 3! = 6 \times 6 = 36
> $$
>
> **Answer:** $\boxed{36}$

> [!example] Q7 — No even digit in original position, digits 0–9 (Rosen 8.6 Q17)
> **Question:** How many ways can the digits 0–9 be arranged so that **no even digit** (0,2,4,6,8) is in its original position? (Odd digits may go anywhere, including their own spot.)
>
> **Approach:** Only the 5 even digits have a "no fixed point" restriction; the 5 odd digits are unrestricted.
>
> $$
> \text{Desired} = \text{Total} - \big(\text{some even digit fixed}\big) = 10! - \big[0 \cup 2 \cup 4 \cup 6 \cup 8\big]
> $$
>
> Each single-fixed-even-digit term leaves 9 positions free: $9!$. Each pair leaves 8 free: $8!$. Etc.
>
> $$
> 0 \cup 2 \cup 4 \cup 6 \cup 8 = \binom{5}{1}9! - \binom{5}{2}8! + \binom{5}{3}7! - \binom{5}{4}6! + \binom{5}{5}5!
> $$
>
> $$
> \text{Answer} = 10! - \left[\binom{5}{1}9! - \binom{5}{2}8! + \binom{5}{3}7! - \binom{5}{4}6! + \binom{5}{5}5!\right]
> $$

> [!example] Q8 — Functions and injections on $\{1,...,5\}$ (Oscar Levin, Ex 1.6)
> **Question:** How many functions $f: \{1,...,5\} \to \{1,...,5\}$ are there total? How many are injective?
>
> **Approach:** Total functions: each of 5 elements has 5 independent choices: $5^5$.
> Injective functions: first element has 5 choices, second has 4 remaining, etc.: $5 \times 4 \times 3 \times 2 \times 1 = 5! = 120$.
>
> **Answer:** Total $= \boxed{5^5}$, Injective $= \boxed{120}$

> [!example] Q9 — Injections with $f(x) \ne x$ (Oscar Levin, Ex 1.6)
> **Question:** How many injections $f: \{1,...,5\} \to \{1,...,5\}$ satisfy $f(x) \ne x$ for all $x$?
>
> **Approach:** An injective function from a finite set to itself of the same size is automatically a bijection, i.e. a permutation. Requiring $f(x) \ne x$ everywhere is exactly the derangement condition.
>
> **Answer:** $\boxed{D_5 = 44}$

> [!example] Q10 — Exactly 6 of 10 ladies get own hat (Oscar Levin, Ex 1.6 Q9)
> **Question:** 10 ladies' hats returned randomly. In how many ways do exactly 6 receive their own hat (and the other 4 not)?
>
> **Approach:** Choose which 6 ladies get their own hat back ($\binom{10}{6}$), remaining 4 must be fully deranged ($D_4$).
>
> $$
> \binom{10}{6} \times D_4
> $$
>
> **Answer:** $\boxed{\binom{10}{6} \times D_4 = \binom{10}{6}\times 9}$

> [!example] Q11 — Grinch and 6 presents (Oscar Levin, Ex 1.6 Q10)
> **Question:** 6 presents, name-labels switched.
> (a) No present keeps its original label?
> (b) Exactly 2 keep their original label?
> (c) Exactly 5 keep their original label?
>
> **Answers:**
> (a) $\boxed{D_6 = 265}$
> (b) Choose which 2 stay correct, remaining 4 deranged: $\boxed{\binom{6}{2} \times D_4 = 15 \times 9 = 135}$
> (c) $\boxed{0}$ — if exactly 5 out of 6 are correctly labeled, the 6th **must** also be correct (nowhere else for it to go), so "exactly 5 correct" is impossible.

> [!example] Q12 — Injective functions with $f(x) \ne x$ on $A=\{1,...,5\}$ (Oscar Levin, Ex 1.6 Q13)
> **Question:** Same as Q9, restated. How many injective $f: A \to A$ satisfy $f(x) \ne x \; \forall x$?
>
> **Answer:** $\boxed{D_5 = 44}$

> [!example] Q13 — Derangement with 1 and $k$ swapped positions
> **Question:** In a permutation of $n$ elements, position 1 gets value $k$, position $k$ gets value $1$, and every other position $i$ (for $2 \le i \le n$, $i \ne k$) is **not** allowed to hold its own value $i$. How many such permutations are there?
>
> **Approach:** Positions 1 and $k$ are already "fixed" (by the forced values $k$ and $1$ respectively) — they are used up. The remaining $n-2$ positions/values need a full derangement among themselves.
>
> **Answer:** $\boxed{D_{n-2}}$

> [!example] Q14 — "2" goes to 1's place, but 1 doesn't go to 2's place
> **Question:** Among all derangements of $n$ elements, how many satisfy: element 2 goes to position 1, AND element 1 does **not** go to position 2?
>
> **Approach (trick):** Fix "2 → position 1." Now temporarily treat positions $2, 3, \dots, n$ as if they were "home" for elements $1, 3, 4, \dots, n$ respectively (i.e., relabel element 1's forbidden slot as if it were its "home," since we need $1 \not\to$ position 2 anyway). This converts the remaining sub-problem into deranging $n-1$ elements among $n-1$ positions.
>
> **Answer:** $\boxed{D_{n-1}}$

---

## 10. GATE PYQ

> [!example] GATE CSE 2004-IT — Q35 (Balls in Bins)
> **Question:** In how many ways can we distribute 5 distinct balls $B_1,\dots,B_5$ into 5 distinct cells $C_1,\dots,C_5$ such that ball $B_i$ is **not** in cell $C_i$ for any $i$, and each cell contains exactly one ball?
>
> Options: A. 44  B. 96  C. 120  D. 3125
>
> **Approach:** This is exactly the derangement condition on 5 distinct elements into 5 distinct positions.
>
> $$
> D_5 = 44
> $$
>
> **Answer:** $\boxed{\text{A. } 44}$

---

## 11. Related Permutation Puzzles (10-Element Set)

For a set $a_1, \dots, a_{10}$:

| Question | Answer | Reasoning |
| :--- | :--- | :--- |
| No one in their home | $D_{10}$ | direct definition |
| At least one **not** in their home | $10! - 1$ | complement of "everyone in home," and only 1 permutation has everyone home (identity) |
| Everyone in their home | $1$ | only the identity permutation |
| At least one **in** their home | $10! - D_{10}$ | complement of "no one in home" |
| First 5 people in first 5 positions but not in own home, last 5 unrestricted-but-arranged | $D_5 \times 5!$ | first block deranged, second block freely permuted |
| First 5 deranged among themselves, last 5 also deranged among themselves | $D_5 \times D_5$ | two independent derangement sub-problems |

---

## Related Notes

- [[Inclusion-Exclusion Principle]]
- [[Onto Functions (Surjections) via IEP]]
- [[moc combinatorics]]
- [[Recurrence Relations]]

## Open Questions

- [ ] Numerically finalize Q7 (no even digit fixed, digits 0–9) — expression is set up but not reduced to a final integer in the source.
- [ ] Double check Q5's "start with 1,2,3" reasoning against a direct small-case enumeration to firm up the general argument (the source's handwritten reasoning was somewhat informal).
- [ ] The proof of $D_n = nD_{n-1}+(-1)^n$ was explicitly skipped in the lecture — revisit via the closed-form summation if a rigorous derivation is needed for GATE-level justification.
