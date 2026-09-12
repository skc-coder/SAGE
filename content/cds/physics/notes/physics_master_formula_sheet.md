---
exam: CDS / NDA / Science
subject: Physics
topic: Master Formula Sheet
difficulty: Medium
tags:
  - physics
  - formulas
  - cds
  - science
  - mechanics
  - optics
  - electricity
  - thermodynamics
---

# ⚡ Comprehensive Physics Master Formula Sheet

Exhaustive quantitative reference guide covering all principles, physical constants, SI units, scalar/vector rules, and formulas across Kinematics, Dynamics, Gravitation, Hydrostatics, Thermodynamics, Optics, Electricity, Magnetism, and Modern Physics.

---

## 1. Physical Quantities, Units & Dimensional Analysis

### 1.1 SI Base & Derived Units
| Quantity | Fundamental Unit | Symbol | Dimensional Formula |
| :--- | :--- | :--- | :--- |
| Length | Meter | $\text{m}$ | $[L]$ |
| Mass | Kilogram | $\text{kg}$ | $[M]$ |
| Time | Second | $\text{s}$ | $[T]$ |
| Electric Current | Ampere | $\text{A}$ | $[I]$ |
| Temperature | Kelvin | $\text{K}$ | $[\Theta]$ |
| Amount of Substance | Mole | $\text{mol}$ | $[N]$ |
| Luminous Intensity | Candela | $\text{cd}$ | $[J]$ |

### 1.2 Fundamental Physical Constants
- Speed of light in vacuum ($c$): $3.00 \times 10^8\text{ m/s}$
- Acceleration due to gravity ($g$): $9.81\text{ m/s}^2$
- Universal Gravitational Constant ($G$): $6.674 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$
- Planck's constant ($h$): $6.626 \times 10^{-34}\text{ J}\cdot\text{s}$
- Elementary charge ($e$): $1.602 \times 10^{-19}\text{ C}$
- Boltzmann constant ($k_B$): $1.380 \times 10^{-23}\text{ J/K}$
- Universal Gas constant ($R$): $8.314\text{ J/mol}\cdot\text{K}$

---

## 2. Kinematics & One/Two-Dimensional Motion

### 2.1 Uniformly Accelerated Kinematic Equations
1. $v = u + a t$
2. $s = u t + \frac{1}{2} a t^2$
3. $v^2 = u^2 + 2 a s$
4. Distance in $n$-th second: $s_n = u + \frac{a}{2}(2n - 1)$
5. Average Velocity: $v_{\text{avg}} = \frac{u + v}{2}$

### 2.2 Relative Motion & Harmonic Average Speed
- **Relative Velocity**: $\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$.
  - Opposing directions: $v_{\text{rel}} = v_1 + v_2$.
  - Same direction: $v_{\text{rel}} = |v_1 - v_2|$.
- **Harmonic Mean Speed**: Equal distance $s$ at speeds $v_1$ and $v_2$:
  $$v_{\text{avg}} = \frac{2 v_1 v_2}{v_1 + v_2}$$

### 2.3 Projectile Motion Formulas
For projection speed $u$ at angle $\theta$ to horizontal:
- **Time of Flight ($T$)**: $T = \frac{2 u \sin\theta}{g}$
- **Maximum Height ($H$)**: $H = \frac{u^2 \sin^2\theta}{2g}$
- **Horizontal Range ($R$)**: $R = \frac{u^2 \sin 2\theta}{g}$
  - Maximum range at $\theta = 45^\circ$: $R_{\text{max}} = \frac{u^2}{g}$.
  - Equal range for complementary angles: $\theta$ and $(90^\circ - \theta)$.

---

## 3. Dynamics, Momentum, Work, Energy & Power

### 3.1 Newton's Laws & Linear Momentum
- **Linear Momentum ($\vec{p}$)**: $\vec{p} = m \vec{v} \quad (\text{SI Unit: kg}\cdot\text{m/s})$
- **Newton's 2nd Law**: $\vec{F} = \frac{d\vec{p}}{dt} = m \vec{a} \quad (1\text{ N} = 10^5\text{ dynes})$
- **Impulse ($\vec{I}$)**: $\vec{I} = \vec{F} \Delta t = \Delta \vec{p}$
- **Conservation of Momentum**: $m_1 \vec{u}_1 + m_2 \vec{u}_2 = m_1 \vec{v}_1 + m_2 \vec{v}_2$

### 3.2 Friction & Circular Motion Dynamics
- **Frictional Force**: $f_{\text{max}} = \mu N$
  - Order: $\mu_{\text{static}} > \mu_{\text{kinetic}} > \mu_{\text{rolling}}$.
- **Centripetal Acceleration**: $a_c = \frac{v^2}{r} = \omega^2 r$
- **Centripetal Force**: $F_c = \frac{m v^2}{r}$
- **Optimum Banked Road Angle ($\theta$)**: $\tan\theta = \frac{v^2}{r g}$

### 3.3 Work, Energy & Power
- **Work ($W$)**: $W = \vec{F} \cdot \vec{s} = F s \cos\theta \quad (1\text{ J} = 10^7\text{ ergs})$
- **Work-Energy Theorem**: $W_{\text{net}} = \Delta K = \frac{1}{2} m v^2 - \frac{1}{2} m u^2$
- **Kinetic Energy & Momentum**: $K = \frac{p^2}{2m} \implies p = \sqrt{2mK}$
- **Gravitational Potential Energy ($U$)**: $U = m g h$
- **Power ($P$)**: $P = \frac{dW}{dt} = \vec{F} \cdot \vec{v} \quad (1\text{ HP} = 746\text{ W})$
- **Commercial Electrical Unit**: $1\text{ kWh} = 3.6 \times 10^6\text{ J}$

---

## 4. Rotational Motion & Gravitation

### 4.1 Rotational Dynamics
- **Angular Velocity ($\omega$)**: $\omega = \frac{d\theta}{dt} = 2\pi f = \frac{2\pi}{T}$
- **Moment of Inertia ($I$)**: $I = \sum m_i r_i^2 = M K^2$
  - Solid Sphere: $I = \frac{2}{5} M R^2$
  - Thin Spherical Shell: $I = \frac{2}{3} M R^2$
  - Solid Cylinder / Disc: $I = \frac{1}{2} M R^2$
  - Thin Circular Ring: $I = M R^2$
- **Torque ($\tau$) & Angular Momentum ($L$)**:
  $$\tau = I \alpha = \frac{dL}{dt}, \quad L = I \omega = m v r \sin\theta$$

### 4.2 Universal Gravitation
- **Newton's Gravitational Law**: $F = G \frac{m_1 m_2}{r^2}$
- **Acceleration due to Gravity ($g$)**: $g = \frac{G M}{R^2}$
  - Variation with Altitude $h$: $g' = g \left(1 - \frac{2h}{R}\right)$
  - Variation with Depth $d$: $g' = g \left(1 - \frac{d}{R}\right)$ (At center, $g = 0$)
- **Orbital Velocity ($v_o$)**: $v_o = \sqrt{\frac{GM}{R}} = \sqrt{g R} \approx 7.9\text{ km/s}$
- **Escape Velocity ($v_e$)**: $v_e = \sqrt{\frac{2GM}{R}} = \sqrt{2 g R} = \sqrt{2} v_o \approx 11.2\text{ km/s}$
- **Kepler's 3rd Law**: $T^2 \propto a^3$

---

## 5. Fluid Mechanics, Hydrostatics & Surface Dynamics

### 5.1 Fluid Pressure & Buoyancy
- **Pressure ($P$)**: $P = \frac{F}{A} \quad (1\text{ atm} = 1.013 \times 10^5\text{ Pa} = 760\text{ mmHg})$
- **Pressure at Depth $h$**: $P = P_0 + \rho g h$
- **Archimedes' Principle**: $F_{\text{buoyant}} = \rho_{\text{fluid}} V_{\text{submerged}} g$
- **Liquid Mixture Density**:
  - Equal Volumes ($V_1 = V_2$): $D_{\text{avg}} = \frac{d_1 + d_2}{2}$ (Arithmetic Mean)
  - Equal Masses ($m_1 = m_2$): $D_{\text{avg}} = \frac{2 d_1 d_2}{d_1 + d_2}$ (Harmonic Mean)

### 5.2 Hydrodynamics & Surface Tension
- **Equation of Continuity**: $A_1 v_1 = A_2 v_2 = \text{constant}$
- **Bernoulli's Principle**: $P + \frac{1}{2}\rho v^2 + \rho g h = \text{constant}$
- **Surface Tension ($T$)**: $T = \frac{F}{L} \quad (\text{N/m})$
- **Capillary Rise ($h$)**: $h = \frac{2 T \cos\theta}{r \rho g}$
- **Stokes' Viscous Force**: $F_v = 6 \pi \eta r v$
- **Terminal Velocity ($v_T$)**: $v_T = \frac{2 r^2 (\rho - \sigma) g}{9 \eta}$

---

## 6. Heat, Thermal Physics & Thermodynamics

### 6.1 Temperature Scale Conversions
$$\frac{C}{5} = \frac{F - 32}{9} = \frac{K - 273.15}{5} = \frac{R}{4}$$
- Equal reading in Celsius & Fahrenheit: $-40^\circ\text{C} = -40^\circ\text{F}$.

### 6.2 Heat Capacity & Expansion
- **Heat Energy**: $Q = m c \Delta T \quad (c_{\text{water}} = 1\text{ cal/g}^\circ\text{C} = 4186\text{ J/kg}\cdot\text{K})$
- **Latent Heat**: $Q = m L \quad (L_{\text{ice}} = 80\text{ cal/g}, L_{\text{steam}} = 540\text{ cal/g})$
- **Thermal Expansion Coefficients**: $\alpha : \beta : \gamma = 1 : 2 : 3$
  $$\Delta L = \alpha L \Delta T, \quad \Delta A = \beta A \Delta T, \quad \Delta V = \gamma V \Delta T$$

### 6.3 Laws of Thermodynamics
- **1st Law**: $\Delta Q = \Delta U + W$
- **Work in Isothermal Process**: $W = n R T \ln\left(\frac{V_2}{V_1}\right)$
- **Work in Adiabatic Process**: $W = \frac{P_1 V_1 - P_2 V_2}{\gamma - 1} \quad (P V^\gamma = \text{constant})$

---

## 7. Oscillations & Wave Physics

### 7.1 Simple Harmonic Motion (SHM)
- Displacement: $x(t) = A \sin(\omega t + \phi)$
- Velocity: $v = \omega \sqrt{A^2 - x^2}$
- Acceleration: $a = -\omega^2 x$
- **Simple Pendulum Period**: $T = 2\pi \sqrt{\frac{L}{g}}$

### 7.2 Waves & Sound
- Wave Speed: $v = f \lambda = \frac{\lambda}{T}$
- Speed of Sound in Gas (Laplace Formula): $v = \sqrt{\frac{\gamma P}{\rho}} = \sqrt{\frac{\gamma R T}{M}}$
- Doppler Effect Observed Frequency:
  $$f' = f \left(\frac{v \pm v_o}{v \mp v_s}\right)$$

---

## 8. Optics & Ray Light Dynamics

### 8.1 Reflection & Refraction
- Mirror Formula: $\frac{1}{f} = \frac{1}{v} + \frac{1}{u} \quad (f = R/2)$
- Lens Formula: $\frac{1}{f} = \frac{1}{v} - \frac{1}{u}$
- Lens Power: $P = \frac{1}{f \text{ (in meters)}} \quad (\text{Dioptres, D})$
- Snell's Law: $\mu = \frac{\sin i}{\sin r} = \frac{c}{v}$
- Critical Angle for Total Internal Reflection: $\sin\theta_c = \frac{1}{\mu}$

### 8.2 Vision Correction Lenses
- **Myopia (Short-sightedness)**: Concave Lens ($P < 0$)
- **Hypermetropia (Far-sightedness)**: Convex Lens ($P > 0$)
- **Astigmatism**: Cylindrical Lens

---

## 9. Electricity, Magnetism & Modern Physics

### 9.1 Electrostatics & Current Electricity
- Coulomb's Law: $F = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{r^2} \quad (k \approx 9 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2)$
- Electric Current: $I = \frac{Q}{t} \quad (\text{Amperes})$
- Ohm's Law & Resistance: $V = I R, \quad R = \rho \frac{L}{A}$
  - Series: $R_{\text{eq}} = R_1 + R_2 + \dots$
  - Parallel: $\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots$
- Joule's Heating: $H = I^2 R t = V I t = \frac{V^2}{R} t$
- Power: $P = V I = I^2 R = \frac{V^2}{R}$

### 9.2 Electromagnetic Induction & Quantum Physics
- Faraday's Law: $\mathcal{E} = -\frac{d\Phi_B}{dt}$
- Einstein's Photoelectric Equation: $E = h \nu = W_0 + K_{\text{max}} = h \nu_0 + \frac{1}{2} m v_{\text{max}}^2$
- Mass-Energy Equivalence: $E = m c^2$
- De Broglie Wavelength: $\lambda = \frac{h}{p} = \frac{h}{m v}$

---

## Navigation
- [[cds/physics/physics_overview|Physics Master Dashboard]]
- [[content/index.md|Central Vault Index]]
