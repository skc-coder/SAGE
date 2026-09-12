## 1. Why Paging?

Contiguous memory allocation causes **external fragmentation** — free memory exists but in scattered non-contiguous chunks too small to use. Paging solves this by allowing a process's physical memory to be non-contiguous.

**Internal fragmentation** can still occur in paging — the last page of a process may not be completely full.

---

## 2. Core Idea

- Physical memory is divided into fixed-size blocks called **frames**.
- Logical memory (process address space) is divided into same-size blocks called **pages**.
- Page size = Frame size (always, by definition).
- The OS maintains a **page table** per process that maps page numbers to frame numbers.

```

Logical Address Space Physical Memory ┌──────────┐ ┌──────────┐ │ Page 0 │ ──────────────► │ Frame 3 │ ├──────────┤ ├──────────┤ │ Page 1 │ ──────────────► │ Frame 7 │ ├──────────┤ ├──────────┤ │ Page 2 │ ──────────────► │ Frame 1 │ └──────────┘ └──────────┘ (process) (scattered in RAM)

```

---

## 3. Address Translation

A logical address has two parts:

```

┌─────────────────┬──────────────────┐ │ Page Number │ Page Offset │ │ (p) │ (d) │ └─────────────────┴──────────────────┘ upper bits lower bits

```

### Formulas

If page size = $2^n$ bytes:

$$\text{Offset bits} = n$$

$$\text{Page number bits} = \text{Total logical address bits} - n$$

$$\text{Number of pages} = \frac{\text{Logical address space size}}{\text{Page size}} = 2^{\text{page number bits}}$$

$$\text{Number of frames} = \frac{\text{Physical memory size}}{\text{Frame size}}$$

$$\text{Page table entries} = \text{Number of pages}$$

### Translation Steps

1. Extract page number $p$ = upper bits of logical address.
2. Look up page table at index $p$ → get frame number $f$.
3. Physical address = $f \times \text{page size} + d$ (offset $d$ stays the same).

```

Logical address: [ p | d ] │ Page Table [p] → f │ Physical address: [ f | d ]

```

### Example

- Logical address space: 32-bit → $2^{32}$ bytes = 4 GB
- Page size: $4$ KB = $2^{12}$ bytes → offset = **12 bits**
- Page number = $32 - 12$ = **20 bits** → $2^{20}$ = **1M pages**
- Each page table entry: 4 bytes → page table size = $2^{20} \times 4$ = **4 MB per process**

This 4 MB page table sitting in memory for every process is the problem that multilevel paging solves.

---

## 4. Page Table Size Problem

For a 32-bit system with 4 KB pages:

$$\text{Page table entries} = \frac{2^{32}}{2^{12}} = 2^{20} \approx 1 \text{ million entries}$$

$$\text{Page table size} = 2^{20} \times 4 \text{ bytes} = 4 \text{ MB}$$

For a 64-bit system with 4 KB pages:

$$\text{Page table entries} = \frac{2^{64}}{2^{12}} = 2^{52} \approx 4 \text{ quadrillion entries}$$

This is clearly impossible to store in a flat table. Solutions:
- **Multilevel paging** (hierarchical page tables)
- Inverted page tables
- Hashed page tables

---

## 5. TLB — Translation Lookaside Buffer

Every memory access requires a page table lookup (which is itself a memory access) — so every logical access would need 2 physical accesses. Too slow.

The **TLB** is a small, fast hardware cache inside the MMU that stores recent page→frame mappings.

### Effective Memory Access Time (EAT)

$$\text{EAT} = \alpha \times (t_{TLB} + t_{mem}) + (1-\alpha) \times (t_{TLB} + 2 \times t_{mem})$$

Where:
- $\alpha$ = TLB hit ratio
- $t_{TLB}$ = TLB access time
- $t_{mem}$ = main memory access time

Simplified (if $t_{TLB}$ is negligible or included in hit case):

$$\text{EAT} = \alpha \times t_{mem} + (1-\alpha) \times 2 \times t_{mem}$$

$$\text{EAT} = (2 - \alpha) \times t_{mem}$$

### Example

- $t_{mem}$ = 100 ns, $\alpha$ = 0.90 (90% hit ratio), $t_{TLB}$ = 0 (negligible)
- $\text{EAT} = 0.9 \times 100 + 0.1 \times 200 = 90 + 20 = \mathbf{110 \text{ ns}}$

> [!tip] GATE formula to remember
> $$\boxed{\text{EAT} = (2 - \alpha) \times t_{mem}}$$
> Only valid when $t_{TLB} \approx 0$ and no multilevel paging.

---

## 6. Multilevel Paging


Instead of one huge flat page table, break it into a **tree of smaller page tables**.

The logical address is split into multiple parts — one index per level, plus the offset.

### 6.1 Two-Level Paging (32-bit)

![](attachments/Pasted%20image%2020260430165800.png)

#### Translation

1. $p1$ → index into **outer page table** → get base address of a second-level page table.
2. $p2$ → index into **second-level page table** → get frame number $f$.
3. Physical address = $f$ concatenated with $d$.

#### Why it saves memory

With a flat page table, all $2^{20}$ entries must exist even if the process only uses a few pages.

With two-level paging, the outer page table has $2^{10}$ = 1024 entries. Each entry points to a second-level table. Second-level tables are only allocated for pages the process actually uses. Unused regions → null pointer in outer table → no second-level table allocated.

#### Page table size formula (2-level)

$$\text{Outer PT size} = 2^{p1} \times \text{entry size}$$

$$\text{Each inner PT size} = 2^{p2} \times \text{entry size}$$

$$\text{Total PT size} = \text{Outer PT} + (\text{number of valid outer entries}) \times \text{inner PT size}$$

In the worst case (process uses all pages): same as flat. In the best case (sparse process): much smaller.

### 6.3 Memory Accesses with Multilevel Paging

| Paging level | Memory accesses without TLB | With TLB hit | With TLB miss |
| ------------ | --------------------------- | ------------ | ------------- |
| Single-level | 2 (1 PT + 1 data)           | 1            | 2             |
| Two-level    | 3 (2 PT + 1 data)           | 1            | 3             |
| Three-level  | 4 (3 PT + 1 data)           | 1            | 4             |
| $k$-level    | $k+1$                       | 1            | $k+1$         |

$$\boxed{\text{Memory accesses (no TLB)} = k + 1}$$

where $k$ = number of paging levels.

### EAT with k-level paging

$$\text{EAT} = \alpha \times (t_{TLB} + t_{mem}) + (1-\alpha) \times (t_{TLB} + (k+1) \times t_{mem})$$

Simplified ($t_{TLB} \approx 0$):

$$\boxed{\text{EAT} = [\alpha + (1-\alpha)(k+1)] \times t_{mem}}$$

$$= [1 + (1-\alpha) \times k] \times t_{mem}$$

---

## 7. How the Bit Split is Decided

Given: logical address = $m$ bits, page size = $2^n$ bytes, $k$ levels.

- Offset = $n$ bits (fixed by page size).
- Remaining = $m - n$ bits split across $k$ levels.
- Split as evenly as possible, but must satisfy: each level's bits ≤ bits needed so that each page table fits within one page.

### Constraint: page table fits in one page

Each page table (at any level) should fit in exactly one page. This is the standard design constraint.

$$\text{entries per page table} = \frac{\text{page size}}{\text{entry size}}$$

$$\text{bits per level} = \log_2\left(\frac{\text{page size}}{\text{entry size}}\right)$$

### Example — 32-bit, 4 KB pages, 4-byte entries

$$\text{entries per page} = \frac{4096}{4} = 1024 = 2^{10}$$

So each level uses **10 bits**. 
Total non-offset bits = $32 - 12 = 20$. 
So, two levels of 10 bits each → **2-level paging**.

### Example — 64-bit, 4 KB pages, 8-byte entries

$$\text{entries per page} = \frac{4096}{8} = 512 = 2^{9}$$

Each level = 9 bits. Non-offset bits = $64 - 12 = 52$. Need $\lceil 52/9 \rceil = 6$ levels — impractical. Real 64-bit systems (x86-64) only use 48 bits of address space, giving $48 - 12 = 36$ bits → 4 levels of 9 bits each (PGD → PUD → PMD → PTE). Linux uses this exact scheme.

---

## 8. Page Table Entry (PTE) Structure

Each entry in a page table contains more than just the frame number:

![](attachments/Pasted%20image%2020260430170332.png)

| Bit | Name            | Meaning                                                             |
| --- | --------------- | ------------------------------------------------------------------- |
| V   | Valid/Present   | 1 = page is in memory; 0 = page not in memory (triggers page fault) |
| R   | Referenced      | Set by hardware when page is accessed (used by page replacement)    |
| M   | Modified/Dirty  | Set when page is written to (need to write back before replacing)   |
| P   | Protection      | Read/Write/Execute permissions                                      |
| U   | User/Supervisor | Whether user mode can access this page                              |
| X   | Execute disable | NX bit — prevents code execution in data pages                      |

---

## 9. Inverted Page Table

Instead of one page table per process (indexed by page number), have one **global** page table indexed by **frame number**.

Each entry contains: `(PID, page number)` — which process's which page is in this frame.

$$\text{Size of inverted PT} = \text{number of physical frames} \times \text{entry size}$$

**Advantage:** Fixed size regardless of number of processes or address space size.

**Disadvantage:** To translate a logical address, must search the table for `(PID, p)` — linear search is slow. Mitigated with a hash table.

---

## 10. Important Formulas

### Basic

$$\text{Page size} = 2^n \text{ bytes} \Rightarrow \text{offset} = n \text{ bits}$$

$$\text{Number of pages} = \frac{\text{Logical address space}}{{\text{Page size}}} = 2^{m-n}$$

$$\text{Number of frames} = \frac{\text{Physical memory size}}{\text{Frame size}}$$

$$\text{Page table size (flat)} = \text{Number of pages} \times \text{entry size}$$

$$\text{Internal fragmentation (avg)} = \frac{\text{Page size}}{2}$$

### TLB

$$\text{EAT (1-level)} = \alpha \cdot t_{mem} + (1-\alpha) \cdot 2t_{mem} = (2-\alpha) \cdot t_{mem}$$

$$\text{EAT (k-level)} = [1 + (1-\alpha) \cdot k] \cdot t_{mem}$$

### Multilevel


$$\text{Memory accesses per translation} = k + 1 \quad \text{(no TLB)}$$

$$\text{Bits per level} = \log_2\!\left(\frac{\text{page size}}{\text{PTE size}}\right)$$

$$\text{Minimum levels needed} = \left\lceil \frac{m - n}{\text{bits per level}} \right\rceil$$

### Physical Address

$$\text{Physical address} = f \times \text{page size} + d$$

$$= (f \ll n) \mid d$$

---

## 11. Worked Examples

### Example 1 — Basic translation

- 16-bit logical address space, page size = 256 bytes
- Page table: `[0→5, 1→2, 2→9, 3→1]`
- Logical address = `0x0123`

Offset bits = $\log_2(256) = 8$

Page number = upper 8 bits of `0x0123` = `0x01` = 1

Offset = lower 8 bits = `0x23` = 35

Frame = page table[1] = 2

Physical address = $2 \times 256 + 35 = 512 + 35 = \mathbf{547}$ = `0x0223`

### Example 2 — EAT

- Memory access time = 200 ns
- TLB access time = 20 ns
- TLB hit ratio = 80%
- Single-level paging

$$\text{EAT} = 0.8 \times (20 + 200) + 0.2 \times (20 + 200 + 200)$$

$$= 0.8 \times 220 + 0.2 \times 420$$

$$= 176 + 84 = \mathbf{260 \text{ ns}}$$

### Example 3 — Number of levels needed

- 32-bit logical address, page size = 4 KB, PTE = 4 bytes

Offset = 12 bits. Remaining = 20 bits.

Bits per level = $\log_2(4096/4) = \log_2(1024) = 10$

Levels = $\lceil 20/10 \rceil = \mathbf{2}$

### Example 4 — Total page table memory

- Process uses 3 pages, 2-level paging, 10-10-12 split, 4-byte PTE

Outer page table: $2^{10}$ entries × 4 bytes = **4 KB** (always allocated)

Inner page tables: 3 pages → they could all fall in 1 outer entry (same 10-bit $p1$) or up to 3 different outer entries.

Worst case (3 different $p1$ values): 3 inner page tables × 4 KB = **12 KB**

Total worst case = 4 KB + 12 KB = **16 KB** (vs 4 MB flat — huge saving)

---

