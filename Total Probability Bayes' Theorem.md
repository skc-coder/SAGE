# Total Probability Theorem & Bayes' Theorem

Topic: GATE CS > Probability > Conditional Probability Source: GO Classes — Probability Lec (Axioms of Conditional Probability, Marginalization, Bayes) Tags: #probability #total-probability #bayes-theorem #GATE2027 Links: [[moc probablity]] | [[Conditional Probability]] | [[Multiplication Rule, Tree Diagrams & Sequential Models]]

---

> [!info] Overview This note proves that conditional probability satisfies the three probability axioms, derives the Total Probability (Marginalization) theorem from a partition, states Bayes' Theorem, and works through the classic bags/chess-tournament examples.

---

## 1. Conditional Probability Satisfies the Three Axioms

It's not obvious in advance that $P(\cdot \mid B)$ behaves like a genuine probability law — this section proves it does.

### 1.1 Nonnegativity

$$ P(A) \geq 0 \quad\Longrightarrow\quad P(A\mid B) = \frac{P(A\cap B)}{P(B)} \geq 0 $$

(numerator and denominator are both nonnegative probabilities).

### 1.2 Normalization

$$ P(\Omega \mid B) = \frac{P(\Omega \cap B)}{P(B)} = \frac{P(B)}{P(B)} = 1 $$

### 1.3 Additivity

If $A_1, A_2$ are disjoint, we want to show $P(A_1 \cup A_2 \mid B) = P(A_1\mid B) + P(A_2 \mid B)$.

**Proof:**

$$ \begin{aligned} P(A_1 \cup A_2 \mid B) &= \frac{P\big((A_1 \cup A_2)\cap B\big)}{P(B)} \ &= \frac{P\big((A_1 \cap B)\cup(A_2\cap B)\big)}{P(B)} \quad \text{(distributive law)} \ &= \frac{P(A_1\cap B) + P(A_2 \cap B)}{P(B)} \quad \text{(} A_1\cap B,\ A_2\cap B \text{ disjoint since } A_1,A_2 \text{ are)}\ &= P(A_1\mid B) + P(A_2\mid B) \end{aligned} $$

> [!note] Key Idea Since conditional probability satisfies all three axioms, **every** rule derived from the axioms (Inclusion-Exclusion, De Morgan, complement rule, etc.) automatically also holds in "conditional form" — just insert "$\mid B$" everywhere.

### 1.4 Axioms — side-by-side comparison

||Axioms of Probability|Axioms of Conditional Probability|
|:--|:--|:--|
|Nonnegativity|$P(A) \geq 0$|$P(A\mid B) \geq 0$|
|Normalization|$P(\Omega) = 1$|$P(\Omega\mid B) = 1$|
|Additivity|$P(A_1\cup A_2)=P(A_1)+P(A_2)$, $A_1,A_2$ disjoint|$P(A_1\cup A_2\mid B)=P(A_1\mid B)+P(A_2\mid B)$, $A_1,A_2$ disjoint|

### 1.5 Rules — side-by-side comparison

|Rule|Unconditional|Conditional (add "$\mid B$" throughout)|
|:--|:--|:--|
|Equally likely|$P(A) = \dfrac{\text{elements in } A}{\text{total elements}}$|$P(A\mid B) = \dfrac{\text{elements of } A\cap B}{\text{elements of } B}$|
|Inclusion-Exclusion|$P(E\cup F) = P(E)+P(F)-P(E\cap F)$|$P(E\cup F\mid B) = P(E\mid B)+P(F\mid B)-P(E\cap F\mid B)$|
|De Morgan|$P((E\cap F)^c) = P(E^c\cup F^c)$|$P((E\cap F)^c\mid B) = P(E^c\cup F^c\mid B)$|
|Complement sum|$P(A)+P(A^c)=1$|$P(A\mid B)+P(A^c\mid B)=1$|

---

## 2. Marginalization / Total Probability Theorem

### 2.1 Partition requirement

**Critical condition:** the events $A_1, A_2, \dots, A_n$ must form a **partition** of the sample space, meaning:

1. **Mutually exhaustive:** $A_1 \cup A_2 \cup \cdots \cup A_n = \Omega$
2. **Mutually disjoint:** $A_i \cap A_j = \varnothing$ for $i \neq j$

> [!warning] Common Mistake The lecture explicitly demonstrates a case where $B$ does **not** touch $A_1,\dots,A_5$ at all (they don't cover the space or intersect $B$) — in that setting you _cannot_ write $B = (B\cap A_1)\cup\cdots\cup(B\cap A_5)$. The decomposition is only valid once the $A_i$'s are a genuine partition of the whole space.

### 2.2 Statement and proof (via Venn diagram / disjoint decomposition)

If $A_1, A_2, A_3$ partition $\Omega$, then for **any** event $B$:

$$ B = (B\cap A_1)\cup(B\cap A_2)\cup(B\cap A_3) $$

Since $A_1, A_2, A_3$ are disjoint, so are $B\cap A_1$, $B\cap A_2$, $B\cap A_3$. By additivity:

$$ P(B) = P(B\cap A_1) + P(B\cap A_2) + P(B\cap A_3) $$

Generalizing to $n$ parts, and rewriting each term via the multiplication rule:

$$ P(B) = \sum_{i=1}^{n} P(B\cap A_i) = \sum_{i=1}^{n} P(A_i),P(B \mid A_i) $$

$$ \boxed{P(B) = P(A_1)P(B|A_1) + P(A_2)P(B|A_2) + \cdots + P(A_n)P(B|A_n)} $$

This is also written (in a data-modeling context) as:

$$ P(X=2) = \sum_{k=1}^{n} P(X=2, Y=k) $$

### 2.3 Conditional-on-conditional version

Total probability also holds _inside_ an already-conditioned law:

$$ P(B \mid A) = P(B\cap A_1 \mid A) + P(B\cap A_2\mid A) + P(B\cap A_3 \mid A) $$

---

## 3. Bayes' Theorem

Starting from the definition of conditional probability and substituting the Total Probability expansion for the denominator:

$$ P(A \mid B) = \frac{P(A\cap B)}{P(B)} = \frac{P(A\cap B)}{P(B\cap A_1)+P(B\cap A_2)+P(B\cap A_3)} $$

Or, given a partition $A_1,\dots,A_n$ and using the multiplication rule throughout:

$$ \boxed{P(A_i \mid B) = \frac{P(A_i),P(B\mid A_i)}{\displaystyle\sum_{j=1}^{n} P(A_j),P(B\mid A_j)}} $$

**Extended (multi-condition) version**, conditioning everything additionally on background evidence $E$:

$$ P(A \mid B, E) = \frac{P(A\cap B \mid E)}{P(B\mid E)} = \frac{P(A\cap B\mid E)}{P(B\cap A_1\mid E)+P(B\cap A_2\mid E)+P(B\cap A_3\mid E)} $$

> [!note] Key Idea Bayes' Theorem is nothing more than "conditional probability definition" + "total probability to expand the denominator." You don't need to memorize it as a separate formula if the two building blocks are solid.

---

## 4. Worked Examples

> [!example] Three Bags of Marbles Question: Three bags each with 100 marbles: Bag 1 has 75 red/25 blue; Bag 2 has 60 red/40 blue; Bag 3 has 45 red/55 blue. Choose a bag at random, then a marble at random. What is $P(\text{red})$?
> 
> Approach: Step 1 — Each bag chosen with probability $1/3$ (a valid partition). Step 2 — Apply Total Probability.
> 
> $$ P(R) = \frac{1}{3}(0.75) + \frac{1}{3}(0.6) + \frac{1}{3}(0.45) = \frac{1}{3}(1.8) = 0.6 $$
> 
> Answer: $\boxed{0.6}$

> [!example] Chess Tournament Question: Probability of winning is $0.3$ against half the players (type 1), $0.4$ against a quarter (type 2), $0.5$ against the remaining quarter (type 3). You play a randomly chosen opponent. Find $P(\text{win})$.
> 
> Approach: Step 1 — $P(A_1)=0.5,\ P(A_2)=0.25,\ P(A_3)=0.25$; $P(B|A_1)=0.3,\ P(B|A_2)=0.4,\ P(B|A_3)=0.5$. Step 2 — Apply Total Probability.
> 
> $$ P(B) = 0.5(0.3) + 0.25(0.4) + 0.25(0.5) = 0.15+0.1+0.125 = 0.375 $$
> 
> Answer: $\boxed{0.375}$

---

## 5. Additional Conceptual T/F & Derivation Exercises

> [!example] Which is equal to P(B∩C | A)? Question: Which of the following equals $P(B\cap C \mid A)$? (a) $P(B\mid C\cap A)$ — (b) $\dfrac{P(B|C)}{P(A)}$ — (c) $P(B|C\cap A)P(C|A)$ — (d) $P(B|C)P(C|A)$
> 
> Approach: Treat "given $A$" as defining a whole new conditional probability law $P_A(\cdot)$. Then applying the multiplication rule _inside that law_:
> 
> $$ P(B\cap C \mid A) = P_A(B\cap C) = P_A(B\mid C)\cdot P_A(C) = P(B \mid C\cap A)\cdot P(C\mid A) $$
> 
> Answer: $\boxed{\text{(c)}}$

> [!example] Complement Identity — P(B̄ ∩ A) Question: Which is true — (a) $P(\overline{B}\cap A) = P(A) - P(B\cap A)$, or (b) $P(\overline{B}\cap A) = P(B) - P(B\cap A)$?
> 
> Approach: Split $A$ into two disjoint pieces: $A = (A\cap B)\cup(A\cap B^c)$. By additivity:
> 
> $$ P(A) = P(A\cap B) + P(A\cap B^c) \ \Rightarrow\ P(A\cap B^c) = P(A) - P(A\cap B) $$
> 
> Answer: $\boxed{\text{(a)}}$

> [!example] Exercise — Expressing P(B|A) in terms of B and Ā Question: Express $P(B\mid A)$ using only $P(B)$, $P(B\mid\overline{A})$, and $P(\overline{A})$.
> 
> Approach: Step 1 — Start from Total Probability with the partition ${A, \overline{A}}$:
> 
> $$ P(B) = P(B\mid A)P(A) + P(B\mid \overline{A})P(\overline{A}) $$
> 
> Step 2 — Solve for $P(B\mid A)$, using $P(A) = 1-P(\overline{A})$:
> 
> $$ P(B\mid A) = \frac{P(B) - P(B\mid\overline{A})P(\overline{A})}{1-P(\overline{A})} $$
> 
> This is presented in the lecture as a "does not simplify nicely" exercise — a reminder that Bayes-style rearrangements aren't always clean, and the more natural quantity to compute directly is usually $P(B\mid A)$ from context rather than backing it out from complements.

---

## Related Notes

- [[Conditional Probability]]
- [[Multiplication Rule, Tree Diagrams & Sequential Models]]
- [[GATE PYQs — Conditional Probability & Bayes' Theorem]]

## Open Questions

- [ ] None outstanding — all derivations in this note are complete and internally verified.

---

[[GATE PYQs — Conditional Probability & Bayes' Theorem]]