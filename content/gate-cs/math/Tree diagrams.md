# Multiplication Rule, Tree Diagrams & Sequential Models

Topic: GATE CS > Probability > Conditional Probability Source: GO Classes — Probability Lec (Multiplication Rule & Tree Diagrams) Tags: #probability #tree-diagrams #multiplication-rule #GATE2027 Links: [[moc probablity]] | [[Conditional Probability]] | [[Total Probability Theorem & Bayes' Theorem]]

---

> [!info] Overview The multiplication (product) rule lets you build up joint probabilities from a chain of conditionals; tree diagrams are the visual tool for sequential experiments. This note also covers the "concept question" MCQ set on reading tree diagrams correctly.

---

## 1. Multiplication Rule (Product Rule)

Directly follows from the definition of conditional probability:

$$ P(A \cap B) = P(A),P(B \mid A) = P(B),P(A \mid B) $$

since

$$ P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B \mid A) = \frac{P(A \cap B)}{P(A)} $$

**Notation:** $P(A \cap B)$ is often written $P(A,B)$ or $P(AB)$.

### 1.1 Chain rule for three or more events

$$ P(A \cap B \cap C) = P(A,B,C) = P(C)\cdot P(B \mid C)\cdot P(A \mid B,C) $$

$$ P(A,B,C,D) = P(D)\cdot P(C\mid D)\cdot P(B \mid C,D)\cdot P(A \mid B,C,D) $$

> [!note] Key Idea The chain rule works for **any** ordering of the events — you can peel them off in any sequence, as long as each step conditions on everything already "fixed."

### 1.2 MSQ — Valid Chain-Rule Expansions

> [!example] Concept MSQ — P(A,B,C) equivalent forms Question: Which of the following equal $P(A,B,C)$? (A) $P(C)\cdot P(B|C)\cdot P(A|B,C)$ (B) $P(A)\cdot P(B|A)\cdot P(C|A,B)$ (C) $P(B)\cdot P(A|B)\cdot P(C|A,B)$ (D) $P(B)\cdot P(C|B)\cdot P(A|B,C)$
> 
> Approach: Every option is just a different ordering in which the three events are "peeled off" — start with a marginal, condition the next on it, then condition the last on both previous. All four are algebraically valid decompositions of the same joint probability.
> 
> Answer: $\boxed{\text{All four (A, B, C, D) are correct}}$

---

## 2. Tree Diagrams for Sequential Experiments

Many experiments have an inherently sequential structure — e.g., tossing a coin three times, observing a stock over five days, or receiving eight successive digits at a receiver. A **tree diagram** represents each stage as a branching point, where each branch is labeled with a conditional probability given everything before it.

### 2.1 Basic structure

- **Branch** = one possible transition at a stage, labeled with its probability.
- **Node** = an intermediate or final outcome.
- Multiplying probabilities _along_ a path from root to leaf gives the **joint probability** of that full outcome sequence.

### 2.2 Coin toss tree (two tosses)

```
Start
├─0.5→ H
│        ├─0.5→ HH
│        └─0.5→ HT
└─0.5→ T
         ├─0.5→ TH
         └─0.5→ TT
```

Each leaf probability = product of branch probabilities along its path, e.g. $P(HH) = 0.5 \times 0.5 = 0.25$.

### 2.3 General partition tree

For a partition $A_1, A_2, A_3$ of the first stage, each followed by $B$ or $B^c$:

$$ P(A_i \cap B) = P(A_i)\cdot P(B \mid A_i) $$

Summing across all branches ending in $B$ gives the **total probability** of $B$ — this is developed fully in [[Total Probability Theorem & Bayes' Theorem]].

---

## 3. Worked Tree-Diagram Examples

> [!example] Goalkeeper Problem Question: With Coach Sam (probability $0.6$ of being coach today), your probability of being goalkeeper is $0.5$. With Coach Alex (probability $0.4$), it's $0.3$. What is the overall probability of being goalkeeper today?
> 
> Approach: Step 1 — Build the tree: Start → Sam ($0.6$) / Alex ($0.4$); Sam → G ($0.5$)/NG ($0.5$); Alex → G ($0.3$)/NG ($0.7$). Step 2 — Multiply along each "G" path, then sum (total probability rule).
> 
> $$ P(G) = P(\text{Sam}),P(G\mid\text{Sam}) + P(\text{Alex}),P(G\mid\text{Alex}) = 0.6\times0.5 + 0.4\times0.3 = 0.3 + 0.12 = 0.42 $$
> 
> Answer: $\boxed{0.42}$

> [!example] Sunday Evening — Watching Cricket and Seeing Ads Question: On a Sunday evening, 50% watch a movie, 30% watch cricket, 20% watch comedy. The percentage skipping ads is 20%, 25%, 15% respectively. Find $P(\text{watch cricket AND see ads})$.
> 
> Approach: Step 1 — $P(\text{skip ads}\mid\text{cricket}) = 0.25 \Rightarrow P(\text{see ads}\mid\text{cricket}) = 0.75$. Step 2 — Multiply along the branch: cricket ($0.3$) → see ads ($0.75$).
> 
> $$ P(\text{cricket} \cap \text{see ads}) = P(\text{cricket})\cdot P(\text{see ads}\mid\text{cricket}) = 0.3 \times 0.75 = 0.225 $$
> 
> Answer: $\boxed{0.225}$
> 
> (Full tree also computes the other five leaf probabilities: Movies+see ads $=0.4$, Movies+skip $=0.1$, Cricket+skip $=0.075$, Comedy+see ads $=0.17$, Comedy+skip $=0.03$ — all six sum to $1$.)

> [!example] Urn Problem — Sequential Draws Without Replacement Question: An urn has 5 red and 2 green balls. Draw a ball; if green, add a red ball to the urn; if red, add a green ball (original ball not returned). Draw a second ball. What is the probability the second ball is red?
> 
> Approach: Step 1 — First draw: $P(R_1) = 5/7$, $P(G_1) = 2/7$. Step 2 — After a red draw + green ball added: urn has 4R, 3G (of 7) → $P(R_2\mid R_1) = 4/7$. Step 3 — After a green draw + red ball added: urn has 6R, 1G (of 7) → $P(R_2\mid G_1) = 6/7$. Step 4 — Apply total probability.
> 
> $$ P(R_2) = P(R_2|R_1)P(R_1) + P(R_2|G_1)P(G_1) = \frac{4}{7}\cdot\frac{5}{7} + \frac{6}{7}\cdot\frac{2}{7} = \frac{20}{49}+\frac{12}{49} = \frac{32}{49} $$
> 
> Answer: $\boxed{32/49}$

---

## 4. Concept MCQs — Reading a Tree Diagram Correctly

The lecture uses a 4-level tree (Root → $A_1/A_2$ → $B_1/B_2$ → $C_1/C_2$) with branch labels $x$ (Root→$A_1$), $y$ ($A_1$→$B_1$), $z$ ($B_2$→$C_1$, under $A_1$), and a circled leaf node $A_1 \cap B_2 \cap C_1$.

|Q|Asks about|Answer|Reasoning|
|:--|:--|:--|:--|
|1|What does branch $x$ (Root→$A_1$) represent?|(a) $P(A_1)$|It's the _first_ branching, unconditioned — a plain marginal probability.|
|2|What does branch $y$ ($A_1$→$B_1$) represent?|(c) $P(B_2 \mid A_1)$|Second-level branch — conditioned on everything above it, i.e. on $A_1$.|
|3|What does branch $z$ ($B_2$→$C_1$, under $A_1$) represent?|(d) $P(C_1 \mid B_2 \cap A_1)$|Third-level branch — conditioned on the _entire path_ above it.|
|4|What does the circled leaf node represent?|(c) $A_1 \cap B_2 \cap C_1$|A leaf node is the **event** of the full path, not a probability value.|

> [!warning] Common Mistake Students often mistake a deep branch's label for an _unconditional_ probability (e.g., calling $z$ just "$P(C_1|B_2)$"). Every branch below the root is conditioned on **the entire path taken to reach it**, not just the immediately preceding node.

---

## 5. Informal Sequential/Chain-Rule Illustrations (from lecture, non-numeric)

The lecture also sketches informal chain-rule intuitions without full numeric solutions:

- **WhatsApp autocomplete example:** modeling next-word prediction as a chain of conditionals, e.g. $P(\text{"Mittal"} \mid \text{"I am Sachin"}) \approx 0.9$ vs. $P(\text{"Mittal"} \mid \text{"I am"}) \approx 0.2$ — illustrating how more context (longer conditioning history) sharpens the prediction.
- **"Broken computer in IISc" example:** used to motivate that conditioning on a _longer_ history ($A, B$, starting point) but where later stages only depend on the immediate recent state simplifies to $P(C \mid A,B,\text{start}) = P(C \mid A, B)$ — an early, informal nod to the _Markov property_ (only recent state matters, not full history).

These are conceptual scaffolding for tree diagrams and are not presented as standalone solvable questions.

---

## Related Notes

- [[Conditional Probability]]
- [[Total Probability Theorem & Bayes' Theorem]]

## Open Questions

- [ ] The "broken computer in IISc" and WhatsApp examples are informal — check if GO Classes ties these explicitly to the term "Markov chain" later in the course (relevant since Aishwarya's CS/Math PYQ in the next note is a 2-state Markov chain).

---

