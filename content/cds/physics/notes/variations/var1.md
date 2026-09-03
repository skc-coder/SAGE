---
exam: "CDS"
subject: "Physics"
topic: "Mechanics"
subtopic: "Kinematics"
difficulty: "Hard"
tags: [cds, physics, variation, mechanics, kinematics, calculus]
---

# Variation 1: Non-Uniform Acceleration Kinematics

## Conceptual Variation

Instead of uniform acceleration where $v = u + a t$, consider a body moving along a straight line where acceleration varies linearly with time $t$:
$$a(t) = k t$$
where $k$ is a constant, and initial velocity at $t = 0$ is $u$.

---

## Derivation & Solution

1. **Velocity Function**:
   $$a(t) = \frac{dv}{dt} = k t \implies \int_u^v dv = \int_0^t k t \, dt$$
   $$v(t) = u + \frac{1}{2} k t^2$$

2. **Displacement Function**:
   $$v(t) = \frac{ds}{dt} = u + \frac{1}{2} k t^2 \implies \int_0^s ds = \int_0^t \left(u + \frac{1}{2} k t^2\right) dt$$
   $$s(t) = u t + \frac{1}{6} k t^3$$

---

## Exam Takeaway

For time-dependent acceleration $a(t)$, standard equations of motion ($v = u + at$, $s = ut + \frac{1}{2}at^2$) **CANNOT** be used. Direct integration of $a = \frac{dv}{dt}$ and $v = \frac{ds}{dt}$ is mandatory.

---

## Navigation

- [[cds/physics/notes/mechanics|Mechanics Overview]]
- [[cds/physics/notes/formulas|Physics Formulas]]
