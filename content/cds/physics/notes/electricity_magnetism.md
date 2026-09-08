---
exam: "CDS"
subject: "Physics"
topic: "Electricity and Magnetism"
difficulty: "Medium"
tags: [cds, physics, electricity, magnetism, circuit, ohms-law]
---

# Electricity and Magnetism

Electrostatics, Current Electricity, Ohm's Law, Circuit Combinations, Joule Heating, Electromagnetic Induction, and Magnetic Effects.

---

## 1. Charge & Current Electricity

**TL;DR:**

  

The image shows the step-by-step calculation to find the **number of electrons in 1 Coulomb ($1\text{ C}$) of charge**:

  

- **Formula:** $Q = n \cdot e$
    
      
    
- **Values:** $Q = 1\text{ C}$, $e = 1.6 \times 10^{-19}\text{ C}$
    
      
    
- **Calculation:** $n = \frac{1}{1.6 \times 10^{-19}} = \frac{100}{16} \times 10^{18}$
    
      
    
- **Result:** **$6.25 \times 10^{18}$ electrons**0


Here is a clear breakdown of the physics notes shown in the image, organized by topic:

  

### 1. Resistance ($R$) & Resistivity ($\rho$)

- **Formula:** $R = \rho \frac{l}{A}$
    
      
    - $R$ = Resistance
        
          
        
    - $l$ = Length of the conductor
        
          
        
    - $A$ = Cross-sectional area
        
          
        
    - $\rho$ = Resistivity (Unit: $\Omega \cdot \text{m}$)
        
          
        
- **Key Concept:** Resistivity ($\rho$) depends **only on the type of material** and temperature. It does **not** depend on the dimensions ($l$ or $A$) of the wire.
    
      
    

### 2. Temperature Dependence

- **Conductors:** $R \propto T$ and $\rho \propto T$
    
    _(Resistance and resistivity increase as temperature increases)._
    
      
    
- **Semiconductors & Insulators:** $R \propto \frac{1}{T}$ and $\rho \propto \frac{1}{T}$
    
    _(Resistance and resistivity decrease as temperature increases)._
    
      
    

### 3. Order of Resistivity ($\rho$)

From lowest resistivity (best conductors) to highest resistivity (insulators):

  

$$\text{Silver} < \text{Cu} < \text{Al} < \text{W} < \text{Ni} < \text{Fe} < \text{Cr} < \text{Hg} < \text{Mn} < \text{Constantan} < \text{Manganin} < \text{Nichrome} < \text{Glass} < \text{Rubber} < \text{Ebonite} < \text{Diamond} < \text{Dry Paper}$$

### 4. Common Materials & Applications

- **Copper ($\text{Cu}$) + Aluminum ($\text{Al}$):** Used for **transmission lines** due to very low resistivity.
    
      
    
- **Constantan ($\text{Cu} + \text{Ni}$) & Manganin ($\text{Cu} + \text{Mn} + \text{Ni}$):** Used to make **standard resistors** because their resistivity ($\rho$) is high and barely changes with temperature (low temperature coefficient).
    
      
    
- **Nichrome ($\text{Ni} + \text{Cr} + \text{Mn} + \text{Fe}$):** Used in **heating elements** (irons, hairdryers, heaters, presses) because it has high resistivity and can withstand high temperatures without burning.
    
      
    
- **Tungsten ($\text{W}$):** Used for **filaments** in incandescent bulbs. Converts input power into both light and heat.
    
      
    

### 5. Conductance ($G$) & Conductivity ($\sigma$)

- **Conductance ($G$ or $C$):** The reciprocal of resistance.
    
      
    
    $$\text{Conductance} = \frac{1}{R}$$
    
    - **Unit:** $\text{mho}$ or $\Omega^{-1}$ (or Siemens, $\text{S}$)
        
          
        
- **Conductivity ($\sigma$):** The reciprocal of resistivity ($\rho$).
    
      
    
    $$\text{Conductivity} = \frac{1}{\rho}$$
    
    - **Unit:** $\text{mho/m}$ or $\text{Siemens/m}$ ($\text{S/m}$)
        
          
        
- **Relationship:**
    
    $$\rho \times \sigma = 1$$

- **Electric Current ($I$)**:
  $$I = \frac{Q}{t} \quad (\text{Ampere, A})$$
- **Ohm's Law**:
  $$V = I R \implies R = \frac{\rho L}{A}$$
  - Series Equivalent Resistance: $R_{\text{eq}} = R_1 + R_2 + R_3$
  - Parallel Equivalent Resistance: $\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$

---

## serires paralle
Here is a side-by-side comparison explaining the handwritten notes on **Series vs. Parallel Combination of Resistors**:

| **Feature**                           | **Series Combination**                                      | **Parallel Combination**                                                    |
| ------------------------------------- | ----------------------------------------------------------- | --------------------------------------------------------------------------- |
| **Current ($I$)**                     | **Same** across all resistors ($I$ is constant).            | **Different** through each branch ($I = I_1 + I_2 + I_3$).                  |
| **Voltage ($V$)**                     | **Different** across each resistor ($V = V_1 + V_2 + V_3$). | **Same** across all branches ($V$ is constant).                             |
| **Individual Voltages / Currents**    | $V_1 = I R_1$, $V_2 = I R_2$, $V_3 = I R_3$                 | $I_1 = \frac{V}{R_1}$, $I_2 = \frac{V}{R_2}$, $I_3 = \frac{V}{R_3}$         |
| **Equivalent Resistance Formula**     | $$R_{\text{eq}} = R_1 + R_2 + R_3$$                         | $$\frac{1}{R_{\text{eq}}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}$$ |
| **For $n$ Identical Resistors ($R$)** | $$R_{\text{eq}} = nR$$                                      | $$R_{\text{eq}} = \frac{R}{n}$$                                             |

## 2. Electrical Energy & Power

- **Joule's Law of Heating**:
- **TL;DR:**

  

- **Concept:** Current flowing through a wire generates heat because moving electrons collide with fixed atoms, transferring energy.
    
      
    
- **Main Formula (Joule's Law):**
    
      
    
    $$H = I^2 R t$$
    
    _(Heat = $\text{Current}^2 \times \text{Resistance} \times \text{Time}$)_
    
      
    
- **Quick Memory Trick:** Think **"I Square Art"** ($I^2 R t$).
    
      
    
- **Alternative Formulas:** $H = V I t = \frac{V^2 t}{R} = P t$
    
      
    
- **Key Applications:**
    
      
    - **Heaters/Irons:** High resistance generates heat.
        
          
        
    - **Bulbs:** Tungsten filament gets hot enough to glow without melting.
        
          
        
    - **Fuse Wire:** Low melting point wire melts during short circuits to protect appliances.
  $$H = I^2 R t = V I t = \frac{V^2}{R} t$$
- **Electrical Power ($P$)**:
  $$P = V I = I^2 R = \frac{V^2}{R}$$
- - **Definition:** Power ($P$) is the rate of electrical energy consumption per second.
    
- **Core Formula:** $P = VI$
    
- **Derived Formulas:**
    
    - $P = I^2 R$ _(for series)_
        
    - $P = \frac{V^2}{R}$ _(for parallel)_
        
    - $P = \frac{VQ}{t}$ _(charge rate form)_
        
- **SI Units:** **Watt ($\text{W}$)** or **Volt-Ampere ($\text{V}\cdot\text{A}$)**.
- 
- **Commercial Electrical Unit**:
  $$1\text{ Unit (kWh)} = 1000\text{ W} \times 3600\text{ s} = 3.6 \times 10^6\text{ Joules}$$

---
- **Lightning Conductor:** Uses a pointed metal rod connected to a copper plate buried underground to safely route lightning strikes into the earth.
    
- **Domestic Wires:** **Red** = Live, **Black** = Neutral, **Green** = Earth.
    
- **Indian AC Supply:** **$220\text{ V}$, $50\text{ Hz}$**, where current changes direction **twice per cycle** (every $\frac{1}{100}\text{ second}$).

## capacitor
**TL;DR:**

  

- **What it does:** Stores electrical energy and charge ($Q = CV$).
    
      
    
- **DC Behavior:**
    
      
    - **$t = 0$ (Turning ON):** Acts like a **plain wire** (current flows fully while charging).
        
          
        
    - **Steady State:** Acts like an **open circuit / broken wire** (blocks all DC once fully charged).
        
          
        
- **AC Behavior:** **Allows AC to pass** through continuously because the voltage constantly changes direction, keeping it in a state of perpetual charging and discharging ($X_C = \frac{1}{2\pi f C}$).
    
      
    
- **Formulas:**
    
      
    - Series: $\frac{1}{C_{\text{eq}}} = \frac{1}{C_1} + \frac{1}{C_2}$
        
          
        
    - Parallel: $C_{\text{eq}} = C_1 + C_2$
        
          
        
    - Energy: $U = \frac{1}{2} C V^2$
## 3. [[Magnetism]] & Electromagnetic Induction

- **Right-Hand Thumb Rule**: Direction of magnetic field around straight current-carrying wire.
- **Faraday's Law of Induction**: Induced EMF is proportional to rate of change of magnetic flux:
  $$\mathcal{E} = -\frac{d\Phi_B}{dt}$$
- **Lenz's Law**: Induced current flows in direction opposing the flux change causing it (Energy conservation principle).

---

## Navigation

- [[cds/physics/physics_overview|Physics Overview]]
- [[cds/physics/notes/formulas|Master Formulas]]
