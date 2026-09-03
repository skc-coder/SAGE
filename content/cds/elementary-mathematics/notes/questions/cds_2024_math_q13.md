---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Trigonometry"
subtopic: "Heights and Distances"
question_type: "Two-point Angle of Elevation"
difficulty: "Medium"
source: "CDS 2024 I"
source_file_link: "[[content/cds/elementary-mathematics/test_sessions/2026-09-03_cds_mock_01|Mock Test 01]]"
question_number: "Q13"
status: "Wrong"
mistake_category: "Formula Misapplication"
tags: [cds, elementary-mathematics, trigonometry, heights-and-distances]
date: 2026-09-03
---

# CDS 2024 Q13

> **Question Statement**:
> An observer on top of a cliff $h$ meters high finds that the angles of depression of two ships moving directly towards the base of the cliff are $30^\circ$ and $45^\circ$. If the distance between the two ships is $100(\sqrt{3} - 1)$ meters, find the height of the cliff $h$.

> [!faq]- View Solution & Derivation
> Let the height of the cliff be $h$.
> Let the distance of the closer ship ($45^\circ$ angle) from the base be $x$.
> 
> From the triangle with the closer ship:
> $$\tan(45^\circ) = \frac{h}{x} \implies 1 = \frac{h}{x} \implies x = h$$
> 
> From the triangle with the farther ship ($30^\circ$ angle):
> $$\tan(30^\circ) = \frac{h}{x + 100(\sqrt{3}-1)}$$
> $$\frac{1}{\sqrt{3}} = \frac{h}{h + 100(\sqrt{3}-1)}$$
> $$h + 100(\sqrt{3}-1) = h\sqrt{3}$$
> $$h(\sqrt{3} - 1) = 100(\sqrt{3}-1)$$
> $$h = 100\text{ meters}$$

---

## Tier 1 Direct Question Variation

### Variation 1.1 (Modified Distance & Angles)
An observer standing on top of a tower of height $H$ observes two cars in a straight line with the base. The angles of depression are $45^\circ$ and $60^\circ$. If the distance between the cars is $50$ meters, what is the height of the tower $H$?

> [!faq]- View Solution
> Let distance of closer car be $d_1$:
> $$\tan(60^\circ) = \frac{H}{d_1} \implies d_1 = \frac{H}{\sqrt{3}}$$
> 
> Let distance of farther car be $d_1 + 50$:
> $$\tan(45^\circ) = \frac{H}{d_1 + 50} \implies H = d_1 + 50$$
> $$H = \frac{H}{\sqrt{3}} + 50 \implies H\left(1 - \frac{1}{\sqrt{3}}\right) = 50$$
> $$H\left(\frac{\sqrt{3}-1}{\sqrt{3}}\right) = 50 \implies H = \frac{50\sqrt{3}}{\sqrt{3}-1} = 25\sqrt{3}(\sqrt{3}+1) = 75 + 25\sqrt{3}\text{ meters}$$
