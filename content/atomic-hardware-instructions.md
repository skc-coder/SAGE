Modern computer architectures provide special hardware instructions that execute read-modify-write cycles **atomically** (i.e., as a single, uninterruptible unit of computation at the hardware bus/cache level).

> [!property] Common Atomic Hardware Primitives
> 1. **Test-and-Set (`TSL` / `test_and_set`):**
>    ```c
>    bool test_and_set(bool *target) {
>        bool rv = *target;
>        *target = true;
>        return rv;
>    }
>    ```
>    *Sets the memory location to `true` and returns its old value atomically.*
>
> 2. **Fetch-and-Add (`fetch_and_add`):**
>    ```c
>    int fetch_and_add(int *target, int val) {
>        int old = *target;
>        *target += val;
>        return old;
>    }
>    ```
>    *Increments the value at target memory location by `val` and returns the previous value atomically.*
>
> 3. **Compare-and-Swap (`CAS` / `compare_and_swap`):**
>    ```c
>    bool compare_and_swap(int *ptr, int expected, int new_val) {
>        if (*ptr == expected) {
>            *ptr = new_val;
>            return true;
>        }
>        return false;
>    }
>    ```
>    *Checks if `*ptr == expected`; if equal, updates `*ptr` to `new_val` and returns `true`. Otherwise, returns `false` without modifying memory.*
