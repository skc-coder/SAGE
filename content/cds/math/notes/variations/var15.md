---
exam: "CDS"
subject: "Elementary Mathematics"
topic: "Rational Expressions"
variation_id: "var15"
derived_from: "Pathfinder Ch 16 Q15"
tags: [cds, math, variation, novel-problem]
---

# Variation 15: Double Shifted Rational Sum with Weighted Coefficients

## Problem Statement
Given that $x, y, z > 0$ satisfy the relation:
$$\frac{3x}{3x+2} + \frac{5y}{5y+4} + \frac{7z}{7z+6} = \frac{7}{4}$$

Find the exact value of the expression:
$$E = \frac{1}{3x+2} + \frac{2}{5y+4} + \frac{3}{7z+6}$$

## Solution Walkthrough

1. Express each term in the target expression $E$ in terms of the given terms.
   Notice the numerator scaling:
   * For the first term: $1 - \frac{3x}{3x+2} = \frac{2}{3x+2} \implies \frac{1}{3x+2} = \frac{1}{2}\left(1 - \frac{3x}{3x+2}\right)$
   * For the second term: $1 - \frac{5y}{5y+4} = \frac{4}{5y+4} \implies \frac{2}{5y+4} = \frac{1}{2}\left(1 - \frac{5y}{5y+4}\right)$
   * For the third term: $1 - \frac{7z}{7z+6} = \frac{6}{7z+6} \implies \frac{3}{7z+6} = \frac{1}{2}\left(1 - \frac{7z}{7z+6}\right)$

2. Factor out $\frac{1}{2}$ across the sum:
   $$E = \frac{1}{2} \left[ \left(1 - \frac{3x}{3x+2}\right) + \left(1 - \frac{5y}{5y+4}\right) + \left(1 - \frac{7z}{7z+6}\right) \right]$$

3. Simplify inside the brackets:
   $$E = \frac{1}{2} \left[ 3 - \left( \frac{3x}{3x+2} + \frac{5y}{5y+4} + \frac{7z}{7z+6} \right) \right]$$

4. Substitute the given sum value $\frac{7}{4}$:
   $$E = \frac{1}{2} \left[ 3 - \frac{7}{4} \right] = \frac{1}{2} \left[ \frac{5}{4} \right] = \frac{5}{8}$$

## Verification
* If $\frac{3x}{3x+2} = \frac{5y}{5y+4} = \frac{7z}{7z+6} = \frac{7}{12}$, then $1 - \frac{7}{12} = \frac{5}{12}$.
* Term 1: $\frac{1}{2} \times \frac{5}{12} = \frac{5}{24}$
* Term 2: $\frac{1}{2} \times \frac{5}{12} = \frac{5}{24}$
* Term 3: $\frac{1}{2} \times \frac{5}{12} = \frac{5}{24}$
* Sum $E = 3 \times \frac{5}{24} = \frac{5}{8}$. Verified!
