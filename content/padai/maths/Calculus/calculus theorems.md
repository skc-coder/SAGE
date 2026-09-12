---
source: https://www.youtube.com/watch?v=1l-cAG5zIt0
tags:
  - calculus
---
## Intermediate Value Theorem (IVT)
- If $f$ continuous on $[a,b]$, and $f(a) < k < f(b)$, then $\exists c \in (a,b)$ s.t. $f(c) = k$.
- Example: $f(a) < 0 < f(b) \Rightarrow \exists c$ where $f(c) = 0$.

## Extreme Value Theorem (EVT)
- If $f$ continuous on $[a,b]$, then $f$ has abs min & max on $[a,b]$.
- Not guaranteed on open/infinite intervals. Counter: $f(x)=x$ on $(-\infty,\infty)$.

## Rolle’s Theorem
- If $f$ cont on $[a,b]$, diff on $(a,b)$, and $f(a)=f(b)$, then $\exists c \in (a,b)$ s.t. $f'(c)=0$.
- Requires $f(a)=f(b)$. (e.g., $[-2,2]$ for $x^2-4$).

## Mean Value Theorem (Derivatives)
- If $f$ cont on $[a,b]$, diff on $(a,b)$, then $\exists c \in (a,b)$ s.t. $f'(c) = \frac{f(b)-f(a)}{b-a}$.
- Slope of tangent = slope of secant. 
- Counter: if RHS ≠ 0, fix RHS (e.g., 43 not 0).

## Mean Value Theorem (Integrals)
- If $f$ cont on $[a,b]$, then $\exists c \in [a,b]$ s.t. $f(c) = \frac{1}{b-a} \int_a^b f(x)\,dx$.
- This is the average value. Counter: if given $f(c)=44$, fix to actual avg (e.g., 11 for $x^3-5$ on $[0,4]$).
