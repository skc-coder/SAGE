---
source1: https://www.youtube.com/watch?v=c2ULnLjXztQ
tags:
source:
---

📝 [[Problems - Alligation]]

---

### Core Concept
1. The percentage of total mixture removed = percentage of individual component liquids removed.
2. ratios of liquid components in total liquid removed = same ratio as in the mixture
	1. Ensure same volume across two cases of mixtures.
	2. ![](attachments/Pasted%20image%2020260427120057.png)


---

## Type 1: Replacement (Fixed Replacement)
When p% of a liquid solution is replaced by another liquid y:

$$x_{\text{final}} = x_{\text{initial}} \times \left(1-\frac{p}{100}\right)^n$$

where x=the other liquid, n = number of replacements

**Tip**: Find the fraction/percentage of liquid removed, then apply it to the decreasing liquid.

---

## Type 2: Replacement with Specific Ratio Change

### Method: Multiplying Factor

$$\frac{\text{Final Value}}{\text{Initial Value}} = k$$

Where k is the multiplying factor
### Example
- Initial ratio Milk:Water = 13:1 (Total 14 units)
- After replacement: 11:9 (Total 20 units)
- Find replacement fraction

$$k = \frac{11}{13}, \quad \text{Replacement} = 1 - \frac{11}{13} = \frac{2}{13}$$
(focus on decreasing liquid)
इस समस्या में मुख्य चुनौती यह है कि कुल मात्रा (Total Quantity) बदल रही है। रिप्लेसमेंट के सवालों में 'मल्टीप्लाइंग फैक्टर' (k) का नियम तभी सीधे काम करता है जब आप 'समान कुल मात्रा' में से दूध की तुलना करें।

यहाँ आपकी समस्या और उसके समाधान का विस्तृत विश्लेषण दिया गया है:

## 1. समस्या (The Problem)

- प्रारंभिक स्थिति: दूध:पानी = 13:1 (कुल 14 यूनिट)
- अंतिम स्थिति: दूध:पानी = 11:9 (कुल 20 यूनिट)

जब आप $k = \frac{11}{13}$ कहते हैं, तो आप यह मान रहे हैं कि 13 लीटर दूध में से अब केवल 11 लीटर बचा है। लेकिन यह तब तक सच नहीं है जब तक दोनों मिश्रणों का कुल वॉल्यूम एक जैसा न हो। 14 लीटर के मिश्रण का '11' और 20 लीटर के मिश्रण का '11' अलग-अलग मान रखते हैं।

---

## 2. सही समाधान (The Solution - Step by Step)

मल्टीप्लाइंग फैक्टर मेथड का सही उपयोग करने के लिए हमें कुल यूनिट्स को बराबर करना होगा:

स्टेप 1: कुल मात्रा समान करें (Equalize Total)  
14 और 20 का LCM 140 होता है।

- प्रारंभिक मिश्रण (x 10): दूध : पानी = $130 : 10$ (कुल 140)
- अंतिम मिश्रण (x 7): दूध : पानी = $77 : 63$ (कुल 140)

स्टेप 2: दूध (घटने वाले द्रव) पर ध्यान दें  
अब हमारे पास एक ही स्केल पर वैल्यूज़ हैं:

- प्रारंभिक दूध (Initial Value) = 130
- अंतिम दूध (Final Value) = 77

स्टेप 3: मल्टीप्लाइंग फैक्टर (k) निकालें  
$$k = \frac{\text{Final Value}}{\text{Initial Value}} = \frac{77}{130}$$

स्टेप 4: रिप्लेसमेंट फ्रैक्शन (Replacement Fraction)  
$$1 - k = 1 - \frac{77}{130} = \frac{53}{130}$$

---

## निष्कर्ष (Summary)

आपका $\frac{2}{13}$ वाला उत्तर गलत था क्योंकि आपने टोटल यूनिट्स (14 vs 20) के अंतर को नजरअंदाज कर दिया था।

याद रखने वाली बात: अनुपात के अंकों को सीधे तभी घटाएं या भाग दें जब उनका योग (Sum of Ratio) बराबर हो।

क्या आप एक ऐसा उदाहरण देखना चाहेंगे जहाँ कुल मात्रा पहले से ही बराबर हो, ताकि आप अपना शॉर्टकट इस्तेमाल कर सकें?
The replacement fraction (in this case, $\frac{53}{130}$) tells you exactly how much of the original mixture was removed and replaced with something else (usually water).

Here is the breakdown of what it signifies:

## 1. The "How Much" Part

It represents the proportion of the total volume that was taken out.

- If your container holds 130 liters, you removed 53 liters of the mixture and added back 53 liters of pure water.
- If the fraction was $\frac{1}{4}$, it would mean you replaced 25% of the total content.

## 2. The Impact on "Decreasing Liquid" (Milk)

Since you are removing a _mixture_ but adding back only _water_, the milk content can only go down.

- The fraction tells you the percentage drop in the milk's concentration.
- The multiplying factor $k$ (which was $\frac{77}{130}$) tells you that 77/130th of the original milk is still there. Therefore, the rest ($1 - k$) is what was lost during replacement.

## 3. Practical Usage

In exams, this fraction helps you find:

- The Quantity Replaced: If the total volume is 260L, the quantity replaced is $260 \times \frac{53}{130} = 106L$.
- The Original Volume: If you are told "106 liters were replaced," you can use the fraction to find the total volume ($106 \times \frac{130}{53} = 260L$).

Summary: It is the ratio of [Volume Removed] : [Total Volume of Container].

Would you like to see how this fraction changes if we do two successive replacements instead of just one?

---


## Type 3: Mixing Two Solutions

### When ratio of mixing is given:

We are given liquid ratios and need to find component liquid ratios in the new solution. 

Use **Ratio Method** — multiply to make liquid quantities in the given ratio, then sum individual components and find the ratio.

**Problem:** Solution A has Milk and Water in a **3:1** ratio. Solution B has them in a **5:3** ratio. If they are mixed in a **2:3 ratio**, what is the final ratio?

**Step 1: Equalize**

- Solution A: \(3 + 1 = 4\) units
- Solution B: \(5 + 3 = 8\) units
- _LCM of 4 and 8 is 8._
- Adjust A: Multiply by 2 \(\rightarrow \) **6 : 2** (Total 8)
- Adjust B: Multiply by 1 \(\rightarrow \) **5 : 3** (Total 8) [[1](https://www.tiktok.com/@freemathstutor_uk/video/7311062602359115041), [2](https://prepp.in/question/fill-in-the-blank-with-the-correct-option-in-three-645d2a01e8610180957d406a), [3](https://prepp.in/question/two-vessels-containing-35-litres-and-47-litres-qua-699df4db8d6f8545fcdae3a1)]

**Step 2: Apply Mixing Ratio (2:3)**

- Multiply A by 2: \((6 \times 2) : (2 \times 2) = \mathbf{12 : 4}\)
- Multiply B by 3: \((5 \times 3) : (3 \times 3) = \mathbf{15 : 9}\)

**Step 3: Sum Components**

- Milk: \(12 + 15 = 27\)
- Water: \(4 + 9 = 13\)
- **Final Ratio: 27 : 13**
### When ratio is NOT given:

We need to find how much of each liquid to mix. Use **Alligation Method**

### Alligation Rule
$$\frac{\text{Quantity of A}}{\text{Quantity of B}} = \frac{\text{(Average - B's value)}}{\text{(A's value - Average)}}$$

### Example
- Solution A: 78% concentration
- Solution B: 46% concentration  
- Desired: 75% concentration
- Ratio: $\frac{75-46}{78-75} = \frac{29}{3}$

---

## Type 4: Multiple Solutions Mixed

### Deviation Method (Fastest)
1. Find desired average
2. Calculate deviation for each: (Value - Average)
3. Sum of (Quantity × Deviation) = 0

### Example
- Solution A: 20% (3 parts)
- Solution B: 30% (5 parts)
- Solution C: 40% (? parts)
- Desired: 30%

$$3(20-30) + 5(30-30) + x(40-30) = 0$$
$$-30 + 0 + 10x = 0$$
$$x = 3$$

#doubt relation between wt. avg and alligation in general

---

## Type 5: Sequential Mixing

### Process
1. Calculate initial quantities in each vessel
2. Track changes after each transfer
3. Maintain ratio relationships

**Critical**: When removing from mixture, remove in the ratio of that mixture

---

📝 [[Problems - Alligation]]