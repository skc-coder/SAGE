Heap sort is an **unstable**, comparison-based sorting algorithm. It uses a binary heap data structure to sort elements.

## Algorithm Logic

1. **Build a Max-Heap:** Transform the input array into a max-heap where the parent is always greater than or equal to its children.
    
2. **Extract Elements:** - Swap the root (maximum element) with the last element of the heap.
    
    - Reduce the heap size by 1.
        
    - "Heapify" the root to restore the max-heap property.
        
3. Repeat until the heap is empty.
    

### Complexity

- **Time Complexity:** $O(n \log n)$ for all cases.
    
- **Space Complexity:** $O(1)$ (In-place).
    

---

## Implementations

### C Implementation (Unstable)

```C
void heapify(int arr[], int n, int i) {
    int largest = i;
    int l = 2 * i + 1;
    int r = 2 * i + 2;

    if (l < n && arr[l] > arr[largest])
        largest = l;

    if (r < n && arr[r] > arr[largest])
        largest = r;

    if (largest != i) {
        int swap = arr[i];
        arr[i] = arr[largest];
        arr[largest] = swap;
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    for (int i = n - 1; i > 0; i--) {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heapify(arr, i, 0);
    }
}
```

### Python Implementation


```python
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Build maxheap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
```

---

## Why Heap Sort is Unstable
https://stackoverflow.com/questions/19336881/why-isnt-heapsort-stable

The instability of Heap Sort arises from two main operations:

### 1. Long-distance Swaps

During the extraction phase, the root (maximum) is swapped with the last element in the current heap. This swap can move an element across many others, including elements with the same value, potentially reversing their relative order.

### 2. The Heap Structure

The heap is a complete binary tree mapped onto an array. The parent-child relationship is determined by indices ($2i+1$ and $2i+2$). This structure ignores the original relative positions of equal elements.

**Example: `[21a, 21b, 21c]`**

1. When building the max-heap, `21a` is the root.
    
2. When sorting, `21a` is swapped with the last element (`21c`) and moved to the end of the array.
    
3. The final sorted array becomes `[..., 21a]`, even though `21a` was originally at the front.