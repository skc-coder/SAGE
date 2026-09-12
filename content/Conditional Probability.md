# Conditional Probability — Concepts, Definition & Examples

Topic: GATE CS > Probability > Conditional Probability Source: GO Classes — Probability Lec (Conditional Probability intro) Tags: #probability #conditional-probability #GATE2027 Links: [[moc probablity]] | [[Probability foundations]] | [[Multiplication Rule, Tree Diagrams & Sequential Models]]

---

> [!info] Overview 
> Conditional probability is about updating belief once you learn partial information. This note covers the intuition, the formal definition, its own set of axioms, and a large batch of worked examples (dice, coins, covid, family-gender puzzle).

---

## 1. Intuition — "Change in Belief"

Conditional probability answers: _given that some event has already occurred, how does that change the probability of another event?_

### 1.1 Cricket example

Let $A$ = "India will win," $B$ = "India scores 395 runs batting first."

- Before play starts: $P(A) = 0.5$.
- After India scores 395: $P(A \mid B) > 0.8$.

Learning that $B$ occurred **changed our belief** about $A$:

$$ P(A \mid B) \neq P(A), \qquad P(A \mid B) > P(A) $$

### 1.2 The three possible relationships

In general, knowing $B$ occurred can:

$$ \begin{aligned} P(A|B) &> P(A) \ P(A|B) &< P(A) \ P(A|B) &= P(A) \end{aligned} $$

There is no fixed rule connecting $P(A)$ and $P(A|B)$ in general — it depends entirely on how $A$ and $B$ relate.

### 1.3 Covid example

If $1\%$ of the population has Covid, $P(\text{has covid}) = 1/100$. But given someone shows **symptoms** of Covid, $P(\text{has covid} \mid \text{symptoms}) \approx 1$ — conditioning drastically shifts the belief.

---

## 2. Dice-Rolling Examples of Conditioning

### 2.1 Sum of two dice equals 9, with partial info

Without any prior information:

$$ P(\text{sum}=9) = \frac{4}{36} = \frac{1}{9} \qquad \text{(from } (3,6),(4,5),(5,4),(6,3)\text{)} $$

**Case B — first face is known to be 6:** among ${(6,1),\dots,(6,6)}$ (6 outcomes), only $(6,3)$ sums to 9.

$$ P(\text{sum}=9 \mid \text{first}=6) = \frac{1}{6} $$

**Case — first face is 4:** among ${(4,1),\dots,(4,6)}$, only $(4,5)$ sums to 9.

$$ P(\text{sum}=9 \mid \text{first}=4) = \frac{1}{6} $$

### 2.2 Even face given, probability that a 2 occurred

Without conditioning: $P(2) = 1/6$.

With the information that the face is even, the sample space effectively shrinks to ${2,4,6}$:

$$ P(2 \mid \text{even face}) = \frac{1}{3} $$

**Formal derivation (redistribution view):** each even outcome originally had probability $1/6$; summed together the even outcomes have total probability $1/2$. 
Renormalizing (since odd faces have probablity zero, to satisfying axioms of probability that of normalization, we normalize, thus dividing each by $1/2$) redistributes $1/6 \to 1/3$ for each of ${2,4,6}$.

> [!note] Not Required for GATE 
> The lecture explicitly frames this "new sample space $\Omega' = {2,4,6}$ with redistributed probability $q(2)=1/3$" viewpoint as conceptual background, **not required for GATE** directly — the formula-based approach below is what matters for exams.

### 2.3 Skewed-probability version of the same idea

Given a die with unequal face probabilities $P(S_1){=}1/4, P(S_2){=}1/8, P(S_3){=}1/4, P(S_4){=}1/8, P(S_5){=}1/8, P(S_6){=}1/8$, and conditioning on the event ${S_1, S_3, S_5}$ (total probability $= 1/4+1/4+1/8 = 5/8$):

$$ P(S_1 \mid {S_1,S_3,S_5}) = \frac{1/4}{5/8} = \frac{1}{4}\times\frac{8}{5} = \frac{2}{5} $$

$$ P(S_2 \mid {S_1,S_3,S_5}) = 0 \qquad \text{(} S_2 \text{ is not in the conditioning set)} $$

---

## 3. Formal Definition of Conditional Probability

(think in terms of discrete elements)

![[2026-07-01_19-09.png]]
$$ P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad \text{valid when } P(B) > 0 $$

Under equally likely outcomes, this reduces to a pure counting formula:

$$ P(A \mid B) = \frac{n(A \cap B)}{n(B)} \qquad \left(\text{since } P(A\cap B) = \frac{n(A\cap B)}{n(S)},\ P(B)=\frac{n(B)}{n(S)}\right) $$

### 3.1 Properties (from MIT 6.041 notes)

- $P(A \mid B)$, for fixed $B$ with $P(B) > 0$, defines a **brand-new probability law** on the same sample space $\Omega$. All the usual axioms/properties of probability still hold for this conditional law.
- **Intuitively, conditioning can be viewed as defining a probability law on a new universe $B$ — all the probability "mass" becomes concentrated on $B$.**
- For finitely many equally-likely outcomes:

$$ P(A \mid B) = \frac{\text{number of elements of } A \cap B}{\text{number of elements of } B} $$

### 3.2 Venn-diagram intuition (15 equally-weighted dots)

Sample space has 15 equally likely dots ($P(\text{each dot}) = 1/15$). Circle $A$ contains 3 dots, circle $B$ contains 2... actually contains 4 dots total in the lecture's labeled diagram, with $A \cap B$ containing 2 dots, giving $P(B) = 4/15$.

"$B$ has already occurred" means we mentally discard everything outside $B$ and **renormalize** within $B$:

$$ P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{2/15}{4/15} = \frac{2}{15} \times \frac{15}{4} = \frac{1}{2} $$

$$ P(A^{c} \mid B) = \frac{1}{4} + \frac{1}{4} = \frac{1}{2} $$

(consistent with $P(A|B) + P(A^c|B) = 1$).

> [!warning] Common Mistake A wrong intuitive shortcut in the lecture explicitly flags: don't just re-label the dots inside $A \cap B$ with their _original_ unconditioned probability ($1/15$) and stop there — you must divide by $P(B)$ to renormalize. Forgetting to renormalize is the single most common conditional-probability slip.

---

## 4. Worked Examples

> [!example] Die Roll — P(2) Given Face < 4 Question: A die is rolled with the extra information that the result is less than 4. What is the probability that 2 occurred?
> 
> Approach: Step 1 — Conditioning event: ${1,2,3}$. Step 2 — Apply the formula.
> 
> $$ P({2} \mid {1,2,3}) = \frac{P({2})}{P({1,2,3})} = \frac{1/6}{3/6} = \frac{1}{3} $$
> 
> Answer: $\boxed{1/3}$

> [!example] Family With Two Children (Part a) Question: Sample space $S = {(G,G),(G,B),(B,G),(B,B)}$, all equally likely. What is the probability both children are girls, given the first child is a girl?
> 
> Approach: Step 1 — Conditioning event: ${(G,G),(G,B)}$.
> 
> $$ P\big((G,G) \mid {(G,G),(G,B)}\big) = \frac{1/4}{1/4+1/4} = \frac{1}{2} $$
> 
> Answer: $\boxed{1/2}$

> [!example] Family With Two Children (Part b) Question: The father says "I have at least one daughter." Given this, what is the probability both children are girls?
> 
> Approach: Step 1 — Conditioning event now includes all outcomes with at least one girl: ${(G,G),(G,B),(B,G)}$.
> 
> $$ P\big((G,G) \mid {(G,G),(G,B),(B,G)}\big) = \frac{1/4}{3/4} = \frac{1}{3} $$
> 
> Answer: $\boxed{1/3}$
> 
> Note the contrast with Part (a): "first child is a girl" pins down _order_, giving $1/2$; "at least one is a girl" is a weaker, order-agnostic condition, giving $1/3$. This is a classic conditional-probability trap.

> [!example] Two Dice — Sum Equals 5 Question: A fair six-sided die is thrown twice. $E = {$sum of the two tosses is 5$}$. (a) Find $P(E)$. (b) Given $E$ happens, what is the probability the first toss is less than the second?
> 
> Approach: Step 1 — $E = {(1,4),(2,3),(3,2),(4,1)}$, so $P(E) = 4/36 = 1/9$. Step 2 — Within $E$, "first < second" corresponds to ${(1,4),(2,3)}$.
> 
> $$ P(\text{first} < \text{second} \mid E) = \frac{2/36}{4/36} = \frac{1}{2} $$
> 
> Answer: (a) $\boxed{1/9}$, (b) $\boxed{1/2}$

> [!example] Three Coin Flips — Events A and B Question: Flip three fair coins. $A$ = "first two coins are both heads." $B$ = "third coin is different from the second coin." (a) Find $P(A)$ and $P(B)$. (b) Find $P(A \mid B)$.
> 
> Approach: Step 1 — Enumerate: $A = {HHT, HHH}$, so $P(A) = 2/8 = 1/4$. Step 2 — $B = {HHT, THT, HTH, TTH}$ (third differs from second), so $P(B) = 4/8 = 1/2$. Step 3 — $A \cap B = {HHT}$, so $P(A \cap B) = 1/8$.
> 
> $$ P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{1/8}{4/8} = \frac{1}{4} $$
> 
> Answer: $P(A) = \boxed{1/4}$, $P(B) = \boxed{1/2}$, $P(A|B) = \boxed{1/4}$

---

## 5. True/False Drill — Conditional Probability Identities

The lecture uses a long True/False set to stress-test intuition about which identities actually hold. All are worked with brief reasoning; see [[Total Probability Theorem & Bayes' Theorem]] for the axioms these rely on.

|#|Statement|Verdict|One-line reason|
|:--|:--|:--|:--|
|1|$P(A|B) + P(A^{c}|B) = 1$|
|2|$P(A|B) + P(A|B^{c}) = 1$|
|3|$P(A|B^{c}) + P(A^{c}|B) = 1$|
|4|$P(\overline{B}|A) = 1 - P(B|A)$|
|5|$P(\overline{B}|A) = P(B) - P(B|A)$|
|6|$P(E,F) + P(E^{c}\cup F^{c}) = 1$|**True**|$E^c \cup F^c = (E\cap F)^c$ by De Morgan, so this is just $P(EF)+P((EF)^c)=1$.|
|7|$P(E\cup F) = 1 - P(E^{c}|F^{c})P(F^{c})$|**True**|
|8|$P(E|F^{c}) + P(E|F) = 1$|
|9|$P(E,F|E) = P(E,F|F)$|
|10|$P(E|F) = P(E|F,G)P(G|
|11|$P(E,F,G) \leq \min{P(E),P(F),P(G)}$|**True**|$E\cap F\cap G$ is a subset of each of $E$, $F$, $G$ individually, so its probability can't exceed any of theirs.|
|12|If $P(E|F)>P(E)$, then $P(F|E)>P(F)$|

> [!note] Key Idea Whenever a T/F statement conditions on _two different_ events on each side (e.g., $B$ vs $B^c$), be suspicious — these almost never simplify to a clean identity unless you can invoke total probability or De Morgan explicitly.

### 5.1 Subset monotonicity

> [!example] If A ⊆ B, then P(A) ≤ P(B) Question: True or False — if $A$ and $B$ are events with $A \subseteq B$, then $P(A) \leq P(B)$?
> 
> Approach: Step 1 — Define $C = B \setminus A$ (the part of $B$ outside $A$), so $B = A \cup C$ with $A, C$ disjoint.
> 
> $$ P(B) = P(A \cup C) = P(A) + P(C) $$
> 
> Step 2 — Since $P(C) \geq 0$ (Axiom 1), $P(B) \geq P(A)$.
> 
> Answer: $\boxed{\text{True}}$

---

## Related Notes

- [[Probability foundations]]
- [[Multiplication Rule, Tree Diagrams & Sequential Models]]
- [[Total Probability Theorem & Bayes' Theorem]]

## Open Questions

- [ ] The "new sample space redistribution" framing (§2.2) is marked "not required for GATE" — confirm this isn't secretly needed for any PYQ pattern before fully deprioritizing it.

---

