Source: [StackOverflow — FD and Normalization](https://stackoverflow.com/questions/4199444/functional-dependency-and-normalization)

**Terminology:** PA = Prime Attribute (part of some CK), NPA = Non-Prime Attribute, CK = Candidate Key, SK = Super Key.

### Types of non-trivial FDs (X → Y)

| Type | X | Y |
|---|---|---|
| 1 | Proper subset of a CK | NPA |
| 2 | Proper subset of CK + NPA | NPA |
| 3 | NPA | NPA |
| 4 | Proper subset of one CK | Proper subset of some other CK |
| 5 | Proper subset of one CK + NPA | Proper subset of some other CK |

Type 3 also notes: NPA → PA and Proper subset of CK → Proper subset of same CK are **not possible**.

| | Type 1 | Type 2 | Type 3 | Type 4 | Type 5 |
|---|---|---|---|---|---|
| 1NF | ✅ | ✅ | ✅ | ✅ | ✅ |
| 2NF | ❌ | ✅ | ✅ | ✅ | ✅ |
| 3NF | ❌ | ❌ | ❌ | ✅ | ✅ |
| BCNF | ❌ | ❌ | ❌ | ❌ | ❌ |

### Rules
"A NPA should depend on whole key (not its part) and nothing but the key."

That's Codd's statement paraphrased. Original:

> "Every non-key attribute must depend on the key, the whole key, and nothing but the key."

- "the key" → 1NF (atomic values, primary key exists)
- "the whole key" → 2NF (no partial dependency)
- "nothing but the key" → 3NF (no transitive dependency)


**2NF** — No partial dependency. NPA must depend on the **whole** CK, not a proper subset of it (Type 1 disallowed). NPA → NPA is still allowed.

**3NF** — No transitive dependency. NPA must depend **directly** on a SK/CK, not through another NPA (Types 1,2,3 disallowed). If the determined attribute is a PA, no need to check — it satisfies 3NF automatically.

**BCNF** — Every determiner must be a SK/CK, whether determined is NPA or PA. Strictest — eliminates all FD-based redundancy.

Normalization is done by **decomposing** relations.