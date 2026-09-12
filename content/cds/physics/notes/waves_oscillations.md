---
exam: "CDS"
subject: "Physics"
topic: "Waves and Oscillations"
difficulty: "Medium"
tags: [cds, physics, waves, SHM, sound, Doppler, SONAR]
---

# Waves and Oscillations

Simple Harmonic Motion (SHM), Wave Classification, Sound Propagation, Doppler Effect, and Applications (SONAR, Echo).

---

## 1. Simple Harmonic Motion (SHM)

Periodic motion where restoring force is directly proportional to displacement and directed towards equilibrium:
$$F = -k x \implies a = -\omega^2 x$$

- Displacement Equation:
  $$x(t) = A \sin(\omega t + \phi)$$
- Simple Pendulum Time Period:
  $$T = 2\pi \sqrt{\frac{L}{g}}$$
  *(Period depends strictly on pendulum length $L$ and acceleration due to gravity $g$; independent of bob mass.)*

---

## 2. Wave Mechanics & Sound

- **Wave Speed Formula**:
  $$v = f \lambda = \frac{\lambda}{T}$$
- **Transverse Waves**: Particle oscillation perpendicular to wave propagation (e.g., light waves, plucked string).
- **Longitudinal Waves**: Particle oscillation parallel to wave propagation (e.g., sound waves in air).
- **Speed of Sound in Air**:
  $$v = \sqrt{\frac{\gamma R T}{M}} \approx 332\text{ m/s at } 0^\circ\text{C}$$
  - Speed increases with temperature ($+0.61\text{ m/s per } ^\circ\text{C}$ elevation).
  - Speed increases with humidity (moist air is less dense than dry air).
  - Speed is independent of pressure.

---

## 3. Acoustic Phenomena & Applications

- **Audible Frequency Spectrum**:
  - Infrasonic: $< 20\text{ Hz}$ (Earthquakes, elephants).
  - Audible Range: $20\text{ Hz} - 20,000\text{ Hz}$ ($20\text{ kHz}$).
  - Ultrasonic: $> 20,000\text{ Hz}$ (Bats, SONAR, medical ultrasound).
- **SONAR (Sound Navigation and Ranging)**: Uses ultrasonic waves to calculate ocean depth $d$:
  $$d = \frac{v \times t}{2}$$
- **Doppler Effect**: Apparent shift in observed wave frequency due to relative motion between source and observer:
  $$f' = f \left(\frac{v \pm v_o}{v \mp v_s}\right)$$

---

| **Medium Category** | **Medium (NCERT Standard at 25∘C)** | **Speed (v)**     | **Determining Factors & Governing Formula**     | **Physical Reason for the Relative Order**                                                                                      |
| ------------------- | ----------------------------------- | ----------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| **Solids**          | **Aluminium**                       | $6420\text{ m/s}$ | $v = \sqrt{\dfrac{Y}{\rho}}$                    | High specific stiffness: low density ($\sim 2700\text{ kg/m}^3$) with good elasticity gives the highest $\frac{Y}{\rho}$ ratio. |
|                     | **Nickel**                          | $6040\text{ m/s}$ | • $Y$: Young's Modulus (tensile elasticity)     | High stiffness balances its relatively high density.                                                                            |
|                     | **Steel**                           | $5960\text{ m/s}$ | • $\rho$: Density (inertia)                     | Iron alloyed with carbon increases lattice rigidity and stiffness with minimal density addition.                                |
|                     | **Iron**                            | $5950\text{ m/s}$ |                                                 | Slightly lower stiffness than steel at similar density.                                                                         |
|                     | **Brass**                           | $4700\text{ m/s}$ |                                                 | Copper-zinc alloy has a lower Young's modulus compared to ferrous metals and nickel.                                            |
|                     | **Glass (Flint)**                   | $3980\text{ m/s}$ |                                                 | Amorphous non-crystalline structure results in lower bulk tensile elasticity than metals.                                       |
| **Liquids**         | **Sea Water**                       | $1531\text{ m/s}$ | $v = \sqrt{\dfrac{B}{\rho}}$                    | Dissolved mineral salts increase bulk modulus (incompressibility) significantly more than density.                              |
|                     | **Distilled Water**                 | $1498\text{ m/s}$ | • $B$: Bulk Modulus (resistance to compression) | Strong 3D hydrogen bonding network makes water much stiffer against compression than organic solvents.                          |
|                     | **Ethanol**                         | $1207\text{ m/s}$ | • $\rho$: Density                               | Longer carbon chain than methanol provides stronger intermolecular dispersion forces, raising bulk modulus.                     |
|                     | **Methanol**                        | $1103\text{ m/s}$ |                                                 | Short chain, low intermolecular packing density, and highest compressibility among common exam solvents.                        |
| **Gases**           | **Hydrogen**                        | $1284\text{ m/s}$ | $v = \sqrt{\dfrac{\gamma R T}{M}}$              | Lowest molar mass ($M = 2\text{ g/mol}$); minimal molecular inertia allows rapid particle collision.                            |
|                     | **Helium**                          | $965\text{ m/s}$  | • $\gamma$: Adiabatic index ($C_p / C_v$)       | Monatomic gas with very low molar mass ($M = 4\text{ g/mol}$) and high $\gamma = 1.67$.                                         |
|                     | **Air**                             | $346\text{ m/s}$  | • $T$: Temperature                              | Diatomic mix ($\text{N}_2, \text{O}_2$) with moderate average molar mass ($M \approx 29\text{ g/mol}$).                         |
|                     | **Oxygen**                          | $316\text{ m/s}$  | • $M$: Molar Mass (inertia per mole)            | Heavier diatomic gas ($M = 32\text{ g/mol}$) than bulk air.                                                                     |
|                     | **Sulphur Dioxide**                 | $213\text{ m/s}$  | • $R$: Universal gas constant                   | Heavy polyatomic gas ($M = 64\text{ g/mol}$); high molecular inertia yields the slowest speed.                                  |
|                     |                                     |                   |                                                 |                                                                                                                                 |


---

- **Human Hearing Delay:** The brain holds sound for **$0.1\text{ s}$** (persistence of hearing); an echo must arrive after this delay to be heard separately.
    
      
    
- **Round Trip:** Sound travels to the wall and back, covering a distance of **$2d$**.
    
      
    
- **The Math:** At $22^\circ\text{C}$, the speed of sound is $344\text{ m/s}$:
    

$$d = \frac{v \times t}{2} = \frac{344 \times 0.1}{2} = \mathbf{17.2\text{ m}}$$

- At **$0^\circ\text{C}$**: **$331\text{ m/s}$** (often approximated as $330\text{ m/s}$ or $332\text{ m/s}$)
    
      
    
- At **$22^\circ\text{C}$**: **$344\text{ m/s}$**

- Hitting a tuning fork harder increases its vibration amplitude ($A$), pushing air molecules with greater force $\implies$ **louder sound (higher intensity)**, but the note (frequency $f$) stays unchanged.
    
- Singing a high note (high $f$) vs. a low bass note (low $f$) does not automatically make the high note louder or carry more energy; they can both be sung at a whisper or a roar.
    
- Therefore, exams test the rule: **Intensity/Loudness is controlled by Amplitude ($A^2$), independent of Frequency ($f$)**.



- **Core Idea:** Trapping or guiding sound waves by bouncing them repeatedly off surfaces stops energy from scattering, making faint sounds loud or projecting them in a specific direction.
    
      
    
- **Megaphones & Horns:** Sound bounces off the conical tube's walls, focusing the wave into a single forward beam instead of dispersing.
    
      
    
- **Stethoscope:** Heart sounds undergo **multiple internal reflections** inside the narrow rubber tubing, reaching the doctor's ears with almost zero loss of volume.
    
      
    
- **Curved Ceilings & Soundboards:** Sound bounces off concave surfaces (like a satellite dish) to distribute sound evenly across every row of an auditorium or project it forward from behind the stage.

| Category       | Frequency Range     | Key Producers / Detectors                     |
| -------------- | ------------------- | --------------------------------------------- |
| **Infrasound** | <20 Hz              | Whales, Elephants, Rhinos, Earthquakes        |
| **Audible**    | 20 Hz−20 kHz        | Human adults (Children up to 25 kHz)          |
| **Ultrasound** | >20 kHz (20,000 Hz) | Bats, Dolphins, Rats, Dogs (up to ∼40–50 kHz) |
|                |                     |                                               |



- **Cleaning:** Ultrasonic vibrations create cavitation bubbles in liquids to scrub hard-to-reach, delicate parts.
    
      
    
- **Flaw Detection:** Waves reflect early if they hit internal cracks in metal blocks (non-destructive test; safer alternative to ionizing X-rays).
    
      
    
- **Machining:** High-frequency energy paired with abrasive slurries cuts and drills brittle, hard materials like diamonds.
    
      
    
- **Medicine:**
    
      
    - **Echocardiography:** Maps heart structures; uses the **Doppler effect** to track blood flow.
        
          
        
    - **Ultrasonography:** Safe internal imaging (pregnancy, organ scans) and breaking stones without ionizing radiation.
        
          
        
- **Nature:** Bats and porpoises navigate and hunt via ultrasonic echolocation.
    
      
    
- **Generation:** Produced electrically using **piezoelectric materials** (e.g., quartz crystals).


- **What it is:** **SO**und **N**avigation **A**nd **R**anging—uses **ultrasound** to map underwater objects because radio waves/radar fail in water.
    
      
    
- **Core Principle:** **Echo ranging** (reflection of sound waves).
    
      
    
- **Two Key Parts:**
    
      
    - **Transmitter:** Sends out ultrasonic pulses.
        
          
        
    - **Detector:** Catches the reflected pulses.
        
          
        
- **The Formula:** Covers round-trip distance $2d$:
    
      
    

$$d = \frac{v \times t}{2}$$

- **Primary Uses:** Measuring ocean depth, spotting icebergs/submarines/shipwrecks, and finding fish shoals.




- **EM Nature:** Gamma rays and X-rays are 100% electromagnetic waves—just with the shortest wavelengths, highest frequencies, and maximum photon energy ($E = h\nu$).
    
      
    
- **Radio Waves:** Huge wavelengths bend around obstacles and terrain, making them ideal for long-distance broadcasts.
    
      
    
- **Microwaves:** Frequencies flip water molecules back and forth to heat food quickly, and pass clean through the ionosphere for satellite signals.
    
      
    
- **Infrared:** Matches the vibration frequencies of chemical bonds to transfer heat (grills) and lets cameras see objects by their natural heat glow.
    
      
    
- **Visible Light:** Matches the exact energy needed to trigger chemical sight receptors in our eyes without damaging cells.
    
      
    
- **Ultraviolet:** High energy kicks dye electrons up so they glow on banknotes (fluorescence), and damages the DNA of microbes for disinfection.
    
      
    
- **X-Rays:** Photons pass through soft tissue but get blocked by dense, high-atomic-number materials like bone calcium and structural metals to cast sharp shadow images.
    
      
    
- **Gamma Rays:** Massive nuclear energy tears apart atoms and rips double-stranded DNA, killing cancer cells and sterilizing medical tools right through their sealed packaging.


|**Ray / Radiation**|**Nature**|**Electric Charge**|**Rest Mass**|**Production Mechanism**|**Deflection in Electric / Magnetic Field?**|
|---|---|---|---|---|---|
|**Cathode Rays**|Beam of fast-moving electrons ($e^-$)|Negative ($-1e$ or $-1.6 \times 10^{-19}\text{ C}$)|$9.11 \times 10^{-31}\text{ kg}$|Emitted from the cathode of a discharge tube under low pressure and high voltage.|**Yes** (deflects toward positive electric plate)|
|**Anode / Canal Rays**|Stream of positive gas ions ($H^+, He^+$, etc.)|Positive ($+ne$, depends on gas)|Depends on gas; minimum is proton ($1.67 \times 10^{-27}\text{ kg}$)|Formed in discharge tubes behind a perforated cathode by ionization of residual gas.|**Yes** (deflects toward negative electric plate)|
|**Alpha Rays ($\alpha$)**|Doubly ionized Helium nuclei ($He^{2+}$: 2 protons, 2 neutrons)|Positive ($+2e$ or $+3.2 \times 10^{-19}\text{ C}$)|$\sim 4\text{ amu}$ ($6.64 \times 10^{-27}\text{ kg}$)|Spontaneous nuclear disintegration of heavy radioactive nuclei (e.g., Uranium, Radium).|**Yes** (deflects toward negative plate; slight deflection due to high mass)|
|**Beta-Minus ($\beta^-$) Rays**|High-speed nuclear electrons|Negative ($-1e$ or $-1.6 \times 10^{-19}\text{ C}$)|$9.11 \times 10^{-31}\text{ kg}$|Nuclear weak decay when a neutron converts into a proton ($n \to p + e^- + \bar{\nu}_e$).|**Yes** (strongly deflects toward positive plate)|
|**Beta-Plus ($\beta^+$) Rays**|High-speed positrons (antielectrons)|Positive ($+1e$ or $+1.6 \times 10^{-19}\text{ C}$)|$9.11 \times 10^{-31}\text{ kg}$|Nuclear decay when a proton converts into a neutron ($p \to n + e^+ + \nu_e$).|**Yes** (strongly deflects toward negative plate)|
|**X-Rays**|High-energy electromagnetic photons|**Neutral ($0$)**|**Zero**|High-speed cathode rays decelerating upon hitting a heavy metal target (e.g., Tungsten) in a Coolidge tube (Bremsstrahlung & characteristic transitions).|**No** (passes straight through unperturbed)|
|**Gamma Rays ($\gamma$)**|Highest-energy electromagnetic photons|**Neutral ($0$)**|**Zero**|Nuclear de-excitation when an excited nucleus drops to a lower energy state following $\alpha$ or $\beta$ decay.|**No** (passes straight through unperturbed)|
|**Cosmic Rays**|Energetic particles (mostly protons $\sim 90\%$, $\alpha$ particles $\sim 9\%$, heavy ions)|Positive (mostly $+1e$)|Mostly proton mass|Astrophysical phenomena outside the solar system (supernovae, active galactic nuclei).|**Yes** (deflected by Earth's geomagnetic field)|

**Key Differences to Remember for Exams**

  

- **EM Waves vs. Particle Streams:** X-rays and Gamma rays are massless, uncharged photons ($q = 0$). Alpha, Beta, Cathode, and Canal rays are physical particle beams carrying mass and charge.
    
      
    
- **X-ray vs. Gamma Ray Origin:** Both are uncharged EM waves, but **X-rays originate from electron transitions outside the nucleus**, whereas **Gamma rays originate from inside the nucleus**.
    
      
    
- **Penetrating Power:** $\gamma > \beta > \alpha$ (Gamma penetrates several centimeters of lead; Alpha is stopped by a single sheet of paper).
    
      
    
- **Ionizing Power:** $\alpha > \beta > \gamma$ (Alpha is the most heavily ionizing due to its large $+2e$ charge and mass).





**Question (CDS II 2020):**

  

A sound wave having a frequency of $300\text{ Hz}$ is travelling in an unknown medium. Its wavelength is not known. It travels a distance equal to $150$ times its wavelength in time $t$. The value of $t$ is:

  

a) $0.5\text{ s}$

  

b) $1\text{ s}$

  

c) $1.5\text{ s}$

  

d) $2\text{ s}$

  

**Answer:**

  

The correct option is **a) 0.5 s**.

  

- **Given:**
    
      
    - Frequency ($f$) = $300\text{ Hz}$
        
          
        
    - Distance ($d$) = $150 \lambda$
        
          
        
- **Formulas:**
    
      
    - Wave speed: $v = f \times \lambda$
        
          
        
    - Distance: $d = v \times t$
        
          
        
- **Calculation:**
    
    $$150 \lambda = (f \times \lambda) \times t$$
    
    $$150 = f \times t$$
    
    $$t = \frac{150}{f} = \frac{150}{300} = \mathbf{0.5\text{ s}}$$
**Question (NDA I 2023):**

  

Which one among the following is true for the speed of sound in a given medium?

  

a) speed of sound remains same at all frequency

  

b) speed of sound is faster at higher frequency

  

c) speed of sound is slower at higher frequency

  

d) speed of sound is slower at higher wavelengths

  

**Answer:**

  

The correct option is **a) speed of sound remains same at all frequency**.

  

- **Why:** The speed of sound depends strictly on the physical properties of the medium itself—its elasticity and density ($v = \sqrt{\frac{E}{\rho}}$) as well as its temperature—not on the characteristics of the source emitting it.
    
      
    
- **Frequency vs. Wavelength:** In the wave relation $v = f \lambda$, if you increase the frequency ($f$), the wavelength ($\lambda$) shortens proportionately so that the product $v$ remains constant:
    
      
    

$$v = \text{constant} \implies \lambda \propto \frac{1}{f}$$

- **Intuition:** If sounds of different frequencies traveled at different speeds in air, a live music performance would be unintelligible from the back of an auditorium, as high-pitched violin notes and deep drum beats would reach your ears at different times.

**Question (CDS II 2021):**

  

A sound wave has a frequency of $4\text{ kHz}$ and wavelength $30\text{ cm}$. How long will it take to travel $2.4\text{ km}$?

  

a) $2\text{ s}$

  

b) $0.6\text{ s}$

  

c) $1\text{ s}$

  

d) $8\text{ s}$

  

**Step-by-Step Solution:**

  

- **Convert all given values into SI units:**
    
      
    - Frequency ($f$) = $4\text{ kHz} = 4 \times 1000 = 4000\text{ Hz}$
        
          
        
    - Wavelength ($\lambda$) = $30\text{ cm} = \frac{30}{100} = 0.3\text{ m}$
        
          
        
    - Distance ($d$) = $2.4\text{ km} = 2.4 \times 1000 = 2400\text{ m}$
        
          
        
- **Calculate the speed of the sound wave ($v$):**
    
      
    
    $$v = f \times \lambda$$
    
    $$v = 4000\text{ Hz} \times 0.3\text{ m} = 1200\text{ m/s}$$
    
- **Calculate time taken ($t$):**
    
      
    
    $$\text{Time } (t) = \frac{\text{Distance } (d)}{\text{Speed } (v)}$$
    
    $$t = \frac{2400\text{ m}}{1200\text{ m/s}} = \mathbf{2\text{ s}}$$
    

**Answer:**

  

The correct option is **a) 2 s**.



**Question (CAPF 2020):**

  

The radar used by police to check overspeeding vehicles works on the principle of:

  

a) Raman effect

  

b) Induction effect

  

c) Doppler effect

  

d) Coulomb effect

  

**Answer:**

  

The correct option is **c) Doppler effect**.

  

- **How it works (Doppler Radar):**
    
      
    - The speed gun fires a beam of electromagnetic waves (microwaves or radio waves) of a known frequency ($f$) at a moving vehicle.
        
          
        
    - The moving vehicle reflects these waves back to the radar detector.
        
          
        
    - Because the target is moving relative to the gun, the reflected wave experiences an apparent frequency shift ($\Delta f$):
        
          
        - **Vehicle approaching:** Reflected frequency increases (blue shift).
            
              
            
        - **Vehicle moving away:** Reflected frequency decreases (red shift).
            
              
            
- **Speed Calculation:** The internal computer measures this frequency difference ($\Delta f$), which is directly proportional to the vehicle's speed ($v$):
    
      
    

$$\Delta f \approx \frac{2v}{c} f$$

**Why Other Options Are Wrong:**

  

- **Raman effect:** Inelastic scattering of photons by matter resulting in a change in vibrational/rotational energy states (used in chemical spectroscopy).
    
      
    
- **Induction effect:** Electromagnetic induction (generating current via a changing magnetic field) or inductive electronic displacement in chemistry.
    
      
    
- **Coulomb effect / law:** Electrostatic attraction or repulsion between stationary electric charges.
## Navigation

- [Physics Overview](/cds/physics/physics_overview)
- [Master Formulas](/cds/physics/notes/formulas)
