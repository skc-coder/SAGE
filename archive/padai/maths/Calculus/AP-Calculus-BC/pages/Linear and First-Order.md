Standard Form
$$
\frac{dy}{dx} + Py = Q
$$
where $P$ and $Q$ are functions of $x$ (or constants)

Solution Steps

(i) Rearrange the given equation into the form $\frac{dy}{dx} + Py = Q$

(ii) Determine $\int P \, dx$  
    Integrate $P$ with respect to $x$ (don’t add constant yet)

(iii) Find the integrating factor (IF)  
    $$
    \text{IF} = e^{\int P \, dx}
    $$

(iv) Multiply both sides by IF  
    $$
    e^{\int P \, dx} \cdot \frac{dy}{dx} + e^{\int P \, dx} \cdot Py = e^{\int P \, dx} \cdot Q
    $$  
Left side becomes $\frac{d}{dx} \left[ y \cdot e^{\int P \, dx} \right]$

(v) Integrate both sides  
    $$
    \frac{d}{dx} \left[ y \cdot e^{\int P \, dx} \right] = e^{\int P \, dx} \cdot Q
    $$  
    $$
    y \cdot e^{\int P \, dx} = \int e^{\int P \, dx} \cdot Q \, dx + c
    $$

(vi) Solve for $y$  
    $$
    y = \frac{ \int e^{\int P \, dx} \cdot Q \, dx + c }{ e^{\int P \, dx} }
    $$

(vii) Apply boundary/initial conditions to find particular solution

Example
Given: $\frac{dy}{dx} + 2y = 12e^{2x}$  
- $P = 2$, $Q = 12e^{2x}$  
- $\int P \, dx = 2x$  
- $\text{IF} = e^{2x}$  
- Multiply: $e^{2x} \frac{dy}{dx} + 2e^{2x} y = 12e^{4x}$  
- Left side: $\frac{d}{dx} \left[ y e^{2x} \right]$  
- Integrate: $y e^{2x} = \int 12e^{4x} dx = 3e^{4x} + c$  
- Solution: $y = 3e^{2x} + c e^{-2x}$