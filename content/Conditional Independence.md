# Conditional Independence vs Independence

**Topic:** GATE CSE > Probability & Statistics > Independence **Source:** GO Classes — Probability Lecture (Slides 62–83) **Tags:** #probability #independence #conditional-independence #gate-cse **Links:** [[Probability MOC]] | [[Independent Events]] | [[Conditional Probability]]

---

> [!info] Overview This note covers the relationship between independence and conditional independence of events. The central result: neither concept implies the other. Two events can be independent but not conditionally independent given some event $C$, and two events can be conditionally independent given $C$ but not unconditionally independent. The note works through the formal definitions, three worked counterexamples, and a set of practice questions on decomposing joint/conditional probability expressions.

---

## 1. Core Definitions

### 1.1 Intuitive Foundation

Independence of two events means that the occurrence or non-occurrence of one event has no effect on the probability of the other. This is captured by:

$$ P(A \mid B) = P(A \mid B^c) $$

Combined with the definition of conditional probability,

$$ P(A \mid B) = \dfrac{P(A \cap B)}{P(B)} $$

this leads to the standard product-form condition for independence, derived in Section 1.2.

**Extension to conditional independence.** The same criterion extends naturally when a conditioning event $C$ is present. Suppose $C$ is the conditioner. Then $A$ and $B$ are independent given $C$ when

$$ P(A \mid B, C) = P(A \mid B^c, C) $$

That is, once the sample space is already restricted to $C$, further conditioning on $B$ or on $B^c$ within that restricted space does not change the probability of $A$.

### 1.2 Independence (Formal Definition)

Two events $A$ and $B$ are independent if

$$ P(A \cap B) = P(A)P(B) $$

If additionally $P(B) > 0$, this is equivalent to

$$ P(A \mid B) = P(A) $$

If $A$ and $B$ are independent, then so are the following pairs:

- $A$ and $B^c$
- $A^c$ and $B$
- $A^c$ and $B^c$

### 1.3 Conditional Independence (Formal Definition)

Two events $A$ and $B$ are conditionally independent given an event $C$ (with $P(C) > 0$) if

$$ P(A \cap B \mid C) = P(A \mid C),P(B \mid C) $$

If additionally $P(B \cap C) > 0$, this is equivalent to

$$ P(A \mid B \cap C) = P(A \mid C) $$

If $A$ and $B$ are conditionally independent given $C$, then the same relationship holds for the complements, conditioned on $C$:

- $A$ and $B^c$ are independent given $C$
- $A^c$ and $B$ are independent given $C$
- $A^c$ and $B^c$ are independent given $C$

> [!warning] Key Result Independence and conditional independence are logically unrelated conditions. Neither one implies the other:
> 
> $$ P(A \cap B) = P(A)P(B) \quad \not\Leftrightarrow \quad P(A \cap B \mid C) = P(A \mid C)P(B \mid C) $$

This means four distinct cases are possible for a given pair $A, B$ and a conditioning event $C$: (1) independent and conditionally independent, (2) independent but not conditionally independent, (3) not independent but conditionally independent, (4) neither.

---

## 2. Intutive Example: Conditional Independence Does Not Imply Independence

### 2.1 Alice and Bob Phone Call Example

Suppose Alice and Bob are the only two people who ever call. Each day they decide independently whether to call. Let:

- $A$ = event that Alice calls
- $B$ = event that Bob calls

Since the decisions are made independently by each person, $A$ and $B$ are unconditionally independent.

Now suppose the phone is heard ringing. Let $R$ be the event that the phone is ringing. Conditional on $R$, $A$ and $B$ are **no longer independent**: if the call is not from Alice, it must be from Bob (since only these two people ever call). Formally,

$$ P(B \mid R) < 1 = P(B \mid A^c, R) $$

This shows $B$ and $A^c$ are not conditionally independent given $R$, and by symmetry the same holds for $A$ and $B$.

> [!note] Intuition 
> Knowing that the phone is ringing creates a dependency between "Alice called" and "Bob called" through a process of elimination — this is sometimes called "explaining away." Unconditionally the two events are independent, but conditioning on the shared consequence (the ring) links them.

### 2.2 Example: Kevin's Number to Alice and Bob

Kevin phones Alice and Bob separately and tells each of them the same number $n_k \in {1, \dots, 10}$. Due to noise on the phone line, Alice and Bob each independently and imperfectly hear a number. Let $n_a$ and $n_b$ be the numbers Alice and Bob believe they heard.

**Are $n_a$ and $n_b$ marginally independent?**

No. Intuitively, $P(n_a = 1 \mid n_b = 1) > P(n_a = 1)$, since both being told the same value biases their heard values toward agreement.

**Why are $n_a$ and $n_b$ conditionally independent given $n_k$?**

Once the true value $n_k$ is known, the noise processes corrupting Alice's and Bob's hearing are independent of each other, so knowing $n_b$ gives no additional information about $n_a$ beyond what $n_k$ already gives:

$$ P(n_a = 1 \mid n_b = 1,, n_k = 2) = P(n_a = 1 \mid n_k = 2) $$

---

## 3. Example: Independence Does Not Imply Conditional Independence

### 3.1 Die Roll Setup

Roll a fair six-sided die. Define:

$$ A = {1, 2}, \qquad B = {2, 4, 6}, \qquad C = {1, 4} $$

### 3.2 Checking Unconditional Independence

$$ P(A) = \dfrac{2}{6} = \dfrac{1}{3}, \qquad P(B) = \dfrac{3}{6} = \dfrac{1}{2} $$

$$ P(A \cap B) = P({2}) = \dfrac{1}{6} $$

$$ P(A)P(B) = \dfrac{1}{3} \times \dfrac{1}{2} = \dfrac{1}{6} = P(A \cap B) $$

Since $P(A \cap B) = P(A)P(B)$, $A$ and $B$ are independent.

### 3.3 Checking Conditional Independence Given C

$$ P(A \mid C) = \dfrac{P(A \cap C)}{P(C)} = \dfrac{P({1})}{P({1,4})} = \dfrac{1/6}{2/6} = \dfrac{1}{2} $$

$$ P(B \mid C) = \dfrac{P(B \cap C)}{P(C)} = \dfrac{P({4})}{P({1,4})} = \dfrac{1/6}{2/6} = \dfrac{1}{2} $$

$$ P(A \cap B \mid C) = \dfrac{P(A \cap B \cap C)}{P(C)} = \dfrac{P({2} \cap {1,4})}{P(C)} = \dfrac{P(\varnothing)}{P(C)} = 0 $$

Since

$$ P(A \cap B \mid C) = 0 \neq \dfrac{1}{2} \times \dfrac{1}{2} = P(A \mid C)P(B \mid C) $$

$A$ and $B$ are **not** conditionally independent given $C$, even though they are unconditionally independent.

> [!note] Why This Happens
>  $A \cap B = {2}$ and $C = {1,4}$ are disjoint, so conditioning on $C$ makes the joint event $A \cap B$ impossible ($P(A \cap B \mid C) = 0$), while $A$ and $B$ individually still have positive probability given $C$. This structural clash between the sets destroys the independence relationship once conditioning is introduced.

---

## 5. Summary Table

| Two events A and B are independent — | Two events A and B are independent given C —  |
| :----------------------------------- | :-------------------------------------------- |
| $P(A \cap B) = P(A)P(B)$             | $P(A \cap B \mid C) = P(A \mid C)P(B \mid C)$ |
| or $P(A \mid B) = P(A)$              | or $P(A \mid B, C) = P(A \mid C)$             |
| or $P(B \mid A) = P(B)$              | or $P(B \mid A, C) = P(B \mid C)$             |
| **If A and B are independent then:** | **If A and B are independent given C then:**  |
| $A$ and $B^c$ are independent        | $A$ and $B^c$ are independent given $C$       |
| $A^c$ and $B$ are independent        | $A^c$ and $B$ are independent given $C$       |
| $A^c$ and $B^c$ are independent      | $A^c$ and $B^c$ are independent given $C$     |

---

## 6. Practice Questions

### 6.1 True/False: Factorization Implies Conditional Independence

> [!example] GO Classes Practice Question **Question:** Given the factorization $P(A, B, C) = P(C),P(A \mid C),P(B \mid C)$, can we say $A$ and $B$ are independent given $C$?
> 
> **Approach:** Step 1 — Write the general (always-true) chain-rule factorization for comparison:
> 
> $$ P(B, A, C) = P(C) \cdot P(A \mid C) \cdot P(B \mid A, C) $$
> 
> Step 2 — Compare this general form to the given factorization. The given form replaces $P(B \mid A, C)$ with $P(B \mid C)$, which is exactly the definition of $A \perp B \mid C$.
> 
> **Answer:** $\boxed{\text{True}}$ — the factorization directly matches the conditional independence definition.

### 6.2 Consequences of Conditional Independence

> [!example] GO Classes Practice Question **Question:** Suppose $A$ and $B$ are conditionally independent given $C$ (i.e., $A \perp B \mid C$). Which of the following are true?
> 
> a) $P(A \cap B) = P(A)P(B)$ b) $P(A, B, C) = P(A \mid B, C),P(B \mid C),P(C)$ c) $P(A, B, C) = P(A \mid C),P(B \mid C),P(C)$ d) $P(A, B \mid C) = P(A \mid C),P(B \mid C)$
> 
> **Approach:** Step 1 — (a) is false in general. Conditional independence given $C$ says nothing about unconditional independence (see Section 4).
> 
> Step 2 — (b) is always true regardless of independence; it is just the standard chain rule $P(A,B,C) = P(C) \cdot P(A,B \mid C)$.
> 
> Step 3 — (c) follows directly by substituting the definition $P(A,B\mid C) = P(A\mid C)P(B\mid C)$ into $P(A,B,C) = P(C),P(A,B\mid C)$.
> 
> Step 4 — (d) is simply the definition of $A \perp B \mid C$, hence true.
> 
> **Answer:** $\boxed{\text{b, c, d are true; a is false}}$

### 6.3 Expressions Equal to P(A | B)

> [!example] GO Classes Practice Question **Question:** Mark all expressions equal to $P(A \mid B)$, given no independence assumptions:
> 
> $\square\ P(A, C \mid B) + P(A, C^c \mid B)$ $\square\ \dfrac{P(B \mid A),P(A \mid C)}{P(B, C) + P(B, C^c)}$ $\square\ \dfrac{P(A, C \mid B)}{P(C \mid B)}$ $\square\ \dfrac{P(A \mid C, B),P(C \mid A, B)}{P(C \mid B)}$ $\square\ P(A \mid B, C) + P(A \mid B, C^c)$ $\square\ \dfrac{P(A, B, C) + P(A, B, C^c)}{P(B, C) + P(B, C^c)}$ $\square\ \text{None of the options provided}$
> 
> **Approach:** Step 1 — Option 1: By the law of total probability conditioned on $B$, splitting over $C$ and $C^c$:
> 
> $$ P(A, C \mid B) + P(A, C^c \mid B) = P(A \mid B) $$
> 
> This is **true**.
> 
> Step 2 — Option 2: The denominator $P(B,C) + P(B,C^c) = P(B)$, but the numerator $P(B\mid A)P(A\mid C)$ does not simplify to $P(A,B)$ in general. **False**.
> 
> Step 3 — Option 3: $\dfrac{P(A,C\mid B)}{P(C\mid B)} = \dfrac{P(A,B,C)/P(B)}{P(C,B)/P(B)} = \dfrac{P(A,B,C)}{P(C,B)}$, which is $P(A \mid B, C)$, not $P(A \mid B)$ in general. **False**.
> 
> Step 4 — Option 4: Simplify numerator and denominator:
> 
> $$ \frac{P(A \mid C,B),P(C \mid A,B)}{P(C \mid B)} = \frac{\dfrac{P(A,B,C)}{P(B,C)} \cdot \dfrac{P(A,B,C)}{P(A,B)}}{\dfrac{P(C,B)}{P(B)}} $$
> 
> This does not reduce to $P(A,B)/P(B)$ in general. **False**.
> 
> Step 5 — Option 5: $P(A \mid B,C) + P(A \mid B,C^c)$ is not a valid decomposition (missing weighting by $P(C\mid B)$ and $P(C^c \mid B)$), so it does **not** equal $P(A\mid B)$ in general. **False**.
> 
> Step 6 — Option 6: Numerator $= P(A,B,C) + P(A,B,C^c) = P(A,B)$ by total probability. Denominator $= P(B,C) + P(B,C^c) = P(B)$. So this equals $\dfrac{P(A,B)}{P(B)} = P(A\mid B)$. **True**.
> 
> **Answer:** $\boxed{\text{Options 1 and 6 only}}$

### 6.4 Expressions Equal to P(A, B, C) Given A ⊥ B

> [!example] GO Classes Practice Question **Question:** Mark all expressions equal to $P(A, B, C)$, given that $A \perp B$ (unconditionally independent):
> 
> $\square\ P(A),P(B),P(C \mid A, B)$ $\square\ P(A),P(C \mid A),P(B \mid C)$ $\square\ P(C),P(A \mid C),P(B \mid C)$ $\square\ P(A, C),P(B \mid A, C)$ $\square\ P(A),P(B \mid A),P(C \mid A, B)$ $\square\ \text{None of the provided options}$ $\square\ P(A \mid C),P(C \mid B),P(B)$
> 
> **Approach:** Step 1 — The general chain-rule expansion (always true, no assumptions needed) is:
> 
> $$ P(A, B, C) = P(A, C) \cdot P(B \mid A, C) $$
> 
> Step 2 — Option 1: Since $A \perp B$, $P(B \mid A) = P(B)$, so $P(A)P(B)P(C\mid A,B) = P(A)P(B\mid A)P(C\mid A,B)$, which matches the general chain rule form. **True**.
> 
> Step 3 — Option 2: $P(A)P(C\mid A)P(B\mid C)$ does not correspond to a valid chain-rule decomposition of $P(A,B,C)$; it implicitly assumes $A \perp B \mid C$, which is not given. **False**.
> 
> Step 4 — Option 3: $P(C)P(A\mid C)P(B\mid C)$ requires $P(B \mid A, C) = P(B \mid C)$, i.e., conditional independence given $C$, which is not implied by $A \perp B$ (see Section 3). **False**.
> 
> Step 5 — Option 4: $P(A,C)P(B\mid A,C)$ is exactly the general chain-rule identity from Step 1. **True**.
> 
> Step 6 — Option 5: $P(A)P(B\mid A)P(C\mid A,B)$ is the standard chain rule $P(A)P(B\mid A)P(C\mid A,B) = P(A,B,C)$, always true. **True**.
> 
> Step 7 — Option 7: $P(A\mid C)P(C\mid B)P(B)$ does not correspond to any valid decomposition of $P(A,B,C)$ under the given assumption. **False**.
> 
> **Answer:** $\boxed{\text{Options 1, 4, and 5 only}}$

### 6.5 Expressions Equal to P(A, B | C) Given A ⊥ B | C

> [!example] GO Classes Practice Question **Question:** Mark all expressions equal to $P(A, B \mid C)$, given that $A \perp B \mid C$:
> 
> $\square\ P(A \mid C),P(B \mid C)$ $\square\ \dfrac{P(C, A \mid B),P(B)}{P(C)}$ $\square\ \dfrac{P(C),P(B \mid C),P(A \mid C)}{P(C \mid A, B)}$ $\square\ P(A \mid B),P(B \mid C)$
> 
> **Approach:** Step 1 — Option 1 is exactly the definition of $A \perp B \mid C$, so it is **true**.
> 
> Step 2 — Option 2: Simplify using $P(C,A\mid B) = P(A,B,C)/P(B)$:
> 
> $$ \frac{P(C,A\mid B),P(B)}{P(C)} = \frac{\dfrac{P(A,B,C)}{P(B)} \cdot P(B)}{P(C)} = \frac{P(A,B,C)}{P(C)} = P(A,B\mid C) $$
> 
> This is **true**.
> 
> Step 3 — Option 3: Simplify numerator and denominator step by step:
> 
> $$ \begin{aligned} \frac{P(C),P(B\mid C),P(A\mid C)}{P(C\mid A,B)} &= \frac{P(C) \cdot \dfrac{P(B,C)}{P(C)} \cdot \dfrac{P(A,C)}{P(C)}}{\dfrac{P(C,A,B)}{P(A,B)}} \[6pt] &= \frac{P(B,C),P(A,C),P(A,B)}{P(C),P(A,B,C)} \end{aligned} $$
> 
> This simplifies to $P(A,B)$, not $P(A,B\mid C)$, in general. **False**.
> 
> Step 4 — Option 4: $P(A\mid B)P(B\mid C)$ has no valid derivation matching $P(A,B\mid C)$ under the given assumption. **False**.
> 
> **Answer:** $\boxed{\text{Options 1 and 2 only}}$

---

## Related Notes

- [[Independent Events]]
- [[Conditional Probability]]
- [[Bayes' Theorem]]
- [[Chain Rule of Probability]]

## Open Questions

- [ ] Verify the exact point distribution in Section 4's Venn diagram — the source description of "8 named regions summing to 11" was slightly ambiguous in how the 6th point within $C$ was allocated; re-derive from the diagram image if available.
- [ ] Confirm whether GATE has historically tested this exact "conditional independence ⇏ independence" concept directly, or only through Bayesian network conditional independence (D-separation) questions.
- [ ] Practice constructing an original example (own choice of $A, B, C$) exhibiting both directions of non-implication, to test true understanding rather than memorized examples.