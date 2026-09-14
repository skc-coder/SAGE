# Sample Space, Events, Axioms and theorems of Probability

Topic: GATE CS > Probability > Foundations Source: GO Classes — Probability Lec (Reference: John Tsitsiklis, MIT 6.041 course notes) Tags: #probability #axioms #foundations #GATE2027 Links: [[moc probablity]] | [[Inclusion-Exclusion & De Morgan's Law for Probability]]

---

> [!info] Overview This note covers the building blocks of probability theory: experiments, sample spaces, events, the probability function, and the three axioms that everything else in the course is built on.

---

## 1. Scope of the Course

### 1.1 What will be studied

The course builds probability from first principles: basic definitions, sample space and events, Bayes' theorem, and random variables/probability distributions.

### 1.2 What will NOT be studied

Combinatorics-style counting (permutations & combinations) is treated as a separate topic under Discrete Mathematics, not under Probability.

> [!note] Reference Primary reference text: John Tsitsiklis' MIT probability course notes.

---

## 2. What Does "Probability" Actually Mean?

### 2.1 The frequentist intuition

Saying "probability of heads on a fair coin is $1/2$" does **not** mean that in any small number of tosses you'll get exactly half heads.

- Toss 2 times → 1 head? Not guaranteed.
- Toss 4 times → 2 heads? Not guaranteed.
- Toss 100 times → 50 heads? Not guaranteed.

Even 100 heads in a row is _possible_, just extremely unlikely: probability $(1/2)^{100}$.

### 2.2 The long-run limit

As the number of trials grows very large, the _fraction_ of heads converges to $1/2$. Karl Pearson tossed a coin 24,000 times and got 12,012 heads; a separate experiment of 2,000 tosses gave 996 heads — both very close to 50%.

$$ \lim_{n \to \infty} \frac{n(H)}{n} = \frac{1}{2} $$

where $n(H)$ is the number of heads observed and $n$ is the total number of tosses.

> [!note] Key Idea Probability describes long-run relative frequency, not a guarantee about any specific finite run.

---

## 3. Sample Space and Events

### 3.1 Experiment and Sample Space

An **experiment** is an underlying process that produces exactly one out of several possible outcomes. The **sample space** $\Omega$ (or $S$) is the set of _all_ possible outcomes of that experiment.

Example — tossing a coin: $\Omega = {H, T}$.

### 3.2 Properties a valid sample space must satisfy

- It is a list (set) of possible outcomes.
- The outcomes must be **mutually exclusive** (no overlap).
- The outcomes must be **collectively exhaustive** (cover every possibility).

### 3.3 Events

An **event** is a subset of the sample space — a collection of possible outcomes.

Example — rolling a die, sample space $\Omega = {1,2,3,4,5,6}$:

- $E_1 = {1,2}$, $P(E_1) = 2/6$
- $E_2 = {3,4,5}$, $P(E_2) = 3/6$
- $E_3 = {5}$, $P(E_3) = 1/6$ (intersection region of $E_1,E_2$-style diagram in lecture)

The set of _all possible events_ is the power set $2^{\Omega}$. For $\Omega = {H,T}$:

$$ 2^{\Omega} = \big{, \varnothing,\ {H},\ {T},\ {H,T} ,\big} $$

with $P(\varnothing)=0$, $P({H})=1/2$, $P({T})=1/2$, $P({H,T})=1$.

### 3.4 Probability as a function

Probability is a **function** that maps every event (a subset of $\Omega$) to a real number:

$$ P : 2^{\Omega} \longrightarrow [0,1] $$

> [!note] Key Idea $\Omega$ is the _universe_ of outcomes; an event is a _subset_; probability is a _function_ from subsets to $[0,1]$. Keep these three roles distinct.

### 3.5 Worked sample space examples

| Experiment                                          | Sample space                                       |
| :-------------------------------------------------- | :------------------------------------------------- |
| Sex of a newborn child                              | $S = {g, b}$                                       |
| Finish order of a 7-horse race (post positions 1–7) | $S = {$all $7!$ permutations of $(1,2,3,4,5,6,7)}$ |
| Flipping two coins                                  | $S = {(H,H),(H,T),(T,H),(T,T)}$                    |
| Tossing a coin twice                                | ${HH, HT, TH, TT}$                                 |
| Rolling a die                                       | $\Omega = {1,2,3,4,5,6}$                           |

For the horse race: knowing only who finished **first** gives sample space ${1,\dots,7}$ (7 outcomes). Knowing the **first two** finishing positions gives $7 \times 6 = 42$ ordered outcomes, e.g. ${12, 13, 14, \dots, 76}$.

---

## 4. Axioms of Probability

### 4.1 The three axioms

$$ \begin{aligned} \textbf{1. Nonnegativity:}\quad & P(A) \geq 0 \ \textbf{2. Normalization:}\quad & P(\Omega) = 1 \ \textbf{3. Additivity:}\quad & \text{If } A \cap B = \varnothing, \text{ then } P(A \cup B) = P(A) + P(B) \end{aligned} $$

For a partition of the sample space into disjoint elementary outcomes ${s_1, s_2, s_3}$:

$$ P({s_1, s_2, s_3}) = P(s_1) + P(s_2) + P(s_3) = 1 $$

More generally, for disjoint outcomes $s_1, \dots, s_n$ covering $\Omega$:

$$ P({s_1, s_2, \dots, s_n}) = P(s_1) + P(s_2) + \dots + P(s_n) $$

### 4.2 Countable Additivity Axiom

If $A_1, A_2, \dots$ are pairwise disjoint events (possibly infinitely many, but **countable**), then:

$$ P(A_1 \cup A_2 \cup \cdots) = P(A_1) + P(A_2) + \cdots $$

> [!warning] Countable vs Uncountable This axiom only applies to a _countable_ union. For an uncountable union (e.g., summing probability over every real point in $[0,1]$), the additivity argument breaks down — that's why a single point on a continuous interval, e.g. $P(X = 0.2)$, is $0$ even though the interval itself has probability $1$.

---

## 5. Equally Likely Outcomes

### 5.1 Deriving $P(s_i) = 1/n$

If all outcomes $s_1, \dots, s_n$ are equally likely, Axiom 2 (normalization) plus Axiom 3 (additivity) give:

$$ \begin{aligned} P({s_1} \cup {s_2} \cup \cdots \cup {s_n}) &= 1 \ P(s_1) + P(s_2) + \cdots + P(s_n) &= 1 \ \Rightarrow \quad P(s_i) &= \frac{1}{n} \quad \text{for every } i \end{aligned} $$

### 5.2 Probability of an event under equally likely outcomes

For an event $A = {s_1, \dots, s_k}$:

$$ P(A) = \underbrace{\dfrac{1}{n} + \dfrac{1}{n} + \cdots + \dfrac{1}{n}}_{k \text{ terms}} = \dfrac{k}{n} = \dfrac{\text{number of elements in } A}{\text{total number of sample points}} $$

> [!warning] Common Mistake 
> This formula (count of favorable / total count) **only** works when outcomes are equally likely. The lecture explicitly shows a counter-example where ${s_1,s_2,s_3}$ have probabilities $1/6, 1/6, 2/6$ (not equal) — here $P(s_1,s_2,s_3) = 4/6 = 2/3$, **not** $3/6$ (which you'd wrongly get by just counting elements).

---

## 6. Worked PYQ

> [!example] Two Dice — Sum Equals 7 Question: If two dice are rolled, what is the probability that the sum of the upturned faces equals 7?
> 
> Approach: Step 1 — Total equally likely outcomes when rolling two dice: $6 \times 6 = 36$. Step 2 — Favorable outcomes summing to 7: $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$ — 6 outcomes.
> 
> $$ P(\text{sum}=7) = \frac{n(A)}{n} = \frac{6}{36} = \frac{1}{6} $$
> 
> Answer: $\boxed{1/6}$

---

## Related Notes

- [[Inclusion-Exclusion & De Morgan's Law for Probability]]
- [[Conditional Probability]]

## Open Questions

- [ ] Double check the exact bar-chart values from the "die with unequal probabilities" diagram (0.1, 0.25, 0.3, 0.05, 0.1, 0.45) — these don't sum to 1 in the raw notes (sums to 1.25), likely a transcription/handwriting issue in the source slide. Worth re-checking against the original lecture recording.

---

# Inclusion-Exclusion & De Morgan's Law for Probability

Topic: GATE CS > Probability > Foundations Source: GO Classes — Probability Lec Tags: #probability #inclusion-exclusion #demorgan #GATE2027 Links: [[moc probablity]] | [[Probability foundations]]

---

> [!info] Overview Covers the Inclusion-Exclusion Principle (2 and 3 events, with proof) and De Morgan's Laws applied to probability, plus two classic GATE PYQs that use them directly.

---

## 1. Inclusion-Exclusion Principle

### 1.1 Two events

$$ P(E \cup F) = P(E) + P(F) - P(E \cap F) $$

### 1.2 Three events

$$ \begin{aligned} P(E \cup F \cup G) = \ &P(E) + P(F) + P(G) \ &- P(E \cap F) - P(E \cap G) - P(F \cap G) \ &+ P(E \cap F \cap G) \end{aligned} $$

### 1.3 Proof for two events (via disjoint decomposition)

Split the Venn diagram of $E$ and $F$ into three **disjoint** regions:

- $a = E \cap F^{c}$ (only $E$)
- $b = E \cap F$ (overlap)
- $c = F \cap E^{c}$ (only $F$)

Since $E \cup F = a \cup b \cup c$ and these three pieces are disjoint, Axiom 3 gives:

$$ P(E \cup F) = P(a) + P(b) + P(c) $$

Now express $P(E)$, $P(F)$, and $P(E \cap F)$ in terms of $a, b, c$:

$$ \begin{aligned} P(E) &= P(a) + P(b) \ P(F) &= P(b) + P(c) \ P(E \cap F) &= P(b) \end{aligned} $$

So:

$$ P(E) + P(F) - P(E \cap F) = \big[P(a)+P(b)\big] + \big[P(b)+P(c)\big] - P(b) = P(a)+P(b)+P(c) $$

which matches $P(E \cup F)$ exactly — the extra $P(b)$ term cancels because $b = E \cap F$ was double-counted once in $P(E)$ and once in $P(F)$.

> [!note] Key Idea Inclusion-Exclusion is really just "count the overlap once, not twice" — the proof works by breaking the union into disjoint pieces where plain additivity (Axiom 3) applies directly.

---

## 2. De Morgan's Law for Probability

$$ (E \cap F)^{c} = E^{c} \cup F^{c} \qquad \Longrightarrow \qquad P\big((E \cap F)^{c}\big) = P(E^{c} \cup F^{c}) $$

$$ (E \cup F)^{c} = E^{c} \cap F^{c} \qquad \Longrightarrow \qquad P\big((E \cup F)^{c}\big) = P(E^{c} \cap F^{c}) $$

### 2.1 Complement identities derived from De Morgan

Using $P(A) + P(A^{c}) = 1$ together with De Morgan's Law:

$$ \begin{aligned} P(E \cap F) &= 1 - P\big((E \cap F)^{c}\big) = 1 - P(E^{c} \cup F^{c}) \[4pt] P(E \cup F) &= 1 - P\big((E \cup F)^{c}\big) = 1 - P(E^{c} \cap F^{c}) \end{aligned} $$

These are extremely useful whenever a question gives you complement-side information and asks for a union or intersection.

---

## 3. Worked PYQs

> [!example] GATE CSE 1997 — Rain Today and Tomorrow Question: The probability that it will rain today is $0.5$. The probability that it will rain tomorrow is $0.6$. The probability that it will rain either today or tomorrow is $0.7$. What is the probability that it will rain today **and** tomorrow?
> 
> Approach: Step 1 — Recognize this is a direct Inclusion-Exclusion setup. Step 2 — Let $x = P(\text{today} \cap \text{tomorrow})$.
> 
> $$ P(\text{today} \cup \text{tomorrow}) = P(\text{today}) + P(\text{tomorrow}) - x $$
> 
> $$ 0.7 = 0.5 + 0.6 - x \ \Rightarrow\ x = 1.1 - 0.7 = 0.4 $$
> 
> Answer: $\boxed{0.4}$ (Option D)

> [!example] GATE IT 2008 — Union from Complements Question: A sample space has two events $A$ and $B$ such that $P(A \cap B) = \dfrac{1}{2}$, $P(A') = \dfrac{1}{3}$, $P(B') = \dfrac{1}{3}$. Find $P(A \cup B)$.
> 
> Approach: Step 1 — Convert complements to direct probabilities: $P(A) = 1 - \dfrac{1}{3} = \dfrac{2}{3}$, $P(B) = \dfrac{2}{3}$. Step 2 — Apply Inclusion-Exclusion.
> 
> $$ P(A \cup B) = P(A) + P(B) - P(A \cap B) = \frac{2}{3} + \frac{2}{3} - \frac{1}{2} = \frac{4}{3} - \frac{1}{2} = \frac{8-3}{6} = \frac{5}{6} $$
> 
> Answer: $\boxed{10/12 = 5/6}$ (Option B)

---

## Related Notes

- [[Probability foundations]]
- [[Conditional Probability]]

## Open Questions

- [ ] None — both PYQs fully solved and cross-checked against the source's ticked answers.

---

