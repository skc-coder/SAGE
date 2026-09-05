The [Basic Proportionality Theorem](https://www.khanacademy.org/math/ncert-class-10/xd6a17b08edbd2443:triangles-ncert-new/xd6a17b08edbd2443:basic-proportionality-theorem-thales-theorem-and-its-converse/v/basic-proportionality-theorem), also known as Thales' Theorem, states that ==if a line is drawn parallel to one side of a triangle to intersect the other two sides, it divides those two sides in the same ratio==.

Statement

In △ ABC, if a line DE is drawn parallel to BC such that it meets AB at D and AC at E, then:  
\(\frac{AD}{DB}=\frac{AE}{EC}\)

and mid point theorem dervies from it
### centers of traaingle

To make these formulas second nature, strip away the algebra and look directly at the geometric geometry that forces them to be true.

  Here is how to see the geometric mechanism behind each inradius formula so they stick effortlessly:

  

**The Core Picture: What is Inradius ($r$)?**

The incircle sits snugly trapped inside the triangle, touching all three walls (edges). The incenter is the center point, and $r$ is the perpendicular distance from this center straight to any of the three sides.

  

**1. General Triangle: $r = \frac{\Delta}{s}$**

  

- **The Tent / Pizza Slice Vision:** Connect the incenter to all three vertices ($A, B, C$). This slices the big triangle into three smaller internal triangles, each having one of the outer sides ($a, b, c$) as its base.
    
      
    
- **Shared Height ($r$):** The height of every single one of these three smaller triangles is identical—it is simply the inradius $r$, because the circle touches all three sides perpendicularly.
    
      
    
- **Summing the Pieces:**
    
      
    
    $$\text{Total Area } (\Delta) = \frac{1}{2}ar + \frac{1}{2}br + \frac{1}{2}cr = r \left(\frac{a + b + c}{2}\right) = r \cdot s$$
    
    $$\implies r = \frac{\Delta}{s}$$
    
    _(where $s$ is the semi-perimeter)_
    
      
    
- **Instant Anchor:** The area is simply the perimeter's half-weight ($s$) expanded outward by radius $r$.
    
      
    

**2. Equilateral Triangle: $r = \frac{\text{Side}}{2\sqrt{3}}$**

  

- **The $2:1$ Split Again:** In an equilateral triangle, the incenter is also the centroid. The centroid cuts the total altitude $h$ into two pieces:
    
      
    - Top $2/3$ stretches outward to the sharp corners $\implies R = \frac{a}{\sqrt{3}}$.
        
          
        
    - Bottom $1/3$ drops straight down to touch the flat edge $\implies r$.
        
          
        
- **The Math in One Step:** Since total height $h = \frac{\sqrt{3}}{2}a$:
    
      
    
    $$r = \frac{1}{3} h = \frac{1}{3} \left(\frac{\sqrt{3}}{2}a\right) = \frac{a}{2\sqrt{3}}$$
    
- **Visual Symmetry:** Notice that the denominator here ($2\sqrt{3}$) is exactly twice the denominator of $R$ ($\sqrt{3}$), locking in $r = \frac{R}{2}$.
    
      
    

**3. Right-Angled Triangle: $r = \frac{B + P - H}{2}$**

  

- **The Corner Square:** Look at the $90^\circ$ corner formed by Base ($B$) and Perpendicular ($P$). The two radii drawn to these legs meet them at $90^\circ$. With three right angles already in place, the fourth is also $90^\circ$, forming an $r \times r$ square right at the corner.
    
      
    
- **Tangents from a Point:** The two tangent segments from any vertex to a circle are always equal:
    
      
    - Along the base, the segment next to the right angle is $r$, leaving $B - r$ for the remaining part.
        
          
        
    - Along the height, the segment next to the right angle is $r$, leaving $P - r$ for the remaining part.
        
          
        
- **Rebuilding the Hypotenuse ($H$):** Those two leftover segments wrap around and meet along the hypotenuse:
    
      
    
    $$H = (B - r) + (P - r) = B + P - 2r$$
    
    $$2r = B + P - H \implies r = \frac{B + P - H}{2}$$
    
- **Instant Anchor:** $(B + P)$ is walking around the two legs; $H$ is the diagonal shortcut. The difference between the long walk and the shortcut is exactly the overlap of two radii ($2r$).

**The Core Picture: What is Circumradius ($R$)?**

The circumcircle passes through all three sharp corners (vertices) of a triangle. The circumcenter is the single pivot point equally far from every corner.

  

**1. General Triangle: $R = \frac{abc}{4\Delta}$**

  

- **Why the Sine Rule holds:** Imagine a side $a$ acting as a chord inside a circle of radius $R$. If you open the angle $\angle A$ wider, the chord $a$ gets longer. When the angle hits $90^\circ$ ($\sin 90^\circ = 1$), the chord stretches all the way across the circle to become the full diameter ($2R$). That is the visual anchor:
    
      
    
    $$\text{Chord length} = \text{Diameter} \times \sin(\text{angle facing it}) \implies a = 2R \sin A$$
    
- **Turning it into Area ($\Delta$):** The area of any triangle is $\frac{1}{2}bc \sin A$. From the chord relation, $\sin A = \frac{a}{2R}$. Drop that into the area formula:
    
      
    
    $$\Delta = \frac{1}{2}bc \left(\frac{a}{2R}\right) = \frac{abc}{4R} \implies R = \frac{abc}{4\Delta}$$
    
- **Instant Mental Check:** $abc$ has cubic dimensions ($\text{length}^3$), and area $\Delta$ is quadratic ($\text{length}^2$). Dividing them yields linear length ($\text{length}^1$), which matches radius $R$.
    
      
    

**2. Equilateral Triangle: $R = \frac{a}{\sqrt{3}}$**

  

- **The Balance Point:** In a perfectly symmetric triangle, every special center—centroid, circumcenter, incenter—collapses into the exact same point.
    
      
    
- **The $2:1$ Split:** The centroid always cuts every median/altitude into a $2:1$ ratio:
    
      
    - The long top piece ($2/3$) reaches outward to the corners $\implies$ **Circumradius ($R$)**.
        
          
        
    - The short bottom piece ($1/3$) drops straight to the flat edges $\implies$ **Inradius ($r$)**.
        
          
        
- **Visualizing the numbers:** Total height is $h = \frac{\sqrt{3}}{2}a$. Taking two-thirds gives:
    
      
    
    $$R = \frac{2}{3} \left(\frac{\sqrt{3}}{2}a\right) = \frac{a}{\sqrt{3}}$$
    
- **The Instant Link ($R = 2r$):** Since $R$ is $2/3$ of the height and $r$ is $1/3$, $R$ is naturally twice $r$.
    
      
    

**3. Right-Angled Triangle: $R = \frac{\text{Hypotenuse}}{2}$**

  

- **The Half-Box Vision:** Take any right-angled triangle and duplicate it to form a rectangle. The diagonal of this rectangle is the hypotenuse ($H$).
    
      
    
- **Thales' Theorem:** The diagonals of a rectangle bisect each other and are completely equal. Their intersection point sits at identical distances from all four corners.
    
      
    
- Therefore, the exact midpoint of the hypotenuse _is_ the circumcenter. The distance from that midpoint to any vertex is simply half the hypotenuse:
    
      
    
    $$R = \frac{H}{2}$$
    

Would you like to explore how these circumradius properties connect directly with the inradius ($r$) formulas?




# Right traingles lenght and similarity proofs

![[Pasted image 20260905070425.png]]


# incenter
angle formula ![[Pasted image 20260905070635.png]]## 1. Interior Angle Bisector Theorem (Angle at Incenter)

- Name: Interior Angle Bisector Theorem (Angle at Incenter)
- Statement:

> _"The angle formed by the intersection of the interior angle bisectors of any two angles of a triangle is equal to $90^\circ$ plus half of the third angle."_

Mathematical Form:  
In $\triangle ABC$, if the interior bisectors of $\angle B$ and $\angle C$ intersect at the incenter ($I$), then:  
$$\angle BIC = 90^\circ + \frac{\angle A}{2}$$

---

## 2. Exterior Angle Bisector Theorem (Angle at Excenter)

- Name: Exterior Angle Bisector Theorem (Angle at Excenter)
- Statement:

> _"The angle formed by the intersection of the exterior angle bisectors of any two angles of a triangle is equal to $90^\circ$ minus half of the third interior angle."_

Mathematical Form:  
In $\triangle ABC$, if the exterior bisectors of $\angle B$ and $\angle C$ intersect at the excenter ($O$), then:  
$$\angle BOC = 90^\circ - \frac{\angle A}{2}$$

Would you like me to explain the names and statements for the remaining similarity theorems shown on the right side of your image (such as $BC^2 = CD \times CA$)? Let me know how you want to proceed!

# triangle ration constantenss
## 1. Condition for Similarity

Two triangles are similar if their corresponding angles are equal or their corresponding sides are in the same ratio ($k$).  
$$\Delta ABC \sim \Delta DEF \implies \frac{AB}{DE} = \frac{BC}{EF} = \frac{CA}{FD} = k$$

## 2. Linear Ratio Property

The ratio of any linear length is exactly equal to the side ratio ($k$).

- Perimeter ratio $= k$
- Altitude ratio $= k$
- Median ratio $= k$
- Angle Bisector ratio $= k$
- Inradius & Circumradius ratio $= k$

## 3. Area Ratio Property

The ratio of their areas is equal to the square of the side ratio ($k^2$).  
$$\frac{\text{Area}(\Delta ABC)}{\text{Area}(\Delta DEF)} = k^2$$

Want a 10-second mental trick to never confuse when to use $k$ vs $k^2$?
![[Pasted image 20260905071213.png]]