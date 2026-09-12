# Inclusion-Exclusion Principle (IEP)

**Topic:** Discrete Mathematics > Combinatorics > Set Theory
**Source:** GO Classes — Discrete Mathematics, Combinatorics (IEP Lecture)
**Tags:** #combinatorics #set-theory #IEP #gate-cse
**Links:** [[moc combinatorics]] | [[Derangements]] | [[Generating Functions]]

---

> [!info] Overview
> IEP is a counting tool used to find the size of a union of finite sets when the sizes of the individual sets and their intersections are known. This note covers IEP for 2, 3, and 4 sets, its generalization to $n$ sets, and a wide range of application-style problems (divisibility, strings, card hands, distributions, permutations with restrictions).

---

## 1. IEP for Two Sets

### 1.1 Motivation

If you simply add $|A|$ and $|B|$, every element that lies in both sets gets counted twice. To fix the double counting, the overlap is subtracted once.

$$
|A \cup B| = |A| + |B| - |A \cap B|
$$

This is sometimes called the **subtraction rule** version of IEP. In the Venn diagram, the region $A \cap B$ receives a count of 2 when you add $|A|+|B|$, so subtracting $|A \cap B|$ brings every region back down to a count of exactly 1.

### 1.2 Worked Examples

> [!example] Algebra / Probability class
> **Question:** In a class, 20 students study Algebra, 25 study Probability, and 8 study both. How many study Algebra or Probability?
>
> **Approach:**
> Let $A$ = Algebra students, $P$ = Probability students. $|A| = 20$, $|P| = 25$, $|A \cap P| = 8$.
>
> $$
> |A \cup P| = 20 + 25 - 8 = 37
> $$
>
> **Answer:** $\boxed{37}$

> [!example] CS / Math majors (Rosen, Example 1)
> **Question:** Every student majors in CS or Math or both. CS majors = 25, Math majors = 13, both = 8. How many students total?
>
> **Approach:**
> $$
> |CS \cup M| = 25 + 13 - 8 = 30
> $$
>
> **Answer:** $\boxed{30}$

### 1.3 Useful Variations

Splitting a union into disjoint "only" regions gives an alternative identity:

$$
|A \cup B| = |A| + |B - A|
$$

$$
|A \cup B| = |A - B| + |B - A| + |A \cap B|
$$

Here $B - A$ means "only in $B$, not in $A$."

> [!note] Complement form
> $$
> |A \cup B| = \text{Total} - |\overline{A} \cap \overline{B}|
> $$
> This says: everything outside both $A$ and $B$ is exactly the complement of $A \cup B$. This identity is the backbone of almost every "at least one" / "none of" counting problem.

### 1.4 Bounds on $|A \cup B|$

$$
\max(|A|, |B|) \leq |A \cup B| \leq |A| + |B|
$$

| Case | Condition | Result |
| :--- | :--- | :--- |
| Lower bound achieved | $A \subseteq B$ or $B \subseteq A$ | $\lvert A \cup B \rvert = \max(\lvert A \rvert, \lvert B \rvert)$ |
| Upper bound achieved | $A \cap B = \varnothing$ (disjoint) | $\lvert A \cup B \rvert = \lvert A \rvert + \lvert B \rvert$ |

**Proof sketches (from the formula):**

- If $A, B$ disjoint, $|A \cap B| = 0$, so $|A \cup B| = |A| + |B| - 0 = |A|+|B|$.
- If $A \subseteq B$, then $A \cap B = A$, so $|A \cup B| = |A| + |B| - |A| = |B|$.

---

## 2. IEP for Three Sets

### 2.1 Deriving the Formula (Region-Counting Method)

The derivation is built up step by step, tracking how many times each region of the three-circle Venn diagram is counted:

$$
\begin{aligned}
\text{Step 1:} \quad & |A| + |B| + |C| \quad \text{— pairwise overlaps counted twice, triple overlap counted 3 times} \\
\text{Step 2:} \quad & |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| \quad \text{— triple overlap now counted 0 times} \\
\text{Step 3 (final):} \quad & |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|
\end{aligned}
$$

$$
\boxed{|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |B \cap C| - |A \cap C| + |A \cap B \cap C|}
$$

> [!note] Key Idea
> Each region's final count equals 1 only after: add singles (over-adds intersections), subtract pairwise intersections (over-subtracts the triple region), add back the triple intersection (restores it to count 1).

### 2.2 Numeric Check

Let $A = \{1,2,3,4\}$, $B = \{3,4,5,6\}$, $C = \{2,3,4,5,6,7\}$.

$$
7 = 4 + 4 + 6 - 2 - 3 - 4 + 2
$$

This confirms $|A \cup B \cup C| = 7$.

---

## 3. IEP for Four Sets

$$
\begin{aligned}
|A \cup B \cup C \cup D| = \; & |A| + |B| + |C| + |D| \\
& - |A \cap B| - |A \cap C| - |B \cap C| - |A \cap D| - |B \cap D| - |C \cap D| \\
& + |A \cap B \cap C| + |A \cap B \cap D| + |A \cap C \cap D| + |B \cap C \cap D| \\
& - |A \cap B \cap C \cap D|
\end{aligned}
$$

> [!example] 4-set numeric problem
> **Question:** Four sets, each has 15 elements. Every pairwise intersection has 5 elements. Every three-way intersection has 2 elements. The four-way intersection has 1 element. Find $|A \cup B \cup C \cup D|$.
>
> **Approach:** There are $\binom{4}{1}=4$ singles, $\binom{4}{2}=6$ pairs, $\binom{4}{3}=4$ triples, $\binom{4}{4}=1$ quadruple.
>
> $$
> 4(15) - \binom{4}{2}(5) + \binom{4}{3}(2) - \binom{4}{4}(1) = 60 - 30 + 8 - 1 = 37
> $$
>
> **Answer:** $\boxed{37}$

---

## 4. General Formula for $n$ Sets

$$
|A_1 \cup A_2 \cup \dots \cup A_n| = \sum |A_i| - \sum |A_i \cap A_j| + \sum |A_i \cap A_j \cap A_k| - \dots
$$

In words: add all singles, subtract all pairwise intersections, add all triple intersections, subtract all quadruple intersections, and so on, alternating sign, until the full $n$-way intersection is reached.

---

## 5. Set Theory Region-Labeling (3-Set Diagram)

For three sets $A, B, C$ inside a universal set, label the 8 regions:

| Region | Description |
| :--- | :--- |
| 1 | Outside all circles (universal set only) |
| 2 | $A$ only |
| 3 | $B$ only |
| 4 | $C$ only |
| 5 | $A \cap C$ only (not $B$) |
| 6 | $A \cap B$ only (not $C$) |
| 7 | $B \cap C$ only (not $A$) |
| 8 | $A \cap B \cap C$ |

Using this labeling:

$$
|A \cap B| = \text{regions } 6+8, \qquad |A| = \text{regions } 2+5+6+8
$$

$$
|A - B| = \text{regions } 2+5, \qquad |A \cap B \cap C| = \text{region } 8
$$

$$
|A \cap B \cap \overline{C}| = \text{region } 6, \qquad |A \cap \overline{B} \cap \overline{C}| = \text{region } 2 \text{ (in A, not in B and not in C)}
$$

$$
\text{Only } B = \text{region } 3, \qquad \text{Only } C = \text{region } 4, \qquad \text{(only } A) \cup (\text{only } B) = \text{regions } 2+3
$$

---

## 6. Divisibility / Counting Multiples

### 6.1 Base Case: 1 to $n$

The count of integers from $1$ to $n$ (inclusive by default) divisible by $b$ is:

$$
\left\lfloor \frac{n}{b} \right\rfloor
$$

> [!example] Multiples of 6 up to 40
> $\left\lfloor \dfrac{40}{6} \right\rfloor = \lfloor 6.67 \rfloor = 6$

### 6.2 General Range: $a$ to $b$

Because the count "1 to $b$" divisible by $n$ minus the count "1 to $(a-1)$" divisible by $n$ leaves exactly the multiples in $[a, b]$:

$$
\boxed{\left\lfloor \frac{b}{n} \right\rfloor - \left\lfloor \frac{a-1}{n} \right\rfloor}
$$

### 6.3 Divisible by 7 or 11, up to 1000

> [!example] Divisible by 7 or 11 (Rosen, Example 2)
> **Question:** How many positive integers not exceeding 1000 are divisible by 7 or 11?
>
> **Approach:** Careful with range — "1 to 1000" is correct (not 0-based, not 0-999).
> $A$ = divisible by 7, $B$ = divisible by 11, $A \cap B$ = divisible by $\text{lcm}(7,11) = 77$.
>
> $$
> |A| = \left\lfloor \tfrac{1000}{7} \right\rfloor = 142, \quad |B| = \left\lfloor \tfrac{1000}{11} \right\rfloor = 90, \quad |A \cap B| = \left\lfloor \tfrac{1000}{77} \right\rfloor = 12
> $$
>
> $$
> |A \cup B| = 142 + 90 - 12 = 220
> $$
>
> **Answer:** $\boxed{220}$

### 6.4 Neither Multiple of 2 nor 9, from 1 to 100

> [!example] Neither divisible by 2 nor by 9
> **Question:** How many integers from 1 to 100 are neither multiples of 2 nor multiples of 9?
>
> **Approach:**
> $$
> \overline{2} \cap \overline{9} = \overline{2 \cup 9} = \text{Total} - (2 \cup 9)
> $$
>
> Multiples of 2: 50, multiples of 9: 11, multiples of $\text{lcm}(2,9)=18$: 5.
>
> $$
> 100 - (50 + 11 - 5) = 100 - 56 = 44
> $$
>
> **Answer:** $\boxed{44}$

### 6.5 Full Divisibility Problem Set (1 to 999, divisibility by 7 and 11)

> [!example] Multi-part divisibility problem
> **Question:** How many positive integers less than 1000 (i.e., $1$ to $999$):
> (a) are divisible by 7? (b) by 7 but not 11? (c) by both 7 and 11? (d) by either 7 or 11? (e) by exactly one of 7, 11? (f) by neither 7 nor 11? (g) have distinct digits? (h) have distinct digits and are even?
>
> **Approach & Answers:**
>
> **(a)** $\left\lfloor \dfrac{999}{7} \right\rfloor$
>
> **(b)** Subtract the "both" region (LCM = 77) from "divisible by 7":
> $$
> \left\lfloor \frac{999}{7} \right\rfloor - \left\lfloor \frac{999}{77} \right\rfloor
> $$
>
> **(c)** Divisible by both means divisible by $\text{lcm}(7,11)=77$:
> $$
> \left\lfloor \frac{999}{77} \right\rfloor
> $$
>
> **(d)** Let $S = \left\lfloor \dfrac{999}{7} \right\rfloor + \left\lfloor \dfrac{999}{11} \right\rfloor - \left\lfloor \dfrac{999}{77} \right\rfloor$ (standard IEP)
>
> **(e)** Exactly one = (divisible by either) minus (divisible by both), i.e. subtract the intersection once more:
> $$
> S - \left\lfloor \frac{999}{77} \right\rfloor = \left\lfloor \frac{999}{7} \right\rfloor + \left\lfloor \frac{999}{11} \right\rfloor - 2\left\lfloor \frac{999}{77} \right\rfloor
> $$
>
> **(f)** Neither = complement of (d):
> $$
> 999 - S
> $$
>
> **(g)** Distinct digits — case on number of digits:
> $$
> \underbrace{9}_{\text{1-digit}} + \underbrace{9 \times 9}_{\text{2-digit } = 81} + \underbrace{9 \times 9 \times 8}_{\text{3-digit}}
> $$
> (1-digit numbers 1–9 automatically have distinct digits; 2-digit: first digit 1–9 (9 ways), second digit any of remaining 9 digits incl. 0; 3-digit: first digit 9 ways, second 9 ways (incl. 0 now allowed, excl. first), third 8 ways.)
>
> **(h)** Distinct digits **and** even — split by last-digit parity constraint:
> $$
> \underbrace{4}_{\text{1-digit even: } 2,4,6,8} + \underbrace{(9 \times 1) + (8 \times 4)}_{\text{2-digit} = 41} + \underbrace{(9 \times 8 \times 1) + (8 \times 8 \times 4)}_{\text{3-digit} = 72 + 256}
> $$
> The split accounts for whether the last digit is 0 (only 1 way, but frees up the leading digit to be any of 9 nonzero digits) versus a nonzero even digit (4 choices: 2,4,6,8, but leading digit then has one fewer option since 0 is now excluded from lead but available elsewhere).

---

## 7. Symmetric Difference

$$
A \oplus B = |A \cup B| - |A \cap B| = |A| + |B| - 2|A \cap B| = |A - B| + |B - A|
$$

This is exactly the "exactly one of $A$, $B$" region — used directly in part (e) of the divisibility problem above.

---

## 8. String Counting Problems (Alphabet $\{A,B,C\}$, length 6)

### 8.1 Start with C or End with C

> [!example] Start with C or end with C
> **Approach:** Let $X$ = starts with C ($3^5$ strings, since remaining 5 positions are free), $Y$ = ends with C ($3^5$), $X \cap Y$ = starts **and** ends with C ($3^4$, since 4 middle positions are free).
>
> $$
> |X \cup Y| = 2 \times 3^5 - 3^4
> $$

### 8.2 Start with C AND End with C

$$
C\_\_\_\_C \implies 3^4 \quad \text{(4 free middle positions, each 3 choices)}
$$

### 8.3 At Least 5 Consecutive A's (length 6)

> [!example] At least 5 consecutive A's
> **Approach:** Two overlapping patterns cover this: $AAAAA\_$ (last symbol free, 3 ways) and $\_AAAAA$ (first symbol free, 3 ways). These are **exhaustive but not exclusive** — the all-A's string $AAAAAA$ is counted in both.
>
> $$
> 3 + 3 - 1 = 5
> $$
>
> **Answer:** $\boxed{5}$

### 8.4 At Least 4 Consecutive A's, Alphabet $\{A,B,C,D,E\}$, length 6

> [!example] At least 4 consecutive A's, 5-letter alphabet
> **Approach:** Three overlapping patterns, $S_1 = AAAA\_\_$, $S_2 = \_AAAA\_$, $S_3 = \_\_AAAA$. Each individually gives $5^2 = 25$ (2 free positions). Use full 3-set IEP:
>
> $$
> |S_1 \cup S_2 \cup S_3| = 3(5^2) - |S_1 \cap S_2| - |S_1 \cap S_3| - |S_2 \cap S_3| + |S_1 \cap S_2 \cap S_3|
> $$
>
> Pairwise intersections: $S_1 \cap S_2$ forces $AAAAA\_$ (5 A's consecutive, 1 free) $=5$; $S_2 \cap S_3$ similarly $=5$; $S_1 \cap S_3$ forces all 6 positions to be A ($AAAAAA$) $=1$. Triple intersection also forces all A's $=1$.
>
> $$
> |S_1 \cup S_2 \cup S_3| = 75 - 5 - 1 - 5 + 1
> $$

---

## 9. Card Hand Problems

### 9.1 Exactly One King or Exactly One Queen (inclusive or)

> [!example] Exactly one King or exactly one Queen
> **Approach:**
> $1K$ = exactly one King, rest from the 48 non-Kings: $\binom{4}{1} \times \binom{48}{4}$
> $1Q$ = exactly one Queen, similarly: $\binom{4}{1} \times \binom{48}{4}$
> $1K \cap 1Q$ = exactly one King **and** exactly one Queen: $\binom{4}{1} \times \binom{4}{1} \times \binom{44}{3}$
>
> $$
> 2 \times \binom{4}{1}\binom{48}{4} - \binom{4}{1}\binom{4}{1}\binom{44}{3}
> $$

### 9.2 At Least One Ace or At Least One Queen

> [!warning] Common mistake
> Writing $\binom{4}{1} \times \binom{51}{4}$ for "at least one Ace" **overcounts** — after reserving one Ace, the remaining $\binom{51}{4}$ still allows more Aces to appear, causing the same hand to be counted multiple times (once per choice of "the" reserved Ace).

**Correct approach — complement method:**

$$
|A \cup Q| = \text{Total} - |\overline{A} \cap \overline{Q}| = \binom{52}{5} - \binom{44}{5}
$$

**Correct approach — direct IEP:**

$$
\left[\binom{52}{5} - \binom{48}{5}\right] + \left[\binom{52}{5} - \binom{48}{5}\right] - \left[\binom{52}{5} - 2\binom{48}{5} + \binom{44}{5}\right]
$$

where $\binom{52}{5}-\binom{48}{5}$ correctly counts "at least one Ace" (total minus hands with **no** Ace), and the bracketed subtracted term is "at least one Ace **and** at least one Queen" computed the same complement way.

---

## 10. Line-Up / Arrangement Problems (Adjacency Constraints)

### 10.1 Mother Next to At Least One of 3 Sons (7 people: M, F, 3 sons, 2 daughters)

**Method 1 — Complementary counting:**

$$
7! - \big(\text{Mother not adjacent to any son}\big)
$$

Case on Mother's position:
- Mother at either end (2 positions), Father must not be adjacent either — actually here Father is placed in the adjacent slot to keep Mother "blocked": $2 \times 3 \times 5!$
- Mother in a middle position (5 slots), both neighbors must be non-sons: $5 \times 3 \times 2 \times 4!$

$$
D = 7! - \left(2 \times 3 \times 5! + 5 \times 3 \times 2 \times 4!\right)
$$

**Method 2 — IEP directly on "adjacent to $s_1$", "adjacent to $s_2$", "adjacent to $s_3$":**

Let $(m,s_i)$ denote "Mother adjacent to son $i$" treated as a block.

$$
(m,s_1) \cup (m,s_2) \cup (m,s_3) = \sum (m,s_i) - \sum (m,s_i,s_j)_{\text{both adjacent}} + (m,s_1,s_2,s_3)
$$

- $(m, s_i)$: glue Mother+$s_i$ into one block (2 internal orders), arrange 6 units: $6! \times 2$
- $(m,s_i,s_j)$ both adjacent simultaneously means $s_i$–M–$s_j$ as one block (2 internal orders for which son is on which side), arrange 5 units: $5! \times 2$
- Triple term (all 3 sons adjacent to M simultaneously) is impossible: $0$ (Mother has only 2 sides)

$$
\binom{3}{1}(6! \times 2) - \binom{3}{2}(5! \times 2) + 0
$$

### 10.2 Related HW-style Variants (referenced, not fully solved in source)
- Mother next to at least one of 2 daughters (family of 2 parents, 2 daughters, 2 sons).
- Mother next to at least one daughter (family of 2 parents, 3 daughters, 4 sons).

These follow the same complementary / IEP block method as above, scaled to the new family sizes.

---

## 11. Language / Course Enrollment (3-Set Reverse Problem)

> [!example] Spanish / French / Russian
> **Question:** 1232 students take Spanish, 879 French, 114 Russian. $S \cap F = 103$, $S \cap R = 23$, $F \cap R = 14$. Total taking at least one $= 2092$. Find $S \cap F \cap R$.
>
> **Approach:** Rearrange the 3-set IEP formula to solve for the unknown triple intersection:
>
> $$
> F \cup R \cup S = F + R + S - FR - FS - RS + FRS
> $$
>
> $$
> FRS = (F \cup R \cup S) - (F+R+S) + (FR+FS+RS)
> $$
>
> $$
> FRS = 2092 - (879+114+1232) + (103+23+14)
> $$
>
> **Answer:** solve the arithmetic above for $FRS$.

---

## 12. Distribution with Upper-Bound Constraints (Stars and Bars + IEP)

### 12.1 General Technique

When variables have upper bounds, compute the unrestricted count and subtract the cases where a bound is **violated**, using IEP on the "violation" events.

### 12.2 Worked Example — Three Variables

> [!example] $x_1+x_2+x_3=11$, with $x_1 \le 3$, $x_2 \le 4$, $x_3 \le 6$
> **Approach:** Define properties $P_1: x_1 \ge 4$, $P_2: x_2 \ge 5$, $P_3: x_3 \ge 7$ (violations). Want $N(P_1' P_2' P_3')$.
>
> $$
> N(P_1'P_2'P_3') = N - \big[N(P_1)+N(P_2)+N(P_3)\big] + \big[N(P_1P_2)+N(P_1P_3)+N(P_2P_3)\big] - N(P_1P_2P_3)
> $$
>
> Substituting $x_1 \to x_1 - 4$ etc. to remove the lower-bound violation shifts the total by the violated amount (standard stars-and-bars substitution):
>
> $$
> \begin{aligned}
> N &= \binom{3+11-1}{11} = \binom{13}{11} = 78 \\
> N(P_1) &= \binom{3+7-1}{7} = \binom{9}{7} = 36 \\
> N(P_2) &= \binom{3+6-1}{6} = \binom{8}{6} = 28 \\
> N(P_3) &= \binom{3+4-1}{4} = \binom{6}{4} = 15 \\
> N(P_1P_2) &= \binom{3+2-1}{2} = \binom{4}{2} = 6 \\
> N(P_1P_3) &= \binom{3+0-1}{0} = 1 \\
> N(P_2P_3) &= 0 \quad (\text{sum needed} < 0 \text{ after both shifts}) \\
> N(P_1P_2P_3) &= 0
> \end{aligned}
> $$
>
> $$
> N(P_1'P_2'P_3') = 78 - 36 - 28 - 15 + 6 + 1 + 0 - 0 = 6
> $$
>
> **Answer:** $\boxed{6}$

### 12.3 Worked Example — Donuts (4 Varieties, Upper Bounds on 2)

> [!example] 20 donuts, 4 flavors, $C \le 5$, $J \le 3$
> **Question:** $G+M+C+J=20$, $G,M \ge 0$ unrestricted, $C \le 5$, $J \le 3$. Count solutions.
>
> **Approach:**
> $$
> \text{Desired} = \text{Total} - \big(C \ge 6 \text{ OR } J \ge 4\big)
> $$
>
> $$
> = \binom{20+3}{3} - \left[\binom{14+3}{3} + \binom{16+3}{3} - \binom{10+3}{3}\right]
> $$
>
> where $\binom{14+3}{3}$ comes from substituting $C \to C-6$ (new total $=14$), $\binom{16+3}{3}$ from $J \to J-4$ (new total $=16$), and $\binom{10+3}{3}$ from both substitutions simultaneously (new total $=10$).

> [!note] General pattern
> $$
> \underbrace{\text{\# with all constraints satisfied}}_{\text{desired}} = \underbrace{\text{\# unrestricted}}_{\text{total}} - \underbrace{\text{\# violating at least one constraint}}_{\text{IEP on violation events}}
> $$

---

## 13. Homework / Unsolved-in-Source Problems (flagged, no worked solution given)

> [!example] Drug test symptom overlap (HW)
> Population of 1000. Symptom A: 122, B: 88, C: 112, $A\cap B=27$, $A\cap C=29$, $B\cap C=32$, $A\cap B\cap C=10$. Find how many get **at least one** symptom.
>
> **Approach (to complete):** Direct 3-set IEP:
> $$
> |A \cup B \cup C| = 122+88+112-27-29-32+10
> $$

---

## Related Notes

- [[Derangements]]
- [[Onto Functions (Surjections) via IEP]]
- [[moc combinatorics]]
- [[Generating Functions]]

## Open Questions

- [ ] Confirm final numeric answers for the divisibility multi-part problem (parts a–h) by direct computation.
- [ ] Confirm final numeric answer for the Spanish/French/Russian triple-intersection problem.
- [ ] Complete and verify the drug-test HW problem (currently only the setup is given in the source).
- [ ] Verify the "22 in the range 1–42 divisible by 2, 3, or 7" HW problem — no worked solution was present in the source; only the question was listed.
