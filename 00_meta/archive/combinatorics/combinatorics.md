# Combinatorics

combinatorics = science and art of counting discrete objects (strings, events, draws, hands of cards, categorizations etc.)
objects subdivided into parts/stages; atoms come from sets — same set or distinct sets.
different rules have different requirements.

---

## Core Counting Rules

### Sum Rule
- use when: choosing **one** thing OR from disjoint sets
- $|A \cup B| = |A| + |B|$ when disjoint
- overlap? → inclusion-exclusion
- eg: selecting which city to go: {a,b}, {b,c} → total = 3, not 4 (overlap at b)

### Product Rule
- use when: task has **sequential stages** (AND situation)
- key requirement: for each outcome of stage 1, there must be **exactly n ways** for stage 2 — not n1 or n2, all n
- $\text{total} = n_1 \times n_2 \times \dots \times n_k$
- formally: if $|A \times B| = |A| \times |B|$ (cardinality of cartesian product)

### Subtraction Rule (Inclusion-Exclusion, 2 sets)
- $|A \cup B| = |A| + |B| - |A \cap B|$
- practice questions:
  - how many bit strings of length 8 either start with 1 or end with 00?
  - strings starting with 00 or 101?
  - with 10 and 00? with 00 or 000 (overlap!)?

### Division Rule
- use when: procedure counts each outcome exactly $d$ times
- $\text{distinct ways} = n / d$
- set form: if finite set A is union of n pairwise disjoint subsets each with d elements → $n = |A|/d$
- function form: if $f: A \to B$ is d-to-one → $|B| = |A|/d$
- comes in handy when it *appears* there are n ways but each outcome is counted d equivalent times

### Complement Rule
- $\text{desired} = \text{total} - \text{undesired}$
- total cases restrict the universe of discourse; must cover all desired cases
- use when undesired is easier to count

---

## Overcounting
- happens when same object is counted multiple times across stages/parts
- fix 1: **division rule** — if each outcome has a fixed number of equivalent forms
- fix 2: **case by case** — if overcounting factor varies
- cases must be: **exhaustive** (cover all) + **mutually disjoint** (no overlap)
- overlap between cases → inclusion-exclusion or Venn diagram

---

## Permutations

### r-permutations (no repetition)
$$P(n, r) = \frac{n!}{(n-r)!} = n(n-1)(n-2)\dots(n-r+1)$$
eg: how many ways to select 3 students from 5 to stand in line? $P(5,3) = 5 \cdot 4 \cdot 3 = 60$

### Permutations with repetition allowed (in output)
$$n^r$$
eg: strings of length 10 from lowercase English alphabet = $26^{10}$

### Permutations with repeated elements (in input)
$$\frac{n!}{n_1!\, n_2!\, \dots\, n_k!} \quad \text{where } n_1 + n_2 + \dots + n_k = n$$
eg: reordering letters of SUCCESS = $\frac{7!}{3!\,2!\,1!\,1!} = 420$

**two methods for repeated elements:**

method 1 (division rule): treat repeated elements as distinct → permute → divide by repetitions
eg: COOK → treat both O's as distinct → $4!$ total → divide by $2!$ for two O's

method 2 (position assignment): assign positions to each letter type iteratively
eg: C → choose 1 pos from 4 = $\binom{4}{1}$; O → choose 2 pos from 3 = $\binom{3}{2}$; K → fixed
more powerful — handles complex constraints

**harder example using position assignment:**
In how many ways can letters of PERMUTATIONS be arranged?
- 12 letters, T repeated twice
- $\binom{12}{2} \cdot 10!$

In how many ways can letters of PERMUTATIONS be arranged if there are always 4 letters between P and S?
- P and S with exactly 4 letters between them: 7 possible positions for the pair, 2 arrangements (PS or SP) → $7 \times 2$
- remaining 10 letters (T repeated): $10!/2!$
- total: $7 \times 2 \times 10!/2!$

**notation:** $\binom{n}{n_1, n_2, \dots, n_k} = \frac{n!}{n_1!\, n_2!\, \dots\, n_k!}$
eg: $\binom{20}{5,9,6} = \frac{20!}{5!\,9!\,6!}$

---

## Combinations

### r-combinations (no repetition)
$$C(n,r) = \binom{n}{r} = \frac{n!}{r!(n-r)!} = C(n,n-r)$$

combination = fancy application of division rule + product rule
→ divide by $r!$ so that permutation of selected objects doesn't matter

eg: how many committees of 3 from 5 students? $C(5,3) = 10$
eg: 3 professors from 9-person math dept AND 4 from 11-person CS dept? $C(9,3) \cdot C(11,4) = 84 \times 330 = 27720$

### Combinations with repetition (CWR)
$$\binom{n+r-1}{r} = \binom{n+r-1}{n-1}$$

eg: selecting 5 fruits from apple, mango, orange (with repetition) → star-bar problem

Notation: ((n, r)) = n boxes, r stars.

---

## Summary Table

| | Repetition allowed | No repetition |
|---|---|---|
| Ordered (lists) | $n^k$ | $P(n,k) = \frac{n!}{(n-k)!}$ |
| Unordered (sets/multisets) | $\binom{n+k-1}{k}$ | $C(n,k) = \binom{n}{k}$ |

---

## Special Arrangement Cases

| Situation                          | Method                                                  |
| ---------------------------------- | ------------------------------------------------------- |
| substring (order fixed)            | treat as single unit, permute with rest                 |
| subsequence (order doesn't matter) | treat as single unit; divide by 2 for unordered pair    |
| next to each other                 | bundle as one unit → permute → permute internally       |
| never next to each other           | fix other elements first → permute in gaps between them |

**super question:** In how many ways can letters of WONDERING be arranged with exactly two consecutive vowels?
- vowels: O, U, I; W, N, N, D, R, G
- which two vowels together: $\binom{3}{2}$ ways
- internal arrangement of chosen vowel pair: $2!$
- remaining consonants + vowel unit permutation: $\frac{6!}{2!}$ (N repeated)
- place the vowel pair in gaps: $_7P_2$ ... wait — actually place the pair among 7 positions
- total: $\binom{3}{2} \times 2! \times \frac{6!}{2!} \times {}_7P_2$
- key: OU, I → the third vowel must NEVER be adjacent to the pair

---

## Distributing Objects

### Distinguishable objects, distinguishable boxes (DODB)
$$\frac{n!}{n_1!\, n_2!\, \dots\, n_k!}$$
- if sizes don't sum to n → add a trash box
- no size constraint on boxes → each object picks any of m boxes → $m^n$

eg: distribute hands of 5 cards to 4 players from 52-card deck
- method 1: $\binom{52}{5}\binom{47}{5}\binom{42}{5}\binom{37}{5}$
- method 2: permute all 52 cards, first 5 go to player A, next 5 to B etc., order within box doesn't matter → divide by $5!$ four times → $52!/(5!\,5!\,5!\,5!\,32!)$

**at-least case (no trash box):**
Q: 8 distinct objects, 3 boys, everyone gets at least 2 objects
- case $(2+2+4)$: $\binom{3}{1} \times \binom{8}{4} \times \binom{4}{2} \times \binom{2}{2}$
- case $(2+3+3)$: $\binom{3}{1} \times \binom{8}{2} \times \binom{6}{3} \times \binom{3}{3}$
- **most common mistake:** $\binom{8}{2}\binom{6}{2}\binom{4}{2} \times 3^2$ ← wrong, overcounts

**size requirement permutable among boxes:**
eg: 15 distinguishable objects into 5 boxes with sizes 1,2,3,4,5
→ looks like IODB but it's DODB — permute the size assignments among boxes then apply
ie. permute the box sizes then apply the star bar method
### Identical objects, distinguishable boxes (IODB) — Star-Bars
$$\binom{n+r-1}{r} = \binom{n+r-1}{n-1}$$
- $r$ = objects (stars), $n$ = boxes, $n-1$ = bars
- only the count per box matters, not which identical object goes where

**two ways to derive:**
1. assign positions to bars (box boundaries): $\binom{r+n-1}{n-1}$
2. assign positions to stars (objects): $\binom{r+n-1}{r}$
3. via division: permute $(n-1+r)!$ total → divide by $r!$ (identical stars) and $(n-1)!$ (identical bars)

---

#### IODB Template — 6 Equivalent Problems

all reduce to $\binom{n+r-1}{r}$:

1. **Star-bar** — $r$ stars, $n$ boxes, $n-1$ bars
2. **IODB** — $r$ identical objects into $n$ distinct boxes
3. **CWR** — $r$-combinations from $n$ elements with repetition
4. **Multiset** — size-$r$ multisets from $n$-element set
5. **Integer solutions** — non-negative integer solutions to $x_1 + x_2 + \dots + x_n = r$
6. **Non-decreasing sequence** — sequences $1 \le a_1 \le a_2 \le \dots \le a_r \le n$

**variable restrictions in integer solutions:**
- $x_i > c$ → substitute $x_i' = x_i - c - 1$, reduce RHS by $c+1$
- $x_i \ge c$ → reduce RHS by $c$
- $\sum \le n$ → add slack variable $x_{r+1}$, solve $\sum = n$
- upper bound → complement or case-by-case if bound is small

eg: $x_1+x_2+x_3 < 11$, non-negative integers → introduce $x_4$: $x_1+x_2+x_3+x_4 = 11$
eg: $x_1+x_2+x_3+x_4+x_5 = 20$, all positive, $x_3 \le 3$ → complement or cases

**non-decreasing digit sequences:**
- digits from $\{1,\dots,9\}$, length $n$: $\binom{n+8}{8}$
- digits from $\{0,\dots,9\}$, length $n$: $\binom{n+9}{9} - 1$ (subtract all-zeros)
- strictly increasing/decreasing: not IODB. Simple combination problem.
- for numbers (not sequences): non-decreasing from $\{0,\dots,9\}$ → leftmost digit can't be 0 (except trivially); non-increasing → only leftmost can be nonzero constraint matters

Integer composition (ordered summation):
a composition of a positive integer n is a way of writing n as the sum of a sequence of positive integers.

This problem can be solved case by case:
Cases are the number of terms in composition of the integer.
For case k (number of terms), we have 
T1 + T2+....TK = n
and each T>=1
so it is IODB problem = (n-1,k-1) (after subtracting k from n and then dding k - 1)

Thus total no of compositons for n = sum((n-1,r-1)) from r=1  to n
= 2^n-1
Let n be a positive integer. Then the number of compositions of n is 2"-1. Proof: Let n be a positive integer. Then n can be written as a composition into 1 part, or 2 parts,..., and into n parts. So by the Addition rule and Theorem 3, the number of compositions of n is n Σ k=1 n- n- 1 (2) k- - -


---


### DOIB template
Friends Trip to Haunted Hotel with Same Rooms
=== no  of partitions or equaivlanet classes

When room sizes are distinct no problem of overcouting....
just select the object as per size requirment..
but when room sizes are same we have to use divide rool (divide rool)

9 Friends. Creating four groups, of size 2, size 2, Size 2, Size 3. How many ways?
answer = 
12 Friends. Creating five groups, of size 2, size 2, Size 2, Size 3, Size 3. How many ways?

A variation: the size requirments of rooms removed. now how many ways can the allocation happen?
work case by case....
the cases are how many rooms totaly used....
3 Friends. How many ways partitions can be created?
cases 1: 1 room (abc) -> i way
2 room: total two ways (2,1), (1,2) but these two are equivalnet so only one way (1,2)...hnece total 3c2*1c1 way = 3 ways now apply the previous method
3 room: only q way
total answer = 5

4 Friends. How many ways partitions can be created? 
(order doesnt matter)
Here is the simplified summary:

The total ways to partition $n$ elements into $k$ non-empty groups is calculated using **Stirling numbers of the second kind**, denoted as $S(n, k)$.

The total partitions for 4 elements is the 4th Bell number, $B_4$:

$$B_4 = \sum_{k=1}^{4} S(4, k)$$

## Step-by-Step Cases

- **1 Part $(k=1)$:** All together.
    
    $$S(4,1) = 1 \text{ way} \quad \implies \{abcd\}$$
    
- **2 Parts $(k=2)$:** Split as $(1,3)$ or $(2,2)$.
    
    $$S(4,2) = \binom{4}{1} + \frac{\binom{4}{2}}{2!} = 4 + 3 = 7 \text{ ways}$$
    
- **3 Parts $(k=3)$:** Split as $(1,1,2)$.
    
    $$S(4,3) = \binom{4}{2} = 6 \text{ ways}$$
    
- **4 Parts $(k=4)$:** All separate.
    
    $$S(4,4) = 1 \text{ way} \quad \implies \{a\},\{b\},\{c\},\{d\}$$
    

## Final Answer

$$\text{Total Ways} = 1 + 7 + 6 + 1 = 15$$

This DOIB is used to find number of equivlane realtions of a set (same as doing paritions of set)

---

### IOIB template
(intterger parititon probme)
In this case too we go case by case but here even (1,3) == (3,1) and each (1,3) has only 1 way...not like in the previous case becuase of disitnct objects muktiple ways...
so we have 
An **integer partition** of 4 treats the elements as **identical** (unlike the previous distinct items/employees). Therefore, we only care about the _sizes_ of the groups, not who is in them.

Here is the case-by-case breakdown for the partitions of 4:

### Case-by-Case Breakdown

- **1 Part:**
    
    $$4$$
    
    (1 way)
    
- **2 Parts:**
    
    $$3 + 1$$
    
    (1 way)
    
    $$2 + 2$$
    
    (1 way)
    
- **3 Parts:**
    
    $$2 + 1 + 1$$
    
    (1 way)
    
- **4 Parts:**
    
    $$1 + 1 + 1 + 1$$
    
    (1 way)
    

### Total Calculation

Adding up the ways from each case:

$$\text{Total Partitions } P(4) = 1 + 2 + 1 + 1 = 5$$
## Binomial Theorem

$$(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^k b^{n-k}$$

patterns:
1. $n+1$ terms, from $a^n$ to $b^n$
2. every term: coefficient $\times$ power of $a$ $\times$ power of $b$
3. exponents on $a$ and $b$ always sum to $n$
4. powers of $a$ decrease from $n$ to $0$; powers of $b$ increase from $0$ to $n$
5. $\sum_{r=0}^{n}\binom{n}{r} = 2^n$ (set $a=b=1$)

---

## Combinatorial Identities

### Symmetry
$$\binom{n}{r} = \binom{n}{n-r}$$

### Pascal's Identity
$$\binom{n+1}{k} = \binom{n}{k-1} + \binom{n}{k}$$
story: already selected one particular element (contributes $\binom{n}{k-1}$) OR already excluded it (contributes $\binom{n}{k}$)

variation with two particular elements:
$$\binom{n}{k} = \binom{n-2}{k-2} + 2\binom{n-2}{k-1} + \binom{n-2}{k}$$

recursive definition:
$$\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}$$

### Hockey Stick Identity
$$\sum_{k=r}^{n}\binom{k}{r} = \binom{n+1}{r+1}$$
$$nC_r + (n-1)C_r + \dots + rC_r = \binom{n+1}{r+1}$$

**story:** select $r+1$ numbers from $\{1, 2, \dots, n+1\}$
- side 1: $\binom{n+1}{r+1}$
- side 2: fix the maximum element
  - max = $n+1$ → $\binom{n}{r}$ ways for rest
  - max = $n$ → $\binom{n-1}{r}$
  - ...
  - max = $r+1$ → $\binom{r}{r}$

variation:
$$\binom{n}{r} = \binom{n+1}{r+1} - \binom{n}{r+1}$$
$$\binom{n-1}{r-1} = \binom{n}{r} - \binom{n-1}{r}$$

eg: ${}^5C_5 + {}^6C_5 + {}^7C_5 + {}^8C_5 + {}^9C_5 = ?$

### Vandermonde's Identity
$$\binom{m+n}{r} = \sum_{k=0}^{r}\binom{m}{k}\binom{n}{r-k}$$
story: choose $r$ from $m$ men + $n$ women; split by how many men selected
tip: when top of one side is a sum like $m+n$ → try committee from $m$ men + $n$ women (note: $2n = n+n$)

corollary: $\binom{2n}{n} = \sum_{k=0}^{n}\binom{n}{k}^2$
also: $\binom{2n}{2} = 2\binom{n}{2} + n^2$

### Committee-Chairman Identity
$$k\binom{n}{k} = n\binom{n-1}{k-1}$$
story:
1. pick $k$ committee members then pick president from them
2. pick president from $n$ first, then pick remaining $k-1$ from $n-1$

variation: pick $k-1$ ordinary members first, then president from remaining $n-k+1$
→ $(n-k+1)\binom{n}{k-1}$ gives same value

$$\sum_{k=0}^{n} k\binom{n}{k} = n \cdot 2^{n-1}$$
story: LHS = all ways to pick a subcommittee and designate one member as chairman
RHS = pick chairman first ($n$ ways), then pick rest of subcommittee ($2^{n-1}$ ways)

also: $(n,r) = \frac{n}{r}(n-1, r-1)$ — important, also a recursive definition

---

## Combinatorial Proof Strategy (GO Classes)
- argue LHS and RHS count the **same thing** two different ways
- summation on one side → sum rule; break into cases using a special object
- products involved → staged counting, product rule
- top involves $m+n$ → try committee from $m$ men + $n$ women
- no single "right" thing to count — pick something that makes it natural

**bijective proofs:** simplify by solving an equivalent problem
eg: counting subsets of size $k$ ↔ counting bit strings of length $n$ with exactly $k$ ones
→ assigning numbers or positions to elements often makes the problem easier

---

## Finding union

#### Use venn diagram. 
Many possibilites ways exisit to find union depending on given values
For eg |A UB| = |A-B| U |B-A| = |A|+|B| -|A and B|
etc
Inclusion exlcuion principle is one way out of many
#### Inclusion-Exclusion (General)
$$|A_1 \cup A_2 \cup \dots \cup A_n| = \sum|A_i| - \sum|A_i \cap A_j| + \sum|A_i \cap A_j \cap A_k| - \dots$$

- assign numbers to regions in Venn diagram based on how many sets they belong to
- add single-set regions, subtract double intersections, add triple, etc.
- $\max(|A|,|B|) \le |A \cup B| \le |A|+|B|$
  - first equality: when one is subset of the other
  - second equality: when disjoint

**counting multiples:**
- multiples of $r$ in $(a, b]$: $\lfloor b/r \rfloor - \lfloor a/r \rfloor$
- if $a$ included: $\lfloor b/r \rfloor - \lfloor (a-1)/r \rfloor$
- if $b$ is not a multiple of $r$, inclusive/exclusive at $b$ doesn't matter; if it is, it does
- by defualt thigns are inclusive\
- 