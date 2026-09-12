#+TITLE: Logic Notes
#+AUTHOR: Study Notes
#+DATE: 2026-02-01

* Introduction to Logic

Logic is the study of argumentation. It studies informal/formal systems of arguing.

Formal logic consists of a formal language (alphabets, syntactic rules), axioms/premises and rules of inferences.
Formal logic studies argumentation in general and doesn't deal with particular things.

Mathematical logic is formal logic.

There are many formal logic systems based on the defining components.

* Aristotelian Logic

Aristotelian logic is logic of syllogism. A syllogism is argumentation consisting of two premises and making a conclusion.
The propositions consist of subject and copula and predicate. There is restriction on what the copula and predicate can be.

* Propositional Logic (Zero Order Logic)

** Basic Concepts

Zero order (propositional logic) consists of propositions and their combinations via logical connectives.
The propositions can be simple or compound (made from logically connecting simple propositions).
Here the simple propositions are the basic units and we don't deal with internals of a proposition.
A simple proposition is treated as a whole and has a truth value of true or false.

Reference: https://en.wikipedia.org/wiki/Atomic_sentence

Example of atomic propositions: "I am a human."
Not an atomic proposition: "I like mars and you like earth."

** Logical Truths and Tautologies

Some sentences and propositions are true because of their structure and not because of their composing units.
These are called logical truths or tautologies.

** Definition

Propositional logic comprises formal systems in which formulae are built from atomic propositions using logical connectives.
For instance, propositional logic represents the conjunction of two atomic propositions P and Q as the complex formula P ∧ Q.

Unlike predicate logic where terms and predicates are the smallest units, propositional logic takes full propositions with truth values as its most basic component.

Thus, propositional logics can only represent logical relationships that arise from the way complex propositions are built from simpler ones. But it cannot represent inferences that result from the inner structure of a proposition.

** Truth Tables

Truth table, say for p → q tells us the truthfulness of the p → q for different possibilities of truthfulness of its components.

** Biconditional (Material Equivalence)

*** Definition

Biconditional, iff or material equivalence.
When two statements have same truth value.

Example: "All spiders are poisonous" and "No spider is poisonous" are materially equivalent (both are false).

*** Notation

p if and only if q = p ↔ q

This means two things:
- p if q AND p only if q
- p if q = q → p
- p only if q = p → q

*** Material Equivalence vs Logical Equivalence

There is also logical equivalence: https://en.wikipedia.org/wiki/Logical_equivalence

Logical equivalence is different from material equivalence. Formulas p and q are logically equivalent if and only if the statement of their material equivalence (p ↔ q) is a tautology.

The material equivalence of p and q (often written as p ↔ q) is itself another statement in the same object language as p and q. This statement expresses the idea "p if and only if q". In particular, the truth value of p ↔ q can change from one model to another.

On the other hand, the claim that two formulas are logically equivalent is a statement in metalanguage, which expresses a relationship between two statements p and q. The statements are logically equivalent if, in every model, they have the same truth value.

*** Material vs Logical Implication

Logical implication means replaceable or saying the same thing.
Surely "Dogs are mammals" and "Whales are mammals" are not saying the same thing, in different way.
They can't be replaced with each other.

Logical implication is tighter than material implication in that it is true in all circumstances, i.e. the two statements have same truth value in all cases (See Copi).

p ↔ q is false when p is true and q is false. But in p ≡ q, if p is true then q must be true.

*** Relation Between Logical and Material Equivalence

p ≡ q iff (p ↔ q is a tautology) iff (p → q and q → p are tautologies).

** Implication

*** Basic Forms

- p → q ≡ ¬p ∨ q
- p → q ≡ ¬q → ¬p

In particular ¬p → q ≡ ¬q → p.

*** Contrapositive, Converse, Inverse

Take the statement "If P then Q".

- *Converse*: If Q then P
- *Inverse*: If not P then not Q
- *Contrapositive*: If not Q then not P

The specialty of contrapositive is that it is logically equivalent to the base statement. Hence when base is true then contrapositive is also true.

*** Various Ways of Writing Implication

**** "P only if Q"

It means P only if (necessary) when Q, but Q doesn't necessarily imply P.
So that sufficiently means when not Q then not P.
So P only if Q = ¬Q → ¬P which we know is ≡ P → Q.

**** "P is sufficient condition for Q"

P → Q

**** "Q is necessary condition for P"

P → Q

**** "P unless Q"

It means that when ¬Q then P.
¬Q → P ≡ ¬P → Q.

** General Logical Equivalences

*** Identity Laws
- p ∧ ⊤ ≡ p
- p ∨ ⊥ ≡ p

*** Domination Laws
- p ∨ ⊤ ≡ ⊤
- p ∧ ⊥ ≡ ⊥

*** Idempotent or Tautology Laws
- p ∨ p ≡ p
- p ∧ p ≡ p

*** Double Negation Law
- ¬(¬p) ≡ p

*** Commutative Laws
- p ∨ q ≡ q ∨ p
- p ∧ q ≡ q ∧ p

*** Associative Laws
- (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)
- (p ∧ q) ∧ r ≡ p ∧ (q ∧ r)

*** Distributive Laws
- p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)
- p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)

*** De Morgan's Laws
- ¬(p ∧ q) ≡ ¬p ∨ ¬q
- ¬(p ∨ q) ≡ ¬p ∧ ¬q

*** Absorption Laws
- p ∨ (p ∧ q) ≡ p
- p ∧ (p ∨ q) ≡ p

*** Negation Laws
- p ∨ ¬p ≡ ⊤
- p ∧ ¬p ≡ ⊥

** Logical Equivalences Involving Conditional Statements

- p → q ≡ ¬p ∨ q
- p → q ≡ ¬q → ¬p
- p ∨ q ≡ ¬p → q
- p ∧ q ≡ ¬(p → ¬q)
- ¬(p → q) ≡ p ∧ ¬q
- (p → q) ∧ (p → r) ≡ p → (q ∧ r)
- (p → q) ∨ (p → r) ≡ p → (q ∨ r)
- (p → r) ∧ (q → r) ≡ (p ∨ q) → r
- (p → r) ∨ (q → r) ≡ (p ∧ q) → r

** Logical Equivalences Involving Biconditionals

- p ↔ q ≡ (p → q) ∧ (q → p)
- p ↔ q ≡ ¬p ↔ ¬q
- p ↔ q ≡ (p ∧ q) ∨ (¬p ∧ ¬q)
- ¬(p ↔ q) ≡ ¬p ↔ q
- ¬(p ↔ q) ≡ p ↔ ¬q
- ¬(p ↔ q) ≡ p ⊕ q

Where ⊕ represents XOR.

** Tautology, Contradiction, and Contingency

*** Tautology
A statement that's always true regardless of the truth values of its components (e.g., "P OR NOT P"). It's valid and satisfiable.

*** Contradiction
A statement that's always false regardless of the truth values (e.g., "P AND NOT P"). It's invalid and not satisfiable.

*** Contingency
A statement that can be either true or false depending on the truth values of its components (e.g., "P AND Q"). It's invalid but satisfiable.

*** Key Insight

Validity requires being always true (only tautologies), while satisfiability just requires being true in at least one case (tautologies and contingencies both qualify).

Satisfiable is that which is not contradictory and hence = contingency + tautology.
Note that contingency doesn't include tautology.

*** Important Equivalences

Commutative, associative, distributive, De Morgan's, absorption laws. Common stuff.

* First-Order Logic (Predicate Logic)

** Definition

First-order logic includes the same propositional connectives as propositional logic but differs from it because it articulates the internal structure of propositions.

This happens through devices such as:
- *Singular terms*, which refer to particular objects
- *Predicates*, which refer to properties and relations
- *Quantifiers*, which treat notions like "some" and "all"

** Examples

To express the proposition "this raven is black", one may use the predicate B for the property "black" and the singular term r referring to the raven to form the expression B(r).

To express that some objects are black, the existential quantifier ∃ is combined with the variable x to form the proposition ∃x B(x).

First-order logic contains various rules of inference that determine how expressions articulated this way can form valid arguments, for example, that one may infer ∃x B(x) from B(r).

** Scope of Variables

We cannot quantify a single variable using multiple quantifiers. Even if we see something like that, then variable will be quantified using innermost quantifier.

Example:

∃y ∀y M(y) → ∃z W(z, y)

"y" of predicate M is under the scope of (→) using innermost quantifier ∃y as well as ∀y.

** Conversion Between Quantifiers

- ∀x P(x) ≡ ¬∃x (¬P(x))
- ∃x P(x) ≡ ¬∀x (¬P(x))

** Equivalences with Quantifiers

*** Basic Equivalences

- ∀x [P(x) ∧ Q(x)] ≡ [∀x P(x)] ∧ [∀x Q(x)]
- ∃x [P(x) ∨ Q(x)] ≡ [∃x P(x)] ∨ [∃x Q(x)]

*** Important Implications (Not Equivalences)

**** Formula 3
∀x P(x) ∨ ∀x Q(x) ⇒ ∀x [P(x) ∨ Q(x)]

**** Formula 4
∃x [P(x) ∧ Q(x)] ⇒ [∃x P(x)] ∧ [∃x Q(x)]

**** Formula 5
∀x [P(x) → Q(x)] ⇒ [∀x P(x)] → [∀x Q(x)]

*** With Independent Statements Q and P

- ∀x [P(x) ∧ Q] ≡ ∀x P(x) ∧ Q
- ∃x [P(x) ∨ Q] ≡ ∃x P(x) ∨ Q
- ∀x [P(x) ∨ Q] ≡ ∀x P(x) ∨ Q
- ∃x [P(x) ∧ Q] ≡ ∃x P(x) ∧ Q

*** Implications with Independent Statements

When 'x' is not a free variable in P:
- ∀x [P → Q(x)] ≡ P → ∀x Q(x)
- ∃x [P → Q(x)] ≡ P → ∃x Q(x)

When 'x' is not a free variable in Q:
- ∀x [P(x) → Q] ≡ ∃x P(x) → Q
- ∃x [P(x) → Q] ≡ ∀x P(x) → Q

** Important Note on Existential Quantifier with Implication

∃x{ Human(x) → Intelligent(x) }

This tells that there IS ONE non-human intelligent being OR human intelligent being.

It is NOT the same as saying "some humans are intelligent".

Hence don't use → (implications) for denoting statements involving "some".

** Correct Usage of Quantifiers and Connectives

*** Examples

- ∀x {Human(x) → Intelligent(x)} means "All humans are intelligent."
  This correctly uses universal quantification with implication: for every x, if x is human, then x is intelligent.

- ∃x {Human(x) ∧ Intelligent(x)} means "Some humans are intelligent."
  This correctly uses existential quantification with conjunction: there exists at least one x that is both human and intelligent.

- ∀x {Human(x) ∧ Intelligent(x)} means "All are human & intelligent."
  This would mean everything in the domain is both human and intelligent, which is a much stronger (and likely unintended) claim.

*** General Rule

*In general:*
- If question is related to "some" then we use "∧"
- If question is related to "all" then we use "→"

This summarizes a fundamental principle in formal logic:

For statements involving "some" (existential quantification, ∃x), use conjunction (∧) to combine the condition and the property.
Example: "Some humans are intelligent" becomes ∃x (Human(x) ∧ Intelligent(x)).

For statements involving "all" (universal quantification, ∀x), use implication (→).
Example: "All humans are intelligent" becomes ∀x (Human(x) → Intelligent(x)).

** Tautology in Predicate Logic

*** Distinction from Propositional Logic

- In propositional logic, tautologies and validities are the same.
- A propositional function which is always true is called a valid propositional function or tautology.
- But in predicate logic, a distinction is maintained between logical validities and tautologies.
- A predicate formula which is always true is called a valid predicate formula but it may or may not be a tautology.
- In predicate logic, tautologies are a proper subset of logical validities.

*** Definition of Tautology in Predicate Logic

A tautology in predicate logic is a sentence that can be obtained by taking a tautology of propositional logic and uniformly replacing each propositional variable by a predicate formula (one formula per propositional variable).

*NOTE:* To check whether a given predicate formula is a tautology or not, we can only use the concepts that we have learned in propositional logic.

We cannot use the concepts of predicate logic to check whether the predicate formula is a tautology or not.

Example: A ↔ A is a tautology.

* Arguments and Inference

** Rules of Inference

Rules of inference are ways of deriving conclusions from premises. They are integral parts of formal logic, serving as norms of the logical structure of valid arguments.

Reference: https://en.wikipedia.org/wiki/Rule_of_inference

Rules of inference only ensure that the conclusion is true if the premises are true. An argument with false premises can still be valid, but its conclusion could be false.

For example, the argument "If pigs can fly, then the sky is purple. Pigs can fly. Therefore, the sky is purple." is valid because it follows modus ponens, even though it contains false premises.

A valid argument is called a *sound argument* if all of its premises are true.

** Validity of Arguments

An inference is deductively correct or valid if it follows a valid rule of inference. Whether this is the case depends only on the form or syntactical structure of the premises and the conclusion, that is, the actual content or concrete meaning of the statements does not affect validity.

This means that an argument is considered on its own, and an argument's correctness is judged based on the structure of the argument and not the truthfulness of its propositions making it up.

Example: "If God exists then world is good. God exists hence world is good" is valid argument but whether it is actually true in reality is not its concern.

** Turnstile Symbol (⊢)

⊢ (turnstile, produced tee) MEANS yields and it is a different concept from implies.

Reference: https://math.stackexchange.com/questions/286077/implies-rightarrow-vs-entails-models-vs-provable-vdash

⊢ is a shorthand for "yields", and it is part of meta language used to discuss a logical system.
→ is whereas a logical connective and part of the formal system talked about.

(What is the relation between meta language and object language? How are ≡ and ↔ related? How are ⊢ and → related?)

** Equivalent Forms of Specifying Arguments

Following statements are equivalent:

① Argument {P₁, P₂, P₃,..., Pₙ} ⊢ Q is valid.

② {P₁, P₂, P₃,..., Pₙ} Logically implies Q is valid

③ {P₁ ∧ P₂ ∧ P₃ ∧ ... ∧ Pₙ} → Q is a tautology

④ Conclusion Q follows from the premises {P₁, P₂, ... Pₙ}

** Common Rules of Inference

*** Modus Ponens (Valid)

P → Q
P
∴ Q

Example:
- If Kim is in Seoul, then Kim is in South Korea.
- Kim is in Seoul.
- Therefore, Kim is in South Korea.

*** Fallacy of Affirming the Consequent (Invalid)

P → Q
Q
∴ P

This is invalid.

*** Modus Tollens (Valid)

P → Q
¬Q
∴ ¬P

Example:
- If Koko is a koala, then Koko is cuddly.
- Koko is not cuddly.
- Therefore, Koko is not a koala.

*** Fallacy of Denying the Antecedent (Invalid)

P → Q
¬P
∴ ¬Q

This is invalid.

** Special Types of Proof

*** Conditional Proof

Argument {P₁, P₂, P₃, ..., Pₙ} ⊢ Q → R is valid

if and only if

Argument {P₁, P₂, P₃, ..., Pₙ, Q} ⊢ R is valid.

*** Proof by Contradiction

If we want to check whether the argument

P₁
P₂
⋮
Pₙ
∴ Q

is valid or not:

We will assume that the conclusion of the argument is false, i.e. we will assume that Q is false, i.e. ¬Q is true, and include that false conclusion in the set of premises.

∴ New set of premises becomes {P₁, P₂, P₃, ..., Pₙ, ¬Q}

*Note:* If this results in any contradiction, then our assumption is false & conclusion of the argument is true and hence argument is valid.

Hence, argument is invalid if there is no contradiction, then our assumption may be true.

** Additional Rules of Inference for Predicate Logic

In predicate logic, we can use some additional inference rules, along with all the rules of inference we have discussed in propositional logic.

Additional Rules of Inference w.r.t. Predicate Logic:
- Universal Instantiation (Universal Specification)
- Universal Generalization
- Existential Instantiation (Existential Specification)
- Existential Generalization

* Important Notes and Examples

** Testing Implications and Equivalences

In both types of logic [A →, ≡ and ↔ are tested differently]:

*** Testing →
We assume LHS to be true then check if RHS is true as well or not.
If RHS is itself an implication then we only need to check its LHS being true then its RHS being true or not, using the LHS of the outer implication.

*** Testing ↔
↔ requires us checking if both LHS and RHS have same truth value or not. It requires us doing LHS → RHS and RHS → LHS. It is double work.

*** Testing ≡
≡ requires us making a table and checking all cases of combinations of truth values of the individual variables
to check if both sides have same truth value or not.

** Important Example Analysis

*** Example 1: Non-equivalence of Quantifiers

Consider: ∀x [P(x) → Q(x)] vs [∀x P(x)] → [∀x Q(x)]

In the RHS, the x of P and Q both are quantified by for all.
And in LHS too, but P and Q's x are independent.

So LHS can be true when:
- All P is true then Q is also true
- When not all P is not true then Q doesn't matter

RHS is true when:
- When P then Q
- When not P then fuck off Q

So clearly, if some P is true but not all then "for all P" will be wrong, but LHS will automatically be true but RHS may evaluate to false when Q is wrong for some true P.

*** Example 2: Implication Analysis

Let E = ∀x [P(x) → Q(x)]
Let Z = [∀x P(x)] → [∀x Q(x)]

E says that if P(x) then Q(x), for all x, i.e. if P(x) is true then Q(x) or P(x) is false.
Z says that if all P(x) then all Q(x).

For E → Z to be true, when E then Z must be true. Now when E is true then if "for all x P(x)" is wrong (in Z) then Z is automatically true hence E → Z holds, but if it is true (for all x P(x)) then from E it follows that for all x Q(x).

*** Example 3: Implication Direction

If LHS is true then two cases might be:
- α is true for all x
  So β is also true for all x.
  In this case RHS = ∀x(α → β) is of course true
- α is not true for all x
  then β has no restriction, it can be true or false
  If suppose β is false then the RHS is of course false
  Hence whole option is false

*** Example 4: Combined Analysis

LHS is assumed true: so when α is true then β is also true, and the RHS of sub-implication of RHS is assumed true (for all x α) then combining these two we get that for all β.

* Meta Notes on Approach

For both types of logic:

When testing →, ≡ and ↔:
- For → we assume LHS to be true then check if RHS is true as well or not. If RHS is itself an implication then we only need to check its LHS being true then its RHS being true or not, using the LHS of the outer implication.

- For ↔ requires us checking if both LHS and RHS have same truth value or not. It requires us doing LHS → RHS and RHS → LHS. It is double work.

- For ≡ requires us making a table and checking all cases of combinations of truth values of the individual variables to check if both sides have same truth value or not.