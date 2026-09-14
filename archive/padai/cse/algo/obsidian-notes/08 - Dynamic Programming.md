# ⚡ Dynamic Programming

> [!abstract] Properties
> 
> - **Source:** GoClasses.in — Lectures 36a → 42e
>     
> - **Topic:** #algorithms #dp #GATE
>     
> - **Prerequisites:** Recursion, Greedy, Divide & Conquer
>     
> - **Links:** [[LCS]], [[Matrix Chain Multiplication]], [[Floyd Warshall]]
>     
> - **Note Meta:** Chapter 5 | Pages 45–51 | Quantum City (AIR 107)
>     

---

## 📑 Table of Contents

1. [[#Introduction — Fibonacci]]
    
2. [[#Elements of Dynamic Programming]]
    
3. [[#5.1 Longest Common Subsequence (LCS)]]
    
4. [[#5.2 Matrix Chain Multiplication & Knapsack]]
    
5. [[#5.3 More Dynamic Programming Algorithms]]
    
6. [[#Summary Table]]
    

---

## Introduction — Fibonacci

`// Lecture 36a`

The classic example motivating DP is the Fibonacci sequence. The brute-force recursive approach recomputes many subproblems repeatedly.

> [!warning] Brute Force — Exponential
> 
> $T(n) = T(n-1) + T(n-2) + 1 \implies O(2^n)$
> 
> The recursion tree shows **same computation done twice** (e.g., `fib(3)` computed multiple times).

C

```
// Brute Force
int fibo(n) :
    if(n == 0 or n == 1) return 1;
    return fibo(n-1) + fibo(n-2);
```

### Top-Down (Memoization)

Save previously calculated values in an array. **Trades space for time.** We go from $n$ down to $1$, hence _top-down_.

C

```
// dp is initialized all -1
int fibo(n) :
    if(dp[n] != -1) return dp[n];   // already computed
    if(n == 0 or n == 1) dp[n] = 1;
    else dp[n] = fibo(n-1) + fibo(n-2);
    return dp[n];
```

### Bottom-Up (Tabulation)

Fill the DP table iteratively from base cases upward: $dp[0] \to dp[1] \to dp[2] \to \dots \to dp[n]$.

C

```
int fibo(n) :
    dp[0] = dp[1] = 1;
    for(i = 2 to n)
        dp[i] = dp[i-1] + dp[i-2];
    return dp[n];
```

|**🔽 Top-Down**|**🔼 Bottom-Up**|
|---|---|
|Start from $n$, recurse down to base cases. Uses memoization.|Start from base cases, iteratively build up. Uses tabulation.|
|$n \to n-1 \to \dots \to 1$|$dp[0] \to dp[1] \to \dots \to dp[n]$|

> [!tip] 📝 Note
> 
> After getting recurrence relation from problem statement, use **tabular approach** to find value of specifics asked in question. (Lecture 37b)

Example: $A(i, j) = \min( A(i, j-1), A(i-1, j), A(i-1, j+1) )$. Fill the table **row-wise** observing dependencies.

---

## Elements of Dynamic Programming

`// Lecture 37c`

> [!info] 🧩 Optimal Substructure
> 
> Solving **smaller subproblems of the same kind**. An optimal solution to the problem contains optimal solutions to its subproblems.

> [!tip] ♻️ Overlapping Subproblems
> 
> Check if a problem is being **solved again**. If so, keep a table and save time by reusing computed results.

### DP vs Divide & Conquer vs Greedy

- **Merge Sort (D&C):** Subproblems are _independent_ — no overlapping subproblems.
    
- **Fibonacci (DP):** Subproblems are _dependent/overlapping_.
    
- **Greedy:** Has optimal substructure but _not_ overlapping subproblems (one move at a time).
    
- **D&C:** Has optimal substructure but _not_ overlapping subproblems (two halves are independent).
    

**Q:** Do we have optimal substructure in Divide and Conquer?

**A:** Yes — subproblems of the same kind. But **no overlapping subproblems** because the two subproblems are independent.

**Q:** Do we have optimal substructure in Greedy?

**A:** Yes — after selecting one element we decrease the search key area. But **no overlapping subproblems** because we do one move at a time.

---

## 5.1 Longest Common Subsequence (LCS)

`// Lecture 38a — 38c`

> [!important] Definition
> 
> A sequence **Z** is a _subsequence_ of $X$ if $Z$ can be obtained from $X$ by **dropping symbols** (not necessarily contiguous).
> 
> _Example:_ `BDFH` is a subsequence of `ABCDEFGH`.

### Naïve Algorithm

1. Enumerate all possible subsequences of $X$ ($2^n$ total).
    
2. For each, check if it is a subsequence of $Y$ using two pointers.
    
3. **Running time:** $O(n \cdot 2^n)$
    

### 5.1.1 Using Dynamic Programming

Let $LCS[i, j]$ = length of the longest common subsequence of $X[1\dots i]$ and $Y[1\dots j]$.

$$LCS[i, j] = \begin{cases} 1 + LCS[i-1, j-1] & \text{if } x_i = y_j \\ \max \{ LCS[i-1, j], LCS[i, j-1] \} & \text{if } x_i \neq y_j \\ 0 & \text{if } i = 0 \text{ or } j = 0 \end{cases}$$

**Complexity:**

- **Recursive Calls:** $O(\max(2^m, 2^n))$
    
- **Unique Calls (DP):** $m \times n$ (one per table cell).
    

---

## 5.2 Matrix Chain Multiplication & Knapsack

`// Lecture 40a — 40c`

> [!note] Key Fact
> 
> Multiplying matrix $A_{p \times q}$ with $B_{q \times r}$ requires $p \times q \times r$ scalar multiplications.

**Problem:** Find parenthesization that minimizes scalar multiplications.

- **Brute Force:** Number of ways = **Catalan number** = $\frac{(2n)!}{(n+1)! \cdot n!}$. Complexity is $\Omega(2^n)$.
    

### 5.2.1 DP Formulation

Let $m[i, j]$ = minimum cost of multiplying matrices $A_i \dots A_j$.

$$m[i, j] = \min_{k=i \text{ to } j-1} (m[i, k] + m[k+1, j] + P_{i-1} \cdot P_k \cdot P_j) \text{ if } i < j$$

$$m[i, j] = 0 \text{ if } i = j$$

**Time Complexity:** $O(n^3)$ (Table size $O(n^2) \times O(n)$ per entry).

---

### 5.2.2 0/1 Knapsack Problem

> [!warning] 🚨 Important
> 
> Greedy only gives optimal solution in **fractional** knapsack. For **0/1**, we use DP.

Let $ks[j, x]$ = optimal value for capacity $x$ with items $1 \dots j$.

$$ks[i, C] = \begin{cases} 0 & \text{if } i=0 \text{ or } C=0 \\ ks[i-1, C] & \text{if } w_i > C \\ \max \{ ks[i-1, C - w_i] + p_i, ks[i-1, C] \} & \text{Take / Don't Take} \end{cases}$$

**Complexity:**

- **Unique Calls:** $n \cdot C$ (Pseudo-polynomial).
    
- **Time:** $O(nC)$.
    

---

## 5.3 More Dynamic Programming Algorithms

`// Lecture 42a — 42e`

### 5.3.1 Subset Sum Problem

**Variant: Check if subset sum equals exactly K**

- $ss[i, S] = \text{True}$ if $S=0$.
    
- $ss[i, S] = ss[i-1, S - a_i] \lor ss[i-1, S]$ if $S > a_i$.
    

### 5.3.2 Coin Change Problem

**Find minimum number of notes to return.**

$$CC[i, S] = \min \{ 1 + CC[i, S - v_i], CC[i-1, S] \}$$

> [!info]
> 
> Uses same row $i$ because a coin can be reused (unbounded).

### 5.3.3 Floyd-Warshall Algorithm

**All-Pairs Shortest Path.**

- **Complexity:** $O(V^3)$.
    
- **Features:** Works on negative weights, detects negative cycles (diagonal entry becomes negative).
    

### 5.3.4 Travelling Salesman Problem (TSP)

> [!danger] NP-Hard
> 
> Minimum cost tour visiting every city once and returning to start. No polynomial algorithm is known.
> 
> **Complexity (DP):** $O(2^n \cdot n^2)$.

---

## Summary Table

|**Problem**|**TC (DP)**|**Table Size**|**Type**|
|---|---|---|---|
|**LCS**|$O(mn)$|$m \times n$|Sequence DP|
|**Matrix Chain**|$O(n^3)$|$n \times n$|Interval DP|
|**0/1 Knapsack**|$O(nC)$|$n \times C$|Pseudo-poly|
|**Subset Sum**|$O(nW)$|$n \times W$|Pseudo-poly|
|**Coin Change**|$O(nS)$|$n \times S$|Unbounded DP|
|**Floyd-Warshall**|$O(V^3)$|$V \times V$|All-pairs SP|
|**TSP**|$O(2^n \cdot n^2)$|—|NP-Hard|
