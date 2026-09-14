# Recurrence Relations

**Topic:** Discrete Math > Recurrence Relations
**Source:** GO Classes — Deepak Poonia
**Tags:** #gate/discrete-math #recurrence-relations #sequences
**Links:** [[padai/maths/discrete maths/moc dm]] | [[combinatorics/combinatorics]] | [[Sequences]]

---

> [!info] Overview
> A recurrence relation expresses a term $a_n$ in terms of previous terms. Together with initial conditions, it uniquely determines a sequence.

---

## 1. Sequences & Recurrence Relations

A **sequence** is an ordered list of elements — order matters, so $\langle 1, 2, 3 \rangle \neq \langle 2, 1, 3 \rangle$.

A **recurrence relation** for $\{a_n\}$ is an equation expressing $a_n$ in terms of $a_0, a_1, \dots, a_{n-1}$, for all $n \geq n_0$.

**Initial conditions** specify the terms before $n_0$ (where the recurrence kicks in). Equation + initial conditions → unique sequence.

> [!note] Key Point
> Many sequences can satisfy the same recurrence. Initial conditions are what pin down a unique one.

### 1.1 Standard Examples

**Arithmetic sequence** $\langle 3, 8, 13, 18, \dots \rangle$:

$$
a_n = a_{n-1} + 5, \quad a_0 = 3
$$

**Fibonacci sequence** $\langle 0, 1, 1, 2, 3, 5, 8, \dots \rangle$:

$$
a_n = a_{n-1} + a_{n-2}, \quad n \geq 2, \quad a_0 = 0,\ a_1 = 1
$$

**Natural numbers** $\langle 1, 2, 3, 4, \dots \rangle$:

$$
a_n = a_{n-1} + 1, \quad a_0 = 1
$$

### 1.2 Same Recurrence, Different Sequences

$$
a_n = 2a_{n-1} - a_{n-2}, \quad n \geq 2
$$

- $a_0 = 5,\ a_1 = 5 \Rightarrow \langle 5, 5, 5, 5, \dots \rangle$
- $a_0 = 0,\ a_1 = 5 \Rightarrow \langle 0, 5, 10, 15, \dots \rangle$

Both satisfy the same recurrence — initial conditions make them distinct.

---

## 2. Worked Examples — Finding Closed Form

**Given:** $a_n = 5a_{n-1} - 6a_{n-2}$

**Case 1:** $a_0 = 1,\ a_1 = 2$

$$
a_2 = 4,\ a_3 = 8,\ a_4 = 16 \implies a_n = 2^n
$$

**Case 2:** $a_0 = 1,\ a_1 = 3$

$$
a_2 = 9,\ a_3 = 27 \implies a_n = 3^n
$$

---

## 3. Recursive Functions

A recursive function defines its value using smaller instances of itself — same idea as a recurrence relation, applied to functions.

| Function       | Recurrence                                     |
| :------------- | :--------------------------------------------- |
| Factorial      | $f(n) = n \cdot f(n-1),\quad f(0) = 1$         |
| Multiplication | $\text{mul}(a,b) = \text{mul}(a, b-1) + a$     |
| Exponentiation | $\text{pow}(a,b) = \text{pow}(a, b-1) \cdot a$ |
| Fibonacci      | $f(n) = f(n-1) + f(n-2)$                       |
| Sum of list    | $S_{0\dots n} = S_{0\dots n-1} + a_n$          |

---

## 4. Applications — Counting Problems

### 4.1 Bit strings with NO two consecutive 0s

Let $f(n)$ = number of $n$-length bit strings with no two consecutive 0s.

**Recurrence:** split on last bit(s):
- Ends in `1` → prefix is any valid $(n-1)$-length string: $f(n-1)$ ways
- Ends in `10` → prefix is any valid $(n-2)$-length string: $f(n-2)$ ways

$$
f(n) = f(n-1) + f(n-2), \quad f(1) = 2,\ f(2) = 3
$$

Sequence: $2, 3, 5, 8, 13, \dots$ (Fibonacci-like). $f(5) = 13$.

### 4.2 Bit strings WITH two consecutive 0s

Let $T(n)$ = number of $n$-length bit strings containing at least one `00`.

Split on how the string ends:
- Ends in `1` → $T(n-1)$
- Ends in `10` → $T(n-2)$
- Ends in `00` → first $n-2$ bits are anything → $2^{n-2}$

$$
T(n) = T(n-1) + T(n-2) + 2^{n-2}, \quad T(1) = 0,\ T(2) = 1
$$

Verify: $T(3) = 1 + 0 + 2 = 3$ → $\{001, 100, 000\}$ ✓

### 4.3 Bit strings with THREE consecutive 0s

Let $a_n$ = number of $n$-length bit strings containing `000`.

Split on how the string ends:

| Suffix | Remaining prefix | Count |
| :--- | :--- | :--- |
| `1` | $(n-1)$-length with `000` | $a_{n-1}$ |
| `10` | $(n-2)$-length with `000` | $a_{n-2}$ |
| `100` | $(n-3)$-length with `000` | $a_{n-3}$ |
| `000` | first $(n-3)$ bits are anything | $2^{n-3}$ |

$$
a_n = a_{n-1} + a_{n-2} + a_{n-3} + 2^{n-3}, \quad n \geq 3
$$

Initial conditions: $a_0 = a_1 = a_2 = 0,\ a_3 = 1$

Computed sequence: $0, 0, 0, 1, 3, 8, 20, 47, \dots$

**$a_7 = 47$**

### 4.4 Permutations of $n$ elements

Let $P(n)$ = number of permutations of an $n$-element set.

Choose which of the $n$ elements goes last — the remaining $(n-1)$ elements form $P(n-1)$ arrangements:

$$
P(n) = n \cdot P(n-1), \quad P(1) = 1
$$

### 4.5 Paying $n$ pesos (ordered)

Coins: 1, 2, 5, 10 peso. Bills: 5, 10 peso. Order matters.

$$
a_n = a_{n-1} + a_{n-2} + 2 \cdot a_{n-5} + 2 \cdot a_{n-10}, \quad a_0 = 1, \quad a_n = 0 \text{ for }  n<0
$$

(Factor of 2 for 5 and 10 because coin ≠ bill of same denomination.)

$a_{17} = 9494$

---

## 5. GATE PYQ

> [!example] GATE 2016-1 — Q2
> **Question:** Let $a_n$ = number of $n$-bit strings NOT containing two consecutive 1s. Which recurrence?
>
> A. $a_n = a_{n-1} + 2a_{n-2}$
> B. $a_n = a_{n-1} + a_{n-2}$
> C. $a_n = 2a_{n-1} + a_{n-2}$
> D. $a_n = 2a_{n-1} + 2a_{n-2}$
>
> **Approach:**
> Split on last bit(s) — same logic as no-consecutive-0s:
> - Ends in `0` → $a_{n-1}$
> - Ends in `01` → $a_{n-2}$
>
> $$
> a_n = a_{n-1} + a_{n-2}
> $$
>
> Quick check: $a_1=2,\ a_2=3,\ a_3=5$ ✓
>
> **Answer:** $\boxed{B}$

---

## Related Notes

- [[Discrete Math MOC]]
- [[Combinatorics — Counting]]
- [[Linear Recurrences — Solving (Characteristic Equation)]]
- [[GATE PYQs — Recurrence Relations]]

## Open Questions

- [ ] General method for solving linear recurrences with constant coefficients?
- [ ] 
- [ ] Why does the "split on last suffix" trick always work — what's the formal justification?
- [x] Revisit the pesos problem: why exactly is $a_0 = 1$ (empty payment)?
- [ ] [[recursion]] [[Recursions]] [[recursion 1]] [[Linear Recurrences — Solving (Characteristic Equation)]] [[4.1 Characteristic Polynomial & Superposition]]

lets get mathy.... there is recurreration relations in matheatics and there is recure equaitons in time complexity..... there is clear relation between them.....but there is also recurrences relation to functions...... i want you to realte these three...... like how does solving time recureces realte to the math ones and how do recurecnes of function relate to the other.... also relate the type of recurence how to convert between them..... and how to solve those problems where one function recuvisely calls other and that fucntiosn calls the same function or other function recuviely...and they interweve .... how do i solve those questions by hand..... hwo to resaons about the whole things the types of problems in all these types of recurecnes....what unites them what sperates themmm common patterns that help me solve them with itutive understaing.... like how does master method realte to math recurces....... eg of recusrive spaggeti probem i am talig about: int bar(int n) { if (n == 1) return 0; else return 1 + bar(n/2); } int foo(int n) { if (n == 1) return 1; else return 1 + foo(bar(n)); } #include < stdio.h > int foo(int S[],int size){ if(size == 0) return 0; if(size == 1) return 1; if(S[0] != S[1]) return 1+foo(S+1,size-1); return foo(S+1,size-1); } int main(){ int A[]={0,1,2,2,2,0,0,1,1}; printf("%d",foo(A,9)); return 0; } #include < stdio.h > int foo(int x, int y, int q) { if ((x < = 0) && (y < = 0)) return q; if (x < = 0) return foo(x, y-q, q); if (y < = 0) return foo(x-q, y, q); return foo(x, y-q, q) + foo(x-q, y, q); } int main( ) { int r = foo(15, 15, 10); printf("%d", r); return 0; } int f(int x) { if(x<1) return 1; else return (f(x-1) + g(x)); } int g(int x) { if(x<2) return 2; else return (f(x-1) + g(x/2)); }....


	claude:
		Good question to dig into — these three "recurrences" really are one concept wearing three different costumes. Let me unify them, then work through your spaghetti examples by hand.

## Why they're the same object

A recurrence relation is just: _a value defined in terms of itself at smaller arguments, plus a base case._ That's it. The three flavors you mention differ only in what the "value" represents:

- **Math recurrence**: the value is a number in a sequence. $a_n = a_{n-1} + a_{n-2}$.
- **Time complexity recurrence**: the value is _runtime_ of an algorithm on input size $n$. $T(n) = T(n-1) + O(1)$.
- **Recursive function**: the value is the _actual output_ the function computes. `bar(n) = 1 + bar(n/2)`.

The deep point: when a recursive function does $O(1)$ work outside its recursive call(s), its **output recurrence** and its **time-complexity recurrence** are literally the same equation, just relabeled. `bar(n) = 1 + bar(n/2)` computing a _value_ has the identical shape as `T(n) = T(n/2) + O(1)` computing _time_ — because each call contributes one unit of "work" (the `+1`) the same way it contributes one unit of "time." This is why solving "what does this function return" and "what is this function's complexity" often feels like the same exercise — for simple cases it literally is the same recurrence.

So a math recurrence is the general theory; complexity recurrences are math recurrences specialized to runtime; recursive functions are math recurrences specialized to whatever value the function is computing. Same toolbox.

## The taxonomy (and which tool solves which)

**1. Linear, constant-coefficient, fixed-offset** — $a_n = c_1 a_{n-1} + c_2 a_{n-2} + \dots$ (Fibonacci-style). Solved with the **characteristic equation**: guess $a_n = r^n$, plug in, get a polynomial in $r$, solve for roots, general solution is a combination of $r_i^n$ terms, fit constants with base cases.

**2. Decreasing-by-constant with extra work per level** — $T(n) = T(n-1) + f(n)$. Solved by **telescoping/summation**: unroll and sum $f$ across all levels. $T(n) = T(0) + \sum_{k=1}^n f(k)$.

**3. Divide-and-conquer** — $T(n) = aT(n/b) + f(n)$. Solved by **recursion tree**, **substitution method**, or the **Master theorem** as a shortcut.

**4. Nested/composed recurrences** — one recurrence's output feeds into another as the _argument_, e.g. `foo(n) = 1 + foo(bar(n))`. No standard theorem — you solve `bar` first in closed form, then study how repeatedly applying that closed form shrinks $n$ to the base case. Often produces **iterated functions** like $\log^* n$ (iterated log).

**5. Mutual recursion / interleaved functions** — `f` calls `g`, `g` calls `f`, possibly with different shrinking rules. Solved by **substitution-elimination** (substitute one into the other to get a single recurrence in one variable) when the argument patterns align, or by **building a coupled value table** and unrolling by hand when they don't (this is what you'll actually do under exam pressure).

## How Master theorem relates to characteristic equations

These are secretly the same idea, expressed two different ways. The characteristic equation finds the **dominant root** $r$ of a linear recurrence — the growth rate is $\Theta(r^n)$. The Master theorem does the same job for divide-and-conquer recurrences, except since $b$ in $T(n/b)$ usually isn't a clean integer ratio, you can't factor a polynomial the same way. Instead you reason about the **recursion tree**: $a$ children per node, tree depth $\log_b n$, so total leaves $= n^{\log_b a}$. The Master theorem is just "compare the cost of all the leaves ($n^{\log_b a}$) against the cost of the root's own work ($f(n)$), and whichever dominates wins" — that's a shortcut for the recursion-tree method, the same way the characteristic equation is a shortcut for "guess $r^n$ and solve." Recursion tree is the general method that subsumes both; Master theorem and characteristic equations are just closed-form fast paths for well-behaved special cases.

## The actual problem-solving algorithm for messy/nested/mutual recursions

When functions call each other and call themselves, in practice (especially for GATE-style "compute the exact output" questions), the _closed-form_ approach is usually a trap — these problems are designed to be solved by **disciplined hand-tracing with memoization**, not algebra. The method:

1. Write a small table: column for each distinct argument value that appears, value computed.
2. Unroll outward from the deepest/smallest arguments first (bottom-up), reusing table entries instead of recomputing — this is literally dynamic programming applied by hand.
3. Watch for arguments that recur across both functions — that's where the "interweaving" creates shared subproblems, and your table catches that automatically instead of you getting lost in nested call stacks.
4. Only look for a closed form / pattern in $n$ if the trace reveals a regular structure (geometric, telescoping, etc.) — otherwise just trust the table.

Now let's run this method on your four examples.

### 1. `bar`/`foo` — nested recurrence, log-star pattern

$\text{bar}(n) = 1 + \text{bar}(n/2)$, $\text{bar}(1) = 0$ gives the closed form $\text{bar}(n) = \log_2 n$.

$\text{foo}(n) = 1 + \text{foo}(\text{bar}(n))$, $\text{foo}(1) = 1$ — each call replaces $n$ with $\log_2 n$. So the argument sequence is $n, \log n, \log\log n, \log\log\log n, \dots$ until it hits 1. This is exactly the definition of **iterated logarithm**, $\log^* n$: foo counts how many times you can apply $\log$ before reaching 1, plus the base case. So $\text{foo}(n) = \log^_(n) + 1$ (roughly — exact constant depends on how `bar(1)=0` interacts with `foo`'s base case, worth tracing for a specific $n$ if you need an exact number). The general lesson: **function composed with itself recursively → growth governed by how many times you can iterate the inner function before hitting the base case.** This pattern shows up constantly in GATE (Union-Find's $\log^_ n$ bound is the canonical example).

### 2. Array `foo` — counts contiguous runs

Tracing `foo(A, 9)` on `A = {0,1,2,2,2,0,0,1,1}`: at each step it compares `S[0]` vs `S[1]` and adds 1 only when they differ, recursing on the suffix. Walking the array: (0,1) differ, (1,2) differ, (2,2) same, (2,2) same, (2,0) differ, (0,0) same, (0,1) differ, (1,1) same, plus the base case `size==1` contributes 1.

$1+1+0+0+1+0+1+0+1 = 5$.

So `foo(A,9) = 5`. Notice this exactly equals the number of "runs" in the array (0 | 1 | 2,2,2 | 0,0 | 1,1 → 5 runs). The recurrence is secretly counting **run-length boundaries** — recognizing this pattern means you don't need to trace at all next time, you just count distinct adjacent groups.

### 3. `foo(x,y,q)` — branching subtraction, recursion-tree-as-table

This one genuinely needs the table method since it branches in two directions. Tracing `foo(15,15,10)` bottom-up (computing smallest/most-negative argument pairs first):

`foo(-5,-5,10) = 10` (base case, both ≤ 0) `foo(5,-5,10) = foo(-5,-5,10) = 10` `foo(-5,5,10) = foo(-5,-5,10) = 10` `foo(15,-5,10) = foo(5,-5,10) = 10` `foo(5,5,10) = foo(5,-5,10) + foo(-5,5,10) = 10+10 = 20` `foo(-5,15,10) = foo(-5,5,10) = 10` `foo(15,5,10) = foo(15,-5,10) + foo(5,5,10) = 10+20 = 30` `foo(5,15,10) = foo(5,5,10) + foo(-5,15,10) = 20+10 = 30` `foo(15,15,10) = foo(15,5,10) + foo(5,15,10) = 30+30 = 60`

**Answer: 60.** This is a great example of why the table beats trying to find a closed form — the branching makes a clean formula messy, but a bottom-up table is mechanical and fast by hand.

### 4. `f`/`g` mutual recursion

`f(x) = 1` if `x<1` else `f(x-1)+g(x)`; `g(x) = 2` if `x<2` else `f(x-1)+g(x/2)` (integer division). Build one shared table, smallest $x$ first:

$f(0)=1,\ g(0)=2,\ g(1)=2$ $f(1) = f(0)+g(1) = 1+2 = 3$ $g(2) = f(1)+g(1) = 3+2 = 5$ $f(2) = f(1)+g(2) = 3+5 = 8$ $g(3) = f(2)+g(1) = 8+2 = 10$ (since $3/2=1$) $f(3) = f(2)+g(3) = 8+10 = 18$ $g(4) = f(3)+g(2) = 18+5 = 23$ $f(4) = f(3)+g(4) = 18+23 = 41$

Note how `g(x/2)` makes `g` jump around non-adjacent indices — exactly the kind of interweaving where a shared table (rather than trying to substitute one equation into the other algebraically) is the only sane hand method, since the integer-division term breaks any clean characteristic-equation approach.

**The unifying takeaway**: linear/divide-conquer recurrences with a single clean recursive call have algebraic shortcuts (characteristic equation, Master theorem). The moment you get composition (`foo(bar(n))`), branching (two recursive calls with different arguments), or mutual recursion with non-uniform shrinking (`x/2` mixed with `x-1`), the reliable hand technique is always the same: build a bottom-up table of (argument → value), fill in smallest arguments first, and let shared subproblems collapse the work. Pattern-spotting (run-length counting, iterated-log) is a bonus you get _after_ tracing enough small cases to see it — don't go hunting for a closed form first under exam time pressure.


gemini

## The Unifying Philosophy: Reductions and State Space

At their core, all three concepts—mathematical recurrence relations, time complexity recurrences, and recursive functions—are exactly the same fundamental entity viewed through different lenses.

- **Mathematical Recurrence Relations** are the pure, symbolic abstraction. They describe a sequence of values where each term is a function of preceding terms.
    
- **Time Complexity Recurrences** are a specific application of mathematical recurrences where the sequence values represent _computational cost_ (steps, time, or memory) relative to an input size $n$.
    
- **Recursive Functions** are the concrete implementation. They represent a computational process that navigates a state space by breaking a problem into smaller instances of itself.
    

What unites them is the concept of a **Directed Acyclic Graph (DAG) of dependencies**. Every recurrence defines a rule for traversing this graph from a complex state down to base cases. What separates them is merely what you are measuring: the output value of the state (functions), the mathematical sequence position (math), or the total work done to traverse the sub-graph (time complexity).

## Mapping and Converting Between Types

To navigate these problems smoothly, you need to understand how to translate the behavior of a code snippet into a formal mathematical representation.

### From Function to Math Recurrence (Value Tracking)

When you want to find the mathematical value returned by a recursive function, you track the output. For example, if a function is defined as:

C

```
int f(int n) {
    if (n <= 1) return 1;
    return f(n-1) + f(n-2);
}
```

The exact mathematical recurrence for its _value_, $V(n)$, directly mirrors the return statements:

$$V(n) = V(n-1) + V(n-2) \quad \text{for } n > 1, \quad V(0)=1, V(1)=1$$

### From Function to Time Complexity Recurrence (Work Tracking)

When analyzing runtime, you ignore the _value_ returned by the function and instead count the _operations_ performed. If the same function `f(n)` executes an addition operation (which takes $O(1)$ constant time) alongside its recursive calls, its time complexity $T(n)$ is modeled as:

$$T(n) = T(n-1) + T(n-2) + \Theta(1)$$

### How the Master Method Bridges the Gap

The Master Method is simply a shortcut cookbook for solving a specific class of mathematical divide-and-conquer recurrences: $T(n) = aT(n/b) + f(n)$.

In pure mathematics, you can solve this using substitution or characteristic equations. The Master Method bypasses that tedious algebraic work by comparing the rate of problem reduction ($n^{\log_b a}$, which represents the number of leaves in the implicit recursion tree) against the work done at the current level ($f(n)$). It identifies which component dominates the total computational growth.

## Untangling "Recursive Spaghetti": A Framework for Manual Solution

When dealing with complex, interleaved, or multi-variable recursive functions, trying to hold the execution execution trace in your head leads to errors. You must formalize your analysis using three distinct mental models depending on the problem structure.

### 1. Interleaved and Mutually Recursive Functions

When Function $f$ calls Function $g$, and Function $g$ calls Function $f$, you are dealing with a system of simultaneous recurrence equations.

**Example from your prompt:**

C

```
int f(int x) {
    if(x<1) return 1;
    return f(x-1) + g(x);
}
int g(int x) {
    if(x<2) return 2;
    return f(x-1) + g(x/2);
}
```

**How to reason and solve by hand:**

- **Step 1: Write the algebraic system.** Translate the code directly into equations.
    
    $$f(x) = f(x-1) + g(x)$$
    
    $$g(x) = f(x-1) + g(x/2)$$
    
- **Step 2: Substitute to decouple.** Attempt to isolate one function by substituting one equation into the other. From the first equation, we know that $g(x) = f(x) - f(x-1)$. Therefore, we can also write $g(x/2) = f(x/2) - f(x/2 - 1)$.
    
- Substitute these back into the equation for $g(x)$ to get a recurrence containing only $f$:
    
    $$f(x) - f(x-1) = f(x-1) + f(x/2) - f(x/2 - 1)$$
    
    $$f(x) = 2f(x-1) + f(x/2) - f(x/2 - 1)$$
    
- **Step 3: Tabulate small values if looking for an exact match.** If the algebraic substitution yields an unpliable form, map out a dependency table for small integer values of $x$:
    

|**x**|**f(x) base / evaluated**|**g(x) base / evaluated**|
|---|---|---|
|**0**|$f(0) = 1$ (Base)|$g(0) = 2$ (Base)|
|**1**|$f(1) = f(0) + g(1) = 1 + 2 = 3$|$g(1) = 2$ (Base)|
|**2**|$f(2) = f(1) + g(2) = 3 + g(2)$|$g(2) = f(1) + g(1) = 3 + 2 = 5 \implies f(2) = 3 + 5 = 8$|

### 2. Functional Composition inside Recursion

When the argument of a recursive call is determined by the output of another recursive call, you must evaluate from the inside out.

**Example from your prompt:**

C

```
int bar(int n) {
   if (n == 1) return 0;
   return 1 + bar(n/2);
}
int foo(int n) {
   if (n == 1) return 1;
   return 1 + foo(bar(n));
}
```

**How to reason and solve by hand:**

- **Step 1: Solve the inner function first.** Analyze `bar(n)` independently. It repeatedly divides $n$ by 2 until it hits 1, adding 1 each time. This is the definition of the floor of the binary logarithm: $\text{bar}(n) = \lfloor \log_2(n) \rfloor$.
    
- **Step 2: Rewrite the outer function.** Replace the inner call with its closed-form solution.
    
    $$\text{foo}(n) = 1 + \text{foo}(\lfloor \log_2(n) \rfloor)$$
    
- **Step 3: Track the state decay.** Watch how rapidly $n$ drops. Let's trace $\text{foo}(16)$:
    
    - $\text{foo}(16) = 1 + \text{foo}(\text{bar}(16)) = 1 + \text{foo}(4)$
        
    - $\text{foo}(4) = 1 + \text{foo}(\text{bar}(4)) = 1 + \text{foo}(2)$
        
    - $\text{foo}(2) = 1 + \text{foo}(\text{bar}(2)) = 1 + \text{foo}(1)$
        
    - $\text{foo}(1) = 1$ (Base case)
        
    - Total for $\text{foo}(16) = 1 + 1 + 1 + 1 = 4$.
        
- This log-of-logs pattern reveals that the function tracks the number of times you can apply the logarithm function before hitting the base case, closely mirroring the iterated logarithm function, $\log^* n$.
    

### 3. Multi-Variable State Space and Tracking Grids

When functions take multiple arguments that decrement differently, treat the problem as a walk across a coordinate grid or matrix.

**Example from your prompt:**

C

```
int foo(int x, int y, int q) {
    if ((x <= 0) && (y <= 0)) return q;
    if (x <= 0) return foo(x, y-q, q);
    if (y <= 0) return foo(x-q, y, q);
    return foo(x, y-q, q) + foo(x-q, y, q);
}
```

**How to reason and solve by hand:**

- **Step 1: Identify invariant variables.** Notice that $q$ never changes during execution ($q = 10$). It acts as a static step size.
    
- **Step 2: Map the grid coordinates.** Your state is a coordinate $(x, y)$. The operations reduce either $x$ or $y$ by $q$. For `foo(15, 15, 10)`, the step size is 10. Subtracting 10 from 15 drops the coordinate to 5. Subtracting 10 again drops it to -5 (which triggers the $\le 0$ base cases).
    
- **Step 3: Draw the Execution Tree.** For small discrete steps, a tree diagram explicitly maps the paths:
    

```
                  (15, 15)
                 /        \
          (15, 5)          (5, 15)
          /     \          /     \
     (15, -5)  (5, 5)  (5, -5)  (5, 5)
```

- When either coordinate hits $\le 0$, the branching stops and it converts to a single track or hits the final base case value $q$. By tracing this grid manually, you transform an imposing multi-variable equation into a finite set of coordinate pathways.
    

### 4. Array Pointer Manipulation Tracking

When a recursive function processes an array by advancing pointers, do not think of it as a mathematical sequence. Think of it as a state machine scanning an array.

**Example from your prompt:**

C

```
int foo(int S[], int size) {
    if(size == 0) return 0;
    if(size == 1) return 1;
    if(S[0] != S[1]) return 1 + foo(S+1, size-1);
    return foo(S+1, size-1);
}
```

**How to reason and solve by hand:**

- **Step 1: Decipher the pointer shift.** `S+1` moves the array pointer forward by one element, and `size-1` keeps the bounds accurate. This means the function processes the array linearly from left to right, one element at a time.
    
- **Step 2: Translate the conditional logic.** The condition `if(S[0] != S[1])` checks if the current element is different from the immediate next element. If they are different, it adds 1 to the tally. If they are identical, it advances without adding to the tally.
    
- **Step 3: State the invariant purpose.** This function counts the number of times adjacent elements change value, plus a base case value of 1 for the remaining element. Given your array `A[] = {0, 1, 2, 2, 2, 0, 0, 1, 1}`, let's mark where transitions occur:
    
    - $0 \to 1$ (Different: count = 1)
        
    - $1 \to 2$ (Different: count = 2)
        
    - $2 \to 2$ (Same)
        
    - $2 \to 2$ (Same)
        
    - $2 \to 0$ (Different: count = 3)
        
    - $0 \to 0$ (Same)
        
    - $0 \to 1$ (Different: count = 4)
        
    - $1 \to 1$ (Same)
        
    - The execution reaches `size == 1` at the final element, returning 1.
        
    - Total accumulated value = $4 + 1 = 5$.
        

## Summary of Common Patterns

|**Pattern Type**|**Key Characteristic**|**Best Mental Tool for Manual Solution**|
|---|---|---|
|**Mutual Recursion**|Functions call each other in a loop.|Algebraic substitution to isolate variables, or a dependency table.|
|**Nested Composition**|Outer function accepts inner function's result.|Inner-out execution analysis; determine how fast the core argument decays.|
|**Multi-Variable Grid**|Step modifications to multiple inputs.|Coordinate tree or state lattice mapping.|
|**Linear Pointer Scan**|Linear reduction of data collection structures.|Stream parsing interpretation (identifying the pattern condition).|

Which of these four structural patterns do you find most challenging to visualize when analyzing a problem completely from scratch?

https://claude.ai/chat/1205840e-fef7-45d0-8809-326ab632cb63
https://share.gemini.google/JQRvwrcI6G66
https://claude.ai/share/cb6c2b5b-8228-42bc-aa1c-cdaf256d35d3