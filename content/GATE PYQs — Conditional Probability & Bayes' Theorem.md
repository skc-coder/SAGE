
# GATE PYQs — Conditional Probability & Bayes' Theorem

Topic: GATE CS > Probability > Conditional Probability Source: GO Classes — GATE PYQs on Conditional Probability Tags: #probability #GATE-PYQ #bayes-theorem #GATE2027 Links: [[moc probablity]] | [[Total Probability Theorem & Bayes' Theorem]] | [[Multiplication Rule, Tree Diagrams & Sequential Models]]

---

> [!info] Overview A dedicated PYQ set applying total probability, Bayes' theorem, and tree diagrams to real GATE (and GATE-adjacent) questions. Every question below is fully solved, including a few where the lecture only sketched the setup.

---

## 1. Sequential Travel — Samsung Coding Test Style

> [!example] Bengaluru → Hyderabad/Chennai → Mumbai/Pune Question: A person starts in Bengaluru. With probability $0.1$ he goes to Hyderabad, $0.9$ to Chennai. From Hyderabad: $0.3$ to Mumbai, $0.7$ to Pune. From Chennai: $0.8$ to Mumbai, $0.2$ to Pune. (i) $P(\text{Pune})$? (ii) $P(\text{Mumbai})$? (iii) Given he's in Mumbai, $P(\text{came from Hyderabad})$?
> 
> Approach: Step 1 — Note the Markov-style simplification used in the lecture: $P(M\mid H, B) = P(M\mid H)$ — once you know he went to Hyderabad, the earlier "started in Bengaluru" fact adds nothing more. Step 2 — Total probability for Pune and Mumbai.
> 
> $$ P(\text{Pune}) = 0.1(0.7) + 0.9(0.2) = 0.07+0.18 = 0.25 $$
> 
> $$ P(\text{Mumbai}) = 0.1(0.3) + 0.9(0.8) = 0.03+0.72 = 0.75 $$
> 
> Step 3 — Bayes' theorem for part (iii).
> 
> $$ P(H\mid M) = \frac{P(H\cap M)}{P(M)} = \frac{0.03}{0.75} = 0.04 $$
> 
> Answer: (i) $\boxed{0.25}$, (ii) $\boxed{0.75}$, (iii) $\boxed{0.04}$

---

## 2. ISRO 2016 — Private Car / Bus / Metro

> [!example] ISRO 2016 Question: Choice between private car ($P=0.45$) and public transport. Within public transport, bus probability is $0.55$ (metro is the remainder). Find probabilities of car, bus, and metro respectively. (a) 0.45, 0.30, 0.25 — (b) 0.45, 0.25, 0.30 — (c) 0.45, 0.55, 0 — (d) 0.45, 0.35, 0.20
> 
> Approach: Step 1 — $P(\text{public transport}) = 1-0.45 = 0.55$. Step 2 — Multiply along the tree: bus $= 0.55\times0.55$, metro $= 0.55\times0.45$.
> 
> $$ P(\text{bus}) = 0.55 \times 0.55 = 0.3025 \approx 0.30, \qquad P(\text{metro}) = 0.55\times0.45 = 0.2475 \approx 0.25 $$
> 
> Answer: $\boxed{\text{(a) } 0.45,\ 0.30,\ 0.25}$

---

## 3. GATE CSE 2008 — Aishwarya's Study Habit (2-State Markov Chain)

> [!example] GATE CSE 2008 Question: If Aishwarya studies CS on a day, $P(\text{studies Math next day}) = 0.6$. If she studies Math, $P(\text{studies CS next day}) = 0.4$. Given she studies CS on Monday, find $P(\text{studies CS on Wednesday})$. A. 0.24 — B. 0.36 — C. 0.4 — D. 0.6
> 
> Approach: Step 1 — Monday = CS (given). Tuesday: $P(M)=0.6$, $P(CS)=0.4$. Step 2 — Branch 1 (Tue=M, prob $0.6$): Wed=CS with prob $0.4$ → contributes $0.6\times0.4=0.24$. Step 3 — Branch 2 (Tue=CS, prob $0.4$): Wed=CS with prob $0.4$ → contributes $0.4\times0.4=0.16$.
> 
> $$ P(\text{Wed}=CS) = 0.24 + 0.16 = 0.4 $$
> 
> Answer: $\boxed{\text{(C) } 0.4}$

---

## 4. GATE CSE 2021 — Signal Transmission (H/L)

> [!example] GATE CSE 2021 Question: Sender transmits $H$ with probability $0.1$, $L$ with probability $0.9$. Channel: $P(H_R|H_S)=0.3$, $P(L_R|H_S)=0.7$, $P(H_R|L_S)=0.8$, $P(L_R|L_S)=0.2$. If the received signal is $H$, find $P(\text{transmitted was } H)$.
> 
> Approach: Apply Bayes' theorem directly.
> 
> $$ P(H_S\mid H_R) = \frac{P(H_S)P(H_R|H_S)}{P(H_S)P(H_R|H_S)+P(L_S)P(H_R|L_S)} = \frac{0.1\times0.3}{0.1\times0.3 + 0.9\times0.8} = \frac{0.03}{0.75} = 0.04 $$
> 
> Answer: $\boxed{0.04}$

---

## 5. GATE IT 2006 — Rain and Temperature

> [!example] GATE IT 2006 Question: $P(\text{rain}) = 0.6$. Given noon temperature $\leq 25^{\circ}C$, $P(\text{rain}) = 0.4$. Temperature is equally likely to be $>25^\circ C$ or $\leq 25^\circ C$. Find $P(\text{rain} \mid >25^\circ C)$. A. 0.4 — B. 0.6 — C. 0.8 — D. 0.9
> 
> Approach: Step 1 — Let $x = P(\text{rain}\mid >25^\circ C)$. Step 2 — Total probability, partitioning by temperature:
> 
> $$ P(\text{rain}) = P(>25^\circ C)\cdot x + P(\leq 25^\circ C)\cdot P(\text{rain}\mid\leq25^\circ C) $$
> 
> $$ 0.6 = 0.5x + 0.5(0.4) \ \Rightarrow\ 0.6 - 0.2 = 0.5x \ \Rightarrow\ x = 0.8 $$
> 
> Answer: $\boxed{\text{(C) } 0.8}$

---

## 6. GATE CSE 2018 — Guwahati/Delhi Temperature

> [!example] GATE CSE 2018 Question: Given the conditional table below for $P(D\text{-temp} \mid G\text{-temp})$, and $P(H_G)=0.2,\ P(M_G)=0.5,\ P(L_G)=0.3$, find $P(H_G \mid H_D)$ (correct to 2 decimals).
> 
> ||$H_D$|$M_D$|$L_D$|
> |:--|:--|:--|:--|
> |$H_G$|0.40|0.48|0.12|
> |$M_G$|0.10|0.65|0.25|
> |$L_G$|0.01|0.50|0.49|
> 
> Approach: Step 1 — Total probability for $P(H_D)$.
> 
> $$ P(H_D) = 0.40(0.2) + 0.10(0.5) + 0.01(0.3) = 0.08+0.05+0.003 = 0.133 $$
> 
> Step 2 — Bayes' theorem.
> 
> $$ P(H_G\mid H_D) = \frac{P(H_G)P(H_D|H_G)}{P(H_D)} = \frac{0.08}{0.133} \approx 0.60 $$
> 
> Answer: $\boxed{0.60}$

---

## 7. GATE CSE 2017 — P and Q Applying for a Job

> [!example] GATE CSE 2017 Question: $P(P\text{ applies}) = 1/4$. $P(P\text{ applies}\mid Q\text{ applies}) = 1/2$. $P(Q\text{ applies}\mid P\text{ applies}) = 1/3$. Find $P(P^c \mid Q^c)$. A. 4/5 — B. 5/6 — C. 7/8 — D. 11/12
> 
> Approach: Step 1 — Get $P(P\cap Q)$ via the multiplication rule using the _easier_ direction:
> 
> $$ P(P\cap Q) = P(Q\mid P)\cdot P(P) = \frac{1}{3}\cdot\frac{1}{4} = \frac{1}{12} $$
> 
> Step 2 — Recover $P(Q)$ using the _other_ conditional:
> 
> $$ P(P\mid Q) = \frac{P(P\cap Q)}{P(Q)} \ \Rightarrow\ \frac{1}{2} = \frac{1/12}{P(Q)} \ \Rightarrow\ P(Q) = \frac{1}{6} $$
> 
> Step 3 — Inclusion-Exclusion for the union, then De Morgan for the complement.
> 
> $$ \begin{aligned} P(P\cup Q) &= P(P)+P(Q)-P(P\cap Q) = \frac{1}{4}+\frac{1}{6}-\frac{1}{12} = \frac{3+2-1}{12}=\frac{4}{12}=\frac{1}{3} \ P(P^c\cap Q^c) &= 1-P(P\cup Q) = \frac{2}{3} \ P(Q^c) &= 1-\frac{1}{6} = \frac{5}{6} \end{aligned} $$
> 
> Step 4 — Final conditional probability.
> 
> $$ P(P^c\mid Q^c) = \frac{P(P^c\cap Q^c)}{P(Q^c)} = \frac{2/3}{5/6} = \frac{2}{3}\times\frac{6}{5} = \frac{4}{5} $$
> 
> Answer: $\boxed{\text{(A) } 4/5}$

---

## 8. GATE CSE 2009 — Unbalanced Dice

> [!example] GATE CSE 2009 Question: An unbalanced die has $P(\text{odd face}) = 0.9 \times P(\text{even face})$ (totals). Every even face has equal individual probability $e$. Given $P(\text{even}\mid \text{face}>3) = 0.75$, find $P(\text{face}>3)$. A. 0.453 — B. 0.468 — C. 0.485 — D. 0.492
> 
> Approach: Step 1 — Total even probability $=3e$; total odd probability $=0.9(3e)=2.7e$. Normalization:
> 
> $$ 3e+2.7e = 1 \ \Rightarrow\ e = \frac{1}{5.7} $$
> 
> Step 2 — Faces $>3$ are ${4,5,6}$: two even ($4,6$, each $=e$) and one odd ($5$, unknown probability $P(5)$).
> 
> $$ P(\text{even}\mid\text{face}>3) = \frac{2e}{2e+P(5)} = 0.75 \ \Rightarrow\ 2e = 1.5e + 0.75P(5) \ \Rightarrow\ P(5)=\frac{2}{3}e $$
> 
> Step 3 — Combine.
> 
> $$ P(\text{face}>3) = 2e + \frac{2}{3}e = \frac{8}{3}e = \frac{8}{3}\times\frac{1}{5.7} \approx 0.468 $$
> 
> Answer: $\boxed{\text{(B) } 0.468}$

---

## 9. GATE CSE 2016 — LED Bulb Lifetime

> [!example] GATE CSE 2016 Question: Equal number of two LED bulb types. $P(>100\text{h}\mid\text{Type 1}) = 0.7$, $P(>100\text{h}\mid\text{Type 2}) = 0.4$. Find $P(>100\text{h})$ for a randomly chosen bulb.
> 
> Approach: Equal proportions means $P(\text{Type 1})=P(\text{Type 2})=0.5$. Apply Total Probability.
> 
> $$ P(>100\text{h}) = 0.5(0.7) + 0.5(0.4) = 0.35+0.2 = 0.55 $$
> 
> Answer: $\boxed{0.55}$

---

## Related Notes

- [[Total Probability Theorem & Bayes' Theorem]]
- [[Multiplication Rule, Tree Diagrams & Sequential Models]]
- [[Conditional Probability]]

## Open Questions

- [ ] GATE CSE 2018 (Guwahati/Delhi) answer $0.60$ was derived independently (not present in the raw lecture scan) — worth cross-checking against GateOverflow before trusting fully during revision.
- [ ] GATE CSE 2009 (unbalanced dice) assumed the odd-face probabilities are _not_ individually equal (only even faces are stated as equal) — this assumption drove the derivation; re-verify against the official solution if accuracy matters for marks.