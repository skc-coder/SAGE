---
exam: "CDS"
subject: "Physics"
topic: "Mechanics"
subtopic: "Projectile Motion"
difficulty: "Medium"
tags: [cds, physics, mechanics, projectile, derivation]
---

# Projectile Motion

Two-dimensional motion under constant gravitational acceleration $g$ directed downwards, where horizontal velocity remains invariant in the absence of air resistance.

---

## 1. Mathematical Formulation

Let a projectile be launched with initial velocity $u$ at angle $\theta$ to the horizontal ground.

- Initial Velocity Components:
  $$u_x = u \cos\theta, \quad u_y = u \sin\theta$$
- Acceleration Components:
  $$a_x = 0, \quad a_y = -g$$

---

## 2. Derivations of Key Parameters

### 1. Time of Flight ($T$)

At maximum height, vertical velocity $v_y = 0$:
$$v_y = u_y - g t_{\text{up}} \implies 0 = u \sin\theta - g t_{\text{up}}$$
$$t_{\text{up}} = \frac{u \sin\theta}{g}$$

Total time of flight $T = 2 t_{\text{up}}$:
$$T = \frac{2 u \sin\theta}{g}$$

### 2. Maximum Height ($H$)

Using third kinematic equation $v_y^2 = u_y^2 - 2 g H$:
$$0 = (u \sin\theta)^2 - 2 g H$$
$$H = \frac{u^2 \sin^2\theta}{2g}$$

### 3. Horizontal Range ($R$)

Range is the horizontal distance covered during time $T$:
$$R = u_x \times T = (u \cos\theta) \left( \frac{2 u \sin\theta}{g} \right)$$
$$R = \frac{u^2 (2 \sin\theta \cos\theta)}{g} = \frac{u^2 \sin(2\theta)}{g}$$

---

## 3. Important Properties & Invariants

1. **Maximum Range Angle**:
   $$R_{\text{max}} = \frac{u^2}{g} \quad \text{at } \theta = 45^\circ$$
2. **Complementary Angles Property**:
   Range for angle $\theta$ and $(90^\circ - \theta)$ are identical:
   $$\sin(2(90^\circ - \theta)) = \sin(180^\circ - 2\theta) = \sin(2\theta)$$
3. **Trajectory Equation (Parabola)**:
   $$y = x \tan\theta - \frac{g x^2}{2 u^2 \cos^2\theta}$$

---

## Navigation

- [[content/cds/physics/notes/mechanics|Mechanics Overview]]
- [[content/cds/physics/notes/formulas|Physics Formulas]]
