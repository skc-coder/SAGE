---
exam: "CDS"
subject: "Physics"
topic: "Master Cheat Sheet"
difficulty: "Medium"
tags: [cds, physics, formulas, definitions, cheatsheet]
---

# Physics Cheat Sheet & Formula Master

Comprehensive reference guide containing all essential definitions, principles, SI units, and quantitative formulas across all major physics domains for competitive examinations.

---

## 1. Physical Quantities, Kinematics & Mechanics

### Core Definitions

- **Scalar Quantities**: Physical quantities possessing magnitude only and no directional dependence (e.g., Mass, Speed, Volume, Energy, Work, Time, Power).
- **Vector Quantities**: Physical quantities possessing both magnitude and specific direction that obey the vector addition triangle law (e.g., Displacement, Velocity, Acceleration, Force, Linear Momentum, Torque).
- **Distance ($s$)**: Total scalar path length traversed by an object between initial and final states ($s \ge 0$).
- **Displacement ($\vec{x}$)**: Shortest directed vector path from initial position $\vec{x}_1$ to final position $\vec{x}_2$.
  $$\|\vec{x}\| \le \text{Distance}$$
- **Speed ($v$)**: Time rate of scalar distance coverage:
  $$v = \frac{\Delta s}{\Delta t}$$
- **Velocity ($\vec{v}$)**: Time rate of change of position vector:
  $$\vec{v} = \frac{d\vec{x}}{dt}$$
- **Harmonic Average Speed**: If equal distances $s$ are traversed at speeds $v_1$ and $v_2$, the average speed is:
  $$v_{\text{avg}} = \frac{2 v_1 v_2}{v_1 + v_2}$$
- **Relative Velocity**:
  - Same direction: $v_{\text{rel}} = v_1 - v_2$
  - Opposite direction: $v_{\text{rel}} = v_1 + v_2$
- **Acceleration ($\vec{a}$)**: Time rate of change of velocity:
  $$\vec{a} = \frac{d\vec{v}}{dt} \quad (\text{SI Unit: m/s}^2)$$

### Kinematic Equations of Motion (Constant Acceleration $a$)

1. Linear Speed-Time Relation:
   $$v = u + a t$$
2. Position-Time Relation:
   $$s = u t + \frac{1}{2} a t^2$$
3. Position-Velocity Relation:
   $$v^2 = u^2 + 2 a s$$
4. Distance Traversed in the $n$-th Second:
   $$s_n = u + \frac{a}{2} (2n - 1)$$

*Note for motion under gravity:* Replace $a$ with $+g$ (downward) or $-g$ (upward), where $g \approx 9.8\text{ m/s}^2$.

---

## 2. Dynamics, Projectile Motion & Work-Energy-Power

### Projectile Motion Formulas
For projection angle $\theta$ with initial speed $u$:

- **Time of Flight ($T$)**:
  $$T = \frac{2 u \sin\theta}{g}$$
- **Maximum Height ($H$)**:
  $$H = \frac{u^2 \sin^2\theta}{2g}$$
- **Horizontal Range ($R$)**:
  $$R = \frac{u^2 \sin(2\theta)}{g}$$
  *(Max range occurs at $\theta = 45^\circ$, and identical range occurs at complementary angles $\theta$ and $90^\circ - \theta$.)*

### Newton's Laws of Motion & Momentum

- **First Law (Law of Inertia)**: A body remains at rest or in uniform linear motion unless compelled by a net external force. Mass measures quantitative inertia.
- **Second Law**:
  $$\vec{F} = \frac{d\vec{p}}{dt} = m \vec{a} \quad (1\text{ N} = 10^5\text{ dynes})$$
- **Third Law**: To every action force, there is an equal and opposite reaction force acting on distinct bodies ($\vec{F}_{AB} = -\vec{F}_{BA}$).
- **Linear Momentum ($\vec{p}$)**: $\vec{p} = m \vec{v}$ (SI Unit: $\text{kg}\cdot\text{m/s}$).
- **Conservation of Linear Momentum**: In an isolated system ($\vec{F}_{\text{ext}} = 0$):
  $$m_1 \vec{u}_1 + m_2 \vec{u}_2 = m_1 \vec{v}_1 + m_2 \vec{v}_2$$
- **Impulse ($\vec{I}$)**: Product of a large force and short time interval:
  $$\vec{I} = \vec{F} \Delta t = \Delta \vec{p}$$

### Friction & Centripetal Acceleration

- **Frictional Force**: Opposes relative interfacial motion:
  $$f_{\text{max}} = \mu N$$
  $$\mu_s > \mu_k > \mu_r \quad (\text{Static} > \text{Kinetic} > \text{Rolling})$$
- **Centripetal Acceleration**:
  $$a_c = \frac{v^2}{r} = \omega^2 r$$
- **Centripetal Force**:
  $$F_c = \frac{m v^2}{r}$$

### Work, Energy & Power

- **Work ($W$)**: Scalar product of force and displacement:
  $$W = \vec{F} \cdot \vec{s} = F s \cos\theta \quad (\text{SI Unit: Joule, } 1\text{ J} = 10^7\text{ ergs})$$
- **Kinetic Energy ($K$)**: Energy due to motion:
  $$K = \frac{1}{2} m v^2 = \frac{p^2}{2m}$$
- **Gravitational Potential Energy ($U$)**:
  $$U = m g h$$
- **Power ($P$)**: Rate of work execution:
  $$P = \frac{dW}{dt} = \vec{F} \cdot \vec{v} \quad (\text{SI Unit: Watt, } 1\text{ HP} = 746\text{ W})$$
- **Commercial Electrical Energy**:
  $$1\text{ kWh} = 3.6 \times 10^6\text{ J}$$

---

## 3. Rotational Motion & Gravitation

### Rotational Dynamics

- **Angular Velocity ($\omega$)**: $\omega = \frac{d\theta}{dt} = \frac{2\pi}{T} = 2\pi f$.
- **Linear vs Angular Relation**: $v = r \omega$.
- **Moment of Inertia ($I$)**:
  $$I = \sum m_i r_i^2 = M K^2$$
  - Solid Sphere: $I = \frac{2}{5} M R^2$
  - Circular Ring / Thin Shell: $I = M R^2$
  - Circular Disc / Solid Cylinder: $I = \frac{1}{2} M R^2$
- **Angular Momentum ($L$)**:
  $$L = I \omega = r p \sin\theta$$
- **Torque ($\tau$)**:
  $$\tau = I \alpha = \vec{r} \times \vec{F}$$

### Gravitation & Celestial Mechanics

- **Newton's Law of Gravitation**:
  $$F = G \frac{m_1 m_2}{r^2} \quad (G \approx 6.67 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2)$$
- **Acceleration due to Gravity ($g$)**:
  $$g = \frac{G M}{R^2} \approx 9.8\text{ m/s}^2$$
  - Altitude $h$: $g' = g \left(1 - \frac{2h}{R}\right)$
  - Depth $d$: $g' = g \left(1 - \frac{d}{R}\right)$ (At Earth's center, $g' = 0$).
  - Earth Latitude $\lambda$: $g' = g - R \omega^2 \cos^2\lambda$ (Max at poles, min at equator).
- **Orbital Velocity ($v_o$)**:
  $$v_o = \sqrt{\frac{G M}{R}} = \sqrt{g R} \approx 7.92\text{ km/s}$$
- **Escape Velocity ($v_e$)**:
  $$v_e = \sqrt{\frac{2 G M}{R}} = \sqrt{2 g R} = \sqrt{2} v_o \approx 11.2\text{ km/s}$$
- **Geostationary Satellite**: Altitude $h \approx 36,000\text{ km}$, Time Period $T = 24\text{ hours}$, rotates West to East in equatorial plane.
- **Kepler's Laws**:
  1. Elliptical Orbits with Sun at one focus.
  2. Areal Velocity conservation ($\frac{dA}{dt} = \text{constant}$).
  3. Harmonic Law: $T^2 \propto a^3$.

---

## 4. Properties of Matter & Fluid Mechanics

### Elasticity & Hydrostatics

- **Stress & Strain**:
  $$\text{Stress} = \frac{\text{Force}}{\text{Area}}, \quad \text{Strain} = \frac{\Delta L}{L}$$
- **Hooke's Law**: $\text{Stress} \propto \text{Strain}$ (up to elastic limit).
  $$Y = \frac{\text{Longitudinal Stress}}{\text{Longitudinal Strain}}$$
- **Fluid Pressure ($P$)**:
  $$P = \frac{F}{A} \quad (\text{SI Unit: Pascal, } 1\text{ Pa} = 1\text{ N/m}^2, 1\text{ atm} = 1.013 \times 10^5\text{ Pa} = 760\text{ mmHg})$$
- **Hydrostatic Pressure at Depth $h$**:
  $$P = P_0 + \rho g h$$
- **Pascal's Law**: Pressure applied to enclosed incompressible fluid is transmitted undiminished in all directions (basis for hydraulic press).
- **Archimedes' Principle & Buoyancy**:
  $$F_B = \text{Weight of displaced liquid} = \rho_{\text{fluid}} V_{\text{submerged}} g$$
  - Floating condition: $\text{Weight of object} = \text{Buoyant force}$.
- **Density & Specific Gravity**:
  $$\text{Density } \rho = \frac{\text{Mass}}{\text{Volume}}, \quad \text{Relative Density} = \frac{\rho_{\text{substance}}}{\rho_{\text{water at } 4^\circ\text{C}}}$$

### Hydrodynamics & Surface Dynamics

- **Equation of Continuity**:
  $$A_1 v_1 = A_2 v_2 = \text{constant}$$
- **Bernoulli's Theorem**: For streamlined flow of an ideal fluid:
  $$P + \frac{1}{2} \rho v^2 + \rho g h = \text{constant}$$
- **Surface Tension ($T$)**: Liquid surface contractive force per unit length:
  $$T = \frac{F}{L} \quad (\text{SI Unit: N/m})$$
- **Capillary Rise ($h$)**:
  $$h = \frac{2 T \cos\theta}{r \rho g}$$
  *(Water rises in glass capillary ($\theta < 90^\circ$), mercury depresses ($\theta > 90^\circ$).)*
- **Stokes' Law & Terminal Velocity**:
  $$F_v = 6 \pi \eta r v$$
  $$v_T = \frac{2 r^2 (\rho - \sigma) g}{9 \eta}$$

---

## 5. Heat, Thermodynamics & Waves

### Temperature Scales & Thermal Physics

- **Temperature Scale Conversion**:
  $$\frac{C}{5} = \frac{F - 32}{9} = \frac{R}{4} = \frac{K - 273.15}{5}$$
  - Absolute Zero: $0\text{ K} = -273.15^\circ\text{C}$.
  - Equal Celsius and Fahrenheit reading: $-40^\circ\text{C} = -40^\circ\text{F}$.
- **Heat Capacity & Specific Heat**:
  $$Q = m c \Delta T \quad (c_{\text{water}} = 1\text{ cal/g}^\circ\text{C} = 4186\text{ J/kg}\cdot\text{K})$$
- **Latent Heat ($L$)**:
  $$Q = m L \quad (L_{\text{fusion, ice}} = 80\text{ cal/g}, L_{\text{vaporization, water}} = 540\text{ cal/g})$$
- **Thermal Expansion**:
  $$\Delta L = \alpha L \Delta T, \quad \Delta A = \beta A \Delta T, \quad \Delta V = \gamma V \Delta T$$
  $$\alpha : \beta : \gamma = 1 : 2 : 3$$

### Thermodynamics & Waves

- **First Law of Thermodynamics**:
  $$\Delta Q = \Delta U + W$$
- **Second Law & Entropy**: Heat cannot spontaneously flow from a colder body to a hotter body without external work.
- **Simple Harmonic Motion (SHM)**:
  $$x(t) = A \sin(\omega t + \phi)$$
  - Simple Pendulum Time Period: $T = 2\pi \sqrt{\frac{L}{g}}$
- **Wave Velocity ($v$)**:
  $$v = f \lambda = \frac{\lambda}{T}$$
- **Speed of Sound**:
  $$v = \sqrt{\frac{\gamma P}{\rho}} = \sqrt{\frac{\gamma R T}{M}}$$
  *(Sound requires a physical medium; $v_{\text{solid}} > v_{\text{liquid}} > v_{\text{gas}}$. In air at $0^\circ\text{C}$, $v \approx 332\text{ m/s}$.)*

---

## 6. Optics & Light

### Reflection & Refraction

- **Laws of Reflection**: $\theta_i = \theta_r$.
- **Mirror Formula & Magnification**:
  $$\frac{1}{f} = \frac{1}{v} + \frac{1}{u}, \quad m = -\frac{v}{u} = \frac{h_i}{h_o}$$
  - Focal length: $f = \frac{R}{2}$ (Concave: $f < 0$, Convex: $f > 0$).
- **Snell's Law of Refraction**:
  $$\mu = \frac{\sin i}{\sin r} = \frac{c}{v}$$
- **Critical Angle ($\theta_c$) & Total Internal Reflection (TIR)**:
  $$\sin\theta_c = \frac{1}{\mu}$$
  *(Condition for TIR: Light travels from denser to rarer medium with $i > \theta_c$. Applications: Optical fibers, mirages, diamond sparkle.)*
- **Lens Formula & Power**:
  $$\frac{1}{f} = \frac{1}{v} - \frac{1}{u}, \quad P = \frac{1}{f \text{ (meters)}} \quad (\text{Unit: Dioptre, D})$$

### Human Eye Defects & Corrections

- **Myopia (Short-sightedness)**: Image forms in front of retina. Corrected using **Concave Lens** ($P < 0$).
- **Hypermetropia (Far-sightedness)**: Image forms behind retina. Corrected using **Convex Lens** ($P > 0$).
- **Presbyopia**: Age-related loss of accommodation. Corrected using **Bifocal Lens**.
- **Astigmatism**: Asymmetrical cornea curvature. Corrected using **Cylindrical Lens**.

---

## 7. Electricity, Magnetism & Modern Physics

### Electrostatics & Current Electricity

- **Coulomb's Law**:
  $$F = \frac{1}{4\pi\varepsilon_0} \frac{q_1 q_2}{r^2} \quad (k \approx 9 \times 10^9\text{ N}\cdot\text{m}^2/\text{C}^2)$$
- **Electric Current ($I$)**: Rate of charge flow:
  $$I = \frac{Q}{t} \quad (\text{Unit: Ampere, A})$$
- **Ohm's Law & Resistance**:
  $$V = I R, \quad R = \rho \frac{L}{A}$$
  - Series Combination: $R_{\text{eq}} = R_1 + R_2 + R_3$
  - Parallel Combination: $\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$
- **Joule's Heating Effect & Power**:
  $$H = I^2 R t = V I t = \frac{V^2}{R} t$$
  $$P = V I = I^2 R = \frac{V^2}{R} \quad (\text{Unit: Watt})$$

### Magnetism & Modern Physics

- **Faraday's Law of Electromagnetic Induction**:
  $$\mathcal{E} = -\frac{d\Phi_B}{dt}$$
- **Photoelectric Effect (Einstein's Equation)**:
  $$E = h \nu = W_0 + K_{\text{max}} = h \nu_0 + \frac{1}{2} m v_{\text{max}}^2$$
- **Mass-Energy Equivalence**:
  $$E = m c^2 \quad (c \approx 3 \times 10^8\text{ m/s})$$

---

## Navigation

- [[cds/physics/physics_overview|Physics Master Overview]]
- [[cds/physics/notes/mechanics|Mechanics Note]]
