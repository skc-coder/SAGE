**Topic:** GATE CS > Discrete Mathematics > Combinatorics > Pigeonhole Principle 

**Source:** GO Classes — Deepak Poonia (Discrete Mathematics Course, Combinatorics module: "Pigeon-hole Principle", "Generalized Pigeonhole Principle", "Pigeonhole Principle Practice") 

**Tags:** #gate-cs #discrete-math #combinatorics #pigeonhole-principle 
**Links:** [[Discrete Mathematics MOC]] | [[moc combinatorics]] | [[Generating Functions]] | [[Recurrence Relations]]

---

> [!info] Overview 
> This note covers the Pigeonhole Principle (PHP) in three layers: the simple version, the generalized version (ceiling/floor bounds), and a large set of GATE-style practice problems including the "ordered pairs / couple" pattern. The core skill tested isn't memorizing a formula — it's the "try to prevent the event" reasoning technique.

---

## 1. The Simple Pigeonhole Principle

### 1.1 Core Statement

If you have $m$ pigeons being placed into $n$ holes (boxes), and $m > n$, then at least one hole must contain two or more pigeons. You cannot spread more items than slots without some slot getting a duplicate.

$$ \text{Proposition (PHP, simple version): if } k+1 \text{ or more pigeons are placed into } k \text{ holes, at least one hole has} \ge 2 \text{ pigeons.} $$

The whole principle is about **guarantees**, not possibilities. A question like "can two pigeons end up in the same hole" is trivially yes (a possibility). The PHP question is "is it _forced_, no matter how you arrange things."

### 1.2 The Master Technique: "Try to Prevent It"

> [!tip] Key Idea Whenever a question asks you to **guarantee** some event $X$, the cleanest way to find the threshold is to ask: "what's the maximum I can do while actively _preventing_ $X$?" The next item beyond that maximum forces $X$ to happen.

This is the single most repeated instruction across all three lectures (it appears as "NOTE 1" in every source PDF). Two complementary instructions go with it:

- **NOTE 1:** To guarantee event $X$, try to _prevent_ $X$ from happening — find the max count under which prevention is still possible, then add 1.
- **NOTE 2:** To prevent "too much" piling up in one room, the optimal strategy is to _uniformly distribute_ items across all rooms — uneven distributions only make prevention harder, not easier.
- **NOTE 3:** Don't blindly memorize formulas — use common sense and logical thinking, since many questions (worded slightly differently) break a naive formula.

### 1.3 Walking Through the Pigeons/Holes Intuition

The lecture builds intuition with a sequence of small cases (4 pigeons against shrinking hole counts):

|Pigeons|Holes|Can you guarantee a shared hole?|
|:--|:--|:--|
|4|5|No — each pigeon can get its own hole|
|4|4|No — exact 1-to-1 fit is possible|
|4|3|**Yes** — one hole must hold $\ge 2$|
|4|2|**Yes** — forced sharing, in fact one hole gets $\ge 2$ pigeons even in the "best" spread|

The pattern: guarantee kicks in exactly when pigeons exceed holes ($m > n$).

### 1.4 Classic Applications

**Birthday months:** with 13 office clerks (pigeons) and 12 months (holes), since $13 > 12$, two clerks must share a birthday month. The lecture also checks smaller counts: 10 or 12 people give _no_ guarantee (you can assign one person per month with room to spare), but as soon as you cross 12 people, sharing is forced.

**English words by starting letter:** with 26 letters as holes, any group of 27 words (pigeons) forces two words to share a starting letter — 26 or fewer words can each get a distinct letter, so no guarantee exists until you hit 27.

**Leap year birthdays:** 366 people do _not_ guarantee a shared birthday if it's a leap year (366 days = 366 holes, so a perfect 1-to-1 mapping exists). This is a useful counter-example showing you must check the _exact_ hole count for the scenario, not just memorize "366 → guarantee."

**Exam scores:** with scores ranging $0$ to $100$ (101 possible distinct values = 101 holes), you need $\ge 102$ students to force two students into the same score.

### 1.5 Functions and the Pigeonhole Principle

If $f: A \to B$ is a function between finite sets and $|A| > |B|$, then $f$ **cannot** be one-to-one (injective). Elements of $A$ are the pigeons, elements of $B$ are the holes; since pigeons outnumber holes, at least two elements of $A$ must map to the same element of $B$.

$$ \text{A function } f \text{ from a set with } k+1 \text{ or more elements to a set with } k \text{ elements is not one-to-one.} $$

> [!warning] Common Trap PHP guarantees $f$ is **not injective** when $|A| > |B|$. It says nothing about $f$ being **onto (surjective)**. The lecture explicitly tests this: "Does PHP say $f$ will definitely be onto?" — **No.** Injectivity-failure and surjectivity are unrelated conclusions here.

### 1.6 Modular Arithmetic Version

If $S \subseteq \mathbf{Z}^+$ and $|S| > n$ (for some positive integer $n$), then there must exist two distinct elements $a, b \in S$ with the same remainder when divided by $n$.

This is just PHP with the $n$ possible remainders ($0, 1, \dots, n-1$) acting as the holes. Worked example: with $|S| = 37$ and dividing by 36, there are only 36 possible remainders, so two elements of a 37-element set must share a remainder mod 36.

### 1.7 Reformulating the Pigeons and Holes (Word Problems)

A recurring exam skill is correctly **identifying** what the pigeons and what the holes are, since this isn't always literal.

> [!example] Sum-to-10 Subset Problem 
> **Question:** Show that any subset of size 6 from $S = {1, 2, \dots, 9}$ must contain two elements whose sum is 10.
> 
> **Approach:** Step 1 — List all pairs summing to 10: $(1,9), (2,8), (3,7), (4,6)$, plus the unpaired element $5$. That's **5 "holes"**: ${1,9}, {2,8}, {3,7}, {4,6}, {5}$. Step 2 — To _prevent_ a sum-10 pair, pick at most one number from each pair-hole — e.g. ${1, 2, 7, 4, 5}$, a 5-element subset with no sum-10 pair. Step 3 — Any 6th element forces you into a hole that's already occupied, creating a sum-10 pair.
> 
> **Answer:** minimum subset size to guarantee a sum-10 pair $= \boxed{6}$

The same "prevent" technique generalizes: for $A = {1,\dots,8}$ ensuring a sum of 9 needs $n \ge 5$ (pairs: $(1,8),(2,7),(3,6),(4,5)$ — 4 holes, prevent with one-per-pair, 5th forces it). For $B = {1,\dots,100}$ ensuring a sum of 101 needs $n \ge 51$ (pairs $(1,100)$ through $(50,51)$ — 50 holes, prevent with ${1,\dots,50}$, 51st element forces it).

### 1.8 The "Same Degree" Party/Graph Theorem

> [!note] Key Idea In any simple graph with at least 2 vertices, two vertices must share the same degree. Equivalently: at a party with $\ge 2$ people, two people know the same number of other people there.

**Why:** for $n$ people, each person's degree (number of handshakes/friends) lies in the range $0$ to $n-1$ — that's $n$ possible values. Naively this looks like $n$ pigeons into $n$ holes, which wouldn't force a collision. The trick is realizing **degree 0 and degree $n-1$ can never both occur simultaneously** in the same graph:

- If someone has degree $n-1$ (knows everyone), then nobody can have degree $0$ (since that "isolated" person would have to be known by the degree-$(n-1)$ person — contradiction).
- So the _actual_ usable range of degrees is only $n-1$ distinct values at any one time (either ${0, \dots, n-2}$ or ${1, \dots, n-1}$, never both extremes together).

That collapses the holes from $n$ down to $n-1$, while pigeons (people) remain $n$. Since $n > n-1$, PHP forces two people to share a degree.

> [!example] GATE CSE 1991 — Q16(b) 
> **Question:** Show that all vertices in an undirected finite graph cannot have distinct degrees, if the graph has at least two vertices.
> 
> **Approach:** Step 1 — Possible degree values for $n$ vertices range over $n$ values ($0$ to $n-1$). Step 2 — Degree $0$ and degree $n-1$ cannot coexist in the same graph (proof by contradiction, as above). Step 3 — This leaves only $n-1$ usable values (holes) for $n$ vertices (pigeons), forcing a repeat by PHP.
> 
> **Answer:** Proven — two vertices must share a degree. $\boxed{\text{QED}}$

> [!example] GATE CSE 2009 — Q3 
> **Question:** Which is TRUE for any simple connected undirected graph with more than 2 vertices? (A) No two vertices have the same degree (B) At least two vertices have the same degree (C) At least three vertices have the same degree (D) All vertices have the same degree
> 
> **Approach:** Connectedness rules out a degree-0 vertex entirely, so the degree-0/degree-$(n-1)$ exclusion argument applies the same way, giving $n-1$ holes for $n$ pigeons.
> 
> **Answer:** $\boxed{\text{B}}$

---

## 2. The Generalized Pigeonhole Principle

### 2.1 Motivation: Beyond "At Least 2"

The simple PHP only tells you _some_ hole has $\ge 2$ pigeons. But what if you want a stronger guarantee — e.g., that some hole has $\ge 6$ pigeons? You need the **generalized** version, which scales with how far pigeons outnumber holes.

### 2.2 The Formula

$$ \textbf{Theorem (Generalized PHP):}\quad \text{If } N \text{ objects are placed into } k \text{ boxes, then at least one box contains} \ge \left\lceil \dfrac{N}{k} \right\rceil \text{ objects.} $$

And the complementary "floor" statement (less commonly asked, but proven the same way):

$$ \text{Some box contains} \le \left\lfloor \dfrac{N}{k} \right\rfloor \text{ objects.} $$

### 2.3 Deriving It via "Uniform Distribution to Prevent"

The cleanest way to _derive_ (not just recall) the ceiling formula is NOTE 2's strategy: to prevent any one hole from getting "too many," spread pigeons as evenly as possible.

**Worked logic (22 pigeons, 4 holes):**

$$ 22 / 4 = 5 \ \text{remainder} \ 2 $$

If you try to cap every hole at 5, you can place at most $4 \times 5 = 20$ pigeons — but you have 22, so 2 pigeons are left with nowhere to go except into already-full holes. Hence some hole must reach $\ge 6 = \lceil 22/4 \rceil$.

**Worked logic (father giving ₹27 to 5 children):** $27/5 = 5$ remainder $2$ → capping each child at ₹5 only distributes ₹25, leaving ₹2 unassigned → at least one child gets $\ge 6$.

**Worked logic (100 people, 12 birth months):** $100/12 = 8$ remainder $4$ → capping each month at 8 distributes only 96 people, leaving 4 → at least one month has $\ge 9$ people. (Note: the lecture flags that claiming "some month has _exactly_ 9" is **false** — PHP only guarantees the lower bound, not the exact value.)

### 2.4 Worked GATE-Style Examples

> [!example] Standard Deck — At Least 3 of Same Suit **Question:** How many cards must be selected from a standard 52-card deck to guarantee at least 3 cards of the same suit?
> 
> **Approach:** Step 1 — 4 suits = 4 holes. To _prevent_ 3-of-a-suit, cap each suit at 2 cards: $4 \times 2 = 8$ cards max while still avoiding the event. Step 2 — The 9th card forces a 3rd card into some suit.
> 
> $$ \lceil N/4 \rceil \ge 3 \implies N_{\min} = 2 \cdot 4 + 1 = 9 $$
> 
> **Answer:** $\boxed{9}$

> [!example] Standard Deck — At Least 3 Hearts Specifically **Question:** How many cards must be selected to guarantee at least 3 **hearts** (not just any suit)?
> 
> **Approach:** This is a trap for the generalized-PHP formula — it does **not** apply directly, because we care about one _specific_ hole (hearts), not "some hole." Worst case: draw all 39 non-heart cards first (clubs+diamonds+spades), then the next 3 cards must all be hearts.
> 
> **Answer:** $39 + 3 = \boxed{42}$

> [!example] GATE CSE 2000 — Q1.1 **Question:** The minimum number of cards to be dealt from a shuffled 52-card deck to guarantee three cards from the same suit is (A) 3 (B) 8 (C) 9 (D) 12
> 
> **Approach:** Same as the "at least 3 of same suit" derivation above: cap each of 4 suits at 2 → 8 cards can still avoid it → 9th card forces it.
> 
> **Answer:** $\boxed{\text{C (9)}}$

> [!example] 14 Pigeons, 4 Holes — Multi-Option Analysis **Question:** With 14 pigeons and 4 holes, which statements are guaranteed to be true? Options include "at least 4 pigeons share a hole," "some hole has at most 2/3/4/5 pigeons."
> 
> **Approach:** Step 1 — Ceiling bound: $\lceil 14/4 \rceil = 4$, so "at least 4 pigeons in some hole" is guaranteed. Note "exactly 4" is **not** guaranteed (could be 5+ in the worst spread) — this is a recurring trap (at least vs. exactly). Step 2 — Floor bound: $\lfloor 14/4 \rfloor = 3$, so "some hole has at most 3" is guaranteed (to prevent it, every hole would need $\ge 4$, requiring $\ge 16$ pigeons — but we only have 14). Step 3 — "Some hole has at most 4" and "at most 5" are weaker/looser versions of the true statement (at most 3), so they're automatically also true (any hole satisfying $\le 3$ also satisfies $\le 4$ and $\le 5$). Step 4 — "Some hole has at most 2" is **not** guaranteed — it's possible to distribute as $3,3,4,4$ or $3,3,3,5$, where every hole has $\ge 3$.
> 
> **Answer:** Guaranteed: "at least 4 share a hole," "some hole has $\le 3, \le 4, \le 5$." Not guaranteed: "exactly 4," "some hole has $\le 2$."

> [!example] TIFR CSE 2014 — Part A, Q5 **Question:** A five-a-side cricket team requires all 5 members to share a birthday month. What is the minimum number of math students needed to guarantee a full team can be raised? (A) 23 (B) 91 (C) 60 (D) 49 (E) None
> 
> **Approach:** Step 1 — Goal: force some month (of 12) to reach $\ge 5$ students. Step 2 — To prevent: cap each month at 4 → $4 \times 12 = 48$ students max while avoiding it. Step 3 — The 49th student forces some month to hit 5.
> 
> **Answer:** $\boxed{49 \text{ (D)}}$

> [!example] GATE CSE 2005 — Q44 (AND version) **Question:** What is the minimum number of ordered pairs $(a,b)$ that must be chosen to guarantee two pairs $(a,b)$, $(c,d)$ with $a \equiv c \pmod 3$ **and** $b \equiv d \pmod 5$? (A) 4 (B) 6 (C) 16 (D) 24
> 
> **Approach:** see §3.3 below for the full "couple" reasoning.
> 
> **Answer:** $\boxed{16 \text{ (C)}}$

> [!example] Kenneth Rosen Ex. 6.2, Q12 **Question:** How many ordered pairs of integers $(a,b)$ are needed to guarantee two pairs $(a_1,b_1), (a_2,b_2)$ with $a_1 \bmod 5 = a_2 \bmod 5$ **and** $b_1 \bmod 5 = b_2 \bmod 5$?
> 
> **Approach:** Same AND-pattern as above with $m=n=5$: $(5\times5)+1$.
> 
> **Answer:** $\boxed{26}$

> [!example] Kenneth Rosen Ex. 6.2, Q5 **Question:** Show that among any group of five integers, two have the same remainder when divided by 4.
> 
> **Approach:** 4 possible remainders ($0,1,2,3$) = 4 holes; 5 integers = 5 pigeons; $5 > 4$ forces a repeat by simple PHP.
> 
> **Answer:** Proven by direct PHP application.

> [!example] Kenneth Rosen Ex. 6.2, Q6 **Question:** Let $d$ be a positive integer. Show that among any group of $d+1$ integers, two have exactly the same remainder when divided by $d$.
> 
> **Approach:** Generalizes Q5 — $d$ possible remainders ($0$ to $d-1$) = $d$ holes, $d+1$ pigeons forces a repeat.
> 
> **Answer:** Proven by direct PHP application.

---

## 3. The "Ordered Pairs / Couple" Pattern (Practice Lecture)

### 3.1 Setting Up the Pattern

This recurring GATE-style pattern asks: given ordered pairs $(a,b)$ drawn from non-negative integers, how many pairs are needed to **guarantee** two pairs $(a,b)$ and $(c,d)$ form a "couple" satisfying some modular condition?

The lecture builds this up gradually through smaller sub-cases before the full AND/OR theorem.

### 3.2 Single-Condition Case

**Condition:** guarantee $a \equiv c \pmod 3$ for two chosen pairs.

Remainders mod 3 are ${0, 1, 2}$ — 3 holes. To prevent a match, pick at most 1 pair from each remainder class → max 3 pairs avoid a match → the 4th pair forces it.

$$ \text{Answer} = 3 + 1 = \boxed{4} $$

Similarly for $b \equiv d \pmod 5$: 5 remainder classes (holes) → max 5 pairs avoid a match → 6th forces it: $\boxed{6}$.

### 3.3 The AND Case (Both Conditions Simultaneously)

**Condition:** guarantee $a \equiv c \pmod 3$ **and** $b \equiv d \pmod 5$ together in the same pair-match.

Here the "hole" isn't just the remainder mod 3, and it isn't just the remainder mod 5 — it's the **combination** $(\text{rem mod }3, \text{rem mod }5)$. There are $3 \times 5 = 15$ such combinations (holes).

To prevent a couple, pick at most one ordered pair per combination-hole: max $15$ pairs avoid the event. The 16th pair must repeat a combination, forcing both conditions to match simultaneously.

$$ \text{Answer} = (3 \times 5) + 1 = \boxed{16} $$

> [!note] Key Idea For the general AND case with conditions $a \equiv c \pmod m$ and $b \equiv d \pmod n$: $$ \text{Minimum pairs needed} = (m \times n) + 1 $$ The intuition: the "hole" is the joint (remainder-mod-$m$, remainder-mod-$n$) category, and there are $mn$ such categories.

### 3.4 The OR Case (Either Condition Suffices)

**Condition:** guarantee $a \equiv c \pmod 3$ **OR** $b \equiv d \pmod 5$ (only one needs to match).

Here OR is _easier_ to force than AND — you only need to win the easier of the two races. With $\ge 4$ pairs, the mod-3 condition alone is already guaranteed (from §3.2), so OR is satisfied a fortiori.

$$ \text{Answer} = \boxed{4} \quad (= \min(m,n) + 1 = \min(3,5)+1) $$

> [!note] Key Idea For the general OR case: $$ \text{Minimum pairs needed} = \min(m, n) + 1 $$ The weaker/easier-to-satisfy condition (smaller modulus) determines the threshold, since forcing the easier one is sufficient for the OR to hold.

### 3.5 Worked Couple Examples (Parity-Based)

> [!example] Same-Parity Couple **Question:** Minimum ordered pairs $(a,b)$ needed to guarantee two pairs $(a,b),(c,d)$ where $a,c$ have the same parity **and** $b,d$ have the same parity.
> 
> **Approach:** Step 1 — Parity has 2 categories (even/odd) for $a$, and 2 for $b$ → joint holes $= 2 \times 2 = 4$. Step 2 — Max pairs avoiding a match $= 4$ (one per joint category). Step 3 — 5th pair forces a repeat.
> 
> **Answer:** $\boxed{5}$

> [!example] Same-Parity Couple (OR version) **Question:** Minimum pairs to guarantee $a,c$ same parity **OR** $b,d$ same parity.
> 
> **Approach:** OR case with $m=n=2$: $\min(2,2)+1 = 3$.
> 
> **Answer:** $\boxed{3}$

> [!example] "a even AND c even" — Degenerate Case **Question:** Minimum ordered pairs needed to guarantee two pairs where both first-elements are even?
> 
> **Approach:** This is a trick question. You can choose infinitely many pairs all with **odd** first elements (e.g., $(3,5), (5,7), (9,10), (11,10), \dots$) and _never_ satisfy "both even," no matter how many pairs you pick. There's no finite threshold.
> 
> **Answer:** $\boxed{\text{None — impossible to guarantee (Option G)}}$

> [!example] Kenneth Rosen Ex. 6.2, Q12 (OR variant) **Question:** How many ordered pairs $(a,b)$ guarantee $a_1 \bmod 5 = a_2 \bmod 5$ **OR** $b_1 \bmod 5 = b_2 \bmod 5$?
> 
> **Approach:** OR case, $m=n=5$: $\min(5,5)+1$.
> 
> **Answer:** $\boxed{6}$

---

## 4. The "Repunit" Theorem — Multiples Made of Repeated Digits

### 4.1 The Cool Result

> [!note] Key Idea For any positive integer $n$, there exists a nonzero multiple of $n$ whose decimal digits are made up of only 0s and 1s (in fact, of the specific form $\underbrace{11\dots1}_{k}\underbrace{00\dots0}_{j}$ — a block of 1s followed by a block of 0s).

This is presented as a genuinely elegant, possibly-future-GATE-worthy theorem, proved entirely with PHP.

### 4.2 Proof by Pigeonhole Principle

**Setup:** generate the sequence of repunits $1, 11, 111, 1111, \dots$ up to $n+1$ such numbers (i.e., $n+1$ numbers each made purely of 1s, of increasing length).

**Step 1 — Pigeons and holes.** There are $n+1$ repunits (pigeons) and only $n$ possible remainders mod $n$ (holes: $0, 1, \dots, n-1$).

**Step 2 — Force a collision.** By PHP, two repunits $a$ and $b$ (say $a$ has fewer digits than $b$) must satisfy:

$$ a \equiv b \pmod n $$

**Step 3 — Examine the difference.** Since $a \equiv b \pmod n$, we know $n \mid (a-b)$. Subtracting a shorter repunit from a longer one digit-by-digit always produces a number of the form $\underbrace{1\dots1}_{}\underbrace{0\dots0}_{}$ — e.g.:

$$ \begin{aligned} 111111111 \

- \ \ 111111 \ \hline 111000000 \end{aligned} $$

**Conclusion:**

$$ n \mid \underbrace{11\dots1}_{k\text{ ones}}\underbrace{00\dots0}_{j\text{ zeros}} \quad \text{for some } k, j $$

This proves every $n$ has such a multiple.

### 4.3 Generalization: Other Digit Pairs

The same proof technique (using $k+1$ copies of repeated digits instead of repunits) extends to other digit pairs:

|Source PDF claim|Digits used|
|:--|:--|
|Grimaldi Ex. 5.5, Q16 (as stated)|0's and 3's|
|Variant mentioned|0's and 7's|
|Variant mentioned|0's and 4's|
|Variant mentioned (derived in-lecture)|0's and 9's, 0's and 8's|

> [!example] Grimaldi Exercise 5.5 — Q16 **Question:** Let $k \in \mathbf{Z}^+$. Prove there exists a positive integer $n$ such that $k \mid n$ and the only digits in $n$ are 0's and 3's.
> 
> **Approach:** Step 1 — Generate $k+1$ numbers of the form $3, 33, 333, \dots$ (i.e., repdigits of 3s, increasing length) — $k+1$ pigeons. Step 2 — Only $k$ possible remainders mod $k$ — $k$ holes. Step 3 — By PHP, two of these numbers $a, b$ satisfy $a \equiv b \pmod k$, so $k \mid (b-a)$. Step 4 — Subtracting same-digit repdigits of different lengths gives a number of form $33\dots300\dots0$.
> 
> **Answer:** Proven — such $n$ exists for every $k$. $\boxed{\text{QED}}$

---

## 5. Quick-Reference Formula Table

| Scenario                          | Formula                                                | Notes                                 |
| :-------------------------------- | :----------------------------------------------------- | :------------------------------------ |
| Simple PHP                        | $m > n \implies$ some hole has $\ge 2$                 | Basic guarantee of a duplicate        |
| Generalized PHP (upper)           | $\left\lceil \dfrac{N}{k} \right\rceil$                | Some box has at least this many       |
| Generalized PHP (lower)           | $\left\lfloor \dfrac{N}{k} \right\rfloor$              | Some box has at most this many        |
| Ordered pairs, AND condition      | $(m \times n) + 1$                                     | Joint category as the hole            |
| Ordered pairs, OR condition       | $\min(m, n) + 1$                                       | Easier condition dominates            |
| Same-degree graph theorem         | $n$ vertices $\implies$ only $n-1$ usable degree-holes | Degree 0 and $n-1$ mutually exclusive |
| Repunit/repdigit multiple theorem | $k+1$ repdigits, $k$ remainder-holes                   | Difference gives the multiple         |

---

## Related Notes

- [[moc combinatorics]]
- [[Generating Functions]]
- [[Recurrence Relations]]
- [[Modular Arithmetic — Number Theory Basics]] _(flagged — unsure if this note exists yet in your vault)_
- [[Graph Theory — Degree Sequences]] _(flagged — unsure if this note exists yet)_

## Open Questions

- [ ] The lecture states the floor-bound generalized PHP ("some box has at most $\lfloor N/k \rfloor$") but barely uses it in practice problems — worth hunting for a GATE PYQ that specifically tests the floor side rather than the ceiling side.
- [ ] Double-check whether the "same parity" couple problems generalize cleanly the same way the mod-$m$/mod-$n$ AND/OR pairs do (parity is essentially mod 2, so this should reduce to the $m=n=2$ case, but worth verifying with a few more examples).
- [ ] The repdigit theorem digit list (3s, 7s, 4s, 9s, 8s) appears to be the same proof template applied repeatedly — confirm whether GATE has ever actually asked this directly, or if it's GO Classes flagging it as "future-possible."
- [ ] No PYQ numbers/years were given for GATE CSE 2005 Q44 follow-up variants (the "OR" version) — only Kenneth Rosen sourcing was clear there.