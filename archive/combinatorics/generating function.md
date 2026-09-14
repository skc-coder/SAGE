[[combinatorics/combinatorics]]
# Generating Functions

## What is a Generating Function?

A **generating function** transforms problems about sequences into problems about functions.

Given a sequence $a_0, a_1, a_2, a_3, \dots$, its **Ordinary Generating Function (OGF)** is:

$$G(x) = a_0 + a_1x + a_2x^2 + a_3x^3 + \dots = \sum_{k=0}^{\infty} a_k x^k$$

- $x$ is just a **placeholder** — not a variable you plug values into
- The **coefficient of $x^n$** in $G(x)$ is $a_n$
- GF is defined for **infinite sequences** only (finite sequences padded with $0, 0, 0, \dots$)

> **Open form:** $1 + x + x^2 + x^3 + \dots$
> **Closed form:** $\dfrac{1}{1-x}$

---

## Reading a GF → Sequence

$$G(S) = x^2 - x^4 + x^5 + x^6 + x^7 + \dots$$

Read off coefficients of each power:

| $x^0$ | $x^1$ | $x^2$ | $x^3$ | $x^4$ | $x^5$ | $x^6$ | $\dots$ |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------- |
| 0     | 0     | 1     | 0     | −1    | 1     | 1     | $\dots$ |
|       |       |       |       |       |       |       |         |

---

## Core Sequences & Their GFs

| Sequence                                                       | GF                     |
| -------------------------------------------------------------- | ---------------------- |
| $1, 1, 1, 1, \dots$                                            | $\dfrac{1}{1-x}$       |
| $1, a, a^2, a^3, \dots$                                        | $\dfrac{1}{1-ax}$      |
| $1, -1, 1, -1, \dots$                                          | $\dfrac{1}{1+x}$       |
| $1, 2, 3, 4, \dots$                                            | $\dfrac{1}{(1-x)^2}$   |
| $0, 1, 2, 3, \dots$                                            | $\dfrac{x}{(1-x)^2}$   |
| $1, 4, 9, 16, \dots$                                           | $\dfrac{1+x}{(1-x)^3}$ |
| $1, 0, 1, 0, 1, \dots$                                         | $\dfrac{1}{1-x^2}$     |
| $0, 0, 0, 1, 1, 1, \dots$                                      | $\dfrac{x^3}{1-x}$     |
| $\binom{m}{0}, \binom{m}{1}, \dots, \binom{m}{m}, 0, 0, \dots$ | $(1+x)^m$              |
|                                                                |                        |

---

## GATE Scope

- **GATE:** Ordinary GF only ✅
- **MTech:** Exponential GF
- **PhD:** Bell series, etc.

---

## Types of GF (for awareness)

- **OGF:** $G(x) = \sum a_i x^i$
- **EGF:** $G(x) = \sum \dfrac{a_i}{i!} x^i$
  - e.g. seq $1,1,1,\dots \to e^x$ ; seq $1,2,4,8,\dots \to e^{2x}$

EGF not important for GATE.

---

## Critical Note: GF ≠ Formula

$$G(n) \neq a_n \quad \text{(WRONG)}$$

$$G(0) = a_0 \quad \checkmark$$

$$G(1) = a_0 + a_1 + a_2 + \dots \neq a_1$$

**Exception:** You can evaluate $G(0)$ to get $a_0$.

---

## Extracting $a_n$ via Derivatives

$$G(x) \leftrightarrow a_0, a_1, a_2, a_3, \dots$$

$$G(0) = a_0$$
$$G'(0) = a_1$$
$$G''(0) = 2!\, a_2$$
$$G^{(n)}(0) = n!\, a_n \implies a_n = \frac{G^{(n)}(0)}{n!}$$

---

## Derivative Rule (Effect on Sequence)

Differentiating $G(x)$ shifts the sequence left and multiplies each term by its index:

$$G(x) \leftrightarrow a_0, a_1, a_2, a_3, \dots$$
$$G'(x) \leftrightarrow a_1, 2a_2, 3a_3, 4a_4, \dots$$

**Derivation of $\langle 1,2,3,4,\dots \rangle$:**

$$\frac{d}{dx}\left(\frac{1}{1-x}\right) = \frac{1}{(1-x)^2} \leftrightarrow 1, 2, 3, 4, \dots \checkmark$$

**Derivation of $\langle 0,1,2,3,\dots \rangle$:**

Multiply by $x$ to shift right:

$$x \cdot \frac{1}{(1-x)^2} = \frac{x}{(1-x)^2} \leftrightarrow 0, 1, 2, 3, \dots$$

**Derivation of $\langle 1,4,9,16,\dots \rangle$ (squares):**

$$\frac{d}{dx}\frac{x}{(1-x)^2} = \frac{1+x}{(1-x)^3} \leftrightarrow 1, 4, 9, 16, \dots$$

---

## AP, GP, AGP — Summation Formulas

### GP (finite)
$$S = a + ar + ar^2 + \dots + ar^{n-1} \quad (\text{n terms})$$
$$\sum S = \frac{a(r^n - 1)}{r - 1}$$

**Formula to remember:** $\text{first term} \times \dfrac{r^{\#terms} - 1}{r - 1}$

### GP (infinite)
$$\sum S = \frac{a}{1-r}, \quad |r| < 1$$

### AGP (infinite) — Very Important for GFs

$$S = a + (a+d)r + (a+2d)r^2 + \dots$$

$$\sum S = \frac{a}{1-r} + \frac{dr}{(1-r)^2}$$

where AP starts $a, a+d, a+2d, \dots$ and GP multiplier starts $1, r, r^2, \dots$

> ⚠️ For **finite AGP** → use the procedure (multiply by $r$, subtract), don't apply the formula directly.
> For **infinite AGP** → apply the formula, but check that the series is in the correct desired format first.

**Getting into desired AGP format:**

If the series isn't directly in AGP form (AP starts from 0, or GP factor doesn't start from term 1), factor out the extra terms first, then apply.

e.g. $\dfrac{1}{2} + \dfrac{2}{4} + \dfrac{3}{8} + \dots$: factor out $\dfrac{1}{2}$ → inside bracket is AGP with $a=1, d=1, r=\dfrac{1}{2}$ ✅

---

## Extended Binomial Coefficient

For $n \in \mathbb{R}$, $r \in \mathbb{W}$:

$$\binom{n}{r} = \frac{n(n-1)(n-2)\cdots(n-r+1)}{r!} \quad (r \text{ terms in numerator})$$

$$\binom{n}{0} = 1$$

> ⚠️ When $n \notin \mathbb{N}$: $\binom{n}{r} = \binom{n}{n-r}$ is **NOT allowed**.

**Examples:**

$$\binom{1/2}{2} = \frac{(\frac{1}{2})(\frac{1}{2}-1)}{2!} = \frac{-\frac{1}{4}}{2} = -\frac{1}{8}$$

$$\binom{-2}{4} = \frac{(-2)(-3)(-4)(-5)}{4!} = 5$$

$$\binom{-3}{3} = \frac{(-3)(-4)(-5)}{3!} = -10$$

---

## Key Identity: Negative Integer on Top

$$\binom{-n}{r} = (-1)^r \binom{n+r-1}{r} \quad (n \in \mathbb{N})$$

**Examples:**

$$\binom{-10}{7} = (-1)^7 \binom{16}{7} = -\binom{16}{7}$$

$$\binom{-5}{2} = (-1)^2 \binom{6}{2} = 15$$

---

## Extended Binomial Theorem

For $n \in \mathbb{R}$:

$$(1+x)^n = \sum_{r=0}^{\infty} \binom{n}{r} x^r$$

$$(1-x)^n = \sum_{r=0}^{\infty} \binom{n}{r} (-x)^r$$

When $n \in \mathbb{N}$: series terminates (all terms beyond $r=n$ are 0)
When $n \notin \mathbb{N}$ (e.g. $n = -3$): series is **infinite**

**Useful derived GFs:**

$$\frac{1}{(1-x)^2} = (1-x)^{-2} \leftrightarrow \text{coeff of } x^i = (-1)^i \binom{-2}{i} = 1+i$$

So: $g(i) = i+1$ ← GATE 2005 result

**For expressions like $(2+x)^n$:**

$$(2+x)^n = 2^n\left(1 + \frac{x}{2}\right)^n \quad \checkmark$$

Then apply extended binomial theorem to $\left(1 + \frac{x}{2}\right)^n$.

---

## Template: Solving Counting Problems with GFs

1. **Problem → GF** (model the constraints as a power series)
2. **Simplify GF** to closed form
3. **Extract coefficient of $x^n$** → that's your answer $a_n$

---

## GATE PYQs

### GATE 2005
$G(x) = \dfrac{1}{(1-x)^2}$, find $g(i)$ (coeff of $x^i$).

$= (1-x)^{-2}$, coeff of $x^i = (-1)^i\binom{-2}{i} = (-1)^i(-1)^i(1+i) = i+1$ ✅

### GATE 2016
Coeff of $x^{12}$ in $(x^3 + x^4 + x^5 + \dots)^3$?

Factor: $= x^9(1+x+x^2+\dots)^3$ → need coeff of $x^3$ in $\left(\dfrac{1}{1-x}\right)^3 = (1-x)^{-3}$

Coeff of $x^3$: $(-1)^3\binom{-3}{3} = -(-10) = \mathbf{10}$

### GATE 2017
$G(z) = \dfrac{1+z}{(1-z)^3}$, find $a_3 - a_0$.

$a_0 = G(0) = 1$

Split: $\dfrac{1}{(1-z)^3} + \dfrac{z}{(1-z)^3}$

$a_3 =$ coeff of $z^3$ in first part + coeff of $z^2$ in second part $= 10 + 6 = 16$

$a_3 - a_0 = 16 - 1 = \mathbf{15}$

### GATE 2018
$a_n = 2n+3$, find closed form GF.

Seq: $3, 5, 7, 9, \dots$ → infinite AGP with $a=3, d=2, r=x$

$$G(x) = \frac{3}{1-x} + \frac{2x}{(1-x)^2} = \frac{3-x}{(1-x)^2} \checkmark$$

### GATE 2022
$a_n = n+1$ if $n$ odd, $1$ if $n$ even.

Seq: $1, 2, 1, 4, 1, 6, 1, 8, \dots$

Split into even-indexed and odd-indexed terms:

Even part $A = 1 + x^2 + x^4 + \dots = \dfrac{1}{1-x^2}$

Odd part $B = 2x + 4x^3 + 6x^5 + \dots = 2x(1 + 2x^2 + 3x^4 + \dots) = \dfrac{2x}{(1-x^2)^2} + \dfrac{2x^3}{(1-x^2)^2}$

Wait — $2x \cdot \dfrac{1}{(1-x^2)^2}$ (using $1+2z+3z^2+\dots = \frac{1}{(1-z)^2}$ with $z=x^2$... see simplification in class)

Final answer: $\dfrac{x(1+x^2)}{(1-x^2)^2} + \dfrac{1}{1-x}$ → **Option A** ✅