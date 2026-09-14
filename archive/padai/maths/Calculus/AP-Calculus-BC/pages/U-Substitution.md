Tags: #Theorem #FindingIntegrals 
sources: 
https://openstax.org/books/calculus-volume-1/pages/5-5-substitution
https://tutorial.math.lamar.edu/classes/calci/substitutionruleindefinite.aspx
https://tutorial.math.lamar.edu/Classes/CalcI/SubstitutionRuleIndefinitePtII.aspx
# U-Substitution

A method of integrating that can reverse some uses of the chain rule.


> **TIP:**
> As a shortcut to solve for $dx$, you can just use the formula,
> 
> $$\Large dx = \frac{du}{u'}$$
> 
> where $u'$ is the derivative of $u$.

> **TIP:**
> When picking a term to substitute $u$ with, try to pick a term whose derivative will cancel out with all the $x$ variables in the integrand.
> 
> Also try to ensure that the resulting integral with $u$ is something that you can integrate.

> **TIP:**
> You can always verify your solution by taking the derivative of it and seeing if you end up with the original integrand.

U-Substitution — Key Intuitions

1. To guess the right substitution, mentally differentiate the integrand using the chain rule.
   Whatever sits *inside* a composite function is your candidate for u.
   e.g. in ∫ sin(x²) · 2x dx → x² is inside sin, so u = x²

2. One substitution or type of substitution may not be enough.
   Some integrals need successive or multiple substitutions — don't force a single u to do all the work.

3. The integrand may need algebraic manipulation before or after substitution.
   Multiply/divide by constants, complete the square, factor — whatever makes du appear cleanly.

4. If the full integrand doesn't collapse into u and du,
   solve for the leftover variable explicitly in terms of u and substitute that too.
   e.g. if u = x + 1, then x = u − 1 — replace every x, not just part of it.