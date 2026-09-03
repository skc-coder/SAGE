---
exam: "CDS"
subject: "Physics"
topic: "Gravitation"
difficulty: "Medium"
tags: [cds, physics, gravitation, rotation, Kepler, satellites]
---

# Gravitation and Rotational Motion

Theory of Universal Gravitation, Acceleration due to Gravity Variations, Kepler's Laws of Planetary Motion, Satellite Dynamics, and Rotational Mechanics.

---

## 1. Newton's Law of Universal Gravitation

Every particle attracts every other particle with a force proportional to the product of their masses and inversely proportional to the square of distance:
$$F = G \frac{m_1 m_2}{r^2}$$
$$G \approx 6.67 \times 10^{-11}\text{ N}\cdot\text{m}^2/\text{kg}^2$$

---

## 2. Acceleration due to Gravity ($g$)

On Earth's surface ($M = 5.97 \times 10^{24}\text{ kg}, R = 6371\text{ km}$):
$$g = \frac{G M}{R^2} \approx 9.8\text{ m/s}^2$$

### Variations in $g$

1. **Altitude ($h$)**:
   $$g_h = g \left(1 + \frac{h}{R}\right)^{-2} \approx g \left(1 - \frac{2h}{R}\right)$$
2. **Depth ($d$)**:
   $$g_d = g \left(1 - \frac{d}{R}\right) \implies g_{\text{center}} = 0$$
3. **Latitude ($\lambda$) due to Earth Rotation**:
   $$g' = g - R \omega^2 \cos^2\lambda$$
   - At Poles ($\lambda = 90^\circ$): $g' = g$ (Maximum).
   - At Equator ($\lambda = 0^\circ$): $g' = g - R \omega^2$ (Minimum).

---

## 3. Satellite Dynamics & Escape Speed

- **Orbital Velocity ($v_o$)**: Speed required to orbit near Earth's surface:
  $$v_o = \sqrt{\frac{G M}{R}} = \sqrt{g R} \approx 7.92\text{ km/s}$$
- **Escape Velocity ($v_e$)**: Minimum speed to break gravitational pull:
  $$v_e = \sqrt{\frac{2 G M}{R}} = \sqrt{2 g R} = \sqrt{2} v_o \approx 11.2\text{ km/s}$$
- **Geostationary Satellite**: Altitude $\approx 35,786\text{ km}$, Time period $T = 24\text{ hours}$, orbits West to East above Equator.

---

## 4. Kepler's Laws of Planetary Motion

1. **First Law (Ellipses)**: Planets revolve around the Sun in elliptical orbits with the Sun at one focus.
2. **Second Law (Equal Areas)**: A line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time ($\frac{dA}{dt} = \text{constant}$).
3. **Third Law (Harmonies)**: The square of the orbital period is proportional to the cube of the semi-major axis:
   $$T^2 \propto a^3$$

---

## Navigation

- [[cds/physics/physics_overview|Physics Overview]]
- [[cds/physics/notes/formulas|Master Formulas]]
