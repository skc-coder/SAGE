---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Sequence and Series"
subtopic: "AM GM HM Inequalities"
difficulty: "Hard"
tags: [cds, elementary-mathematics, sequence-series, subtopic]
---

# Harmonic Progression & AM-GM-HM Fundamental Inequalities

## Theory, Intuition & Derivations

### 1. Harmonic Progression (HP)
A sequence $a_1, a_2, \dots, a_n$ is in HP if $\frac{1}{a_1}, \frac{1}{a_2}, \dots, \frac{1}{a_n}$ form an AP.
- Harmonic Mean $H$ of $a$ and $b$:
  $$\frac{1}{H} - \frac{1}{a} = \frac{1}{b} - \frac{1}{H} \implies \frac{2}{H} = \frac{1}{a} + \frac{1}{b} = \frac{a+b}{ab} \implies H = \frac{2ab}{a+b}$$

### 2. Proof of $A \ge G \ge H$
For two positive real numbers $a, b > 0$:

#### A. Proof of $A \ge G$
Consider $(\sqrt{a} - \sqrt{b})^2 \ge 0$:
$$a + b - 2\sqrt{ab} \ge 0 \implies a + b \ge 2\sqrt{ab} \implies \frac{a+b}{2} \ge \sqrt{ab} \implies A \ge G$$

#### B. Proof of $G \ge H$
Since $A \ge G$ for positive numbers $\frac{1}{a}$ and $\frac{1}{b}$:
$$\frac{\frac{1}{a} + \frac{1}{b}}{2} \ge \sqrt{\frac{1}{a} \cdot \frac{1}{b}} \implies \frac{a+b}{2ab} \ge \frac{1}{\sqrt{ab}} \implies \sqrt{ab} \ge \frac{2ab}{a+b} \implies G \ge H$$

Combining both gives:
$$A \ge G \ge H$$

#### C. Proof of $G^2 = A \cdot H$
$$A \cdot H = \left(\frac{a+b}{2}\right) \times \left(\frac{2ab}{a+b}\right) = ab = (\sqrt{ab})^2 = G^2$$

---

## Linked Practice Questions

- [[cds/math/notes/questions/q112|CDS Sequence & Series Q3: AP, HP, GP relationship transform]]

---

## Navigation

- [[cds/math/notes/sequence_series|Topic: Sequence and Series]]
- [[cds/math/math_overview|Elementary Mathematics Overview]]
