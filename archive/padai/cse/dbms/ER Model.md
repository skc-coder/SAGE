Used to design database schema visually before converting to relations.

---

## Entities

**Strong Entity** — has its own primary key. Exists independently.
- Represented by a rectangle.

**Weak Entity** — no primary key of its own. Depends on a strong entity (owner) for identification.
- Represented by a double rectangle.
- Has a **partial key** (discriminator) — uniquely identifies weak entity among all entities related to same owner. Shown with dashed underline.
- Full key = owner's PK + partial key.

**Example:** `Loan(loan_no)` is strong. `Payment(payment_no, amount, date)` is weak — payment_no alone doesn't identify it uniquely across all loans, but (loan_no, payment_no) does.

---

## Attributes

| Type        | Notation                   | Meaning                                            |
| ----------- | -------------------------- | -------------------------------------------------- |
| Simple      | Oval                       | Single atomic value                                |
| Composite   | Oval with sub-ovals        | Made of sub-attributes (e.g. Name → First, Last)   |
| Multivalued | Double oval                | Can have multiple values (e.g. phone numbers)      |
| Derived     | Dashed oval                | Computed from other attributes (e.g. Age from DOB) |
| Key         | Oval with underline        | Primary key attribute                              |
| Partial key | Oval with dashed underline | Discriminator of weak entity                       |

---

## Relationships

Represented by a diamond. Weak entity's identifying relationship shown as double diamond.

### Cardinality Ratios

**One-to-One (1:1)** — one entity in A relates to at most one in B and vice versa.
Arrow on both sides.
```
A ←→ B
```
Example: Person — Aadhar Card

**One-to-Many (1:N)** — one entity in A relates to many in B, but each B relates to at most one A.
Arrow on the "one" side.
```
A ←—— B
```
Example: Department → Employees (one dept, many employees)

**Many-to-One (N:1)** — same as above, just perspective flipped.

**Many-to-Many (M:N)** — entities on both sides can relate to many on the other.
No arrows (or arrows on neither side).
```
A ——— B
```
Example: Students ↔ Courses

---
-> one, to remember the horizontal line as 1, and the arrow telling which one is one.
### Participation Constraints

**Total participation** — every entity must participate in the relationship. Shown by **double line**.
**Partial participation** — some entities may not participate. Shown by **single line**.

Example: Every employee must work in some department (total), but not every department has a manager yet (partial).

---

## Notation Summary

| Symbol           | Meaning                                    |
| ---------------- | ------------------------------------------ |
| Rectangle        | Strong entity                              |
| Double rectangle | Weak entity                                |
| Diamond          | Relationship                               |
| Double diamond   | Identifying relationship (for weak entity) |
| Oval             | Attribute                                  |
| Double oval      | Multivalued attribute                      |
| Dashed oval      | Derived attribute                          |
| Underline        | Primary key                                |
| Dashed underline | Partial key                                |
| Single line      | Partial participation                      |
| Double line      | Total participation                        |
| Arrow (→)        | "One" side of relationship                 |
| No arrow         | "Many" side                                |

---

## Cardinality in Chen vs Crow's Foot Notation

Chen notation uses arrows. Crow's foot (used in tools like MySQL Workbench) uses:
- `|` = one
- `>` or `<` = many
- `o` = zero (optional)

---

## Converting ER to Relations

**Strong entity** → relation with same attributes, PK = key attribute.

**Weak entity** → relation with partial key + owner's PK as foreign key. PK = (owner PK + partial key).

**1:1 relationship** → merge into one relation, or add FK on total participation side.

**1:N relationship** → add FK on the "many" side pointing to "one" side.

**M:N relationship** → create a new relation with PKs of both entities as composite PK.

**Multivalued attribute** → separate relation with entity PK + the attribute. PK = (entity PK + attribute).