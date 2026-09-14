Tags: #Topic 

# Differential Equations

**Differential Equation** - An equations that relates a function to one or more of its derivatives

> **Ex.**
> $$
\Large
\begin{aligned}
& \frac{dy}{dx} = y^2 + 34 \\
& \frac{d^2y}{dx^2} + \frac{dy}{dx} - 52 = y \\
\end{aligned}
> $$

First-order differential equations (ie. $\dfrac{dy}{dx} = y \ldots$) can be represented graphically by using [[Slope Fields]].

The solutions to a differential equations is a set of possible functions for that function.

> **Ex.**
> $$\Large \frac{d^2y}{dx^2} + 2\frac{dy}{dx} = 3y$$
> 
> Could have these equations as possible solutions:
> 
> $$
\Large
\begin{aligned}
& y=e^{-3x} \\
& y=e^{x} \\
\end{aligned}
> $$

## Seperable Differential Equations

1. Given some differential equation of $x$ and $y$ containing only first-order derivatives, try and seperate all the $y$ variables to one side and all the $x$ variables to the other side.

> **Ex.**
> $$
\Large 
\begin{aligned}
& \frac{dy}{dx} = 3xy^2 \\
& dy = 3xy^2dx \\
& \frac{dy}{y^2} = 3xdx \\
\end{aligned}
> $$

3. If this is possible, then you can solve for a generation solution for the differential equation by integrating both sides

> **Ex.**
> $$
\Large 
\begin{aligned}
& \int \frac{1}{y^2}dy = \int 3xdx \\
& \frac{y^{-3}}{-3} = 3\cdot\frac{x^2}{2} + C\\
& -\frac{1}{3y^3} = \frac{3x^2}{2} + C\\
\end{aligned}
> $$

3. If you want a specific solution, then you must solve for $y$.

> Sources: Bird's Engineering Math (Ch. 46–53) + Paul's ODE Notes (Lamar Univ.)

---
#### Quick Index by Method
[[Separable]] · [[Homogeneous]] · [[Linear (IF)]] · [[Exact]] · [[Bernoulli]]
[[Undetermined Coefficients]] · [[Variation of Parameters]] · [[Euler Method]]
[[Laplace Transforms]] · [[Power Series]] · [[Frobenius]] · [[Separation of Vars]]

---
### 0. Prerequisites
- [[Calculus Review — Differentiation]]
- [[Integration Techniques]]
- [[Linear Algebra Review — Matrices & Eigenvalues]]
- [[Power Series & Taylor Series Review]]

---

### 1. Introduction & Basic Concepts
- [[1.1 Family of Curves]]
- [[1.2 What is a Differential Equation]]
- [[1.3 Order, Linearity, Initial Conditions]]
- [[1.4 Direction Fields]]
- [[1.5 Interval of Validity]]
#de/basics

---

### 2. First-Order DEs — Analytical Methods

#### 2.1 Separable Equations
- [[2.1a Equations of the form dy∕dx = f(x)]]
- [[2.1b Equations of the form dy∕dx = f(y)]]
- [[2.1c Equations of the form dy∕dx = f(x)·f(y)]]
- [[2.1d Separable Equations — Paul's Notes]]
#de/first-order/separable

#### 2.2 Homogeneous Equations
- [[Homogeneous DEs]]
- [[2.2c Substitutions — Paul's Notes]]
#de/first-order/homogeneous

#### 2.3 Linear and First-Order
- [[Linear and First-Order]]
- ![](attachments/Pasted%20image%2020260502062200.png)
- [[2.3b Worked Problems — Linear First-Order]]
#de/first-order/linear

#### 2.4 Exact Equations
- [[2.4a Exact Equations — Test & Solution]]
#de/first-order/exact

#### 2.5 Bernoulli Equations
- [[2.5a Bernoulli DE — Substitution Method]]
#de/first-order/bernoulli

#### 2.6 Equilibrium Solutions
- [[2.6a Autonomous Equations & Equilibrium Points]]
- [[2.6b Stability — Asymptotic, Unstable, Semi-stable]]
#de/first-order/equilibrium

#### 2.7 Modeling with First-Order DEs
- [[2.7a Mixing Problems]]
- [[2.7b Population Models]]
- [[2.7c Falling Objects — Gravity & Air Resistance]]
#de/applications

---

### 3. First-Order DEs — Numerical Methods
- [[3.1 Euler's Method]]
- [[3.2 Euler-Cauchy Method]]
- [[3.3 Runge-Kutta Method]]
#de/numerical

---

### 4. Second-Order DEs — Homogeneous (Constant Coeff.)
- [[4.1 Characteristic Polynomial & Superposition]]
- [[4.2 Real Distinct Roots]]
- [[4.3 Complex Roots]]
- [[4.4 Repeated Roots]]
- [[4.5 Reduction of Order]]
- [[4.6 Wronskian & Fundamental Sets of Solutions]]
#de/second-order/homogeneous

---

### 5. Second-Order DEs — Nonhomogeneous
- [[5.1 Complementary Function & Particular Integral]]
- [[5.2 Undetermined Coefficients]]
- [[5.3 Variation of Parameters]]
- [[5.4 f(x) as polynomial, exponential, trig, sum∕product]]
#de/second-order/nonhomogeneous

---

### 6. Applications — Mechanical Vibrations
- [[6.1 Spring-Mass System — Free Oscillation]]
- [[6.2 Damped & Forced Vibrations]]
#de/applications

---

### 7. Higher-Order DEs
- [[7.1 nth Order — Basic Concepts & Wronskian]]
- [[7.2 Linear Homogeneous — Real & Complex Repeated Roots]]
- [[7.3 Undetermined Coefficients (Higher Order)]]
- [[7.4 Variation of Parameters (Higher Order)]]
#de/higher-order

---

### 8. Laplace Transforms
- [[8.1 Definition & Basic Transforms]]
- [[8.2 Laplace Transform Table]]
- [[8.3 Inverse Laplace Transforms]]
- [[8.4 Step Functions (Heaviside)]]
- [[8.5 Dirac Delta Function]]
- [[8.6 Solving IVPs with Laplace Transforms]]
- [[8.7 Convolution Integral]]
- [[8.8 Nonconstant Coefficient IVPs]]
#de/laplace

---

### 9. Systems of DEs
- [[9.1 Matrix Form of Systems]]
- [[9.2 Phase Plane & Phase Portraits]]
- [[9.3 Real Eigenvalues — Saddle Points & Nodes]]
- [[9.4 Complex Eigenvalues — Centers & Spirals]]
- [[9.5 Repeated Eigenvalues — Improper Nodes]]
- [[9.6 Nonhomogeneous Systems]]
- [[9.7 Laplace Transforms for Systems]]
- [[9.8 Modeling — Tank Mixing, Predator-Prey, Vibrations]]
#de/systems

---

### 10. Series & Special Methods

#### 10.1 Power Series Methods
- [[10.1a Higher-Order Differential Coefficients as Series]]
- [[10.1b Leibniz's Theorem]]
- [[10.1c Leibniz-Maclaurin Method]]
- [[10.1d Frobenius Method]]
- [[10.1e Series Solutions — Ordinary & Singular Points]]
- [[10.1f Euler's Differential Equation]]
#de/series

#### 10.2 Special Functions
- [[10.2a Bessel's Equation & Bessel Functions]]
- [[10.2b Legendre's Equation & Legendre Polynomials]]
#de/series/special-functions

---

### 11. Boundary Value Problems & Fourier Series
- [[11.1 Boundary Value Problems vs IVPs]]
- [[11.2 Eigenvalues & Eigenfunctions (BVP)]]
- [[11.3 Periodic & Orthogonal Functions]]
- [[11.4 Fourier Sine Series]]
- [[11.5 Fourier Cosine Series]]
- [[11.6 Full Fourier Series]]
- [[11.7 Convergence of Fourier Series]]
#de/bvp #de/fourier

---

### 12. Partial Differential Equations
- [[12.1 Introduction & Partial Integration]]
- [[12.2 Separation of Variables — Method]]
- [[12.3 Heat Equation]]
- [[12.4 Heat Equation — Non-Zero Boundaries]]
- [[12.5 Wave Equation & Vibrating String]]
- [[12.6 Laplace's Equation]]
- [[12.7 Engineering PDEs — Overview]]
#de/pde
