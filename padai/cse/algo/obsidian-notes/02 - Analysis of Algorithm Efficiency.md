# 1. Time Complexity of Recursive Programs

> $T(n)$ = time taken by a program with input value $n$

https://gateoverflow.in/401465/go-classes-iiith-pgee-2026-mock-test-2-question-64?show=401465#q401465

dijstras algo with neg weights
https://www.youtube.com/watch?v=SgULLcChnxQ
---

## 1.1 Introduction to Recurrence Relations

```c
int fun(n) {
    if (n <= 1) return 1;       // cost: 1
    else return fun(n/2) + n;   // cost: T(n/2) + n
}
```

$$T(n) = T(n/2) + n \quad \text{(NOT } T(n) = T(n/2) + n\text{, i.e. cost of current level)}$$

> [!warning] **Common Mistake**
> 
> ```c
> return 2 * fun(n/2);   →   T(n) = T(n/2) + 1   // multiplying answer, NOT calling twice
> ```
> 
> ```c
> return fun(n/2) + fun(n/2);   →   T(n) = 2T(n/2) + 1   // actually calling twice!
> ```
> 
> These are **NOT** the same!

---

## Three Methods to Solve Recurrences

1. **Iteration / Repeated Substitution**
2. **Tree Method**
3. **Master Theorem**

---

## 1.1.1 Iteration Method (Repeated Substitution)

### Example 1 — $T(n) = T(n-1) + 1$

$$T(n) = T(n-1) + 1$$ $$= T(n-2) + 1 + 1 = T(n-2) + 2$$ $$= T(n-k) + k$$

If $T(1) = 1$, set $k = n-1$:

$$T(n) = T(1) + n - 1 = \boxed{n} \implies T(n) = \Theta(n)$$

---

### Example 2 — $T(n) = T(n/2) + n$

$$T(n) = T!\left(\tfrac{n}{2}\right) + n = T!\left(\tfrac{n}{4}\right) + \tfrac{n}{2} + n = T!\left(\tfrac{n}{2^k}\right) + \cdots + \tfrac{n}{2} + n$$

When $2^k = n$, i.e. $k = \log_2 n$:

$$T(n) = T(1) + n!\left[1 + \tfrac{1}{2} + \tfrac{1}{4} + \cdots + \tfrac{1}{2^{k-1}}\right] = T(1) + n \cdot \frac{2^k - 1}{2^{k-1}}$$

$$\therefore T(n) = 2n - 1 = \Theta(n)$$

---

## 1.1.2 Tree Method

> Use tree method when iteration becomes lengthy and confusing.

### Example — $T(n) = T!\left(\tfrac{n}{5}\right) + T!\left(\tfrac{4n}{5}\right) + n$

```
Level   Nodes (index)              Cost
  0         n                  →    n
  1       n/5,  4n/5           →    n
  2     n/25, 4n/25, 4n/25, 16n/25 →  n
  ...
  k     (4/5)^k · n            →    n
```

- **Shortest path** (always take $n/5$): stops when $(1/5)^k \cdot n = 1 \Rightarrow k = \log_5 n$
- **Longest path** (always take $4n/5$): stops when $(4/5)^k \cdot n = 1 \Rightarrow k = \log_{5/4} n$

$$n \log_5 n \leq T(n) \leq n \log_{5/4} n$$

Since $\log_{5/4} n = \frac{\log_2 n}{\log_2(5/4)} = \Theta(\log_2 n)$:

$$\therefore T(n) = \Theta(n \log n)$$

> [!important] **Tree Method Rule** Always find **lower bound** (shortest leaf path) and **upper bound** (longest leaf path), then conclude $\Theta(f(n))$.

---

### Example — $T(n) = T!\left(\tfrac{n}{3}\right) + T!\left(\tfrac{2n}{3}\right) + n^2$

Each level costs:

$$n^2 + \frac{5n^2}{9} + \left(\frac{5}{9}\right)^2 n^2 + \cdots$$

$$T(n) = n^2\left(1 + \frac{5}{9} + \left(\frac{5}{9}\right)^2 + \cdots\right) = n^2 \cdot \frac{1}{1 - 5/9} = \Theta(n^2)$$

---

### Geometric Series Formula (Essential!)

$$1 + c + c^2 + \cdots + c^n = \sum_{i=1}^{n} c^i = \begin{cases} \Theta(1) & \text{if } c < 1 \ \Theta(n) & \text{if } c = 1 \ \Theta(c^n) & \text{if } c > 1 \end{cases}$$

---

### General Solution for $T(n) = aT!\left(\tfrac{n}{b}\right) + cn^k$

Let $m = \log_b n$ (depth of tree):

$$T(n) = cn^k + ac!\left(\tfrac{n}{b}\right)^k + a^2c!\left(\tfrac{n}{b^2}\right)^k + \cdots + a^{m-1}c!\left(\tfrac{n}{b^{m-1}}\right)^k$$

$$T(n) = cn^k!\left(1 + \tfrac{a}{b^k} + \tfrac{a^2}{b^{2k}} + \cdots + \tfrac{a^{m-1}}{b^{k(m-1)}}\right)$$

Using GP formula:

$$\boxed{T(n) = \Theta!\left(n^k \cdot g(n)\right) \quad \text{where } g(n) = \begin{cases} 1 & \text{if } a < b^k \ \log_b n & \text{if } a = b^k \ \left(\tfrac{a}{b^k}\right)^{\log_b n} & \text{if } a > b^k \end{cases}}$$

---

## 1.2 Master Theorem

> **Theorem 4.1 (Master Theorem)** Let $a \geq 1$, $b > 1$ be constants, $f(n)$ a function, and $T(n) = aT(n/b) + f(n)$. Compare $f(n)$ with $n^{\log_b a}$:

| Case  | Condition                                                                                                    | Result                               |
| ----- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| **1** | $f(n) = O(n^{\log_b a - \varepsilon})$ for some $\varepsilon > 0$                                            | $T(n) = \Theta(n^{\log_b a})$        |
| **2** | $f(n) = \Theta(n^{\log_b a})$                                                                                | $T(n) = \Theta(n^{\log_b a} \log n)$ |
| **3** | $f(n) = \Omega(n^{\log_b a + \varepsilon})$ for some $\varepsilon > 0$, and $af(n/b) \leq cf(n)$ for $c < 1$ | $T(n) = \Theta(f(n))$                |

### ⚠️ Polynomial Greater — Critical Requirement

$f(n)$ must be **polynomially greater** than $n^{\log_b a}$ — not just asymptotically.

**Example:** $T(n) = 2T(n/2) + n \log n$

$$n^{\log_2 2} = n^1 = n \qquad \text{Is } n \log n \text{ polynomially greater than } n?$$

$$\frac{n \log n}{n} = \log n \not> 1 \quad \Rightarrow \text{ NOT polynomially greater. Cannot apply Master Theorem!}$$

> [!note] If instead of $n \log n$ we had $n^2 \log n$, then $\frac{n^2 \log n}{n} = n \log n > 1$ — polynomially greater ✓

**Note on $2^n$ and $n!$:** $2^n > n$ is a polynomial, so $2^n$ is polynomially greater. Same for $n!$

---

### Proof Sketch (Tree Method)

```
T(n) = f(n) + a·f(n/b) + a²·f(n/b²) + ... + a^(k-1)·f(n/b^(k-1))   [k = log_b n]
```

- If $f(n) > a^{\log_b n}$: series is **decreasing** → $T(n) = \Theta(f(n))$ ← Case 3
- If $f(n) < a^{\log_b n}$: series is **increasing** → $T(n) = \Theta(a^{\log_b n}) = \Theta(n^{\log_b a})$ ← Case 1
- If $f(n) = a^{\log_b n}$: all terms equal → sum with GP → $T(n) = \Theta(f(n) \cdot \log_b n)$ ← Case 2

---

## 1.2.1 Generalized Master Theorem

> Handles cases where $f(n) = \Theta(n^{\log_b a})$ but with logarithmic factors.

**Extended Case 2** (replaces the simple Case 2):

$$\text{If } f(n) = \Theta(n^{\log_b a} \cdot \log^k n) \text{ with } k \geq 0 \implies T(n) = \Theta(n^{\log_b a} \cdot \log^{k+1} n)$$

**Sub-cases for Case 2:**

|Condition|Result|
|---|---|
|$f(n) = \Theta!\left(\tfrac{n^{\log_b a}}{\log n}\right)$|$T(n) = \Theta(n^{\log_b a} \log \log n)$|
|$f(n) = \Theta!\left(\tfrac{n^{\log_b a}}{\log^p n}\right)$ with $p \geq 2$|$T(n) = \Theta(n^{\log_b a})$|

---

### Example — $T(n) = 2T(n/2) + \tfrac{n}{\log n}$, $T(2) = 1$

Using substitution (since master theorem fails here):

$$T(n) = 2^k T!\left(\tfrac{n}{2^k}\right) + \sum_{i=0}^{k-1} \frac{n}{\log(n/2^i)} \quad [k = \log n - 1]$$

$$T(n) = \sum_{i=0}^{\log n} \frac{n}{\log n - i} = n \sum_{l=1}^{\log n} \frac{1}{l} = \Theta(n \log \log n)$$

---

### Example — $T(n) = 2T(n/2) + \tfrac{n}{(\log n)^2}$, $T(2) = 1$

$$T(n) = \sum_{i=1}^{\log n} \frac{n}{i^2} = n \sum_{i=1}^{\log n} \frac{1}{i^2} \approx n \cdot \frac{\pi^2}{6} = \Theta(n)$$

---

## Extended Master Theorem (Full Form)

> Applies to: $T(n) = aT!\left(\tfrac{n}{b}\right) + f(n)$ where $a \geq 1$, $b > 1$, $f(n)$ is asymptotically **positive**.

|Case|Condition|Result|
|---|---|---|
|**1**|$f(n) = O(n^{\log_b a - \varepsilon})$|$T(n) = \Theta(n^{\log_b a})$|
|**2a**|$f(n) = \Theta(n^{\log_b a} \log^k n)$, $k \geq 0$|$T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$|
|**2b**|$f(n) = \Theta!\left(\tfrac{n^{\log_b a}}{\log n}\right)$|$T(n) = \Theta(n^{\log_b a} \log \log n)$|
|**2c**|$f(n) = \Theta!\left(\tfrac{n^{\log_b a}}{\log^p n}\right)$, $p \geq 2$|$T(n) = \Theta(n^{\log_b a})$|
|**3**|$f(n) = \Omega(n^{\log_b a + \varepsilon})$|$T(n) = \Theta(f(n))$|

---

### Example — $T(n) = 4T(n/2) + \tfrac{n}{(\log n)^2}$

$$n^{\log_2 4} = n^2 \qquad \frac{n}{(\log n)^2} \ll n^2$$

$$\frac{n}{(\log n)^2} \text{ vs } n^2 \quad\Rightarrow\quad 1 < n \log n \text{ (polynomially greater)}$$

$$f(n) = O(n^{2-\varepsilon}) \implies T(n) = \Theta(n^2)$$

---

## 1.2.2 Problems Master Theorem Cannot Solve

> [!warning] **Master theorem requires:** $a \geq 1$ constant, $b > 1$ constant, $f(n)$ positive

|Example|Issue|
|---|---|
|$T(n) = \sqrt{n}, T(n/2) + n$|$a = \sqrt{n}$ is not constant|
|$T(n) = 2T(n/\log n) + n^2$|$b$ is not constant|
|$T(n) = \tfrac{1}{2}T(n/2) + n^2$|$a = 1/2 < 1$|
|$T(n) = 2T(n/(3/4)) + n$|$b = 3/4 < 1$|
|$T(n) = 3T(n/2) - n$|$f(n) = -n$ is not positive|
|$T(n) = 25T(n/2) + n\sin n$|Trigonometry not allowed|
|$T(n) = T(n/2) + T(n/3) + n$|$a$ and $b$ are not fixed (two subproblems of different sizes)|

---

## 1.3 Change of Variable

> Replace existing variable with a new one to simplify the recurrence.

### Example 1 — $T(n) = T(\sqrt{n}) + \sqrt{n}$

Let $n = 2^m$, so $T(2^m) = T(2^{m/2}) + 2^{m/2}$. Let $S(m) = T(2^m)$:

$$S(m) = S(m/2) + 2^{m/2}$$

Hmm, still complex. Alternatively:

$$S(m) = \Theta(2^{m/2} \cdot \log m) \implies T(n) = \Theta(\sqrt{n} \cdot \log \log n)$$

---

### Example 2 — $T(n) = T!\left(\tfrac{n}{161}\right)^{161} \cdot n$

Take $\log$ on both sides:

$$\log T(n) = 161 \cdot \log T!\left(\tfrac{n}{161}\right) + \log n$$

Let $S(n) = \log T(n)$:

$$S(n) = 161 \cdot S(n/161) + \log n$$

By master theorem: $n^{\log_{161} 161} = n^1 = n > \log n \implies S(n) = \Theta(n)$

$$\boxed{T(n) = \Theta(e^n) = O(2^n)}$$

---

### Example 3 — $T(n) = \sqrt{n}, T(\sqrt{n}) + 100n$

Divide by $n$:

$$\frac{T(n)}{n} = \frac{T(\sqrt{n})}{\sqrt{n}} + 100$$

Let $S(n) = T(n)/n$:

$$S(n) = S(\sqrt{n}) + 100$$

Let $n = 2^m$: $S(2^m) = S(2^{m/2}) + 100$. Let $R(m) = S(2^m)$:

$$R(m) = R(m/2) + 100 \implies R(m) = \Theta(\log m)$$

Back-substituting: $m = \log n$, so $R(m) = \Theta(\log \log n)$

$$S(n) = \Theta(\log \log n) \implies T(n) = n \cdot S(n)$$

$$\boxed{T(n) = \Theta(n \log \log n)}$$

---

## 🔁 Summary Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                   RECURRENCE SOLVING GUIDE                      │
├────────────────────────┬────────────────────────────────────────┤
│ T(n) = T(n-1) + 1      │  Θ(n)                                  │
│ T(n) = T(n-1) + n      │  Θ(n²)                                 │
│ T(n) = 2T(n-1) + 1     │  Θ(2ⁿ)                                 │
│ T(n) = T(n/2) + 1      │  Θ(log n)                              │
│ T(n) = T(n/2) + n      │  Θ(n)                                  │
│ T(n) = 2T(n/2) + 1     │  Θ(n)                                  │
│ T(n) = 2T(n/2) + n     │  Θ(n log n)                            │
│ T(n) = 2T(n/2) + n²    │  Θ(n²)                                 │
│ T(n) = T(n/3)+T(2n/3)+n│  Θ(n log n)  [tree method]             │
└────────────────────────┴────────────────────────────────────────┘
```

---

## 🔗 Related Topics

- [[Master Theorem]]
- [[Divide and Conquer]]
- [[2.3.4 - Select Algorithm]]
- [[2.4.5 - Counting Sort & Radix Sort]]
- [[Asymptotic Notation]]

---

_Source: Go Classes — goclasses.in | Lectures 2a, 3d, 4a–4c, 5a–5d, 6a_