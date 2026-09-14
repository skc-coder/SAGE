Selection sort is a comparison-based sorting algorithm. It divides the input list into two parts: a sorted sublist which is built up from left to right, and a sublist of the remaining unsorted items.

## Algorithm Logic

1. Find the minimum element in the unsorted array.
    
2. Swap it with the leftmost unsorted element.
    
3. Move the boundary between the sorted and unsorted segments one element to the right.
    

### Complexity

- **Time Complexity:** $O(n^2)$ in all cases (best, average, worst).
    
- **Space Complexity:** $O(1)$ (In-place).
    

---

## Implementations

### C Implementation (Standard Swapping)

This version is **unstable**.

```C
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        // Swap the found minimum element with the first element
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}
```

### Python Implementation (Stable via Insertion)

By shifting elements instead of swapping, we preserve the relative order of equal elements.

```python
def stable_selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Pull the minimum element out
        key = arr[min_idx]
        
        # Shift all elements between i and min_idx to the right
        while min_idx > i:
            arr[min_idx] = arr[min_idx - 1]
            min_idx -= 1
        
        # Place key at its sorted position
        arr[i] = key
    return arr
```

---

## Stability Analysis

### Why standard Selection Sort is Unstable
https://stackoverflow.com/questions/20761396/why-selection-sort-can-be-stable-or-unstable

Stability means that elements with equal keys appear in the same order in sorted output as they appear in the input. Standard selection sort uses **swapping**, which can move an element past an equal element.

**Example: `[1a, 3a, 4, 3b, 1b]`**

1. The algorithm finds the minimum element in the whole array, which is `1b`.
    
2. It swaps `1b` with the first element `1a`.
    
3. In this specific case, `1a` and `1b` might seem fine, but consider the swap's effect on other elements:
    

If the array is `[3a, 3b, 1]`:

1. Minimum is `1`.
    
2. Swap `3a` with `1`.
    
3. Array becomes `[1, 3b, 3a]`.
    
4. **Result:** The relative order of `3a` and `3b` is lost.
    

### Making it Stable

To make selection sort stable, the minimum element should not be swapped to the front. Instead, it should be **inserted** into its correct position by shifting all intervening elements.

- **Array Implementation:** Shifting takes $O(n)$ time, making the total complexity $O(n^2)$.
    
- **Linked List Implementation:** If using a Linked List, you can delete the minimum node and insert it at the beginning in $O(1)$ (after finding it in $O(n)$), maintaining stability without additional time overhead.
    

$$\text{Stability} \implies \text{Relative order of } K_i = K_j \text{ is preserved.}$$