---
exam: "CDS"
subject: "Physics"
topic: "Mechanics"
difficulty: "Medium"
tags: [cds, physics, mechanics, kinematics, forces, momentum]
---

# Mechanics

Comprehensive theoretical framework and formula derivations for Kinematics, Dynamics, Newton's Laws, Momentum, Impulse, Work, Energy, Power, and Projectile Motion.

---

## 1. Physical Quantities & Vectors

### Scalar and Vector Definitions

- **Scalar Quantities**: Quantities specified completely by magnitude alone (e.g., Mass $m$, Distance $s$, Speed $v$, Energy $E$, Work $W$, Power $P$, Temperature $T$).
- **Vector Quantities**: Quantities possessing both magnitude and direction that satisfy the triangle law of vector addition:
  $$\vec{A} + \vec{B} = \vec{C}, \quad \|\vec{C}\| = \sqrt{A^2 + B^2 + 2 A B \cos\theta}$$
  Examples: Displacement $\vec{x}$, Velocity $\vec{v}$, Acceleration $\vec{a}$, Force $\vec{F}$, Momentum $\vec{p}$, Torque $\vec{\tau}$.

---

## 2. Kinematics in One and Two Dimensions

### Motion Parameters

- **Distance vs Displacement**:
  - Distance ($s$) is the total length of path traversed ($s \ge 0$).
  - Displacement ($\vec{x}$) is the net change in position vector ($\vec{x} = \vec{x}_2 - \vec{x}_1$).
  - Inequality: $\|\vec{x}\| \le s$.

- **Speed and Velocity**:
  - Average Speed:
    $$v_{\text{avg}} = \frac{\text{Total Distance}}{\text{Total Time}} = \frac{\sum s_i}{\sum t_i}$$
  - Special Case (Equal Distances):
    $$v_{\text{avg}} = \frac{2 v_1 v_2}{v_1 + v_2}$$
  - Average Velocity:
    $$\vec{v}_{\text{avg}} = \frac{\vec{x}_2 - \vec{x}_1}{t_2 - t_1}$$

- **Relative Velocity**:
  - Same Direction: $v_{\text{rel}} = v_1 - v_2$
  - Opposite Direction: $v_{\text{rel}} = v_1 + v_2$

### Equations of Motion (Uniform Acceleration $a$)

- Linear Motion:
  $$v = u + a t$$
  $$s = u t + \frac{1}{2} a t^2$$
  $$v^2 = u^2 + 2 a s$$
  $$s_n = u + \frac{a}{2} (2n - 1)$$

- Vertical Motion under Gravity:
  - Downward ($a = +g$): $v = u + g t, \quad h = u t + \frac{1}{2} g t^2, \quad v^2 = u^2 + 2 g h$
  - Upward ($a = -g$): $v = u - g t, \quad h = u t - \frac{1}{2} g t^2, \quad v^2 = u^2 - 2 g h$

---

## 3. Subtopics & Specialized Proofs

- [[cds/physics/notes/subtopics/projectile_motion|Projectile Motion Derivations & Range]]
- [[cds/physics/notes/subtopics/newtons_laws_momentum|Newton's Laws & Momentum Conservation]]
- [[cds/physics/notes/subtopics/work_energy_power|Work-Energy Theorem & Power]]
- [[cds/physics/notes/subtopics/friction_circular|Friction & Centripetal Acceleration]]

---

## 4. Linked Practice Questions

- [[cds/physics/notes/questions/q1|Q1: Projectile Maximum Range Angle]]
- [[cds/physics/notes/questions/q2|Q2: Recoil Velocity of Gun]]

---

## Navigation

- [[cds/physics/physics_overview|Physics Overview]]
- [[cds/physics/notes/formulas|Master Formulas]]
