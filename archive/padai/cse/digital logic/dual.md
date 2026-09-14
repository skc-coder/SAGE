## Finding the Dual

Replace all **ANDs (·)** with **ORs (+)** and vice versa.

Equivalently:
1. Find complement $f'$ (invert output)
2. Complement each literal individually

## Interpretation of Dual

### Physical Circuit Perspective

A circuit has fixed physical behavior. For input "001" it produces output 1.

The **dual** represents the same circuit under different **logic conventions**:
- **Positive logic:** 0 = Low (L), 1 = High (H)
- **Negative logic:** 0 = High (H), 1 = Low (L)

The circuit's physical behavior remains identical, but its logical interpretation changes.

### Why This Happens

**Example:** If $(000) \to 0$ in positive logic:

In negative logic (where L = 1, H = 0):
- Input $(000)$ becomes $(HHH)$ physically
- Output $0$ becomes $H$ physically
- So $(HHH) \to H$ in negative logic interpretation

**Result:** Both inputs and output get complemented, which is exactly how we compute the dual.
Or 
input gets the complemented output of the inputs complementary pair
### Key Insight

The dual captures the same physical circuit behavior under inverted logic conventions. Inputs and outputs flip together, preserving the functional relationship.

---

# [[palindrome functions]]