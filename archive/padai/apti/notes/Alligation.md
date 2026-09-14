---
source: https://www.youtube.com/watch?v=4XsebLB1R9o
tags:
---

📝 [[Problems - Alligation]]

---
## Core Concept
Ratio obtained is **inversely proportional** to quantity being mixed.

$$\text{Middle value or weigthed Average} = \frac{\sum(\text{Value} \times \text{Weight})}{\sum(\text{Weight})}$$

$$\text{Alligation Ratio} = \text{The factor that was "weighted" in the average}$$

![[Pasted image 20260403155621.png]]

## Profit/Loss Alligation
[[Profit & Loss]]
In general in allegation problems:

$$P\%_{avg} = \frac{P\%_1 \times CP_1 \times Q_1 + P\%_2 \times CP_2 \times Q_2}{CP_1 \times Q_1 + CP_2 \times Q_2}$$

The **weights are $(CP \times Q)$** (total investment):

$$\boxed{\frac{CP_1 Q_1}{CP_2 Q_2} = \frac{P\%_{avg} - P\%_2}{P\%_1 - P\%_{avg}}}$$

| Case | Weights | Ratio |
|------|---------|-------|
| Q same | CP | CP ratio |
| CP same | Q | Q ratio |
| Both vary | CP × Q | CP × Q ratio |

## Key Rules
- Always subtract same direction
- Identify what ratio needed first
- Convert %: $20\% = \frac{1}{5}$, $25\% = \frac{1}{4}$
- Eliminate fractions by multiplying by denominator
- Bolling average = runs given/wickets taken
- No loss or gain => SP = CP.

---

📝 [[Problems - Alligation]]



# Mixture & Alligation — Complete Master Notes

## 1. Core Concept & The Alligation Cross Method

Alligation is a fast arithmetic technique derived from weighted averages. It is used when two groups or ingredients of differing values/concentrations are combined into a single mixture.

  

```
       Quantity / Rate 1 (Q1)             Quantity / Rate 2 (Q2)
                 \                                 /
                  \                               /
                   Mean / Combined Value (Qm)
                          /             \
                         /               \
              (Qm - Q2) or (Q2 - Qm)   :   (Q1 - Qm) or (Qm - Q1)
                    [Ratio of base unit: n1 : n2]
```

### Mathematical Principle

If two groups with values $A$ and $B$ combine to give average $M$ (where $A > M > B$):

  

$$\frac{n_1}{n_2} = \frac{M - B}{A - M}$$

### Determining What the Resulting Ratio Represents

The output ratio ($n_1 : n_2$) always belongs to the **denominator entity** of the rates being compared:

  

- **Average Weight** ($\text{Total Weight} / \text{Number of Students}$) $\rightarrow$ Ratio of **Number of Students**.
    
      
    
- **Profit/Loss %** ($\text{Profit} / \text{Cost Price}$) $\rightarrow$ Ratio of **Cost Prices (or Quantities at CP)**.
    
      
    
- **Concentration %** ($\text{Solute Volume} / \text{Total Volume}$) $\rightarrow$ Ratio of **Total Volumes**.
    
      
    
- **Speed** ($\text{Distance} / \text{Time}$) $\rightarrow$ Ratio of **Time Taken**.
    
      
    

> [!CAUTION]
> 
> **Strict Homogeneity Rule:** All three values placed in the cross must represent the exact same unit, type, and baseline.
> 
>   
> 
> - If comparing cost prices, all three must be CP. Do **not** mix CP and SP directly.
>     
>       
>     
> - If one ingredient undergoes a loss, treat it as a **negative profit** (e.g., $18\%$ loss $= -18\%$).
>     
>       
>     

## 2. Fundamental Problem Archetypes & Methods

### Type 1: Simple Averages & Weighted Mixtures

Used to find the ratio of constituents given individual rates and the mixture rate.

  

- **Method:** Set $Q_1$, $Q_2$, and $Q_m$. Subtract diagonally (always larger value minus smaller value).
    
      
    
- **Common Trap:** Watch the exact wording of the target question (e.g., Ratio of Boys : Girls vs. Girls : Boys, or percentage of total from a specific source).
    
      
    

### Type 2: Profit & Loss with Mixing

When a seller sells parts of a commodity at different profit/loss percentages, yielding an overall profit/loss percentage.

  

- **Setup:**
    
      
    - Component 1: $+\%P_1$
        
          
        
    - Component 2: $+\%P_2$ (or $-\%L_2$ if loss)
        
          
        
    - Mean: $+\%P_m$
        
          
        
- **Resulting Ratio:** Ratio of the quantities sold at each rate.
    
      
    

> [!NOTE]
> 
> When negative values appear:
> 
>   
> 
> $$Q_m - (-L) = Q_m + L$$

### Type 3: The Selling Price to Cost Price Conversion

Often, the problem provides the CP of ingredients, but gives the **Selling Price (SP) and Profit %** of the mixture.

  

- **Method:** Never place the mixture's SP in the center. Calculate the mixture CP ($CP_m$) first:
    
      
    
    $$\text{If Profit} = P\% \implies CP_m = \frac{SP_m}{1 + \frac{P}{100}}$$
    
    Or use the unit method: $25\% = \frac{1}{4} \implies CP=4, \text{Profit}=1, SP=5$. Thus $CP_m = SP_m \times \frac{4}{5}$.
    
      
    
- **Then:** Apply the cross with $CP_1$, $CP_2$, and $CP_m$.
    
      
    

### Type 4: Pure Additions (Zero or Pure Concentrations)

When adding pure water or pure acid/milk into an existing solution:

  

- **Reference Substance Approach:** Focus exclusively on **one** constituent (e.g., either only alcohol or only water).
    
      
    - If adding **pure water** and tracking **alcohol**: Water contains **$0\%$ alcohol**.
        
          
        
    - If adding **pure water** and tracking **water**: Water contains **$100\%$ water**.
        
          
        
- **Pro-tip:** Choose whichever constituent makes one of the entries $0\%$, as subtraction becomes trivial.
    
      
    

### Type 5: Fractional Ratios & Scale Normalization

When solutions are given as ratios (e.g., Acid : Water $= 5:2$ and $8:5$ to achieve $9:4$):

  

- **Single-Component Fraction Method:**
    
      
    1. Pick one component (e.g., Acid).
        
          
        
    2. $A_1 = \frac{5}{7}$, $A_2 = \frac{8}{13}$, $A_m = \frac{9}{13}$.
        
          
        
    3. Clear fractions by multiplying all terms by $\text{LCM}(7, 13) = 91$:
        
          
        - $A_1' = 65$, $A_2' = 56$, $A_m' = 63$.
            
              
            
    4. Perform the standard integer cross:
        
          
        - $\vert{}65 - 63\vert{} = 2$
            
              
            
        - $\vert{}56 - 63\vert{} = 7 \implies \text{Ratio} = 7:2$.
            
              
            

### Type 6: Melting & Mixing Alloys in Specified Proportions

#### Case A: Equal Quantities / Equal Capacities

When two or more containers of equal total volume are mixed:

  

1. Write down component ratios for each container.
    
      
    
2. Sum the parts for each container (e.g., $5+3 = 8$ and $5+11 = 16$).
    
      
    
3. Find the LCM of the total parts (here, $\text{LCM}(8, 16) = 16$).
    
      
    
4. Multiply each ratio by the scale factor to make all total sums identical.
    
      
    
5. Directly add the corresponding scaled components together.
    
      
    

#### Case B: Unequal / Arbitrary Quantities

When mixed in ratio $k_1 : k_2$ (or volumes like $2\text{ kg} : 3\text{ kg}$):

  

1. First normalize each container to equal totals (as in Case A).
    
      
    
2. Multiply container 1's parts by $k_1$ and container 2's parts by $k_2$.
    
      
    
3. Sum the scaled components.
    
      
    

### Type 7: Invariant Tracking (Common Component Balancing)

Applies when mixing complex alloys or multi-liquid systems where one component is introduced via only a single source.

  

- **Method:**
    
      
    1. Identify the constituent that enters the final mixture from **only one** container (e.g., Tin present in $Y$ and $Z$, but completely absent in $X$).
          
        
    2. Because all Tin in $Z$ originates from $Y$, the relative ratio of Tin must be mathematically harmonized between $Y$ and $Z$.
        
          
        
    3. Scale the ratio of $Y$ and $Z$ so the Tin share matches.
        
          
        
    4. The residual difference between components in $Z$ and scaled components from $Y$ gives the exact contribution from container $X$.
        
          
        

### Type 8: Successive Replacement & Dilution Formula

Used when an initial quantity of pure (or mixed) liquid has $x$ units removed and replaced with another liquid, repeated $n$ times.

  

$$\frac{\text{Final Quantity of Original Liquid}}{\text{Total Volume}} = \left(\frac{\text{Initial Quantity}}{\text{Total Volume}}\right) \times \left(1 - \frac{x}{V}\right)^n$$

- **Generalized Step-by-Step Form:**
    
      
    
    $$\text{Final Proportion} = \text{Initial Proportion} \times \left(\frac{V - x_1}{V}\right) \times \left(\frac{V - x_2}{V}\right) \times \dots$$
    
- **Key Definitions:**
    
      
    - $\text{Initial Proportion} = 1$ if the starting liquid is pure ($100\%$).
        
          
        
    - If initial liquid is already diluted (e.g., Milk : Water $= 3:2$), $\text{Initial Proportion} = \frac{3}{5}$.
        
          
        
    - $V$ is the total volume after replacement (assuming volume removed $=$ volume added back).
        
          
        

### Type 9: Removal and Single-Component Replacement (Ratio Shift)

**Scenario:** A vessel has liquids $A$ and $B$ in ratio $r_1 : r_2$. A specific volume $x$ of the mixture is removed, and replaced with an equal volume of pure liquid $B$. The ratio becomes $r_3 : r_4$.

  

#### The 3-State Invariance Model

1. **State 1 (Initial):** Original full volume, ratio $= r_1 : r_2$.
    
      
    
2. **State 2 (After Removal of Mixture):**
    
      
    - Volume is reduced by $x$ liters.
        
          
        
    - **Crucial Rule:** The ratio of $A : B$ remains strictly $r_1 : r_2$ because drawing out a homogeneous mixture does not alter the concentration of what remains.
        
          
        
3. **State 3 (After Adding Pure $B$):**
    
      
    - Only liquid $B$ is added.
        
          
        
    - Liquid $A$ remains **strictly invariant** between State 2 and State 3.
        
          
        
    - Total volume of State 3 equals the total volume of State 1.
        
          
        

#### Step-by-Step Operational Procedure

1. Set State 2 ratio ($A:B$) and State 3 ratio ($A:B$).
    
      
    
2. **Normalize $A$:** Multiply ratios so that the value representing $A$ is identical in both states.
    
      
    
3. **Analyze $B$'s Increase:** The increase in units of $B$ from State 2 to State 3 equals the actual physical volume $x$ added.
    
      
    
    $$\Delta B \text{ units} = x \text{ liters} \implies 1 \text{ unit} = \frac{x}{\Delta B} \text{ liters}$$
    
4. **Compute Total Volume:** Calculate the total units in State 3.
    
      
    
    $$\text{Total Volume} = (\text{Units of } A + \text{Units of } B \text{ in State 3}) \times (1 \text{ unit value})$$
    
5. **Backtrack to State 1:** Distribute this Total Volume using the original State 1 ratio to find initial individual quantities.
    
      
    

## 3. Heuristics, Edge Cases & Caveats

> [!WARNING]
> 
> **Check Feasibility (Mean Value Boundary):**
> 
> For any real alligation, the combined average $Q_m$ **must strictly lie between** the two component values:
> 
>   
> 
> $$\min(Q_1, Q_2) < Q_m < \max(Q_1, Q_2)$$
> 
> - If a problem claims adding kerosene to a $60\%$ kerosene mixture results in a $20\%$ kerosene mixture, this is **physically impossible**.
>     
>       
>     
> - An alligation cross that yields negative weights indicates contradictory premises or unachievable criteria.
>     
>       
>     

- **Head & Legs (Simultaneous Equations via Alligation):**
    
      
    - You can solve 2-variable linear problems (like 2-legged ducks vs. 4-legged deer) using alligation:
        
          
        - Average legs per animal $= \frac{\text{Total Legs}}{\text{Total Animals}}$.
            
              
            
        - $Q_1 = 2$ (Ducks), $Q_2 = 4$ (Deer), $Q_m = \text{Average Legs}$.
            
              
            
        - The diagonal cross gives the exact ratio of Duck count to Deer count.
            
              
            
- **Variable Replacements / Non-Uniform Steps:**
    
      
    - When replacement volumes change per iteration (e.g., $20\text{ L}$ first, then $10\text{ L}$), never use exponents. Multiply each independent scale factor $\left(\frac{V - x_i}{V}\right)$ sequentially.
        
          
        
- **Reverse Calculation via Root Extraction:**
    
      
    - If a problem states that after $n$ operations the ratio is known, simplify the ratio to $\frac{\text{Original}}{\text{Total}}$ and take the $n$-th root to isolate the single-step dilution factor $\left(1 - \frac{x}{V}\right)$.
        

## Quick Reference Summary Sheet

|**Problem Variant**|**Primary Tool / Shortcut**|**Key Invariance to Exploit**|
|---|---|---|
|**Two commodities mixed at cost**|Alligation Cross on CP|Cost Price units|
|**SP given with profit %**|Convert $SP_m \rightarrow CP_m$ first|Baseline homogeneity|
|**Ratio solutions combined**|Convert to single-component fraction $\times \text{LCM}$|Total parts|
|**Containers of equal volume**|Equalize total ratio sums|Sum of ratio components|
|**Mixture drawn & single liquid added**|3-State Model (Compare State 2 & 3)|Quantity of untouched liquid|
|**Repeated removal & refill**|Dilution formula: $C_f = C_i \times (1 - x/V)^n$|Vessel total volume|