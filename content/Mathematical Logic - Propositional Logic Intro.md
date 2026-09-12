# Mathematical Logic & Propositional Logic — Introduction

**Topic:** GATE CS > Discrete Mathematics > Mathematical Logic **Source:** GO Classes — Discrete Mathematics (Deepak Poonia, IISc Bangalore), Lecture 1 (Mathematical Logic — intro) & Lecture 2 (Propositional Logic — intro) **Tags:** #gate-cs #discrete-math #mathematical-logic #propositional-logic **Links:** [[Discrete Mathematics MOC]] | [[Propositional Logic - Atomic and Compound Propositions]]

---

> [!info] Overview 
> This note covers _why_ mathematical logic exists at all (natural language is ambiguous, logic isn't), where propositional logic sits inside the broader family of logics, and the first building blocks of propositional logic: what a proposition is, what it isn't, and how propositional variables and truth values work. This is pure foundation — no connectives (∧, ∨, →) yet, that's the next note.

---

## 1. Why Do We Need Mathematical Logic?

### 1.1 Three Roles of Mathematical Logic

The lecture frames mathematical logic as serving three audiences at once:

- **Language for Mathematics** — gives precise, unambiguous meaning to mathematical statements and theorems.
- **Language for Mathematicians** — a shared, rigorous notation everyone agrees on.
- **Language for Computers / AI / Automated Reasoning** — machines can't tolerate ambiguity the way humans can, so they need a formal system.

The unifying idea: logic exists to remove ambiguity that natural languages (like English) carry by default.

### 1.2 Natural Language Is Ambiguous

This is the core motivating problem of the whole chapter. A few worked examples show the same surface structure ("X or Y") hiding very different intended meanings.

**Example 1 — Integers:**

> Let $a, b$ be two integers. If $a \cdot b$ is even, then "$a$ is even" **or** "$b$ is even".

Here, if $p$ = "$a$ is even" and $q$ = "$b$ is even", the statement is true whether $p$ alone holds, $q$ alone holds, or **both** hold simultaneously. So "or" here clearly means the _inclusive_ or ($p \lor q$).

**Example 2 — Missile command:**

> Attack city A **or** city B.

Structurally identical to Example 1 — same "P or Q" shape. But here, if both $P$ and $Q$ happen to be interpreted as true (attack both cities), it's a **disaster** — that is not what the command meant. The intended meaning is the _exclusive_ or: attack exactly one, not both ($M \oplus N$).

> [!warning] Same English Words, Different Logic Both sentences use the word "or", and both have the exact same grammatical structure. Yet one needs **inclusive OR** ($\lor$) and the other needs **exclusive OR** ($\oplus$). English alone cannot tell you which one is meant — you have to guess from context. This is precisely the ambiguity mathematical logic is built to eliminate.

**Example 3 — Causation vs. independence:**

> "The sun is shining and I feel happy."

At first glance this seems to mean the sun _causes_ the happiness. But compare it to:

> "Cats are furry and elephants are heavy."

Both sentences have the **exact same grammatical structure** ("X and Y"), yet nobody reads the second one as claiming elephants are heavy _because_ cats are furry — the two facts are obviously unrelated. So "and" in English can silently imply causation in one context and pure independent conjunction in another, with no grammatical signal to tell them apart.

**How logic resolves this:**

|English sentence|Natural reading (ambiguous)|Logical variable|Logical formula (unambiguous)|
|:--|:--|:--|:--|
|"$a$ is even OR $b$ is even"|Could be inclusive or exclusive|$p$ = "a is even", $q$ = "b is even"|$p \lor q$ (inclusive OR)|
|"Attack city A OR city B"|Could be inclusive or exclusive|$M$ = attack A, $N$ = attack B|$M \oplus N$ (exclusive OR)|
|"The sun is shining and I feel happy"|Might imply causation|$A$ = sun shining, $B$ = I feel happy|$A \land B$ (plain conjunction, no causal claim)|
|"Cats are furry and elephants are heavy"|No causation implied|$C$ = cats furry, $D$ = elephants heavy|$C \land D$|

> [!note] Key Idea The moment you translate an English sentence into propositional variables and connectives, the ambiguity disappears. $p \lor q$ always means "at least one of $p, q$ is true" — full stop, no room for reinterpretation. That precision is the entire point of the formal system.

---

## 2. Logic as the Basis of Reasoning

### 2.1 Valid vs. Invalid Arguments

Two arguments are contrasted to show that "logical-sounding" language can still produce wrong conclusions if the underlying structure is invalid.

**Argument 1 (valid):**

> All men are mortal. Socrates is a man. Hence, Socrates is mortal.

This is a textbook valid syllogism — the conclusion follows necessarily from the premises.

**Argument 2 (invalid):**

> All cats like fish. Silvy isn't a cat. Hence, Silvy doesn't like fish.

This _looks_ similarly structured to Argument 1, but it is **invalid**. "All cats like fish" only tells you about cats — it says nothing about what non-cats do or don't like. Silvy not being a cat gives you zero information about whether Silvy likes fish. The relationship is really "Cat $\to$ likes fish", and knowing $\lnot \text{Cat}$ does not let you conclude $\lnot(\text{likes fish})$ (denying the antecedent is a classical logical fallacy).

|Argument|Structure|Valid?|
|:--|:--|:--|
|All men are mortal; Socrates is a man; ∴ Socrates is mortal|Universal → instance → conclusion follows|✅ Valid|
|All cats like fish; Silvy isn't a cat; ∴ Silvy doesn't like fish|Denies the antecedent of "Cat → likes fish"|❌ Invalid|

> [!note] Key Idea Logic isn't just about translating sentences — it's also the machinery that lets you check whether a conclusion _actually_ follows from given premises, independent of whether the premises or conclusion happen to be true in the real world.

### 2.2 Automated Reasoning and AI

The lecture connects this directly to computing: feed two inputs (premises) into an "automated reasoning" system (the slides sketch this as a box — conceptually, something like an automated reasoning engine, with a nod to tools like ChatGPT as an example of "automated software" built on these foundations) and the system should output whether the argument is **valid or invalid**. This is presented as the reason CS people specifically care about mathematical logic — it's described as "Chapter 1" of essentially every formal AI textbook, because all automated reasoning is built on top of it.

**Why Mathematical Logic Matters (as stated in the lecture):**

- The rules of logic specify the precise meaning of mathematical statements.
- Logic is the basis of **all** mathematical reasoning and **all** automated reasoning.

---

## 3. The Landscape of Logics

When people casually say "logic", they usually mean one of two things: **propositional logic** or **first-order predicate logic**. But the lecture is careful to note that the _formal_ definition of "a logic" is much broader — hundreds of distinct logics have been studied across philosophy, computer science, and mathematics.

|Type of logic|In GATE syllabus?|
|:--|:--|
|Propositional logic|✅ Yes|
|First-order logic|✅ Yes|
|Second-order logic|❌ No|
|Fuzzy logic, and hundreds of others|❌ No|

For GATE CSE purposes, the scope is exactly propositional logic + first-order logic — everything else mentioned is just to show the discipline is much bigger than the syllabus slice.

---

## 4. Propositional Logic: The Basics

### 4.1 Propositional Logic Is a "World of True/False"

The lecture draws a deliberate contrast with ordinary mathematics to set expectations:

- In ordinary math, an **integer variable** $x$ can take infinitely many values: $-3, 0, 3, 3000, \dots$
- Similarly, a **real variable** $y$ can be $\pi, 2.3, 0, \dots$
- In **propositional logic**, a variable $p$ can only ever be **True** or **False** — nothing else. Same for $q$, $r$, and so on.

This is emphasized as a genuinely "very simple world" compared to the rest of mathematics — the entire universe of values for a propositional variable has exactly two elements.

$$ p \to T \text{ or } F, \qquad q \to T \text{ or } F $$

A propositional variable is also called a **Boolean variable**.

### 4.2 What Is a Proposition?

> [!note] Definition 
> A **proposition** (or **statement**) is a declarative sentence — a sentence that asserts a fact — that is **either true or false**, and it **must be exactly one of the two, never both**.

Equivalently: a proposition is a declarative sentence to which it is _possible_ to assign a truth value (true or false).

### 4.3 Examples of Propositions

All of the following are propositions **because** each one can be assigned a definite truth value (even if we're not 100% sure which one, or if it's clearly false) — the requirement is just that it _has_ a truth value, not that the truth value is known or that it's true.

| Sentence                                        | Proposition?                                                              | Truth value                                                 |
| :---------------------------------------------- | :------------------------------------------------------------------------ | :---------------------------------------------------------- |
| "Jaipur is the capital of India."               | ✅ Yes                                                                     | False (it's a proposition regardless — happens to be false) |
| "All cows are brown."                           | ✅ Yes                                                                     | False                                                       |
| "The Earth is further from the sun than Venus." | ✅ Yes                                                                     | True                                                        |
| "$2 \times 2 = 5$."                             | ✅ Yes                                                                     | False                                                       |
| "There are 1000 stones on Mars."                | ✅ Yes                                                                     | Unknown to us, but it's still definitely T or F             |
| "In the 7th century, 90000 people were born."   | ✅ Yes                                                                     | Unknown to us, but still T or F                             |
| "Puppies are cuter than kittens."               | ✅ Yes (treated as a proposition in the lecture, despite being subjective) | T or F                                                      |
| "Usain Bolt can outrun everyone in this room."  | ✅ Yes                                                                     | T or F                                                      |
| "This is the last entry on this list."          | ✅ Yes                                                                     | T or F                                                      |

> [!tip] The Key Test 
> You don't need to _know_ whether a sentence is true to call it a proposition. "There are 1000 stones on Mars" is a perfectly good proposition even though nobody in the room can currently verify it — what matters is that it is **the kind of sentence** that has a definite, singular truth value.

### 4.4 Things That Are NOT Propositions

The lecture identifies four categories of sentences that fail to qualify as propositions:

| Category                                   | Example                                                                | Why it fails                                                                                     |
| :----------------------------------------- | :--------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| Questions                                  | "How far is it to the next town?" / "Do you want to go to the movies?" | Questions don't assert anything — they can't be assigned true/false.                             |
| Commands / imperative sentences            | "Look out!" / "Clean up your room."                                    | Imperatives aren't declarative — they issue an instruction, not a factual claim.                 |
| Sentences with free (unassigned) variables | "$x + 2 = 2x$" / "$2x = 2 + x$"                                        | Until $x$ is given a specific value, the sentence is neither true nor false — it depends on $x$. |
| Paradoxes                                  | "This sentence is false."                                              | Leads to a logical contradiction no matter which truth value you try to assign (see §4.5).       |

### 4.5 Free Variables: When a Variable Blocks a Proposition

Two similar-looking statements are contrasted to sharpen the "free variable" idea:

- **$4n = 2 + 3n$** — Here $n$ is a **free variable**: its value isn't fixed or bound by anything (like "for all" or "there exists"), so the sentence's truth depends entirely on which integer you plug in for $n$. **Not a proposition.**
- **"For all integers $n$, $2n$ is an even number."** — Here $n$ is **not free** — it is bound by the quantifier "for all". The sentence as a whole is a single, complete claim that is either true or false (and in this case, it's true). **This IS a proposition.**

> [!note] Key Idea
>  A **quantifier** ("for all", "there exists") _binds_ a variable and turns an otherwise-ambiguous open sentence into a single fixed statement. This is the bridge concept that leads into first-order logic later in the course.

### 4.6 The Paradox Case: "This Sentence Is False"

Let $S$ = the sentence "$S$ is false." Walk through both possible truth assignments:

**Case 1 — Suppose $S$ is True:**

$$ S = \text{True} \implies \text{what } S \text{ asserts is true} \implies S \text{ is false} $$

So assuming $S$ is true forces $S$ to be false. Contradiction.

**Case 2 — Suppose $S$ is False:**

$$ S = \text{False} \implies \text{what } S \text{ asserts (that } S \text{ is false) is not true} \implies S \text{ is True} $$

So assuming $S$ is false forces $S$ to be true. Contradiction again.

$$ \begin{aligned} S = \text{True} &\implies S = \text{False} \ S = \text{False} &\implies S = \text{True} \end{aligned} $$

Since **both** possible truth values immediately flip to their opposite, $S$ can be neither consistently true nor consistently false. This is a genuine **paradox**, and by definition it is **not a proposition** — it violates the core requirement that a proposition be exactly one of true/false.

### 4.7 Summary: The Core Rule of Propositions

> [!note] Key Idea A proposition must be **True or False, but never both, and never neither.** If a sentence can be assigned no truth value (questions, commands) or an inconsistent one (paradoxes) or an undetermined one (free variables), it is **not** a proposition.

**Full list of "not a proposition" categories from the lecture:**

1. Questions
2. Imperative sentences / commands
3. Sentences with free variables
4. Paradoxes

Also stated as a logical identity in this framework:

$$ \lnot(\text{True}) \equiv \text{False}, \qquad \lnot(\text{False}) \equiv \text{True} $$

---

## 5. Propositional Variables and Truth Values (Notation)

### 5.1 Representing Propositions with Variables

Every proposition can be _represented_ by a single propositional variable, conventionally a lowercase letter: $p, q, r, s, \dots$. Each such variable can take on exactly one of two values: **true** or **false**.

**Worked mapping (from the "sun shining / happy / cats / elephants" examples):**

|English proposition|Propositional variable|
|:--|:--|
|"The sun is shining."|$A$ (or $p$)|
|"I feel happy."|$B$ (or $H$)|
|"Cats are furry."|$C$|
|"Elephants are heavy."|$D$ (or $R$)|

Another standalone example given: proposition $p$ = "Today is Friday."

### 5.2 Truth Value Notation

> [!note] Definition The **truth value** of a proposition is **True** (denoted $T$) if the proposition is true, and **False** (denoted $F$) if the proposition is false.

Standard notational equivalences used throughout the course:

$$ \text{True} \equiv T \equiv 1, \qquad \text{False} \equiv F \equiv 0 $$

So, for example, if a propositional variable $R$ represents a true proposition, we say "the truth value of $R$ is $T$." If a variable $S$ represents a false proposition, "the truth value of $S$ is $F$."

---

## PYQ / Practice Questions from the Lecture

> [!example] Lecture Example — GO Classes, Discrete Mathematics, Lec 2 **Question:** Which of the following is a proposition? (i) $4n = 2 + 3n$ (ii) For all integers $n$, $2n$ is an even number.
> 
> **Approach:** Step 1 — Check whether each sentence contains a free (unbound) variable. Step 2 — (i) has $n$ free — its truth depends on which integer you substitute, so it is not fixed to a single T/F value. Step 3 — (ii) has $n$ bound by the quantifier "for all" — the sentence as a whole makes one single, fixed claim.
> 
> $$ \text{(i): free variable } n \implies \text{not a proposition} $$ $$ \text{(ii): } n \text{ bound by } \forall \implies \text{single fixed truth value (True)} \implies \text{proposition} $$
> 
> **Answer:** Only (ii), "For all integers $n$, $2n$ is an even number," is a proposition — and it is **True**.

> [!example] Lecture Example — GO Classes, Discrete Mathematics, Lec 2 **Question:** Is the sentence "This sentence is false" a proposition?
> 
> **Approach:** Step 1 — Assume the sentence $S$ is True, and see what that forces. Step 2 — Assume $S$ is False, and see what that forces. Step 3 — If both assumptions lead to contradictions, the sentence cannot consistently be assigned any truth value.
> 
> $$ \begin{aligned} S = \text{True} &\implies S = \text{False} \quad (\text{contradiction}) \ S = \text{False} &\implies S = \text{True} \quad (\text{contradiction}) \end{aligned} $$
> 
> **Answer:** No — it is a **paradox**, not a proposition, since it cannot be assigned a single consistent truth value.

---

## Related Notes

- [[Propositional Logic - Atomic and Compound Propositions]] _(next lecture in sequence — not yet created)_
- [[Discrete Mathematics MOC]]
- [[First Order Logic]] _(link placeholder — create when covered)_

## Open Questions

- [ ] The lecture treats subjective statements like "Puppies are cuter than kittens" as propositions purely because they're grammatically declarative — worth revisiting whether GATE would ever test a genuinely ambiguous/subjective sentence as a trick "is this a proposition?" question.
- [ ] Need to confirm the exact formal definition of "free variable" vs "bound variable" once first-order logic / quantifiers are covered in depth — this note only previews the idea via the $4n = 2+3n$ example.
- [ ] Slide 26/28/30 diagrams (automated reasoning box, AI course chapter reference) were sketchy/handwritten in the source — captured here as descriptions only; if the original lecture video has more detail on the "automated reasoning system" diagram, worth adding.