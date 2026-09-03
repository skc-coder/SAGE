---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Time and Work"
subtopic: "Pipes and Cisterns"
difficulty: "Medium"
tags: [cds, elementary-mathematics, time-and-work, subtopic]
---

# Pipes, Cisterns & Outlet Leakage Invariants

## Core Principles & Mathematical Model

Pipes and cisterns are physical analogies of time and work, with the key distinction that work can be either positive (inlet filling) or negative (outlet emptying/leakage).

### 1. Inlets and Outlets Sign Convention
- **Inlet Pipe $A$**: Fills a full tank in $a$ hours.
  $$\text{Filling Rate } R_A = +\frac{1}{a}$$
- **Outlet Pipe $C$ (or Leak)**: Empties a full tank in $c$ hours.
  $$\text{Emptying Rate } R_C = -\frac{1}{c}$$

### 2. Simultaneous Operation Equation
If two inlet pipes $A, B$ fill a tank in $a, b$ hours respectively and an outlet $C$ empties it in $c$ hours, the net fill rate per hour when all three operate together is:
$$R_{\text{net}} = \frac{1}{a} + \frac{1}{b} - \frac{1}{c} = \frac{bc + ac - ab}{abc}$$

The total time $T$ to fill the empty tank completely is:
$$T = \frac{1}{R_{\text{net}}} = \frac{abc}{bc + ac - ab}$$

---

### 3. Leakage Deduction Property
If an inlet pipe fills a tank in $T_{\text{in}}$ hours normally, but due to a leak at the bottom it takes $T_{\text{with\_leak}}$ hours to fill:
- Net filling rate:
  $$\frac{1}{T_{\text{with\_leak}}} = \frac{1}{T_{\text{in}}} - \frac{1}{T_{\text{leak}}}$$
- Leakage rate:
  $$\frac{1}{T_{\text{leak}}} = \frac{1}{T_{\text{in}}} - \frac{1}{T_{\text{with\_leak}}}$$
- Time taken by leak alone to empty full tank:
  $$T_{\text{leak}} = \frac{T_{\text{in}} \cdot T_{\text{with\_leak}}}{T_{\text{with\_leak}} - T_{\text{in}}}$$

---

## Linked Practice Questions
- [[cds/math/notes/questions/q43|Q43: Three Pipes Fill and Outlet Empty System]]

---

## Variations
- [[cds/math/notes/variations/var26|Variation 26: Variable Rate Cistern Filling with Altitude Leakage Threshold]]

---

## Navigation
- [[cds/math/notes/work|Time and Work Topic]]
- [[cds/math/math_overview|Subject Dashboard]]
