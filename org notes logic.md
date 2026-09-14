https://en.wikipedia.org/wiki/Logic

Logic is study of argumentation. It studies informal/formal systems of argumenting.

Formal logic consits of a formal langugage (alphabets, syntactic rules), axioms/premises and rules of inferences.
Formal logic studies argumentation in general and dont deal with particular things.

Mathematical logic is formal logic.

There are many formal logic systmes based on the defining components.

Aristitolgin logic is logic of syllogism. A syllogism is argumentation consisition of two presmisies and making a conclusion.
The propositions consits of subject and copula and predicate. THere is restriction on what the copula and predicate can be.

Zero order (propositional logic) consits of propisitons and their comboations via lgocial connectives.
The propositions can be simple or compound (made from loggically connecting simples propositons).
Here the simple propositons are the basic units and we don't deal with internals of a proposition.
A simple proposition is tread as a whole and has a truthiy value of true or false.

https://en.wikipedia.org/wiki/Atomic_sentence

Example of atomic propsitons: I am a human. Not a atomic propositon: I like mars and you like earth.

Some setnesces and propsotions are true because of their structure and not because of their composing units.
These are called logical truths or tatuolgies.

Propositional logic
Main article: Propositional calculus
Propositional logic comprises formal systems in which formulae are built from atomic propositions using logical connectives.
For instance, propositional logic represents the conjunction of two atomic propositions 
P
 and 
Q
 as the complex formula 
P
∧
Q
. Unlike predicate logic where terms and predicates are the smallest units,
propositional logic takes full propositions with truth values as its most basic component.
[121] Thus, propositional logics can only represent logical relationships that arise from the way complex propositions
are built from simpler ones. But it cannot represent inferences that result from the inner structure of a proposition.[122]

First-order logic
Symbol introduced by Gottlob Frege for the universal quantifier
Gottlob Frege's Begriffsschrift introduced the notion of quantifier in a graphical notation, which here represents the judgment that 
∀
x
.
F
(
x
)
 is true.
Main article: First-order logic
First-order logic includes the same propositional connectives as propositional logic but differs from it because it
articulates the internal structure of propositions. This happens through devices such as singular terms,
which refer to particular objects, predicates, which refer to properties and relations, and quantifiers,
which treat notions like "some" and "all".[123] For example, to express the proposition "this raven is black",
one may use the predicate 
B
 for the property "black" and the singular term 
r
 referring to the raven to form the expression 
B
(
r
)
. To express that some objects are black, the existential quantifier 
∃
 is combined with the variable 
x
 to form the proposition 
∃
x
B
(
x
)
. First-order logic contains various rules of inference that determine how expressions articulated this way can form valid arguments,
for example, that one may infer 
∃
x
B
(
x
)
 from 
B
(
r
)
.[124]

----
Propositonal logic:
Truth table, say for p->q tell us the truthness of the p->q for different possiblites of truthness of its components.
---
Biconditonal, iff or material equivalcne.
When two statments have same truth value.
Eg. All spiders are posinus, and no spider is poisinus are materially equvialent (both are false).

p if and only if = p <-> q
means two things =
p if q and p only if q.
p if q = q -> p
and
p only if q = p -> q

there is also logical equivlance. https://en.wikipedia.org/wiki/Logical_equivalence
Logical equivalence is different from material equivalence. Formulas 
p
 and 
q
 are logically equivalent if and only if the statement of their material equivalence (
p
↔
q
) is a tautology.

The material equivalence of 
p
 and 
q
 (often written as 
p
↔
q
) is itself another statement in the same object language as 
p
 and 
q
. This statement expresses the idea "'
p
 if and only if 
q
'". In particular, the truth value of 
p
↔
q
 can change from one model to another.

On the other hand, the claim that two formulas are logically equivalent is a statement in metalanguage,
which expresses a relationship between two statements 
p
 and 
q
.
The statements are logically equivalent if, in every model, they have the same truth value.

Logical implication means replacble or saying the same thing.
Suerly "Dogs are mamamls" and "Whales are mamals" are not saying the same thing, in different way.
They cant be reaplced with each other.

Logical implication is tigheter than material implication in that it is true in all circutstaces,
ie the two statmnets have same truth value in all cases (See copi).

p <-> q is false when p is true and q is false. But in p = q, if p is true then q must be true.

Relation between logical and material equiacne

p = q iff (p <-> q is a tautology) iff (p->q and q->p are tautoglogies).

-----

 
Implication:
p -> q = ~p v q
p -> = ~q -> ~p
 in parituclar ~p->q = ~q->p.
contrapositve, converse, ineerse.
Take the statement “If P then Q”.

Converse: If Q then P. Inverse: If not P then not Q. Contrapositive: If not Q then not P.

The spciecially of contrapsoitvie is that it is loggically equivalne to the base statment. Hence when base is true then contrapositive is also true.

Various ways of writing implication.
- P only if Q.
It means P only if (necessary) when Q and but Q doenst necersarily imply P.
So that succicently means when not Q then not P.
So P only if Q = ~Q -> ~P which we know is = P -> Q.

- P is suffciecnt condition for Q
  P -> q

- Q is neccasry condtion for P
  p -> q

- P unless Q
  it means that when ~Q then P.
  ~q -> p = ~p -> q.


General logical equivalences
Equivalence	Name
p
∧
⊤
≡
p

p
∨
⊥
≡
p
Identity laws
p
∨
⊤
≡
⊤

p
∧
⊥
≡
⊥
Domination laws
p
∨
p
≡
p

p
∧
p
≡
p
Idempotent or tautology laws
¬
(
¬
p
)
≡
p
Double negation law
p
∨
q
≡
q
∨
p

p
∧
q
≡
q
∧
p
Commutative laws
(
p
∨
q
)
∨
r
≡
p
∨
(
q
∨
r
)

(
p
∧
q
)
∧
r
≡
p
∧
(
q
∧
r
)
Associative laws
p
∨
(
q
∧
r
)
≡
(
p
∨
q
)
∧
(
p
∨
r
)

p
∧
(
q
∨
r
)
≡
(
p
∧
q
)
∨
(
p
∧
r
)
Distributive laws
¬
(
p
∧
q
)
≡
¬
p
∨
¬
q

¬
(
p
∨
q
)
≡
¬
p
∧
¬
q
De Morgan's laws
p
∨
(
p
∧
q
)
≡
p

p
∧
(
p
∨
q
)
≡
p
Absorption laws
p
∨
¬
p
≡
⊤

p
∧
¬
p
≡
⊥
Negation laws
Logical equivalences involving conditional statements
p
→
q
≡
¬
p
∨
q
p
→
q
≡
¬
q
→
¬
p
p
∨
q
≡
¬
p
→
q
p
∧
q
≡
¬
(
p
→
¬
q
)
¬
(
p
→
q
)
≡
p
∧
¬
q
(
p
→
q
)
∧
(
p
→
r
)
≡
p
→
(
q
∧
r
)
(
p
→
q
)
∨
(
p
→
r
)
≡
p
→
(
q
∨
r
)
(
p
→
r
)
∧
(
q
→
r
)
≡
(
p
∨
q
)
→
r
(
p
→
r
)
∨
(
q
→
r
)
≡
(
p
∧
q
)
→
r
Logical equivalences involving biconditionals
p
↔
q
≡
(
p
→
q
)
∧
(
q
→
p
)
p
↔
q
≡
¬
p
↔
¬
q
p
↔
q
≡
(
p
∧
q
)
∨
(
¬
p
∧
¬
q
)
¬
(
p
↔
q
)
≡
¬
p
↔
q
¬
(
p
↔
q
)
≡
p
↔
¬
q
¬
(
p
↔
q
)
≡
p
⊕
q
Where 
⊕
 represents XOR.



Tautology: A statement that's always true regardless of the truth values of its components (e.g., "P OR NOT P"). It's valid and satisfiable.

Contradiction: A statement that's always false regardless of the truth values (e.g., "P AND NOT P"). It's invalid and not satisfiable.

Contingency: A statement that can be either true or false depending on the truth values of its components (e.g., "P AND Q"). It's invalid but satisfiable.

The key insight: validity requires being always true (only tautologies), while satisfiability just requires being true in at least one case (tautologies and contingencies both qualify).

Satisfiblae is that which is not contraditory and hence = contignecy + tagutoly.
Note that contignecy doesnt inclue tatuology.

IMportatn equivalcnes:

Commutative, assosiative, distributive, demorgas, absortipon laws. COmmon shit.


--
Argiemnt and infrence

Rules of inference are ways of deriving conclusions from premises. They are integral parts of formal logic, serving as norms of the logical structure of valid arguments.
https://en.wikipedia.org/wiki/Rule_of_inference
Rules of inference only ensure that the conclusion is true if the premises are true. An argument with false premises can still be valid, but its conclusion could be false. For example, the argument "If pigs can fly, then the sky is purple. Pigs can fly. Therefore, the sky is purple." is valid because it follows modus ponens, even though it contains false premises. A valid argument is called a sound argument if all of its premises are true.[34]

An inference is deductively correct or valid if it follows a valid rule of inference. Whether this is the case depends only on the form or syntactical structure of the premises and the conclusion, that is, the actual content or concrete meaning of the statements does not affect validity.  THis means that an arugment is considered on its own, and an arguments correct is judged based on the strcture of the argument and not the truthiness of its  premises/propsistions making it up. "If God exists then world is good. God exists hence world is good" is valid argument but wheater it is actually true in reality is not its concern.
|- (turnstile, procued tee) MEANS yields and it is different concept from implies.
https://math.stackexchange.com/questions/286077/implies-rightarrow-vs-entails-models-vs-provable-vdash

|- is a shorthand for "yields", and it is part of meta language used to discuss a logical system. -> is whearass a logical connect and part of the formal system talked about.

(What is the relation between meta langauge and object lanugage? How are =, and <-> related? How are |- and -> related?)

Note these forms of specifying arguments:

Following statements are equivalent, yields

① Argument {P1, P2, P3,......,Pn} ⊢Q is valid.

② {P1, P2, P3,......,Pn} Logically implies Q is valid

③ {P1 ∧ P2 ∧ P3 ∧ ...... ∧ Pn} → Q is a tautology

④ Conclusion Q follows from the premises {P1, P2, --- Pn}


rules of inferences:

6. Modus Ponens

P → Q
P
∴ Q

is valid

7. Fallacy of affirming the consequent

P → Q
Q
∴ P

is invalid

Topic: Rules of inference

8. Modus Tollens

P → Q
~Q
∴ ~P

is valid

9. Fallacy of denying the antecedent

P → Q
~P
∴ ~Q

is invalid

Modus ponens
P → Q     If Kim is in Seoul, then Kim is in South Korea.
P         Kim is in Seoul.
Q         Therefore, Kim is in South Korea.

Modus tollens
P → Q     If Koko is a koala, then Koko is cuddly.
¬Q        Koko is not cuddly.
¬P        Therefore, Koko is not a koala.

SOme special type of proof:



Topic: Conditional proof

Argument
{ P₁, P₂, P₃, … , Pₙ } ⊢ Q → R

is valid if and only if

Argument
{ P₁, P₂, P₃, … , Pₙ, Q } ⊢ R

is valid.


Topic: Proof by contradiction

If we want to check whether the argument

P₁
P₂
⋮
Pₙ
∴ Q

is valid or not

We will assume that the conclusion of the argument is false
i.e. we will assume that Q is false
i.e. ~Q is true

and include that false conclusion in the set of premises.

∴ New set of premises becomes
{ P₁, P₂, P₃, … , Pₙ, ~Q }

Note: If this results in any contradiction, then our assumption is false & conclusion of the argument is true and hence argument is valid.

Hence, argument is invalid if there is no contradiction, then our assumption may be true.


-------
Predicate logic

Scope of varaibles

We can not quantify a single variable using multiple quantifiers, even if we see something like that then variable will be quantified using inner-most quantifier.

e.g.

∃y ∀y M(y) → ∃z W(z, y)

“y” of predicate M is under the scope of (→) using innermost quantifier ∃y as well as ∀y.

Comversion between qunaitifers

∀x P(x) ≡ ¬∃x (¬P(x))

∃x P(x) ≡ ¬∀x (¬P(x))

Relationship diagram
[have to add image here]

Topic: Rules of Inferences w.r.t. predicate logic

In predicate logic, we can use some additional inference rules, along with all the rules of inference we have discussed in propositional logic.

Additional Rules of Inference w.r.t. Predicate Logic

Universal Instantiation (Universal Specification)

Universal Generalization

Existential Instantiation (Existential Specification)

Existential Generalization




SOme equivalcnes

∀x [P(x) ∧ Q(x)] ≡ [∀x P(x)] ∧ [∀x Q(x)]
∃x [P(x) ∨ Q(x)] ≡ [∃x P(x)] ∨ [∃x Q(x)]

SOme implications

Formula 3:
∀x P(x) ∨ ∀x Q(x) ⇒ ∀x [P(x) ∨ Q(x)]
Formula 4:
∃x [P(x) ∧ Q(x)] ⇒ [∃x P(x)] ∧ [∃x Q(x)]
Formula 5 (highlighted):
∀x [P(x) → Q(x)] ⇒ [∀x P(x)] → [∀x Q(x)]


WIth indepednt statemtes Q nad P:

∀x [P(x) ∧ Q] ≡ ∀x P(x) ∧ Q
∃x [P(x) ∨ Q] ≡ ∃x P(x) ∨ Q
∀x [P(x) ∨ Q] ≡ ∀x P(x) ∨ Q
∃x [P(x) ∧ Q] ≡ ∃x P(x) ∧ Q


∀x [P → Q(x)] ≡ P → ∀x Q(x)
'x' is not a free variable in predicate formula 'P'.
∃x [P → Q(x)] ≡ P → ∃x Q(x)
∀x [P(x) → Q] ≡ ∃x P(x) → Q
'x' is not a free variable in Q.
∃x [P(x) → Q] ≡ ∀x P(x) → Q

----

Note:
∃x{ Human(x) → Intelligent(x) }
tells that there IS ONE non human intellgient or human intelligent being.

It is not the same as saying "some humans are intelligent".

Hence dont use -> (implications) for denoting statments involving some.

∀x {Human(x) → Intelligent(x)} is labeled "All humans are intelligent."
This correctly uses universal quantification with implication: for every x, if x is human, then x is intelligent.
∃x {Human(x) ∧ Intelligent(x)} is labeled "Some humans are intelligent."
This correctly uses existential quantification with conjunction: there exists at least one x that is both human and intelligent.
∀x {Human(x) ∧ Intelligent(x)} is labeled "All are human & intelligent."
This would mean everything in the domain is both human and intelligent, which is a much stronger (and likely unintended) claim.

In general,
If question is related to "some" then we use "∧"
If question is related to "all" then we use "→"

This summarizes a fundamental principle in formal logic:

For statements involving "some" (existential quantification, ∃x), use conjunction (∧) to combine the condition and the property.
Example: "Some humans are intelligent" becomes ∃x (Human(x) ∧ Intelligent(x)).
For statements involving "all" (universal quantification, ∀x), use implication (→).
Example: "All humans are intelligent" becomes ∀x (Human(x) → Intelligent(x)).


Slide 1: Tautology in Predicate Logic

    In propositional logic, tautologies and validities are the same.

    A propositional function which is always true is called a valid propositional function or tautology.

    But in predicate logic, a distinction is maintained between logical validities and tautologies.

    A predicate formula which is always true is called a valid predicate formula but it may or may not be a tautology.

    In predicate logic, tautologies are a proper subset of logical validities.

Slide 2: Tautology in Predicate Logic

    A tautology in predicate logic is a sentence that can be obtained by taking a tautology of propositional logic and uniformly replacing each propositional variable by a predicate formula (one formula per propositional variable).

    NOTE: To check whether a given predicate formula is a tautology or not, we can only use the concepts that we have learned in propositional logic.

    We cannot use the concepts of predicate logic to check whether the predicate formula is a tautology or not.

    Valid Predicate Functions

    Tautology

    A ↔ A
---



In predicate logic pdf 7,
on page 12:
OPtion C.
in not true becasue note that
in the RHS the x of P and Q both are quantified by for all.
ANd in LHS too, but P and Q's x are independent. S

So LHS can be true when:
all P is true then Q is also true
when not all P is not true then Q doesnt matter

RHS is true when:
when P then W
when not P then fuck off W.

So clearly, if some P is true but not all then for all P will be wrong, but LHS will automaticlly be true but RHS may evaluate to false when Q is wrong for some ture P.

Page 15.
OPtion A.
The option wants us to evaluate wheater E -> Z is true where.
E says that if P(x) then Q(x), for all x ie if P(x) is true then Q(x) or P(x) is false.
Z says that if all P(x) then all Q(x).

ONe page 16
Option A:
If LHS is true then two cases might be:
- alpha is ture for all x
  So beta is allso true for all x.
  IN this cases RHS= for all x(alpha -> beta) is of course true
- alpha is not true for all x
  then beta has no resctriction, it can be true or false
  if suppose beta is false then the RHS is of coruse fasle
  Hence whole option A is false

OPtion D:
LHS is asummed true: so when alpha is true then beta is also true, and the RHS of sub implication of  RHS is assumed true (for all x alpha) then combiing these two we get that for all beta.



For E->Z to be true, when E then Z must be true. Now when E is true then if for all P(x) is wrong (in Z) then Z is automatically ture hence E -> Z holds, but if it is true (for all x P(x)) then fromt E it follows that for all x Q(x).

In both type of logic.
[A ->, = and <-> are teseted differnlty]
-> we assume LHS to be true then check if RHS is true as well or not. If RHS is itself a implication then we only need to check its LHS being true then its RHS being true or not, using the LHS of the outer implication.

<-> requires us checking if both LHS and RHS have same truthiy value or not. It requires us doing LHS -> RHS and RHS -> LHS. It is double work.

= requires us making a table and chceking all cases of comibiatons of truth values of the indivual varibales to check if both sides have same truthiy value or not.