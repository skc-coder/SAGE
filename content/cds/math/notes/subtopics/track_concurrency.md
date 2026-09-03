---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "HCF and LCM"
subtopic: "Circular Track Concurrency"
difficulty: "Medium"
tags: [cds, elementary-mathematics, lcm, circular-track, race, subtopic]
---

# Circular Track Concurrency & Race Masterclass

## The Ultimate Memory Trick: "START vs ANYWHERE"

When solving circular track problems, ask yourself **ONE single question**:

> **"Are they asking for meeting at the STARTING POINT, or meeting ANYWHERE on the track?"**

```text
                  ┌──────────────────────────────────────────────┐
                  │          Where do they need to meet?         │
                  └──────────────────────┬───────────────────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
     ┌───────────────────────┐                       ┌───────────────────────┐
     │   AT STARTING POINT   │                       │  ANYWHERE ON TRACK    │
     └───────────┬───────────┘                       └───────────┬───────────┘
                 │                                               │
    LCM of Individual Lap Times                    Distance / Relative Speed
      Direction DOES NOT Matter!                      Same Dir: (S1 - S2)
     Formula = LCM(t1, t2, t3)                        Opp Dir:  (S1 + S2)
```

---

## 🔍 Core Difference: Why Are The Two Methods Different?

| Feature | **Type 1: Meeting at STARTING POINT** | **Type 3: Meeting ANYWHERE on the Track** |
| :--- | :--- | :--- |
| **Meeting Location** | **Strictly locked to the 0m Start Line** | **Can happen at ANY random spot** (e.g. 142.5m mark) |
| **Physical Condition** | Every runner MUST complete **whole integer laps** | Runners do **NOT** need to complete whole laps |
| **Direction Impact** | **IRRELEVANT** (Same or Opposite gives same answer) | **CRITICAL** (Relative speed depends on direction) |
| **Calculation Method** | Direct **$\operatorname{LCM}(t_1, t_2, t_3)$** of lap times | Pairwise Relative Times **$\operatorname{LCM}(t_{AB}, t_{BC})$** |

---

## The 4 Exam Question Types

### TYPE 1: Meeting at the STARTING POINT (Most Common in CDS)

#### Question Wording:
*"$A, B, C$ start running around a circular track at the same time. When will they all meet again at the starting point?"*

#### Intuition:
- Runner $A$ passes the starting point at $t_1, 2t_1, 3t_1, \dots$ (Multiples of $t_1$).
- Runner $B$ passes the starting point at $t_2, 2t_2, 3t_2, \dots$ (Multiples of $t_2$).
- For all runners to be at the start at the exact same moment, the time MUST be a **common multiple** of all lap times.
- The **first time** this happens is the **Least Common Multiple (LCM)**.

#### Rule / Formula:
$$\mathbf{\text{Time to meet at START} = \operatorname{LCM}(t_1, t_2, t_3)}$$

> [!WARNING]
> **Direction does NOT matter at all for starting point questions!**  
> Whether $A, B, C$ run in the same direction or opposite directions, they pass the start line at the exact same time intervals ($t_1, t_2, t_3$).

#### Worked Example (Pathfinder Example 13):
$A = 250\text{ s}, B = 300\text{ s}, C = 150\text{ s}$.
$$\operatorname{LCM}(250, 300, 150) = 1500\text{ seconds} = \mathbf{25\text{ minutes}}$$

---

### TYPE 2: Two Runners Meeting ANYWHERE on the Track

#### Question Wording:
*"Two runners $A$ and $B$ with speeds $S_A$ and $S_B$ run on a track of length $L$. When do they meet anywhere on the track for the first time?"*

#### Intuition:
For two runners to meet anywhere on a circular track, the **faster runner must gain exactly 1 full lap ($L$) over the slower runner**.

#### Formula:
- **Same Direction:** Relative speed $= S_A - S_B$.
  $$\mathbf{T_{\text{meet}} = \frac{\text{Track Length } L}{S_A - S_B}}$$
- **Opposite Direction:** Relative speed $= S_A + S_B$.
  $$\mathbf{T_{\text{meet}} = \frac{\text{Track Length } L}{S_A + S_B}}$$

#### Alternative Formula (Using Lap Times $t_A, t_B$ directly):
- **Same Direction:** $\mathbf{T_{\text{meet}} = \frac{t_A \cdot t_B}{|t_A - t_B|}}$
- **Opposite Direction:** $\mathbf{T_{\text{meet}} = \frac{t_A \cdot t_B}{t_A + t_B}}$

---

### TYPE 3: Three or More Runners Meeting ANYWHERE on the Track for the First Time

#### Question Wording:
*"Three runners $A, B, C$ run around a circular track. When do all three meet anywhere on the track for the first time?"*

#### 💡 Mathematical Intuition: Why ONLY 2 Pairs ($t_{AB}$ and $t_{BC}$)? Why NOT all 3 pairs?

Let's demystify the magic!

1. **The Transitive Property of Meeting:**  
   If $A$ is at the exact same physical spot as $B$ (i.e. $A = B$), and $B$ is at the exact same physical spot as $C$ (i.e. $B = C$), then **mathematically and physically, $A$ MUST be at the same spot as $C$ ($A = C$)**!
2. **Redundancy of $t_{AC}$:**  
   - $t_{AB}$ is the time interval at which $A$ and $B$ overlap anywhere.
   - $t_{BC}$ is the time interval at which $B$ and $C$ overlap anywhere.
   - Any time $T$ that is a common multiple of $t_{AB}$ and $t_{BC}$ guarantees $A = B$ AND $B = C$.
   - By transitivity, $A = B = C$.  
   - Including $t_{AC}$ is mathematically redundant because if $A=B$ and $B=C$, $A=C$ is automatically guaranteed! Taking $\operatorname{LCM}(t_{AB}, t_{BC}, t_{AC})$ yields the exact same answer, but working with 2 pairs saves time!

#### Formula & Method:
1. **Find pairwise meeting times:**
   - $t_{AB} = \frac{L}{|S_A \pm S_B|}$
   - $t_{BC} = \frac{L}{|S_B \pm S_C|}$
2. **Take LCM of the fraction times:**
   $$\mathbf{T_{\text{All meet anywhere}} = \operatorname{LCM}(t_{AB}, \, t_{BC}) = \frac{\operatorname{LCM}(\text{Numerators})}{\operatorname{HCF}(\text{Denominators})}}$$

---

### TYPE 4: Number of Distinct Meeting Points on the Track

#### Question Wording:
*"How many distinct points on the circular track will two runners $A$ and $B$ meet?"*

#### 💡 Mathematical Proof & Intuition: Why $|a - b|$ and $a + b$?

Let two runners $A$ and $B$ have reduced speed ratio $a : b$ (where $\operatorname{GCD}(a, b) = 1$).  
This means: **In the time $T_{\text{start}}$ it takes both runners to complete a full cycle and return to the START line, Runner $A$ completes $a$ full laps, and Runner $B$ completes $b$ full laps.**

##### 1. Same Direction Case ($\text{Points} = |a - b|$):
- Runner $A$ covers $a$ laps, Runner $B$ covers $b$ laps in total cycle $T_{\text{start}}$.
- Relative lap difference = $|a - b|$.
- Every time the faster runner gains 1 full lap over the slower runner, they **meet once**.
- Therefore, in 1 full cycle back to start, they meet **$|a - b|$ times**.
- Since the speed ratio $a:b$ is co-prime, **all $|a - b|$ meeting locations are equally spaced and distinct**!

##### 2. Opposite Direction Case ($\text{Points} = a + b$):
- Runner $A$ moves clockwise $a$ laps, Runner $B$ moves counter-clockwise $b$ laps.
- Together, their combined total laps = $a + b$.
- Every time their combined distance equals 1 full lap, they **meet once**.
- Therefore, in 1 full cycle back to start, they meet **$a + b$ times** at $a + b$ distinct points!

#### Worked Example:
Speeds are $15\text{ m/s}$ and $25\text{ m/s}$ on a track.
1. Reduce speed ratio: $\frac{15}{25} = \frac{3}{5} \implies a = 3, b = 5$. ($\operatorname{GCD}(3,5)=1$).
2. **Same Direction**: $|5 - 3| = \mathbf{2 \text{ distinct points}}$.
3. **Opposite Direction**: $5 + 3 = \mathbf{8 \text{ distinct points}}$.

---

## Linked Practice Questions

- [[cds/math/notes/questions/q8|Question 8: Bell Ringing Concurrency Interval]]
- [[cds/math/notes/questions/q22|Question 22: Circular Track Concurrency Meeting Time]]

---

## Navigation

- [[cds/math/notes/subtopics/lcm_models|LCM Models & Remainder Theorems]]
- [[cds/math/notes/hcf_lcm|HCF and LCM Topic Page]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
