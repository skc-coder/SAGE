Paiging:
https://cirosantilli.com/x86-paging#how-the-k-ary-tree-is-used-in-x86

Done by a hardware called MMU. Working explained above.
https://en.wikipedia.org/wiki/Memory_management_unit#

Virtual Memory:

Segmentation:

Loader:
https://en.wikipedia.org/wiki/Loader_(computing)
Process structure:
https://en.wikipedia.org/w/index.php?title=Data_segment&oldid=441263263#Program_memory


https://stackoverflow.com/questions/14795164/why-do-linux-program-text-sections-start-at-0x0804800-and-stack-tops-start-at-0
![[Pasted image 20250822151114.png]]    ![[Pasted image 20250822151145.png]]
the dash above heap is modifed using brk.


bss: https://en.wikipedia.org/wiki/.bss
		used to store [[statically allocated variables]] variables.
		for saving data as only length of bss is stored in object files at compile time, as the value of these variables/constants is zero or uninitialised.
		In [C](https://en.wikipedia.org/wiki/C_\(programming_language\) "C (programming language)"), statically allocated objects without an explicit initializer are initialized to zero (for arithmetic types) or a null pointer (for pointer types) and that includes variables/constants defined outside of functions without any intiazlaition and static local variables.

stack:
https://unix.stackexchange.com/questions/145557/how-does-stack-allocation-work-in-linux/239323#239323


[[Memory]]