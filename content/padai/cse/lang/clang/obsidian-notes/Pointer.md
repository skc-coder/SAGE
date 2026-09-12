https://vimeo.com/1187212140?share=copy&fl=sv&fe=ci
## Pointer

```c
int *p = anything;
// means:
p   = anything     // address
*p  = *anything    // what does p point to?
```

---

## Core Rule

$$p + k = p + k \times \text{sizeof}(*p)$$

`*p` = what `p` points to.

The increment is decided by the size of pointed object.

Here `p` can also be an array i.e.
`arr + k = arr + sizeof(*arr = arr[0])`

---

## Arrays as Pointers

An array name is a **pointer-like** thing — it points to its **first element**.

| Declaration        | arr is like     |
| ------------------ | --------------- |
| `int arr[N]`       | `int (*)`       |
| `int arr[N][Q]`    | `int (*)[Q]`    |
| `int arr[N][Q][R]` | `int (*)[Q][R]` |

for `int arr[N][Q]`
arr + 2 = &\*(arr+2) = &arr[2] = points to array of size [Q], but it is the 3rd such array. Pointer type.

arr[2]= points at the same thing as above, but sizeof is different. Array type. Pointer like.

for `int arr[N][Q][R]`
arr + 2 = pointer pointing to  `&arr[2][0]`. 
arr[2] = array of size [Q]*[R] = points to the 1d array = `&arr[2][0]`. 

---

## 3D Array Example

```c
int arr[P][Q][R];
```


- `arr` type = `int (*)[Q][R]`
- `sizeof(arr)` = `P*Q*R * sizeof(int)`
- `arr + k` → jumps by `k * Q*R * sizeof(int)`
	- everything except the `*` in `int (*)[Q][R].`
	- or by `sizeof(*arr) = sizeof(arr[0]`
- `arr` = `&*arr = arr[0]` (first 2D table of size `[Q][R]`)

Similiary
- `arr[x]` type = `int (*)[R]`
- `sizeof(arr[x])` = `Q*R * sizeof(int)`
- `arr[x] + k` → jumps by `k * R * sizeof(int)`
	- everything except the `*` in `int (*)[R].`
	- or by `sizeof(*arr[x]) = sizeof(arr[x][0]`
- `arr[x]` = `&*arr[x] = arr[x][0]` (first 1D table of size `[R]`)

---

## Indexing Rules for `int arr[P][Q][R]`

| Expression      | What it is           | Points to                             |
| --------------- | -------------------- | ------------------------------------- |
| `arr`           | array (pointer-like) | `arr[0]` — first 2D table             |
| `arr + k`       | pointer              | `arr[k]` — k-th 2D table              |
| `arr[k]`        | 2D array             | `arr[k][0]` — first row of k-th table |
| `arr[k] + t`    | pointer              | `arr[k][t]` — t-th row                |
| `arr[k][t]`     | 1D array             | `arr[k][t][0]` — first element        |
| `arr[k][t] + u` | pointer              | `arr[k][t][u]`                        |

> `arr[k]` is an **array** (no sizeof-of-pointer), `*(arr+k)` is also `arr[k]`. Same address, same type.

---

## Type Mismatch

```c
int arr[2][3][4];

int ***p       = arr;  // ❌ WRONG — type mismatch
int (*p)[3][4] = arr;  // ✓ correct
```

---

## `&arr` vs `arr`

```c
int arr[2][3];

int (*pt)[2][3] = &arr;  // pointer to WHOLE array, step = sizeof(*pt = *&arr = arr) = 2*3*sizeof(int)

int (*p)[3]     = arr;   // pointer to first ROW,   step = 3*sizeof(int)
```

- Both `p` and `arr` point to the **same address** (first row).
- Different types → different step sizes.
- `sizeof(p)` = 8 (pointer), `sizeof(arr)` = `2*3*sizeof(int)` (array).


---

now explore [gallery pointers](gallery%20pointers.md)
[Array of Pointers gallery](Array%20of%20Pointers%20gallery.md)