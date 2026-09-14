# Limit, Continuity & Differentiability — Types of Discontinuity, Algebra of Continuity

**Topic:** JEE PCM > Calculus > Limits, Continuity & Differentiability **Source:** Class Notes 07 & 08 (handwritten, JEE Mains/Advanced PYQ-based lecture) — _coaching institute name not stated in source, flagging as unsure_ **Tags:** #jee #maths #calculus #limits #continuity #discontinuity **Links:** [[Calculus MOC]] | [[Limit Continuity Differentiability 06]] _(guessed — link to previous lecture if it exists in your vault)_

---

> [!info] Overview 
> This note covers two consecutive lectures on Limits & Continuity: recap of the continuity definition, a large PYQ set on evaluating limits/continuity constants, the three types of discontinuity (removable and non-removable), a checklist of "suspicious points" where continuity must be checked, the algebra of continuity (how continuous/discontinuous functions combine), and a self-practice DIBY problem set.

---

## 1. Recap — Continuity at a Point

**Flowchart (Class 07 recap):**

```
Continuity at x = a
        │
        ├── LHL  (Left Hand Limit)
        ├── RHL  (Right Hand Limit)
        └── f(a) (value of function)
                │
                ▼
     {LHL, RHL, f(a)} must be
        EQUAL and FINITE
                │
                ▼
        f is continuous at x = a
```

So continuity at a point requires three numbers — $\displaystyle\lim_{x\to a^-} f(x)$, $\displaystyle\lim_{x\to a^+} f(x)$, and $f(a)$ — to all exist, be finite, and be equal.

---

## 2. Question Practice Set 1 (Limits & Continuity)

### 2.1 Piecewise limit with floor/fractional part

> [!example] JEE Mains 2022 **Question:** Let $[t]$ denote the greatest integer $\leq t$ and ${t}$ denote the fractional part of $t$. Find the integral value of $\alpha$ for which the left hand limit of $$ f(x) = [1+x] + \dfrac{\alpha^{2[x]+{x}} + [x] - 1}{2[x]+{x}} $$ at $x = 0$ equals $\alpha - \dfrac{4}{3}$.
> 
> **Approach:** For $x \to 0^-$: $[x] = -1$, and ${x} = x - [x] = x+1$.
> 
> $$ \begin{aligned} \lim_{x\to 0^-}\left([1+x] + \dfrac{\alpha^{2[x]+{x}} + [x] - 1}{2[x]+{x}}\right) &= 0 + \dfrac{\alpha^{-2+(x+1)} - 1 - 1}{2(-1)+(x+1)} \ &= \lim_{x\to 0^-}\dfrac{\alpha^{x-1} - 2}{x-1} \ &= \dfrac{\alpha^{-1} - 2}{-1} = 2 - \dfrac{1}{\alpha} \end{aligned} $$
> 
> Setting this equal to $\alpha - \dfrac{4}{3}$:
> 
> $$ \begin{aligned} 2 - \dfrac{1}{\alpha} &= \alpha - \dfrac{4}{3} \ \dfrac{2\alpha-1}{\alpha} &= \dfrac{3\alpha-4}{3} \ 6\alpha - 3 &= 3\alpha^2 - 4\alpha \ 3\alpha^2 - 10\alpha + 3 &= 0 \ (3\alpha-1)(\alpha-3) &= 0 \end{aligned} $$
> 
> **Answer:** $\alpha = \boxed{3}$ (integral value; $\alpha = \tfrac13$ rejected as non-integral)

### 2.2 Paragraph-type question (two parts) — limit-defined function

Both parts below share the same setup:

$$ f(x) = \lim_{n\to\infty} \dfrac{x^2 + 2(x+1)^{2n}}{(x+1)^{2n+1} + x^2 + 1}, \quad n\in\mathbb{N}, \qquad g(x) = \tan\left(\dfrac{1}{2}\sin^{-1}\left{\dfrac{2f(x)}{1+f^2(x)}\right}\right) $$

**Finding $f(x)$ first** (key trick — behavior of $(x+1)^{2n}$ as $n\to\infty$):

$$ \begin{aligned} |x+1| &> 1 ;\Rightarrow; (x+1)^{2n}\to\infty \ |x+1| &< 1 ;\Rightarrow; (x+1)^{2n}\to 0 \end{aligned} $$

Dividing numerator and denominator by $(x+1)^{2n}$ gives the piecewise result:

$$ f(x) = \begin{cases} \dfrac{2}{x+1}, & x < -2 \text{ or } x>0 \[6pt] \dfrac{x^2}{x^2+1}, & -2<x<0 \[6pt] \dfrac{x^2+2}{x^2+x+2}, & x=0,-2 \end{cases} $$

**Simplifying $g(x)$:** substitute $f(x) = \tan\theta$. Since $\dfrac{2\tan\theta}{1+\tan^2\theta} = \sin 2\theta$,

$$ g(x) = \tan\left(\dfrac{1}{2}\sin^{-1}(\sin 2\theta)\right) = \tan\theta = f(x) $$

(valid as long as $2\theta \in \left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right)$, i.e. $\theta \in \left(-\tfrac{\pi}{4},\tfrac{\pi}{4}\right)$, so $g(x)=f(x)$ on the domain considered here).

> [!example] Sub-question (A) **Question:** If $x \in (-2,0)$, find the range of $g(x)$.
> 
> **Approach:** On $(-2,0)$, $g(x) = f(x) = \dfrac{x^2}{1+x^2} = 1 - \dfrac{1}{1+x^2}$.
> 
> $$ \begin{aligned} x \in (-2,0) &\Rightarrow x^2 \in (0,4) \Rightarrow x^2+1 \in (1,5) \ &\Rightarrow \dfrac{1}{x^2+1} \in \left(\dfrac{1}{5},1\right) \ &\Rightarrow 1-\dfrac{1}{x^2+1} \in \left(0,\dfrac{4}{5}\right) \end{aligned} $$
> 
> **Answer:** $\boxed{\left(0,\dfrac{4}{5}\right)}$

> [!example] Sub-question (B) **Question:** Evaluate $\displaystyle\lim_{x\to -3} \dfrac{\sin(x+3)\cdot g(x)}{x^2+4x+3}$.
> 
> **Approach:** Near $x=-3$, we're outside $(-2,0)$, so $f(x) = g(x) = \dfrac{2}{x+1}$, giving $g(-3) = -1$. Factor the denominator: $x^2+4x+3 = (x+3)(x+1)$.
> 
> $$ \lim_{x\to -3} \dfrac{\sin(x+3)}{(x+3)} \cdot \dfrac{g(x)}{(x+1)} = 1 \times \dfrac{-1}{-2} = \dfrac{1}{2} $$
> 
> **Answer:** $\boxed{\dfrac{1}{2}}$

### 2.3 Composite function limit

> [!example] JEE Mains 2023 **Question:** Let $f,g,h: \mathbb{R}\to\mathbb{R}$ be defined by $$ f(x) = \begin{cases} \dfrac{x}{|x|}, & x\neq 0 \ 1, & x=0\end{cases}, \quad g(x) = \begin{cases} \dfrac{\sin(x+1)}{x+1}, & x\neq -1 \ 1, & x=-1\end{cases}, \quad h(x) = 2[x]-f(x) $$ Find $\displaystyle\lim_{x\to 1} g(h(x-1))$.
> 
> **Approach:** $$ f(0^+) = \dfrac{x}{|x|}=1, \qquad f(0^-)=\dfrac{x}{-x}=-1 $$
> 
> $$ \begin{aligned} h(0^+) &= 2[0^+] - f(0^+) = 0 - 1 = -1 \ h(0^-) &= 2[0^-] - f(0^-) = -2 - (-1) = -1 \end{aligned} $$
> 
> As $x\to 1$, the argument $x-1 \to 0$, so both one-sided limits feed into $h \to -1$, and $g(-1)=1$ (by direct definition).
> 
> $$ \lim_{x\to 1^+} g(h(x-1)) = g(-1) = 1, \qquad \lim_{x\to 1^-} g(h(x-1)) = g(-1) = 1 $$
> 
> **Answer:** $\boxed{1}$ (Option A)

---

## 3. Continuity — Section Marker

The source explicitly marks a new section header **"CONTINUITY"** here (page 9), separating the pure-limit practice above from continuity-specific problems below.

### 3.1 Finding constants for continuity

> [!example] IIT-JEE 1994 **Question:** If $$ f(x) = \begin{cases} (1+|\sin x|)^{a/|\sin x|}, & -\dfrac{\pi}{6}<x<0 \ b, & x=0 \ e^{\tan 2x/\tan 3x}, & 0<x<\dfrac{\pi}{6} \end{cases} $$ find $a$ and $b$ if $f(x)$ is continuous at $x=0$.
> 
> **Approach:** Need $LHL = RHL = f(0)$, i.e. $e^a = e^{2/3} = b$.
> 
> **RHL:** $$ \lim_{x\to 0^+} e^{\tan 2x/\tan 3x} = e^{\lim_{x\to0^+}\frac{\tan 2x}{2x}\cdot\frac{3x}{\tan 3x}\cdot\frac{2x}{3x}} = e^{2/3} $$
> 
> **LHL:** for $x\to0^-$, $|\sin x| = -\sin x$, so $$ \lim_{x\to 0^-}(1-\sin x)^{a/(-\sin x)} = e^{\lim_{x\to0^-}\left(\frac{-a}{\sin x}\right)(-\sin x)} = e^{a} $$
> 
> **Answer:** $\boxed{a = \dfrac{2}{3}, ; b = e^{2/3}}$

### 3.2 Challenger Question (multi-constant continuity)

> [!example] Challenger Question **Question:** Let $$ f(x) = \begin{cases} \dfrac{\alpha(1-x\sin x)+\beta\cos x+5}{x^2}, & x<0 \ 3, & x=0 \ \left(1+\dfrac{\gamma x+\delta x^3}{x^2}\right)^{1/x}, & x>0 \end{cases} $$ If $f(x)$ is continuous at $x=0$, find $\alpha^2+\beta^2+\gamma^2+e^{2\delta}$.
> 
> _(Marked as homework in Class 07, fully worked out in Class 08.)_
> 
> **Approach — Left side ($x\to 0^-$):** Since $f(0)=3$, and the expression is $\tfrac{0}{0}$ as $x\to0$, first the numerator must vanish at $x=0$: $$ \alpha + \beta + 5 = 0 $$ Applying L'Hôpital's rule twice (since it's still $\tfrac00$ after one differentiation): $$ \begin{aligned} \lim_{x\to 0^-}\dfrac{\alpha(-\sin x - x\cos x) - \beta\sin x}{2x} &= \lim_{x\to0^-}\dfrac{\alpha(-\cos x - \cos x + x\sin x) - \beta\cos x}{2} \ &= \dfrac{\alpha(-2)-\beta}{2} = 3 \end{aligned} $$ So $2\alpha+\beta = -6$. Combined with $\alpha+\beta=-5$: $$ \alpha = -1, \quad \beta = -4 $$
> 
> **Approach — Right side ($x\to 0^+$):** As $\tfrac1x \to +\infty$, for the limit to be finite the inner bracket exponent's "extra" part must vanish appropriately: $$ \lim_{x\to0^+}\left(\dfrac{\gamma}{x}+\delta x\right) \text{ must behave so that } \gamma = 0 $$ Then $$ \lim_{x\to0^+}(1+\delta x)^{1/x} = e^{\delta} = 3 ;\Rightarrow; e^{2\delta} = 9 $$
> 
> **Final computation:** $$ \alpha^2+\beta^2+\gamma^2+e^{2\delta} = (-1)^2+(-4)^2+0^2+9 = 1+16+0+9 = 26 $$
> 
> **Answer:** $\boxed{26}$

### 3.3 More continuity-constant problems

> [!example] JEE Mains 2024 **Question:** For $a,b>0$, let $$ f(x) = \begin{cases} \dfrac{\tan((a+1)x)+b\tan x}{x}, & x<0 \ 3, & x=0 \ \dfrac{\sqrt{ax+b^2x^2}-\sqrt{ax}}{b\sqrt{ax}\sqrt{x}}, & x>0 \end{cases} $$ be continuous at $x=0$. Find $\dfrac{b}{a}$.
> 
> **Approach — LHL (form $\tfrac00$, apply L'Hôpital):** $$ \lim_{x\to0^-}\dfrac{\tan((a+1)x)+b\tan x}{x} = \lim_{x\to0^-}\left[(a+1)\sec^2((a+1)x)+b\sec^2 x\right] = a+1+b $$ Setting $LHL = f(0) = 3$: $;a+1+b=3 \Rightarrow a+b=2$.
> 
> **Approach — RHL:** $$ \begin{aligned} \lim_{x\to0^+}\dfrac{\sqrt{ax}\left[\left(1+\dfrac{b^2}{a}x\right)^{1/2}-1\right]}{b\sqrt{ax},x} &= \dfrac{1}{b}\cdot\lim_{x\to0^+}\dfrac{\frac{b^2}{a}x\cdot\frac12}{x} \ &= \dfrac{b^2}{2ab} = \dfrac{b}{2a} \end{aligned} $$ Setting $RHL = 3$: $;\dfrac{b}{2a}=3 \Rightarrow \dfrac{b}{a}=6$.
> 
> **Answer:** $\boxed{6}$ (Option D)

> [!example] JEE Mains 2024 **Question:** Consider $$ f(x) = \begin{cases} \dfrac{a(7x-12-x^2)}{b|x^2-7x+12|}, & x<3 \ 2^{\sin(x-3)/(x-[x])}, & x>3 \ b, & x=3 \end{cases} $$ where $[x]$ is the greatest integer function. If $S$ is the set of ordered pairs $(a,b)$ for which $f$ is continuous at $x=3$, find $n(S)$.
> 
> **Approach — RHL:** $$ \lim_{x\to3^+} 2^{\sin(x-3)/(x-3)} = 2^{1} = 2 \quad\text{(since } [x]=3 \text{ just above 3, so } x-[x]=x-3\text{)} $$
> 
> **Approach — LHL:** Note $7x-12-x^2 = -(x^2-7x+12)$, and just below $x=3$, $x^2-7x+12>0$ so $|x^2-7x+12| = x^2-7x+12$: $$ \lim_{x\to3^-}\dfrac{a\cdot[-(x^2-7x+12)]}{b(x^2-7x+12)} = \dfrac{-a}{b} $$
> 
> **Matching all three:** $LHL = f(3) = RHL \Rightarrow \dfrac{-a}{b} = b = 2$ $$ b=2, \qquad \dfrac{-a}{b}=b \Rightarrow a = -b^2 = -4 $$ $S = {(-4,2)}$
> 
> **Answer:** $\boxed{n(S)=1}$ (Option D)

> [!example] JEE Mains 2022 **Question:** $$ f(x) = \begin{cases} \dfrac{\ln(1+5x)-\ln(1+\alpha x)}{x}, & x\neq 0 \ 10, & x=0 \end{cases} $$ is continuous at $x=0$. Find $\alpha$.
> 
> **Answer:** $\boxed{\alpha = -5}$ (Option D) — _cross-referenced in source as DIBY problem A; solved answer only, no intermediate steps given._

> [!example] JEE Mains 2025 **Question:** $$ f(x) = \begin{cases} \dfrac{2}{x}\left{\sin(k_1+1)x + \sin(k_2-1)x\right}, & x<0 \ 4, & x=0 \ \dfrac{2}{x}\ln\left(\dfrac{2+k_1x}{2+k_2x}\right), & x>0 \end{cases} $$ is continuous at $x=0$. Find $k_1^2+k_2^2$.
> 
> **Answer:** $\boxed{10}$ (Option B) — _cross-referenced in source as DIBY problem B; answer only._

> [!example] JEE Mains 2022 **Question:** $f:\mathbb{R}\to\mathbb{R}$ defined by $$ f(x) = \lim_{n\to\infty}\dfrac{\cos(2\pi x)-x^{2n}\sin(x-1)}{1+x^{2n+1}-x^{2n}} $$ is continuous for all $x$ in which set?
> 
> _(Marked homework in Class 07; fully worked in Class 08.)_
> 
> **Approach:** Split by the behavior of $x^{2n}$ as $n\to\infty$:
> 
> - **$|x|<1$:** $x^{2n}\to 0 \Rightarrow f(x) = \cos(2\pi x)$
> - **$|x|=1$:** $x^{2n}=1 \Rightarrow f(x) = \cos(2\pi x)$ as well (checked directly)
> - **$|x|>1$**, i.e. $x\in(-\infty,-1)\cup(1,\infty)$: divide numerator & denominator by $x^{2n}$:
> 
> $$ \dfrac{x^{2n}\left(\dfrac{\cos 2\pi x}{x^{2n}} - \sin(x-1)\right)}{x^{2n}\left(\dfrac{1}{x^{2n}}+x-1\right)} ;\longrightarrow; \dfrac{-\sin(x-1)}{x-1} $$
> 
> So overall: $$ f(x) = \begin{cases} \cos(2\pi x), & x\in[-1,1] \ \dfrac{-\sin(x-1)}{x-1}, & x\in(-\infty,-1)\cup(1,\infty) \end{cases} $$
> 
> Checking the joins at $x=\pm1$: the two pieces need to be checked for a possible mismatch at $x=-1$ (this is where the removable-type discontinuity from $\frac{\sin(x-1)}{x-1}$ near $x=-1$ doesn't match $\cos(2\pi x)$ smoothly) — this is why $x=-1$ is excluded.
> 
> **Answer:** $\boxed{\mathbb{R}-{-1,1}}$ (Option B)

---

## 4. Types of Discontinuity

> [!info] Why this matters Once a limit fails to give $LHL=RHL=f(a)$, the _type_ of failure tells you whether the function can be "patched" (removable) or not (non-removable).

### 4.1 Overview Diagram

```
TYPES OF DISCONTINUITY
│
├── Removable Type   (limit EXISTS: LHL = RHL = finite, but ≠ f(a) or f(a) undefined)
│     ├── 1. Missing Point Discontinuity
│     └── 2. Isolated Point Discontinuity
│
└── Non-Removable Type   (limit DOES NOT EXIST)
      ├── 1. Finite Type      (LHL ≠ RHL, both finite)
      ├── 2. Infinite Type    (LHL or RHL → ±∞)
      └── 3. Oscillatory Type (limit oscillates, no fixed value)
```

### 4.2 Removable Type

**1. Missing Point Discontinuity** — the limit exists but $f(a)$ is simply not defined.

Example: a straight line with a hole at $(2,3)$. $$ LHL = 3, \quad RHL = 3, \quad f(2) \text{ is not defined (n.d.)} $$

**2. Isolated Point Discontinuity** — the limit exists but $f(a)$ takes a _different_ value than the limit.

Example: same line with a hole at $(2,3)$ but a solid dot placed at $(2,4)$. $$ LHL = 3, \quad RHL = 3, \quad f(2) = 4 \quad\Rightarrow\quad LHL = RHL \neq f(a) $$

### 4.3 Non-Removable Type

**1. Finite Type** — $LHL \neq RHL$, but both are finite.

Example: a jump at $x=2$ with $LHL=4$, $RHL=3$.

$$ \text{Jump of discontinuity} = |LHL - RHL| = |3-4| = 1 $$

**2. Infinite Type** — either $LHL$ or $RHL$ (or both) tends to $\pm\infty$ (vertical asymptote behavior).

Example: $RHL = 4$, $LHL = +\infty$ at $x=2$.

**3. Oscillatory Type** — the limit oscillates between values with no single limiting value.

$$ \lim_{x\to 0}\sin\left(\dfrac{1}{x}\right) $$

$$ \lim_{x\to0^+}\sin\left(\dfrac{1}{0^+}\right) = \sin(+\infty) \in [-1,1], \qquad \lim_{x\to0^-}\sin\left(\dfrac{1}{0^-}\right) = \sin(-\infty) \in [-1,1] $$

> [!note] Not every oscillation is discontinuous $\displaystyle\lim_{x\to0} x\sin\left(\dfrac{1}{x}\right) = (0^+)\cdot[-1,1] = 0$ — here the oscillating factor gets **squeezed** to zero by the vanishing $x$, so the overall limit _does_ exist (Squeeze Theorem in action).

**Fractional-part oscillatory example:**

$$\lim_{x\{to} 1^+}\left{\dfrac{1}{x-1}\right} = \left{\dfrac{1}{0^+}\right} = {+\infty} \in [0,1) \quad\text{(fails to exist — f.p.f. oscillates)}$$

---

## 5. Suspicious Points — Where to Check Continuity

> [!info] The core problem An interval has infinitely many points — you obviously can't check continuity everywhere by brute force. This checklist tells you _exactly_ which points are worth checking.

### 5.1 The Checklist

| #   | Type of point                                | What to check                                                              |
| :-- | :------------------------------------------- | :------------------------------------------------------------------------- |
| 1   | Where the definition of the function changes | Piecewise breakpoints, e.g. $x=a$ in $f(x)={\ldots, x\geq a; \ldots, x<a}$ |
| 2   | $[f(x)]$ or ${f(x)}$ (floor/fractional part) | Values of $x$ where $f(x)$ becomes an **integer**                          |
| 3   | $\text{sgn}(f(x))$ or $                      | f(x)                                                                       |
| 4   | Where a denominator vanishes                 | $h(x) = \dfrac{f(x)}{g(x)} \Rightarrow$ check where $g(x)=0$               |
| 5   | Endpoints of the given interval/domain       | Boundary points of the interval                                            |

### 5.2 Worked Mini-Examples

**Example 1:** $$ f(x) = \begin{cases} x^2-3x+2, & x\geq 1 \ 5-3x, & x<1\end{cases} $$ Check at $x=1$: $LHL = 5-3(1)=2$, $RHL = 1-3+2=0$, $f(1)=0$. Since $LHL\neq RHL$, **discontinuous at $x=1$**.

**Example 2:** $f(x) = [\sqrt{x}]$

$\sqrt{x} = \text{integer} \Rightarrow x = 0,1,4,9,\ldots$ — these are the true suspicious points (not simply $x=0,1,2,3,4,5$).

**Example 3:** $f(x) = {x^2+1}$, $x\in(0,2)$

$x^2+1 = \text{integer} \Rightarrow x = 1, \sqrt2, \sqrt3$ (within the interval).

### 5.3 Detailed Practice Problems

> [!example] JEE Mains 2023 **Question:** $f(x) = [x^2-x] + |-x+[x]|$. Determine continuity at $x=0$ and $x=1$.
> 
> _(Marked homework in Class 07; fully worked in Class 08.)_
> 
> **Approach — at $x=0$:** $f(0) = 0$.
> 
> $$ \begin{aligned} LHL = \lim_{x\to0^-}\left([x^2-x] + |-x+[x]|\right) &: ; [x^2-x]\to -1 \text{ (since for } x\to0^-, ; x^2-x \to 0^+ \text{ from below zero... evaluated as} -1) \ &= -1 + |-x-1| \to 1 \end{aligned} $$
> 
> $$ RHL = \lim_{x\to0^+}\left([x^2-x]+|-x+[x]|\right) : [x^2-x]\to -1, ; [x]\to0 ;\Rightarrow; -1+|-x+0| \to -1 $$
> 
> Since $LHL(=1) \neq RHL(=-1)$, **discontinuous at $x=0$**.
> 
> **Approach — at $x=1$:** $f(1)=0$.
> 
> $$ LHL = \lim_{x\to1^-}\left([x^2-x]+|-x+[x]|\right) = -1 + |-x| \to -1+1 = 0 $$
> 
> $$ RHL = \lim_{x\to1^+}\left([x^2-x]+|-x+[x]|\right) = 0 + |-x+1| \to 0 $$
> 
> Since $LHL = RHL = f(1) = 0$, **continuous at $x=1$**.
> 
> **Answer:** $\boxed{\text{Continuous at } x=1 \text{ but not at } x=0}$ (Option C)

> [!example] JEE Mains 2023 **Question:** Let $[x]$ be the greatest integer $\leq x$. Find the number of points in $(-2,1)$ where $f(x) = |[x]| + \sqrt{x-[x]} = |[x]|+\sqrt{{x}}$ is discontinuous.
> 
> **Approach:** Suspicious points are the integers in the interval where $[x]$ jumps: $x=-1, 0$.
> 
> **At $x=0$:** $f(0) = 0$. $$ \lim_{x\to0^+}\left(|[x]|+\sqrt{{x}}\right) = 0+\sqrt{x} \to 0 $$ $$ \lim_{x\to0^-}\left(|-1|+\sqrt{x-(-1)}\right) = 1+\sqrt{x+1} \to 2 $$ $LHL \neq RHL$ → **discontinuous at $x=0$**.
> 
> **At $x=-1$:** $f(-1) = 1+\sqrt{-1-(-1)}=1$. $$ \lim_{x\to(-1)^+}\left(|-1|+\sqrt{x+1}\right) = 1+0=1 $$ $$ \lim_{x\to(-1)^-}\left(2+\sqrt{x+2}\right) = 3 \quad\text{(since } [x]=-2 \text{ for } x \text{ slightly less than } -1\text{)} $$ $LHL \neq RHL$ → **discontinuous at $x=-1$**.
> 
> **Answer:** $\boxed{2}$ points of discontinuity

---

## 6. Algebra of Continuity

> [!info] Purpose Instead of re-deriving $LHL/RHL/f(a)$ from scratch every time, these rules let you combine known continuous ($C$) and discontinuous ($DC$) functions and instantly know (or know you need to check) the result.

### 6.1 Core Rules

**Two continuous functions at $x=a$:**

$$ C_1 \pm C_2, \quad C_1 \times C_2, \quad \dfrac{C_1}{C_2}\Big|_{C_2(a)\neq0} \quad\longrightarrow\quad \text{always continuous} $$

**One continuous + one discontinuous at $x=a$:**

$$ C_1 \pm DC_2 \quad\longrightarrow\quad \text{always discontinuous at } x=a $$

$$ C_1 \times DC_2, \quad \dfrac{C_1}{DC_2}, \quad \dfrac{DC_2}{C_1} \quad\longrightarrow\quad \text{no direct conclusion — must check case by case} $$

**Combination of two or more discontinuous functions:**

$$ DC_1 \pm DC_2, \quad DC_1\times DC_2, \quad DC_1 \div DC_2 \quad\longrightarrow\quad \text{always check — no shortcut} $$

### 6.2 Illustrative Examples

**Example 1:** $f(x) = x^2 + [x]$ at $x=1$.

$x^2$ is continuous, $[x]$ is discontinuous at $x=1$ → sum is $C+DC$ → **always discontinuous at $x=1$**.

**Example 2:** $f(x)=x$ (continuous everywhere) and $g(x)=[x]$ (discontinuous at $x=0$). Consider $h(x) = x\cdot[x]$ at $x=0$.

This is $C \times DC$ — no direct rule, so check manually: at $x=0$, $L=0, R=0, V=0$ → **continuous at $x=0$**. (This is the special case below.)

**Example 3:** ${x}$ is discontinuous at $x=1$; $[x]$ is discontinuous at $x=1$. But: $$ f(x) = {x} + [x] = x \quad\longrightarrow\quad \text{always continuous!} $$ Two discontinuous pieces can cancel out their jumps exactly.

**Example 4 (checking $L,R,V$ triples for a product):**

|Function|$L$ (LHL)|$R$ (RHL)|$V$ ($f(a)$)|
|:--|:--|:--|:--|
|$f(x)$ — continuous|$0$|$0$|$0$|
|$g(x)$ — discontinuous|$2$|$3$|$1$|
|$f(x)\cdot g(x)$|$0$|$0$|$0$|

versus:

|Function|$L$|$R$|$V$|
|:--|:--|:--|:--|
|$f(x)$|$1$|$1$|$1$|
|$g(x)$|$2$|$3$|$1$|
|$f(x)\cdot g(x)$|$2$|$3$|$1$|

### 6.3 Key Special Case

> [!note] Continuous × Discontinuous, when $f(a)=0$ If $f(x)$ is continuous at $x=a$ with $f(a)=0$, and $g(x)$ is discontinuous at $x=a$ but has **finite** $LHL$ and $RHL$ (and $g(a)$ is defined), then $f(x)\cdot g(x)$ is **continuous at $x=a$** — because the zero from $f$ "absorbs" the finite jump in $g$.

$$ \underbrace{f(x)}_{C,; f(a)=0} \cdot \underbrace{g(x)}_{DC,\text{ finite }L,R,V} \quad\longrightarrow\quad \text{continuous at } x=a $$

Symbolically: $(0,0,0)\cdot(2,3,1) \to (0,0,0)$.

### 6.4 Applications

**Example:** $f(x) = |x-1|\left(e^{[x^2-x]} - 3^{[x^2]}\right)$ — check continuity at $x=1$.

- $|x-1|$ is continuous at $x=1$ with value $0$: $(0,0,0)$.
- $e^{[x^2-x]}-3^{[x^2]}$ is discontinuous at $x=1$ but has finite $L,R,V$ (some triple $p,q,r$).

By the special case above, the product is **continuous at $x=1$**.

**Example:** $f(x) = |\sin(\pi x)|\left(\dfrac{{x-1}-[x-2]}{3}\right)$ — comment on continuity over all $\mathbb{R}$.

$|\sin(\pi x)|$ is continuous everywhere and equals $0$ at every integer: $(0,0,0)$ at each integer.

The suspicious points of the second factor are also exactly the integers ($\ldots,-1,0,1,2,3,\ldots$), where it's discontinuous but has finite $L,R,V = (p,q,r)$.

By the special case, the product is **continuous for all $x\in\mathbb{R}$**.

---

## 7. DIBY (Do It By Yourself) — Self-Practice Set

> [!note] No worked solutions in source The following are self-practice problems from the notes — only final answers are given in the source material, so no derivation steps are fabricated here. Attempt these independently before checking the boxed answers.

> [!example] DIBY-19 — JEE (Advanced) 2015, Paper-2 **Question:** Let $m,n$ be positive integers greater than $1$. If $$ \lim_{\alpha\to0}\left(\dfrac{e^{\cos(\alpha^n)}-e}{\alpha^m}\right) = -\dfrac{e}{2} $$ find $\dfrac{m}{n}$.
> 
> **Answer:** $\boxed{2}$

> [!example] DIBY-20 — JEE (Advanced) 2012 **Question:** If $\displaystyle\lim_{x\to-\infty}\left(\dfrac{x^2+x+1}{x+1}-ax-b\right)=4$, find $(a,b)$.
> 
> _(Same problem appears earlier in Section 2 practice, listed there as DIBY-D.)_
> 
> **Answer:** $\boxed{a=1,, b=-4}$ (Option B)

> [!example] DIBY-21 **Question:** $$ \lim_{x\to\infty}\left(\dfrac{1^{1/x}+2^{1/x}+3^{1/x}+\cdots+n^{1/x}}{n}\right)^{nx} $$
> 
> **Answer:** $\boxed{n!}$

> [!example] DIBY-22 **Question:** Find $\displaystyle\lim_{n\to\infty}\sum_{r=1}^{n}\left(\dfrac{r}{n^2+r}\right)$.
> 
> **Answer:** $\boxed{\dfrac{1}{2}}$

> [!example] DIBY-23 **Question:** Evaluate $$ \lim_{n\to\infty}\left(\dfrac{1}{\sqrt{n^2}}+\dfrac{1}{\sqrt{n^2+1}}+\dfrac{1}{\sqrt{n^2+2}}+\cdots+\dfrac{1}{\sqrt{n^2+2n}}\right) $$
> 
> **Answer:** $\boxed{2}$

> [!example] DIBY-24 **Question:** Let $$ f(x) = \begin{cases} x+1, & x>0 \ 2-x, & x\leq0\end{cases}, \qquad g(x) = \begin{cases} x+3, & x<1 \ x^2-2x-2, & 1\leq x<2 \ x-5, & x\geq2\end{cases} $$ Find $LHL$ and $RHL$ of $g(f(x))$ at $x=0$, hence $\displaystyle\lim_{x\to0}g(f(x))$.
> 
> **Answer:** $\boxed{-3}$

> [!example] DIBY-25 **Question:** $\displaystyle\lim_{x\to-2}\left(\dfrac{1}{x+2}-\dfrac{12}{x^3+8}\right)$
> 
> **Answer:** $\boxed{-\dfrac{1}{2}}$

> [!example] DIBY-26 **Question:** $\displaystyle\lim_{x\to0}\dfrac{1-3^x-4^x+12^x}{\sqrt{2\cos x+7}-3}$
> 
> **Answer:** $\boxed{-12\ln2\cdot\ln3}$

> [!example] DIBY-27 — JEE Mains 2023 **Question:** $\displaystyle\lim_{t\to0}\left(1^{\sin^2t}+2^{\sin^2t}+\cdots+n^{\sin^2t}\right)^{1/\sin^2t}$
> 
> **Answer:** $\boxed{n}$ (Option B)

> [!example] DIBY-28 — JEE Mains 2021 
> **Question:** $\displaystyle\lim_{x\to0^+}\dfrac{\cos^{-1}(x-[x]^2)\cdot\sin^{-1}(x-[x]^2)}{x-x^3}$, where $[x]$ is the greatest integer $\leq x$.
> 
> **Answer:** $\boxed{\dfrac{\pi}{2}}$ (Option D)

> [!example] DIBY-29 — JEE Mains 2021 **Question:** $\displaystyle\lim_{x\to2}\left(\sum_{n=1}^{9}\dfrac{x}{n(n+1)x^2+2(2n+1)x+4}\right)$
> 
> **Answer:** $\boxed{\dfrac{9}{44}}$ (Option A)

---

## 8. Additional Homework Question (unsolved in source)

> [!example] Homework — not worked in source **Question:**
>  $f(x) = [x^2-x]+|-x+[x]|$ where $x\in\mathbb{R}$ — _(this refers to the JEE Mains 2023 discontinuity-count style question; note that a structurally similar problem on discontinuity in $(-2,1)$ is already solved in Section 5.3 — treat as the same family of problem.)_

> [!warning] Ambiguity flagged Page 24 marks a JEE Mains 2023 question as "H.W." with options (A)–(D) about continuity at $x=0$ and $x=1$ — this is the _same question_ solved later in Section 5.3. No separate unsolved homework question was left unaddressed in the source; flagging here just so you don't think something was skipped.

---

## 9. Homework (as assigned in lecture)

- Re-attempt all Class Examples.
- Solve DPP (Daily Practice Problems) & DIBY & complete relevant NCERT exercises.

---

## Related Notes

- [[Limits — Standard Forms and L'Hopital's Rule]]
- [[Continuity and Differentiability — Differentiability at a Point]]
- [[Greatest Integer and Fractional Part Functions]]
- [[Calculus MOC]]

## Open Questions

- [ ] Confirm exact source/institute name for citation (not stated in extracted text — assumed PW/coaching lecture based on "PW Store" ad on page 34).
- [ ] Section 2.1 (JEE Mains 2022, $\alpha$ problem): source only ticks $\alpha=3$ but doesn't explicitly reject $\alpha=\tfrac13$ in writing — confirm reasoning is "must be integral" per question wording.
- [ ] DIBY-20 is a verbatim repeat of the JEE (Adv.) 2012 question already solved in Section 2 practice (page 26) — confirm if your syllabus wants both entries kept or merged.
- [ ] Section 5.3, first problem's $LHL$ derivation for $[x^2-x]$ as $x\to0^-$ was reconstructed from sparse handwritten work (page 44) — recommend re-deriving independently to double check the floor evaluates to $-1$ on both sides near $0$.